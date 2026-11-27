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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

#### مثال سخت — کنترل جایگزین

سرور قدیمی بدون Patch که نمی‌توان ارتقا داد: کنترل جبرانی: Segmentation شدید، فقط پورت لازم، IPS، پایش.

#### Lab

یک جدول دارایی/تهدید/کنترل برای شبکه‌ی خودتان بنویسید.

#### عیب‌یابی طراحی

| علامت | علت | رفع |
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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. وظیفه‌ی فایروال را در مدل لایه‌ها توضیح دهد.
2. Packet filter (Stateless)، Stateful و NGFW را مقایسه کند.
3. جدول State را برای TCP/UDP/ICMP شرح دهد.
4. یک ACL Stateless و یک Policy Stateful را برای یک سناریو مقایسه و اشکال ACL را پیدا کند.
5. محدودیت‌های هر نوع را بگوید.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا باید بدانیم فایروال چیست؟** تصور کنید ساختمانی دارید. قفل در ورودی (Router/ACL) فقط می‌پرسد «کارت دارید؟». نگهبان (Firewall) می‌پرسد «شما را قبلاً دیده‌ام؟ کسی شما را دعوت کرده؟ همراه شما کیست؟». فایروال دستگاهی است که ترافیک بین دو یا چند شبکه را بر اساس **سیاست** (Policy) مجاز یا ممنوع می‌کند.

**دو نسل**

1. **Stateless (بی‌حافظه):** مثل ACL. هر بسته را جداگانه بررسی می‌کند. چون حافظه ندارد، باید برای برگشت ترافیک هم قاعده بنویسید.
2. **Stateful (با حافظه):** برای هر اتصال یک «پرونده» (Session) می‌سازد. وقتی کاربر به وب می‌رود، فایروال ثبت می‌کند «10.10.0.5 به 198.51.100.8:443 رفت». بسته‌ی برگشت را با پرونده تطبیق می‌دهد و خودکار می‌پذیرد.

**چرا Stateful امن‌تر است؟** مهاجم نمی‌تواند بسته‌ی جعلی «ACK» بفرستد و عبور کند؛ چون پرونده‌ای برایش نیست. همچنین قواعد ساده‌تر می‌شود (فقط جهت آغاز اتصال).

**محدودیت‌های Stateful:** ظرفیت جدول Session، نیاز به مسیر متقارن، و هزینه‌ی CPU/حافظه.

**جمع‌بندی اصلی درس:** نگهبان ساختمان را تصور کنید. نگهبان نوع اول فقط لیست «مجاز/ممنوع» دارد و هر بار برگه را چک می‌کند (Stateless). نگهبان نوع دوم یادش می‌ماند چه کسی بیرون رفت و فقط جواب او را اجازه‌ی ورود می‌دهد (Stateful). نوع سوم داخل کیف هم نگاه می‌کند (NGFW).

### ۳) توضیح عمیق فنی

#### ۱) سه نسل

| نوع | تصمیم بر اساس | حافظه‌ی Session |
|---|---|---|
| Packet filter | Src/Dst IP، پورت، پروتکل | ندارد |
| Stateful | همان + وضعیت اتصال | دارد |
| NGFW | همان + برنامه، کاربر، محتوا | دارد |

#### ۲) چرا Stateless مشکل دارد

برای اجازه‌ی وب باید هم خروج به 443 و هم «برگشت از 443 به پورت‌های بالا» را باز کنید؛ یعنی هر کسی از بیرون با Source-port 443 وارد می‌شود.

``` text
access-list OUT permit tcp 10.0.0.0 0.0.0.255 any eq 443
access-list IN  permit tcp any eq 443 10.0.0.0 0.0.0.255 gt 1023
! the IN rule also admits crafted packets with source port 443
```

#### ۳) Stateful

اولین بسته (SYN) را با Policy بررسی می‌کند؛ اگر مجاز بود، ورودی در جدول State ساخته می‌شود: Src, Dst, پورت‌ها، پروتکل، وضعیت، Timeout. بسته‌های برگشتی با جدول مطابقت می‌کنند و بدون Policy جدید عبور می‌کنند.

``` text
Session: tcp 10.0.0.5:51000 -> 203.0.113.10:443  state=ESTABLISHED  timeout=3600
Return : tcp 203.0.113.10:443 -> 10.0.0.5:51000  matched to the session
```

#### ۴) UDP و ICMP

UDP اتصال ندارد؛ فایروال «شبه‌Session» با Timeout کوتاه می‌سازد. ICMP Echo Reply فقط در صورتی که Request قبلاً دیده شده باشد.

#### ۵) NGFW

بازرسی عمیق (IPS، Application Control، SSL Inspection، AV) نیازمند لایسنس و CPU است (Needs-License)؛ و خطر اشتباه بیشتر.

#### ۶) محدودیت

Stateful نمی‌داند داخل 443 چه می‌رود؛ جدول State محدود است (DoS با SYN Flood)؛ مسیر نامتقارن را نمی‌پسندد.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Stateless/Stateful/NGFW | مرز شبکه: Stateful؛ بازرسی عمیق فقط ترافیک ریسک‌دار |
| Timeout | طبق سرویس |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — تفاوت در یک نگاه

وب برای کاربر داخلی:

``` text
Stateless (ACL): permit tcp 10.10.0.0/24 any eq 443  AND  permit tcp any eq 443 10.10.0.0/24 established
Stateful       : allow 10.10.0.0/24 -> any : 443   (return traffic automatic)
```

#### مثال متوسط — حمله‌ی ACK

مهاجم بسته‌ی TCP با پرچم ACK به یک سرور داخلی می‌فرستد بدون Handshake. ACL با `established` آن را عبور می‌دهد؛ فایروال Stateful رد می‌کند چون Session ندارد (Log: `no session matched`). این نمونه‌ی ساده‌ی ACK Scan است.

#### مثال متوسط — جدول Session

``` text
Proto  Src                  Dst                  State        Timeout
tcp    10.10.0.5:49152      198.51.100.8:443     ESTABLISHED  3600
```

ورودی تا Timeout یا بسته‌شدن اتصال می‌ماند. پس بسته‌ی برگشت از 198.51.100.8:443 به 10.10.0.5:49152 می‌خورد و پذیرفته می‌شود.

#### مثال سخت — نامتقارن

SYN از فایروال A می‌گذرد و SYN-ACK از B می‌آید. B Session ندارد و Drop می‌کند؛ علامت: «اتصال بعضی وقت‌ها کار می‌کند». اثبات با Sniffer دوطرفه؛ رفع با طراحی متقارن (درس ۲۳).

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** کاربر 10.0.0.5 به 203.0.113.10:443 می‌رود؛ Session ساخته می‌شود و جواب بدون Policy دوم برمی‌گردد.

**متوسط (تحلیل):** ACL Stateless با `permit tcp any eq 443 ... gt 1023`: مهاجم با Source-port 443 به پورت 3389 داخل بسته می‌فرستد و می‌گذرد (چون dst>1023). راه: Stateful (`established`/Policy).

**سخت (طراحی):** سازمان وب را باز و RDP را بسته می‌خواهد؛ NGFW برای Application Control؛ ولی CPU کم: ابتدا Stateful+IPS روی ترافیک حساس؛ اندازه‌گیری Throughput قبل و بعد؛ معیار: افت < 30٪.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! FortiGate (Unverified in lab)
diagnose sys session list
diagnose sys session filter dst 203.0.113.10
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- Session برای جریان اجازه‌داده‌شده ساخته می‌شود.
- بسته‌ی برگشت بدون Policy جدید عبور می‌کند.
- بسته‌ی بدون SYN رد می‌شود.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| برگشت رد می‌شود | Session | مسیر/Asymmetric |
| Session پر | جدول | Timeout/DoS |

### ۱۰) نکات امنیتی

- Stateless به‌تنهایی برای مرز اینترنت کافی نیست.

### ۱۱) جمع‌بندی مفهومی

- Stateless بی‌حافظه.
- Stateful جدول State.
- NGFW عمیق ولی پرهزینه.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) تفاوت Stateless و Stateful؟ *(پاسخ: 11-1-ت1)*

**ت2.** (ساده) NGFW چه چیزی اضافه دارد؟ *(پاسخ: 11-1-ت2)*

**ت3.** (متوسط) چرا ACL برگشتی با eq 443 خطرناک است؟ *(پاسخ: 11-1-ت3)*

**ت4.** (متوسط) UDP چطور Session می‌گیرد؟ *(پاسخ: 11-1-ت4)*

**ت5.** (سخت) CPU کم و نیاز به NGFW. *(پاسخ: 11-1-ت5)*

**ت6.** (سخت، طراحی) انتخاب نوع فایروال برای مرز. *(پاسخ: 11-1-ت6)*

