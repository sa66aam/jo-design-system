"""A painted still from two flat passes: ink line and soft watercolour wash on warm paper, in-house, 0 credits.

Input: a flat-colour pass (fills only, no strokes) and an ink pass (black strokes on white), the same size,
drawn by code (SVG, a composition's snapshot) or by hand. Output: the painting as PNG, and with --stages the
four steps beside it (flat, paper, wash, ink) for looking. With --layer the paper is left white, so the result
multiplies cleanly over a painting of the same size: a separately painted layer that moves (a lamp's glow,
steam, an orbit) over a still base (ARCHITECTURE.md 6, "Painted stills that move").

The steps, in order (each one answers a defect of the first version, build-reference/04-defects.md D-73):
  paper      warm cold-press paper: tooth, cloud and horizontal fibres (the default tone is #F7F2E8)
  misregister  the wash is displaced twice (large and small), so it never sits exactly inside the ink
  wash       edge-preserving smooth, then transparent pigment (density = 1 - colour, times strength)
  wet-in-wet large soft blotches of more and less pigment, and a slow drift of blue against red
  lights    soft holes of bare paper where light falls
  pooling   pigment dries darker on the rim of every colour region
  granulate pigment settles in the tooth, mostly in the dark washes (kept quiet: loud grain reads as sandpaper)
  backruns  a few cauliflower blooms with a darker ring
  vignette  the paint dissolves into the paper toward the edges (the book look); the ink fades later than the wash
  ink       the line displaced, swelling and thinning with the nib, broken where the pen lifts, a faint pencil pass
            under it, sepia-black (#463428), multiplied over everything

Every random choice is seeded (--seed, default 7): the same inputs and seed give the same pixels, so a still can
be re-made exactly, as the studio's fixed core asks of every frame.

Run with the studio's Python (numpy, opencv-python-headless from tools/requirements.txt):
  python3 tools/watercolor.py <flat.png> <ink.png> <out-dir> <name> [--layer] [--stages] [--seed N]
  python3 tools/watercolor.py --bleed <out.png> [--size 1024]
The second form writes the wet-wash bloom mask (white on transparent) that a page grows from 1% to 270% so a
painting arrives like a wash spreading on paper. A worked example, frozen with its hashes:
build-reference/examples/watercolor-v1/.
"""
import argparse
import os

import cv2
import numpy as np


