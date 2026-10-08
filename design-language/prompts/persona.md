# برومبت الشخصيّة: مشهد ومقصوص

> الشخصيّة العامّة للبوّابة (الصفحة العامّة وكبسولة المستشار). الأصول في `design/persona/`: `*-scene.webp` و
> `*-cutout.webp` (1254 مربّعا)، والمشتقّات في `src/assets/persona/` من `tools/persona-assets.mjs`. رسمها جو بنفسه؛
> الوصفة هنا **مستنتجة من الأصول** لتُعاد بنفس اليد، لا نصّ برومبته الأصليّ.

## القاعدة: زوج لكلّ لقطة

كلّ لقطة تُولَّد مرّتين بنفس البذرة والوصف: **مشهد** (الشخص على ورق مائيّ بغيمة لون) و**مقصوص** (الشخص وحده
بخلفيّة شفّافة). المشهد للأماكن الواسعة التي يكون فيها الورق نفسه خلفيّة (رأس الصفحة العامّة)، والمقصوص للأماكن
التي يقف فيها على ورق الصفحة (الكبسولة، البطاقة). لا يُقصّ المشهد بالأداة: القصّ الآليّ يترك هالة (§11 «إزالة
الخلفيّة»)؛ المقصوص يُولَّد مقصوصا.

## البرومبت الأساس

```text
Portrait illustration of a [PERSON], [POSE], soft natural expression, looking [GAZE].
Ink-and-watercolor editorial style: clean confident ink contour, transparent watercolor fills,
warm skin tones, white garment rendered with pale warm-grey shadows, not pure white.
Behind the figure a loose watercolor bloom in [TONE_NAME] ([TONE_HEX]) fading into cream paper (#fffdf8),
a few tiny muted-gold flecks (#b8912e) scattered like spatter. No hard background, no room, no props
unless listed: [PROPS]. No text, no logo, no watermark.
Framed from mid-chest up, figure centered, generous headroom. Square 1:1, high resolution.
```

وللمقصوص يُستبدل سطر الخلفيّة بـ:

```text
Isolated figure on a fully transparent background, no bloom, no paper, no shadow on the ground,
clean alpha edges around hair and shoulders.
```

## متغيّرات القمّة

| الخانة | القيمة |
|---|---|
| `[PERSON]` | young Saudi man in his twenties, white thobe, thin-framed glasses, neatly trimmed beard |
| `[POSE]` | الصفحة العامّة: calm, one hand relaxed; الكبسولة: slight head tilt, attentive listening |
| `[GAZE]` | toward the reader's right (the page's reading start in RTL) |
| `[TONE]` | teal `#0e7d86` |
| `[PROPS]` | none |

## جيهان: المعلّمة (2026-09-29، ب-332)

بطلب جو: «بشكل معلمة، لابسة نظارة... محجبة حجاب سعودي. بنفس طريقة الرسمة». تُولَّد **ورسمة الشابّ (`design/persona/capsule-scene.webp`) مرفقة
مرجعا للأسلوب**، فتخرج بيدٍ واحدة. والنظرة إلى القارئ لا إلى يمينه: الكبسولة وجهٌ يُكلَّم (وجه الشابّ المقصوص ينظر للكاميرا).

```text
Portrait illustration of a friendly Saudi woman teacher in her late twenties, a female counterpart to the attached reference character. She wears a black Saudi-style hijab (shayla) wrapped neatly around her head and neck, hair fully covered, face fully visible, a simple black abaya, and thin-framed glasses. Slight head tilt, attentive listening, warm confident smile, looking at the viewer.
Same hand and style as the attached reference image: ink-and-watercolor editorial illustration, clean confident ink contour, transparent watercolor fills, warm skin tones, the black fabric rendered in soft ink-wash greys with gentle highlights, not flat black. Not photorealistic.
Behind her a loose watercolor bloom in teal (#0e7d86) fading into cream paper (#fffdf8), a few tiny muted-gold flecks (#b8912e) scattered like spatter. No room, no props, no text, no logo, no watermark.
Framed from mid-chest up, figure centered, generous headroom. Square 1:1, high resolution.
```

**وخرجت الرسمة المعتمدة من هذا البرومبت** (جو 16:37: «ووافعلها عند اختيار جهان، والـ default للبوابة راح يكون أبو محمد. وعند اختيارها، ستتفاعل»): محفوظة في
`design/persona/jihan-scene.webp`، ومقصوصة بأداة وجه الشابّ نفسها (`node tools/face-crop.mjs --jihan`، المربّع مقيس من بكسلاتها) إلى
`src/assets/persona/advisor-face-jihan.webp`، ويلبسها المجلس ساعة يُختار صوت جيهان (الجولة 255، دليل التصميم §13-ق).

## المستشاران في صدر الهبوط (2026-09-29، ب-335)

أرفق جو ستّ رسمات بيده نفسها (20:41)، ولا برومبت منّا لها: جيهان واقفة بطولها، والاثنان وجها للكاميرا، والاثنان ينظر كلّ منهما للآخر، كلّ واحدة مشهدا مائيّا ومقصوصا. محفوظة في `design/persona/` (`jihan-landing-scene.webp` و`jihan-cutout.webp`، و`duo-front-*`، و`duo-gaze-*`). ومنها تشتقّ `tools/landing-shots.mjs` أحجام لقطات الصدر (`src/assets/persona/shot-*`، والبيان `shots.json`)، ولقطتا الاثنين بصندوق قصّ واحد فيبقى الوجهان في موضعهما حين يلتفتان. والتسلسل والأوقات في دليل التصميم §19.

## التنويع

الشخص والمهنة والنغمة تتغيّر بين المشاريع؛ **الثابت**: حبر نظيف، ماء شفّاف، ورق كريميّ `#fffdf8` لا بيج، رذاذ
معدن التوقيع، إطار من الصدر، لا نصّ. شخصيّة بخلفيّة مصمتة أو صورة فوتوغرافيّة تخرج عن العائلة.

## الفحص

`node tools/persona-assets.mjs --check` بعد الاشتقاق، ثمّ النظر على 390 و1440: الوجه والنظّارة مكبّرة مرّتين بلا
تشويش، والحافّة على ورق الصفحة بلا هالة بيضاء.

## برومبتات جو بحرفها

لا شيء بعد. أوّل برومبت يولّد رسما مقبولا يُلصق هنا بنصّه وتاريخه والرسم الذي ولّده.