**Q1.** Quick quiz (English): What does a stateful firewall store for each allowed connection? *(پاسخ: 11-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NGFW | Next-Generation Firewall | فایروال نسل بعد |
| SYN | Synchronize flag | پرچم شروع اتصال |

- *A stateful firewall tracks connection state.* ← فایروال حالت‌دار وضعیت اتصال را دنبال می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** Stateful. **Evidence:** `03-ops/stateful.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policy
- RFC 793

<a id="l-11-2"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: مقایسه‌ی عملی Stateless و Stateful با یک سناریو و عدد

**سناریو.** شعبه‌ی کوچک باید فقط وب (443) را برای ۵۰ کاربر مجاز کند. دو طراحی را مقایسه می‌کنیم.

**طراحی ۱: ACL Stateless روی روتر**

``` text
ip access-list extended OUT-IN
 permit tcp 10.0.0.0 0.0.0.255 any eq 443
ip access-list extended IN-OUT
 permit tcp any eq 443 10.0.0.0 0.0.0.255 gt 1023
interface Gi0/0
 ip access-group IN-OUT in    ! from internet
```

**ایراد:** بسته‌ی مهاجم با Source Port 443 و Destination Port 3389 (> 1023) از ACL ورودی می‌گذرد؛ ACL «پاسخ بودن» را نمی‌فهمد.

**طراحی ۲: Policy Stateful**

``` text
Policy 10: LAN -> WAN, src NET-USERS, svc HTTPS, ACCEPT, NAT, log
(implicit) WAN -> LAN: deny
```

بسته‌ی ورودی فقط وقتی مجاز است که با Session موجود (ساخته‌شده توسط SYN خروجی) مطابق باشد.

**گام‌ها**
1. کاربر 10.0.0.5:51000 → 203.0.113.10:443 (SYN).
2. Policy 10 مطابق است ⇒ Session ساخته می‌شود.
3. پاسخ 203.0.113.10:443 → 198.51.100.2:51000 فقط به همان Session مطابق است.
4. بسته‌ی مهاجم 203.0.113.10:443 → 10.0.0.9:3389 Session ندارد ⇒ Drop.

**ظرفیت جدول Session.** اگر هر کاربر ۵۰ Session باز داشته باشد، ۵۰ کاربر ⇒ ۲۵۰۰ Session. حافظه‌ی هر Session صد‌ها بایت است؛ پس مشکل ظرفیت معمولاً از DoS (SYN Flood) است نه کاربران عادی.

``` text
Sessions = users x sessions per user = 50 x 50 = 2500
```

**اشتباهات رایج**
- «Stateful یعنی امن»: NGFW و IPS هنوز لازم‌اند.
- Timeout را نادیده گرفتن: Session بیکار حذف می‌شود.
- مسیر نامتقارن با Stateful.

**پرسش‌های مصاحبه**
1. *تفاوت Packet filter و Stateful؟* حافظه‌ی وضعیت اتصال.
2. *UDP و ICMP چطور؟* شبه‌Session با Timeout.
3. *NGFW چه اضافه می‌کند؟* برنامه، کاربر، محتوا، IPS (بعضی Needs-License).

### تکمیل عمیق: Stateless در برابر Stateful — با مثال

#### چرا؟

فهمیدن این تفاوت بسیاری از رفتارهای «عجیب» را توضیح می‌دهد: چرا ACL نیاز به قاعده‌ی برگشت دارد و چرا فایروال نیاز ندارد.

#### توضیح ساده

- **Stateless (ACL)**: هر بسته به‌تنهایی بررسی می‌شود؛ حافظه ندارد.
- **Stateful**: برای هر اتصال یک Session نگه می‌دارد؛ بسته‌ی برگشت را با Session تطبیق می‌دهد.

#### مثال ساده

کاربر به وب (443) می‌رود. با ACL Stateless باید هم «outbound 443» و هم «inbound established/پورت‌های بالا» را بنویسید. با Stateful فقط «outbound 443» کافی است.

``` text
Stateless:  permit tcp src any eq 443 dst 10.10.0.0/24 established
Stateful :  (return traffic accepted automatically via session)
```

#### مثال متوسط — حمله‌ی ACK Scan

ACL ساده با `established` بسته‌ی ACK ساختگی را می‌پذیرد؛ فایروال Stateful بسته‌ی بدون Session را رد می‌کند.

#### مثال سخت — محدودیت Stateful

Stateful ترافیک نامتقارن را نمی‌پسندد (درس 23)، و Session Table ظرفیت دارد (DoS با SYN Flood).

#### جدول مقایسه

| ویژگی | Stateless | Stateful |
|---|---|---|
| حافظه | ندارد | Session |
| سرعت | بالا | کمی کمتر |
| امنیت | محدود | بیشتر |
| ترافیک برگشت | قاعده‌ی جدا | خودکار |

#### Lab

یک ACL ساده Stateless را برای وب بنویسید و مشکلات آن را فهرست کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| برگشت رد | بدون قاعده | Stateful |
| ACK scan | established | Stateful |
| Session پر | SYN flood | DoS Policy |

#### پرسش‌ها با پاسخ

**۱. چرا ACL قاعده‌ی برگشت؟** حافظه ندارد.
**۲. Stateful محدودیت؟** نامتقارن و ظرفیت.
**۳. ACK scan؟** بسته‌ی بی‌Session.

#### English Corner

- *A stateful firewall allows return traffic by matching it to an existing session.*
- Q: Why can a stateless ACL be fooled by crafted ACK packets?

## درس 11-2 — Zone، Trust Boundary، Default Deny و Least Privilege: از ماتریس تا Policy

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰، ۱۱-۱ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Zone و سطح اعتماد را تعریف و ماتریس Zone-to-Zone بسازد.
2. Default Deny و Least Privilege را در Policy واقعی اعمال کند.
3. Policy را از ماتریس استخراج و ترتیب خاص به عام را رعایت کند.
4. Policy گشاد (ALL) را با Log شناسایی و تنگ کند.
5. آزمون مثبت/منفی برای هر خانه‌ی ماتریس بنویسد.
6. ماتریس را برای ممیزی مستند و نگهداری کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Zone و Trust Boundary؟** شبکه‌ی سازمان یکدست نیست: اینترنت، DMZ (سرورهای عمومی)، کاربران، سرورهای داخلی، مدیریت. هرکدام «سطح اعتماد» متفاوتی دارند. **Zone** گروهی از Interfaceها با یک سطح اعتماد است. **Trust Boundary** مرزی است که ترافیک از یک سطح به سطح دیگر می‌رود؛ فایروال باید همان‌جا باشد.

**مثال روزمره:** ساختمان اداری: لابی (عمومی)، طبقات کارکنان (متوسط)، اتاق سرور (بسیار محرمانه). ورود از لابی به اتاق سرور از چند در می‌گذرد، هر دری کارت‌خوان جدا.

**سه اصل**

1. **Default Deny:** هر چه صریحاً مجاز نشده، ممنوع.
2. **Least Privilege (حداقل دسترسی):** فقط همان که لازم است، نه بیشتر.
3. **ماتریس قبل از Policy:** ابتدا جدول «از کجا به کجا چه سرویسی» را بکشید؛ سپس هر خانه‌ی پر یک Policy.

**جمع‌بندی اصلی درس:** فرودگاه را در نظر بگیرید: سالن عمومی، گیت امنیتی، سالن پرواز، باند و اتاق کنترل. هر منطقه سطح اعتماد متفاوت و مرز مشخص دارد؛ عبور از هر مرز فقط با مجوز مخصوص. اگر همه‌ی درها باز باشند، دیوار بی‌معناست.

شبکه هم همین است. Zone یعنی «منطقه‌ی هم‌اعتماد»؛ Trust Boundary مرز بین دو سطح اعتماد؛ Default Deny یعنی «هر عبور ثبت‌نشده ممنوع»؛ Least Privilege یعنی «فقط همان‌قدر که لازم است». اگر این چهار را درست بفهمید، طراحی Policy از «حدس» به «استخراج از جدول» تبدیل می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) Zoneها و سطح اعتماد

| Zone | سطح اعتماد | مثال |
|---|---|---|
| Internet | صفر | WAN |
| DMZ | کم | وب‌سرور عمومی |
| Users | متوسط | VLAN کاربران |
| Servers | متوسط‌بالا | App/DB |
| Mgmt | بالا | ایستگاه Admin |

قانون: ترافیک از اعتماد کمتر به بیشتر سخت‌گیرانه‌تر است؛ از بیشتر به کمتر هم باید کنترل شود (Exfiltration).

#### ۲) ماتریس

``` text
from\to   Internet  DMZ     Users  Servers  Mgmt
Internet  -         443VIP  -      -        -
DMZ       Updates   -       -      DB-only  -
Users     HTTP/S    HTTPS   -      App 443  -
Servers   Updates   -       -      -        -
Mgmt      -         SSH     SSH    SSH      -
```

هر خانه‌ی «-» = Deny. هر خانه‌ی پر = یک یا چند Policy با سرویس مشخص.

#### ۳) از ماتریس به Policy

``` text
ID  from   to       src         dst        service     action
10  Users  Internet NET-USERS   all        HTTP,HTTPS,DNS ACCEPT
20  Users  Servers  NET-USERS   SRV-APP    TCP-443     ACCEPT
30  Mgmt   Servers  HOST-ADMIN  GRP-SERVERS SSH        ACCEPT
99  any    any      all         all        ALL         DENY + log
```

ترتیب: خاص بالا، عام پایین، Deny صریح آخر.

#### ۴) Least Privilege در عمل

- به‌جای dst=all فقط مقصد لازم.
- به‌جای ALL فقط سرویس لازم.
- به‌جای always فقط Schedule لازم (مثلاً پیمانکار).
- مدیریت فقط از Mgmt.

#### ۵) تشخیص Policy گشاد

``` text
Policy 55: Users -> Servers  ALL/ALL ACCEPT  (hit count: 1.2M)
```

Log ۱۴ روز نشان می‌دهد فقط 443/445/1433 به سه سرور استفاده شده؛ جایگزین: سه Policy خاص.

#### ۶) آزمون ماتریس

برای هر خانه: آزمون مثبت (مجاز کار کند) و منفی (ممنوع رد شود و Log شود). ثبت در جدول Evidence.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| تعداد Zone | طبق تفاوت اعتماد؛ نه بیش‌ازحد |
| ترتیب | خاص→عام |
| Log | Deny همیشه؛ Accept حساس |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — ماتریس

| از ↓ / به → | Internet | DMZ | Servers | Mgmt |
|---|---|---|---|---|
| Users | HTTP/S, DNS | HTTPS | HTTPS, SMB | — |
| Guest | HTTP/S, DNS | — | — | — |
| Internet | — | HTTPS (VIP) | — | — |
| Mgmt | — | SSH | SSH | همه |

خانه‌ی خالی یعنی Deny.

#### مثال متوسط — تبدیل ماتریس به Policy

``` text
Policy 10 USERS -> SRV  HTTPS,SMB accept log
Policy 20 USERS -> INET HTTP,HTTPS,DNS accept nat log
Policy 30 GUEST -> INET HTTP,HTTPS,DNS accept nat log
Policy 90 any -> any   deny log
```

برای هر Policy آزمون مثبت و برای هر خانه‌ی خالی نمونه‌ای آزمون منفی (مثلاً Guest → Servers).

#### مثال متوسط — حداقل دسترسی

به‌جای `Users -> Servers ALL`، بنویسید `Users -> SRV-ERP HTTPS`. اگر یک کاربر آلوده شود، فقط یک سرویس در معرض است.

#### مثال سخت — Zone با intrazone باز

دو Interface در یک Zone با `intrazone allow` آزادانه با هم صحبت می‌کنند و ایزولاسیون از بین می‌رود. راه: `set intrazone deny` و Policy صریح برای هر جریان لازم.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Users→Internet فقط HTTP/HTTPS/DNS. ورودی: کاربر 10.10.0.5 با SSH به اینترنت. مراحل: Policy 10 تطبیق نمی‌کند (Service)؛ Policy 99 Deny. پاسخ: رد و Log با policyid=99.

**متوسط (تنگ‌سازی):** Policy 55 ALL/ALL بین Users و Servers. مراحل: ۱) Log All روشن. ۲) ۱۴ روز جمع‌آوری. ۳) استخراج: 10.20.0.10:443، 10.20.0.11:445، 10.20.0.20:1433. ۴) سه Policy خاص بالای 55. ۵) 55 را Disable و دو هفته مشاهده. ۶) حذف. پاسخ: کاهش سطح حمله از ALL به سه مسیر.

**سخت (طراحی ۵ Zone):** سازمان ۱۵۰ کاربر؛ وب عمومی؛ DB داخلی؛ مدیریت. طراحی: ۱) ۵ Zone. ۲) ماتریس ۲۵ خانه؛ ۹ خانه پر. ۳) ۱۲ Policy. ۴) DMZ→DB ممنوع؛ فقط App→DB. ۵) آزمون ۲۵ خانه (۹ مثبت، ۱۶ منفی). ۶) Evidence. معیار پذیرش: صفر Policy ALL، همه‌ی Deny ها Log دارند.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Interfaces → Create New → Zone.
2. Policy & Objects → Firewall Policy → Create New با Zone.
3. Policy → Drag برای ترتیب.
4. Hit Count/Log برای ممیزی.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall policy
 edit 20
  set name "USERS-to-APP-443"
  set srcintf "ZN-USERS"
  set dstintf "ZN-SERVER"
  set srcaddr "NET-USERS"
  set dstaddr "SRV-APP"
  set action accept
  set schedule "always"
  set service "HTTPS"
  set logtraffic all
 next
end
```

### ۸) Verification (اثبات صحت)

- آزمون مثبت/منفی هر خانه.
- Hit Count Policyها.
- Log Deny‌ها.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy کار نمی‌کند | ترتیب/Zone | خاص قبل عام |
| ALL گشاد | Log | تنگ‌سازی |
| DMZ→DB باز است | Lookup | Policy حذف |

### ۱۰) نکات امنیتی

- Default Deny با Log.
- ALL/ALL ممنوع.

### ۱۱) جمع‌بندی مفهومی

- Zone=منطقه‌ی هم‌اعتماد.
- ماتریس منبع Policy.
- Least Privilege.
- آزمون هر خانه.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Default Deny یعنی چه؟ *(پاسخ: 11-2-ت1)*

**ت2.** (ساده) Least Privilege؟ *(پاسخ: 11-2-ت2)*

**ت3.** (متوسط) چرا ماتریس؟ *(پاسخ: 11-2-ت3)*

**ت4.** (متوسط) چرا ترتیب مهم است؟ *(پاسخ: 11-2-ت4)*

**ت5.** (سخت) Policy ALL را چطور تنگ می‌کنید؟ *(پاسخ: 11-2-ت5)*

**ت6.** (سخت، طراحی) ماتریس ۵ Zone و آزمون. *(پاسخ: 11-2-ت6)*

**Q1.** Quick quiz (English): What does default deny mean? *(پاسخ: 11-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DMZ | Demilitarized Zone | منطقه‌ی حائل |
| Trust boundary | Trust boundary | مرز اعتماد |

- *Apply least privilege to every rule.* ← به هر Rule حداقل دسترسی را بدهید.

### ۱۴) کارت Lab

**کارت Lab:** ماتریس Zone (اجرا نشده). **Evidence:** `03-ops/zone-matrix.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- NIST SP 800-41 Rev.1

<a id="l-11-3"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: ساخت ماتریس Zone از Flow واقعی تا Policy و آزمون

**سناریو.** شرکت ۱۵۰ نفره با وب‌سایت عمومی، سرور فایل، Active Directory و کاربران. ماتریس را از Log واقعی می‌سازیم.

**گام ۱ — Discovery (۱۴ روز).** Policy موقت `Users→Servers ALL` با Log All. خروجی نمونه:

``` text
USERS -> SRV-FILE   tcp/445     1.2M sessions
USERS -> SRV-AD     tcp/389,88,53 600k
USERS -> SRV-WEB    tcp/443     90k
USERS -> SRV-DB     tcp/1433    14      <- suspicious (users should not talk to DB)
```

**گام ۲ — طبقه‌بندی.** لازم: 445، 389/88/53، 443. مشکوک: 1433 (۱۴ Session). بررسی: دو کاربر IT با SSMS مستقیم به DB وصل می‌شوند ⇒ باید از Jump Host یا VPN مدیریتی.

**گام ۳ — ماتریس نهایی.**

``` text
from\to  SRV-FILE  SRV-AD       SRV-WEB  SRV-DB
USERS    445       389,88,53    443      -
IT-ADM   445       389,88,53    443      1433 (jump host only)
WEB      -         -            -        1433 (app tier)
```

**گام ۴ — Policy.** یک Policy برای هر ردیف (Object گروهی برای پورت‌های AD)، `Deny` صریح با Log در انتها؛ ALL غیرفعال و ۲ هفته مشاهده.

**گام ۵ — آزمون.** ۴ آزمون مثبت و ۴ آزمون منفی (Users→DB باید رد و Log شود).

**اشتباهات رایج**
- تعریف Zone بدون تعریف «چه چیزی از چه سطح اعتمادی»: ماتریس بی‌معنی می‌شود.
- حذف فوری Policy ALL بدون Log کافی.
- نداشتن Owner برای Policy.

**پرسش‌های مصاحبه**
1. *Least Privilege را چگونه اندازه می‌گیرید؟* تعداد Policy ALL = ۰ و Hit Count هر Policy.
2. *Default Deny با Log چرا؟* برای ممیزی و Alert.
3. *Trust Boundary چیست؟* مرزی که ترافیک از سطح اعتماد کمتر به بیشتر یا برعکس عبور می‌کند.

### تکمیل عمیق: Zone، Default Deny و Least Privilege از ماتریس تا Policy

#### چرا؟

قبل از نوشتن Policy یک ماتریس نیاز بکشید؛ بعد هر خانه یا «Allow با سرویس مشخص» یا «Deny» است.

#### ماتریس نمونه

| از ↓ / به → | Internet | DMZ | Servers | Mgmt |
|---|---|---|---|---|
| Users | HTTP/S,DNS | HTTPS | HTTPS,SMB | — |
| Guest | HTTP/S,DNS | — | — | — |
| Mgmt | — | SSH | SSH | همه |
| Internet | — | HTTPS (VIP) | — | — |

خانه‌ی خالی = Deny.

#### مثال ساده — تبدیل به Policy

هر خانه‌ی پر یک Policy؛ در پایان Deny All با Log.

#### مثال متوسط — Least Privilege

به‌جای `Users -> Servers ALL` بنویسید `Users -> SRV-ERP HTTPS`. مقصد دقیق، سرویس دقیق.

#### مثال سخت — دور زدن Zone

در Zone با `intrazone allow` دو Interface همان Zone آزادانه صحبت می‌کنند؛ حتماً `deny` و Policy صریح.

#### آزمون

برای هر Policy یک آزمون مثبت و برای هر خانه‌ی خالی یک آزمون منفی (چند نمونه).

#### Lab

ماتریس را برای سازمان فرضی خودتان بکشید و ۱۰ Policy بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Policy ALL | تنبلی | تنگ |
| Zone باز | intrazone | deny |
| بی‌آزمون | غفلت | آزمون منفی |

#### پرسش‌ها با پاسخ

**۱. خانه‌ی خالی؟** Deny.
**۲. Least privilege؟** حداقل لازم.
**۳. آزمون منفی؟** اثبات بستن.

#### English Corner

- *Every empty cell in the access matrix is an implicit deny that should be tested.*
- Q: What does least privilege mean for a firewall rule?

## درس 11-3 — مسیر بسته در فایروال: Transit، Local-in، Local-out و ترتیب DNAT/Route/Policy/SNAT

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۱-۲ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مراحل پردازش بسته (Ingress، RPF، Session، DNAT، Route، Policy، SNAT، Egress) را به ترتیب بگوید.
2. سه نوع ترافیک را تفکیک و کنترل هرکدام را بگوید.
3. Policy را با آدرس درست (بعد DNAT) بنویسد.
4. سناریو را روی کاغذ شبیه‌سازی کند.
5. با Debug/Session مسیر را اثبات کند.
6. علائم هر مرحله‌ی شکست را بشناسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا مسیر بسته را بدانیم؟** هر Policy یا قابلیتی در مرحله‌ی مشخصی اجرا می‌شود. اگر ترتیب را ندانید، Policy را جای اشتباه می‌نویسید. مثلاً می‌خواهید SSH به خود فایروال را ببندید؛ Policy عادی بی‌اثر است چون این ترافیک **Local-in** است.

**سه نوع ترافیک**

1. **Transit:** از میان فایروال می‌گذرد (کاربر به سرور) ⇒ Firewall Policy.
2. **Local-in:** مقصدش خود فایروال است (SSH، ping به FW) ⇒ allowaccess/Local-in Policy.
3. **Local-out:** از خود فایروال می‌آید (NTP، FortiGuard، Syslog) ⇒ تنظیمات سرویس و Routing.

**ترتیب مراحل Transit (مفهومی):** ورود ← Session موجود؟ ← DoS ← RPF ← DNAT ← Routing ← Policy ← UTM ← SNAT ← خروج.

**جمع‌بندی اصلی درس:** کاربر می‌گوید «سایت باز نمی‌شود». بدون نقشه‌ی مسیر بسته، حدس می‌زنید: Policy؟ Route؟ NAT؟ DNS؟ با نقشه، مرحله‌به‌مرحله می‌پرسید: بسته رسید؟ Session ساخته شد؟ Route دارد؟ Policy؟ NAT؟ خارج شد؟ هر پاسخ «نه» محل خرابی را نشان می‌دهد.

### ۳) توضیح عمیق فنی

#### ۱) مراحل ترافیک عبوری (Transit)

``` text
1 Ingress interface
2 Anti-spoof / RPF check
3 Session lookup (existing session? -> fast path)
4 DNAT (VIP)
5 Route lookup (egress interface)
6 Policy lookup (srcintf, dstintf, src, dst, service, schedule)
7 UTM inspection (if enabled)
8 SNAT (IP pool / interface address)
9 Egress
```

نکته‌ی ظریف: DNAT قبل از Route و Policy است؛ پس Policy با آدرس **داخلی** (بعد DNAT) و VIP object تطابق می‌کند.

#### ۲) سه نوع ترافیک

| نوع | مقصد | کنترل |
|---|---|---|
| Transit | شبکه‌ی پشت فایروال | Firewall Policy |
| Local-in | خود فایروال (Admin، BGP، IPsec، DNS) | Allowaccess + Local-in policy |
| Local-out | تولیدشده توسط فایروال (NTP، FortiGuard، Syslog) | Routing خود فایروال + Source-IP |

#### ۳) شبیه‌سازی

``` text
User 10.10.0.5:40000 -> 203.0.113.10:443
1 ingress port2, RPF: route to 10.10.0.5 via port2 OK
2 no session -> new
3 no DNAT
4 route: default -> port1
5 policy: ZN-USERS->port1 src NET-USERS svc HTTPS -> ACCEPT (id 10)
6 SNAT -> 198.51.100.2:40000
7 egress port1
```

#### ۴) اثبات

``` text
diagnose debug flow filter addr 203.0.113.10
diagnose debug flow show function-name enable
diagnose debug flow trace start 20
diagnose debug enable
diagnose sys session list
```

#### ۵) علائم هر مرحله

| پیام | مرحله |
|---|---|
| reverse path check fail | RPF |
| no matching policy / Denied by forward policy check | Policy |
| iprope_in_check() check failed | Local-in |
| find a route: ... | Route |
| no session matched | بسته میانه‌ی اتصال |

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Local-in | Policy برای BGP/IPsec/Admin |
| Source IP Local-out | Loopback/Interface ثابت |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — کدام نوع؟

| ترافیک | نوع | کنترل |
|---|---|---|
| PC → سرور ERP | Transit | Firewall Policy |
| PC → SSH به فایروال | Local-in | allowaccess |
| فایروال → NTP | Local-out | تنظیم NTP/Route |

#### مثال متوسط — بررسی با Debug

``` text
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow trace start 10
```

خروجی «allocate a new session» ⇒ Transit؛ «local in» (طبق نسخه) ⇒ Local-in.

#### مثال سخت — اشتباه رایج

مهندس Policy `Users -> any SSH deny` را برای بستن SSH به فایروال نوشت؛ بی‌اثر ماند چون Local-in است. راه صحیح: حذف `ssh` از `allowaccess` Interface یا `config firewall local-in-policy`. آزمون: `ssh admin@FW` از Users باید Timeout بدهد.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** کاربر به اینترنت: Walk بالا؛ نتیجه: Policy 10، SNAT.

**متوسط (VIP):** کاربر اینترنت به 203.0.113.10:443 (VIP به 10.30.0.10). مراحل: DNAT اول؛ Route به DMZ؛ Policy با dstaddr=VIP-WEB (نه IP داخلی)؛ Accept. اگر Policy با 10.30.0.10 نوشته شود تطابق نمی‌کند ⇒ `Denied by forward policy check`.

**سخت (Local-in):** Admin از Mgmt به https فایروال وصل نمی‌شود. مراحل: ۱) ترافیک Local-in؛ ۲) Debug flow: `iprope_in_check() check failed`. ۳) allowaccess https روی Interface Mgmt نیست یا Local-in policy بسته. رفع: allowaccess و Trusted host؛ آزمون ورود.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose debug flow filter addr 203.0.113.10
diagnose debug flow show function-name enable
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
```

### ۸) Verification (اثبات صحت)

- Debug flow مراحل را نشان می‌دهد.
- policy-id مطابق.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| no policy | Lookup | آدرس بعد DNAT |
| RPF fail | Route برگشت | Route |
| Admin وارد نمی‌شود | allowaccess | Interface Mgmt |

### ۱۰) نکات امنیتی

- Debug را خاموش کنید.

### ۱۱) جمع‌بندی مفهومی

- DNAT قبل Route/Policy.
- سه نوع ترافیک.
- Debug flow اثبات.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) DNAT قبل یا بعد Policy؟ *(پاسخ: 11-3-ت1)*

**ت2.** (ساده) Local-in چیست؟ *(پاسخ: 11-3-ت2)*

**ت3.** (متوسط) چرا Policy VIP با IP داخلی کار نمی‌کند؟ *(پاسخ: 11-3-ت3)*

**ت4.** (متوسط) RPF چیست؟ *(پاسخ: 11-3-ت4)*

**ت5.** (سخت) Admin به https نمی‌رسد؛ مسیر عیب‌یابی. *(پاسخ: 11-3-ت5)*

**ت6.** (سخت، طراحی) نقشه‌ی Flow سازمان. *(پاسخ: 11-3-ت6)*

**Q1.** Quick quiz (English): Does destination NAT occur before or after the policy lookup? *(پاسخ: 11-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس |
| VIP | Virtual IP | آدرس مجازی |

- *Trace the packet stage by stage.* ← بسته را مرحله‌به‌مرحله ردیابی کنید.

### ۱۴) کارت Lab

**کارت Lab:** Flow (اجرا نشده). **Evidence:** `03-ops/packet-walk.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Packet flow
- FortiOS 7.0 Troubleshooting guide

<a id="l-11-4"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Packet Walk سه‌حالته با Debug واقعی

**حالت A — کاربر به اینترنت (SNAT).**

``` text
diagnose debug flow filter addr 203.0.113.10
diagnose debug flow show function-name enable
diagnose debug flow trace start 10
diagnose debug enable
 id=20085 ... received a packet(proto=6, 10.10.0.5:50000->203.0.113.10:443) from port2. flag [S]
 id=20085 ... allocate a new session-0001a2b3
 id=20085 ... find a route: flag=00000000 gw-198.51.100.1 via port1
 id=20085 ... Allowed by Policy-10: SNAT
 id=20085 ... SNAT 10.10.0.5->198.51.100.2:50000
```

**حالت B — اینترنت به وب (VIP/DNAT).** DNAT قبل از Policy:

``` text
 ... received a packet(proto=6, 8.8.4.4:41000->203.0.113.10:443) from port1
 ... Find an existing session / VIP 203.0.113.10:443 -> 10.30.0.10:443
 ... Allowed by Policy-40: 
```

**حالت C — Admin به فایروال (Local-in).**

``` text
 ... iprope_in_check() check failed on policy 0, drop     ! allowaccess missing
```

**جدول قضاوت**

| پیام | معنی | اقدام |
|---|---|---|
| Denied by forward policy check (policy 0) | Implicit Deny | Policy/Interface/Zone |
| reverse path check fail | RPF | Route برگشت |
| iprope_in_check() check failed | Local-in | allowaccess/Local-in policy |
| no session matched | میانه‌ی اتصال بدون SYN | Asymmetric/Timeout |

**اشتباهات رایج**
- Policy برای IP داخلی به‌جای VIP.
- فراموشی `debug disable` و `debug reset`.
- آزمون روی NP-offload شده (بسته دیده نمی‌شود؛ ICMP را آزمون کنید یا Offload را غیرفعال).

**پرسش‌های مصاحبه**
1. *ترتیب DNAT و Route؟* DNAT اول.
2. *Local-out چیست؟* ترافیک تولیدشده توسط خود فایروال (NTP، FortiGuard).
3. *Route چند بار جستجو می‌شود؟* معمولاً دو بار در عمر Session (بسته‌ی اول و اولین پاسخ).

### تکمیل عمیق: مسیر بسته — Transit، Local-in و Local-out

#### چرا؟

مسیر بسته تعیین می‌کند کدام کنترل اعمال شود. بدون این نقشه، Policy اشتباه می‌نویسید.

#### سه مسیر

``` text
Transit   : A -> Firewall -> B       (firewall policy)
Local-in  : A -> Firewall itself    (allowaccess / local-in policy)
Local-out : Firewall itself -> B    (service config, routing)
```

#### مثال ساده

- SSH به فایروال ⇒ Local-in.
- Users→Server ⇒ Transit.
- فایروال به NTP ⇒ Local-out.

#### مثال متوسط — ترتیب

در Transit: Session، DoS، RPF، DNAT، Route، Policy، UTM، SNAT.

#### مثال سخت — اشتباه رایج

مهندس Policy `Users -> any SSH` برای باز کردن SSH به فایروال نوشت؛ بی‌اثر است چون Local-in است.

#### Lab

برای شش ترافیک مختلف نوع و کنترل را بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| SSH به FW نه | allowaccess | افزودن |
| Update نه | Local-out Route | تنظیم |
| Policy بی‌اثر | نوع اشتباه | شناسایی |

#### پرسش‌ها با پاسخ

**۱. SSH به FW؟** Local-in.
**۲. Policy عادی کافی است؟** خیر.
**۳. Local-out مثال؟** NTP.

#### English Corner

- *Identify whether traffic is transit, local-in or local-out before writing a rule.*
- Q: Which control applies to SSH connections to the firewall?

## درس 11-4 — ACL، Policy و NAT: تفاوت‌ها، ارتباط‌ها و ترکیب درست

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۱-۳ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. وظیفه‌ی ACL، Firewall Policy و NAT را تفکیک کند.
2. Source NAT، Destination NAT و PAT را بشناسد.
3. NAT و Policy را برای انتشار سرویس هماهنگ کند.
4. Hairpin NAT و Split DNS را مقایسه کند.
5. خطاهای رایج (NAT بدون Policy، Policy بدون Route) را رفع کند.
6. مثال کامل Publish و آزمون منفی بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا ACL، Policy و NAT را یکی نمی‌گیریم؟** سه ابزار سه سؤال متفاوت را جواب می‌دهند: **ACL/Policy:** «اجازه هست؟»؛ **NAT:** «آدرس چه شود؟»؛ **Routing:** «از کجا برود؟». ترکیب غلط آنها یکی از رایج‌ترین علل خطاست.

**ترتیب مهم:** DNAT (ترجمه‌ی مقصد) **قبل از** Policy و Routing؛ SNAT (ترجمه‌ی مبدأ) **بعد از** Policy. نتیجه: Policy ورودی برای سرور منتشرشده باید به **آدرس عمومی (VIP)** اشاره کند نه آدرس داخلی.

**فرق ACL و Policy:** ACL Stateless و روی Interface؛ Policy Stateful با Interface/Address/Service/Action/Profile.

**جمع‌بندی اصلی درس:** سه اشتباه رایج: «NAT گذاشتم ولی کار نمی‌کند»، «Policy گذاشتم ولی ترجمه نمی‌شود»، «ACL گذاشتم ولی دور زده می‌شود». هر سه از یکی‌گرفتن سه ابزار با وظایف متفاوت می‌آید.

مثال روزمره: ACL فهرست مهمان‌های مجاز، Policy مجوز ورود هر مهمان (با شرایط)، NAT تغییر نام روی تابلو (مثلاً «اتاق ۲۱۴» برای بیرون «طبقه‌ی بالا»).

### ۳) توضیح عمیق فنی

#### ۱) جدول تفاوت

| | ACL | Policy | NAT |
|---|---|---|---|
| وظیفه | فیلتر ساده | اجازه/ردّ + بازرسی | بازنویسی آدرس/پورت |
| وضعیت | معمولاً Stateless | Stateful | Stateful |
| معیار | IP/پورت | Interface/Zone، User، Service، App | آدرس مبدأ/مقصد |

#### ۲) انواع NAT

- Source NAT (SNAT/PAT): کاربران داخلی با IP عمومی.
- Destination NAT (DNAT/VIP): انتشار سرور داخلی.
- Static NAT: یک‌به‌یک.

#### ۳) انتشار وب

``` text
VIP: 203.0.113.10:443 -> 10.30.0.10:443
Policy: Internet -> DMZ, dst=VIP-WEB, service=HTTPS, ACCEPT, log all
```

بدون Policy: VIP ترجمه می‌کند ولی بسته رد می‌شود. بدون VIP: Policy مقصد عمومی را نمی‌شناسد.

#### ۴) Hairpin

کاربر داخلی به IP عمومی وب داخلی: بسته به فایروال می‌رود، DNAT می‌شود و به سرور می‌رسد؛ سرور پاسخ را مستقیم به کاربر می‌دهد (هم‌شبکه) و فایروال را دور می‌زند ⇒ Session ناقص. راه‌ها: Split DNS (ترجیح) یا SNAT برای Hairpin.

#### ۵) خطاها

| علامت | علت |
|---|---|
| VIP کار نمی‌کند | Policy dst=VIP نیست |
| برگشت نیست | سرور Default Gateway ندارد/Route |
| فقط بعضی کاربران | NAT Overlap |

#### ۶) آزمون

مثبت: HTTPS از اینترنت. منفی: SSH به VIP باید رد شود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Hairpin | Split DNS |
| VIP | Port-forward حداقل |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — Users به اینترنت

Routing می‌گوید خروجی port1؛ Policy آن را مجاز می‌کند؛ NAT آدرس عمومی را می‌گذارد.

#### مثال متوسط — VIP

``` text
Outside client -> 203.0.113.10:443
DNAT -> 10.30.0.10:443
Policy lookup uses dst = VIP-WEB
```

اگر Policy با IP داخلی نوشته شود، Lookup مطابق نخواهد شد.

#### مثال سخت — NAT یک‌به‌یک روی Tunnel

شبکه‌ی سایت B با 192.168.1.0/24 هم‌پوشان است؛ در A به 10.222.1.0/24 ترجمه می‌شود. Policy در A باید به **آدرس ترجمه‌شده** اشاره کند. راه‌های تأیید: `diagnose sys session list` و Debug Flow.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** PAT: ۲۰۰ کاربر با یک IP؛ Session با SNAT.

**متوسط (VIP بدون Policy):** VIP ساخته ولی سایت باز نمی‌شود؛ Debug flow: `Denied by forward policy check`. Policy dst=VIP-WEB؛ آزمون موفق.

**سخت (Hairpin):** کاربران داخلی به وب با نام عمومی نمی‌رسند ولی از اینترنت باز است. مراحل: ۱) DNS عمومی IP عمومی. ۲) مسیر Hairpin ناقص. رفع: Split DNS با پاسخ 10.30.0.10؛ آزمون nslookup و باز شدن سایت. جایگزین: Hairpin NAT با ریسک پیچیدگی.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall vip
 edit "VIP-WEB-443"
  set extintf "port1"
  set extip 203.0.113.10
  set mappedip "10.30.0.10"
  set portforward enable
  set extport 443
  set mappedport 443
 next
end
```

### ۸) Verification (اثبات صحت)

- آزمون مثبت/منفی.
- Session DNAT.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| VIP کار نمی‌کند | Policy | dst=VIP |
| برگشت نیست | Route سرور | Gateway |

### ۱۰) نکات امنیتی

- فقط پورت لازم.

### ۱۱) جمع‌بندی مفهومی

- ACL≠Policy≠NAT.
- VIP+Policy.
- Split DNS.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) NAT چه می‌کند؟ *(پاسخ: 11-4-ت1)*

**ت2.** (ساده) PAT چیست؟ *(پاسخ: 11-4-ت2)*

**ت3.** (متوسط) چرا VIP بدون Policy کار نمی‌کند؟ *(پاسخ: 11-4-ت3)*

**ت4.** (متوسط) Hairpin چیست؟ *(پاسخ: 11-4-ت4)*

**ت5.** (سخت) Hairpin را چطور حل می‌کنید؟ *(پاسخ: 11-4-ت5)*

**ت6.** (سخت، طراحی) انتشار سه سرویس. *(پاسخ: 11-4-ت6)*

**Q1.** Quick quiz (English): Why does a VIP alone not allow traffic through? *(پاسخ: 11-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PAT | Port Address Translation | ترجمه‌ی پورت |
| VIP | Virtual IP | آدرس مجازی |

- *NAT alone does not permit traffic.* ← NAT به‌تنهایی ترافیک را مجاز نمی‌کند.

### ۱۴) کارت Lab

**کارت Lab:** NAT و VIP (اجرا نشده). **Evidence:** `02-design/fgt-nat.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: NAT; Virtual IPs

<a id="l-11-5"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: انتشار سه سرویس با VIP و حل Hairpin با Split DNS

**سناریو.** سه سرویس داخلی: وب (10.30.0.10:443)، پورتال (10.30.0.11:8443)، SFTP (10.30.0.12:22). فقط یک IP عمومی 203.0.113.10 داریم.

**گام ۱ — سه VIP با Port-forward.**

``` text
VIP-WEB     203.0.113.10:443  -> 10.30.0.10:443
VIP-PORTAL  203.0.113.10:8443 -> 10.30.0.11:8443
VIP-SFTP    203.0.113.10:2222 -> 10.30.0.12:22
```

اشتراک IP با پورت‌های متفاوت ممکن است؛ پورت داخلی 22 با پورت خارجی 2222 (کاهش اسکن خودکار).

**گام ۲ — Policy هر سرویس** (dst=VIP، Service مشخص، Log).

**گام ۳ — Hairpin.** کاربر داخلی `https://web.example.com` را می‌زند و DNS عمومی 203.0.113.10 می‌دهد. مسیر: LAN → فایروال → DNAT به 10.30.0.10 در همان یا شبکه‌ی دیگر. اگر سرور هم‌Subnet کاربر باشد، پاسخ مستقیم به کاربر می‌رود و Session ناقص می‌شود.

**راه‌حل مرجح: Split DNS.**

``` text
Internal DNS: web.example.com -> 10.30.0.10   (for internal users)
Public DNS  : web.example.com -> 203.0.113.10 (for internet)
```

راه جایگزین (طبق مستند Fortinet): Policy با Incoming Interface داخلی و Destination=VIP (بسته به نسخه‌ی اجرا) یا Hairpin NAT؛ `nat-source-vip` برای Hairpin نیست.

**گام ۴ — آزمون.** از اینترنت: 3 سرویس؛ منفی: پورت‌های دیگر (21، 3389) رد؛ از LAN: nslookup باید IP داخلی بدهد.

**اشتباهات رایج**
- باز کردن همه‌ی پورت‌ها با Static NAT.
- نبود Policy برای VIP.
- DNS داخلی/خارجی یکسان.

**پرسش‌های مصاحبه**
1. *DNAT کجا Policy را عوض می‌کند؟* Policy روی VIP نوشته می‌شود.
2. *PAT ظرفیت؟* حدود ۶۴ هزار پورت به‌ازای IP و مقصد.
3. *Hairpin چیست؟* دسترسی داخلی به IP عمومی سرور داخلی.

### تکمیل عمیق: ACL، Policy و NAT — تفاوت‌ها و ترکیب

#### چرا؟

این سه مفهوم اغلب با هم قاطی می‌شوند؛ هرکدام سؤال متفاوتی را جواب می‌دهند.

#### سه سؤال

| ابزار | سؤال |
|---|---|
| ACL/Policy | اجازه هست؟ |
| NAT | آدرس چه شود؟ |
| Routing | از کجا برود؟ |

#### مثال ساده — ترکیب

Users→Internet: Route می‌گوید «از port1»، Policy می‌گوید «مجاز»، NAT می‌گوید «با IP عمومی».

#### مثال متوسط — ترتیب

DNAT قبل از Policy؛ SNAT بعد از Policy. پس Policy ورودی VIP باید به IP عمومی نگاه کند.

#### مثال سخت — خطای Overlap

NAT یک‌به‌یک روی Tunnel برای شبکه‌های هم‌پوشان: Policy باید به آدرس «ترجمه‌شده» اشاره کند.

``` text
Original : 192.168.1.10 (remote site B)
Translated at A: 10.222.1.10
Policy at A uses 10.222.1.10
```

#### Lab

سه ترافیک را از نظر Route/Policy/NAT تحلیل کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Policy مچ نمی‌شود | آدرس قبل/بعد NAT | تصحیح |
| Route اشتباه | Interface | بررسی |
| NAT بی‌اثر | Policy | فعال |

#### پرسش‌ها با پاسخ

**۱. سه سؤال؟** مجاز؟ آدرس؟ مسیر؟
**۲. DNAT/Policy؟** DNAT اول.
**۳. Policy و آدرس ترجمه‌شده؟** باید هماهنگ.

#### English Corner

- *Routing, policy and NAT answer three different questions about a packet.*
- Q: Does a firewall policy match the pre-NAT or post-NAT destination address?

## درس 11-5 — Session، Timeout، MTU/MSS و ریشه‌ی خرابی‌های «نیمه‌کارکرده» TCP/UDP

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۴-۲، ۱۱-۳ · ≈ 10 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. چرخه‌ی Session TCP/UDP/ICMP و Timeoutها را توضیح دهد.
2. MTU، MSS، PMTUD و Fragmentation را با محاسبه تحلیل کند.
3. علائم MTU Black-hole را بشناسد و PMTU را اندازه بگیرد.
4. MSS-clamp را محاسبه و اعمال کند.
5. خرابی‌های Timeout (SSH، DB) را رفع کند.
6. آزمون پایدار برای تأیید طراحی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا خرابی‌های «نیمه‌کارکرده»؟** بدترین مشکلات آنهایی‌اند که «گاهی کار می‌کند». سه علت اصلی: **Timeout** Session، **MTU/MSS** و **نامتقارن**. این درس دو تای اول را باز می‌کند.

**Timeout:** Session بعد از مدتی بدون ترافیک حذف می‌شود. TCP برقرار پیش‌فرض ۳۶۰۰ ثانیه، UDP کوتاه‌تر. اتصال طولانی بی‌کار (مثل SSH) ممکن است قطع شود.

**MTU/MSS:** بسته‌ی کوچک رد می‌شود ولی بزرگ نه؛ علامت «ping کار می‌کند ولی وب نه». MSS = MTU منهای ۴۰.

**جمع‌بندی اصلی درس:** شکایت رایج: «سایت باز می‌شود ولی بعد از لاگین گیر می‌کند»، «ping جواب می‌دهد ولی دانلود می‌ایستد»، «SSH بعد از چند دقیقه می‌پرد». اینها Policy نیستند؛ MTU یا Timeout‌اند. تشخیصشان نیاز به دانستن این دارد که در لایه‌ی انتقال چه می‌گذرد.

### ۳) توضیح عمیق فنی

#### ۱) Timeoutها

| پروتکل | Timeout تقریبی |
|---|---|
| TCP Established | ۳۶۰۰ ثانیه |
| TCP Half-open (SYN) | کوتاه (در حد ثانیه‌ها تا چند ده ثانیه؛ عدد دقیق را از مستند نسخه بخوانید) |
| UDP | چند ده ثانیه تا حدود ۱۸۰ ثانیه (بسته به نسخه و Service) |
| ICMP | کوتاه |

فقط عدد TCP Established و مفهوم «Timeout سراسری و Timeout هر Service» مرجع است: طبق مستند Fortinet مقدار سراسری پیش‌فرض ۳۶۰۰ ثانیه است، Timeout هر پورت/Service آن را بازنویسی می‌کند و برای UDP مقدار `udp-idle-timer` در تعریف Service مقدار سراسری را override می‌کند. مقادیر دقیق بسته به نسخه فرق دارند؛ با `get system session-ttl` و `show full-configuration` ببینید. Session بیکار حذف می‌شود؛ سرویس‌های طولانی (SSH، DB) Keepalive یا Timeout بیشتر می‌خواهند.

#### ۲) MTU و MSS

``` text
Ethernet MTU = 1500
IP header = 20
TCP header = 20
MSS = 1500 - 20 - 20 = 1460
```

تونل (IPsec) سربار دارد: مثلاً MTU مؤثر 1400 ⇒ MSS ≈ 1360.

#### ۳) PMTUD و Black-hole

TCP بسته‌ها را با DF می‌فرستد؛ اگر مسیر MTU کوچک‌تر دارد، روتر ICMP «Fragmentation needed» برمی‌گرداند. اگر فایروالی ICMP را ببندد، فرستنده نمی‌فهمد و بسته‌های بزرگ بی‌خبر می‌میرند: Black-hole. علامت: Handshake و بسته‌های کوچک ok؛ بزرگ نه.

#### ۴) اندازه‌گیری

``` text
ping -f -l 1472 203.0.113.10     (Windows; 1472+28=1500)
execute ping-options df-bit yes
execute ping-options data-size 1372
execute ping 203.0.113.10
```

کاهش تا اولین موفقیت ⇒ PMTU = اندازه + 28.

#### ۵) MSS-clamp

``` text
config firewall policy
 edit 2
  set tcp-mss-sender 1360
  set tcp-mss-receiver 1360
 next
end
```

(`Unverified` روی 7.0.3؛ با CLI help ببینید.)

#### ۶) آزمون پایدار

دانلود ۱۰۰ MB، صفحه‌ی HTTPS بزرگ، SSH ۳۰ دقیقه‌ی بیکار.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| MSS | PMTU−40 با حاشیه |
| Timeout | سرویس‌محور |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — Timeout

SSH پس از ۱ ساعت بی‌کاری قطع می‌شود. رفع: Keepalive در کلاینت (`ServerAliveInterval`) یا Timeout سفارشی برای سرویس.

#### مثال متوسط — MSS

``` text
Path MTU 1400 -> MSS = 1400 - 40 = 1360
```

با Clamp روی Policy (`tcp-mss-sender/receiver`) رفع می‌شود.

#### مثال سخت — دو علت هم‌زمان

DNS با پاسخ بزرگ + TCP/53 بسته + MTU کوچک. Capture نشان می‌دهد Query UDP بی‌پاسخ و بعد TCP تلاش می‌شود؛ رفع: باز کردن TCP/53 و MSS Clamp.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** MSS=1500−40=1460.

**متوسط (PMTU):** IPsec: ping 1472 شکست، 1372 موفق، 1422 شکست، 1400 موفق ⇒ PMTU=1428؛ MSS ≈ 1388؛ clamp 1380 (حاشیه).

**سخت (SSH می‌پرد):** SSH Admin پس از ۵ دقیقه بیکاری قطع می‌شود. مراحل: ۱) Session expire ۳۰۰. ۲) `session-ttl` پورت 22 = 7200 یا Keepalive 60s در کلاینت. ۳) آزمون ۳۰ دقیقه بیکار. ریسک: Session بیکار منابع می‌گیرد؛ فقط برای پورت لازم.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute ping-options df-bit yes
execute ping-options data-size 1372
execute ping 203.0.113.10
get system session-ttl
```

### ۸) Verification (اثبات صحت)

- دانلود بزرگ.
- SSH ماندگار.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| فقط بزرگ می‌میرد | DF ping | MSS/MTU |
| SSH می‌پرد | Timeout | Keepalive/session-ttl |

### ۱۰) نکات امنیتی

- ICMP frag-needed را کامل نبندید.

### ۱۱) جمع‌بندی مفهومی

- MSS=MTU−40.
- Black-hole.
- Timeout.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) MSS برای MTU 1500؟ *(پاسخ: 11-5-ت1)*

**ت2.** (ساده) علامت Black-hole؟ *(پاسخ: 11-5-ت2)*

**ت3.** (متوسط) محاسبه برای MTU 1400. *(پاسخ: 11-5-ت3)*

**ت4.** (متوسط) چرا ICMP لازم است؟ *(پاسخ: 11-5-ت4)*

**ت5.** (سخت) SSH بعد ۵ دقیقه می‌پرد. *(پاسخ: 11-5-ت5)*

**ت6.** (سخت، طراحی) MSS روی IPsec و آزمون. *(پاسخ: 11-5-ت6)*

**Q1.** Quick quiz (English): What causes an MTU black hole? *(پاسخ: 11-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MTU | Maximum Transmission Unit | حداکثر اندازه‌ی بسته |
| MSS | Maximum Segment Size | حداکثر قطعه |

- *Lower the MSS on tunnels.* ← MSS را روی تونل‌ها کاهش دهید.

### ۱۴) کارت Lab

**کارت Lab:** MTU (اجرا نشده). **Evidence:** `03-ops/mtu-mss.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Session TTL
- RFC 1191
- RFC 4821

