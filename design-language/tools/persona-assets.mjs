#!/usr/bin/env node
// ═══ أحجام رسمة الشخصيّة العامّة (الجولة 149) ═══
// الرسمة الأصل رسمها المالك بنفسه (design/persona/landing-cutout.webp، 1254 مربّعا بخلفيّة شفّافة)، وهذي الأداة
// تشتقّ منها أحجام الصفحة ولا تعيد رسمها: تقصّ الهامش الشفّاف حول الجسم (والحافّة السفلى المقطوعة تبقى حافّة
// الصورة)، ثمّ تصغّر إلى كلّ عرض مطلوب، وتحفظ ويب بي بقناة الشفافيّة. لا تلوين ولا تشويه: الأبعاد بنسبتها، والألوان
// كما هي (بلا تحويل فضاء لون ولا ضرب في الشفافيّة عند الفكّ).
//
//   node tools/persona-assets.mjs            يكتب الأحجام والبيان ويطبع ما كتبه
//   node tools/persona-assets.mjs --check    يقرأ فقط: هل البيان يطابق الأصل والملفّات؟ (الحارس يفعل مثله في البوّابة)
//
// الفكّ والتصغير والترميز في كروميوم خفيّ (المتصفّح نفسه الذي تشغّله فحوص e2e): لا مكتبة جديدة في المستودع.
import { chromium } from 'playwright-core'
import fs from 'fs'
import path from 'path'
import crypto from 'crypto'
import { fileURLToPath } from 'url'

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const EXE = process.env.CHROME || '/opt/pw-browsers/chromium'
export const SOURCE = 'design/persona/landing-cutout.webp'
export const OUT_DIR = 'src/assets/persona'
export const MANIFEST = OUT_DIR + '/persona.json'
// العروض: 560 للجوال بكثافة 2 وما دونها، و800 لكثافة 3 على الجوال، والعرض الأصليّ للمقصوص للشاشة العريضة بكثافة 2.
// والأصليّ لا يُكبَّر أبدا: عرضٌ فوق عرض المقصوص يُسقط لأنّه يثقل ولا يزيد حدّة.
const WIDTHS = [560, 800, 'native']
const QUALITY = 0.76     // قِيست بالعين على الوجه والنظّارة مكبّرة مرّتين: 0.76 لا تُفرَّق عن 0.84 وأخفّ بنحو 15%
const PAD = 12            // هامش حول الجسم بعد القصّ (بكسل من الأصل)، إلّا الحافّة السفلى المقطوعة

const sha = buf => crypto.createHash('sha256').update(buf).digest('hex')

async function derive() {
  const src = fs.readFileSync(path.join(ROOT, SOURCE))
  const b = await chromium.launch({ executablePath: EXE, args: ['--no-sandbox'] })
  try {
    const page = await b.newPage()
    const out = await page.evaluate(async ({ b64, widths, q, pad }) => {
      const bytes = Uint8Array.from(atob(b64), c => c.charCodeAt(0))
      const bm = await createImageBitmap(new Blob([bytes], { type: 'image/webp' }), { premultiplyAlpha: 'none', colorSpaceConversion: 'none' })
      const W = bm.width, H = bm.height
      const cv = new OffscreenCanvas(W, H), g = cv.getContext('2d')
      g.drawImage(bm, 0, 0)
      const d = g.getImageData(0, 0, W, H).data
      let x0 = W, y0 = H, x1 = -1, y1 = -1
      for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (d[(y * W + x) * 4 + 3] > 8) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y }
      const cx = Math.max(0, x0 - pad), cy = Math.max(0, y0 - pad), cw = Math.min(W, x1 + 1 + pad) - cx, ch = H - cy
      const cutAtBottom = y1 === H - 1
      const res = []
      for (const want of widths) {
        const w = want === 'native' ? cw : Math.min(want, cw)
        if (want !== 'native' && want >= cw) continue
        const h = Math.round(ch * w / cw)
        const piece = w === cw
          ? await createImageBitmap(bm, cx, cy, cw, ch, { premultiplyAlpha: 'none', colorSpaceConversion: 'none' })
          : await createImageBitmap(bm, cx, cy, cw, ch, { resizeWidth: w, resizeHeight: h, resizeQuality: 'high', premultiplyAlpha: 'none', colorSpaceConversion: 'none' })
        const oc = new OffscreenCanvas(w, h), og = oc.getContext('2d')
        og.drawImage(piece, 0, 0)
        const blob = await oc.convertToBlob({ type: 'image/webp', quality: q })
        if (blob.type !== 'image/webp') throw new Error('المتصفّح لم يرمّز ويب بي (' + blob.type + ')')
        // تحقّق بعد الترميز: الزوايا شفّافة، وقلب الجسم معتم، والأبعاد كما طُلبت
        const back = await createImageBitmap(blob, { premultiplyAlpha: 'none', colorSpaceConversion: 'none' })
        const vc = new OffscreenCanvas(back.width, back.height), vg = vc.getContext('2d')
        vg.drawImage(back, 0, 0)
        const vd = vg.getImageData(0, 0, back.width, back.height).data
        const a = (x, y) => vd[(Math.round(y) * back.width + Math.round(x)) * 4 + 3]
        const check = { corner: a(1, 1), cornerR: a(back.width - 2, 1), chest: a(back.width * 0.55, back.height * 0.62) }
        const buf = new Uint8Array(await blob.arrayBuffer())
        let s = ''; for (let i = 0; i < buf.length; i += 0x8000) s += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000))
        res.push({ w, h, b64: btoa(s), check, dims: [back.width, back.height] })
      }
      return { src: [W, H], crop: [cx, cy, cw, ch], bbox: [x0, y0, x1, y1], cutAtBottom, res }
    }, { b64: src.toString('base64'), widths: WIDTHS, q: QUALITY, pad: PAD })
    return { src, out }
  } finally { await b.close() }
}