def _noise(h, w, scale, octaves, seed):
    """Value noise in 0..1: random grids upsampled and summed, octave by octave."""
    rng = np.random.default_rng(seed)
    out = np.zeros((h, w), np.float32)
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        s = max(2, int(scale / (2 ** o)))
        small = rng.random((h // s + 2, w // s + 2)).astype(np.float32)
        out += cv2.resize(small, (w, h), interpolation=cv2.INTER_CUBIC) * amp
        tot += amp
        amp *= 0.5
    out /= tot
    out -= out.min()
    return out / (out.max() + 1e-6)


def paper(h, w, seed, tone=(232, 242, 247)):
    """Warm paper (BGR of #F7F2E8) and its tooth, the fine grain the pigment settles in."""
    base = np.ones((h, w, 3), np.float32) * np.array(tone, np.float32) / 255.0
    tooth = _noise(h, w, 6, 2, seed) - 0.5
    cloud = _noise(h, w, 220, 4, seed + 1) - 0.5
    fib = np.random.default_rng(seed + 2).random((h, w)).astype(np.float32)
    fib = cv2.GaussianBlur(fib, (0, 0), sigmaX=6, sigmaY=0.6) - 0.5
    shade = 1 + tooth * 0.045 + cloud * 0.05 + fib * 0.06
    return np.clip(base * shade[..., None], 0, 1), tooth


def wobble(img, amp, scale, seed):
    """Displace an image by smooth noise, so nothing stays ruler-straight."""
    h, w = img.shape[:2]
    dx = (_noise(h, w, scale, 3, seed) - 0.5) * 2 * amp
    dy = (_noise(h, w, scale, 3, seed + 9) - 0.5) * 2 * amp
    xs, ys = np.meshgrid(np.arange(w, dtype=np.float32), np.arange(h, dtype=np.float32))
    return cv2.remap(img, xs + dx, ys + dy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def vignette(h, w, seed, reach=1.02, gain=5.5):
    """1 in the middle, 0 at the edges, with a ragged border like a wash that stopped."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.maximum(np.abs(xx - w / 2) / (w / 2), np.abs(yy - h / 2) / (h / 2))
    v = np.clip((reach - d + (_noise(h, w, 70, 4, seed) - 0.5) * 0.35) * gain, 0, 1)
    return cv2.GaussianBlur(v, (0, 0), 2.0)


def wash(flat_bgr, tooth, seed, strength=0.72, pool=0.9, gran=0.10):
    """Pigment density (0..1 per channel) from the flat pass."""
    h, w = flat_bgr.shape[:2]
    c = wobble(wobble(flat_bgr, 7.0, 140, seed), 2.0, 30, seed + 1)
    regions = c.copy()
    c = cv2.edgePreservingFilter(c, flags=cv2.RECURS_FILTER, sigma_s=30, sigma_r=0.25)
    c = cv2.GaussianBlur(c, (0, 0), 1.6).astype(np.float32) / 255.0
    dens = (1.0 - c) * strength
    # wet-in-wet, and the hue drift
    dens *= (0.55 + 0.75 * _noise(h, w, 260, 4, seed + 2) * (0.75 + 0.5 * _noise(h, w, 90, 3, seed + 3)))[..., None]
    drift = (_noise(h, w, 300, 3, seed + 12) - 0.5) * 0.16
    dens[..., 0] *= 1 + drift
    dens[..., 2] *= 1 - drift
    # the lights
    holes = cv2.GaussianBlur(np.clip((_noise(h, w, 120, 3, seed + 13) - 0.72) * 5, 0, 1), (0, 0), 6)
    dens *= (1 - 0.65 * holes)[..., None]
    # pooling on every region's rim
    q = (regions // 24).astype(np.int32)
    key = (q[..., 0] * 10000 + q[..., 1] * 100 + q[..., 2]).astype(np.float32)
    edge = ((np.abs(cv2.Sobel(key, cv2.CV_32F, 1, 0, ksize=1)) + np.abs(cv2.Sobel(key, cv2.CV_32F, 0, 1, ksize=1))) > 0)
    rim = cv2.GaussianBlur(edge.astype(np.float32), (0, 0), 1.8)
    if rim.max() > 0:
        rim = np.clip(rim / (np.percentile(rim[rim > 0], 90) + 1e-6), 0, 1)
    rim = wobble(rim, 1.5, 25, seed + 4)
    dens *= (1 + pool * rim * (dens.mean(axis=2) > 0.03))[..., None]
    # granulation, quiet
    tb = cv2.GaussianBlur(tooth, (0, 0), 0.8)
    dens *= np.clip(1 - gran * tb * 12.0 * dens.mean(axis=2), 0.75, 1.3)[..., None]
    # backruns
    rng = np.random.default_rng(seed + 30)
    bl = np.zeros((h, w), np.float32)
    for _ in range(max(2, int(h * w / 220000))):
        cv2.circle(bl, (int(rng.integers(0, w)), int(rng.integers(0, h))), int(rng.integers(30, 80)), 1.0, -1)
    bl = cv2.GaussianBlur(wobble(bl, 14, 26, seed + 8), (0, 0), 2.5)
    ring = np.clip(cv2.Laplacian(bl, cv2.CV_32F, ksize=5) * -0.08, 0, 1)
    dens *= (1 - 0.35 * bl + 0.45 * ring)[..., None]
    # the book look
    dens *= vignette(h, w, seed + 20)[..., None]
    return np.clip(dens, 0, 1)


def ink(line_gray, seed, tone=(40, 52, 70)):
    """A multiplicative layer (BGR, 0..1) from the ink pass: 0 is ink, 255 is paper."""
    h, w = line_gray.shape[:2]
    a0 = 1.0 - line_gray.astype(np.float32) / 255.0
    a = wobble(a0, 2.2, 45, seed)
    press = _noise(h, w, 60, 2, seed + 1)
    a = a * (1 - press) + cv2.dilate(a, np.ones((3, 3), np.uint8)) * press
    lifts = (_noise(h, w, 7, 1, seed + 2) > 0.10).astype(np.float32)
    a = a * (0.25 + 0.75 * cv2.GaussianBlur(lifts, (0, 0), 0.7))
    pencil = wobble(a0, 4.0, 60, seed + 7) * 0.16
    a = np.clip(np.maximum(a * (0.70 + 0.25 * _noise(h, w, 30, 2, seed + 3)), pencil), 0, 1)
    a = cv2.GaussianBlur(a, (0, 0), 0.6) * vignette(h, w, seed + 25, reach=1.08, gain=4.0)
    t = np.array(tone, np.float32) / 255.0
    return 1 - a[..., None] * (1 - t)


def paint(flat_path, ink_path, out_dir, name, layer=False, stages=False, seed=7):
    flat = cv2.imread(flat_path, cv2.IMREAD_COLOR)
    line = cv2.imread(ink_path, cv2.IMREAD_GRAYSCALE)
    if flat is None or line is None:
        raise SystemExit(f"cannot read {flat_path if flat is None else ink_path}")
    if flat.shape[:2] != line.shape[:2]:
        raise SystemExit(f"the two passes differ in size: {flat.shape[1]}x{flat.shape[0]} and {line.shape[1]}x{line.shape[0]}")
    h, w = flat.shape[:2]
    pap, tooth = paper(h, w, seed)
    pigment = 1 - wash(flat, tooth, seed)
    lines = ink(line, seed)
    os.makedirs(out_dir, exist_ok=True)

    def save(fname, arr):
        cv2.imwrite(os.path.join(out_dir, fname), (np.clip(arr, 0, 1) * 255).astype(np.uint8))

    save(f"{name}.png", pigment * lines if layer else pap * pigment * lines)
    if stages and not layer:
        save(f"{name}.stage-1-flat.png", flat.astype(np.float32) / 255)
        save(f"{name}.stage-2-paper.png", pap)
        save(f"{name}.stage-3-wash.png", pap * pigment)
        save(f"{name}.stage-4-ink.png", pap * lines)
    print(f"{name}: {w}x{h}, seed {seed}, {'layer on white' if layer else 'on paper'} -> {out_dir}")


def bleed(path, size=1024, seed=21):
    n = _noise(size, size, 70, 5, seed)
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    d = np.sqrt((xx - size / 2) ** 2 + (yy - size / 2) ** 2) / (size / 2)
    a = cv2.GaussianBlur(np.clip(((1 - d) + (n - 0.5) * 0.9 - 0.15) * 4, 0, 1), (0, 0), 2)
    rgba = np.zeros((size, size, 4), np.uint8)
    rgba[..., :3] = 255
    rgba[..., 3] = (a * 255).astype(np.uint8)
    cv2.imwrite(path, rgba)
    print(f"bleed mask: {size}x{size}, seed {seed} -> {path}")


def main():
    p = argparse.ArgumentParser(description="A painted still from a flat pass and an ink pass.")
    p.add_argument("flat", nargs="?")
    p.add_argument("ink", nargs="?")
    p.add_argument("out_dir", nargs="?")
    p.add_argument("name", nargs="?")
    p.add_argument("--layer", action="store_true", help="paper left white: a moving layer to multiply over a base")
    p.add_argument("--stages", action="store_true", help="also write the four steps")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--bleed", metavar="OUT.png", help="write the wet-wash bloom mask instead")
    p.add_argument("--size", type=int, default=1024)
    a = p.parse_args()
    if a.bleed:
        bleed(a.bleed, a.size)
    elif all([a.flat, a.ink, a.out_dir, a.name]):
        paint(a.flat, a.ink, a.out_dir, a.name, a.layer, a.stages, a.seed)
    else:
        p.error("give <flat.png> <ink.png> <out-dir> <name>, or --bleed <out.png>")


if __name__ == "__main__":
    main()