<a id="l-11-6"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: اندازه‌گیری PMTU قدم‌به‌قدم و آزمون پایدار

**سناریو.** تونل IPsec شعبه به مرکز؛ دانلود فایل ۵۰ MB بعد از چند ثانیه می‌ایستد؛ ping عادی موفق.

**گام ۱ — جست‌وجوی دودویی PMTU** (Windows):

``` text
ping -f -l 1472 10.20.0.5   -> Packet needs to be fragmented but DF set (fail)
ping -f -l 1372 10.20.0.5   -> ok
ping -f -l 1422 10.20.0.5   -> fail
ping -f -l 1397 10.20.0.5   -> ok
ping -f -l 1410 10.20.0.5   -> ok
ping -f -l 1416 10.20.0.5   -> fail
  => largest ok = 1410 -> PMTU = 1410 + 28 = 1438
```

**گام ۲ — MSS.**

``` text
MSS = PMTU - 40 = 1438 - 40 = 1398 ; use 1380 for margin
```

**گام ۳ — اعمال.** روی Policy تونل (FortiGate) `tcp-mss-sender 1380` و `tcp-mss-receiver 1380` (مستند: ۰ تا ۶۵۵۳۵). و ICMP نوع 3 کد 4 را در مسیر مجاز کنید (PMTUD).

**گام ۴ — Capture پیش و پس.** پیش: بسته‌های 1460 بایتی Retransmit می‌شوند؛ پس: SYN با `MSS=1380` و بدون Retransmit.

**گام ۵ — آزمون پایدار.** دانلود ۱۰۰ MB سه بار، ۲۰ Query DNS، SSH بیکار ۳۰ دقیقه.

**Timeout.** TCP Established پیش‌فرض سراسری ۳۶۰۰ ثانیه است؛ Timeout هر پورت/Service آن را بازنویسی می‌کند؛ برای SSH طولانی `session-ttl` پورت 22 را بیشتر کنید یا Keepalive کلاینت بگذارید.

**اشتباهات رایج**
- MSS برابر MTU.
- بستن کامل ICMP.
- اندازه‌گیری با ping بدون DF.

**پرسش‌های مصاحبه**
1. *علامت Black-hole؟* Handshake و بسته‌ی کوچک موفق، بسته‌ی بزرگ نه.
2. *MSS-clamp کجاست؟* روی فایروال/تونل در SYN.
3. *MTU و Fragmentation؟* IPv4 می‌تواند Fragment کند، DF=1 نمی‌تواند.

### تکمیل عمیق: Session، Timeout، MTU/MSS و خرابی «نیمه‌کارکرده»

#### چرا؟

اتصال‌هایی که «باز می‌شوند ولی قطع می‌شوند» معمولاً از Timeout یا MTU می‌آیند.

#### Timeout

``` text
TCP established default = 3600 s
UDP default = 60 s ; DNS shorter
```

(پیش‌فرض‌ها را از مستند نسخه بخوانید.)

#### مثال ساده — SSH بی‌کار

SSH پس از ۱ ساعت بی‌کاری قطع می‌شود: Session Timeout. رفع: Keepalive در کلاینت یا Timeout سفارشی برای Service.

#### مثال متوسط — MTU/MSS

``` text
MSS = MTU - 40 ; Path MTU 1400 -> MSS 1360
```

نشانه: ping کار می‌کند ولی HTTPS نه.

#### مثال سخت — دو علت

UDP DNS با پاسخ بزرگ + TCP/53 بسته + MTU: ترکیب. تشخیص با Capture.

#### Lab

Timeout را با اتصال بی‌کار آزمایش کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| قطع بعد ۱ ساعت | Timeout | Keepalive |
| ping ok، HTTPS نه | MTU | Clamp |
| DNS گاهی | TCP/53 | باز |

#### پرسش‌ها با پاسخ

**۱. Timeout TCP؟** ۳۶۰۰ ثانیه (پیش‌فرض).
**۲. MSS؟** MTU منهای ۴۰.
**۳. Keepalive؟** جلوگیری از قطع.

#### English Corner

- *Idle sessions are removed when their timeout expires.*
- Q: How do you calculate TCP MSS from the MTU?

## درس 11-6 — کارگاه طراحی Policy، ۱۰ پرسش مسیر بسته و آزمون G4: پروژه‌ی حل‌شده‌ی کامل

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰ تا ۱۱-۷ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. ماتریس Zone و ۱۰ Policy کامل بنویسد.
2. ۱۰ پرسش مسیر بسته را با دستور و شاهد پاسخ دهد.
3. ۹ آزمون مثبت و ۱۶ آزمون منفی را طراحی کند.
4. Gate G4 را با Evidence و Rubric تحویل دهد.
5. طراحی را بازبینی و ضعف‌ها را بیابد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا کارگاه و G4؟** تا وقتی خودتان یک مجموعه Policy را از ماتریس تا آزمون نسازید، مفهوم جا نمی‌افتد. G4 این مهارت را می‌سنجد: طراحی، ده پرسش مسیر بسته، آزمون مثبت و منفی.

**ده پرسش مسیر بسته:** ورودی؟ Session؟ RPF؟ DNAT؟ Route؟ Policy؟ UTM؟ SNAT؟ خروجی؟ برگشت؟

**جمع‌بندی اصلی درس:** این کارگاه آخرین مرحله‌ی فصل ۱۱ است: به‌جای جمله‌های کلی، یک شرکت کوچک را از صفر تا آزمون طراحی می‌کنید. هدف این است که وقتی ممیز پرسید «چرا DB از اینترنت دیده نمی‌شود؟» با Policy، Log و آزمون جواب بدهید.

### ۳) توضیح عمیق فنی

#### ۱) سناریو

``` text
Internet - [FW] - DMZ  10.30.0.0/24 (web 10.30.0.10)
                - SRV  10.20.0.0/24 (app 10.20.0.10, db 10.20.0.20)
                - USR  10.10.0.0/24
                - MGT  10.99.0.0/24
```

#### ۲) ماتریس

``` text
from\to  INET        DMZ       SRV         USR   MGT
INET      -           443 (VIP) -           -     -
DMZ       Updates     -         app 8443    -     -
SRV       Updates     -         -           -     -
USR       HTTP/S,DNS  HTTPS     app 443     -     -
MGT       -           SSH       SSH         SSH   -
```

#### ۳) ده Policy

| ID | از | به | Src | Dst | Service | NAT |
|---|---|---|---|---|---|---|
| 10 | USR | INET | NET-USERS | all | HTTP/HTTPS/DNS | SNAT |
| 20 | USR | DMZ | NET-USERS | SRV-WEB | HTTPS | - |
| 30 | USR | SRV | NET-USERS | SRV-APP | TCP-443 | - |
| 40 | INET | DMZ | all | VIP-WEB | HTTPS | DNAT |
| 50 | DMZ | SRV | SRV-WEB | SRV-APP | TCP-8443 | - |
| 60 | SRV | SRV | SRV-APP | SRV-DB | MS-SQL | - |
| 70 | MGT | DMZ,SRV,USR | HOST-ADMIN | GRP-ALL | SSH | - |
| 80 | DMZ,SRV | INET | GRP-DMZ-SRV | UPDATE-SITES | HTTPS | SNAT |
| 90 | DMZ | SRV | all | SRV-DB | ALL | Deny+log |
| 99 | any | any | all | all | ALL | Deny+log |

#### ۴) پاسخ ۱۰ پرسش

1. Users→Internet: Policy 10، SNAT. 2. VIP-WEB-443→10.30.0.10، Policy 40 dst=VIP. 3. DB: بدون مسیر از INET؛ فقط 60. 4. Admin: Policy 70 فقط MGT. 5. Default Deny: Policy 99 با Log. 6. Log: FortiAnalyzer/Syslog. 7. NAT: فقط Policy 10، 40، 80. 8. MTU 1400 ⇒ MSS 1360. 9. Asymmetric: Session «no session matched» و Capture دو سمت. 10. آزمون منفی DMZ→DB: Policy 90.

#### ۵) آزمون‌ها

۹ مثبت: 10، 20، 30، 40، 50، 60، 70، 80 و VIP. ۱۶ منفی: هر خانه‌ی «-» (مثلاً INET→SRV، DMZ→USR، SRV→DMZ، USR→MGT...).

#### ۶) Rubric

ماتریس ۲۰، Policy ۲۵، پاسخ ۲۵، آزمون ۲۰، صداقت ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — مسیر Users→ERP

ingress port2، Session جدید، RPF ok، بدون DNAT، Route port3، Policy 10، SNAT نه، egress port3، برگشت از همان.

#### مثال متوسط — خطای تزریقی

Policy با srcintf اشتباه: سؤال ۶ پاسخ «policy 0» می‌دهد. رفع و آزمون.

#### مثال سخت — طراحی کامل

ماتریس چهار Zone، هشت Policy، ده آزمون (پنج مثبت و پنج منفی)، گزارش. Rubric: ماتریس ۲۰، Policy ۳۰، مسیر بسته ۲۰، آزمون ۲۰، گزارش ۱۰.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** پرسش ۱: کاربر 10.10.0.5 به 203.0.113.10:443 ⇒ Policy 10، SNAT 198.51.100.2؛ `session list` act=snat.

**متوسط (تحلیل):** پرسش ۳: اگر Policy 90 حذف شود، Implicit Deny هنوز DMZ→DB را رد می‌کند ولی بدون Log؛ پس Deny صریح برای Alert لازم است.

**سخت (آزمون منفی):** DMZ→DB: `telnet 10.20.0.20 1433` از وب؛ انتظار Timeout؛ Log: policyid=90 action=deny؛ Alert؛ Evidence ثبت.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose firewall iprope lookup 10.30.0.10 40000 10.20.0.20 1433 tcp port3
execute log filter field policyid 90
execute log display
```

### ۸) Verification (اثبات صحت)

- G4: ۹ مثبت و ۱۶ منفی با Evidence.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy گشاد | Log | تنگ‌سازی |
| VIP کار نمی‌کند | Policy dst | VIP object |

### ۱۰) نکات امنیتی

- Default Deny با Log.

### ۱۱) جمع‌بندی مفهومی

- طراحی از ماتریس.
- آزمون مثبت/منفی.
- Evidence.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Default Deny کجاست؟ *(پاسخ: 11-6-ت1)*

**ت2.** (ساده) DB از Internet؟ *(پاسخ: 11-6-ت2)*

**ت3.** (متوسط) چرا Deny صریح با وجود Implicit Deny؟ *(پاسخ: 11-6-ت3)*

**ت4.** (متوسط) NAT کجا؟ *(پاسخ: 11-6-ت4)*

**ت5.** (سخت) ۱۶ آزمون منفی را فهرست کنید. *(پاسخ: 11-6-ت5)*

**ت6.** (سخت، طراحی) بهبود طرح. *(پاسخ: 11-6-ت6)*

**Q1.** Quick quiz (English): Name one negative test for a DMZ policy. *(پاسخ: 11-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| G4 | Gate 4 | دروازه‌ی ۴ |

- *Test both allowed and denied flows.* ← هم جریان مجاز و هم ممنوع را آزمون کنید.

### ۱۴) کارت Lab

**کارت Lab:** کارگاه Policy G4 (اجرا نشده). **Evidence:** `03-ops/g4.md`.

### ۱۵) منابع

- درس‌های فصل ۱۱
- Fortinet FortiOS 7.0 Administration Guide: Firewall policies

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: کلید کامل کارگاه با ۹ آزمون مثبت و ۱۶ آزمون منفی

**جدول آزمون مثبت (۹)**

| # | آزمون | انتظار |
|---|---|---|
| P1 | Users→Internet HTTPS | Accept، SNAT |
| P2 | Users→WEB (DMZ) 443 | Accept |
| P3 | Users→APP 443 | Accept |
| P4 | Internet→VIP 443 | Accept، DNAT |
| P5 | WEB→APP 8443 | Accept |
| P6 | APP→DB 1433 | Accept |
| P7 | MGT→همه SSH | Accept |
| P8 | DMZ/SRV→Update HTTPS | Accept |
| P9 | DNS از Users | Accept |

**آزمون منفی (۱۶) — هر خانه‌ی «-»**

``` text
N1  INET -> SRV any        N9  SRV -> DMZ any
N2  INET -> USR any        N10 SRV -> USR any
N3  INET -> MGT any        N11 SRV -> MGT any
N4  DMZ  -> USR any        N12 USR -> MGT any
N5  DMZ  -> MGT any        N13 USR -> DB 1433
N6  DMZ  -> DB  1433       N14 WEB -> DB 1433
N7  MGT  -> INET any       N15 INET -> VIP 22
N8  DB   -> INET any       N16 SRV -> INET 22
```

برای هر مورد: دستور آزمون، نتیجه (Timeout/Refused)، Log (`policyid`، `action=deny`) و زمان. نمونه Evidence:

``` text
N14: telnet 10.20.0.20 1433 from 10.30.0.10 -> timeout
log: srcip=10.30.0.10 dstip=10.20.0.20 dstport=1433 policyid=90 action=deny
```

**ده پرسش مسیر بسته — پاسخ نمونه‌ی کامل**
1. Users→Internet: Policy 10، SNAT 198.51.100.2.
2. VIP: 203.0.113.10:443→10.30.0.10؛ Policy 40 با dst=VIP.
3. DB از اینترنت: بدون VIP، بدون Policy.
4. Admin: Policy 70 از MGT با Trusted host.
5. Default Deny: Policy 99 با Log.
6. Log: FortiAnalyzer/Syslog.
7. NAT: Policy 10، 40، 80.
8. MSS = 1400 − 40 = 1360.
9. Asymmetric: `no session matched`.
10. آزمون منفی DMZ→DB: Policy 90.

**Rubric خودارزیابی:** ماتریس ۲۰، Policy ۲۵، پاسخ‌ها ۲۵، آزمون‌ها ۲۰، صداقت ۱۰؛ قبولی ۷۵ با حداقل ۲۰ در آزمون.

**پرسش‌های مصاحبه**
1. *چرا ۱۶ آزمون منفی؟* هر خانه‌ی ممنوع باید اثبات شود.
2. *Log Deny چه می‌دهد؟* Evidence و Alert.
3. *بهبود طرح؟* MFA/SSO، Segment بیشتر، WAF.

### تکمیل عمیق: کارگاه طراحی Policy و آزمون G4

#### چرا؟

G4 طراحی Policy کامل را از ماتریس تا آزمون می‌سنجد.

#### کار

۱. ماتریس. ۲. Policy. ۳. ۱۰ پرسش مسیر بسته. ۴. آزمون مثبت/منفی.

#### ده پرسش مسیر بسته

``` text
1 ingress interface? 2 session exists? 3 RPF ok? 4 DNAT? 5 route? 6 policy? 7 UTM? 8 SNAT? 9 egress? 10 reply path?
```

#### مثال ساده

Users→ERP HTTPS: ingress port2، session جدید، RPF ok، بدون DNAT، route port3، policy 10، SNAT نه، egress port3، reply از همان.

#### مثال متوسط — خطای تزریقی

Policy با srcintf اشتباه: پاسخ سؤال ۶ «policy 0».

#### Rubric

``` text
Matrix 20 | Policies 30 | Packet path 20 | Tests 20 | Report 10
```

#### Lab

یک کارگاه کامل انجام دهید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Policy بی‌دلیل | ماتریس ناقص | بازنگری |
| آزمون منفی نیست | غفلت | افزودن |
| Path ناقص | فراموشی SNAT | چک‌لیست |

#### پرسش‌ها با پاسخ

**۱. چرا ده پرسش؟** پوشش.
**۲. Reply path؟** برگشت.
**۳. آزمون منفی؟** مرز.

#### English Corner

- *Walk the ten packet-path questions for every new policy.*
- Q: Which stage of the packet path decides the egress interface?

## درس 11-7 — Stateful Inspection از درون: State Table، TCP State و Timeout

**فصل ۱۱ · درس افزوده (تکمیل ۱۱-۱) · پیش‌نیاز: ۱۱-۰، ۱۱-۱، فصل ۲ (TCP) · ≈ ۶ ساعت**

> **وضعیت:** مفهومی با مثال Linux conntrack؛ رفتار FortiGate در فصل ۱۲ و ۱۳ ادامه می‌یابد؛ Labها «اجرا نشده».

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. تفاوت **Stateless (Packet Filter)** و **Stateful** را با مثال بسته‌به‌بسته بگوید.
2. توضیح دهد جدول State (Session/Connection Table) چه چیزی نگه می‌دارد و هنگام ساخت، استفاده و حذف ورودی چه می‌شود.
3. حالت‌های TCP (SYN_SENT، ESTABLISHED، FIN_WAIT، TIME_WAIT، ...) را در جدول State تفسیر کند.
4. رفتار UDP و ICMP (بدون اتصال) را در یک فایروال Stateful توضیح دهد.
5. بداند چرا Timeout، Asymmetric Routing و تغییر Policy بر Session اثر می‌گذارند.
6. محدودیت‌های Stateful (ALG، Fragmentation، Session Exhaustion) را بشناسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Stateful از درون؟** تا بدانید «پرونده‌ی اتصال» چگونه ساخته و حذف می‌شود، رفتارهای عجیب (چرا Policy حذف شد ولی اتصال ادامه دارد؟) را توضیح می‌دهید.

**چرخه‌ی TCP:** SYN_SENT ← SYN_RECV ← ESTABLISHED ← FIN_WAIT ← TIME_WAIT ← CLOSED. فایروال Session را با SYN می‌سازد؛ بسته‌های بعدی باید با آن و با پنجره‌ی Sequence هم‌خوان باشند. هر حالت Timeout خود را دارد.

**جمع‌بندی اصلی درس:** TCP Three-way Handshake و Flagها (SYN، ACK، FIN، RST)، تفاوت UDP/ICMP، Packet Flow پایه (۵-۰).

### ۳) مفهوم پایه

**Packet Filter (Stateless):** هر بسته را مستقل و بدون حافظه با قوانین مقایسه می‌کند. برای اجازه‌ی «کلاینت به وب»، باید دو قانون بنویسیم: رفت (مقصد پورت 443) و برگشت (مبدأ پورت 443 به هر پورت بالا). قانون برگشت یک سوراخ بزرگ است (هر بسته با مبدأ 443 رد می‌شود، حتی بدون درخواست قبلی).

**Stateful Inspection:** فایروال **ارتباط** را می‌شناسد. وقتی کلاینت اتصال را شروع می‌کند، فایروال یک **Session** ثبت می‌کند. بسته‌ی برگشت فقط اگر **با یک Session موجود مطابقت کند** مجاز است. پس به قانون برگشت نیاز نیست و سوراخ‌ها بسته می‌شوند.

> **تشبیه:** Stateless مثل نگهبانی است که برای هر نامه فقط نشانی را می‌خواند. Stateful مثل منشی‌ای است که دفترچه دارد: «نامه‌ی پاسخ را فقط وقتی تحویل می‌دهم که قبلاً خودمان درخواستش را فرستاده باشیم.»

### ۴) توضیح عمیق فنی

#### ۴-۱) Session چیست؟

یک Session معمولاً با **۵-تایی (5-tuple)** شناسایی می‌شود:

``` text
(src_ip, src_port, dst_ip, dst_port, protocol)
```

به‌علاوه: Interface ورودی/خروجی، Policy مطابق، اطلاعات NAT، Timeout باقی‌مانده، شمارنده‌ی بایت/بسته، و وضعیت TCP. جدول State در RAM است و ظرفیت محدود دارد (**Session Exhaustion** حمله‌ی رایج: سیل SYN).

#### ۴-۲) چرخه‌ی عمر یک Session TCP

``` text
Client           Firewall                 Server
SYN  ---------->  (lookup: no session)
                  policy check: allowed
                  create session [SYN_SENT / half-open, short timeout]
                  SYN  ------------------> 
                  <---------------- SYN/ACK
                  [session -> SYN_RECV / ESTABLISHED]
