"""The flat passes of the watercolour engine's worked example (build-reference/examples/watercolor-v1), drawn by
code: each shape is authored once and rendered twice, a fill-only colour pass and a stroke-only ink pass. Three
scenes (a study desk, an atom, a school lab bench) and their moving layers (the lamp's light, tea steam, four
electron shells, a burner flame, bubbles), drawn for the illustrated-companion trial of 2026-10-07.

Needs cairosvg (pip install cairosvg), which is not in tools/requirements.txt: the example only. Any tool that
writes two PNGs of one size (a fill pass and an ink pass) can feed tools/watercolor.py.
  python3 scenes.py <out-dir>
"""
import math, os, random, sys
import cairosvg

random.seed(4)
OUT = sys.argv[1] if len(sys.argv) > 1 else "in"
os.makedirs(OUT, exist_ok=True)

class Scene:
    def __init__(self, w, h):
        self.w, self.h, self.items = w, h, []
    def add(self, tag, fill=None, line=True, sw=3.2, **a):
        attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in a.items())
        self.items.append((tag, attrs, fill, line, sw))
        return self
    def svg(self, mode):
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">',
               f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>']
        for tag, attrs, fill, line, sw in self.items:
            if mode == "color" and fill:
                out.append(f'<{tag} {attrs} fill="{fill}" stroke="none"/>')
            if mode == "line" and line:
                out.append(f'<{tag} {attrs} fill="none" stroke="#000" stroke-width="{sw*0.72:.2f}" stroke-linecap="round" stroke-linejoin="round"/>')
        out.append("</svg>")
        return "\n".join(out)
    def render(self, name):
        for mode in ("color", "line"):
            cairosvg.svg2png(bytestring=self.svg(mode).encode(), write_to=os.path.join(OUT, f"{name}.{mode}.png"))

def wiggle_path(pts, j=1.2):
    p = [(x + random.uniform(-j, j), y + random.uniform(-j, j)) for x, y in pts]
    d = f"M{p[0][0]:.1f},{p[0][1]:.1f} " + " ".join(f"L{x:.1f},{y:.1f}" for x, y in p[1:])
    return d

def frond(cx, cy, ang, length, curl=0.35):
    a = math.radians(ang)
    ex, ey = cx + math.cos(a) * length, cy + math.sin(a) * length
    mx, my = cx + math.cos(a) * length * .5, cy + math.sin(a) * length * .5 - length * curl
    nx, ny = -math.sin(a) * length * .09, math.cos(a) * length * .09
    return (f"M{cx},{cy} Q{mx + nx:.1f},{my + ny:.1f} {ex:.1f},{ey:.1f} "
            f"Q{mx - nx:.1f},{my - ny:.1f} {cx},{cy} Z")

def palm(s, x, base, h, col="#5E7A55", trunk="#8A6A4A"):
    s.add("path", trunk, d=f"M{x-9},{base} C{x-14},{base-h*.5} {x+6},{base-h*.8} {x+2},{base-h} L{x+12},{base-h} C{x+16},{base-h*.8} {x+2},{base-h*.5} {x+9},{base} Z", sw=2.4)
    for k in range(4, int(h / 14)):
        yy = base - k * 14
        s.add("path", None, d=f"M{x-8},{yy} Q{x+2},{yy+5} {x+12},{yy}", sw=1.4)
    for ang in (-170, -140, -110, -70, -40, -10, 200):
        s.add("path", col, d=frond(x + 7, base - h, ang, h * .42), sw=2.2)

