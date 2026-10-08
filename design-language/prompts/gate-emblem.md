# برومبت شعار البوّابة: الوصول إلى القمّة داخل لؤلؤتها

> وُلد 2026-09-29 (ب-336) بطلب جو، مكان رسمة الذيب على القمّة. **ووصلت الرسمة (21:16) وركبت في الجولة 256** (`design/brand/gate-emblem.webp`)، ومعها كلمته: «وأقترح أن يكون صورة الطالب هي صورة القمة اللي أرفقتها الآن، إضافة إلى شعار البوابة».

## بحرف جو (2026-09-29، 20:41)

«وبما أننا تطورنا، أنا أرى أن صورة الذيب في القمة صارت خارجة عن نموذجنا الجديد. فنحتاج إلى صورة مثل جودة الصور التي أرفقتها لك فوق لأبو محمد وجيهان. أن تعطيني وصفًا يكون من نفس الـ Theme، لكن يعطيك الإمكانية أن تضعها فعلاً في لؤلة البوابة، كأن واحد ماسك القمة، فهمتني؟ هكذا يعني، فأعطني برومت اللي يخص الوصول القمة ويعبر عنها، ليك أن واحد طلع لها وحط العلم.»

## البرومبت

يُلصق في مولّد الصور، **ومعه رسمة أبو محمد وجيهان المائيّة مرجعا للأسلوب** (`design/persona/duo-front-scene.webp`)، كما وُلدت جيهان من رسمة الشابّ (ب-332).

```text
Circular emblem illustration for a study platform named after reaching the summit. A small young climber, seen from behind in three-quarter view and gender-neutral (simple hooded jacket and small backpack, face not visible), stands on the very top of a single sharp mountain peak and has just planted a flag: one hand still gripping the flagpole, the other arm raised toward the sky in quiet triumph. The flag is plain teal (#0e7d86) with a thin muted-gold (#b8912e) edge, rippling in the wind; no symbol, no text, no emblem on it, not a national flag.
Same hand and style as the attached reference image: ink-and-watercolor editorial illustration, clean confident ink contour, transparent watercolor washes, the rock rendered in soft ink-wash greys with gentle highlights, warm light. Not photorealistic.
Composition for a round badge: the whole scene sits inside a perfect circle that fills the square frame with a small margin. The peak rises from the bottom edge to the center, and the climber and flag stand in the upper middle, large and simple enough to stay readable when the badge is shrunk to 40 pixels: the climber is the darkest ink accent and the flag the brightest color. Behind them a loose watercolor bloom in teal fading into cream paper (#fffdf8), a pale gold sun low behind the summit, soft clouds wrapping the base of the mountain to show height, and a few tiny muted-gold flecks scattered like spatter. Outside the circle: flat plain white, nothing else.
No frame, no border ring, no text, no letters, no logo, no watermark. Square 1:1, high resolution.
```

## لماذا هكذا

- **المتسلّق بلا جنس ظاهر ومن ظهره:** المنصّة للأولاد والبنات (جو، 20:41: «إحنا ما احنا موجهين هذه المنصة للأولاد فقط، حتى البنات»)، والوجه لا يُقرأ في عملة 40 بكسلا أصلا.
- **العلم بلا رمز ولا كتابة ولا علم دولة:** رمزٌ في شعار يُصغَّر يصير بقعة، وعلم دولة لا يُستعار شعارا.
- **الحلقة الذهبيّة لا تُرسم في الصورة:** الوسام يرسم حلقتيه فوق الوجه (`Medallion` في `src/components/BadgeMoment.jsx`)، وحلقة مخبوزة في الصورة تتضاعف معهما.
- **ما خارج الدائرة أبيض سادة:** تُقصّ الدائرة بالكود، فلا يُعتمد على شفافيّة يعطيها المولّد أو لا يعطيها.

## الإصدار الثاني: الظلّ بدراما الذيب (ب-339، 2026-09-29)

**بحرف جو (22:35، بعد نشر 256):** «The mountain is not very clear, to be honest. I think we should make it a shadow with the same drama format, but it should appear like a shadow of a man in the mountain with his flag. The background will show the flag and the mountain. Like the wolf before, we should tweak it a little bit like this.» **ثمّ (22:39):** «Give me a prompt, and I will do it perfectly.»

يُلصق في مولّد الصور ومعه مرجعان: **عملة الذيب القديمة** للدراما (`git show 80ec761:src/assets/gate-mark.webp`)، و**رسمة القمّة** للموضوع (`design/brand/gate-emblem.webp`).

```text
Circular badge emblem in the same dramatic backlit silhouette style as the attached wolf emblem, with the subject of the attached summit illustration. A huge luminous sun disc fills the middle of the circle, glowing warm pale gold (#f2d27e) and fading to soft cream white (#fffdf8) at its core. In front of it, everything is one solid dark silhouette in deep ink (#152a2d, near black) with no inner detail: a single sharp mountain peak rising from the bottom of the circle to just below its center, and on the very top a small gender-neutral climber seen from behind, one fist raised high in triumph, the other hand gripping a tall flagpole planted in the summit, a small backpack on the back. The flag waves to the right and sits completely inside the bright disc, so the climber, the pole and the flag read as clean dark shapes against the light. Bold simple shapes and crisp edges, readable even when the emblem is shrunk to 40 pixels.
Around the disc a soft misty sky of pale teal (#a9d3d0) and cream watercolor washes, lighter near the disc and deepening gently to muted teal (#3d7b80) at the circle's edge, always lighter than the mountain so its outline stands out everywhere. Low mist wraps the base of the mountain, a faint gold rim light traces its ridges, and a few tiny muted-gold flecks (#b8912e) are scattered like spatter. No other colors.
Ink-and-watercolor editorial illustration, same hand as the references, not photorealistic, not flat vector art. The whole scene sits inside a perfect circle that fills the square frame with a small margin; outside the circle plain flat white. No text, no letters, no logo, no border ring, no watermark. Square 1:1, high resolution.
```