ACK  ---------->  ACK --------------------> 
data <----> data  (fast path: session lookup only; no policy re-eval)
FIN  ---------->  FIN -------------------->
                  [FIN_WAIT / TIME_WAIT] -> removed after timeout
```

نکات:

- **Policy فقط برای بسته‌ی اول** ارزیابی می‌شود. بسته‌های بعدی با Session مطابقت می‌کنند و Policy دوباره بررسی نمی‌شود. بنابراین تغییر Policy روی Sessionهای موجود فوراً اثر نمی‌گذارد (درس ۱۳-۷).
- بسته‌ای که ACK/ دیتا دارد ولی Session برایش نیست (مثلاً بعد از Timeout یا در مسیر Asymmetric) **Drop** می‌شود، چون «ارتباط ناشناخته» است.
- **Half-open** (فقط SYN دیده شده) Timeout کوتاه دارد تا SYN Flood جدول را پر نکند.
- **Established** Timeout طولانی دارد (مثلاً چند ساعت)؛ برای ارتباط‌های بی‌فعالیت مثل SSH ممکن است Session قبل از قطع ارتباط حذف شود (راه‌حل: Keepalive یا افزایش Timeout).

#### ۴-۳) UDP و ICMP

UDP بدون اتصال است؛ فایروال «شبه‌Session» می‌سازد: بسته‌ی اول ← Session با Timeout کوتاه (مثلاً دقایق)، پاسخ مطابق 5-tuple معکوس مجاز. ICMP Echo/Reply با شناسه‌ی Echo (ID) تطبیق می‌شود. برای Error ICMP (مثل Destination Unreachable) فایروال می‌تواند آن را به Session مرتبط (RELATED) نسبت دهد.

#### ۴-۵) Application Layer Gateway و پروتکل‌های چندکاناله

FTP فعال، SIP و ... پورت‌های دوم را در **محتوای** بسته مذاکره می‌کنند. فایروال باید داخل Payload را بخواند (ALG/Helper/Session Helper) و Session فرعی (**Expected/Related Session**) بسازد. اگر Helper غیرفعال یا اشتباه باشد، اتصال داده‌ی FTP قطع می‌شود. (در FortiGate: Session Helper/ALG؛ فصل ۱۳.)

#### ۴-۶) Timeout و حافظه

``` text
Total sessions ~= connections per second x average session lifetime (seconds)
```

مثال: ۲۰۰۰ اتصال در ثانیه و عمر متوسط ۶۰ ثانیه = ۱۲۰٬۰۰۰ Session هم‌زمان. اگر Timeout را از ۶۰ به ۳۶۰۰ ثانیه ببریم، جدول ۶۰ برابر بزرگ می‌شود.

#### ۴-۷) رفتار در Asymmetric و Failover

- Asymmetric: برگشت از فایروال دیگر ← Session نیست ← Drop (درس ۱۰-۶).
- Failover در HA: بدون **Session Sync/Pickup**، Sessionهای TCP قطع می‌شوند و کاربر باید دوباره وصل شود (فصل ۲۲).

### ۵) مثال حل‌شده (Linux conntrack)

#### مثال ساده

بسته‌ی SYN-ACK بدون SYN ⇒ Session ندارد ⇒ Drop.

#### مثال متوسط — Timeoutها

SYN_SENT کوتاه (چند ثانیه)، ESTABLISHED طولانی (ساعت)، TIME_WAIT کوتاه.

#### مثال سخت — SYN Flood

هزاران SYN ساختگی Session Table را پر می‌کنند؛ دفاع: DoS Policy `tcp_syn_flood` با آستانه از Baseline و SYN Cookies.

#### مثال‌های اصلی درس (مرور)

``` text
# Linux router/firewall lab (example)
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -i lan -o wan -m conntrack --ctstate NEW -j ACCEPT
iptables -P FORWARD DROP

conntrack -L | head
conntrack -L -p tcp --dport 443
```

تحلیل: بسته‌ی NEW از LAN به WAN مجاز است؛ پاسخ‌ها با ESTABLISHED رد می‌شوند. یک بسته‌ی ACK ناخواسته از اینترنت (بدون Session) ردیف NEW/INVALID می‌شود و `DROP` پیش‌فرض آن را می‌ریزد.

**مثال متوسط:** SSH بی‌فعالیت پس از ۱۰ دقیقه قطع می‌شود. علت: Timeout Established کوتاه‌تر از انتظار. راه‌حل‌ها: `ServerAliveInterval` در SSH، یا Timeout بلندتر فقط برای سرویس SSH.

**مثال سخت:** فایروال در برابر SYN Flood: ۵۰٬۰۰۰ SYN/s با IP جعلی. بدون محافظت جدول Half-open پر می‌شود و کاربران واقعی Session نمی‌گیرند. راه‌حل‌ها: SYN Cookies/SYN Proxy، DoS Policy (Threshold)، کاهش Timeout Half-open، و محدودیت نرخ Session به‌ازای Source (فصل ۱۶: DoS).

### ۶) طراحی و تصمیم‌گیری

| سؤال | گزینه | معیار |
|---|---|---|
| Timeout پیش‌فرض یا سفارشی؟ | پیش‌فرض / Per-service | سرویس‌های طولانی (SSH، DB) |
| محافظت SYN Flood | DoS Policy / SYN cookie | حساس بودن سرویس به در دسترس بودن |
| ALG روشن یا خاموش؟ | روشن برای FTP/SIP در صورت نیاز | امنیت در برابر سازگاری |
| ظرفیت Session | محاسبه‌ی CPS × عمر | انتخاب مدل/لایسنس |

### ۷) Verification (Linux و مفهومی)

``` text
conntrack -L
conntrack -C
sysctl net.netfilter.nf_conntrack_max
sysctl net.netfilter.nf_conntrack_tcp_timeout_established
```

- شمارش Session (`conntrack -C`) را با حد (`nf_conntrack_max`) مقایسه کنید.
- در FortiGate معادل: `diagnose sys session list` و `get system performance status` (فصل ۱۳ و ۱۴).

### ۸) Troubleshooting

| علامت | شاهد | علت |
|---|---|---|
| ارتباط طولانی قطع می‌شود | Session حذف بعد از X دقیقه | Timeout |
| SYN می‌رود، SYN/ACK برنمی‌گردد | Capture | Policy/Route/Asymmetric |
| پاسخ‌ها Drop می‌شوند | Log: no session | Asymmetric یا Timeout |
| FTP لیست دایرکتوری نمی‌دهد | Capture | ALG/Helper |
| کاربران جدید Session نمی‌گیرند | جدول پر | Session Exhaustion/حمله |

### ۹) نکات امنیتی

- Stateful بخشی از دفاع است؛ فایروال محتوا را نمی‌فهمد مگر UTM/IPS فعال باشد.
- Timeoutهای بسیار بلند برای همه‌ی سرویس‌ها ریسک Exhaustion دارند.
- Logging باید بسته‌های Drop به‌دلیل «بدون Session» را ثبت کند؛ نشانه‌ی Asymmetric یا اسکن است.

### ۱۰) جمع‌بندی مفهومی

- Stateless بسته را مستقل می‌سنجد؛ Stateful ارتباط را می‌شناسد.
- Policy فقط برای بسته‌ی اول؛ بعد از آن Session Lookup.
- جدول State محدود و هدف DoS است؛ Timeout تعادل کارایی/امنیت است.
- بدون Session، بسته‌ی برگشت Drop می‌شود (Asymmetric، Timeout).
- ALG برای پروتکل‌های چندکاناله لازم است.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) تفاوت Stateless و Stateful را بگویید. *(پاسخ: 11-7-ت1)*

**ت2.** (ساده) 5-tuple شامل چه فیلدهایی است؟ *(پاسخ: 11-7-ت2)*

**ت3.** (متوسط) چرا پس از ایجاد Session، Policy برای هر بسته بازبینی نمی‌شود؟ *(پاسخ: 11-7-ت3)*

**ت4.** (متوسط) ۱۵۰۰ اتصال در ثانیه با عمر متوسط ۴۵ ثانیه چند Session هم‌زمان می‌سازد؟ *(پاسخ: 11-7-ت4)*

**ت5.** (سخت) SSH کاربر پس از ۲۰ دقیقه سکوت قطع می‌شود. سه راه‌حل با مزایا/ریسک بدهید. *(پاسخ: 11-7-ت5)*

**ت6.** (سخت، طراحی) برای سرور وب روی اینترنت، محافظت در برابر SYN Flood را از سه لایه (فایروال، سرور، شبکه) شرح دهید. *(پاسخ: 11-7-ت6)*

**م1.** Half-open Session چیست؟ *(پاسخ: 11-7-م1)*

**Q1.** Quick quiz (English): Why are return packets accepted by a stateful firewall without an explicit rule? *(پاسخ: 11-7-Q1)*

### ۱۲) اصطلاحات و English Corner

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

### ۱۳) منابع

- NIST SP 800-41 Rev.1 — Guidelines on Firewalls and Firewall Policy (Stateful Inspection).
- RFC 9293 — Transmission Control Protocol (TCP).
- Linux kernel documentation: nf_conntrack sysctl.

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: Stateful Inspection از درون — State Table و TCP State

#### چرا؟

دانستن اینکه Session چطور ساخته و حذف می‌شود، رفتارهای عجیب را توضیح می‌دهد.

#### TCP State

``` text
SYN_SENT -> SYN_RECV -> ESTABLISHED -> FIN_WAIT -> TIME_WAIT -> CLOSED
```

فایروال Session را با SYN می‌سازد؛ بسته‌ی بعدی باید با آن همخوان باشد (Sequence در Window).

#### مثال ساده

بسته‌ی SYN-ACK بدون SYN ⇒ Session ندارد ⇒ Drop.

#### مثال متوسط — Timeoutها

هر State Timeout دارد؛ SYN_SENT کوتاه، ESTABLISHED طولانی، TIME_WAIT کوتاه.

#### مثال سخت — SYN Flood

هزاران SYN ساختگی Session Table را پر می‌کنند. دفاع: DoS Policy با آستانه (`tcp_syn_flood`) و SYN Cookies.

#### Lab

Session را در هر State ببینید.

``` text
diagnose sys session list | grep proto_state
```

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Drop بسته‌ی ACK | بی‌Session | نامتقارن |
| Table پر | SYN flood | DoS |
| قطع زود | Timeout | تنظیم |

#### پرسش‌ها با پاسخ

**۱. Session با چه ساخته می‌شود؟** SYN.
**۲. SYN flood؟** پر شدن جدول.
**۳. Timeout هر State؟** متفاوت.

#### English Corner

- *A stateful firewall creates a session on the first SYN and validates later packets against it.*
- Q: How does a DoS policy protect the session table?

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

دو نکته‌ی فراتر از جدول:

- **DNAT قبل از Route و Policy** اتفاق می‌افتد؛ بنابراین Policy باید بر اساس آدرس **مقصد بعد از DNAT** (آدرس داخلی) تطبیق شود، نه IP عمومی VIP. در مستند Fortinet و مقاله‌ی Central NAT این ترتیب «ingress → session lookup → DNAT → route → policy → SNAT» آمده است.
- **SNAT بعد از Policy** است؛ Policy مبدأ اصلی (قبل از SNAT) را می‌بیند.

#### ۴-۲) Ingress و Anti-spoofing (RPF)

FortiGate هر بسته‌ی ورودی را با **Reverse Path Forwarding (RPF)** می‌سنجد: آیا بهترین مسیر به آدرس **مبدأ** از همان Interfaceی که بسته آمده می‌گذرد؟ اگر نه، به‌عنوان جعل/Asymmetric Drop می‌شود (Debug: `reverse path check fail, drop`). این یکی از شایع‌ترین دلایل Drop در شبکه‌های نامتقارن یا با Route ناقص است (فصل ۱۰-۶، ۲۳).

#### ۴-۳) Session Lookup (Fast path)

اگر بسته با یک Session موجود (در یکی از جهت‌ها) مطابقت کند، Route و Policy برای آن دوباره بررسی نمی‌شوند (به‌جز موارد خاص مثل تغییر Route و `session-route-check`). نتیجه:

- پاسخ‌های برگشتی بدون Policy عبور می‌کنند (چون Session دارند).
- تغییر Policy یا Route روی **Sessionهای موجود** تا پایان Session یا پاک کردن آن اثر ندارد (درس ۱۳-۷).

#### ۴-۴) Route Lookup

انتخاب Interface خروجی و Next-hop با همان قواعد (LPM، Distance، Priority، Policy Route). در FortiOS: ترتیب بررسی: **Policy Route (PBR)** ← **SD-WAN Rule** ← **Routing Table (RIB/FIB)**. (جزئیات SD-WAN: فصل ۲۱.) **Zone** و Interface خروجی همین‌جا مشخص می‌شود.

> تفاوت مهم: **Routing می‌گوید بسته از کجا برود؛ Policy می‌گوید اجازه‌ی عبور دارد یا نه.** هر دو باید درست باشند؛ Route درست و Policy غایب = Drop؛ Policy درست و Route غلط = Drop یا مسیر اشتباه.

#### ۴-۵) Policy Lookup

بررسی Policyها **از بالا به پایین؛ اولین تطبیق برنده است (First Match)**. فیلدهای تطبیق: Incoming Interface/Zone، Outgoing Interface/Zone، Source (آدرس/کاربر/دستگاه)، Destination، Service، Schedule. اگر هیچ Policy مطابق نباشد، **Implicit Deny** (Policy شناسه‌ی 0) و ثبت `Denied by forward policy check (policy 0)`.

#### ۴-۶) Security Profile Inspection

پس از تطبیق Policy، اگر Profileها وصل باشند (AV، IPS، Web Filter، Application Control، SSL Inspection ...)، بسته/جریان بر اساس **Inspection Mode (Flow یا Proxy)** بازرسی می‌شود. در 7.0 حالت بازرسی در **هر Policy** تنظیم می‌شود (`set inspection-mode flow|proxy`). جزئیات در فصل ۱۶.

#### ۴-۷) NAT و ساخت Session

اگر Policy NAT فعال باشد، آدرس مبدأ به IP خروجی Interface یا IP Pool تغییر می‌کند و در Session ذخیره می‌شود تا بسته‌های بعدی و پاسخ بدون پردازش مجدد ترجمه شوند. پس هر Session دو جهت دارد: Original و Reply.

#### ۴-۸) ترافیک Local-in و Local-out (مرور)

ترافیکی که **مقصدش خود FortiGate** است (Local-in) یا **مبدأش خود FortiGate** است (Local-out) مسیر متفاوتی دارد و Forward Policy بر آن اعمال نمی‌شود؛ درس ۱۲-۸ آن را کامل توضیح می‌دهد.

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
- Session موجود Policy/Route را دور می‌زند.
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

- *The firewall policy is evaluated only for the first packet of a session.* ← Policy فقط برای بسته‌ی اول Session ارزیابی می‌شود.
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

| علامت | علت | رفع |
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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. اجزای معماری (CPU/NPU، FortiOS، VDOM root، Management) را شرح دهد.
2. مراحل اولین بوت (کنسول، IP پیش‌فرض، تغییر رمز) را اجرا کند.
3. نسخه، سریال، لایسنس و HA را با `get system status` تأیید کند.
4. تنظیمات پایه (hostname، timezone، DNS، NTP) را اعمال کند.
5. تأیید کند نسخه‌ی روی دستگاه همان نسخه‌ی هدف دوره (7.0.3) است و در صورت مغایرت گزارش دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا باید معماری FortiGate را بشناسیم؟** وقتی با یک دستگاه ناآشنا شروع می‌کنید، اولین سؤال‌ها این است: «چه سیستم‌عاملی؟ چه نسخه‌ای؟ لایسنس دارد؟ چه چیزی را می‌توانم تنظیم کنم؟». مثل رانندگی با ماشین جدید: قبل از حرکت باید بدانید دنده، فرمان و ترمز کجاست.

**اجزای اصلی**

- **FortiOS:** سیستم‌عامل فورتی‌گیت. همه‌ی دستورها و قابلیت‌ها به نسخه‌ی آن بستگی دارد (در این دوره 7.0.3 «نامی» و بوت‌نشده).
- **CPU:** پردازش عمومی و بازرسی عمیق (UTM).
- **NPU/SPU:** تراشه‌ی سخت‌افزاری که Sessionهای ساده را سریع عبور می‌دهد (درس ۱۲-۹).
- **Management plane:** ورود ادمین (CLI، GUI، API).
- **Data plane:** عبور ترافیک.

**اولین بوت:** ورود با کنسول یا Interface مدیریتی، تغییر رمز پیش‌فرض ادمین، بررسی نسخه (`get system status`) و لایسنس. در Lab ما FortiGate VM بدون لایسنس معتبر است؛ بنابراین بسیاری از قابلیت‌ها «Needs-License» و اجرا نشده‌اند.

**جمع‌بندی اصلی درس:** دستگاه جدید را از جعبه درمی‌آورید. پیش از هر Policy باید بدانید چه دستگاهی است، چه نسخه‌ای دارد و لایسنس دارد یا نه؛ چون ویژگی‌ها و دستورها به نسخه وابسته‌اند و «همان‌طور که در دوره نوشته شده» کار نمی‌کند اگر نسخه فرق کند.

### ۳) توضیح عمیق فنی

#### ۱) معماری

``` text
Console/GUI/SSH --> FortiOS (control plane: routing, policy, daemons)
Traffic --> CPU (flow) and/or NPU/SPU (offload) --> interfaces
```

مدل‌های دارای NPU بخشی از ترافیک را Offload می‌کنند (درس ۱۲-۹). نسخه‌ی مجازی (VM) NPU ندارد و برای Lab مناسب است.

#### ۲) اولین اتصال

| مورد | مقدار پیش‌فرض رایج |
|---|---|
| Admin | admin |
| رمز | خالی (در اولین ورود الزام تغییر) |
| IP مدیریت | 192.168.1.99/24 روی مدل‌های سخت‌افزاری (طبق مدل متفاوت) |

رمز را بلافاصله قوی کنید و در Inventory ننویسید (طبق قوانین پروژه).

#### ۳) تأیید نسخه

``` text
get system status
```

خروجی باید Version (مثلاً v7.0.3 build ...)، Serial، License Status، Hostname و Operation Mode را نشان دهد.

#### ۴) تنظیمات پایه

``` text
config system global
 set hostname FGT-EDGE-01
 set timezone 26
end
config system dns
 set primary 1.1.1.1
 set secondary 8.8.8.8
end
config system ntp
 set ntpsync enable
 set type fortiguard
end
```

کد منطقه‌ی زمانی عددی است و طبق CLI help (`set timezone ?`) باید انتخاب شود.

#### ۵) نسخه‌ی هدف

دوره روی 7.0.3 نوشته شده؛ اگر دستگاه نسخه‌ی دیگری دارد، هر درس را با Release Notes همان نسخه مقایسه کنید و تفاوت را ثبت کنید، نه اینکه دستور را کورکورانه بزنید.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| نام‌گذاری | سایت-نقش-شماره |
| NTP | FortiGuard یا داخلی |
| نسخه | نسخه‌ی پایدار و توصیه‌شده‌ی Fortinet برای مدل |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — خواندن `get system status`

``` text
Version: FortiGate-VM64 v7.0.3,build...
Virtual domain configuration: disable
Serial-Number: FGVM...
License Status: Valid / Trial (check)
```

از آن نسخه، حالت VDOM و وضعیت لایسنس را بخوانید. اگر نسخه با مستندات شما نمی‌خواند، دستورها ممکن است متفاوت باشد.

#### مثال متوسط — اولین ورود ایمن

``` text
config system admin
 edit admin
  set password ***
 next
end
config system interface
 edit mgmt
  set allowaccess https ssh ping
 next
end
```

رمز جدید در Vault؛ فقط HTTPS/SSH؛ Telnet/HTTP هرگز.

#### مثال سخت — «ویژگی در GUI نیست»

1. آیا لایسنس/مدل پشتیبانی می‌کند؟ (دیتاشیت)
2. آیا در Feature Visibility خاموش است؟ (`config system settings` / GUI System ← Feature Visibility)
3. آیا نسخه‌ی FortiOS آن را دارد؟ (Release Notes)
4. آیا در حالت VDOM اشتباه هستید؟

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** `get system status` را می‌زنید؛ نسخه 7.0.3؛ License valid؛ hostname تغییر می‌کند.

**متوسط (تحلیل):** پس از تغییر hostname، SSH قطع شد؟ خیر؛ ولی اگر `set timezone` اشتباه باشد لاگ‌ها ساعت غلط دارند؛ برای Correlation در SIEM مشکل می‌شود؛ پس NTP را بررسی کنید: `diagnose sys ntp status`.

**سخت (مغایرت نسخه):** دستگاه v7.2 دارد ولی دوره 7.0.3؛ مراحل: ثبت نسخه، مقایسه Release Notes، علامت `Unverified` روی دستورهای مشکوک، و عدم Downgrade بدون Backup و تأیید.

### ۶) پیاده‌سازی از مسیر GUI

1. ورود به GUI از طریق IP مدیریت.
2. Dashboard → System Information: نسخه و سریال.
3. System → Settings: Hostname، Timezone، NTP.
4. Network → DNS.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get system status
get system performance status
diagnose sys ntp status
show system global | grep hostname
```

### ۸) Verification (اثبات صحت)

- نسخه و Build ثبت شده.
- License وضعیت صحیح.
- NTP همگام.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ورود ممکن نیست | کابل/IP/Admin access | کنسول؛ IP را بررسی |
| NTP sync نمی‌شود | DNS/Route | DNS و مسیر اینترنت |
| License invalid | FortiCare | ثبت/اتصال |

### ۱۰) نکات امنیتی

