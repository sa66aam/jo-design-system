#!/usr/bin/env python3
# (145) رسوم بطاقات الشبكة: من الأصل الخام في «مراجع الشبكة» (خارج قِت) إلى src/assets/grid/<المفتاح>.webp.
# جو يسمّي كلّ رسم باسم محطّته بالعربيّة، فالاسم يدلّ على المفتاح، وما لا يُعرف اسمه يُطبع باسمه ولا يُخمَّن.
# الرسم لا يُرسم من جديد ولا يُلوَّن: يُسطَّح على الأبيض (البطاقة تطبعه بالضرب فيسقط البياض)، ويُقصّ على حدود
# حبره بهامش صغير (فالبطاقة تحتويه في خانتها كاملا بلا قصّ ولا يعبر إلى الكلام)، ويُصغَّر، ويُحفظ ويب بي.
# ويُشغَّل حيث توجد مكتبة الصور (صندوق الجلسة)، والأصل الخام لا يدخل قِت أبدا.
# python3 tools/grid-art.py [مجلّد الأصل] [مجلّد المخرج] [--dry]
import os, re, sys, unicodedata
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
SRC = args[0] if len(args) > 0 else os.path.join(ROOT, 'مراجع الشبكة')
OUT = args[1] if len(args) > 1 else os.path.join(ROOT, 'src', 'assets', 'grid')
DRY = '--dry' in sys.argv
MAX_SIDE, QUALITY = 560, 90
INK, MARGIN = 236, 0.035   # الحبر: أدنى قناة تحت 236 (ورق الرسم فوقها)، والهامش نسبة من ضلع الرسم الأطول

def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = ''.join(c for c in s if not (0x064B <= ord(c) <= 0x0655 or ord(c) in (0x0640, 0x0670)))
    return s.translate(str.maketrans('أإآةى', 'اااهي'))

# الكلمة التي تميّز كلّ محطّة في اسم ملفّها (بعد التطبيع)، بالترتيب: الأدقّ أوّلا
KEYS = [('مستوي', 'level'), ('نماذج', 'models'), ('اخطا', 'errors'), ('جديد', 'fresh'),
        ('لفظي', 'lafzi'), ('كمي', 'kami'), ('ذهبي', 'golden')]

def key_of(name):
    n = norm(os.path.splitext(name)[0])
    hits = [k for w, k in KEYS if w in n]
    return hits[0] if len(hits) == 1 else None

files = sorted(f for f in os.listdir(SRC) if re.search(r'\.(png|jpe?g|webp)$', f, re.I)) if os.path.isdir(SRC) else []
seen, unknown, rows = {}, [], []
for f in files:
    k = key_of(f)
    if not k: unknown.append(f); continue
    if k in seen: sys.exit('مفتاح لملفّين: %s ← %s و%s' % (k, seen[k], f))
    seen[k] = f
for k, f in sorted(seen.items()):
    im = Image.open(os.path.join(SRC, f))
    w0, h0 = im.size
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    else:
        im = im.convert('RGB')
    im = im.point(lambda v: min(255, round(v * 255 / 247)))   # ورق الرسم أبيض خالص، فلا يترك الضرب مربّعا باهتا حوله
    a = np.asarray(im).min(axis=2) < INK
    ys, xs = np.where(a.sum(axis=1) >= 3)[0], np.where(a.sum(axis=0) >= 3)[0]
    if len(ys) and len(xs):
        m = round(MARGIN * max(xs[-1] - xs[0], ys[-1] - ys[0]))
        im = im.crop((max(0, xs[0] - m), max(0, ys[0] - m), min(im.width, xs[-1] + 1 + m), min(im.height, ys[-1] + 1 + m)))
    if max(im.size) > MAX_SIDE:
        r = MAX_SIDE / max(im.size)
        im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    dst = os.path.join(OUT, k + '.webp')
    if not DRY:
        os.makedirs(OUT, exist_ok=True)
        im.save(dst, 'WEBP', quality=QUALITY, method=6)
    rows.append((k, f, '%dx%d' % (w0, h0), '%dx%d' % im.size, os.path.getsize(dst) if not DRY else 0))
for r in rows: print('%-7s ← %s · %s → %s · %s بايت' % r)
for f in unknown: print('لم يُعرف مفتاحه (يُسمّى باسم محطّته ويُعاد):', f)
missing = [k for _, k in KEYS if k not in seen]
if missing: print('بلا رسم بعد:', '، '.join(missing))
print('رسوم:', len(rows), '· مجهولة:', len(unknown), '· %s' % ('معاينة بلا كتابة' if DRY else 'كُتبت في ' + os.path.relpath(OUT, ROOT)))