# ---------------------------------------------------------------- scene A: the desk
def desk():
    s = Scene(1600, 1000)
    # window
    s.add("rect", "#F3CDA6", x=880, y=90, width=560, height=420, sw=4)
    s.add("rect", "#E9B48A", x=880, y=330, width=560, height=180, line=False)
    s.add("circle", "#F6E1B8", cx=1300, cy=300, r=46, sw=2)
    for x, h in ((980, 230), (1110, 300), (1380, 210)):
        palm(s, x, 510, h)
    s.add("path", "#8C9C86", d="M880,470 Q1000,440 1120,465 T1440,455 L1440,510 L880,510 Z", line=False)
    s.add("path", None, d="M1160,90 L1160,510 M880,300 L1440,300", sw=5)
    s.add("rect", "#C9B79C", x=860, y=505, width=600, height=26, sw=3)
    # lamp
    s.add("ellipse", "#3F5E4F", cx=330, cy=640, rx=105, ry=24, sw=3)
    s.add("path", None, d="M330,630 L250,420 L400,250", sw=9)
    s.add("path", "#3F5E4F", d="M360,220 L520,300 L470,360 Q400,330 330,280 Z", sw=3)
    s.add("circle", "#3F5E4F", cx=250, cy=420, r=14, sw=2.4)
    # desk
    s.add("path", "#B98A5E", d="M40,640 L1560,620 L1580,700 L20,722 Z", sw=3.6)
    s.add("path", "#946842", d="M20,722 L1580,700 L1580,1000 L20,1000 Z", sw=3.6)
    s.add("path", None, d="M120,800 L1480,786 M120,880 L1480,866", sw=2)
    # open book
    s.add("path", "#F1E7D2", d="M520,660 Q650,610 790,650 L790,690 Q650,656 520,700 Z", sw=3)
    s.add("path", "#F4ECDB", d="M790,650 Q930,610 1060,656 L1060,698 Q930,656 790,690 Z", sw=3)
    for k in range(5):
        s.add("path", None, d=f"M{560+k*2},{662+k*5} Q{650},{634+k*5} {760},{660+k*5}", sw=1.3)
        s.add("path", None, d=f"M{820},{660+k*5} Q{930},{632+k*5} {1030},{664+k*5}", sw=1.3)
    s.add("path", "#C35A3C", d="M780,650 L790,720 L800,650 Z", sw=2)        # ribbon bookmark
    # flask
    s.add("path", "#DCE8EC", d="M1185,470 L1185,530 L1110,650 Q1105,664 1120,666 L1290,666 Q1305,664 1300,650 L1225,530 L1225,470 Z", sw=3)
    s.add("path", "#5FA3A8", d="M1141,600 L1269,600 L1300,650 Q1305,664 1290,666 L1120,666 Q1105,664 1110,650 Z", sw=2)
    s.add("rect", "#C9B79C", x=1178, y=455, width=54, height=18, sw=2.4)
    # tea glass + saucer
    s.add("ellipse", "#E6D3B3", cx=1440, cy=660, rx=74, ry=13, sw=2.6)
    s.add("path", "#B5652A", d="M1410,560 Q1400,600 1418,628 Q1404,646 1420,656 L1460,656 Q1476,646 1462,628 Q1480,600 1470,560 Z", sw=2.6)
    # notebook + pencil
    s.add("path", "#7D93A6", d="M150,690 L420,682 L432,720 L156,730 Z", sw=3)
    s.add("path", "#E4B64A", d="M440,700 L640,708 L640,718 L440,712 Z", sw=2)
    s.add("path", "#2A231E", d="M640,708 L660,713 L640,718 Z", sw=1.6)
    s.render("desk")
    # moving layers
    L = Scene(1600, 1000)       # lamp light pool
    L.add("path", "#F6DD8A", d="M470,350 L700,690 L170,700 L340,300 Z", line=False)
    L.render("desk-glow")
    T = Scene(1600, 1000)       # tea steam
    for k, off in enumerate((-14, 4, 20)):
        T.add("path", None, d=f"M{1440+off},545 C{1420+off},505 {1465+off},480 {1440+off},440 S{1425+off},380 {1450+off},350", sw=2.6)
    T.render("desk-steam")

# ---------------------------------------------------------------- scene B: the atom
def atom(Z=11):
    s = Scene(1200, 1200); c = 600
    radii = (150, 270, 390, 510)
    for r in radii:
        s.add("circle", None, cx=c, cy=c, r=r, sw=2.2)
    s.add("circle", "#F2E2C4", cx=c, cy=c, r=96, line=False)
    pos = []
    for k in range(23):
        a = k * 2.399; d = 17.5 * math.sqrt(k)
        pos.append((c + math.cos(a) * d, c + math.sin(a) * d))
    for i, (x, y) in enumerate(pos):
        col = "#C8553D" if i % 2 == 1 else "#8796A3"
        s.add("circle", col, cx=f"{x:.1f}", cy=f"{y:.1f}", r=21, sw=2.4)
        if i % 2 == 1:
            s.add("path", None, d=f"M{x-7:.1f},{y:.1f} L{x+7:.1f},{y:.1f} M{x:.1f},{y-7:.1f} L{x:.1f},{y+7:.1f}", sw=2)
    s.render("atom")
    shells = [2, 8, 8, 2]
    left = Z
    for i, r in enumerate(radii):
        n = min(left, shells[i]); left -= n
        E = Scene(1200, 1200)
        for k in range(n):
            a = 2 * math.pi * k / max(n, 1) + i * .6
            x, y = c + math.cos(a) * r, c + math.sin(a) * r
            E.add("circle", "#2F6FA8", cx=f"{x:.1f}", cy=f"{y:.1f}", r=17, sw=2.4)
            E.add("path", None, d=f"M{x-6:.1f},{y:.1f} L{x+6:.1f},{y:.1f}", sw=2)
        E.render(f"atom-e{i+1}")

