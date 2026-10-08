# Design Language Build Guide - v3.1 · لغة الورق: هويّة تنتقل

> **الحال (2026-10-08، الإصدار 3.1): بيت واحد للّغة.** بطلب جو بحرفه: «أحتاج الآن تتوحّد لغة التصميم من كلّ الثلاثة
> مشاريع في مجلّد واحد، وكلّهم يتكلّمون نفس لغة التصميم بكلّ الأصول التي تحتاجها، وبملفّ عربيّ يشرح السياق ويعرف أنّ هذا ليس
> خاصّا بمشروع واحد، وهي لغة عامّة وشحن أدوات». فصار الأصل هنا، في `jo-design-system/` بمجلّد المشاريع، لا في مشروع بعينه:
> - **هذا الملفّ** هو الأصل الوحيد. ونسخه في المشاريع **مرايا** تُنسخ منه بأداة الشحن (`tools/ship.sh`) ولا يُكتب فيها؛ أيّ
>   تعديل يقع هنا أوّلا ثمّ يُشحن.
> - **أصل القمّة** (`naif-gate-app/Lessons and Guides/`) دخل بحرفه كما هو يوم التوحيد (الأقسام 1 إلى 19)، **والجزء و** من
>   نسخة ستاندردز هب (ومعه إشاراته القصيرة في أ وب وج) دخل بحرفه كما كُتب هناك في 2026-09-28، بكلمة جو اليوم بدل انتظار
>   نقله. **والجزء ز** هو دليل أداة سباهي (الإصدار 2.6، بالإنجليزيّة) بحرفه، مثالا ثالثا من زمن ما قبل الورق. **والجزء ح**
>   جديد: الصفحة الحيّة واللوحة التي تتحرّك، وأداة الألوان المائية.
> - **الأصول كلّها** في `design-language/` بجانب هذا الملفّ (الجزء د): ما كان في القمّة وما زاد في ستاندردز هب، والأحدث من
>   كلّ ملفّ، ومعها الأدوات وأمثلة مجمّدة (الأمثلة في البيت وحده لا تُشحن لثقلها). **ومرجعا الحركة** في `worlds/`: جولة
>   ستاندردز هب الميدانيّة وفيلم صفحة هبوطها.
> - **من يقرأ:** أيّ جلسة تلمس واجهة في أيّ مشروع من مشاريع جو. اقرأ `اقرأني.md` بجانب هذا الملفّ أوّلا (السياق بالعربيّ)،
>   ثمّ الجزأين أ وب، ثمّ ما يخصّ سطحك.
>

> **الحال (2026-09-27، الجولة 217):** هذا الدليل صار **هويّة تنتقل بين المشاريع** لا وصفا لمشروع واحد. بطلب جو بحرفه:
> «نحدث هذا النموذج تحديث جوهري مع كل المراجع المطلوبة والأصول المطلوبة، ليخرج لنا لغة تصميمية تسمح بالتمييز ولكن
> لا تلغي الأساس. يعني المقصد ما نبي المشاريع كلها نسخة من بعض، لكن نبيها تحمل المنطق والهوية التصميمية ولديها حرية
> الابتكار في الألوان والشكل من نفس الـ palette أو من palettes متقاربة.» وقبلها بيومين: «كل رحلة التعديلات هذي وثقها
> بالتفصيل والمرجعية البنائية لملف لغة التصميم علشان يتطور ويكبر معنا».
>
> **فالترتيب الجديد أربعة أجزاء ثمّ السجلّ:**
> - **أ. النواة الثابتة:** ما يحمله كلّ مشروع من العائلة ولا يُساوَم عليه.
> - **ب. طبقة التنويع:** ما يتغيّر بين مشروع وآخر، وكيف يُشتقّ، وحدوده.
> - **ج. المتقاعد وليش:** كلّ ما قاد إلى التصميم المسطّح والأرضيّة البيج السادة والألوان التي من نوع واحد، خارج القواعد، ومعه سببه.
> - **د. الأصول:** البرومبتات وطريقة الدمج والرموز والرسوم والعيّنة، في `Lessons and Guides/design-language/`، كلّ أصل مربوط بمكانه في الكود.
> - **هـ. القمّة مثالا (§1 إلى §16):** السجلّ الكامل كما نضج، بأرقام أقسامه نفسها لأنّ الكود والحرّاس يشيرون إليها. **وحيث
>   يخالف قسمٌ قديم (§1 إلى §11، زمن قبل الورق) الجزء أ، فالجزء أ هو الحكم**، والقسم القديم يحمل علامة «متقاعد في 3.0» عند موضعه.
>
> **بيت واحد (جو، 2026-09-02):** هذا الملفّ البيت الوحيد للّغة البصريّة؛ أيّ قاعدة تصميم في مكان آخر مؤشّر إليه لا نسخة ثانية.
> وسجلّ الإصدارات من 2.x انتقل إلى **ملحق** في آخر الملفّ بحرفه.
>
> **لمن:** أيّ جلسة تلمس واجهة، في القمّة أو في مشروع شقيق. اقرأ الجزأين أ وب قبل أيّ سطر، ثمّ افتح من هـ القسم الذي
> يخصّ سطحك. والهدف أن يعرف جو كلّ سطح جديد أنّه «له» بلا جولة تصحيح واحدة، **وأن يعرف في الوقت نفسه أيّ مشروع هو**.

---

## أ. النواة الثابتة

ما يلي يحمله كلّ مشروع من العائلة. تغييره ليس تنويعا بل خروج من العائلة، ويحتاج كلمة جو.

### أ-1. المنطق في عشرة أحكام (تسبق أيّ لون وأيّ شكل)

1. **ورقة على مكتب، والفرق رقم.** كلّ سطح يُقرأ ورقة دافئة فاتحة، تقف على مكتب أغمق منها بنسبة تباين **1.08 فأكثر**
   تُقاس ولا تُقدَّر (§13-هـ). ورقة بلا مكتب مسمّى لم تُصمَّم بعد.
   **ستاندردز هب (و-1):** المادّة محور لا نواة: بورسلان أبيض على جوّ حيّ نجح بالمنطق نفسه، و1.08 تحقّق فيه ولم يكفِ؛
   الطفو أرضيّة حيّة، ومادّة غير مادّتها، وظلّ يُرى تحتها.
2. **ثلاث طبقات لا تختلط:** ورق لما يُقرأ، ومكتب لما يحمل غيره، وورق ناهض لما يُلمس (§15-ب 1). ما يُلمس ينهض، وما يُقرأ
   يسكن (§2b)؛ وإن نهض كلّ شيء لم ينهض شيء.
3. **لا ورق فوق ورق.** الحاوية التي تجمع أوراقا تخلع ورقتها. والصندوق داخل الصندوق عيب لا ستايل.
4. **زرّ مصبوغ واحد في الصفحة.** الخطوة المعتادة وحدها مصبوغة بلون البيت؛ كلّ ما سواها ورق ناهض، وحاله في جوهرة أو خطّ
   قاع، لا في تعبئة (§15-ب 3).
5. **اللون الكبير من الرسم، لا من العلبة.** مكتب الصفحة ودرجات إخوتها تُشتقّ من رسم قسمها (`tools/art-palette.py`)،
   وتُركَّب ماءً بطبقات لا لطخة سادة (§15-ب 5 و7، الوصفة 11).
   **ستاندردز هب (و-1):** حيث لا رسم للقسم يأتي اللون الكبير من هويّة الصفحة (لون فصلها)، والمنطق واحد: لا علبة محايدة.
6. **الإخوة درجات من عائلة، مرتّبة فلا تتجاور درجتان متقاربتان.** هذا علاج «الألوان كلّها بنفس الصفة»: التمييز بالدرجة
   والشبح والرسم، والعائلة واحدة (§15-ب 6، §10 #23).
   **ستاندردز هب (و-1):** ألوان هويّة ثابتة من المحتوى تُرسم جواهر بضوء، لا درجات من عائلة؛ والباهت فيها عيب.
7. **الحال جوهرة صغيرة، والحكم بنبرة الورق.** الشارة ورقة صغيرة بحبر الصفحة وجوهرة بلون الحال قبل الكلمة، ووجهها واحد
   في المشروع كلّه (`gem.css`)؛ والصحّ والغلط هادئان بعلامة مرسومة (§15-ب 4، §15-ج 2-ز).
   **ستاندردز هب:** ثبت كما هو (شارته الواحدة `.ui-pill`)، وألوان الحكم محور (و-2).
8. **الصورة تُدمج ولا تُلصق.** كلّ رسم يُطبع بالضرب في خانة تحتويه كاملا، والدمغة بثلث حبرها تذوب من ركنها (أ-3).
9. **كلّ كلمة تفرّق، وكلّ أيقونة فكرة، وكلّ حركة تقول ما تغيّر** (§15-ب 8). ما يتكرّر على الكلّ يُحذف، والأيقونة قناع
   بخطّ واحد، والحركة تسكن.
10. **الأصل الحقيقيّ يحكم، والعين آخر الحكم.** الخطّ الحقيقيّ والرسم الحقيقيّ وأطول نصّ حقيقيّ، على 390 و430 و1280
    و1440؛ والرقم شرط لازم لا كافٍ (§10 #22، §15-هـ 8 إلى 10).

### أ-2. الورقة ومكتبها والطبقات

| الطبقة | الوجه | القيم (القمّة، تُنقل كما هي) | البيت في الكود |
|---|---|---|---|
| الورقة | دافئة فاتحة، زاوية 22 (18 جوال) | `#fffdf8`، حدّ `rgba(176,150,96,.46)`، ظلّ `0 1px 2px rgba(74,63,46,.09), 0 10px 26px -16px rgba(74,63,46,.36)` | `src/styles/coach2.css` قسم 164 |
| المكتب | ماء بطبقات من رسم القسم | أربع درجات `--pg-base --pg1 --pg2 --pg3` + حبيبة ورق؛ الاحتياط `#f2ece0` | `src/styles/record.css`، `admin.css` |
| الورق الناهض | تدرّج ورق، إضاءة علويّة، ظلّ تلامس ثمّ عمق | `linear-gradient(180deg,#fffefb,#fbf6ec)`؛ يرتفع 1.5 عند المرور وينضغط 0.5 | `src/styles/product.css` 171-ب |
| الطافي | بلا مكتب | حدّ الورق + حلقة بلون المكتب `0 0 0 4px` + ظلّ أعمق | آخر `src/styles/companion.css` |
| اللؤلؤ (النافذة) | ورقة قرار بختم معناها | تدرّج لؤلؤيّ، ستار دافئ، فعل مصبوغ واحد على الأكثر ولا واحد على وجه يمسح | `src/styles/dialog.css` (§13-ع) |

**الظلّ دافئ دائما** (`rgba(74,63,46,…)`)؛ ظلّ أسود بارد على سطح جديد عيب. والرموز كلّها في `design-language/core-tokens.css`.

**ستاندردز هب (و-1):** الظلّ بلون الأرضيّة التي يقع عليها، لا دافئ دائما: حبر تيل على ضباب بارد، وكحليّ على مخطّط الجولة،
والبنّيّ الدافئ هناك عيب. والثابت في المشروعين: لا ظلّ أسود ولا رماديّ.

### أ-3. الرسم المدموج: ما لا يقدر عليه الكود

حين عجز CSS وSVG والجافاسكربت عن عمق مرسوم باليد، لجأنا إلى **صور تُولَّد لتُدمج**: طبيعة صامتة بالحبر والماء على
ورق أبيض نقيّ، جسم واحد يحمل معنى القسم، ظلّ مائيّ واحد، نغمة القسم وحدها مع لمسة معدن التوقيع. ثمّ:

1. **الأصل الخام خارج قِت** باسم محطّته بالعربيّة، و`tools/grid-art.py` يبيّض ورقه ويقصّه على حبره ويحفظه ويب بي.
2. **يُطبع بالضرب** (`mix-blend-mode:multiply`) في خانة محسوبة (`object-fit:contain`) في الجهة البعيدة عن الكلام، داخل
   ورقة معزولة (`isolation:isolate`) حتّى يضرب في ورقها لا في فراغ (§15-د 12). **هذا هو الدمج ثلاثيّ الأبعاد:** الحبر يغمق
   الورق كحبر حقيقيّ، والظلّ المائيّ يأخذ دفء المكتب.
3. **الدمغة** نفس الرسم بثلث حبره وقناع يذيب ركنه، في رأس الصفحة.
4. **ولون الصفحة كلّها يُشتقّ منه** (أ-1 حكم 5).

البرومبتات بنصّها وطريقة الدمج خطوة خطوة في `design-language/prompts/`، والشخصيّة (مشهد ومقصوص) في `persona.md` منها.
**ولا رسم خلف فقرة تُقرأ، ولا نصّ داخل الرسم، ولا خلفيّة مرسومة.**

### أ-4. العنوان والشبح والاسم

- **العنوان بخطّ العرض** بحروفه المرسلة وخطّ قلم تحته بنغمة قسمه، للعناوين وحدها (§13). والجملة التي تلتفّ تأخذ خطّ قلم
  قصيرا تحتها لا شريطا تحت كلّ سطر (§13-ج إضافة 210).
- **الشبح يفرّق السلسلة:** رقم أو رمز كبير بعُشر النغمة يرسمه النمط لا النصّ (`content:attr(data-n) / ""`)، في الجهة
  البعيدة، مقصوصا بحافّة الورقة.
- **الاسم بماء الذهب** (أو معدن التوقيع في مشروع آخر) مقصوصا على الحروف.
- **كلّ صفحة لها رأس بدمغة قسمها وشبح وخلفيّة ماء من ألوانها؛ الجدار الصامت مرفوض.**

### أ-5. الشارة الواحدة والحكم

وجه واحد للوسم في المشروع كلّه، وبيت واحد (`src/styles/gem.css`): ورقة صغيرة ناهضة بحبر الصفحة، وجوهرة بلون الحال قبل
الكلمة (سليم، انتبه وكلمتها وحدها بالطوبيّ، راقب، فرصة وانتظار، جارٍ ينبض، جديد بختم ذهب، بلا بيانات حلقة جوفاء).
والتغيّر جملة لا وسم: مثلّث مرسوم بلون معناه والرقم بالحبر. **ولا سطح يصبغ الشارة؛ يضعها فقط.** والحكم: صحّ مريميّ
`#3f7354` وغلط طوبيّ `#a8483f` بـ✓ و× مرسومتين، وكلمتهما تُقرأ على غسلتهما بنسبة 4.5.

### أ-6. النافذة والحركة والنظافة

- **كلّ نافذة لؤلؤ بختم معناها** (§13-ع)، والكبسولة لاصقة بمكانها: لا تهتزّ ولا تنطّ ولا تغبش ولا ترفرف، ولا تغطّي محتوى.
- **الحركة:** منحنى السباحة `cubic-bezier(.2,.7,.3,1)`، دخول قصير لما يتبدّل ثمّ سكون، كلّ كشف له إخفاء، وتُطفأ كلّها
  مع تقليل الحركة (§7، الوصفة 14).
- **النظافة:** أرقام غربيّة دائما، بلا شَرطة طويلة، عربيّ 12 فما فوق وما دون 14 بوزن 600، وتباين 4.5 للكلام (§9).

### أ-7. فحص ما قبل التسليم (يحلّ محلّ §11 القديم)

- [ ] كلّ مكوّن مصنّف في طبقة من الثلاث، والحاوية التي تجمع أوراقا بلا ورقة.
- [ ] الورقة على مكتبها ≥ 1.08 مقيسة من البكسلات، في أعلى الصفحة وبعد التمرير.
- [ ] المكتب ماء من رسم القسم، لا لون سادة ولا تدرّج طويل.
- [ ] زرّ مصبوغ واحد؛ المختار بخطّ قاع لا بتعبئة؛ الشارة من `gem.css`.
- [ ] كلّ رسم بالضرب في خانته، لا يقصّ ولا يعبر إلى الكلام، ولا مربّع أفتح حوله.
- [ ] الإخوة درجات مرتّبة من عائلة واحدة، لا لونان متجاوران من صفة واحدة ولا لون خارج الباليت.
- [ ] رأس بدمغة وشبح؛ لا جدار صامت.
- [ ] 390 و430 و440 بأطول النصوص بلا يتيم في صفّ ولا تمرير جانبيّ، و1280 و1440 بتصميم أعرض.
- [ ] تقليل الحركة، والألوان القسريّة، وأرقام غربيّة، وحارس بطفرة حمراء.

**ستاندردز هب:** بنوده الزائدة في و-8.

---

## ب. طبقة التنويع: نفس المنطق، شكل آخر

**القاعدة:** مشروع شقيق يأخذ الجزء أ كما هو، ويختار في كلّ محور من المحاور أدناه قيمة واحدة يلتزم بها في كلّ صفحاته.
التنويع **داخل المشروع** ممنوع (يكسر الرفّ)، والتنويع **بين المشاريع** مطلوب (حتّى لا تكون نسخا).

### ب-1. المحاور الحرّة

| المحور | في القمّة | مساحة التنويع | ما لا يُتجاوز |
|---|---|---|---|
| لون البيت (الزرّ المصبوغ) | تيل `#0e7d86` | أيّ لون عميق هادئ يحمل أبيض بتباين 4.5 | لون مشبع صارخ؛ لونان للبيت |
| معدن التوقيع | ذهب `#b8912e` | نحاس، برونز، فضّة دافئة، نيليّ حبريّ | يُستعمل لمسات لا مساحات |
| نغمات الأقسام | البنك الصامت (§10b) | أيّ عائلة «الوسط الهادئ» بنفس الإشباع تقريبا | لون من خارج العائلة، أو نغمتان متجاورتان من صفة واحدة |
| المكتب | ماء من رسم القسم | يتغيّر بتغيّر الرسم تلقائيّا | لون سادة؛ تدرّج على طول الصفحة؛ بيج بلا رسم |
| الورقة | `#fffdf8` | من الأبيض الدافئ إلى العاجيّ الفاتح | ورقة أغمق من مكتبها أو بفرق دون 1.08 |
| مادّة الرسم | أشياء الدراسة | أشياء المشروع (تمور، أدوات طبّيّة، ملفّات) | مشهد بخلفيّة، شخص في رسم قسم، نصّ في الرسم |
| أداة الرسم (2026-10-08) | رسم مولَّد بمحرّك صور ثمّ مسطَّح ومضروب على الورق (`prompts/`، `tools/grid-art.py`) | لوحة مائيّة يرسمها الكود داخليّا بلا رصيد (`tools/watercolor.py`، الجزء ح)؛ أو محرّك مولِّد آخر؛ وماغنيفيك ون (Magnific One) مرشّح لم يُختبر، عدّة هويّته (Brand Kit) تقابل كتلة العائلة في `core-tokens.css` | خلط أداتين في مجموعة واحدة من الرسوم؛ كلمة مرسومة داخل اللوحة (العربيّة يكتبها التكوين) |
| زاوية الرسم وخطّه | ثلاثة أرباع، خطّ حرّ | من فوق، أو مستوى العين؛ خطّ هندسيّ أو فرشاة | خلط زاويتين في مشروع واحد |
| الانحناء | 22 للورقة، 15 للزرّ | من 14 إلى 28، أو أزرار كبسوليّة كاملة | زوايا حادّة صفريّة، أو انحناءان للطبقة نفسها |
| خطّ العرض | ثمانية بمرسلاته | أيّ خطّ عرض عربيّ مرخّص بعناية للعناوين | خطّ عرض على المتن؛ خطّ بلا رخصة ويب |
| الشبح | رقم بخطّ العرض | رقم، حرف، رمز مرسوم بخطّ رفيع | شبح يُقرأ (بشفافيّة فوق السدس) |

**ستاندردز هب:** قيمه على هذه المحاور، وأربعة محاور زادها (الكروم، وألوان الحكم، ولون الظلّ، وعالم ثانٍ لنشاط آخر)، في و-2.

### ب-2. كيف تُبنى باليت مشروع جديد

1. **ابدأ بالرسوم لا بالألوان.** ولّد رسوم الأقسام بالبرومبت (`prompts/station-still-life.md`) بنغمات مقترحة.
2. **اشتقّ المكتب من كلّ رسم:** `python3 tools/art-palette.py <الرسم>` يطبع الدرجات الأربع وتباين الورقة عليها؛ خذها بداية،
   والعين تضبطها (قيم «سجلّي» المشحونة قريبة منها لا مطابقة).
3. **اختر البيت والمعدن** من خارج نغمات الأقسام، حتّى لا يتلبّس زرّ الفعل بلون قسم.
4. **رتّب الإخوة:** اصفف النغمات بالصبغة، ثمّ باعد بين المتقاربة (§15-ب 6). وأيّ نغمتين تتجاوران في شبكة يجب أن يختلفا
   في الصبغة أو العمق بما تراه العين من بعيد.
5. **ثبّت نبرة الحكم** (صحّ وغلط وراقب) هادئة من عائلة المشروع، ولا تستعر أخضر وأحمر الأنظمة.
6. **ضع القيم في كتلة «العائلة»** من `core-tokens.css` وحدها، واترك كتلة «النواة».

### ب-3. مثالان من منطق واحد

`design-language/specimen.html` يرسم العائلتين بجوار بعض من النواة نفسها، ولقطتاه في الأصول:

- **القمّة:** مكتب بنفسجيّ مائيّ من رسم النماذج، بيت تيل، ذهب، زوايا 22.
- **مشروع شقيق (تمور فاخرة مثالا):** مكتب رمليّ دافئ من رسم آخر، بيت بنّيّ `#7a4a24`، معدن برونز، أزرار كبسوليّة كاملة.

والعين تعرف الاثنين من عائلة واحدة (ورقة على ماء، رسم مدموج، زرّ مصبوغ واحد، شارة واحدة)، وتفرّق بينهما من أوّل نظرة.

**ومثال ثالث حيّ، ستاندردز هب (5.0):** جوّ سيلادون حيّ من هويّة الصفحة بدل المكتب المائيّ، وبورسلان أبيض، وظلّ بلون الأرضيّة،
والفصول جواهر من ألوانها، وبيت تيل بخيط ذهبيّ، وكروم زجاج، وعالم ليليّ لجولة المنشأة. التفصيل في و.

---

## ج. المتقاعد وليش

كلّ بند هنا **خارج القواعد**، ومذكور فقط حتّى لا يرجع. وسطر «الأصل» يدلّ على موضعه في السجلّ.
**ستاندردز هب:** ما تقاعد عنده وليش في و-7.

| المتقاعد | ليش تقاعد | البديل | الأصل |
|---|---|---|---|
| لوحة ملوّنة شفّافة (0.72 إلى 0.9) على لوح | التصميم المسطّح: كلّ شيء نفس العمق فلا طبقة | ورقة على مكتب + ورق ناهض (أ-2) | §1، §2 |
| الأرضيّة البيج السادة، وتدرّج طويل على الصفحة كلّها | الورقة تذوب فيه (تباين 1.00 في أعلى صفحة طويلة)، وجدار صامت بلا هويّة | مكتب مائيّ من رسم القسم، والاحتياط لون ثابت يُقاس | §1 `.phc-canvas`، §10 #11، §13-هـ |
| «قماش واحد، ماء واحد» `#faf7f0` لكلّ الصفحات | ساوى بين الصفحات فصارت كلّها بصفة واحدة | لكلّ صفحة ماؤها من رسمها، والعائلة واحدة | §10 #11 |
| ألوان الحال المشبعة `#059669` و`#dc2626` و`#d97706` | صارخة، وتقرأ كتحذير نظام لا كحكم معلّم | مريميّ `#3f7354`، طوبيّ `#a8483f`، كهرمانيّ `#b36b2c` | §3 |
| تيل مائل وذهب مصبوغ على الألواح والصدر | لون كبير يطغى، وكلّ لوح بنفس الصبغة | ورقة بيضاء دافئة + لون في الرسم والجوهرة | §10 #21، §13 |
| الحفر: مسار فلاتر غائر وصفّ أرقام غائر ونوافذ الشيء الواحد على مسار رمليّ | يقرأ كثقب في الورق، وجو سمّاه «محفور» | خانات ورق ناهضة (يبقى الغائر للبئر التي تحمل صيغة تُقرأ وحدها) | §15-ج 4-ب و4-ج، §13-م (200) |
| شريط لون على حافّة البطاقة | علامة قديمة، ولون بلا معنى على كلّ بطاقة | غسلة من الركن أو جوهرة | §12 (208)، §2d |
| الكتلة العريضة المسطّحة | جدار نصّ بلا طبقات | ورقات مستقلّة بدمغة نوعها | §13-م |
| الكبسولة المصبوغة للوسم | كلّ سطح يصبغها بلونه فتتعدّد الأوجه | الشارة الواحدة `gem.css` | §15-ج 2-ز |
| الصندوق داخل الصندوق | «مربّعات في كلّ مكان» | الحاوية تخلع ورقتها؛ الغسلة الداخليّة | §13-س، §15-ب 1 |
| زرّ الرجوع الذهبيّ بسهم مكتوب | لون التوقيع يُستهلك على فعل تافه | زرّ الرجوع المشترك ورقة بصفيحة بنغمة الوجهة | §13-م (211) |
| شريط التظليل تحت جملة تلتفّ | يصير بلاطة تحت كلّ سطر | خطّ قلم قصير تحت الجملة | §13-ج (210) |
| مربّعات أيقونات ملوّنة («مجلّد ويندوز 95») | مسطّحة، ولون لكلّ مربّع | حلقة أو قناع بخطّ واحد، أو رسم مدموج | §5، §10 #9 |
| الشعار الملوّن وسلسلة الصبغ (duotone) | الألوان تخرج عن حيويّة المكان | علامة رماديّة بخطّ ذهب مرسوم | §11 (2026-07-27) |
| ألوان النشاط الزاهية v1 | صارخة | البنك الصامت | §10b |
| نموذج ملوّن بلون مختلف (تيل الأوّل وذهب الثاني) | لونان متبقّيان يقرآن ضجيجا لا معنى | نغمة القسم + رقم شبح | §10 #23، §13 |

**والقاعدة التي تجمعها:** كلّ ما سبق يعطي **عمقا واحدا لكلّ شيء** (مسطّح) أو **لونا واحدا لكلّ شيء** (بيج أو صبغة
واحدة). والنواة تعطي ثلاث طبقات، ولونا يتبع الرسم.

**ولقطات «قبل» التي فتحت هذه الجولة** (لوحة القيادة ولوحة الحساب يوم 2026-09-26 قبل 207 و208): بطاقات بيضاء متساوية على
أرضيّة رماديّة بيج سادة، وشريط لون على حافّة بطاقات الانتباه، وكلّ التبويبات بنفس الوجه. هي بعينها قائمة هذا الجدول.

---

## د. الأصول: `design-language/` (بجانب هذا الملفّ)

| الأصل | ما هو | مربوط بـ |
|---|---|---|
| `README.md` | فهرس الأصول وطريقة استعمالها في مشروع جديد | هذا الجزء |
| `core-tokens.css` | رموز النواة (ثابتة) وكتلة العائلة (تتبدّل) + وصفات `.pl-*` قصيرة | قيم `coach2.css` 164، `product.css`، `gem.css`، `dialog.css`، `record.css` |
| `prompts/station-still-life.md` | برومبت رسم القسم، متغيّراته، التنويع، الفحص | `src/assets/grid/*.webp` |
| `prompts/persona.md` | برومبت الشخصيّة: مشهد ومقصوص | `design/persona/*`، `src/assets/persona/*` |
| `prompts/blend-pipeline.md` | من الصورة إلى الصفحة: التسطيح، الضرب، الدمغة، الباليت | `tools/grid-art.py`، `tools/art-palette.py`، `tools/persona-assets.mjs` |
| `svg/icon-*.svg` | أقنعة الأيقونات بخطّ 1.9 و`currentColor` | `--ico-*` في `coach2.css` و`product.css` |
| `svg/paper-grain.svg` | حبيبة الورق | `--lw-grain` في `laws.css`، ومكتب `record.css` |
| `svg/gem.svg` `seal.svg` `pen-stroke.svg` `ghost-summit.svg` | الجوهرة، الختم، خطّ القلم، دمغة مرسومة | `gem.css`، `dialog.css`، §13، `.st2-ghost` |
| `specimen.html` | عيّنة حيّة بعائلتين من النواة نفسها | الجزء ب-3 |
| `tools/art-palette.py` | يشتقّ درجات المكتب الأربع من رسم | الوصفة 11، ب-2 |
| `prompts/gate-emblem.md` | برومبت شعار البوّابة (القمّة، ب-336) | `design/brand/gate-emblem.webp` في القمّة |
| `tools/grid-art.py`، `tools/persona-assets.mjs` | تسطيح الرسم للضرب، وأحجام الشخصيّة؛ من أدوات القمّة بحرفها، تُمرَّر لها المجلّدات وسيطا | الوصفة في `prompts/blend-pipeline.md` |
| `tools/watercolor.py` (2026-10-08) | لوحة بالحبر والألوان المائية على ورق دافئ من رسمين يرسمهما الكود (تعبئة وحبر)، وطبقة تتحرّك فوقها، وقناع الانتشار؛ بلا رصيد ومكرّرة بالبذرة | الجزء ح؛ ونسختها المرجعيّة في استوديو الإطلاق `Launching Video/tools/` |
| `grid/*.webp` | رسوم الأقسام السبعة كما شُحنت في القمّة، تحملها العيّنة | `specimen.html` |
| `examples/watercolor-v1/` | مثال الأداة مجمّدا ببصماته: المكتب بمراحله الأربع وطبقة الضوء وقناع الانتشار | الجزء ح |
| `examples/atom-capsule-v1/` | «كبسولة الذرة»: صفحة حيّة كاملة ملفّا واحدا مع صورها، أجازها جو نمطا | الجزء ح |
| `../worlds/standardshub/` | مرجعا الحركة: الجولة الميدانيّة (بناؤها وقيمها ولقطاتها الستّ) وفيلم صفحة الهبوط (12.5 ثانية) | الجزء و-6، والجزء ح |

**الأصل الخام** (رسوم جو قبل التسطيح، وملفّ خطّ ثمانية) خارج قِت بقصد: الرسم في «مراجع الشبكة»، والخطّ على جهاز جو
برخصته (§13). **وبرومبتات جو الأصليّة لم تُحفظ نصّا**، فالوصفات في `prompts/` مستنتجة من الأصول المشحونة وتعيد الأسلوب؛
وحين يولّد جو رسما جديدا ببرومبت جديد يُلصق نصّه في الملفّ نفسه تحت «برومبتات جو بحرفها».

---

## هـ. القمّة مثالا: السجلّ الكامل

ما يلي هو كيف نضجت اللغة على بوّابة القمّة وقبلها على أداة الاعتماد، بأرقام أقسامه كما يشير إليها الكود. **الأقسام §1
إلى §11 من زمن قبل الورق**: فيها ما بقي حيّا (الحركة §7، النظافة §9، ذوق جو §10) وفيها ما تقاعد (علامته عند موضعه
وسببه في الجزء ج). والأقسام §12 إلى §16 هي لغة الورق نفسها بوصفاتها وقيمها، ومنها استُخلص الجزء أ.

## 1. The canvas system (the executable layer)

> **متقاعد في 3.0:** القماش الواحد `.phc-canvas` بتدرّجه الطويل هو الأرضيّة البيج التي تذوب فيها الورقة (§13-هـ). الحيّ منه تصنيف «ورقة / تسمية عارية / كروم» و`scrollbar-gutter`؛ والأرضيّة صارت مكتبا مائيّا (الجزء أ-2، ج).

Lives in `src/index.css`. Four utilities are the law:

| Class | Role | Key values |
|---|---|---|
| `.phc-canvas` | THE page background. One per page, on the shell. | Warm paper gradient `#fefdfb → #faf7f0 → #f6f1e7` + ambient radials + 2.6% grain film |
| `.phc-card` | Blended card surface | `rgba(255,255,255,0.88)` + gold hairline `rgba(196,176,128,0.32)` + `0 12px 36px -20px rgba(74,63,46,0.28)` |
| `.phc-chrome` | Sticky bars only | `rgba(252,250,244,0.82)` + blur(14px) saturate(130%) + warm hairline |
| `.phc-lift` / `.phc-stagger` | Hover lift + entrance stagger | swim curve `cubic-bezier(0.2, 0.7, 0.3, 1)` |

The one-canvas taxonomy (LESSONS #134) governs everything: every visible surface is a **CARD**, a **BARE LABEL**, or **CHROME**. Anything else is a strip, and strips get retired, not recolored. `html { scrollbar-gutter: stable }` is load-bearing infrastructure (kills overflow-toggle layout shifts app-wide) - never remove it.

## 2. Surface tiers (pop tiers)

> **متقاعد في 3.0:** الشفافيّة 0.85 إلى 0.9 على كلّ لوح هي التصميم المسطّح نفسه. الحيّ: الظلّ الدافئ `rgba(74,63,46,…)` وحده؛ والطبقات صارت ورقا ومكتبا وورقا ناهضا (أ-2).

Translucency 0.72-0.78 is the documented "feels flat" failure. The tiers:

- **Rest card:** `0.88` + `0 12px 36px -20px rgba(74,63,46,0.28)`.
- **Dominant panel / hero:** `0.9` + tint wash + `0 18px 46px -24px rgba(74,63,46,0.35)`.
- **Nested plate (card inside a card):** `0.85` + `0 8px 24px -16/18px rgba(74,63,46,0.25)`.
- **Hover lift:** deepen to `0 24px 56px -20px rgba(74,63,46,0.42)` + translateY(-1.5 to -2px). Never Tailwind's `shadow-2xl` (cool black).

Shadows are ALWAYS in the warm family `rgba(74,63,46,…)`. A cool `rgba(0,0,0,…)` shadow on a new surface is a defect.

## 2b. Lift language for small elements - touchable rises, readable rests (2026-09-02, Qimma coach reading 2.0)

Born on Qimma's coach-reading redesign (ب-116). Jo's words: "the question boxes need to rise and not be flat, respecting hierarchy"; "many flat boxes don't clarify - they scatter"; "apply the rise to every sibling: buttons, chips, exercise tags - this is the design language everywhere." The pop tiers in §2 cover cards; this section covers everything smaller than a card.

**The rule.** Every element the user can touch rises off the paper: question-number chips, law / repeat / trap tags, part chips (كمي / لفظي), ghost and primary buttons, status pills, evidence cards. Everything the user only reads rests flat: headings, prose, hairline dividers, list rows. **Lift is a signal, not decoration - if everything rises, nothing stands out.** This is the cure for the "flat boxes" failure, which is really two failures: too many boxes, and boxes with no depth.

**Three tokens, one CSS home, prefix `--lift-`** (today scoped to the coach surfaces in `src/styles/coach2.css` under `.co`; app-wide rollout is a separate screenshot round, screen by screen):

- `--lift-chip: 0 4px 10px -6px rgba(74,63,46,.45), inset 0 1px 0 rgba(255,255,255,.85)` and `--lift-chip-hover` (deeper, same family)
- `--lift-btn: 0 10px 22px -12px rgba(14,125,134,.7), 0 1px 2px rgba(74,63,46,.1)` (primary buttons keep their teal shadow; the warm family stays for everything else)
- three quiet gradients: `--lift-teal` (`#eef6f5 → #dbe9e7`, questions and actions), `--lift-gold` (`#fbf5e2 → #f1e6c3`, badges and "after hesitation"), `--lift-paper` (`#ffffff → #f6f1e6`, neutral chips and ghost buttons)

No shadow is written as numbers at its point of use; if a surface needs lift it uses a token. Depth comes from the gradient + inner highlight + shadow, **never from a saturated hue**: a solid `#dc2626` number badge was tried and rejected the same night as "hot and loud" - the palette is the muted middle (§3, §10b).

**Hierarchy inside a lifted element is fixed:** the thing to read first in full ink and heavier weight, the facts beneath it in quieter type, the number in a badge. Never four things at one volume.

**Same thing, same color, everywhere.** A question number in an evidence card is the same question number as the chip on the end screen and the questions page - same family (`--lift-teal`). Consistency outranks emphasis.

**Duplication is measured by screenshot before build.** An element that repeats a number already visible on the same screen is removed or merged, not restyled (§10 #2): the section capsules under the time strip repeated each panel's percentage and died; the one value they carried (average seconds per question) moved into the panel head next to the percentage.

**Waiting states are a coach's desk, not an order tracker.** A vertical checklist ("your request arrived - saved for you") reads like a delivery app ("I feel like I am at a gelato store, not waiting for an important coaching session"). The doctrine: a horizontal metro line with four stations (on the desk · your turn · reading · writing), the filled segment up to the current station, only the current station speaks (one line under the line), elapsed time against a *measured* usual with the bar labelled "estimate", failure marked on the station where it stopped, and no promise the app cannot keep (no "I'll call you" - "you'll find it in your log with a *new* badge").

**Wait-screen law (2026-09-06, Qimma coach, ب-138). Percentage first, time as a corner hint, one quiet control at a
time.** On any screen where the student waits for work he cannot see, the primary signal is a **progress percentage with
its bar** - it answers "how far along" in one glance. The elapsed time is a **corner hint in meta type** opposite the
eyebrow ("1:20 · العادة نحو دقيقتين"), never a large numeral: a big running clock pulls the eye off the message and reads
as pressure, which is the opposite of what a waiting screen is for. An estimate says so with its own tag and caps itself
below completion; where there is nothing to estimate yet (queued), the bar shows position, never an invented number. The
controls are **one quiet ghost button at a time** - undo, then stop, then retry - with at most one line of meta type
under it; a costly action earns a free undo window (a thin depleting line under the button), never an explanatory card.
Same muted bank, same lift language, no new colour: a halt the student chose wears the neutral stop tone, and only a real
failure wears the alert one.

**Chips that carry words - the containment law (2026-09-10, Qimma ب-148, LESSONS #343).** A chip with a name in it
(law tag, topic tag) is never styled through a structural selector shared with its neighbours (`.co2-evv i` was written
for the 20px answer letters and swallowed the law chip: one word per line, hanging outside the card). Every chip gets
its own class; the label is one line with `white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:100%`;
and every grid/flex item that can hold long text carries `min-width:0` (columns as `minmax(0,1fr)`), because the default
`min-width:auto` lets content push the row out of its card. A chip is never a door: when a law must be opened from a question, it gets
the full law card before the answers (`قانون هذا السؤال` - name as link, rule, «افتح القانون وتدرّب عليه»), the same
card on the visit page and the questions page; a chip-sized link was read by the owner first as "the link was removed"
and then as "whitewashed" (ب-149, 2026-09-10). The coach evidence row carries no law chip at all - the laws band under
the notes is its home.
Two doors on one panel must not be twins: primary action = filled teal, large; return = gold, smaller, soft infinite
pulse (`.law-return`).

## 2c. Figure language - moved (2026-09-21)

**The drawing language for figures inside a question moved out of this guide.** Its ten rules, born here
on 2026-09-02 (Qimma ب-122 / ب-123), now live with the build layer they govern, in
`Lessons and Guides/FIGURE_AND_DIAGRAM_BUILD_GUIDE.md` §13 - one home for the taste and the build together,
so a drawing agent opens one file and not two. Nothing was cut: the section moved whole.
The question surface itself (card, choices, reveal, explanation layers, groups, resume, phone rules) keeps its
own home, `Lessons and Guides/QUESTION_CARD_BUILD_GUIDE.md`.

## 3. Palette

> **متقاعد في 3.0:** ألوان الحال المشبعة (`#059669`، `#dc2626`، `#d97706`) متقاعدة، والحكم مريميّ وطوبيّ (أ-5). الحيّ: الذهب توقيعا، والمحظورات. والباليت كلّها صارت «كتلة العائلة» القابلة للتبديل (ب-1، `core-tokens.css`).

**Structural family:**
ink `#1d3349` (titles, hero values) · body warm `#5d5a4e` / `#3f4a4a` · sand label `#a39574` (small-caps labels) · sand mid `#8a8068` · sand muted `#a39a82` · sand faint `#b9ad92` / `#c2b79a` · hairline `#e7dcc2` / `rgba(196,176,128,0.28-0.45)` · tracks `#f0ece0` / `#ece5d4`.

**Gold (the signature):** `#E5C461 → #B8912E` gradients; text gold `#97702f` / `#B8912E`.

**App ink action:** teal `#084848 → #0d6e6e` (primary buttons, tour CTA, Save).

**Semantic (matured palette - the score-capsule standard):**
Met/success `#059669` (deep `#047857`/`#065f46`, gradient `#065f46 → #10b981`) · Partial/draft `#d97706` (gradient to `#fbbf24`) · Not Met/danger `#dc2626` · N/A `#475569` on `#f1f5f9` · Pending/unscored: dashed slate.

**Forbidden in new work:** mint `#34d399` and bright `#10b981` as a text/accent color (pre-v2 register; `#10b981` survives only as gradient endpoint), indigo (one exception below), cool slate text (`#334155`/`#475569`/`#94a3b8`) outside the locked-axis and N/A semantics, Tailwind gray utility colors on new surfaces, em-dash anywhere, Eastern numerals anywhere.

**Reserved identities:**
- **Locked / archived / read-only:** the slate lock pill - `rgba(241,245,249,0.96)` bg, `#334155` text, `rgba(100,116,139,0.45)` border, lock glyph. NEVER green (green lies "success" where the meaning is "frozen"). Deliberately outside the domain colors.
- **Help:** teal glass `rgba(15,106,116,0.06)` + `#0f6a74` + the BOOK glyph - identical everywhere (Header, SA chrome, tours). Help has one face.
- **Domain colors** (`getDomainColor`) belong to chapters only. State palettes must never collide with them.

## 4. Card anatomy (the Settings architecture)

Born in the SettingsModal rebuild, now app-wide. Three zones, top to bottom:

1. **Identity header** - emblem/ring/chip + name. Pinned to the top.
2. **The gold rule** - `height: 2, borderRadius: 2, opacity: 0.6-0.7, background: linear-gradient(90deg, transparent, #E5C461, #B8912E, #E5C461, transparent)` (symmetric). Isolates identity from data.
3. **Data zone** - hero numbers, plates, bars. Variable-height content (lifecycle rows, optional sections) collects BELOW; the tops of sibling cards stay level.

**Dosage rule (Jo, 2026-06-12):** the gold rule earns its place in large cards (Settings sections, center cards, stat cards, SA/Director pair). In small repeated cards (chapter performance grid) it reads as noise - tried and removed. Gold that repeats eight times in one grid stops being gold.

**Edge-to-edge bands** (chapter headers in scoring surfaces) use the tint-wash recipe instead: `linear-gradient(135deg, ${color}1c 0%, ${color}0a 42%, transparent 75%), rgba(255,255,255,0.82-0.9)` + gold hairline border. White text on saturated gradient plates is the OLD language - gone.

**Layout integrity:** card-shaped `<button>` elements need `flex flex-col items-stretch` - the browser's native content-centering otherwise makes short cards drift downward inside grid-stretched rows (LESSONS #138). Sidebars that should bottom out level with a neighboring grid use flex stretch + `flex-1` rows, never computed heights.

## 5. Identity rings and the jewel series

> **متقاعد في 3.0:** المربّع الملوّن للأيقونة متقاعد منذ هنا؛ والحلقة باقية، والجوهرة صارت شارة `gem.css` الواحدة (أ-5).

**The ring** (icon tiles, replacing flat tinted squares): white circle, `1.5px solid {color}40-59` border, `boxShadow: 0 6-8px 14-18px -6/-8px {color}40, inset 0 0 0 3-4px {color}0f-14`. Used by: Settings gear, SA/Director pair, submissions rows, domain cards, empty states.

**The jewel** (center capsule) - one design, three sizes:
- Moderator header: emblem 30, text 14.
- Director header: emblem 28, text 14.
- SA page identity: emblem 44, text 22 (replaces any big-title + English-subtitle block).
Recipe: `rgba(255,255,255,0.82-0.85)` + `rgba(196,176,128,0.45)` border + blur(16px) saturate(130%), RTL, name in ink + ` · ` + city in gold `#B8912E`, `nameAr.replace(` في ${locationAr}`, '')`.

**Header brand position is hierarchy:** tool name CENTERED on the All Centers view; LEFT (with the center jewel centered) inside a center.

**Ghost emblem:** the center's seal watermarks its own dominant panels - absolute corner, size 170-190, `opacity: 0.05-0.06`, pointer-events none.

## 6. Hero numbers

The number is the hero; the label explains it. `font-extrabold` + `tabular-nums` + `lineHeight: 1` + `letterSpacing: '-0.02em'` on percentages. **Amended 2026-09-25 (§14, measured):** a number that sits still inside a ring takes proportional digits, because a tabular cell moved the ink of «100%» 3 px off centre; tabular stays for numbers that change under the eye (timers, live counters). Sizes: quadrant values 19px, chapter % 20px, ring % 16-24px, big counters 26-30px, row-level hero % 18px. Labels: 10px uppercase tracking-wider `#a39574` ABOVE the value. `lineHeight: 1` is what lets values grow without moving the layout. Counts in repeated rows sit in fixed-width chips (`minWidth: 38`) so they align like a table. **Verdict words** (Ready / At Risk) are set in Lora - a word is a certificate, not a number.

## 7. Motion standard

Swim curve `cubic-bezier(0.2, 0.7, 0.3, 1)` everywhere. The FLIP drop-list standard (LESSONS #133) plus the v2.6 amendments:

- **Every reveal has a conceal** (LESSONS #135): exit twin keyframe (`saConceal`), two-phase close (sweep shut → FLIP back), `forwards` + overflow clip + padding collapse inside the keyframe.
- **Smooth scroll both ways:** glide on open AFTER the FLIP settles (~520ms); on close, glide at sweep start AND settle-glide after the FLIP-back. `overflowAnchor: 'none'` on animated grids.
- **Never freeze motion mid-flight** (LESSONS #136): scroll locks defer (~520ms) until the opening glide lands; measurements use settle-polls (two consecutive identical reads), never fixed timeouts.
- `prefers-reduced-motion` short-circuits all of it, always.
- Modal entrance: `modal-in` scale(0.95)+translateY(10px) → identity, 0.22-0.25s.

## 7b. Ambient 3D layer - the cherry, never the cake (2026-07-10)

A garnish tier ABOVE the doctrine, never a replacement for it: quiet 3D-feel life (CSS 3D + canvas projection, ZERO libraries) that gives a surface its intention without ever carrying information alone. Jo's framing: professional yet engaging, never visually impairing. One ambient element per surface, waiting/landing surfaces only - a LIVE work surface (scoring inputs, editors mid-work) stays still.

**The laws (each one bought by a 2026-07-10 field-walk correction):**

- **Presentation-only, by construction.** `pointer-events: none`, `aria-hidden`, zero data paths: no `storage.*`, no sync, no handlers exported. An ambient layer that authors a write is a defect by definition (cf ERR-137/138 law).
- **One stage, not scattered popups.** Concentrate the life in ONE place near the subject (the scattered six-spot echoes were "visually disturbing"; the single scoring theater below the card was "exactly what we want").
- **FX layers own their opacity.** Never nest the life inside a watermark's low opacity - the whole bloom died under the ghost's 0.13 until aura/motes took their own layer (`amh-bloom-fx`).
- **Truthful simulation only.** Real component anatomy, real terminology (Met / Partially Met / Not Met), real colors from the one source (`getDomainColor(chapterId).primary`), real logic: a Fully Met item never generates a finding, an Enrichment proposal is ACCEPTED in a dialog before it reflects below. No fake numbers on pages that own real ones - wire the page's value via props (`nowPct={analysis?.summary?.complianceRate}`) or show none.
- **Calm rhythms - everything rests.** Play-then-rest beats infinite loops: choreographies run whole cycles (iteration count via `--amh-runs`) and stop on `animationend`, NEVER on timers guessing the stop moment (the "one paper jumped" cure); content micro-pulses (name swap ~5s) ride separate from motion breaths (~2min); shine VISITS (sheen every 10s), standing emblems do not float.
- **Cursor theater grammar** (for scripted simulations): glide (swim curve ~1s) → hover face on arrival → pointer becomes a HAND → press (scale dip) → consequence. Waiting spot lives NEAR the action; no cross-card travels.
- **Performance guards, always:** `prefers-reduced-motion` collapses to a meaningful static pose (never blank); rAF loops pause via IntersectionObserver + `document.hidden`; phone untouched by construction (`src/phone/` separate; `hidden md/lg/xl:block` guards on desktop). ONE deliberate exception (Jo's call, 2026-07-12): the phone's link sheet carries the link-pulse - CSS-only, no canvas, no rAF, one run per sheet open, reduced-motion hidden. Any future phone ambient element inherits exactly these limits.
- **Composited motion only (the 2026-07-12 pulse cure).** Ambient travel animates `transform` + `opacity`, NEVER layout properties (`left`/`top`): a layout animation repaints every frame over blurred backdrops, and the compositor-layer release at `animationend` snaps a shade shift a trained eye catches. Keep the layer alive with `willChange`, and let a traveling light DISSOLVE IN MOTION (opacity gone by ~94% of the run) - never die at the wall.
- **True WebGL (Three.js) is post-visit, calm-window, valve-gated, desktop-only.** The canvas point-cloud (~700 hand-projected points) already delivers the WebGL feel at zero bundle cost.

**Reference implementations - `src/components/heroes/AmbientHeroes.jsx` + `ambientHeroes.css` (all `amh-` prefixed):**

| Pattern | Component | Home |
|---|---|---|
| Living watermark (aura + motes + float around an existing ghost) | `HeroEmblemBloom` | Dashboard mod-hero |
| Shiny standing badge (sheen visit, no float), ONE identity across boot + chrome | `HeroAssessCrest` | `Header.jsx` + `HydrationSplash.jsx` |
| Choreographed object story (fan → bind → seal) + calm rhythm + name pulse | `HeroReportBind` | ReportEditor narrative plate |
| Metaphor with real data (plates + slats bridging the gap) | `HeroGapBridge` | GapAnalysisView hero |
| Canvas 3D point-cloud morph (؟ → ✓, glyph-sampled, hand projection) | `HeroMirrorCloud` | SelfAssessmentHome panel |
| Full scripted-cursor simulation (verdicts + Enrichment + acceptance dialog + reflect) | `HeroScoringTheater` | NewAssessmentPlate |
| Seal visit on a standing page (the sealed-deliverable intention: seal lands once, sheen visits every 10s; the matured sage/brass plate rode the same pass) | `HeroSealVisit` | CenterDashboard download dialog |
| Link pulse (the LINK's voice, everywhere a link appears: teal jewel settles + ONE light pulse travels the URL line per open, then rest; transform-composited travel + dissolve-in-motion + willChange layer kept) | inline per surface (`phn/dsk/ed` keyframe families) | PhoneEditorialView link sheet · CenterDashboard share dialog · ReportEditor /r/ dialog · ReportEditor 24h card dialog |
| Brand-jewel sheen (a standing mark's shine VISIT, the HeroAssessCrest rhythm at 10s; CSS-only `::after` sweep) | `sg-brand-icon::after` | StandardGuideView header (the guide's ONE ambient stage) |
| Doc descent into the tray (download intention; one run per open + gold-thread glow) | `HeroDocDescent` | library pattern, currently unmounted (Jo's field revision 2026-07-12 preferred B + C in the dialogs) |

Theatrical originals for taste reference: `_mockups/hero-3d-concepts.html` + `_mockups/hero-dialog-concepts.html`.

**Replication recipe:** (1) name the page's intention in one sentence; (2) prototype theatrically in `_mockups/` first; (3) Jo's verdict; (4) production cousin at HALF the drama (opacity, size, rest cycles); (5) insert as an absolute ambient layer inside the existing plate, guards on; (6) ERR-136 gates + sweeps; (7) tune by field walk - tuning knobs live as named constants (`THR_TARGET`, `REPLAY_EVERY_MS`, sheen period).

## 7c. Procedural spectacle - the data-driven singularity (2026-07-24; **SHIPPED 2026-08-25 on Qimma's landing**)

Source spark: the viral three.js "SINGULARITY" single-file piece (procedural
blackhole + generated music, zero external assets). Jo's standing verdict that
prompted this section: the youth-facing wow level (Qimma) is NOT there yet.
This section filters that spark into doctrine - what earns a place, what does not.

**What transfers (the real lessons):**

- **One gravitational centerpiece.** The piece works because ONE massive object
  owns the screen and everything orbits it - §7b's "one stage" law pushed to
  hero scale. A youth-facing landing deserves ONE living procedural object,
  not six polite garnishes.
- **Procedural-only, zero assets.** Every pixel from code (particles, trails,
  glow) - already our canvas doctrine; the wow is math, not downloads. Canvas
  2D with hand projection first (the ~700-point cloud precedent); true WebGL
  only through the §7b valve.
- **Reactive to a SIGNAL - and OUR signal is the student's truth.** Their
  driver is music FFT; ours is REAL data (amāna law extends to FX): particles
  = his answered questions, energy = his streak, orbit tightness = accuracy,
  a medal earn = the burst. The spectacle IS the progress render. A particle
  count that claims to be his questions IS his questions - no fake energy on
  surfaces that own real numbers.
- **Full-cycle choreography still rules.** A music visualizer may run forever;
  we may not: idle = low-energy breathing, full drama ONLY on events (streak,
  medal, wave delivery), then rest (§7b play-then-rest verbatim).

**What does NOT transfer:** dark-void full-screen backgrounds (identity is warm
paper - spectacle lives INSIDE it: gold/teal particles over paper, or a
contained dark viewport card like Qimma's bankpulse instrument); audio of any
kind (study app, never autoplay sound); GPU-hungry full-screen shaders on
phones.

**Qimma candidate applications (mockup-first, Jo's verdict gates each):**

| Intention | Concept | Real signal |
|---|---|---|
| Landing hero wow («سديم القمة») - **BUILT AND LIVE** (`src/components/landing/SummitCloud.jsx`) | mountain-of-light point cloud forming the summit; on the PUBLIC page the honest signal is the BANK, so each particle is a real bank question (verbal flank teal, quant flank kami-blue, summit gold) | `liveStats(progress).total`, verbal/quant split |
| Medal moment | gravity-burst: particles collapse into the wolf coin, then settle | badge-earn event |
| Wave arrival | brief particle inflow into the bankpulse instrument when a delivery lands | meta/pipeline deliveredAt |
| Break screen | calm orbital breathing behind ذيبان's tip - rest surface, lowest energy | section-break state |

**Qimma addendum to the §7b guards (phone-primary, unlike the desktop
dashboards):** frame budget <3ms mid-phone, particle count adapts via
devicePixelRatio + deviceMemory, pause on document.hidden + IntersectionObserver,
stop after N idle cycles, reduced-motion = meaningful static pose (the drawn
summit, never blank). Composited transform/opacity only.

**Recipe addition:** the mockup (`_mockups/qimma-singularity.html`) must expose
THREE switchable energy states (idle / active / burst) so the verdict sees the
full envelope, not the demo's best minute.

**What the shipped one taught (2026-08-25, the Qimma landing round).** The
production piece is `src/components/landing/SummitCloud.jsx` - canvas 2D, hand
projection, zero libraries, ~250 lines - and it validated the doctrine on a real
phone-primary surface. What was NOT obvious before building it:

- **The honest signal depends on WHO is looking.** §7c's table assumed the
  student's own numbers. A PUBLIC landing has no student, so a particle cloud
  claiming to be "his questions" would be a lie to a visitor. The signal there is
  the BANK's real question count, and the page SAYS so in a legend
  («كلّ نقطة هنا سؤال في البنك») with the split counted beside it. The rule
  generalizes: **pick the signal the current viewer actually owns, and name it on
  screen.** The canvas carries `data-particles` and `data-honest` so a test can
  assert the claim, and when the device budget forces fewer points than the bank
  holds, the legend changes its wording instead of lying.
- **Placement and animation must never share an SVG node.** A `<g>` with both a
  `transform="translate(...)"` attribute and a CSS keyframe animating `transform`
  loses the attribute the moment the animation starts - every group snaps to the
  origin. Nest: outer group places, inner group animates. (Cost this round: one
  full re-render cycle before it was seen in a screenshot.)
- **Grep the class-prefix namespace before writing the block.** ~200 lines went
  out under `.lp-*`, which the law panel already owned; the landing's number band
  rendered as blue law chips. Renamed to `.ld-*`. A new surface picks its prefix
  by search, not by initials.
- **A class an old test navigates by is an interface.** Duplicating `.place-btn`
  on the closing CTA gave the suite two nodes and killed it. One holder per
  navigational class, or the suite gets a dedicated hook.
- **Rest is cheap and must be explicit.** The cloud stops 40s after the last
  interaction, on `document.hidden`, and via IntersectionObserver - three
  independent brakes, because any one of them alone leaves a phone spinning a rAF
  loop in a background tab.
- **`prefers-reduced-motion` deserves its own test context**, not a code read.
  Playwright's `reducedMotion: 'reduce'` context proved the static pose actually
  draws (a blank canvas would have passed a naive "no animation" assertion).

**The sequencing lesson, which cost more than all the craft ones.** This surface
was built three times (rounds 12, 12-ب, 12-ج). Each build was competent and each
was reframed, because the owner's frame for a TASTE surface arrived after the
build instead of before it. For anything whose verdict is taste, get the frame
first - one sentence naming the intention, or a mockup - and only then build.

## 8. Iconography

A glyph must be the symbol the profession would recognize: LD landmark columns (governance), PC pulse line, MM capsule/pill (the anchor-lookalike was a v1 defect), LB conical flask, MIS monitor, IPC shield, FMS multi-wing facility building (not a house), MOI database cylinders. Audit any new icon against this bar; "abstract but pretty" loses to "instantly recognizable".

## 9. Typography, numerals, hygiene

Lora (English serif, titles + verdicts) · Noto Naskh Arabic (Arabic) · mono only for keys/slugs. **Western numerals (0-9) always**, even inside Arabic prose: Arabic date formatting must use the `'ar-u-nu-latn'` locale, never bare `'ar-SA'`; the sweep is `perl -CSD -ne '... /[\x{0660}-\x{0669}]/'` - WITHOUT `-CSD` the check silently passes violations (LESSONS #139). No em-dash anywhere Jo sees a string. `%` is Latin. **Display titles (since 2026-09-23):** Thmanyah Serif Display Bold with its swash letters, over the UI font as fallback, on titles only - never on body text. Its recipe, sizes, licence handling and the places the swash is turned off live in §13.

## 10. Jo's taste - the decision heuristics (هوية الذوق)

What two days of correction rounds distilled. Apply these BEFORE he has to say them:

1. **Strips get retired, not recolored.** A full-width band that isn't chrome must either become a card, become chrome, or have its contents rehomed and die.
2. **Duplication is a defect.** A "4 Centers" capsule above four visible center cards, two saved-state pills, a center name repeated under itself - remove, don't restyle. Every element must add value a neighbor doesn't already provide.
3. **Landing surfaces fit one viewport.** Jo's users don't scroll to discover. Compress one notch everywhere before inventing new layouts.
4. **The first question answered at a glance.** Non-technical directors ask "وين وصلت؟" - a decision ring or hero number answers it before any reading. Simplicity for the audience outranks density.
5. **Consistency across portals, distinction for special pages.** Moderator and director see the same language (same trays, capsules, pills, anatomies). A special surface (SA page) may stand out via composition, never via a different language.
6. **Components float, never melt** (LESSONS #134 corollary). Borders + shadow + radius stay on every functional panel; "blending" means the canvas unifies, not that edges dissolve.
7. **Tops align, variance sinks.** Within a card row, identity/data zones pin level; optional content differences collect at the bottom.
8. **Numbers earn prominence through weight, not size inflation.** lineHeight 1 + extrabold inside the same line box - the component must not grow.
9. **Old design tells:** saturated gradient plates with white text, mint greens, indigo accents, cool slate text, flat tinted icon squares, blue in-progress states, loud green status chips. Seeing any of these = the surface predates v2 and needs the treatment.
10. **He will test with his eyes.** Walk every state (empty, draft, complete, locked) before delivery; the state he finds broken is always the one not walked.
11. **[متقاعد في 3.0: ماء واحد لكلّ الصفحات صار أرضيّة بيج سادة؛ لكلّ صفحة ماؤها من رسمها، ج] One canvas, one water (2026-07-12, the guide's two-pools cure).** The app body's paper `#faf7f0` is THE canvas; a sub-surface never carries its own neutral. Two neighboring neutrals read as two pools, and every matured component over the foreign one floats like an island with strange corners. Blend the water first - each surface's identity then lives in its components, not its backdrop. Jo's phrasing: "الجميع دامج، تنفسوا مع بعض، مطبوخة مع بعض."
12. **Feedback timing: no dead clicks, no flashes - hold BOTH.** Progress chrome mounts at the click only if the work is still running after ~400ms (the show-delay); an instant result shows the result itself; a failure mounts immediately. A capsule that flashes for 0.1s is noise; a click silent for a second is a dead button (the 2026-07-12 capsule cure, `startExportCapsule`).

13. **Touchable rises, readable rests (2026-09-02).** Lift marks what can be touched; prose and headings stay flat. Many flat boxes scatter; a few lifted ones guide. See §2b.
14. **Same thing, same color, everywhere.** Emphasis never buys a new hue for something that already has one elsewhere on the screen. A number badge that turns red where its sibling chips are teal is a defect, not an accent.
15. **The muted middle.** Neither dull nor loud. Depth from gradient, highlight and warm shadow - never from saturation. Jo: "our colors are usually muted, gently, not fully dull nor screaming - the sweet middle."
16. **Waiting is part of the product.** A progress state is judged by the same voice and hierarchy as the result it precedes: horizontal, one speaking station, measured time, honest failure. A checklist of delivery-app steps is a pre-2.0 tell.
17. **A drawing is the question's picture, not an icon of its type (2026-09-02).** Every labeled given in the stem is in the figure; a shape without its numbers is "less than the description" and a defect. And the inverse: a figure that shows the answer is worse than none. See §2c.
18. **Labels sit beside lines, never on them; points are labeled where there is room.** Halo + `ltr` + perpendicular offset for sides, collision-tested quadrants for points. A number sitting on an edge is the pre-2.0 tell of a drawing.
19. **Story first, then the move (2026-09-10, Qimma coach reading).** In a diagnostic reading the narrative (what the coach saw) precedes the actionable list (which laws broke). A rule-list that opens the page before the observations reads as a table of contents, not as coaching. Jo, on seeing ب-143 live: «يجب ألّا تكون هي أوّل قراءة بعد قراءة الملخّص... تحت قراءة الملاحظات». Corollary: a placement decided in prose is provisional until it is seen on the real page.
20. **A named thing is a door, not a label (2026-09-10).** When the UI names an entity that has its own page (a law, a section, a question), the name links to that page - underlined lightly in the entity's hue, never a filled button beside it. One door per entity: the link opens the page, the page carries the action (train, review). A dead button next to a plain-text name is the tell of a capability built and never wired (the ب-140 family).
21. **Paper, not panels (2026-09-23).** Every surface a student lives on is warm paper `#fffdf8` with a warm hairline and a two-layer warm shadow; a container that holds papers sheds its own frame. Tinted gradient panels (the teal slant, the dyed gold) are now an old tell. See §13.
22. **The real asset judges the design.** Stand-in fonts and placeholder art passed every guard while hiding the defects that mattered: art crossing text, a swash breaking the longest title. A visual round closes on the owner's machine with the real files, never on the stand-in.
23. **A series is told apart by its own identity, not by color.** Nine cards of one structure get their own ghost numerals; the tone stays the station's. Two leftover colors (teal model 1, gold model 2) read as noise, not as meaning (Jo: «ما في تمييز»).

## 10b. The 2026-06-13 sweep additions (locked doctrine)

Born in the all-night v2.6 rollout across Gap Analysis, SA report, Saved
Reports, scoring, toasts, and capsules. These are now law:

- **Enrichment has ONE identity: gold.** The sparkle trigger ring, the
  Suggested Finding dialog (rail, header ring, version chip, shimmer), and
  the refine field's armed state all speak `#B8912E / #E5C461`. Violet and
  blue on any rewrite/enrichment surface are pre-v2 tells.
- **Activity colors are the MUTED set, app-wide.** `ACTIVITY_TYPES` in
  `src/lib/config.js` carries DOC `#5378A0` / INT `#5C8567` / OBS `#B5874A` /
  PER `#7E5F92` / MRR `#9C5E2F` - the same family as the PDF's
  getActivityColor, so screen and print match. The bright v1 set
  (`#3498db`...) must not return.
- **Score-capsule button standard:** unselected = white capsule, 1.5px tone
  hairline, tone text; selected = solid tone gradient + top inner highlight
  + tone shadow + scale 1.06; hover = tone tint lift. N/A stays slate.
- **Wash-from-the-rail grammar at row scale:** score/state feedback on rows
  and standard headers is `linear-gradient(90deg, tone-alpha 0%, transparent
  ~55%), #ffffff` anchored at the left rail - never a full-plate tint, never
  a vertical fade.
- **Toasts:** top-RIGHT below the chrome (top 76 / right 24), warm paper
  card + jewel-ring icon + tone rail, 5s duration. Info = teal, never blue.
- **Generation capsule:** keeps its dark accent identity; the progress fill
  is the gold gradient (one "work in progress" face with the enrichment
  chip), gold hairline edge, warm overlay tokens.
- **Scope truth:** every "full scope?" computation uses the fixed
  `APP_DOMAIN_TOTAL` universe; badges derive from saved content first
  (LESSONS #142).

## 11. Pre-delivery checklist

> **متقاعد في 3.0:** حلّ محلّها فحص أ-7. تبقى هنا سجلّا.

- [ ] Page has exactly one `.phc-canvas`; every surface is card / bare label / chrome.
- [ ] No cool-black shadows, no 0.72 translucency, no forbidden colors (§3).
- [ ] Gold rule only where the card is large enough to carry it.
- [ ] Buttons-as-cards are flex-col; rows of cards top-align.
- [ ] Every reveal has a conceal; reduced-motion respected.
- [ ] Ambient 3D layer (if any): one per surface, presentation-only, rests after playing, truthful logic + real colors, guards on (§7b).
- [ ] `perl -CSD` Eastern-numeral sweep clean; no em-dash in strings; tabular-nums on data.
- [ ] Locked = slate, draft = amber, success = mature sage, help = teal book.
- [ ] esbuild parse on every touched file; full `npm run build` on Jo's Mac before commit.
- [ ] Any drawn figure: every stem given labeled with its unit and name; no label on an edge; width ≤ 270 / height ≤ 180; construction in gold, outline in ink; nothing drawn that answers the question; new builder previewed before/after from the shelf before wiring (§2c).

---

## 11. Visual identity change — 2026-07-27 (Qimma Gate): every coloured logo removed

> **(نُسخ 2026-09-29، الجولة 256):** الشعار صار رسمة القمّة المائيّة بألوانها بكلمة جو («صورة الذيب في القمة صارت خارجة عن نموذجنا الجديد»)، مشتقّة بأداة إلى العملة (`gate-mark.webp`) والأيقونات؛ **وختم شاشة الجولة (`gate-ghost.webp`) خرج كلّه ولم يُبدَّل** («Don't replace it. We want a clean background»، ب-338). انظر §19. والباقي من هذا القسم حكمه: **لا تلوين بالفلتر**، والذهب مرسوم لا مخبوز في العملة.

Owner's ruling, verbatim: «إزالة كلّ اللوغوهات الملوّنة، واستبدالها بالمطوّرة...
الألوان كانت مزعجة وتخرج عن حيوية المكان.» This section exists because an
identity change without a record is an identity you cannot reproduce.

### What was retired

`src/assets/medal-scene.webp` — the teal night scene with a baked gold rim, used
in three places at once (app-bar coin, medallion face, run-screen watermark).
**Deleted from the repo.** With it went the whole v5 duotone chain that had been
tinting it per lane: `grayscale → brightness↑ → contrast↓ → sepia →
hue-rotate(lane) → saturate` plus `mix-blend-mode: multiply`. No `hue-rotate`,
no `sepia`, no blend mode anywhere in the emblem path now.

### What replaced it, and where the originals live

Originals (owner-generated, 1024×1024 PNG) in the project root, NOT in the repo:

| Original | Derivative in repo | Used by |
|---|---|---|
| `ghost logo or badges.png` | `src/assets/gate-mark.webp` (512², tight circular crop, greyscale) | app-bar coin (42px), medallion face (120px SVG) |
| `ghost logo or badges.png` | `src/assets/gate-ghost.webp` (radial alpha falloff) | run-screen watermark, opacity .3 |
| `new Wolf Mountain theeban.png` | `src/assets/theeban.webp` (512², background removed) | ذيبان everywhere |

**The gold is now drawn, never baked.** The medallion's rim is two SVG circles
(`#b8912e` 2.4px + `#e5c461` 1.1px) and the coin's rim is a CSS ring — so the
gold is always the app's gold and can never drift with an image swap. A data
category still gets its tone from the muted bank (§10b) **as a marker**, never as
a filled shape; and a status colour (green = correct) is never borrowed for an
identity axis — that was the specific complaint that killed the old chip row.

### Background removal on owner-generated art — the method that worked

Both PNGs arrive on a smooth grey gradient (L 147–212), **not** transparent, even
when the brief says isolated. Say so rather than shipping a grey box. Three
signals combined, and no two of them suffice:

1. **GrabCut** with a rect inset from the border → coarse silhouette.
2. **Distance from a background surface** fitted (cubic least-squares) to the
   image's 90px border ring → soft edges, fur wisps, misty base.
3. **Laplacian texture energy**, blurred σ≈4 → the discriminator that matters.
   Fur reads 70–195, mist ≈25, and the smooth AI glow beside the ear reads ≈5 —
   identical to the paper. Signals 1+2 alone left a grey slab through three
   attempts; adding texture killed it in one.

Body mask: `((tex > 16) | ((d > 32) & (sat > 35))) & grabcut`, then fill holes —
the saturation clause keeps the teal cape and gold medallion (smooth but
saturated) while excluding the neutral glow. **Fill the holes**: white fur can sit
at the exact background luminance and punch invisible gaps that only appear once
the asset lands on a coloured page.

### The life layer travels with the artwork, and must be re-measured

ذيبان's blink and ear twitch are CSS over the image (`companion.css`), so their
coordinates are **artwork-specific percentages**. On an art swap the effects are
kept verbatim and only the numbers are re-measured: eyes at 38.2% / 52.7%
horizontal and 24.6% vertical; ear-twitch crop `left:52% width:17% height:16%`
with the inner self-image at `width:588.2% left:-305.9%`. Two lid colours, not
one — the wolf's left side sits in shadow, the right in light.

Verify with a rendered sheet that forces the lids open and shut and outlines the
ear-crop box; do not eyeball it at display size.

## 2d. لطخة البوية - لغة الوسم على البطاقة (2026-09-17 ليلا، منتقي الأقسام في بوابة القمة)

**الأصل بكلمة جو من الشاشة الحيّة:** الوسم الذي يقول «هذه البطاقة من مجموعة» لا يكون حاوية ولا خيطا عريضا ولا
غسلا يعمّ البطاقة، بل **لطخة واحدة تشبه البوية أو البخاخ** في رأس البطاقة عند حافّة البداية (يمينا في العربيّة)،
تتدرّج في الشدّة وتختفي قبل ثلث العرض وفي النصف الأعلى. جو تعرّف على ذوقه فيها فورا («عرفت جوّي في التصميم»)،
فهي من الآن خيار معتمد في هذه اللغة، لا حيلة صفحة واحدة.

**القاعدة:**
- البطاقة العاديّة تحمل اللطخة نفسها بلون رقمها (التيل)، والموسومة بلون مجموعتها من البنك الصامت (§10b): البنفسج
  للأكثر تكرارا، والطوب للأقسام الحمراء. لغة واحدة يفرّق بينها **اللون لا الشكل**.
- الفرق عن البطاقة العاديّة بقدر ما يقول إنّها من المجموعة لا أكثر: خيط 1.5 بكسل على حافّة البداية، ورقم بغسل
  اللون (نحو 20%)، وكلمة الوسم بحبر اللون مع نقطة صغيرة، **بلا كبسولة**.
- المحاولة الأولى في الليلة نفسها (خيط 4 بكسل، ورقم ووسم بلون كامل، وغسل على البطاقة كلّها) رُفضت بوصفها
  «كبسولة واقفة» و«هياكل هندسيّة كثيرة»: التباين يُرفع باللطخة لا بالبنية.
- هيكل البطاقة واحد للجميع: رأس (الرقم يمينا والوسم يسارا في الفراغ الأبيض) ثمّ الاسم **سطرا واحدا** ثمّ ذيل
  (القسم يمينا والعدد يسارا)، والعرض الأدنى يتّسع لأطول اسم (240 بكسل)، فلا بطاقة أطول من جارتها.
- بطاقة «ابدأ التدريب» فعلٌ لا شرح: عنوان بصيغة الأمر، وزرّ «خذني للتدريب» بلون الفعل في طرف السطر، والبطاقة
  كلّها هي الزرّ («حسبته شرحا»).

**الوصفة (CSS):**
```css
/* البطاقة العاديّة، لون رقمها */
background: radial-gradient(ellipse 30% 65% at 100% 0%, rgba(14,125,134,.16) 0%, rgba(14,125,134,.06) 50%, rgba(14,125,134,0) 100%), rgba(255,255,255,.86);
/* الموسومة، لون مجموعتها (البنفسج مثالا) */
background: radial-gradient(ellipse 30% 65% at 100% 0%, rgba(126,95,146,.24) 0%, rgba(126,95,146,.09) 50%, rgba(126,95,146,0) 100%), rgba(255,255,255,.86);
border-inline-start-color: #7E5F92;
/* بطاقة البدء العريضة: اللطخة على الحافّة كلّها بارتفاعها */
background: radial-gradient(ellipse 22% 100% at 100% 50%, rgba(126,95,146,.20) 0%, rgba(126,95,146,0) 100%), rgba(255,255,255,.9);
```
`at 100% 0%` هي الزاوية اليمنى العليا بالإحداثيّات الفيزيائيّة، وهي حافّة البداية في العربيّة؛ في واجهة يسار-يمين تُقلب إلى `0% 0%`.

**فخّ مقيس في الليلة نفسها:** صنف `.sec` يسكنه أيضا وسم القسم في صفّ شرائح السؤال (`.chip.sec`)، فخصائص الهيكل
(flex وmin-height) تُقيَّد بحاوية الشبكة `.secs-grid .sec` ولا تُكتب على الصنف العامّ، وإلّا طال الوسم 120 بكسل في كلّ سؤال.

### 2d-2. البطاقة المطفأة في خريطة أقسام (2026-09-18، منتقي الأقسام الحمراء)

**الحال:** شبكةٌ تعرض **كلّ** أقسام مصدرٍ ما، وبعضها لم يصل البنك بعد. الغريزة أن تُخفى
الفارغة، **وهي خطأ**: الشبكة حينئذ تقول «هذي كلّ الأقسام» وهي تعرض بعضها، فيقرأ الناظر
امتلاءً لا وجود له.

**الشكل:** البطاقة تبقى في موضعها بترتيبها، وشفافيّتها `.45`، وخيط سكّتها يعود إلى لون
الخطّ المحايد (لا لون المجموعة)، **ولا ترتفع عند المرور ولا تُنقر ولا تدخل مسار التبويب**
(`tabIndex=-1` و`aria-disabled`)، وعدّادها بلون الصامت لا الذهبيّ. فالعين تقرؤها **خانةً
فارغة في خريطة**، لا بطاقةً معطوبة.

**ولماذا لا تُخفى:** «الخريطة تُري ما امتلأ وما بقي» (جو، 2026-09-18). والفارغ هنا معلومةٌ
للطالب (قسمٌ سيأتي) وللمكتب (ما بقي من العمل)، لا نقصٌ يُستر.

### 2d-3. شريط الكبسولات: القادم أعلى، والماضي أهدأ (2026-09-18)

**الحال:** منطقةٌ فوق الشبكة تحمل **فعلا واحدا قادما** (ابدأ الجولة التالية) و**عدّة آثار
ماضية** (جولاتٌ تمّت، لكلّ واحدة درجتها وسطر قراءة).

**القانون:** التفريق بين القادم والماضي **بالعلوّ والهدوء لا بلونٍ ثانٍ**. القادم بطاقة
البدء نفسها بكامل هيئتها: خيط سكّة بلون المجموعة، وترتفع عند المرور، وزرّ فعلها ظاهر.
والماضية أخفض: خيط أرقّ بشفافيّة، وورقٌ أهدأ، وبلا رفع - وسطر قراءتها مقصوص بسطرين
(`-webkit-line-clamp:2`) فلا يطول الشريط. **ولا لون سادس** (قانون عدد الألوان، ب-68).

**وما لا يدخل الشريط:** محتوى بيته في مكان آخر. الكبسولة الماضية **تفتح** قراءتها في
السجلّ ولا تنسخها فيها (قانون عدم الازدواجيّة، ب-121): تحمل اسمها ودرجتها وسطرا واحدا وبابا.

**والفخّ المقيَّد:** بطاقة البدء تلبس `sec red red-lead`، وخصائص هيكلها كانت مقيّدة
بـ`.secs-grid` عمدا (§2d والدرس 449). فحين خرجت من الشبكة إلى شريط الكبسولات **فقدت هيكلها
كلّه** ووقفت عمودا. فأُعيدت لها خصائصها تحت `.red-caps` بعينها - لا بتعميمها على `.sec`.

### 2d-4. اللسان على حافّة البطاقة، والكبسولة في الزاوية (2026-09-23، زرّا البلاغ والاقتراح في بوّابة القمة)

**الحال:** فعلٌ ثانويّ يخصّ بطاقة بعينها (بلّغ عن هذا السؤال)، وفعلٌ عامّ يلزم أن يُنال من كلّ صفحة (اقترح تحسينا)، ولا
مكان لأيّهما داخل المحتوى ولا في شريط الجوال.

**ما فشل:** علامة «هادئة» بحبر رمليّ بلا إطار داخل صفّ وسوم البطاقة، ورمزها وحده على الجوال - قرأها جو «ذائبة فيها»
ونقطةً على الجوال؛ والفعل العامّ في قائمة الترس، لا يراه من لم يفتحها. **الهدوء يُصنع باللون والحجم، لا بنزع الإطار
والرفع والاسم** (§2b، §10 #6، والدرس 528).

**القاعدة:**
- **لسان الحافّة:** جوهرة صغيرة (ورق §2b، شعرة ذهبيّة، رفع دافئ) على حافّة البطاقة العليا في زاويتها الأخرى، ثلثاها فوق
  الحافّة، فيها اسم الفعل مكتوبا، على الجوال أيضا، ثمّ حلقة هويّة (§5) بلونه. لا تسكن صفّا ولا تركب محتوى، والبطاقة
  تفسح لها فوقها وحشوةً أعلى قليلا تحتها. **وإذا كانت الحلقة علامة ترقيم فهي بحرف الواجهة وفي موضعها من الجملة:**
  «؟» العربيّة معكوسة اللاتينيّة، بعد الكلام لا قبله (جو: «برسم العربيّ في نهاية الكلام»؛ الدرس 529). **ولا وسم يزاحمها
  في زاويتها:** وسم المصدر في صفّ البطاقة غاب لأنّه «لا يضيف قيمة للسؤال».
- **كبسولة الزاوية:** للفعل العامّ على الجوال، ثابتة في زاوية سفلى لا يسكنها غيرها (مقابل رصيف المستشار)، باسمها في رأس
  الصفحة، وتنطوي إلى حلقتها إذا نزل القارئ، وتغيب إذا حضر ساكن الزاوية (ذيبان). وفي العريض جوهرةٌ بالحلقة نفسها في الشريط.
  **ومنذ 2026-09-24 (الجولة 146) الكبسولة والجوهرة على رئيسيّة التدريب وحدها** بكلمة جو: «تسكن الصفحة الرئيسية فقط في
  الجوال، وحتى في الـ desktop، ما تدخل داخل التفاصيل».
- **اللون من معنى معتمد، ولا لون سادس:** البلاغ بحبر التحذير الذي تلبسه أفعال القرار (إنهاء الاختبار)، والاقتراح بالذهب
  لأنّ الإثراء هويّته الذهب (§10b)، والاختيار داخل النافذة بالتيل. **ولا يشارك الفعلُ وسومَ البطاقة لونها:** البنّيّ للنوع
  اللفظيّ وللأقسام الحمراء، فلم يُعطَه البلاغ.
- **النافذة من الهويّة:** رأسٌ بلطخة لون الحال (§2d) وحلقة، ثمّ الخيط الذهبيّ (§4)، ثمّ بطاقات ترتفع، ثمّ كبسولتان
  متساويتان؛ وعلى الجوال ورقة من أسفل الشاشة بمقبض يُسحب. **واللطخة بحبرٍ ثقيل تخفّ:** حبر التحذير بشدّة .14 قُرئ ورديّا
  في اللقطة فنزل إلى .09، وبقي الذهب على .18.

### 2d-5. صورة البلاغ: زرّ بمشبك تحت الخانة، ومصغّرة بزرّ يشيلها (2026-09-25 في كوورك، نُقلت 2026-09-27 بالجولة 214 في بوّابة القمة)

**بكلمة جو:** «وضيف في خانة الملاحظة إرسال صورة او مرفق وياليت تقوله في الخانة الحرة وياليت ترسل لنا صورة».

- **الطلب في الخانة نفسها قبل الزرّ:** نصّ الخانة الحرّة يقول ما نريد («اكتب لنا وش لاحظت (اختياري)، ويا ليت ترفق صورة للشاشة»)، فالزرّ جواب دعوة لا فعل غريب.
- **الزرّ من الدرجة الثانية (§2b):** كبسولة ورق بخيط دافئ وظلّ تماسّ، في رأسها حلقة صغيرة (§5) بمشبك بلون التيل، واسمها مكتوب «أرفق صورة»، وحدّ لمسها 44 بكسلا على الأقلّ؛ ترتفع بكسلا عند المرور وتنضغط عند اللمس، ولا حركة مع تقليل الحركة. ولا لون جديد: التيل لون الاختيار داخل النافذة (§2d-4).
- **والمرفقة خانة بيضاء بخطّ شعر:** مصغّرة بطول 56 بكسلا لا أكثر (فلا تدفع زرّي الورقة تحت طيّ الجوال)، ثمّ سطران «الصورة مرفقة» و«توصلنا مع بلاغك/اقتراحك»، ثمّ زرّ دائريّ 40 بكسلا بعلامة × يحمرّ عند المرور. على خطّ واحد في الجوال والديسكتوب.
- **والتعثّر سطر صادق:** ملفّ لا يُقرأ صورة يقول «ما قدرنا نجهّز الصورة. جرّب صورة غيرها.» بحبر الخطأ، والختام يقول «الصورة ما وصلت، بس بلاغك وصلنا» إن لم تُحفظ.
- **وفي لوحة القيادة (§12):** وسم «صورة» بالشارة الواحدة (`gem-chip` بجوهرة التيل، `data-gem="run"`) في رأس البلاغ بجانب «عولج»/«مفتوح»، والصورة في تفصيله بإطار شعر لا يزيد على 360 في 420، والضغطة تفتحها بحجمها، وتحتها سطر يقول إنّ النظرة مقيّدة في السجلّ.

## 12. لوحة القيادة - شاشة تُدار منها البوّابة (2026-09-23، الجولة 142 في بوّابة القمة)

**السياق:** «لوحة القيادة» شاشة جو وحده: عشرة تبويبات (كانت ثمانية يوم الجولة 142) بأرقام حيّة وتاريخ وتشخيص. وقانونها من كلمته في §11-5 من وثيقة الفصل: «الـ tabs هي السرّ الذي سيجعلنا نجعل كلّ شيء نظيفا بدون unended scrolls». والشاشة من الورق نفسه لا لوحة إدارة رماديّة مستعارة.

- **الورق نفسه، والكروم ملتصق:** غلاف يغطّي الصفحة (بوّابة على جسدها) بورق دافئ واحد (§1)، ورأس ملتصق بحلقة ذهبيّة واسم وتاريخ اليوم ووقت آخر قراءة ونقطة حيّة، ثمّ شريط التبويبات ملتصقا تحته: كلّ تبويب حلقة هويّة صغيرة واسم، والحاليّ ورقة ناهضة بخطّ قاع نغمته (الجولة 208، تصل مع دمجها؛ كان كبسولة تيل ترتفع، §2b). وعلى الجوال يمرّ الشريط أفقيّا ويُرى الحاليّ كاملا.
- **شكل التبويب ثابت، ثلاث طبقات لا رابعة:** صفّ مربّعات أرقام، ثمّ رسم رئيسيّ واحد، ثمّ جدول واحد بمجموعات من عشرة (قانون المجموعات 2026-07-26). ما زاد تبويب جديد أو تفصيل يُطوى، لا تمرير.
- **المربّع:** الاسم بحبر الرمل الصغير، ثمّ الرقم بطلا (§6)، ثمّ خطّه الصغير **تحت الرقم بعرض المربّع** (كان فوق الاسم فقصّه)، ثمّ الفرق بمعناه لا باتّجاهه: زيادة الكلفة طوبيّة وزيادة الزوّار مريميّة، **جملةً بسهم مرسوم لا كبسولة** (`.gem-delta`، §15-ج 2-ز). والغائب يُكتب بسببه («التحليلات ما ردّت») لا صفرا.
- **الحال محور لون مستقلّ، بخمسة لا سادس لها:** انتبه بالطوبيّ، وراقب بالكهرمان، وفرصة بالذهب (هويّة الإثراء §10b)، وسليم بالمريميّ (معنى «صحّ» نفسه)، وبلا بيانات بحلقة أردوازيّة جوفاء. **ولا يُقرأ الحال باللون وحده:** كلمة وجوهرة دائما، في الشارة الواحدة (`.gem-chip`، §15-ج 2-ز) لا في رقاقة مصبوغة.
- **بطاقة الضوء:** غسلة بلون حالها من ركنها (`radial-gradient` من ركن البداية، الجولة 208، تصل مع دمجها؛ كانت موجة من الحافّة بشريط لون على طرفها)، وحلقة وشارة (`.gem-chip`) واسم منطقتها، ثمّ العنوان والرقم ثمّ الحكاية، ثمّ «القانون» و«التكرار» و«المصدر» سطورا صغيرة، ثمّ الباب. **القصّة ثمّ الحركة** (§10 #19).
- **ألوان الرسوم أربعة وباقٍ، مدقَّقة بمدقّق مهارة الرسم** (الوضوح والتمايز لعمى الألوان وتباين السطح): `#008c99` ثمّ `#a87400` ثمّ `#4a63c8` ثمّ `#b24e3a`، والباقي `#a39a82`، بترتيب ثابت لا يُدار. والسلسلة الواحدة بلا مفتاح (العنوان يسمّيها)، والأكثر بمفتاح.
- **نحو الرسم:** خطّ 2 بكسل ومساحته بعُشر لونه؛ عمود لا يتعدّى 24 بكسلا بطرف مدوَّر 4 وقاعدة مربّعة، وفجوة 2 بكسل بين القطع المكدّسة؛ شبكة شعريّة صلبة؛ ومحور واحد أبدا. **والزمن يمشي من اليمين** (ب-84)، **والذيل الذي لم يصل من المصدر يُظلَّل ويُسمّى** («لم يصل بعد») لا يُرسم صفرا. **وكلّ رسم له جدول توأم بزرّ**، والتلميح يُثري ولا يحجب.
- **المحور الرأسيّ:** أرقامه في هامش الرسم **باتّجاه يسار إلى يمين معلَن** (في صفحة يمين إلى يسار يمتدّ «start» إلى داخل الرسم فيركب آخر عمود)، والنصف لا يُرسم إلّا إذا صدق لفظه موضعه (سقفٌ 5 بأعداد صحيحة لا يُكتب له «3» عند 2.5).
- **الأرقام داخل الجمل العربيّة جزر يسار إلى يمين:** المال («$7.69») والمضاعف («×2.5») بين علامتي عزل، وإلّا انقلبا إلى «7.69$» و«2.5×». **والعدد بجمعه العربيّ من بيت واحد** (`plural`): «مكالمتين» و«3 أيّام» و«14 يوما» و«100 سؤال».
- **فخّان مقيسان:** `naif.css` يضع كلّ `svg` على 18 بكسلا، فكلّ رسم يحمل مقاسه في أسلوبه لا في صفته؛ **وصنفٌ مفرد يُعرَّف مرّة واحدة** (`.adm-area` كان مساحة الرسم واسم منطقة البطاقة، فورثت البطاقة شفافيّة العُشر) - وحارسه في `admin.test`.
- **اللوحة بلغة الورق (الجولة 208، ب-272؛ تصل مع دمجها):** المكتب مائيّ، ورأس كلّ تبويب هيرو بسطر بخطّ العناوين وخطّ قلم ذهبيّ وشبح رمزه بنغمته (150، .075). والإشارات والأوسمة تلبس الشارة الواحدة، والأسهم جملة بسهم مرسوم (§15-ج 2-ز)، والمبدّلات أوراق بلا حوض (وصفة 204)، والمربّعات دفتر واحد بفواصل شعرة (وصفة 180) وتلميحها على ذيلها. لا شريط لون على طرف بطاقة؛ الانتباه غسلة زاوية. الأرقام بلورا، ولا عربيّ تحت 12. والحارس `tools/admin-paper.test.mjs`، والتصوير `tools/shot-208.mjs` على التبويبات العشرة بخمسة عروض.

## 13. لغة الورق - الرئيسيّة ومحطّاتها بخطّ العناوين ورسومها (2026-09-23، الجولة 145 في بوّابة القمّة)

**السياق:** بدأت بطلب جو «ارفع الشبكة الستّ بنسخة أرقى... الخطّ العربيّ لثمانية يكون عناوين الـ Grids الستّة... رسم sketch لطيف، خلفيّة لكلّ مستطيل»، ثمّ ألحق بها لوحي القواعد الذهبية والبنك («هدول شاذين»)، ثمّ الصدر («الوحيد اللي ما ارتقى للتحديثات الأخيرة»)، ثمّ محطّة النماذج من الداخل («ما في تمييز»). ورأى الحصيلة على جهازه فقال: «التحديث على هذا النموذج يعطينا لغة تصميميّة جديدة حديثة... حدّث المستند حتى لا نكرّره في كلّ مرّة». **فهذا القسم هو تلك اللغة**: تُطبَّق على كلّ سطح يعيش عليه الطالب، ولا يُعاد شرحها في جولة. **ووصفاتها بقيمها الحقيقيّة، ورحلة ليلة 2026-09-25 التي نضجت فيها (الطبقات الثلاث، والزرّ المصبوغ الواحد، واللون من صورة القسم، وورق الألوان المائيّة)، في §15.**

**الأركان الستّة:**
- **الورقة:** كلّ سطح يعيش عليه الطالب ورقة دافئة `#fffdf8`، بحدّ شعريّ دافئ `rgba(196,176,128,.34)`، وزاوية 22 (18 على الجوال)، وظلّ من طبقتين دافئتين لا رماديّتين. والمرور يرفعها 2 بكسل ويعمّق ظلّها ويلوّن حدّها بنغمة محطّتها. **ولا ورق فوق ورق:** الحاوية التي تجمع أوراقا تُنزع حدودها وظلّها، فتجلس الأوراق على صفحة الشاشة كما تجلس بطاقات الشبكة على الرئيسيّة (محطّة النماذج، ولوح البنك داخل محطّته). والغسل الملوّن القديم على الألواح والصدر (تيل مائل أو ذهب مصبوغ) صار علامة قِدم. **والورقة تقف على مكتب لا على ورق (§13-هـ، الجولة 164):** الصفحة تحتها لون رمليّ ثابت `--desk` أغمق منها بنسبة تباين 1.08 على الأقلّ، وحدّها `--paper-edge` وظلّها `--paper-shadow` يبدأ من حافّتها؛ والورقة الطافية (إشعار، بطاقة عابرة) لا مكتب لها فيفصلها حدّها وحلقتها وظلّها.
- **العنوان:** خطّ ثمانية «عرض السيرف» العريض، **بحروفه المرسلة** (`font-feature-settings:'salt' 1`، وهي في هذا الخطّ نفسها `swsh`، مطفأة افتراضا كما تقول صفحة أسئلته)، **وتحته خطّ قلم** بلون محطّته: شريط من 60% إلى 88% من ارتفاع السطر بخُمس اللون تقريبا، ويشتدّ عند المرور. والأحجام: عنوان بطاقة الشبكة 27 (22 بين 760 و999، و20 على الجوال)، ورأس المحطّة 28 (23)، وعنوان النموذج 24 (21)، وعنوان اللوح 20 (19)، والتحيّة 26 (21). **والمرسلة تُطفأ حيث تكسر العنوان سطرين** (أطول عناوين الشبكة، والجوال تحت 380 بكسل): زينةٌ لا تُشترى بسطر. والخطّ للعناوين وحدها؛ المتن والشرائح والأرقام الصغيرة بخطّ الواجهة.
- **الرسم:** رسوم مائيّة بخطّ قلم يولّدها جو بموجّهات (الموضوع في يسار اللوحة والباقي ورق أبيض، بنغمة المحطّة)، ويسمّيها بمحطّاتها في «مراجع الشبكة» خارج قِت؛ والأداة `tools/grid-art.py` تعرف المفتاح من الاسم العربيّ، وتقصّ الرسم على حدود حبره، وتبيّض ورقه، وتحفظه ويب بي (560 لأطول ضلع، جودة 90؛ 184 كيلوبايت للسبعة). **وللرسم خانته لا يعبرها:** يسار البطاقة (البعيد عن الكلام) بعرض 34% وعمود الكلام 64%، يُحتوى فيها كاملا (`object-fit:contain`) ويُطبع على الورق بالضرب (`multiply`) فيسقط بياضه ويبقى حبره وغسلته. وعلى الجوال زاوية صغيرة خافتة (شفافيّة 0.6) تذوب من ركنها. وفي اللوح العريض عمودان: الرسم ثمّ القائمة بفواصلها، فلا فاصل يشقّ الرسم. **ولا رسم خلف قاعدة أو فقرة تُقرأ.** وبلا رسم: أيقونة المحطّة كبيرة باهتة بخطّ رفيع مكانه، فالشبكة كاملة في كلّ نسخة.
- **الرقم الشبح:** سلسلةٌ من بطاقات متشابهة البنية تُميَّز برقم كلّ واحدة، **لا بألوان عشوائيّة**: رقم كبير (170، و132 على الجوال) بخطّ العناوين ونغمة المحطّة بعُشر الشفافيّة، في الجهة البعيدة عن الكلام، مقصوص بحافّة الورقة من أسفل. **يرسمه النمط من `data-n`** (`content:attr(data-n) / ""`) فلا يدخل نصّ البطاقة، ولا يقرؤه قارئ الشاشة مرّتين (الاسم يقوله)، ويبقى في المتصفّح الذي لا يعرف النصّ البديل.
- **الاسم بماء الذهب:** اسم الطالب في التحيّة وفي سطر الجولة المعلّقة بذهب البوّابة نفسه متدرّجا كورق الذهب (`#c29b3c` ثمّ `#a67f27` ثمّ `#7a5b15`، مقصوصا على الحروف). جو طلب «لونا غريبا، ليس لونا شاطحا»: والذهب يعرفه البيت (توقيع البوّابة وأوسمتها) فلا يدخل الصفحةَ لونٌ لا تعرفه، والتدرّج يميّزه عن كلّ ذهب مسطّح حوله. ويسقط في وضع الألوان القسريّة إلى لون النصّ.
- **الشريحة الساكنة والزرّ الناهض:** سطر حالٍ (مستوى، آخر وسام) شريحةٌ مسطّحة بحدّ شعريّ، وأيقونة محطّتها في حلقة بعُشر لونها، **بلا ظلّ** لأنّها للقراءة؛ وما يُلمس (سجلّي، إنجازاتي، الدخول، البطاقات) ينهض بظلّه (§2b، §10 #13). والعدّاد شارة مرفوعة فوق حلقة زرّها تلامس حافّتها العليا ولا تنزل على رسمها، ولا تظهر بصفر.

**النغمات من سجلّ واحد لا غير** (`src/components/home/stations.js`، من البنك الصامت §10b): المستوى `#B5874A`، والنماذج `#7E5F92`، والأخطاء `#9C5E2F`، والجديدة `#5C8567`، واللفظي والكمّي `#5378A0`، والسجلّ والبنك `#0b656d`، والقواعد والإنجازات `#8a6d1f` و`#b8912e`. **سطحٌ جديد يأخذ نغمة محطّته، ولا يُخترع له لون.** وموروث زمن النموذجين (تيل الأوّل وذهب الثاني) انتهى: كلّ نموذج ببنفسج محطّته، ويفرّق بينها رقمها.

**والشريط بثلاث خانات:** البيت يمينا، والشعار في المنتصف تماما (عمودان جانبيّان متساويان `minmax(max-content, 1fr)` فلا يتراكب شيء إن ضاق العرض)، والاقتراح والحساب يسارا. و«لوحة القيادة» في قائمة الحساب لا ترس لها.

**الخطّ ورخصته (لا يُخالَف، وتفصيله في ب-215):** رخصة ثمانية بنسختها العربيّة الحاكمة تبيح التضمين في الويب «فقط كجزء من منتج مُجمّع أو مُعبّأ أو مُعمّى»، وتمنع ما يمكّن الزائر من تنزيله ملفّا مستقلّا، وتمنع التعديل والتحويل وإعادة التوزيع، ولا يُنزَّل إلّا من موقعه الرسميّ. فالملفّ على جهاز جو في `src/assets/fonts/thmanyah/` **خارج قِت**، ومكوّن البناء (`tools/lib/displayFontPlugin.mjs`) يختار منه ملفّا واحدا ويعمّيه ويضعه قطعة شيفرة كسولة (`virtual:display-font`)، والمتصفّح يفكّه في الذاكرة بلا رابط ملفّ خطّ أبدا؛ وبناء الملفّ الواحد خالٍ منه، و`tools/font-dist-check.mjs` يوقف السلسلة إن ظهر الخطّ ملفّا في المخرجات. **لا `@font-face` برابط، ولا ملفّ خطّ في `public/`، ولا استيراد للملفّ من شيفرة الواجهة.** وحين يغيب الملفّ (جهاز غير جهاز جو) تسقط العناوين إلى خطّ الواجهة بلا كسر، وتنطفئ المرسلة لأنّ خطّي الواجهة لا يحملانها.

**الوصفة (CSS):**
```css
/* الورقة، والمرور عليها */
--paper:#fffdf8; background:var(--paper); border:1px solid rgba(196,176,128,.34); border-radius:22px;
box-shadow:0 1px 2px rgba(74,63,46,.06), 0 16px 32px -24px rgba(74,63,46,.5);
transform:translateY(-2px); border-color:color-mix(in srgb, var(--st) 42%, rgba(196,176,128,.34));
box-shadow:0 2px 5px rgba(74,63,46,.08), 0 24px 44px -26px rgba(74,63,46,.6);
/* العنوان وخطّ القلم (قاعدة واحدة: .st2-mark, .m-mark, .stp-mark) */
font-family:'Thmanyah Serif Display', var(--f); font-weight:700; letter-spacing:0; font-feature-settings:'salt' 1;
background-image:linear-gradient(transparent 60%, color-mix(in srgb, var(--st) 20%, transparent) 60%, color-mix(in srgb, var(--st) 20%, transparent) 88%, transparent 88%);
/* الرسم في خانته */
position:absolute; top:14px; left:14px; width:calc(34% - 14px); height:calc(100% - 28px); object-fit:contain; object-position:left center; mix-blend-mode:multiply;
/* الرقم الشبح */
content:attr(data-n); content:attr(data-n) / ""; position:absolute; z-index:-1; left:22px; bottom:-38px; font-size:170px; line-height:1; color:var(--st); opacity:.1;
/* الاسم بماء الذهب */
background:linear-gradient(180deg, #c29b3c 0%, #a67f27 46%, #7a5b15 100%); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent;
```
`left` هنا فيزيائيّ عمدا: هو الجهة البعيدة عن بداية الكلام في العربيّة؛ في واجهة يسار-يمين يُقلب إلى `right`.

**فخاخ مقيسة في الجولة:**
- **البديل يخفي العيب الذي يهمّ:** ملفّات خطّ لاتينيّة بديلة ورسوم تجريبيّة مرّت بكلّ الحرّاس، والحقيقيّ كشف عيبين لم يظهرا قبله: الرسم عبر إلى الكلام في ثلاث بطاقات، والمرسلة كسرت أطول العناوين سطرين. **فالحكم على الشكل بالملفّ الحقيقيّ** على جهاز جو (متصفّح الجلسة على خادمه المحلّيّ)، والبديل للتشغيل وحده.
- **خاصّيّة الخطّ بين علامتي تنصيص مزدوجتين داخل نمطٍ مزدوج التنصيص تسقط بصمت**، فتبدو الخاصّيّات كلّها بلا أثر؛ والقيمة المحسوبة (`getComputedStyle`) تُقرأ قبل الحكم على خطّ.
- **الضرب يترك مربّعا باهتا** حين لا يكون ورق الرسم أبيض خالصا (قيمة 250 تعتم الورق 2%)، فالأداة تبيّض الورق قبل الحفظ.
- **كلّ ما يكبّر الصدر يمسّ حارس الشاشة الواحدة** (`e2e-home`: البيت تحت 1060 على الديسكتوب): التحيّة الأكبر والشريحتان عُوّضت من الفراغ وزرّ الدخول، فبقي البيت 1050.
- **الرقم الذي يُكتب نصّا يدخل `innerText`** فيكسر ما يقرأ نصّ البطاقة ويقرؤه قارئ الشاشة مرّتين؛ فالزخرف الذي يكرّر معلومة موجودة يُرسم بالنمط.

**حرّاسها:** `tools/home-grid.test.mjs` (الورقة، وخانة الرسم ومجموعها مع عمود الكلام، والمرسلة ومواضع إطفائها، والرقم الشبح بلا نصّ مقروء، والاسم وسقوطه، والشريحة الساكنة، ونغمة النماذج من السجلّ، والرخصة كلّها)، و`tools/font-dist-check.mjs` بعد كلّ بناء، و`tools/e2e-home.mjs` في المتصفّح. والشيفرة في آخر `src/styles/product.css` بأقسام الجولة 145 المرقّمة.

### 13-ب. الصفحات الداخليّة على الجوال: السجلّ والإجابات (2026-09-24، الجولة 146 في بوّابة القمّة)

**السياق:** لقطات جو من آيفونه بعد 145: وسم الأقسام الحمراء انحشر عمودا كلمة في كلّ سطر، والعناوين انكسرت، والأزرار العائمة غطّت الأسطر؛ وبكلمته «from scratch»، ثمّ حكمه على الصورة «رائع، واعتمد هذا». فهذه لغة الورق نفسها على صفحة قائمة طويلة، لا لغة جديدة.

- **الرأس رأس المحطّة، ولا ورق فوق ورق:** الصفحة الداخليّة تفتح برأس محطّتها الواحد (`StationShell`)، والقائمة أوراق على صفحة المحطّة بلا بطاقة تحملها. ونوافذ الشيء الواحد (الختام، الإجابات، القراءة) ثلاث أوراق ناهضة متساوية لا مسار رمليّ، ووصفتها في §13-م (الجولة 200؛ تصل مع دمجها).
- **البطاقة بمناطق مسمّاة لا بأعمدة موضعيّة:** العمود الموضعيّ عقدٌ على عدد الأبناء، والابن الزائد ينضغط في العمود المرن (الدرس 557). فلكلّ ابن منطقته (`grid-template-areas`)، والاختياريّ يسكن سطرا يُقصّ من آخره.
- **العنوان سطر وحده، والوسوم فوقه:** لا شريحة تزاحم العنوان في سطره. وكلمات العنوان التي هي وسوم (جانب البنك، اسم المجموعة) تُفرد وسوما فوقه، ونوع الشيء يُقال مرّة: إن سمّاه العنوان فلا كلمة نوع، ويبقى لونه لطخة في الركن ونقطة في سطر الوسوم (§2d). والرقاقة التي حكم بها المالك تبقى رقاقة («بمساعدة مستشارك»، الجولة 69).
- **الوسم في الذيل كلمةٌ بحبر مجموعته ونقطة**، يُقصّ من آخره فيسقط أقلّه قيمة أوّلا (اسم القسم قبل رقمه)، ولا يُحشر عمودا.
- **رقم السؤال حلقة بلون حكمه (§5):** صحّ بالأخضر، وغلط بالأحمر، ومتقطّعة بالكهرمان لبدون إجابة، فعمود الأرقام يقول من نظرة وين الغلط ووين المتروك. والحكم يُكتب في الذيل كلمة وحرفا، فلا يحمل اللون المعنى وحده.
- **الرقم الذي يصف جولة يسكن سطرها:** الفرق عن السابق في سطر المحاولة لا تحت الحلقة، وإشارته جزيرة يسار إلى يمين («+66» لا «66+»).
- **الزرّ الناهض يُصرف حيث ينتظر شيء جديد:** في قائمة من ثلاث عشرة بطاقة، ثلاثة عشر زرّا بلون الفعل لا يتميّز منها شيء؛ فالبابان بدرجة واحدة، ويصير باب المستشار ناهضا حين تنتظر قراءة لم تُفتح وحدها.
- **الطافي ينطوي في القراءة:** في صفحة تُقرأ نزولا، الطافي ينطوي إذا نزل القارئ ويعود إذا صعد أو وقف في أوّل الصفحة أو آخرها (كشريط سفاري)، والمكالمة الحيّة لا تُطوى، والصفحة تترك في آخرها فسحة بقدره. **وارتفاع الطافي له سببه:** رصيف المستشار يرتفع 96 بكسل لأجل شريط التنقّل في شاشة الأسئلة وحده، فحيث لا شريط يجلس في الشريط السفليّ.
- *(نسخها 182، §13-م: الفلاتر خمس أوراق متساوية بجواهر، لا سطر يمرّ)* ~~**شرائح الفرز سطرٌ يمرّ أفقيّا على الجوال الضيّق** بحافّة تذوب في جهة النهاية، بدل شريحة يتيمة في سطر ثانٍ؛ والهامش السالب يساوي حافّة الصفحة بالضبط (12 على الجوال)، وإلّا صار للصفحة تمرير أفقيّ.~~
- **والاقتراح يسكن رئيسيّة التدريب وحدها** (جو 2026-09-24: «ما تدخل داخل التفاصيل»)، الكبسولة على الجوال والجوهرة في الشريط العريض (§2d-4).

**حرّاسها:** `tools/record-phone.test.mjs` في البوّابة (البنية والقصّ والحلقة والعنوان والفرق والزرّ والطيّ والاقتراح، وكلّ حكم رأى نفسه أحمر بطفرة)، و`tools/e2e-record.mjs` في المتصفّح (جوالا وعريضا). والشيفرة في آخر `src/styles/coach.css` بقسم الجولة 146، والرصيف في آخر `advisor.css`.

### 13-ج. صفحة تُقرأ كرسالة: قراءة المستشار (2026-09-25، الجولة 162 في بوّابة القمّة)

**السياق:** بكلمة جو من أربع لقطات آيفون: «تطوّرت البوّابة كلّها بلغتها التصميميّة الجديدة، ماعدا هذا الجزء». والصفحة بحكمه القديم (ب-121) «رسالة من كبير إلى ابنه»، فهي لغة الورق نفسها على صفحة تُقرأ نزولا، لا لغة جديدة.

- **النغمة نغمة الشيء المقروء:** الصفحة تأخذ نغمة نوع محاولتها من سجلّ السجلّ نفسه (`t-<النوع>`، §10b)، فتكمل الصفحة جملة بطاقتها في «سجلّي». والألواح داخلها بنغمات محطّاتها: القوانين والفجوة بالأزرق، والقوّة بالأخضر الصامت، والقواعد بالذهب، وباب الأسئلة بتيل السجلّ.
- **الرأس:** وجه المستشار بهالة من نغمته لا في حلقة تقصّ كتفيه، والعين «قراءة المستشار»، واسم المحاولة عنوانٌ بخطّ العناوين (30، و25 على الجوال) وتحته خطّ قلم، والافتتاح فقرة رئيسة 17 بعد خطّ شعر يذوب من طرفيه.
- **الملاحظة ورقة برقمها شبحا** (160، و128 على الجوال) في الركن البعيد عن الكلام، لا دائرة ذهبيّة؛ وعنوانها بخطّ العناوين وخطّ قلمه.
- **الأدلّة أسطرٌ لا أوراق:** داخل ورقة الملاحظة، كلّ دليل سطرٌ يُلمس بفاصل شعريّ ويتلوّن بنغمته عند المرور، ورقمه حلقة بلون حكمه (§13-ب)، ولا ظلّ ولا إطار (لا ورق فوق ورق).
- **الخطوات خيطٌ واحد** يصل حلقاتها الذهبيّة، والحلقة ورق بحدّ ذهب لا قرص مصبوغ.
- **اللطخة لا الخيط:** كلّ لوح كان يميّزه خيط عريض على سكّته صار ورقة بلطخة نغمته في ركن السكّة (§2d)، والقواعد الذهبيّة ورقة لا غسلة ذهب.
- **الختام توقيع:** الكلمة الأخيرة بلا صندوق، وتحتها «مستشارك» بخطّ العناوين ووجهه الصغير بين خطّي شعر. رسالةٌ تنتهي باسم كاتبها.
- **والرجوع رابط صغير يسمّي وجهته**، والرصيف ينطوي وأنت نازل ويجلس في الشريط السفليّ (§13-ب)، وللصفحة في آخرها فسحة بقدره.
- **النطاق:** كلّ قاعدة تحت `.co2-page`، فالختام (`.co2.co-end`) وبقيّة أسطح المستشار لا تتغيّر.

**حارسها:** `tools/coach-paper.test.mjs` في البوّابة (النطاق، والورقة، والأدلّة أسطرا، والشبح، وخطّ القلم، والحلقة، والتوقيع، والطيّ؛ وثلاث طفرات حمراء). والشيفرة في آخر `src/styles/coach2.css` بقسم الجولة 162.

**§13-ج، إضافة (210، ب-274): الانتظار على مكتب محاولته لا على جدار بيج.** بحرف جو بلقطة انتظار القراءة: «كفشت بلاطتنا البيج القبيحة في انتظار قرادة المستشار، شوف لها حل». **والجذر عيب في اللغة لا في الصفحة:** نافذة القراءة في المحاولة ترسم صفحتها خارج غلاف المحاولة، فلم يصلها المكتب المائيّ (§13-م) وسقطت على المكتب الرمليّ الثابت (§13-هـ)، وفي الانتظار البطاقتان قصيرتان فنصف الشاشة جدار سادة.

- **الصفحة التي تُفتح من محاولة تقف على مكتب تلك المحاولة، أينما رُسمت في الشجرة.** `.co2-page` تحمل `data-f={deskOf(attempt)}`، والمكتب المائيّ محدِّده `body:not(.inrun):has(:is(.nb-page, .nb-attempt, .co2-page))` بلوحات مجموعاته الأربع. **وقسمة المجموعة ورسمها بيت واحد** (`src/components/coach/attemptDesk.js`: `ERR_KEYS` و`deskOf` و`artKeyOf`) يقرؤه السجلّ وصفحة القراءة، فلا تنحرف لوحة الصفحة عن لوحة بطاقتها. قيس بالبكسل: الورقة على أفتح نقطة في المكتب 1.16 إلى 1.20، وعلى وسيطه 1.22 إلى 1.28 (كان 1.09).
- **والجولة القائمة تبقي مكتب حارتها:** شاشة النتيجة الحيّة داخل الجولة (`body.inrun`) تفتح القراءة فوق مكتب الحارة (`body.inrun::before` في `product.css`)، فالمائيّ يُستثنى منها بـ`:not(.inrun)` ولا يغطّي الحارة.
- **دمغة الرأس رسم نوع المحاولة، دمغة بطاقتها نفسها:** `artOf(artKeyOf(attempt))` في خانة تحتويه كاملا (`object-fit:contain`، والضرب `multiply` يذيب بياض ورق الرسم، وشفافيّة .9، ومَيل −5°) في الطرف البعيد من الرأس: 120×104، و150×128 على 1000 فما فوق، و84×72 على الجوال. **وعلى الجوال (≤560) يصير الرأس ترويسة:** الوجه والعين والدمغة سطرا واحدا، والاسم تحتها بعرض الورقة فلا يعصره الرسم، والشارة إن كانت سطرا وحدها.
- **الحال تُقال مرّة في الصفحة:** حين تقولها بطاقة تحت الرأس (الانتظار، أو الدعوة بعد إيقاف) لا شارة في الرأس تعيدها، ولا سطر «ما قرأها مستشارك بعد» يناقض «يقرأ الحين». **ووجه المستشار مرّة** (حكم ب-116): الرأس يحمله، فبطاقة الانتظار بلا وجه.
- **شريط التظليل للاسم، وخطّ القلم للجملة:** الشريط (`.co2-mark`) لاسم قصير (اسم المحاولة، عنوان الملاحظة)؛ والجملة إذا التفّت صار الشريط بلاطة تحت كلّ سطر. فعنوان بطاقة الانتظار جملة بلا شريط، بـ`text-wrap:balance`، وتحتها خطّ قلم 46×4 بنغمة المحاولة (خطّ عنوان النافذة، §13-ع).
- **الزرّ تحت ما يتحكّم فيه:** على 900 فما فوق «وقّف» تحت النسبة التي توقفها (العمود 2، الصفّ 4)، لا يتيما في آخر العمود.
- **الألوان القسريّة:** لا دمغة، وخطّ القلم بلون النصّ، والمكتب لوح النظام.

**حارسها:** `tools/reading-wait-desk.test.mjs` (34، رُئي أحمر بخمس طفرات: نزع مجموعة الصفحة، وإرجاع الوجه الثاني، وإخراج الصفحة من المكتب المائيّ، وإعادة الشارة فوق بطاقة الانتظار، ومكتب أفتح من ورقته)، و`attempt-head` و`record-paper` بالمحدِّد الجديد. والشيفرة في آخر `src/styles/coach2.css` بقسم (210، ب-274)، والمكتب في `src/styles/record.css` (ج).

### 13-د. صفحة الأرقام: تبويب الختام (2026-09-25، الجولة 163 في بوّابة القمّة)

**السياق:** بكلمة جو من خمس لقطات آيفون بعد 13-ج: «نحتاج نرتقي بنفس المستوى لتبويب الختام الذي على هويته القديمة». فالختام يلبس ورق صفحة القراءة التي يفتح منها، ولغتها هي لغة §13 نفسها على صفحة أرقام.

- **النغمة نغمة نوع المحاولة** (`t-<النوع>`)، والألواح بنغمات محطّاتها: شريط الزمن وباب الأسئلة بتيل السجلّ، والمواضيع والإشارات بالأزرق، والملاحظة الأولى بالتيل والثانية بالذهب والقوّة بالأخضر الصامت، و«خذها معك» بالذهب.
- **نوع المحاولة كلمة بنقطة نغمته** لا كبسولة ملوّنة (§13-ب)؛ والمحاكاة ورقاقة «بمساعدة مستشارك» كما حكم بهما المالك.
- **العناوين بخطّ العناوين وخطّ قلمها:** عنوان الختام 28 (32 عريضا، 24 على الجوال)، وعنوانا الشريط والمواضيع 23 (20)، والملاحظة 24 (21)، و«خذها معك» 22 (20).
- **الحبر لا الصبغ:** الافتتاح فقرة رئيسة 17 بعد خطّ شعر لا صندوق غسلة؛ والبلاطات الأربع وأقسام الشريط إطارات شعريّة ساكنة بلا ظلّ (الشريحة الساكنة §13، ولا ورق فوق ورق)؛ ووسم الملاحظة والإشارة والفجوة كلمة بنغمتها لا كبسولة؛ و«قاعدتك» سطر بخيط ذهب على سكّته لا صندوق؛ والأرقام حلقات ذهب لا أقراص.
- **الملاحظة برقمها شبحا** (150، 180 عريضا، 120 على الجوال) من `data-n`.
- **الختام توقيع البوّابة:** الكلمة الأخيرة بلا صندوق، ثمّ «بوابة القمة» بخطّ العناوين بين خطّي شعر، ثمّ سطر المصدر الصغير.
- **الزرّ الناهض واحد** («قراءة مستشارك»)، والأبواب الأخرى ورقيّة كما كانت.
- **النطاق:** كلّ قاعدة تحت `.co2-endp`، والمكوّن الواحد يخدم ختام السجلّ وشاشة النتيجة الحيّة والمختبر.

**حارسها:** `tools/closing-paper.test.mjs` في البوّابة (النطاق، والورقة، والعناوين، والحبر، والشبح، والقاعدة، والتوقيع، والطيّ؛ وثلاث طفرات حمراء). والشيفرة في آخر `src/styles/coach2.css` بقسم الجولة 163.

### 13-هـ. المكتب تحت الورق: عيبٌ في اللغة نفسها لا يتكرّر (2026-09-25، الجولة 164 في بوّابة القمّة)

**العيب بحرف جو** (لقطة آيفون لصفحة «أسئلتك» بعد نشر 163): «عندك عيب في تصميمك الجديد تحتاج تنتبه له: الحاويات والتصميم لا يندمج ويذوب وما نفرّق الخلفيّة عن اللي فوقها». ثمّ: «حتى حاوية تحديث التطبيق ذايبة مع الخلفيّة... سجّل هذا العيب علشان ما يتكرّر في تصاميمنا القادمة».

**الجذر المقيس:** لغة الورق عرّفت الورقة ولم تعرّف ما تقف عليه. جسد الصفحة تدرّج من `#fefdfb` إلى `#f4efe4` على طول الصفحة كلّها، فأعلى صفحة طويلة شبه أبيض، والورقة `#fffdf8` فوقه بنسبة تباين **1.00**؛ والحدّ بثلث شفافيّة، والظلّ الطويل بانتشار سالب لا يُرى إلّا تحت الورقة. فالورقة لا تُرى لأنّها على ورق. ولم يظهر في لقطات الجولات السابقة لأنّها قصيرة تقع حيث التدرّج أغمق قليلا، وظهر على الآيفون في صفحة طويلة.

**القاعدة (لكلّ سطح يُصمَّم بعد اليوم):**
- **كلّ سطح يُعرَّف بزوجه: الورقة ومكتبها.** لا تُعطى ورقةٌ لونا دون أن يُسمّى ما تحتها ويُقاس الفرق رقما. الحدّ الأدنى هنا نسبة تباين 1.08 بين الورقة `#fffdf8` والمكتب `#f2ece0` (القائم 1.09)، ويُقاس في الحارس لا بالعين.
- **المكتب لون ثابت، لا تدرّج على طول الصفحة:** التدرّج الطويل يجعل التباين يتغيّر بطول الصفحة، فيصحّ في أسفلها ويذوب في أعلاها.
- **حدّ الورقة يُرى، وظلّها يبدأ من حافّتها:** `--paper-edge` `rgba(176,150,96,.46)`، و`--paper-shadow` = `0 1px 2px rgba(74,63,46,.09), 0 10px 26px -16px rgba(74,63,46,.36)`.
- **الطافي لا مكتب له:** إشعار أو بطاقة عابرة تطفو فوق أيّ شيء (ورقة أو صورة أو فراغ) لا يفصلها لون ما تحتها. فلها حدّ الورق الجديد، وحلقة فاصلة بلون المكتب حولها (`0 0 0 4px`)، وظلّ أعمق من ظلّ الورق الساكن لأنّها أعلى منه طبقة. **وإشعار النسخة وحده بذهب شارته في الشريط**: حدّ ذهب ولطخة ذهب وهالة تنبض كنبض الشارة، لأنّه الإشعار الذي يطلب ضغطة؛ ويسكن نبضه لمن طلب حركة أقلّ.
- **والحكم على صفحة طويلة:** لقطة الشاشة الأولى لا تكفي؛ تُصوَّر الصفحة في أعلاها وبعد التمرير، على الجوال والعريض.

**أين يسكن:** رموز `--desk` و`--paper-edge` و`--paper-shadow` على `:root` في قسم 164 من `src/styles/coach2.css`، والمكتب على الجسد حين تحمل الصفحة `.co2-page` أو `.co2-endp` أو `.co2-qp` أو `.co2-vp` أو `.nb-page` أو `.an-page`؛ والطافي في آخر `src/styles/companion.css`. **وفوقه يغلب المكتب المائيّ** حيث تُفتح الصفحة من محاولة: «سجلّي» والمحاولة منذ 182 و200، وقراءة المستشار خارج الجولة منذ 210 (§13-ج إضافة 210)؛ وما بقي على هذا المكتب السادة مقيّد في ب-274. **سطحٌ جديد يعيش على الورق يُضاف اسمه إلى قائمة المكتب، لا يُعطى مكتبا خاصّا.** والرئيسيّة خارج المكتب حتى يحكم جو (ب-227).

**صفحة «أسئلتك» على هذه اللغة (`.co2-qp`):** نغمة نوع المحاولة؛ والرأس ورقة بلطختها وعنوانه بخطّ العناوين (28، 32 عريضا، 24 على الجوال) وخطّ قلمه؛ والمرشّح سطرٌ داخل الورقة بخطّ شعر فوقه ومسار رمليّ، لا ورقة بيضاء فوقها؛ وكلّ سؤال ورقة برقمه شبحا (128، 150، 104) وحلقة بلون حكمه (§13-ب)، والقسم والوسوم كلمات بنقطة؛ والوقت وزرّ الزيارة سطر أخير على الجوال؛ والرجوع رابط في بدايته (وصفحة القراءة كذلك)؛ والرصيف ينطوي.

**حارسها:** `tools/questions-paper.test.mjs` في البوّابة (نسبة التباين رقما، ووراثة الصفحات الخمس، والحدّ والظلّ، والنطاق، والرأس، والمرشّح، والبطاقة، والطافي وإشعار النسخة؛ وخمس طفرات حمراء).

### 13-و. زيارة السؤال: السؤال ورقة، والحكم بنبرة الورق، والحلّ ورقته الثانية (2026-09-25، الجولة 165 في بوّابة القمّة)

**السياق:** بكلمة جو من لقطتي آيفون لسؤال مزور من «أسئلتك» بعد 13-هـ: «حاوية السؤال نفسه خارج التصميم والهويّة، الخيارات تحسّها فلات، واللون الأخضر والأحمر مزعج في الدرجة، تطوير الجزء الإثرائي وتحسين التراتبيّة ووضوح الخطّ بدون تغيير بالحجم، ثمّ آخر الصورة اللي هو مؤشّر التقرير». فهي لغة §13 نفسها على صفحة سؤال واحد.

- **السؤال ورقة على المكتب** بنغمة نوع المحاولة (`t-<النوع>`)، ورقمه شبحا في الركن البعيد أسفل الورقة، وترويسته حلقة بلون حكمه (§13-ب) والقسم والحكم والوسوم كلمات بنقطة.
- **الخيار بلاطة لها عمق لا صفّ مسطّح:** تدرّج ورق خفيف من أعلى، وإضاءة علويّة داخليّة، وظلّ تماس قصير؛ والحرف حلقة. **وهي للقراءة فلا تنهض عند المرور** (§2b): العمق هنا سماكة الورق لا دعوة إلى لمس.
- **الحكم بنبرة الورق، والفرق يبقى من نظرة:** ألوان الحالة المشبعة (`#059669` تشبّعه 0.93، و`#dc2626` 0.72) مزعجة على الورق الدافئ؛ فالصفحة التي تعرض حكما كثيرا تعيد تعريف `--co-ok` و`--co-bad` وغسلتيهما على نطاقها بنبرة أهدأ (مريميّ `#3f7354` وطوب `#a8483f`، تشبّع تحت 0.4 و0.5)، فيسري الرمز الواحد في الخيارات والكلمة وحلقة الرقم وأعمدة الشريط معا. **وكلمة الحكم تُقرأ على غسلتها بنسبة 4.5 على الأقلّ**، ومعها علامة مرسومة بالحدود (✓ للصحيحة، × للغلط) فلا يحمل اللون المعنى وحده.
- **الحلّ ورقته الثانية، لا صندوق داخل السؤال:** قانون «ورقة المعرفة» (07-26: الإثرائيّ معزول عمّا فوقه بلغة أخرى) وقانون «لا ورق فوق ورق» يلتقيان بأن يكون الحلّ ورقة شقيقة تحت السؤال على المكتب نفسه، برقّ دافئ ولطخة ذهب في ركن السكّة. **والتراتبيّة داخلها بالبنية لا بالتكبير:** الفكرة رأسها يفصلها خطّ شعر، والخطوات خيط ذهب، والمصدر توقيع أسفلها. **ولا رمز تعبيريّ في لافتة** (سقطت صاعقة الزبدة).
- **الإثراء حاويات مميّزة بدمغة، وعناوينه بأيقونات (حكم جو الثاني 09-25: «حاوياته يجب أن تكون مميّزة وتتميّز بدمغة بالطرف أحد الزوايا قريدنق... والنقطة في العناوين إس في جي صغير احترافيّ يحمل فكرة الفقرة»):** أوّل بناء جعل الزبدة والخدعة والاقتباس أسطرا بسكّة فذابت في الورقة، ورُفض. فكلّ واحدة حاوية بنغمتها `--et` (ذهب للزبدة، وطوب للخدعة، ورمل للاقتباس): ورقة فاتحة بحدّ من نغمتها وظلّ تماس، **ودمغة في ركنها البعيد عن العنوان** تدرّج شعاعيّ يذوب في الورقة وفوقه أيقونة الفقرة كبيرة باهتة مائلة. والعنوان يحمل الأيقونة نفسها صغيرة (17 بكسلا) بلونه: مصباح للزبدة، ومثلّث تنبيه للخدعة، وفقاعة كلام للمدرّس، ومفتاح لـ«الحلّ»، وميزان لـ«قانون هذا السؤال». الأيقونات أقنعة إس في جي مضمّنة تُصبغ بـ`currentColor`، لا ملفّات ولا رموز. **وأيقونة وسط سطر عربيّ لا تشبه حرفا ولا رقما:** الصنّارة قُرئت «ل» وعلامتا الاقتباس قُرئتا «55»، فاستُبدلتا قبل التسليم.
- **الوضوح بلا تكبير:** حين يطلب جو وضوح الخطّ «بدون تغيير بالحجم» فالأدوات هي الحبر (المتن بحبر كامل، والباهت أغمق درجة ويُقرأ على الورق بنسبة 6 على الأقلّ) والوزن (المتن 500) والتنفّس؛ ولا `font-size` على نصّ المحتوى في القسم كلّه، والحارس يعدّها.
- **المؤشّر ورقة ثالثة:** عنوانان بنغمة المحاولة، وأسطر بخطّ شعر لا متقطّع، وأقسام الشريط إطارات ساكنة (§13-د)، وسؤال الصفحة في الشريط بحلقة حبر لا بسطوع.
- **والتنقّل:** الرجوع رابط يسمّي وجهته، والسابق والتالي مسار رمليّ واحد في آخر السطر لا ثلاثة أزرار بعرض الجوال، والرصيف ينطوي ويجلس في الشريط السفليّ.
- **والرصيف يُسحب (جو: «نزّلها تحت... وخلّها قابلة للسحب في المكان اللي تريده»):** في كلّ الصفحات، إزاحةٌ عن ركنه الأصليّ تُقصّ داخل الشاشة بهامش 8 وتُحفظ على الجهاز، وتقرؤها خاصّيّة `translate` وحدها فلا تصطدم بـ`transform` الطيّ. اللمسة تبقى نقرة حتى ستّ بكسلات، والنقرة التي تختم سحبا تُبلع.

**حارسها:** `tools/visit-paper.test.mjs` في البوّابة (النطاق، والورق، والحلّ شقيقا، والبلاطة، وتشبّع الحكم وتباين كلمته رقما، والعلامة، والحاويات ودمغتها وأيقوناتها، ولا حجم خطّ، والمؤشّر، والطيّ، والسحب وقصّه وحفظه؛ وثماني طفرات حمراء). والشيفرة في آخر `src/styles/coach2.css` بقسم الجولة 165 تحت `.co2-vp` وحده.

**§13-و، إضافة (178): ورقة السؤال مكوّن واحد.** أجزاء السؤال بعد الكشف (الخيارات بحروف حلقات ووسوم مرسومة، وبطاقة القانون بسكّة وميزان، وورقة الحلّ الثانية بمفتاحها وإثرائها) مكوّنات في `QuestionCards.jsx` (`ChoiceList` و`LawCard` و`SolutionSheet`)، وشكلها قاعدة واحدة تحت `:is(.co2-vp, .co2-pq)`. أيّ سطح يعرض سؤالا مكشوفا يستعملها ولا يكتبها. ونبرة الحكم الهادئة (مريميّ `#3f7354` وطوب `#a8483f`) رمز واحد لكلّ صفحات الإجابات، ولا تُعرَّف مرّة ثانية.

### 13-ز. لوحة بنظرة: دليل يُرى لا يُقرأ، ووسم لا يسكن ركن غيره (2026-09-25، الجولة 166 في بوّابة القمّة)

**بكلمة جو من لقطتي آيفونه للدليل:** «مبالغ فيها، تفاصيل كأنّها مقال!! الهدف لوحة وحدة شريحة جميلة بتصميمنا، كويك تور على المزايا بنظرة وحدة»، و«علامة الاستفهام تغطّي على التايمر في المكالمة الحيّة وصعبة الضغط».

- **الجولة السريعة لوحة لا مقال:** عنوان بخطّ العناوين وخطّ قلمه، وسطر واحد يقول كيف تبدأ، ثمّ شبكة بلاطات (ستّ: عمودان على الجوال وثلاثة على العريض)، كلّ بلاطة أيقونة في حلقة وما يسوّيه في خمس كلمات على الأكثر وعبارة واحدة، ثمّ سطر ذيل والزرّان. **تُرى كاملة بلا تمرير على 360**، والورقة السفليّة بطول محتواها لا بطول ثابت. ولا مطويّ ولا أقسام: ما يحتاج شرحا طويلا مكانه غير الجولة السريعة.
- ~~**النافذة الطافية مكتبٌ لبلاطاتها:** لونها `--desk` والبلاطات ورق بدمغة~~ **نسختها الجولة 201** (بكلمة جو «تفقد الروح الجديدة بوضوح»): البلاطات صارت مربّعات في كلّ مكان، فالقشرة ورقة القرار والفقرات بلا إطار (البند الأخير أدناه).
- **ما يخصّ مكان الطالب يُضاء ولا يُنقل:** البلاطة التي تخصّ غرفته الآن بحلقة بلون المستشار، والترتيب ثابت فتُحفظ الخريطة بالعين.
- **الوسم الصغير لا يسكن ركن غيره، وهدفه 44:** شارتان على ركنين لعنصر واحد تتراكبان متى اختلف اتّجاه إحداهما (العدّاد `direction:ltr` قلب ركنه). فالعدّاد يتوسّط أعلى الكبسولة، والوسم أسفلها جنبها من جهة وسط الشاشة **لاصقا بالدائرة لا بعيدا عنها** (حكم جو بعد الصورة: «الوقت يكون فوق... علامة الاستفهام جنب اللي تحت... ما تكون بعيدة كثير عن الدائرة»؛ ونسختي الأولى رفعته فوقها فرُدّت). وما يُلمس هدفه 44 وإن كانت حلقته المرئيّة 34.

**حارسها:** `src/core/advisor/guide.test.mjs` (§1 و§8: ستّ بلاطات قصيرة، والقشرة لؤلؤ والفقرة بلا خلفيّة ولا حدّ وجوهرة واحدة (201)، والورقة بطول محتواها، وهدف 44، والوسم أسفل الدائرة لاصقا بها، والعدّاد في منتصف أعلاها؛ وخمس طفرات حمراء). والشيفرة في `src/styles/advisor.css` بقسم 166 ثمّ 201، ولقطاتها `tools/shot-201.mjs`.

- **لوحة تعريف داخل نافذة (الجولة 201):** قشرة ورقة القرار (§13-ع) وفقرات على اللؤلؤ بلا إطار، لكلّ فقرة قرص لؤلؤ ناهض برسمها، واللون جوهرة واحدة لما يخصّ الطالب الآن. **والزرّ العائم الصغير** ختم الورقة مصغّرا (قرص لؤلؤ وجوهرة النغمة)، وعرضه في التخطيط ثابت والجوهرة رسم.

### 13-ح. لحظة القيمة: ما يُكسب يُحتفل به ورقا لا لونا (2026-09-25، الجولة 168 في بوّابة القمّة)

**بكلمة جو بعد أوّل كود فعّله:** «الآن بعد تفعيل الكود، الحمد لله نجح... لكن نحتاج أن نعطيها فعلًا صبغة قيمة. يعني أنت لما تأخذ كود، يجب أن تشعر بقيمة ما أخذته. فيخرج له المستشار مع تهنئة، مع ألعاب نارية بسيطة، وscaled برضو على screen الجوال بحيث ما تكون أكبر من اللازم... لازم كلها قيمة، مو مجرد highlight أخضر.»

- **النجاح الذي له قيمة لحظةٌ لا سطر ملوّن:** غطاء مكتب رمليّ (`--win-desk` `#ece3cf`، والورقة فوقه بنسبة يقيسها الحارس وحدّها 1.08)، ووجه المستشار بحلقة ورقه وفقاعة باسمه ذيلها إليه، ثمّ ورقة ما كُسب: عين صغيرة بختم مرسوم (حلقة بشرشورتين وعلامة، لا حرف ولا رقم)، والاسم بخطّ العناوين وخطّ قلم بنغمة ما كُسب، والتاريخ بطلا بخطّ لورا، والمزايا بعلاماتها، وزرّ أوّل بنغمته وثانٍ ورقيّ.
- **الاحتفال خفيف ومقاس:** رشقات إس في جي بألوان البنك الهادئ في شريط **فوق** الكلام لا عليه، ارتفاعه يتبع عرض الشاشة بسقف (`clamp(78px, 22vw, 124px)`)، رشقتان ثمّ تنطفئ، ولا تلتقط لمسة، وتغيب كلّها لمن طلب تقليل الحركة. والصندوق `min(440px, 100%)`.
- **وما يبقى بعد اللحظة ورقٌ بنغمة ما كُسب** (سطر بختم وحدّ وظلّ)، لا الأخضر: الأخضر لون حكم (صحّ)، لا لون مكسب.

**حارسها:** `tools/code-win.test.mjs`. والشيفرة في `src/styles/gate.css` قسم (7).

### 13-ط. رسالة المستشار فقاعة كلام لا ورقة مستطيلة (2026-09-25، الجولة 169 و169-ب في بوّابة القمّة)

**بكلمة جو من لقطة ورقة 151:** «تكون فعلا كأنها رسائل... بفقاعات كلام... أما هذا الشكل المستطيل، هذه علامة النسخة القديمة.» **ثمّ قبل النشر (169-ب):** «أخرج من موضوع الشكل الهندسي مستطيلات... الـ bubble المعروفة حقت الكاريكاتير... بشكل أنعم وليس بشكل كأنه غيمة... واجعل لها هويتها الخاصة.»

- **هويّتها الخاصّة لا هويّة التهنئة:** فقاعة كاريكاتير ناعمة، زواياها 28 (24 على الجوال)، وحدّها ذهبيّ `rgba(184,145,46,.5)` بسمك 1.5، وورقها `#fffcf4` بتوهّج ذهبيّ دافئ من زاويتها، وذيل منحنٍ مرسوم (`svg`) يخرج نحو وجه المستشار في حلقته خارجها. فقاعة التهنئة (§13-ح) باقية على ورقها، والسؤال هل تتبع هذي مفتوح في ب-232.
- **لا اسم مؤلّف على الشاشة، بل أيقونة فكرة:** حلقة ذهبيّة 34 (30 على الجوال) بإحدى تسع أيقونات خطّيّة تحمل فكرة النصيحة (مصباح، تقويم، هدف، ورقة، قطرة، هلال، برعم، عين، مفتاح)، ولا أيقونة تشبه حرفا أو رقما. ونصّ النصيحة لعبة ذهنيّة لا توجيه.
- **الأزرار على الحافّة لا داخل الفقاعة**، كالاستفهام والساعة على كبسولة المستشار (§13-ز)، فلا تكبر الفقاعة بها: X شارة 34 في الزاوية العليا، و«حفظ» شريطة ذهبيّة مقصوصة الذيل على الحافّة العليا تمتلئ حين تُحفظ، والإبهامان شارتان 34 على الحافّة السفلى، الموافق يمتلئ مريميّا `#3f7354` والرافض طوبيّا `#a8483f` (§13-و). وكلّ شارة هدفها 44 بحاشية غير مرئيّة (`::after` بـ`inset:-5px`).
- **الفقاعة لا تغطّي شيئا:** تحجز ارتفاعها في قاع الصفحة (`--tip-h`، ومعه حاشية الشارات)، ويرتفع فوقها ما يلتصق بالقاع؛ وفي عمود الجولة على العريض ينزاح العمود عنها؛ والهامش الواسع بيتها إن اتّسع لها. **ولا تظهر في البيت**: مكانها الأسئلة والاستراحة والختام.
- **الاسم «خلّك ذهين» والمستودع «مستودع الذهانة» (169-ج):** كبسولة الاسم ورق صغير 28 على الحافّة العليا، وشريطة «حفظ» بجنبها تنصرف بعد الحفظ فلا يبقى وسم «محفوظة». وعلى بطاقة السؤال في التدريب المباشر لسان ذهبيّ «خلّك ذهين» بحلقة فيها شرارتان، في الزاوية المقابلة للسان «مشكلة في السؤال» وبهندسته نفسها (ثلثاه فوق الحافّة، ولمسته 44)، يفتح المستودع. ومن السؤال تحمل الورقة ذيلا ملتصقا بقاعها فيه «رجّعني للسؤال» بورق وحدّ تيليّ وسهم، في الزاوية البعيدة عن النصائح (169-د).
- **ورقة المستودع لوحة واحدة تُفتح من «سجلّي» ومن لسان السؤال:** شريط ورق فيه أيقونة الفكرة وعدد المحفوظة، ثمّ النصائح بأيقوناتها على ورق أدفأ، ولكلّ واحدة البوكمارك نفسه يشيلها. على الجوال ورقة سفليّة.

**حارسها:** `src/core/companion/tips.test.mjs`، والشيفرة في `src/styles/tips.css`.

### 13-ي. صفحة الاختيار: منتقي الأقسام والمواضيع (2026-09-25، الجولة 170 في بوّابة القمّة)

**بحرف جو** (لقطة آيفون لـ«تدرّب كمي بالمواضيع»): الزرّان «فلات قديمة... ذائبة في الخلفية محد يقدرها»، والفلاتر «شكلها المزحوم» تترتّب «بلغة ثيم خاصة قريبة من صورتها في الصفحة الرئيسية»، و«الصورة للكمي تكون قوست في رأس القسم»، و«المواضيع مستطيلة المفروض تكون مربعات».

**القاعدة (لكلّ صفحة يختار منها الطالب من شبكة):**
- **الرأس ورقة واحدة تحمل هويّة القسم:** رسم القسم نفسه من بطاقته في الرئيسيّة شبحا في الجهة البعيدة (32%، شفافيّة 0.34، بالضرب، مذابا من ركنه)، والعنوان بخطّ العناوين وخطّ قلمه في عمود 66% لا يعبر إلى الرسم. ولا رسم خلف الفلاتر.
- **الزرّ في الرأس ورق ناهض لا رابط:** 46 ارتفاعا، وحدّ الورق، وظلّ تلامس ثمّ عمق، ويرتفع 1.5 عند المرور على أجهزة المرور وحدها. وأيقونته لا تشبه حرفا، ولا يحمل رمزَ وجهة أخرى على الشاشة نفسها (بيت الشريط للهبوط، فزرّ الرجوع للشبكة بأيقونة الشبكة).
- **الفلتر خانات ورق ناهضة من عائلة زرّي الرأس، لا مسار محفور ولا حبوب ملوّنة (176-ب):** بعد خطّ شعر، والخانات تقف على الورقة بفجوة 10 بلا حوض غائر، وكلّ خانة ورقة بتدرّج زرّ المكالمات وظلّه، فيها جوهرة 30 بنغمة مجموعتها (حلقة بغسلة النغمة ونقطة بحدّها) ثمّ اسمها ثمّ عددها سطرا ثانيا. **المختارة ورقتها بغسلة نغمتها من ركنها وخطّ نغمتها في قاعها وجوهرتها معبّأة، لا تعبئة للخانة**. (نسخت المسار الرمليّ الغائر بكلمة جو: «حاوية الفلتر غير جيدة أبدا وتختلف عن بقية الحاويات، نظام الحفر سيء ولا يليق لذوق التصميم، غيره اقتباسا من هويات المؤشرات».) وعلى الجوال خانتان في الصفّ، **والمسار ذو الخانات الثلاث بالضبط صفّ واحد بثلاثة أعمدة** (174؛ القاعدة القديمة «الوحيدة في آخر صفّ تأخذه كلّه» نُسخت). والمحور التابع مفتاح صغير أهدأ تحته.
- **العنصر القليل الحقول مربّع:** اسم وعدد لا يستحقّان مستطيلا عريضا، فالبطاقة `aspect-ratio:1/1` **ومعها عرض صريح `width:100%`** (174: سفاري لا يمدّ عنصر شبكة له نسبة، §15-د 11)، رقمها شبح من `data-n`، واسمها بخطّ العناوين وخطّ قلم بنغمة مجموعتها، وذيلها في القاع مهما طال الاسم، وعمودان على الجوال.

- **ذيل المربّع يحمل ما يفرّق فقط:** كلمة تتكرّر على كلّ مربّع في الصفحة («كمي» على كلّ موضوع في صفحة الكمي) لا تفرّق شيئا، فتُحذف ويأخذ العدد مكانها في أوّل السطر (بحرف جو: «لا داعي لكلمة كمي أو لفظي، زيادة بلا قيمة، وانقل رقم الأسئلة مكانها»). ويبقى في الذيل ما يختلف من مربّع لآخر فقط (رقم القسم مثلا).

**وعلى الدسك توب (176، بحرف جو بلقطة «تدرّب لفظي بالأقسام»: «شكل الصفحة كأنه مخفور مع الخلفية الصامتة غير الحيوية... القريدز مربعات صغيرة في مساحة عريضة، خلوها اعرض... الحاويات للفلاتر غير متوازنة بصريا بمساحاتها»):**
- **المكتب ورق مائيّ لا لون صامت:** `body:has(.pk-page)` بلون قاعدة الصفحة، و`::before` ثابت على الشاشة كلّها (`position:fixed; inset:0; z-index:-1`) بطبقات الوصفة 11 من ألوان صورة القسم نفسها (§15-ج)، في كلّ العروض. فالوصفة لم تعد لصفحات السؤال والقوانين وحدها.
- **البطاقة أعرض من طولها على 1000 فأعلى:** `aspect-ratio:16/9` في أعمدة `minmax(320px, 1fr)` بفارق 18، والاسم 25 بسطرين أقصى، والرقم الشبح 150 في الجهة البعيدة. والمربّع يبقى للجوال. وعلى 1500 فأعلى يرتفع سقف العمود لهذي الصفحة وحدها (`.wrap:has(.pk-page){ max-width:1500px }`) فتصير أربعا في الصفّ لا ثلاثا تسبح في فراغ.
- **خانات الفلاتر أعمدة متساوية على عرض الورقة كلّه، وكلام كلّ خانة في وسطها:** `repeat(n, minmax(0, 1fr))` و`justify-content:center`. أوّل محاولة كانت خانات بعرض ثابت (212) في بداية المسار، فبقي ثلثه فارغا وهو عين «غير متوازنة»؛ المسار يُقسم بالتساوي لا يُحشى من طرف.
- **رسم الرأس بثلث عرضه ذائب في الورق:** شفافيّة كاملة، والضرب (`multiply`) في ورق الرأس المائيّ، **وعزل `.pk-top` يُرفع على العريض (`isolation:auto`)** وإلّا ظهر بياض الصورة مربّعا (§15-د 12). والعنوان وسطره وزرّاه في 62% لا يعبرون إليه.
- **نهوض خفيف:** البطاقات ترتفع 10 بكسل بتدرّج .04 ثانية (الوصفة 14)، **وملء الحركة للخلف فقط (`backwards`)** كي لا تحبس رفعة المرور، وتُطفأ مع تقليل الحركة.
- **العدّاد والرقم الشبح في زاويتين متقابلتين، و«القسم N» محذوف (176-ب ثمّ 176-ج):** بحرف جو: «الأرقام باللفظي فوق بعض، انقل واحد منهم للزاوية المقابلة»، ثمّ بعد اللقطة: «ممتاز، هذا التصميم المطلوب... القسم واحد في الزاوية السفلى يمين زائد، والرقم موجود... انقل الرقم 13 من 13 إلى الزاوية السفلى يمين». فالذيل للعدّاد وحده في الزاوية السفلى الأولى (يمين في العربيّ، `justify-content:flex-start`)، والرقم الشبح في الزاوية السفلى البعيدة، ورقم القسم يبقى لقارئ الشاشة في اسم البطاقة (`aria-label`). والقاعدة العامّة: **كلمة تكرّر ما يقوله الشبح لا تفرّق شيئا فتُحذف** (امتداد ذيل 170). وجُرّب في الطريق نقل الشبح إلى الأعلى فرُدّ (الرقم الثلاثيّ يصطدم بالاسم)، ثمّ العدّاد في الأعلى فقبله جو شكلا وأنزله إلى القاع.
- **قيس:** 357×201 لكلّ بطاقة على 1280 و1440، وأربع 354×199 على 1920، والورقة على مكتبها 1.22 إلى 1.44، والجوال 390 و430 كما في 174.

**رحلة التعديل كما جرت (مرجع للبناء القادم):**

| الخطوة | ما كان | ما صار | منطقه |
|---|---|---|---|
| 1. الصفحة | بطاقة بيضاء على جسم أبيض | ورقة على المكتب الرمليّ (§13-هـ) | الحاوية تنفصل عن مكتبها بفرق مقيس، فلا تذوب |
| 2. الرأس | عنوان عاديّ بلا هويّة | رسم القسم من بطاقته في الرئيسيّة شبحا، والعنوان بخطّ العناوين وخطّ قلمه | الصفحة تعرّف نفسها بالصورة التي عرفها منها الطالب في الرئيسيّة |
| 3. الزرّان | حبّة لافندر مسطّحة ورابط عاديّ | ورق ناهض بظلّين، وسمّاعة للمكالمات وشبكة للرئيسيّة | الزرّ يُرى زرّا من ظلّه، والأيقونة تقول وجهتها ولا تشبه حرفا (السيقما قُرئت حرفا فحلّت محلّها السمّاعة) |
| 4. الفلاتر | حبوب ملفوفة مزحومة، والمختارة معبّأة بالطوبيّ | مسار رمليّ بخانات: نقطة ثمّ اسم ثمّ عدد، والمختارة ورقة ناهضة بخطّ نغمتها | التمييز بالارتفاع لا بالتعبئة، فلا يبتلع اللون الصفحة |
| 7. الفلاتر (176-ب) | مسار رمليّ غائر تختلف حاويته عن بقيّة الصفحة | خانات ورق ناهضة بجوهرة نغمتها، من عائلة زرّي الرأس | الحفر لغة المكتب لا لغة ما يُلمس؛ ما يُختار منه يلبس هويّة الأزرار التي بجانبه |
| 8. الأرقام (176-ب، 176-ج) | العدّاد في القاع فوق الرقم الشبح، و«القسم N» في الزاوية الأخرى | العدّاد وحده في الزاوية السفلى الأولى، والشبح في المقابلة، و«القسم N» محذوف | رقمان في زاوية واحدة يقرآن رقما مكسورا، والكلمة التي يقولها الشبح زيادة |
| 5. المواضيع | مستطيلات عريضة بمربّع رقم أخضر | مربّعات ورق برقم شبح واسم بخطّ العناوين | اسم وعدد لا يملآن مستطيلا، والمربّع يسع الشبكة القليلة |
| 6. الذيل | «كمي» + العدد | العدد وحده في أوّل السطر | ما لا يفرّق بين مربّع ومربّع لا يستحقّ مكانا |

**وقبول جو بحرفه بعد اللقطة الأخيرة:** «هذي اللغة المطلوبة والكمال في فهم منطق التصميم». فالمنطق الذي قُبل ثلاثة: **الحاوية تنفصل عن مكتبها** (ورق على رمل، وظلّ)، **والعنصر يتميّز بالارتفاع لا بالتعبئة** (المختار ناهض بخطّ نغمة)، **وكلّ كلمة على الشاشة تفرّق شيئا** (ما يتكرّر على الكلّ يُحذف). وأيّ صفحة اختيار قادمة تُبنى على هذه الثلاثة قبل أن يُكتب لها سطر.

**فخّ مقيس:** `.sec span` في الطبقة الأولى ابتلع علامة الاسم الجديدة فصغّرها إلى 12 وبهّتها؛ العنصر الملفوف حديثا يُصفَّر صراحة ويُحرس.

**أين يسكن وحارسه:** `src/styles/picker.css` (نطاق `.pk-page`)، و`tools/picker-paper.test.mjs`.

### 13-ك. ورقة الحلّ في التدريب المباشر، ومقعد مستشارك فوق «التالي» (2026-09-25، الجولة 171 في بوّابة القمّة)

**بحرف جو** (لقطتا آيفون: مستشارك يمين يغطّي الخيار الخامس، ومستشارك يسار فوق «التالي» كما يريد): «مكون الاسئلة والإجابات الإثرائية قديم، نبنيه على نفس الإجابات التي عملناها اول الليل في قراءة المدرب... بدون الإخلال بمكونات السوال... فوق مكون (التالي) يتحرك معه بنفس المسافة كل سوال مع استمرار التحكم والسحب الحالي... لاتنسى التمييز وعدم ذوبان اي مكون في الآخر».

**القاعدة:**
- **الحلّ ورقة ثانية لا امتداد للسؤال:** يخرج من بطاقة السؤال ويقعد تحتها قبل شريط التنقّل، بلغة §13-و نفسها (رقّ دافئ، حدّ ذهبيّ، حكم بحلقة مريميّة `#3f7354` أو طوبيّة `#a8483f` فيها ✓ أو × مرسومة، بلا غسلة). وبطاقة السؤال وخياراتها لا تُمسّ.
- **كلّ حاوية إثرائيّة تتميّز بنغمتها وأيقونتها ودمغتها:** الزبدة ذهب بمصباح، والخدعة طوبيّ بمثلّث، وكلام المدرّس بنّيّ بفقاعة، وقانون السؤال تيليّ بميزان؛ دمغة متدرّجة في ركن، والأيقونة قناع إس في جي منسوخ من ورقة الزيارة حرفا (أيقونة واحدة لكلّ فكرة في المنصّة كلّها).
- **الرصيف له مقعد على الصفحة التي فيها زرّ متقدّم:** العنصر يحمل `data-dock-anchor` بمفتاح سؤاله، والرصيف يجلس فوقه بمسافة 10 على حافّته البعيدة عن الكلام، ويرجع إليه بانزلاق حين يتغيّر المفتاح. والسحب حرّ داخل المفتاح الواحد ولا يُحفظ على الجهاز؛ وعلى الشاشة العريضة يجلس في الهامش بجنبه إن اتّسع. ويتبع مقعده عند التمرير، لأنّ «التالي» لاصق على الجوال.

**فخّ مقيس:** الحلقة `color:#fff; background:currentColor` تطلع بيضاء كاملة، فلون الحلقة متغيّر (`--xp-v`) لا `currentColor`.

**171-ب، صفحة السؤال كلّها 2.0** (بحرف جو: «العزل والذوبان لم تتقنه، يجب تفريق المكونات ونهوضها، كل مكونات الصفحة الباقية لم تعطيها وجه واهتمام من خلفية وانيميشن يجب أن تكون بلغة مختلفة، أزرار المكون كلها انقلها في صفحة السؤال والاختبار لفيرجن 2.0»):
- **ثلاث طبقات لا تختلط:** ورق لما يُقرأ (الشريط، وصفّ الأرقام، وبطاقة السؤال، وورقة الحلّ)، ومكتب رمليّ غائر لما يُختار منه أو يُحمل (شريط التنقّل، والساعة؛ وصفّ الأرقام حتّى 177 حين صار خانات ناهضة)، وزرّ ورق ناهض يرتفع ويُضغط.
- **زرّ واحد مصبوغ:** «التالي» بنغمة المسار وسهمه، وكلّ زرّ آخر ورق بصفيحة أيقونة بنغمته؛ والعلامة والإنهاء والخروج بالذهب.
- **الخيار ورق يرتفع، والمختار بخطّ نغمته في قاعه**، والكشف مريميّ وطوبيّ بخطّ قاعه وحرفه ممتلئ، والباقي يهدأ.
- **حاوية الإثرائيّ ورق أبيض فوق الرقّ** بسكّة نغمتها في رأسها وظلّ عمق، فلا تذوب في ورقتها.
- **الحركة تقول ما تغيّر:** الشريط ينزل، والسؤال والخيارات تصعد واحدا بعد واحد، والحكم ينبض؛ وتُطفأ كلّها مع تقليل الحركة، والصفحة نفسها بلا تحويل.
- **حالة الزرّ صنف لا ستايل سطر.**

**171-ج، خلفية الأسئلة من صورة قسمها** (بحرف جو: «ركّبها بالتوزيع اللوني لكل قسم ولا تختار لون يذوب فيه التصميم... فكّر خارج الصندوق»):
- **الخلفية تُقاس من صورة القسم ولا تُختار من البنك:** أربع درجات لكلّ مسار (مكتب شبه محايد، ولونان غالبان خافتان، ودرجة عميقة) مأخوذة من صورته في الرئيسية.
- **ورق ألوان مائيّة لا غسلة:** بقعتان من ركنين متقابلين، وحافّة مدّ أعمق عند طرف الأولى، ورذاذ، وطيف الصورة مضروبا في المكتب (`background-blend-mode: multiply`) فيذوب بياضه.
- **ما بقي كما هو:** البوق يفتحها من القضيب، ولا شيء على `.qscreen`، والورقة فوقها 1.08 وأكثر.

**أين يسكن وحارسه:** `src/styles/product.css` (قسما «(171)» و«(171-ب)»)، و`src/core/advisor/dockPos.js` (`seatOf`)، و`tools/run-expl.test.mjs`، والقياس `tools/shot-171.mjs`.
### 13-ل. صفحة المراجع: لوح القوانين (2026-09-25، الجولة 172 في بوّابة القمّة)

**بحرف جو:** «انقلها لمستوى آخر وحافظ على اشتراطاتنا السابقة من ناحية حجم الخطّ والتصميم والأزرار... أجمل ما تمّ تصميمه لعرض القوانين الرياضية».

- **المواضيع أوراق ناهضة بجوهرة، ومسارها بلا أرضيّة (233-ب، نسخت اللؤلؤ):** بكلمة جو «الفلاتر تسكن على البيج القبيح»، ثمّ رفضه اللؤلؤ «بدّلت بيج بأبيض لؤلؤي بنفس اللصقة، تشعر أنها مقصوصة داخل». فالمسار لا أرضيّة له، وكلّ موضوع ورقة ناهضة (وجه `#fffefb` إلى `#fbf8f1`، وحدّ شعر، وظلّا تماسّ وعمق) بجوهرة حلقيّة بحبر الموضوع؛ المختار ينهض 2 بكسل وتمتلئ جوهرته بقلب أبيض وخطّ حبر في قاعدته. والعدد بحبر `#4f5b6b` تباينه 6.79 (كان 4.09 بالرماديّ على الرمل).
- **المرجع أوراق على مكتب، لا بطاقة تحمل دفاتر:** الرأس ورقة، والمجموعة رأس على المكتب بخطّ شعر يذوب من طرفه، والقانون ورقة. ورق الدفتر المربّع الملوّن تحت الأوراق البيضاء (النسخة الحادية عشرة) صار علامة قِدم.
- **الصيغة بطلة الورقة، مضاءة لا محبوسة (233-ب، نسخت البئر الرمليّة وورق المربّعات):** بكلمة جو «readability هنا فيها شك»، ثمّ «وأنت تضع القانون على خطوط غامقة... ابتكر لإبرازها بشكل رائع». فالصيغة على الورقة نفسها بلا صندوق ولا حدّ ولا خطوط ولا حفر، تحتها هالة شعاعيّة من حبر قانونها (`--lw-glow`: 13% في القلب إلى 5% ثمّ شفاف) وفوقها خطّ قلم قصير بحبره يفصلها عن الاسم، وتشتدّ الهالة عند المرور. وكبرت لأنّها المقروء: 18 على الورقة (16 جوالا)، و32 في اللوحة (23 جوالا)، و19 في بطاقة الحلّ؛ تباينها 13.61. والأسّ بنغمة المجموعة كما حكم المالك في الحادية عشرة. **وكلّ أرضيّة تحت الصيغة، أيّا كان لونها، لصقة.**
- **الرقم الشبح حيث يتّسع له المكان:** على اللوحة الكبيرة (150، ومخفيّ على الجوال) لا على الورقة الصغيرة، لأنّ اسمها سطران يقعان عليه.
- **الحاوية تسمّي فقرتها بأيقونة:** قلم للمثال، ومثلّث بالطوب للفخّ، وراية بالذهب لـ«وفي الاختبار»، ولكلّ حاوية غسلة بنغمتها في ركن البداية (233، خلفت السكّة) ودمغة في ركنها البعيد (§13-و).
- **ما يُحفظ قصاصات في رأس مجموعته مقابل عنوانها (233-ج):** بكلمة جو «نادرة وهي وحيدة ومهمة، فوجودها تحت يلغي أهميتها». «أرقام تُحفظ» رأس ذهبيّ صغير وأربع قصاصات في الطرف البعيد من سطر عنوان الأسس مكان المحرف الشبحيّ، وعلى الجوال سطر تحت العنوان مباشرة. **النادر المهمّ يسكن الرأس لا الذيل.** وكلّ رقم قصاصة ورق ناهضة بشعرة ذهب وجوهرة وخطّ سطر ذهبيّ، بلا لوح كريميّ ولا سطر مصدر.
- **الإحالة ورقة تفتح وجهتها لا سطر برمز داخليّ:** «من الجبر» بأيقونة وصل وحدّ متقطّع، وتفتح لوحة القانون في موضوعه.
- **التنقّل داخل اللوحة:** رجوع ورقيّ ناهض يسمّي وجهته، وموضع «3 من 26»، والسابق والتالي ورقتان ناهضتان بلا مسار تحتهما (233-ب)

- **صينيّة الفئة ورق ألوان مائيّة لا لطخة:** غسلة وحافّة مدّ وغسلة ثانية ورذاذ ومربّعات دفتر وحبيبات ورق، والألوان من باليت صورة القسم وحدها (لغة خلفية الأسئلة §13 من 171-ج). والمزج مع `transparent` بـ`srgb`: بـ`oklch` خرجت درجة المنقلة ورديّة.
- **كلّ فئة بدرجتها، وحاويتها صينيّة لا ورقة:** درجات من عائلة لون الموضوع نفسه لا ألوان غريبة، مرتّبة فلا تتجاور درجتان متقاربتان، ودرجاتها غسلات فاتحة من الصورة لا ألوان مشبعة تُخلط بالرمليّ (خلطها يخرج رماديّا باهتا). واسم الفئة درجة في الهرم بين عنوان الصفحة واسم القانون.
- **(262 و267) البطاقة المختصرة، شرح القوانين 2.0:** العنوان القاعدةُ بجملة، والصيغة، ثمّ ليش ومثال ومتى **سطورٌ لا حاويات**، وأخو القانون ورقة ناهضة بحافّة متقطّعة تفتح لوحته. **وكلّ سطر غسلةٌ من حبر مجموعته على الأبيض تشتدّ نزولا** (ليش 7% ومثال 13% ومتى 20%، وكلمة عنوانه بحبر 66% و80% و94%، متغيّران `--lw-sh` و`--lw-ink`)، بكلمة جو (267، ب-359): «لمسة للتفريق بين الثلاثة؟ مو لمسة جمالية، لمسة ممكن تكون حتى بدرجات ألوان من نفس اللون مختلفة؛ لأن الحين شكلها كتلة واحدة». **على الأبيض لا على ورق البطاقة:** الغسلة نفسها على الدافئ `#fffdf8` خرجت رماديّة بلا زرقة (مقيسٌ باللقطة: 245 و237 و227 على القنوات الثلاث)، وهو قانون «خلطها بالرمليّ يخرج رماديّا باهتا» أعلاه بعينه. والبطاقة داخل ورقة الحلّ بالدرجات نفسها (`--lwc-sh`)، فالسطر الذي عرفه في اللوحة يعرفه هناك.
- **(271) والجزيرة في السطر سطرٌ لا صندوق، والكسر المركّب يطوّل سطره:** جزيرة الرياضيّات في سطور ليش ومثال ومتى `display:inline` مع `white-space:nowrap` (`.lw .lw-ln dd .m` في `src/styles/laws.css`، و`.lwc.is-lean .lwc-row > span .m` في `src/styles/lawcard.css`)؛ كانت `inline-block` من `.m` العامّة ففتحت فرصة كسر قبل الفاصلة التي تليها، فبدأ سطرٌ بـ«،» على 390. **وكلّ سطر سطران حدّا على الجوّال، والحكم للمتصفّح لا لعدّ الحروف:** الجزيرة لا تنكسر فتدفع السطر أبكر، والكسر المركّب يرفع سطره، فسطرا صفٍّ واحد لا يحملان كسرين (يُعدّان ثلاثة بالارتفاع)، ويُقاس السطر وهو يُكتب بـ`tools/e2e-laws-fit.mjs`.
- **القانون داخل ورقة الحلّ حاوية إثراء لا ورقة ثانية:** نغمة مجموعته، وميزان في رأسه («قانون السؤال») ودمغته في الركن، والاسم بخطّ العناوين، والصيغة مضاءة بهالة حبرها نفسها بلا شريط ولا خطوط (233-ب)، والمثال والفخّ سطران بخطّ شعر لا حاويتان داخل حاوية.

**أين يسكن وحارسه:** `src/styles/laws.css` (نطاق `.lw`) و`src/styles/lawcard.css` (نطاق `.lwc`، البطاقة داخل الحلّ)، يستوردهما `Laws.jsx`، و`tools/laws-paper.test.mjs`.

### 13-م. «سجلّي» ورقٌ على مكتب مائيّ، وزرّ الرجوع المشترك (2026-09-26، الجولة 182 في بوّابة القمّة، ب-245)

**بحرف جو (بلقطة السجلّ على الديسكتوب):** «الأزرار فوق حقت الفلاتر... قديمة. زر الرئيسية قديم... هل يرضيك الخلفية الصامتة اللي كأنها جدار لغرفة السجل؟ وين الـ hero، وين الـ ghost، وين الإبداع؟ ما ينفع هذا الـ block أبدًا، ولا تجعله أبدًا في أي تصميم لنا.»

- **قانون دائم: الصفّ العريض المسطّح ممنوع في كلّ تصميم لنا.** قائمة بطاقات بعرض الشاشة كلّها، كلّ واحدة شريط أفقيّ منخفض على ورق بلا مكتب، هي «البلوك» الذي رفضه جو. القائمة أوراق قائمة بذاتها: عمود على الجوال، **وعمودان على العريض** (≥900)، ولكلّ ورقة رأس ومتن وذيل.
- **الهيرو رأس المحطّة نفسه لا ورقة فوقه:** `StationShell` يقبل `extra` يُلحق برأسه. رأس السجلّ ورقة ناهضة (حافّة 22، غسلة نغمة المحطّة في ركنها)، عنوانها بخطّ العناوين 40 (46 على ≥1360، و32 على الجوال) ولا يتجاوز 60% من العرض.
- **الشبح مروحة رسوم الأقسام:** أربعة رسوم من `artOf` (النماذج، والأخطاء، والمستوى، والكمي) في الطرف المقابل للعنوان، مائلة، بالضرب `multiply` وشفافيّة .34 تحت قناع يذوب نحو النصّ. **والفلتر المختار يُبرز رسمه** (1.18 وشفافيّة .72) ويخفت الباقي إلى .12.
- **دفتر الأرقام وصفة 180 بعينها:** ثلاثة أعمدة بفجوة 1 على خلفيّة شعرة، ولكلّ عمود جوهرة 10 بنغمته قبل اسمه: «أعلى نموذج» (أو «أعلى نتيجة»)، و«آخر جولة» كلمةً بخطّ العناوين، و«آخر أسبوع» بعدد جولاته ومعدّلها. الرقم بخطّ الأرقام 28 معزولا يسار إلى يمين.
- **الفلاتر خمس أوراق متساوية بجوهرة بلون مجموعتها (وصفة 4-ب بلا حفر):** الكلّ `#0b656d`، والنماذج `#7E5F92`، واختبارات الأخطاء `#9C5E2F`، وتحديد المستوى `#B5874A`، والتدريبات `#5378A0`. الورقة: تدرّج ورق، وظلّ خارجيّ، وارتفاع 60؛ فيها الاسم ثمّ عدّها («8 محاولات»، أو «ما فيه» ولا تختفي). **المختار:** غسلة بنغمته وخطّ قاع `inset 0 -3px 0 var(--ft)` والجوهرة ممتلئة. **الفارغ:** مسطّح مقروء. على الجوال (≤760) الأوراق الخمس عموديّة الترتيب: الجوهرة فوق والاسم سطران.
- **الورقة دمغتها رسم نوعها:** `img.nb-stamp` في ركن النهاية العلويّ (104، و124 على العريض، و84 على الجوال) بالضرب وشفافيّة خفيفة، والوسوم والعنوان يحجزان مكانها. العنوان بخطّ العناوين 22 سطران على الأكثر (19 على الجوال). **خانة الحلقة ثابتة 64** (58 على الجوال)، وشكل الحلقة للجولة 185. والفرق عن السابق كبسولة مريميّة أو طوبيّة في سطر المحاولة.
- **البابان بعرض الورقة في قاعها** (شبكة 1fr 1fr، `margin-top:auto`)، ووجههما لعائلة أزرار القراءة (§15-ج 2-ج)؛ السجلّ يرتّبهما ولا يلبسهما.
- **المكتب مائيّ بلوحة كلّ فلتر (وصفة 11):** `body:has(.nb-page)::before` طبقة ثابتة: حبيبات، وغسلتان، وحافّتا مدّ خافتتان (13% و11%، فلا تُقرأ دوائر)، ورشّة. «الكلّ» يمزج لوحات الرسوم الأربعة؛ وكلّ فلتر بلوحة رسمه (`data-f` على الصفحة). قيس: ورق على مكتب بين 1.26 و1.51. **(210) والمحدِّد اليوم** `body:not(.inrun):has(:is(.nb-page, .nb-attempt, .co2-page))`: صفحة قراءة المستشار تقف على مكتب محاولتها وإن رُسمت خارج غلافها، والجولة القائمة تبقي مكتب حارتها (§13-ج إضافة 210).
- **زرّ الرجوع المشترك في رأس كلّ محطّة:** ورقة 46 بتدرّج ورق وصفيحة أيقونة 30 (`.stp-back-ic`، قناع `--stp-ic`)؛ «الرئيسية» بشبكة البيت (`.stp-home`)، وغيرها بسهم (`.stp-ret`). يرتفع عند المرور وينضغط عند اللمس.
- **(211، ب-275) وزرّ الرجوع المشترك يصل كلّ صفحة ترجع إلى مكان:** رأس المحطّة ورأس المحاولة ولوح القوانين (`:is(.stp-head, .nb-ahead, .lw) .stp-back`). ونغمة الصفيحة من وجهة الرجوع: تيل المستشار `#0b656d` لـ«رجوع لقراءة مستشارك»، ونغمة الموضوع (`--lt`) لـ«رجوع للقوانين». **ولا زرّ رجوع ذهبيّ ولا سهم محرف «‹» في أيّ صفحة.** وحيث يُحمَّل نمط الصفحة بعد `record.css` (لوح القوانين يُحمَّل كسولا بعده) تُكتب قاعدة واحدة بمحدِّد أعلى تعيد المقاس وتسكت أيّ حركة موروثة (التنفّس الذهبيّ القديم).

- **نوافذ الشيء الواحد أوراق ناهضة لا مسار رمليّ (الجولة 200، ب-264؛ تصل مع دمجها):** الختام والإجابات كاملة وقراءة المستشار ثلاث خانات متساوية من عائلة 4-ب، ارتفاع 52 وفجوة 10 بلا حفر تحتها، ولكلّ خانة صفيحة أيقونة 30 بنغمة مجموعة المحاولة (لوحة المرشّحات؛ الذهب `#8a6d1f` للقراءة). الحاليّة غسلة ركنها وخطّ قاع 3 وصفيحتها معبّأة، والنغمة لا تتبدّل بين النوافذ. على الجوال (≤560) الرجوع سطر وحده والصفيحة فوق اسمها بارتفاع 74. والرجوع إلى السجلّ زرّ الرجوع المشترك بسهمه، ومكتب المحاولة مائيّ بلوحة مجموعتها (`data-f`).

**أين يسكن وحارسه:** `src/styles/record.css` (يُحمَّل بعد أنماط المستشار وقبل المنتقي)، و`Notebook.jsx` (`RecordHero`، `AttemptCard`)، و`StationShell.jsx`. الحارس `tools/record-paper.test.mjs` (33 في 182، و38 بعد 211؛ رُئي أحمر بطفرتين في كلّ منهما)، و`record-phone` و`e2e-record` (40) على البنية الجديدة.

### 13-ن. صفحة مرجع تُقرأ: «قواعدك الذهبية» (2026-09-26، الجولة 184 في بوّابة القمّة؛ تصل مع دمجها)

- الصفحة التي تعيش على رأس المحطّة المشترك تلبسه بطلا بنمط في نطاقها (`.st-page-<key> .stp-head`) لا بتعديل المكوّن: ورقة معزولة، ورسم قسمها `::before` بالضرب في 34% البعيدة، والعنوان في 60% لا يعبر إليه.
- المكتب من رسم القسم نفسه: درجاته مكمَّمة من الملفّ (الوصفة 11 بقيمها الأربع)، وصفحة لا لوح لها في الشبكة تأخذ رسم لوحها في الرئيسيّة.
- **قائمة نصوص متساوية الشأن تكبر بلا حدّ: عمودان يجري فيهما الورق (`columns:2` و`break-inside:avoid`) لا شبكة صفوف.** الشبكة تترك يتيمة، والقائدة بعرض الصفحة شريط بوسط فارغ.
- الرقم الشبح يحلّ محلّ الكرة المرقّمة: `content:attr(data-n) / ""` بخطّ العناوين، و`--gh` .13 (والثقيلة .2)، والرقم المقروء مخفيّ بـ`clip` لا بـ`display:none`.
- سطر حالٍ حيّ (يكتب، ينتظر) ورقة طافية فوق ما يخبر عنه، بجوهرة أيقونة تتحرّك وشريط ذهب يلمع، ويُطفأ كلّه مع تقليل الحركة.

### 13-س. دروس المكالمات: ورقة السلوك، وشبكة فلتر بلا يتيمة، ودرجات السلوكيّات (2026-09-26، الجولة 187 في بوّابة القمّة؛ تصل مع دمجها)

- **ورقة السلوك (§13/§15):** ورقة ناهضة بظلّ المكتب، وجوهرة بلون السلوك قبل اسمه بخطّ قلم تحته، و«خطوتك الجاية» ورقة داخليّة بغسلة 6% من لونه وظلّ تلامس لا خطّ، والمكالمات صفوف بخطوط شعر لا بطاقات (لا حاوية داخل حاوية).
- **شبكة فلتر بلا يتيمة:** `filterGrid(n)`: حتّى 4 خانات صفّ واحد، وفوقها 3 أو 4 أعمدة أيّها يترك «الكل» أضيق حين يتمدّد، وعلى الجوال عمودان و«الكل» صفّ كامل إن كان العدد فردا.
- **درجات السلوكيّات من عائلة صورة القسم** مرتّبة فلا تتجاور درجتان متقاربتان (`SHADES` في `StationLessons.jsx`).

### 13-ع. ورقة القرار: كلّ نافذة لؤلؤ بختم معناها (2026-09-26، الجولة 189 في بوّابة القمّة، ب-253؛ تصل مع دمجها)

بكلمة جو: «الـ dialogues اللي تطلع كلها على النسخة القديمة. نحتاج نسخة مميزة وليست عادية؛ كل شغلنا لؤلؤي وأبيض... ما يصير فيه تكرار». كانت تسع عشرة نافذة وجها واحدا: ورقة `#fff` ومربّع أصفر بمثلّث تحذير فوق كلّ سؤال، والحفظ والمسح النهائيّ بزرّ أزرق واحد.

- **مكوّن واحد، ووجه من المعنى:** `Dialog.jsx` يحمل الهيكل، و`dialogFaces.js` يحمل الوجه (نغمة ورسم): الحفظ تيل `#0b656d` بعلامة كتاب، والوقت ذهب `#8a6d1f` بساعة رمليّة، والناقص حبر رمل `#6d5a36` بقائمة فيها خانة فارغة، والختام مريميّ `#3f7354` بعلم، والقسم `#5378A0` بفنجان الاستراحة، والباب بنغمة الجولة المعلّقة من سجلّ الحارات، والمسح والتصفير طوبيّ `#a8483f` بسلّة أو سهم رجوع، والمستشار تيل بفقاعة كلام. **نافذة جديدة تسمّي معناها ولا ترث وجها.**
- **الستارة ضباب دافئ لا حبر:** `radial-gradient(110% 80% at 50% 42%, rgba(255,251,242,.34), rgba(74,63,46,.44) 78%)` مع `blur(10px) saturate(1.08)`.
- **الورقة لؤلؤ أبيض:** `linear-gradient(180deg, #fffefb, #fdf9f1 62%, #faf4e8)` وفوقها لمستان باهتتان في ركنين (`rgba(214,226,240,.34)` و`rgba(240,224,232,.30)`) وهمسة النغمة 7% في رأسها، وحدّ `rgba(176,150,96,.42)`، وزاوية 26، وظلّ `0 34px 64px -26px rgba(74,63,46,.62)`، وبريق يمرّ مرّة ساعة الدخول. **لا هالة عريضة حولها:** ستّة بكسلات بيضاء قُرئت إطارا ثانيا (حاوية داخل حاوية) فحُذفت.
- **الختم نصفه خارج الورقة:** قرص لؤلؤ 72 (`top:-36px`) فيه جوهرة 52 بتدرّج النغمة وحلقة ورق، والرسم أبيض بخطّ 1.8. والعنوان بخطّ العناوين 22 (24 على العريض)، وتحته خطّ قلم 46 بالنغمة، والمتن 15.5 بحبر `#4f4738`.
- **الأفعال صفّ من ورقتين، والمصبوغ واحد:** الفعل المعتاد وصفة §15-ج-3 بنغمة الوجه، والهادئ ورق الزرّ الناهض (§15-ج-2)، ولمسة 50. **ووجه الإتلاف بلا مصبوغ أبدا:** الماسح ورق بحبر طوبيّ `#8a3831` وخطّ قاع `inset 0 -3px 0 #a8483f`، فلا يلبس المسح النهائيّ وجه الخيار الآمن. والمخرج الثالث صفّه وحده، ورق بحبر وجهته (تيل للقفز، طوبيّ للقتل).
- **الكلام لا يتكرّر:** ما قاله العنوان لا يعيده المتن (اسم الجولة المعلّقة مرّة في المتن).
- **الشيفرة والحارس:** `src/styles/dialog.css`، و`tools/dialog-paper.test.mjs`، و`tools/shot-189.mjs` يفتح النوافذ الحقيقيّة على 390 و430 و440 و1280 و1440.
- **ورقة الحساب: الختم وجه صاحبه (الجولة 207، ب-271؛ تصل مع دمجها).** لوحة الحساب ورقة من عائلة ورقة القرار (اللؤلؤ نفسه، وانحناء 26، والختم 72 نصفه خارجها)، لكنّ ختمها **صورة صاحبها** 54 بحلقة نغمته (تيل `#0b656d`، وذهب `#8a6d1f` للمشترك) لا جوهرة برسم، لأنّ معناها «أنت». والاسم بخطّ العناوين 21 (22 على العريض) وخطّ قلم بالنغمة. **والأبواب سطور لا بطاقات:** كلّ باب سطر في الورقة نفسها، يفصله خطّ شعر `rgba(176,150,96,.28)`، وله جوهرة 40 بنغمة معناه في رأسه وكلامه في وسطه وفعله في ذيله (ورقة صغيرة للباب الذي يفتح صفحة، وسهم لؤلؤيّ 30 للسطر الذي هو كلّه باب). **والفعلان ورقتان متساويتان بعرض خانتيهما، بلا صبغة:** لا شيء في الحساب فعل معتاد يستحقّ الصبغ، والخروج مغادرة لا إتلاف، فحبره طوبيّ `#8a3831` بلا خطّ قاع. وعلى الجوال تتوسّط الورقة الستارة بعرضها، وعلى العريض تتعلّق تحت الرقاقة بعرض 392. والشيفرة `src/styles/account.css`، والحارس `tools/account-paper.test.mjs`، والتصوير `tools/shot-207.mjs`.

### 13-ف. الوسام مرسوم لا صورة برقم، و«إنجازاتي» رفوف تحمّس (2026-09-26، الجولة 195 في بوّابة القمّة، ب-259)

**بحرف جو:** «نحتاج أن ننهض فيه بحيث يكون يبين الوسام فعلًا... عدّة أوسمة بأشكال مختلفة تكون متوقّفة أو dimmed حتى يكون يحمّس الطلاب... موضوع أنها تكون فقط صورة ذي برقم يعني أحتاج يحتاج من عندك إعادة نظر».

- **الوسام رسم خالص بلا صورة ولا مكتبة (`Badge.jsx`، وحكمه النقيّ `core/progress/badgeArt.js`):** شكلٌ لكلّ مسار: **الأسئلة قرص بأربعة وعشرين سنّا ليّنا وشريطتين**، و**النماذج درع بشريطتين**، و**الدقّة نجمة ثمانيّة**، و**أيّام المذاكرة سداسيّة**. ووجهٌ لؤلؤيّ في الوسط (قرص بتدرّج من الأبيض إلى وجه المعدن) فيه رمز المسار (صحّ، ساعة رمليّة، هدف، شمس) والرقم بخطّ الأرقام بحبر المعدن، وتحت الرقم نقاط بعدد درجات المسار، الممتلئة حتّى درجته.
- **المعدن بالدرجة داخل المسار:** نحاس `#9a6236` ثمّ فضّة `#6f7c86` ثمّ ذهب `#9c7718` بالثلث، **وأعلى درجة في مسارها ذهب دائما بتاج جوهرة تيل**. لكلّ معدن حافّة ووسط ولمعة وحبر ووجه (`METALS`)، وظلّ الوسام من معدنه. وبريق يمرّ على المعدن كلّ ستّ ثوان (مقصوص بشكله)، ويسكن مع تقليل الحركة.
- **المقفل الشكلُ نفسه بلا لون:** `grayscale(1)` وشفافيّة .36 على جسمه، فيرى الطالب ما ينتظره ولا يلتبس بما أخذه. **والقادم في مساره** يلبس فوق ذلك قوس تقدّم ذهبيّا `#b8912e` حول حافّته بنسبته، وتحته «باقي 40» بحبر الذهب؛ فلا قسم ثانٍ «القادم» يكرّر الرفّ.
- **رأس «إنجازاتي» هيرو من المحطّة نفسها (`extra`):** عنوان بخطّ العناوين 40، وسطر «5 من 14 وسام على رفوفك»، و**مروحة أربعة أوسمة بأشكال المسارات** دمغةً في الجهة البعيدة (أعلى ما أُخذ في كلّ مسار، أو أوّله باهتا) بشفافيّة .42 تحت قناع يذوب نحو النصّ، ثمّ **دفتر أرقام بأربعة أعمدة** (وصفة 180: فجوة 1 على شعرة، وجوهرة بنغمة كلّ عمود): سؤال أنجزته، ودقّة إجاباتك، ويوم مذاكرة، ونموذج كامل. وعلى الجوال اثنين في اثنين. ولا شريحة عدد في الرأس: الدفتر والسطر يقولانه.
- **الرفوف ورقة لكلّ مسار** بغسلة نغمته في ركنها، وجوهرة واسمه بخطّ العناوين وخطّ قلم تحته، و«2 من 6» في الطرف. الأوسمة شبكة بلا يتيم: ثلاثة أعمدة (الدقّة اثنان)، **وعلى العريض (≥900) رفّ الأسئلة بعرض الصفحة بستّة، وتحته الثلاثة الباقية جنبا إلى جنب**. المأخوذ على ورقة صغيرة ناهضة بغسلة ذهب وتاريخ أخذه («أخذته 24 سبتمبر»)، والمقفل مسطّح بحدّه بلسان الطالب («عند 250 سؤال»، «دقّة 85% بعد 100 سؤال»). الوسام 78 (92 على العريض، 72 على الجوال).
- **المكتب مائيّ من معادن الأوسمة** (وصفة 11: ذهب `#ecd9a8` ونحاس `#e4c8b0` وفضّة `#d9e0e6` على `#f4efe4`)، وكتم ذيبان سطر هادئ على المكتب لا ورقة.
- **لحظة الوسام ورقة القرار (§13-ع) والوسام ختمها:** الوسام 168 نصفه فوق الورقة (`top:-84px`)، خلفه أشعّة مقنّعة دائريّا وعشر رشقات بلون المعدن تنطفئ وحدها، ويدخل بقفزة (`scale(.35) rotate(-18deg)`). ونغمة الورقة وزرّها المصبوغ الوحيد من معدن الوسام. تحته: «وسام جديد على رفّك»، والعنوان بخطّ العناوين 28 وخطّ قلم، وكلمة ذيبان بصورته، ثمّ ورقة داخليّة ناهضة للجاي بوسامه المقفل بقوسه وشريط ذهب. **والجاي يُحسب بعد الوسام نفسه لا من التقدّم المسجَّل**، فلا يقول «الجاي: العشرة الأولى» ساعة أخذها.
- **الوسام في وقته:** العبور يُحتفى به عند السؤال الذي حقّقه، لا عند ختم الجولة (تحديد المستوى يبثّ ما أجاب، §`liveCrossings`). والجولة المؤقّتة تبقى على ختمها (قدسيّة الجلسة).
- **(209) الهيرو بيت برنامج اللفلات (`core/progress/levels.js`، ب-273):** بكلمة جو «خلي موضوع الأوسمة يكون برنامج مطور... levels... في الـ hero section». **شعار اللفل الكلّي** قرص لؤلؤ (`#fffefb` إلى `#e9dcc0`) بحلقة ذهب (`#f0d57e` إلى `#8f6d1c`) وقوس تقدّم نحو أقرب ترقية، ورقمه في مركزه وكلمة «لفل» تحته، و**رتبته** بخطّ العناوين (من صورة الجبل: على السفح، طالع الجبل، نصّ الطريق، قريب من القمّة، على القمّة، أسطورة القمّة) وتحتها «أقرب ترقية» بباقيها. ثمّ **تحدّي الأسبوع** ورقة ناهضة بسبع حبّات ذهب للأحد إلى السبت (المذاكَر ممتلئ، واليوم بحلقة، والآتي باهت). ثمّ **دفتر الألقاب الخمسة** بوصفة 180 (خمسة أعمدة بفجوة شعرة، وجوهرة بلون كلّ لقب، وشريط قلم وباقيه)، وعلى الجوال سطور بلا يتيم. **والرقم في لقبه مرّة والرفوف للأوسمة وحدها** (دفتر الأرقام الأربعة القديم خرج). **وختم «جديد» على اللقب الذي ترقّى منذ آخر زيارة هو الشارة الواحدة** (`gem-chip` بحال `new`، جوهرتها ذهب)، والمحطّة تضعه ولا تصبغه، ويظهر مرّة ثمّ يُحفظ ما شافه.
- **الشيفرة والحارس:** `src/styles/achievements.css` (بعد ورقة القرار وقبل المنتقي)، و`Milestones.jsx`، و`StationAchievements.jsx`، و`BadgeMoment.jsx`. الحارس `tools/badges.test.mjs` (27، رُئي أحمر بطفرتين)، واللقطات `tools/shot-195.mjs` على 390 و430 و440 و1280 و1440 ومعها مشي تحديد المستوى.

### 13-ص. محطّة بأبواب: «على أخطائك» (2026-09-28، الجولة 231 في بوّابة القمّة، ب-299)

**بحرف جو:** «يجب أن نبين ما هو بمؤقت، وما هو بدون جواب مباشر، من الذي بجواب مباشر. نعطيه هذه البوابة أو هذه المحطة روح البوابة الجديدة.»

- **كلّ باب ورقة أخت، لا باب داخل باب:** الأبواب على المكتب بترتيب طريقها، ورقم كلّ باب شبح من `data-n` في ركنه البعيد العلويّ، فلا يختبئ خلف الأزرار.
- **الصفة التي يسأل عنها الطالب قبل أن يبدأ شارة ثابتة الموضع تحت الاسم، ولها قيمتان مقروءتان حتى حين تكون «لا»:** «بلا مؤقّت / بمؤقّت» بساعة، و«الحلّ فور الإجابة / الحلّ عند الختام» بمصباح، من `gem.css` بجوهرة حالها (الخافت والكهرمانيّ، والمريميّ والذهبيّ). والكبسولة المصبوغة في ركن تقاعدت هنا كما في ج.
- **الأحجام خانات ناهضة بصفّ متساوٍ** (`flex:1 1 0` وعنوانها سطر كامل فوقها)، فلا يتيم مهما قلّ عددها؛ الرقم بخطّ العناوين وتحته ما يفرّقه وحده.
- **الباب الذي يحمل جدولا أو جدارا يأخذ عرض الصفحة على العريض،** والبابان الخفيفان جنبا إلى جنب؛ والجدار غسلة داخل الورقة لا صندوق ثانٍ.

- **(232) قائمة قوانين على باب: التصنيف خانة، والقانون بطاقة مؤشّر.** رقمه بخطّ العناوين بنغمة الصفحة، ومؤشّره المختصر سطران على الأكثر (شطر الاسم قبل «:»)، وما بقي عليه بجوهرة؛ والمقفول ورق بغسلة مريميّة وعلامة ✓. نصّ القانون لا يسكن الباب.
- **(232) قانون الجلسة شريط ورق بمسحة الكمّيّ فوق الأسئلة، ومؤشّره بخطّ العناوين وحبر الكمّيّ العميق `#34508f`، بلا شريط تظليل خلف الحروف** (جو 09-28 09:23، وعتاب 233: لا خطوط خلف حروف)، والبطاقة كاملة خلف زرّ ثانويّ لا مفروضة.
- **(232) الحالة التي تظهر أحيانا تُرسم مثل الافتراضيّة، بثلاث قصاصات لا رابع لها:** المعلّق ورقة ناهضة بنغمة الصفحة (عنوان بخطّ العناوين، وعدّ بمقياس، والوقت بشارة، والفعل الأوّل بحبر الصفحة والثاني ورق هادئ)، والمقفل غسلة داخل الباب بقفل وسبب ومقياس إن كان للشرط رقم، والمكتمل غسلة مريميّة. ولا تُكرَّر حال يقولها سطح بجانبها (العنوان «انتهى الوقت» يغني عن شارته، والجدار «أقفلتها كلها» يغني عن سطر ثانٍ). ومن يعيد تصميم صفحة يصوّر كلّ حالاتها، لا الافتراضيّة وحدها.
- **(232) أبواب صفحة واحدة تتمايز بدرجة لا بلون جديد:** كلّ باب يضع ورقه و`--tile` لبلاطاته (واحد أغمق ببلاطات فاتحة، وآخر فاتح بمسحة لون الصفحة)، فلا يطغى البنّيّ على الصفحة ولا الأبيض على الأزرار. والباب الذي ينتمي لقسم آخر (إقفال القوانين للكمّيّ) يلبس لوحة ذلك القسم كاملة، ومرشّحاته عمود جانبيّ بجوار محتواه على العريض لا شريط بعرض الصفحة. والتلميح المؤقّت يسكن مجرى رأسه، لا يطفو خلف حدّ حاوية مقصوصة.
- **(240) الخريطة الحراريّة بلاطات صغيرة ناهضة لا مربّعات مسطّحة:** كلّ خليّة ضوء من فوق وظلّ تلامس، ودرجاتها الأربع متباعدة من حبر بابها (أوّلها لا يقلّ عن 20% على الأبيض، وآخرها الحبر كاملا)، والمفتاح يرسم التدرّج كلّه لا درجة واحدة، والمقفول مريميّ. ومقاسها من عددها، وما فوق المئات يأخذ عرض حاويته ويقف بتمرير داخليّ لا بطول بلا حدّ. والخريطة نفسها تصغر نقاطا تحت كل بند يجمع أسئلة (القانون)، وسما لا زرّا داخل بطاقة هي الزرّ.

- **(255، ب-333) «سجلّ أخطائك» جسمٌ ثانٍ تحت رأس المحطّة نفسه، فيلبس لغتها لا لغة الجولة 22.** بحرف جو من لقطتي جوّاله: «عائش في الحقبة الماضية للتصميم القديم، يحتاج إعادة تصميم بهويتنا الجديدة مع احترام التاجات وتعداد الأخطاء». فلا ورقة تحمل الأسطر؛ والعنوان بخطّ العناوين وتحته خطّ قلم 46×3 لا شريط خلف الحروف (233)؛ والخلاصة سطر بأعداده؛ والفرز خانات ورق 52 من عائلة «تدرّب على» (نغمة الكمّيّ `#5378A0` واللفظيّ `#0b656d`، والمختارة بخطّ قاعها)، و«بالأقسام» خانة تابعة، وعلى الجوال الخانات سطرٌ أفقيّ بنقطة صغيرة كخانات «تدرّب على» فوقها؛ والتلميح سطرٌ بمصباح في مجرى الرأس لا صندوق.
- **(255) الأسطر أوراق إخوة:** عمود على الجوال وعمودان من 900، والمفتوح بعرض الصفحة (§13-م)؛ الورقة بزوايا 18 وظلّ دافئ بطبقتين وغسلة ركن بنغمة قسمها؛ والوسوم فوق نصّ السؤال (§13-ب) بحبر مجموعتها ونقطة، ومعها باب «افتح» لؤلؤة 28 تدور حين ينفتح السطر، فلا يسقط وحده في سطر ثالث؛ والنصّ سطران على الأكثر 16/700؛ والقانون بحبر الكمّيّ العميق `#34508f`؛ **والتكرار الشارة الواحدة** (`gem-chip`، §15-ج 2-ز: مرّتان «راقب» وثلاث فما فوق «انتبه») لا قرص ملوّن.
- **(255) السطر المفتوح أوراق إخوة لا صندوق داخل صندوق:** بطاقة السؤال نفسها (ب-100)، ثمّ ورقة «نصيحة قانونك» بمسحة الكمّيّ واسم القانون بخطّ العناوين، ثمّ دفتر أرقامه خلايا ورق بفواصل شعر (عمودان على الجوال بلا يتيمة). والمجموعة رأسها اسمها بخطّ العناوين 20 وعدّها وبابها، وأسطرها تحتها على سكّة بنغمة قسمها.
- **(255) الرجوع زرّ الرجوع المشترك في رأس المحطّة «رجوع لمحطّتك» (211)،** لا سهم محرفيّ داخل الصفحة؛ والشِّق لا يكرّر في السجلّ عدّا تقوله خلاصته.

**أين يسكن وحارسه:** `src/styles/errors.css` (نطاق `.st-page-errors`، وشريط الجلسة في `.qscreen.runlane-lawlock`، وقسم «سجلّ أخطائك» في آخره)، و`tools/errors-paper.test.mjs` و`tools/ledger-paper.test.mjs` (255)، واللقطات `tools/shot-231.mjs` و`tools/shot-232.mjs`.

### 13-ق. المجلس الواحد: بابان في شريحة، والسبّورة زرّ، والفقاعات بأصحابها (2026-09-29، الجولة 255 في بوّابة القمّة، ب-327)

**بحرف جو:** «نخلي كل الجينيريشن في صفحة واحدة مو بلازم يتنقل في أربع جهات مرة للكلام ومرة للصور ومرة للحفظ»، و«فيها دائرة تحمل اسمه وليس كتبتها له».

- **الأبواب شريحتان في ورقة لؤلؤ لا درج جانبيّ:** شريحة `#f0e9da` بحدّ ذهبيّ خافت، والمختار ورقة ناهضة (تدرّج `#fffefb` إلى `#fbf6ec`، وضوء من فوق، وظلّ تلامس)، والهدف 40. وزرّ السبّورة ورق بلون المنصّة يمتلئ بالتيل حين تكون ظاهرة، وعدد بنودها شارة على كتفه.
- **على الجوال السبّورة شريطٌ فوق المحادثة لا بابٌ يحلّ محلّها:** الحديث تحته له 170 على الأقلّ، والشريط لا ينقص عن 150، ومقبضه خطّ 40×4 بلون الذهب الخافت في شريط 22 يُسحب.
- **كلّ فقاعة جنبها صاحبها:** فقاعة المستشار فقاعة كلام بذيل (عائلة §13-ط: ورق `#fffcf4`، وحدّ ذهبيّ 1.5، وتوهّج من ركنها، وزوايا 22) ووجهه في حلقة ذهبيّة 28؛ وفقاعة الطالب ورق `#eee7da` بزوايا 18 وزاوية جهته 6، وجنبها دائرته 28 (**256، ب-337:** شعار البوّابة نفسه بحلقة تيل رفيعة لكلّ طالب سواء، مكان كبسولة لقبه ورمز الزائر). **وكلّ صاحب على حافّة فقاعته الخارجيّة كالواتساب:** وجه المستشار يسار فقاعته، ودائرة الطالب يمين فقاعته وزاوية الفقاعة الصغيرة نحوها (كانت الدائرة يسارها بين الفقاعة ووسط المجلس، ولقطها جو من جوّاله). والصاحب على آخر فقاعة من كلامه المتتابع، وما قبلها فراغ بعرضه فتصطفّ. ولا وسم «كتبتها له».
- **الصورة في طريقها ورقة تتحمّض في المحادثة:** مستطيل 148 تطلع ألوانه (تيل وذهب وأزرق) من تحت ثمّ تثبت، وسطرها تحته بحبر الذهب العميق؛ والحركة تسكن مع تقليلها.
- **«محادثاتك» بطاقات ورق مجمّعة باليوم:** رأس اليوم سطر رماديّ ثقيل («اليوم»، «أمس»، ثمّ اسم اليوم وتاريخه)، والبطاقة ورق بزوايا 16 وحدّ ذهبيّ خافت، والمفتوحة بحدّ تيل وهالة؛ والأعداد وسوم ورق صغيرة بمعدودها («دورين»، «4 أدوار»)؛ وزرّ المسح ورق بخطّ قاع طوبيّ `#a8483f`؛ والمرشّحات الستّ شبكة ثلاث بلا يتيمة (§13-س).
- **ووجه جيهان** يلبس المجلس ساعة يُختار صوتها، مقصوصا من رسمتها المعتمدة بأداة وجه الشابّ نفسها (البرومبت في `design-language/prompts/persona.md`).

**بيته وحارسه:** `src/styles/advisor.css` (القسم «المجلس الواحد»)، و`src/core/advisor/majlis.test.mjs` في البوّابة، و`tools/e2e-majlis.mjs` في المتصفّح.

### 13-ر. السبّورة لوح: اللوح الداكن، وحلقات الخطوات، والصفحة الجديدة بدل المسح (2026-09-30، الجولة 258 في بوّابة القمّة، ب-327)

**بحرف جو:** «أحتاجك أن تنقلها من 2.0 إلى 5.0... اللوحة الجانبية التي تعطيك سبورة تمتد عرضًا وطولًا حسب الـ interaction. هذه ميزة حلوة، حافظ عليها»، ثمّ حكمه على لوح «المجلس 5.0»: «لون السبورة، أنا عجبني اللون الـ اللوح وأتفق معك حضوره أقوى. الصفحة الجديدة بدل مسحة، أتفق معك فيها». والقيم مقروءة حرفا من `BoardTone` (الوجه «لوح») على لوح التصميم.

- **اللوح استثناء الورق الوحيد في المجلس، وله بيت واحد:** `.advslatebox` في العمود والشريط والتوسيع وبطاقة «محادثاتك»، ولا يفرق بينها إلّا القياس. التدرّج `linear-gradient(180deg, #183b40, #10292d)` تحت لمعة `radial-gradient(120% 80% at 30% 0%, rgba(255,255,255,.06), rgba(255,255,255,0) 60%)`، وحدّ `1px solid rgba(229,196,97,.3)`، وظلّ `0 1px 2px rgba(0,0,0,.2), 0 16px 30px -18px rgba(16,41,45,.7)`، وزوايا 18 (13 في الشريط، و14 في البطاقة)، والحبر عاجيّ `#f3ecdc`، وشبكة نقاط `rgba(243,236,220,.12)` كلّ 20 بشفافيّة .6.
- **واللوح قطعة على مكتب رمليّ لا جدار ملوّن:** العمود على المكتب أرضيّته `#ebe3d2` بحشوة 14 وظلّ داخليّ من جهة المجلس، والشريط على الجوّال على الأرضيّة نفسها بمقبضه كما كان (§13-ق).
- **الرأس:** «السبّورة» 21 بوزن 700 تحتها تظليل ذهبيّ `rgba(229,196,97,.32)` من 60% إلى 88% من سطرها، وسطر صفحتها تحتها 13 بوزن 600 `rgba(243,236,220,.72)` («السؤال 7، …»)، وخطّ تحت الرأس `rgba(229,196,97,.22)`، وزرّا التوسيع والإغلاق 40 في 40 بزوايا 12 وحدّ `rgba(243,236,220,.22)` وأرضيّة `rgba(243,236,220,.06)`، وأيقونة التوسيع ذهب `#e5c461` والإغلاق عاج .8. وفي الشريط الرأس سطرٌ واحد: «السبّورة» 17 وسطرها 12.5 جنبها.
- **الخطوة حلقة على خطّ هامش:** حلقة 30 (24 في الشريط، و22 في البطاقة) حدّها `1.5px solid #e5c461` ورقمها لورا 700 بقياس 14 ذهبا، وخطّ هامش رأسيّ `1px rgba(229,196,97,.35)` بين الحلقات والكتابة، مقطعٌ لكلّ خطوة يصلها بما قبلها وما بعدها. **والحاليّة ممتلئة ذهبا برقم ليليّ `#10292d`**، وخلف سطرها `rgba(229,196,97,.10)` بزوايا 12؛ **والتي يكتبها القلم تنبض** حول حلقتها بالشفافيّة والتحويل وحدهما، وتسكن مع تقليل الحركة. وحلقةٌ حاليّة واحدة لا اثنتان، والخطوة الحاليّة تنزل إلى العين بتمرير اللوح وحده لا الصفحة.
- **المحتوى:** الكتابة 19.5 بوزن 500 وسطر 2 (16.5 في الشريط، و14.5 في البطاقة، و21 في التوسيع)، والرياضيّات ماء فاتح `#8fd0d4` بلورا 600. والرسم بلا ورقة تحته، ورموزه الأربعة تُعاد على اللوح: التمييز `#8fd0d4`، والتظليل `#e5c461`، والفخّ مرجانيّ `#f2a391` يُقرأ على الداكن، والحبر عاجيّ؛ فرسم العقل يلبس اللوح بلا مسّ عقده.
- **الذيل بين الصفحات:** سهمان 40 في 40، ونقاط (الحاليّة ذهب بعرض 18 وارتفاع 8، والباقية دوائر 8 عاجيّة .32)، و«صفحة 2 من 3» 13 بوزن 700؛ و«صفحة جديدة» زرّ ذهبيّ خفيف: أرضيّة `rgba(229,196,97,.12)` وحدّ `rgba(229,196,97,.45)` وحبر ذهب. وفي الشريط والبطاقة يغيب سطر العدد وتبقى النقاط، وبطاقة «محادثاتك» بلا «صفحة جديدة».
- **التوسيع:** اللوح نفسه فوق ستارة `rgba(10,20,24,.72)`، بعرض `min(1040px, 100%)` وارتفاع `min(880px, 100dvh - 48px)`؛ وعلى الجوّال الشاشة كلّها بلا زوايا ولا حدّ.
- **والامتداد لا يتراجع:** العمود `clamp(360px, 30vw, 540px)` بطول الشاشة، والجسم يتمرّر مع طوله، والشريط بين 150 وجوف المجلس ناقص 170.

**بيته وحارسه:** `src/styles/advisor.css` (القسم «(258) السبّورة لوح»)، و`src/core/advisor/slate.test.mjs` في البوّابة، و`tools/e2e-slate.mjs` في المتصفّح بالقيم المحسوبة على 1440 و1280 و390.

### 13-ش. الحلقة الهادئة حول وجه الرأس، وخطّ القلم (2026-09-30، الجولة 259 في بوّابة القمّة، ب-327)

**بحكم جو على لوح «المجلس 5.0»:** «القلم شكله أحسن من الكور الثلاثية الأبعاد»، و«الهالة لا تلغي حق الكبسولة المستشار»، وبعد لقطة الحلقة: «اتفق مع كل الحالات، راس الهدية ينسحب لنفس الثيم». والقيم من صفحة `States` حرفا (بنتها جلسة شقيقة ودُمجت مع §13-ر).

- **الحلقة الهادئة حول وجه الرأس** (المجلس والهديّة)، على بُعد 5 من الوجه: يسمعك تيل ينبض 2.4 ثانية (من `0 0 0 2px rgba(11,101,109,.5)` إلى `0 0 0 2px rgba(11,101,109,.75), 0 0 0 7px rgba(11,101,109,.12)`)، ويتكلّم ذهب يتنفّس 1.6 ذهابا وإيابا (من `0 0 0 2px #b8912e` إلى `0 0 0 2.5px #b8912e, 0 0 0 8px rgba(184,145,46,.18)`)، والسبّورة التنفّس نفسه وشارة قلم 26 على طرف الوجه (لؤلؤ وقلم `#8a6d1f`)، والصورة قوس ذهبيّ يدور 2.4 ثانية فوق حلقة `inset 0 0 0 2.5px rgba(184,145,46,.2)`، والردّ المكتوب حلقة ساكنة `0 0 0 1.5px rgba(11,101,109,.4)`، والانقطاع حلقة متقطّعة `2px dashed rgba(23,48,57,.3)` ووجه `grayscale(.7)` بشفافيّة .8 وزرّ «المس وجهي خلال» بعدّاده. **والنبض والتنفّس طبقتان تتبادلان بالشفافيّة** (قانون الحركة: تحويل وشفافيّة وقصّ)، لا ظلٌّ يتحرّك. والكبسولة العائمة بهالتها لا تلبسها.
- **خطّ القلم مؤشّر الشغل:** ذهب `#b8912e` سماكته 3 وطوله 40 (22 في سطر «يكتب لك على السبّورة»)، يمتدّ من اليمين في 1.8 ثانية بانحناء `cubic-bezier(.2,.7,.3,1)`: إلى 55%، ويبقى، ويخبو؛ داخل فقاعة ورق المستشار `#fffcf4` بحدّ `1.5px solid rgba(184,145,46,.5)` وزوايا 22. والكرات الثلاث متقاعدة.
- **فقاعة كلامه المكتوب** (إن فُتح المفتاح): ورق `#fffcf4` بحدّ `1.5px solid rgba(184,145,46,.7)` وزوايا 22، والكلام بتظليل `rgba(184,145,46,.24)`. **والمفتاح** جنب مبدّل الصوت، ومساره ذهب إذا فُتح، وفقاعة تعريفه ورق بحدّ ذهب خافت وذيل.
- **وحركة أقلّ:** كلّها ساكنة.

**بيته وحارسه:** `src/styles/advisor.css` (القسم «(259، ب-327) الحلقة الهادئة في رأس المجلس» وقسم مؤشّر الشغل)، و`tools/css-laws.test.mjs` في البوّابة، و`tools/e2e-majlis.mjs` في المتصفّح.

### 13-ت. اختيار المستشار: وجهان في دائرتين باسميهما (2026-09-30، الجولة 261 في بوّابة القمّة، ب-347)

**بحرف جو:** «the two characters... should appear in small circles»، و«change the names in the capsules inside the chat box to their circles with their names small».

- **في ذيل «كيف أساعدك؟»:** سطر «اختر مستشارك» 13 بوزن 700 بلون `#6b604c`، ثمّ الوجهان متجاوران بينهما 26 (22 على الجوّال)، كلّ وجه دائرة 60 (56 على الجوّال، و50 على الجوّال القصير) بحلقة لؤلؤ على وصفة أقراص الدليل (`0 0 0 3px #fffdf8, 0 0 0 4px var(--dlg-edge)` وظلّ دافئ)، واسمه تحته 14 بوزن 700 بحبر الورقة. وفي الهوفر والتركيز يرتفع الوجه 2 وتصير حلقته ذهبا `#b8912e`. **ولا زرّ مصبوغ في الذيل:** الوجهان هما الفعل، و«بعدين» ورقٌ ناهض تحتهما بعرض 260.
- **في مبدّل المجلس:** كلّ خيار دائرة وجه 28 واسمه جنبه 12 بوزن 600، بلا كبسولة ولا خلفيّة؛ الحاضر وجهه بحلقة ذهب `0 0 0 2px #fff, 0 0 0 3.5px #b8912e` واسمه بحبره 700، والآخر باهت (شفافيّة 0.7 وتشبّع 0.55) حتى يمرّ عليه المؤشّر.
- **وحركة أقلّ:** بلا ارتفاع ولا انتقال.

**بيته وحارسه:** `src/styles/advisor.css` (قسما «(261، ب-347)»)، و`src/core/advisor/guide.test.mjs` في البوّابة، و`tools/e2e-majlis.mjs` (القسم 6) في المتصفّح.

## 14. الحلقة التي تحمل رقما، وبطاقة الهديّة (2026-09-25، الجولة 160 في بوّابة القمة)

**بكلمة جو من لقطتي آيفونه:** «التناظر الصوري وسنترة الأعداد والنسب في داخل الدائرة... كانت كلها سيئة». وقِيس قبل أيّ علاج: رقم حلقة النتيجة على 13.7 بكسلا يمين مركز دائرته و10.7 فوقه على 360، وأرقام حلقات المستشار والاستراحة 8 إلى 13 بكسلا فوق مركزها ولم يشتكِ منها أحد لأنّ أحدا لم يقسها، وختم «مستشارك» على 109 إلى 124 بكسلا من محور البطاقة.

1. **الحلقة بمقاس صندوقها لا بمقاس ثابت.** الرسم بـ`viewBox` وعرضه وطوله 100%، والقوس يُدار بسمته هو دورانا واحدا فيبدأ من الثانية عشرة، ولا يُدار الرسم كلّه. ولكلّ عائلة مكوّن واحد: `ScoreRing.jsx` للنتيجة (تحديد المستوى وختام الجولات)، و`coach/Ring.jsx` للمستشار والسجلّ، وحلقة الاستراحة في `Break.jsx`.
2. **الرقم وحده في المركز، والكلمة معلّقة تحته** على نحو 64 إلى 65% من القطر، لا مجموعَين في شبكة واحدة (المجموع يرفع الرقم بنصف الكلمة).
3. **والموسَّط صندوق الحرف الكبير لا صندوق السطر:** `text-box: trim-both cap alphabetic` على الرقم، فيقع حبر الأرقام على المركز؛ والمتصفّح الذي لا يعرفها يوسّط صندوق السطر كما كان. والرقم الثابت بأرقام متناسبة، والعدّاد الذي يتبدّل تحت العين بأرقام جدوليّة (§6 معدَّلة).
4. **الحكم بموضع الحبر لا بالعين ولا بصندوق العنصر:** `tools/lib/ringMeasure.mjs` يلتقط الحلقة ويخفي قوسها ويعدّ الحبر داخل الدائرة وحدها، والشرط ±1 بكسل على 360 و390 و1280؛ ومحور البطاقة بـ`axisOf` (أسطر النصّ بمستطيلات المدى، والأختام والأزرار بصناديقها) ±1.5. والفحص يُثبت أحمر على القاعدة القديمة قبل أن يُصدَّق أخضره.
5. **بطاقة الهديّة** (`gift.css`، آخر سلسلة `main.jsx`): ورقة بيضاء بخطّ شعر، وعين «هديّتك من البوّابة» بالأزرق المخضرّ، وعنوان بخطّ العناوين 23، وسطران هادئان بأيقونتين في حلقتين يفصلهما خطّ شعر، ثمّ الزرّ الأزرق الأوّل بحرف جوجل، و«الاشتراك» ورقيّ، و«أكمل للمنصّة» رابطا. **لا سعر ولا ريال ولا فقرة شرح**: السعر بيته صفحة الباقات وحدها.
6. **رأس مكالمة الهديّة** (`GiftCall.jsx`): حلقة حول وجه المستشار نصف قطرها 46 من 100 تنقص مع الوقت بلون التركيز `#5378A0` وتدفأ إلى لون تحديد المستوى `#B5874A` في آخر عشر ثوان وحدها، وساعة `m:ss` بخطّ لورا 30 وأرقام جدوليّة، وتحتها «باقي من دقيقتيك»، و«يتّصل...» قبل أن يرفع، و«يودّعك» بعد الوداع. ولا ترجمة حيّة للكلام (قانون المالك: «الصوت كافٍ»). وبطاقة الختام «هذي عيّنة من البوّابة» بزرّين لا ثالث لهما.
7. **ميداليّة الدرجة (الجولة 185، ب-248؛ تصل مع دمجها).** بكلمة جو: «تصميمها قديم جدًا... اخترع لك تصميمًا جديدًا فعلًا يعطيك شكلًا فخمًا يليق بالمنصة ولغتها الجديدة». كلّ حلقة تحمل نسبة وجهها واحد في `ScoreMedal.jsx` و`medal.css`:
- الوجه: `radial-gradient(circle at 36% 28%, #fffefb 0, #fcf8ee 52%, #f1e8d3 100%)` على دائرة الغلاف، وظلّ `0 1px 1.5px rgba(74,63,46,.10), 0 12px 24px -13px rgba(74,63,46,.46)` (وتحت 80: `0 6px 12px -7px`). لا ظلّ داخليّ.
- في إحداثيّات 100: حافّة ذهب r 48.6 سُمك .9 `#d9c188`؛ خطّ داخليّ r 34.2 سُمك .55 `rgba(184,145,46,.34)` (الكبير وحده)؛ مدرَّج r 41 سُمك 4.6 (5.5 تحت 80) بأربعين خطّا عرض الواحد .85 (24 بعرض 1.1 تحت 80) لونه `#d5c7a4`؛ علامات الأرباع r 46 سُمك 2.8 `#ab966a`؛ القوس r 41 بسُمك المدرَّج وطرف مدوّر، وهو آخر `circle` في الرسم دائما.
- الجوهرة: قطر `max(7px, 8.5%)` على نصف قطر القوس (أعلى 9%)، بطبقة بحجم الوجه تدور `النسبة × 3.6` درجة بزمن القوس (1.1 ثانية)، وحلقة ورق `#fffdf8` 1.6 وظلّ صغير، وبريق أبيض. رسمها بيضاويّ لا `circle`.
- الرقم: لورا 700 بربع القطر (27% تحت 80)، و«%» `.46em` مرفوعة `.82em` بلون الرقم نفسه.
- النغمات (القوس / الرقم): مريميّ `#3f7354`/`#2f5a41`، مغرة `#b5874a`/`#7d5a24`، طوبيّ `#a8483f`/`#8f3a32`، ذهب `#b8912e`/`#7a5f1a`، تيل `#0e7d86`/`#0b656d`.
- **فخّان:** لون قريب من الرقم في عنصر HTML داخل الحلقة يُعدّ من حبر الرقم في القياس، فكلّ زينة ملوّنة ترسم SVG؛ وقواعد المقاس القديمة بـ`.co-ring svg` تصيب كلّ رسم داخل الحلقة، فرسم الجوهرة بمحدِّد أقوى.

## 15. رحلة ليلة الورق ومرجعيّتها البنائيّة (2026-09-25، الجولات 170 و171 و172 في بوّابة القمّة، وثّقتها 173)

**لماذا هذا القسم:** بكلمة جو بعد آخر لقطة من الليلة (22:18 بالتوقيت العالميّ): «ياسلام، هذي اللغة المطلوبة والكمال في فهم منطق التصميم، كل رحلة التعديلات هذي وثّقها بالتفصيل والمرجعية البنائية لملف لغة التصميم علشان يتطور ويكبر معنا». **فالأقسام 13-ي و13-ك و13-ل تحمل قاعدة كلّ صفحة في بيتها، وهذا القسم يحمل ما لا تحمله واحدة منها:** الرحلة عبر الصفحات بترتيبها (ماذا قال جو، وماذا كان مقيسا، وماذا صار، وما القاعدة التي تركها)، والمنطق الذي قُبل مستخلصا منها، **والوصفات بقيمها الحقيقيّة من الكود** حتّى يبني الثريد القادم صفحة بهذه اللغة دون أن يرجع إلى الشات ولا إلى اللقطات. وكلّ قيمة هنا منسوخة من ملفّها المسمّى؛ **فإن اختلف الملفّ عن هذا القسم فالملفّ هو الحقّ، ويُصحَّح هذا القسم في الجولة نفسها التي غيّرت الملفّ.**

### 15-أ. الرحلة بترتيبها

الأوقات بالتوقيت العالميّ كما في شات المشروع. وكلّ خطوة: كلمة جو بحرفها، وما كان قبلها مقيسا، وما صار، والقاعدة التي بقيت بعدها.

**1. 20:20 · ثلاث لقطات بعد نشر 168 و169 (فُرّقت على الجولتين 170 و171).**
- **بحرفه:** «ممتاز، بدأت المنصة تأخذ شكلها الذي يتكلم نفس اللغة بتناغم ومراحل ممتازة... الصورة الأولى لمكونات أزرار... فلات قديمة، لون أخضر للتاب، كلها قديمة وذائبة في الخلفية محد يقدرها. الثانية: مكون الأسئلة والإجابات الإثرائية قديم، نبنيه على نفس الإجابات التي عملناها أول الليل في قراءة المدرب... فوق مكون (التالي) يتحرك معه بنفس المسافة كل سؤال مع استمرار التحكم والسحب الحالي. الثالثة: تحديث أسئلة الكمي كخلفية وتصميم أيضا لازالت قديمة وترتيب الفلاتر بدل شكلها المزحوم بلغة ثيم خاصة قريبة من صورتها في الصفحة الرئيسية، الصورة للكمي تكون قوست في رأس القسم. المواضيع مستطيلة المفروض تكون مربعات... حلّق بإبداعك، لا تنسى التمييز وعدم ذوبان أي مكون في الآخر».
- **ما كان (منتقي الكمّيّ، `Picker.jsx`):** حاوية `.card pad` بيضاء على جسد خارج قائمة المكتب (عيب §13-هـ نفسه)؛ زرّ المكالمات حبّة بحدّ لونيّ بلا ظلّ و«الرئيسية» رابط مسطّح؛ الفلاتر حبوب تلتفّ صفّين والمختارة تعبئة طوبيّة؛ المواضيع مستطيلات بعرض أدنى 240 بمربّع رقم تيليّ.
- **ما كان (التدريب المباشر، `Runner.jsx`):** الحلّ صندوق داخل ورقة السؤال (ورق فوق ورق) برأس حكم أخضر أو أحمر مشبع، وصاعقة على الزبدة، ولا أيقونة تحمل فكرة فقرة؛ والرصيف يمين أسفل يغطّي الخيار الخامس وأسطر كلام المدرّس.
- **ما صار:** 170 (§13-ي): الصفحة على المكتب، والرأس ورقة برسم القسم شبحا، والزرّان ورق ناهض، والفلاتر مسار رمليّ، والمواضيع مربّعات برقم شبح. و171 (§13-ك): الحلّ ورقة شقيقة تحت السؤال بلغة ورقة الزيارة (§13-و)، والحاويات الإثرائيّة بنغماتها وأيقوناتها ودمغاتها، والرصيف له مقعد فوق «التالي».
- **القاعدة التي بقيت:** «لا ذوبان» ليست ذوقا يُقدَّر، بل شرطان: الورقة تُرى على مكتبها (1.08 فأكثر يقيسه الحارس)، والعنصر المختار يتميّز بالارتفاع لا بالتعبئة.

**2. 20:54 · ذيل المربّع (170).**
- **بحرفه:** «ولا داعي لكلمة كمي أو لفظي، زيادة بلا قيمة، وانقل رقم الأسئلة مكانها».
- **ما صار:** العدد وحده في أوّل الذيل.
- **القاعدة:** كلمة تتكرّر على كلّ عنصر في الصفحة لا تفرّق شيئا فتُحذف؛ يبقى في الذيل ما يختلف من عنصر لآخر.

**3. 20:58 · رفضٌ بعتاب لأوّل ورقة حلّ (171-ب، صفحة السؤال كلّها).**
- **بحرفه:** «العزل والذوبان لم تتقنه، يجب تفريق المكونات ونهوضها، كل مكونات الصفحة الباقية لم تعطيها وجه واهتمام من خلفية وانيميشن يجب أن تكون بلغة مختلفة، أزرار المكون كلها انقلها في صفحة السؤال والاختبار لفيرجن 2.0».
- **ما كان مقيسا:** نسبة الورقة إلى المكتب في لقطات 171 الأولى 1.187 و1.168 و1.217، أي فوق الحدّ بكثير، **ورُدّت مع ذلك**: الشريط وصفّ الأرقام وبطاقة السؤال كلّها بياض بظلّ واحد، والأرقام مربّعات مسطّحة، والخيارات صناديق متشابهة، وشريط التنقّل لوح أبيض فيه زرّ بلونين مكتوبين في السطر، والإنهاء إطار ذهبيّ مسطّح، وحاويات الإثرائيّ بنغمة تذوب في الرقّ.
- **ما صار:** ثلاث طبقات (ورق يُقرأ، ومكتب رمليّ غائر يُختار منه، وزرّ ورق ناهض)، وزرّ مصبوغ واحد هو «التالي»، والخيار ورق يرتفع والمختار بخطّ نغمته في قاعه، والكشف مريميّ وطوبيّ، وحاوية الإثرائيّ ورق أبيض بسكّة نغمتها في رأسها، وحركة دخول لكلّ ما يتبدّل مع السؤال.
- **القاعدة:** **رقم التباين شرط لازم لا كافٍ.** صفحة كلّ مكوّناتها ورق بظلّ واحد تذوب مكوّناتها في بعضها وإن انفصلت عن مكتبها؛ التفريق بين المكوّنات يحتاج اختلاف الطبقة (ورق، مكتب، زرّ)، والعين هي الحكم الأخير.

**4. 21:02 · لوح القوانين (172).**
- **بحرفه:** «لأننا نشتغل بنفس القسم والذي يحتوي على القوانين، انقلها لمستوى آخر وحافظ على اشتراطاتنا السابقة من ناحية حجم الخط والتصميم والأزرار، آخر القوانين كان هناك نصيحة رياضية في بدايات تطوير القسم وكانت مهمة بس أصبحت شاذة اجعلها في مكانها المناسب. تحتاج فعلا منك أجمل ما تم تصميمه لعرض القوانين الرياضية».
- **ما كان:** دفتر مربّع ملوّن تحت أوراق بيضاء (النسخة الحادية عشرة)، ولوح «أرقام تُحفظ» بعد الجذور في ذيل الصفحة، والوصلة سطر يحيل إلى رمز داخليّ («جب-18»).
- **ما صار (§13-ل):** الرأس ورقة، والمجموعة رأس على المكتب، والقانون ورقة وصيغته في **بئر رمليّة** محفورة فيها، واللوحة المفتوحة ورقة كبيرة بسابق وتالٍ، و«أرقام تُحفظ» لوح ذهبيّ بعد قوانين الأسس، والوصلة ورقة تفتح قانونها.
- **القاعدة:** **أحجام الخطّ المعتمدة عقدٌ لا يُمسّ في إعادة التصميم** (الحارس `laws-paper.test` يعدّها واحدا واحدا)؛ والارتقاء يأتي من الطبقات والوجوه لا من التكبير. **وما صار شاذّا يُنقل إلى بيته المنطقيّ، لا يُحذف.**

**5. 21:21 · مكوّن طاح بين ثريدين (172-ب، بتنبيه المنسّق).**
- **ما كان:** بطاقة القانون التي تنفتح داخل ورقة الحلّ ملكها لوح القوانين (`Laws.jsx`) وتسكن ورقة الحلّ (`Runner.jsx`)؛ 171 تركتها لأنّها ليست ملفّها، و172 لم تحسبها من نطاقها، فبقيت على اللغة القديمة.
- **ما صار:** حاوية إثراء بلغة 171 (ميزان، ودمغة، ونغمة مجموعتها، وبئر رمليّة) في ملفّ جديد `lawcard.css`، بلا سطر في `Runner.jsx`.
- **القاعدة:** مكوّن يسكن صفحة ويملكه ملفّ آخر يُسمّى مالكه صراحة لكلّ ثريد يمسّ أيّا منهما، وإلّا سقط بينهما.

**6. 21:28 · الفئات مملّة (172-ج).**
- **بحرفه:** «كل فئات القوانين تحمل نفس اللون فتخرج مملة، ميّزها وميّز حاويتها الكبيرة، ميّزها عن بعضها بلغة لون شبيهة من درجة أخرى أو نفس اللون with different shade or depth، it's your call. أيضا أسماء الفئات احترم فيها الهايراركي وكبّرها شوي».
- **ما صار أوّلا (ورُدّ في الخطوة 8):** ستّ درجات مشبعة مختارة «قريبة» من أزرق الكمّيّ (`#5378A0` و`#2B7A83` و`#5E5C9A` و`#34597C` و`#4A8C8A` و`#6E7FAE`)، والصينيّة تدرّج مسطّح من اللون ممزوجا بالرمليّ في فضاء `oklch`.
- **ما بقي منه:** كلّ فئة بدرجتها، وحاويتها صينيّة لا ورقة، واسمها 21 (19 على الجوال) بين عنوان الصفحة 23 واسم القانون 13.
- **القاعدة:** الإخوة المتجاورون يتفرّقون بالدرجة داخل عائلة لون واحدة، والاسم يأخذ درجته في الهرم.

**7. 21:51 · خلفيّة الأسئلة (171-ج).**
- **بحرفه:** «في خلفية الأسئلة؟ شكلها بعيد تماما. ركّبها بالتوزيع اللوني لكل قسم ولا تختار لون يذوب فيه التصميم، أو من غير الملائمة كفصيلة ألوان "باليت"، فكّر خارج الصندوق. الباقي ممتاز».
- **ما كان:** غسلة واحدة بلون المسار تسيل من القضيب؛ ففي النموذج بنفسجيّ رماديّ مسطّح لا علاقة له بصورة النماذج في الرئيسيّة.
- **ما صار:** كلّ مسار يلبس ألوان صورة قسمه في الرئيسيّة، مقيسة من الصورة بتكميم ألوانها بعد حذف بياض الورق، أربع درجات لكلّ مسار، مركّبة **ورق ألوان مائيّة**: بقعتان من ركنين متقابلين، وحافّة مدّ أعمق، ورذاذ، ونسيم، وطيف الصورة نفسها مضروبا في المكتب.
- **القاعدة:** **اللون يُقاس من صورة القسم ولا يُختار من البنك ولا من الذوق.** الصورة هي ما عرف الطالبُ القسمَ به في الرئيسيّة، فخلفيّته تكمل جملتها.

**8. 22:09 · رفضٌ بعتاب لألوان الفئات (172-د).**
- **بحرفه:** «معليش ودي أصارحك عجزت أرتاح لوضع خلفيات القوانين اللي ماله أي علاقة بالنموذج، ترى فكرة الشيد المختلف مميزة أيضا، ما تشطح بألوان خارج الباليت، هذي ما فيها ابتكار، لطخة سادة، فكّر بأحسن البراكتيس في هذي التدرجات، تكستشر وأي شيء مناسب».
- **ما صار:** باليت صورة الكمّيّ وحدها (الفرجار والمنقلة وكريم الورق)، زوجٌ لكلّ فئة (غسلة وحبر)، والصينيّة ورق ألوان مائيّة بلغة 171-ج نفسها، **وزاد عليها ملمسان:** مربّعات دفتر رياضيّات باهتة، وحبيبات ورق مرسومة (`feTurbulence`).
- **القاعدة:** **لا لطخة سادة.** السطح الملوّن الكبير طبقاتٌ لها منطق مادّة (ماء يجفّ، ورق له حبّ، دفتر له مربّعات)، لا لون واحد ولا تدرّج خطّيّ. وفكرة جيّدة تُرفض ألوانها لا تُرمى: الدرجة المختلفة بقيت، وتغيّر مصدرها.

**9. 22:18 · القبول.**
- **بحرفه:** «ياسلام، هذي اللغة المطلوبة والكمال في فهم منطق التصميم».
- **ما قُبل:** الصفحات الثلاث معا، واندمجت في `main` بالترتيب: 170 (`e1ac67f`) ثمّ 171 (`485e4b1`) ثمّ 172 (`aa4e1e6`)، ونُشرت بكلمته «الآن انشر» (ختم `20260926-0136`).

**10. 22:58 · بعد النشر، على الآيفون: الصفحات غير متوازنة (174، ب-237).**
- **بحرفه:** «فيه مشاكل كثير بالنشر، الصفحات غير متوازنة»، ومعها لقطة من سفاري الآيفون لصفحة اللفظيّ.
- **ما كان:** مربّعات الأقسام بعروض وأطوال مختلفة من صفّ إلى صفّ، كلّ مربّع بعرض اسمه («فقراء بريطانيا وخطر داهم» أعرض وأطول من «الاحتكاك والنجاح»)، فالصفوف لا تقف على حافّة واحدة؛ ومسار فلاتر اللفظيّ خانتان وثالثة وحيدة تحتهما. **وكلّ لقطات 170 كانت على كروم، فلم يظهر شيء من هذا قبل النشر.**
- **الجذر المقيس:** المربّع عنصر شبكة بنسبة `aspect-ratio:1/1` **بلا عرض صريح**؛ كروم يمدّه على عرض عموده، وسفاري لا يمدّ عنصر شبكة له نسبة أبعاد، فيأخذ عرضه من محتواه، والطول يتبعه بالنسبة.
- **ما صار:** عرض المربّع عرض عموده صراحة في الصفحتين، ومسار اللفظيّ الثلاثيّ صفّ واحد بثلاث خانات متساوية على الجوال، والكمّيّ بخاناته الأربع صفّان؛ مقيسا على كروم: 170×170 على 390 و190×190 على 430، بلا اسم فلتر ينكسر ولا تمرير جانبيّ. والحكم الأخير آيفون جو، لأنّ الصندوق لا يحمل ويب كِت.
- **القاعدة:** **القبول على شاشة ليس قبولا على كلّ شاشة، والنسبة بلا عرض صريح وعدٌ لا يفي به سفاري.** كلّ صفحة تُفحص بأطول محتواها على مقاسات الآيفون قبل أن تُعدّ منتهية، وكلّ عنصر بنسبة أبعاد في شبكة يحمل عرضه صراحة.

### 15-ب. المنطق الذي قُبل (ثمانية أحكام تسبق أيّ سطر)

1. **ثلاث طبقات لا تختلط:** **ورق** لما يُقرأ (`#fffdf8` بحدّه وظلّه)، **ومكتب رمليّ غائر** لما يُختار منه أو يحمل غيره (مسار الفلاتر إلّا في المنتقي حيث صار خانات ناهضة في 176-ب لأنّها تجاور زرّي الرأس فتلبس هويّتهما، شريط التنقّل، الساعة، بئر الصيغة؛ وصفّ الأرقام حتّى 177 حين صار خانات ناهضة؛ `#f2ece0` بظلّ داخليّ)، **وزرّ ورق ناهض** لما يُلمس (تدرّج ورق، إضاءة علويّة، ظلّ تلامس ثمّ عمق؛ يرتفع 1.5 عند المرور وينضغط 0.5 عند اللمس). مكوّن لا تعرف طبقته لم يُصمَّم بعد.
2. **العزل يُقاس ثمّ تحكم العين:** الورقة على مكتبها 1.08 فأكثر شرط لازم، والتفريق بين المكوّنات يأتي من اختلاف طبقاتها؛ ولقطة قبل التسليم على الجوال والعريض.
3. **التمييز بالارتفاع وخطّ القاع، لا بالتعبئة:** المختار (فلتر، رقم سؤال، خيار، تبويب موضوع) ورقةٌ ناهضة من مساره بخطّ نغمته في قاعها `inset 0 -3px 0`، والباقي شفّاف على المسار. **وزرّ مصبوغ واحد في الصفحة** (الخطوة المعتادة، «التالي»)، وكلّ زرّ آخر ورق بصفيحة أيقونة بنغمته، والذهب للعلامة والإنهاء والخروج.
4. **الحكم بنبرة الورق:** الصحّ مريميّ `#3f7354`، والغلط طوبيّ `#a8483f`، بعلامة مرسومة (✓ و×) وحرف ممتلئ وخطّ قاع، لا غسلة خضراء أو حمراء مشبعة.
5. **اللون من صورة القسم، مقيسا:** خلفيّة المسار ودرجات الفئات تُكمَّم من رسم القسم في الرئيسيّة؛ لا لون من خارج باليتها، ولا لون يذوب فيه الورق.
6. **الدرجة تفرّق الإخوة والعائلة واحدة:** العناصر المتجاورة من نوع واحد درجاتٌ من عائلة لون موضوعها، مرتّبة فلا تتجاور درجتان متقاربتان؛ وحبر الدرجة (لا غسلتها) هو ما يلوّن العنوان والسكّة والنقطة.
7. **لا لطخة سادة:** السطح الملوّن الكبير ورق ألوان مائيّة بطبقات (غسلة تسيل من ركن، حافّة مدّ حيث جفّت، غسلة ثانية في الركن المقابل، رذاذ، ملمس)، والورقة فوقه تبقى بيضاء دافئة.
8. **كلّ كلمة تفرّق، وكلّ أيقونة فكرة، وكلّ حركة تقول ما تغيّر:** ما يتكرّر على الكلّ يُحذف؛ الأيقونة قناع إس في جي بـ`currentColor`، واحدة لكلّ فكرة في المنصّة كلّها، ولا تشبه حرفا ولا رقما؛ والحركة دخولٌ قصير لما يتبدّل، وتُطفأ كلّها مع تقليل الحركة، ولا تحويل على الصفحة نفسها.

### 15-ج. المرجعيّة البنائيّة: الوصفات بقيمها

**أين تسكن الشيفرة (الحقّ عند الاختلاف):** المنتقي `src/styles/picker.css` (نطاق `.pk-page`)؛ صفحة السؤال `src/styles/product.css` في أقسامه الثلاثة المعنونة «(171)» و«(171-ب)» و«(171-ج)» (نطاق `.qscreen` و`body.inrun`)؛ لوح القوانين `src/styles/laws.css` (نطاق `.lw`) وألوان فئاته في `src/components/Laws.jsx` (`KAMI_SHADES` و`shadeOf`)؛ بطاقة القانون داخل الحلّ `src/styles/lawcard.css` (نطاق `.lwc`)؛ مقعد الرصيف `src/core/advisor/dockPos.js` (`seatOf`) و`src/components/useDockDrag.js`؛ ورموز المكتب `--desk` و`--paper-edge` و`--paper-shadow` في قسم 164 من `src/styles/coach2.css` (§13-هـ).

**1) الرموز.** تُعرَّف على نطاق الصفحة (`.qscreen` مثالها) وتُقرأ بأسمائها، ولا تُكتب القيم في القواعد مرّتين:

```css
--rp-paper:#fffdf8;                  /* الورق */
--rp-edge:rgba(176,150,96,.46);      /* حدّ الورق = --paper-edge */
--rp-desk:#f2ece0;                   /* المكتب = --desk، والورقة عليه 1.09 */
--rp-sh:0 1px 2px rgba(74,63,46,.09), 0 10px 26px -16px rgba(74,63,46,.36);          /* ظلّ الورق الساكن */
--rp-lift:inset 0 1px 0 #fff, 0 1px 2px rgba(74,63,46,.10), 0 8px 18px -10px rgba(74,63,46,.5);    /* الزرّ الناهض */
--rp-lift-h:inset 0 1px 0 #fff, 0 2px 4px rgba(74,63,46,.12), 0 14px 26px -12px rgba(74,63,46,.55); /* عند المرور */
--rp-press:inset 0 1px 2px rgba(74,63,46,.14), 0 1px 1px rgba(74,63,46,.08);           /* عند اللمس */
--rp-ok:#3f7354; --rp-bad:#a8483f; --rp-gold:#8a6d1f;                                   /* الحكم والذهب */
```

والنغمة في كلّ صفحة من سجلّها الواحد لا من هنا: `--st` في المنتقي من سجلّ المحطّات، و`--acc`/`--acc-2` في صفحة السؤال من سجلّ المسارات، و`--lt`/`--gw` في القوانين من `shadeOf`.

**2) الزرّ الورقيّ الناهض** (السابق، العلامة، الخروج، الإنهاء، المكالمات، الرئيسيّة، الرجوع):

```css
min-height:46px; border-radius:15px; color:var(--ink); font-weight:800;
background:linear-gradient(180deg, #fffefb, #fbf6ec); border:1px solid var(--rp-edge); box-shadow:var(--rp-lift);
transition:transform .18s var(--ease), box-shadow .2s, border-color .2s;
/* المرور، على أجهزة المرور وحدها @media (hover:hover) */
transform:translateY(-1.5px); box-shadow:var(--rp-lift-h); border-color:color-mix(in srgb, var(--acc) 45%, rgba(176,150,96,.46));
/* اللمس */
transform:translateY(.5px); box-shadow:var(--rp-press);
/* صفيحة الأيقونة داخله: حلقة 28 بعُشر النغمة */
width:28px; height:28px; padding:6px; border-radius:50%; color:var(--acc-2);
background:color-mix(in srgb, var(--acc) 12%, #fff); box-shadow:inset 0 0 0 1px color-mix(in srgb, var(--acc) 26%, transparent);
```

**وحالته صنف لا ستايل سطر:** العلامة المُعلَّمة `.rp-flag.on` تلبس ذهبها (`linear-gradient(180deg, #fffaf0, #f8eed6)`، وخطّ قاع `inset 0 -3px 0 #c9a13d`، وصفيحة ممتلئة `linear-gradient(180deg, #d4ae4a, #a8821f)`). والخروج والإنهاء ذهب البوّابة ورقا (`color:#6f5410`، حدّ `rgba(184,145,46,.58)`، صفيحة `#fbf1d6`).

**2-ب) أزرار صفحات القراءة (الجولة 179، ب-242)، وأرقام الختام وأبوابه (الجولة 180، ب-243)** (الختام، والقراءة، والأسئلة، والزيارة، وصفحة البناء):

- **زرّ صفحات القراءة:** وصفة §15-ج-2 نفسها على نطاق `.co`، برموز `--rb-lift` و`--rb-lift-h` و`--rb-press` و`--rb-edge`، ونغمة الصفيحة `--bt` (`#0b656d`). والصفيحة `::before` والأيقونة `::after` مطلقة فوق مركز الصفيحة، فالحشوة منطقيّة (`padding-inline`) لا مختصرة، وإلّا انزاح القناع في الاتّجاه العربيّ.
- **أرقام الختام دفترٌ واحد، واللون في الحبر لا الوجه (الجولة 180، ب-243؛ نسخت «البلاطة الناهضة» التي قرأها جو «ألوان فولدرات ويندوز 95... Squares في كل مكان»):** أربع أوراق مصبوغة بسكّة في رأسها هي عبثٌ هندسيّ ولونيّ مهما نهضت. فالأرقام **ورقة واحدة ناهضة** من عائلة الزرّ (`--rb-lift` وحدّ `--rb-edge` وزاوية 18)، وأعمدتها بلا إطار ولا ظلّ يفصلها خطّ شعر هو **فجوة 1 تُظهر خلفيّة الدفتر** (`background:var(--ghair); gap:1px`)، فيصلح الفاصل نفسه لأربعة أعمدة على العريض ولعمودين بصفّين على الجوال. وكلّ عمود: **جوهرة 10 بنغمته** (نقطة بحلقة غسلتها) قبل اسمه بحبرها، والرقم بلورا 30 بحبر الصفحة، وسطره الثاني `#5f5646`، و**خطّ قلم 4 بنسبته** يسيل من جهة البداية (`linear-gradient(to left, var(--tl) var(--p), rgba(176,150,96,.2) var(--p))`)، ووجهه ورق الزرّ بغسلة 7% من ركنه لا صبغة. **والمقارنة ذيل الدفتر لا ورقة ثانية:** خطّ شعر فوقها، والفرق كبسولة بحبر الحكم (مريميّ صاعد، طوبيّ نازل) وسهم مرسوم، و`direction:ltr; unicode-bidi:isolate` فيُقرأ «-26» لا «26-». والأحبار الصغيرة مقيسة على أغمق وجه للدفتر `#faf4e8` بـ4.5 فأكثر (الذهب `#8a6d1f` سقط عنده 4.47، فصار `#7c6217`).

```css
.co-ledger{ border-radius:18px; overflow:hidden; border:1px solid var(--rb-edge); background:var(--ghair); box-shadow:var(--rb-lift) }
.co-ledger .co-tiles{ gap:1px; grid-template-columns:repeat(4, minmax(0,1fr)) }   /* الجوال: repeat(2, …) */
.co-ledger .co-tile{ border:0; border-radius:0; box-shadow:none;
  background:radial-gradient(ellipse 70% 90% at 100% 0%, color-mix(in srgb, var(--tl) 7%, transparent) 0%, transparent 70%), linear-gradient(180deg, #fffefb, #faf4e8) }
.co-ledger .co-tile span::before{ width:10px; height:10px; border-radius:50%; background:var(--tl);
  box-shadow:0 0 0 3px color-mix(in srgb, var(--tl) 18%, #fff), 0 0 0 4px color-mix(in srgb, var(--tl) 26%, transparent) }
```

- **باب المستشار: المصبوغ الوحيد بختم ذهب لا ملصق (180):** وصفة 3 بتيل البوّابة (`#0e7d86` ثمّ `#0b656d`)، وذهبه **خطّ في قاعه** (`inset 0 -3px 0 #c9a13d`) **وختمٌ حول أيقونته** (دائرة 42 بتدرّج `#d4ae4a` ثمّ `#a8821f` وحلقة بيضاء)، وسهم تقدّم مرسوم في طرفه يتقدّم 3 عند المرور. والملصق الذهبيّ الذي كان يطلّ على حافّته يعيد سطر الزرّ نفسه، فيسكت (ما يتكرّر يُحذف، §15-ب-8).
- **المواضيع مجموعتان بعنوانيهما (180):** وسم «لفظي/كمي» الصغير على كلّ سطر (11 بكسل) صار عنوانا واحدا لكلّ مجموعة بخطّ العناوين وجوهرة قسمه وخطّ شعر تحته؛ والسطر اسمٌ كامل لا يُقصّ فوق شريطه، والعدد في ركنه بحبر القسم، والشريط خطّ قلم 6 بنغمة القسم، **والضعيف (تحت 60) طوبيّ الحكم** لا تدرّج برتقاليّ أحمر. وعلى العريض المجموعتان عمودان.
- **أرقام الأسئلة جواهر في ورق ناهض، في كلّ صفحات القراءة (180):** `.co .co-qchip` كبسولة 40 من عائلة الزرّ، والرقم فيها جوهرة 30 بغسلة التيل 11% وحدّها 30%، والملاحظة بعدها بحبر الصفحة (13، 700، `#4f4738`)؛ والرقم وحده قرصٌ ورقيّ حول جوهرته. وعند المرور ينهض وتمتلئ الجوهرة بتيلها ورقمها أبيض. حارس الوصفات كلّها `tools/reading-ledger.test.mjs`.

**2-ج) أبواب القراءة وجهٌ واحد، والقراءة الجديدة ختم ذهب (الجولة 186؛ تصل مع دمجها):**

Reading doors (answers, advisor reading, questions) are one raised-paper face everywhere (the 179 family); state is never a second face colour. Each door has an icon plate in its own tone: answers in sand ink `#6d5a36` with the document icon, the advisor in teal `#0b656d` with a speech-bubble icon. A reading that arrived and hasn't been opened is a gold seal on the same button: the plate becomes a gold radial with a gold ring, the button's border and a 3px halo take gold, a 14px gold gem sits at the inline-end top corner (white 2px ring, one entrance pulse, silent under reduced motion), and «جديدة» is read to screen readers only. Plate size and start padding are variables (`--rb-pl` 28, `--rb-ps` 18; on phones 24 and 10), and the icon mask centres on the plate by calc, so any size stays aligned. On phones the advisor column is wider (.85fr / 1.15fr) so its label never clips at 390.

**2-د) كتلة الجولة المعلّقة: الفعل الأوّل ورقة بجوهرة، والثاني هادئ (الجولة 183، ب-246؛ تصل مع دمجها):**

```css
/* «كمل»: ورقة زرّ ناهضة، ولونها في جوهرتها وخطّ قاعها لا في وجهها */
.hm-go{ display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:14px; min-height:80px; border-radius:18px; color:var(--ink);
  border:1px solid color-mix(in srgb, var(--gt) 32%, rgba(176,150,96,.46));
  background:radial-gradient(ellipse 60% 130% at 100% 0%, color-mix(in srgb, var(--gt) 9%, transparent), transparent 70%), linear-gradient(180deg, #fffefb, #fbf6ec);
  box-shadow:inset 0 1px 0 #fff, inset 0 -3px 0 var(--gt), 0 1px 2px rgba(74,63,46,.10), 0 12px 24px -12px color-mix(in srgb, var(--gt) 50%, rgba(74,63,46,.5)) }
.hm-go-gem{ width:46px; height:46px; border-radius:50%; color:#fff; background:linear-gradient(180deg, color-mix(in srgb, var(--gt) 80%, #fff), var(--gt2));
  box-shadow:0 0 0 3px #fffdf8, 0 0 0 4px color-mix(in srgb, var(--gt) 30%, transparent), 0 6px 12px -6px var(--gt2) }
.hm-go-pen{ height:4px; border-radius:99px; background:linear-gradient(to left, var(--gt) var(--p), rgba(176,150,96,.22) var(--p)) }
/* «تجاهلها»: ورق زرّ القراءة بحبر الصفحة الثاني وصفيحة × رمليّة، بلا نغمة ولا خطّ قاع */
.hm-skip{ min-height:46px; border-radius:15px; color:#5f5646; border:1px solid rgba(176,150,96,.46); background:linear-gradient(180deg, #fffefb, #fbf6ec) }
```

والنغمة من سجلّ الحارات (`--gt`/`--gt2`: النموذج `#7E5F92`، التدريب `#5378A0`، الأخطاء `#9C5E2F`، الجديد `#5C8567`، المستوى `#B5874A`). وعلى الجوال صفّان بعرض واحد، والسهم يختفي. والقاعدة: **فعلٌ أوّل على صفحة ورق لا يحتاج صبغة ليُرى؛ يكفيه الارتفاع وجوهرة الوجهة وخطّ نغمتها في القاع، والثاني بجانبه ورق بلا نغمة.**

**وتعديل 191 على «تجاهلها» (ب-255؛ تصل مع دمجها):** جو: «خيار التجاهل أيضًا ذايب... ميّزه قليلاً، وممكن يكون أقلّ عرضًا». **الثاني الهادئ لا يلبس ورق الحاوية التي يجلس فيها:** وجهه رمل أعمق درجة (`#f6efe0 → #ede1c8`، فرق 1.08 فأكثر على صدره)، بحافّة رمل `rgba(138,109,58,.52)` وحبر `#4f4535`، وصفيحة أيقونته محبّرة مملوءة (`#7d6f57 → #5a4e3c`) بعلامة بيضاء وحلقة ورق؛ بلا نغمة ولا خطّ قاع، فالأوّل يبقى «كمل» وحده. **وعلى الجوال الثاني بمقاسه في الوسط** (`align-self:center; width:auto; min-width:164px`) تحت الأوّل لا بعرضه: الثاني العريض يُقرأ فعلا منافسا.

**2-هـ) خيار السؤال لؤلؤ ينهض عن ورقته (الجولة 190، ب-254؛ تصل مع دمجها):** جو: «خيارات الأسئلة تقريبًا ذائبة... السؤال يكون وزنها أعلى قليلاً بحيث أنها تبان واضحة على الجوال».

- **الوجه أبيض من أوّله لآخره** (`#ffffff` إلى `#fffffe`): لا درجة فيه أغمق من ورقته. **«ناهض» يُقاس بدرجة قاع الوجه لا بظلّه:** التدرّج الذي يغمق نحو قاعه (كان `#fcf8ef` على ورقة `#fffdf8`) يغوص مهما كان ظلّه.
- **الحدّ** `rgba(150,122,72,.5)` ومعه حلقة بيضاء خارجيّة بكسلا واحدا، **والظلّ بطبقتين:** تماسّ `0 1px 2px rgba(74,63,46,.13)` وعمق `0 9px 18px -11px rgba(74,63,46,.55)`، ولمعة `inset 0 1px 0 #fff`.
- **الكتابة 600 بحبر `#15242c`**، و16 على الجوال بدل 15، وحلقة الحرف 48% من نغمة المسار.
- **المختار والصحيح والغلط** نغماتهم على الوجه الأبيض نفسه (`linear-gradient(180deg, #ffffff, <نغمة> 8-10%)`)، والباهت كما كان. القاعدة في آخر `product.css` تحت «(190)» على `.qscreen .qbody .choice`، وحارسها `tools/run-expl.test.mjs`.

**2-و) بطاقة الانتظار (الجولة 196، ب-260؛ تصل مع دمجها):** ورقة الصفحة بلطخة نغمة المحاولة في ركن السكّة (`radial-gradient` 46%×72% عند
100% 0، النغمة 13% ثمّ 4%)، والعنوان بخطّ العناوين وخطّ قلم. المحطّات عملات ورق ناهضة 36 بكسل (#fffefb إلى #fbf6ec، وظلّ
الخانة الناهضة)؛ المقطوعة مملوءة بالنغمة، والحاليّة ورق بخطّ قاع `inset 0 -3px 0` بالنغمة وحلقة 5 بكسل تنبض بالنغمة لا
بالتيل. الرقم أوّل ما تقع عليه العين (40، و36 على الجوال، و46 على الدسك توب) و«%» بنصف حجمه، و«تقدير» كلمة بجوهرة
بالنغمة لا كبسولة. الشريط خيط 6 بكسل بلا إطار ولا ظلّ داخليّ، تركب رأسَه جوهرة 16 بكسل بحلقة 3 بالنغمة، وتحته سطر
الزمن: مضى يمينا والباقي يسارا. لا خطّ فاصل داخل الورقة: المسافة تفصل. وعلى 900 فما فوق عمودان: المحطّات في البداية
والرقم مقابلها. والسقوط لا صندوق ورديّ: سطر بخطّ طوبيّ `#a8483f` في بدايته.

**2-ز) الشارة: وجه واحد في التطبيق كلّه، وبيت واحد (الجولة 203، ب-267):** جو عن رأس القراءة: «إشارة جاهزة وإشارة قوة، تاغات قديمة خضراء بالتصميم القديم»، وعن لوحة القيادة: «خاصّة أنّه التاجات». فالشارة لا تُرسم في كلّ سطح من جديد: **وجهها في `src/styles/gem.css` وحده** (قبل المنتقي في السلسلة)، والسطح يضعها في مكانها (هامش، ترتيب، محاذاة) ولا يصبغها. وحارسها `tools/gem.test.mjs` يرفض أيّ ملفّ نمط آخر يمسّ خلفيّتها أو حدّها أو ظلّها أو حبرها أو حشوتها أو خطّها، **باسمها أو باسم أيّ صنف يسكن معها على العنصر** (الحارس يقرأ رفاقها من الكومبوننتات: `co2-pill` اليوم، ومقبض اللوحة غدا)، فالرفيق مقبض مكان وحده. ولون جوهرتها وحده يجوز لسطح أن يعطيه نغمته (`--gm`).

- **شارة الحال** `<span class="gem-chip" data-gem="…">كلمة</span>`: ورقة صغيرة ناهضة من عائلة الخانة الناهضة، والكلمة بحبر الصفحة، والحال **جوهرة 8 بكسل قبل الكلمة** بلونها. تُقرأ ولا تُلمس: لا مرور ولا ضغط، وما يُلمس زرّ من طبقات الأزرار.

```css
padding-block:5px; padding-inline:12px 13px; border-radius:999px; font-size:12.5px; font-weight:800; color:var(--ink);
border:1px solid rgba(176,150,96,.42); background:linear-gradient(180deg, #fffefb, #fbf6ec);
box-shadow:inset 0 1px 0 #fff, 0 1px 2px rgba(74,63,46,.10), 0 6px 12px -8px rgba(74,63,46,.45);
/* الجوهرة: */ background:radial-gradient(circle at 35% 30%, color-mix(in srgb, var(--gm) 35%, #fff), var(--gm) 70%);
box-shadow:0 0 0 2.5px color-mix(in srgb, var(--gm) 16%, transparent);
```

| `data-gem` | معناه | الجوهرة |
|---|---|---|
| `ok` | سليم، جاهزة | مريميّة `#3f7354` |
| `alert` | انتبه، سقطت | طوبيّة `#a8483f`، **والكلمة وحدها هنا بحبر طوبيّ `#8a3831`** |
| `watch` | راقب | كهرمان `#b36b2c` |
| `chance` | فرصة | ذهب `#b8912a` |
| `wait` | على الطاولة، محفوظة لبكرة | ذهب `#b8912a` |
| `run` | يقرأ الحين | تيل `#0b656d` ينبض كلّ 2.2 ثانية، ويسكن لمن طلب حركة أقلّ |
| `new` | جديدة | ختم ذهب 10 بكسل (ختم 186) وحدّ مذهّب |
| `nodata` | بلا بيانات | حلقة أردوازيّة `#64748b` جوفاء: ما قيس شيء |
| `off` | وقّفتها | جوهرة باهتة `#9aa39f` |
| بلا قيمة | - | جوهرة خافتة، لا «سليمة» كاذبة |

  والكلمة الصغيرة بعد الحال (`<small>`، «· قبل 3 أيّام») بحجم الشارة لا أصغر (قانون الـ12) وبحبر خافت. **والأيقونة اختيار السطح:** `svg` ابن مباشر يصير هو الجوهرة بلونها وتسقط النقطة. فإن كانت بجنب الشارة حلقة تحمل أيقونة الحال نفسها (بطاقات الضوء في اللوحة) فالشارة بنقطتها ولا تتكرّر الأيقونة، وإن وقفت الشارة وحدها في سطر (قائمة الفحوص) فأيقونتها جوهرتها.
- **شارة الفرق** `<span class="gem-delta" data-trend="good|bad|flat" data-dir="up|down|flat" aria-label="زاد 232%">232%</span>`: **جملة لا شارة**، بلا خلفيّة ولا حدّ ولا حشوة. سهم مثلّث 9×8 مرسوم قبل الرقم في اتّجاهه (`clip-path`، والنازل مقلوب)، **ولونه بالمعنى لا بالاتّجاه**: زيادة الكلفة طوبيّة ونقص الحسابات طوبيّ، وزيادة الزوّار مريميّة، والمحايد خافت. والرقم بحبر الصفحة بأرقام متساوية العرض، والسيّئ وحده بحبر طوبيّ. والثابت كلمة خافتة بلا سهم («مثل أمس»). **والرقم وحده في النصّ:** السهم مرسوم، فلا «↑» في النصّ، والعنصر يحمل `aria-label` بكلمة الاتّجاه لأنّ السهم المرسوم لا يُقرأ.
- **وسم السطر الذي يعيد عنوان بطاقته يُحذف**، وتحلّ مكانه جوهرة 10 بكسل على أوّل السطر (`.co2-gem`، مخفيّة عن قارئ الشاشة) بنغمة البطاقة: مريميّة في «اللي ثابت عندك»، ونغمة المحاولة في «إشارات»؛ والأسطر يفصلها خيط شعر `var(--ghair)`. والوسم الذي يفرّق بين نوعين في بطاقة واحدة (إشارة وفجوة في الختام) يبقى كلمة ساكنة بلا كبسولة (وصفة 180).
- **وجه قديم يُحذف، لا يُغلب:** السطح الذي كانت له رقاقة مصبوغة يحذف قاعدتها حين يلبس الشارة. وملفّ اللوحة (`admin.css`) يُحمَّل مع حزمتها بعد السلسلة كلّها، فقاعدة قديمة باقية بصنف على العنصر تغلب الوجه الواحد بترتيبها. **وفي لوحة القيادة** (208 تطبّقها بعد دمج 203): `StateChip` يرسم `gem-chip` بـ`data-gem={state}` (الحالات الخمس أسماؤها نفسها)، و`Tile` يرسم `gem-delta` بـ`data-trend={d.tone}` و`data-dir={d.dir}` والرقم بلا سهمه، و`.adm-state` و`.adm-delta` يُحذفان؛ ورموز الحال فيها (`--adm-alert` وأخواتها) تأخذ قيم الجوهرة، فتكون الحلقة والجوهرة في البطاقة الواحدة لونا واحدا. والعيّنة في `handoff/203-shots/gem-*-admin-sample.png`.

**3) الزرّ المصبوغ الوحيد** («التالي»):

```css
min-height:48px; border-radius:15px; color:#fff; border:1px solid var(--acc-2);
background:linear-gradient(180deg, color-mix(in srgb, var(--acc) 84%, #fff) 0%, var(--acc) 48%, var(--acc-2) 100%);
box-shadow:inset 0 1px 0 rgba(255,255,255,.35), 0 1px 2px color-mix(in srgb, var(--acc-2) 45%, transparent),
  0 12px 22px -12px color-mix(in srgb, var(--acc-2) 85%, transparent);
/* سهمه قناع 18 يتقدّم 3 بكسلات عند المرور، والسهم مرسوم لا محرف */
```

**4-ب) خانة الفلتر الناهضة (فلاتر المنتقي منذ 176-ب؛ نسخت الوصفة 4 فيه وحده):**

```css
/* الصفّ: لا حوض */
gap:10px; padding:0; background:none; box-shadow:none;
/* الخانة: ورقة زرّ المكالمات */
min-height:58px; padding:8px 14px 8px 10px; border-radius:15px; background:linear-gradient(180deg, #fffefb, #fbf6ec);
border:1px solid var(--paper-edge); box-shadow:inset 0 1px 0 #fff, 0 1px 2px rgba(74,63,46,.10), 0 8px 18px -10px rgba(74,63,46,.5);
/* الجوهرة 30: غسلة النغمة 11% وحدّها 30%، ونقطتها 10 بحدّ 2 */
/* المختارة: غسلة النغمة 10% من ركنها على #fffdf8، وخطّ النغمة في القاع، والجوهرة معبّأة بنقطة بيضاء */
box-shadow:inset 0 1px 0 #fff, inset 0 -3px 0 var(--ft), 0 1px 2px rgba(74,63,46,.12), 0 10px 20px -10px color-mix(in srgb, var(--ft) 55%, rgba(74,63,46,.5));
/* ثلاث خانات في 390: الجوهرة تنكمش إلى نقطتها 12 فيسع الاسم */
```

**4) المسار الرمليّ وخانته المختارة** (مواضيع القوانين، السابق والتالي في اللوحة؛ وكان لفلاتر المنتقي حتّى 176-ب، ولصفّ الأرقام ولمرشّحي «أسئلتك» حتّى 177 فصار لهما 4-ج):

```css
/* المسار */
padding:6px; gap:6px; border-radius:18px; background:var(--desk, #f2ece0);
box-shadow:inset 0 1px 2px rgba(74,63,46,.12), inset 0 0 0 1px rgba(176,150,96,.18);
/* الخانة: شفّافة، نقطة بنغمتها ثمّ الاسم (14.5، 800) ثمّ العدد سطرا ثانيا (12.5، 600) */
min-height:58px; padding:9px 12px; border-radius:13px; background:transparent; border:1px solid transparent;
/* المختارة: ورقة ناهضة بخطّ نغمتها في القاع، لا تعبئة */
background:#fffdf8; border-color:color-mix(in srgb, var(--ft) 38%, rgba(176,150,96,.46));
box-shadow:inset 0 -3px 0 var(--ft), 0 1px 2px rgba(74,63,46,.10), 0 8px 16px -10px rgba(74,63,46,.5);
```

على الجوال خانتان في الصفّ (`repeat(2, minmax(0,1fr))`)، والمسار ذو الخانات الثلاث صفّ واحد بثلاثة أعمدة (الوصفة 9). **وقاعدة 170 «الوحيدة في آخر صفّ تأخذه كلّه» (`:last-child:nth-child(odd){ grid-column:1 / -1 }`) حُذفت في 174** لأنّها تركت خانة «الباقي» تحت اثنتين على الآيفون. والمحور التابع تحته صار ورقتين ناهضتين بلا حوض (4-د).

**4-ج) صفّ الأرقام ومرشّحا «أسئلتك»: خانات ناهضة على الورقة، والمجاب جوهرة معبّأة (177، ب-240)** - بحرف جو بلقطة صفّ الأرقام: «حاوية داخل حاوية... وينطبق عليها نظام المحفور. السؤال اللي ينتهي يجب أن يكون معلَّمًا وليس مظللًا تظليلًا خفيفًا... بلغتنا التصميمية الجديدة ولكن باقتباس من الشكل السابق». فلا حوض داخل الورقة: الخانات تقف عليها بفجوة 6، و**المجاب يعود معبّأً بنغمة المسار ورقمه أبيض كما كان قبل الورق** (الاقتباس)، لكن بتدرّج الجوهرة وظلّها لا تعبئة مسطّحة:

```css
/* الخانة (نطاق .qscreen .pdots .dot) */
background:linear-gradient(180deg, #fffefb, #fbf6ec); border:1px solid rgba(176,150,96,.42);
box-shadow:inset 0 1px 0 #fff, 0 1px 2px rgba(74,63,46,.10), 0 6px 12px -8px rgba(74,63,46,.45);
/* المجاب */
color:#fff; border-color:var(--acc-2); background:linear-gradient(180deg, color-mix(in srgb, var(--acc) 86%, #fff), var(--acc-2));
/* الحاليّ: ينهض 2 بخطّ نغمته في قاعه؛ والمجاب الحاليّ معبّأ بحلقة نغمته حوله */
transform:translateY(-2px); box-shadow:inset 0 -3px 0 var(--acc), ...;
box-shadow:0 0 0 2px #fffdf8, 0 0 0 3.5px var(--acc), ...;
/* خطّ التقدّم شعرة على الورق لا مجرى: height:4px; background:rgba(176,150,96,.2); box-shadow:none */
```

ومرشّحا «أسئلتك» (`.co2-qp .co-seg`) خانات من عائلة 4-ب بنغمة المحاولة `--tt`: جوهرة 9 حلقةً، والمختارة بغسلة ركنها وخطّ قاعها وجوهرتها معبّأة. والحارس `tools/qnav-paper.test.mjs`.

**4-د) المحور التابع: ورقتان على قدّ كلامهما بلا حوض (الجولة 204، ب-268؛ تصل مع دمجها)** - جو: «مندمج تصميميًا مع الحاوية حقته. اجعلها مقتصرة على هذين الاثنين، وصغرهم بحيث لا يكونون على كامل عرض الحاوية». مفتاح من خانتين تحت مسار فلاتر («بالمواضيع / بالأقسام» تحت ورقتي الأقسام الحمراء والمفكّر، `.pk-page .ef-row.pk-axis`): يبدأ من طرف ورقته بعرض محتواه ولا يُمطّ؛ بلا حوض ولا ظلّ غائر؛ وكلّ خانة كبسولة ورق ناهض ارتفاعها 40 بجوهرة حلقة 10 بنغمة مجموعتها، والمختارة ورقتها مغسولة بنغمتها وجوهرتها معبّأة بحلقة ضوء. أصغر من خانات المسار لأنّه تابع لها.

```css
justify-self:start; width:max-content; max-width:100%; gap:8px; background:none; box-shadow:none;
```

**والفخّ الذي ولّده:** الأب `.pk-filters` شبكة، والشبكة تمدّ ابنها على خانتها وإن كان `inline-flex`، فالمحور ظهر على كامل العرض ولا خطأ في قاعدته. العرض يُقاس في المتصفّح (248×40 على 390 و430 و1280 و1440)، لا يُقرأ من `display`. والحارس `tools/picker-paper.test.mjs` يرفض المطّ والحوض.

**5) الخيار بلاطة ترتفع، وكشفه** (نطاق `.qscreen .qbody .choice`):

```css
background:linear-gradient(180deg, #fffefb, #fcf8ef); border:1px solid rgba(176,150,96,.4);
box-shadow:inset 0 1px 0 #fff, 0 1px 2px rgba(74,63,46,.07), 0 6px 14px -10px rgba(74,63,46,.4);
/* المختار */
border-color:color-mix(in srgb, var(--acc) 55%, transparent);
box-shadow:inset 0 -3px 0 var(--acc), 0 1px 2px rgba(74,63,46,.1), 0 10px 20px -12px color-mix(in srgb, var(--acc-2) 70%, transparent);
/* الكشف: خطّ قاع وحرف ممتلئ بالمريميّ أو الطوبيّ، والباقي يهدأ */
box-shadow:inset 0 -3px 0 var(--rp-ok), 0 10px 20px -14px color-mix(in srgb, var(--rp-ok) 80%, transparent);
.lock.dim{ opacity:.6; box-shadow:none; background:#fdfaf3 }
```

الحرف حلقة بعُشر النغمة (`color-mix(in srgb, var(--acc) 10%, #fff)` وحدّ داخليّ 1.5)، وتمتلئ بتدرّج النغمة حين يُختار. **ولا حجم خطّ يتغيّر على نصّ سؤال أو خيار** (الحارس يعدّها).

**6) ورقة الحلّ الشقيقة** (نطاق `.qscreen .xp`، تحت `.qbody` وقبل `.qnav`):

```css
margin-top:16px; border-radius:22px; border:1px solid rgba(184,145,46,.46);
background:radial-gradient(ellipse 46% 60% at 100% 0%, rgba(229,196,97,.2) 0%, rgba(229,196,97,.06) 55%, transparent 100%),
  linear-gradient(180deg, #fffcf3, #fdf7e8);
box-shadow:0 1px 2px rgba(74,63,46,.09), 0 10px 26px -16px rgba(74,63,46,.36), 0 22px 44px -30px rgba(74,63,46,.5);
/* رأس الحكم: حلقة 30 بلون الحكم وعلامة مرسومة، وخطّ شعر ذهبيّ تحته */
--xp-v:var(--xp-bad); .ok{ --xp-v:var(--xp-ok) }
background:var(--xp-v); box-shadow:0 0 0 3px #fffcf3, 0 0 0 4.5px color-mix(in srgb, var(--xp-v) 35%, transparent), 0 6px 14px -6px var(--xp-v);
border-bottom:1px solid rgba(184,145,46,.3);
```

وداخلها: «الحلّ» بمفتاح، والفكرة رأس بخطّ شعر `rgba(184,145,46,.26)`، والخطوات خيط ذهب (`linear-gradient(180deg, rgba(184,145,46,.5), rgba(184,145,46,.18))` بعرض 2) بحلقات ورق، والمصدر توقيع بعد خطّ شعر.

**7) الحاوية الإثرائيّة بدمغتها** (الزبدة، الخدعة، كلام المدرّس، القانون؛ ومثلها حاويات لوحة القانون وبطاقته):

```css
--et:<نغمة الفكرة>; --ei:<أيقونة الفكرة>;
margin-top:14px; padding:12px 16px 13px; padding-inline-end:58px; border-radius:14px;
border:1px solid color-mix(in srgb, var(--et) 42%, rgba(176,150,96,.3));
background:radial-gradient(circle at 0% 0%, color-mix(in srgb, var(--et) 26%, transparent) 0, color-mix(in srgb, var(--et) 9%, transparent) 38px, transparent 92px),
  linear-gradient(180deg, #fff, #fffdf9);
box-shadow:inset 0 3px 0 color-mix(in srgb, var(--et) 70%, #fff), 0 1px 2px rgba(74,63,46,.10), 0 14px 26px -16px rgba(74,63,46,.6);
/* الدمغة: الأيقونة نفسها 40 مائلة باهتة في الركن البعيد عن العنوان */
::after{ inset-block-start:7px; inset-inline-end:8px; width:40px; height:40px; background:var(--et); opacity:.2; transform:rotate(-10deg);
  mask:var(--ei) center / contain no-repeat }
/* العنوان: الأيقونة 17 بحبر النغمة color-mix(in srgb, var(--et) 78%, #1f1a12) */
```

| الفكرة | النغمة `--et` | الأيقونة |
|---|---|---|
| الزبدة | `#b8912e` | مصباح `--ico-bulb` |
| الخدعة والفخّ | `#a8483f` | مثلّث تنبيه `--ico-warn` |
| كلام المدرّس | `#8a7247` | فقاعة كلام `--ico-quote` |
| قانون السؤال | `#0e7d86` (وفي بطاقة القانون نغمة مجموعته) | ميزان `--ico-scale` |
| الحلّ | ذهب `#8a6d1f` | مفتاح `--ico-key` |
| مثال القانون | نغمة مجموعته | قلم |
| «وفي الاختبار» | ذهب | راية |
| الإحالة إلى قانون | نغمة وجهته | وصلة |

الأيقونات أقنعة إس في جي مضمّنة في المتغيّرات (`viewBox 0 0 24 24`، خطّ 1.9، أطراف مستديرة)، منسوخة حرفا من ورقة الزيارة (§13-و)، والحارس `run-expl.test` يقارن النسختين فلا تفترقان.

**8) البئر الرمليّة للصيغة** (نطاق `.lw`، ومثلها في `.lwc`):

```css
display:block; text-align:center; border-radius:12px; background:var(--desk, #f2ece0);
box-shadow:inset 0 1px 3px rgba(74,63,46,.13), inset 0 0 0 1px rgba(176,150,96,.2);
/* المرور على الورقة يشتدّ حدّها: inset 0 0 0 1px color-mix(in srgb, var(--lt) 26%, transparent) */
/* الأسّ بحبر المجموعة: sup{ color:var(--lt) }، والكسر المكدّس يوسّع البئر: :has(.frac){ padding-block:10px 12px; line-height:2.1 } */
/* بئر الحفظ الذهبيّة: background:#f6efdc; inset 0 1px 3px rgba(122,91,21,.14), inset 0 0 0 1px rgba(184,145,46,.2) */
```

**9) المربّع برقم شبح** (مواضيع المنتقي؛ وأصله الرقم الشبح في §13):

```css
aspect-ratio:1 / 1; padding:16px 16px 14px; border-radius:22px; display:flex; flex-direction:column; gap:8px;
width:100%; min-width:0; justify-self:stretch; align-self:start;  /* (174) لا تُحذف: بدونها يأخذ سفاري العرض من طول الاسم */
background:radial-gradient(ellipse 60% 55% at 100% 0%, color-mix(in srgb, var(--tt) 11%, transparent), transparent 70%), #fffdf8;
::after{ content:attr(data-n) / ""; left:12px; bottom:-30px; font-size:118px; color:var(--tt); opacity:.14 }  /* 100 على الجوال */
/* الاسم بخطّ العناوين 21 (18 على الجوال)، ثلاثة أسطر على الأكثر، وخطّ قلمه 16% من نغمة مجموعته؛ والذيل margin-top:auto */
```

عمودان على الجوال (`repeat(2, minmax(0,1fr))`، فجوة 12)، و`minmax(172px, 1fr)` على العريض. **ومسار الفلاتر على الجوال** عمودان، إلّا مسارا بثلاث خانات فصفّ واحد بثلاثة أعمدة (`.pk-track:has(> .pk-f:nth-child(3):last-child){ grid-template-columns:repeat(3, minmax(0,1fr)) }`، وحشوة الخانة `8px 8px`)، فلا تبقى خانة وحيدة تحت اثنتين. (القيم من فرع الجولة 174 قبل دمجه؛ الملفّ `src/styles/picker.css` هو الحقّ.)

**10) رأس الصفحة بشبح رسمها** (المنتقي، ويصلح لكلّ صفحة لها رسم في الرئيسيّة):

```css
/* الرسم نفسه من بطاقة القسم في الرئيسيّة (artOf) خلف الكلام، في الجهة البعيدة */
position:absolute; z-index:-1; top:-6px; left:-6px; width:32%; object-fit:contain; object-position:left top;
mix-blend-mode:multiply; opacity:.34;
mask-image:radial-gradient(120% 120% at 0% 0%, #000 55%, transparent 100%);
/* والكلام في عمود 66% لا يعبر إليه؛ وعلى الجوال: width:30%; height:92px; opacity:.3، والعنوان 72% */
```

**11) خلفيّة المسار: ورق ألوان مائيّة من صورة القسم** (`body.inrun::before`، والقضيب `::after`):

```css
background:
  radial-gradient(62% 48% at 96% 6%, color-mix(in srgb, var(--pg1) 92%, transparent), color-mix(in srgb, var(--pg1) 40%, transparent) 46%, transparent 72%), /* بقعة غالبة من القضيب */
  radial-gradient(64% 50% at 96% 6%, transparent 63%, color-mix(in srgb, var(--pg3) 26%, transparent) 69%, transparent 74%),  /* حافّة المدّ */
  radial-gradient(58% 44% at 4% 96%, color-mix(in srgb, var(--pg2) 96%, transparent), color-mix(in srgb, var(--pg2) 45%, transparent) 50%, transparent 76%), /* البقعة الثانية */
  radial-gradient(circle at 4% 62%, color-mix(in srgb, var(--pg3) 60%, transparent) 0 4px, transparent 5px),   /* رذاذ */
  radial-gradient(circle at 7.5% 58%, color-mix(in srgb, var(--pg3) 45%, transparent) 0 2.5px, transparent 3.5px),
  radial-gradient(circle at 2.5% 55%, color-mix(in srgb, var(--pg3) 40%, transparent) 0 2px, transparent 3px),
  radial-gradient(80% 60% at 50% 55%, color-mix(in srgb, var(--pg1) 24%, transparent), transparent 70%),        /* نسيم يمنع انقسام المكتب */
  linear-gradient(color-mix(in srgb, var(--pg-base) 80%, transparent), color-mix(in srgb, var(--pg-base) 80%, transparent)), /* ستار */
  var(--pg-art) no-repeat left 2vw bottom 2vh / min(34vw, 380px) auto,                                          /* طيف الصورة */
  var(--pg-base);
background-blend-mode:normal, normal, normal, normal, normal, normal, normal, normal, multiply; /* الصورة وحدها بالضرب */
/* القضيب: linear-gradient(180deg, var(--pg3), var(--lane)) */
```

| المسار (صنف الجسد) | الصورة | `--pg-base` | `--pg1` | `--pg2` | `--pg3` |
|---|---|---|---|---|---|
| الافتراضيّ | بلا | `#f3ede2` | `#dcd3c2` | `#ece4d2` | `#b9a98d` |
| التدريب المباشر، كمّيّ (`runlane-focus.runpart-kami`) | الفرجار والمنقلة `kami.webp` | `#eff0ee` | `#c8d3e3` | `#d3e5e4` | `#95a4bb` |
| التدريب المباشر، لفظيّ (`runpart-lafzi`) | الدفتر والمحبرة `lafzi.webp` | `#f1efe6` | `#cbdbd6` | `#e8e2c8` | `#8da4a3` |
| النماذج (`runlane-model`) | الساعة الرمليّة `models.webp` | `#f3ede8` | `#d3c1db` | `#ecd6d6` | `#9a819b` |
| الأخطاء والاختبار والإقفال | الدفتر الجلديّ `errors.webp` | `#f4ece1` | `#dfc6a8` | `#f0ddd3` | `#b39172` |
| الجديدة (`runlane-fresh`) | البرعم `fresh.webp` | `#f2f0e4` | `#c9d9b3` | `#efeccd` | `#8fa883` |
| تحديد المستوى (`runlane-placement`) | الجبل `level.webp` | `#f5eddf` | `#efd2a1` | `#f7e5c9` | `#cd9f68` |

**ومنطق الدرجات الأربع:** `--pg-base` مكتب شبه محايد يحمل صبغة الصورة الخفيفة، و`--pg1` و`--pg2` لوناها الغالبان خافتين، و`--pg3` درجتها العميقة (للحافّة والرذاذ والقضيب). و`Runner.jsx` يضع `runpart-kami` أو `runpart-lafzi` بأغلب أسئلة الجولة. **مسارٌ جديد يأخذ صورته من الرئيسيّة وتُقاس درجاته الأربع منها، ولا تُخترع.** والحدّ: ورقة السؤال فوق هذي الخلفيّة 1.08 فأكثر، تُقاس من بكسلات اللقطة لا من قيم الأنماط.

**12) صينيّة الفئة: ورق ألوان مائيّة بملمس** (نطاق `.lw .lw-group`، والزوج من `shadeOf`):

```css
padding:14px 18px 18px; border-radius:24px;
background:
  var(--lw-grain),  /* حبيبات ورق: svg فيه feTurbulence fractalNoise baseFrequency .9، numOctaves 2، ألفا .09، بلاطة 160 */
  radial-gradient(44% 68% at 100% 0%, color-mix(in srgb, var(--gw) 96%, transparent), color-mix(in srgb, var(--gw) 46%, transparent) 48%, transparent 76%), /* الغسلة من ركن البداية */
  radial-gradient(46% 70% at 100% 0%, transparent 72%, color-mix(in srgb, var(--lt) 13%, transparent) 76%, transparent 81%),  /* حافّة المدّ بالحبر */
  radial-gradient(55% 60% at 0% 100%, color-mix(in srgb, var(--gw) 70%, transparent), transparent 72%),   /* الغسلة الثانية */
  radial-gradient(circle at 5% 14%, color-mix(in srgb, var(--lt) 26%, transparent) 0 3.5px, transparent 4.5px), /* رذاذ */
  radial-gradient(circle at 8% 9%, color-mix(in srgb, var(--lt) 20%, transparent) 0 2px, transparent 3px),
  repeating-linear-gradient(0deg, color-mix(in srgb, var(--lt) 7%, transparent) 0 1px, transparent 1px 24px),  /* مربّعات الدفتر */
  repeating-linear-gradient(90deg, color-mix(in srgb, var(--lt) 7%, transparent) 0 1px, transparent 1px 24px),
  color-mix(in srgb, var(--gw) 22%, #f6f2e8);
border:1px solid color-mix(in srgb, var(--lt) 24%, transparent); border-inline-start:4px solid color-mix(in srgb, var(--lt) 82%, transparent);
box-shadow:inset 0 1px 0 rgba(255,255,255,.6), 0 1px 2px rgba(74,63,46,.06), 0 14px 30px -24px color-mix(in srgb, var(--lt) 60%, transparent);
/* اسم الفئة: خطّ العناوين 21 (19 جوالا) بحبر color-mix(in srgb, var(--lt) 78%, #1a1610)، وخطّ قلمه 24% */
/* وكلّ ورقة قانون فيها تحمل خطّا علويّا 3 بكسل بحبر فئتها (opacity .75) يربطها بصينيّتها */
```

| ترتيب الفئة | الغسلة `w` | الحبر `d` | من الصورة |
|---|---|---|---|
| 1 | `#c8d3e3` | `#5b7092` | رماديّ أزرق: جسم الفرجار |
| 2 | `#d3e5e4` | `#4d7f80` | رماديّ مخضرّ: المنقلة |
| 3 | `#e6dcc6` | `#8a7550` | كريم الورق وحبره البنّيّ |
| 4 | `#b9c6da` | `#46597a` | الأزرق في عمقه |
| 5 | `#cfdedb` | `#5f8a86` | المخضرّ في عمقه |
| 6 | `#d8dbe4` | `#6d7690` | الرماديّ البارد |
| الجذور (نغمة `teal`) | `#cfe1dc` | `#0b656d` | تيل البيت |

الزوج يُحسب بموضع الفئة في موضوعها (`shadeOf(topic, key)`)، فاللوح واللوحة والإحالة والبطاقة داخل السؤال يلبسون الحبر نفسه. **والمزج مع الشفّاف بـ`srgb` لا بـ`oklch`** (الفخّ 4 أدناه).

**13) مقعد الرصيف فوق الزرّ المتقدّم** (`seatOf(anchor, column, dock, view, gap = 10)`):
- العنصر يحمل `data-dock-anchor` بمفتاح سؤاله. المقعد فوقه بمسافة 10 على حافّته البعيدة عن الكلام؛ وإن اتّسع الهامش بجنب العمود على العريض (عرض الرصيف ومسافتان) جلس فيه بمحاذاة قاع المرساة.
- يُعاد حسابه على التمرير (بإطار رسم واحد) وتغيّر الشجرة والتحجيم معا، لأنّ «التالي» لاصق على الجوال. وحين يتغيّر المفتاح ينزلق إلى مقعده الجديد؛ والسحب حرّ داخل المفتاح الواحد ولا يُكتب على الجهاز من صفحة السؤال. وقيس: تغطية صفر، والمسافة 10 على 360 و390.

**14) الحركة:**

```css
@keyframes rpDrop{ from{ opacity:0; transform:translateY(-6px) } to{ opacity:1; transform:none } }  /* الشريط .45s، وصفّ الأرقام بعده بـ .06s */
@keyframes rpRise{ from{ opacity:0; transform:translateY(8px) } to{ opacity:1; transform:none } }   /* السؤال .5s بعد .1s، والخيارات .42s بفارق .05s، والحاويات بفارق .08s */
@keyframes rpOk{ 0%{ transform:scale(.6) } 60%{ transform:scale(1.14) } 100%{ transform:scale(1) } } /* حرف الصحيح وحلقة الحكم */
/* والساعة في دقيقتيها الأخيرتين: طوبيّة بنبض حلقة 4 بكسل كلّ 1.6s */
```

`key` على الخيارات في `Runner.jsx` يجعلها تدخل مع كلّ سؤال. وكلّها تحت `@media (prefers-reduced-motion:reduce){ animation:none; transition:none }`، ولا `transform` على `.qscreen` نفسها (ندبة التحويل في `CLAUDE.md`).

**14-ب) ما يحيا في كبسولة مستشارك (الجولة 205، ب-269؛ وصحّحت 213 سببها، ب-277)** - جو بعد 199: «وضع الكهرباء السالبة اللي أصاب الكبسولة، لا زال موجود. ترف كذا رفرفا بالثانية». **وقِيس في 213 أنّ ما رآه كان الرصيف كلّه يتناوب بين مقعده وبيته فوق الأزرار مع كلّ تصيير للمكالمة (188 إلى 212)**، بعد أن قال جو: «قبل ماكان فيها مشكلة انت غيرت كودها في مرحلة معينة». فموضع الكبسولة أوّلا (213):

- **يُكتب مرّة على الرصيف ويُقرأ منه:** الأثر الذي يُقعدها يُعاد مع كلّ تصيير، والمكالمة تصيّر المستشار كلّ ثانية ومع كلّ كلمة، فلا يحفظ نسخة من مقعدها في متغيّر يبدأ من صفر (`seatOn` و`seatOrigin` في `src/core/advisor/dockPos.js`).
- **ويُحسب بعرض الصفحة لا بعرض الشاشة:** الجوّال يوسّع الشاشة (`innerWidth`) بقدر ما يخرج عن الصفحة، فمقعد يُقاس بها يحفظ خروجه (ثمانية بكسلات من 199 إلى 212: الصفحة تنزاح تحت الإصبع). `seatInPage` يقيس بصندوق `documentElement` (حافّته، وعرضه `clientWidth`) ثمّ يرجع بإحداثيّ الشاشة، والخروج يُفحص بـ`scrollWidth - clientWidth`.
- **وسطر النداء يفتح لجهة الوسط إذا ضاق يساره:** «يطلب المايك من المتصفّح» (139 بكسلا) و«يعقد المكالمة» تفتح من الرصيف إلى الحافّة، والرصيف على الجوال عند الحافّة، فكان السطر خارج الشاشة ويوسّع الصفحة لحظة النداء. `dialSide` يقلبه (`data-dial="in"`) من موضع الرصيف وحده (`DIAL_ROOM` 160) فلا يقفز بين الحالين، ومقعد الهامش على العريض لا يُقلب (جنبه «التالي»).
- **والقياس بمكالمة تصيّر فعلا لا بأصناف تُضاف باليد:** `tools/shot-213.mjs` يستبدل خطّاف المكالمة في المتصفّح بمكالمة مزيّفة تحرّك حالات ريأكت بإيقاعها (بالأصناف وحدها فاتت الرفرفة 199 و205)، وحارسها `tools/run-expl.test.mjs`.

ثمّ الطبقة الحيّة في الوجه (205):

- **لا تتحرّك بـ`steps()` ولا بقفزات شفافيّة:** الوميض بالخطوات يُقرأ على الجوال كهرباء لا هولوغرام. خطوط الهولوغرام لمعة ناعمة بطيئة (`advShimmer`: من 0.18 إلى 0.27 في 6.9 ثانية، `ease-in-out`)، وزمن اللمعة 5 ثوان فأكثر ومداها 0.12 فأقلّ.
- **ما يتبع الصوت يتبعه بالزمن لا بالإطار،** وبثابت أبطأ من المقطع (`levelStep` في `src/core/advisor/presence.js`: صعود 110 ملّي ثانية وهبوط 420، والإطار الطويل يُقصّ عند 100): يعلو مع الجملة ويهدأ بعدها ولا يرفرف مع كلّ مقطع، ولا يتبدّل بوضع توفير الطاقة (30 إطارا).
- **ومدى ما يتبع الصوت صغير:** التوهّج بضع بكسلات (`12px + lv * 10px` ضبابا، `1px + lv * 2.5px` انتشارا، بانتقال 0.2 ثانية)، والشفافيّة خُمس المدى. وقيس في كروميوم: صفر قفزات، والتوهّج يتأرجح بين 0.3 و0.7 بكسل بعد أن كان 3.4 إلى 4.5. والحرّاس `tools/css-laws.test.mjs` §5 و`advisor.test` و`tools/shot-205.mjs`، والحكم الأخير عين جو على الآيفون في مكالمة حيّة.

### 15-د. فخاخ الليلة، مقيسة

1. **محدِّد نسليّ قديم يبتلع العنصر الملفوف حديثا (170):** `.sec span{ font-size:12px; color:var(--muted) }` في الطبقة الأولى صغّر اسم الموضوع وبهّته لمّا لُفّ بـ`span` لخطّ القلم، والحارس النصّيّ أخضر؛ كشفته اللقطة. العنصر الملفوف يُصفَّر صراحة (`display:inline; font-size:inherit; color:inherit`) ويُحرس.
2. **صنف قصير عامّ في نطاق جديد (172):** `lw-kind grp` التقط `.grp` القائم في `product.css` (حلقات المجموعات، `flex-direction:column`). كلّ صنف يُكتب في نطاق جديد يحمل بادئة النطاق، لا الجذر وحده (امتداد قانون 07-26).
3. **`currentColor` في حلقة لونها أبيض (171):** `color:#fff; background:currentColor` تطلع بيضاء كاملة؛ لون الحلقة متغيّر (`--xp-v`).
4. **`oklch` في المزج مع الشفّاف (172-د):** درجة المنقلة خرجت ورديّة؛ المزج مع `transparent` بـ`srgb`.
5. **المشبع ممزوجا بالرمليّ يخرج رماديّا باهتا (172-ج):** الدرجات تُؤخذ غسلات فاتحة من الصورة ومعها حبرها، لا ألوان مشبعة تُخلط.
6. **ستايل السطر يقفل الزرّ على حالته القديمة (171-ب):** `style={{ borderColor, color }}` على العلامة منع كلّ لغة جديدة من الوصول إليها إلّا بـ`!important`. الحالة صنف، ولا ستايل سطر إلّا لما يُحسب (نسبة، إزاحة، ظهور).
7. **مقعد مربوط بعنصر لاصق (171):** مقعد يُحسب عند تغيّر السؤال وحده يطفو بعيدا بعد أوّل تمرير؛ يُحسب على التمرير أيضا.
8. **نسبة الورقة إلى مكتب مرسوم تُقاس من البكسلات (171):** الورقة والمكتب كلاهما متدرّج ببقع، فقيم الأنماط لا تعطي النسبة؛ `tools/shot-171.mjs` يقيسها من اللقطة.
9. **حدّ اللقطات (171-ج):** معاينة مسار بتبديل صنف الجسد وحده تُبقي الأزرار بنغمة المسار الأصليّ؛ الحكم على نغمة مسار من جولة حقيقيّة فيه.
10. **مكوّن بين ثريدين (172-ب):** بطاقة القانون تسكن صفحة ثريد ويملكها ملفّ ثريد آخر؛ يُسمّى مالكها صراحة في البريف.
11. **نسبة أبعاد بلا عرض صريح في شبكة (170، كُشف بعد النشر في 174):** `aspect-ratio` على عنصر شبكة بلا `width` يُمَدّ في كروم ولا يُمَدّ في سفاري، فيأخذ المربّع عرضه من اسمه وتتفاوت الصفوف. واللقطات كلّها كروم، فلم يرها أحد قبل آيفون جو. العنصر ذو النسبة يحمل `width:100%; min-width:0; justify-self:stretch`، والحارس يرفض غيابها.
12. **رسم بخلفيّة بيضاء في أب معزول (176):** `mix-blend-mode:multiply` يضرب في ما تحته داخل سياق تكديسه؛ و`.pk-top` معزول (`isolation:isolate`) بلا خلفيّة، فالضرب يقع على شفّاف ويبقى بياض الصورة مربّعا ظاهرا حين تُرفع الشفافيّة. يُرفع العزل عن الأب فيضرب الرسم في ورق الرأس، أو تُعطى الصورة خلفيّة شفّافة.

### 15-هـ. صفحة جديدة بهذه اللغة: الترتيب

1. **سمِّ المكتب:** أضف نطاق الصفحة إلى قائمة المكتب (§13-هـ) أو اجعل جسدها مكتبا (`body:has(.<النطاق>)`)، ولا تعطها مكتبا خاصّا.
2. **صنّف كلّ مكوّن في طبقة من ثلاث** (ورق، مكتب غائر، زرّ ناهض) قبل أن تكتب له قاعدة؛ والحاوية التي تجمع أوراقا تُنزع ورقتها.
3. **اختر الزرّ المصبوغ الواحد**، واجعل الباقي ورقا بصفيحة، وكلّ حالة صنفا.
4. **النغمة من سجلّها، واللون الكبير من صورة القسم:** كمّم صورته في الرئيسيّة بعد حذف بياض الورق، وخذ منها المكتب والغالبين والعميق، ثمّ ركّب ورق الألوان المائيّة (الوصفة 11 أو 12)؛ والإخوة درجات مرتّبة من الباليت نفسها.
5. **ثبّت أحجام الخطّ القائمة في الحارس قبل أن تبدأ**، فالارتقاء بالطبقات لا بالتكبير؛ ولا عربيّ تحت 12.
6. **الأيقونات من الجدول في الوصفة 7** (فكرة واحدة، أيقونة واحدة في المنصّة كلّها)، والجديدة قناع لا يشبه حرفا ولا رقما.
7. **الحركة من الوصفة 14** وحدها، وتُطفأ مع تقليل الحركة.
8. **ابنِ حارسك واره أحمر بطفرة:** النطاق، والطبقة، والنسبة رقما، والأحجام، وغياب ستايل السطر؛ وسجّله في `tools/run-tests.mjs`. **ثمّ صوّر** على 360 و390 والعريض، في أعلى الصفحة وبعد التمرير، بالخطّ الحقيقيّ إن أمكن، واحكم بعينك قبل أن تسلّم: الرقم شرط، والعين الحكم.
9. **افحص مقاسات الآيفون بأطول المحتوى (174):** على 390 و430 بأطول عنوان في البنك الحقيقيّ لا بعيّنة، وقِس أنّ كلّ بطاقة في الشبكة بعرض واحد وطول واحد، وأنّ لا اسم فلتر ينكسر ولا تمرير جانبيّ. **والصندوق كروم وحده**، فكلّ ما يتّكئ على سلوك تخطيط يختلف بين المتصفّحات (النسبة، والتمدّد، و`:has`) يُذكر في التسليم أنّ حكمه الأخير على آيفون جو بعد النشر.
10. **افحص الدسك توب بعرضين على الأقلّ (176):** 1280 و1440، ومعهما 1920. شبكة تكفي الجوال تترك الشاشة العريضة فارغة: البطاقة تأخذ نسبة أعرض، والمسار يُقسم بالتساوي، والعمود يتّسع حين تسبح البطاقات في فراغ. وقس الورقة على مكتبها من البكسلات هناك أيضا.

**حرّاس الليلة:** `tools/picker-paper.test.mjs` (المنتقي)، و`tools/run-expl.test.mjs` (ورقة الحلّ وصفحة السؤال وخلفيّاتها، ومعه القياس `tools/shot-171.mjs`)، و`tools/laws-paper.test.mjs` (لوح القوانين وبطاقته وأحجامه).

## 16. الكسر صندوق سطريّ، والإشارة في مكانها (2026-09-25 في كوورك، نُقلت 2026-09-27 بالجولة 214 في بوّابة القمة)

**بلقطة جو للسؤال 8 من تحديد المستوى (كسر متسلسل بخطوط قصيرة ومقامات مكسورة أسطرا) وكلمته:** «لازم نشوف وش وضعها ونفحص البنك فحص عام عن مثل هذه التشوهات وأسبابها». وقِيس البنك الحيّ قبل أيّ علاج (ب-224).

1. **خطّ الكسر بعرض أعرض سطريه:** الكسر صندوق سطريّ (`inline-block`، وسط)، والبسط والمقام كتلتان بعرضه لا تلتفّان (`nowrap`)، والخطّ حدّ البسط السفليّ الذي صار بعرض الصندوق. **لا عمود مرن:** العمود المرن الموسَّط يجعل الخطّ بعرض البسط وحده، وسفاري يقيس الصندوق أضيق من محتواه فيكسر المقام المركّب أسطرا.
2. **الإشارة السالبة ملاصقة لرقمها في جهة القراءة:** كلّ حدّ في السطر الرياضيّ معزول يسارا في جزيرة يمينيّة (اتّفاق 08-01)، **ويُطبَّق وقت العرض في المعبر الواحد (`renderMath`)** لا في البيانات وحدها؛ والسطر الرياضيّ الواقف وحده (خيار «−3») جزيرة هو أيضا. ولا يُحكم على اتّجاه بالعين: الإشارة يسار رقمها بمستطيل الحرف.
3. **الجذر فوق الجذر مرسوم طبقة طبقة،** بقضيب يغطّي ما تحته كلّه.
4. **الحكم بالأداة على الأرشيف كلّه:** `tools/e2e-mathrender.mjs` يرسم كلّ حقل فيه كسر أو سالب أو جذر بأنماط التطبيق على 390 و360 ويشترط صفرا في الخطّ القصير والكسر المنكسر والإشارة المقلوبة، ويحمرّ بمعبر ما قبل الجولة (شاهد الحسّاسيّة، الدرس 593).

---

## 17. ورقة الدليل (2026-09-28، الجولة 229 في بوّابة القمة)

**بكلمة جو:** «اعملها أنت بلمستك اللي تعكس هويتنا». فورقة الدليل من عائلة الدايلوقات اللؤلؤيّة لا شكل جديد:

1. **الورقة:** لؤلؤ دافئ بحافّة ذهبيّة رفيعة وظلّين، وختم الجوهرة فوق رأسها بلون الصفحة، وعنوانها بخطّ العناوين وتحته خطّ القلم، والعدّ «3 من 7» ورقة صغيرة، والنقاط تمشي تحت النصّ.
2. **البقعة:** تفتح على المكوّن الحقيقيّ بظلّ دافئ (لا أسود) وحلقة ذهبيّة، وتنتقل بين الخطوات بالحركة نفسها، والخطوة بلا مكوّن ورقة في الوسط بلا بقعة.
3. **الجوال:** ورقة سفليّة بعرض الشاشة، تنقلب فوق حين تغطّي المكوّن، ولا فيضان على 360.
4. **السكون:** عند التخطّي أو التمام تطير الورقة إلى زرّ البوصلة في الشريط وتصغر فيه، والزرّ ينبض مرّة. وتقليل الحركة يلغي الطيران والنبض.

الكود: `src/styles/guide.css` (بادئة `ug-`)، والمحتوى `src/core/guide/content.js`.

## 18. مقياس الصفحة الواحد: الرئيسيّة مسطرة (2026-09-28، الجولة 236 في بوّابة القمة)

**بكلمة جو بلقطتي الرئيسيّة وقسم الكمّيّ:** «صار فيها zoom in... صفحة التطبيق هادئة، أحجامها للعين. فتخيّل وضعها على لابتوب أصغر أو على آيباد... Rethink the scale and footprint... at the level of the code... وهذا صحيح في كلّ الأقسام».

1. **الرئيسيّة مسطرة، والصفحة الداخلة لا تكبر عنها:** عمود واحد (1140) لكلّ الصفحات، وعنوان الصفحة فوق عنوان بطاقة الرئيسيّة بقليل (24 إلى 30)، وبطاقة الشبكة داخل القسم على قدّ بطاقة الرئيسيّة لا أطول. **صفحة ترفع سقف عمودها لنفسها تكبر كلّها معه**، وهذا جذر «الزوم» المقيس: 1260 و1320 و1500 وعناوين 34 إلى 46 وصدور 210 إلى 300.
2. **المقاس رموز في بيت واحد (`src/styles/scale.css`) وكلّ صفحة تستهلكها:** `--page-max`، و`--fs-page-title` و`--fs-page-lead` بـ clamp تنمو مع العرض ولا تتجاوز سقفها، و`--hero-min` و`--hero-pad` لصدر الصفحة، و`--tile-min` و`--tile-title` و`--tile-ghost` لبطاقة الشبكة. ملفّ صفحة يكتب رقما من عنده بدل رمز خرقٌ لهذا البند.
3. **الارتفاع يُقاس كما يُقاس العرض:** على لابتوب قصير (768 و800 ارتفاعا) الصدر أقصر، فأوّل صفّ من المحتوى يظهر بلا تمرير.
4. **البطاقة من الآيباد فما فوق أعرض من طولها بارتفاع الرمز، لا بنسبة أبعاد:** نسبة 16:9 تكبر مع عرض البطاقة، فالشاشة الأعرض تعطي بطاقة أطول وصفحة أطول. ثلاث في الصفّ على الآيباد الطوليّ، وأربع على العمود. والجوال عموداه كما هما.
5. **الاستثناء الوحيد وثيقة لا قسم:** صفحات القراءة الطويلة (الختام والتقرير وقراءة المستشار) سقفها في `coach.css` بقانون الجولة 13، وهي وثائق تُقرأ لا أقسام تُتصفّح.

الحارس: `tools/page-scale.test.mjs` (لا سقف عمود خاصّ بقسم، ولا عنوان بكسلا، والصدور من الرمز)، والقياس `node tools/scale-audit.mjs` (عرض المحتوى والعنوان والبطاقة وطول الصفحة بالشاشات والتمرير الأفقيّ لكلّ صفحة على كلّ مقاس).
- **واللوح الذي يسكن داخل صفحة درجة تحت عنوانها (بعد دمج 233):** `--fs-section-title` بين 20 و24 لعنوان لوح القوانين، واسم الفئة تحته بدرجتين، وسطره وحشوته من رموز الصدر.

## 19. المستشاران في صدر الهبوط، وشعار القمّة (2026-09-29، الجولة 256 في بوّابة القمة)

**بكلمة جو (20:41 و20:46):** «ندمج شكلها وشكل أبو محمد في Landing Page ويطلع شكلهم فعلًا. إحنا ما احنا موجهين هذه المنصة للأولاد فقط، حتى البنات»، و«ممكن يبدأ بنفس التايك اللي موجود الآن في المنصة، بعدين [جيهان] وحدها. بعدين يجون هما، بعضي ينظرون إلى عين الكاميرا ثم ينظرون في بعضهم... ممكن تتعدد اللقطات، مو شرط لقطة واحدة. بعدين تثبت على لقطتهم اللي مع بعض». **وفي الشعار:** «أرى أن صورة الذيب في القمة صارت خارجة عن نموذجنا الجديد. فنحتاج إلى صورة مثل جودة الصور التي أرفقتها لك فوق لأبو محمد وجيهان» (البرومبت `design-language/prompts/gate-emblem.md`).

1. **اللقطات أربع على المسرح نفسه، لا فيلم جديد:** الشابّ كما كان حرفا (أوّل جلب وأوّل رسم)، ثمّ جيهان وحدها، ثمّ الاثنان إلى الكاميرا، ثمّ ينظر كلّ منهما للآخر ويثبت هناك. كلّ لقطة طبقة فوق الصدر بقناعه نفسه (الحافّة السفلى المقطوعة تذوب في الورق)، والزهرة خلفها كما هي. **الأوقات** (`src/components/landing/shots.js`): تبقى 3.4 ثمّ 3 ثمّ 2.6 ثانية، والذوبان إليها 1 و1 و0.8 ثانية. **والالتفاتة أقصر ذوبانا** لأنّ الوجهين في موضعهما (قصّ اللقطتين بصندوق واحد)، فتُقرأ التفاتة لا قطعا. **وبين لقطتين مختلفتي التكوين تتأخّر الداخلة 380 جزءا من الألف**، فتذوب الخارجة في الزهرة قبل أن تحلّ مكانها، ولا يظهر وجهٌ عائم فوق وجه (قِيس في لقطة الجوال).
2. **الوقت لا يمضي إلّا والصدر يُرى:** يُعدّ ما دام الصدر على الشاشة والصفحة ظاهرة وصورة اللقطة وصلت، ولا تتقدّم لقطة قبل وصول التالية؛ فمن غاب لا تفوته لقطة، ومن بطُؤت شبكته يرى الشابّ أطول لا فراغا. و«حركة أقلّ» ترى اللقطة الأخيرة ساكنة من أوّل لحظة ولا تجلب غيرها.
3. **لقطتا الاثنين أعرض من المسرح** (قصّهما 1251 × 1224 على ارتفاعه نفسه، فعرضهما 121.6% ويفيضان 10.8% على كلّ جانب داخل هامش الزهرة 16.19%)، **وعلى العريض تميلان يسارا 3%** عن عمود النصّ (كمّ الشابّ المرفوع كان يقترب من سطر الوصف). والحافّة اليمنى المقطوعة تذوب كالسفلى.
4. **القناعان في عنصرين لا في عنصر:** قناع الحافّة اليمنى على غلاف اللقطتين، وقناع السفلى على كلّ صورة. **وكانا في العنصر نفسه بتقاطع (`mask-composite`) فرسم كروميوم صفّا معتما تحت الحافّة السفلى** (خطّ تحت عباءة جيهان، يزول بنزع الثاني). وكلّ قناع بمقاس عنصره ولا يتكرّر (`mask-size:100% 100%`، `no-repeat`): ارتفاع المسرح كسريّ، والقناع المبلّط يعيد طرفه عند الحافّة.
5. **الأحجام والوزن:** كلّ لقطة ثلاثة أحجام (560 و800 وكاملة) بـ`srcset` وأولويّة جلب منخفضة، وسقوف 60 و100 و170 كيلوبايت، والمجموع تحت 780 (`tools/landing-shots.mjs` وبيانه `src/assets/persona/shots.json`). والرسمات الأصليّة المائيّة في `design/persona/` أزواجا (مشهد ومقصوص).
6. **شعار القمّة مكان الذيب في أربعة مواضع** (`tools/gate-emblem.mjs` من الأصل `design/brand/gate-emblem.webp`): عملة الشريط (لؤلؤة البوّابة) بحلقتها الذهبيّة المرسومة، ودائرة الطالب في المحادثة (§13-ق)، ووجه الوسام القديم، وأيقونات التطبيق (على ورق البوّابة بحلقة ذهب، والدائرة داخل منطقة الأمان 80%). **ويُعرض كما رُسم** بلا فلتر ولا مزج، **ومقاسه على قدر أكبر رسم له:** العملة 256 (26 كيلوبايت، والرماديّة قبلها 38 بمقاس 512). **وأيقونات الشاشة الرئيسيّة برمز نسخة في رابطها** (`?v=`)، فلا تبقى أيقونة الذيب في ذاكرة المتصفّح؛ ومن ثبّت البوّابة على الآيفون قبلها يحذفها ويضيفها لتتبدّل.
7. **ولا ختم شعار على شاشة الجولة (ب-338):** كان الذيب الباهت لصق العمود في كلّ سؤال (التدريب والنماذج وتحديد المستوى وأخطاؤك)، واشتُقّ في هذي الجولة من رسمة القمّة، ثمّ قال جو قبل نشره: «Don't replace it. We want a clean background». فخرج ولم يُبدَّل: خلفيّة الجولة غسلة حارتها ورسم محطّتها وحدهما.
8. **(257، ب-339) الشعار ظلّ بدراما الذيب، مقصوص أقرب:** الرسمة المائيّة الأولى لم تُقرأ في العملة (المتسلّق نحو 10 بكسلات، والعلم تيل على سماء تيل، والجبل وسط سحاب أبيض)، فرسم جو الظلّ ببرومبت منّا: المتسلّق والعلم والجبل ظلّ داكن واحد أمام قرص مضيء، والسماء أفتح من الجبل. **وبكلمته «You can make it closer»** تُقصّ المخرجات كلّها من دائرة أصغر داخل الرسمة (`FOCUS` في الأداة: تكبير 1.8 حول القرص والمتسلّق)، فيصير المتسلّق والعلم ضعفي ما كانا في العملة، وحافّة القرص قوس على جانبيها، وظلّ الجبل تحتهما. **وضوء قمر لا شمس:** بكلمته بعد لقطة القصّ «the yellow color is destroying everything. I like it more of a moon-like color»، فالأصفر في القرص وحافّة الضوء والرذاذ والسحاب المضاء يُسحب في الاشتقاق (`MOON`: الدافئ في فضاء لاب يبقي نحو خُمس صفائه، والتيل والحبر كما هما)، واختار من أربعة (فضّيّ بارد، ولؤلؤيّ، وأفضّ، وكريميّ) «The middle pearl one»؛ فالقرص قمر لؤلؤيّ وملمس الماء فيه كتضاريس القمر. **والحكم على الشعار بأصغر مقاس يُرسم فيه جنب الذي يحلّ محلّه** (42 و28، ومعهما 84 للكثافة المضاعفة)، قبل الاعتماد لا بعد النشر.

**الحرّاس:** `tools/persona.test.mjs` (§10: الترتيب والأوقات والخطوة، والبيان بأحجامه وسقوفه، والأسلاك، والقناعان في عنصرين، وحركة أقلّ) و`tools/gate-emblem.test.mjs` (والختم غائب من كلّ ملفّ في `src`) في البوّابة؛ و`tools/e2e-persona.mjs` في المتصفّح (التسلسل كما مرّ فعلا على الشاشة، والثبات على الأخيرة، والأبواب في الشاشة الأولى على الجوال، وحركة أقلّ)، و`tools/e2e-dose.mjs` (لا ختم في شاشة الجولة).

---

## و. ستاندردز هب مثالا ثانيا: الضوء والعمق (5.0، 2026-09-28)

> **بطلب جو بحرفه (2026-09-28):** «من الضروري تحديث لغة التصميم بناءً على أحدث الموافقات والتعديلات الدقيقة، بالإضافة إلى
> دليل البناء لنشاط جولة المنشأة.»
>
> **لماذا هذا الجزء:** ستاندردز هب (أداة تقييم مراكز الأسنان على معايير سباهي، المستودع `sa66aam/standardshub-v4`) أوّل
> مشروع غير القمّة يحمل هذه اللغة. أخذت محاولته الأولى (2026-09-27) سطح الدليل كما هو: مكتب رمليّ، وورق دافئ، وشارات
> هادئة؛ فرجع البيج نفسه الذي لا يحبّه جو، وانتهى اليوم بتراجع كامل على المكتب والآيباد (سجلّه `PROJECT_LOG.md`، Entries 53
> إلى 60). وفي الليلة نفسها أخذت المحاولة الثانية المنطق وكتبت وصفاتها من هويّة المشروع، فاعتمدها جو صباحا، وتلتها ثلاث
> جولات ضبط في الصباح نفسه. هذا الجزء يسجّل ما أثبته المثال الثاني على النواة (و-1)، وقيمه على المحاور (و-2)، والرحلة
> بموافقاتها ورفضها بحرف جو (و-3)، والوصفات بقيمها (و-4)، وقرارات الأسطح (و-5)، وعالم جولة المنشأة (و-6)، والمتقاعد
> وليش (و-7)، وفحص ما قبل التسليم (و-8)، وكيف يبدأ مشروع ثالث (و-9).
>
> **بيته في الكود:** القوانين في `.claude/skills/standardshub-design/SKILL.md` ويحرسها `tests/v5.test.js`، والرموز في
> `src/core/design/tokens.css` و`base.css`؛ وحيث يختلف رقم هنا عن الكود فالكود هو الحكم. ولجولة المنشأة مرجعها البنائيّ
> بجانب هذا الملفّ: `FACILITY_TOUR_ARCHITECTURE.md`، ولقطاتها في `tour/`.

### و-1. ما أثبته المثال الثاني على النواة: المنطق ينتقل، والمادّة محور

كُتبت النواة (أ) من مشروع واحد، فحملت مع منطقه مادّته. ونجح ستاندردز هب بمادّة أخرى على المنطق نفسه، فصار ممكنا أن يُفصل
بينهما. هذا كلّ حكم تغيّرت مادّته عنده، وما ثبت منه، والصياغة المقترحة للأصل (تُعتمد في الأصل بكلمة جو):

| الحكم في أ | ما فعله ستاندردز هب | ما ثبت (المنطق) | الصياغة المقترحة |
|---|---|---|---|
| أ-1 حكم 1: ورقة على مكتب، والفرق 1.08 فأكثر | بورسلان أبيض على جوّ سيلادون حيّ. والمحاولة الأولى بلغت تباينا أدناه 1.15 ووسيطه 1.26 على 178 زوجا، ورآها جو قطعا مقصوصة من الورقة لا طافية | الطفو ثلاثة أشياء معا: أرضيّة حيّة، وسطح من مادّة غير مادّتها، وظلّ تقع طبقته البعيدة تحت البطاقة بمسافة تُرى (LESSONS #611) | «سطح على أرضيّة حيّة، من مادّة غير مادّتها، وظلّ يُرى تحته. رقم 1.08 شرط لازم لا كافٍ، والحكم للعين في أعلى الصفحة وبعد التمرير.» |
| أ-1 حكم 5: اللون الكبير من الرسم | لا رسوم أقسام فيه؛ لون الأرضيّة من هويّة الصفحة: تيل في البيت، ولون الفصل داخل فصله، والكحليّ في الجولة | الأرضيّة تأخذ لونها من هويّة الصفحة، لا من علبة محايدة | «اللون الكبير من هويّة الصفحة: من رسمها حيث لها رسم، ومن لون فصلها حيث لها فصل.» |
| أ-1 حكم 6: الإخوة درجات من عائلة | سبعة فصول بسبعة ألوان ثابتة من المحتوى (تحرسها نسخة المحتوى)، تُرسم جواهر | السلسلة تتمايز بهويّتها، والمتقاربان لا يتجاوران، ولا يُعرف أحدها باللون وحده: رمزه أو اسمه بجانبه | «الإخوة يتمايزون بهويّتهم: درجات من عائلة، أو ألوان هويّة ثابتة تُرسم بضوء.» |
| أ-1 حكم 7 وأ-5: الحال جوهرة صغيرة | الشارة الواحدة (`.ui-pill`): ورقة بورسلان صغيرة ناهضة، كلمتها بالحبر وحالها جوهرة مضيئة (القرار 1 في و-3) | ثبت كما هو | لا تغيير؛ ألوان الحكم محور (و-2) |
| أ-2: الظلّ دافئ دائما، والبارد عيب | الظلّ بلون الأرضيّة: حبر تيل `rgba(16,42,58,a)` على الضباب، وكحليّ `rgba(4,14,30,a)` على مخطّط الجولة؛ والبنّيّ الدافئ `rgba(74,63,46)` عيب عنده يحرسه اختبار | الظلّ من لون ما يقع عليه، والأسود والرماديّ عيب في كلّ مشروع | «الظلّ بلون الأرضيّة التي يقع عليها: دافئ على مكتب القمّة، وحبر تيل على ضباب ستاندردز هب، وكحليّ على مخطّط الجولة.» |
| أ-1 حكم 4: زرّ مصبوغ واحد | جوهرة التيل بخيط ذهبيّ في قاعها؛ وفي الجولة جوهرة ذهب (التالي) | ثبت كما هو | لا تغيير |
| أ-1 حكما 2 و3: ثلاث طبقات، ولا ورق فوق ورق | أربع موادّ: الجوّ (مكان المكتب)، والبورسلان (الورقة)، والجواهر (المصبوغ والمختار)، والزجاج (الكروم)؛ ولا بطاقة داخل بطاقة (يحرسه اختبار) | ثبت، وزاد عليه الزجاج مادّة رابعة للكروم | «...وإن احتاج المشروع كروما يطفو فوق الصفحة فهو زجاج يمرّر هواءها.» |
| أ-4: العنوان بخطّ العرض | لا خطّ عرض: Lora وNoto Naskh Arabic وحدهما، وخيط ذهبيّ تحت عنوان الصفحة | الإشارة تحت العنوان ثبتت؛ الخطّ محور | خطّ العرض محور لا نواة |
| أ-6: الحركة والنظافة | منحنى السباحة نفسه `cubic-bezier(.2,.7,.3,1)`، وثلاث نبضات ثمّ سكون، وأرقام غربيّة | ثبت كما هو | لا تغيير |
| ب-1: نغمات الأقسام من «البنك الصامت»، والممنوع اللون المشبع الصارخ | جواهر من ألوان الهويّة، لا هادئة ولا مسطّحة؛ واعتراض جو على المحاولة الأولى أنّ الألوان باهتة تماما | المسطّح الصارخ ممنوع، والباهت كذلك حيث يرفضه المالك | مدى المحور من البنك الصامت إلى جواهر الهويّة، والممنوع التعبئة المسطّحة في الطرفين |

**الخلاصة:** ما لا يُساوَم عليه هو المنطق بصياغته المجرّدة. أمّا الورق الدافئ والمكتب المائيّ والظلّ البنّيّ والبنك الصامت
فقيم القمّة على محاور: تُنقل كما هي إلى مشروع يشبه القمّة، ولا تُفرض على مشروع لا يشبهها. ولو قرأ مشروع ثالث (أداة PHC)
الجزء أ بمادّته لرجع إلى ليلة 2026-09-27 نفسها.

### و-2. قيم ستاندردز هب على المحاور

| المحور | القمّة | ستاندردز هب |
|---|---|---|
| لون البيت (الزرّ المصبوغ) | تيل `#0e7d86` | جوهرة تيل `linear-gradient(170deg,#1b8f92,#0f6a74 48%,#0a4a57)` بخيط ذهبيّ في قاعها |
| معدن التوقيع | ذهب `#b8912e` | خيط ذهبيّ من `#e5c461` إلى `#b8912e` بجرعات صغيرة: تحت عنوان الصفحة، وفي قاع الجوهرة، وعلى حافّة البطل العليا، وعلى المسار الممشيّ في الجولة |
| نغمات الأقسام | البنك الصامت | ألوان الفصول من المحتوى كما هي: LD `#2c5282`، PC `#1f7a72`، DL `#6b4fa0`، MOI `#3b82a6`، IPC `#8a4b8f`، FMS `#596b7d`، DA `#a64d6d`؛ تُرسم جواهر (و-4) |
| المكتب | ماء من رسم القسم | الجوّ: ضباب سيلادون `#e3ebe9` إلى `#e9ede6`، وبركة من نغمة الصفحة من الركن العلويّ البعيد وعليها خطّ مدّ جفّ، وبركة ذهب من القاع، ونفَس كحليّ عند الحافّة الأولى، وحبيبة؛ ثابت على النافذة لا يمتدّ مع الصفحة الطويلة؛ وداخل الفصل البركة بلون الفصل |
| الورقة | `#fffdf8` دافئة | بورسلان: مينا بيضاء `linear-gradient(180deg,#fff,#fefefd 58%,#f9faf8)`، حدّها `rgba(16,42,58,.1)`، حافّتها العليا مضيئة، وظلّها ثلاث طبقات |
| مادّة الرسم | طبيعة صامتة لأشياء الدراسة | رسوم خطّيّة على شبكة 48 بخطّ 1.7، وأيقونات؛ والصورة تتكلّم كالمقيّم الذي يلجأ إليه الناس في الحوكمة، والسنّ حيث الموضوع أسنان فقط (جو، 2026-09-27) |
| الانحناء | 22 للورقة، 15 للزرّ | 16 إلى 22 للبطاقات (18 بطاقة التقييم، 22 الإرشاد في الجولة)، و28 للنوافذ والأوراق السفليّة، والكبسولات كاملة، ومربّعات الفصول بزوايا 10 إلى 12 |
| خطّ العرض | ثمانية | لا يوجد: Lora وNoto Naskh Arabic، والعنوان يأخذ الخيط الذهبيّ |
| الشبح | رقم بخطّ العرض | غير مستعمل |
| **محور زاده:** الكروم | لا يوجد | زجاج `rgba(255,255,255,.62)` بتغبيش 18 وتشبّع 1.7؛ على الجوال كبسولات عائمة بعيدة عن حوافّ الشاشة؛ وشريط البوابة ورق بورسلان صلب (جو، 2026-09-27: الصفحة لا تظهر من خلاله) |
| **محور زاده:** ألوان الحكم | صحّ مريميّ وغلط طوبيّ | أربع حالات محجوزة يحبّها جو كما هي: Fully Met `#3f6b3a`، Partial `#86652b`، Not Met `#97474a`، N/A `#756a58`، ولكلّ منها غسلته وخطّه؛ والمختار جوهرة حالته؛ ولا تُستعمل زينة أبدا |
| **محور زاده:** لون الظلّ | دافئ | بلون الأرضيّة (و-1) |
| **محور زاده:** عالم ثانٍ لنشاط آخر | لا يوجد | جولة المنشأة: مخطّط المبنى ليلا (و-6) |

### و-3. الرحلة بترتيبها: الموافقة والرفض بحرف جو

**يوم المحاولة الأولى، 2026-09-27** (من سجلّ ستاندردز هب، Entries 53 إلى 60؛ اعتراضات جو هنا كما لخّصها السجلّ):

1. أعطى جو الدليل وطلب ضبطه على ستاندردز هب؛ فنُقل سطحه: مكتب رمليّ، وورق دافئ، وشارات الفصول ممزوجة 70% برماديّ دافئ
   ومغسولة 10% (`--chm`).
2. اعتراضه: الألوان باهتة تماما ولا يتمايز منها شيء. فجاءت جداول ألوان من مكتبة (Radix)، وخرج فصلان من الورديّ.
3. اعتراضه: صارخة في الدليل، وليست بمستوى البوابة؛ ثمّ: رجّعوا الألوان كما كانت.
4. حكمه آخر اليوم: التصميم السابق كان أجمل، والآن كلّ شيء مدموج ومشوّه؛ فرجع المكتب والآيباد إلى ما قبل المحاولة، وبقي الجوال
   لأنّه «ممتاز»، بشكلين لجهازين في ملفّات مشتركة (LESSONS #618).

**الطلب، 2026-09-27 الساعة 23:06Z، بحرف جو:**

> «أكره إنه يكون عندي لون صامت، وأكره مكونات الشاشة إنها تكون flat مع الخلفية وما تقدر تفرقها.»
> «ألوان الـ chapters جميلة بس يعني تحتاج إنك tweak it شوي.»
> «أحتاج أن يكون الـ Facility Tour mode أكثر ابتكارًا، يعني كله مصمت وbeige.»
> «صراحة الـ SVGs والـ icons جميلة.»
> «التحديث الأخير خلى شرائح الجوال ... بيضاء على خلفية بيج كأنها قطع كذا مقصوصة من داخل الورقة الخلفية، ما هي طافية.»
> «تقدر تأخذها كمرجع، ولكن إذا أنت بتاخذها بنفس طريقة المشروع السابق، فبتعدمنا.»

**الطريق:** قرئ الدليل مقاصد لا وصفات (LESSONS #614)، ورُسمت نماذج قبل البناء: رئيسيّة الجوال بثلاثة أجواء، والجولة مضيئة
ومظلمة؛ ثمّ البناء ليلة كاملة، ثمّ صفحة قبل وبعد فيها ثلاثة قرارات صغيرة.

**الاعتماد، 2026-09-28 الساعة 05:48Z:** «اعتمد وانشر.» فنزل البناء `6d3b4cf`، والقرارات الثلاثة على التوصية:

1. الحال كلمة بلون الحبر وبجانبها جوهرة ملوّنة، لا كلمة ملوّنة.
2. زرّ الإنهاء (Finalize) جوهرة التيل لا الأخضر، لأنّ الأخضر لون تقييم.
3. التقارير (PDF وExcel وصفحة المشاركة) تبقى على ألوانها الأولى حتّى تُنشر الدوالّ.

**الضبط الأوّل، 06:05Z، بحرف جو:** «المكونات الطافية على الجزء الجميل الكحلي ... ممكن تعملها tweak بحيث أنها تكون متلائمة
مع الخلفية الدرامية الكحلية ... ممكن تطفي هذا اللون وتنهض فيه.» فصارت بطاقات الجولة بورسلانا بضوء القمر (و-6)، وبقيت أزرار
التقييم بيضاء لأنّها تُلمس وتنهض فوق البطاقة. وجاء ردّه: «حلوو»، ومعه طلب فلتر نصف المقيّم الآخر، فنزل البناء `e18c4a5`.

**الضبط الثاني، 07:19Z و07:27Z** (بطاقات الشرح الثلاث في صفحة التقييم)، **بحرف جو:**

> «لا أفضل أن تكون بالشكل الأفقي، بل عادي أن تكون أريح وعمودية أكثر، بحيث إن الـ Text يرتاح.»
> «خطها أكبر من اللزوم على مستوى الـ Desktop ... يجب أن تُراعي إمكانية التكبير والتصغير.»
> «فأعد تصميم البطاقات وليس محتواها.»
> «وأحتاجك تشيل filter English Arabic لأنه كل المقيمين عرب.»
> «فأعطينا تصميم مميز أيضًا لتصفح البطاقات بالجوال.»

كان الجواب الأوّل عمودا واحدا بعرض البطاقة، وخريطة على الجوال بدل النقاط. فردّ جو 08:00Z:

> «شوف كيف الصفحة فاضية من اليمين. إحنا نحتاج الكروت مصفوفة بشكل أطول من السابق.»
> «الألوان الزيتية للمؤشرات ما حبيتها حقيقة، لأنها تشعر أنها خارج منظومة التصميم الجديد ... لا زالت روح التصميم القديم فيها.»
> «طريقتك في أنها تكون في مكان واحد وتُسحب، لا تنتقل يمين ويسار، أعجبتني. لكن التصميم واختيار الألوان يحتاج إعادة نظر.»

وأضاف 08:01Z أنّ لون المؤشّرات الجديد ينطبق على دوائر دليل المعايير أيضا.

**الاعتماد الأخير، 08:16Z:** «رائع. انشر.» فنزل البناء `f7496ee`.

**صفحة المركز، 2026-09-29** (أوّل جلسة على الحساب الجديد، بلقطة مجمع عيادات رام على الديسكتوب)، **بحرف جو:**

> «Informative grids should be informative, not include any actionable buttons, so it will be shortened.»
> «لن نحمّل الـ hero أكثر مما يحتمل، ولكن باستطاعتك أن تعمل عليه بشكل نظيف.»
> «الـ progress ممكن ينزل تحت في خانة اللي في كرت الـ progress، ليش يحتل الـ hero؟ ... فخلي الـ progress تحت وخليه أيسر كرت.»
> والهيرو: «لونه غامق مرة».

فرُسم الهيرو ثلاث مرّات على الصفحة الحقيقيّة: لوح التيل بلا كحليّ، والسيلادون الفاتح، والبورسلان الأبيض، والتوصية السيلادون؛
فاختار **التيل الأفتح**، وطلب باب جولة المنشأة في الهيرو. ثمّ على الكروت: شريط تقدّم واحد، شريط الكرت الأيسر؛ ولا مقياس في
الاعتماد ما دام التقييم جاريا بلا حكم؛ ولا نصّ إلا المطلوب. فصار القانون: الهيرو يفعل والكروت تُخبر، وكلّ باب مرّة واحدة في
الهيرو، وعلى لوحه الأبواب زجاج لتبقى جوهرة التيل أسطع ما فيه (`SKILL.md`، PROJECT_LOG Entry 70).

### و-4. المرجعيّة البنائيّة: الوصفات بقيمها (البناء `f7496ee`)

1. **الجوّ** (`.sh-atm` على جذر لا يتمرّر أو صندوق تمرير، و`.sh-atm-fixed` تحت صفحة تمرّر النافذة):

   ```css
   background:
     url("data:image/svg+xml,...") 0 0 / 220px 220px,           /* حبيبة: feTurbulence بتردّد .85 وشفافيّة .07 */
     radial-gradient(85% 58% at 100% 0%, color-mix(in srgb, var(--atm-tone) 36%, transparent),
                     color-mix(in srgb, var(--atm-tone) 12%, transparent) 44%, transparent 70%),   /* بركة النغمة */
     radial-gradient(90% 62% at 102% -2%, transparent 62%,
                     color-mix(in srgb, var(--atm-3) 7%, transparent) 67.5%, transparent 74%),     /* خطّ المدّ */
     radial-gradient(78% 48% at -4% 102%, color-mix(in srgb, var(--atm-gold) 44%, transparent),
                     color-mix(in srgb, var(--atm-gold) 12%, transparent) 50%, transparent 74%),   /* بركة الذهب */
     radial-gradient(62% 40% at -2% 28%, color-mix(in srgb, var(--atm-navy) 10%, transparent), transparent 72%),
     linear-gradient(180deg, var(--atm-mist) 0%, var(--atm-mist-2) 100%);
   ```

   `--atm-tone` تيل `#1b8f92` في البيت ولون الفصل داخل فصله، و`--atm-gold #e5c461`، و`--atm-navy #14224f`، و`--atm-3`
   النغمة 55% مع `#0a2a33`. والاحتياط المسطّح `--paper #e6ecea`.

2. **البورسلان:**

   ```css
   --sheet-face: linear-gradient(180deg, #ffffff 0%, #fefefd 58%, #f9faf8 100%);
   --sheet-edge: rgba(16, 42, 58, 0.1);
   --shadow-rest: inset 0 1px 0 rgba(255,255,255,.95), 0 1px 2px rgba(16,42,58,.07),
                  0 6px 14px -5px rgba(16,42,58,.11), 0 22px 42px -18px rgba(16,42,58,.26);
   --shadow-dominant: inset 0 1px 0 rgba(255,255,255,.95), 0 2px 4px rgba(16,42,58,.07),
                      0 12px 26px -8px rgba(16,42,58,.16), 0 38px 66px -26px rgba(16,42,58,.36);
   --shadow-hover: inset 0 1px 0 #fff, 0 2px 5px rgba(16,42,58,.08),
                   0 16px 30px -8px rgba(16,42,58,.18), 0 44px 76px -28px rgba(16,42,58,.38);
   ```

   الطبقة الأخيرة (المحيطة) هي التي تجعل البطاقة تطفو: تقع تحتها بمسافة تُرى. وداخل البطاقة خطّ شعريّ (`--hair`) أو بئر
   (`--well #f4f7f6`)، لا بطاقة ثانية.

3. **ما يُلمس** (زرّ، شارة، بلاطة): بورسلان ناهض `--sheet-lift` (حافّة مضيئة وظلّ قصير)، يرتفع تحت المؤشّر
   (`--sheet-lift-hover`) وينضغط بظلّ داخليّ (`--sheet-press`). وزرّ المسح بورسلان بحبر طوبيّ وخطّ طوبيّ عند قدمه، لا جوهرة.

4. **الجواهر:**

   ```css
   --jewel: linear-gradient(170deg, #1b8f92 0%, #0f6a74 48%, #0a4a57 100%);
   --jewel-rim: inset 0 1px 0 rgba(255,255,255,.32), inset 0 -2.5px 0 rgba(229,196,97,.72),
                0 0 0 1px rgba(8,60,68,.55);                 /* الخيط الذهبيّ في القاع */
   --jewel-glow: 0 10px 22px -8px rgba(15,106,116,.75), 0 2px 4px rgba(16,42,58,.14);
   --jewel-gold: linear-gradient(170deg, #f6e3a1 0%, #e5c461 45%, #c79d36 100%);
   ```

   وجوهرة الفصل تُمزج من لونه `--ch` على كلّ عنصر يضعه:

   ```css
   --ch-hi: color-mix(in oklab, var(--ch) 74%, #ffffff);
   --ch-lo: color-mix(in oklab, var(--ch) 70%, #081522);
   --ch-glow: color-mix(in srgb, var(--ch) 55%, transparent);
   --ch-wash: color-mix(in oklab, var(--ch) 9%, #ffffff);
   --ch-wash-2: color-mix(in oklab, var(--ch) 17%, #ffffff);
   /* الصلبة (رمز الفصل، والمختار): */ background: linear-gradient(165deg, var(--ch-hi), var(--ch) 55%, var(--ch-lo));
   /* المصبوغة في راحتها: */          background: linear-gradient(180deg, var(--ch-wash), var(--ch-wash-2));
   ```

   الصلبة بكتابة بيضاء وحلقة ووهج من لون الفصل؛ والمصبوغة بكتابة من `--ch-lo`، حيّة لا باهتة.

5. **الزجاج:** `--glass rgba(255,255,255,.62)`، و`--glass-strong rgba(255,255,255,.8)`، و`--glass-edge` (حافّة عليا مضيئة
   وحلقة بيضاء خفيفة)، و`--glass-blur blur(18px) saturate(1.7)`، وظلّه `--shadow-chrome`.

6. **الحبر والبيت:** `--ink #1d3349` للعناوين والأرقام، و`--ink-body #37434f`، و`--ink-soft #55606c`، و`--ink-mute
   #626d79`؛ والتيل `#0f6a74` و`#1b8f92` و`#0a4a57`.

7. **البطاقة التي تنتمي لفصل:** بورسلان برشّة من لون الفصل من ركنها العلويّ تذوب قبل ثلث عرضها؛ لا شريط على الحافّة، ولا
   شريط ملوّن في الرأس.

8. **الميداليّة** (حلقة الجاهزيّة): وجه بورسلان في إطار ذهبيّ رفيع، وأربعون تدريجة، وعلامات الأرباع ذهبيّة، والقوس يتوهّج
   بنغمته، وجوهرة تركب طرفه.

9. **خطوات بطاقة الإرشاد الثلاث** (نشاط المقيّم، وما يُبحث عنه، والقصور المحتمل؛ عربيّة وحدها بلا مفتاح لغة):
   - **الأرقام** جواهر بلون الفصل، متدرّجة من الأعمق (1) إلى الأفتح (3):

     ```css
     /* 1 */ --gs-a: color-mix(in srgb, var(--ch) 85%, #fff); --gs-b: color-mix(in srgb, var(--ch) 72%, #000);
     /* 2 */ --gs-a: color-mix(in srgb, var(--ch) 62%, #fff); --gs-b: var(--ch);
     /* 3 */ --gs-a: color-mix(in srgb, var(--ch) 42%, #fff); --gs-b: color-mix(in srgb, var(--ch) 84%, #fff);
     ```

     قرص 42 بكسل يضيء تاجه، بحلقة بيضاء 3 وحلقة ذهبيّة 4.5، وأيقونة الخطوة شارة عند قدمه.
   - **على الشاشة العريضة:** ثلاث بطاقات بورسلان جنبا إلى جنب في بئر داخل بطاقة التقييم، كلّ واحدة أطول من عرضها، والجوهرة
     تركب ركنها العلويّ؛ الخطّ بوحدة rem (0.875 للإنجليزيّ و0.98 للعربيّ، بوزن 500)، أصغر من خطّ الجوال بدرجة، ليحمله
     تكبير المتصفّح؛ وتحت 1000 بكسل تقف واحدة تحت الأخرى.
   - **على الجوال:** الخطوة في مكانها وتُسحب، وفوقها مسار في بئر فيه الأرقام الثلاثة على جواهرها بأسمائها، وجوهرة الفصل
     تنزلق إلى الخطوة المعروضة (`translateX` بزمن الحال). بلا نقاط.
   - والأرقام نفسها في دليل المعايير على كلّ جهاز.

10. **الخطّ:** Lora من 400 إلى 700، وNoto Naskh Arabic من 400 إلى 700، مستضافان ذاتيّا. العربيّ بلا تتبّع ولا مائل ولا أحرف
    كبيرة، أكبر وأرحب (المتن 17 بكسل للإنجليزيّ و18.5 للعربيّ بسطر 1.9). الأرقام غربيّة. الرمز (LD.24.2) داخل `bdi.code`
    من اليسار دائما. والمصطلح الإنجليزيّ داخل العربيّ جزيرة واحدة (`bdi.term` بحجم 0.9 لا تنقسم) على قانون المصطلحات
    (`docs/guide/terms.json`).

11. **الحركة:** `--swim cubic-bezier(0.2, 0.7, 0.3, 1)`، والأزمنة 160 و220 و600 مللي ثانية، تحويل وشفافيّة فقط، وثلاث نبضات
    ثمّ سكون، وتقليل الحركة يضع الحال الأخيرة فورا.

12. **الهندسة:** الملاحة لا تملك الشاشة (85 إلى 90% منها عمل)؛ هدف اللمس 44 بكسل و52 لما يُستعمل مشيا؛ أدوات المشي في النصف
    الأسفل أو في مرسى عائم؛ شارات الفصول مربّعات صغيرة بزوايا ليّنة فيها الرمز وحده، صفّان على الأكثر، مجموعة واحدة في
    الوسط مع القائمة التي تقودها (جو، 2026-09-27).

### و-5. قرارات الأسطح

- **التقييم على المكتب والآيباد:** شريط الحال على طرف البطاقة صار جوهرة مضيئة، والإنهاء جوهرة التيل، والخطوات الثلاث كما
  في و-4 (9).
- **الجوال:** كلّ شاشة في الجوّ، وداخل الفصل لونه على الشاشة كلّها؛ الشريط العلويّ وشريط التقييم والمراسي كبسولات زجاج
  عائمة؛ بطاقات الفصول برشّة لونها؛ والتالي جوهرة الفصل بخيط ذهبيّ.
- **لوحة التقارير:** بطل بورسلان بضوء تيل وخيط ذهبيّ، وبطاقات الشريط الجانبيّ تطفو، وأزرار التصدير بلاطات بورسلان (خرجت
  أيقوناتها من ألوان التقييم)، وجوهرة واحدة في كلّ شاشة.
- **بوابة المركز:** الجوّ على كلّ جهاز، وشعار جو في البطل، وشريطها بورسلان صلب.
- **الصفحة العامّة:** الجوّ نفسه بدرجة أهدأ.
- **التقارير المطبوعة:** ألوانها الأولى حتّى تُنشر الدوالّ (القرار 3).

### و-6. عالم ثانٍ لنشاط آخر: جولة المنشأة

حين يكون الوضع نشاطا آخر (المشي في مبنى بهاتف في يد، مقابل الجلوس أمام الدليل)، يأخذ عالما خاصّا داخل العائلة: مخطّط
المبنى ليلا، كحليّ إلى تيل بشبكة رسم، وضوء تيل فوق رأس المحطّة؛ الكروم زجاج داكن؛ ما يُقرأ ويُقيَّم بورسلان بضوء القمر
(`#e7eef2` إلى `#d5dfe5`) يطفو عاليا بظلّ طويل كحليّ؛ والفعل المضيء الوحيد جوهرة ذهب (التالي)؛ والمسار الممشيّ ذهب،
والمكتمل تيل، والفجوة مرجانيّ `#ff9d92` على الكحليّ وحده. ويبقى من العائلة ما يجعله منتجا واحدا: بطاقة التقييم نفسها وألوان
الحكم الأربعة، وجوهرة الفصل على كلّ رمز، والخيط الذهبيّ، والخطّان، ومنحنى السباحة.

والدرس: الأبيض النقيّ يلمع على الأرضيّة الداكنة؛ اشتقّ وجه البطاقة من لون الأرضيّة، واحفظ ارتفاعها، وقِس كلّ لون كلام على
الوجه الجديد (LESSONS #612). المعماريّة والمنظر والقيم كاملة في `FACILITY_TOUR_ARCHITECTURE.md`، ولقطاتها في `tour/`.

### و-7. المتقاعد في ستاندردز هب وليش (يُقرأ مع ج)

| المتقاعد | ليش تقاعد | البديل | الأصل |
|---|---|---|---|
| المكتب الرمليّ والورق الدافئ (المحاولة الأولى) | البيج نفسه، والبطاقة مقصوصة مع أنّ التباين 1.15 فما فوق | الجوّ والبورسلان وظلّ تُرى طبقته البعيدة | Entry 53، LESSONS #611 |
| النغمة الهادئة `--chm` (الفصل 70% برماديّ دافئ، غسلة 10%) | باهتة تماما، والأرضيّات السبع شبه متساوية | جواهر من ألوان الهويّة | Entries 53 و61، #613 |
| جداول ألوان المكتبة، وإخراج فصلين من الورديّ | صارخة في الدليل، وخرجت عن الهويّة | ألوان المحتوى ثابتة، والرسم هو الذي يتغيّر | Entries 54 و59، #613 |
| شكلان لجهازين في ملفّات مشتركة | كلّ تعديل بعده يُكتب مرّتين | شكل واحد، والتخطيط بالعرض وحده (يحرسه اختبار) | Entry 60، #618 |
| شريط ملوّن على طرف البطاقة أو في رأسها | علامة قديمة، ولون بلا معنى | رشّة من الركن، أو جوهرة | Entry 61 |
| لون تقييم زينةً (الإنهاء بالأخضر، وأيقونات التصدير بألوان التقييم) | لون الحكم معنى لا زينة | جوهرة التيل، وبلاطات بورسلان | القرار 2 |
| كلمة الحال ملوّنة | أوجه كثيرة للوسم | الكلمة بالحبر والحال جوهرة | القرار 1 |
| الأبيض النقيّ على كحليّ الجولة | يلمع | بورسلان بضوء القمر، والارتفاع باقٍ | Entry 62، #612 |
| الجولة المصمتة البيج | لا تقول «مشي في مبنى» | مخطّط المبنى ليلا | Entry 61 |
| الخطوات الثلاث صناديق قصيرة عريضة بخطّ ثقيل (15 و17 بكسل) وإطار ملوّن فوقها | مزنوقة، وصندوق داخل صندوق، وخطّ أكبر من اللازم على المكتب | بطاقات بورسلان طويلة جنبا إلى جنب، وخطّ rem | Entry 64، #615 و#616 |
| الخطوات عمودا واحدا بعرض البطاقة (الجواب الأوّل) | نصف الصفحة فارغ | جنبا إلى جنب، كلّ بطاقة أطول من عرضها | Entry 65، #615 |
| المؤشّرات الزيتيّة والكاكيّة (`--olive-*` و`--khaki-*`) | روح التصميم القديم | جواهر الفصل المتدرّجة، واختبار يمنع رجوعها | Entry 65، #617 |
| نقاط السحب تحت الخطوات على الجوال | قديمة | مسار تنزلق فيه جوهرة الفصل | Entries 64 و65 |
| مفتاح العربيّ والإنجليزيّ فوق الخطوات | كلّ المقيّمين عرب | الخطوات عربيّة دائما، ودليل المعايير يحتفظ بمفتاحه | Entry 64 |
| الظلّ البنّيّ الدافئ `rgba(74,63,46)`، والظلّ الأسود أو الرماديّ | غريب عن أرضيّة باردة | بلون الأرضيّة (يحرسه اختبار) | Entry 61 |

### و-8. فحص ستاندردز هب قبل التسليم (يُضاف إلى أ-7)

- [ ] 390 و820 و1180 و1440، بالعربيّ والإنجليزيّ؛ وما يذهب لجو الشاشة كاملة بمقاسها الحقيقيّ، ولقطة للصفحة كلّها حين تتمرّر.
- [ ] كلّ بطاقة تطفو في أعلى الصفحة وبعد التمرير، وطبقة ظلّها البعيدة تُرى تحتها.
- [ ] لا شارة باهتة، ولا زيتيّ ولا كاكيّ، ولا ظلّ بنّيّ أو رماديّ، ولا لون تقييم زينةً (الاختبارات تحرسها).
- [ ] خطّ القراءة على المكتب بوحدة rem، وأصغر من خطّ الجوال بدرجة.
- [ ] النسب على عرض شاشة المالك نفسه: لا صفحة نصفها فارغ، و«عموديّ» يعني عناصر أطول لا عمودا واحدا.
- [ ] شكل جديد يبدأ بنموذجين أو ثلاثة يختار منها جو، ولا يُنشر إلّا بكلمته بعد أن يراه.
- [ ] شكوى من لون: ابحث عن العنصر في لقطة المالك قبل أن تلمس أيّ باليت (LESSONS #619).

### و-9. مشروع ثالث من المثالين (أداة PHC أوّلا)

1. اقرأ أ بصياغة و-1، ثمّ ب.
2. اختر قيمة لكلّ محور (ب-1 وو-2). وأداة PHC أقرب إلى ستاندردز هب: منها ورث الحبر والتيل والخيط الذهبيّ (لغة PHC 2.6)،
   فالأقرب أن تأخذ موادّ ستاندردز هب الأربع بألوان فصولها هي. أمّا سطحها اليوم (قماش الورق `.phc-canvas`، والبطاقة
   الشفّافة 0.88، وألوان الحال المشبعة) فهو بعينه ما في ج.
3. نماذج قبل البناء، ثمّ فحص أ-7 وو-8.
4. الجولة من `FACILITY_TOUR_ARCHITECTURE.md`: الجزء 7 فيه خريطة PHC قطعة قطعة، وثلاثة قرارات تنتظر جو قبل النقل.

---

## ز. أداة الاعتماد (سباهي للرعاية الأوّليّة) مثالا ثالثا: الإصدار 2.6 بحرفه

> **لماذا هنا (2026-10-08):** بطلب جو أن تتكلّم المشاريع الثلاثة لغة واحدة من بيت واحد. هذا دليل أداة سباهي كما هو في
> `CBAHI PHC/_docs/03_build-guides/DESIGN_LANGUAGE_BUILD_GUIDE.md` يوم التوحيد (29,678 بايتا)، منقول بحرفه وبلغته
> (الإنجليزيّة)، وعناوينه نزلت درجتين فقط لتسكن تحت هذا الجزء. هو من زمن ما قبل الورق، ومنه خرجت أشياء بقيت في النواة
> (الطفو لا الذوبان، الورقة الواحدة، ذوق جو §10). **وحكمه:** على سطوح أداة سباهي كما هي مشحونة اليوم يبقى ملزما حتّى
> تنقلها جولة إلى النواة بكلمة جو؛ وفي أيّ مشروع جديد الجزء أ هو الحكم، وما خالفه هنا تاريخ.


> **Status:** Living document. Captures the design identity as crystallized through the v2 caravan (2026-06-11/12) and the v2.6 app-wide rollout (`2905f21`, 2026-06-12). This is the single home for the visual language; `LESSONS.md` #133-#139 hold the portable versions of the rules born here; `src/index.css` holds the executable tokens.
>
> **Who this serves:** any future session touching UI. Read this BEFORE styling anything. The goal is that Jo (أبو سطام) recognizes every new surface as "his" without a single correction round.

---

#### 1. The canvas system (the executable layer)

Lives in `src/index.css`. Four utilities are the law:

| Class | Role | Key values |
|---|---|---|
| `.phc-canvas` | THE page background. One per page, on the shell. | Warm paper gradient `#fefdfb → #faf7f0 → #f6f1e7` + ambient radials + 2.6% grain film |
| `.phc-card` | Blended card surface | `rgba(255,255,255,0.88)` + gold hairline `rgba(196,176,128,0.32)` + `0 12px 36px -20px rgba(74,63,46,0.28)` |
| `.phc-chrome` | Sticky bars only | `rgba(252,250,244,0.82)` + blur(14px) saturate(130%) + warm hairline |
| `.phc-lift` / `.phc-stagger` | Hover lift + entrance stagger | swim curve `cubic-bezier(0.2, 0.7, 0.3, 1)` |

The one-canvas taxonomy (LESSONS #134) governs everything: every visible surface is a **CARD**, a **BARE LABEL**, or **CHROME**. Anything else is a strip, and strips get retired, not recolored. `html { scrollbar-gutter: stable }` is load-bearing infrastructure (kills overflow-toggle layout shifts app-wide) - never remove it.

#### 2. Surface tiers (pop tiers)

Translucency 0.72-0.78 is the documented "feels flat" failure. The tiers:

- **Rest card:** `0.88` + `0 12px 36px -20px rgba(74,63,46,0.28)`.
- **Dominant panel / hero:** `0.9` + tint wash + `0 18px 46px -24px rgba(74,63,46,0.35)`.
- **Nested plate (card inside a card):** `0.85` + `0 8px 24px -16/18px rgba(74,63,46,0.25)`.
- **Hover lift:** deepen to `0 24px 56px -20px rgba(74,63,46,0.42)` + translateY(-1.5 to -2px). Never Tailwind's `shadow-2xl` (cool black).

Shadows are ALWAYS in the warm family `rgba(74,63,46,…)`. A cool `rgba(0,0,0,…)` shadow on a new surface is a defect.

#### 3. Palette

**Structural family:**
ink `#1d3349` (titles, hero values) · body warm `#5d5a4e` / `#3f4a4a` · sand label `#a39574` (small-caps labels) · sand mid `#8a8068` · sand muted `#a39a82` · sand faint `#b9ad92` / `#c2b79a` · hairline `#e7dcc2` / `rgba(196,176,128,0.28-0.45)` · tracks `#f0ece0` / `#ece5d4`.

**Gold (the signature):** `#E5C461 → #B8912E` gradients; text gold `#97702f` / `#B8912E`.

**App ink action:** teal `#084848 → #0d6e6e` (primary buttons, tour CTA, Save).

**Semantic (matured palette - the score-capsule standard):**
Met/success `#059669` (deep `#047857`/`#065f46`, gradient `#065f46 → #10b981`) · Partial/draft `#d97706` (gradient to `#fbbf24`) · Not Met/danger `#dc2626` · N/A `#475569` on `#f1f5f9` · Pending/unscored: dashed slate.

**Forbidden in new work:** mint `#34d399` and bright `#10b981` as a text/accent color (pre-v2 register; `#10b981` survives only as gradient endpoint), indigo (one exception below), cool slate text (`#334155`/`#475569`/`#94a3b8`) outside the locked-axis and N/A semantics, Tailwind gray utility colors on new surfaces, em-dash anywhere, Eastern numerals anywhere.

**Reserved identities:**
- **Locked / archived / read-only:** the slate lock pill - `rgba(241,245,249,0.96)` bg, `#334155` text, `rgba(100,116,139,0.45)` border, lock glyph. NEVER green (green lies "success" where the meaning is "frozen"). Deliberately outside the domain colors.
- **Help:** teal glass `rgba(15,106,116,0.06)` + `#0f6a74` + the BOOK glyph - identical everywhere (Header, SA chrome, tours). Help has one face.
- **Domain colors** (`getDomainColor`) belong to chapters only. State palettes must never collide with them.

#### 4. Card anatomy (the Settings architecture)

Born in the SettingsModal rebuild, now app-wide. Three zones, top to bottom:

1. **Identity header** - emblem/ring/chip + name. Pinned to the top.
2. **The gold rule** - `height: 2, borderRadius: 2, opacity: 0.6-0.7, background: linear-gradient(90deg, transparent, #E5C461, #B8912E, #E5C461, transparent)` (symmetric). Isolates identity from data.
3. **Data zone** - hero numbers, plates, bars. Variable-height content (lifecycle rows, optional sections) collects BELOW; the tops of sibling cards stay level.

**Dosage rule (Jo, 2026-06-12):** the gold rule earns its place in large cards (Settings sections, center cards, stat cards, SA/Director pair). In small repeated cards (chapter performance grid) it reads as noise - tried and removed. Gold that repeats eight times in one grid stops being gold.

**Edge-to-edge bands** (chapter headers in scoring surfaces) use the tint-wash recipe instead: `linear-gradient(135deg, ${color}1c 0%, ${color}0a 42%, transparent 75%), rgba(255,255,255,0.82-0.9)` + gold hairline border. White text on saturated gradient plates is the OLD language - gone.

**Layout integrity:** card-shaped `<button>` elements need `flex flex-col items-stretch` - the browser's native content-centering otherwise makes short cards drift downward inside grid-stretched rows (LESSONS #138). Sidebars that should bottom out level with a neighboring grid use flex stretch + `flex-1` rows, never computed heights.

#### 5. Identity rings and the jewel series

**The ring** (icon tiles, replacing flat tinted squares): white circle, `1.5px solid {color}40-59` border, `boxShadow: 0 6-8px 14-18px -6/-8px {color}40, inset 0 0 0 3-4px {color}0f-14`. Used by: Settings gear, SA/Director pair, submissions rows, domain cards, empty states.

**The jewel** (center capsule) - one design, three sizes:
- Moderator header: emblem 30, text 14.
- Director header: emblem 28, text 14.
- SA page identity: emblem 44, text 22 (replaces any big-title + English-subtitle block).
Recipe: `rgba(255,255,255,0.82-0.85)` + `rgba(196,176,128,0.45)` border + blur(16px) saturate(130%), RTL, name in ink + ` · ` + city in gold `#B8912E`, `nameAr.replace(` في ${locationAr}`, '')`.

**Header brand position is hierarchy:** tool name CENTERED on the All Centers view; LEFT (with the center jewel centered) inside a center.

**Ghost emblem:** the center's seal watermarks its own dominant panels - absolute corner, size 170-190, `opacity: 0.05-0.06`, pointer-events none.

#### 6. Hero numbers

The number is the hero; the label explains it. `font-extrabold` + `tabular-nums` + `lineHeight: 1` + `letterSpacing: '-0.02em'` on percentages. Sizes: quadrant values 19px, chapter % 20px, ring % 16-24px, big counters 26-30px, row-level hero % 18px. Labels: 10px uppercase tracking-wider `#a39574` ABOVE the value. `lineHeight: 1` is what lets values grow without moving the layout. Counts in repeated rows sit in fixed-width chips (`minWidth: 38`) so they align like a table. **Verdict words** (Ready / At Risk) are set in Lora - a word is a certificate, not a number.

#### 7. Motion standard

Swim curve `cubic-bezier(0.2, 0.7, 0.3, 1)` everywhere. The FLIP drop-list standard (LESSONS #133) plus the v2.6 amendments:

- **Every reveal has a conceal** (LESSONS #135): exit twin keyframe (`saConceal`), two-phase close (sweep shut → FLIP back), `forwards` + overflow clip + padding collapse inside the keyframe.
- **Smooth scroll both ways:** glide on open AFTER the FLIP settles (~520ms); on close, glide at sweep start AND settle-glide after the FLIP-back. `overflowAnchor: 'none'` on animated grids.
- **Never freeze motion mid-flight** (LESSONS #136): scroll locks defer (~520ms) until the opening glide lands; measurements use settle-polls (two consecutive identical reads), never fixed timeouts.
- `prefers-reduced-motion` short-circuits all of it, always.
- Modal entrance: `modal-in` scale(0.95)+translateY(10px) → identity, 0.22-0.25s.

#### 7b. Ambient 3D layer - the cherry, never the cake (2026-07-10)

A garnish tier ABOVE the doctrine, never a replacement for it: quiet 3D-feel life (CSS 3D + canvas projection, ZERO libraries) that gives a surface its intention without ever carrying information alone. Jo's framing: professional yet engaging, never visually impairing. One ambient element per surface, waiting/landing surfaces only - a LIVE work surface (scoring inputs, editors mid-work) stays still.

**The laws (each one bought by a 2026-07-10 field-walk correction):**

- **Presentation-only, by construction.** `pointer-events: none`, `aria-hidden`, zero data paths: no `storage.*`, no sync, no handlers exported. An ambient layer that authors a write is a defect by definition (cf ERR-137/138 law).
- **One stage, not scattered popups.** Concentrate the life in ONE place near the subject (the scattered six-spot echoes were "visually disturbing"; the single scoring theater below the card was "exactly what we want").
- **FX layers own their opacity.** Never nest the life inside a watermark's low opacity - the whole bloom died under the ghost's 0.13 until aura/motes took their own layer (`amh-bloom-fx`).
- **Truthful simulation only.** Real component anatomy, real terminology (Met / Partially Met / Not Met), real colors from the one source (`getDomainColor(chapterId).primary`), real logic: a Fully Met item never generates a finding, an Enrichment proposal is ACCEPTED in a dialog before it reflects below. No fake numbers on pages that own real ones - wire the page's value via props (`nowPct={analysis?.summary?.complianceRate}`) or show none.
- **Calm rhythms - everything rests.** Play-then-rest beats infinite loops: choreographies run whole cycles (iteration count via `--amh-runs`) and stop on `animationend`, NEVER on timers guessing the stop moment (the "one paper jumped" cure); content micro-pulses (name swap ~5s) ride separate from motion breaths (~2min); shine VISITS (sheen every 10s), standing emblems do not float.
- **Cursor theater grammar** (for scripted simulations): glide (swim curve ~1s) → hover face on arrival → pointer becomes a HAND → press (scale dip) → consequence. Waiting spot lives NEAR the action; no cross-card travels.
- **Performance guards, always:** `prefers-reduced-motion` collapses to a meaningful static pose (never blank); rAF loops pause via IntersectionObserver + `document.hidden`; phone untouched by construction (`src/phone/` separate; `hidden md/lg/xl:block` guards on desktop). ONE deliberate exception (Jo's call, 2026-07-12): the phone's link sheet carries the link-pulse - CSS-only, no canvas, no rAF, one run per sheet open, reduced-motion hidden. Any future phone ambient element inherits exactly these limits. A SECOND deliberate exception (Jo's call, 2026-09-29): the landing page's governance film runs on the phone too (canvas, rAF) and loops by Jo's word (take one, take two, it goes, it runs again), with every guard on: it pauses off screen and in a hidden tab, drops its drawing quality on a slow device, and shows one still under reduced motion (`src/landing/film/`).
- **Composited motion only (the 2026-07-12 pulse cure).** Ambient travel animates `transform` + `opacity`, NEVER layout properties (`left`/`top`): a layout animation repaints every frame over blurred backdrops, and the compositor-layer release at `animationend` snaps a shade shift a trained eye catches. Keep the layer alive with `willChange`, and let a traveling light DISSOLVE IN MOTION (opacity gone by ~94% of the run) - never die at the wall.
- **True WebGL (Three.js) is post-visit, calm-window, valve-gated, desktop-only.** The canvas point-cloud (~700 hand-projected points) already delivers the WebGL feel at zero bundle cost.

**Reference implementations - `src/components/heroes/AmbientHeroes.jsx` + `ambientHeroes.css` (all `amh-` prefixed):**

| Pattern | Component | Home |
|---|---|---|
| Living watermark (aura + motes + float around an existing ghost) | `HeroEmblemBloom` | Dashboard mod-hero |
| Shiny standing badge (sheen visit, no float), ONE identity across boot + chrome | `HeroAssessCrest` | `Header.jsx` + `HydrationSplash.jsx` |
| Choreographed object story (fan → bind → seal) + calm rhythm + name pulse | `HeroReportBind` | ReportEditor narrative plate |
| Metaphor with real data (plates + slats bridging the gap) | `HeroGapBridge` | GapAnalysisView hero |
| Canvas 3D point-cloud morph (؟ → ✓, glyph-sampled, hand projection) | `HeroMirrorCloud` | SelfAssessmentHome panel |
| Full scripted-cursor simulation (verdicts + Enrichment + acceptance dialog + reflect) | `HeroScoringTheater` | NewAssessmentPlate |
| Seal visit on a standing page (the sealed-deliverable intention: seal lands once, sheen visits every 10s; the matured sage/brass plate rode the same pass) | `HeroSealVisit` | CenterDashboard download dialog |
| Link pulse (the LINK's voice, everywhere a link appears: teal jewel settles + ONE light pulse travels the URL line per open, then rest; transform-composited travel + dissolve-in-motion + willChange layer kept) | inline per surface (`phn/dsk/ed` keyframe families) | PhoneEditorialView link sheet · CenterDashboard share dialog · ReportEditor /r/ dialog · ReportEditor 24h card dialog |
| Brand-jewel sheen (a standing mark's shine VISIT, the HeroAssessCrest rhythm at 10s; CSS-only `::after` sweep) | `sg-brand-icon::after` | StandardGuideView header (the guide's ONE ambient stage) |
| Doc descent into the tray (download intention; one run per open + gold-thread glow) | `HeroDocDescent` | library pattern, currently unmounted (Jo's field revision 2026-07-12 preferred B + C in the dialogs) |
| A jewel in depth (the update intention, Jo 2026-10-08: "a 3D SVG icon"): the house teal tile with its thickness and gold edge rises over its own shadow, then floats a breath above it every 5s (Jo: "3D animated") while the shadow tightens, its embossed arrows turn once at each crest and rest between, the light visits its face every 10s right after a turn; after the refresh press the arrows turn until the page reloads; a still jewel under reduced motion | `UpdateJewel` (in `UpdatePrompt.jsx`, rules `dx-upd-` in `overlaySheet.css`) | the update dialog |

Theatrical originals for taste reference: `_mockups/hero-3d-concepts.html` + `_mockups/hero-dialog-concepts.html`.

**Replication recipe:** (1) name the page's intention in one sentence; (2) prototype theatrically in `_mockups/` first; (3) Jo's verdict; (4) production cousin at HALF the drama (opacity, size, rest cycles); (5) insert as an absolute ambient layer inside the existing plate, guards on; (6) ERR-136 gates + sweeps; (7) tune by field walk - tuning knobs live as named constants (`THR_TARGET`, `REPLAY_EVERY_MS`, sheen period).

#### 8. Iconography

A glyph must be the symbol the profession would recognize: LD landmark columns (governance), PC pulse line, MM capsule/pill (the anchor-lookalike was a v1 defect), LB conical flask, MIS monitor, IPC shield, FMS multi-wing facility building (not a house), MOI database cylinders. Audit any new icon against this bar; "abstract but pretty" loses to "instantly recognizable".

#### 9. Typography, numerals, hygiene

Lora (English serif, titles + verdicts) · Noto Naskh Arabic (Arabic) · mono only for keys/slugs. **Western numerals (0-9) always**, even inside Arabic prose: Arabic date formatting must use the `'ar-u-nu-latn'` locale, never bare `'ar-SA'`; the sweep is `perl -CSD -ne '... /[\x{0660}-\x{0669}]/'` - WITHOUT `-CSD` the check silently passes violations (LESSONS #139). No em-dash anywhere Jo sees a string. `%` is Latin.

#### 10. Jo's taste - the decision heuristics (هوية الذوق)

What two days of correction rounds distilled. Apply these BEFORE he has to say them:

1. **Strips get retired, not recolored.** A full-width band that isn't chrome must either become a card, become chrome, or have its contents rehomed and die.
2. **Duplication is a defect.** A "4 Centers" capsule above four visible center cards, two saved-state pills, a center name repeated under itself - remove, don't restyle. Every element must add value a neighbor doesn't already provide.
3. **Landing surfaces fit one viewport.** Jo's users don't scroll to discover. Compress one notch everywhere before inventing new layouts. (One exception by Jo's call, 2026-09-29: the login page on a phone gives its first screen to the film and scrolls once to the four centers; desktop and iPad stay one screen.)
4. **The first question answered at a glance.** Non-technical directors ask "وين وصلت؟" - a decision ring or hero number answers it before any reading. Simplicity for the audience outranks density.
5. **Consistency across portals, distinction for special pages.** Moderator and director see the same language (same trays, capsules, pills, anatomies). A special surface (SA page) may stand out via composition, never via a different language.
6. **Components float, never melt** (LESSONS #134 corollary). Borders + shadow + radius stay on every functional panel; "blending" means the canvas unifies, not that edges dissolve.
7. **Tops align, variance sinks.** Within a card row, identity/data zones pin level; optional content differences collect at the bottom.
8. **Numbers earn prominence through weight, not size inflation.** lineHeight 1 + extrabold inside the same line box - the component must not grow.
9. **Old design tells:** saturated gradient plates with white text, mint greens, indigo accents, cool slate text, flat tinted icon squares, blue in-progress states, loud green status chips. Seeing any of these = the surface predates v2 and needs the treatment.
10. **He will test with his eyes.** Walk every state (empty, draft, complete, locked) before delivery; the state he finds broken is always the one not walked.
11. **One canvas, one water (2026-07-12, the guide's two-pools cure).** The app body's paper `#faf7f0` is THE canvas; a sub-surface never carries its own neutral. Two neighboring neutrals read as two pools, and every matured component over the foreign one floats like an island with strange corners. Blend the water first - each surface's identity then lives in its components, not its backdrop. Jo's phrasing: "الجميع دامج، تنفسوا مع بعض، مطبوخة مع بعض."
12. **Feedback timing: no dead clicks, no flashes - hold BOTH.** Progress chrome mounts at the click only if the work is still running after ~400ms (the show-delay); an instant result shows the result itself; a failure mounts immediately. A capsule that flashes for 0.1s is noise; a click silent for a second is a dead button (the 2026-07-12 capsule cure, `startExportCapsule`).

#### 10b. The 2026-06-13 sweep additions (locked doctrine)

Born in the all-night v2.6 rollout across Gap Analysis, SA report, Saved
Reports, scoring, toasts, and capsules. These are now law:

- **Enrichment has ONE identity: gold.** The sparkle trigger ring, the
  Suggested Finding dialog (rail, header ring, version chip, shimmer), and
  the refine field's armed state all speak `#B8912E / #E5C461`. Violet and
  blue on any rewrite/enrichment surface are pre-v2 tells.
- **Activity colors are the MUTED set, app-wide.** `ACTIVITY_TYPES` in
  `src/lib/config.js` carries DOC `#5378A0` / INT `#5C8567` / OBS `#B5874A` /
  PER `#7E5F92` / MRR `#9C5E2F` - the same family as the PDF's
  getActivityColor, so screen and print match. The bright v1 set
  (`#3498db`...) must not return.
- **Score-capsule button standard:** unselected = white capsule, 1.5px tone
  hairline, tone text; selected = solid tone gradient + top inner highlight
  + tone shadow + scale 1.06; hover = tone tint lift. N/A stays slate.
- **Wash-from-the-rail grammar at row scale:** score/state feedback on rows
  and standard headers is `linear-gradient(90deg, tone-alpha 0%, transparent
  ~55%), #ffffff` anchored at the left rail - never a full-plate tint, never
  a vertical fade.
- **Toasts:** top-RIGHT below the chrome (top 76 / right 24), warm paper
  card + jewel-ring icon + tone rail, 5s duration. Info = teal, never blue.
- **Generation capsule:** keeps its dark accent identity; the progress fill
  is the gold gradient (one "work in progress" face with the enrichment
  chip), gold hairline edge, warm overlay tokens.
- **Scope truth:** every "full scope?" computation uses the fixed
  `APP_DOMAIN_TOTAL` universe; badges derive from saved content first
  (LESSONS #142).

#### 11. Pre-delivery checklist

- [ ] Page has exactly one `.phc-canvas`; every surface is card / bare label / chrome.
- [ ] No cool-black shadows, no 0.72 translucency, no forbidden colors (§3).
- [ ] Gold rule only where the card is large enough to carry it.
- [ ] Buttons-as-cards are flex-col; rows of cards top-align.
- [ ] Every reveal has a conceal; reduced-motion respected.
- [ ] Ambient 3D layer (if any): one per surface, presentation-only, rests after playing, truthful logic + real colors, guards on (§7b).
- [ ] `perl -CSD` Eastern-numeral sweep clean; no em-dash in strings; tabular-nums on data.
- [ ] Locked = slate, draft = amber, success = mature sage, help = teal book.
- [ ] esbuild parse on every touched file; full `npm run build` on Jo's Mac before commit.

#### 12. Version 5 on PHC (2026-09-29): the phone first, the desktop next

The phone layer now speaks StandardsHub v4's version 5 "light and depth" language (the donor's MAIN language; its Facility Tour's night world is one activity's special place and never covers the professional look). Four materials, with PHC's own values: **atmosphere** (a pearl-blue mist lit by the chapter's colour), **porcelain** (cards that float, washed from one corner, never striped), **jewels** (the one lit action per screen, PHC teal `#1f8f89` to `#084848`; a chapter's jewel on its own colour), **glass** (chrome and docks). Scores wear the calm version 5 states (met `#3f6b3a`, partial `#86652b`, not met `#97474a`, n/a `#756a58`), not the saturated board set. Motion rides the swim curve; nothing loops; every reveal has its conceal.

**Doctrine added this round (Jo):**
- Chapters keep PHC's official identity everywhere (code jewel on `getDomainColor(id).gradient`, white ink, English name with the Arabic under it); a themed world never restyles them.
- Drama comes from light, not ornament: the Facility Tour is StandardsHub's night floor plan in PHC's navy and teal with one lamp over the station's head and darkness gathering away from it; the galaxy's stars were removed because they distract.
- Reading surfaces for senior surveyors never shrink their type to make room; fold or scroll what is crowded.
- An entry point changed on one form factor changes on its twin in the same pass.

**Where it lives.** Tokens and materials: `src/phone/phoneSkin.css` (on `.phx`); drawn parts: `src/phone/phoneKit.jsx`; the tour's night: `src/tour/tour.css` (on `.tour`). Method and the guide's rules: `MOBILE_INTERFACE_BUILD_GUIDE.md` §15; the tour: `FACILITY_TOUR_BUILD_GUIDE.md`. **The login page (2026-09-29)** is the first shared surface in version 5 on both form factors, on a porcelain paper that keeps the inside's warmth without its yellow (Jo: "not very far from the inside, but more well designed", then "too yellowish, you could do better, even inside"): its root carries `.phx` with the tokens re-toned to a near-white stone and a slate shade, its own rules live in `src/landing/landingSkin.css` (prefix `lp-`: two corner pills instead of a full-width bar, glazed ceramic tiles, the teal biometric mark, Thmanyah for the Arabic with words that float), and its film in `src/landing/`; Jo's decisions are in `DESIGN_SYSTEM_UPGRADE_PLAN.md` §6 item 4. The desktop kit should start from this pairing: version 5 materials on the porcelain paper, gold only as fine threads, not the cool mist and not the cream. **Next:** one shared token set and a desktop kit for the desktop components, recommended in `_docs/06_audits/DESIGN_SYSTEM_UPGRADE_PLAN.md`.

#### 13. The desktop's first page in version 5: All Centers (2026-09-30, `ec3bb37`)

The patterns the moderator's All Centers page set for every desktop page after it (Jo's calls in `DESIGN_SYSTEM_UPGRADE_PLAN.md` §6 item 5; the pathway, red lines and risk register for the next pages in `_docs/06_audits/DESIGN_UPGRADE_RISK_PLAN.md`):
- **One plate for the page.** Every plate on a page shares ONE recipe, declared once on the page root: `--plate-radius`, `--plate-glaze` (a white highlight over a porcelain gradient), `--plate-grain` (a fine ceramic grain), `--plate-float` (the lip, the hairline ring, a near shade and a long far one). A plate may add its own light over it (a card's center colour from its top corner, the house teal from a masthead's seal corner) but never a different material. Tiles inside a plate become lines (hairlines on the text's axis, never across a jewel); a tile rises only under the pointer.
- **The masthead.** A page's name does not float apart from its first plate: the emblem, a small caps kicker, the title with its Arabic, the page's measures on the right, a fine gold thread, then the plate's content. Every line of text starts on one axis; the emblem stands in the margin.
- **A ledger over a grid aligns to it.** When a plate reads across the items shown below it, its columns land on theirs (the Portfolio Overview's first column is the chapters column's width, its centers stand over the cards). Figures are Lora numerals with a raised small percent over a fine jewelled thread with a bead at its tip, never a thick bar.
- **The app emblem** (`src/components/AppEmblem.jsx`): the eight chapters as eight segments with square ends, the gold check at the heart, the teal jewel with the house gold rim along its foot (a masked crescent). It names the tool wherever the tool names itself; its light visits every ten seconds (`shine`), never under reduced motion.
- **The app bar** (`Header.jsx`, `ab-` classes in `index.css`): porcelain glass over whatever scrolls beneath, a soft float instead of a floor line, no gold bar along its top; porcelain keys in the ink family, the guide's key the one teal jewel; the active tab on a fine gold thread.
- **Fitting a screen.** A page meant to read on one screen is sized under the app bar (`calc(100dvh - 64px)`, ERR-153) and stands centred in it. It is SCALED as one piece where the screen allows (a zoom step in the stylesheet, guarded by width AND height), never stretched: stretched rows hollow the cards. Minor means minor: a spacing wish is a stylesheet tweak, never a new mechanism.
- **Prefixes on the desktop:** `dx-` for the desktop layer (`dx-co-`, `dx-pf-` on this page), `ab-` for the app bar; a page's rules in its own stylesheet imported by its component (`src/components/centersOverview.css`), the house tokens from `src/phone/phoneSkin.css` via `.phx` on the page root. A dev-only preview per page (`centers-demo.html`) lets Jo review before a deploy.

#### 14. The desktop pages in version 5 (2026-10-06/07): the dental portal's sheets as the reference

Jo's verdict on the first guide and board skins (2026-10-07: "no glossy appearance ... no neon colors in the chips ... muted, or at least a luxury feel ... the cards all have the same color, they should have gradient shades ... one block, not edited") set the rules every later pass follows:

- **Materials, read from the dental portal's own files** (`StandardsHub v4/src/core/design/tokens.css`, `core/ui/guideReader.css`, `shells/desktop/board/board.css`), never from memory: the atmosphere as the ground (celadon mist lit by a pool of the page's tone and a pool of gold, a grain); matte porcelain for what is read (`--sheet-face`, a lit top edge, a crisp outline, the three-part `--shadow-rest`; `--shadow-dominant` for the hero); jewels only for what is chosen or named; glass for the chrome. No plate glaze or grain on cards.
- **Colour calmed before any jewel:** `--chm: color-mix(in oklab, var(--ch) 74%, #6b7580)`; the jewel's rim at 0.2; tinted washes at rest, the muted jewel only when chosen. Leadership's blue is the dental portal's (`#2c5282`). The scores' tones are reserved.
- **Hierarchy by shades:** the hero's pool and tide line, the welcome plate's lighter wash, a measure's rim in its tone, a plain card, a groove for the steps, a well for an open text; one radius family (22 to 26 px), one gutter rhythm.
- **Scrolling and chrome:** an inner scroller hides its scrollbar and shows a reading line; a page's head stands on the atmosphere, not in a bar; a standalone takeover fills the page under the bar.
- **Sketches, minimal and CSS only:** a drafting grid fading from a corner, a gold pen stroke under a title, a monoline sketch per chapter as an SVG mask in the chapter's colour, never under words, never a new element.
- **The mechanics of a pass:** hooks only (class names, `data-skin-*`, custom properties in existing style objects) applied by a two-phase anchor script; the look in one sheet under the page's root class with `!important` where inline styles must yield; `check-skin` strict, eslint parity rule by rule, the red-line paths untouched (`git status` on them), shots beside the reference's own shots before pictures go to Jo.
- **No card holds a card, on every page (round 6, 2026-10-07):** the chapter's standards page, the scoring landing and History lost their container cards; each standard, row and record floats on the paper as its own plate. The live round's red stays a gem (`--live`), never a stripe.
- **Proofs without reduced motion:** a pass that emulates `prefers-reduced-motion` switches staggered entrances off and shows what a sheet may have hidden (ERR-157: the board's measures at opacity 0 under `animation: none`); one pass runs without the emulation and probes the computed opacity of what matters.

---

## ح. الصفحة الحيّة واللوحة التي تتحرّك (2026-10-08، الإصدار 3.1)

> **بكلمة جو بحرفها (2026-10-08) عن «كبسولة الذرة»:** «كبسولة الذرة كانت رائعة جدًا، وهي مثال لبناء مواقع حية أو إضافة
> شرائح داخل مواقع»، ثمّ: «فأنا أجيزها»؛ نمطا لا تجربة. وأصلها دراسة صفحة بوريس تشيرني (Boris Cherny) المصوّرة
> (2026-10-07، بطاقتها في `Launching Video/references/cards/boris_cherny-1.md`)، وأداتها `design-language/tools/watercolor.py`.

### ح-1. ما هي

مادّة الورق نفسها تحمل صفحة كاملة لا فيلما فقط: موقعا حيّا كاملا، أو شريحة تُزرع في موقع قائم ورموزها مربوطة برموزه.
والمثال المجمّد `design-language/examples/atom-capsule-v1/` (ملفّ واحد وصوره)، وكلّ جهاز فيه مسمّى بمكانه في الكود.

### ح-2. الأجهزة (كلّ واحد يُعاد استعماله)

1. **عمود قراءة واحد على الورق** (نحو 36rem)، واللوحات تخرج منه إلى نحو 66rem.
2. **مسطرة بوحدة الموضوع نفسه** ثابتة أعلى الصفحة: دقائق الحصّة الخمس والأربعون، أو زمن الحلقة؛ تقرأ موضعها من
   التمرير، وتقفز بلمسة وبالأسهم.
3. **عناوين الفصول من أشياء الموضوع:** شريط الكتاب المعلّق يحمل رقم الفصل. والقاعدة: أشياء الموضوع هي الواجهة.
4. **بطاقة الشفرة:** رقم كبير أو قانون، وحدته، والسطر الذي يُحفظ، ورمز فهرسة صغير؛ ولها وجه «فخّ الاختبار» بلون آخر.
5. **لوحة ساكنة تحتها وطبقات مرسومة وحدها تتحرّك فوقها** بالضرب على الورق، لكلّ طبقة سبب مرئيّ: ضوء المصباح يتنفّس،
   بخار الشاي يصعد، أغلفة الإلكترونات تدور، لهب، فقاعات. لا فيديو مولَّد كامل.
6. **وصولان يناسبان المادّة:** بقعة ماء تنتشر على الورق (قناع ينمو من 1% إلى 270% في نحو ثانيتين)، أو رسم رصاص يتلوّن
   (مرشّح رماديّ بنّيّ يُرفع في نحو 2.4 ثانية).
7. **في الجوّال:** اللوحة العريضة تثبت تحت الشريط وتمشي الكاميرا عليها مع التمرير.
8. **أداة واحدة يحرّكها القارئ:** المستكشف (العدد الذرّيّ من 1 إلى 20 تُرسم أغلفته حيّة، والغلاف الأخير معلَّم، وسطر
   واحد عمّا يريده العنصر)، وأرقامه مطويّة تحته في جدول.
9. **ورشة في الختام** تري كيف رُسمت اللوحات بمراحلها الأربع، لمن يبني لا لمن يقرأ.

### ح-3. القوانين

- **أوّل شاشة كاملة وهي ساكنة:** لا ينتظر شيء ممّا يُقرأ تمريرا ليظهر؛ اللوحات تحت الطيّة وحدها تنتظر وصولها.
- **من طلب حركة أقلّ** (`prefers-reduced-motion`) لا تتحرّك له طبقة ولا يقع وصول.
- **الكلمات لا تُرسم داخل اللوحة أبدا:** العربيّة يكتبها التكوين بخطّه، والمحرّكات تشوّه العربيّة.
- **اللوحات على ورق في الثيمين:** في الداكن تبقى اللوحة على ورقها داخل إطار مطبوع بظلّ، ولا تُقلب ألوانها.
- **أرقام غربيّة، وخطّا العائلة** (نسخ للعربيّة بعناوينها، ولورا للاتينيّة) ما لم يختر المشروع خطّ عرض في ب-1.

### ح-4. أداة الألوان المائية: `design-language/tools/watercolor.py`

لوحة بالحبر والألوان المائية على ورق دافئ من رسمين بحجم واحد يرسمهما الكود: تعبئة بلا خطوط، وحبر بلا تعبئة. مراحلها
بالترتيب، وكلّ واحدة جواب عيب في نسختها الأولى (التي خرجت «قلم خشب على ورق صنفرة»): الورق، الإزاحة، الغسلة، البلل في
البلل، الأضواء، تجمّع الصبغة على الحواف، الحبيبة الهادئة، الأزهار، التلاشي إلى الورق، ثمّ الحبر بضغط الريشة وانقطاعها
وخطّ رصاص خفيف تحته. بذرتها ثابتة فتعيد اللوحة نفسها بالبكسل. والأمر:

```
python3 design-language/tools/watercolor.py <flat.png> <ink.png> <out-dir> <name> --stages
```

`--layer` يخرج طبقة على أبيض تُضرب فوق لوحة بحجمها، و`--bleed <out.png>` يخرج قناع الانتشار. والمثال المجمّد
`design-language/examples/watercolor-v1/`. وتبقى مفتوحة من التجربة: أزهار ثقيلة على مساحة رماديّة كبيرة، وحافّة رقميّة
خفيفة في الحبر عند تكبير 200%.

### ح-5. ماغنيفيك ون مرشّحا (لم يُختبر)

موديل صور يحسم الإخراج الفنّيّ قبل أن يرسم: مسودّة من 4 أو 8 أو 16 اتّجاها، ونهائيّة بدقّة 2K أو 4K، وعدّة هويّة تُبنى
من موقع أو ملفّ أو صور وتُفحص عليها النهائيّات. يصل إلى كلود برابط MCP مخصّص على خطّة ماغنيفيك مدفوعة، ويأكل رصيدا مع
كلّ توليد حتّى للموديلات غير المحدودة في الخطّة. لا اشتراك قبل كلمة جو؛ ويدخل فقط إن غلب محرّكنا الحاليّ على المشهد
نفسه بعين جو، والعربيّة داخل صوره لم تُجرَّب. تفاصيل التسعير والاختبار في `Launching Video/build-reference/08-spend.md` 8.8.

### ح-6. التقسيم بين البيتين (بكلمة جو، 2026-10-08)

**استوديو الإطلاق** (`Launching Video/`) للفيديو والترويج: اللقطات واللوحات المتحرّكة في الأفلام، وماغنيفيك في مسار
الصرف. **وهذا البيت** لتصميم الواجهات: الصفحة الحيّة، والحركة على الشاشة، والأصول. والأداة نفسها في البيتين نسختان من
ملفّ واحد؛ ومرجعها في الواجهات هنا، وفي الأفلام هناك.

---

## ملحق: سجلّ الإصدارات 2.x (نُقل بحرفه من رأس الملفّ في 3.0)

> **Status:** Living document. Captures the design identity as crystallized through the v2 caravan (2026-06-11/12), the v2.6 app-wide rollout (`2905f21`, 2026-06-12), the v2.8 lift language born on Qimma's coach reading (2026-09-02, §2b, §10 #13-#16), and the v2.9 figure language born on Qimma's geometry questions (2026-09-02 evening, §2c, §10 #17-#18), and the v2.10 door rules born on Qimma's law band (2026-09-10, §10 #19-#20), and the v2.11 paper language born on Qimma's home and stations (2026-09-23, §13, §10 #21-#23), and the v2.13 ring law and gift card born on Qimma's placement result (2026-09-25, §14). v2.15 adds the question visit page and the verdict in the paper's tone (2026-09-25, §13-و). v2.16 records the night of 2026-09-25 (rounds 170-172: the picker, the question page 2.0 with its watercolor lane backgrounds, and the laws board) as a journey and a build reference with the real values from the code (§15), with the iPhone Safari lesson of round 174 (an aspect-ratio grid item needs an explicit width). v2.17 adds the picker on the desktop (round 176, §13-ي: the watercolor desk, 16:9 cards, equal-column filter tiles, a drawing multiplied into its header paper, §15-د 12, §15-هـ 10), and 176-ب replaces the picker's inset filter track with raised paper tiles from the header buttons' family (§15-ج 4-ب) and puts the count and the ghost number in opposite bottom corners, dropping the redundant «القسم N» label (176-ج). v2.18 (rounds 177-179): the question page's number row and the «أسئلتك» filters become raised tiles with the answered question as a filled gem (§15-ج 4-ج), the question sheet is one component across answer pages (§13-و, 178), and the reading pages' buttons and closing tiles get their recipe (§15-ج 2-ب, 179). v2.19 (round 180): the closing numbers become ONE raised ledger whose colour lives in the ink (a gem and a pen meter per column), not in four tinted squares; the comparison is its footer, the advisor door is the one dyed button with a gold seal, topics are two titled groups, and question numbers are gems in raised paper (§15-ج 2-ب). v2.20 (round 181): the closing page's save/print bar (a sentence and three buttons: print / standalone page / download) is removed by Jo's word, so the closing page ends at the questions door and the print, open and download icons leave the icon set. v2.21 (round 182): the record («سجلّي») is a hero paper with a fan of the station art and a three-column ledger, filters are five equal raised leaves each with a gem in its group tone, entries are standalone papers with their type's art stamped in a corner, the desk is a watercolour that follows the filter, the shared station back button is a paper leaf with an icon plate, and the wide flat row block is banned from every design (§13-م). v2.22 (round 186): reading doors are one face with a gold seal for a fresh reading, not a teal fill (§15-ج 2-ج). v2.23 (rounds 183, 184, 185, one bump): the pending-round block's first action is raised paper whose tone lives in a gem and a bottom line, the second is quiet paper (§15-ج 2-د); a reference page wears the shared station head as a hero from its own scope, its long list of equal texts flows in two columns (`columns:2`, never a row grid), and a ghost number replaces the numbered ball (§13-ن); every ring that carries a percentage is one score medal (`ScoreMedal.jsx`, `medal.css`) with a paper face, gold rim, graduated track, quarter ticks, a gem riding the arc and five named tones (§14 item 7). v2.24 (round 187): the call-lessons page: a behaviour is a raised paper with a gem in its tone and a pen line under its name, its next step an inner wash (never a box in a box), calls as hairline rows; a filter grid never leaves an orphan (`filterGrid(n)`); behaviour shades come from the section image's family, ordered so near shades never touch (§13-س). v2.25 (rounds 189, 190, 191, one bump): every dialog is one pearl paper with a seal whose face comes from its meaning, one dyed action at most and none on an erasing face (§13-ع); the question option is white from top to bottom so it rises off its paper and never sinks into it (§15-ج 2-هـ); and the quiet second action wears a sand face one step deeper than the container it sits in, at its own width on the phone (§15-ج 2-د). v2.26 (rounds 195, 196, 200, 201, one bump; 195 owns the guide in this batch): a medal is drawn, never a picture with a number: a shape per track (a toothed coin with ribbons, a shield, an eight-point star, a hexagon), a metal per rank (bronze, silver, gold, the top rank gold with a gem crown), a pearl face with the track glyph and the number; a locked medal is the same shape greyscale at .36, the next one wears a gold progress arc; «إنجازاتي» is a hero paper with a fan of four medals and a four-column ledger, then one raised paper per track shelf; the medal moment is the decision paper with the medal as its seal (§13-ف). The waiting card (196, §15-ج 2-و), the one-thing windows as raised tiles (200, §13-م), and the tour panel inside a dialog (201, §13-ز) arrive with their merges. v2.27 (rounds 203, 204, 205, 207, 208, one bump; 203 owns the guide in the batch 203-209, and 209 adds its own at merge): a tag has ONE face in the whole app and one home, `src/styles/gem.css`: the status chip (`.gem-chip[data-gem]`) is a small raised paper chip in page ink with the status as a gem before the word (sage ok, brick alert whose word alone takes brick ink, amber watch, gold chance and waiting, pulsing teal running, a gold seal for new, a hollow slate ring for no data), an icon becoming the gem when the chip stands alone; the change figure (`.gem-delta`) is a sentence, not a tag: a drawn triangle coloured by meaning and the number in ink; a row label that only repeats its card's title becomes a gem at the start of the row; and no surface dyes the chip, it only places it (§15-ج 2-ز, §12). The picker's subordinate axis is two raised pills at their own width with no track (204, §15-ج 4-د), and what lives in the advisor capsule never moves in `steps()` and follows the voice by time, not by frame (205, §15-ج 14-ب). The account panel is a pearl paper of the decision family whose seal is its owner's photo in a ring of their tone, its doors hairline rows each with a gem, and its two actions equal undyed papers with the exit in brick ink (207, §13-ع). The dashboard sits on a watercolour desk, each tab opens with a hero line in the display font over a gold pen stroke and its icon as a ghost, its tiles are one ledger with hairline gaps and the source hint on the tile's tail, no card wears a colour stripe (attention is a corner wash), and its tags wear the one tag (208, §12). All four arrive with their merges. v2.28 (round 209, added at its merge): the «إنجازاتي» hero is the home of the levels program: a pearl crest with a gold ring and progress arc carrying the overall level, the rank in the display font, a weekly challenge paper with seven gold day beads, and a five-column ledger of titles (rows on the phone); the level-up seal is the one tag with its gold `new` gem (§13-ف). v2.29 (rounds 210 and 211, one bump; 210 owns the guide in the batch 210-211): a page opened from an attempt stands on that attempt's watercolour desk even when it renders outside the attempt's wrapper, so the advisor reading, waiting or read, is no longer a flat sand wall; its head carries the attempt type's art as a stamp in a slot that contains it whole; a page says its state once (no head chip over a card that says it) and shows the advisor's face once; a sentence title takes a short pen stroke under it, never the highlighter band, which slabs under every line once a sentence wraps; and a page inside a running round keeps its lane desk (§13-ج addendum 210). The shared back button reaches every page that returns somewhere, the laws board included, with its plate tone taken from the destination and no gold or typed-chevron back button anywhere (211, §13-م). v2.30 (round 213, added at its merge because the batch's guide owner, 210, merged before it): the advisor capsule's seat is written once on the dock and read back from it, never kept in a local of an effect that re-runs on every render; it is computed in the page box, not the screen, since a phone's screen widens with whatever overflows; the dial line flips toward the centre when the dock's outer side has no room for it; and motion is measured with a fake call that re-renders the component, not with classes toggled by hand (§14-ب). v2.31 (round 214, ported from the uncommitted Cowork round of 2026-09-25): the report picture is a paperclip button under the note, asked for by the note itself, with a 56 px thumbnail and a way to remove it, and the console badge wears the shared chip (§2d-5); the fraction is a line box whose bar spans its widest line and never wraps, and every sign is isolated at render time in the one gateway (§16). **This file is the ONE home of the visual language (Jo, 2026-09-02: "evolve our current design reference so that any improvement and maturity of our design will not be scattered across multiple documents"). A design rule that lives anywhere else is a pointer to here, never a second copy.** This is the single home for the visual language; `LESSONS.md` #133-#139 hold the portable versions of the rules born here; `src/index.css` holds the executable tokens.
>
> **Who this serves:** any future session touching UI. Read this BEFORE styling anything. The goal is that Jo (أبو سطام) recognizes every new surface as "his" without a single correction round.