- رمز قوی و تغییر پیش‌فرض.
- مدیریت فقط روی Interface مدیریتی.

### ۱۱) جمع‌بندی مفهومی

- اول شناخت دستگاه.
- نسخه مرجع است.
- Hostname/NTP/DNS پایه‌اند.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) کدام دستور نسخه را نشان می‌دهد؟ *(پاسخ: 12-1-ت1)*

**ت2.** (ساده) چرا NTP مهم است؟ *(پاسخ: 12-1-ت2)*

**ت3.** (متوسط) چرا نسخه‌ی دستگاه باید با دوره تطبیق شود؟ *(پاسخ: 12-1-ت3)*

**ت4.** (متوسط) رمز پیش‌فرض را چه کنیم؟ *(پاسخ: 12-1-ت4)*

**ت5.** (سخت) نسخه v7.2 است؛ چه می‌کنید؟ *(پاسخ: 12-1-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی اولین بوت. *(پاسخ: 12-1-ت6)*

**Q1.** Quick quiz (English): Which command displays the FortiOS version and serial number? *(پاسخ: 12-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NPU | Network Processor Unit | پردازنده‌ی شبکه |
| VDOM | Virtual Domain | دامنه‌ی مجازی |
| NTP | Network Time Protocol | هماهنگ‌سازی زمان |

- *Always verify the firmware version first.* ← همیشه اول نسخه‌ی Firmware را تأیید کنید.

### ۱۴) کارت Lab

**کارت Lab:** اولین بوت (اجرا نشده). **Evidence:** `03-ops/fgt-asbuilt-1.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Getting started
- FortiOS 7.0.3 Release Notes

<a id="l-12-2"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: برگه‌ی اولین بوت با خروجی نمونه و تصمیم‌ها

**سناریو.** FortiGate جدید برای شعبه رسیده؛ باید قبل از هر Policy «شناسنامه»اش را ثبت کنید.

**گام ۱ — خروجی‌های حیاتی.**

``` text
FGT-BR1 # get system status
Version: FortiGate-60F v7.0.3,build...
Serial-Number: FGT60FTK...
Operation Mode: NAT
Current virtual domain: root
Virtual domain configuration: disable
License Status: Valid
Hostname: FGT-BR1
```

تفسیر: نسخه با نسخه‌ی هدف دوره مقایسه می‌شود؛ Virtual domain disable یعنی تک‌VDOM؛ License Valid یعنی FortiCare/FortiGuard فعال است (برای UTM لازم).

**گام ۲ — تنظیمات پایه (ترتیب).**

``` text
config system global
 set hostname FGT-BR1
 set timezone 26
end
config system ntp
 set ntpsync enable
 set type fortiguard
end
config system dns
 set primary 1.1.1.1
 set secondary 8.8.8.8
end
```

**گام ۳ — ثبت Inventory.** جدول: Hostname، Serial، Version، License تا تاریخ، IP مدیریت، مالک، تاریخ بوت. و Backup اولیه: `execute backup config tftp ...`.

**گام ۴ — اختلاف نسخه.** اگر Image شما 7.2.x است، پیش از استفاده از درس‌ها Release Notes را برای تغییر رفتار (SD-WAN، SSL-VPN، لاگ) بخوانید؛ هر دستور مشکوک را در Evidence با «نسخه‌ی واقعی» ثبت کنید.

**اشتباهات رایج**
- فراموشی NTP: Logها، گواهی و Kerberos/VPN آسیب می‌بینند.
- رمز پیش‌فرض و Admin پیش‌فرض.
- نداشتن Backup پیش از تغییر.

**پرسش‌های مصاحبه**
1. *اولین کار روی دستگاه جدید؟* تأیید نسخه/لایسنس/سریال و Backup.
2. *Operation Mode NAT در برابر Transparent؟* NAT مسیریابی L3 می‌کند؛ Transparent مثل Bridge.
3. *VDOM چیست و کی فعال می‌شود؟* جداسازی مجازی؛ فقط در صورت نیاز و لایسنس.

### تکمیل عمیق: معماری FortiGate و اولین بوت

#### چرا؟

قبل از پیکربندی باید بدانید با چه چیزی کار می‌کنید: FortiOS، VM یا سخت‌افزار، NPU/CPU و روش‌های دسترسی.

#### اجزا

| جزء | نقش |
|---|---|
| FortiOS | سیستم‌عامل |
| CPU | پردازش عمومی/UTM |
| NPU (SPU) | Offload ترافیک |
| Management plane | CLI/GUI/API |
| Data plane | عبور ترافیک |

#### مثال ساده — تأیید نسخه

``` text
get system status
```

نسخه، Serial، HA، Virtual Domain، License Status را می‌خوانید. در این دوره FortiOS 7.0.3 «نامی» است و بوت نشده.

#### مثال متوسط — اولین دسترسی

کنسول یا HTTPS مدیریتی روی Interface مدیریتی؛ پیش‌فرض ادمین بدون رمز در بعضی مدل‌هاست و باید بلافاصله تغییر کند.

``` text
config system admin
 edit admin
  set password ***
 next
end
```

#### مثال سخت — لایسنس VM

FortiGate VM بدون لایسنس معتبر عملاً محدود (Trial) است؛ بسیاری از قابلیت‌ها Needs-License هستند و اجرا نشده.

#### Lab

نسخه و ظرفیت مدل را از دیتاشیت رسمی بخوانید و جدول بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| GUI باز نمی‌شود | allowaccess | CLI |
| ویژگی نیست | لایسنس/مدل | دیتاشیت |
| نسخه ناهمخوان | Release Notes | بررسی |

#### پرسش‌ها با پاسخ

**۱. NPU؟** شتاب سخت‌افزاری.
**۲. چرا رمز اول؟** امنیت.
**۳. Needs-License؟** نیاز به اشتراک.

#### English Corner

- *Change the default administrator credentials during the first boot.*
- Q: What are the management plane and data plane?

## درس 12-2 — Interface، VLAN، Role، Administrative Access و سخت‌سازی پورت‌های FortiGate

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۱، ۳-۱، ۴-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. انواع Interface (Physical، VLAN، Aggregate/LACP، Loopback، Zone) را بشناسد و کاربرد هرکدام را بگوید.
2. IP، Role، Alias و Allowaccess را درست پیکربندی کند.
3. VLAN Sub-interface را با Trunk سوییچ هماهنگ کند.
4. فقط سرویس‌های لازم را روی هر Interface باز و WAN را سخت‌سازی کند.
5. Verification (وضعیت لینک، آمار خطا، ARP) را اجرا کند.
6. خطاهای رایج (VLAN، Duplex، Allowaccess) را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Interface و دسترسی مدیریتی؟** Interface دروازه‌ی ورود ترافیک است، و همچنین دروازه‌ی ورود مدیریت. یک تنظیم اشتباه `allowaccess` روی WAN پنل مدیریت را به اینترنت می‌دهد.

**مفاهیم**

- **Interface فیزیکی و VLAN Interface:** VLAN با برچسب 802.1Q روی پورت Trunk.
- **Role:** lan/wan/dmz؛ رفتار GUI و پیش‌فرض‌ها را تغییر می‌دهد.
- **allowaccess:** سرویس‌های مدیریتی که روی Interface پاسخ می‌دهند (ping، https، ssh، snmp).
- **Trusted Host:** فقط از IPهای مشخص مجاز.

**اصل:** مدیریت فقط روی Interface مدیریتی و از شبکه‌ی Mgmt؛ WAN هیچ‌چیز یا حداکثر ping.

**جمع‌بندی اصلی درس:** FortiGate را به شبکه وصل می‌کنید و «کار نمی‌کند». ۷۰٪ مواقع علت در Interface است: کابل در پورت دیگر، VLAN ID اشتباه، یا Allowaccess بسته. و بدتر: مدیر برای راحتی HTTPS را روی WAN باز می‌گذارد و چند روز بعد پنل مدیریت از اینترنت Brute-force می‌شود.

Interface در FortiGate فقط پورت فیزیکی نیست؛ تعیین می‌کند چه کسی با دستگاه چه سرویسی صحبت کند، در چه Zoneای است و Policy به چه نامی به آن ارجاع می‌دهد.

### ۳) توضیح عمیق فنی

#### ۱) انواع Interface

| نوع | کاربرد |
|---|---|
| Physical | پورت واقعی (port1...) |
| VLAN | Sub-interface با vlanid روی Physical/Aggregate |
| Aggregate (LACP) | تجمیع چند لینک برای پهنای باند و افزونگی |
| Loopback | آدرس پایدار برای مدیریت/BGP/IPsec |
| Zone | گروه Interfaceها در Policy |
| Software Switch | چند پورت در یک Bridge L2 |

#### ۲) پیکربندی پایه

``` text
config system interface
 edit "port1"
  set alias "WAN-ISP-A"
  set mode static
  set ip 198.51.100.2 255.255.255.252
  set allowaccess ping
  set role wan
  set description "To ISP-A circuit ID XYZ"
 next
 edit "port2"
  set alias "LAN-TRUNK"
  set mode static
  set ip 10.10.0.1 255.255.255.0
  set allowaccess ping
  set role lan
 next
 edit "VLAN20"
  set vdom "root"
  set interface "port2"
  set vlanid 20
  set ip 10.20.0.1 255.255.255.0
  set allowaccess ping
  set role lan
 next
end
```

#### ۳) Role

Role (wan، lan، dmz، undefined) روی نمایش GUI، پیشنهادهای Policy و Security Fabric اثر دارد؛ بر مسیر بسته اثر ندارد. با این حال Role درست مستندسازی را آسان می‌کند.

#### ۴) Allowaccess (حیاتی)

| سرویس | توصیه |
|---|---|
| https، ssh | فقط Mgmt و با Trusted host |
| ping | محدود (WAN فقط در صورت نیاز) |
| http، telnet | غیرفعال |
| snmp | فقط Mgmt و نسخه‌ی ۳ |
| fgfm | فقط برای FortiManager |
| fabric | فقط لینک Fabric |

``` text
set allowaccess https ssh ping    ! only on MGMT interface
```

#### ۵) VLAN و Trunk

VLAN20 روی port2 فقط وقتی کار می‌کند که پورت سوییچ مقابل Trunk باشد و VLAN 20 را Allow کند. علامت خرابی: لینک up ولی ping به Gateway/کلاینت نه، و ARP incomplete.

#### ۶) Verification

``` text
get system interface physical
diagnose hardware deviceinfo nic port2
diagnose ip arp list
show system interface VLAN20
```

شمارنده‌های خطا (CRC، collisions) و Speed/Duplex را بخوانید؛ عدم‌تطابق Duplex علامت «کند ولی up» است.

#### ۷) Aggregate (LACP)

``` text
config system interface
 edit "agg1"
  set type aggregate
  set member "port5" "port6"
  set lacp-mode active
  set ip 10.50.0.1 255.255.255.0
 next
end
```

سوییچ هم باید LACP active/passive باشد؛ عدم‌تطابق باعث Flap می‌شود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Role | lan/wan/dmz |
| Mgmt | Interface جدا |
| Aggregate | برای لینک پرترافیک و افزونگی |
| Alias/Description | شناسه‌ی مدار و مالک |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — VLAN

``` text
config system interface
 edit "vlan10"
  set vdom "root"
  set interface "port2"
  set vlanid 10
  set ip 10.10.0.1 255.255.255.0
  set allowaccess ping
 next
end
```

#### مثال متوسط — Trusted Host

``` text
config system admin
 edit "netadmin"
  set trusthost1 10.50.0.0 255.255.255.0
 next
end
```

حتی با رمز درست، ورود فقط از شبکه‌ی Mgmt ممکن است.

#### مثال سخت — قفل‌شدن از مدیریت

پس از تغییر allowaccess، GUI قطع شد. راه نجات: کنسول؛ تنظیم برگردد. پیشگیری: `cfg-save revert` (درس ۱۲-۷) و Session دوم باز.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** ورودی: port2 با IP 10.10.0.1/24 و ping. مراحل: ۱) `edit port2`. ۲) `set ip ...`. ۳) `set allowaccess ping`. ۴) از PC با ping 10.10.0.1 آزمون. پاسخ: جواب می‌گیرید؛ ولی HTTPS باز نیست چون allowaccess ندارد (مطلوب).

**متوسط (VLAN):** VLAN20 ساخته شد ولی ping به 10.20.0.1 از PC ناموفق. مراحل: ۱) `get system interface physical` لینک up. ۲) `diagnose ip arp list` برای 10.20.0.x ورودی ندارد. ۳) پورت سوییچ Access روی VLAN 1 است، نه Trunk. رفع: Trunk allowed 20. آزمون: ping و ARP.

**سخت (سخت‌سازی WAN):** لاگ نشان می‌دهد صدها تلاش ورود به HTTPS از اینترنت. مراحل: ۱) `show system interface port1` allowaccess شامل https ssh. ۲) حذف به ping (یا هیچ). ۳) مدیریت فقط از Mgmt با Trusted host. ۴) Local-in policy برای تکمیل. ۵) آزمون: از اینترنت nmap پورت 443/22 بسته. ۶) Log تلاش‌ها کاهش. درس: WAN بدون مدیریت.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Interfaces → Edit.
2. IP/Netmask، Role، Alias و Administrative Access را تنظیم کنید.
3. Create New → Interface → Type: VLAN، VLAN ID.
4. Create New → Interface → Type: 802.3ad Aggregate.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system interface
 edit "port2"
  set ip 10.10.0.1 255.255.255.0
  set allowaccess ping
 next
end
get system interface physical
diagnose ip arp list
```

### ۸) Verification (اثبات صحت)

- لینک up، Speed/Duplex صحیح.
- ping Gateway/کلاینت.
- Allowaccess حداقل.
- آزمون nmap از WAN.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| VLAN کار نمی‌کند | Trunk/VLAN سوییچ | Trunk allowed |
| کند ولی up | Duplex/CRC | Auto-neg/کابل |
| GUI باز نمی‌شود | allowaccess/Trusted host | https روی Interface |
| LACP flap | mode دو سر | active/passive |

### ۱۰) نکات امنیتی

- WAN: بدون مدیریت.
- Trusted host برای Admin.
- Telnet/HTTP غیرفعال.

### ۱۱) جمع‌بندی مفهومی

- Interface تعیین‌کننده‌ی مدیریت و Policy.
- Allowaccess حداقل.
- VLAN با Trunk.
- Aggregate با LACP هماهنگ.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) allowaccess چیست؟ *(پاسخ: 12-2-ت1)*

**ت2.** (ساده) VLAN Sub-interface چیست؟ *(پاسخ: 12-2-ت2)*

**ت3.** (متوسط) چرا نباید https روی WAN باز باشد؟ *(پاسخ: 12-2-ت3)*

**ت4.** (متوسط) لینک up ولی VLAN کار نمی‌کند؛ علت‌ها؟ *(پاسخ: 12-2-ت4)*

**ت5.** (سخت) از اینترنت Brute-force می‌شود؛ طرح رفع. *(پاسخ: 12-2-ت5)*

**ت6.** (سخت، طراحی) Interfaceهای یک شعبه با WAN، LAN، DMZ، Mgmt. *(پاسخ: 12-2-ت6)*

**Q1.** Quick quiz (English): Which setting controls which management services are reachable on an interface? *(پاسخ: 12-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| LACP | Link Aggregation Control Protocol | پروتکل تجمیع لینک |
| Trunk | 802.1Q trunk | لینک حامل چند VLAN |

- *Never expose management services on the WAN interface.* ← هرگز سرویس‌های مدیریتی را روی Interface WAN باز نگذارید.

### ۱۴) کارت Lab

**کارت Lab:** Interface و VLAN (اجرا نشده). **Evidence:** `02-design/fgt-interfaces.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Interfaces
- FortiOS 7.0 Hardening guide

<a id="l-12-3"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: طراحی Interfaceهای یک شعبه و پرونده‌ی «VLAN کار نمی‌کند»

**سناریو.** شعبه با WAN (port1)، Trunk داخلی (port2) با VLAN 10 Users و VLAN 20 Servers، DMZ (port3) و Mgmt (mgmt).

**جدول طراحی**

| Interface | IP | Role | allowaccess | یادداشت |
|---|---|---|---|---|
| port1 | 198.51.100.2/30 | wan | - | بدون مدیریت |
| port2.10 | 10.10.0.1/24 | lan | ping | Users |
| port2.20 | 10.20.0.1/24 | lan | ping | Servers |
| port3 | 10.30.0.1/24 | dmz | ping | وب |
| mgmt | 10.99.0.1/24 | lan | https ssh ping | با Trusted host |

**پیکربندی VLAN**

``` text
config system interface
 edit "VLAN10"
  set vdom "root"
  set interface "port2"
  set vlanid 10
  set ip 10.10.0.1 255.255.255.0
  set allowaccess ping
  set role lan
 next
end
```

**عیب‌یابی «VLAN10 Ping Gateway ندارد»**

``` text
get system interface physical        ! port2 up, speed 1000 full
diagnose ip arp list                  ! no entry for 10.10.0.x -> L2 issue
```

شاهد: ARP بدون ورودی ⇒ پورت سوییچ Access روی VLAN 1 است؛ باید Trunk (`switchport mode trunk` + `allowed vlan 10,20`).

**Hardening WAN.** اگر لاگ‌ها تلاش ورود به HTTPS از اینترنت نشان می‌دهد: allowaccess را از port1 حذف کنید، مدیریت فقط از Mgmt، Trusted host، MFA.

**اشتباهات رایج**
- allowaccess https روی WAN.
- VLAN بدون Trunk روی سوییچ.
- Speed/Duplex ناهماهنگ (کند ولی Up).

**پرسش‌های مصاحبه**
1. *Role چه اثری دارد؟* GUI/Fabric؛ نه مسیر بسته.
2. *Zone چه فایده؟* گروه‌کردن Interfaceها در Policy.
3. *LACP چه می‌کند؟* تجمیع لینک برای پهنای باند و افزونگی.

### تکمیل عمیق: Interface، VLAN، Role و دسترسی مدیریتی

#### چرا؟

Interface نقطه‌ی ورود ترافیک و مدیریت است؛ تنظیم اشتباه `allowaccess` مدیریت را به اینترنت می‌دهد.

#### مثال ساده — VLAN Interface

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

#### مثال متوسط — حداقل مدیریت

روی WAN فقط `ping` یا هیچ؛ روی Mgmt: `https ssh ping`. هرگز `http`/`telnet`.

#### مثال سخت — Trusted Host

``` text
config system admin
 edit "netadmin"
  set trusthost1 10.50.0.0 255.255.255.0
 next
end
```

حتی با رمز لورفته، ورود فقط از Mgmt ممکن است.

#### Role

Roleها (lan/wan/dmz/undefined) رفتار GUI و پیش‌فرض‌ها را تغییر می‌دهند؛ برای WAN Role wan.

#### Lab

یک VLAN و حداقل دسترسی بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| ping نمی‌آید | allowaccess | افزودن |
| ورود از اینترنت | allowaccess | حذف |
| VLAN کار نمی‌کند | Trunk | سوئیچ |

#### پرسش‌ها با پاسخ

**۱. Trusted Host؟** مبدأ مجاز ادمین.
**۲. چرا WAN بی‌مدیریت؟** سطح حمله.
**۳. VLAN ID؟** برچسب 802.1Q.

#### English Corner

- *Management access on the WAN interface should be disabled.*
- Q: What does a trusted host restrict?

## درس 12-3 — Zone و Objectها: Address، Service، Group، Schedule و استاندارد نام‌گذاری

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۲، ۱۱-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Zone را بسازد و مزیت آن را بر Interface مستقل توضیح دهد.
2. Address (Subnet، Range، FQDN، Geography)، Service و Group را بسازد.
3. استاندارد نام‌گذاری و Comment را رعایت کند.
4. Objectها را در Policy درست استفاده و بلااستفاده‌ها را پاک کند.
5. تغییر Object را با اثر بر Policyها ارزیابی کند.
6. Where-used را برای ممیزی به‌کار ببرد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Objectها؟** به‌جای نوشتن IP و پورت در هر Policy، یک نام می‌دهید («SRV-ERP»). با تغییر IP فقط یک Object اصلاح می‌شود، نه ده‌ها Policy. و اگر نام‌گذاری استاندارد باشد، Policy مثل جمله خوانده می‌شود.

**انواع:** Address، Address Group، Service، Service Group، Schedule، VIP، IP Pool. **Zone** گروه Interface است. **قرارداد نام** (مثال: NET-، SRV-، GRP-، SVC-، ZN-) و **comment** با مالک.

**جمع‌بندی اصلی درس:** Policy بدون Object مثل کدی با عددهای جادویی است: «10.20.0.10» در ۴۰ Policy پخش شده و وقتی سرور عوض شد، باید ۴۰ جا را پیدا کنید. با Object، فقط یک تعریف عوض می‌شود و همه‌ی Policyها به‌روز می‌شوند. Zone همین ایده برای Interfaceهاست.

### ۳) توضیح عمیق فنی

#### ۱) Zone

``` text
config system zone
 edit "ZN-SERVER"
  set interface "port3" "VLAN20"
  set intrazone deny
 next
end
```

`intrazone deny` یعنی ترافیک بین اعضای همان Zone بدون Policy رد می‌شود (امن‌تر)؛ `allow` رفتار L2-ish.

نکته: Interface عضو Zone دیگر مستقیماً در Policy انتخاب نمی‌شود؛ Zone جایگزین است.

#### ۲) Address

``` text
config firewall address
 edit "NET-USERS"
  set subnet 10.10.0.0 255.255.255.0
 next
 edit "SRV-WEB"
  set subnet 10.30.0.10 255.255.255.255
 next
 edit "RNG-GUEST"
  set type iprange
  set start-ip 10.60.0.10
  set end-ip 10.60.0.200
 next
 edit "FQDN-UPDATE"
  set type fqdn
  set fqdn "update.vendor.com"
 next
end
```

FQDN به DNS وابسته است؛ در Policy خروجی مفید ولی خطای DNS = خطای Policy.

#### ۳) Service

``` text
config firewall service custom
 edit "TCP-8443"
  set tcp-portrange 8443
 next
end
config firewall service group
 edit "GRP-WEB"
  set member "HTTP" "HTTPS"
 next
end
```

#### ۴) Address Group

``` text
config firewall addrgrp
 edit "GRP-SERVERS"
  set member "SRV-WEB" "SRV-APP" "SRV-DB"
 next
end
```

#### ۵) استاندارد نام‌گذاری

| نوع | الگو | نمونه |
|---|---|---|
| Subnet | NET- | NET-USERS |
| Host | SRV-/HOST- | SRV-DB |
| Range | RNG- | RNG-GUEST |
| FQDN | FQDN- | FQDN-UPDATE |
| Service | TCP-/UDP- | TCP-8443 |
| Group | GRP- | GRP-SERVERS |
| Zone | ZN- | ZN-SERVER |

هر Object Comment (مالک، دلیل) داشته باشد.

#### ۶) Where Used و پاک‌سازی

GUI: روی Object → Where Used. Object بدون مصرف و بدون Comment کاندید حذف. تغییر Object مشترک روی همه‌ی Policyها اثر می‌گذارد؛ قبل از تغییر Where Used را ببینید.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Zone یا Interface | Zone برای چند پورت هم‌نقش |
| intrazone | deny |
| FQDN | فقط جایی که DNS مطمئن است |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

``` text
config firewall address
 edit "SRV-ERP"
  set subnet 10.20.0.10 255.255.255.255
  set comment "ERP owner Finance"
 next
end
```

#### مثال متوسط — Group و Service

``` text
config firewall addrgrp
 edit "GRP-SERVERS"
  set member "SRV-ERP" "SRV-DB"
 next
end
config firewall service custom
 edit "SVC-APP-8443"
  set tcp-portrange 8443
 next
end
```

#### مثال سخت — Schedule و Session

Schedule کاری 08 تا 18؛ Session بازِ ساعت 17:59 پس از 18:00 تا Timeout می‌ماند؛ برای قطع فوری Session را پاک کنید.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** NET-USERS=10.10.0.0/24 ساخته و در Policy 2 استفاده شد؛ بعداً شبکه به 10.11.0.0/24 تغییر کرد؛ فقط Object ویرایش شد و Policyها بدون تغییر ماندند.

**متوسط (Zone):** Interface port3 در Zone ZN-SERVER است ولی در Policy قابل انتخاب نیست. علت: عضو Zone؛ رفع: Zone را انتخاب کنید یا Interface را از Zone خارج کنید. درس: Policy با Zone.

**سخت (ممیزی Object):** ۲۰۰ Object: ۵۰ بدون Where-used؛ ۱۰ با نام یکسان تکراری. برنامه: Export، تأیید مالکان، حذف بلااستفاده‌ها پس از Backup، ادغام تکراری‌ها (Policyها را به Object اصلی بردارید)، اعمال استاندارد نام. معیار: صفر Object بی‌مالک، صفر تکراری.

### ۶) پیاده‌سازی از مسیر GUI

1. Policy & Objects → Addresses → Create New.
2. Services، Address Groups، Schedules.
3. Network → Interfaces → Create New → Zone.
4. روی Object → Where Used.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall address
 edit "NET-USERS"
  set subnet 10.10.0.0 255.255.255.0
  set comment "User VLAN; owner NOC"
 next
end
config system zone
 edit "ZN-SERVER"
  set interface "port3"
 next
end
```

### ۸) Verification (اثبات صحت)

- Where Used نشان می‌دهد Object استفاده شده.
- Policy از Zone استفاده می‌کند.
- نام‌ها مطابق استاندارد.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Interface در Policy نیست | عضو Zone | Zone را انتخاب کنید |
| Policy FQDN کار نمی‌کند | DNS | Resolver |
| تغییر Object اثر ناخواسته | Where Used | قبل از تغییر بررسی |

### ۱۰) نکات امنیتی

- Objectها را با Least Privilege.
- FQDN را کنترل کنید.

### ۱۱) جمع‌بندی مفهومی

- Object = یک نقطه‌ی تغییر.
- Zone برای خوانایی.
- نام‌گذاری و Comment.
- Where Used قبل از تغییر.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) مزیت Address Object چیست؟ *(پاسخ: 12-3-ت1)*

**ت2.** (ساده) intrazone deny چه می‌کند؟ *(پاسخ: 12-3-ت2)*

**ت3.** (متوسط) چرا Interface عضو Zone در Policy قابل انتخاب نیست؟ *(پاسخ: 12-3-ت3)*

**ت4.** (متوسط) خطر Object FQDN؟ *(پاسخ: 12-3-ت4)*

**ت5.** (سخت) ۲۰۰ Object را ممیزی کنید. *(پاسخ: 12-3-ت5)*

**ت6.** (سخت، طراحی) استاندارد نام‌گذاری شرکت. *(پاسخ: 12-3-ت6)*

**Q1.** Quick quiz (English): Why use zones instead of individual interfaces in policies? *(پاسخ: 12-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FQDN | Fully Qualified Domain Name | نام کامل دامنه |

- *Use a naming standard for every object.* ← برای هر Object استاندارد نام‌گذاری بگذارید.

### ۱۴) کارت Lab

**کارت Lab:** Objectها (اجرا نشده). **Evidence:** `02-design/fgt-objects.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall objects; Zones

<a id="l-12-4"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: استانداردسازی Objectها و ممیزی ۲۰۰ Object

**سناریو.** FortiGate پس از ۳ سال ۲۰۰ Address و ۴۰ Service دارد؛ بسیاری تکراری و بی‌مصرف‌اند.

**گام ۱ — Export و Where-used.** برای هر Object: Policy مصرف‌کننده را فهرست کنید.

**گام ۲ — دسته‌بندی.**

``` text
used & standard name      : keep
used & bad name           : rename (update policies automatically by object)
unused & no owner         : disable review -> delete after 30 days
duplicates (same subnet)  : merge into one object, repoint policies
```

**گام ۳ — الگوی نام.**

``` text
NET-USERS     (subnet)     SRV-DB      (host)
RNG-GUEST     (range)      FQDN-UPDATE (fqdn)
TCP-8443      (service)    GRP-SERVERS (group)
ZN-SERVER     (zone)
```

هر Object یک Comment با مالک و دلیل: `set comment "owner NOC; REQ-123"`.

**گام ۴ — Zone و intrazone.**

``` text
config system zone
 edit "ZN-SERVER"
  set intrazone deny
  set interface "port3" "VLAN20"
 next
end
```

با `intrazone deny` ترافیک بین اعضای Zone بدون Policy رد می‌شود (مستند Fortinet).

**گام ۵ — آزمون.** پس از Merge، Policy Lookup برای ۵ جریان مهم و مقایسه با قبل.

**اشتباهات رایج**
- Object FQDN برای سرویس‌هایی که DNS ندارد.
- تغییر Object مشترک بدون Where-used.
- Interface عضو Zone در Policy مستقیم.

**پرسش‌های مصاحبه**
1. *چرا Group؟* خوانایی و یک نقطه‌ی تغییر.
2. *ریسک FQDN؟* وابستگی به DNS و تغییر ناگهانی IP.
3. *Zone چه کاری می‌کند؟* Policy کوتاه‌تر و مدیریت ساده‌تر.

### تکمیل عمیق: Zone و Objectها — استاندارد نام‌گذاری

#### چرا؟

Objectهای شلوغ و بی‌نام ممیزی را غیرممکن می‌کنند. نام‌گذاری استاندارد زمان عیب‌یابی را نصف می‌کند.

#### قرارداد نام

``` text
Address : NET-USERS, SRV-ERP, HOST-DC1
Group   : GRP-SERVERS
Service : SVC-APP-8443
Zone    : ZN-DMZ
```

#### مثال ساده

``` text
config firewall address
 edit "NET-USERS"
  set subnet 10.10.0.0 255.255.255.0
  set comment "VLAN10 users, owner NOC"
 next
end
config firewall service custom
 edit "SVC-APP-8443"
  set tcp-portrange 8443
 next
end
```

#### مثال متوسط — Zone

``` text
config system zone
 edit "ZN-DMZ"
  set interface "port2" "port5"
  set intrazone deny
 next
end
```

`intrazone deny` ترافیک بین Interfaceهای همان Zone را پیش‌فرض می‌بندد.

#### مثال سخت — Schedule

``` text
config firewall schedule recurring
 edit "WORK-HOURS"
  set day monday tuesday wednesday thursday friday
  set start 08:00
  set end 18:00
 next
end
```

Session موجود پس از پایان Schedule تا انقضا می‌ماند.

#### Lab

ده Object با قرارداد نام بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Object تکراری | بی‌قرارداد | ادغام |
| intrazone باز | پیش‌فرض | deny |
| Schedule | Session | Clear |

#### پرسش‌ها با پاسخ

**۱. چرا comment؟** مالک و دلیل.
**۲. intrazone؟** داخل Zone.
**۳. Schedule و Session؟** قدیمی می‌ماند.

#### English Corner

- *Use consistent object naming and always record an owner in the comment.*
- Q: What does intrazone deny do?

## درس 12-4 — Static Route، Default Route، Policy Route، Distance/Priority و Failover

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۲، ۱۰-۴ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Static و Default Route را بسازد و Distance/Priority را تفاوت بگذارد.
2. ECMP و Failover دو ISP را با Link-monitor طراحی کند.
3. Policy Route را به‌کار ببرد و ترتیبش با جدول مسیر را بداند.
4. جدول مسیر را بخواند (all/details/database).
5. RPF، Blackhole و Summary را بشناسد.
6. خرابی‌های رایج مسیر را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Routing در فورتی‌گیت؟** Route تعیین می‌کند ترافیک از کدام Interface خارج شود. Policy درست با Route نادرست بی‌فایده است. دو عدد کلیدی: **Distance** (اعتبار؛ کمتر بهتر) و **Priority** (شکستن تساوی).

**انواع:** Static، Default، Policy Route (قبل از جدول عادی). برای Dual-ISP کنار Route باید **Link Monitor** باشد تا قطع واقعی را تشخیص دهد (فقط Up بودن لینک کافی نیست).

**جمع‌بندی اصلی درس:** Policy درست و ترافیک نمی‌رسد؟ اغلب Route است. در FortiGate Route قبل از Policy تصمیم می‌گیرد بسته از کدام Interface خارج شود؛ سپس Policy برای همان جفت (ورودی، خروجی) جست‌وجو می‌شود. پس Route اشتباه = Policy بی‌اثر.

### ۳) توضیح عمیق فنی

#### ۱) Static و Default

``` text
config router static
 edit 1
  set dst 0.0.0.0 0.0.0.0
  set gateway 198.51.100.1
  set device "port1"
  set distance 10
  set priority 1
  set comment "ISP-A primary"
 next
 edit 2
  set dst 0.0.0.0 0.0.0.0
  set gateway 203.0.113.1
  set device "port4"
  set distance 10
  set priority 10
  set comment "ISP-B backup"
 next
end
```

#### ۲) Distance و Priority

| ویژگی | معنی |
|---|---|
| Distance | اعتبار منبع؛ کمتر بهتر؛ بین Routeهای متفاوت |
| Priority | تعیین‌کننده بین Routeهای هم‌Distance به یک مقصد؛ کمتر ترجیح |

اگر Distance برابر و Priority متفاوت: مسیر با Priority کمتر Active (Primary) و دیگری آماده؛ اگر هر دو برابر: ECMP.

#### ۳) Failover با Link-monitor

``` text
config system link-monitor
 edit "ISP-A-MON"
  set srcintf "port1"
  set server "8.8.8.8"
  set gateway-ip 198.51.100.1
  set interval 1000
  set failtime 5
  set recoverytime 5
  set update-static-route enable
 next
end
```

بدون Link-monitor، اگر Gateway زنده ولی ISP قطع باشد، Route فعال می‌ماند و ترافیک گم می‌شود. `Unverified` برای ثبات پارامترها در 7.0.3.

#### ۴) Policy Route

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.20.0/255.255.255.0"
  set gateway 203.0.113.1
  set output-device "port4"
 next
end
```

Policy Route قبل از جدول مسیر؛ مسیر ترافیک مالی از ISP-B. اگر نیازی نیست، به‌جای آن SD-WAN (فصل ۱۶) بهتر است.

#### ۵) خواندن جدول

``` text
get router info routing-table all
get router info routing-table details 8.8.8.8
get router info routing-table database
diagnose firewall proute list
```

#### ۶) Blackhole و Summary

``` text
config router static
 edit 10
  set dst 10.0.0.0 255.0.0.0
  set blackhole enable
  set distance 254
 next
end
```

Summary داخلی با Blackhole و Distance بالا مانع Leak به Default می‌شود.

#### ۷) RPF

FortiGate مسیر معکوس Source را چک می‌کند؛ اگر Route برگشت از Interface دیگری باشد بسته Drop می‌شود (`reverse path check fail`).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Primary/Backup | Distance برابر، Priority متفاوت |
| Failover | Link-monitor به مقصد مستقل (نه فقط Gateway) |
| Summary | Blackhole |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

``` text
config router static
 edit 1
  set gateway 203.0.113.1
  set device "port1"
 next
end
```

#### مثال متوسط — دو ISP

Route 1 با distance 10 و Route 2 با 20 + Link Monitor. زمان تشخیص = interval × failtime = 1 s × 5 = 5 s.

#### مثال سخت — Failover ناقص

Link Monitor نیست و ISP-A بالادست مشکل دارد: Route فعال می‌ماند و ترافیک می‌ریزد. با افزودن Monitor، Route غیرفعال و مسیر دوم فعال می‌شود؛ Session قدیمی را پاک کنید.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Default به ISP-A. `get router info routing-table all` نشان می‌دهد `S* 0.0.0.0/0 [10/0] via 198.51.100.1, port1`.

**متوسط (Failover):** Primary ISP-A (priority 1) و Backup ISP-B (priority 10). مراحل: ۱) Link-monitor روی ISP-A. ۲) قطع ISP-A (نه فقط Gateway). ۳) Monitor ۵ بار شکست ⇒ Route ISP-A غیرفعال ⇒ ISP-B. ۴) آزمون traceroute. ۵) بازگشت: recoverytime. معیار: Failover < 10 s.