# ---------------------------------------------------------------- scene C: the lab bench (wide)
def lab():
    s = Scene(2400, 900)
    # periodic poster
    s.add("rect", "#EFE4CF", x=160, y=60, width=720, height=330, sw=3.4)
    cols = ["#D98C6A", "#E8C36A", "#9CC1A0", "#8EB4CF", "#C9A6C9"]
    for r in range(6):
        for q in range(14):
            if (r == 0 and 0 < q < 13) or (r in (1, 2) and 1 < q < 8):
                continue
            s.add("rect", cols[(q // 3) % 5], x=190 + q * 47, y=86 + r * 48, width=40, height=40, sw=1.6)
    # shelf with bottles
    s.add("rect", "#9C7550", x=1100, y=300, width=760, height=22, sw=3)
    for i, x in enumerate(range(1140, 1840, 110)):
        col = ["#B04A3A", "#3E7C8C", "#C79A2F", "#5C7A4E", "#7A5A8C", "#3E7C8C", "#B04A3A"][i % 7]
        hgt = 120 + (i * 37) % 70
        s.add("path", col, d=f"M{x},{300} L{x},{300-hgt} Q{x},{300-hgt-18} {x+20},{300-hgt-22} L{x+20},{300-hgt-50} L{x+40},{300-hgt-50} L{x+40},{300-hgt-22} Q{x+60},{300-hgt-18} {x+60},{300-hgt} L{x+60},300 Z", sw=2.6)
        s.add("rect", "#F3EAD8", x=x + 10, y=300 - hgt + 30, width=40, height=34, sw=1.6)
    # window with palms
    s.add("rect", "#F1CFA8", x=1960, y=80, width=360, height=420, sw=4)
    palm(s, 2080, 500, 260); palm(s, 2240, 500, 190)
    s.add("path", None, d="M2140,80 L2140,500", sw=5)
    # bench
    s.add("path", "#6F7F78", d="M0,560 L2400,560 L2400,610 L0,610 Z", sw=3.6)
    s.add("path", "#9AA79F", d="M0,610 L2400,610 L2400,900 L0,900 Z", sw=3.6)
    for x in range(200, 2400, 520):
        s.add("rect", None, x=x, y=650, width=420, height=220, sw=2.4)
        s.add("path", None, d=f"M{x+190},{760} L{x+230},{760}", sw=6)
    # beakers
    for x, liq, h in ((240, "#5FA3A8", 120), (420, "#C8553D", 90), (1500, "#E4B64A", 140)):
        s.add("path", "#DCE8EC", d=f"M{x},{560-h-60} L{x},{560} L{x+130},{560} L{x+130},{560-h-60} L{x+145},{560-h-72} L{x-10},{560-h-72} Z", sw=3)
        s.add("rect", liq, x=x + 4, y=560 - h, width=122, height=h - 3, line=False)
        for k in range(3):
            s.add("path", None, d=f"M{x+90},{560-h+20+k*30} L{x+126},{560-h+20+k*30}", sw=1.6)
    # burner + stand + flask
    s.add("path", "#4E5A55", d="M880,560 L1000,560 L985,535 L895,535 Z", sw=3)
    s.add("rect", "#7C8780", x=926, y=420, width=28, height=118, sw=3)
    s.add("path", None, d="M820,560 L840,300 M1060,560 L1040,300 M830,320 L1050,320", sw=5)
    s.add("path", "#DCE8EC", d="M915,170 L915,230 L850,310 Q960,340 1030,310 L965,230 L965,170 Z", sw=3)
    s.add("path", "#7A5A8C", d="M868,288 L1012,288 L1030,310 Q960,340 850,310 Z", line=False)
    s.render("lab")
    F = Scene(2400, 900)
    F.add("path", "#F2A43A", d="M940,420 C915,390 925,350 940,320 C955,350 965,390 940,420 Z", sw=2)
    F.add("path", "#4F8DD6", d="M940,420 C930,405 932,385 940,370 C948,385 950,405 940,420 Z", line=False)
    F.render("lab-flame")
    B = Scene(2400, 900)
    for k in range(7):
        B.add("circle", None, cx=900 + (k * 37) % 120, cy=200 - k * 18, r=6 + k % 3 * 3, sw=2)
    B.render("lab-bubbles")

if __name__ == "__main__":
    desk(); atom(); lab()
    print(sorted(os.listdir(OUT)))