**لماذا هكذا:**

- **ظلّ واحد بلا تفاصيل داخله:** في عملة 42 بكسلا لا يُقرأ إلّا الشكل، وتفاصيل الماء والصخر تصير نقشا. وفي الرسمة الأولى المتسلّق نحو 10 بكسلات في العملة.
- **القرص خلف المتسلّق والعلم معا:** أقوى تباين في العملة يقع على أهمّ شكلين. وفي الرسمة الأولى العلم تيل على سماء فيها تيل، فلم يظهر.
- **السماء أفتح من الجبل في كلّ موضع:** هذي شكوى جو بعينها («The mountain is not very clear»)، والذيب كان داكنا على سماء فاتحة.
- **الظلّ حبر عميق لا أسود خالص** (`#152a2d`): يبقى في عائلة التيل، والذهب في القرص وحافّة الضوء والرذاذ وحدها.
- **وكما في الإصدار الأوّل:** المتسلّق بلا جنس ظاهر، وما خارج الدائرة أبيض سادة، والحلقة لا تُرسم في الصورة.

**وحين تصل الرسمة:** تُقصّ دائرتها على شفافيّة وتوضع مكان الأصل، ثمّ `node tools/gate-emblem.mjs` ثمّ `--check`، ويُرفع رمز نسخة الأيقونات في `index.html` و`public/manifest.json`، ويُحكم عليها في العملة (42) ودائرة الطالب (28) والأيقونة.

**ووصلت الرسمة (22:51) وركبت في الجولة 257** بكلمته: «You can make it closer and do your job». جاءت دائرة على شفافيّة (1254 مربّعا)، فوُضعت مكان الأصل كما هي، والقصّ الأقرب صار ثابتا في الأداة (`FOCUS`: تكبير 1.8 حول القرص والمتسلّق، اختير بالنظر على 42 و28 و84 و180 بين 1.4 و2). **ثمّ قال بعد لقطة القصّ (23:05):** «the yellow color is destroying everything. I like it more of a moon-like color»، فالأصفر يُسحب في الاشتقاق (`MOON`)، واختار من أربع (23:07): «The middle pearl one is the best one». **فالبرومبت القادم لأيّ شعار من هذي العائلة يطلب القرص قمرا لؤلؤيّا لا شمسا صفراء** (`pale pearl moon, soft ivory-grey, no yellow` مكان سطر القرص الذهبيّ).

## أين يسكن في الكود (ركب في الجولة 256)

الأصل واحد (`design/brand/gate-emblem.webp`، دائرة على شفافيّة)، ومشتقّاته بأداة لا بيد: `node tools/gate-emblem.mjs` يكتبها وبيانها `src/assets/gate-emblem.json`، و`--check` يقرأ فقط. ورسمة جديدة تُوضع مكان الأصل وتُشغَّل الأداة.

| المشتقّ | يُستعمل في | كيف |
|---|---|---|
| `src/assets/gate-mark.webp` (256) | عملة الشريط (`AppBar.jsx`)، ودائرة الطالب في المحادثة (`AdvisorParts.jsx`، ب-337)، ووجه الوسام القديم (`BadgeMoment.jsx`) | الدائرة مقصوصة بشفافيّة خارجها |
| `public/icons/icon-512.png` و192 و180 | أيقونة التطبيق (`public/manifest.json`)، وأيقونة المتصفّح والآيفون (`index.html`) | على ورق البوّابة بحلقة ذهب رفيعة، والدائرة داخل منطقة الأمان (80%)، والرابط برمز نسخة `?v=` |

**والمقاس على قدر أكبر رسم:** الرسمة المائيّة أثقل من الرماديّة قبلها، فلو بقيت بمقاس الذيب (512) لتضاعف وزن العملة (87 كيلوبايت مقابل 38) وهي في كلّ صفحة؛ فصارت 256 (26 كيلوبايت).

**وختم شاشة الجولة الباهت لم يُشتقّ من هذي الرسمة** (ب-338): اشتُقّ أوّلا مكان الذيب، ثمّ قال جو قبل نشره (21:55): «Take the old wolf from the ghost in each training question... Don't replace it. We want a clean background». فخرج الختم كلّه، عنصره وقواعده وملفّه، ولا يعود بأيّ شعار.

**وقانون 2026-07-26 «لا شعار ملوّن» نُسخ بكلمة جو** في الجولة نفسها: في `.claude/rules/qimma-design.md` («شعار البوّابة رسمة القمّة المائيّة») وسطر فهرسها في `CLAUDE.md`، وفي دليل التصميم §11 و§19. والباقي منه حكمه: لا تلوين بالفلتر ولا مزج. وحارسه `tools/gate-emblem.test.mjs`.
