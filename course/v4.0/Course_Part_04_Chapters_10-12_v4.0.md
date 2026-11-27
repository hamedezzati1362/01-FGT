# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۴ از ۱۱ — فصل‌های ۱۰ تا ۱۲

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۴ از ۱۱ |
| فصل‌های این فایل | ۱۰ ، ۱۱ ، ۱۲ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۱۰–۱۲ تولید شد؛ مبانی تا Baseline FortiGate.** همه‌ی Labها «اجرا نشده»؛ FortiGate هنوز بوت نشده. محتوای FortiGate از مستند عمومی FortiOS 7.0 و دانش مؤلف است و باید در بوت اول تطبیق داده شود. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 20.

| Lab | وضعیت |
|---|---|
| 10-1 | اجرا نشده (فقط طراحی) |
| 10-2 | اجرا نشده (فقط طراحی) |
| 10-3 | اجرا نشده (فقط طراحی) |
| 10-4 | اجرا نشده (فقط طراحی) |
| 10-5 | اجرا نشده (فقط طراحی) |
| 10-6 | اجرا نشده (فقط طراحی) |
| 10-7 | اجرا نشده (فقط طراحی) |
| 11-1 | اجرا نشده (فقط طراحی) |
| 11-2 | اجرا نشده (فقط طراحی) |
| 11-3 | اجرا نشده (فقط طراحی) |
| 11-4 | اجرا نشده (فقط طراحی) |
| 11-5 | اجرا نشده (فقط طراحی) |
| 11-6 | اجرا نشده (فقط طراحی) |
| 12-1 | اجرا نشده (فقط طراحی) |
| 12-2 | اجرا نشده (فقط طراحی) |
| 12-3 | اجرا نشده (فقط طراحی) |
| 12-4 | اجرا نشده (فقط طراحی) |
| 12-5 | اجرا نشده (فقط طراحی) |
| 12-6 | اجرا نشده (فقط طراحی) |
| 12-7 | اجرا نشده (فقط طراحی) |

---

<a id="ch10"></a>

> **نسخه‌ی اصلاح‌شده (v3.1، دسته B):** این فایل نسخه‌ی توسعه‌یافته‌ی `course/Course_Part_04_Chapters_10-12.md` است؛ فایل اصلی حفظ شده است. درس‌های افزوده: ۱۰-۸ و ۱۰-۹ (فصل ۱۰). پاسخ‌های آن‌ها در «پاسخ‌های فصل» همان فصل است.

> **نسخه‌ی اصلاح‌شده (v3.9):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۱۰-۸، ۱۰-۹، ۱۱-۰، ۱۱-۷، ۱۲-۰، ۱۲-۸، ۱۲-۹ (دسته‌های B و A). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

# فصل 10 — Redistribution، ECMP، PBR، VRF-lite و Asymmetric Routing

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۹ (BGP)، فصل ۶ (OSPF).
**اهداف:** انتقال مسیر بین پروتکل‌ها بدون حلقه؛ توزیع بار با ECMP؛ هدایت ترافیک با PBR؛ جداسازی جداول مسیریابی با VRF-lite؛ تحلیل و رفع مسیر نامتقارن.
**چرا برای فایروال؟** فایروال Stateful با مسیر نامتقارن خراب می‌شود؛ ECMP/PBR/VRF همان ابزارهایی هستند که باعث نامتقارن‌شدن یا جداسازی می‌شوند.
**معیار تسلط:** Redistribution دوطرفه با Tag و بدون حلقه؛ پیش‌بینی مسیر ECMP؛ PBR با Track؛ VRF مستقل؛ تشخیص Asymmetric با traceroute دوطرفه.
**اشتباهات رایج:** Redistribution بدون `subnets`؛ حلقه‌ی دوطرفه؛ PBR روی Interface اشتباه؛ نشت VRF ناخواسته؛ بررسی مسیر فقط در یک جهت.

**درس‌های فصل:**
- [درس 10-1 — Redistribution: مفهوم و Seed Metric](#l-10-1)
- [درس 10-2 — Redistribution دوطرفه و جلوگیری از حلقه با Tag](#l-10-2)
- [درس 10-3 — ECMP و توزیع بار](#l-10-3)
- [درس 10-4 — Policy-Based Routing (PBR)](#l-10-4)
- [درس 10-5 — VRF-lite: جداسازی جدول مسیریابی](#l-10-5)
- [درس 10-6 — Asymmetric Routing: تحلیل مسیر رفت و برگشت](#l-10-6)
- [درس 10-7 — طراحی مسیر برای چندفایروالی و آزمون کوچک](#l-10-7)

---

<a id="l-10-1"></a>

## درس 10-1 — Redistribution: مفهوم، Seed Metric، Subnets و Route Type

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۶-۴، ۹-۲ · ≈ 9 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. توضیح دهید چرا Redistribution لازم است و چه خطرهایی دارد.
2. Seed Metric را برای OSPF، EIGRP و RIP تعیین کنید.
3. فرق E1 و E2 را با محاسبه‌ی عددی نشان دهید.
4. Redistribute یک‌طرفه را بین OSPF و EIGRP پیکربندی و تأیید کنید.
5. نقش `subnets`، `metric` و `route-map` را بدانید.
6. خرابی «مسیر وارد نمی‌شود» را با روش مرحله‌ای عیب‌یابی کنید.

### چرا باید یاد بگیریم؟

در سازمان‌های واقعی چند پروتکل مسیریابی کنار هم زندگی می‌کنند: هسته با OSPF، شعب با EIGRP، لبه با BGP. دلیل‌ها تاریخی و سازمانی‌اند (ادغام شرکت‌ها، سازنده‌های متفاوت، مهاجرت تدریجی). هر پروتکل «زبان» خودش را دارد و مستقیم با دیگری حرف نمی‌زند. **Redistribution** یک «مترجم» است که مسیرهای یک زبان را به زبان دیگر می‌گوید. مثل دو شهر با دو واحد پول: بدون نرخ تبدیل نمی‌توان معامله کرد. اگر نرخ (Metric) را اشتباه بدهید، یا مسیر وارد نمی‌شود یا ترافیک از مسیر نادرست می‌رود، یا بدتر: حلقه‌ی مسیریابی می‌سازید (درس بعد).

### چرا Metric مسئله است؟

هر پروتکل مقیاس متفاوتی دارد:

| پروتکل | معیار | نکته |
|---|---|---|
| RIP | تعداد Hop (۱ تا ۱۵؛ ۱۶ = غیرقابل‌دسترس) | ساده |
| OSPF | Cost = Reference BW / BW | ۱ تا ۶۵۵۳۵ برای هر لینک |
| EIGRP | ترکیب Bandwidth، Delay (پیش‌فرض)، Reliability، Load، MTU | ۵ عدد |
| BGP | صفات (AS-Path، MED و ...) | سیاست‌محور |

مسیر OSPF با Cost=20 در EIGRP چه معنایی دارد؟ هیچ. پس وقتی مسیر از OSPF وارد EIGRP می‌شود باید یک **Seed Metric** (متریک اولیه) تعیین کنید؛ بعد از ورود، EIGRP به آن Hop به Hop هزینه اضافه می‌کند.

### قواعد هر پروتکل

**ورود به OSPF:** مسیر به‌عنوان **External** (LSA نوع 5 در Area عادی، نوع 7 در NSSA) وارد می‌شود. روتری که این کار را می‌کند **ASBR** (Autonomous System Boundary Router) است. Seed Metric پیش‌فرض 20 (برای BGP: 1) است و نوع آن E2 است.

- **E2 (پیش‌فرض):** متریک خارجی در مسیر ثابت می‌ماند؛ هزینه‌ی داخلی OSPF تا ASBR **اضافه نمی‌شود**.
- **E1:** متریک خارجی + هزینه‌ی داخلی تا ASBR.

``` text
E2 total = external metric (e.g. 20)
E1 total = external metric + internal cost to ASBR = 20 + 15 = 35
```

E1 زمانی مفید است که چند ASBR یک Prefix را اعلام می‌کنند و می‌خواهید روتر نزدیک‌ترین ASBR را انتخاب کند؛ E2 ممکن است ASBR دورتر را (چون متریک خارجی کمتر) بردارد.

**ورود به EIGRP:** باید ۵ عدد بدهید: Bandwidth (Kbps)، Delay (ده‌میکروثانیه)، Reliability (1–255)، Load (1–255)، MTU.

``` text
redistribute ospf 1 metric 10000 100 255 1 1500
```

به‌جای تکرار در هر `redistribute`، می‌توان `default-metric 10000 100 255 1 1500` زیر `router eigrp` گذاشت. اگر هیچ‌کدام نباشد، مسیرها وارد EIGRP نمی‌شوند (از قدیمی‌ترین خطاها). EIGRP مسیر وارد‌شده را با AD برابر **170** (External) می‌سازد.

**ورود به RIP:** `default-metric` یا `metric` به Hop؛ مقدار 16 یعنی غیرقابل‌دسترس.

**کلمه‌ی `subnets` در Cisco:** `redistribute <proto> subnets` در OSPF؛ بدون آن فقط شبکه‌های Classful وارد می‌شوند و زیرشبکه‌ها (مثلاً 10.5.1.0/24) رد می‌شوند.

### پیکربندی‌های نمونه

**EIGRP → OSPF:**

``` text
router ospf 1
 redistribute eigrp 100 subnets metric 20 metric-type 1
```

**OSPF → EIGRP:**

``` text
router eigrp 100
 redistribute ospf 1 metric 10000 100 255 1 1500
```

**مسیرهای Connected و Static:**

``` text
router ospf 1
 redistribute connected subnets
 redistribute static subnets
```

**فیلتر با Route-map (توصیه):**

``` text
ip prefix-list EIGRP-NETS seq 5 permit 10.5.0.0/16 le 24
route-map E2O permit 10
 match ip address prefix-list EIGRP-NETS
 set metric 30
 set metric-type type-1
router ospf 1
 redistribute eigrp 100 subnets route-map E2O
```

### Verification

``` text
show ip route eigrp                 (on ASBR: are the routes there?)
show ip ospf database external      (Type 5 LSAs)
show ip route 10.5.0.0              (on a far OSPF router)
show ip protocols
```

در روتر دور OSPF: `O E2 10.5.0.0/16 [110/20] via ...` یعنی مسیر خارجی E2 با Metric 20. با `metric-type 1`: `O E1 ... [110/35]`.

### مثال‌های حل‌شده

#### مثال ساده — Redistribute اول

OSPF Area 0 و EIGRP AS 100 در R5. مراحل: ۱) `redistribute eigrp 100 subnets metric 20` در OSPF ۲) `show ip route` در R1 (OSPF): مسیرهای `O E2` از EIGRP ۳) ping به شبکه‌ی EIGRP. اگر `subnets` را فراموش کنید ممکن است فقط /8 (Classful) بیاید.

#### مثال متوسط — E1 در برابر E2 با عدد

R1 فاصله‌ی داخلی تا ASBR-A برابر 10 و تا ASBR-B برابر 40. هر دو Prefix 10.5.0.0/16 را با Seed=20 اعلام می‌کنند.

``` text
E2 : via A = 20 ; via B = 20 -> tie (both 20)  -> picks by lowest forward cost to ASBR = A
E1 : via A = 20 + 10 = 30 ; via B = 20 + 40 = 60 -> picks A
```

با E2 در تساوی، OSPF از «هزینه‌ی داخلی تا ASBR» برای شکستن تساوی استفاده می‌کند. ولی اگر B متریک خارجی 15 داشت: E2: B=15 < A=20 ⇒ B برنده (حتی دورتر)؛ E1: A=30 < B=55 ⇒ A. این مثال تفاوت واقعی را نشان می‌دهد.

#### مثال متوسط — Seed در EIGRP

مسیر OSPF با لینک 10 Mbps و تأخیر 100 μs: `metric 10000 10 255 1 1500` (Bandwidth به Kbps=10000 برای 10 Mbps، Delay=10 (ده‌میکروثانیه برابر 100 μs)). Metric EIGRP با Bandwidth و Delay کمینه‌شده محاسبه می‌شود؛ اگر Seed را بدون دقت بدهید، EIGRP لینک‌های واقعی را سریع‌تر یا کندتر از واقعیت می‌بیند. در عمل یک مقدار مشخص و ثابت (مثلاً لینک پیش‌فرض ۱ Gbps) انتخاب و مستند می‌شود.

#### مثال متوسط — مسیر وارد نمی‌شود

علامت: Prefix EIGRP در OSPF دیده نمی‌شود.

1. `show ip route eigrp` در ASBR ⇒ Prefix هست؟ (اگر نه، مشکل EIGRP است نه Redistribution)
2. `show run | section router ospf` ⇒ `subnets`؟ `metric`؟
3. `show ip ospf database external` ⇒ LSA نوع 5 هست؟
4. روتر دور: Area Stub؟ (در Stub Area LSA نوع 5 وارد نمی‌شود؛ NSSA لازم است)
5. Route-map/Prefix-list رد می‌کند؟
6. پس از رفع، `O E2` ظاهر می‌شود.

#### مثال سخت — دو ASBR و انتخاب مسیر بهینه

شبکه‌ی 10.5.0.0/16 از دو شعبه‌ی EIGRP (A و B) اعلام می‌شود. هدف: روتر هر منطقه از ASBR نزدیک‌تر استفاده کند. راه‌حل: `metric-type 1` و Seed برابر ⇒ انتخاب بر پایه‌ی هزینه‌ی داخلی. آزمون: traceroute از دو منطقه؛ اگر هر دو از A می‌روند، Seed/نوع را بررسی کنید.

#### مثال سخت — Redistribute در Stub/NSSA

ASBR در Area 10 که Stub است؛ LSA نوع 5 ممنوع است و Redistribute بی‌اثر. راه: تبدیل Area به NSSA (`area 10 nssa`) که LSA نوع 7 اجازه می‌دهد و در ABR به نوع 5 تبدیل می‌شود. نشانه: `show ip ospf database nssa-external`.

### Lab هدایت‌شده (اجرا نشده)

1. سه روتر: R1 (OSPF)، R5 (هر دو پروتکل، ASBR)، R9 (EIGRP).
2. Redistribute EIGRP→OSPF با `subnets metric 20`؛ آزمون `O E2`.
3. تغییر به E1 و مقایسه‌ی Metric.
4. OSPF→EIGRP بدون Seed ⇒ مسیر وارد نمی‌شود؛ سپس با Seed.
5. Evidence و جدول «تنظیم ← اثر».

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| مسیر وارد EIGRP نمی‌شود | Seed نیست | `metric` یا `default-metric` |
| فقط شبکه‌ی Classful وارد OSPF می‌شود | `subnets` ندارد | افزودن |
| در Stub مسیر نمی‌آید | LSA 5 ممنوع | NSSA |
| Metric عجیب | E1/E2 | مقایسه |

### نکات امنیتی

- Redistribute بدون Filter می‌تواند مسیرهای ناخواسته (مثلاً Static به Null0) را وارد کند؛ همیشه Route-map/Prefix-list.
- تغییر Redistribute را با CHG و آزمون ثبت کنید.

### جمع‌بندی

Redistribution مترجم بین پروتکل‌ها است. Seed Metric ضروری است. در OSPF مسیر خارجی E2 (ثابت) یا E1 (+ هزینه‌ی داخلی) است و `subnets` را فراموش نکنید. در EIGRP ۵ عدد لازم است. Filter و آزمون از ورود مسیر ناخواسته جلوگیری می‌کند.

### تمرین و ارزیابی

**ت1.** (ساده) Seed Metric پیش‌فرض Redistribution به OSPF چند است؟ *(پاسخ: 10-1-ت1)*

**ت2.** (ساده) چرا EIGRP و RIP Metric پیش‌فرض ندارند؟ *(پاسخ: 10-1-ت2)*

**ت3.** (متوسط) تفاوت E1 و E2؟ *(پاسخ: 10-1-ت3)*

**ت4.** (متوسط) اگر `subnets` نباشد چه می‌شود؟ *(پاسخ: 10-1-ت4)*

**ت5.** (سخت) دو ASBR و تصمیم Type. *(پاسخ: 10-1-ت5)*

**ت6.** (سخت، طراحی) طرح Redistribution یک‌طرفه با فیلتر. *(پاسخ: 10-1-ت6)*

**Q1.** Quick quiz (English): What happens if you redistribute into EIGRP without specifying a metric? *(پاسخ: 10-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ASBR | Autonomous System Boundary Router | روتر مرزی دامنه |
| E2 | OSPF External Type 2 | مسیر خارجی نوع ۲ |
| Seed | Seed metric | Metric اولیه |

- *Redistribution injects routes from one protocol into another.* ← Redistribution مسیرهای یک پروتکل را به دیگری تزریق می‌کند.

### کارت Lab

**کارت Lab:** Redistribution یک‌طرفه. **Evidence:** `03-ops/redist1.md`.

### منابع

- Cisco IOS IP Routing guide: Redistribution
- RFC 2328 (OSPF) بخش External

<a id="l-10-2"></a>

## درس 10-2 — Redistribution دوطرفه، Route Feedback و جلوگیری از حلقه با Tag

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۱ · ≈ 9 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Route Feedback و حلقه‌ی Redistribution دوطرفه را توضیح دهید.
2. با Route Tag حلقه را شناسایی و جلوگیری کنید.
3. نقش Administrative Distance را در انتخاب مسیر نادرست بفهمید.
4. Redistribute دوطرفه‌ی ایمن را با Route-map طراحی کنید.
5. حلقه را از روی traceroute و جدول مسیر تشخیص دهید.
6. راه‌حل‌های جایگزین (یک‌طرفه + Default، Summary) را بشناسید.

### چرا باید یاد بگیریم؟

Redistribute یک‌طرفه نسبتاً ایمن است. ولی در بسیاری از شبکه‌ها دو پروتکل در **دو نقطه** به هم وصل‌اند (برای افزونگی) و باید دوطرفه Redistribute شود. اینجا خطرناک‌ترین حالت است: مسیری که از A به B رفته، می‌تواند از نقطه‌ی دیگر دوباره به A برگردد و A آن را «جدید» بداند. نتیجه: مسیر زیرین (Suboptimal)، ناپایداری یا حلقه. مثل دو دفتر پست که هر کدام نامه‌ی «جدید» را به دیگری می‌فرستند و نامه بی‌انتها می‌چرخد. راه‌حل مهر «ارسال‌شده» است؛ در شبکه این مهر **Route Tag** است.

### Route Feedback — سناریو

``` text
          OSPF Area 0                       EIGRP AS 100
   +----------------+                 +------------------+
   |  R1 --- R2     |                 |   R9             |
   +--|------|------+                 +----|----|--------+
      |      |                             |    |
     ASBR-1 ASBR-2 -------------------------+----+
   (R3: redistributes both ways)   (R4: redistributes both ways)
```

مراحل مشکل:

1. شبکه‌ی 10.5.0.0/24 در EIGRP (R9) وجود دارد.
2. R3 آن را به OSPF Redistribute می‌کند (LSA نوع 5).
3. R4 در OSPF این مسیر را می‌بیند و آن را دوباره به EIGRP Redistribute می‌کند (به‌عنوان مسیر External).
4. حالا EIGRP یک مسیر اصلی (AD 90) و یک مسیر External (AD 170) دارد. تا وقتی مسیر اصلی هست، مشکلی دیده نمی‌شود.
5. با قطع مسیر اصلی، مسیر چرخشی (از طریق R3→OSPF→R4) نصب می‌شود؛ ترافیک می‌چرخد و ممکن است حلقه شود.

### راه‌حل ۱: Route Tag

Tag یک عدد (۱ تا ۴ میلیارد) است که به مسیر هنگام Redistribute می‌چسبد و در پروتکل می‌ماند (در OSPF و EIGRP پشتیبانی می‌شود).

``` text
! On R3 and R4 (both ASBRs)
route-map EIGRP-TO-OSPF permit 10
 set tag 100
route-map OSPF-TO-EIGRP deny 10
 match tag 100
route-map OSPF-TO-EIGRP permit 20
!
router ospf 1
 redistribute eigrp 100 subnets route-map EIGRP-TO-OSPF
router eigrp 100
 redistribute ospf 1 route-map OSPF-TO-EIGRP metric 10000 100 255 1 1500
```

منطق: مسیری که از EIGRP به OSPF می‌رود Tag 100 می‌گیرد؛ هنگام برگشت از OSPF به EIGRP، اگر Tag=100 دارد رد می‌شود. بنابراین مسیرهای اصیل OSPF (بدون Tag) به EIGRP می‌روند و مسیرهای «برگشتی» نمی‌روند.

### راه‌حل ۲: Prefix-list

اگر می‌دانید کدام Prefixها از کدام سمت‌اند، فقط همان‌ها را اجازه دهید:

``` text
ip prefix-list OSPF-ORIG seq 5 permit 10.1.0.0/16 le 24
ip prefix-list EIGRP-ORIG seq 5 permit 10.5.0.0/16 le 24
```

### راه‌حل ۳: AD

مشکل زمانی بدتر می‌شود که AD مسیر وارد‌شده کمتر از مسیر اصلی شود. مثلاً OSPF External=110 و EIGRP External=170، EIGRP Internal=90، OSPF Internal=110. اگر در یک روتر دو مسیر برای یک Prefix از دو پروتکل هست، AD بین آنها حکم می‌کند؛ مسیر درست ممکن است بازنده شود. با تنظیم `distance` می‌توان مسیر External را بدتر کرد یا مسیر خاصی را ترجیح داد:

``` text
router eigrp 100
 distance eigrp 90 150
```

(Internal=90، External=150.)

### راه‌حل ۴: طراحی ساده‌تر

- ترجیحاً **یک نقطه** Redistribute (یک جفت روتر ASBR با افزونگی کنترل‌شده).
- یک‌طرفه + **Default Route** از هسته به EIGRP، و Summary از EIGRP به OSPF.
- حداقل Redistribute و حداکثر Summarization.

### Verification

``` text
show ip route 10.5.0.0
show ip ospf database external 10.5.0.0
show ip eigrp topology 10.5.0.0
traceroute 10.5.0.1
show route-map
```

برای دیدن Tag: `show ip route 10.5.0.0` خط «Route tag 100»؛ `show ip ospf database external` فیلد «External Route Tag».

### مثال‌های حل‌شده

#### مثال ساده — شناسایی Feedback

R3 و R4 هر دو دوطرفه. `show ip route 10.5.0.0` در R4 دو مسیر دارد: EIGRP داخلی (via R9) و EIGRP External با Source «Redistributed from OSPF». نشانه‌ی Feedback.

#### مثال متوسط — اجرای Tag

با بالا: پس از اعمال Route-map، در R4 فقط مسیر داخلی باقی می‌ماند و مسیر External حذف می‌شود. تأیید: `show ip eigrp topology 10.5.0.0` یک ورودی. آزمون منفی: قطع لینک R9–R4؛ مسیر باید از R3 برود (مسیر EIGRP داخلی از R3) و بدون حلقه.

#### مثال متوسط — AD نامطلوب

در R4 مسیر اصلی EIGRP (AD 90) و مسیر OSPF External (AD 110). EIGRP ترجیح داده می‌شود؛ خوب. ولی اگر `distance` را 80 برای OSPF External تنظیم کرده باشند، مسیر OSPF برنده می‌شود و ترافیک زیرین می‌رود. بررسی: `show ip protocols` فیلد Distance.

#### مثال سخت — حلقه‌ی واقعی

علامت: traceroute به 10.5.0.1:

``` text
1 R1 2 R3 3 R4 4 R3 5 R4 6 R3 ... (TTL exceeded)
```

1. Hopها تکراری R3↔R4 ⇒ حلقه.
2. `show ip route 10.5.0.1` در R3: Next-hop R4؛ در R4: Next-hop R3.
3. علت: دو Redistribute بدون Tag پس از قطع مسیر اصلی؛ هر کدام دیگری را مسیر می‌بیند.
4. رفع فوری: `clear ip route 10.5.0.0` یا غیرفعال‌کردن یک Redistribute؛ سپس Tag.
5. آزمون منفی: بازگردانی لینک، قطع دوباره؛ بدون حلقه.
6. RCA: نبود Review و فقدان Tag در طراحی.

#### مثال سخت — طراحی جایگزین

به‌جای دوطرفه: هسته → EIGRP فقط Default (`ip route 0.0.0.0 0.0.0.0` + `redistribute static`)؛ EIGRP → OSPF فقط Summary (10.5.0.0/16). تعداد مسیرها کم، حلقه ناممکن. مزیت: سادگی و پایداری؛ عیب: مسیریابی بهینه‌ی کمتر (ترافیک از نقطه‌ی ثابت می‌رود).

### Lab هدایت‌شده (اجرا نشده)

1. توپولوژی دو ASBR (R3، R4) بین OSPF و EIGRP.
2. دوطرفه بدون Tag؛ قطع مسیر اصلی؛ مشاهده‌ی Feedback/حلقه با traceroute.
3. اعمال Tag و تکرار آزمون.
4. تغییر AD و بررسی اثر.
5. طراحی جایگزین با Default/Summary.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| حلقه | Feedback | Tag |
| مسیر زیرین | AD | `distance`/Filter |
| ناپایداری دوره‌ای | دو نقطه | یک‌طرفه |
| Tag دیده نمی‌شود | `set tag` نیست | Route-map |

### نکات امنیتی

- Redistribution خطای رایج در تغییر است؛ Review و آزمون در Lab اجباری.
- Tag و Prefix-list را مستند کنید.

### جمع‌بندی

Redistribute دوطرفه در دو نقطه Feedback و حلقه می‌سازد. Route Tag (set tag و match tag) مسیر را نشان‌گذاری می‌کند؛ Prefix-list و AD تنظیم‌کننده‌اند. ساده‌ترین راه: طراحی با یک‌طرفه + Default/Summary.

### تمرین و ارزیابی

**ت1.** (ساده) Route Feedback چیست؟ *(پاسخ: 10-2-ت1)*

**ت2.** (ساده) Tag چه کاری می‌کند؟ *(پاسخ: 10-2-ت2)*

**ت3.** (متوسط) چرا Route-map باید روی هر دو ASBR باشد؟ *(پاسخ: 10-2-ت3)*

**ت4.** (متوسط) AD External OSPF و EIGRP؟ *(پاسخ: 10-2-ت4)*

**ت5.** (سخت) پس از R-B حلقه شد؛ تحلیل. *(پاسخ: 10-2-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی Tag سازمان. *(پاسخ: 10-2-ت6)*

**Q1.** Quick quiz (English): Why is route tagging used in two-way redistribution? *(پاسخ: 10-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Tag | Route tag | برچسب مسیر |
| Feedback | Route feedback | بازگشت مسیر |

- *Tag routes at the boundary to stop loops.* ← مسیرها را در مرز Tag کنید تا حلقه نشود.

### کارت Lab

**کارت Lab:** دوطرفه با Tag. **Evidence:** `03-ops/redist2.md`.

### منابع

- Cisco IOS Route-map guide
- RFC 2328

<a id="l-10-3"></a>

## درس 10-3 — ECMP و توزیع بار: Equal-cost، Hashing و Load Balancing

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۱۰-۱ · ≈ 8 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ECMP را تعریف کنید و شرط تشکیل آن را بگویید.
2. توضیح دهید چرا توزیع به‌ازای Flow است نه بسته.
3. Hash و عوامل آن (IP، پورت) و اثر روی یکنواختی بار را بفهمید.
4. با `show ip cef exact-route` مسیر یک Flow را تعیین کنید.
5. خطر نامتقارن بودن ECMP با فایروال را تشخیص دهید.
6. `maximum-paths` و محدودیت‌ها را تنظیم کنید.

### چرا باید یاد بگیریم؟

دو لینک با هزینه‌ی برابر دارید. اگر فقط یکی استفاده شود، نصف ظرفیت هدر می‌رود. ECMP (Equal-Cost Multi-Path، یعنی «چندمسیره با هزینه‌ی برابر») هر دو مسیر را در جدول می‌گذارد و ترافیک را بین آنها تقسیم می‌کند. مثل دو باجه‌ی بانک که مشتریان به هر دو فرستاده می‌شوند. ولی «تقسیم» به‌ظاهر ساده، جزئیات خطرناکی دارد: یک Flow بزرگ فقط یک لینک را پر می‌کند و رفت و برگشت ممکن است از دو مسیر بروند.

### شرط تشکیل ECMP

- پروتکل مسیریابی چند مسیر با **Metric برابر** برای یک Prefix یاد گرفته (OSPF با Cost برابر، EIGRP با Metric برابر یا `variance`، Static با AD/Distance برابر، BGP با شرایط Multipath).
- تعداد مسیرها ≤ `maximum-paths` (OSPF پیش‌فرض 4 در بسیاری از IOS؛ قابل افزایش تا 16 یا بیشتر).

``` text
router ospf 1
 maximum-paths 8
```

جدول مسیر:

``` text
O  10.20.0.0/24 [110/20] via 10.1.1.2, Gi0/0
                [110/20] via 10.1.2.2, Gi0/1
```

### Flow و Hash

برای جلوگیری از بی‌ترتیبی بسته‌ها (که TCP را کند می‌کند)، روتر همه‌ی بسته‌های یک **Flow** را از یک مسیر می‌فرستد. Flow معمولاً با 5-tuple تعریف می‌شود:

``` text
5-tuple = source IP, destination IP, protocol, source port, destination port
```

روتر از فیلدها یک **Hash** می‌سازد و با `Hash mod تعداد مسیرها` مسیر را انتخاب می‌کند.

``` text
index = hash(5-tuple) mod N
N = 2 -> index in {0,1} ; N = 4 -> index in {0..3}
```

در CEF سیسکو، الگوریتم پیش‌فرض بر پایه‌ی IP مبدأ و مقصد (و در بعضی پلتفرم‌ها پورت) است. اگر فقط IP استفاده شود، دو میزبان که به هم صحبت می‌کنند همه‌ی Flowهایشان یک مسیر را می‌گیرد.

### نکته: یک Flow = یک لینک

``` text
Two 1 Gbps links in ECMP. One 900 Mbps backup transfer -> one link carries 900 Mbps; the other link idle.
```

ECMP ظرفیت **کل** را بالا می‌برد، نه ظرفیت **یک Flow** را. برای Flow بزرگ باید لینک سریع‌تر یا EtherChannel (که آن هم Hash دارد) یا Flow موازی (iperf -P).

### ابزارهای بررسی

``` text
show ip route 10.20.0.0
show ip cef 10.20.0.5
show ip cef exact-route 10.10.0.5 10.20.0.5
show ip cef 10.20.0.5 internal
show interfaces | include rate
```

`exact-route` نشان می‌دهد این جفت IP از کدام Next-hop می‌رود.

### ECMP و فایروال Stateful

اگر دو مسیر ECMP از **دو فایروال جدا** عبور کنند، رفت و برگشت ممکن است از دو فایروال متفاوت بروند و Stateful شکست بخورد (فصل ۲۳). راه‌ها: Hash متقارن (مرتب‌سازی IP/پورت در Hash)، SNAT، Session Sync، یا Active/Standby به‌جای ECMP.

### مثال‌های حل‌شده

#### مثال ساده — دو مسیر

`show ip route 10.20.0.0` دو Next-hop نشان می‌دهد؛ `maximum-paths` اگر 1 باشد فقط یکی. با `maximum-paths 4` هر دو.

#### مثال متوسط — اندازه‌گیری توزیع

۱۰۰۰ Flow با Hash یکنواخت و N=2: انتظار ≈۵۰۰ و ۵۰۰ (با انحراف تصادفی ±۳٪). با دو Flow: احتمال هر دو روی یک لینک:

``` text
P(both flows on the same path) = 1 / N = 1 / 2 = 50 %
P(10 flows all on the same path) = (1/2)^9 ~ 0.2 %
```

یعنی با Flow کم، توزیع نامتوازن شایع است.

#### مثال متوسط — iperf

``` text
iperf3 -c 10.20.0.10 -P 1   -> one flow: one link
iperf3 -c 10.20.0.10 -P 16  -> 16 flows: both links used
```

مقایسه‌ی `show interfaces ... | include rate` دو لینک.

#### مثال متوسط — exact-route

``` text
R1# show ip cef exact-route 10.10.0.5 10.20.0.5
10.10.0.5 -> 10.20.0.5 : GigabitEthernet0/0 (next hop 10.1.1.2)
R1# show ip cef exact-route 10.10.0.6 10.20.0.5
10.10.0.6 -> 10.20.0.5 : GigabitEthernet0/1 (next hop 10.1.2.2)
```

دو میزبان مختلف مسیرهای مختلف می‌گیرند.

#### مثال سخت — ECMP و دو فایروال

دو مسیر ECMP: Gi0/0 به FW-A و Gi0/1 به FW-B. رفت از Gi0/0 (FW-A)، پاسخ سرور بر اساس Hash روتر مقابل از FW-B. Sniffer: FW-A SYN؛ FW-B SYN-ACK ⇒ Drop. راه‌حل: SNAT روی FW-A (برگشت به IP FW-A و همان مسیر)، یا Hash متقارن در هر دو روتر (استفاده از min/max(IP) در Hash)، یا حذف ECMP. تأیید: ۱۰۰ بار curl بدون خطا.

#### مثال سخت — یک لینک خالی

`show interfaces`: لینک A ۹۰۰ Mbps، B ۵۰ Mbps. علل: ۱) Flow بزرگ ۲) Hash فقط IP و دو میزبان ۳) EtherChannel با Hash `src-mac`. رفع: Hash با پورت (`ip cef load-sharing algorithm include-ports source destination` طبق پلتفرم) و آزمون با Flow زیاد.

### Lab هدایت‌شده (اجرا نشده)

1. روتر با دو مسیر هم‌هزینه؛ تأیید ECMP در جدول.
2. iperf با ۱ و ۱۶ Stream؛ مقایسه‌ی شمارنده‌ها.
3. `exact-route` برای چند جفت IP.
4. افزودن فایروال Stateful روی یک مسیر و مشاهده‌ی Drop؛ رفع با SNAT.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| یک لینک خالی | Flow کم/Hash | Flow بیشتر/Hash پورت |
| قطع Session | نامتقارن با فایروال | SNAT/Hash متقارن |
| مسیر دوم نیست | Metric نابرابر/maximum-paths | تنظیم |
| تأخیر بی‌ثبات | مسیرهای با تأخیر متفاوت | بررسی |

### جمع‌بندی

ECMP بار را به‌ازای Flow تقسیم می‌کند؛ Hash از فیلدهای بسته می‌آید. ظرفیت یک Flow بیش از یک لینک نمی‌شود. ECMP با فایروال Stateful بدون SNAT/Hash متقارن خطرناک است. `exact-route` مسیر Flow را نشان می‌دهد.

### تمرین و ارزیابی

**ت1.** (ساده) شرط ECMP؟ *(پاسخ: 10-3-ت1)*

**ت2.** (ساده) Per-flow چیست؟ *(پاسخ: 10-3-ت2)*

**ت3.** (متوسط) چرا Per-packet برای TCP بد است؟ *(پاسخ: 10-3-ت3)*

**ت4.** (متوسط) maximum-paths پیش‌فرض OSPF؟ *(پاسخ: 10-3-ت4)*

**ت5.** (سخت) توزیع ۹۰/۱۰ را چطور حل کنید؟ *(پاسخ: 10-3-ت5)*

**ت6.** (سخت، طراحی) ECMP دو فایروال. *(پاسخ: 10-3-ت6)*

**Q1.** Quick quiz (English): Why is per-flow load balancing preferred over per-packet? *(پاسخ: 10-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ECMP | Equal-Cost Multi-Path | چندمسیری هم‌هزینه |
| CEF | Cisco Express Forwarding | ارسال سریع سیسکو |

- *Per-flow hashing keeps a flow on one path.* ← Hash روی جریان، جریان را روی یک مسیر نگه می‌دارد.

### کارت Lab

**کارت Lab:** ECMP. **Evidence:** `03-ops/ecmp.md`.

### منابع

- Cisco CEF guide

<a id="l-10-4"></a>

## درس 10-4 — Policy-Based Routing (PBR): مسیریابی بر اساس سیاست با Route-map، Track و Failover

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۸-۱، ۱۰-۱ · ≈ 10 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. PBR را تعریف کنید و فرق آن با Routing مبتنی بر مقصد را بگویید.
2. PBR را با ACL و Route-map در Cisco و با `config router policy` در FortiGate بسازید.
3. ترتیب ارزیابی PBR نسبت به جدول Routing را بدانید.
4. با Next-hop غیرقابل‌دسترس و Verify-availability کار کنید.
5. خطرهای نامتقارن بودن و CPU را تشخیص دهید.
6. PBR را با traceroute و شمارنده‌ها تأیید کنید.

### چرا باید یاد بگیریم؟

Routing معمولی مثل راننده‌ای است که فقط به «مقصد» نگاه می‌کند. گاهی می‌خواهید تصمیم بر اساس «چه کسی» یا «چه سرویسی» باشد: «ترافیک مهمان از ISP ارزان، ترافیک مدیران از ISP اصلی»، «VoIP از لینک A». **Policy-Based Routing (PBR)** این امکان را می‌دهد: قبل از جدول مسیر، بسته را با شرط‌ها می‌سنجید و Next-hop/Interface را مستقیماً تعیین می‌کند. PBR قدرتمند است ولی خطر هم دارد: دور زدن جدول مسیر، مسیر نامتقارن و فشار روی CPU.

### منطق PBR

``` text
packet arrives -> PBR rules (in order) -> if a rule matches: use its next-hop/interface
                                        -> if none matches: normal routing table
```

- شرط‌ها: منبع، مقصد، پروتکل، پورت (با ACL)، اندازه‌ی بسته، Interface ورودی.
- عمل: Next-hop، Interface خروجی، Default Next-hop (فقط اگر مسیر دقیق نباشد)، تنظیم DSCP.
- معمولاً روی **ورودی** Interface اعمال می‌شود و ترافیک برگشت را تغییر نمی‌دهد.
- طبق رفتار پیش‌فرض Cisco/FortiGate، اگر هیچ Rule مطابق نبود، Routing عادی انجام می‌شود (Drop نمی‌شود).

### پیکربندی Cisco

``` text
ip access-list extended GUEST-NETS
 permit ip 10.10.99.0 0.0.0.255 any
!
route-map PBR permit 10
 match ip address GUEST-NETS
 set ip next-hop 198.51.100.1
!
interface GigabitEthernet0/1
 ip policy route-map PBR
```

**Next-hop مرده و تأیید دسترسی:** اگر Next-hop خراب شود ولی Interface بالا بماند، PBR همچنان بسته را به آن می‌فرستد (چاه). با IP SLA و Track:

``` text
ip sla 10
 icmp-echo 198.51.100.1 source-interface GigabitEthernet0/2
 frequency 5
ip sla schedule 10 life forever start-time now
track 10 ip sla 10 reachability
route-map PBR permit 10
 match ip address GUEST-NETS
 set ip next-hop verify-availability 198.51.100.1 1 track 10
```

### پیکربندی FortiGate

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.99.0/24"
  set dst "0.0.0.0/0"
  set gateway 198.51.100.1
  set output-device "port3"
 next
end
```

بررسی: `diagnose firewall proute list`. در FortiOS PBR **قبل** از جدول Routing ارزیابی می‌شود؛ مسیریابی SD-WAN هم نوعی PBR پیشرفته است.

### Verification

``` text
show route-map PBR            (policy routing matches)
show ip policy
debug ip policy               (briefly)
traceroute 8.8.8.8 source 10.10.99.5
show access-lists GUEST-NETS  (hit counts)
```

در `show route-map` شمارنده‌ی «Policy routing matches: N packets» اثبات می‌کند Rule کار می‌کند.

### مثال‌های حل‌شده

#### مثال ساده — مهمان از ISP دوم

شبکه‌ی مهمان 10.10.99.0/24 از ISP2 خارج شود، بقیه از ISP1. Route-map بالا. تأیید: traceroute با Source مهمان از Hop ISP2؛ با Source کاربر عادی از ISP1.

#### مثال متوسط — بر اساس سرویس

VoIP (UDP 5060 و RTP 16384–32767) از لینک A:

``` text
ip access-list extended VOIP
 permit udp any any eq 5060
 permit udp any any range 16384 32767
route-map PBR permit 10
 match ip address VOIP
 set ip next-hop 203.0.113.1
```

بررسی: `show access-lists VOIP` شمارنده‌ی match.

#### مثال متوسط — خطای ترتیب

دو Sequence: 10 برای 10.10.0.0/16 به ISP-A و 20 برای 10.10.99.0/24 به ISP-B. چون 10 اول است و /16 مهمان را هم می‌گیرد، Sequence 20 هرگز اجرا نمی‌شود (Shadow). رفع: ترتیب خاص ⇒ عام.

#### مثال سخت — Next-hop مرده

ISP-A خراب (Interface بالا). مهمان‌ها بی‌اینترنت. بدون Track ترافیک به چاه. با `verify-availability` و Track، وقتی SLA شکست می‌خورد Rule دیگر اعمال نمی‌شود و ترافیک از جدول عادی (یا Rule بعدی) می‌رود. شاهد: `show track 10` Down و traceroute مسیر جایگزین.

#### مثال سخت — نامتقارن

PBR روی ورودی LAN، ترافیک مهمان را از ISP-B می‌فرستد؛ پاسخ سرور (با SNAT به IP ISP-B) از ISP-B برمی‌گردد (خوب). بدون SNAT، پاسخ به IP داخلی از مسیر پیش‌فرض (ISP-A) می‌آید و فایروال Stateful بین راه Drop می‌کند. رفع: SNAT متناسب با خروجی و Policy دوطرفه‌ی هماهنگ.

### Lab هدایت‌شده (اجرا نشده)

1. روتر با دو ISP (دو Interface)؛ دو شبکه‌ی داخلی.
2. PBR مهمان به ISP2؛ traceroute و شمارنده‌ها.
3. IP SLA/Track و قطع ISP2؛ مشاهده‌ی Failover.
4. خطای ترتیب Sequence و رفع.
5. در FortiGate: `config router policy` و `diagnose firewall proute list`.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| PBR اعمال نمی‌شود | ACL/ترتیب/Interface | `show route-map`، `show ip policy` |
| قطع کامل | Next-hop مرده | Track/SLA |
| فقط یک‌طرفه کار می‌کند | نامتقارن | SNAT/Policy دوطرفه |
| CPU بالا | PBR نرم‌افزاری | سخت‌افزار/محدودکردن |

### نکات امنیتی

- PBR می‌تواند ACLها و فایروال‌ها را دور بزند؛ آزمون و Review.
- مستندسازی Ruleها و مالک.

### جمع‌بندی

PBR قبل از جدول Routing با شرط‌های منبع/سرویس Next-hop را تعیین می‌کند. بدون تطابق، Routing عادی. Track و Verify-availability از Next-hop مرده جلوگیری می‌کنند؛ نامتقارن و ترتیب Rule خطاهای رایج‌اند.

### تمرین و ارزیابی

**ت1.** (ساده) PBR بر چه اساسی تصمیم می‌گیرد؟ *(پاسخ: 10-4-ت1)*

**ت2.** (ساده) PBR روی کدام Interface اعمال می‌شود؟ *(پاسخ: 10-4-ت2)*

**ت3.** (متوسط) تفاوت next-hop و default next-hop؟ *(پاسخ: 10-4-ت3)*

**ت4.** (متوسط) بسته‌ای که با هیچ Sequence از Route-map PBR مطابقت نکند چه می‌شود؟ *(پاسخ: 10-4-ت4)*

**ت5.** (سخت) Failover PBR را طراحی کنید. *(پاسخ: 10-4-ت5)*

**ت6.** (سخت، طراحی) PBR برای دو ISP با ریسک‌ها. *(پاسخ: 10-4-ت6)*

**Q1.** Quick quiz (English): What is the purpose of the track keyword with a PBR next hop? *(پاسخ: 10-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PBR | Policy-Based Routing | مسیریابی سیاست‌محور |
| SLA | IP SLA | پایش لینک |

- *PBR overrides destination-based routing.* ← PBR مسیریابی مبتنی بر مقصد را لغو می‌کند.

### کارت Lab

**کارت Lab:** PBR (اجرا نشده). **Evidence:** `03-ops/pbr.md`.

### منابع

- Cisco IOS IP Routing: Policy-Based Routing

<a id="l-10-5"></a>

## درس 10-5 — VRF-lite: چند جدول مسیریابی مستقل، Overlap آدرس و ارتباط با فایروال

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۱۰-۴ · ≈ 10 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. VRF و VRF-lite را تعریف و کاربرد آن را بگویید.
2. VRF با آدرس هم‌پوشان را بسازید و Interface را به آن اختصاص دهید.
3. پروتکل مسیریابی را در VRF پیکربندی کنید.
4. دستورهای ping/show را با `vrf` به‌کار ببرید.
5. فرق VRF و VDOM را بدانید.
6. خطاهای رایج (ترتیب دستور، Router ID) را رفع کنید.

### چرا باید یاد بگیریم؟

دو مشتری هر دو شبکه‌ی 10.1.1.0/24 دارند و به یک روتر وصل‌اند. در یک جدول مسیر نمی‌توان دو Route با یک Prefix برای دو مقصد داشت. **VRF (Virtual Routing and Forwarding)** یک «جدول مسیر مجازی» می‌دهد. مثل ساختمانی با دو طبقه‌ی کاملاً جدا که هر کدام واحد شماره‌ی 101 دارند و تداخل ندارند. کاربردها: ISPها (VPN مشتریان)، سازمان‌هایی که شبکه‌های کاملاً جدا می‌خواهند (مهمان، مدیریت، PCI)، و Labهای چندمستاجره.

### مفاهیم

- هر **VRF** جدول مسیر، جدول ARP و (اختیاری) نمونه‌ی پروتکل مسیریابی مستقل دارد.
- هر **Interface** فقط به **یک** VRF تعلق دارد (پیش‌فرض Global/Default).
- ترافیک بین VRFها به‌صورت پیش‌فرض عبور نمی‌کند (ایزولاسیون)؛ فقط با Route Leaking کنترل‌شده (درس 10-8) یا عبور از فایروال.
- **VRF-lite:** VRF بدون MPLS؛ هر لینک بین روترها باید برای هر VRF Interface/Subinterface جدا داشته باشد.

### پیکربندی (Cisco)

``` text
ip vrf CUST-A
 rd 65001:100
ip vrf CUST-B
 rd 65001:200
!
interface GigabitEthernet0/1
 ip vrf forwarding CUST-A
 ip address 10.1.1.1 255.255.255.0
interface GigabitEthernet0/2
 ip vrf forwarding CUST-B
 ip address 10.1.1.1 255.255.255.0
```

**نکته‌ی مهم ترتیب:** `ip vrf forwarding` باید **قبل از** `ip address` باشد؛ تغییر VRF آدرس IP را پاک می‌کند و باید دوباره وارد شود.

(در نسخه‌های جدید IOS XE: `vrf definition CUST-A` + `address-family ipv4` + `vrf forwarding CUST-A`.)

**پروتکل در VRF:**

``` text
router ospf 10 vrf CUST-A
 network 10.1.1.0 0.0.0.255 area 0
router ospf 20 vrf CUST-B
 network 10.1.1.0 0.0.0.255 area 0
!
ip route vrf CUST-A 0.0.0.0 0.0.0.0 10.1.1.254
```

### Verification

``` text
show ip vrf
show ip vrf interfaces
show ip route vrf CUST-A
show ip ospf 10 neighbor
ping vrf CUST-A 10.1.1.5
traceroute vrf CUST-A 10.1.1.5
show ip arp vrf CUST-A
```

بدون `vrf` همه‌ی دستورها روی جدول Global هستند و جواب «اشتباه» می‌دهند.

### VRF و VDOM

| معیار | VRF | VDOM (FortiGate) |
|---|---|---|
| جدول مسیر | جدا | جدا |
| Policy/NAT | مشترک | جدا |
| ادمین | مشترک | جدا |
| ایزولاسیون | Routing | کامل (Policy، Log، ادمین) |

VDOM سطح بالاتری از جداسازی است؛ VRF مفهوم مسیریابی است.

### مثال‌های حل‌شده

#### مثال ساده — آدرس هم‌پوشان

دو VRF هر دو 10.1.1.1/24 روی دو Interface. تأیید: `show ip route vrf CUST-A` و `CUST-B` هر دو `C 10.1.1.0/24` با Interface‌های مختلف. `ping vrf CUST-A 10.1.1.5` فقط به میزبان مشتری A می‌رسد.

#### مثال متوسط — OSPF در VRF

CUST-A با OSPF به روتر مشتری. `show ip ospf 10 neighbor` همسایه‌ی Full؛ `show ip route vrf CUST-A ospf` مسیرهای یادگرفته. اگر به‌جای `router ospf 10 vrf CUST-A` فرایند Global را بسازید، همسایه در VRF Global دیده می‌شود نه CUST-A.

#### مثال متوسط — خطای ترتیب

Interface قبلاً IP داشت؛ `ip vrf forwarding CUST-A` را زدید. پیام: `% Interface GigabitEthernet0/1 IPv4 disabled and address(es) removed due to enabling VRF CUST-A`. باید IP را دوباره بنویسید.

#### مثال سخت — «همسایه OSPF بالا نمی‌آید»

1. `show ip vrf interfaces` ⇒ Interface در VRF درست؟
2. فرایند OSPF با `vrf` درست؟
3. `ping vrf CUST-A <peer>` موفق؟
4. Router-ID: دو فرایند OSPF (A و B) در یک روتر؛ هر کدام Router-ID جدا (`router-id 1.1.1.1` و `1.1.1.2`).
5. ACL/فایروال بین دو سر.
6. پس از رفع Full.

#### مثال سخت — نشت ناخواسته

از CUST-A به 10.99.0.5 (سرویس مشترک در Global) ping می‌رود بدون اجازه. علت: Route Static `ip route vrf CUST-A 10.99.0.0 255.255.255.0 10.99.1.1 global` قدیمی. شاهد: `show ip route vrf CUST-A 10.99.0.5`. رفع: حذف Route و آزمون منفی.

### Lab هدایت‌شده (اجرا نشده)

1. روتر با دو VRF و دو مشتری هم‌آدرس.
2. OSPF جدا برای هر VRF.
3. آزمون ping بین VRFها (باید شکست بخورد).
4. خطای ترتیب `vrf forwarding` و رفع.
5. ثبت جدول مسیرها.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| ping جواب نمی‌دهد | بدون `vrf` | `ping vrf X` |
| آدرس پاک شد | ترتیب دستور | IP دوباره |
| همسایه بالا نمی‌آید | Process بدون vrf | `router ospf N vrf X` |
| Router-ID تکراری | دو Process | RID جدا |

### جمع‌بندی

VRF جدول مسیر مجازی است؛ هر Interface یک VRF. ترتیب `vrf forwarding` قبل از `ip address` مهم است. پروتکل و دستورهای ping/show باید `vrf` را بدانند. ایزولاسیون پیش‌فرض است و نشت باید کنترل‌شده باشد.

### تمرین و ارزیابی

**ت1.** (ساده) VRF چیست؟ *(پاسخ: 10-5-ت1)*

**ت2.** (ساده) چرا IP هنگام forwarding پاک می‌شود؟ *(پاسخ: 10-5-ت2)*

**ت3.** (متوسط) چگونه ping کنید؟ *(پاسخ: 10-5-ت3)*

**ت4.** (متوسط) RD چیست؟ *(پاسخ: 10-5-ت4)*

**ت5.** (سخت) سه مشتری با اینترنت مشترک. *(پاسخ: 10-5-ت5)*

**ت6.** (سخت، طراحی) جداسازی با فایروال. *(پاسخ: 10-5-ت6)*

**Q1.** Quick quiz (English): What does VRF-lite provide? *(پاسخ: 10-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VRF | Virtual Routing and Forwarding | مسیریابی مجازی |
| RD | Route Distinguisher | تمایزدهنده‌ی مسیر |

- *VRF separates routing tables.* ← VRF جدول‌های مسیریابی را جدا می‌کند.

### کارت Lab

**کارت Lab:** VRF (اجرا نشده). **Evidence:** `03-ops/vrf.md`.

### منابع

- Cisco VRF-lite configuration guide

<a id="l-10-6"></a>

## درس 10-6 — Asymmetric Routing: تحلیل رفت و برگشت، اثر بر فایروال و راه‌حل‌ها

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۳، ۱۱-۱، ۱۱-۳ · ≈ 10 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. مسیر نامتقارن را تعریف و علل رایج آن را بگویید.
2. اثر آن را روی فایروال Stateful توضیح دهید.
3. با Sniffer هم‌زمان و traceroute آن را اثبات کنید.
4. راه‌حل‌ها را به‌ترتیب اولویت اعمال کنید.
5. RPF را در این زمینه بفهمید.
6. شواهد و ریسک راه‌حل را مستند کنید.

### چرا باید یاد بگیریم؟

مسیر رفت و برگشت همیشه یکی نیست: دو ISP، ECMP، PBR، شبکه‌ی چندمسیره. برای **روتر** بی‌مسئله است چون هر بسته مستقل است. برای **فایروال Stateful** مشکل‌ساز است: Session را با SYN می‌سازد و پاسخ را با آن می‌خواند؛ اگر پاسخ از فایروال دیگری بیاید که SYN را ندیده، رد می‌کند. مثل نگهبانی که فقط ورود را ثبت کرده و کسی از در دیگر خارج می‌شود؛ او را نمی‌شناسد. نتیجه «گاهی کار می‌کند، گاهی نه» است و سخت‌ترین خرابی‌ها.

### علل رایج

1. **دو ISP بدون SNAT:** خروج از ISP-A ولی IP مبدأ داخلی؛ پاسخ از ISP دیگر.
2. **ECMP** با Hash متفاوت رفت و برگشت.
3. **PBR** که فقط مسیر رفت را تغییر می‌دهد.
4. **دو فایروال موازی** بدون Session Sync.
5. **سرور چندکارته** که پاسخ را از کارت دیگر می‌فرستد.
6. **Route نامتقارن بین سایت‌ها** (مثلاً دو Tunnel با Metric متفاوت).

### اثر روی فایروال Stateful

``` text
Client -> FW-A -> Server        (SYN: Session created on FW-A)
Server -> FW-B -> Client        (SYN-ACK arrives at FW-B: no session)
FW-B: "no session matched" -> Drop
```

علامت‌ها: اتصال شروع می‌شود و گیر می‌کند؛ بعضی اتصال‌ها کار و بعضی نه؛ در Log: `no session matched`، `Denied by forward policy check (policy 0)`. **RPF (Reverse Path Forwarding)** هم ممکن است Drop کند: بسته از Interface‌ای آمده که Route به مبدأ از آن نمی‌گذرد.

### اثبات

**۱) traceroute از دو سر** (در Lab):

``` text
Forward : PC -> R1 -> FW-A -> ISP-A -> Server
Return  : Server -> ISP-B -> FW-B -> R1 -> PC
```

**۲) Sniffer هم‌زمان روی هر دو فایروال:**

``` text
FW-A: diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l   -> SYN, ACK
FW-B: diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l   -> SYN-ACK only
```

**۳) Route رفت و برگشت:**

``` text
get router info routing-table details <dst>   (forward decision)
get router info routing-table details <src>   (return decision on the other side)
```

### راه‌حل‌ها به ترتیب اولویت

1. **طراحی متقارن:** رفت و برگشت از یک فایروال (ساده‌ترین و امن‌ترین).
2. **SNAT:** IP مبدأ را به IP همان فایروال/ISP ترجمه کنید تا برگشت از همان مسیر باشد.
3. **Policy Route/SD-WAN Rule هماهنگ** برای دو جهت.
4. **Session Sync** (HA Active-Active) تا هر دو فایروال Session را بدانند.
5. **سست‌کردن بازرسی** (`asymroute`): آخرین راه؛ امنیت و Evidence کم می‌شود.

### مثال‌های حل‌شده

#### مثال ساده — دو ISP بدون SNAT

کاربر 10.10.0.5 از ISP-A خارج می‌شود (Policy Route). سرور اینترنتی پاسخ را به 10.10.0.5 می‌فرستد؛ چون IP خصوصی است، اینترنت آن را به هیچ‌جا نمی‌برد و پاسخ اصلاً نمی‌رسد. با SNAT به IP ISP-A پاسخ همان مسیر را برمی‌گردد.

#### مثال متوسط — Sniffer

FW-A: SYN و ACK دیده، SYN-ACK نه. FW-B: SYN-ACK دیده، SYN نه ⇒ رفت از A و برگشت از B. اثبات با زمان‌ها و Sequence در دو سمت.

#### مثال متوسط — RPF

فایروال بسته‌ای با Src=10.10.0.5 از port3 دریافت می‌کند ولی Route به 10.10.0.0/24 از port2 است:

``` text
msg="reverse path check fail, drop"
```

رفع: Route درست یا `set src-check disable` (فقط با پذیرش ریسک Spoofing).

#### مثال سخت — ECMP و دو فایروال

دو لینک با ECMP به دو فایروال. اتصال‌ها بی‌نظم قطع می‌شوند. راه‌ها: Hash متقارن، SNAT، یا حذف ECMP و Active/Standby. آزمون: ۱۰۰ بار curl:

``` text
for i in $(seq 1 100); do curl -s -o /dev/null -w "%{http_code}\n" https://app.example.com; done | sort | uniq -c
```

انتظار ۱۰۰ × 200.

#### مثال سخت — ریسک راه‌حل

SNAT پنهان می‌کند IP واقعی کاربر در Log سرور؛ ردیابی با Log فایروال (NAT mapping) انجام شود. و `asymroute` حتی برای یک بازه‌ی کوتاه، حملات Spoofing را ممکن می‌کند؛ باید با CHG و پایش.

### Lab هدایت‌شده (اجرا نشده)

1. دو فایروال موازی و یک سرور.
2. مسیر برگشت را عمداً از فایروال دیگر بگذارید؛ مشاهده‌ی Drop.
3. Sniffer دو سمت.
4. رفع با SNAT؛ آزمون ۱۰۰ بار curl.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| SYN-ACK Drop | نامتقارن | SNAT/طراحی |
| گاهی کار می‌کند | ECMP | Hash/SNAT |
| فقط یک سرور | چندکارته | policy routing روی سرور |
| RPF fail | Route | تصحیح |

### جمع‌بندی

مسیر نامتقارن برای روتر بی‌اشکال و برای فایروال Stateful مرگبار است. با traceroute و Sniffer دو سمت اثبات کنید. راه‌حل: متقارن، SNAT، Policy Route، Session Sync و آخر `asymroute`.

### تمرین و ارزیابی

**ت1.** (ساده) Asymmetric یعنی؟ *(پاسخ: 10-6-ت1)*

**ت2.** (ساده) چرا Stateful Drop می‌کند؟ *(پاسخ: 10-6-ت2)*

**ت3.** (متوسط) سه علت؟ *(پاسخ: 10-6-ت3)*

**ت4.** (متوسط) چگونه ثابت کنیم؟ *(پاسخ: 10-6-ت4)*

**ت5.** (سخت) راه‌حل سازمان. *(پاسخ: 10-6-ت5)*

**ت6.** (سخت، طراحی) Active-Active. *(پاسخ: 10-6-ت6)*

**Q1.** Quick quiz (English): Why do stateful firewalls drop asymmetric flows? *(پاسخ: 10-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Asymmetric | Asymmetric routing | مسیر نامتقارن |

- *Asymmetric paths break stateful inspection.* ← مسیر نامتقارن بازرسی حالت‌دار را خراب می‌کند.

### کارت Lab

**کارت Lab:** Asymmetric (اجرا نشده). **Evidence:** `03-ops/asym.md`.

### منابع

- Fortinet FortiOS 7.0: Asymmetric routing

<a id="l-10-7"></a>

## درس 10-7 — طراحی مسیر چندفایروالی و آزمون جامع فصل ۱۰: پروژه‌ی حل‌شده‌ی کامل

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۱ تا ۱۰-۶ · ≈ 12 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. اثر ترکیبی Redistribution، ECMP، PBR، VRF و مسیر نامتقارن را در یک طراحی ببینید.
2. برای هر جریان مسیر رفت و برگشت را بنویسید و نقاط Stateful را علامت بزنید.
3. خطرهای ترکیبی را فهرست و اولویت‌بندی کنید.
4. راه‌حل را مرحله‌ای (یک تغییر در هر زمان) اعمال و آزمون کنید.
5. آزمون Failover را با عدد انجام دهید.
6. گزارش طراحی و Evidence بنویسید.

### چرا باید یاد بگیریم؟

مفاهیم فصل ۱۰ هیچ‌کدام تنها نیستند. در عمل Redistribute باعث ECMP می‌شود؛ ECMP با فایروال Stateful نامتقارن می‌شود؛ PBR مسیر رفت را عوض می‌کند و برگشت را نه؛ VRF ایزولاسیون می‌دهد ولی Leak ناخواسته می‌سازد. این درس مثل «آزمون رانندگی» است: همه‌ی مهارت‌ها در یک مسیر. هدف دیدن «اثر ترکیبی» و رعایت یک انضباط ساده است: **یک تغییر در هر زمان، آزمون پس از هر تغییر.**

### چارچوب حل

1. **توپولوژی** را بکشید: همه‌ی دستگاه‌ها، پروتکل‌ها، Zone/VRF و فایروال‌ها.
2. **جریان‌ها** را فهرست کنید: مبدأ، مقصد، سرویس.
3. برای هر جریان **مسیر رفت و برگشت** (Hop به Hop) و **NAT** را بنویسید.
4. **نقاط Stateful** (فایروال) و **نقاط تصمیم** (PBR، ECMP، Redistribution) را علامت بزنید.
5. **خطرها** را بنویسید: حلقه، نامتقارن، Shadow، Leak.
6. **راه‌حل** با کمترین پیچیدگی انتخاب کنید.
7. **آزمون** مثبت و منفی و Failover.
8. **Evidence** و گزارش.

### پروژه‌ی نمونه

سازمان با دو ISP، دو فایروال Edge (FW-A و FW-B) و دو منطقه‌ی داخلی (OSPF هسته، EIGRP شعب). نیازها:

- N1: کاربران از ISP-A خارج شوند؛ در قطع ISP-A به ISP-B.
- N2: مهمان فقط از ISP-B.
- N3: شبکه‌ی EIGRP شعب برای هسته قابل‌دسترس باشد.
- N4: Failover کمتر از ۱۰ ثانیه.
- N5: هیچ مسیر نامتقارنی که Session را قطع کند.

### طراحی پیشنهادی

``` text
Users  -> Core (OSPF) -> ECMP? no: Active/Standby default via FW-A, backup via FW-B (Floating)
Guests -> PBR (src 10.10.99.0/24) -> ISP-B next-hop (with SLA track)
Branches (EIGRP) <-> ASBR pair -> OSPF (one-way + summary 10.5.0.0/16, tag 100, default down)
FW-A/FW-B: SNAT to egress interface IP (so return path = forward path)
```

تصمیم‌ها و دلیل:

- ECMP کنار گذاشته شد چون دو فایروال Stateful جدا هستند؛ به‌جای آن Floating Static/SD-WAN.
- PBR برای مهمان + Track برای Next-hop.
- Redistribute یک‌طرفه + Summary + Tag.
- SNAT روی هر Edge برای تضمین برگشت.

### آزمون‌ها

| # | آزمون | انتظار | شاهد |
|---|---|---|---|
| T1 | کاربر → اینترنت | از ISP-A | traceroute، Session |
| T2 | قطع ISP-A | ISP-B ظرف <10 s | ping مداوم |
| T3 | مهمان → اینترنت | ISP-B | traceroute با Source مهمان |
| T4 | قطع ISP-B | مهمان بی‌اینترنت (طبق سیاست) یا ISP-A | Track |
| T5 | EIGRP→OSPF | Prefix خلاصه | `show ip route` |
| T6 | حلقه | وجود ندارد | traceroute بدون تکرار |
| T7 | نامتقارن | رفت/برگشت یکی | Sniffer دو سمت |

### محاسبه‌ی Failover

``` text
Failover = detection + convergence
detection (IP SLA 5 s x 3 failures = 15 s)  -> too slow for <10 s
use: interval 2 s, failures 3 -> 6 s  + convergence ~1 s = ~7 s  (meets target)
```

### مثال‌های حل‌شده

#### مثال ساده — طراحی پایه

جریان کاربر: Core → FW-A (Policy، SNAT به IP خروجی FW-A) → ISP-A. برگشت: ISP-A → FW-A (Session) → Core. هر دو جهت از FW-A؛ متقارن.

#### مثال متوسط — آزمون Failover

``` text
ping -i 0.2 8.8.8.8
(ISP-A cut) lost 28 packets x 0.2 s = 5.6 s outage
```

۵٫۶ ثانیه < ۱۰ ثانیه ⇒ N4 برآورده؛ ثبت.

#### مثال متوسط — PBR مهمان

traceroute با Source مهمان از Hop ISP-B؛ `show route-map` شمارنده‌ی match افزایش. با قطع ISP-B و Track، Rule غیرفعال و مهمان طبق سیاست (بدون اینترنت یا ISP-A) رفتار می‌کند.

#### مثال سخت — خرابی ترکیبی

Redistribute بی‌Tag حلقه ساخت و هم‌زمان ECMP ناخواسته نامتقارن. ترتیب رفع:

1. ابتدا حلقه: Tag/Filter؛ آزمون T6.
2. سپس نامتقارن: حذف ECMP/افزودن SNAT؛ آزمون T7.
3. پس از هر رفع، همه‌ی آزمون‌ها دوباره.
4. ثبت: «رفع ۱ ← اثر ← آزمون».

#### مثال سخت — دو مسیر بازگشت

با Summary 10.5.0.0/16 و یک مسیر Specific از دو ASBR، روتر Core مسیر Specific را (LPM) ترجیح می‌دهد و ترافیک از ASBR نادرست می‌رود. رفع: Summary فقط از ASBR مرجع؛ Specific فیلتر شود. آزمون: traceroute به چند Host.

### Lab هدایت‌شده (اجرا نشده)

1. توپولوژی بالا را بسازید.
2. جدول T1–T7 را اجرا و Evidence ثبت کنید.
3. دو خرابی تزریقی (حلقه + نامتقارن) را به‌ترتیب رفع کنید.
4. گزارش: طراحی، شواهد، ریسک‌ها.

### Rubric

``` text
Design 25 | Routing 25 | Failover 25 | Evidence 15 | Report 10
```

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| حلقه | Redistribute | Tag |
| Drop متناوب | نامتقارن | SNAT |
| Failover کند | Timer SLA | کاهش |
| Leak | Route نشتی | حذف/Filter |

### جمع‌بندی

طراحی چندفایروالی یعنی کنترل اثر ترکیبی مفاهیم. جریان‌ها، مسیر رفت و برگشت، نقاط Stateful، خطرها و آزمون‌های اندازه‌گیری‌شده را بنویسید و یک تغییر در هر زمان اعمال کنید.

### تمرین و ارزیابی

**ت1.** (ساده) چرا NAT فقط Edge؟ *(پاسخ: 10-7-ت1)*

**ت2.** (ساده) نقش Local-pref؟ *(پاسخ: 10-7-ت2)*

**ت3.** (متوسط) چرا Track در PBR؟ *(پاسخ: 10-7-ت3)*

**ت4.** (متوسط) Guest را چگونه جدا کردید؟ *(پاسخ: 10-7-ت4)*

**ت5.** (سخت) Asymmetric پس از لینک دوم؛ تحلیل. *(پاسخ: 10-7-ت5)*

**ت6.** (سخت، طراحی) طرح را برای سه ISP گسترش دهید. *(پاسخ: 10-7-ت6)*

**Q1.** Quick quiz (English): Which tool ensures PBR stops using a dead next hop? *(پاسخ: 10-7-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HA | High Availability | دسترس‌پذیری بالا |

- *Test negative cases as well as positive ones.* ← علاوه بر مثبت، حالت‌های منفی را هم آزمون کنید.

### کارت Lab

**کارت Lab:** پروژه‌ی فصل ۱۰ (اجرا نشده). **Evidence:** `03-ops/multi-fw.md`.

### منابع

- درس‌های ۱۰-۱ تا ۱۰-۶

## درس 10-8 — Route Leaking میان VRFها و جدول Global: طراحی کنترل‌شده

**فصل ۱۰ · درس افزوده (تکمیل ۱۰-۵) · پیش‌نیاز: درس‌های ۱۰-۱ تا ۱۰-۵ · ≈ ۶ ساعت**

> **وضعیت:** مفهومی با مثال VRF-lite؛ ویژگی‌های Leaking بسته به پلتفرم فرق دارد (IOS vs IOS-XE vs CSR)؛ Lab «اجرا نشده»؛ برخی دستورها `Unverified` روی vIOS.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Route Leaking را تعریف و کاربرد و ریسک آن را بگویید.
2. نشت ایستا بین VRF و Global را پیکربندی کنید.
3. با RD/RT و Import/Export آشنا شوید.
4. نشت را با Prefix-list/Route-map کنترل کنید.
5. آزمون منفی ایزولاسیون را اجرا کنید.
6. نشت ناخواسته را پیدا و رفع کنید.

### چرا باید یاد بگیریم؟

VRFها عمداً ایزوله‌اند. ولی گاهی یک **سرویس مشترک** (DNS، NTP، Syslog، مدیریت) باید برای همه‌ی VRFها در دسترس باشد. «Route Leaking» یعنی فقط چند Prefix مشخص بین VRFها منتقل شود، نه همه‌چیز. مثل راهروی مشترک بین دو واحد که فقط برای نگهبانی باز است. ریسک: اگر نشت بی‌قید باشد، ایزولاسیون شکسته و هم‌پوشانی آدرس مشکل‌ساز می‌شود. پس باید دقیق و کنترل‌شده باشد.

### روش‌ها

**۱) Static Route بین VRF و Global:**

``` text
! From VRF CUST-A to a shared service in the Global table
ip route vrf CUST-A 10.99.0.0 255.255.255.0 10.99.1.1 global
! From Global back to CUST-A
ip route 10.1.1.0 255.255.255.0 GigabitEthernet0/1 10.1.1.2
```

کلمه‌ی `global` یعنی Next-hop در جدول Global جست‌وجو می‌شود. مسیر برگشت هم لازم است؛ وگرنه ترافیک می‌رود و برنمی‌گردد.

**۲) Import/Export با Route Target (RT):** در VRF استاندارد (MPLS L3VPN یا VRF-lite با BGP): هر VRF با `route-target export X` مسیرهایش را برچسب می‌زند و VRF دیگر با `route-target import X` همان‌ها را می‌گیرد.

``` text
ip vrf SHARED
 rd 65001:1
 route-target export 65001:1
 route-target import 65001:100
ip vrf CUST-A
 rd 65001:100
 route-target export 65001:100
 route-target import 65001:1
```

CUST-A فقط مسیرهای SHARED را (RT 65001:1) و SHARED فقط CUST-A را می‌گیرد؛ CUST-B (اگر RT متفاوت) هیچ‌چیز نمی‌گیرد.

**۳) فایروال بین VRFها:** امن‌ترین روش: ترافیک بین VRFها از یک فایروال (با Policy و Log) عبور کند؛ نشت Routing نیست بلکه «ارتباط کنترل‌شده».

### کنترل نشت

``` text
ip prefix-list SHARED-ONLY seq 5 permit 10.99.0.0/24
route-map EXPORT-SHARED permit 10
 match ip address prefix-list SHARED-ONLY
ip vrf SHARED
 export map EXPORT-SHARED
```

فقط 10.99.0.0/24 صادر می‌شود، نه کل جدول.

### Verification

``` text
show ip route vrf CUST-A 10.99.0.5
ping vrf CUST-A 10.99.0.5
show ip vrf detail
show bgp vpnv4 unicast all    (if BGP-based)
```

### مثال‌های حل‌شده

#### مثال ساده — DNS مشترک

DNS 10.99.0.5 در Global. CUST-A و CUST-B هر دو باید آن را ببینند: دو Static `ip route vrf X 10.99.0.0/24 ... global` و Route برگشت. آزمون: `ping vrf CUST-A 10.99.0.5` موفق و `ping vrf CUST-A 10.1.1.5` در VRF CUST-B شکست (ایزولاسیون بین مشتریان حفظ).

#### مثال متوسط — RT محدود

SHARED RT 1، CUST-A 100، CUST-B 200. CUST-A و CUST-B فقط RT 1 را import می‌کنند. بنابراین هر دو SHARED را می‌بینند ولی همدیگر را نه.

#### مثال متوسط — آزمون منفی

از CUST-A: `ping vrf CUST-A 10.2.2.5` (شبکه‌ی CUST-B) باید شکست بخورد؛ `show ip route vrf CUST-A 10.2.2.5` ⇒ `Network not in table`. اگر موفق بود، نشتی هست.

#### مثال سخت — نشت ناخواسته

دو VRF هر دو Default Route را از Global می‌گیرند (`ip route vrf X 0.0.0.0 0.0.0.0 <GW> global`). ترافیک A→B از Global می‌گذرد و به B می‌رسد (Hairpin). شاهد: traceroute از A به B از Global. رفع: Default فقط برای اینترنت؛ ACL/فایروال در Global بین دو شبکه؛ Prefix-list.

#### مثال سخت — هم‌پوشانی

CUST-A و CUST-B هر دو 10.1.1.0/24 دارند و هر دو به SHARED نشت دارند؛ SHARED نمی‌تواند 10.1.1.5 را مبهم تشخیص دهد. راه: NAT ۱:۱ به آدرس‌های یکتا قبل از نشت، یا Renumber.

### Lab هدایت‌شده (اجرا نشده)

1. سه VRF: SHARED، CUST-A، CUST-B.
2. نشت ایستا و آزمون مثبت/منفی.
3. RT Import/Export (اگر BGP).
4. نشت ناخواسته عمدی و کشف با traceroute.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| ping شکست (نشت شده) | Route برگشت نیست | Route دو جهته |
| دو مشتری همدیگر را می‌بینند | RT مشترک/Default | RT/ACL |
| مسیر نمی‌آید | RT/export map | بررسی |
| هم‌پوشانی | آدرس یکسان | NAT/Renumber |

### نکات امنیتی

- ترجیحاً نشت را با فایروال و Log انجام دهید؛ Routing خالص ردپا ندارد.
- بازبینی دوره‌ای Routeهای `global`.

### جمع‌بندی

Route Leaking انتقال کنترل‌شده‌ی چند Prefix بین VRFها است. با Static، RT یا فایروال انجام می‌شود. مسیر برگشت، Prefix-list و آزمون منفی الزامی‌اند.

### تمرین و ارزیابی

**ت1.** (ساده) VRF چه چیزی را از هم جدا می‌کند؟ *(پاسخ: 10-8-ت1)*

**ت2.** (ساده) چرا Leak باید دوطرفه باشد؟ *(پاسخ: 10-8-ت2)*

**ت3.** (متوسط) چرا برای DNS مشترک /32 بهتر از /8 است؟ *(پاسخ: 10-8-ت3)*

**ت4.** (متوسط) آزمون منفی در Leak چیست و چرا لازم است؟ *(پاسخ: 10-8-ت4)*

**ت5.** (سخت) دو VRF با آدرس‌های 10.0.0.0/24 هم‌پوشان دارید. Leak ممکن است؟ راه‌حل را شرح دهید. *(پاسخ: 10-8-ت5)*

**ت6.** (سخت، طراحی) برای ۳ VRF (Corp، Guest، Servers) و یک DNS مشترک، جدول Leak و تست‌های مثبت/منفی را بنویسید. *(پاسخ: 10-8-ت6)*

**م1.** تفاوت Leak و عبور از فایروال را بگویید. *(پاسخ: 10-8-م1)*

**Q1.** Quick quiz (English): Why should route leaking be limited to host routes? *(پاسخ: 10-8-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VRF | Virtual Routing and Forwarding | جدول مسیریابی مجازی مستقل |
| RT | Route Target | برچسب Import/Export در VRF با MPLS |
| Leak | Route leaking | نشت عمدی مسیر بین جداول |
| Multi-tenant | Multi-tenancy | چندمستأجری |

- *Route leaking should be minimal, bidirectional and documented.* ← Leak باید حداقلی، دوطرفه و مستند باشد.
- *Always run a negative test to prove isolation.* ← همیشه آزمون منفی برای اثبات جداسازی انجام دهید.

### منابع

- Cisco: «Configuring VRF-lite» و «Route leaking / Inter-VRF routing» (IOS XE IP Routing Configuration Guides).
- RFC 4364 — BGP/MPLS IP VPNs (مفهوم VRF و Route Target).

## درس 10-9 — ECMP: Hashing، Load Balancing واقعی و خرابی‌های پنهان

**فصل ۱۰ · درس افزوده (تکمیل ۱۰-۳ و ۱۰-۶) · پیش‌نیاز: ۱۰-۳، ۱۰-۶، ۵-۰ · ≈ ۵ ساعت**

> **وضعیت:** مفهومی؛ رفتار Hash در Lab vIOS «اجرا نشده» و `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Hash ECMP و عوامل توزیع را در عمق توضیح دهید.
2. Polarization و راه رفع آن را بدانید.
3. اثر خرابی لینک (Rehash) را پیش‌بینی کنید.
4. توزیع بار را با iperf و شمارنده اندازه بگیرید.
5. مسئله‌ی احتمال با Flow کم را حساب کنید.
6. خرابی‌های پنهان ECMP را تشخیص دهید.

### چرا باید یاد بگیریم؟

ECMP ساده به نظر می‌رسد ولی خطاهای پنهان دارد: «چرا یک لینک پر است و دیگری خالی؟»، «چرا با قطع یک لینک، Session قطع شد؟»، «چرا دو لایه‌ی روتر همه‌ی ترافیک را روی یک شاخه می‌ریزند؟». این درس دلیل ریاضی و فنی این رفتارها را می‌گوید.

### Hash چگونه کار می‌کند؟

1. فیلدهای بسته (مثلاً IP مبدأ/مقصد، پروتکل، پورت‌ها) انتخاب می‌شود.
2. یک تابع Hash روی آنها اجرا می‌شود.
3. `index = hash mod N` شماره‌ی مسیر.

قاعده: Flow همیشه همان فیلدها را دارد ⇒ همان Hash ⇒ همان مسیر.

### سه خطای پنهان

**۱) Flow کم ⇒ توزیع نامتوازن.**

``` text
P(all k flows on the same one of N paths) = (1/N)^(k-1)
N = 2, k = 2  -> 1/2 = 50 %
N = 2, k = 10 -> (1/2)^9 ~ 0.2 %
```

با دو Flow در ۵۰٪ مواقع هر دو روی یک لینک می‌افتند. ECMP برای «تعداد زیاد Flow» خوب است.

**۲) Polarization.** وقتی چند لایه‌ی روتر (Spine/Leaf یا Core/Distribution) از الگوریتم و Seed یکسان استفاده کنند، تصمیم‌ها همبسته‌اند: لایه‌ی اول Flow را روی شاخه‌ی ۱ می‌گذارد و لایه‌ی دوم هم با همان Hash همان شاخه‌ی ۱ را انتخاب می‌کند ⇒ همه‌ی Flowها از یک مسیر. راه: Seed/Algorithm متفاوت در لایه‌ها (در IOS: `ip cef load-sharing algorithm universal <id>` یا `include-ports`)، یا شامل‌کردن فیلدهای مختلف.

**۳) Rehash با خرابی.** با افتادن یک لینک، N عوض می‌شود (مثلاً از 4 به 3) و `hash mod 3` Flowها را دوباره توزیع می‌کند؛ **همه‌ی Flowها** (نه فقط Flowهای لینک خراب) ممکن است مسیر عوض کنند. در حضور Stateful بین راه، Sessionها قطع می‌شود. راه: Resilient Hashing (در بعضی پلتفرم‌ها) که فقط Flowهای خراب را جابه‌جا می‌کند، یا Session Sync.

### اندازه‌گیری

``` text
iperf3 -c 10.20.0.10 -P 16 -t 20
show interfaces GigabitEthernet0/0 | include rate
show interfaces GigabitEthernet0/1 | include rate
show ip cef exact-route 10.10.0.5 10.20.0.5
```

شاخص: نسبت بار دو لینک. هدف نزدیک به ۱:۱؛ نسبت ۹:۱ یعنی Polarization یا Flow ناکافی.

### مثال‌های حل‌شده

#### مثال ساده — احتمال

``` text
2 flows, 2 paths: P(same path) = 1/2 = 50 %
100 flows, 2 paths: expected split ~ 50/50 (+/- 5)
```

#### مثال متوسط — iperf

با `-P 1` یک لینک ۹۰۰ Mbps و دیگری 0؛ با `-P 16` تقریباً ۴۵۰/۴۵۰. اگر باز یک‌طرفه بماند: Hash فقط IP و هر دو Host ثابت‌اند؛ `include-ports`.

#### مثال متوسط — اثر Rehash

4 لینک؛ Flowهای A، B، C، D روی لینک‌های 0..3. لینک 2 می‌افتد: `mod 3`. Flowهای 0، 1 و 3 هم ممکن است جابه‌جا شوند. اگر مسیر شامل NAT/فایروال Stateful باشد، این Sessionها قطع می‌شود. آزمون: ping/Session باز و قطع یک لینک؛ شمارش اتصال‌های قطع‌شده.

#### مثال سخت — Polarization

دو لایه Spine-Leaf با الگوریتم یکسان. هر Flow در لایه‌ی اول شاخه‌ی ۰ و لایه‌ی دوم هم شاخه‌ی ۰:

``` text
Layer1: link0 90 % , link1 10 %
Layer2 (below link0): link0 90 %, link1 10 %
```

نتیجه: یک مسیر ۸۱٪ کل بار. رفع: Seed متفاوت در لایه‌ی دوم؛ آزمون با ۱۰۰ Flow و مقایسه‌ی شمارنده‌ها.

#### مثال سخت — خرابی پنهان

لینک 1 از ۴ لینک خطای CRC دارد ولی `up/up`. ECMP همچنان ۲۵٪ ترافیک را به آن می‌دهد ⇒ کندی و Retransmission برای ۲۵٪ Flowها. تشخیص: `show interfaces counters errors`. رفع: حذف لینک خراب از ECMP یا رفع فیزیکی (درس 3-8). درس: ECMP خطای کیفیت لینک را نمی‌بیند؛ پایش خطا لازم است.

### Lab هدایت‌شده (اجرا نشده)

1. دو مسیر برابر؛ iperf با ۱ و ۱۶ Stream.
2. `exact-route` برای چند جفت IP.
3. قطع یک لینک از ۴ و بررسی Rehash.
4. تزریق خطای فیزیکی روی یک لینک و مشاهده‌ی اثر.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| یک لینک پر | Flow کم/Polarization | Flow بیشتر/Seed |
| قطع Session هنگام خرابی | Rehash | Resilient/Sync |
| کندی بخشی از Flowها | لینک خراب در ECMP | پایش خطا |
| تأخیر ناهمگن | مسیرهای نابرابر | بررسی |

### جمع‌بندی

ECMP با Hash توزیع می‌کند: Flow کم ⇒ نامتوازن؛ Polarization ⇒ همه روی یک مسیر؛ Rehash هنگام خرابی ⇒ جابه‌جایی همه‌ی Flowها. با iperf و شمارنده اندازه بگیرید و خطای لینک را پایش کنید.

### تمرین و ارزیابی

**ت1.** (ساده) شرط ECMP چیست؟ *(پاسخ: 10-9-ت1)*

**ت2.** (ساده) چرا بار بر پایه‌ی Flow است؟ *(پاسخ: 10-9-ت2)*

**ت3.** (متوسط) چرا دو لینک ۱ گیگ برای یک دانلود تک‌Flow ۲ گیگ نمی‌دهند؟ *(پاسخ: 10-9-ت3)*

**ت4.** (متوسط) Polarization یعنی چه؟ *(پاسخ: 10-9-ت4)*

**ت5.** (سخت) ECMP پشت دو فایروال Stateful ایجاد Drop می‌کند. سه راه‌حل را مقایسه کنید. *(پاسخ: 10-9-ت5)*

**ت6.** (سخت) نشان دهید چگونه می‌فهمید یک Flow مشخص از کدام لینک می‌رود. *(پاسخ: 10-9-ت6)*

**م1.** Per-packet load sharing چه ایراد دارد؟ *(پاسخ: 10-9-م1)*

**Q1.** Quick quiz (English): Why does ECMP hash per flow instead of per packet? *(پاسخ: 10-9-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ECMP | Equal-Cost Multi-Path | چند مسیر هم‌هزینه |
| Hash | Hash function | تابع تبدیل فیلدها به شماره‌ی مسیر |
| Flow | Network flow | رشته‌ی بسته‌های یک ارتباط |
| Elephant flow | Elephant flow | Flow بسیار بزرگ |
| Reordering | Packet reordering | به‌هم‌ریختن ترتیب بسته‌ها |

- *ECMP balances flows, not individual packets.* ← ECMP Flowها را متوازن می‌کند، نه بسته‌ها.
- *A single flow never exceeds the speed of one link.* ← یک Flow هرگز از سرعت یک لینک بیشتر نمی‌شود.

### منابع

- Cisco: «Cisco Express Forwarding — Load Balancing» (IP Switching Configuration Guide).
- RFC 2991 — Multipath Issues in Unicast and Multicast Next-Hop Selection.
- RFC 2992 — Analysis of an Equal-Cost Multi-Path Algorithm.

## پاسخ‌های فصل 10

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 10-1

**10-1-ت1** — ۲۰ و نوع E2 (برای BGP مقدار ۱).

هنگام Redistribution به OSPF، مسیرها به‌صورت External Type 2 (E2) با Metric ثابت ۲۰ وارد می‌شوند (برای BGP مقدار ۱). یعنی هر روتر OSPF هزینه‌ی خارجی ۲۰ را می‌بیند و هزینه‌ی داخلی تا ASBR را جمع نمی‌کند. با `metric` و `metric-type 1` می‌توان مقدار و نوع را تغییر داد.

**10-1-ت2** — Metric OSPF/BGP قابل تبدیل نیست؛ نبود Metric یعنی بی‌نهایت و مسیر منتقل نمی‌شود؛ باید دستی بدهید.

**10-1-ت3** — E2 فقط Metric خارجی؛ E1 هزینه‌ی داخلی تا ASBR را هم جمع می‌کند.

**10-1-ت4** — فقط مسیرهای classful منتقل می‌شوند؛ زیرشبکه‌ها نمی‌روند.

بدون کلمه‌ی `subnets` در `redistribute ... ospf`، فقط مسیرهای classful (مثلاً /8، /16، /24 کلاس‌دار) وارد OSPF می‌شوند و زیرشبکه‌ها (مثل 172.16.5.0/24) ناپدید می‌شوند؛ این شایع‌ترین علت «مسیر Redistribute نمی‌رسد» است. رفع: افزودن `subnets` و آزمون با `show ip route ospf`.

**10-1-ت5** — E1 برای انتخاب نزدیک‌ترین ASBR؛ آزمون با traceroute.

با چند ASBR، E2 همه‌ی روترهای OSPF را با Metric برابر می‌بیند و ممکن است ترافیک به ASBR دورتر برود. E1 هزینه‌ی داخلی تا ASBR را هم جمع می‌کند و نزدیک‌ترین ASBR را ترجیح می‌دهد. آزمون: traceroute از دو نقطه‌ی مختلف و مقایسه‌ی ASBR انتخاب‌شده.

**10-1-ت6** — فقط Prefixهای لازم با Prefix-list+Route-map، Seed صریح، E1 در صورت چند ASBR و آزمون منفی روی Prefix غیرمجاز.

**10-1-Q1** — The routes are not redistributed because the seed metric is infinite.


### پاسخ‌های بازنویسی عمیق درس 10-2

**10-2-ت1** — مسیری که به پروتکل دیگر رفته دوباره به مبدأ برگردد.

Route Feedback یعنی مسیری که از دامنه‌ی A به B تزریق شده، توسط ASBR دوم دوباره به A برگردانده شود. نتیجه: مسیر با AD بهتر ممکن است مسیر اصلی را بازنویسی کند و حلقه یا مسیر زیربهینه بسازد. این در Redistribution دوطرفه با دو ASBR رایج است.

**10-2-ت2** — مبدأ مسیر را علامت می‌زند تا بازگشت آن رد شود.

Tag برچسب عددی روی مسیر است که مبدأ را مشخص می‌کند. با Route-map، مسیری که Tag دارد در جهت بازگشت رد می‌شود؛ مثلاً مسیرهای EIGRP→OSPF با Tag 100 و در جهت OSPF→EIGRP با `match tag 100` deny می‌شوند تا برنگردند.

**10-2-ت3** — وگرنه ASBR بدون Route-map حلقه می‌سازد.

اگر Route-map فقط روی یک ASBR باشد، ASBR دیگر بدون فیلتر مسیرها را برمی‌گرداند و حلقه ساخته می‌شود. پس همه‌ی ASBRها باید Route-map یکسان داشته باشند و پس از تغییر آزمون شوند.

**10-2-ت4** — 110 و 170.

AD مسیر خارجی OSPF برابر ۱۱۰ و EIGRP External برابر ۱۷۰ است. اگر مسیر از OSPF به EIGRP رفته و برگردد، رقابت AD ممکن است مسیر اصلی را بازنویسی کند؛ Tag این را از ریشه قطع می‌کند.

**10-2-ت5** — Route-map فقط روی R-A؛ یکسان‌سازی و آزمون.

پس از افزودن R-B حلقه شد چون Route-map فقط روی R-A بود. مراحل: ۱) `show route-map` روی R-B. ۲) یکسان‌سازی Tag و Route-map. ۳) آزمون: traceroute و `show ip route` برای مسیر مشکوک؛ ۴) قطع یک لینک و تأیید نبود حلقه.

**10-2-ت6** — مبدأ، Tag، جهت، Route-map و مالک.

برگه‌ی Tag سازمان: برای هر دامنه شناسه‌ی Tag (OSPF=100، EIGRP=200، BGP=300)، جهت Redistribution، Route-map مربوط، مالک و تاریخ بازبینی. این برگه از اشتباه هنگام اضافه‌شدن ASBR جدید جلوگیری می‌کند.

**10-2-Q1** — To prevent routes from being re-redistributed back into their source domain, avoiding loops.


### پاسخ‌های بازنویسی عمیق درس 10-3

**10-3-ت1** — Metric و AD برابر.

شرط ECMP: چند مسیر با Metric و AD برابر به همان Prefix، و تعداد مسیرها ≤ `maximum-paths` (مقدار پیش‌فرض بسته به پلتفرم/نسخه فرق دارد). اگر Cost حتی یک واحد فرق کند ECMP نمی‌شود؛ برای تنظیم Cost یکسان `ip ospf cost` به‌کار می‌رود.

**10-3-ت2** — هر جریان همیشه از یک مسیر.

Per-flow یعنی هر جریان (مثلاً یک اتصال TCP) با Hash روی IP/پورت‌ها همیشه از یک مسیر می‌رود. مزیت: ترتیب بسته‌ها حفظ می‌شود و با دستگاه Stateful سازگار است؛ عیب: توزیع بار ممکن است ناهموار باشد.

**10-3-ت3** — بسته‌ها نامرتب می‌رسند.

Per-packet بسته‌ها را بین مسیرها می‌چرخاند و چون تأخیر مسیرها متفاوت است، بسته‌ها نامرتب می‌رسند؛ TCP آن را Loss فرض می‌کند و سرعت را پایین می‌آورد و فایروال Stateful ممکن است Session را بشکند. پس برای TCP بد است.

**10-3-ت4** — بسته به پلتفرم/نسخه؛ در بسیاری از Imageها ۴.

مقدار پیش‌فرض `maximum-paths` در OSPF به پلتفرم و نسخه‌ی IOS بستگی دارد (در مستند Cisco عدد ثابتی داده نشده؛ در بسیاری از Imageها ۴ است و حداکثر مجاز بسته به پلتفرم می‌تواند ۸ یا ۱۶ باشد). با `show ip protocols` خط «Maximum path» را ببینید. اگر تعداد مسیرهای برابر از این حد بیشتر باشد فقط به همان تعداد در RIB می‌آید.

**10-3-ت5** — الگوریتم Hash با پورت؛ آزمون با چند جریان.

توزیع ۹۰/۱۰ معمولاً نشانه‌ی Hash ناهموار (چند جریان بزرگ با Src/Dst ثابت) است. راه: الگوریتم Hash که پورت را هم لحاظ کند (`ip cef load-sharing algorithm include-ports source destination`؛ پیش‌فرض الگوریتم universal است)، و آزمون با iperf چند جریان.

**10-3-ت6** — Symmetric hash/Active-Standby.

ECMP بین دو فایروال Stateful فقط با Symmetric Hash (هر دو جهت جریان از یک فایروال) یا طراحی Active-Standby/Session sync ایمن است. در غیر این صورت Asymmetric رخ می‌دهد (درس ۱۰-۶).

**10-3-Q1** — It preserves packet order within a flow and works with stateful devices.


### پاسخ‌های بازنویسی عمیق درس 10-4


### پاسخ‌های بازنویسی عمیق درس 10-4

**10-4-ت1** — بر اساس ACL (مبدأ، پروتکل، پورت) و نه فقط مقصد.

PBR با ACL تصمیم می‌گیرد: مبدأ، مقصد، پروتکل و پورت. به‌خلاف مسیریابی عادی که فقط مقصد را می‌بیند. مثال: ترافیک 10.10.20.0/24 از ISP-A و بقیه از ISP-B.

**10-4-ت2** — Interface ورودی ترافیک.

PBR روی Interface ورودی ترافیک (`ip policy route-map`) اعمال می‌شود؛ نه روی خروجی. برای ترافیک خود روتر از `ip local policy` استفاده می‌شود.

**10-4-ت3** — default فقط وقتی مسیر مشخص در RIB نباشد استفاده می‌شود.

`set ip next-hop` حتی اگر مسیر مشخص در RIB باشد، Next-hop تعیین‌شده را ترجیح می‌دهد؛ `set ip default next-hop` فقط وقتی استفاده می‌شود که RIB مسیر مشخصی (غیر از Default) نداشته باشد.

**10-4-ت4** — با جدول مسیریابی عادی ارسال می‌شود (Drop نمی‌شود).

طبق مستند Cisco، بسته‌ای که با هیچ Sequence از Route-map مطابقت نکند یا با `deny` مطابق شود، از PBR خارج شده و با جدول مسیریابی عادی ارسال می‌شود (برخلاف تصور رایج «deny ضمنی = Drop»). پس Sequence پایانی خالی لازم نیست؛ خطر واقعی Sequence بدون `match` با `set` است که همه‌ی بسته‌ها را به همان Next-hop می‌برد.

**10-4-ت5** — IP SLA+Track، verify-availability، Next-hop دوم، آزمون قطع لینک.

Failover PBR: `ip sla` با icmp-echo روی Next-hop، `track 1 ip sla 1 reachability`، و `set ip next-hop verify-availability X 10 track 1` به‌همراه Next-hop دوم. آزمون: قطع لینک ISP-A و دیدن اینکه ترافیک Finance به Next-hop دوم می‌رود (شمارنده‌ها و traceroute).

**10-4-ت6** — ACL، Track، Failover، مستند و آزمون منفی؛ ریسک: Next-hop مرده.

PBR دو ISP: ACL برای Finance، Route-map با Track و Next-hop دوم، Failover آزمون‌شده، مستند و آزمون منفی (ترافیک غیر Finance از مسیر عادی). ریسک اصلی: Next-hop مرده؛ جبران با Track.

**10-4-Q1** — To stop using the next hop when it becomes unreachable.

### پاسخ‌های بازنویسی عمیق درس 10-5


### پاسخ‌های بازنویسی عمیق درس 10-5

**10-5-ت1** — جدول مسیریابی مجازی مستقل روی همان روتر.

VRF یک جدول مسیریابی مجازی مستقل روی همان روتر است: Interfaceها، Routeها و پروتکل‌ها در هر VRF جدا هستند؛ پس آدرس‌های تکراری (مثلاً دو مشتری با 192.168.1.0/24) مشکلی ندارند.

**10-5-ت2** — چون Interface به جدول دیگری منتقل می‌شود و IP قبلی در جدول Global ثبت بوده.

**10-5-ت3** — ping vrf NAME.

ping بدون vrf در جدول Global اجرا می‌شود؛ برای تست داخل VRF `ping vrf CUST-A 192.168.1.2` و `traceroute vrf ...` لازم است. فراموشی این دستور شایع‌ترین «ping کار نمی‌کند» در VRF است.

**10-5-ت4** — شناسه‌ی یکتا برای Prefix در VRF.

RD (Route Distinguisher) مقدار یکتا (مثلاً 65000:1) است که Prefix را در VRF متمایز می‌کند تا در MPLS/BGP آدرس‌های تکراری با هم قاطی نشوند. در VRF-lite لازم نیست ولی استاندارد پیکربندی است.

**10-5-ت5** — VRF جدا، فایروال Zone، NAT جدا، آزمون منفی.

سه مشتری با اینترنت مشترک: سه VRF، Default هر VRF به Interface/Zone جدا در فایروال، NAT جدا برای هر مشتری، و آزمون منفی (مشتری A به B نرسد). ریسک: Leak ناخواسته از Static یا Redistribute.

**10-5-ت6** — VRF+Zone+Policy+Log.

جداسازی با فایروال: VRF مسیرها را جدا می‌کند و Zone/Policy فایروال تعیین می‌کند چه چیزی بین Zoneها عبور کند. فقط VRF امنیت کامل نیست؛ Policy و Log لازم است.

**10-5-Q1** — Multiple isolated routing tables on one router without MPLS.

### پاسخ‌های بازنویسی عمیق درس 10-6


### پاسخ‌های بازنویسی عمیق درس 10-6

**10-6-ت1** — رفت و برگشت از مسیر یا فایروال متفاوت.

Asymmetric یعنی بسته‌ی رفت و برگشت یک جریان از مسیر یا فایروال متفاوت عبور کنند. در Stateless مشکلی نیست؛ در Stateful باعث Drop می‌شود.

**10-6-ت2** — Session اولیه را ندیده.

فایروال Stateful فقط وقتی بسته‌ی برگشت را می‌پذیرد که Session اولیه (SYN) را دیده باشد؛ در Asymmetric فایروال دوم SYN را ندیده و `no session matched` می‌دهد و Drop می‌کند.

**10-6-ت3** — ECMP، دو ISP، Redistribution.

سه علت رایج: ECMP/Per-packet بین فایروال‌ها، دو ISP با Policy ورودی/خروجی متفاوت (Local-pref و Prepend)، و Redistribution/Route-map ناهمگون. موارد دیگر: HA نادرست و NAT متفاوت.

**10-6-ت4** — Capture دو سویه.

با Capture هم‌زمان روی هر دو فایروال: FW1 فقط SYN و FW2 فقط SYN-ACK را می‌بیند؛ و traceroute از دو سر مسیر متفاوت نشان می‌دهد. این دو شاهد با هم Asymmetric را ثابت می‌کنند.

**10-6-ت5** — Symmetric یا Session sync.

راه سازمان: طراحی Symmetric (Local-pref/Weight/PBR تا هر دو جهت از یک فایروال) یا Cluster با Session sync. `asymroute` فقط موقت و ضعیف‌کننده‌ی امنیت است.

**10-6-ت6** — Sync+Hash+آزمون.

Active-Active با Session sync: فعال‌سازی session-pickup، آزمون قطع FW1 و ماندگاری Sessionها، و اندازه‌گیری Delay Sync. جایگزین ساده‌تر: Active-Standby. معیار: صفر قطع Session در Failover آزمایشی.

**10-6-Q1** — They never saw the initial packet, so no session exists.


### پاسخ‌های بازنویسی عمیق درس 10-7


### پاسخ‌های بازنویسی عمیق درس 10-7

**10-7-ت1** — رد‌یابی ساده و جلوگیری از NAT دوباره.

NAT فقط روی Edge: Log و رد‌یابی ساده می‌شود، IP واقعی کاربر در Internal دیده می‌شود و NAT دوباره (Double NAT) مشکلات VPN/Port-forward نمی‌سازد.

**10-7-ت2** — تعیین ISP خروجی در کل AS.

Local-pref (مقدار بزرگ‌تر بهتر) در کل AS از طریق iBGP پخش می‌شود و ISP خروجی را برای همه‌ی روترها تعیین می‌کند؛ ابزار اصلی کنترل خروج.

**10-7-ت3** — بدون آن ترافیک به Next-hop مرده می‌رود.

بدون Track، PBR به Next-hop مرده ادامه می‌دهد و ترافیک بی‌صدا Drop می‌شود. Track/IP SLA Next-hop مرده را از Policy خارج می‌کند و Failover را ممکن می‌سازد.

**10-7-ت4** — VRF جدا، Default مستقل، Policy فایروال، آزمون منفی.

Guest در VRF جدا قرار می‌گیرد با Default مستقل به Interface فایروال؛ Policy فایروال فقط اینترنت را مجاز می‌کند و آزمون منفی (Guest→Servers) رد می‌شود و Log دارد.

**10-7-ت5** — Capture، Local-pref/Prepend، آزمون.

Asymmetric پس از لینک دوم: Capture روی هر دو فایروال، اصلاح Local-pref/Prepend یا PBR تا هر دو جهت از یک فایروال برود، و آزمون تکرار (Capture Symmetric).

**10-7-ت6** — Local-pref، Prepend، PBR، Track، VRF.

طرح سه‌ISP: Local-pref برای ترتیب خروج، Prepend برای ورود، PBR با Track برای ترافیک حساس، VRF برای مهمان و آزمون Failover هر ISP؛ مستندسازی ریسک و Rollback.

**10-7-Q1** — IP SLA with a track object.

IP SLA به‌همراه Track Object می‌تواند Next-hop مرده را از PBR کنار بگذارد.

### پاسخ‌های درس‌های افزوده‌ی فصل 10 (۱۰-۸ و ۱۰-۹)

**10-8-ت1** — جدول‌های مسیریابی (و در نتیجه Reachability لایه ۳) را؛ آدرس‌ها می‌توانند هم‌پوشان باشند.

**10-8-ت2** — چون بسته‌ی پاسخ برای برگشت به مبدأ نیاز به Route دارد؛ Leak یک‌طرفه باعث Drop یا Asymmetric می‌شود.

**10-8-ت3** — /32 فقط همان سرور را باز می‌کند؛ /8 صدها هزار آدرس و سرویس دیگر را هم قابل‌دسترس می‌کند و سطح حمله را بزرگ می‌کند.

**10-8-ت4** — آزمونی که باید شکست بخورد (مثلاً ping از Guest به Corp). اثبات می‌کند جداسازی هنوز برقرار است و Leak فراتر از هدف نیست.

**10-8-ت5** — Leak مستقیم ممکن نیست چون Prefix تکراری است (مسیر مبهم). راه‌حل: NAT (ترجمه‌ی یک طرف)، تغییر Addressing، یا عبور از فایروال/Proxy که NAT و Policy را بر عهده بگیرد.

**10-8-ت6** — Leak فقط DNS (/32) از SHARED به هر سه VRF و Subnet هر VRF برای برگشت در SHARED. تست مثبت: هر VRF به DNS برسد. تست منفی: Guest به Corp و Servers نرسد؛ Corp به Guest نرسد؛ Guest به Servers نرسد.

**10-8-م1** — Leak مسیر را مستقیم باز می‌کند و بازرسی/Log ندارد؛ عبور از فایروال ترافیک را Inspect و Log می‌کند.

**10-8-Q1** — Because a host route opens only the single required service, minimizing exposure and the risk of unintended reachability.

**10-9-ت1** — چند مسیر به یک Prefix با AD و Metric برابر (و پشتیبانی/تنظیم `maximum-paths`).

**10-9-ت2** — برای جلوگیری از Reordering بسته‌ها در یک ارتباط TCP؛ با Hash همه‌ی بسته‌های یک Flow یک مسیر را می‌گیرند.

**10-9-ت3** — چون یک Flow فقط یک لینک را می‌گیرد؛ حداکثر سرعت آن سرعت یک لینک است.

**10-9-ت4** — وقتی Hash یا الگوریتم یکسان در چند Hop پشت‌سرهم یا تنوع کم فیلدها باعث می‌شود ترافیک روی یک مسیر جمع شود.

**10-9-ت5** — (۱) Hash متقارن تا رفت و برگشت از یک فایروال بگذرد: ساده ولی به تجهیزات وابسته است. (۲) Active-Passive یا Session Sync بین فایروال‌ها: مؤثر ولی پیچیده‌تر و گاه Needs-License. (۳) Policy Routing/SNAT برای برگشت از همان فایروال: عملی ولی عیب‌یابی را سخت می‌کند.

**10-9-ت6** — با `show ip cef exact-route <src> <dst>` (در پلتفرم‌هایی که پشتیبانی می‌کنند) یا با مقایسه‌ی شمارنده‌ی ترافیک Interfaceها و Capture روی هر لینک هنگام ایجاد همان Flow.

**10-9-م1** — بسته‌های یک Flow روی مسیرهای مختلف می‌روند و Reordering ایجاد می‌شود؛ TCP کند می‌شود.

**10-9-Q1** — To avoid packet reordering within a connection, which would degrade TCP performance.


# فصل 11 — مبانی فایروال

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۷ (ACL/NAT)، فصل ۸، فصل ۱۰ (مسیر نامتقارن).
**اهداف:** Stateless/Stateful؛ Session؛ Zone و Trust Boundary؛ Default Deny و Least Privilege؛ مسیر بسته در فایروال؛ ترافیک عبوری در برابر ترافیک خود فایروال؛ تفاوت Routing، Policy، ACL، NAT؛ Segmentation؛ **Gate G4**.
**چرا اینجا؟** قبل از FortiGate باید «چرا» را بدانید تا هر منو و دستور برایتان معنی داشته باشد.
**معیار تسلط:** پاسخ به ۱۰ پرسش مسیر بسته برای یک ارتباط؛ نوشتن Policy Matrix با Least Privilege؛ توضیح تفاوت ACL/Policy/NAT با مثال.
**اشتباهات رایج:** گمان اینکه NAT امنیت است؛ ترتیب Policy؛ فراموشی Default Deny؛ نادیده‌گرفتن ترافیک خود فایروال.

**درس‌های فصل:**
- [درس 11-1 — فایروال چیست؟ Stateless در برابر Stateful](#l-11-1)
- [درس 11-2 — Zone، Trust Boundary، Default Deny و Least Privilege](#l-11-2)
- [درس 11-3 — مسیر بسته در فایروال و ترافیک عبوری در برابر ترافیک خود فایروال](#l-11-3)
- [درس 11-4 — ACL، Policy و NAT: تفاوت‌ها و ارتباط‌ها](#l-11-4)
- [درس 11-5 — Session، Timeout، MTU/MSS و ریشه‌ی خرابی‌های TCP/UDP](#l-11-5)
- [درس 11-6 — کارگاه طراحی Policy و ۱۰ پرسش مسیر بسته + Gate G4](#l-11-6)

---

<a id="l-11-1"></a>

## درس 11-0 — مدل تهدید، مرز اعتماد و Defense in Depth: قبل از نوشتن اولین Policy

**فصل ۱۱ · درس افزوده (پیش‌درس ۱۱-۱) · پیش‌نیاز: فصل ۲، ۴، ۱۰ · ≈ ۶ ساعت**

> **وضعیت:** مفهومی؛ مستقل از برند؛ مبنای تصمیم‌های فصل‌های ۱۲ تا ۳۲.

### ۱) هدف آموزشی

در پایان می‌توانید:

1. **دارایی (Asset)، تهدید (Threat)، آسیب‌پذیری (Vulnerability)، ریسک (Risk)** و کنترل (Control) را تعریف و تفکیک کنید.
2. یک **مدل تهدید ساده** برای یک شبکه‌ی سازمانی بسازید (چه چیزی را از چه کسی و از چه راهی محافظت می‌کنیم).
3. **مرز اعتماد (Trust Boundary)** را روی نقشه مشخص و برای هر مرز یک کنترل تعیین کنید.
4. **Defense in Depth** را با مثال لایه‌به‌لایه توضیح دهید و بگویید چرا یک فایروال به‌تنهایی کافی نیست.
5. **Least Privilege** را به Policy واقعی تبدیل کنید و تفاوت **Default Deny** و **Default Allow** را بگویید.
6. مسیر **North-South** و **East-West** را تفکیک و کنترل‌های هرکدام را انتخاب کنید.

### ۲) پیش‌نیازها

VLAN و Subnet (فصل ۳ و ۲)، Routing (فصل ۵)، مفهوم NAT و DMZ در حد آشنایی.

### ۳) مفهوم پایه: چرا قبل از Policy باید «فکر کرد»؟

بسیاری از شبکه‌ها فایروال دارند ولی ناامن‌اند، چون Policyها بر پایه‌ی «کار بیفتد» نوشته شده‌اند، نه بر پایه‌ی تحلیل ریسک. نتیجه: `any → any → ALL → accept` که فایروال را به یک روتر گران‌قیمت تبدیل می‌کند.

مهندس امنیت به‌جای سؤال «چطور این پورت را باز کنم؟» می‌پرسد:

1. چه چیزی ارزشمند است؟ (Asset: دیتابیس مشتری، AD، سرور مالی)
2. چه کسی/چه چیزی می‌تواند به آن آسیب بزند؟ (Threat: مهاجم خارجی، کارمند ناراضی، بدافزار)
3. از چه راهی؟ (Attack Path: VPN، ایمیل، سرور وب، حرکت جانبی)
4. کدام کنترل جلوی هر مسیر را می‌گیرد؟ و اگر آن کنترل شکست خورد، کنترل بعدی چیست؟

> **تشبیه:** امنیت یک بانک فقط «در ورودی» نیست: در ورودی، نگهبان، دوربین، درب شیشه‌ای، صندوق‌های جدا، خزانه، و دستور بازرسی. اگر یکی بشکند، بقیه می‌مانند. این Defense in Depth است.

### ۴) توضیح عمیق فنی

#### ۴-۱) واژگان ریسک

| واژه | تعریف | مثال |
|---|---|---|
| Asset | چیزی که ارزش دارد | پایگاه‌داده‌ی مشتریان |
| Threat | عامل بالقوه‌ی آسیب | باج‌افزار، مهاجم خارجی |
| Vulnerability | ضعفی که تهدید از آن استفاده می‌کند | سرور بدون Patch، رمز پیش‌فرض |
| Risk | احتمال × اثر | احتمال بالا × اثر زیاد = ریسک بالا |
| Control | اقدام کاهش ریسک | فایروال، Patch، MFA، Segmentation |

``` text
Risk ~= Likelihood x Impact
```

ریسک صفر وجود ندارد؛ هدف کاهش به سطح قابل‌قبول و مدیریت باقی‌مانده است.

#### ۴-۲) مدل تهدید ساده (چهار سؤال)

یک چارچوب عملی (الهام‌گرفته از STRIDE و مدل‌های ساده): برای هر سیستم بپرسید:

1. **چه چیزی می‌سازیم/محافظت می‌کنیم؟** (نقشه + جریان داده)
2. **چه چیزی می‌تواند خراب شود؟** (Spoofing، Tampering، Information Disclosure، DoS، Elevation)
3. **چه کاری برایش می‌کنیم؟** (کنترل)
4. **آیا کافی است؟** (آزمون/Verification)

STRIDE = Spoofing (جعل هویت)، Tampering (دستکاری)، Repudiation (انکار)، Information disclosure (افشا)، Denial of service (انکار سرویس)، Elevation of privilege (ارتقای دسترسی).

#### ۴-۳) Trust Boundary و Zone

**مرز اعتماد** جایی است که سطح اعتماد تغییر می‌کند: Internet ↔ DMZ، DMZ ↔ LAN، Guest ↔ Corporate، Server ↔ Management. **هر عبور از مرز باید کنترل شود** (Policy + Log). شبکه را به **Zoneها** تقسیم می‌کنیم؛ هر Zone سطح اعتماد مشابه دارد:

| Zone | سطح اعتماد | نمونه |
|---|---|---|
| Internet (Untrust) | صفر | همه‌ی اینترنت |
| DMZ | پایین/متوسط | وب‌سرور عمومی |
| Users | متوسط | PC کارمندان |
| Servers | بالا | اپلیکیشن/DB |
| Management | بسیار بالا | سرورهای مدیریت، OOB |
| Guest | صفر/بسیار پایین | مهمان |

قانون عبور: از اعتماد کمتر به بیشتر **سخت‌تر**؛ از بالاتر به پایین‌تر معمولاً مجاز با Inspection.

#### ۴-۴) Defense in Depth

لایه‌های کنترل (از بیرون به داخل):

``` text
1 Perimeter     : edge firewall, DoS protection, IPS
2 Network       : segmentation (VLAN/Zone), ACL, internal firewall
3 Host          : EDR/antivirus, host firewall, patching
4 Application   : WAF, secure coding, authentication
5 Data          : encryption, backup, DLP
6 Identity      : MFA, least privilege, privileged access management
7 Monitoring    : logs, SIEM, alerting, incident response
```

ایده: **هیچ لایه‌ای را کامل فرض نکن.** اگر مهاجم لایه‌ی ۱ را رد کند، لایه‌ی ۲ حرکت جانبی را محدود می‌کند.

#### ۴-۵) Least Privilege و Default Deny

- **Least Privilege:** هر کاربر/سیستم فقط حداقل دسترسی لازم.
- **Default Deny:** هر چه صریحاً مجاز نشده، رد است؛ برخلاف Default Allow که همه‌چیز مجاز است مگر ممنوع.
- در Policy: Source دقیق (نه all)، Destination دقیق، Service دقیق (نه ALL)، زمان‌بندی در صورت نیاز، Log فعال.

``` text
BAD : srcintf=any dstintf=any src=all dst=all service=ALL action=accept
GOOD: srcintf=users dstintf=servers src=Users-subnet dst=App-1 service=HTTPS action=accept log=all
```

#### ۴-۶) North-South و East-West

- **North-South:** ورود/خروج از سازمان (اینترنت). سنتی‌ترین نقطه‌ی کنترل.
- **East-West:** ترافیک داخلی بین سرورها/کاربران. بیشتر حملات واقعی پس از نفوذ اولیه از همین مسیر **حرکت جانبی (Lateral Movement)** می‌کنند. اگر فقط لبه کنترل شود، مهاجمی که یک PC را بگیرد آزادانه به سرورها می‌رسد.

نتیجه: **Segmentation داخلی** و Policy بین Zoneهای داخلی ضروری است (فصل ۲۴: Data Center).

### ۵) مثال حل‌شده

**سازمان کوچک:** وب‌سرور عمومی (DMZ)، اپلیکیشن و دیتابیس (Servers)، کاربران، Guest، Management.

مدل تهدید:

| Asset | Threat | مسیر حمله | کنترل |
|---|---|---|---|
| DB مشتری | مهاجم پس از نفوذ به وب‌سرور | DMZ → Servers | Policy فقط وب‌سرور→App روی پورت لازم؛ App→DB؛ هیچ مسیر DMZ→DB |
| AD | بدافزار روی PC | Users → DC | فقط پروتکل‌های لازم (Kerberos/LDAP) از Users به DC؛ Log |
| فایروال | مدیر ناشناس | اینترنت → GUI مدیریت | غیرفعال‌سازی `allowaccess` روی WAN، Trusted Host، MFA |
| Guest | کاربر مهمان آلوده | Guest → Users | Zone جدا، فقط اینترنت |

``` text
Users   -> Internet : HTTP/HTTPS/DNS      allow + UTM
Users   -> Servers  : HTTPS to app only   allow + log
Servers -> DB       : TCP 1433 only       allow + log
DMZ     -> Servers  : TCP 8080 to app only
DMZ     -> DB       : none (deny)
Guest   -> Internet : HTTP/HTTPS/DNS only
Guest   -> any internal : deny
any     -> any      : implicit deny + log
```

**مثال سخت:** مدیر شبکه می‌خواهد برای عیب‌یابی «موقتاً» همه‌چیز را باز کند. با مدل تهدید توضیح دهید چرا خطرناک است و روش جایگزین ایمن چیست (Policy موقت با Source دقیق + زمان‌بندی + Log + حذف بعد از اتمام، با Change). 

### ۶) طراحی و تصمیم‌گیری

| تصمیم | گزینه‌ها | معیار |
|---|---|---|
| تعداد Zone | کم (ساده) / زیاد (امن‌تر) | ریسک، پیچیدگی عملیات |
| فایروال یکتا یا چندلایه | تک/دوتایی | ریسک + بودجه؛ برای داده‌ی حساس: دو لایه (فصل ۱۵) |
| Inspection کامل یا انتخابی | UTM همه/انتخابی | Performance (فصل ۱۶) |
| Logging | همه‌ی Deny + Allow مهم | فضا، هزینه |

### ۷) پیاده‌سازی و Verification (مفهومی)

- نقشه‌ی Zoneها و جدول Policy Matrix (Source Zone، Destination Zone، Service، Action) را قبل از پیکربندی بنویسید.
- پس از پیاده‌سازی: **آزمون مثبت** (مجاز موفق) و **آزمون منفی** (غیرمجاز شکست) برای هر خط.
- ابزار: `nmap` از هر Zone، `ping/curl`، و Log فایروال.

### ۸) Troubleshooting (مبتنی بر طراحی)

| علامت | علت محتمل |
|---|---|
| «همه چیز کار می‌کند» ولی ناامن | Policy any-any؛ آزمون منفی انجام نشده |
| سرویس کار نمی‌کند | Service/Port ناقص، یا Zone اشتباه |
| Log حجیم و بی‌فایده | Log همه‌ی Allow بدون هدف |

### ۹) نکات امنیتی

- بزرگ‌ترین اشتباه: تصمیم امنیتی بدون مدل تهدید.
- Policyهای موقت را با تاریخ انقضا بنویسید.
- مرز مدیریتی (Management) را جدا نگه دارید و از اینترنت قابل‌دسترس نکنید.

### ۱۰) جمع‌بندی مفهومی

- Risk = احتمال × اثر؛ کنترل ریسک را کم می‌کند، صفر نمی‌کند.
- مرز اعتماد = جایی که سطح اعتماد عوض می‌شود؛ هر عبور کنترل می‌شود.
- Defense in Depth: چند لایه‌ی مستقل.
- Default Deny و Least Privilege پایه‌ی Policy خوب‌اند.
- East-West را هم کنترل کنید؛ حرکت جانبی واقعی‌ترین مسیر بعد از نفوذ است.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) Asset، Threat و Vulnerability را با مثال تعریف کنید. *(پاسخ: 11-0-ت1)*

**ت2.** (ساده) Trust Boundary یعنی چه؟ *(پاسخ: 11-0-ت2)*

**ت3.** (متوسط) چرا Default Deny امن‌تر از Default Allow است؟ *(پاسخ: 11-0-ت3)*

**ت4.** (متوسط) چرا فایروال لبه به‌تنهایی از حرکت جانبی جلوگیری نمی‌کند؟ *(پاسخ: 11-0-ت4)*

**ت5.** (سخت) برای شبکه‌ای با Users، Servers، DMZ، Guest و Management جدول Policy Matrix بنویسید و برای هر سطر یک دلیل ذکر کنید. *(پاسخ: 11-0-ت5)*

**ت6.** (سخت، طراحی) مهاجمی از طریق VPN کاربر آلوده به شبکه نفوذ کرده است. چهار لایه‌ی Defense in Depth که باید او را متوقف کنند نام ببرید. *(پاسخ: 11-0-ت6)*

**م1.** STRIDE سرنام چیست؟ *(پاسخ: 11-0-م1)*

**Q1.** Quick quiz (English): What is lateral movement and which control limits it? *(پاسخ: 11-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| STRIDE | Spoofing, Tampering, Repudiation, Information disclosure, DoS, Elevation | مدل دسته‌بندی تهدید |
| DiD | Defense in Depth | دفاع چندلایه |
| NS/EW | North-South / East-West | ترافیک ورود/خروج و ترافیک داخلی |
| LM | Lateral Movement | حرکت جانبی مهاجم |
| MFA | Multi-Factor Authentication | احراز چندعاملی |
| DMZ | Demilitarized Zone | ناحیه‌ی واسط |

- *Never rely on a single control; layer your defenses.* ← هرگز فقط به یک کنترل اتکا نکنید؛ دفاع را لایه‌ای کنید.
- *Segment the network to limit lateral movement.* ← شبکه را بخش‌بندی کنید تا حرکت جانبی محدود شود.

### ۱۳) منابع

- NIST SP 800-30 — Guide for Conducting Risk Assessments.
- NIST SP 800-41 Rev.1 — Guidelines on Firewalls and Firewall Policy.
- Microsoft: STRIDE Threat Modeling.
- MITRE ATT&CK — Lateral Movement (مفهومی).

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: مدل تهدید و Defense in Depth قبل از نوشتن اولین Policy

#### چرا باید یاد بگیریم؟

Policy بدون مدل تهدید مثل قفل‌گذاری بی‌دانستن اینکه دزد از کجا می‌آید است. اول باید بپرسید: «چه چیزی ارزش دارد؟ چه کسی می‌خواهد آن را؟ از کدام مسیر؟».

#### مدل ساده

``` text
Asset      : ERP database, customer data
Threat     : external attacker, malware, insider, misconfiguration
Path       : internet -> web -> app -> db ; user PC -> server
Control    : segmentation, policy, IPS, MFA, logging
Residual   : what remains after controls
```

#### Defense in Depth

لایه‌های مستقل: محیط (فایروال)، شبکه (Segmentation)، میزبان (EDR/Patch)، برنامه (WAF)، داده (رمزنگاری)، هویت (MFA)، پایش (Log). شکست یک لایه نباید همه را بشکند.

#### مثال ساده — مرز اعتماد

Trust Boundary جایی است که سطح اعتماد تغییر می‌کند: اینترنت→DMZ، DMZ→داخل، Users→Servers.

#### مثال متوسط — امتیاز ریسک

``` text
Risk = Likelihood (1-5) x Impact (1-5)
Web exposed to internet: 4 x 5 = 20 (high)
Internal print server  : 2 x 2 = 4  (low)
```

> **حدود اعتبار (v4.0):** «احتمال × اثر» یک **ابزار رتبه‌بندی نیمه‌کمّی آموزشی** است، نه مدل کامل ریسک. مقیاس‌های ۱ تا ۵ ترتیبی‌اند (نه احتمال یا هزینه‌ی واقعی)، حاصل‌ضرب مقادیر متفاوت را ممکن است برابر کند (۵×۱ و ۱×۵) در حالی که ماهیت‌شان فرق دارد، و به برآورد انسانی وابسته است. برای تصمیم، فرض‌های برآورد، دارایی/تهدید/آسیب‌پذیری و کنترل‌های موجود را کنار عدد بنویسید؛ عدد را «تضمین» ندانید. (مدل‌های کامل‌تر مثل ISO/IEC 27005 یا FAIR فراتر از دامنه‌ی این درس‌اند.)


#### مثال سخت — کنترل جایگزین

سرور قدیمی بدون Patch که نمی‌توان ارتقا داد: کنترل جبرانی: Segmentation شدید، فقط پورت لازم، IPS، پایش.

#### Lab

یک جدول دارایی/تهدید/کنترل برای شبکه‌ی خودتان بنویسید.

#### عیب‌یابی طراحی

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| کنترل بی‌هدف | بدون مدل | مدل تهدید |
| یک لایه | بدون عمق | لایه‌ها |
| ریسک نامعلوم | بدون امتیاز | ارزیابی |

#### پرسش‌ها با پاسخ

**۱. Trust boundary؟** تغییر سطح اعتماد.
**۲. Defense in depth؟** لایه‌های مستقل.
**۳. کنترل جبرانی؟** جایگزین وقتی Patch ممکن نیست.

#### English Corner

- *Threat modeling asks what to protect, from whom, and via which path.*
- Q: What is a compensating control?

## درس 11-1 — فایروال چیست؟ Stateless در برابر Stateful، و چرا هر دو مهم‌اند

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰، ۲-۱ · ≈ 9 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. فایروال را تعریف و جایگاه آن را در شبکه توضیح دهید.
2. فرق Stateless (ACL/Packet Filter) و Stateful را با مثال بگویید.
3. Session Table و چرخه‌ی عمر یک اتصال را شرح دهید.
4. فرق Stateful با Application-aware/NGFW را بدانید.
5. محدودیت‌های Stateful (ظرفیت، نامتقارن، UDP) را فهرست کنید.
6. حمله‌ی ACK Scan را روی ACL و فایروال مقایسه کنید.

### چرا باید یاد بگیریم؟

ساختمانی را تصور کنید. قفل در ورودی فقط می‌پرسد «کارت دارید؟». نگهبان می‌پرسد «شما را قبلاً دیده‌ام؟ کسی شما را دعوت کرده؟ از کدام در رفتید؟». فایروال دستگاهی است که ترافیک بین شبکه‌ها را بر اساس **سیاست** مجاز یا ممنوع می‌کند. نسل اول فقط «کارت» را می‌دید (فیلتر بسته)؛ نسل‌های بعدی «حافظه» (Stateful) و بعد «محتوا» (UTM/NGFW) را اضافه کردند. این درس اساس همه‌ی فصل‌های بعد است: Policy، NAT، Session، عیب‌یابی همه به همین تفاوت برمی‌گردد.

### نسل‌های فایروال

| نسل | ویژگی | مثال |
|---|---|---|
| Packet Filter (Stateless) | هر بسته مستقل با ACL | ACL روتر |
| Stateful Inspection | Session و وضعیت اتصال | فایروال کلاسیک |
| Application-aware | تشخیص برنامه (L7) | Application Control |
| NGFW/UTM | IPS، AV، Web، SSL Inspection | FortiGate |

### Stateless (ACL)

هر بسته را فقط با قواعد می‌سنجد؛ حافظه‌ای از بسته‌ی قبل ندارد. پس برای وب باید هم رفت و هم برگشت را بنویسید:

``` text
permit tcp 10.10.0.0 0.0.0.255 any eq 443
permit tcp any eq 443 10.10.0.0 0.0.0.255 established
```

`established` یعنی بسته‌ی TCP با پرچم ACK یا RST. ولی ACL نمی‌داند این ACK پاسخ یک درخواست واقعی است یا بسته‌ی جعلی؛ مهاجم می‌تواند بسته‌ی ACK ساختگی بفرستد و از ACL عبور کند (ACK Scan).

### Stateful

برای هر اتصال یک **Session** (یک رکورد در Session Table) می‌سازد و بسته‌ها را با آن تطبیق می‌دهد:

``` text
Proto  Src               Dst                 State        Timeout
tcp    10.10.0.5:49152   198.51.100.8:443    ESTABLISHED  3600
```

وقتی کاربر به وب می‌رود:

1. SYN از Interface داخلی می‌رسد.
2. Policy بررسی می‌شود؛ مجاز ⇒ Session ساخته می‌شود.
3. بسته‌ی برگشت (SYN-ACK) با Session تطبیق داده و **خودکار** پذیرفته می‌شود (بدون قاعده‌ی برگشت).
4. اتصال بسته (FIN/RST) یا Timeout ⇒ Session حذف.

پس فقط «جهت آغاز اتصال» را در Policy می‌نویسید.

### مزیت‌ها

- امنیت: بسته‌ی بدون Session (ACK/SYN-ACK جعلی) رد می‌شود.
- سادگی: قاعده‌ی برگشت لازم نیست.
- ردیابی: Log در سطح اتصال، نه بسته.
- زیربنای NAT و بازرسی عمیق.

### محدودیت‌ها

- **ظرفیت Session Table:** هر دستگاه سقف Session دارد؛ سیل (SYN Flood) آن را پر می‌کند.
- **نیاز به مسیر متقارن:** بسته‌ی برگشت باید از همان فایروال بگذرد.
- **UDP/ICMP:** اتصال ندارند؛ فایروال «Session مجازی» با Timeout کوتاه می‌سازد.
- **پروتکل‌های چندکاناله (FTP، SIP):** باید ALG/Helper باشد.
- **CPU و حافظه.**

### مثال‌های حل‌شده

#### مثال ساده — تفاوت قاعده‌ها

وب برای شبکه‌ی داخلی:

``` text
ACL (stateless): 2 rules (out + return established)
Firewall (stateful): 1 policy (inside -> outside 443), return automatic
```

#### مثال متوسط — حمله‌ی ACK

مهاجم از اینترنت به سرور 10.20.0.10 بسته‌ی TCP با ACK=1 می‌فرستد (بدون Handshake).

- ACL با `established`: عبور می‌دهد (چون ACK دارد). اگر سرور پاسخ RST بدهد، مهاجم می‌فهمد پورت باز/بسته است و ساختار شبکه را شناسایی می‌کند.
- فایروال Stateful: Session ندارد ⇒ Drop. Log: `no session matched`.

#### مثال متوسط — چرخه‌ی عمر Session

``` text
t=0    SYN        -> session created (SYN_SENT)
t=0.1  SYN-ACK    -> state ESTABLISHED
t=0.2  ... data ... 
t=30   FIN/ACK    -> TIME_WAIT/closing
t=60   removed
```

اگر اتصال بدون FIN رها شود، Timeout (ساعت‌ها برای TCP، ثانیه برای UDP) حذفش می‌کند.

#### مثال سخت — نامتقارن

SYN از فایروال A و SYN-ACK از B. B Session ندارد و Drop می‌کند. علامت: «اتصال بعضی وقت‌ها کار می‌کند». اثبات: Sniffer دو سمت. رفع: طراحی متقارن/SNAT/Session Sync (درس ۲۳).

#### مثال سخت — ظرفیت

دستگاه با سقف 200,000 Session. در حمله‌ی SYN Flood 50,000 SYN/ثانیه: Table در ۴ ثانیه پر می‌شود:

``` text
200000 / 50000 = 4 seconds to fill
```

دفاع: DoS Policy با آستانه (درس 16-10)، SYN Cookie، Timeout کوتاه برای SYN_RECV.

### Lab هدایت‌شده (اجرا نشده)

1. یک ACL ساده برای وب بنویسید و `established` را حذف کنید؛ اثر را ببینید.
2. با `hping3` یک ACK Scan (در Lab) بفرستید و تفاوت ACL/فایروال را ثبت کنید.
3. Session Table را با `diagnose sys session list` ببینید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| پاسخ وب رد می‌شود (ACL) | قاعده‌ی برگشت نیست | `established` یا Stateful |
| اتصال گیر می‌کند | نامتقارن | Sniffer دو سمت |
| Table پر | سیل | DoS Policy |
| FTP/SIP مشکل | ALG | فعال‌سازی |

### جمع‌بندی

Stateless هر بسته را جدا می‌سنجد و قاعده‌ی برگشت می‌خواهد؛ Stateful با Session برگشت را خودکار می‌پذیرد و بسته‌ی بدون Session را رد می‌کند. محدودیت‌ها: ظرفیت، تقارن، UDP/ALG.

### تمرین و ارزیابی

**ت1.** (ساده) تفاوت Stateless و Stateful؟ *(پاسخ: 11-1-ت1)*

**ت2.** (ساده) NGFW چه چیزی اضافه دارد؟ *(پاسخ: 11-1-ت2)*

**ت3.** (متوسط) چرا ACL برگشتی با eq 443 خطرناک است؟ *(پاسخ: 11-1-ت3)*

**ت4.** (متوسط) UDP چطور Session می‌گیرد؟ *(پاسخ: 11-1-ت4)*

**ت5.** (سخت) CPU کم و نیاز به NGFW. *(پاسخ: 11-1-ت5)*

**ت6.** (سخت، طراحی) انتخاب نوع فایروال برای مرز. *(پاسخ: 11-1-ت6)*

**Q1.** Quick quiz (English): What does a stateful firewall store for each allowed connection? *(پاسخ: 11-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NGFW | Next-Generation Firewall | فایروال نسل بعد |
| SYN | Synchronize flag | پرچم شروع اتصال |

- *A stateful firewall tracks connection state.* ← فایروال حالت‌دار وضعیت اتصال را دنبال می‌کند.

### کارت Lab

**کارت Lab:** Stateful. **Evidence:** `03-ops/stateful.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policy
- RFC 793

<a id="l-11-2"></a>

## درس 11-2 — Zone، Trust Boundary، Default Deny و Least Privilege: از ماتریس تا Policy

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰، ۱۱-۱ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Zone، Trust Level و Trust Boundary را تعریف کنید.
2. اصل Default Deny و Least Privilege را توضیح دهید.
3. از نیاز کسب‌وکار، ماتریس ارتباط بسازید.
4. ماتریس را به Policy تبدیل و آزمون مثبت و منفی بنویسید.
5. intrazone را بفهمید و ریسک آن را کنترل کنید.
6. Policy را با Lookup اثبات کنید.

### چرا باید یاد بگیریم؟

شبکه‌ی سازمان یکدست نیست. اینترنت، DMZ (سرورهای عمومی)، کاربران، سرورهای داخلی، مدیریت و مهمان هرکدام «سطح اعتماد» متفاوتی دارند. تصور کنید ساختمان اداری: لابی (عمومی)، طبقات کارکنان (متوسط)، اتاق سرور (بسیار محرمانه). ورود از لابی به اتاق سرور از چند در می‌گذرد، هر دری کارت‌خوان جدا. **Zone** و **Trust Boundary** این منطق را به شبکه می‌آورند. بسیاری از نفوذها پس از ورود اولیه با «حرکت جانبی» ادامه می‌یابند؛ Zoneبندی و Policy حداقلی مانع آن است.

### مفاهیم

- **Zone:** گروه Interface/شبکه‌هایی با سطح اعتماد و سیاست یکسان.
- **Trust Level:** مثلاً Internet=0، DMZ=30، Users=50، Servers=70، Mgmt=90.
- **Trust Boundary:** مرزی که ترافیک از یک سطح به سطح دیگر می‌رود؛ فایروال باید در آن باشد.
- **Default Deny:** هرچه مجاز نشده ممنوع است.
- **Least Privilege:** فقط همان دسترسی لازم، به همان مقصد و همان سرویس.

### قاعده‌ی جریان بین Zoneها

| از → به | قاعده‌ی کلی |
|---|---|
| اطمینان پایین → بالا | بسیار محدود؛ فقط سرویس مشخص |
| بالا → پایین | معمولاً بیشتر مجاز ولی با Log |
| هم‌سطح | بر اساس نیاز |
| Internet → داخل | فقط VIP/سرویس منتشر |

### روش: از ماتریس به Policy

**گام ۱ — فهرست Zoneها:** Internet، DMZ، Users، Servers، Mgmt، Guest.

**گام ۲ — ماتریس نیاز:**

| از ↓ / به → | Internet | DMZ | Servers | Mgmt |
|---|---|---|---|---|
| Users | HTTP/S، DNS | HTTPS | HTTPS، SMB | — |
| Guest | HTTP/S، DNS | — | — | — |
| Internet | — | HTTPS (VIP) | — | — |
| Mgmt | — | SSH | SSH | همه |

خانه‌ی خالی یعنی Deny.

**گام ۳ — تبدیل به Policy:**

``` text
Policy 10 USERS -> SRV  HTTPS,SMB       accept log
Policy 20 USERS -> INET HTTP,HTTPS,DNS  accept nat log
Policy 30 GUEST -> INET HTTP,HTTPS,DNS  accept nat log
Policy 40 INET  -> DMZ  HTTPS (VIP)     accept log
Policy 50 MGMT  -> any  SSH,HTTPS,ICMP  accept log
Policy 90 any   -> any  ALL             deny   log
```

**گام ۴ — آزمون:** برای هر Policy یک آزمون مثبت؛ برای هر خانه‌ی خالی چند آزمون منفی.

### intrazone

در FortiGate اگر دو Interface در یک Zone باشند، ترافیک بین آنها با `intrazone` کنترل می‌شود: `allow` (آزاد) یا `deny` (ابتدا ممنوع و با Policy صریح). برای ایزولاسیون واقعی `deny` بگذارید.

``` text
config system zone
 edit "ZN-DMZ"
  set interface "port2" "port5"
  set intrazone deny
 next
end
```

### Verification

``` text
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.10 445 tcp port2     # policy 10
diagnose firewall iprope lookup 10.99.0.5 40000 10.50.0.20 22 tcp port4      # deny (guest -> mgmt)
```

### مثال‌های حل‌شده

#### مثال ساده — خواندن ماتریس

Users→Servers: HTTPS و SMB؛ Users→Mgmt: خالی ⇒ Deny. اگر کاربری SSH به Mgmt بزند، `policy 90` و Log Deny.

#### مثال متوسط — حداقل دسترسی

درخواست: «دسترسی Users به Servers». پاسخ ضعیف: `Users -> Servers ALL`. پاسخ درست: `Users -> SRV-ERP HTTPS`. اگر یک کاربر آلوده شود، فقط یک سرویس در معرض است. شمارش: ALL (65535 پورت × همه‌ی سرورها) در برابر یک پورت روی یک سرور.

#### مثال متوسط — آزمون منفی

``` text
from GUEST: nc -zv 10.20.0.10 443   -> timeout (expected)
from USERS: nc -zv 10.50.0.20 22    -> timeout (expected)
```

Log هر دو `action=deny policyid=90`.

#### مثال سخت — Zone با intrazone باز

دو Interface DMZ در یک Zone با `intrazone allow`. وب‌سرور هک‌شده مستقیم به DB در همان Zone می‌رود (بدون Policy). شاهد: Session بدون Policy ID. رفع: `set intrazone deny` و Policy صریح Web→App و App→DB.

#### مثال سخت — ماتریس ناقص

پس از Segmentation، مدیر شکایت دارد «چاپگر کار نمی‌کند». ماتریس سطر «Users→Printers» نداشت. با Log Deny ۳۰ روزه (Flow Discovery) کشف می‌شود؛ Policy `USERS -> PRN tcp/9100` اضافه می‌شود. درس: ماتریس را با مالکان سرویس مرور کنید.

### Lab هدایت‌شده (اجرا نشده)

1. چهار Zone؛ ماتریس را بکشید.
2. Policyها را بنویسید و Lookup اجرا کنید.
3. آزمون منفی و Log.
4. intrazone deny و مشاهده‌ی اثر.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Policy ALL | تنبلی | تنگ‌کردن |
| Zone باز | intrazone allow | deny |
| قطع برنامه | ماتریس ناقص | Log + افزودن |
| بی‌آزمون | غفلت | آزمون منفی |

### جمع‌بندی

Zone با سطح اعتماد، Default Deny و Least Privilege. از ماتریس شروع کنید؛ هر خانه‌ی پر یک Policy؛ هر خانه‌ی خالی یک آزمون منفی. intrazone را deny کنید و با Lookup و Log اثبات کنید.

### تمرین و ارزیابی

**ت1.** (ساده) Default Deny یعنی چه؟ *(پاسخ: 11-2-ت1)*

**ت2.** (ساده) Least Privilege؟ *(پاسخ: 11-2-ت2)*

**ت3.** (متوسط) چرا ماتریس؟ *(پاسخ: 11-2-ت3)*

**ت4.** (متوسط) چرا ترتیب مهم است؟ *(پاسخ: 11-2-ت4)*

**ت5.** (سخت) Policy ALL را چطور تنگ می‌کنید؟ *(پاسخ: 11-2-ت5)*

**ت6.** (سخت، طراحی) ماتریس ۵ Zone و آزمون. *(پاسخ: 11-2-ت6)*

**Q1.** Quick quiz (English): What does default deny mean? *(پاسخ: 11-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DMZ | Demilitarized Zone | منطقه‌ی حائل |
| Trust boundary | Trust boundary | مرز اعتماد |

- *Apply least privilege to every rule.* ← به هر Rule حداقل دسترسی را بدهید.

### کارت Lab

**کارت Lab:** ماتریس Zone (اجرا نشده). **Evidence:** `03-ops/zone-matrix.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- NIST SP 800-41 Rev.1

<a id="l-11-3"></a>

## درس 11-3 — مسیر بسته در فایروال: Transit، Local-in، Local-out و ترتیب DNAT/Route/Policy/SNAT

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۱-۲ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. سه نوع ترافیک Transit، Local-in و Local-out را تمایز دهید.
2. مراحل پردازش یک بسته‌ی عبوری را به ترتیب بگویید.
3. بدانید هر کنترل (Policy، allowaccess، DoS، NAT) در کدام مرحله است.
4. با Debug Flow مراحل را مشاهده کنید.
5. خطای رایج «Policy عادی برای مدیریت» را تشخیص دهید.
6. ترتیب DNAT، Routing، Policy و SNAT را بدانید.

### چرا باید یاد بگیریم؟

هر قابلیت فایروال در مرحله‌ی مشخصی از مسیر بسته اجرا می‌شود. اگر ترتیب را ندانید، Policy را جای اشتباه می‌نویسید. مثلاً می‌خواهید SSH به خود فایروال را ببندید و Policy عادی `Users -> any SSH deny` می‌گذارید؛ بی‌اثر است چون ترافیک مقصد خود فایروال **Local-in** است و Policy عبوری آن را نمی‌بیند. این نقشه‌ی ذهنی پایه‌ی عیب‌یابی در همه‌ی فصل‌های بعد است.

### سه نوع ترافیک

| نوع | منشأ ← مقصد | کنترل |
|---|---|---|
| Transit | از میان فایروال (A → B) | Firewall Policy |
| Local-in | به خود فایروال (SSH، ping، SNMP، VPN) | `allowaccess`، Local-in Policy |
| Local-out | از خود فایروال (NTP، DNS، Syslog، FortiGuard) | تنظیم سرویس، Route، Source IP |

### مراحل ترافیک Transit

``` text
1  Ingress interface (link, VLAN)
2  Session lookup: existing session? -> fast path
3  DoS policy / anomaly checks
4  RPF (reverse path forwarding) check
5  DNAT (VIP) / pre-routing
6  Routing decision (policy route first, then route table)
7  Firewall policy lookup
8  UTM / inspection (AV, IPS, web, app)
9  SNAT (policy NAT / IP pool)
10 Egress interface
```

نکات:

- اگر Session موجود است، بسته مستقیم از مسیر سریع می‌گذرد و Policy دوباره بررسی نمی‌شود.
- **DNAT قبل از Policy و Routing** است؛ پس Policy ورودی VIP باید به **IP عمومی (VIP)** اشاره کند.
- **SNAT بعد از Policy** است؛ Policy آدرس **قبل از SNAT** را می‌بیند.
- **RPF** قبل از Policy است؛ اگر Route مبدأ از Interface دیگر باشد، بسته Drop می‌شود.

### Local-in و Local-out

**Local-in:** ترافیک با مقصد یکی از IPهای فایروال. اول `allowaccess` Interface (ping، https، ssh، snmp، fgfm، ...) و سپس Local-in Policy (در FortiGate) آن را کنترل می‌کند.

``` text
config firewall local-in-policy
 edit 1
  set intf "port1"
  set srcaddr "all"
  set dstaddr "all"
  set service "HTTPS" "SSH"
  set action deny
  set schedule "always"
 next
end
```

**Local-out:** ترافیکی که فایروال می‌سازد؛ تنظیم Source Interface/IP و Routing آن مستقل از Policy عبوری است. مشکلات رایج: Update FortiGuard نمی‌رسد، Syslog نمی‌رسد، NTP کار نمی‌کند ⇒ Route/DNS/Source IP.

### مشاهده با Debug Flow

``` text
diagnose debug reset
diagnose debug flow filter addr 10.20.0.10
diagnose debug flow show function-name enable
diagnose debug flow trace start 10
diagnose debug enable
```

نمونه خروجی (ساده):

``` text
msg="vd-root received a packet(proto=6, 10.10.0.5:40000->10.20.0.10:443)"
msg="allocate a new session-0003f1"
msg="find a route: gw-10.20.0.1 via port3"
msg="Allowed by Policy-10"
```

پایان: `diagnose debug disable` و `diagnose debug reset`.

### مثال‌های حل‌شده

#### مثال ساده — کدام نوع؟

| ترافیک | نوع | کنترل |
|---|---|---|
| PC → سرور ERP | Transit | Firewall Policy |
| PC → SSH به فایروال | Local-in | allowaccess/Local-in |
| فایروال → NTP | Local-out | NTP/Route |
| فایروال → Syslog | Local-out | source-ip/Route |

#### مثال متوسط — ترتیب DNAT/Policy

VIP 203.0.113.10:443 → 10.30.0.10:443. بسته‌ی ورودی Dst=203.0.113.10. مراحل: DNAT (Dst→10.30.0.10) ⇒ Routing (Egress به DMZ) ⇒ Policy lookup با dstaddr=VIP-WEB (آدرس قبل از DNAT برای تطبیق VIP) ⇒ UTM ⇒ خروج. اگر Policy با IP داخلی نوشته شود Lookup مطابق نمی‌شود.

#### مثال متوسط — اشتباه رایج

مهندس برای بستن SSH به فایروال، `Users -> any SSH deny` گذاشت. آزمون: `ssh admin@FW` از Users هنوز کار می‌کند. علت: Local-in است. رفع: حذف `ssh` از `allowaccess` Interface یا Local-in Policy. تأیید: Timeout.

#### مثال سخت — Update نمی‌رسد

FortiGuard Update شکست می‌خورد. Local-out:

1. `execute ping update.fortiguard.net`؟
2. DNS فایروال درست؟ (`config system dns`)
3. Route به اینترنت؟ (Default)
4. NAT خروجی برای ترافیک خود فایروال؟ (از IP Interface خروجی)
5. Policy Local-out/ISP که پورت 443/8890 را می‌بندد؟
6. `diagnose debug application update -1` (کوتاه).

#### مثال سخت — RPF در مسیر Transit

کاربر پشت Interface جدید (port6) به سرور می‌رود. Debug: `reverse path check fail`. Route به شبکه‌ی کاربر از port2 است نه port6. رفع: Route درست (Static) یا `set src-check disable` (با ریسک Spoofing؛ ثبت استثنا).

### Lab هدایت‌شده (اجرا نشده)

1. سه ترافیک (Transit، Local-in، Local-out) را تولید کنید.
2. Debug Flow را اجرا و مراحل را علامت بزنید.
3. اشتباه «Policy برای SSH به فایروال» را بسازید و رفع کنید.
4. VIP و ترتیب DNAT/Policy را مشاهده کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| SSH به FW باز است | Local-in | allowaccess |
| Update نمی‌رسد | Local-out | Route/DNS |
| Policy VIP مطابق نمی‌شود | آدرس قبل از DNAT | dst=VIP |
| RPF fail | Route | تصحیح |

### جمع‌بندی

Transit با Policy؛ Local-in با allowaccess/Local-in؛ Local-out با تنظیم سرویس و Route. ترتیب Transit: Session، DoS، RPF، DNAT، Routing، Policy، UTM، SNAT. با Debug Flow ببینید.

### تمرین و ارزیابی

**ت1.** (ساده) DNAT قبل یا بعد Policy؟ *(پاسخ: 11-3-ت1)*

**ت2.** (ساده) Local-in چیست؟ *(پاسخ: 11-3-ت2)*

**ت3.** (متوسط) چرا Policy VIP با IP داخلی کار نمی‌کند؟ *(پاسخ: 11-3-ت3)*

**ت4.** (متوسط) RPF چیست؟ *(پاسخ: 11-3-ت4)*

**ت5.** (سخت) Admin به https نمی‌رسد؛ مسیر عیب‌یابی. *(پاسخ: 11-3-ت5)*

**ت6.** (سخت، طراحی) نقشه‌ی Flow سازمان. *(پاسخ: 11-3-ت6)*

**Q1.** Quick quiz (English): Does destination NAT occur before or after the policy lookup? *(پاسخ: 11-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس |
| VIP | Virtual IP | آدرس مجازی |

- *Trace the packet stage by stage.* ← بسته را مرحله‌به‌مرحله ردیابی کنید.

### کارت Lab

**کارت Lab:** Flow (اجرا نشده). **Evidence:** `03-ops/packet-walk.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Packet flow
- FortiOS 7.0 Troubleshooting guide

<a id="l-11-4"></a>

## درس 11-4 — ACL، Policy و NAT: تفاوت‌ها، ارتباط‌ها و ترکیب درست

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۱-۳ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. سه سؤال متفاوت ACL/Policy، NAT و Routing را از هم جدا کنید.
2. ترتیب DNAT، Policy و SNAT را در یک جریان توضیح دهید.
3. آدرس قبل و بعد از NAT را در Policy درست به‌کار ببرید.
4. NAT ۱:۱ روی Tunnel با آدرس هم‌پوشان را طراحی کنید.
5. خطای «Policy مطابق نمی‌شود» را از روی ترتیب NAT تشخیص دهید.
6. ACL را با Policy مقایسه کنید.

### چرا باید یاد بگیریم؟

ACL، Policy، NAT و Routing اغلب با هم قاطی می‌شوند ولی سه سؤال متفاوتی را جواب می‌دهند: **«اجازه هست؟»** (ACL/Policy)، **«آدرس چه شود؟»** (NAT)، **«از کجا برود؟»** (Routing). ترکیب غلط آنها یکی از رایج‌ترین علل خطاست. مثلاً Policy را با آدرس داخلی می‌نویسید ولی Policy «قبل از DNAT» ارزیابی می‌شود؛ یا Route را بعد از NAT فرض می‌کنید ولی قبل از آن است.

### سه سؤال

| ابزار | سؤال | مثال |
|---|---|---|
| Policy/ACL | مجاز است؟ | Users→ERP HTTPS accept |
| NAT | آدرس چه شود؟ | 10.10.0.5 → 203.0.113.2 |
| Routing | از کدام Interface/Next-hop؟ | 0.0.0.0/0 via port1 |

### ACL و Policy

| ویژگی | ACL | Firewall Policy |
|---|---|---|
| وضعیت | بدون حافظه | Stateful |
| معیار | آدرس، پورت، پروتکل | + Interface، کاربر، برنامه، زمان |
| عمل | permit/deny | accept/deny + UTM + NAT + Log |
| محل | Interface (in/out) | Interface/Zone جفتی |

### ترتیب پردازش در یک جریان با NAT

برای ترافیک ورودی به VIP:

``` text
Client 198.51.100.50 -> 203.0.113.10:443
1 DNAT : dst 203.0.113.10 -> 10.30.0.10
2 Route : to 10.30.0.10 via DMZ interface
3 Policy: INET -> DMZ, dstaddr = VIP-WEB (the VIP object), service HTTPS
4 SNAT : (optional) src can be translated
```

برای ترافیک خروجی با SNAT:

``` text
User 10.10.0.5 -> 198.51.100.8:443
1 Route : egress port1
2 Policy: USERS -> INET (src = 10.10.0.5, pre-SNAT)
3 SNAT  : src -> 203.0.113.2
```

**نتیجه‌ی مهم:** Policy آدرس **مبدأ قبل از SNAT** و آدرس **مقصد قبل از DNAT (یعنی خود VIP)** را می‌بیند.

### NAT یک‌به‌یک روی Tunnel (آدرس هم‌پوشان)

دو سایت هر دو 192.168.1.0/24. در سایت A، سایت B را به 10.222.1.0/24 ترجمه می‌کنیم:

``` text
Real B host      : 192.168.1.10
As seen at site A: 10.222.1.10  (VIP mapping 10.222.1.0/24 -> 192.168.1.0/24)
```

Policy و Route در A باید با **10.222.1.0/24** نوشته شوند و DNS هم نام را به آدرس ترجمه‌شده حل کند.

### مثال‌های حل‌شده

#### مثال ساده — Users به اینترنت

Routing: خروج port1. Policy: Users→Internet accept. NAT: با IP Interface. `diagnose sys session list` فیلد snat را نشان می‌دهد.

#### مثال متوسط — VIP و Policy

``` text
config firewall vip
 edit "VIP-WEB"
  set extip 203.0.113.10
  set mappedip "10.30.0.10"
 next
end
config firewall policy
 edit 40
  set srcintf "port1"
  set dstintf "port2"
  set dstaddr "VIP-WEB"
  set service "HTTPS"
  set action accept
 next
end
```

اگر به‌جای VIP-WEB آدرس 10.30.0.10 را بنویسید، Lookup بسته‌ی ورودی مطابق نمی‌شود (policy 0).

#### مثال متوسط — ACL به Policy

ACL: `permit tcp 10.10.0.0/24 host 10.20.0.10 eq 443`. معادل Policy: srcaddr NET-USERS، dstaddr SRV-ERP، service HTTPS. تفاوت: برگشت خودکار؛ Log و UTM اختیاری.

#### مثال سخت — NAT ۱:۱ روی Tunnel

A (10.1.0.0/24) و B (192.168.1.0/24) و A هم 192.168.1.0/24 (محلی) دارد؟ نه؛ فرض: B هم‌پوشان با شبکه‌ی داخلی A (192.168.1.0/24). راه: در A یک VIP بنویسید:

``` text
config firewall vip
 edit "B-HOSTS"
  set extip 10.222.1.0-10.222.1.255
  set mappedip "192.168.1.0-192.168.1.255"
  set extintf "TO-B"
 next
end
```

Policy: `LAN -> TO-B` با dstaddr=B-HOSTS. DNS: نام سرور B ⇒ 10.222.1.x. آزمون: `ping 10.222.1.10` از LAN؛ Debug Flow نشان می‌دهد DNAT به 192.168.1.10.

#### مثال سخت — «Policy مطابق نمی‌شود»

1. `diagnose firewall iprope lookup` با آدرس‌ها؛ نتیجه policy 0.
2. اگر Policy ورودی VIP است: dstaddr را بررسی (VIP، نه IP داخلی).
3. اگر خروجی با SNAT است: srcaddr قبل از NAT (IP داخلی).
4. Interface/Zone درست؟
5. Policy بالاتر ترافیک را می‌گیرد؟ (Shadow)

### Lab هدایت‌شده (اجرا نشده)

1. VIP ساخته و Policy با IP داخلی بنویسید؛ مشاهده‌ی Drop.
2. اصلاح به VIP و آزمون.
3. SNAT و Lookup با آدرس قبل از NAT.
4. NAT ۱:۱ آزمایشی برای آدرس هم‌پوشان.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Policy مطابق نمی‌شود | آدرس قبل/بعد NAT | dstaddr=VIP |
| NAT بی‌اثر | Policy بدون nat | `set nat enable` |
| Route اشتباه | Interface | بررسی |
| آدرس هم‌پوشان | VIP ۱:۱ | تنظیم |

### جمع‌بندی

Policy مجاز بودن، NAT آدرس و Routing مسیر را تعیین می‌کند. DNAT قبل از Policy، SNAT بعد از آن؛ پس Policy VIP را می‌بیند. NAT ۱:۱ آدرس‌های هم‌پوشان را حل می‌کند ولی Policy/DNS باید با آدرس ترجمه‌شده هماهنگ باشد.

### تمرین و ارزیابی

**ت1.** (ساده) NAT چه می‌کند؟ *(پاسخ: 11-4-ت1)*

**ت2.** (ساده) PAT چیست؟ *(پاسخ: 11-4-ت2)*

**ت3.** (متوسط) چرا VIP بدون Policy کار نمی‌کند؟ *(پاسخ: 11-4-ت3)*

**ت4.** (متوسط) Hairpin چیست؟ *(پاسخ: 11-4-ت4)*

**ت5.** (سخت) Hairpin را چطور حل می‌کنید؟ *(پاسخ: 11-4-ت5)*

**ت6.** (سخت، طراحی) انتشار سه سرویس. *(پاسخ: 11-4-ت6)*

**Q1.** Quick quiz (English): Why does a VIP alone not allow traffic through? *(پاسخ: 11-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PAT | Port Address Translation | ترجمه‌ی پورت |
| VIP | Virtual IP | آدرس مجازی |

- *NAT alone does not permit traffic.* ← NAT به‌تنهایی ترافیک را مجاز نمی‌کند.

### کارت Lab

**کارت Lab:** NAT و VIP (اجرا نشده). **Evidence:** `02-design/fgt-nat.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: NAT; Virtual IPs

<a id="l-11-5"></a>

## درس 11-5 — Session، Timeout، MTU/MSS و ریشه‌ی خرابی‌های «نیمه‌کارکرده» TCP/UDP

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۴-۲، ۱۱-۳ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. چرخه‌ی Session و Timeoutهای TCP/UDP/ICMP را بشناسید.
2. MTU، MSS و Fragmentation را با محاسبه توضیح دهید.
3. PMTUD و Blackhole را تشخیص دهید.
4. MSS Clamp را در Policy و Tunnel تنظیم کنید.
5. خرابی‌های «نیمه‌کارکرده» را دسته‌بندی کنید.
6. با Capture ریشه‌ی مشکل را اثبات کنید.

### چرا باید یاد بگیریم؟

بدترین خرابی‌ها «گاهی کار می‌کند» هستند: سایت باز می‌شود ولی تصاویر نه؛ ping جواب می‌دهد ولی وب نه؛ SSH بعد از یک ساعت بی‌کاری قطع می‌شود. این‌ها معمولاً از سه علت می‌آیند: **Timeout**، **MTU/MSS** و **مسیر نامتقارن**. این درس دو علت اول را با محاسبه و آزمون باز می‌کند.

### Session و Timeout

Session پس از مدتی بدون ترافیک حذف می‌شود. مقادیر نمونه (پیش‌فرض‌ها را از مستند نسخه بخوانید):

| پروتکل/حالت | Timeout نمونه |
|---|---|
| TCP ESTABLISHED | 3600 s (1 ساعت) |
| TCP SYN_SENT / SYN_RECV | چند ثانیه تا دقیقه |
| TCP TIME_WAIT | کوتاه |
| UDP | حدود 60 s |
| ICMP | چند ثانیه |

نتیجه: اتصال بی‌کار TCP پس از ۳۶۰۰ ثانیه حذف می‌شود؛ بسته‌ی بعدی کلاینت Session ندارد و RST می‌گیرد یا Drop می‌شود. راه‌ها: Keepalive در برنامه/کلاینت (کمتر از Timeout)، یا افزایش Timeout برای Service/Policy خاص.

``` text
ssh -o ServerAliveInterval=60 user@server
```

### MTU، MSS و Fragmentation

- **MTU (Maximum Transmission Unit):** بزرگ‌ترین بسته‌ی IP روی لینک (اترنت 1500).
- **MSS (Maximum Segment Size):** بزرگ‌ترین داده‌ی TCP در یک Segment.

``` text
MSS = MTU - IP header (20) - TCP header (20) = 1500 - 40 = 1460
```

اگر در مسیر لینکی با MTU کمتر باشد (مثلاً Tunnel با 1400)، بسته‌ی بزرگ‌تر باید:

1. **Fragment** شود (اگر DF=0)، یا
2. **Drop** شود و ICMP «Fragmentation Needed» (Type 3 Code 4) برگردد (اگر DF=1).

**PMTUD (Path MTU Discovery):** فرستنده با DF=1 می‌فرستد و از ICMP Type 3 Code 4 اندازه‌ی مجاز را می‌فهمد و MSS را کم می‌کند. **اگر ICMP در مسیر فیلتر شود (Blackhole)،** فرستنده نمی‌فهمد و بسته‌های بزرگ بی‌صدا گم می‌شود؛ بسته‌های کوچک (ping معمولی، Handshake) رد می‌شوند. علامت: «ping جواب می‌دهد ولی HTTPS نه» یا «صفحه شروع می‌شود و بعد گیر می‌کند».

### MSS Clamp

مستقل از ICMP، فایروال MSS را در SYN کاهش می‌دهد تا از ابتدا بسته‌ها کوچک باشد:

``` text
config firewall policy
 edit 30
  set tcp-mss-sender 1360
  set tcp-mss-receiver 1360
 next
end
```

و روی Tunnel (Cisco): `ip tcp adjust-mss 1360`.

### آزمون Path MTU

``` text
ping -f -l 1472 198.51.100.8      (Windows; payload 1472 + 28 = 1500)
ping -M do -s 1472 198.51.100.8   (Linux)
```

کاهش اندازه تا اولین موفقیت:

``` text
Max successful payload = 1372  ->  Path MTU = 1372 + 28 = 1400  ->  MSS = 1400 - 40 = 1360
```

### مثال‌های حل‌شده

#### مثال ساده — Timeout SSH

SSH پس از ۱ ساعت بی‌کاری می‌افتد. علت: Timeout ۳۶۰۰ s. رفع: `ServerAliveInterval 60`. تأیید: `diagnose sys session list` expire بازنشانی می‌شود.

#### مثال متوسط — محاسبه‌ی MSS

لینک با MTU 1400:

``` text
MSS = 1400 - 20 - 20 = 1360
```

Clamp روی 1360؛ پس از آن HTTPS و دانلود بزرگ بدون Retransmission.

#### مثال متوسط — ping بزرگ

``` text
ping -f -l 1472 X -> "Packet needs to be fragmented but DF set"
ping -f -l 1372 X -> reply
```

Path MTU = 1400.

#### مثال سخت — دو علت هم‌زمان

DNS با پاسخ بزرگ (DNSSEC) + TCP/53 بسته + MTU کوچک. Capture: Query UDP، پاسخ با بیت TC (Truncated)؛ کلاینت با TCP تلاش می‌کند و SYN رد می‌شود. رفع: باز کردن TCP/53 و MSS Clamp. آزمون: `dig +tcp` و `dig +bufsize=1232`.

#### مثال سخت — Blackhole IPsec

Tunnel IPsec با MTU مؤثر 1427. ICMP Type 3 Code 4 توسط ISP/فایروال مسدود است. نشانه: دانلود فایل بزرگ گیر می‌کند؛ Capture: Retransmission بسته‌ی 1460 و نبود ICMP. رفع: MSS Clamp 1360 روی Policy Tunnel. تأیید: iperf و curl بدون Retransmission.

### Lab هدایت‌شده (اجرا نشده)

1. Path MTU را با ping اندازه بگیرید.
2. MSS Clamp را فعال و قبل/بعد را با Wireshark مقایسه کنید (`tcp.options.mss_val`).
3. Timeout را با اتصال بی‌کار آزمایش و Keepalive اضافه کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| قطع بعد ۱ ساعت | Timeout | Keepalive |
| ping ok، HTTPS نه | MTU | MSS Clamp |
| صفحه نیمه | Blackhole | Clamp/باز کردن ICMP |
| DNS گاهی | TC/TCP53 | باز کردن |

### جمع‌بندی

Timeout اتصال بی‌کار را حذف می‌کند؛ Keepalive لازم است. MSS = MTU − ۴۰. PMTUD به ICMP وابسته است؛ Blackhole با MSS Clamp حل می‌شود. Path MTU را با ping و DF بسنجید.

### تمرین و ارزیابی

**ت1.** (ساده) MSS برای MTU 1500؟ *(پاسخ: 11-5-ت1)*

**ت2.** (ساده) علامت Black-hole؟ *(پاسخ: 11-5-ت2)*

**ت3.** (متوسط) محاسبه برای MTU 1400. *(پاسخ: 11-5-ت3)*

**ت4.** (متوسط) چرا ICMP لازم است؟ *(پاسخ: 11-5-ت4)*

**ت5.** (سخت) SSH بعد ۵ دقیقه می‌پرد. *(پاسخ: 11-5-ت5)*

**ت6.** (سخت، طراحی) MSS روی IPsec و آزمون. *(پاسخ: 11-5-ت6)*

**Q1.** Quick quiz (English): What causes an MTU black hole? *(پاسخ: 11-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MTU | Maximum Transmission Unit | حداکثر اندازه‌ی بسته |
| MSS | Maximum Segment Size | حداکثر قطعه |

- *Lower the MSS on tunnels.* ← MSS را روی تونل‌ها کاهش دهید.

### کارت Lab

**کارت Lab:** MTU (اجرا نشده). **Evidence:** `03-ops/mtu-mss.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Session TTL
- RFC 1191
- RFC 4821

<a id="l-11-6"></a>

## درس 11-6 — کارگاه طراحی Policy، ۱۰ پرسش مسیر بسته و آزمون G4: پروژه‌ی حل‌شده‌ی کامل

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰ تا ۱۱-۷ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. یک طراحی Policy کامل را از نیاز تا آزمون انجام دهید.
2. ده پرسش مسیر بسته را برای هر Policy پاسخ دهید.
3. آزمون مثبت و منفی بنویسید و Evidence ثبت کنید.
4. خطاهای تزریقی (srcintf، Shadow، NAT) را با Lookup تشخیص دهید.
5. Rubric آزمون G4 را بشناسید.
6. گزارش طراحی را مستند کنید.

### چرا باید یاد بگیریم؟

تا وقتی خودتان یک مجموعه Policy را از ماتریس تا آزمون نسازید، مفهوم جا نمی‌افتد. G4 (Gate چهارم) همین مهارت را می‌سنجد: از «نیازهای کسب‌وکار» به «Policy قابل‌اثبات». مثل طراحی یک ساختمان و بعد بازدید با فهرست: برای هر در، قفل و کلید و آزمایش.

### ده پرسش مسیر بسته

برای هر جریان این ده پرسش را بنویسید:

1. Interface ورودی؟
2. Session موجود است؟
3. RPF مجاز است؟
4. DNAT دارد؟
5. Route/Interface خروجی؟
6. کدام Policy؟
7. UTM لازم است؟
8. SNAT دارد؟
9. Interface خروجی نهایی؟
10. مسیر برگشت چیست؟

### پروژه‌ی نمونه

شعبه با Zoneهای Users، Servers، DMZ، Guest، Mgmt و Internet.

**نیازها:**

- R1: Users به اینترنت (وب، DNS).
- R2: Users به ERP (HTTPS) و Fileserver (SMB).
- R3: Internet به وب DMZ (HTTPS).
- R4: Mgmt مدیریت دستگاه‌ها (SSH/HTTPS).
- R5: Guest فقط اینترنت.

**Policy:**

``` text
10 USERS -> INET   HTTP,HTTPS,DNS  accept nat log
20 USERS -> SRV    HTTPS,SMB       accept log
30 INET  -> DMZ    HTTPS (VIP-WEB) accept log
40 MGMT  -> any    SSH,HTTPS       accept log
50 GUEST -> INET   HTTP,HTTPS,DNS  accept nat log
90 any   -> any    ALL             deny log
```

**آزمون‌ها:**

| # | آزمون | انتظار |
|---|---|---|
| T1 | Users→اینترنت HTTPS | accept policy 10 |
| T2 | Users→ERP 443 | accept policy 20 |
| T3 | Guest→Servers 443 | deny policy 90 |
| T4 | Internet→DMZ 443 | accept policy 30 |
| T5 | Internet→Servers 445 | deny |
| T6 | Users→Mgmt 22 | deny |
| T7 | Mgmt→Servers 22 | accept policy 40 |

### روش آزمون

``` text
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.10 443 tcp port2     # policy 20
diagnose firewall iprope lookup 10.99.0.5 40000 10.20.0.10 443 tcp port4     # policy 90
```

و آزمون واقعی با `curl`/`nc`، سپس Log:

``` text
execute log filter field policyid 90
execute log display
```

### مثال‌های حل‌شده

#### مثال ساده — مسیر Users→ERP

ingress port2؛ Session جدید؛ RPF ok؛ بدون DNAT؛ Route port3؛ Policy 20؛ UTM (اختیاری)؛ بدون SNAT (داخلی به داخلی)؛ egress port3؛ برگشت از همان.

#### مثال متوسط — خطای تزریقی srcintf

Policy 20 با srcintf=port5 (اشتباه). سؤال ۶: Lookup ⇒ policy 90. رفع: srcintf=port2؛ آزمون T2 دوباره.

#### مثال متوسط — Shadow

Policy 15 `USERS -> any ALL accept` قبل از 20. T3 (Guest→Servers) هنوز رد می‌شود ولی T6 (Users→Mgmt) باز است: Policy 15 همه‌چیز را می‌گیرد. رفع: حذف/تنگ‌کردن 15 و ترتیب.

#### مثال سخت — طراحی کامل با گزارش

1. ماتریس ۶×۶.
2. ده Policy و ده آزمون مثبت/منفی.
3. اجرای آزمون‌ها و ثبت Evidence (Lookup+Log+زمان).
4. سه خطای تزریقی و رفع.
5. گزارش: نیاز ⇒ طراحی ⇒ آزمون ⇒ نتیجه ⇒ محدودیت‌ها.

**Rubric G4:** ماتریس ۲۰، Policy ۳۰، مسیر بسته ۲۰، آزمون ۲۰، گزارش ۱۰.

### Lab هدایت‌شده (اجرا نشده)

1. FortiGate (یا شبیه‌ساز) با Zoneها.
2. Policyها را بسازید و T1–T7 را اجرا کنید.
3. سه خطا را تزریق و با Lookup پیدا کنید.
4. گزارش بنویسید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| policy 90 به‌جای مجاز | srcintf/Address | تصحیح |
| ترافیک ممنوع باز است | Shadow | ترتیب |
| NAT نمی‌شود | nat disable | enable |
| آزمون منفی نبود | غفلت | افزودن |

### جمع‌بندی

از نیاز به ماتریس، از ماتریس به Policy، برای هر Policy ده پرسش مسیر بسته و آزمون مثبت/منفی با Lookup و Log. Shadow و srcintf نادرست خطاهای رایج‌اند.

### تمرین و ارزیابی

**ت1.** (ساده) Default Deny کجاست؟ *(پاسخ: 11-6-ت1)*

**ت2.** (ساده) DB از Internet؟ *(پاسخ: 11-6-ت2)*

**ت3.** (متوسط) چرا Deny صریح با وجود Implicit Deny؟ *(پاسخ: 11-6-ت3)*

**ت4.** (متوسط) NAT کجا؟ *(پاسخ: 11-6-ت4)*

**ت5.** (سخت) ۱۶ آزمون منفی را فهرست کنید. *(پاسخ: 11-6-ت5)*

**ت6.** (سخت، طراحی) بهبود طرح. *(پاسخ: 11-6-ت6)*

**Q1.** Quick quiz (English): Name one negative test for a DMZ policy. *(پاسخ: 11-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| G4 | Gate 4 | دروازه‌ی ۴ |

- *Test both allowed and denied flows.* ← هم جریان مجاز و هم ممنوع را آزمون کنید.

### کارت Lab

**کارت Lab:** کارگاه Policy G4 (اجرا نشده). **Evidence:** `03-ops/g4.md`.

### منابع

- درس‌های فصل ۱۱
- Fortinet FortiOS 7.0 Administration Guide: Firewall policies

## درس 11-7 — Stateful Inspection از درون: State Table، TCP State و Timeout

**فصل ۱۱ · درس افزوده (تکمیل ۱۱-۱) · پیش‌نیاز: ۱۱-۰، ۱۱-۱، فصل ۲ (TCP) · ≈ ۶ ساعت**

> **وضعیت:** مفهومی با مثال Linux conntrack؛ رفتار FortiGate در فصل ۱۲ و ۱۳ ادامه می‌یابد؛ Labها «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. State Table و ورودی‌های آن را بخوانید.
2. حالت‌های TCP و گذار بین آنها را بشناسید.
3. اعتبارسنجی بسته در برابر Session (Sequence Window) را توضیح دهید.
4. Timeout هر حالت و اثر آن را بدانید.
5. حمله‌ی SYN Flood و دفاع آن را شرح دهید.
6. رفتار UDP و ICMP را در فایروال Stateful بفهمید.

### چرا باید یاد بگیریم؟

دانستن اینکه Session چگونه ساخته و حذف می‌شود، رفتارهای عجیب را توضیح می‌دهد: چرا Policy را حذف کردم ولی اتصال ادامه دارد؟ چرا بسته‌ی ACK جعلی رد می‌شود؟ چرا سیل SYN دستگاه را از پا می‌اندازد؟ این درس «زیر کاپوت» فایروال Stateful است.

### State Table

هر ورودی معمولاً این اطلاعات را دارد:

- پروتکل، IP/پورت مبدأ و مقصد (و پس از NAT).
- حالت اتصال.
- Timeout باقی‌مانده.
- Policy که اجازه داده، Interface ورودی/خروجی.
- شمارنده‌های بایت/بسته.
- شماره‌های Sequence مورد انتظار (برای TCP).

### حالت‌های TCP

``` text
CLOSED -> SYN_SENT -> SYN_RECV -> ESTABLISHED -> FIN_WAIT -> TIME_WAIT -> CLOSED
```

| حالت | معنی | Timeout معمول |
|---|---|---|
| SYN_SENT | SYN فرستاده شد | کوتاه (ثانیه‌ها) |
| SYN_RECV | SYN-ACK دیده شد | کوتاه |
| ESTABLISHED | اتصال برقرار | طولانی (ساعت) |
| FIN_WAIT/CLOSE_WAIT | در حال بستن | کوتاه |
| TIME_WAIT | پایان اتصال | چند ثانیه |

### اعتبارسنجی بسته

فایروال علاوه بر آدرس/پورت، **Sequence/ACK Number** را با پنجره‌ی مورد انتظار می‌سنجد. بسته‌ای با Sequence خارج از پنجره (حمله‌ی تزریق/RST جعلی) رد می‌شود. این سطح دفاع را ACL ندارد.

### UDP و ICMP

UDP اتصال ندارد؛ فایروال برای اولین بسته یک Session «شبه‌حالتی» می‌سازد و پاسخ‌ها را در همان پنجره‌ی Timeout می‌پذیرد. ICMP Echo Reply فقط اگر Echo Request قبلی ثبت شده باشد پذیرفته می‌شود. ICMP خطا (Type 3، 11) با اتصال مرتبط مجاز است (Related).

### SYN Flood

مهاجم هزاران SYN با IP مبدأ جعلی می‌فرستد. فایروال برای هرکدام Session (SYN_RECV) می‌سازد و منتظر ACK می‌ماند؛ ACK هرگز نمی‌رسد. Table پر می‌شود و اتصال‌های واقعی رد می‌شود.

``` text
Table fill time = capacity / SYN rate
200000 / 20000 per s = 10 s
```

**دفاع‌ها:** DoS Policy (`tcp_syn_flood` با آستانه)، SYN Proxy/Cookie (فایروال به‌جای سرور Handshake را انجام می‌دهد و فقط پس از ACK درست Session می‌سازد)، Timeout کوتاه‌تر برای حالت نیمه‌باز، Rate Limit.

### مشاهده

``` text
diagnose sys session list
diagnose sys session stat
diagnose sys session filter dst 10.20.0.10
```

### مثال‌های حل‌شده

#### مثال ساده — بسته‌ی بدون Session

SYN-ACK بدون SYN: Session ندارد ⇒ Drop (Log: no session matched).

#### مثال متوسط — خواندن یک Session

``` text
proto=6 proto_state=01 duration=35 expire=3565 timeout=3600
org=5320/42  reply=48200/55
policy_id=20
```

`proto_state=01` یعنی ESTABLISHED (کد حالت)؛ expire/timeout نشان می‌دهد ۳۵ ثانیه از آخرین تازه‌سازی گذشته؛ بایت/بسته‌ی رفت (org) و برگشت (reply).

#### مثال متوسط — RST جعلی

مهاجم RST با Sequence تصادفی می‌فرستد تا اتصال را قطع کند. فایروال Sequence را با پنجره می‌سنجد؛ خارج از پنجره ⇒ رد. احتمال حدس درست پنجره‌ی 64K از 2^32: 

``` text
P(correct) ~ window / 2^32 = 65535 / 4294967296 ~ 0.0015 %
```

#### مثال سخت — SYN Flood

علامت: Session Table ۹۸٪ پر، کاربران قطع. `diagnose sys session stat`: بیشتر SYN_RECV از IPهای متنوع. اقدام: ۱) DoS Policy با `tcp_syn_flood` (مثلاً آستانه‌ی 5×Peak) روی Interface ورودی ۲) فعال‌سازی SYN Proxy (در صورت پشتیبانی) ۳) Block IPهای پرتکرار ۴) هماهنگی ISP. پس از رفع: Table به حد عادی؛ آزمون با ابزار تولید ترافیک در Lab ایزوله.

#### مثال سخت — Timeout ناسازگار

TIME_WAIT طولانی در Table باعث پر شدن پورت‌های NAT می‌شود (۶۴ هزار پورت برای یک IP). علامت: اتصال‌های جدید به یک مقصد شکست می‌خورند. رفع: IP Pool بزرگ‌تر، Timeout کوتاه‌تر برای TIME_WAIT، Keepalive/Connection pooling در برنامه.

### Lab هدایت‌شده (اجرا نشده)

1. یک اتصال بسازید و Session را بخوانید.
2. SYN-ACK جعلی (hping3) بفرستید و Drop را ببینید.
3. SYN Flood آزمایشی در Lab ایزوله و DoS Policy.
4. شمارنده‌ها را قبل/بعد مقایسه کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Drop ACK | بدون Session | مسیر نامتقارن؟ |
| Table پر | SYN Flood | DoS Policy |
| پورت NAT تمام | TIME_WAIT | IP Pool |
| قطع RST | Sequence | بررسی |

### جمع‌بندی

Session حالت، Timeout، Sequence و شمارنده دارد. فایروال Stateful بسته را با Session و پنجره‌ی Sequence می‌سنجد. SYN Flood Table را پر می‌کند؛ دفاع: DoS Policy و SYN Proxy.

### تمرین و ارزیابی

**ت1.** (ساده) تفاوت Stateless و Stateful را بگویید. *(پاسخ: 11-7-ت1)*

**ت2.** (ساده) 5-tuple شامل چه فیلدهایی است؟ *(پاسخ: 11-7-ت2)*

**ت3.** (متوسط) چرا پس از ایجاد Session، Policy برای هر بسته بازبینی نمی‌شود؟ *(پاسخ: 11-7-ت3)*

**ت4.** (متوسط) ۱۵۰۰ اتصال در ثانیه با عمر متوسط ۴۵ ثانیه چند Session هم‌زمان می‌سازد؟ *(پاسخ: 11-7-ت4)*

**ت5.** (سخت) SSH کاربر پس از ۲۰ دقیقه سکوت قطع می‌شود. سه راه‌حل با مزایا/ریسک بدهید. *(پاسخ: 11-7-ت5)*

**ت6.** (سخت، طراحی) برای سرور وب روی اینترنت، محافظت در برابر SYN Flood را از سه لایه (فایروال، سرور، شبکه) شرح دهید. *(پاسخ: 11-7-ت6)*

**م1.** Half-open Session چیست؟ *(پاسخ: 11-7-م1)*

**Q1.** Quick quiz (English): Why are return packets accepted by a stateful firewall without an explicit rule? *(پاسخ: 11-7-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Stateful | Stateful inspection | بازرسی با حافظه‌ی اتصال |
| 5-tuple | 5-tuple | پنج فیلد شناسایی Session |
| Half-open | Half-open connection | اتصال نیمه‌باز |
| ALG | Application Layer Gateway | دروازه‌ی لایه‌ی کاربرد |
| SYN cookie | SYN cookie | مکانیزم دفاع بدون ذخیره‌ی State |
| conntrack | Connection tracking | ردیابی اتصال در Linux |

- *A stateful firewall matches return traffic against existing sessions.* ← فایروال Stateful ترافیک برگشتی را با Sessionهای موجود تطبیق می‌دهد.
- *Session exhaustion is a common denial-of-service target.* ← پر شدن جدول Session هدف رایج DoS است.

### منابع

- NIST SP 800-41 Rev.1 — Guidelines on Firewalls and Firewall Policy (Stateful Inspection).
- RFC 9293 — Transmission Control Protocol (TCP).
- Linux kernel documentation: nf_conntrack sysctl.

## پاسخ‌های فصل 11

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 11-1

**11-1-ت1** — Stateful وضعیت اتصال را نگه می‌دارد و برگشت را خودکار می‌پذیرد.

**11-1-ت2** — برنامه، کاربر و محتوا.

**11-1-ت3** — هر کس با Source-port 443 می‌تواند وارد شود.

**11-1-ت4** — شبه‌Session با Timeout کوتاه.

**11-1-ت5** — ابتدا Stateful سپس بازرسی انتخابی و اندازه‌گیری.

**11-1-ت6** — Stateful+IPS انتخابی؛ معیار Throughput.

**11-1-Q1** — A session entry with addresses, ports, protocol, state and timeout.


### پاسخ‌های بازنویسی عمیق درس 11-2


### پاسخ‌های بازنویسی عمیق درس 11-2

**11-2-ت1** — هر ترافیک که صریحاً مجاز نشده رد می‌شود.

Default Deny یعنی هر ترافیکی که صراحتاً مجاز نشده رد می‌شود؛ پایه‌ی امنیت مبتنی بر «فهرست مجاز». در FortiGate Implicit Deny انتهای لیست است ولی Log ندارد؛ پس Deny صریح با Log هم بسازید تا Alert و ممیزی ممکن شود.

**11-2-ت2** — حداقل دسترسی لازم برای انجام کار.

Least Privilege یعنی هر کاربر/سیستم فقط حداقل دسترسی لازم برای کارش را دارد: مقصد، پورت و زمان مشخص به‌جای ALL. مثال: Users فقط HTTPS به SRV-APP نه به کل شبکه‌ی سرورها.

**11-2-ت3** — برای اینکه هر مسیر مجاز مستند، قابل ممیزی و قابل آزمون باشد.

ماتریس Zone-to-Zone نشان می‌دهد هر مسیر مجاز چیست؛ منبع Policyها، مرجع ممیزی و پایه‌ی آزمون مثبت/منفی است. بدون ماتریس Policyها ad-hoc می‌شوند و تعداد مسیرهای ناخواسته نامعلوم می‌ماند.

**11-2-ت4** — First Match؛ اگر عام بالا باشد خاص هرگز اجرا نمی‌شود.

چون First Match است: اولین Policy مطابق اعمال می‌شود. اگر Policy عام (مثلاً Users→all ALL) بالاتر باشد، Policyهای خاص هرگز اجرا نمی‌شوند؛ پس خاص بالا و عام پایین، و Deny صریح آخر.

**11-2-ت5** — Log، استخراج مقاصد/سرویس‌ها، Policy خاص، غیرفعال‌سازی ALL، مشاهده، حذف.

تنگ‌سازی Policy ALL: Log را روشن، ۱۴ تا ۳۰ روز جمع‌آوری، مقصد/سرویس‌های واقعی را استخراج، Policyهای خاص بساز و بالای ALL بگذار، ALL را غیرفعال و دو هفته مشاهده، سپس حذف با Backup و مستندسازی.

**11-2-ت6** — جدول ماتریس + ۹ آزمون مثبت و ۱۶ منفی.

ماتریس ۵ Zone: ۲۵ خانه که ۹ خانه مجاز (آزمون مثبت) و ۱۶ خانه ممنوع (آزمون منفی) است. برای هر خانه‌ی ممنوع باید Deny و Log دیده شود؛ این ۲۵ آزمون Evidence طراحی هستند.

**11-2-Q1** — Any traffic not explicitly allowed is blocked.

Default deny blocks everything not permitted. در عمل این یعنی هر سرویس جدید باید با Policy صریح و CHG وارد شود.

### پاسخ‌های بازنویسی عمیق درس 11-3


### پاسخ‌های بازنویسی عمیق درس 11-3

**11-3-ت1** — قبل؛ پس Policy با VIP یا آدرس بعد DNAT مطابقت می‌کند.

DNAT (VIP) قبل از Route و Policy انجام می‌شود؛ پس Policy باید با آدرس پس از DNAT یا شیء VIP نوشته شود نه آدرس عمومی. SNAT بعد از Policy اعمال می‌شود.

**11-3-ت2** — ترافیک به مقصد خود فایروال.

Local-in ترافیکی است که مقصدش خود فایروال است (Admin، BGP، IPsec، DNS). کنترل آن با Allowaccess روی Interface و Local-in policy است؛ Firewall Policy عادی آن را کنترل نمی‌کند.

**11-3-ت3** — Policy مقصد را با شیء VIP تطبیق می‌دهد.

Policy مقصد را با شیء VIP (که DNAT را تعریف می‌کند) تطبیق می‌دهد. اگر آدرس داخلی (10.30.0.10) را به‌جای VIP بنویسید، Policy تطبیق نمی‌کند و `Denied by forward policy check` می‌بینید.

**11-3-ت4** — بررسی اینکه Route به Source از همان Interface ورودی است.

RPF بررسی می‌کند Route به آدرس مبدأ از همان Interface ورودی است. اگر نیست (مثلاً Asymmetric یا Spoof) بسته Drop می‌شود: `reverse path check fail`. رفع: Route برگشت یا طراحی Symmetric.

**11-3-ت5** — Debug flow، allowaccess، Local-in، Trusted host.

Admin به https نمی‌رسد: Debug flow پیام `iprope_in_check() check failed` می‌دهد؛ بررسی allowaccess https روی Interface، Local-in policy و Trusted host؛ رفع و آزمون ورود.

**11-3-ت6** — Transit، Local-in، Local-out، ابزار اثبات هر مرحله.

نقشه‌ی Flow سازمان: Transit (Users→Internet)، Local-in (Admin/BGP/IPsec)، Local-out (NTP/FortiGuard/Syslog) و برای هر کدام ابزار اثبات: Debug flow، Sniffer، Session، Log.

**11-3-Q1** — Before; policies match the translated destination.

DNAT occurs before policy lookup; therefore policies must reference the VIP or translated destination.

### پاسخ‌های بازنویسی عمیق درس 11-4


### پاسخ‌های بازنویسی عمیق درس 11-4

**11-4-ت1** — آدرس/پورت بسته را بازنویسی می‌کند.

NAT آدرس و/یا پورت بسته را بازنویسی می‌کند (SNAT مبدأ، DNAT مقصد). NAT به‌تنهایی اجازه‌ی عبور نمی‌دهد؛ Policy تصمیم‌گیرنده است.

**11-4-ت2** — ترجمه‌ی چند Host با یک IP با استفاده از پورت‌های مختلف.

PAT چند Host داخلی را با یک IP عمومی ترجمه می‌کند و برای تمایز، پورت مبدأ را تغییر می‌دهد؛ ظرفیت تقریبی ۶۴ هزار پورت به‌ازای IP و مقصد.

**11-4-ت3** — NAT اجازه نمی‌دهد؛ Policy لازم است.

VIP فقط ترجمه‌ی مقصد را تعریف می‌کند؛ بدون Policy که اجازه‌ی عبور بدهد ترافیک Implicit Deny می‌شود. پس VIP + Policy (dst=VIP) هر دو لازم‌اند.

**11-4-ت4** — دسترسی داخلی به IP عمومی سرور داخلی.

Hairpin یعنی کاربر داخلی به IP عمومی سروری که داخل همان شبکه است وصل شود: بسته به فایروال می‌رسد و DNAT می‌شود ولی پاسخ سرور مستقیم به کاربر می‌رود و Session ناقص می‌ماند.

**11-4-ت5** — Split DNS یا Hairpin NAT؛ آزمون.

Hairpin را با Split DNS (DNS داخلی IP داخلی را بدهد، ترجیح) یا Hairpin NAT (SNAT برای این جریان) حل می‌کنند؛ آزمون: nslookup و باز شدن سایت از LAN.

**11-4-ت6** — سه VIP، سه Policy، آزمون منفی.

انتشار سه سرویس: سه VIP (با Port-forward حداقل)، سه Policy با dst=VIP و Service مشخص، Log All و آزمون منفی (پورت غیرمجاز رد شود).

**11-4-Q1** — A VIP only translates addresses; a firewall policy must still permit the traffic.

A VIP only translates addresses; a firewall policy is still needed to permit the traffic.

### پاسخ‌های بازنویسی عمیق درس 11-5


### پاسخ‌های بازنویسی عمیق درس 11-5

**11-5-ت1** — 1460.

MSS برای MTU 1500 برابر 1500−20−20=1460 است.

``` text
MSS = MTU - IP(20) - TCP(20) = 1460
```

**11-5-ت2** — Handshake ok، بسته‌ی بزرگ بی‌پاسخ.

علامت Black-hole: Handshake و بسته‌های کوچک (ping معمولی) موفق؛ بسته‌ی بزرگ بی‌پاسخ و Retransmission. علت: بسته‌ی بزرگ با DF از لینک کوچک‌تر عبور نمی‌کند و ICMP Frag-needed بسته شده است.

**11-5-ت3** — 1360.

MSS برای MTU 1400: 1400−40=1360.

``` text
MSS = 1400 - 40 = 1360
```

**11-5-ت4** — PMTUD برای اطلاع از MTU مسیر.

ICMP Fragmentation-needed (Type 3 Code 4) به فرستنده می‌گوید MTU مسیر کوچک‌تر است (PMTUD). اگر فایروال آن را ببندد، Black-hole می‌شود؛ پس این نوع ICMP را مجاز کنید.

**11-5-ت5** — Timeout/Keepalive.

SSH پس از ۵ دقیقه بیکاری قطع می‌شود چون Timeout Session کوتاه است؛ راه: افزایش `session-ttl` برای پورت 22 یا Keepalive در کلاینت، و آزمون ۳۰ دقیقه بیکاری.

**11-5-ت6** — اندازه‌گیری PMTU، clamp، دانلود ۱۰۰MB.

MSS روی IPsec: PMTU را با ping DF اندازه بگیرید (مثلاً 1400)، MSS=PMTU−40 با حاشیه (1360)، روی Policy تونل تنظیم و با دانلود ۱۰۰MB سه بار آزمون کنید.

**11-5-Q1** — Large DF packets are dropped while ICMP fragmentation-needed messages are blocked.

An MTU black hole happens when large DF packets are dropped while ICMP fragmentation-needed messages are blocked.

### پاسخ‌های بازنویسی عمیق درس 11-6


### پاسخ‌های بازنویسی عمیق درس 11-6

**11-6-ت1** — Policy 99 در انتها با Log.

Default Deny در Policy 99 در انتهای لیست با Log All قرار دارد؛ هر ترافیک مجازنشده Deny و ثبت می‌شود و برای Alert و ممیزی استفاده می‌شود.

**11-6-ت2** — هیچ مسیری ندارد؛ ممنوع.

DB از اینترنت هیچ مسیری ندارد: نه VIP، نه Policy؛ فقط APP→DB با Policy 60. آزمون منفی: اتصال از INET به SRV-DB رد و Log شود.

**11-6-ت3** — Implicit Log ندارد؛ صریح برای Alert.

Implicit Deny Log ندارد؛ Deny صریح با Log برای Alert و ممیزی لازم است (مثلاً تلاش DMZ→DB).

**11-6-ت4** — فقط Policy 10، 40، 80.

NAT فقط روی Policy 10 (SNAT کاربران)، 40 (DNAT/VIP وب) و 80 (SNAT خروج سرورها به Update) است؛ بقیه‌ی Policyها بدون NAT.

**11-6-ت5** — هر خانه‌ی «-» ماتریس: INET→SRV/USR/MGT، DMZ→USR/MGT، SRV→DMZ/USR/MGT، USR→MGT، MGT→INET و ... با نتیجه‌ی deny.

۱۶ آزمون منفی: هر خانه‌ی «-» ماتریس؛ مثلاً INET→SRV، INET→USR، INET→MGT، DMZ→USR، DMZ→MGT، SRV→DMZ، SRV→USR، SRV→MGT، USR→MGT، MGT→INET و ...؛ همه باید Deny و Log داشته باشند.

**11-6-ت6** — SSO/MFA برای Admin، Segment بیشتر DMZ، WAF (Needs-License).

بهبود طرح: SSO/MFA برای Admin، Segment بیشتر در DMZ، WAF برای وب (Needs-License)، Alert روی Deny بین لایه‌ها و بازبینی فصلی Policy.

**11-6-Q1** — Attempt a direct connection from the DMZ to the database and confirm it is denied.

A negative test: connect from the DMZ to the database and verify it is denied and logged.

### پاسخ‌های درس افزوده‌ی 11-0 (فصل 11)

**11-0-ت1** — Asset ارزش‌دار (DB)؛ Threat عامل آسیب (باج‌افزار)؛ Vulnerability ضعف قابل‌سوءاستفاده (سرور بدون Patch).

**11-0-ت2** — نقطه‌ای که سطح اعتماد عوض می‌شود (مثلاً Internet↔DMZ)؛ هر عبور باید با Policy و Log کنترل شود.

**11-0-ت3** — چون هر چه صریحاً مجاز نشده رد می‌شود؛ خطای فراموشی به باز بودن نمی‌انجامد.

**11-0-ت4** — مهاجمی که یک PC داخلی را بگیرد از مسیر East-West بدون عبور از لبه به سرورها می‌رسد؛ نیاز به Segmentation داخلی.

**11-0-ت5** — نمونه: Users→Internet: HTTP/HTTPS/DNS + UTM؛ Users→Servers: فقط HTTPS به اپ؛ Servers→DB: فقط TCP 1433؛ DMZ→Servers: فقط 8080 به اپ؛ DMZ→DB: ممنوع؛ Guest→Internet فقط وب/DNS؛ Guest→داخل ممنوع؛ Management فقط از شبکه‌ی مدیریت؛ هر چیز دیگر Implicit deny+Log. دلیل هر سطر: Least Privilege و جلوگیری از مسیر حمله.

**11-0-ت6** — Segmentation/Policy حداقلی، IPS/Inspection، MFA و Least Privilege هویتی، EDR روی میزبان، Monitoring/Alert (SIEM).

**11-0-م1** — Spoofing، Tampering، Repudiation، Information disclosure، Denial of service، Elevation of privilege.

**11-0-Q1** — Lateral movement is an attacker moving between internal systems after the first compromise; internal segmentation and least-privilege policies limit it.


### پاسخ‌های درس افزوده‌ی 11-7 (فصل 11)

**11-7-ت1** — Stateless هر بسته را مستقل می‌سنجد؛ Stateful ارتباط را در جدول State می‌شناسد و برگشت را با Session مطابقت می‌دهد.

**11-7-ت2** — IP مبدأ، پورت مبدأ، IP مقصد، پورت مقصد، پروتکل.

**11-7-ت3** — نتیجه‌ی ارزیابی در Session ذخیره می‌شود؛ بسته‌های بعدی با Session مطابقت می‌کنند و بررسی مجدد هزینه‌ی CPU دارد.

**11-7-ت4** — 1500 × 45 = 67,500 Session هم‌زمان (تقریبی).

**11-7-ت5** — (۱) Keepalive در SSH: ساده و بی‌ریسک. (۲) افزایش Timeout فقط برای سرویس SSH: جدول بزرگ‌تر. (۳) Timeout بلند برای همه: ریسک Exhaustion.

**11-7-ت6** — فایروال: DoS Policy/SYN cookie و Rate limit؛ سرور: SYN backlog/cookies؛ شبکه: Upstream scrubbing/ISP و ACL.

**11-7-م1** — اتصال که فقط SYN دیده شده و هنوز Handshake کامل نشده؛ Timeout کوتاه دارد.

**11-7-Q1** — Because the return packet matches an existing session entry created by the outbound packet.

# فصل 12 — FortiGate I: معماری، Interface، Zone، Object، Routing، Admin و Backup (معماری ۱)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۱ (G4)، فصل ۸ (CP1).
**اهداف:** اولین بوت و تأیید نسخه؛ Interface/VLAN؛ Zone و Object؛ Static Route/Default؛ Admin/RBAC و سخت‌سازی مدیریت؛ Backup/Restore. **هر کار هم با GUI و هم با CLI** آموزش داده می‌شود.
**هشدار نسخه و آزمایش:** Image `fortinet-7.0.3` **تا کنون بوت نشده**. منوها و دستورها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و در بوت اول باید مقایسه شوند. بوت اول فقط با **تأیید صریح شما** و در Lab ایزوله انجام می‌شود (ساعت Evaluation شروع می‌شود؛ طبق `phase0a/fortigate_eval_tracker.md` تاریخ را خودتان ثبت می‌کنید).
**معیار تسلط:** ساخت Baseline کامل (Interface/Zone/Object/Route/Admin) با GUI و CLI؛ اثبات با دستورهای get/show؛ بکاپ و بازیابی موفق.
**اشتباهات رایج:** قفل‌شدن با Trusted Host؛ `allowaccess` روی WAN؛ فراموشی بکاپ قبل از تغییر؛ حذف Interface دارای Policy.

**درس‌های فصل:**
- [درس 12-1 — معماری FortiGate، اولین بوت و تأیید نسخه](#l-12-1)
- [درس 12-2 — Interface، VLAN، Role و Administrative Access](#l-12-2)
- [درس 12-3 — Zone و Objectها: Address، Service، Group و استاندارد نام‌گذاری](#l-12-3)
- [درس 12-4 — Static Route، Default Route و Policy Route](#l-12-4)
- [درس 12-5 — Admin، RBAC و سخت‌سازی مدیریت](#l-12-5)
- [درس 12-6 — Backup/Restore، Firmware و Lifecycle](#l-12-6)
- [درس 12-7 — آزمون پایان فصل ۱۲ و تحلیل خطا (مدیریت قفل‌شده)](#l-12-7)

---

<a id="l-12-1"></a>

## درس 12-0 — Packet Flow در FortiGate: مسیر یک بسته از ورود تا خروج

**فصل ۱۲ · درس افزوده (پیش‌درس ۱۲-۱) · پیش‌نیاز: ۵-۰، ۱۱-۰، ۱۱-۷ · ≈ ۸ ساعت**

> **وضعیت (FortiOS 7.0.3، `Unverified` روی Image):** ترتیب مراحل بر پایه‌ی مستند رسمی «Debugging the packet flow» (Administration Guide 7.0) و مقاله‌های جامعه‌ی Fortinet است؛ جزئیات داخلی نسخه‌ی دقیق باید با `get system status` و Debug واقعی تأیید شود. Lab «اجرا نشده».

> **نکته‌ی علمی v4.0 — حدود اعتبار مدل:** جریان ده‌مرحله‌ای این درس یک «**مدل مفهومی ساده‌شده برای آموزش**» است، نه شرح ثابت و کامل همه‌ی حالات FortiOS. ترتیب دقیق داخلی به نسخه، نوع ترافیک (Transit، Local-in، Local-out)، وجود Session، Hardware Offload، IPsec، Proxy-based Inspection و تنظیمات خاص بستگی دارد. در منابع رسمی FortiOS 7.0 که برای این بازنگری قابل‌دسترسی بود، یک جدول رسمی «ترتیب کامل مراحل» **تأیید نشد**؛ آنچه با منبع رسمی تأیید شد: ترتیب Policy Route ← Routing Table (درس ۴-۴)، حالت‌های Inspection (Flow/Proxy) و ماهیت Local-out. هرجا در متن «مفهوم عمومی شبکه» و «رفتار مختص FortiOS» جدا شده، همین تفکیک مدنظر است.

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند برای یک بسته‌ی واقعی توضیح دهد:

1. از کدام Interface وارد شده، آیا Session موجودی دارد یا جدید است.
2. اگر VIP/DNAT هست، چه موقع و چگونه آدرس مقصد عوض می‌شود.
3. کدام **Route** انتخاب می‌شود و چرا (Route Lookup).
4. کدام **Policy** مطابق می‌شود و چه ترتیبی دارد (Policy Lookup).
5. چه تغییری روی آدرس‌ها اعمال می‌شود (SNAT/IP Pool).
6. چه **Security Profileهایی** اعمال می‌شوند و Session چگونه ساخته می‌شود.
7. چرا بسته عبور کرد یا Drop شد؛ و با Debug Flow آن را اثبات کند.

### ۲) پیش‌نیازها

مسیر عبور در روتر (۵-۰)، مدل تهدید و Stateful (۱۱-۰، ۱۱-۷)، NAT مقدماتی، مفهوم Zone و Interface.

### ۳) مفهوم پایه: چرا Packet Flow مهم‌ترین موضوع FortiGate است؟

وقتی کاربر می‌گوید «سایت باز نمی‌شود»، علت می‌تواند Route، Policy، NAT، Profile، DNS، MTU یا Session باشد. اگر ترتیب پردازش را ندانید، حدس می‌زنید؛ اگر بدانید، **هر مرحله را جداگانه با شواهد بررسی** و دقیقاً مرحله‌ای که بسته در آن رفتار غیرمنتظره دارد را پیدا می‌کنید. تمام عیب‌یابی در فصل ۱۴ و ۲۸ بر همین مسیر ساخته می‌شود.

> **تشبیه:** FortiGate مثل فرودگاه است: ورود (Interface)، بررسی بلیت قبلی (Session Lookup)، تعیین گیت (Route)، کنترل امنیتی (Policy + Profile)، تغییر مشخصات (NAT)، خروج. اگر مسافری در کنترل امنیتی مانده، به گیت دیگر رسیدن بی‌معنی است.

### ۴) توضیح عمیق فنی

#### ۴-۱) نمای کلی (ترتیب منطقی)

![شکل ۱: مراحل منطقی پردازش یک بسته‌ی عبوری (Transit) در FortiGate.](../figures/ch12-l0-fig1.svg)

*شکل ۱: ترتیب منطقی: Ingress → Session Lookup → DNAT → Route → Policy → SNAT/Profile → Egress.*

``` text
1. Ingress           : packet arrives on an interface (L2 checks, VLAN)
2. Anti-spoofing     : reverse path check (RPF)
3. Session lookup    : is it an existing session (fast path)?
                       YES -> apply session state (NAT, profile) and forward
                       NO  -> continue (new session)
4. DNAT / VIP        : destination NAT (before routing and policy)
5. Route lookup      : find egress interface and next-hop
6. Policy lookup     : match firewall policy (in order, first match)
7. Security profiles : AV / IPS / Web / App / SSL (if enabled in policy)
8. SNAT              : source NAT (policy NAT or IP pool)
9. Session create    : install session entry (with NAT info)
10. Egress           : ARP/next-hop MAC, send
```

**حدود اعتبار این ترتیب (مدل مفهومی ساده‌شده):**

| بخش | نوع دانش | توضیح |
|---|---|---|
| Route Lookup و Policy Lookup به‌عنوان دو تصمیم جدا | مفهوم عمومی فایروال/روتر | در هر فایروال Stateful تقریباً صادق است |
| DNAT پیش از Policy | مفهوم مشترک NAT/فایروال + رفتار FortiOS (VIP) | Policy مقصد post-DNAT را می‌بیند؛ جزئیات Central NAT متفاوت است |
| RPF قبل از Session | رفتار FortiOS | تنظیم‌پذیر؛ حالت Strict/Loose و `asymroute` اثر دارند |
| ترتیب Session Lookup نسبت به سایر مراحل | رفتار FortiOS + Offload | بسته‌ی Offload شده ممکن است اصلاً به CPU نرسد |
| Security Profile پس از Policy | رفتار FortiOS | در Proxy mode بازرسی روی جریان بازسازی‌شده انجام می‌شود |
| SNAT پس از Policy | رفتار FortiOS | NAT خروجی با Central NAT یا IP Pool متفاوت پیکربندی می‌شود |

این مدل برای **ترافیک عبوری (Transit)** است. ترافیک Local-in/Local-out و ترافیک IPsec مسیر متفاوت دارند (۴-۸ و ۱۲-۸).

دو نکته‌ی فراتر از جدول:

- **DNAT قبل از Route و Policy** اتفاق می‌افتد؛ بنابراین Policy باید بر اساس آدرس **مقصد بعد از DNAT** (آدرس داخلی) تطبیق شود، نه IP عمومی VIP. در مستند Fortinet و مقاله‌ی Central NAT این ترتیب «ingress → session lookup → DNAT → route → policy → SNAT» آمده است.
- **SNAT بعد از Policy** است؛ Policy مبدأ اصلی (قبل از SNAT) را می‌بیند.

#### ۴-۲) Ingress و Anti-spoofing (RPF)

FortiGate هر بسته‌ی ورودی را با **Reverse Path Forwarding (RPF)** می‌سنجد: آیا بهترین مسیر به آدرس **مبدأ** از همان Interfaceی که بسته آمده می‌گذرد؟ اگر نه، به‌عنوان جعل/Asymmetric Drop می‌شود (Debug: `reverse path check fail, drop`). این یکی از شایع‌ترین دلایل Drop در شبکه‌های نامتقارن یا با Route ناقص است (فصل ۱۰-۶، ۲۳).

#### ۴-۳) Session Lookup — ترافیک جدید در برابر ترافیک دارای Session

- **ترافیک جدید (بسته‌ی اول):** Session پیدا نمی‌شود؛ Route Lookup، Policy Lookup و (در صورت نیاز) NAT اجرا می‌شود و نتیجه در Session ثبت می‌گردد.
- **ترافیک دارای Session:** بسته‌های بعدی هر دو جهت (Original و Reply) با ورودی Session تطبیق می‌خورند و معمولاً **Policy Lookup کامل دوباره انجام نمی‌شود**؛ NAT و وضعیت ذخیره‌شده در Session اعمال می‌شود. پاسخ‌های برگشتی بدون Policy جداگانه عبور می‌کنند چون Session دارند.

**چرا نمی‌توان گفت «Session موجود هرگز Route یا Policy را دوباره بررسی نمی‌کند»؟** چون رفتار به عوامل زیر وابسته است و تعمیم مطلق نادرست است:

1. **تغییر Route:** Session معمولاً به Interface/Gateway ثبت‌شده وابسته می‌ماند، ولی FortiOS گزینه‌هایی برای بازبینی مسیر Session دارد (مثل تنظیمات `snat-route-change`، `session-route-check`/رفتار Route-change؛ **نام و رفتار دقیق وابسته به نسخه‌اند و در منابع این بازنگری تأیید نشدند → نیازمند بررسی در مستند نسخه‌ی هدف**).
2. **تغییر Policy:** تغییر یا حذف Policy ممکن است Sessionهای موجود را فوراً قطع نکند، ولی در بعضی نسخه‌ها/حالت‌ها (مثلاً Proxy-based، یا Policyهایی که Session را با Policy ID مرتبط می‌کنند، یا Session Helper/UTM) Session دوباره ارزیابی یا بازنشانی می‌شود. این رفتار را بدون مستند نسخه قطعی ننویسید.
3. **Offload (NPU):** Session Offload شده در سخت‌افزار پردازش می‌شود و تغییرات نرم‌افزاری ممکن است نیاز به پاک‌کردن/بازسازی Session داشته باشد.
4. **انقضای Session:** Timeout هر پروتکل، Session را پایان می‌دهد و بسته‌ی بعدی دوباره «جدید» محسوب می‌شود.

**جمع‌بندی آموزشی (قابل‌اتکا):** «Session موجود *معمولاً* بدون ارزیابی مجدد Policy ادامه می‌یابد؛ بنابراین بعد از تغییر Route/Policy، نتیجه را با **اتصال جدید** آزمون کنید و برای Session قدیمی وضعیت (`diagnose sys session list`) را ببینید؛ پاک‌کردن Session (فقط با فیلتر و Change) راه تضمین ارزیابی دوباره است.» جزئیات وابسته به نسخه: نیازمند بررسی.

#### ۴-۴) Route Lookup

انتخاب Interface خروجی و Next-hop با همان قواعد (LPM، Distance، Priority، Policy Route). در FortiOS: ترتیب بررسی (مستند رسمی FortiOS 7.0، بخش Policy routes — تأییدشده): فایروال از بالای فهرست Policy Route شروع می‌کند؛ اگر Policy Route تطبیق نخورد یا Interface/Gateway آن کامل نباشد یا مسیر فعالی نیابد، **Routing Table** بررسی می‌شود. نقش **SD-WAN Rule** (Service) نیز در همین مرحله‌ی انتخاب مسیر است، ولی ترتیب دقیق آن نسبت به Policy Route در نسخه‌ی هدف و **Route Cache/FIB** در منابع این بازنگری تأیید نشد → نیازمند بررسی. نکته‌ی تأییدشده: برای ترافیک برگشتی، Policy Route بررسی نمی‌شود، و رفتار خروج برگشتی به تنظیم Auxiliary Session بستگی دارد. (جزئیات SD-WAN: فصل ۲۱.) **Zone** و Interface خروجی همین‌جا مشخص می‌شود.

> تفاوت مهم: **Routing می‌گوید بسته از کجا برود؛ Policy می‌گوید اجازه‌ی عبور دارد یا نه.** هر دو باید درست باشند؛ Route درست و Policy غایب = Drop؛ Policy درست و Route غلط = Drop یا مسیر اشتباه.

#### ۴-۵) Policy Lookup

بررسی Policyها **از بالا به پایین؛ اولین تطبیق برنده است (First Match)**. فیلدهای تطبیق: Incoming Interface/Zone، Outgoing Interface/Zone، Source (آدرس/کاربر/دستگاه)، Destination، Service، Schedule. اگر هیچ Policy مطابق نباشد، **Implicit Deny** (Policy شناسه‌ی 0) و ثبت `Denied by forward policy check (policy 0)`.

#### ۴-۶) Security Profile Inspection

پس از تطبیق Policy، اگر Profileها وصل باشند (AV، IPS، Web Filter، Application Control، SSL Inspection ...)، بسته/جریان بر اساس **Inspection Mode (Flow یا Proxy)** بازرسی می‌شود. در 7.0 حالت بازرسی در **هر Policy** تنظیم می‌شود (`set inspection-mode flow|proxy`). جزئیات در فصل ۱۶.

#### ۴-۷) NAT و ساخت Session

اگر Policy NAT فعال باشد، آدرس مبدأ به IP خروجی Interface یا IP Pool تغییر می‌کند و در Session ذخیره می‌شود تا بسته‌های بعدی و پاسخ بدون پردازش مجدد ترجمه شوند. پس هر Session دو جهت دارد: Original و Reply.

#### ۴-۸) سه حالت: Transit، Local-in و Local-out

| حالت | تعریف | سازوکار اصلی | نکته |
|---|---|---|---|
| **Transit (Forward)** | مبدأ و مقصد هیچ‌کدام خود FortiGate نیستند | Route + **Firewall Policy** (Forward) | مدل ۱۰مرحله‌ای بالا |
| **Local-in** | مقصد = خود FortiGate (SSH/HTTPS/ping/IKE/…) | `allowaccess` روی Interface + **Local-in Policy** (+ DoS Policy پیش از آن) | Firewall Policy عادی اعمال نمی‌شود |
| **Local-out** | مبدأ = خود FortiGate (DNS، FortiGuard، Syslog، NTP) | Routing Table (پیش‌فرض)، یا SD-WAN/Interface دستی | مستند رسمی 7.0: Local out «relies on routing table lookups» مگر SD-WAN/Interface دستی انتخاب شود (تأییدشده) |

سوءبرداشت رایج: «همه‌ی ترافیک مرتبط با فایروال را با Forward Policy کنترل می‌کنم.» ← ترافیک مدیریتی به خود دستگاه با Local-in و `allowaccess` کنترل می‌شود. جزئیات: درس ۱۲-۸.

#### ۴-۹) VIP/DNAT — حداقل لازم برای فهم Flow

- در مدل مفهومی، **مقصد بسته پیش از Route/Policy ترجمه می‌شود**؛ بنابراین Route Lookup بر مقصد جدید (داخلی) انجام می‌شود و Policy باید به **شیء VIP یا مقصد post-DNAT طبق نسخه/حالت** اشاره کند (در FortiOS معمولاً شیء VIP در `dstaddr`؛ در Central NAT رفتار متفاوت است — درس ۱۳-۳).
- Policy بدون Policy مقابل VIP کار نمی‌کند؛ VIP فقط «ترجمه» است نه «اجازه».
- پاسخ سرور داخلی با Session برعکس ترجمه می‌شود (Reverse DNAT/SNAT).

#### ۴-۱۰) Hardware Acceleration و رابطه‌اش با Flow

Session می‌تواند به NPU **Offload** شود؛ در این حالت بسته‌های بعدی ممکن است از مسیر نرم‌افزاری (CPU) نگذرند. پیامدها: ۱) Sniffer/Debug Flow همه‌ی بسته‌ها را نشان نمی‌دهد؛ ۲) تغییرات Policy/Route ممکن است نیاز به پاک‌کردن Session داشته باشد؛ ۳) Offload با بعضی Security Profileها (به‌ویژه Proxy-based) یا ویژگی‌ها ممکن نیست. شرایط دقیق Offload وابسته به مدل/NP/نسخه است (درس ۱۲-۹)؛ در منابع این بازنگری فقط جزئیات IPsec Offload تأیید شد (`npu-offload` در Phase1؛ `auto-asic-offload disable` در Policy ترافیک را Offload نمی‌کند).

### ۵) مثال حل‌شده: Debug Flow

**توپولوژی:** LAN (port2، 192.168.10.0/24) و WAN (port1). کلاینت 192.168.10.5 به 8.8.8.8 پورت 443 وصل می‌شود. Policy 10: LAN→WAN با NAT.

``` text
FGT # diagnose debug reset
FGT # diagnose debug flow filter addr 8.8.8.8
FGT # diagnose debug flow filter port 443
FGT # diagnose debug flow show function-name enable
FGT # diagnose debug flow trace start 10
FGT # diagnose debug enable
```

خروجی نمونه‌ی **مفهومی** (ساده‌شده؛ فرمت واقعی در نسخه‌ی شما را با Lab تأیید کنید):

``` text
id=20085 trace_id=1 func=print_pkt_detail msg="vd-root:0 received a packet(proto=6, 192.168.10.5:51200->8.8.8.8:443) from port2. flag [S], seq ..."
id=20085 trace_id=1 func=init_ip_session_common msg="allocate a new session-00004a2b"
id=20085 trace_id=1 func=vf_ip_route_input_common msg="find a route: flag=00000000 gw-203.0.113.1 via port1"
id=20085 trace_id=1 func=fw_forward_handler msg="Allowed by Policy-10: SNAT"
id=20085 trace_id=1 func=__ip_session_run_tuple msg="SNAT 192.168.10.5->203.0.113.10:51200"
```

**تحلیل خط‌به‌خط:**

| خط | معنی | مرحله |
|---|---|---|
| received a packet ... from port2 | ورود، جدید است (flag S) | Ingress |
| allocate a new session | Session موجود نبود | Session lookup |
| find a route ... via port1 | Route انتخاب شد | Route lookup |
| Allowed by Policy-10 | Policy مطابق | Policy lookup |
| SNAT ... | ترجمه‌ی مبدأ | NAT |

``` text
FGT # diagnose debug disable
FGT # diagnose debug flow trace stop
FGT # diagnose debug reset
```

> **هشدار:** Debug Flow را حتماً پس از کار Disable/Reset کنید. در مستند رسمی آمده که برای مشاهده‌ی Packet Flow روی پلتفرم‌های دارای **NP4/NP6** باید Offload غیرفعال شود (`diagnose npu fastpath disable`) و نسخه‌ی 7.0.12 اضافه می‌کند مانیتور Flow برای ترافیک Offloadشده در NP6/NP7 کار نمی‌کند (درس ۱۲-۹). FortiGate-VM معمولاً NP ندارد (`Unverified`).

**مثال متوسط (Drop):**

``` text
... msg="Denied by forward policy check (policy 0)"
```

یعنی هیچ Policy مطابق نبود. علت‌های رایج: Interface/Zone اشتباه، Service نادرست، Source/Destination اشتباه، یا ترتیب Policyها.

**مثال سخت (RPF):**

``` text
... msg="reverse path check fail, drop"
```

یعنی بهترین مسیر به مبدأ از Interface ورودی نمی‌گذرد: Route ناقص/Asymmetric. بررسی: `get router info routing-table details <src-ip>`.

### ۶) طراحی و تصمیم‌گیری

| تصمیم | معیار |
|---|---|
| Policy بر اساس Interface یا Zone | Zone برای سادگی چند Interface؛ Interface برای دقت |
| DNAT با VIP | Policy مقصد = IP داخلی (post-DNAT) |
| Policy NAT یا Central NAT | Central NAT برای سیاست NAT متمرکز؛ توجه به ترتیب |
| Inspection Mode per policy | Flow (سبک‌تر) / Proxy (قابلیت بیشتر) طبق نیاز |

### ۷) پیاده‌سازی: GUI و CLI

**GUI:**

1. Policy & Objects → Firewall Policy: ترتیب Policyها را ببینید (ستون ID، Hit Count).
2. Log & Report → Forward Traffic: فیلتر بر اساس Source/Destination برای دیدن Action و Policy ID.
3. Network → Diagnostics → Packet Capture: Capture با Filter.
4. (در 7.0) Policy → ستون Bytes/Sessions برای Hit.

**CLI:**

``` text
get router info routing-table details 8.8.8.8
get router info routing-table all
diagnose firewall iprope lookup 192.168.10.5 51200 8.8.8.8 443 tcp port2
diagnose sys session filter dst 8.8.8.8
diagnose sys session list
diagnose sniffer packet any "host 8.8.8.8 and port 443" 4 20 l
```

- `iprope lookup`: شبیه‌سازی Policy Lookup (دقت فرمت `Unverified`).
- `session list`: ورودی Session شامل Policy و NAT است.

### ۸) Troubleshooting (یک الگوی ثابت)

1. Ingress: بسته در Sniffer روی Interface ورودی دیده می‌شود؟
2. RPF: خطای reverse path check دارد؟
3. Session: جدید است یا موجود؟
4. Route: Interface خروجی درست است؟
5. Policy: کدام Policy؟ (ID)
6. NAT/Profile: ترجمه و Profile چیست؟
7. Egress: بسته در Interface خروجی دیده می‌شود؟ پاسخ برمی‌گردد؟

اگر بسته در مرحله‌ی N ناپدید شود، علت در همان مرحله است. این «روش تقسیم مسیر» تمام عیب‌یابی بعدی است.

### ۹) نکات امنیتی

- Debug Flow بار CPU دارد و ممکن است اطلاعات حساس نشان دهد؛ با Filter دقیق و زمان کوتاه.
- Policy با Implicit Deny و Log باعث می‌شود تلاش‌های ناموفق دیده شوند؛ Logging Policy 0 را فعال کنید.
- DNAT/VIP بدون Policy دقیق، سرویس داخلی را برای همه باز می‌کند.

### ۱۰) جمع‌بندی مفهومی

- ترتیب: Ingress → RPF → Session → DNAT → Route → Policy → Profile → SNAT → Session → Egress.
- DNAT قبل از Route/Policy؛ SNAT بعد از Policy.
- Session موجود *معمولاً* بدون ارزیابی مجدد Policy ادامه می‌یابد؛ اما این یک قاعده‌ی مطلق نیست و به نسخه، Offload، Proxy mode و تنظیمات Route-change بستگی دارد (۴-۳).
- Transit، Local-in و Local-out سه مسیر متفاوت‌اند (۴-۸).
- Routing و Policy دو تصمیم جدا هستند؛ هر دو لازم‌اند.
- Debug Flow + Session + Routing Table سه شاهد اصلی‌اند.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) ترتیب مراحل پردازش یک بسته‌ی جدید را بنویسید. *(پاسخ: 12-0-ت1)*

**ت2.** (ساده) Implicit Deny چه شناسه‌ای دارد و چه Log می‌دهد؟ *(پاسخ: 12-0-ت2)*

**ت3.** (متوسط) VIP پورت 443 را به 10.1.1.10 می‌برد. Policy باید مقصد را چه بگذارد؟ چرا؟ *(پاسخ: 12-0-ت3)*

**ت4.** (متوسط) چرا Route درست و Policy غایب باعث Drop می‌شود؟ *(پاسخ: 12-0-ت4)*

**ت5.** (سخت) بسته‌ای در Sniffer روی port2 دیده می‌شود ولی روی port1 نه. فهرست علت‌ها را به ترتیب بررسی بنویسید. *(پاسخ: 12-0-ت5)*

**ت6.** (سخت، طراحی) Debug Flow نشان می‌دهد `reverse path check fail`. سه علت و روش اثبات هر کدام را بنویسید. *(پاسخ: 12-0-ت6)*

**م1.** SNAT بعد از کدام مرحله است؟ *(پاسخ: 12-0-م1)*

**Q1.** Quick quiz (English): Does a reply packet of an existing session go through policy lookup again? *(پاسخ: 12-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس برای ضد جعل |
| DNAT | Destination NAT | ترجمه‌ی مقصد |
| SNAT | Source NAT | ترجمه‌ی مبدأ |
| VIP | Virtual IP | آدرس مجازی برای DNAT |
| Policy ID 0 | Implicit deny | Policy ضمنی رد |
| Debug flow | Packet flow debug | ردگیری گام‌به‌گام بسته |

- *In the simplified model the policy is evaluated for the first packet of a session; real behavior can vary by version and offload.* ← در مدل ساده، Policy برای بسته‌ی اول Session ارزیابی می‌شود؛ رفتار واقعی بسته به نسخه و Offload می‌تواند متفاوت باشد.
- *Check routing and policy as two separate decisions.* ← Routing و Policy را دو تصمیم جدا بررسی کنید.

### ۱۳) منابع

- Fortinet Docs: [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow) (FortiOS 7.0 Administration Guide).
- Fortinet Community: «Central NAT: Packet processing, troubleshooting steps and traffic flow» و «FortiGate Debug Flow Functions» (غیررسمی؛ `Unverified` تا تأیید روی Lab).
- Fortinet Docs: FortiOS 7.0 CLI Reference (`diagnose debug flow`).

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: Packet Flow در FortiGate — مسیر یک بسته از ورود تا خروج

#### چرا باید یاد بگیریم؟

بدون نقشه‌ی ذهنی از مسیر بسته، هر عیب‌یابی حدس است. اگر بدانید بسته ابتدا Anti-spoofing (RPF) می‌شود، سپس DNAT، سپس Routing، سپس Policy و بعد SNAT، هر خطایی را می‌توانید به یکی از این ایستگاه‌ها نسبت دهید.

#### ایستگاه‌ها (مسیر Transit)

``` text
1 Ingress interface        (link, VLAN)
2 Session lookup           (existing session? -> fast path)
3 DoS policy / anomaly
4 RPF (reverse path check)
5 DNAT (VIP) / pre-routing
6 Routing decision (route lookup, PBR first)
7 Firewall policy lookup
8 UTM / inspection
9 SNAT (policy NAT / IP pool)
10 Egress interface
```

#### مثال ساده — دنبال‌کردن SYN

Users (10.10.0.5) به 198.51.100.8:443: ورودی port2 ⇒ Session جدید ⇒ RPF موفق ⇒ Route به port1 ⇒ Policy 30 ⇒ SNAT ⇒ خروج.

#### مثال متوسط — جای هر خطا

| علامت Debug | ایستگاه |
|---|---|
| reverse path check fail | RPF |
| no route to host | Routing |
| Denied by forward policy check | Policy |
| no session matched | Session/نامتقارن |

#### مثال سخت — VIP و Policy

با VIP، DNAT قبل از Routing و Policy انجام می‌شود؛ پس Policy باید به **IP عمومی (VIP)** اشاره کند نه IP داخلی؛ Route باید به IP ترجمه‌شده نگاه کند.

#### Lab

برای ۳ جریان (Users→Internet، Internet→VIP، Users→Mgmt) ایستگاه‌ها را فهرست کنید.

#### عیب‌یابی

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| RPF | Route | تصحیح |
| Policy 0 | Interface/Address | تصحیح |
| نامتقارن | مسیر | طراحی |

#### پرسش‌ها با پاسخ

**۱. DNAT قبل یا بعد Route؟** قبل.
**۲. SNAT؟** بعد از Policy.
**۳. PBR؟** پیش از Routing عادی.

#### English Corner

- *Destination NAT happens before the routing decision; source NAT happens after policy.*
- Q: At which stage does the reverse path check occur?

## درس 12-1 — معماری FortiGate، اولین بوت و تأیید نسخه

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۰، ۱۱-۳ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. اجزای معماری FortiGate (FortiOS، CPU، NPU، Management plane، Data plane، VDOM) را توضیح دهید.
2. مراحل اولین بوت امن (کنسول، IP پیش‌فرض، رمز، Timezone/NTP، Hostname) را اجرا کنید.
3. نسخه، Serial، لایسنس و وضعیت HA را از `get system status` بخوانید.
4. تطبیق نسخه‌ی دستگاه با مستندات و دوره را بسنجید.
5. روش‌های دسترسی (Console، SSH، HTTPS، API) و ریسک هرکدام را بشناسید.
6. برگه‌ی اولین بوت را بنویسید و Backup اولیه بگیرید.

### چرا باید یاد بگیریم؟

وقتی با یک دستگاه ناآشنا شروع می‌کنید، اولین سؤال‌ها این است: «چه سیستم‌عاملی؟ چه نسخه‌ای؟ لایسنس دارد؟ چه چیزی را می‌توانم تنظیم کنم؟». مثل رانندگی با ماشین جدید: قبل از حرکت باید بدانید دنده، فرمان و ترمز کجاست. در FortiGate بسیاری از رفتارها و منوها به **نسخه‌ی FortiOS** بستگی دارد. اگر مستند 7.2 را بخوانید و دستگاه 7.0 باشد، دستور وجود ندارد. و اگر اولین بوت را بی‌دقت انجام دهید (رمز پیش‌فرض، مدیریت باز روی WAN)، دستگاه از همان ساعت اول آسیب‌پذیر است. این درس پایه‌ی همه‌ی فصل‌های FortiGate است.

### معماری

| جزء | نقش |
|---|---|
| FortiOS | سیستم‌عامل اختصاصی؛ CLI، GUI، API |
| CPU | پردازش عمومی، UTM (Proxy)، Control Plane |
| NPU/SPU | تراشه‌ی شتاب‌دهنده‌ی ترافیک (Session Offload، IPsec، NAT) |
| Management plane | ورود ادمین (CLI، GUI، REST API)، تنظیمات |
| Data plane | عبور و بازرسی ترافیک |
| VDOM | دامنه‌ی مجازی؛ پیش‌فرض یک VDOM به نام root |
| FortiGuard | سرویس ابری امضاها (AV، IPS، Web) |

**مدل‌ها:** سخت‌افزاری (شاخص‌ها: Throughput، Session، IPsec، SSL Inspection) و **VM** (FortiGate-VM). در Lab ما VM است؛ NPU ندارد و بسیاری از قابلیت‌ها به لایسنس وابسته‌اند.

### دسترسی‌ها

| روش | مناسب برای | نکته امنیتی |
|---|---|---|
| Console (RJ45/USB/سریال) | اولین بوت، بازیابی | فیزیکی؛ امن‌ترین |
| SSH | مدیریت روزمره | Trusted Host و کلید |
| HTTPS (GUI) | مدیریت گرافیکی | فقط از Mgmt؛ TLS قوی |
| REST API | اتوماسیون | توکن، Trusted Host |
| HTTP/Telnet | — | **غیرفعال** |

IP پیش‌فرض مدیریت بسیاری از مدل‌ها 192.168.1.99/24 روی `mgmt`/`internal` و کاربر `admin` با رمز خالی است (طبق مدل). **باید فوراً تغییر کنید.**

### اولین بوت امن (برگه)

1. اتصال Console؛ ورود `admin` (رمز خالی) و تغییر فوری رمز (بلند و منحصر‌به‌فرد).
2. `get system status` برای نسخه/Serial/لایسنس.
3. Hostname، Timezone، NTP.
4. تنظیم Interface مدیریتی و `allowaccess` فقط لازم.
5. `trusthost` برای ادمین.
6. غیرفعال‌سازی سرویس‌های ناامن.
7. Backup اولیه (Config خام).
8. ثبت Evidence: خروجی `get system status` با زمان.

### دستورها (Unverified)

``` text
get system status
config system global
 set hostname "FGT-HQ-01"
 set timezone 26
 set admintimeout 10
end
config system ntp
 set ntpsync enable
 set server "10.50.0.20"
end
config system admin
 edit "admin"
  set password ***
 next
end
config system interface
 edit "mgmt"
  set ip 10.50.0.1 255.255.255.0
  set allowaccess ping https ssh
 next
end
execute backup config tftp initial.conf 10.50.0.30
```

(کد Timezone را از `set timezone ?` در همان نسخه بخوانید.)

### خواندن `get system status`

``` text
Version: FortiGate-VM64 v7.0.3,build...,(GA)
Virus-DB: ...
Serial-Number: FGVM...
License Status: Valid/Trial
Hostname: FGT-HQ-01
Operation Mode: NAT
Current virtual domain: root
Virtual domain configuration: disable
Current HA mode: standalone
System time: ...
```

نکات: `Operation Mode` (NAT/Transparent)، `Virtual domain configuration` (disable/multi-vdom)، `Current HA mode` و `System time` (برای Log و گواهی‌ها).

### مثال‌های حل‌شده

#### مثال ساده — کدام نسخه؟

`get system status` ⇒ v7.0.3. مستندات 7.0 را بخوانید. اگر مستند 7.2 را دارید، منوها و دستورها ممکن است فرق کنند؛ تفاوت را در Release Notes بسنجید.

#### مثال متوسط — اولین بوت

۱) Console، رمز admin تغییر ۲) Hostname FGT-HQ-01 ۳) NTP ۴) `mgmt` با HTTPS/SSH/ping ۵) Backup ۶) Evidence. زمان: ≈ ۳۰ دقیقه. اگر ساعت اشتباه باشد، Log و گواهی‌ها (TLS، Kerberos، MFA) دچار مشکل می‌شود.

#### مثال متوسط — «ویژگی در GUI نیست»

1. لایسنس/مدل؟ (دیتاشیت)
2. Feature Visibility (System ← Feature Visibility) خاموش؟
3. نسخه‌ی FortiOS؟ (Release Notes)
4. حالت VDOM/Operation mode؟
5. دسترسی ادمین (Profile)؟

#### مثال سخت — نسخه‌ی دستگاه v7.2 است

دوره بر پایه‌ی 7.0.3 است. اقدام: ۱) مفاهیم یکسان‌اند (Policy، NAT، VPN) ۲) برای هر دستور `?` را در CLI بزنید و مستند 7.2 را بخوانید ۳) تفاوت Syntax را در یادداشت ثبت کنید ۴) ارتقا/کاهش نسخه فقط با مسیر رسمی ۵) دستورهای «Unverified» را با نسخه‌ی واقعی راستی‌آزمایی کنید.

#### مثال سخت — مدیریت باز روی WAN

پس از نصب، GUI از اینترنت در دسترس است. ریسک: Brute-force و آسیب‌پذیری. رفع: حذف `https/ssh` از `allowaccess` WAN؛ `trusthost`؛ Local-in Policy؛ بررسی Log ورود ناموفق. شاهد: اسکن پورت از بیرون (Lab) و `show system interface`.

### Lab هدایت‌شده (اجرا نشده)

1. FortiGate VM بوت‌شده؛ Console.
2. اجرای برگه‌ی اولین بوت و ثبت Evidence.
3. تغییر عمدی `allowaccess` و بازگردانی.
4. مقایسه‌ی `get system status` قبل/بعد.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| GUI باز نمی‌شود | allowaccess/IP | Console |
| ویژگی نیست | لایسنس/Visibility | بررسی |
| Log زمان اشتباه | NTP | تنظیم |
| دستور خطا | نسخه | `?` و مستند |

### جمع‌بندی

FortiGate از FortiOS، CPU و NPU ساخته شده؛ نسخه رفتار را تعیین می‌کند. اولین بوت: Console، رمز، Hostname، NTP، Mgmt محدود، Backup و Evidence. نسخه و لایسنس را از `get system status` بخوانید.

### تمرین و ارزیابی

**ت1.** (ساده) کدام دستور نسخه را نشان می‌دهد؟ *(پاسخ: 12-1-ت1)*

**ت2.** (ساده) چرا NTP مهم است؟ *(پاسخ: 12-1-ت2)*

**ت3.** (متوسط) چرا نسخه‌ی دستگاه باید با دوره تطبیق شود؟ *(پاسخ: 12-1-ت3)*

**ت4.** (متوسط) رمز پیش‌فرض را چه کنیم؟ *(پاسخ: 12-1-ت4)*

**ت5.** (سخت) نسخه v7.2 است؛ چه می‌کنید؟ *(پاسخ: 12-1-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی اولین بوت. *(پاسخ: 12-1-ت6)*

**Q1.** Quick quiz (English): Which command displays the FortiOS version and serial number? *(پاسخ: 12-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NPU | Network Processor Unit | پردازنده‌ی شبکه |
| VDOM | Virtual Domain | دامنه‌ی مجازی |
| NTP | Network Time Protocol | هماهنگ‌سازی زمان |

- *Always verify the firmware version first.* ← همیشه اول نسخه‌ی Firmware را تأیید کنید.

### کارت Lab

**کارت Lab:** اولین بوت (اجرا نشده). **Evidence:** `03-ops/fgt-asbuilt-1.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Getting started
- FortiOS 7.0.3 Release Notes

<a id="l-12-2"></a>

## درس 12-2 — Interface، VLAN، Role، Administrative Access و سخت‌سازی پورت‌های FortiGate

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۱، ۳-۱، ۴-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. انواع Interface (Physical، VLAN، Aggregate، Loopback، Zone) را بشناسید.
2. VLAN Sub-interface را با ID و IP بسازید.
3. `role` و `allowaccess` را با اصل حداقل مدیریت تنظیم کنید.
4. Trusted Host، Local-in Policy و سخت‌سازی را به‌کار ببرید.
5. «لینک بالا ولی VLAN کار نمی‌کند» را عیب‌یابی کنید.
6. طراحی Interface یک شعبه را بنویسید.

### چرا باید یاد بگیریم؟

Interface هم دروازه‌ی ورود ترافیک است و هم دروازه‌ی ورود مدیریت. یک تنظیم اشتباه `allowaccess` روی WAN پنل مدیریت را به اینترنت می‌دهد. یک VLAN ID اشتباه یا Trunk ناقص روی سوییچ، کاربران را بی‌شبکه می‌کند. مثل در و قفل ساختمان: اگر قفل را فراموش کنید (allowaccess باز)، هر کس وارد می‌شود؛ اگر شماره‌ی واحد را اشتباه بزنید (VLAN)، کسی پیدایش نمی‌کند.

### انواع Interface

| نوع | توضیح |
|---|---|
| Physical | پورت واقعی (port1، wan1) |
| VLAN | زیرواسط با برچسب 802.1Q روی Physical |
| Aggregate | چند پورت (LACP 802.3ad) یک لینک |
| Redundant | Active/Backup بین دو پورت |
| Loopback | مجازی همیشه بالا (برای Router-ID، منبع Syslog، IPsec) |
| Software Switch/Zone | گروه‌بندی (درس 12-3 و 12-10) |

### VLAN

``` text
config system interface
 edit "vlan10"
  set vdom "root"
  set interface "port2"
  set vlanid 10
  set ip 10.10.0.1 255.255.255.0
  set allowaccess ping
  set role lan
 next
end
```

سوییچ مقابل باید Trunk با VLAN 10 مجاز باشد (`switchport trunk allowed vlan 10,20`) و Native VLAN درست باشد.

### role

`role` (lan، wan، dmz، undefined) رفتار GUI و پیش‌فرض‌ها را تعیین می‌کند (مثلاً Interface با role wan در لیست خروجی NAT پیش‌فرض و بعضی سرویس‌های مدیریتی محدود).

### allowaccess

سرویس‌هایی که روی آن Interface به خود فایروال پاسخ می‌دهند:

| مقدار | سرویس | توصیه |
|---|---|---|
| ping | ICMP | LAN/Mgmt؛ WAN فقط در صورت نیاز |
| https | GUI | فقط Mgmt |
| ssh | CLI | فقط Mgmt |
| snmp | SNMP | فقط Mgmt/Monitoring |
| fgfm | FortiManager | فقط شبکه‌ی FMG |
| http / telnet | ناامن | **غیرفعال** |
| fabric | Security Fabric | فقط Fabric |

### سخت‌سازی

1. **Trusted Host:** ادمین فقط از شبکه‌ی Mgmt.
2. **Local-in Policy:** محدودیت مبدأ/سرویس به خود فایروال.
3. **TLS قوی و timeout:** `admin-https-ssl-versions tlsv1-2 tlsv1-3`، `admintimeout`.
4. **Lockout:** `admin-lockout-threshold`.
5. **Banner** هشدار.
6. غیرفعال‌سازی `ping` از اینترنت در صورت سیاست.

``` text
config system admin
 edit "netadmin"
  set trusthost1 10.50.0.0 255.255.255.0
 next
end
config system global
 set admin-https-ssl-versions tlsv1-2 tlsv1-3
 set admin-lockout-threshold 5
 set admin-lockout-duration 300
end
```

### مثال‌های حل‌شده

#### مثال ساده — VLAN

VLAN 10 با IP 10.10.0.1/24 روی port2. تأیید: `get system interface physical`، سپس ping به PC در VLAN 10. اگر ping شکست خورد: Trunk سوییچ را بررسی.

#### مثال متوسط — طراحی شعبه

``` text
port1  WAN   203.0.113.2/29   role wan   allowaccess: (none)
port2  LAN   Trunk: vlan10 users 10.10.0.1/24, vlan20 servers 10.20.0.1/24
port3  DMZ   10.30.0.1/24
mgmt   MGMT  10.50.0.1/24    allowaccess ping https ssh
```

قواعد: WAN بدون مدیریت؛ فقط Mgmt مدیریت.

#### مثال متوسط — لینک بالا، VLAN کار نمی‌کند

1. سوییچ: `show interfaces trunk` ⇒ VLAN 10 در Allowed و Active؟
2. Native VLAN هر دو سر یکسان؟
3. VLAN ID دو سر یکسان؟
4. FortiGate: Interface Up، IP درست؟
5. ARP: `get system arp`.
6. Policy برای VLAN (ترافیک بدون Policy رد می‌شود).

#### مثال سخت — Brute-force از اینترنت

Log: ۵۰۰ ورود ناموفق به https از 203.0.113.50. رفع:

1. `allowaccess` WAN: حذف https/ssh.
2. Local-in Policy: فقط IPهای مجاز.
3. Lockout.
4. IP مهاجم Block (Quarantine/Policy).
5. MFA برای ادمین.
6. بررسی ورود موفق مشکوک (Event Log).

شاهد: اسکن پورت از بیرون: پورت 443/22 filtered.

#### مثال سخت — ادمین قفل

پس از تغییر allowaccess مدیریت قطع شد. نجات: Console؛ پیشگیری: `cfg-save revert` (درس ۱۲-۷)، Session دوم باز، تست از شبکه‌ی Mgmt.

### Lab هدایت‌شده (اجرا نشده)

1. VLAN 10 و 20 روی port2 با Trunk.
2. allowaccess حداقل؛ اسکن پورت از LAN.
3. Trusted Host و آزمون ورود از IP غیرمجاز.
4. Lockout آزمایشی.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| VLAN بدون ارتباط | Trunk/ID | سوییچ |
| GUI از WAN باز | allowaccess | حذف |
| ورود رد می‌شود | trusthost | منبع |
| قفل ادمین | Lockout | منتظر/Console |

### جمع‌بندی

Interface انواع دارد؛ VLAN با ID و Trunk درست. `allowaccess` فقط لازم و فقط روی Mgmt؛ Trusted Host، Local-in، TLS و Lockout سخت‌سازی‌اند.

### تمرین و ارزیابی

**ت1.** (ساده) allowaccess چیست؟ *(پاسخ: 12-2-ت1)*

**ت2.** (ساده) VLAN Sub-interface چیست؟ *(پاسخ: 12-2-ت2)*

**ت3.** (متوسط) چرا نباید https روی WAN باز باشد؟ *(پاسخ: 12-2-ت3)*

**ت4.** (متوسط) لینک up ولی VLAN کار نمی‌کند؛ علت‌ها؟ *(پاسخ: 12-2-ت4)*

**ت5.** (سخت) از اینترنت Brute-force می‌شود؛ طرح رفع. *(پاسخ: 12-2-ت5)*

**ت6.** (سخت، طراحی) Interfaceهای یک شعبه با WAN، LAN، DMZ، Mgmt. *(پاسخ: 12-2-ت6)*

**Q1.** Quick quiz (English): Which setting controls which management services are reachable on an interface? *(پاسخ: 12-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| LACP | Link Aggregation Control Protocol | پروتکل تجمیع لینک |
| Trunk | 802.1Q trunk | لینک حامل چند VLAN |

- *Never expose management services on the WAN interface.* ← هرگز سرویس‌های مدیریتی را روی Interface WAN باز نگذارید.

### کارت Lab

**کارت Lab:** Interface و VLAN (اجرا نشده). **Evidence:** `02-design/fgt-interfaces.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Interfaces
- FortiOS 7.0 Hardening guide

<a id="l-12-3"></a>

## درس 12-3 — Zone و Objectها: Address، Service، Group، Schedule و استاندارد نام‌گذاری

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۲، ۱۱-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Zone را بسازید و مزیت آن بر Interface مستقل را توضیح دهید.
2. انواع Address (Subnet، Range، FQDN، Geography) و Group را بسازید.
3. Service سفارشی و Group بسازید.
4. Schedule (Recurring، One-time) تعریف کنید و اثر آن بر Session را بفهمید.
5. استاندارد نام‌گذاری و comment را اعمال کنید.
6. Objectها را ممیزی و پاک‌سازی کنید.

### چرا باید یاد بگیریم؟

به‌جای نوشتن IP و پورت در هر Policy، یک «نام» می‌دهید (SRV-ERP). با تغییر IP فقط یک Object عوض می‌شود، نه ده‌ها Policy. و اگر نام‌گذاری استاندارد باشد، Policy مثل جمله خوانده می‌شود. بدون استاندارد، بعد از دو سال ۸۰۰ Object بی‌نام و تکراری دارید که هیچ‌کس جرأت حذفشان را ندارد. Object خوب مثل برچسب روی کارتن‌های انبار است.

### Zone

Zone گروهی از Interfaceها است که در Policy به‌عنوان یک واحد استفاده می‌شوند.

``` text
config system zone
 edit "ZN-DMZ"
  set interface "port3" "port5"
  set intrazone deny
 next
end
```

- Interface عضو Zone در Policy مستقل انتخاب نمی‌شود؛ باید Zone را انتخاب کرد.
- `intrazone`: `allow` ⇒ ترافیک بین اعضای Zone آزاد؛ `deny` ⇒ نیاز به Policy صریح.
- مزیت: افزودن Interface جدید به Zone، Policyها را خودکار پوشش می‌دهد.

### Address

| نوع | مثال | کاربرد |
|---|---|---|
| Subnet | 10.10.0.0/24 | شبکه/میزبان |
| IP Range | 10.10.0.10-10.10.0.50 | بازه |
| FQDN | `*.example.com` یا `app.example.com` | نام دامنه |
| Geography | Country | محدودیت جغرافیایی |
| Wildcard | 10.0.0.0 و ماسک معکوس | الگو |

``` text
config firewall address
 edit "NET-USERS"
  set subnet 10.10.0.0 255.255.255.0
  set comment "VLAN10 users; owner NOC"
 next
 edit "FQDN-SAAS"
  set type fqdn
  set fqdn "app.example.com"
 next
end
config firewall addrgrp
 edit "GRP-SERVERS"
  set member "SRV-ERP" "SRV-DB"
 next
end
```

**خطر FQDN:** نیازمند DNS صحیح؛ اگر DNS جواب ندهد یا IP عوض شود، Policy بدون هشدار رفتار را تغییر می‌دهد؛ TTL کوتاه؛ بهتر است DNS فایروال قابل‌اعتماد باشد.

### Service

``` text
config firewall service custom
 edit "SVC-APP-8443"
  set tcp-portrange 8443
 next
end
config firewall service group
 edit "GRP-WEB"
  set member "HTTP" "HTTPS"
 next
end
```

از Serviceهای از پیش‌تعریف‌شده (HTTP، HTTPS، DNS، SSH) تا حد ممکن استفاده کنید.

### Schedule

``` text
config firewall schedule recurring
 edit "WORK-HOURS"
  set day monday tuesday wednesday thursday friday
  set start 08:00
  set end 18:00
 next
end
config firewall schedule onetime
 edit "MAINT-2026-12-03"
  set start 22:00 2026/12/03
  set end 23:00 2026/12/03
 next
end
```

Session باز ساعت 17:59 پس از پایان Schedule تا Timeout می‌ماند؛ برای قطع فوری Session را پاک کنید.

### استاندارد نام‌گذاری

| نوع | قالب | مثال |
|---|---|---|
| Address شبکه | NET-<نام> | NET-USERS |
| Address میزبان | SRV-/HOST-<نام> | SRV-ERP |
| Group | GRP-<نام> | GRP-SERVERS |
| Service | SVC-<نام>-<پورت> | SVC-APP-8443 |
| Zone | ZN-<نام> | ZN-DMZ |
| Schedule | SCH-<نام> | SCH-WORK |
| VIP | VIP-<نام> | VIP-WEB-443 |

و در `comment` مالک و دلیل.

### مثال‌های حل‌شده

#### مثال ساده — مزیت Object

IP سرور ERP عوض شد (10.20.0.10 → 10.20.0.50). اگر Object SRV-ERP باشد، یک ویرایش؛ اگر IP مستقیم در 12 Policy بود، ۱۲ ویرایش و خطر فراموشی.

#### مثال متوسط — Zone و Policy

دو Interface DMZ (port3 و port5) در ZN-DMZ. Policy: `ZN-USERS -> ZN-DMZ HTTPS accept`. افزودن port6 به ZN-DMZ ⇒ Policy آن را هم می‌پوشاند. با `intrazone deny`، ترافیک بین سرورهای DMZ فقط با Policy صریح.

#### مثال متوسط — خطر FQDN

Policy با FQDN-SAAS؛ DNS فایروال به سرور داخلی که از کار افتاد ⇒ FQDN resolve نمی‌شود ⇒ Address خالی ⇒ Policy مطابق نمی‌شود. شاهد: `diagnose firewall iprope lookup` و `diagnose test application dnsproxy 3`. رفع: DNS افزونه/Forwarder و پایش.

#### مثال سخت — ممیزی ۲۰۰ Object

1. Export و فهرست Objectها با تعداد Reference (GUI: ستون Ref.).
2. Ref=0 و عمر بیش از ۹۰ روز ⇒ کاندید حذف.
3. تکراری: دو Object با همان Subnet ⇒ ادغام.
4. نام‌گذاری غیراستاندارد ⇒ تغییر نام همراه با CHG.
5. Object بدون comment ⇒ مالک‌یابی.
6. Backup و حذف تدریجی (ابتدا Policyها را به Object ادغام‌شده منتقل).

#### مثال سخت — استاندارد شرکت

شرکت ۵۰ شعبه؛ قرارداد: `<SITE>-<TYPE>-<NAME>` مثل `HQ-NET-USERS`، `BR12-SRV-DC1`. Script بررسی نام (regex) در CI روی Config Export: `^(HQ|BR[0-9]{2})-(NET|SRV|GRP|SVC)-[A-Za-z0-9_-]+$`. شاهد: گزارش Objectهای ناسازگار.

### Lab هدایت‌شده (اجرا نشده)

1. ده Object با قرارداد نام و comment.
2. Zone با intrazone deny و Policy.
3. FQDN و آزمون Lookup.
4. Schedule و رفتار Session پس از پایان.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Interface در Policy نیست | عضو Zone | Zone را انتخاب |
| Policy مطابق نمی‌شود (FQDN) | DNS | بررسی/Forwarder |
| Object تکراری | بی‌استاندارد | ادغام |
| Session پس از Schedule | Timeout | Clear |

### جمع‌بندی

Zone گروه Interface؛ Objectها Address/Service/Group/Schedule با نام‌گذاری و comment. FQDN به DNS وابسته است. ممیزی Ref و تکراری، فرایند دوره‌ای است.

### تمرین و ارزیابی

**ت1.** (ساده) مزیت Address Object چیست؟ *(پاسخ: 12-3-ت1)*

**ت2.** (ساده) intrazone deny چه می‌کند؟ *(پاسخ: 12-3-ت2)*

**ت3.** (متوسط) چرا Interface عضو Zone در Policy قابل انتخاب نیست؟ *(پاسخ: 12-3-ت3)*

**ت4.** (متوسط) خطر Object FQDN؟ *(پاسخ: 12-3-ت4)*

**ت5.** (سخت) ۲۰۰ Object را ممیزی کنید. *(پاسخ: 12-3-ت5)*

**ت6.** (سخت، طراحی) استاندارد نام‌گذاری شرکت. *(پاسخ: 12-3-ت6)*

**Q1.** Quick quiz (English): Why use zones instead of individual interfaces in policies? *(پاسخ: 12-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FQDN | Fully Qualified Domain Name | نام کامل دامنه |

- *Use a naming standard for every object.* ← برای هر Object استاندارد نام‌گذاری بگذارید.

### کارت Lab

**کارت Lab:** Objectها (اجرا نشده). **Evidence:** `02-design/fgt-objects.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall objects; Zones

<a id="l-12-4"></a>

## درس 12-4 — Static Route، Default Route، Policy Route، Distance/Priority و Failover

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۲، ۱۰-۴ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Static، Default و Policy Route را در FortiGate بسازید.
2. Distance و Priority را بشناسید و با Link Monitor ترکیب کنید.
3. زمان تشخیص قطع را محاسبه کنید.
4. ترتیب Policy Route و جدول مسیر را بدانید.
5. جدول مسیر را بخوانید (`routing-table all` و `database`).
6. Failover دو ISP را آزمون و ثبت کنید.

### چرا باید یاد بگیریم؟

Routing تعیین می‌کند ترافیک از کدام Interface و به کدام Next-hop خارج شود. Policy درست با Route نادرست بی‌فایده است. و در FortiGate Dual-ISP اگر Link Monitor نباشد، قطع واقعی ISP تشخیص داده نمی‌شود. مثل نقشه‌ی راه: حتی با بهترین مجوز، اگر نقشه اشتباه باشد به مقصد نمی‌رسید.

### مفاهیم

- **Static Route:** مقصد + Gateway + Interface.
- **Default Route:** `0.0.0.0/0`.
- **Distance:** اعتبار (کمتر بهتر)؛ پیش‌فرض Static=10.
- **Priority:** بین Routeهای هم‌Distance، **کمتر** اولویت بیشتر (در FortiGate).
- **Policy Route:** قبل از جدول Routing ارزیابی می‌شود.
- **Link Monitor:** پایش مسیر با ping/HTTP؛ در شکست Route را غیرفعال می‌کند.

### جدول مسیر

``` text
get router info routing-table all
get router info routing-table database
get router info routing-table details 198.51.100.8
```

`all` فقط بهترین مسیرها (فعال)؛ `database` همه‌ی مسیرها (حتی غیرفعال) با Distance/Priority.

### پیکربندی

``` text
config router static
 edit 1
  set dst 0.0.0.0 0.0.0.0
  set gateway 203.0.113.1
  set device "port1"
  set distance 10
 next
 edit 2
  set dst 0.0.0.0 0.0.0.0
  set gateway 198.51.100.1
  set device "port2"
  set distance 20
 next
end
config system link-monitor
 edit "ISP1"
  set srcintf "port1"
  set server "8.8.8.8"
  set gateway-ip 203.0.113.1
  set interval 1000
  set failtime 5
  set recoverytime 5
  set update-static-route enable
 next
end
```

`update-static-route enable` یعنی با شکست Monitor، Route وابسته غیرفعال می‌شود.

**زمان تشخیص:**

``` text
Detection time = interval x failtime = 1000 ms x 5 = 5 s
```

> **حدود اعتبار (v4.0):** این رابطه یک **تقریب آموزشی و حد پایین نظری** است، نه تضمین زمانی. زمان واقعی به نحوه‌ی اجرای Probe (Interval، Timeout، همزمانی)، گم‌شدن تصادفی بسته‌ها، تنظیم failtime/recoverytime، زمان به‌روزرسانی Route/FIB، بازسازی Session/NAT، پروتکل مسیریابی و BFD، و رفتار برنامه‌ی کاربر بستگی دارد. برای عدد قابل‌اتکا باید در محیط هدف **اندازه‌گیری** شود (در این دوره اندازه‌گیری انجام نشده است).


### Policy Route

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.99.0/24"
  set dst "0.0.0.0/0"
  set gateway 198.51.100.1
  set output-device "port3"
 next
end
```

بررسی: `diagnose firewall proute list`. اگر مطابق نبود، جدول عادی.

### مثال‌های حل‌شده

#### مثال ساده — Default

``` text
config router static
 edit 1
  set gateway 203.0.113.1
  set device "port1"
 next
end
```

تأیید: `get router info routing-table all` ⇒ `S* 0.0.0.0/0 [10/0] via 203.0.113.1, port1`.

#### مثال متوسط — Dual-ISP

Route 1 (distance 10، port1) و Route 2 (distance 20، port2)؛ `routing-table all` فقط Route 1؛ `database` هر دو (Route 2 با Standby). با شکست Monitor، Route 1 غیرفعال و Route 2 فعال.

#### مثال متوسط — محاسبه‌ی قطع

``` text
ping -i 0.2 8.8.8.8
lost 38 packets x 0.2 s = 7.6 s outage
```

۵ ثانیه تشخیص + ~۲٫۶ ثانیه همگرایی/Session. اگر هدف ۵ ثانیه: `interval 500` و `failtime 5` ⇒ 2.5 s.

#### مثال سخت — Failover ناقص

ISP-A بالادست مشکل دارد (لینک Up). بدون Link Monitor، Route فعال می‌ماند. با Monitor: `diagnose sys link-monitor status` ⇒ `dead`، Route دوم فعال. سپس Sessionهای قدیمی: Clear یا `snat-route-change`.

#### مثال سخت — Policy Route و Failover

Policy Route برای مهمان با Gateway ISP-B؛ ISP-B می‌افتد. بدون Health-check ترافیک به چاه می‌رود. با SD-WAN یا `set gateway` + Link Monitor مربوط. شاهد: `diagnose firewall proute list` و traceroute.

### Lab هدایت‌شده (اجرا نشده)

1. دو Interface WAN و دو Route.
2. Link Monitor؛ قطع بالادست (مثلاً ACL) و اندازه‌گیری.
3. Policy Route برای یک شبکه.
4. ثبت جدول «Route ← Distance ← فعال؟».

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Failover نمی‌شود | Monitor ندارد | افزودن |
| Policy Route اثر ندارد | ترتیب/Interface | `proute list` |
| Session قدیم | Clear | فیلتر |
| Route دوم فعال نمی‌شود | Distance/Monitor | `database` |

### جمع‌بندی

Static/Default با Distance و Priority؛ Link Monitor قطع واقعی را می‌فهمد؛ Policy Route قبل از جدول. زمان تشخیص = interval × failtime. بعد از Failover Sessionهای قدیمی را مدیریت کنید.

### تمرین و ارزیابی

**ت1.** (ساده) Distance چیست؟ *(پاسخ: 12-4-ت1)*

**ت2.** (ساده) Priority چه فرقی با Distance دارد؟ *(پاسخ: 12-4-ت2)*

**ت3.** (متوسط) چرا Link-monitor لازم است؟ *(پاسخ: 12-4-ت3)*

**ت4.** (متوسط) Policy Route قبل یا بعد از جدول مسیر؟ *(پاسخ: 12-4-ت4)*

**ت5.** (سخت) پس از Policy Route برخی Sessionها قطع می‌شوند؛ تحلیل. *(پاسخ: 12-4-ت5)*

**ت6.** (سخت، طراحی) دو ISP با Primary/Backup. *(پاسخ: 12-4-ت6)*

**Q1.** Quick quiz (English): Which attribute breaks the tie between static routes with equal distance? *(پاسخ: 12-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس |
| Blackhole | Blackhole route | مسیر دورریز |

- *A route decides the egress interface before the policy lookup.* ← Route قبل از Policy Interface خروجی را تعیین می‌کند.

### کارت Lab

**کارت Lab:** Route و Failover (اجرا نشده). **Evidence:** `02-design/fgt-routing.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Static routing; Link monitor; Policy routes

<a id="l-12-5"></a>

## درس 12-5 — Admin، RBAC، MFA و سخت‌سازی مدیریت FortiGate

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۲، ۱۲-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. RBAC را با Admin Profile و ادمین‌های مجزا پیاده کنید.
2. MFA (FortiToken، OTP، RADIUS) را برای ادمین فعال کنید.
3. حساب Break-glass و سیاست رمز را طراحی کنید.
4. Trusted Host، Local-in و Lockout را ترکیب کنید.
5. ممیزی ورود و تغییر (Event Log) را تنظیم و بررسی کنید.
6. گزارش ممیزی هفتگی بنویسید.

### چرا باید یاد بگیریم؟

اگر همه‌ی ادمین‌ها Super Admin باشند، خطای هر نفر خطای کل است، و در حادثه نمی‌دانید چه کسی چه کرد. دسترسی مدیریتی فایروال بالاترین قدرت در شبکه است؛ مهاجمی که ادمین شود همه‌چیز را دارد. RBAC (Role-Based Access Control، یعنی «دسترسی بر پایه‌ی نقش») به هر نفر فقط همان کارِ لازم را می‌دهد؛ MFA رمز لورفته را بی‌اثر می‌کند؛ Log و ممیزی پاسخگویی را ممکن می‌سازد. مثل کلید ساختمان: کارگر نظافت کلید همه‌ی اتاق‌ها را ندارد.

### Admin Profile

Profile مجوزها را به گروه‌های دسترسی (Access Group) می‌دهد: `read`، `read-write`، `none` برای هر گروه (netgrp، fwgrp، loggrp، sysgrp، vpngrp، utmgrp، ...).

``` text
config system accprofile
 edit "noc-ro"
  set netgrp read
  set fwgrp read
  set loggrp read
  set sysgrp read
 next
 edit "fw-eng"
  set netgrp read-write
  set fwgrp read-write
  set loggrp read
 next
end
```

ادمین‌ها:

``` text
config system admin
 edit "noc1"
  set accprofile "noc-ro"
  set trusthost1 10.50.0.0 255.255.255.0
  set vdom "root"
 next
end
```

### نقش‌ها

| نقش | Profile | دسترسی |
|---|---|---|
| NOC | noc-ro | فقط خواندن |
| مهندس شبکه | fw-eng | Policy/Route |
| امنیت | sec-an | Log/UTM |
| Super Admin | super_admin | دو نفر، MFA اجباری |
| Break-glass | super_admin | حساب اضطراری در Vault |

### MFA

- **FortiToken** (سخت‌افزاری یا موبایل): `set two-factor fortitoken`.
- **OTP ایمیل/SMS**.
- **RADIUS+MFA** (NPS/FortiAuthenticator).

``` text
config system admin
 edit "fw1"
  set two-factor fortitoken
  set fortitoken "FTKMOB..."
 next
end
```

نیازمند ساعت دقیق (NTP) برای TOTP؛ توکن زمان‌محور است.

### حساب Break-glass

حساب اضطراری برای وقتی که MFA/AD از کار افتاده: رمز بسیار بلند در Vault، استفاده فقط با دو نفر و ثبت، تغییر پس از استفاده، هشدار روی هر ورود.

### سخت‌سازی

``` text
config system global
 set admin-lockout-threshold 5
 set admin-lockout-duration 300
 set admintimeout 10
end
config system password-policy
 set status enable
 set minimum-length 14
 set min-upper-case-letter 1
 set min-number 1
 set expire-status enable
 set expire-day 90
end
```

### ممیزی

``` text
config log eventfilter
 set event enable
 set system enable
end
```

Event Log ورود/خروج و تغییر Config (`cfgpath`, `user`, `action`). هفتگی با CHGها تطبیق دهید؛ تغییر بدون CHG یعنی خارج از فرایند.

### مثال‌های حل‌شده

#### مثال ساده — Profile فقط‌خواندنی

NOC با `noc-ro`: ورود موفق؛ تلاش برای تغییر Policy ⇒ «Permission denied». Log رویداد ثبت شد.

#### مثال متوسط — MFA

ادمین `fw1` با FortiToken: ورود ⇒ رمز + OTP. آزمون منفی: ورود بدون OTP رد؛ ساعت نادرست (۲ دقیقه اختلاف) ⇒ OTP رد: NTP را بررسی.

#### مثال متوسط — ممیزی هفتگی

``` text
execute log filter category 1
execute log filter field user "netadmin"
execute log display
```

فهرست تغییرات هفته ⇒ تطبیق با CHG-110 تا CHG-118؛ تغییر ناشناس ⇒ بررسی.

#### مثال سخت — «تغییر بدون ردپا»

Policy 47 حذف شده و کسی نمی‌داند. ۱) Event Log: `Action=delete cfgpath=firewall.policy` ۲) کاربر و IP منبع ۳) تطبیق با CHG ۴) اگر ادمین مشترک بود (admin) ⇒ ضعف: حساب مشترک ممنوع؛ حساب‌های شخصی ۵) بازگردانی از Backup.

#### مثال سخت — طراحی MFA ایمن

۵ ادمین؛ همه MFA؛ دو Super Admin؛ Break-glass. سناریوی خرابی: سرور MFA/AD از کار افتاده ⇒ ادمین نمی‌تواند وارد شود ⇒ Break-glass با دو نفر و ثبت. آزمون: شبیه‌سازی خرابی و ورود اضطراری، سپس چرخش رمز.

### Lab هدایت‌شده (اجرا نشده)

1. سه Profile و سه ادمین.
2. MFA برای یک ادمین.
3. آزمون منفی (Profile فقط‌خواندنی، IP غیرمجاز، بدون OTP).
4. گزارش ممیزی.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| همه Super Admin | سهل‌انگاری | Profile |
| OTP رد می‌شود | ساعت | NTP |
| تغییر بی‌ردپا | حساب مشترک/Log خاموش | حساب شخصی، eventfilter |
| قفل ادمین | Lockout | Break-glass/Console |

### جمع‌بندی

RBAC با Profile و ادمین شخصی، Trusted Host، MFA، Break-glass، Lockout و Event Log. ممیزی هفتگی با CHG تطبیق دهید.

### تمرین و ارزیابی

**ت1.** (ساده) RBAC چیست؟ *(پاسخ: 12-5-ت1)*

**ت2.** (ساده) Trusted host چه می‌کند؟ *(پاسخ: 12-5-ت2)*

**ت3.** (متوسط) Lockout چه فایده‌ای دارد؟ *(پاسخ: 12-5-ت3)*

**ت4.** (متوسط) چرا Break-glass؟ *(پاسخ: 12-5-ت4)*

**ت5.** (سخت) Brute-force از یک IP؛ پاسخ. *(پاسخ: 12-5-ت5)*

**ت6.** (سخت، طراحی) سه سطح دسترسی و چک‌لیست. *(پاسخ: 12-5-ت6)*

**Q1.** Quick quiz (English): What does a trusted host setting restrict? *(پاسخ: 12-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MFA | Multi-Factor Authentication | احراز چندعاملی |
| RBAC | Role-Based Access Control | کنترل دسترسی نقش‌محور |

- *Apply least privilege to administrator accounts.* ← به حساب‌های Admin حداقل دسترسی بدهید.

### کارت Lab

**کارت Lab:** سخت‌سازی Admin (اجرا نشده). **Evidence:** `03-ops/fgt-admin-standard.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Administrators; Hardening
- FortiOS 7.0 Hardening guide

<a id="l-12-6"></a>

## درس 12-6 — Backup/Restore، Firmware Upgrade، Rollback و Lifecycle

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۱، ۱۲-۵ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Backup و Restore را اجرا و صحت آن را تأیید کنید.
2. مسیر ارتقای FortiOS (Upgrade Path) و Release Notes را بخوانید.
3. برنامه‌ی ارتقا (Pre/Post-check، Window) را بنویسید.
4. Rollback را طراحی و تمرین کنید.
5. چرخه‌ی عمر (EoS/EoL) و Patch را پیگیری کنید.
6. ارتقای HA را در سطح مفهومی بدانید.

### چرا باید یاد بگیریم؟

بدون Backup آزمون‌شده، یک خطای ساده ساعت‌ها قطعی می‌سازد. و ارتقا مثل تعویض موتور هواپیما در پرواز است: اگر مسیر، Backup و Rollback آماده نباشد، دستگاه بوت نمی‌شود یا ویژگی‌ای که لازم دارید شکسته می‌شود. بسیاری از حوادث امنیتی هم از نسخه‌ی قدیمی بدون Patch می‌آید؛ پس مدیریت چرخه‌ی عمر بخشی از امنیت است.

### Backup

``` text
execute backup config tftp cfg-2026-11-27.conf 10.50.0.30
execute backup config usb cfg.conf
show full-configuration          (CLI view)
```

بهترین‌روش:

1. **قبل از هر تغییر** Backup؛ نام‌گذاری با تاریخ/CHG.
2. **Hash** (`sha256sum`) برای سلامت.
3. نگهداری **خارج از دستگاه**، رمزنگاری‌شده (Config حاوی Secretها).
4. **Restore آزمایشی** ماهانه در Lab.

Restore:

``` text
execute restore config tftp cfg-2026-11-27.conf 10.50.0.30
```

(دستگاه Reboot می‌شود؛ نسخه‌ی Config با Firmware سازگار باشد.)

### ارتقا

**مراحل:**

1. Release Notes نسخه‌ی مقصد: تغییر Syntax، پیش‌فرض، Known Issues.
2. **Upgrade Path** رسمی: ممکن است مرحله‌ای باشد (A→B→C).
3. Lab: ارتقا با Config کپی‌شده.
4. Backup + Image قبلی.
5. پنجره‌ی تغییر و اطلاع‌رسانی.
6. اجرا (GUI/CLI): `execute restore image tftp new.out 10.50.0.30`.
7. Post-check.
8. تصمیم Rollback.

### Pre/Post-check

| مورد | قبل | بعد |
|---|---|---|
| نسخه | `get system status` | نسخه‌ی جدید |
| تعداد Policy | `show firewall policy` (شمارش) | یکسان |
| Tunnel | `diagnose vpn tunnel list` | همه Up |
| HA | `get system ha status` | in-sync |
| Route | `get router info routing-table all` | بدون تفاوت غیرمنتظره |
| UTM | وضعیت FortiGuard | Update فعال |
| Log | Syslog | ادامه |

### Rollback

``` text
execute restore image tftp old.out 10.50.0.30
execute restore config tftp cfg-before.conf 10.50.0.30
```

**معیار Rollback از قبل:** «اگر ظرف ۳۰ دقیقه سرویس حیاتی برنگشت». Rollback هم باید در Lab تمرین شود (زمان‌گیری).

### چرخه‌ی عمر

- **EoS (End of Support) / EoL (End of Life):** تاریخ‌ها را از سایت رسمی Fortinet پیگیری کنید.
- Patch امنیتی: PSIRT را دنبال کنید؛ آسیب‌پذیری قابل‌بهره‌برداری از اینترنت اولویت اول.
- ارتقای برنامه‌ریزی‌شده (سالانه/نیم‌سالانه).

### مثال‌های حل‌شده

#### مثال ساده — Backup با Hash

``` text
execute backup config tftp cfg-2026-11-27.conf 10.50.0.30
sha256sum cfg-2026-11-27.conf   -> store beside file
```

#### مثال متوسط — برنامه‌ی ارتقا

T-14 مطالعه‌ی Release Notes؛ T-7 Lab؛ T-1 Backup + Hash + Image قبلی؛ T0 پنجره ۲۲:۰۰ تا ۲۳:۰۰؛ T+30m Post-check؛ T+24h پایش؛ بستن CHG.

#### مثال متوسط — Restore آزمایشی

Config را در Lab VM Restore کنید؛ تعداد Policy/Route/Interface با مبدأ مقایسه؛ زمان Restore (RTO) = ۸ دقیقه ثبت.

#### مثال سخت — ارتقا SSL-VPN را شکست

پس از ارتقا Portal باز نشد. تحلیل: Release Notes می‌گوید Syntax تغییر کرده. گام‌ها: ۱) Post-check شکست ۲) معیار Rollback: ۳۰ دقیقه ۳) ۱۰ دقیقه تلاش برای رفع (اصلاح Syntax) ناموفق ۴) Rollback Image+Config ۵) تأیید بازگشت ۶) CHG «ناموفق + درس» ۷) آزمون در Lab با Syntax جدید قبل از تلاش بعدی.

#### مثال سخت — Config ناسازگار

Config نسخه‌ی جدید را روی نسخه‌ی قدیم Restore کردید؛ برخی سطرها نامعتبر. درس: Config را فقط با همان نسخه (یا نسخه‌ی سازگار) Restore کنید؛ Backup Image هم داشته باشید.

### Lab هدایت‌شده (اجرا نشده)

1. Backup و Hash.
2. Restore در Lab و مقایسه.
3. ارتقا و Rollback آزمایشی روی VM (Snapshot قبل).
4. جدول Pre/Post-check.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Restore شکست | نسخه | هم‌نسخه |
| بوت نمی‌شود | Image | Console/Rollback |
| ویژگی شکست | Syntax | Release Notes |
| Config ناقص | مسیر ارتقا | Backup |

### جمع‌بندی

Backup قبل از هر تغییر + Hash + Restore آزمایشی. ارتقا: Release Notes، Upgrade Path، Lab، پنجره، Post-check و معیار Rollback از قبل. چرخه‌ی عمر و PSIRT را پیگیری کنید.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Backup رمزگذاری شود؟ *(پاسخ: 12-6-ت1)*

**ت2.** (ساده) Upgrade Path Tool چیست؟ *(پاسخ: 12-6-ت2)*

**ت3.** (متوسط) قبل Upgrade چه بررسی می‌کنید؟ *(پاسخ: 12-6-ت3)*

**ت4.** (متوسط) چرا HA ابتدا Secondary؟ *(پاسخ: 12-6-ت4)*

**ت5.** (سخت) Boot loop بعد Upgrade؛ پاسخ. *(پاسخ: 12-6-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی CHG برای Upgrade. *(پاسخ: 12-6-ت6)*

**Q1.** Quick quiz (English): Why must you plan a rollback before upgrading firmware? *(پاسخ: 12-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| EoS | End of Support | پایان پشتیبانی |
| CHG | Change request | درخواست تغییر |

- *Back up before every change.* ← قبل از هر تغییر Backup بگیرید.

### کارت Lab

**کارت Lab:** Backup/Restore (اجرا نشده). **Evidence:** `03-ops/fgt-backup-log.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Backup and restore; Firmware
- Fortinet Upgrade Path Tool

## درس 12-8 — Transit، Local-in و Local-out: سه نوع ترافیک و سه مسیر پردازش

**فصل ۱۲ · درس افزوده (پس از ۱۲-۶) · پیش‌نیاز: ۱۲-۰، ۵-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3، `Unverified` روی Image):** دسته‌بندی مفهومی است؛ نام دقیق دستورها با CLI Reference 7.0 تطبیق داده شود. Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Transit، Local-in و Local-out را در FortiGate تمایز دهید و کنترل هرکدام را بگویید.
2. `allowaccess` و Local-in Policy را بنویسید.
3. Source IP/Interface سرویس‌های Local-out را تنظیم کنید.
4. با Debug Flow هر سه نوع را شناسایی کنید.
5. خطاهای رایج (Policy برای مدیریت، Update/NTP نمی‌رسد) را رفع کنید.
6. تست‌های مثبت و منفی بنویسید.

### چرا باید یاد بگیریم؟

بسیاری تصور می‌کنند Firewall Policy همه‌ی ترافیک را کنترل می‌کند. ولی Policy فقط ترافیک **عبوری** را می‌بیند. ترافیک به خود فایروال (SSH، ping، SNMP، VPN) مسیر جدا دارد. و ترافیکی که فایروال می‌سازد (NTP، Syslog، FortiGuard) هم مسیر خودش را. اگر این سه را قاطی کنید، یا مدیریت را ناخواسته باز می‌گذارید یا Update و Log کار نمی‌کند.

### سه نوع ترافیک

| نوع | مبدأ ← مقصد | کنترل |
|---|---|---|
| Transit | از میان فایروال | Firewall Policy (+NAT/UTM) |
| Local-in | به IP خود فایروال | `allowaccess` + Local-in Policy |
| Local-out | از خود فایروال | تنظیمات سرویس، Route، Source IP |

### Local-in

دو لایه:

1. **allowaccess** Interface: اگر سرویس باز نباشد، فایروال اصلاً پاسخ نمی‌دهد.
2. **Local-in Policy**: محدودیت مبدأ/سرویس برای ترافیک به خود فایروال.

``` text
config firewall local-in-policy
 edit 1
  set intf "port1"
  set srcaddr "TRUSTED-IPS"
  set dstaddr "all"
  set service "HTTPS" "SSH"
  set action accept
  set schedule "always"
 next
 edit 2
  set intf "port1"
  set srcaddr "all"
  set dstaddr "all"
  set service "HTTPS" "SSH"
  set action deny
  set schedule "always"
 next
end
```

Local-in Policy اول مطابقت‌یافته‌ها را اعمال می‌کند؛ Deny پس از Accept.

### Local-out

سرویس‌های خود فایروال و تنظیم منبع:

``` text
config system ntp
 set ntpsync enable
 set source-ip 10.50.0.1
end
config log syslogd setting
 set status enable
 set server 10.50.0.20
 set source-ip 10.50.0.1
end
config system dns
 set primary 10.20.0.5
end
```

این ترافیک از Routing و (برای NAT) Interface خروجی می‌گذرد؛ مشکل رایج: آدرس مبدأ ناخواسته (IP WAN) یا نبود Route.

### Debug Flow برای تمایز

``` text
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow trace start 10
diagnose debug enable
```

Transit: «allocate a new session» + Policy. Local-in: نشانه‌ی «local-in» (در بعضی نسخه‌ها)/پاسخ مستقیم. Local-out: Session با مبدأ IP خود فایروال.

### مثال‌های حل‌شده

#### مثال ساده — کدام نوع؟

| ترافیک | نوع |
|---|---|
| ping PC به سرور | Transit |
| ping PC به 10.10.0.1 (IP FW) | Local-in |
| FW به NTP | Local-out |
| FW به FortiGuard | Local-out |

#### مثال متوسط — Local-in Policy

فقط 10.50.0.0/24 به GUI/SSH WAN: Policy 1 accept برای `TRUSTED-IPS` و Policy 2 deny. آزمون مثبت: از 10.50.0.5 `ssh` موفق. آزمون منفی: از 198.51.100.9 Timeout و Log Deny.

#### مثال متوسط — اشتباه رایج

`Users -> any SSH deny` برای بستن SSH به فایروال. بی‌اثر چون Local-in است. رفع: حذف `ssh` از `allowaccess` یا Local-in Policy.

#### مثال سخت — Update نمی‌رسد

FortiGuard Update شکست می‌خورد:

1. `execute ping update.fortiguard.net`؟
2. DNS فایروال؟
3. Route Default؟
4. NAT: ترافیک خروجی فایروال از Interface خروجی با IP همان Interface (Source NAT خودکار)؛ اگر IP خصوصی است و ISP آن را Route نمی‌کند، Source IP را به IP عمومی ببرید.
5. ISP/فایروال بالادست پورت 443/8890 را می‌بندد؟
6. `diagnose debug application update -1` (کوتاه).

#### مثال سخت — Syslog از Interface اشتباه

Syslog با IP WAN ارسال می‌شود ولی سرور فقط IP Mgmt را می‌شناسد. رفع: `set source-ip 10.50.0.1`؛ شاهد: `tcpdump` روی سرور.

### Lab هدایت‌شده (اجرا نشده)

1. سه ترافیک را تولید و Debug Flow را اجرا کنید.
2. Local-in Policy و آزمون مثبت/منفی.
3. Source IP برای NTP و Syslog.
4. خطای «Policy عادی برای مدیریت».

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| ping به FW نه | allowaccess | افزودن |
| SSH از اینترنت باز | allowaccess/Local-in | حذف/محدود |
| Update/NTP نمی‌رسد | Route/Source | تنظیم |
| Policy بی‌اثر روی FW | نوع Local-in | local-in-policy |

### جمع‌بندی

Transit با Policy، Local-in با allowaccess و Local-in Policy، Local-out با تنظیم سرویس و Source IP. اشتباه رایج: Policy عبوری برای مدیریت.

### تمرین و ارزیابی

**ت1.** (ساده) سه نوع ترافیک را نام ببرید. *(پاسخ: 12-8-ت1)*

**ت2.** (ساده) کدام تنظیم Ping به فایروال را روی یک Interface مجاز می‌کند؟ *(پاسخ: 12-8-ت2)*

**ت3.** (متوسط) چرا Firewall Policy برای SSH به خود فایروال کافی/لازم نیست؟ *(پاسخ: 12-8-ت3)*

**ت4.** (متوسط) ping از CLI به شبکه‌ی پشت VPN شکست می‌خورد؛ چرا؟ *(پاسخ: 12-8-ت4)*

**ت5.** (سخت) مدیریت را فقط از 192.168.90.0/24 مجاز کنید؛ سه لایه‌ی کنترل را بنویسید. *(پاسخ: 12-8-ت5)*

**ت6.** (سخت، طراحی) فایروال Syslog را به سرور 192.168.90.20 می‌فرستد ولی Log نمی‌رسد؛ مراحل بررسی Local-out را مرتب کنید. *(پاسخ: 12-8-ت6)*

**م1.** Trusted Host چیست؟ *(پاسخ: 12-8-م1)*

**Q1.** Quick quiz (English): Which mechanism controls traffic destined to the firewall itself? *(پاسخ: 12-8-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Local-in | Local-in traffic | ترافیک ورودی به خود فایروال |
| Local-out | Local-out traffic | ترافیک خروجی از خود فایروال |
| Transit | Transit traffic | ترافیک عبوری |
| allowaccess | Administrative access | سرویس‌های مجاز روی Interface |
| Trusted host | Trusted host | IP مجاز برای ورود Admin |

- *Firewall policies do not control traffic destined to the firewall itself.* ← Policyها ترافیک مقصد خود فایروال را کنترل نمی‌کنند.
- *Restrict management access to a dedicated network.* ← دسترسی مدیریتی را به شبکه‌ی اختصاصی محدود کنید.

### منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Interface settings (Administrative access)، Local-in policy؛ CLI Reference `config firewall local-in-policy`، `config system interface`.
- Fortinet: «Hardening your FortiOS» (مقاله‌ی رسمی؛ نسخه‌ی 7.0 را بررسی کنید).

## درس 12-9 — Hardware Acceleration (NPU/SPU) و Session Offload: اثر بر عملکرد و عیب‌یابی

**فصل ۱۲ · درس افزوده (پس از ۱۲-۸) · پیش‌نیاز: ۱۲-۰، ۱۱-۷ · ≈ ۴ ساعت**

> **وضعیت:** مفهومی. FortiGate-VM در Lab ما سخت‌افزار NP ندارد؛ بنابراین رفتار Offload در Lab «اجرا نشده» است. دستورها `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. NPU/SPU و Session Offload را تعریف و فایده‌ی آن را بگویید.
2. شرایط Offload و عواملی که آن را غیرفعال می‌کنند بشناسید.
3. وضعیت Offload یک Session را از `session list` بخوانید.
4. Offload را برای عیب‌یابی موقتاً خاموش کنید.
5. اثر UTM/Proxy بر ظرفیت را محاسبه کنید.
6. مدل را بر پایه‌ی Throughput با UTM انتخاب کنید.

### چرا باید یاد بگیریم؟

فایروال سخت‌افزاری با تراشه‌ی ویژه (NPU) Sessionهای ساده را بدون درگیری CPU عبور می‌دهد و Throughput چند برابر می‌شود. ولی هنگام عیب‌یابی، بسته‌ها دیگر CPU را نمی‌بینند و Sniffer/Debug ناقص می‌شود؛ و UTM عمیق ممکن است Offload را غیرفعال کند و ظرفیت به‌شدت افت کند. اگر این‌ها را ندانید یا دیتاشیت را اشتباه بخوانید (Firewall Throughput به‌جای Throughput با UTM)، دستگاه را کم‌ظرفیت می‌خرید.

### مفاهیم

- **CPU:** پردازش همه‌منظوره؛ کند ولی انعطاف‌پذیر.
- **NPU (Network Processing Unit):** تراشه‌ی ویژه‌ی انتقال بسته (Firewall، NAT، IPsec ساده).
- **SPU (Security Processing Unit):** NPU + CP (Content Processor) برای رمزنگاری/AV.
- **Session Offload:** بسته‌ی اول Session را CPU بررسی و تصمیم می‌گیرد؛ سپس Session به NPU منتقل می‌شود و بقیه‌ی بسته‌ها سخت‌افزاری عبور می‌کنند.

``` text
packet 1 (SYN) -> CPU: policy, route, NAT -> decision
packet 2..N     -> NPU: forwarded in hardware (CPU not involved)
```

### شرایط Offload

برقرار بودن این‌ها (طبق مستند مدل/نسخه):

- Policy بدون UTM عمیق Proxy-based (یا فقط Flow-based محدود).
- بدون Traffic Shaping/QoS پیچیده (در بعضی مدل‌ها).
- پروتکل‌های پشتیبانی‌شده (TCP/UDP معمول).
- `auto-asic-offload` روی Policy فعال (پیش‌فرض).

عوامل غیرفعال‌کننده: Proxy-based UTM (AV/Web عمیق)، SSL Inspection، IPS (بسته به نسخه)، بعضی ALG و Session خاص.

### مشاهده

``` text
diagnose sys session list
 ... npu info: flag=0x81/0x81, offload=8/8, ips_offload=0/0 ...
get hardware npu np6 session-stats 0   (model dependent)
```

وجود `npu info` و `offload=` یعنی Session Offload شده.

### کنترل

``` text
config firewall policy
 edit 30
  set auto-asic-offload disable
 next
end
```

فقط موقت برای عیب‌یابی؛ سپس برگردانید.

### اثر روی ظرفیت

دیتاشیت چند عدد دارد: Firewall Throughput، IPsec VPN، IPS، NGFW (Threat Protection)، SSL Inspection. عدد واقعی شما همان است که مطابق **ویژگی‌هایی که فعال می‌کنید**.

``` text
Firewall 20 Gbps ; IPS 5 Gbps ; NGFW 3 Gbps ; SSL inspection 2 Gbps
```

اگر ترافیک شما 4 Gbps با IPS و AV است، NGFW=3 Gbps کافی نیست.

### مثال‌های حل‌شده

#### مثال ساده — دیدن Offload

`session list` ⇒ `npu info: offload=8/8` ⇒ Session Offload شده و CPU درگیر نیست. در Sniffer فقط چند بسته‌ی اول دیده می‌شود.

#### مثال متوسط — خاموش‌کردن موقت

برای Capture کامل: `set auto-asic-offload disable` روی Policy 30؛ Session جدید ایجاد شود (Sessionهای قدیمی همان می‌مانند؛ Clear). پس از آزمون enable.

#### مثال متوسط — انتخاب مدل

نیاز: 4 Gbps ترافیک با IPS+AV، ۱۰٪ رشد، N+1 HA.

``` text
Required = 4 x 1.1 = 4.4 Gbps (NGFW)
Model A NGFW 3 Gbps  -> no
Model B NGFW 6 Gbps  -> ok (headroom 6/4.4 = 1.36)
```

#### مثال سخت — SSL Inspection

۹۰٪ ترافیک رمز است. SSL Inspection: 2 Gbps. با 4 Gbps ترافیک و ۹۰٪ رمز:

``` text
Encrypted traffic = 4 x 0.9 = 3.6 Gbps > SSL inspection capacity 2 Gbps
```

باید Inspection را فقط روی دسته‌های پرریسک (Exemption)، یا مدل بزرگ‌تر. اندازه‌گیری با iperf و `diagnose sys top`.

#### مثال سخت — Debug Flow بی‌خروجی

فقط بسته‌ی اول Session دیده می‌شود؛ بقیه Offload. برای دیدن همه: خاموش‌کردن Offload موقتاً یا Sniffer روی Interface بالادست. در VM (بدون NPU) این مسئله نیست؛ پس رفتار Lab با دستگاه واقعی متفاوت است.

### Lab هدایت‌شده (اجرا نشده)

۱) `session list` روی دستگاه سخت‌افزاری و دیدن `npu info` ۲) Offload خاموش و مقایسه‌ی Sniffer ۳) مقایسه‌ی Throughput با/بدون UTM (iperf) و جدول ظرفیت. در VM: مفهومی.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Sniffer ناقص | Offload | موقتاً خاموش |
| CPU بالا | UTM/Inspection | Profile/مدل |
| Debug flow بی‌خروجی | Offload | بسته‌ی اول |
| Throughput کم | UTM Offload نمی‌شود | مدل |

### جمع‌بندی

NPU Sessionهای ساده را سخت‌افزاری عبور می‌دهد. Proxy-based UTM و SSL Inspection ظرفیت را کم می‌کنند؛ مدل را بر پایه‌ی Throughput با ویژگی‌های فعال انتخاب کنید. Offload را فقط موقت برای عیب‌یابی خاموش کنید.

### تمرین و ارزیابی

**ت1.** (ساده) NPU چه می‌کند؟ *(پاسخ: 12-9-ت1)*

**ت2.** (ساده) چرا Debug Flow ممکن است ترافیک را نبیند؟ *(پاسخ: 12-9-ت2)*

**ت3.** (متوسط) چرا IPS Throughput را کم می‌کند؟ *(پاسخ: 12-9-ت3)*

**ت4.** (متوسط) چرا عدد Throughput Datasheet برای انتخاب مدل کافی نیست؟ *(پاسخ: 12-9-ت4)*

**ت5.** (سخت) برنامه‌ی تست کنترل‌شده برای مقایسه‌ی Throughput با و بدون Profile بنویسید. *(پاسخ: 12-9-ت5)*

**م1.** Slow path و Fast path چه فرقی دارند؟ *(پاسخ: 12-9-م1)*

**Q1.** Quick quiz (English): Why can offloaded traffic be missing from debug flow output? *(پاسخ: 12-9-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NPU | Network Processor Unit | پردازنده‌ی شبکه‌ی سخت‌افزاری |
| CP | Content Processor | پردازنده‌ی محتوا/رمز |
| ASIC | Application-Specific Integrated Circuit | مدار مجتمع اختصاصی |
| Offload | Session offload | واگذاری Session به سخت‌افزار |

- *Offloaded sessions bypass the CPU for forwarding.* ← Sessionهای Offloadشده ارسال را بدون CPU انجام می‌دهند.
- *Disable offload only temporarily when debugging.* ← Offload را فقط موقت و برای Debug غیرفعال کنید.

### منابع

- Fortinet Docs: [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow) و بخش Hardware acceleration در Administration Guide 7.0 (مدل خود را بررسی کنید).
- Fortinet: FortiGate datasheet مدل مورد استفاده.

<a id="l-12-7"></a>

## درس 12-7 — آزمون پایان فصل ۱۲ و تحلیل خطا: مدیریت قفل‌شده، Route اشتباه و Interface

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۰ تا ۱۲-۶ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. دلیل قفل‌شدن از مدیریت و راه‌های پیشگیری را بگویید.
2. `cfg-save revert` را فعال و رفتار آن را آزمون کنید.
3. روش تغییر ایمن (Session دوم، Backup، Revert) را اجرا کنید.
4. با Console بازگشت از قفل را تمرین کنید.
5. آزمون پایان فصل ۱۲ را مستند کنید.
6. گزارش تحلیل خطا بنویسید.

### چرا باید یاد بگیریم؟

رایج‌ترین حادثه‌ی خودساخته: ادمین با تغییر `allowaccess`، Route یا Policy خودش را از مدیریت قفل می‌کند و باید به محل برود یا Console بخواهد. روش ایمن در شبکه‌های حرفه‌ای «تغییر با بازگشت خودکار» است: اگر تأیید نکردید، دستگاه خودش به وضع قبل برمی‌گردد. مثل نصب نرم‌افزار با «بازگرداندن خودکار» در Windows. در این درس این رفتار را تمرین و مستند می‌کنید.

### cfg-save revert

``` text
config system global
 set cfg-save revert
 set cfg-revert-timeout 600
end
```

رفتار (طبق مستند FortiOS):

- با `revert`، تغییرات Config **فوراً اعمال** می‌شود ولی در Flash **ذخیره نمی‌شود** تا شما با `execute cfg save` تأیید کنید.
- اگر ظرف `cfg-revert-timeout` ثانیه تأیید نکنید، دستگاه Reboot و به آخرین Config ذخیره‌شده برمی‌گردد.

``` text
execute cfg save          (confirm and save)
execute cfg reload        (revert immediately)
```

اگر خودتان را قفل کنید، فقط منتظر بمانید (۱۰ دقیقه) یا از Console `execute cfg reload`.

### روش تغییر ایمن

1. Backup.
2. Session مدیریتی دوم باز (برای تست).
3. `cfg-save revert` فعال.
4. تغییر.
5. آزمون: ورود جدید از شبکه‌ی Mgmt؛ ping؛ Policy.
6. اگر درست بود `execute cfg save`.
7. اگر قفل شدید، صبر برای Revert.
8. ثبت در CHG.

### Console به‌عنوان آخرین راه

``` text
# physical/serial console
config system interface
 edit "mgmt"
  set allowaccess ping https ssh
 next
end
```

Console باید در دسترس باشد (Serial Server/Out-of-band). در VM: کنسول Hypervisor.

### مثال‌های حل‌شده

#### مثال ساده — Revert

تغییر `allowaccess` روی Interface مدیریتی به `ping` فقط؛ GUI قطع. با `cfg-save revert` و ۶۰۰ ثانیه: پس از ۱۰ دقیقه دستگاه بازمی‌گردد و GUI برمی‌گردد.

#### مثال متوسط — آزمون

۱) `cfg-revert-timeout 120` برای آزمون ۲) allowaccess عمداً تغییر ۳) صبر ۲ دقیقه ۴) دستگاه Reboot و بازگشت ۵) ثبت زمان واقعی. نتیجه: زمان بازگشت ≈ ۲ دقیقه + Reboot.

#### مثال متوسط — تأیید

پس از تغییر Route، ping به Gateway و ورود جدید موفق؛ `execute cfg save` و Log: «config saved». بدون این، با Reboot تغییر از بین می‌رفت.

#### مثال سخت — حذف Default Route

کارآموز Default Route را حذف کرد؛ GUI از راه دور قطع (چون مدیریت از اینترنت بود). راه: Console، Route بازگردانی. درس‌ها: مدیریت فقط از Mgmt؛ Revert؛ CHG؛ Backup.

#### مثال سخت — تحلیل خطا

علت اصلی: عدم Revert و مدیریت روی WAN. اقدامات اصلاحی: ۱) `cfg-save revert` استاندارد کار ۲) Mgmt جدا ۳) Console/OOB ۴) Checklist پیش از تغییر ۵) آموزش.

**Rubric:** برنامه‌ریزی ۲۰، اجرا ۳۰، Rollback ۲۵، Evidence ۱۵، گزارش ۱۰.

### Lab هدایت‌شده (اجرا نشده)

1. فعال‌سازی revert (۱۲۰ ثانیه).
2. تغییر عمدی allowaccess و مشاهده‌ی بازگشت.
3. Console و بازگردانی دستی.
4. گزارش.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| قفل مدیریت | allowaccess/Route | صبر Revert/Console |
| Revert نشد | Timeout زیاد | کم |
| ذخیره‌ی ناخواسته | `cfg save` | دقت |
| Console نیست | OOB | تهیه |

### جمع‌بندی

برای تغییر پرریسک `cfg-save revert` فعال کنید، Session دوم باز، تست و سپس `execute cfg save`. Console راه آخر است. مستند و درس‌آموخته‌ها را ثبت کنید.

### تمرین و ارزیابی

**ت1.** (ساده) راه نجات مدیریت قفل؟ *(پاسخ: 12-7-ت1)*

**ت2.** (ساده) ARP incomplete یعنی؟ *(پاسخ: 12-7-ت2)*

**ت3.** (متوسط) چرا Distance مهم است؟ *(پاسخ: 12-7-ت3)*

**ت4.** (متوسط) پیشگیری از قفل‌شدن؟ *(پاسخ: 12-7-ت4)*

**ت5.** (سخت) دو عیب همزمان؟ *(پاسخ: 12-7-ت5)*

**ت6.** (سخت، طراحی) Runbook تغییر Interface. *(پاسخ: 12-7-ت6)*

**Q1.** Quick quiz (English): How can you regain management access after a bad allowaccess change? *(پاسخ: 12-7-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ARP | Address Resolution Protocol | تبدیل IP به MAC |

- *Keep console access ready before risky changes.* ← پیش از تغییر پرریسک کنسول را آماده نگه دارید.

### کارت Lab

**کارت Lab:** آزمون فصل ۱۲ (اجرا نشده). **Evidence:** `03-ops/fgt-asbuilt-1.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Interfaces; Routing

### ضمیمه: پرونده‌ی کامل حل‌شده — «بعد از تغییر Interface دیگر وارد فایروال نمی‌شوم»

**ورودی (گزارش):** مدیر شبکه ساعت ۲۳:۱۰ allowaccess روی port2 را ویرایش کرده و اتصال SSH/HTTPS قطع شده؛ ping به 10.99.0.1 جواب می‌دهد.

**گام ۱ — تعریف علامت:** ping ok (لایه‌ی ۳ سالم)؛ https/ssh نه ⇒ مشکل Local-in یا allowaccess، نه لینک.

**گام ۲ — اقدام اضطراری:** اتصال از کنسول (نه از شبکه).

``` text
config system interface
 edit "port2"
  set allowaccess https ssh ping
 next
end
```

**گام ۳ — Verification:** `show system interface port2` سپس ورود از شبکه با https. انتظار: صفحه‌ی ورود باز می‌شود.

**گام ۴ — RCA کوتاه:**

``` text
Cause    : allowaccess overwritten with 'ping' only (set replaces the list)
Impact   : management lost for 14 min
Fix      : restored via console
Prevent  : change management interface only with console ready + scheduled revert
```

**درس:** در CLI فرمان `set allowaccess` کل فهرست را جایگزین می‌کند (نه افزودن)؛ برای افزودن از `append` استفاده کنید (`Unverified` در 7.0.3): `append allowaccess https`.

<a id="l-12-10"></a>

## درس 12-10 — FortiGate در لایه‌ی ۲: Transparent Mode، Virtual Wire Pair و Software Switch

**فصل 12 · درس افزوده برای انطباق با سرفصل رسمی NSE 4 (FortiOS 7.0): «Configure FortiGate interfaces or VDOMs to operate as Layer 2 devices» · پیش‌نیاز: ۱۲-۰، ۱۲-۲، ۱۲-۳**

> **وضعیت:** نظری/مستندی؛ FortiOS 7.0.3 نامی (بوت نشده)؛ دستورها `Unverified`؛ Lab اجرا نشده.

### ۱) این درس درباره چیست و چرا باید یاد بگیریم؟

**چه چیزی یاد می‌گیریم:** سه روش برای اینکه FortiGate مثل «سوییچ/سیم» رفتار کند: Transparent Mode (VDOM)، Virtual Wire Pair و Software Switch.

**چرا لازم است؟** فرض کنید شبکه‌ی موجودی دارید با آدرس‌دهی ثابت، و می‌خواهید فایروال را بدون تغییر IP و Route بین سوییچ و روتر بگذارید. اگر فایروال در حالت Route/NAT باشد باید آدرس‌ها و مسیرها را عوض کنید. اگر در حالت L2 باشد، مثل یک «سیم هوشمند» وارد می‌شود: ترافیک را بازرسی می‌کند ولی IP/Routing را عوض نمی‌کند. این سناریو در آزمون NSE4 هم آمده است.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا FortiGate در لایه‌ی ۲؟** گاهی باید فایروال را بدون تغییر آدرس‌دهی و Route وارد شبکه‌ی موجود کرد. در حالت Transparent یا Virtual Wire فایروال مثل «سیم هوشمند» رفتار می‌کند: ترافیک را بازرسی می‌کند ولی IP/Routing را عوض نمی‌کند.

**سه روش:** Transparent (VDOM Bridge با IP مدیریتی)، Virtual Wire Pair (دقیقاً دو Interface)، Software Switch (چند Interface در یک LAN L3).

**جمع‌بندی اصلی درس:** #### ۲-۱) حالت‌های عملکرد هر VDOM

| Mode | رفتار |
|---|---|
| NAT/Route (پیش‌فرض) | Interfaceها L3 با IP؛ Routing و NAT |
| Transparent | فایروال مثل Bridge L2؛ یک IP مدیریتی؛ بدون Routing/NAT معمول |

در Transparent، فایروال MAC آدرس‌ها را یاد می‌گیرد و فریم‌ها را بین Interfaceها Forward می‌کند ولی Policy و UTM را اعمال می‌کند.

#### ۲-۲) Virtual Wire Pair

دو Interface که مثل یک «سیم» به هم وصل می‌شوند. هر ترافیک وارد شده از یکی از دو Interface، از دیگری خارج می‌شود؛ بدون Learning MAC و بدون IP. نیاز به Policy بین دو Interface دارد.

#### ۲-۳) Software Switch

چند Interface که در یک دامنه‌ی L2 (یک Bridge) قرار می‌گیرند و **یک IP مشترک** روی Interface سوییچ می‌گیرند. در حالت NAT/Route کار می‌کند و برای ساخت یک LAN از چند پورت مفید است. (در مدل‌های دارای Hardware Switch، پورت‌های داخلی با چیپ سخت‌افزاری سوییچ می‌شوند.)

#### ۲-۴) مقایسه

| معیار | Transparent | Virtual Wire Pair | Software Switch |
|---|---|---|---|
| IP روی Interface | فقط IP مدیریتی | ندارد | IP روی Switch Interface |
| Routing/NAT | ندارد (L2) | ندارد | دارد |
| مقیاس Interface | چند | دقیقاً 2 | چند |
| کاربرد | درج فایروال بدون تغییر IP | بازرسی بین دو نقطه (مثلاً IPS Inline) | یک LAN از چند پورت |

### ۳) دستورها (Unverified)

**Transparent Mode**

``` text
config system settings
 set opmode transparent
 set manageip 192.168.1.99/24
 set gateway 192.168.1.1
end
```

هشدار: تغییر Mode ممکن است Config را پاک/ناسازگار کند؛ ابتدا Backup بگیرید.

**Virtual Wire Pair**

``` text
config system virtual-wire-pair
 edit "VWP1"
  set member "port3" "port4"
 next
end
config firewall policy
 edit 100
  set name "VWP-INSPECT"
  set srcintf "port3"
  set dstintf "port4"
  set srcaddr "all"
  set dstaddr "all"
  set service "ALL"
  set action accept
  set logtraffic all
 next
end
```

(برای جهت مقابل هم Policy لازم است.)

**Software Switch**

``` text
config system switch-interface
 edit "SW-LAN"
  set vdom "root"
  set member "port5" "port6"
  set type switch
 next
end
config system interface
 edit "SW-LAN"
  set ip 10.60.0.1 255.255.255.0
  set allowaccess ping
 next
end
```

### ۴) مثال‌های حل‌شده از ساده به سخت

**ساده — کدام حالت؟** می‌خواهیم بین سوییچ هسته و روتر لبه یک فایروال را بدون تغییر IP قرار دهیم ⇒ Transparent یا Virtual Wire.

**متوسط — تصمیم.** فقط دو پورت و نیاز به IPS روی ترافیک ⇒ Virtual Wire (ساده‌تر). اگر چند VLAN و Management IP لازم است ⇒ Transparent.

**سخت — حلقه‌ی L2.** پس از درج فایروال Transparent بین دو سوییچ، شبکه کند و Broadcast زیاد شد.

1. دو مسیر L2 موازی بین سوییچ‌ها (یکی از فایروال، دیگری مستقیم) ⇒ حلقه.
2. STP: فایروال به‌صورت پیش‌فرض BPDU را عبور نمی‌دهد؛ تنظیم `stpforward` (روی Interface) تا STP حلقه را ببیند.
3. با `show spanning-tree` روی سوییچ‌ها بررسی کنید.
4. یا یکی از مسیرها را حذف کنید.

``` text
config system interface
 edit "port3"
  set stpforward enable
 next
end
```

### ۵) Lab (اجرا نشده)

#### مثال ساده

دو پورت و نیاز به IPS Inline: Virtual Wire Pair.

#### مثال متوسط — مقایسه

Transparent برای چند VLAN و IP مدیریتی؛ Software Switch برای ساخت LAN از چند پورت با Gateway.

#### مثال سخت — حلقه

درج فایروال بین دو سوییچ با مسیر موازی حلقه ساخت؛ `stpforward enable` یا حذف مسیر اضافه.

#### مثال‌های اصلی درس (مرور)

FortiGate VM با دو پورت: یک بار Virtual Wire و یک بار Transparent؛ ping بین دو سمت با IP یکسان و Log Policy را ببینید.

### ۶) اصطلاحات این درس

| اصطلاح | شکل کامل | معنی |
|---|---|---|
| VDOM | Virtual Domain | دامنه‌ی مجازی |
| STP | Spanning Tree Protocol | جلوگیری از حلقه‌ی L2 |
| BPDU | Bridge Protocol Data Unit | پیام STP |
| VLAN | Virtual LAN | شبکه‌ی محلی مجازی |
| NAT | Network Address Translation | ترجمه‌ی آدرس |

### ۷) تمرین‌ها

**ت1.** (ساده) Transparent Mode چه تفاوتی با NAT/Route دارد؟ *(پاسخ: 12-10-ت1 در بخش «پاسخ‌ها» انتهای فصل)*

**ت2.** (ساده) Virtual Wire Pair چند Interface دارد؟ *(پاسخ: 12-10-ت2 در بخش «پاسخ‌ها» انتهای فصل)*

**ت3.** (متوسط) چرا Software Switch IP دارد ولی Virtual Wire نه؟ *(پاسخ: 12-10-ت3 در بخش «پاسخ‌ها» انتهای فصل)*

**ت4.** (سخت) پس از درج فایروال Transparent حلقه ایجاد شد؛ علت و رفع. *(پاسخ: 12-10-ت4 در بخش «پاسخ‌ها» انتهای فصل)*

### ۸) English Corner

- *In transparent mode the FortiGate forwards frames like a bridge but still applies firewall policies.*
- *A virtual wire pair connects exactly two interfaces.*
- **Q1.** Which mode lets you insert a FortiGate without changing IP addressing? *(پاسخ: 12-10-Q1 در بخش «پاسخ‌ها» انتهای فصل)*

---

<a id="l-12-11"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: جدول عیب‌یابی سریع — حالت‌های Layer 2

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| حلقه پس از درج فایروال | `show spanning-tree` سوییچ‌ها | BPDU عبور نمی‌کند؛ `stpforward` یا حذف مسیر موازی |
| ترافیک VWP رد می‌شود | Policy دو جهت | Policy برای یک جهت؛ افزودن جهت مقابل |
| Transparent: دسترسی مدیریتی نیست | `manageip`/gateway | IP مدیریتی یا allowaccess |
| Software Switch بدون ارتباط بین پورت‌ها | Policy intra-switch | تنظیم intra-switch-policy |

## درس 12-11 — Fortinet Security Fabric: معماری، اتصال FortiGateها و Automation

**فصل 12 · درس افزوده برای انطباق با سرفصل رسمی NSE 4 (FortiOS 7.0): «Implement the Fortinet Security Fabric» · پیش‌نیاز: ۱۲-۱، ۲۶-۰**

> **وضعیت:** نظری/مستندی؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ بخش‌هایی به لایسنس نیاز دارند (Needs-License)؛ Lab اجرا نشده.

### ۱) این درس درباره چیست و چرا باید یاد بگیریم؟

**چه چیزی یاد می‌گیریم:** Security Fabric چیست، چطور چند FortiGate به هم وصل می‌شوند (Root و Downstream)، چه چیزی در Fabric به اشتراک گذاشته می‌شود و Automation Stitch چیست.

**چرا لازم است؟** اگر هر فایروال/سوییچ/AP یک جزیره باشد، مهاجم از شکاف بین جزایر عبور می‌کند. Security Fabric مثل «سیستم هشدار یکپارچه‌ی ساختمان» است: اگر دوربین یک طبقه خطر ببیند، در همه‌ی طبقات واکنش نشان داده می‌شود (مثلاً دستگاه آلوده در همه‌ی فایروال‌ها قرنطینه شود).

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Security Fabric؟** اگر هر محصول امنیتی جزیره باشد، مهاجم از شکاف بین جزایر عبور می‌کند. Fabric آنها را یکپارچه می‌کند: Root و Downstream FortiGate، FortiAnalyzer، Switch/AP و غیره، با دید و واکنش مشترک (Automation Stitch).

**جمع‌بندی اصلی درس:** #### ۲-۱) اجزا

- **Root FortiGate:** بالاترین FortiGate Fabric؛ دید کامل توپولوژی.
- **Downstream FortiGate:** FortiGateهایی که به Root (یا میانی) وصل می‌شوند.
- **سایر محصولات:** FortiAnalyzer (Log)، FortiManager، FortiSwitch/FortiAP، FortiClient EMS، FortiSandbox و ...
- **Fabric Connectors:** اتصال به سرویس‌های دیگر (Cloud، SDN، Threat Feed، FSSO).

#### ۲-۲) چه چیزی دیده/اجرا می‌شود

1. **Topology Views:** نقشه‌ی فیزیکی و منطقی.
2. **Security Rating:** امتیازدهی تنظیمات بر اساس بهترین‌روش‌ها (بخشی با لایسنس).
3. **Automation (Stitch):** ترکیب Trigger (رویداد) + Action (واکنش).
4. **Single Pane of Glass:** مدیریت/مشاهده‌ی مرکزی.

#### ۲-۳) Automation Stitch

``` text
Trigger : Compromised host detected (IOC) / Event log / Config change
Action  : Quarantine host / Send email / Run CLI script / Webhook
```

مثال: «اگر FortiClient EMS میزبانی را آلوده اعلام کرد، Address آن را در Group قرنطینه بگذار تا Policy آن را ببندد.» (EMS: Needs-License).

### ۳) دستورها (Unverified)

**Root**

``` text
config system csf
 set status enable
 set group-name "CORP-FABRIC"
 set group-password ***
end
```

**Downstream**

``` text
config system csf
 set status enable
 set group-name "CORP-FABRIC"
 set group-password ***
 set upstream-ip 10.50.0.1
end
```

سپس روی Root در GUI (Security Fabric ← Fabric Connectors/Physical Topology) دستگاه Downstream را **Authorize** کنید. ارتباط Fabric روی پورت مخصوص (طبق مستند، TCP/8013) انجام می‌شود و باید Policy/Allowaccess لازم باز باشد (`set allowaccess fabric` روی Interface مربوطه).

``` text
config system interface
 edit "port5"
  set allowaccess ping fabric
 next
end
```

بررسی:

``` text
get system status
diagnose sys csf downstream
```

### ۴) مثال‌های حل‌شده از ساده به سخت

**ساده — تشخیص نقش.** دو FortiGate: HQ و Branch. HQ Root؛ Branch Downstream با `upstream-ip` برابر HQ.

**متوسط — Stitch ساده.** Trigger: «Configuration changed»؛ Action: ارسال ایمیل به NOC. فایده: هر تغییر خارج از CHG فوری دیده می‌شود (ارتباط با درس ۳۲-۰).

**سخت — Downstream «Pending» می‌ماند.**

1. Root روی `fabric` در allowaccess Interface رو به Downstream مجاز؟
2. `group-name` و `group-password` یکسان؟
3. Downstream به `upstream-ip` می‌رسد؟ (`execute ping`، Policy Local-in)
4. ساعت/NTP برای گواهی‌ها.
5. در Root Authorize شده؟

### ۵) Lab (اجرا نشده)

#### مثال ساده

HQ = Root؛ Branch = Downstream با `upstream-ip`.

#### مثال متوسط — Stitch

Trigger: تغییر Config؛ Action: ایمیل به NOC.

#### مثال سخت — Downstream در Pending

Authorize در Root، `allowaccess fabric`، group-name/password، ارتباط به upstream-ip، NTP.

#### مثال‌های اصلی درس (مرور)

دو FortiGate VM؛ ساخت Fabric و دیدن Topology؛ ساخت یک Stitch ایمیل.

### ۶) اصطلاحات این درس

| اصطلاح | شکل کامل | معنی |
|---|---|---|
| CSF | Cooperative Security Fabric | نام داخلی Fabric در CLI |
| EMS | Endpoint Management Server | مدیریت FortiClient |
| IOC | Indicator of Compromise | نشانه‌ی آلودگی |
| NOC | Network Operations Center | مرکز عملیات شبکه |

### ۷) تمرین‌ها

**ت1.** (ساده) Root و Downstream چیست؟ *(پاسخ: 12-11-ت1 در بخش «پاسخ‌ها» انتهای فصل)*

**ت2.** (ساده) Stitch از چه دو بخش ساخته می‌شود؟ *(پاسخ: 12-11-ت2 در بخش «پاسخ‌ها» انتهای فصل)*

**ت3.** (متوسط) سه شرط اتصال Downstream. *(پاسخ: 12-11-ت3 در بخش «پاسخ‌ها» انتهای فصل)*

**ت4.** (سخت) Downstream در حالت Pending؛ پنج گام عیب‌یابی. *(پاسخ: 12-11-ت4 در بخش «پاسخ‌ها» انتهای فصل)*

### ۸) English Corner

- *The root FortiGate must authorize each downstream device joining the Security Fabric.*
- *An automation stitch combines a trigger and an action.*
- **Q1.** What is the purpose of the Security Rating feature? *(پاسخ: 12-11-Q1 در بخش «پاسخ‌ها» انتهای فصل)*

---

## پاسخ‌های فصل 12

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 12-1

**12-1-ت1** — `get system status`؛ خروجی Version/Serial/License را دارد.

`get system status` نسخه (Version/Build)، Serial، License، Hostname و Operation Mode را نشان می‌دهد؛ اولین دستور برای تأیید نسخه‌ی دستگاه.

**12-1-ت2** — زمان صحیح برای Log، گواهی و Correlation در SIEM لازم است.

NTP زمان صحیح می‌دهد؛ Log، گواهی TLS و Correlation در SIEM به آن وابسته‌اند؛ اختلاف چند دقیقه ترتیب رویدادها را به‌هم می‌ریزد.

**12-1-ت3** — دستورها و رفتارها بین نسخه‌ها فرق دارند (مثلاً SD-WAN/SSL-VPN)؛ بدون تطبیق ممکن است دستور خطا بدهد یا رفتار متفاوت باشد.

**12-1-ت4** — فوراً قوی کنیم و در ریپو ذخیره نکنیم.

رمز پیش‌فرض را فوراً به رمز قوی تغییر دهید و در ریپو/سند ذخیره نکنید؛ رمز در Vault و تغییر نام/غیرفعال‌سازی admin پیش‌فرض.

**12-1-ت5** — ثبت، مقایسه با Release Notes، علامت Unverified، عدم Downgrade بدون Backup.

نسخه‌ی v7.2 به‌جای 7.0.3: نسخه را ثبت، با Release Notes مقایسه، دستورهای مشکوک را `Unverified` علامت بزنید و بدون Backup و تأیید Downgrade نکنید.

**12-1-ت6** — نسخه، سریال، License، hostname، NTP، DNS، رمز، Backup اولیه.

برگه‌ی اولین بوت: نسخه، سریال، License، Hostname، NTP، DNS، رمز قوی، Backup اولیه و ثبت در Inventory.

**12-1-Q1** — get system status.

`get system status` shows the version, serial number and license state.

### پاسخ‌های بازنویسی عمیق درس 12-2

**12-2-ت1** — فهرست سرویس‌های مدیریتی/تشخیصی که روی آن Interface به خود FortiGate اجازه‌ی اتصال دارند (https، ssh، ping، ...). هرچه بیشتر، سطح حمله بیشتر.

**12-2-ت2** — Interface منطقی با vlanid که روی یک پورت فیزیکی/Aggregate ساخته می‌شود تا چند شبکه‌ی جدا روی یک لینک Trunk داشته باشیم.

VLAN Sub-interface یک Interface منطقی با vlanid است که روی پورت فیزیکی یا Aggregate ساخته می‌شود تا چند شبکه‌ی جدا روی یک لینک Trunk داشته باشیم.

**12-2-ت3** — پنل مدیریت از اینترنت قابل Brute-force و سوءاستفاده از آسیب‌پذیری می‌شود؛ مدیریت باید فقط از شبکه‌ی Mgmt و با Trusted host باشد.

**12-2-ت4** — Trunk نبودن پورت سوییچ، VLAN غیرمجاز، vlanid اشتباه؛ شاهد: ARP incomplete.

لینک up ولی VLAN کار نمی‌کند: Trunk نبودن پورت سوییچ، VLAN غیرمجاز یا vlanid اشتباه؛ شاهد: ARP incomplete. رفع روی سوییچ و آزمون ping.

**12-2-ت5** — حذف https/ssh از WAN، Mgmt جدا، Trusted host، Local-in policy، MFA، بررسی Log و آزمون nmap.

حذف https/ssh از WAN، مدیریت فقط از Mgmt با Trusted host، Local-in policy، MFA، بررسی Log و آزمون nmap از اینترنت (پورت‌های 22/443 بسته).

**12-2-ت6** — جدول: نام، IP، Role، allowaccess، VLAN، Zone؛ Mgmt فقط https/ssh با Trusted host.

جدول Interfaceهای شعبه: نام، IP، Role، allowaccess، VLAN و Zone؛ Mgmt فقط https/ssh با Trusted host؛ WAN بدون مدیریت.

**12-2-Q1** — allowaccess.

`allowaccess` controls which management services are reachable on the interface.

### پاسخ‌های بازنویسی عمیق درس 12-3

**12-3-ت1** — یک نقطه‌ی تعریف؛ تغییر آدرس در یک جا همه‌ی Policyها را به‌روز می‌کند و Policy خوانا می‌شود.

Address Object یک نقطه‌ی تعریف است؛ تغییر آدرس سرور در یک جا همه‌ی Policyها را به‌روز می‌کند و Policy خواناتر می‌شود.

**12-3-ت2** — ترافیک بین Interfaceهای همان Zone را بدون Policy رد می‌کند.

`intrazone deny` ترافیک بین Interfaceهای همان Zone را بدون Policy صریح رد می‌کند؛ امن‌تر از allow.

**12-3-ت3** — چون Zone جایگزین آن Interface‌ها در Policy است.

Interface عضو Zone در Policy مستقیماً انتخاب نمی‌شود چون Zone جایگزین آن است؛ باید Zone را انتخاب کرد.

**12-3-ت4** — وابستگی به DNS؛ اگر DNS خراب شود Policy کار نمی‌کند.

Object FQDN به DNS وابسته است؛ اگر Resolver خراب شود Policy کار نمی‌کند؛ فقط جایی که DNS مطمئن است.

**12-3-ت5** — Export، Where-used، تأیید مالک، Backup، حذف/ادغام، استاندارد نام.

ممیزی ۲۰۰ Object: Export، Where-used، تأیید مالک، Backup، حذف/ادغام، اعمال استاندارد نام؛ معیار: صفر Object بی‌مالک.

**12-3-ت6** — جدول پیشوندها، مالک، Comment، مثال.

استاندارد نام‌گذاری: NET-/HOST-/SRV-/RNG-/FQDN-/TCP-/UDP-/GRP-/ZN- همراه Comment مالک و دلیل.

**12-3-Q1** — Zones group interfaces with the same role so policies are shorter and easier to maintain.

Zones group interfaces with the same role so policies stay short and easy to maintain.

### پاسخ‌های بازنویسی عمیق درس 12-4

**12-4-ت1** — اعتبار منبع Route؛ کمتر بهتر؛ بین Routeهای مختلف به یک مقصد انتخاب می‌کند.

Distance اعتبار منبع Route است (کمتر بهتر) و بین Routeهای مختلف به یک مقصد انتخاب می‌کند؛ Static پیش‌فرض ۱۰ در FortiOS.

**12-4-ت2** — Priority بین Routeهای هم‌Distance تعیین‌کننده است.

Priority بین Routeهای هم‌Distance به یک مقصد تعیین‌کننده است (کمتر ترجیح)؛ دو Default با Distance برابر و Priority متفاوت یعنی Primary/Backup.

**12-4-ت3** — Gateway ممکن است زنده باشد ولی ISP قطع؛ Monitor به مقصد خارجی Route را غیرفعال می‌کند.

Gateway ISP ممکن است زنده باشد ولی ISP قطع؛ Link-monitor به مقصد خارجی (مثل 8.8.8.8) Route را غیرفعال می‌کند و Failover می‌شود.

**12-4-ت4** — قبل از جدول مسیر.

Policy Route قبل از جدول مسیر اعمال می‌شود؛ پس مسیر «عجیب» اغلب از `diagnose firewall proute list` پیداست.

**12-4-ت5** — RPF و Route برگشت؛ هماهنگی NAT/Route؛ آزمون.

پس از Policy Route برخی Sessionها قطع می‌شوند: RPF و Route برگشت؛ NAT و Route باید هماهنگ باشند؛ آزمون Debug flow.

**12-4-ت6** — Distance برابر، Priority 1/10، Link-monitor با failtime/recoverytime، آزمون قطع.

دو ISP: Distance برابر، Priority 1/10، Link-monitor با failtime/recoverytime مناسب، آزمون قطع ISP و Failover.

**12-4-Q1** — Priority.

Priority breaks the tie between static routes with equal distance.

### پاسخ‌های بازنویسی عمیق درس 12-5

**12-5-ت1** — کنترل دسترسی بر اساس نقش؛ هر مدیر فقط به اندازه‌ی نقشش دسترسی دارد.

RBAC کنترل دسترسی نقش‌محور است: هر مدیر فقط به اندازه‌ی نقشش دسترسی دارد (Super، Network، ReadOnly).

**12-5-ت2** — ورود Admin را به آدرس‌های مشخص محدود می‌کند.

Trusted host ورود Admin را به آدرس‌های مشخص محدود می‌کند؛ حتی با رمز لورفته از بیرون نمی‌توان وارد شد.

**12-5-ت3** — پس از چند تلاش ناموفق حساب/مبدأ را موقتاً قفل می‌کند و Brute-force را کند می‌کند.

Lockout پس از چند تلاش ناموفق حساب یا مبدأ را موقتاً قفل می‌کند و Brute-force را کند می‌کند.

**12-5-ت4** — دسترسی اضطراری وقتی MFA/SSO در دسترس نیست؛ با Alert و Rotate.

Break-glass حساب اضطراری برای وقتی که MFA/SSO در دسترس نیست؛ رمز طولانی در گاوصندوق، Alert روی استفاده و Rotate پس از آن.

**12-5-ت5** — Lockout، Local-in، Trusted host، Alert و Log.

Brute-force از یک IP: Lockout، Local-in، Trusted host، Alert و بررسی Log؛ مدیریت را از WAN حذف کنید.

**12-5-ت6** — طبق متن.

سه سطح: Super (۲ نفر با MFA)، Network Admin (fwgrp/netgrp رایت)، ReadOnly (NOC)؛ Break-glass جدا.

**12-5-Q1** — The source addresses from which an administrator may log in.

A trusted host restricts the source addresses from which an administrator may log in.

### پاسخ‌های بازنویسی عمیق درس 12-6

**12-6-ت1** — حاوی رمزها و کلیدهاست و افشا یعنی نفوذ.

Backup حاوی رمزها و کلیدهاست؛ افشای آن یعنی نفوذ؛ باید رمزگذاری و محدود شود.

**12-6-ت2** — ابزار Fortinet که مسیر نسخه‌های پشتیبانی‌شده را می‌دهد.

Upgrade Path Tool ابزار Fortinet است که مسیر نسخه‌های پشتیبانی‌شده (و نسخه‌ی میانی) را می‌دهد.

**12-6-ت3** — Backup، Release Notes، Known Issues، Window، Rollback، نسخه‌ی فعلی.

پیش از Upgrade: Backup، Release Notes، Known Issues، Window، Rollback و نسخه‌ی فعلی/Path.

**12-6-ت4** — تا سرویس با Failover حفظ شود.

در HA ابتدا Secondary ارتقا می‌یابد تا با Failover سرویس حفظ شود و سپس Primary قبلی.

**12-6-ت5** — کنسول، Partition قبلی، Restore، گزارش.

Boot loop پس از Upgrade: کنسول، Boot از Partition قبلی، Restore Config در صورت نیاز و گزارش علت.

**12-6-ت6** — هدف، Window، Path، Backup، Rollback، آزمون، تأیید.

برنامه‌ی CHG Upgrade: هدف، Window، Path، Backup، Rollback، آزمون و تأیید.

**12-6-Q1** — Because a failed upgrade can cause outage and you must restore service quickly.

A failed upgrade can cause an outage, so a rollback must be planned in advance.

### پاسخ‌های بازنویسی عمیق درس 12-7

**12-7-ت1** — کنسول و بازگرداندن allowaccess.

قفل‌شدن مدیریت: از کنسول وارد شوید و allowaccess را بازگردانید (`set allowaccess https ssh ping`).

**12-7-ت2** — لایه‌ی ۲ مشکل دارد.

ARP incomplete یعنی لایه‌ی ۲ مشکل دارد (VLAN/Trunk/کابل)، نه Policy.

**12-7-ت3** — Route با Distance کمتر برنده می‌شود.

Route با Distance کمتر برنده می‌شود؛ پس Static اشتباه با Distance کوچک مسیر Default را می‌دزدد.

**12-7-ت4** — تغییر از Mgmt جدا، Rollback/زمان‌بندی، کنسول آماده.

پیشگیری: تغییر مدیریت از Mgmt جدا، Rollback/زمان‌بندی، کنسول آماده و Backup.

**12-7-ت5** — ابتدا لایه‌ی پایین‌تر.

دو عیب هم‌زمان: ابتدا لایه‌ی پایین‌تر (VLAN) و بعد Route؛ هر کدام جدا آزمون.

**12-7-ت6** — Backup، Window، کنسول، آزمون، Rollback.

Runbook تغییر Interface: Backup، Window، کنسول آماده، آزمون و Rollback.

**12-7-Q1** — Log in via the console and restore the setting.

Log in via the console and restore the management setting.

### پاسخ‌های درس افزوده‌ی 12-0 (فصل 12)

**12-0-ت1** — Ingress، RPF، Session lookup، DNAT، Route lookup، Policy lookup، Profiles، SNAT، ساخت Session، Egress.

**12-0-ت2** — Policy ID 0؛ Log: Denied by forward policy check (policy 0).

**12-0-ت3** — مقصد = IP داخلی (10.1.1.10) چون DNAT قبل از Policy انجام می‌شود (post-DNAT).

**12-0-ت4** — Route فقط مسیر را می‌دهد؛ Policy اجازه‌ی عبور را؛ بدون Policy Implicit deny می‌شود.

**12-0-ت5** — ۱) Debug Flow: Denied policy؟ ۲) RPF؟ ۳) Route به port1 هست؟ ۴) Offload باعث نبودن در Debug؟ ۵) NAT/Profile؟ ۶) لینک/ARP روی port1.

**12-0-ت6** — ۱) Route ناقص به مبدأ؛ ۲) Asymmetric (برگشت از Interface دیگر)؛ ۳) مسیر مبدأ به Interface دیگر اشاره می‌کند. اثبات: get router info routing-table details و Sniffer.

**12-0-م1** — بعد از Policy lookup (و بعد از Route/Profile).

**12-0-Q1** — No; reply packets match the existing session and skip policy lookup.


### پاسخ‌های درس افزوده‌ی 12-8 (فصل 12)

**12-8-ت1** — Transit، Local-in، Local-out.

**12-8-ت2** — allowaccess ping روی Interface.

**12-8-ت3** — Policy فقط Transit را کنترل می‌کند؛ SSH به فایروال Local-in است و با allowaccess/Local-in Policy/Trusted Host کنترل می‌شود.

**12-8-ت4** — Local-out با Source IP پیش‌فرض Interface خروجی (Tunnel) می‌رود که در Selector نیست؛ Source را به IP داخلی تغییر دهید.

**12-8-ت5** — allowaccess فقط روی Interface مدیریتی، Trusted Host برای Admin و Local-in Policy (accept از MGMT-NET، deny بقیه).

**12-8-ت6** — Route به سرور، Source IP، ping از CLI، Sniffer روی Interface خروجی، تنظیم syslog (server/port/status)، ACL سرور.

**12-8-م1** — فهرست IPهایی که Admin اجازه‌ی ورود از آن‌ها را دارد.

**12-8-Q1** — Local-in policies together with the interface administrative-access settings and trusted hosts.


### پاسخ‌های درس افزوده‌ی 12-9 (فصل 12)

**12-9-ت1** — Sessionهای ساخته‌شده را در سخت‌افزار ارسال می‌کند و CPU را سبک می‌کند.

**12-9-ت2** — چون ترافیک Offloadشده از مسیر CPU/Kernel نمی‌گذرد و Debug آن را نمی‌بیند.

**12-9-ت3** — بازرسی محتوا در CPU/CP انجام می‌شود و Offload را محدود می‌کند.

**12-9-ت4** — Datasheet معمولاً Firewall خام بدون UTM است؛ با Profile فعال Throughput کم می‌شود.

**12-9-ت5** — Baseline بدون Profile (iperf)، فعال‌کردن یک Profile، تکرار با همان بار و تعداد Session، ثبت CPU/Throughput/Latency، مقایسه.

**12-9-م1** — Slow path در CPU با بررسی کامل؛ Fast path Session موجود را سریع می‌فرستد (و NPU در سخت‌افزار).

**12-9-Q1** — Because offloaded packets are forwarded in hardware and never reach the CPU path that debug flow monitors.

### پاسخ‌های درس افزوده‌ی 12-10 (فصل 12)

**12-10-ت1** — در Transparent فایروال L2 است (Bridge با IP مدیریتی، بدون Routing/NAT معمول)؛ در NAT/Route فایروال L3 است با IP روی Interfaceها.

**12-10-ت2** — دقیقاً دو Interface.

**12-10-ت3** — Software Switch چند پورت را به یک LAN L3 تبدیل می‌کند و باید Gateway/IP داشته باشد؛ Virtual Wire فقط یک سیم L2 بین دو پورت است و Routing ندارد.

**12-10-ت4** — دو مسیر L2 موازی ساخت حلقه؛ فایروال BPDU را عبور نمی‌داد. رفع: `stpforward enable` یا حذف مسیر اضافه؛ تأیید با `show spanning-tree`.

**12-10-Q1** — Transparent mode (یا Virtual Wire Pair).

### پاسخ‌های درس افزوده‌ی 12-11 (فصل 12)

**12-11-ت1** — Root بالاترین FortiGate در Fabric با دید کامل توپولوژی؛ Downstream FortiGateهایی که به آن (یا یک میانی) وصل و توسط Root Authorize می‌شوند.

**12-11-ت2** — Trigger (رویداد) و Action (واکنش).

**12-11-ت3** — group-name/password یکسان، `upstream-ip` قابل‌دسترس و allowaccess `fabric` روی Interface، و Authorize در Root.

**12-11-ت4** — ۱) allowaccess fabric روی Root ۲) group-name/password ۳) ارتباط شبکه به upstream-ip ۴) NTP/زمان ۵) Authorize در Root.

**12-11-Q1** — It scores the configuration against best practices and recommends improvements.

---

# پایان بخش ۴ (فصل‌های ۱۰ تا ۱۲)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- Redistribution با Tag، ECMP، PBR، VRF-lite، تحلیل Asymmetric.
- مبانی فایروال: Stateful، Zone، Default Deny، مسیر بسته، MTU/MSS.
- FortiGate: بوت و نسخه، Interface/VLAN، Zone/Object، Routing، Admin، Backup (GUI و CLI).

## ۲) آزمون پایان سه فصل
**س1** — چرا Redistribution دوطرفه Tag می‌خواهد؟

**س2** — ECMP Per-flow یا Per-packet و اثر آن بر فایروال؟

**س3** — PBR کجا اعمال می‌شود و قبل/بعد از Route Table؟

**س4** — VRF چه می‌کند؟

**س5** — Asymmetric چرا Stateful را خراب می‌کند؟

**س6** — Stateless در برابر Stateful؟

**س7** — Local-in چیست؟

**س8** — MSS چگونه محاسبه می‌شود؟

**س9** — چرا نسخه‌ی Image را قبل از طراحی ثبت می‌کنیم؟

**س10** — Distance در برابر Priority در Static FortiGate؟

**س11** — Trusted Host چه خطری دارد؟

**س12** — چرا بکاپ Config را در Git نمی‌گذاریم؟


## ۳) پاسخ آزمون
- **س1:** جلوگیری از بازگشت مسیر و حلقه/Flap.
- **س2:** Per-flow؛ Session باید روی یک مسیر بماند.
- **س3:** Interface ورودی؛ قبل از Route Table.
- **س4:** جدول مسیریابی مستقل.
- **س5:** Session فقط یک جهت را می‌بیند.
- **س6:** Stateless هر بسته جدا؛ Stateful Session نگه می‌دارد.
- **س7:** ترافیک به خود فایروال.
- **س8:** MTU − 40.
- **س9:** قابلیت/دستور وابسته به نسخه است.
- **س10:** Distance بین منابع؛ Priority تای‌بریک.
- **س11:** قفل‌شدن از مدیریت.
- **س12:** Hash رمز/کلید دارد.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| کنترل مسیر | L3 | Walk + Tag |
| مبانی فایروال | L3 | G4 |
| Baseline FGT | L3 | As-Built (GUI+CLI) |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. FortiGate هنوز بوت نشده؛ همه‌ی دستورها/منوها آزمایش‌نشده. 2. VRF-lite/PBR/BGP روی vIOS آزمایش‌نشده. 3. عمق درس‌های فصل ۱۰–۱۲ کمتر از فصل‌های ۱–۸ است (فشرده‌تر).

## ۶) پیش‌نیازهای بخش بعد
بوت اول FortiGate با تأیید شما؛ Snapshot؛ تأیید `get system status`؛ ثبت تاریخ Evaluation.

## ۷) فهرست Lab و منابع مرتبط
`phase0a/FortiGate_Backup_Restore_Runbook.md` ، `phase0a/fortigate_eval_tracker.md` ، کارت‌های Lab همین فایل

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۱۲ |
| آخرین درس تکمیل‌شده | ۱۲-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۱۳ |
| فایل تولیدشده | `course/Course_Part_04_Chapters_10-12.md` |