**سخت (Policy Route + RPF):** پس از افزودن Policy Route برای 10.10.20.0/24 به ISP-B، برخی Sessionها قطع می‌شوند. مراحل: ۱) Debug flow: `reverse path check fail`. ۲) پاسخ از ISP-B می‌آید ولی Route برگشت Default ISP-A است. ۳) رفع: Policy برای Interface خروجی ISP-B با NAT صحیح و Route برگشت یا `set asymroute`(فقط موقت؛ امنیت کم). ۴) آزمون. درس: Policy Route باید با NAT و مسیر برگشت هماهنگ باشد.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Static Routes → Create New.
2. Network → Policy Routes.
3. Network → SD-WAN (در 7.0) برای Failover پیشرفته.
4. Monitor → Routing Monitor.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config router static
 edit 1
  set gateway 198.51.100.1
  set device "port1"
  set distance 10
  set priority 1
 next
end
get router info routing-table all
get router info routing-table details 8.8.8.8
diagnose firewall proute list
```

### ۸) Verification (اثبات صحت)

- Route Active در جدول.
- traceroute از ISP درست.
- Failover با قطع ISP.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Failover کار نمی‌کند | Link-monitor | Monitor به مقصد خارجی |
| برخی Sessionها قطع | RPF | Route برگشت |
| مسیر عجیب | proute | Policy Route |
| Default غایب | database | Distance/Interface down |

### ۱۰) نکات امنیتی

- Blackhole برای Summary.
- Policy Route را مستند کنید.

### ۱۱) جمع‌بندی مفهومی

- Route قبل Policy.
- Distance/Priority.
- Link-monitor.
- RPF.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Distance چیست؟ *(پاسخ: 12-4-ت1)*

**ت2.** (ساده) Priority چه فرقی با Distance دارد؟ *(پاسخ: 12-4-ت2)*

**ت3.** (متوسط) چرا Link-monitor لازم است؟ *(پاسخ: 12-4-ت3)*

**ت4.** (متوسط) Policy Route قبل یا بعد از جدول مسیر؟ *(پاسخ: 12-4-ت4)*

**ت5.** (سخت) پس از Policy Route برخی Sessionها قطع می‌شوند؛ تحلیل. *(پاسخ: 12-4-ت5)*

**ت6.** (سخت، طراحی) دو ISP با Primary/Backup. *(پاسخ: 12-4-ت6)*

**Q1.** Quick quiz (English): Which attribute breaks the tie between static routes with equal distance? *(پاسخ: 12-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس |
| Blackhole | Blackhole route | مسیر دورریز |

- *A route decides the egress interface before the policy lookup.* ← Route قبل از Policy Interface خروجی را تعیین می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** Route و Failover (اجرا نشده). **Evidence:** `02-design/fgt-routing.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Static routing; Link monitor; Policy routes

<a id="l-12-5"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: طراحی Route و Failover دو ISP با اعداد و آزمون

**سناریو.** ISP-A (port1، GW 198.51.100.1) اصلی؛ ISP-B (port4، GW 203.0.113.1) پشتیبان. هدف: Failover زیر ۱۰ ثانیه.

**گام ۱ — Route.**

``` text
config router static
 edit 1
  set gateway 198.51.100.1
  set device "port1"
  set distance 10
  set priority 1
 next
 edit 2
  set gateway 203.0.113.1
  set device "port4"
  set distance 10
  set priority 10
 next
end
```

Distance برابر و Priority کمتر برای A ⇒ A فعال و B آماده (طبق مستند Fortinet).

**گام ۲ — Link-monitor.**

``` text
config system link-monitor
 edit "ISP-A"
  set srcintf "port1"
  set server "8.8.8.8"
  set gateway-ip 198.51.100.1
  set interval 1000
  set failtime 5
  set recoverytime 5
  set update-static-route enable
 next
end
```

زمان تشخیص ≈ failtime × interval = ۵ × ۱ ثانیه = ۵ ثانیه؛ با Convergence حدود ۶–۸ ثانیه.

**گام ۳ — آزمون.** `ping -t 8.8.8.8` از LAN با Interval ۲۰۰ میلی‌ثانیه؛ ISP-A را قطع؛ شمارش بسته‌های گمشده × ۰٫۲ ثانیه.

``` text
lost 38 packets x 0.2 s = 7.6 s  (target < 10 s: PASS)
```

**گام ۴ — Failback.** recoverytime ۵ ⇒ پس از ۵ موفقیت A برمی‌گردد؛ برای جلوگیری از Flap مقدار بزرگ‌تر یا Hold بگذارید.

**نکته‌ی مستند.** Link-monitor فقط خرابی کامل را می‌بیند؛ برای افت کیفیت (Latency/Jitter/Loss) از Performance SLA در SD-WAN استفاده کنید.

**اشتباهات رایج**
- Monitor روی Gateway فقط.
- Policy Route بدون NAT/Route برگشت ⇒ RPF.
- Distance متفاوت به‌جای Priority وقتی ECMP می‌خواهید.

**پرسش‌های مصاحبه**
1. *Distance و Priority؟* Distance بین منابع، Priority بین Routeهای هم‌Distance.
2. *RPF چیست؟* بررسی Route معکوس مبدأ از Interface ورودی.
3. *Blackhole Route؟* برای Summary و جلوگیری از حلقه.

### تکمیل عمیق: Static Route، Policy Route و Failover با Link Monitor

#### چرا؟

Routing تعیین می‌کند ترافیک از کدام Interface خارج شود؛ هر خطا در Route، Policy درست را بی‌اثر می‌کند.

#### مثال ساده — دو Default

``` text
config router static
 edit 1
  set gateway 203.0.113.1
  set device "port1"
  set distance 10
 next
 edit 2
  set gateway 198.51.100.1
  set device "port2"
  set distance 20
 next
end
```

Distance کمتر ترجیح دارد؛ در تساوی Priority.

#### مثال متوسط — Link Monitor

``` text
config system link-monitor
 edit "ISP1"
  set srcintf "port1"
  set server "8.8.8.8"
  set interval 1000
  set failtime 5
 next
end
```

``` text
Detection time = interval x failtime = 1000 ms x 5 = 5 s
Lost packets x ping interval: 38 x 0.2 s = 7.6 s outage
```

#### مثال سخت — Policy Route

PBR قبل از جدول Routing ارزیابی می‌شود؛ مطابقت ⇒ Gateway PBR؛ عدم مطابقت ⇒ Routing عادی.

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.1.0/24"
  set dst "0.0.0.0/0"
  set gateway 198.51.100.1
  set output-device "port2"
 next
end
```

#### Lab

Failover را اجرا و زمان قطع را اندازه بگیرید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Failover نمی‌شود | Monitor | افزودن |
| PBR اثر ندارد | ترتیب | بررسی |
| Session قدیم | Clear | فیلتر |

#### پرسش‌ها با پاسخ

**۱. Distance/Priority؟** انتخاب و شکست تساوی.
**۲. PBR کجا؟** قبل از Routing.
**۳. زمان تشخیص؟** interval×failtime.

#### English Corner

- *Policy routes are evaluated before the normal routing table.*
- Q: How is the failure detection time calculated?

## درس 12-5 — Admin، RBAC، MFA و سخت‌سازی مدیریت FortiGate

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۲، ۱۲-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Admin Profile (RBAC) با حداقل دسترسی بسازد.
2. Trusted host، Timeout، Lockout و TLS را تنظیم کند.
3. MFA (FortiToken/Email) و حساب Break-glass را طراحی کند.
4. Admin پیش‌فرض و Local-in/Management را محافظت کند.
5. Audit ورود/تغییر را بخواند و Alert بسازد.
6. چک‌لیست سخت‌سازی را اجرا و مستند کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا RBAC و MFA؟** اگر همه‌ی ادمین‌ها Super Admin باشند، خطای هر کدام خطای کل است و در حادثه نمی‌دانید چه کسی چه کرد. RBAC (Role-Based Access Control) به هر نفر فقط نقش لازم را می‌دهد؛ MFA رمز لو رفته را بی‌اثر می‌کند.

**اصول:** Profile مجزا برای NOC (فقط خواندن) و مهندس؛ Trusted Host؛ MFA؛ حساب Break-glass (اضطراری) در Vault؛ Log هر ورود و تغییر.

**جمع‌بندی اصلی درس:** اگر همه‌ی مدیران Super-admin باشند، یک رمز لورفته یعنی تسلط کامل: پاک‌کردن Policy، دریافت Config و حتی VPN backdoor. RBAC هر نفر را به اندازه‌ی کارش محدود می‌کند؛ MFA و Trusted host لایه‌ی بعدی‌اند.

### ۳) توضیح عمیق فنی

#### ۱) Admin Profile

``` text
config system accprofile
 edit "NOC-READONLY"
  set secfabgrp read
  set ftviewgrp read
  set authgrp read
  set sysgrp read
  set netgrp read
  set loggrp read
  set fwgrp read
  set vpngrp read
  set utmgrp read
 next
 edit "NET-ENGINEER"
  set sysgrp read
  set netgrp read-write
  set fwgrp read-write
  set loggrp read
 next
end
```

#### ۲) Admin و Trusted host

``` text
config system admin
 edit "noc01"
  set accprofile "NOC-READONLY"
  set trusthost1 10.99.0.0 255.255.255.0
  set password <STRONG-PASSWORD>
  set two-factor fortitoken
 next
end
```

رمز واقعی هرگز در ریپو/اسناد نمی‌آید.

#### ۳) سخت‌سازی سراسری

``` text
config system global
 set admintimeout 10
 set admin-lockout-threshold 3
 set admin-lockout-duration 300
 set admin-https-ssl-versions tlsv1-2 tlsv1-3
 set admin-ssh-v1 disable
 set strong-crypto enable
 set admin-port 8443
 set admin-sport 8443
end
```

(پورت‌های مدیریت سفارشی کمک متوسط؛ Obscurity.) `Unverified`.

#### ۴) Password Policy

``` text
config system password-policy
 set status enable
 set minimum-length 14
 set min-lower-case-letter 1
 set min-upper-case-letter 1
 set min-number 1
 set min-non-alphanumeric 1
 set expire-status enable
 set expire-day 90
end
```

#### ۵) Break-glass

یک حساب اضطراری با رمز طولانی در گاوصندوق، فقط برای زمان قطع SSO/MFA؛ هر استفاده Alert و Rotate.

#### ۶) Audit

``` text
execute log filter category 1   ! event log
execute log filter field logdesc "Admin login successful"
execute log display
```

در FortiAnalyzer: Alert روی «Admin login failed» >5 در ۵ دقیقه و «Configuration changed».

#### ۷) چک‌لیست

1. admin پیش‌فرض: تغییر نام/غیرفعال. 2. MFA همه. 3. Trusted host. 4. فقط TLS 1.2+. 5. Telnet/HTTP off. 6. Timeout/Lockout. 7. Backup رمزگذاری. 8. Log به خارج.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| سه سطح دسترسی | Super، Engineer، ReadOnly |
| MFA | FortiToken/OTP برای همه |
| Break-glass | گاوصندوق و Alert |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — Profile

``` text
config system accprofile
 edit "noc-ro"
  set netgrp read
  set fwgrp read
  set loggrp read
 next
end
```

#### مثال متوسط — ادمین با MFA

ادمین `noc1` با Profile بالا و Trusted Host؛ MFA با FortiToken. آزمون: ورود بدون OTP رد می‌شود.

#### مثال سخت — ممیزی

گزارش هفتگی: ورود/تغییر از Log، تطبیق با CHG؛ تغییر بدون CHG فوری بررسی شود.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Admin فقط‌خواندنی noc01 با Trusted host 10.99.0.0/24؛ ورود از شبکه‌ی دیگر رد می‌شود.

**متوسط (Brute-force):** لاگ: ۲۰ ورود ناموفق از یک IP. مراحل: ۱) Lockout 3/300 فعال. ۲) IP در Local-in policy مسدود. ۳) Trusted host. ۴) Alert. نتیجه: تلاش‌ها پس از ۳ بار قفل می‌شود.

**سخت (سه سطح + Break-glass):** طراحی: ۱) Super-admin ۲ نفر با MFA. ۲) Network engineer: fwgrp/netgrp رایت. ۳) NOC: فقط‌خواندنی. ۴) Break-glass در گاوصندوق. ۵) Alert روی ورود Break-glass و تغییر Config. ۶) آزمون: ورود با NOC و تلاش تغییر Policy ⇒ رد. معیار: هیچ حساب مشترک، هیچ رمز در ریپو.

### ۶) پیاده‌سازی از مسیر GUI

1. System → Admin Profiles → Create New.
2. System → Administrators → Create New (Trusted hosts، Two-factor).
3. System → Settings: Idle timeout، HTTPS ports.
4. Security Fabric/Log برای Alert.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system global
 set admintimeout 10
 set admin-lockout-threshold 3
 set admin-lockout-duration 300
end
show system admin
```

### ۸) Verification (اثبات صحت)

- ورود با Trusted host.
- Lockout پس از ۳ تلاش.
- NOC تغییر Policy نمی‌تواند.
- Alert ارسال می‌شود.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Admin وارد نمی‌شود | Trusthost | آدرس مدیر |
| MFA قفل | FortiToken | Break-glass |
| Lockout زیاد | دور زدن | Trusted host/Local-in |

### ۱۰) نکات امنیتی

- MFA همه.
- Break-glass.
- رمز در ریپو ممنوع.

### ۱۱) جمع‌بندی مفهومی

- RBAC.
- Trusted host.
- MFA.
- Audit/Alert.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) RBAC چیست؟ *(پاسخ: 12-5-ت1)*

**ت2.** (ساده) Trusted host چه می‌کند؟ *(پاسخ: 12-5-ت2)*

**ت3.** (متوسط) Lockout چه فایده‌ای دارد؟ *(پاسخ: 12-5-ت3)*

**ت4.** (متوسط) چرا Break-glass؟ *(پاسخ: 12-5-ت4)*

