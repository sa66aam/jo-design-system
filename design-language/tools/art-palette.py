#!/usr/bin/env python3
# (217) لون الصفحة من رسمها: يحذف بياض الورق من رسم القسم، ويكمّم ما بقي من حبر وماء، ويطبع أربع درجات لمكتبها
# المائيّ (--pg-base --pg1 --pg2 --pg3، الوصفة 11 في دليل التصميم §15-ج). المكتب يُشتقّ من الرسم ولا يُخترع، فلكلّ
# رسم باليته وتبقى العائلة واحدة. يقرأ فقط ولا يكتب ملفّا. البيت: «Lessons and Guides/design-language/prompts/blend-pipeline.md».
# python3 tools/art-palette.py <رسم.webp> [رسم آخر ...]
import sys, colorsys
import numpy as np
from PIL import Image

PAPER = 236          # ما فوقه في كلّ القنوات ورق (عتبة الحبر نفسها في grid-art.py)
K = 6                # عناقيد التكميم قبل اختيار الأربع

def hexof(c): return '#%02x%02x%02x' % tuple(int(round(v)) for v in c)
def mix(a, b, t): return a * (1 - t) + b * t
def lum(c):
    f = lambda v: (v / 255) / 12.92 if v / 255 <= .04045 else ((v / 255 + .055) / 1.055) ** 2.4
    r, g, b = (f(v) for v in c); return .2126 * r + .7152 * g + .0722 * b

def palette(path):
    im = Image.open(path).convert('RGB')
    im.thumbnail((200, 200))
    px = np.asarray(im, dtype=float).reshape(-1, 3)
    ink = px[px.min(axis=1) < PAPER]
    if len(ink) < 50: sys.exit('%s: لا حبر يكفي للقياس' % path)
    # الحبر الأسود لا يلوّن مكتبا: يُترك ما قلّ إشباعه وعمق ظلامه معا
    hsv = np.array([colorsys.rgb_to_hsv(*(p / 255)) for p in ink])
    wash = ink[(hsv[:, 2] > .35) & (hsv[:, 1] > .12)]
    if len(wash) < 30: wash = ink[hsv[:, 2] > .35]
    rng = np.random.default_rng(7)
    cent = wash[rng.choice(len(wash), K, replace=False)]
    for _ in range(25):
        lab = ((wash[:, None, :] - cent[None]) ** 2).sum(-1).argmin(1)
        cent = np.array([wash[lab == k].mean(0) if (lab == k).any() else cent[k] for k in range(K)])
    size = np.bincount(lab, minlength=K)
    # كلّ عنقود بلونه الأصفى: وسيط الربع الأشدّ إشباعا فيه (متوسّط العنقود يخلط الماء بحافّة الحبر فيرمّد)
    hs = np.array([colorsys.rgb_to_hsv(*(p / 255)) for p in wash])
    def pure(k):
        m = lab == k; h = hs[m]; q = h[h[:, 1] >= np.quantile(h[:, 1], .75)]
        return np.median(q, axis=0)
    rank = sorted((k for k in range(K) if size[k]), key=lambda k: -size[k] * pure(k)[1])
    h1, s1, _ = pure(rank[0])
    near = lambda k: min(abs(pure(k)[0] - h1), 1 - abs(pure(k)[0] - h1)) < .06
    h2, s2, _ = pure(next((k for k in rank[1:] if not near(k)), rank[0]))
    rgb = lambda h, sat, v: np.array(colorsys.hsv_to_rgb(h, sat, v)) * 255
    paper = np.array([255, 253, 248.])
    # الدرجات بقاعدة لا باليد: الهويّة من صبغة الرسم، والإشباع من إشباعه بسقف، والعمق ثابت في العائلة
    s_1 = min(max(s1 * .5, .10), .34)
    v0 = next(v for v in np.arange(.99, .80, -.002) if (lum(paper) + .05) / (lum(rgb(h1, .045, v)) + .05) >= 1.10)
    out = {
        '--pg-base': rgb(h1, .045, v0),                          # الورق المائيّ: همسة الصبغة بفرق 1.10 عن الورقة
        '--pg1': rgb(h1, s_1, .87 + (s_1 - .10) * .3),           # البقعة الغالبة
        '--pg2': rgb(h2, min(max(s2 * .4, .08), .24), .93),      # البقعة المقابلة من الصبغة الثانية
        '--pg3': rgb(h1, min(s_1 * 1.3, .42), .62 + s_1 * .5),   # حافّة المدّ والرذاذ
    }
    print('/* %s */' % path)
    for k, v in out.items(): print('  %s:%s;' % (k, hexof(v)))
    base = out['--pg-base']; print('  /* الورق #fffdf8 على المكتب: %.3f (يجب ≥ 1.08) */' % ((lum(paper) + .05) / (lum(base) + .05)))

for p in [a for a in sys.argv[1:] if not a.startswith('--')] or sys.exit(__doc__ or 'python3 tools/art-palette.py <رسم>'):
    palette(p)