async function main() {
  const check = process.argv.includes('--check')
  if (check) {
    const m = JSON.parse(fs.readFileSync(path.join(ROOT, MANIFEST), 'utf8'))
    const src = fs.readFileSync(path.join(ROOT, SOURCE))
    let bad = 0
    if (m.source.sha256 !== sha(src)) { bad++; console.error('الأصل تغيّر بعد آخر اشتقاق: شغّل node tools/persona-assets.mjs') }
    for (const v of m.variants) {
      const p = path.join(ROOT, v.file)
      if (!fs.existsSync(p)) { bad++; console.error('ناقص:', v.file); continue }
      const buf = fs.readFileSync(p)
      if (buf.length !== v.bytes || sha(buf) !== v.sha256) { bad++; console.error('لا يطابق البيان:', v.file) }
      else console.log('مطابق', v.file, v.w + 'x' + v.h, Math.round(v.bytes / 1024) + ' KB')
    }
    process.exit(bad ? 1 : 0)
  }
  const { src, out } = await derive()
  fs.mkdirSync(path.join(ROOT, OUT_DIR), { recursive: true })
  const variants = []
  for (const r of out.res) {
    const file = OUT_DIR + '/landing-' + r.w + '.webp'
    const buf = Buffer.from(r.b64, 'base64')
    fs.writeFileSync(path.join(ROOT, file), buf)
    if (r.check.corner > 8 || r.check.cornerR > 8 || r.check.chest < 250 || r.dims[0] !== r.w || r.dims[1] !== r.h) throw new Error('فحص ما بعد الترميز فشل في ' + file + ': ' + JSON.stringify(r))
    variants.push({ file, w: r.w, h: r.h, bytes: buf.length, sha256: sha(buf) })
    console.log('كُتب', file, r.w + 'x' + r.h, (buf.length / 1024).toFixed(1) + ' KB', '(زاويتان شفّافتان ' + r.check.corner + '/' + r.check.cornerR + '، والصدر معتم ' + r.check.chest + ')')
  }
  const manifest = {
    note: 'مشتقّ بـ tools/persona-assets.mjs من الرسمة الأصل؛ لا يُحرَّر بيد',
    source: { file: SOURCE, w: out.src[0], h: out.src[1], sha256: sha(src), bytes: src.length },
    crop: { x: out.crop[0], y: out.crop[1], w: out.crop[2], h: out.crop[3], bbox: out.bbox, cutAtBottom: out.cutAtBottom },
    quality: QUALITY,
    variants
  }
  fs.writeFileSync(path.join(ROOT, MANIFEST), JSON.stringify(manifest, null, 2) + '\n')
  const total = variants.reduce((a, v) => a + v.bytes, 0)
  console.log('كُتب', MANIFEST, '· القصّ', out.crop.join(','), '· الحافّة السفلى مقطوعة:', out.cutAtBottom ? 'نعم' : 'لا', '· المجموع', (total / 1024).toFixed(1) + ' KB', '(الأصل ' + (src.length / 1024).toFixed(1) + ' KB)')
}
main().catch(e => { console.error(e.message || e); process.exit(1) })