**ت5.** (سخت) Brute-force از یک IP؛ پاسخ. *(پاسخ: 12-5-ت5)*

**ت6.** (سخت، طراحی) سه سطح دسترسی و چک‌لیست. *(پاسخ: 12-5-ت6)*

**Q1.** Quick quiz (English): What does a trusted host setting restrict? *(پاسخ: 12-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MFA | Multi-Factor Authentication | احراز چندعاملی |
| RBAC | Role-Based Access Control | کنترل دسترسی نقش‌محور |

- *Apply least privilege to administrator accounts.* ← به حساب‌های Admin حداقل دسترسی بدهید.

### ۱۴) کارت Lab

**کارت Lab:** سخت‌سازی Admin (اجرا نشده). **Evidence:** `03-ops/fgt-admin-standard.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Administrators; Hardening
- FortiOS 7.0 Hardening guide

<a id="l-12-6"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: طراحی سه‌سطحی دسترسی و آزمون Lockout

**سناریو.** تیم ۴ نفره: دو مهندس، یک NOC، یک ممیز. ورودهای ناموفق از یک IP خارجی گزارش شده.

**گام ۱ — Profile.**

``` text
config system accprofile
 edit "NET-ENG"
  set netgrp read-write
  set fwgrp read-write
  set loggrp read
  set sysgrp read
 next
 edit "NOC-RO"
  set netgrp read
  set fwgrp read
  set loggrp read
 next
end
```

**گام ۲ — Admin با Trusted host و MFA.**

``` text
config system admin
 edit "noc01"
  set accprofile "NOC-RO"
  set trusthost1 10.99.0.0 255.255.255.0
  set two-factor fortitoken
 next
end
```

**گام ۳ — Hardening.**

``` text
config system global
 set admintimeout 10
 set admin-lockout-threshold 3
 set admin-lockout-duration 300
 set admin-https-ssl-versions tlsv1-2 tlsv1-3
end
```

مستند: threshold ۱ تا ۱۰ (پیش‌فرض ۳)، duration پیش‌فرض ۶۰ ثانیه.

**گام ۴ — آزمون.** سه ورود ناموفق از Host مجاز ⇒ قفل ۳۰۰ ثانیه؛ ورود از IP غیرمجاز با رمز درست ⇒ رد (Trusted host)؛ NOC تلاش تغییر Policy ⇒ رد.

**گام ۵ — Break-glass.** حساب اضطراری با رمز طولانی در گاوصندوق، Alert روی ورود و Rotate پس از استفاده.

**اشتباهات رایج**
- Super-admin برای همه.
- Trusted host خالی.
- رمز در ریپو/سند.

**پرسش‌های مصاحبه**
1. *Local-in در برابر Trusted host؟* Local-in ترافیک به فایروال را فیلتر می‌کند؛ Trusted host ورود Admin را؛ هر دو را با هم استفاده کنید.
2. *MFA چرا؟* رمز لورفته بدون عامل دوم کافی نیست.
3. *Alert چه باشد؟* Admin login failed و Config changed.

### تکمیل عمیق: Admin، RBAC و MFA

#### چرا؟

ادمین کامل بودن همه، یعنی خطای هر کس خطای کل است. RBAC دسترسی را به نقش می‌دهد.

#### مثال ساده — Profile

``` text
config system accprofile
 edit "noc-ro"
  set netgrp read
  set fwgrp read
  set loggrp read
 next
end
config system admin
 edit "noc1"
  set accprofile "noc-ro"
  set trusthost1 10.50.0.0 255.255.255.0
 next
end
```

#### مثال متوسط — MFA

FortiToken یا RADIUS+MFA برای ادمین (`two-factor fortitoken`). حساب Break-glass (اضطراری) جدا و در Vault.

#### مثال سخت — ممیزی

``` text
config log eventfilter
 set system enable
end
```

هر ورود/تغییر ادمین ثبت شود؛ هفتگی با CHGها تطبیق دهید.

#### Lab

سه نقش بسازید و رفتار را آزمون کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| همه super_admin | سهل‌انگاری | Profile |
| قفل شدن | MFA زمان | NTP |
| تغییر بی‌ردپا | Log غیرفعال | فعال |

#### پرسش‌ها با پاسخ

**۱. RBAC؟** نقش‌محور.
**۲. Break-glass؟** حساب اضطراری.
**۳. چرا Trusted Host؟** مبدأ.

#### English Corner

- *Keep a sealed break-glass account for emergencies.*
- Q: Why enable MFA for administrators?

## درس 12-6 — Backup/Restore، Firmware Upgrade، Rollback و Lifecycle

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۱، ۱۲-۵ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Backup کامل (Config، Certificates، License) را بگیرد و ایمن نگه دارد.
2. Restore را در Lab اجرا و صحت آن را بررسی کند.
3. Upgrade Path را از Fortinet تعیین و Window/Rollback را برنامه‌ریزی کند.
4. قبل/بعد Upgrade چک‌لیست اجرا کند.
5. Lifecycle (EoS/EoL، Release Notes) را ردیابی کند.
6. برنامه‌ی تغییر (CHG) و Runbook بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Backup و ارتقا؟** بدون Backup تست‌شده، یک خطا ساعت‌ها قطعی می‌سازد. ارتقا مثل تعویض موتور در پرواز است: باید مسیر ارتقا، Backup، Rollback و آزمون آماده باشد.

**اصول:** Release Notes و Upgrade Path رسمی؛ Backup + Hash؛ Lab اول؛ پنجره‌ی تغییر؛ معیار Rollback از قبل.

**جمع‌بندی اصلی درس:** Upgrade بدون Backup مثل جراحی بدون رضایت‌نامه است. یک Upgrade ساده می‌تواند Config را خراب کند یا Boot loop بسازد. تفاوت مهندس حرفه‌ای با تازه‌کار: Backup، Path، Rollback و آزمون پس از تغییر.

### ۳) توضیح عمیق فنی

#### ۱) Backup

``` text
execute backup config tftp fgt-edge-01_2026-11-26.conf 10.99.0.5
execute backup config sftp fgt-edge-01.conf 10.99.0.5 backupuser
```

GUI: User/Admin → Configuration → Backup (انتخاب Encrypt). Backup حاوی رمزها و کلیدهاست: رمزگذاری، دسترسی محدود، عدم نگهداری در ریپو عمومی.

#### ۲) Restore

``` text
execute restore config tftp fgt-edge-01_2026-11-26.conf 10.99.0.5
```

دستگاه Reboot می‌کند؛ ابتدا در Lab تمرین کنید. پس از Restore: نسخه، Interface، Route و Policyها را مقایسه کنید.

#### ۳) Upgrade Path

از Fortinet Upgrade Path Tool استفاده کنید: ممکن است نسخه‌ی میانی لازم باشد (مثلاً 6.4.x → 7.0.x). Release Notes نسخه‌ی مقصد برای Known Issues، تغییرات رفتاری و حداقل RAM.

#### ۴) چک‌لیست قبل

``` text
1 Backup (config) + export of certificates
2 Release Notes read, Known Issues vs our features
3 Maintenance window + rollback plan + owner
4 Current: get system status ; diagnose sys ha status
5 Download image, verify checksum
```

#### ۵) اجرای Upgrade

GUI: System → Firmware → File Upload (یا FortiGuard). یا CLI: `execute restore image tftp image.out 10.99.0.5`. HA: Cluster ابتدا Upgrade Secondary سپس Primary با Failover (فصل HA).

#### ۶) چک‌لیست بعد

``` text
get system status
get router info routing-table all
diagnose sys session stat
execute ping 8.8.8.8
verify VPN, policies hit counts, logs
```

#### ۷) Rollback

اگر شکست: Boot از Partition قبلی (FortiGate دو Image دارد) یا Restore Config+Firmware قبلی از Backup. زمان تصمیم Rollback را پیش از شروع تعیین کنید (مثلاً بعد ۳۰ دقیقه).

#### ۸) Lifecycle

تاریخ EoS/EoL مدل و FortiOS، آسیب‌پذیری‌های PSIRT، برنامه‌ی جایگزینی؛ ثبت در Inventory.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Backup | قبل هر تغییر و روزانه خودکار |
| Window | زمان کم‌ترافیک + Rollback |
| HA | ابتدا Secondary |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

``` text
execute backup config tftp cfg.conf 10.50.0.30
sha256sum cfg.conf
```

#### مثال متوسط — برنامه‌ی ارتقا

T-7 Lab، T-1 Backup، T0 ارتقا، T+30m آزمون پس از ارتقا (Policy/Route/Tunnel/HA).

#### مثال سخت — Rollback

اگر پس از ارتقا SSL-VPN باز نشد و ظرف ۳۰ دقیقه رفع نشد، Rollback به Image قبلی و Config قبلی؛ ثبت علت و بررسی Release Notes.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Backup با TFTP؛ فایل ۳۰ KB؛ Hash ثبت؛ نگهداری در مخزن رمزگذاری‌شده.

**متوسط (Upgrade Path):** میخواهیم 6.4.8 → 7.0.3. مراحل: ۱) Path Tool: ممکن است 6.4.8 → 7.0.x مستقیم باشد (باید از ابزار تأیید شود؛ ما ادعایی نمی‌کنیم). ۲) Backup. ۳) Upgrade. ۴) چک‌لیست بعد. معیار: همه‌ی Policyها و Routeها حفظ.

**سخت (Rollback):** Upgrade با Boot loop. مراحل: ۱) کنسول. ۲) Boot از Partition قبلی (منوی بوت). ۳) نسخه‌ی قبلی بالا می‌آید. ۴) Restore Config. ۵) گزارش: علت (Known Issue)، تصمیم: عدم Upgrade تا رفع. درس: Window شامل زمان Rollback.

### ۶) پیاده‌سازی از مسیر GUI

1. Dashboard → Admin → Configuration → Backup.
2. System → Firmware.
3. System → Config → Revisions.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute backup config tftp fgt-edge-01.conf 10.99.0.5
get system status
diagnose sys session stat
```

### ۸) Verification (اثبات صحت)

- فایل Backup + Hash.
- نسخه جدید.
- Policy/Route سالم.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Boot loop | کنسول | Partition قبلی |
| Restore ناقص | نسخه/License | Config را مقایسه |
| Upgrade مجاز نیست | Path | نسخه‌ی میانی |

### ۱۰) نکات امنیتی

- Backup رمزگذاری و ایمن.
- Checksum Firmware.

### ۱۱) جمع‌بندی مفهومی

- Backup اول.
- Path.
- Rollback.
- Lifecycle.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Backup رمزگذاری شود؟ *(پاسخ: 12-6-ت1)*

**ت2.** (ساده) Upgrade Path Tool چیست؟ *(پاسخ: 12-6-ت2)*

**ت3.** (متوسط) قبل Upgrade چه بررسی می‌کنید؟ *(پاسخ: 12-6-ت3)*

**ت4.** (متوسط) چرا HA ابتدا Secondary؟ *(پاسخ: 12-6-ت4)*

**ت5.** (سخت) Boot loop بعد Upgrade؛ پاسخ. *(پاسخ: 12-6-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی CHG برای Upgrade. *(پاسخ: 12-6-ت6)*

**Q1.** Quick quiz (English): Why must you plan a rollback before upgrading firmware? *(پاسخ: 12-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| EoS | End of Support | پایان پشتیبانی |
| CHG | Change request | درخواست تغییر |

- *Back up before every change.* ← قبل از هر تغییر Backup بگیرید.

### ۱۴) کارت Lab

**کارت Lab:** Backup/Restore (اجرا نشده). **Evidence:** `03-ops/fgt-backup-log.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Backup and restore; Firmware
- Fortinet Upgrade Path Tool

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: برنامه‌ی Upgrade با Backup، Path و Rollback — نمونه‌ی ساعت‌به‌ساعت

**سناریو.** ارتقا از 6.4.x به 7.0.3 روی FortiGate مرکزی (HA دوتایی).

**گام ۱ — پیش‌نیاز (T-3d).**
1. Upgrade Path Tool: نسخه‌های میانی لازم؟
2. Release Notes: Known Issues و تغییرات رفتاری (SSL-VPN، SD-WAN، لاگ).
3. Backup رمزگذاری‌شده + Hash.
4. Lab آزمون با همان Config (در صورت امکان).

**گام ۲ — Window (T0).**

| ساعت | کار | Checkpoint |
|---|---|---|
| 22:00 | Backup هر دو + تأیید checksum | C1 |
| 22:10 | Upgrade Secondary | C2: in-sync |
| 22:30 | Failover به Secondary | C3: بدون قطع طولانی |
| 22:35 | Upgrade Primary قبلی | C4 |
| 22:55 | Post-check | C5 |

**گام ۳ — Post-check.**

``` text
get system status
get system ha status
diagnose sys ha checksum cluster
get router info routing-table all
diagnose sys session stat
```

**Rollback:** اگر C3 یا C4 تا 22:40 شکست خورد، Boot از Partition قبلی (FortiGate دو Image نگه می‌دارد) یا Restore Config+Firmware.

**گام ۴ — گزارش.** مدت واقعی، انحراف، درس. مثال: Sync ۶ دقیقه کند بود ⇒ در برنامه‌ی بعد منتظر in-sync بمانید.

**اشتباهات رایج**
- Upgrade مستقیم بدون Path.
- Backup بدون رمزگذاری.
- نداشتن زمان تصمیم Rollback.

**پرسش‌های مصاحبه**
1. *چرا Secondary اول؟* با Failover سرویس حفظ می‌شود.
2. *EoS/EoL؟* پایان پشتیبانی؛ برنامه‌ی جایگزینی.
3. *چه چیزی بعد از Upgrade مقایسه می‌کنید؟* Session، Route، IPsec، Policy hit، Log.

### تکمیل عمیق: Backup/Restore، ارتقا و Lifecycle

#### چرا؟

بدون Backup تست‌شده و مسیر ارتقا درست، یک اشتباه ساده می‌تواند ساعت‌ها قطعی بسازد.

#### مثال ساده — Backup

``` text
execute backup config tftp cfg-2026-11-27.conf 10.50.0.30
sha256sum cfg-2026-11-27.conf
```

#### مثال متوسط — ارتقا

1. Release Notes و Upgrade Path.
2. Backup + Image قبلی.
3. Lab.
4. Window.
5. Verify.
6. Rollback.

``` text
Pre : get system status ; backup
Post: get system status ; policy/route counts ; tunnels
```

#### مثال سخت — Rollback

``` text
execute restore image tftp old.out 10.50.0.30
execute restore config tftp cfg-before.conf 10.50.0.30
```

معیار Rollback از قبل: «اگر ۳۰ دقیقه سرویس حیاتی برنگشت».

#### Lifecycle

EoS/EoL نسخه‌ها را از سایت رسمی پیگیری کنید؛ ارتقای برنامه‌ریزی‌شده.

#### Lab

Backup و Restore را در Lab اجرا کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Restore شکست | نسخه | همان |
| بوت نمی‌شود | Image | Console |
| Config ناقص | مسیر ارتقا | Backup |

#### پرسش‌ها با پاسخ

**۱. چرا Hash؟** سلامت.
**۲. چرا Lab اول؟** کشف مشکل.
**۳. EoS؟** پایان پشتیبانی.

#### English Corner

- *Define rollback criteria before the upgrade window.*
- Q: Why verify the backup file with a hash?

## درس 12-8 — Transit، Local-in و Local-out: سه نوع ترافیک و سه مسیر پردازش

**فصل ۱۲ · درس افزوده (پس از ۱۲-۶) · پیش‌نیاز: ۱۲-۰، ۵-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3، `Unverified` روی Image):** دسته‌بندی مفهومی است؛ نام دقیق دستورها با CLI Reference 7.0 تطبیق داده شود. Lab «اجرا نشده».

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. سه نوع ترافیک **Transit (Forward)**، **Local-in** و **Local-out** را تعریف و برای هرکدام مثال بزند.
2. بگوید هر نوع با کدام ساز و کار کنترل می‌شود (Firewall Policy، `allowaccess`، Local-in Policy، تنظیمات Source-IP سرویس).
3. توضیح دهد چرا «Policy برای ping به فایروال لازم نیست ولی `allowaccess ping` لازم است».
4. مدیریت فایروال را ایمن کند (Trusted Host، Admin Port، Local-in Policy).
5. علت رایج‌ترین خطاها را بیابد: «از فایروال ping می‌زنم ولی کاربران نه»، «GUI از WAN باز نمی‌شود/خیلی باز است».

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا سه نوع ترافیک؟** درس ۱۱-۳ نظری بود؛ اینجا در FortiGate عملی می‌شود: Transit، Local-in، Local-out و کنترل هرکدام.

- Transit: Firewall Policy.
- Local-in: `allowaccess` و `local-in-policy`.
- Local-out: Source Interface و Route سرویس‌های خود فایروال (NTP، DNS، Syslog، FortiGuard).

**جمع‌بندی اصلی درس:** Packet Flow (۱۲-۰)، Punt و Management Plane (۵-۰)، مدل تهدید (۱۱-۰).

### ۳) مفهوم پایه

بسته‌ها سه سرنوشت دارند:

| نوع | مبدأ → مقصد | مثال |
|---|---|---|
| **Transit / Forward** | از FortiGate عبور می‌کند | کاربر → اینترنت |
| **Local-in** | مقصد = خود FortiGate | SSH/HTTPS به فایروال، OSPF/BGP، IKE، ping به فایروال |
| **Local-out** | مبدأ = خود FortiGate | ping از CLI فایروال، DNS/NTP/FortiGuard، Syslog، ارسال Log، RADIUS، اتصال IPsec خروجی |

برای هر نوع **ساز و کار کنترل متفاوت** است. اشتباه رایج: فکر می‌کنیم «Firewall Policy همه‌چیز را کنترل می‌کند». ولی Policy فقط **Transit** را کنترل می‌کند.

### ۴) توضیح عمیق فنی

#### ۴-۱) Transit

مسیر کامل درس ۱۲-۰: Session، DNAT، Route، Policy، Profile، SNAT. کنترل: `config firewall policy` (و Central NAT/VIP).

#### ۴-۲) Local-in

ترافیک به سرویس‌های خود فایروال می‌رسد: مدیریت (HTTPS/SSH/Telnet/SNMP)، Ping، پروتکل‌های مسیریابی، IKE/IPsec، DHCP Server، DNS Server، FortiGuard Update (پاسخ‌ها) و ...

کنترل‌ها:

1. **`allowaccess` روی Interface:** مشخص می‌کند کدام سرویس‌ها روی آن Interface پاسخ می‌دهند (`ping https ssh snmp fgfm http telnet ...`).
2. **Local-in Policy** (`config firewall local-in-policy`): قوانین دقیق‌تر روی ترافیک ورودی به فایروال (مثلاً فقط مدیریت از یک Subnet).
3. **Trusted Host** برای هر Admin: فقط از IPهای مشخص.
4. **Admin Port/Redirect:** تغییر پورت و اجبار HTTPS.

نتیجه: مدیریت فایروال از اینترنت = ریسک بحرانی (و تاریخچه‌ی CVE روی GUI/SSL VPN). `allowaccess` را روی WAN حداقل کنید.

#### ۴-۳) Local-out

فایروال هم مثل یک Host ترافیک می‌سازد. نکات:

- مسیر خروجی با **Routing Table** (و گاهی تنظیمات **Source-IP**) تعیین می‌شود، نه Firewall Policy.
- Source IP پیش‌فرض = IP Interface خروجی؛ برای سرویس‌هایی مثل Syslog، SNMP Trap، RADIUS و NTP می‌توان `source-ip` تعیین کرد (در بخش تنظیم آن سرویس؛ نام دقیق پارامتر در 7.0 تطبیق شود).
- اگر Route خروجی از VPN بگذرد، ترافیک Local-out باید در Phase 2 Selector هم بگنجد (مشکل رایج: ping از CLI فایروال به شبکه‌ی آن‌طرف VPN کار نمی‌کند چون Source IP ناسازگار است).
- در 7.0 ترافیک Local-out معمولاً **Firewall Policy** نمی‌خواهد ولی Log آن در بخش Local Traffic Log است.

#### ۴-۴) خلاصه‌ی کنترل‌ها

| نوع | کنترل اصلی | Log |
|---|---|---|
| Transit | Firewall Policy | Forward Traffic |
| Local-in | `allowaccess` + Local-in Policy + Trusted Host | Local Traffic |
| Local-out | Routing + `source-ip` سرویس | Local Traffic |

### ۵) مثال حل‌شده

#### مثال ساده

ping به IP فایروال: Local-in؛ ping به سرور: Transit.

#### مثال متوسط — Local-in Policy

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

#### مثال سخت — Update نمی‌رسد

FortiGuard Update شکست می‌خورد: Local-out. بررسی Route/DNS فایروال، `set source-ip` و Policy ترافیک خروجی؛ `execute ping update.fortiguard.net`.

#### مثال‌های اصلی درس (مرور)

**مسئله:** از CLI فایروال `execute ping 192.168.20.1` (مقصد پشت VPN) جواب نمی‌گیرد ولی کاربران LAN به آن می‌رسند.

``` text
FGT # execute ping-options source 192.168.10.1
FGT # execute ping 192.168.20.1
FGT # get router info routing-table details 192.168.20.1
```

**تحلیل:** Ping از CLI = Local-out؛ Source پیش‌فرض IP Interface خروجی (Tunnel) است که در Selector نیست. با تعیین Source = IP داخلی که در Selector هست، ping موفق می‌شود. نتیجه: شبکه خراب نیست؛ آزمون با Source غلط انجام شده بود.

**مثال متوسط:** GUI فایروال از WAN باز می‌شود. علت: `allowaccess https` روی WAN.

``` text
config system interface
    edit "port1"
        set allowaccess ping
    next
end
config system admin
    edit "admin-lab"
        set trusthost1 192.168.90.0 255.255.255.0
    next
end
```

**مثال سخت:** فقط مدیریت از Subnet مدیریت (192.168.90.0/24) روی HTTPS و SSH مجاز و بقیه رد شود، با Local-in Policy:

``` text
config firewall address
    edit "MGMT-NET"
        set subnet 192.168.90.0 255.255.255.0
    next
end
config firewall local-in-policy
    edit 1
        set intf "port1"
        set srcaddr "MGMT-NET"
        set dstaddr "all"
        set action accept
        set service "HTTPS" "SSH"
        set schedule "always"
    next
    edit 2
        set intf "port1"
        set srcaddr "all"
        set dstaddr "all"
        set action deny
        set service "ALL"
        set schedule "always"
    next
end
```

(نام فیلدها در 7.0 با CLI Reference تطبیق داده شود؛ `Unverified`.)

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| مدیریت از کجا؟ | فقط شبکه‌ی مدیریت/Interface اختصاصی؛ نه WAN |
| چند لایه؟ | `allowaccess` حداقل + Trusted Host + Local-in Policy + MFA |
| Ping به فایروال | روی WAN غیرفعال یا محدود |
| سرویس‌های Local-out | Source-IP مشخص، Route صریح |

### ۷) پیاده‌سازی: GUI و CLI

**GUI:**

1. Network → Interfaces → انتخاب Interface → «Administrative Access»: فقط سرویس‌های لازم.
2. System → Administrators → ویرایش Admin → «Restrict login to trusted hosts».
3. Policy & Objects → Local-in Policy (اگر فعال نیست در Feature Visibility روشن شود).
4. Log & Report → Local Traffic: بررسی ورودی/خروجی.

**CLI:**

``` text
show system interface port1
show firewall local-in-policy
show system admin
diagnose sniffer packet port1 "host 192.168.90.5 and (port 443 or port 22)" 4 20 l
execute ping-options source <ip>
```

### ۸) Troubleshooting

| علامت | علت محتمل | شاهد |
|---|---|---|
| GUI باز نمی‌شود | `allowaccess` نیست/Trusted Host/Local-in deny | Sniffer، Local Traffic Log |
| Ping به فایروال ندارد | `allowaccess ping` غایب | Sniffer: Request بدون Reply |
| ping از CLI به VPN شکست | Source/Selector | `execute ping-options source` |
| NTP/DNS فایروال کار نمی‌کند | Route/Source IP | Sniffer روی Interface خروجی |

### ۹) نکات امنیتی

- مدیریت از اینترنت ممنوع مگر با VPN/Trusted Host/MFA.
- رمز پیش‌فرض و Admin عمومی را تغییر دهید.
- Telnet/HTTP را غیرفعال کنید.
- نسخه‌های 7.0.x دارای CVE روی GUI/SSL VPN هستند؛ در Lab ایزوله کار کنید.

### ۱۰) جمع‌بندی مفهومی

- Policy فقط Transit را کنترل می‌کند.
- Local-in = `allowaccess` + Local-in Policy + Trusted Host.
- Local-out = Routing + Source-IP.
- آزمون از CLI فایروال همیشه شبیه ترافیک کاربران نیست.
- مدیریت را از WAN ببندید.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) سه نوع ترافیک را نام ببرید. *(پاسخ: 12-8-ت1)*

**ت2.** (ساده) کدام تنظیم Ping به فایروال را روی یک Interface مجاز می‌کند؟ *(پاسخ: 12-8-ت2)*

**ت3.** (متوسط) چرا Firewall Policy برای SSH به خود فایروال کافی/لازم نیست؟ *(پاسخ: 12-8-ت3)*

**ت4.** (متوسط) ping از CLI به شبکه‌ی پشت VPN شکست می‌خورد؛ چرا؟ *(پاسخ: 12-8-ت4)*

**ت5.** (سخت) مدیریت را فقط از 192.168.90.0/24 مجاز کنید؛ سه لایه‌ی کنترل را بنویسید. *(پاسخ: 12-8-ت5)*

**ت6.** (سخت، طراحی) فایروال Syslog را به سرور 192.168.90.20 می‌فرستد ولی Log نمی‌رسد؛ مراحل بررسی Local-out را مرتب کنید. *(پاسخ: 12-8-ت6)*

**م1.** Trusted Host چیست؟ *(پاسخ: 12-8-م1)*

**Q1.** Quick quiz (English): Which mechanism controls traffic destined to the firewall itself? *(پاسخ: 12-8-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Local-in | Local-in traffic | ترافیک ورودی به خود فایروال |
| Local-out | Local-out traffic | ترافیک خروجی از خود فایروال |
| Transit | Transit traffic | ترافیک عبوری |
| allowaccess | Administrative access | سرویس‌های مجاز روی Interface |
| Trusted host | Trusted host | IP مجاز برای ورود Admin |

- *Firewall policies do not control traffic destined to the firewall itself.* ← Policyها ترافیک مقصد خود فایروال را کنترل نمی‌کنند.
- *Restrict management access to a dedicated network.* ← دسترسی مدیریتی را به شبکه‌ی اختصاصی محدود کنید.

### ۱۳) منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Interface settings (Administrative access)، Local-in policy؛ CLI Reference `config firewall local-in-policy`، `config system interface`.
- Fortinet: «Hardening your FortiOS» (مقاله‌ی رسمی؛ نسخه‌ی 7.0 را بررسی کنید).

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: Transit، Local-in و Local-out

#### چرا؟

سه نوع ترافیک سه مسیر دارند؛ بسیاری تصور می‌کنند Policy عادی ترافیک به فایروال را هم کنترل می‌کند، در حالی که نمی‌کند.

#### سه نوع

| نوع | مبدأ → مقصد | کنترل |
|---|---|---|
| Transit | از میان فایروال | Firewall Policy |
| Local-in | به خود فایروال | Local-in Policy / allowaccess |
| Local-out | از خود فایروال | تنظیمات سرویس/Route |

#### مثال ساده

ping از Users به IP خود فایروال: Local-in (allowaccess). ping از Users به سرور: Transit (Policy).

#### مثال متوسط — Local-in Policy

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

#### مثال سخت — Local-out

فایروال برای DNS/NTP/FortiGuard خروجی دارد؛ Source Interface و Route آنها را تنظیم کنید (`set source-ip`)؛ مشکل Log/Update اغلب از Route Local-out است.

#### Lab

سه نوع ترافیک را با Debug Flow مقایسه کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| ping به FW نه | allowaccess | افزودن |
| Update نمی‌رسد | Route Local-out | تنظیم |
| Policy بی‌اثر روی FW | Local-in | local-in-policy |

#### پرسش‌ها با پاسخ

**۱. Local-in چیست؟** ترافیک به خود FW.
**۲. Policy عادی آن را کنترل می‌کند؟** خیر.
**۳. Local-out؟** از خود FW.

#### English Corner

- *Local-in policies protect the firewall itself, not the networks behind it.*
- Q: Which policy type controls traffic destined to the firewall?

## درس 12-9 — Hardware Acceleration (NPU/SPU) و Session Offload: اثر بر عملکرد و عیب‌یابی

**فصل ۱۲ · درس افزوده (پس از ۱۲-۸) · پیش‌نیاز: ۱۲-۰، ۱۱-۷ · ≈ ۴ ساعت**

> **وضعیت:** مفهومی. FortiGate-VM در Lab ما سخت‌افزار NP ندارد؛ بنابراین رفتار Offload در Lab «اجرا نشده» است. دستورها `Unverified`.

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. توضیح دهد Hardware Acceleration چیست و چه مشکلی را حل می‌کند.
2. تفاوت پردازش **Software (CPU/Kernel)** و **Offload (NPU)** را برای یک Session بگوید.
3. بداند چه ترافیکی Offload می‌شود و چه چیزی مانع آن است (Profile، NAT خاص، ...).
4. بفهمد چرا Debug Flow و Sniffer روی ترافیک Offloadشده کامل نیست و چه کند.
5. اثر Offload را بر Performance، Log و Troubleshooting ارزیابی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا NPU و Offload؟** فایروال سخت‌افزاری با تراشه‌ی ویژه Sessionهای ساده را بدون CPU عبور می‌دهد و Throughput چند برابر می‌شود. اما بسته‌ها دیگر CPU را نمی‌بینند؛ Sniffer/Debug ناقص می‌شود. باید بدانید چه زمانی Offload فعال است و چگونه برای عیب‌یابی موقتاً خاموش شود.

**اصل:** بسته‌ی اول Session توسط CPU بررسی می‌شود و اگر شرایط (بدون Proxy-based UTM و ...) برقرار باشد، Session به NPU منتقل می‌شود.

**جمع‌بندی اصلی درس:** Packet Flow (۱۲-۰)، Session (۱۱-۷)، مفهوم CPU و ASIC.

### ۳) مفهوم پایه

پردازش بسته روی CPU عمومی گران است. FortiGateهای سخت‌افزاری دارای **ASIC**های اختصاصی‌اند: **NPU (Network Processor)** برای ارسال سریع و **CP (Content Processor)** برای رمزنگاری/Inspection (نام‌گذاری نسل‌ها: NP4/NP6/NP7 ...؛ نسخه/مدل `Unverified`). **Session Offload** یعنی بعد از ساخت Session توسط CPU (بسته‌ی اول، Policy، NAT)، بسته‌های بعدی همان Session مستقیماً در NPU ارسال می‌شوند و CPU را درگیر نمی‌کنند.

> **تشبیه:** CPU مثل مدیر است که اولین بار قانون را تعیین می‌کند؛ NPU مثل کارمند تندکار که بعد از آن، کار تکراری را بدون مراجعه به مدیر انجام می‌دهد.

### ۴) توضیح عمیق فنی

#### ۴-۱) مسیرها

``` text
Slow path (software): CPU -> full policy/NAT/profile -> forward
Fast path (kernel)  : session lookup in CPU kernel -> forward
NPU offload         : session installed in NPU -> forwarded in hardware
```

#### ۴-۲) چه ترافیکی Offload می‌شود؟

- معمولاً Sessionهای TCP/UDP ساده‌ی ارسالی (Forward) با NAT مجاز.
- **Sessionی که نیاز به Inspection محتوایی دارد** (برخی Profile‌ها، Proxy-based) یا ALG خاص، یا فیچرهای نیازمند CPU **Offload نمی‌شود** یا فقط بخشی از آن.
- ترافیک **Local-in/Local-out** اغلب CPU است.
- IPsec: رمزنگاری می‌تواند در CP/NPU انجام شود (`npu-offload` در Phase1؛ پیش‌فرض enable طبق CLI Reference 7.0).

(شرایط دقیق Offload وابسته به مدل، نسل NPU و نسخه است؛ مرجع رسمی آن مدل را ببینید.)

#### ۴-۳) پیامد برای عیب‌یابی

مستند رسمی «Debugging the packet flow» تأکید می‌کند: برای ردگیری Packet Flow روی پلتفرم‌های دارای **NP4/NP6**، Offload باید غیرفعال شود (`diagnose npu fastpath disable`) و برای NP7 باید Offload در Policy موردنظر غیرفعال شود؛ در غیر این صورت Debug Flow و گاهی Sniffer بسته‌های Offloadشده را نمی‌بینند. پس «بسته در Debug دیده نمی‌شود» همیشه یعنی Drop نیست؛ ممکن است Offloadشده باشد.

#### ۴-۴) پیامد برای Log و Counter

شمارنده‌ها و Log ممکن است برای Sessionهای Offloadشده با تأخیر/دقت متفاوت به‌روز شوند. برای تحلیل دقیق، Session را بررسی کنید (`diagnose sys session list` نشانگر Offload دارد؛ نام فیلد `Unverified`).

#### ۴-۵) Trade-off

| عامل | Offload روشن | Offload خاموش |
|---|---|---|
| Throughput | بالا | پایین |
| CPU | کم | زیاد |
| قابلیت Debug | محدود | کامل |
| Inspection عمیق | برخی ممنوع | کامل |

### ۵) مثال حل‌شده

#### مثال ساده

``` text
diagnose sys session list
 ... npu info: ...
```

وجود npu info یعنی Offload شده.

#### مثال متوسط — کنترل

``` text
config firewall policy
 edit 30
  set auto-asic-offload disable
 next
end
```

فقط موقت برای عیب‌یابی.

#### مثال سخت — UTM و ظرفیت

Proxy-based UTM Offload را غیرفعال می‌کند؛ ظرفیت به CPU محدود می‌شود. انتخاب مدل بر اساس Throughput **با UTM** نه فقط Firewall.

#### مثال‌های اصلی درس (مرور)

**مسئله:** مدیر Debug Flow اجرا کرده ولی ترافیک ping ۱۰۰٪ کار می‌کند و در Debug هیچ‌چیز دیده نمی‌شود.

**تحلیل:** احتمال Offload. اقدام (در Lab/Change Window، نه تولید): غیرفعال‌کردن موقت Offload طبق مرجع همان مدل، تکرار تست، و بازگرداندن.

``` text
FGT # diagnose npu fastpath disable
FGT # diagnose debug flow trace start 10
...
FGT # diagnose npu fastpath enable
```

(فقط روی مدل‌هایی که NP4/NP6 دارند؛ روی VM پشتیبانی نمی‌شود/لازم نیست؛ `Unverified`.)

**مثال متوسط:** فعال‌کردن IPS روی Policy باعث افت Throughput از ۲۰ به ۵ گیگابیت می‌شود. دلیل: بخش بازرسی در CPU/CP انجام می‌شود و Offload محدود می‌شود؛ باید Profile را انتخابی کرد (فصل ۱۶).

**مثال سخت:** در مقایسه‌ی دو Policy مشابه یکی Offload می‌شود و دیگری نه. با مقایسه‌ی Profile، Inspection Mode و ALG علت را پیدا کنید؛ سپس تصمیم بگیرید امنیت مهم‌تر است یا Throughput.

### ۶) طراحی و تصمیم‌گیری

| سؤال | معیار |
|---|---|
| Profile را روی همه‌ی ترافیک؟ | فقط جایی که لازم است؛ ترافیک Backup/Data Center ممکن است Offload شود |
| Flow یا Proxy | Flow سبک‌تر؛ Proxy قابلیت بیشتر |
| اندازه‌گیری | Baseline قبل/بعد از فعال‌سازی Profile |
| مدل فایروال | بر اساس Throughput با Inspection فعال (نه عدد Firewall خام Datasheet) |

### ۷) پیاده‌سازی: GUI و CLI

**GUI:** Dashboard → Performance (CPU/Memory/Sessions)؛ Policy & Objects → Firewall Policy → ستون Inspection Mode؛ Log & Report.

**CLI:**

``` text
get system performance status
diagnose sys top 2 20
diagnose sys session list
diagnose npu fastpath status
```

(`diagnose npu ...` فقط مدل‌های دارای NPU؛ `Unverified`.)

### ۸) Troubleshooting

| علامت | علت محتمل | اقدام |
|---|---|---|
| Debug Flow هیچ بسته‌ای نشان نمی‌دهد | Offload | غیرفعال موقت Offload (طبق مدل) |
| Throughput افت کرده | Profile/Proxy | مقایسه‌ی CPU و Profile |
| CPU بالا با ترافیک کم | Inspection سنگین/Local-in | `diagnose sys top` |

### ۹) نکات امنیتی

- خاموش‌کردن Offload در تولید فقط برای زمان کوتاه و با Change.
- Offload به‌معنای «دور زدن امنیت» نیست؛ فقط محل پردازش Sessionهای مجاز است؛ ولی Inspectionهای فعال‌نشده انجام نمی‌شوند.

### ۱۰) جمع‌بندی مفهومی

- Offload بعد از ساخت Session، پردازش را به NPU می‌دهد.
- Inspection عمیق/Proxy Offload را محدود می‌کند.
- Debug/Sniffer روی ترافیک Offloadشده می‌تواند ناقص باشد.
- Performance واقعی با Profile فعال اندازه‌گیری می‌شود.
- در Lab VM این‌ها قابل آزمایش نیستند؛ فقط مفهوم.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) NPU چه می‌کند؟ *(پاسخ: 12-9-ت1)*

**ت2.** (ساده) چرا Debug Flow ممکن است ترافیک را نبیند؟ *(پاسخ: 12-9-ت2)*

**ت3.** (متوسط) چرا IPS Throughput را کم می‌کند؟ *(پاسخ: 12-9-ت3)*

**ت4.** (متوسط) چرا عدد Throughput Datasheet برای انتخاب مدل کافی نیست؟ *(پاسخ: 12-9-ت4)*

**ت5.** (سخت) برنامه‌ی تست کنترل‌شده برای مقایسه‌ی Throughput با و بدون Profile بنویسید. *(پاسخ: 12-9-ت5)*

**م1.** Slow path و Fast path چه فرقی دارند؟ *(پاسخ: 12-9-م1)*

**Q1.** Quick quiz (English): Why can offloaded traffic be missing from debug flow output? *(پاسخ: 12-9-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NPU | Network Processor Unit | پردازنده‌ی شبکه‌ی سخت‌افزاری |
| CP | Content Processor | پردازنده‌ی محتوا/رمز |
| ASIC | Application-Specific Integrated Circuit | مدار مجتمع اختصاصی |
| Offload | Session offload | واگذاری Session به سخت‌افزار |

- *Offloaded sessions bypass the CPU for forwarding.* ← Sessionهای Offloadشده ارسال را بدون CPU انجام می‌دهند.
- *Disable offload only temporarily when debugging.* ← Offload را فقط موقت و برای Debug غیرفعال کنید.

### ۱۳) منابع

- Fortinet Docs: [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow) و بخش Hardware acceleration در Administration Guide 7.0 (مدل خود را بررسی کنید).
- Fortinet: FortiGate datasheet مدل مورد استفاده.

<a id="l-12-7"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: NPU/SPU و Session Offload

#### چرا؟

Session Offload کارایی را چند برابر می‌کند ولی عیب‌یابی را سخت‌تر (Sniffer/Debug ناقص). باید بدانید چه زمانی فعال است و چطور موقتاً خاموش شود.

#### مفهوم

بسته‌ی اول Session توسط CPU بررسی می‌شود؛ اگر شرایط برقرار باشد Session به NPU «Offload» می‌شود و بقیه‌ی بسته‌ها سخت‌افزاری عبور می‌کنند.

#### مثال ساده — دیدن

``` text
diagnose sys session list
 ... npu info: flag=0x81/0x81 ...
```

وجود اطلاعات npu یعنی Offload شده.

#### مثال متوسط — کنترل

``` text
config firewall policy
 edit 30
  set auto-asic-offload disable
 next
end
```

برای عیب‌یابی موقت؛ پس از آزمون برگردانید. `auto-asic-offload` به‌ازای Policy است.

#### مثال سخت — UTM و Offload

فعال‌بودن Proxy-based UTM معمولاً Offload را غیرفعال می‌کند؛ ظرفیت با CPU محدود می‌شود. پس مدل را بر اساس Throughput با UTM انتخاب کنید.

#### Lab

مفهوم را با خروجی Session نمونه توضیح دهید (VM بدون NPU: اجرا نشده).

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Sniffer ناقص | Offload | موقتاً خاموش |
| CPU بالا | UTM | مدل/Profile |
| Debug flow بی‌خروجی | Offload | بسته‌ی اول |

#### پرسش‌ها با پاسخ

**۱. Offload چیست؟** عبور سخت‌افزاری.
**۲. چرا عیب‌یابی سخت؟** بسته‌ها CPU نمی‌بینند.
**۳. کنترل؟** auto-asic-offload.

#### English Corner

- *Offloaded sessions bypass the CPU, so packet captures may be incomplete.*
- Q: How can you temporarily disable offload for troubleshooting?

## درس 12-7 — آزمون پایان فصل ۱۲ و تحلیل خطا: مدیریت قفل‌شده، Route اشتباه و Interface

**فصل 12 · بازنویسی عمیق · پیش‌نیاز: ۱۲-۰ تا ۱۲-۶ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سه پرونده‌ی خرابی (مدیریت، Route، Interface) را با روش ثابت حل کند.
2. Evidence خروجی دستورها را ثبت کند.
3. RCA و اقدام پیشگیرانه بنویسد.
4. آزمون عملی فصل ۱۲ را با Rubric تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا آزمون مدیریت قفل‌شده؟** رایج‌ترین حادثه‌ی خودساخته: ادمین با تغییر allowaccess یا Route خودش را قفل می‌کند. روش ایمن: تغییر با **بازگشت خودکار** (`cfg-save revert`). این آزمون آمادگی شما را برای تغییر بدون ریسک می‌سنجد.

**جمع‌بندی اصلی درس:** «بعد از تغییر Interface نمی‌توانم وارد فایروال شوم.» اگر مدیریت را روی همان Interface تغییر داده باشید، قفل شده‌اید. این آزمون سه خطای واقعی را تمرین می‌کند: قفل‌شدن، Route اشتباه و ناسازگاری VLAN.

### ۳) توضیح عمیق فنی

#### ۱) پرونده ۱: مدیریت قفل‌شده

علامت: بعد از `unset allowaccess` روی port2 دیگر GUI/SSH باز نمی‌شود. شاهد: ping بله، https نه. رفع: کنسول: `config system interface / edit port2 / set allowaccess https ssh ping`. پیشگیری: `execute ... ` Safe-mode/زمان‌بندی Rollback (`config system global / set cfg-save revert`؛ `Unverified`).

#### ۲) پرونده ۲: Route اشتباه

علامت: اینترنت قطع است ولی ping به Gateway ok. شاهد: `get router info routing-table details 8.8.8.8` به port2. علت: Static با Distance کمتر. رفع: اصلاح Distance/حذف. آزمون: traceroute.

#### ۳) پرونده ۳: VLAN

علامت: VLAN20 up ولی ping نه. شاهد: ARP incomplete. علت: Trunk سوییچ. رفع: Trunk allowed 20. آزمون.

#### ۴) تحویل

برای هر پرونده: Evidence، علت، رفع، آزمون، پیشگیری. Rubric: کشف ۳۰، رفع ۳۰، Evidence ۲۰، پیشگیری ۱۰، صداقت ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — Revert

``` text
config system global
 set cfg-save revert
 set cfg-revert-timeout 600
end
```

#### مثال متوسط — آزمون

تغییر عمدی allowaccess؛ اگر تأیید نشود پس از Timeout Config قبلی برمی‌گردد.

#### مثال سخت — حذف Default Route

GUI قطع شد؛ راه: کنسول و بازگردانی Route؛ درس: Revert و CHG. Rubric: برنامه‌ریزی ۲۰، اجرا ۳۰، Rollback ۲۵، Evidence ۱۵، گزارش ۱۰.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** پرونده ۱: ورود از کنسول، allowaccess بازگردانی؛ GUI باز می‌شود.

**متوسط (تحلیل):** پرونده ۲: Route 0.0.0.0 به port2 با distance 5؛ حذف؛ Default ISP برمی‌گردد.

**سخت (هم‌زمان):** دو عیب: Route و VLAN. ابتدا VLAN (لایه‌ی ۲) سپس Route؛ هر کدام آزمون جدا.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get router info routing-table details 8.8.8.8
diagnose ip arp list
show system interface port2
```

### ۸) Verification (اثبات صحت)

- Evidence سه پرونده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| مدیریت قفل | کنسول | allowaccess |

### ۱۰) نکات امنیتی

- تغییر Interface مدیریت فقط با کنسول/Rollback.

### ۱۱) جمع‌بندی مفهومی

- از کنسول.
- Route/ARP.
- پیشگیری.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) راه نجات مدیریت قفل؟ *(پاسخ: 12-7-ت1)*

**ت2.** (ساده) ARP incomplete یعنی؟ *(پاسخ: 12-7-ت2)*

**ت3.** (متوسط) چرا Distance مهم است؟ *(پاسخ: 12-7-ت3)*

**ت4.** (متوسط) پیشگیری از قفل‌شدن؟ *(پاسخ: 12-7-ت4)*

**ت5.** (سخت) دو عیب همزمان؟ *(پاسخ: 12-7-ت5)*

**ت6.** (سخت، طراحی) Runbook تغییر Interface. *(پاسخ: 12-7-ت6)*

**Q1.** Quick quiz (English): How can you regain management access after a bad allowaccess change? *(پاسخ: 12-7-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ARP | Address Resolution Protocol | تبدیل IP به MAC |

- *Keep console access ready before risky changes.* ← پیش از تغییر پرریسک کنسول را آماده نگه دارید.

### ۱۴) کارت Lab

**کارت Lab:** آزمون فصل ۱۲ (اجرا نشده). **Evidence:** `03-ops/fgt-asbuilt-1.md`.

### ۱۵) منابع

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: روش «تغییر ایمن Interface مدیریت» با اثبات

**سناریو.** باید `allowaccess` و IP Interface مدیریتی را تغییر دهید در حالی که از همان Interface متصل هستید.

**روش ایمن (چهار لایه)**
1. **کنسول آماده** (یا Out-of-band) پیش از تغییر.
2. **Backup** و ثبت وضعیت فعلی: `show system interface mgmt`.
3. **Revert خودکار:** از `cfg-save revert` با `cfg-revert-timeout` (پیش‌فرض ۶۰۰ ثانیه) استفاده کنید تا اگر تأیید نکردید، تنظیم به آخرین ذخیره برگردد (طبق مستند).

``` text
config system global
 set cfg-save revert
 set cfg-revert-timeout 300
end
...change...
execute cfg save      ! confirm only after you verified access
```

4. **تغییر کوچک و آزمون:** اول `append` یا اضافه‌کردن، نه جایگزینی؛ در CLI فرمان `set allowaccess` فهرست را جایگزین می‌کند.

**آزمون پس از تغییر**

``` text
ping 10.99.0.1                 ! L3
curl -k https://10.99.0.1      ! service
get system status              ! on console
```

**اگر قفل شدید:** کنسول → بازگردانی allowaccess؛ علت را در RCA ثبت کنید.

**درس‌های سه پرونده‌ی آزمون**
- مدیریت قفل: کنسول.
- Route اشتباه: `get router info routing-table details` و Distance.
- VLAN: ARP incomplete و Trunk.

**پرسش‌های مصاحبه**
1. *چرا cfg-save revert؟* شبکه‌ی ایمنی برای تغییر مدیریتی.
2. *چرا `set allowaccess` خطرناک است؟* فهرست قبلی را جایگزین می‌کند.
3. *چه چیزی در RCA می‌نویسید؟* علت، اثر، زمان، پیشگیری.

### تکمیل عمیق: آزمون پایان فصل ۱۲ — مدیریت قفل‌شده و روش Revert

#### چرا؟

بسیاری از قطعی‌ها وقتی رخ می‌دهد که ادمین با تغییر `allowaccess` یا Route خودش را از مدیریت قفل می‌کند. روش ایمن: تغییر با بازگشت خودکار.

#### روش cfg-save revert

``` text
config system global
 set cfg-save revert
 set cfg-revert-timeout 600
end
```

تغییرات تا زمان تأیید ذخیره نمی‌شوند؛ اگر ظرف ۶۰۰ ثانیه تأیید نشود، دستگاه به Config قبل برمی‌گردد (طبق مستند Fortinet).

#### مثال ساده

تغییر Interface مدیریتی؛ اگر قفل شدید، پس از Timeout Config قبلی برمی‌گردد.

#### مثال متوسط — آزمون

تغییر عمدی allowaccess و بازگشت پس از Timeout (Lab).

#### مثال سخت — تحلیل خطا

کارآموز Default Route را حذف کرد و GUI قطع شد؛ راه: کنسول، Route را بازگردانی، سپس درس: Revert و CHG.

#### Rubric

``` text
Planning 20 | Execution 30 | Rollback 25 | Evidence 15 | Report 10
```

#### Lab

آزمون را اجرا و بازگشت را ثبت کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| قفل مدیریت | allowaccess/Route | Console/Revert |
| Revert نشد | Timeout زیاد | کم |
| ذخیره‌ی ناخواسته | تأیید | دقت |

#### پرسش‌ها با پاسخ

**۱. چرا Console؟** مسیر آخر.
**۲. Revert؟** بازگشت خودکار.
**۳. ثبت؟** ضروری.

#### English Corner

- *Use configuration revert so that a lockout rolls back automatically.*
- Q: What should you do if you lock yourself out of the GUI?

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
