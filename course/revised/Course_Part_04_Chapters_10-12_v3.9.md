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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. توضیح دهد Redistribution یعنی تزریق مسیرهای یک پروتکل به پروتکل دیگر، نه «ترجمه‌ی» پروتکل‌ها.
2. Seed Metric پیش‌فرض و دستور `metric`/`default-metric` را برای OSPF/EIGRP/RIP/BGP تنظیم کند.
3. `subnets` در OSPF، Route Type E1/E2 و اثر آن‌ها را تحلیل کند.
4. نتیجه را با `show ip route` و `show ip ospf database external` تأیید کند.
5. خطاهای رایج (Metric ناسازگار، فراموشی subnets) را رفع کند.

### ۲) مفهوم پایه: چیست و چرا؟

فرض کنید شرکتی دو شعبه دارد: یکی OSPF اجرا می‌کند، دیگری EIGRP. هر دو زبان خودشان را می‌فهمند و یکدیگر را نه. Redistribution مترجمی در مرز است که مسیرهای یک زبان را می‌گیرد و در زبان دیگر اعلام می‌کند. ولی مترجم باید «هزینه» را هم بسازد، چون Metricها قابل تبدیل نیستند. این هزینه‌ی ساختگی همان Seed Metric است.

### ۳) توضیح عمیق فنی

#### ۱) اصل کار

Redistribution فقط مسیرهایی را که **در RIB با آن پروتکل یا نوع مسیر نصب شده‌اند** برمی‌دارد، نه همه‌ی چیزهایی که پروتکل می‌داند. پس اگر مسیر در RIB نباشد، منتقل نمی‌شود.

``` text
OSPF domain  <--- R-ASBR --->  EIGRP domain
R-ASBR: router ospf 1 + router eigrp 100 ; redistribute in the needed direction
```

#### ۲) Seed Metric

| مقصد | Metric پیش‌فرض Seed |
|---|---|
| OSPF | 20 (BGP: 1)، Type E2 |
| EIGRP | بی‌نهایت: باید دستی تعیین شود |
| RIP | بی‌نهایت: باید دستی تعیین شود |
| BGP | Metric (MED) از IGP کپی می‌شود |

``` text
router ospf 1
 redistribute eigrp 100 subnets metric 100 metric-type 1
router eigrp 100
 redistribute ospf 1 metric 10000 100 255 1 1500
 ! bandwidth(Kbps) delay(10us) reliability load MTU
```

#### ۳) `subnets` و Route Type

بدون `subnets` در OSPF فقط مسیرهای classful منتقل می‌شوند و /24ها «ناپدید» می‌شوند: شایع‌ترین خطا. E1 = Metric خارجی + هزینه‌ی داخلی تا ASBR؛ E2 (پیش‌فرض) = فقط Metric خارجی ثابت. E1 برای چند ASBR و انتخاب نزدیک‌ترین خروج مناسب‌تر است.

#### ۴) AD

مسیر خارجی OSPF (AD=110)، EIGRP External (170)، EIGRP داخلی (90). اثر: در Redistribution دوطرفه حلقه و Route Feedback ممکن است (درس ۱۰-۲).

#### ۵) اعتبارسنجی

``` text
show ip route ospf
show ip ospf database external
show ip route 172.16.5.0
show ip eigrp topology 172.16.5.0/24
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Seed Metric | OSPF: metric-type 1 برای چند ASBR؛ EIGRP/RIP: دستی |
| فیلتر | Route-map/Prefix-list؛ نه همه‌چیز |
| جهت | یک‌طرفه تا ممکن؛ دوطرفه با Tag |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** EIGRP 100 دارای 172.16.0.0/16 است؛ در ASBR `redistribute eigrp 100 subnets` زده می‌شود؛ در روتر OSPF دیگر `O E2 172.16.5.0/24 [110/20]` دیده می‌شود. رابطه: Metric 20 همان Seed.

**متوسط (تحلیل):** بعد از Redistribute، در OSPF فقط 172.16.0.0/16 هست و /24ها نیستند. علت: `subnets` نبود. رفع: افزودن `subnets`؛ آزمون: `show ip route ospf` و ping به 172.16.5.1.

**سخت (طراحی):** دو ASBR (A,B) هر دو EIGRP را به OSPF می‌دهند. با E2 هر روتر OSPF Metric یکسان 20 می‌بیند و ممکن است از ASBR دورتر خارج شود. تحلیل: با E1 هزینه تا ASBR هم افزوده می‌شود و نزدیک‌ترین انتخاب می‌شود. آزمون: traceroute از دو نقطه. معیار: هر Router نزدیک‌ترین ASBR.

### ۷) پیاده‌سازی از مسیر CLI

``` text
router ospf 1
 redistribute eigrp 100 subnets metric 100 metric-type 1
router eigrp 100
 redistribute ospf 1 metric 10000 100 255 1 1500
show ip route ospf
show ip ospf database external
```

### ۸) Verification (اثبات صحت)

- مسیرهای Redistribute با نوع E1/E2 یا D EX در جدول.
- ping/traceroute بین دو دامنه.
- Metric مطابق Seed.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| /24ها نیستند | `show ip route` فقط classful | `subnets` را اضافه کنید |
| مسیر EIGRP به OSPF نمی‌رود | Metric EIGRP تعیین نشده | `metric ...` بدهید |
| مسیرها ناپایدار | Feedback | Tag و Route-map (۱۰-۲) |

### ۱۰) نکات امنیتی

- مسیر ناخواسته را وارد نکنید؛ Route-map/Prefix-list.
- ASBR نقطه‌ی حساس: ACL/Auth.

### ۱۱) جمع‌بندی مفهومی

- Redistribution مترجم است نه Merge.
- Seed Metric لازم است.
- subnets در OSPF.
- E1 در برابر E2.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Seed Metric پیش‌فرض Redistribution به OSPF چند است؟ *(پاسخ: 10-1-ت1)*

**ت2.** (ساده) چرا EIGRP و RIP Metric پیش‌فرض ندارند؟ *(پاسخ: 10-1-ت2)*

**ت3.** (متوسط) تفاوت E1 و E2؟ *(پاسخ: 10-1-ت3)*

**ت4.** (متوسط) اگر `subnets` نباشد چه می‌شود؟ *(پاسخ: 10-1-ت4)*

**ت5.** (سخت) دو ASBR و تصمیم Type. *(پاسخ: 10-1-ت5)*

**ت6.** (سخت، طراحی) طرح Redistribution یک‌طرفه با فیلتر. *(پاسخ: 10-1-ت6)*

**Q1.** Quick quiz (English): What happens if you redistribute into EIGRP without specifying a metric? *(پاسخ: 10-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ASBR | Autonomous System Boundary Router | روتر مرزی دامنه |
| E2 | OSPF External Type 2 | مسیر خارجی نوع ۲ |
| Seed | Seed metric | Metric اولیه |

- *Redistribution injects routes from one protocol into another.* ← Redistribution مسیرهای یک پروتکل را به دیگری تزریق می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** Redistribution یک‌طرفه. **Evidence:** `03-ops/redist1.md`.

### ۱۵) منابع

- Cisco IOS IP Routing guide: Redistribution
- RFC 2328 (OSPF) بخش External

<a id="l-10-2"></a>

### تعمیق: پروژه‌ی Redistribution از صفر تا آزمون (OSPF ⇄ EIGRP)

**سناریو.** سازمان پس از ادغام دو شرکت: دفتر مرکزی OSPF Area 0 (10.0.0.0/16) و شعب EIGRP 100 (172.16.0.0/16). یک ASBR (R5) هر دو را می‌بیند. هدف: شعب مرکز را ببینند و مرکز شعب را.

**گام ۱ — Baseline.**

``` text
R5# show ip route ospf | count
R5# show ip route eigrp | count
R1(OSPF)# ping 172.16.5.1   ! expected FAIL before redistribution
```

**گام ۲ — تزریق EIGRP به OSPF (با Metric نوع ۱ برای چند ASBR احتمالی).**

``` text
router ospf 1
 redistribute eigrp 100 subnets metric 100 metric-type 1
```

**گام ۳ — تزریق OSPF به EIGRP.** هر پروتکل Metric خودش را می‌خواهد: bandwidth (Kbps)، delay (واحد ۱۰ میکروثانیه)، reliability، load، MTU:

``` text
router eigrp 100
 redistribute ospf 1 metric 100000 10 255 1 1500
```

معنی: 100 Mbps، delay = 10 × 10µs = 100µs، reliability 255، load 1، MTU 1500.

**گام ۴ — Verification.**

``` text
R1# show ip route 172.16.5.0
 O E1 172.16.5.0/24 [110/120] via R5
BR3# show ip route 10.0.1.0
 D EX 10.0.1.0/24 [170/...] via R5
```

محاسبه‌ی [110/120]: Metric E1 = ۱۰۰ (Seed) + هزینه‌ی داخلی OSPF تا R5 (۲۰) = ۱۲۰.

``` text
E1 metric = seed 100 + internal cost to ASBR 20 = 120
E2 metric = seed 100 (no internal cost added)
```

**گام ۵ — آزمون منفی.** Prefixی که نباید منتقل شود (مثلاً مدیریت 10.99.0.0/24) را با Route-map فیلتر کنید و تأیید کنید در شعب دیده نمی‌شود.

**اشتباهات رایج**
- فراموشی `subnets`: فقط Prefix کلاس‌دار می‌رود.
- فراموشی Metric در EIGRP: مسیر منتقل نمی‌شود (Metric بی‌نهایت).
- Redistribution بدون فیلتر: Default و مسیرهای مدیریت نشت می‌کنند.

**پرسش‌های مصاحبه**
1. *E1 و E2 را کی استفاده می‌کنید؟* E1 وقتی چند ASBR دارید و می‌خواهید نزدیک‌ترین انتخاب شود؛ E2 وقتی هزینه‌ی خارجی ثابت کافی است.
2. *AD مسیر EIGRP External؟* ۱۷۰.
3. *چرا Redistribution دوطرفه خطرناک است؟* Route Feedback و حلقه (درس ۱۰-۲).

### تکمیل عمیق: Redistribution — Seed Metric و Route Type با محاسبه

#### چرا باید یاد بگیریم؟

در سازمان‌های واقعی چند پروتکل مسیریابی کنار هم‌اند (OSPF در هسته، EIGRP در شعب، BGP به ISP). Redistribution مسیرهای یک پروتکل را به پروتکل دیگر «ترجمه» می‌کند؛ ولی اگر درست نباشد، حلقه یا مسیر نادرست می‌سازد.

#### مفهوم Seed Metric

هر پروتکل متریک متفاوتی دارد؛ هنگام ورود مسیر خارجی باید یک متریک اولیه (Seed) داد.

``` text
OSPF -> EIGRP : need bandwidth, delay, reliability, load, MTU
EIGRP -> OSPF : default seed metric 20, type E2 (verify)
RIP seed metric : hop count (16 = unreachable)
```

#### مثال ساده — E1 در برابر E2

E2: متریک خارجی ثابت (cost داخلی OSPF اضافه نمی‌شود). E1: متریک خارجی + cost داخلی تا ASBR.

``` text
E2 total = external metric (e.g. 20)
E1 total = external metric + internal cost to ASBR = 20 + 15 = 35
```

#### مثال متوسط — پروژه OSPF⇄EIGRP

OSPF Area 0 و EIGRP AS 100؛ روتر مرزی هر دو را اجرا می‌کند. ورود EIGRP به OSPF: `redistribute eigrp 100 metric 20 metric-type 1 subnets`. ورود OSPF به EIGRP: `redistribute ospf 1 metric 10000 100 255 1 1500`.

#### مثال سخت — Subnets

بدون کلمه‌ی `subnets` در Cisco فقط شبکه‌های Classful وارد OSPF می‌شوند؛ خطای رایج.

#### Lab

دو روتر با دو پروتکل بسازید و Redistribution یک‌طرفه را آزمون کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| مسیر وارد نمی‌شود | metric | تنظیم |
| Subnet ناقص | subnets | افزودن |
| متریک عجیب | نوع E1/E2 | مقایسه |

#### پرسش‌ها با پاسخ

**۱. Seed Metric؟** متریک اولیه.
**۲. E1 و E2؟** با و بدون Cost داخلی.
**۳. subnets؟** وارد کردن زیرشبکه‌ها.

#### English Corner

- *External type 1 adds the internal cost to the ASBR; type 2 does not.*
- Q: Why must a seed metric be defined during redistribution?

## درس 10-2 — Redistribution دوطرفه، Route Feedback و جلوگیری از حلقه با Tag

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۱ · ≈ 9 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. خطر Route Feedback و Suboptimal routing را در دو ASBR توضیح دهد.
2. با Tag + Route-map حلقه را قطع کند.
3. Prefix-list/Distribute-list را مکمل کند.
4. با آزمون منفی ثابت کند حلقه رخ نمی‌دهد.
5. مسیر چندپروتکلی را تحلیل کند.

### ۲) مفهوم پایه: چیست و چرا؟

دو شعبه با دو ASBR: R-A و R-B هر دو دوطرفه ترجمه می‌کنند. مسیری که R-A از OSPF به EIGRP برد، R-B دوباره از EIGRP به OSPF برمی‌گرداند و کم‌کم همه چیز به هم می‌ریزد. راه‌حل: هر مسیر را با «برچسب مبدأ» (Tag) علامت بزنید تا دوباره منتقل نشود.

### ۳) توضیح عمیق فنی

#### ۱) سناریو

``` text
          OSPF area 0              EIGRP 100
 R1 ----- R-A ======================== R-C
           \\                      //
            R-B ===================
```

#### ۲) راه‌حل Tag

``` text
route-map OSPF-TO-EIGRP deny 10
 match tag 100
route-map OSPF-TO-EIGRP permit 20
 set tag 200
route-map EIGRP-TO-OSPF deny 10
 match tag 200
route-map EIGRP-TO-OSPF permit 20
 set tag 100
router eigrp 100
 redistribute ospf 1 metric 10000 100 255 1 1500 route-map OSPF-TO-EIGRP
router ospf 1
 redistribute eigrp 100 subnets route-map EIGRP-TO-OSPF
```

منطق: مسیری که از EIGRP به OSPF آمد Tag=100 دارد؛ برگشت آن به EIGRP رد می‌شود و برعکس. 

#### ۳) AD و Feedback

EIGRP External AD=170 و OSPF External AD=110؛ مسیری که از OSPF وارد EIGRP شده و بر می‌گردد ممکن است با AD بهتر بر مسیر اصلی غلبه کند. Tag مشکل را از ریشه می‌برد.

#### ۴) مکمل

Prefix-list برای فقط شبکه‌های مجاز؛ و `distance` برای External.

#### ۵) آزمون

``` text
show ip route 10.1.1.0
show ip ospf database external 10.1.1.0
show ip eigrp topology 10.1.1.0/24
```

مسیر باید فقط از منبع اصلی باشد.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| چند ASBR | Tag+Route-map روی همه |
| راه جایگزین | یک‌طرفه+Default |
| مستندسازی | جدول Tagها |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Tag 100 روی مسیرهای EIGRP→OSPF؛ در R-B فیلتر Tag 100 در جهت برگشت؛ آزمون: مسیر از R-A دوباره به EIGRP نمی‌رود.

**متوسط (تحلیل):** ترافیک بین OSPF و EIGRP از مسیر طولانی رفت: Suboptimal؛ علت: ASBR دورتر؛ راه: E1/Metric/Tag؛ و در نهایت طراحی یک ASBR اصلی.

**سخت (چندعلتی):** بعد از افزودن R-B حلقه؛ بررسی: Tag ست نشده روی R-B (Route-map فقط روی R-A)؛ تحلیل: یکسان‌سازی پیکربندی روی هر دو؛ آزمون منفی با شکستن لینک و traceroute. معیار: بدون حلقه و Convergence < 10 s.

### ۷) پیاده‌سازی از مسیر CLI

``` text
route-map OSPF-TO-EIGRP deny 10
 match tag 100
route-map OSPF-TO-EIGRP permit 20
 set tag 200
show route-map OSPF-TO-EIGRP
show ip route 10.1.1.0
```

### ۸) Verification (اثبات صحت)

- Tag در جدول مسیر.
- نبود حلقه (traceroute).
- Convergence پس از قطع لینک.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| مسیر حلقه می‌زند | traceroute/TTL | Tag/Route-map روی همه ASBRها |
| مسیر از بین می‌رود | Tag اشتباه | match/set را بازبینی کنید |
| Suboptimal | AD/Type | E1/Metric |

### ۱۰) نکات امنیتی

- همه‌ی ASBRها یکسان پیکربندی شوند.

### ۱۱) جمع‌بندی مفهومی

- دو ASBR=خطر.
- Tag کلید.
- آزمون منفی.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Route Feedback چیست؟ *(پاسخ: 10-2-ت1)*

**ت2.** (ساده) Tag چه کاری می‌کند؟ *(پاسخ: 10-2-ت2)*

**ت3.** (متوسط) چرا Route-map باید روی هر دو ASBR باشد؟ *(پاسخ: 10-2-ت3)*

**ت4.** (متوسط) AD External OSPF و EIGRP؟ *(پاسخ: 10-2-ت4)*

**ت5.** (سخت) پس از R-B حلقه شد؛ تحلیل. *(پاسخ: 10-2-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی Tag سازمان. *(پاسخ: 10-2-ت6)*

**Q1.** Quick quiz (English): Why is route tagging used in two-way redistribution? *(پاسخ: 10-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Tag | Route tag | برچسب مسیر |
| Feedback | Route feedback | بازگشت مسیر |

- *Tag routes at the boundary to stop loops.* ← مسیرها را در مرز Tag کنید تا حلقه نشود.

### ۱۴) کارت Lab

**کارت Lab:** دوطرفه با Tag. **Evidence:** `03-ops/redist2.md`.

### ۱۵) منابع

- Cisco IOS Route-map guide
- RFC 2328

<a id="l-10-3"></a>

### تعمیق: سناریوی حلقه‌ی واقعی با دو ASBR و رفع قدم‌به‌قدم

**سناریو.** دو ASBR (R5 و R6) هر دو OSPF ⇄ EIGRP دوطرفه دارند. پس از افزودن R6، در شعبه Ping به مرکز گاهی TTL expired می‌دهد.

**گام ۱ — اثبات حلقه.**

``` text
BR3# traceroute 10.0.1.5
 1 172.16.0.5 (R5)  2 172.16.0.6 (R6)  3 172.16.0.5 (R5)  4 172.16.0.6 (R6) ...
```

مسیر 10.0.1.0/24 بین R5 و R6 دور می‌زند.

**گام ۲ — علت.** R5 مسیر OSPF را به EIGRP داد؛ R6 آن را از EIGRP یاد گرفت (AD 170 بدتر از OSPF 110 ولی برای R6 مسیر داخلی OSPF هم هست) و در جهت برگشت دوباره به OSPF تزریق کرد؛ در بعضی Prefixها Metric/AD ناسازگار مسیر را به EIGRP ترجیح می‌دهد.

**گام ۳ — Tag روی هر دو ASBR.**

``` text
route-map OSPF-TO-EIGRP deny 10
 match tag 100
route-map OSPF-TO-EIGRP permit 20
 set tag 200
route-map EIGRP-TO-OSPF deny 10
 match tag 200
route-map EIGRP-TO-OSPF permit 20
 set tag 100
router eigrp 100
 redistribute ospf 1 metric 100000 10 255 1 1500 route-map OSPF-TO-EIGRP
router ospf 1
 redistribute eigrp 100 subnets route-map EIGRP-TO-OSPF
```

منطق: مسیری که از OSPF به EIGRP رفته Tag=200 دارد؛ در جهت EIGRP→OSPF رد می‌شود؛ مسیری که از EIGRP به OSPF رفته Tag=100 دارد؛ در جهت OSPF→EIGRP رد می‌شود.

**گام ۴ — Verification.**

``` text
R6# show ip route 10.0.1.0
 O 10.0.1.0/24 [110/20] via ...     ! native OSPF route, not the EIGRP copy
R6# show ip eigrp topology 10.0.1.0/24    ! tag 200 present
BR3# traceroute 10.0.1.5               ! 2 hops, no loop
```

**گام ۵ — آزمون خرابی.** لینک R5-مرکز را قطع کنید؛ مسیر باید از R6 برود؛ باز هم بدون حلقه.

**اشتباهات رایج**
- Tag فقط روی یک ASBR.
- Tag هر دو جهت یکسان (200 و 200): هر مسیر برگردانده می‌شود یا همه فیلتر می‌شوند.
- Route-map بدون `permit` پایانی: Deny ضمنی همه‌ی مسیرهای دیگر را هم می‌اندازد (در Redistribution برخلاف PBR Deny ضمنی مسیر را حذف می‌کند).

**پرسش‌های مصاحبه**
1. *چرا Tag و نه Distance؟* Distance فقط ترجیح را عوض می‌کند، Tag ریشه‌ی بازگشت را می‌بندد.
2. *OSPF Tag را چگونه حمل می‌کند؟* در LSA نوع ۵ فیلد External Route Tag.
3. *جایگزین بدون دوطرفه؟* Default Route از مرکز به شعب و Summary از شعب به مرکز.

### تکمیل عمیق: Redistribution دوطرفه و جلوگیری از حلقه

#### چرا؟

Redistribution دوطرفه در دو نقطه مرزی خطرناک‌ترین حالت است: مسیری که از A به B رفت می‌تواند از نقطه‌ی دیگر به A برگردد و حلقه یا مسیر زیرین (Suboptimal) بسازد (Route Feedback).

#### مثال ساده — دو نقطه‌ی مرزی

``` text
OSPF --- R1 --- EIGRP
OSPF --- R2 --- EIGRP
```

R1 مسیر EIGRP را به OSPF می‌دهد؛ R2 آن را از OSPF می‌گیرد و دوباره به EIGRP تزریق می‌کند.

#### مثال متوسط — راه‌حل با Tag

``` text
route-map EIGRP-TO-OSPF permit 10
 set tag 100
route-map OSPF-TO-EIGRP deny 10
 match tag 100
route-map OSPF-TO-EIGRP permit 20
```

مسیری که با Tag 100 وارد OSPF شد دوباره به EIGRP نمی‌رود.

#### مثال سخت — Administrative Distance

مسیر E2 در OSPF (AD 110) و EIGRP External (AD 170): R2 ممکن است مسیر OSPF را ترجیح دهد و ترافیک را به‌جای کوتاه‌ترین، از مسیر دیگر بفرستد. با Tag و Filter کنترل کنید.

#### قاعده‌ی طلایی

Redistribution دوطرفه فقط با Tag/Prefix-list و فقط در صورت نیاز؛ ترجیحاً یک‌طرفه + Default.

#### Lab

حلقه را عمداً بسازید و با Tag رفع کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| حلقه | Feedback | Tag |
| مسیر زیرین | AD | Filter |
| ناپایداری | دو نقطه | یک‌طرفه |

#### پرسش‌ها با پاسخ

**۱. Route Feedback؟** برگشت مسیر به مبدأ.
**۲. Tag چرا؟** نشان‌گذاری.
**۳. بهتر؟** یک‌طرفه + Default.

#### English Corner

- *Tag routes at redistribution points to prevent them from being redistributed back.*
- Q: What is route feedback?

## درس 10-3 — ECMP و توزیع بار: Equal-cost، Hashing و Load Balancing

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۱۰-۱ · ≈ 8 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. شرط ECMP (برابری Metric و AD) و Maximum-paths را بگوید.
2. Hashing (Per-flow) را در برابر Per-packet توضیح دهد.
3. `show ip cef`/`show ip route` را برای مسیرهای برابر بخواند.
4. اثر ECMP بر ترافیک Stateful (فایروال) را تحلیل کند.
5. عیب‌یابی نبود Load-balancing را انجام دهد.

### ۲) مفهوم پایه: چیست و چرا؟

دو جاده‌ی هم‌اندازه به مقصد: ECMP هر دو را به‌کار می‌گیرد. ولی ماشین‌هایی که یک «گفتگو» دارند باید همه از یک جاده بروند، وگرنه بسته‌ها برعکس می‌رسند. پس تقسیم «روی جریان» (flow) انجام می‌شود نه روی بسته.

### ۳) توضیح عمیق فنی

#### ۱) شرط

مسیرها با **Metric و AD برابر** و حداکثر `maximum-paths` (مقدار پیش‌فرض بسته به پلتفرم/نسخه‌ی IOS فرق دارد؛ با `show ip protocols` مقدار فعلی را ببینید).

``` text
router ospf 1
 maximum-paths 4
show ip route 10.1.0.0
 10.1.0.0/16 [110/20] via 10.0.1.2 ... via 10.0.2.2
```

#### ۲) Hashing

CEF بر اساس Hash (Src IP/Dst IP ± پورت) جریان را به یک مسیر نگاشت می‌کند ⇒ جریان واحد ترتیب را حفظ می‌کند ولی توزیع بار ممکن است ناهموار باشد (چند جریان بزرگ روی یک لینک).

``` text
ip cef load-sharing algorithm universal
show ip cef 10.1.1.1 internal
```

#### ۳) Per-packet

توزیع بسته به بسته: بار یکنواخت‌تر، ولی بسته‌ها ممکن است نامرتب برسند و برای TCP/فایروال Stateful مشکل می‌سازد؛ ممکن است Session بسته شود.

#### ۴) ECMP و فایروال

با دو فایروال Stateful، رفت از یکی و برگشت از دیگری ⇒ Drop (Asymmetric: درس ۱۰-۶). پس Hash باید Symmetric باشد.

#### ۵) خرابی پنهان

یک لینک Down می‌شود، مسیر حذف می‌شود ولی Flowهای آن به لینک دیگر منتقل می‌شوند و Session ریست می‌شود. اندازه‌گیری پهنای باند قبل/بعد.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Per-flow یا Per-packet | Per-flow برای Stateful |
| Maximum-paths | طبق تعداد لینک |
| Hash | Symmetric |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** دو مسیر OSPF هزینه‌ی 20؛ `show ip route` هر دو را نشان می‌دهد.

**متوسط (تحلیل):** یک لینک ۹۰٪ و دیگری ۱۰٪: Hash بر اساس Src/Dst دو Host اصلی؛ راه: افزودن پورت به Hash یا الگوریتم دیگر؛ آزمون با iperf چند جریان.

**سخت (فایروال):** دو فایروال Stateful پشت ECMP؛ برخی Sessionها قطع می‌شوند: Hash رفت/برگشت متفاوت؛ راه: Symmetric hash/Routing طراحی‌شده/Active-Standby؛ آزمون: `diagnose sys session` روی هر دو.

### ۷) پیاده‌سازی از مسیر CLI

``` text
router ospf 1
 maximum-paths 4
show ip route 10.1.0.0
show ip cef 10.1.1.1 internal
show ip cef exact-route 10.0.0.1 10.1.1.1
```

### ۸) Verification (اثبات صحت)

- چند Next-hop در RIB.
- `exact-route` مسیر جریان را نشان می‌دهد.
- آزمون بار با چند جریان.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| فقط یک مسیر | Metric/AD برابر؟ | Cost را یکسان کنید |
| توزیع ناهموار | Hash | الگوریتم/Port |
| Sessionها قطع | فایروال | Symmetric |

### ۱۰) نکات امنیتی

- ECMP با فایروال بدون Symmetry ممنوع.

### ۱۱) جمع‌بندی مفهومی

- Per-flow.
- Hash.
- Stateful حساس.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) شرط ECMP؟ *(پاسخ: 10-3-ت1)*

**ت2.** (ساده) Per-flow چیست؟ *(پاسخ: 10-3-ت2)*

**ت3.** (متوسط) چرا Per-packet برای TCP بد است؟ *(پاسخ: 10-3-ت3)*

**ت4.** (متوسط) maximum-paths پیش‌فرض OSPF؟ *(پاسخ: 10-3-ت4)*

**ت5.** (سخت) توزیع ۹۰/۱۰ را چطور حل کنید؟ *(پاسخ: 10-3-ت5)*

**ت6.** (سخت، طراحی) ECMP دو فایروال. *(پاسخ: 10-3-ت6)*

**Q1.** Quick quiz (English): Why is per-flow load balancing preferred over per-packet? *(پاسخ: 10-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ECMP | Equal-Cost Multi-Path | چندمسیری هم‌هزینه |
| CEF | Cisco Express Forwarding | ارسال سریع سیسکو |

- *Per-flow hashing keeps a flow on one path.* ← Hash روی جریان، جریان را روی یک مسیر نگه می‌دارد.

### ۱۴) کارت Lab

**کارت Lab:** ECMP. **Evidence:** `03-ops/ecmp.md`.

### ۱۵) منابع

- Cisco CEF guide

<a id="l-10-4"></a>

### تعمیق: ECMP با اندازه‌گیری واقعی و پرونده‌ی «Sessionها قطع می‌شوند»

**سناریو.** دو لینک 1 Gbps بین Core و Edge با Cost برابر؛ ECMP فعال. کاربران گزارش می‌دهند Sessionهای بزرگ (SMB) گاهی ریست می‌شوند.

**گام ۱ — تأیید ECMP.**

``` text
Core# show ip route 10.99.0.0
 O 10.99.0.0/24 [110/20] via 10.0.1.2, Gi0/1
                        [110/20] via 10.0.2.2, Gi0/2
Core# show ip cef 10.99.0.5 internal
Core# show ip cef exact-route 10.10.0.5 10.99.0.5
```

برای هر جفت Src/Dst دستور exact-route مسیر Hash را نشان می‌دهد.

**گام ۲ — اندازه‌گیری توزیع.** با iperf سه حالت:

``` text
1 flow    -> uses one link (about 940 Mbps total, other link idle)
8 flows   -> ~ 55/45 across links (depends on hash)
64 flows  -> ~ 50/50
```

نتیجه: یک جریان از یک لینک می‌رود؛ ECMP پهنای باند «یک جریان» را دو برابر نمی‌کند، «مجموع جریان‌ها» را.

**گام ۳ — علت ریست Session.** بین Core و Edge یک فایروال Stateful در هر مسیر است؛ تغییر الگوریتم Hash یا خرابی یک لینک جریان را به لینک دیگر می‌برد و فایروال دوم Session نمی‌شناسد.

**گام ۴ — رفع.** یکی از سه راه:
1. Symmetric Hash/جفت‌سازی فایروال‌ها با Session sync.
2. به‌جای ECMP، Primary/Backup (Cost متفاوت) برای ترافیک Stateful.
3. EtherChannel به یک فایروال (HA Cluster).

**گام ۵ — الگوریتم Hash.**

``` text
ip cef load-sharing algorithm include-ports source destination
```

پیش‌فرض universal فقط IP را در Hash می‌گذارد؛ include-ports توزیع را بهتر می‌کند ولی Symmetry را تضمین نمی‌کند؛ برای فایروال باید جداگانه بررسی شود.

**اشتباهات رایج**
- انتظار 2 Gbps برای یک انتقال فایل.
- Per-packet برای TCP: بسته‌ها نامرتب می‌رسند.
- ECMP روی دو فایروال Stateful بدون Sync.

**پرسش‌های مصاحبه**
1. *شرط ECMP؟* مسیرهای برابر Metric و AD و ≤ `maximum-paths` (پلتفرم‌محور).
2. *چرا یک جریان فقط یک لینک؟* Hash روی Src/Dst/Port؛ ترتیب بسته‌ها حفظ می‌شود.
3. *تفاوت Per-flow و Per-packet؟* Per-flow ترتیب را حفظ می‌کند و با Stateful سازگار است.

### تکمیل عمیق: ECMP و توزیع بار

#### چرا؟

دو لینک برابر باید هر دو استفاده شوند؛ ولی «توزیع» به Hash بستگی دارد نه یکنواخت بودن بار.

#### مثال ساده

دو مسیر هزینه‌ی برابر ⇒ هر دو در جدول؛ ترافیک بر اساس Hash (منبع/مقصد/پورت) تقسیم می‌شود.

``` text
get router info routing-table all
```

#### مثال متوسط — Hash

یک Flow همیشه یک مسیر را می‌رود (برای جلوگیری از جابه‌جایی بسته‌ها). بنابراین یک اتصال بزرگ فقط یک لینک را پر می‌کند.

``` text
Two 1G links ; one 900 Mbps flow -> uses one link ; second link idle
```

#### مثال سخت — فایروال و ECMP

رفت و برگشت ممکن است Hash متفاوت بگیرند ⇒ نامتقارن ⇒ Session قطع. راه: Hash متقارن یا SNAT.

#### Lab

دو مسیر برابر بسازید و توزیع Flowها را مشاهده کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| یک لینک خالی | Hash | Flow بیشتر |
| قطع Session | نامتقارن | SNAT |
| مسیر دوم نیست | هزینه نابرابر | تنظیم |

#### پرسش‌ها با پاسخ

**۱. ECMP؟** مسیر برابر.
**۲. چرا یک Flow یک مسیر؟** ترتیب بسته‌ها.
**۳. خطر برای فایروال؟** نامتقارن.

#### English Corner

- *ECMP balances flows, not packets, so a single large flow uses only one path.*
- Q: Why can ECMP cause trouble for stateful firewalls?

## درس 10-4 — Policy-Based Routing (PBR): مسیریابی بر اساس سیاست با Route-map، Track و Failover

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۸-۱، ۱۰-۱ · ≈ 10 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. PBR را در برابر مسیریابی بر اساس مقصد توضیح دهد و جای آن را در ترتیب پردازش بگوید.
2. ACL، Route-map و `ip policy route-map` را پیکربندی کند.
3. set ip next-hop را با default next-hop، verify-availability و Track مقایسه و درست انتخاب کند.
4. Local PBR را برای ترافیک خود روتر به‌کار ببرد.
5. Verification با `show route-map`، شمارنده و traceroute را اجرا کند.
6. خطاهای رایج (ACL غلط، Next-hop ناقابل‌دسترس، نبود Failover) را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

مسیریابی عادی فقط یک سؤال می‌پرسد: «مقصد کجاست؟». ولی کسب‌وکار سؤال‌های دیگری دارد: «این بسته از واحد مالی است؟ از وب است یا ویدئو؟». اگر ترافیک مالی باید از ISP گران‌قیمت‌تر ولی مطمئن‌تر برود و بقیه از ISP ارزان، مقصد یکی است ولی مسیر باید فرق کند. PBR همین کار را می‌کند: قبل از نگاه به جدول مسیریابی، شرط می‌گذارد و Next-hop را خودش تعیین می‌کند.

چون PBR مسیر را بدون توجه به جدول مسیریابی تغییر می‌دهد، خطرناک هم هست: Next-hop مرده یعنی ترافیک بی‌صدا گم می‌شود. به همین دلیل Track و Failover بخش جدایی‌ناپذیر این درس‌اند.

### ۳) توضیح عمیق فنی

#### ۱) ترتیب پردازش

``` text
packet in (interface with 'ip policy') -> PBR match? 
    yes -> set next-hop/interface  (if next-hop usable)
    no/permit-without-set -> normal routing table
```

PBR روی Interface **ورودی** اعمال می‌شود، نه خروجی.

#### ۲) ساختار

``` text
ip access-list extended FINANCE
 permit ip 10.10.20.0 0.0.0.255 any
!
route-map PBR-FIN permit 10
 match ip address FINANCE
 set ip next-hop verify-availability 192.0.2.1 10 track 1
 set ip next-hop 192.0.2.5
route-map PBR-FIN permit 20
!
ip sla 1
 icmp-echo 192.0.2.1 source-interface GigabitEthernet0/2
 frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability
!
interface GigabitEthernet0/1
 ip policy route-map PBR-FIN
```

- `permit 10` با Match: ترافیک مالی.
- Sequence پایانی (مثلاً `permit 20`) بدون Match و Set اختیاری است و فقط خوانایی می‌دهد: طبق مستند Cisco بسته‌ای که با هیچ Sequence مطابق نشود (یا با `deny` مطابق شود) **Drop نمی‌شود**؛ از PBR خارج و با جدول مسیریابی عادی ارسال می‌شود. (نکته: Route-map بدون `match` روی همه‌ی بسته‌ها `set` را اعمال می‌کند؛ پس Sequence خالی با `set` خطرناک است.)
- اگر Next-hop اول با Track پایین رفت، Next-hop دوم (192.0.2.5) استفاده می‌شود.

#### ۳) next-hop در برابر default next-hop

| دستور | رفتار |
|---|---|
| `set ip next-hop X` | حتی اگر مسیر دقیق در RIB باشد، X را ترجیح می‌دهد |
| `set ip default next-hop X` | فقط وقتی RIB مسیر مشخصی ندارد (غیر از Default) |

#### ۴) Local PBR

``` text
ip local policy route-map LOCAL-PBR
```

برای ترافیکی که خود روتر تولید می‌کند (مثلاً BGP، SNMP).

#### ۵) آزمون

``` text
show route-map PBR-FIN
show ip policy
traceroute 8.8.8.8 source 10.10.20.5
debug ip policy   ! lab only, rate-limited
```

شمارنده‌های `policy routing matches` باید بالا بروند.

#### ۶) PBR و CEF/عملکرد

PBR با CEF روی بسیاری از پلتفرم‌ها سخت‌افزاری است؛ ولی `set` بعضی ویژگی‌ها (مثل `set ip next-hop recursive`) ممکن است ترافیک را به CPU ببرد. `Unverified` روی vIOS.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| next-hop یا default next-hop | default اگر مسیر عادی ترجیح |
| Track | اجباری برای Next-hop خارجی |
| Local PBR | فقط وقتی لازم |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ترافیک 10.10.20.0/24 باید از 192.0.2.1 برود. ورودی: Host 10.10.20.5 به 8.8.8.8. مراحل: ۱) ACL تطبیق. ۲) Next-hop 192.0.2.1. پاسخ: traceroute از 192.0.2.1 عبور می‌کند؛ Host 10.10.30.5 از مسیر عادی.

**متوسط (تحلیل):** PBR اثری ندارد. مراحل: ۱) `show route-map` شمارنده Match=0. ۲) ACL روی subnet اشتباه (10.10.2.0 به‌جای 10.10.20.0). ۳) اصلاح ACL. ۴) شمارنده بالا می‌رود؛ traceroute تأیید.

**سخت (Failover):** لینک ISP-A قطع شد ولی Finance قطع ماند. مراحل: ۱) `set ip next-hop 192.0.2.1` بدون Track. ۲) روتر همچنان ترافیک را به Next-hop مرده می‌فرستد. ۳) افزودن IP SLA+Track و `verify-availability`، Next-hop دوم. ۴) آزمون: قطع لینک، Finance به ISP-B می‌رود (شمارنده‌ها). معیار: Failover < 15 s.

### ۷) پیاده‌سازی از مسیر CLI

``` text
route-map PBR-FIN permit 10
 match ip address FINANCE
 set ip next-hop verify-availability 192.0.2.1 10 track 1
interface Gi0/1
 ip policy route-map PBR-FIN
show route-map PBR-FIN
show ip policy
```

### ۸) Verification (اثبات صحت)

- شمارنده‌ی Match افزایش.
- traceroute مسیر سیاست.
- آزمون Failover.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Match صفر | ACL/Interface ورودی | ACL و ip policy روی Interface درست |
| Failover ندارد | Track | verify-availability |
| ترافیک گم | Next-hop مرده | ARP/Reachability |
| ترافیک غیرمطابق قطع | بررسی Set/Next-hop | Next-hop مرده یا Route-map بدون match؛ نه Drop به‌دلیل نبود sequence |

### ۱۰) نکات امنیتی

- PBR مسیرهای حفاظتی را دور نزند.
- تغییر با CHG و آزمون.

### ۱۱) جمع‌بندی مفهومی

- PBR قبل از RIB.
- Interface ورودی.
- Track و Failover.
- بسته‌ی غیرمطابق با جدول مسیریابی عادی می‌رود.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) PBR بر چه اساسی تصمیم می‌گیرد؟ *(پاسخ: 10-4-ت1)*

**ت2.** (ساده) PBR روی کدام Interface اعمال می‌شود؟ *(پاسخ: 10-4-ت2)*

**ت3.** (متوسط) تفاوت next-hop و default next-hop؟ *(پاسخ: 10-4-ت3)*

**ت4.** (متوسط) بسته‌ای که با هیچ Sequence از Route-map PBR مطابقت نکند چه می‌شود؟ *(پاسخ: 10-4-ت4)*

**ت5.** (سخت) Failover PBR را طراحی کنید. *(پاسخ: 10-4-ت5)*

**ت6.** (سخت، طراحی) PBR برای دو ISP با ریسک‌ها. *(پاسخ: 10-4-ت6)*

**Q1.** Quick quiz (English): What is the purpose of the track keyword with a PBR next hop? *(پاسخ: 10-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PBR | Policy-Based Routing | مسیریابی سیاست‌محور |
| SLA | IP SLA | پایش لینک |

- *PBR overrides destination-based routing.* ← PBR مسیریابی مبتنی بر مقصد را لغو می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** PBR (اجرا نشده). **Evidence:** `03-ops/pbr.md`.

### ۱۵) منابع

- Cisco IOS IP Routing: Policy-Based Routing

<a id="l-10-5"></a>

### تعمیق: PBR تا Failover با اندازه‌گیری و پرسش‌های مصاحبه

**سناریو.** Finance (10.10.20.0/24) باید از ISP-A (Metro) برود و بقیه از ISP-B. اگر A قطع شد Finance به B برود. شمارنده‌ی Match باید قابل اثبات باشد.

**گام ۱ — کامل‌ترین پیکربندی.**

``` text
ip access-list extended FINANCE
 permit ip 10.10.20.0 0.0.0.255 any
ip sla 1
 icmp-echo 192.0.2.1 source-interface GigabitEthernet0/2
 frequency 5
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability
route-map PBR-FIN permit 10
 match ip address FINANCE
 set ip next-hop verify-availability 192.0.2.1 10 track 1
 set ip next-hop 192.0.2.5
interface GigabitEthernet0/1
 ip policy route-map PBR-FIN
```

`source-interface` باعث می‌شود Probe از لینک A برود؛ بدون آن Probe ممکن است از مسیر دیگر بگذرد و Failover کاذب بدهد (مستند Cisco).

**گام ۲ — اثبات.**

``` text
R1# show route-map PBR-FIN
  Policy routing matches: 4821 packets, 5122340 bytes
R1# traceroute 8.8.8.8 source 10.10.20.5     ! via 192.0.2.1
R1# traceroute 8.8.8.8 source 10.10.30.5     ! normal routing table
```

**گام ۳ — Failover.** ISP-A را قطع کنید: `show track 1` ⇒ Down؛ ترافیک Finance به 192.0.2.5 می‌رود؛ شمارنده‌ی Match همچنان بالا می‌رود ولی Next-hop دوم.

**نکته‌ی مهم (مستند Cisco).** بسته‌ای که با Route-map PBR مطابقت نکند یا با `deny` مطابق شود Drop نمی‌شود؛ با جدول مسیریابی عادی ارسال می‌شود. خطر واقعی این است که Sequence بدون `match` با `set` همه‌ی بسته‌ها را مجبور به همان Next-hop می‌کند.

**اشتباهات رایج**
- Policy روی Interface خروجی (باید ورودی).
- Next-hop بدون ARP/Reachability: ترافیک Drop.
- Track روی Gateway به‌جای مقصد دورتر.

**پرسش‌های مصاحبه**
1. *PBR قبل یا بعد از RIB؟* قبل از جستجوی RIB برای بسته‌های مطابق.
2. *تفاوت next-hop و default next-hop؟* default فقط وقتی مسیر مشخص نیست.
3. *Local PBR برای چه؟* ترافیک تولیدشده توسط خود روتر.

### تکمیل عمیق: Policy-Based Routing

#### چرا؟

Routing عادی فقط به مقصد نگاه می‌کند؛ PBR می‌تواند بر اساس منبع، سرویس یا برنامه مسیر را تغییر دهد (مثلاً Voice از لینک A).

#### مثال ساده — Cisco

``` text
access-list 110 permit ip 10.10.1.0 0.0.0.255 any
route-map PBR permit 10
 match ip address 110
 set ip next-hop 198.51.100.1
interface Gi0/1
 ip policy route-map PBR
```

#### مثال متوسط — FortiGate

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.1.0/24"
  set gateway 198.51.100.1
  set output-device "port2"
 next
end
```

بر اساس مستند، اگر هیچ PBR مطابق نباشد، Routing عادی اعمال می‌شود (Drop نمی‌شود).

#### مثال سخت — Next-hop غیرقابل‌دسترس

اگر Next-hop PBR پایین باشد، رفتار به تنظیم بستگی دارد؛ همیشه Verify و Health-check.

#### Lab

یک PBR بسازید و با traceroute مسیر را ببینید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| PBR اعمال نمی‌شود | ACL/ترتیب | بررسی |
| قطع | Next-hop | Monitor |
| برگشت نامتقارن | PBR یک‌طرفه | دو طرفه |

#### پرسش‌ها با پاسخ

**۱. PBR بر چه چیزی؟** منبع/سرویس.
**۲. عدم تطابق؟** Routing عادی.
**۳. خطر؟** نامتقارن.

#### English Corner

- *Policy-based routing overrides the destination-based routing table for matching traffic.*
- Q: What happens when no policy route matches?

## درس 10-5 — VRF-lite: چند جدول مسیریابی مستقل، Overlap آدرس و ارتباط با فایروال

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۱۰-۴ · ≈ 10 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. VRF را (چند RIB/FIB مستقل) توضیح دهد.
2. VRF-lite با Interface، RD و مسیر مستقل را پیکربندی کند.
3. Overlap آدرس بین مشتریان را مدیریت کند.
4. ping/traceroute/OSPF را در VRF اجرا کند.
5. VRF را با فایروال (Zone/VDOM) هم‌ساز کند.
6. خطاهای رایج (پاک‌شدن IP، نبود vrf در دستور) را رفع کند.

### ۲) مفهوم پایه: چیست و چرا؟

ساختمانی دارید با دو شرکت مستأجر که هر دو شبکه‌ی 192.168.1.0/24 دارند و نباید یکدیگر را ببینند. اگر یک روتر فیزیکی بخرید برای هرکدام، هزینه و فضا هدر می‌رود. VRF روی همان روتر «چند روتر مجازی» می‌سازد؛ هر کدام جدول مسیریابی مستقل دارند و آدرس‌ها می‌توانند تکراری باشند.

### ۳) توضیح عمیق فنی

#### ۱) پیکربندی

``` text
ip vrf CUST-A
 rd 65000:1
ip vrf CUST-B
 rd 65000:2
!
interface GigabitEthernet0/1
 ip vrf forwarding CUST-A
 ip address 192.168.1.1 255.255.255.0
interface GigabitEthernet0/2
 ip vrf forwarding CUST-B
 ip address 192.168.1.1 255.255.255.0
```

دستور `ip vrf forwarding` آدرس Interface را پاک می‌کند (پیام «IPv4 disabled and address(es) removed due to disabling VRF»): اول forwarding بعد IP. نکته: در IOS-XE جدید سینتکس `vrf definition` و `vrf forwarding` ترجیح داده می‌شود و `ip vrf` قدیمی است (طبق مستند Cisco).

#### ۲) مسیریابی

``` text
ip route vrf CUST-A 0.0.0.0 0.0.0.0 10.0.0.1
router ospf 10 vrf CUST-A
 network 192.168.1.0 0.0.0.255 area 0
```

#### ۳) تست

``` text
show ip vrf
show ip route vrf CUST-A
ping vrf CUST-A 192.168.1.2
traceroute vrf CUST-A 8.8.8.8
```

بدون `vrf` به جدول Global می‌رود: شایع‌ترین «ping کار نمی‌کند».

#### ۴) VRF و فایروال

هر VRF یک لینک (یا VLAN) به فایروال؛ فایروال برای هر VRF Zone یا VDOM جدا. جداسازی VRF خودش سیاست امنیتی نیست؛ فقط RIB را جدا می‌کند و Policy فایروال لازم است.

#### ۵) Route Leaking

برای ارتباط کنترل‌شده (مثلاً سرویس مشترک) بین VRFها: درس ۱۰-۸.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| VRF-lite یا MPLS VRF | داخلی: lite |
| RD | یکتا |
| فایروال | Zone/VDOM هر VRF |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** CUST-A و B هر دو 192.168.1.0/24: ping vrf CUST-A 192.168.1.2 فقط Hostهای A را می‌بیند.

**متوسط (تحلیل):** `ping 192.168.1.2` از روتر جواب نمی‌دهد. علت: بدون vrf در جدول Global اجرا شده؛ رفع: `ping vrf CUST-A`.

**سخت (طراحی):** سه مشتری با اینترنت مشترک: ۱) سه VRF. ۲) Default هر VRF به Interface فایروال جدا. ۳) NAT جدا برای هر مشتری. ۴) آزمون: A به B نمی‌رسد؛ A به اینترنت می‌رسد. ۵) Log. ریسک: Leak ناخواسته. معیار: آزمون منفی A→B رد.

### ۷) پیاده‌سازی از مسیر CLI

``` text
ip vrf CUST-A
 rd 65000:1
interface Gi0/1
 ip vrf forwarding CUST-A
 ip address 192.168.1.1 255.255.255.0
show ip route vrf CUST-A
ping vrf CUST-A 192.168.1.2
```

### ۸) Verification (اثبات صحت)

- RIB جدا.
- ping vrf.
- نبود نشت.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| آدرس پاک شد | ترتیب دستور | IP را دوباره بزنید |
| ping ناموفق | بدون vrf | ping vrf |
| نشت | Leak/Static | حذف |

### ۱۰) نکات امنیتی

- VRF امنیت کامل نیست؛ Policy فایروال لازم است.

### ۱۱) جمع‌بندی مفهومی

- VRF=چند RIB.
- Overlap.
- ping vrf.
- فایروال لازم.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) VRF چیست؟ *(پاسخ: 10-5-ت1)*

**ت2.** (ساده) چرا IP هنگام forwarding پاک می‌شود؟ *(پاسخ: 10-5-ت2)*

**ت3.** (متوسط) چگونه ping کنید؟ *(پاسخ: 10-5-ت3)*

**ت4.** (متوسط) RD چیست؟ *(پاسخ: 10-5-ت4)*

**ت5.** (سخت) سه مشتری با اینترنت مشترک. *(پاسخ: 10-5-ت5)*

**ت6.** (سخت، طراحی) جداسازی با فایروال. *(پاسخ: 10-5-ت6)*

**Q1.** Quick quiz (English): What does VRF-lite provide? *(پاسخ: 10-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VRF | Virtual Routing and Forwarding | مسیریابی مجازی |
| RD | Route Distinguisher | تمایزدهنده‌ی مسیر |

- *VRF separates routing tables.* ← VRF جدول‌های مسیریابی را جدا می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** VRF (اجرا نشده). **Evidence:** `03-ops/vrf.md`.

### ۱۵) منابع

- Cisco VRF-lite configuration guide

<a id="l-10-6"></a>

### تعمیق: طراحی VRF-lite برای سه مشتری با آدرس تکراری

**سناریو.** دو مشتری (A و B) هر دو 192.168.1.0/24 دارند؛ مشتری C 10.5.0.0/16. همه از یک روتر و یک فایروال اینترنت می‌گیرند.

**گام ۱ — VRFها و Interfaceها.**

``` text
ip vrf CUST-A
 rd 65000:1
ip vrf CUST-B
 rd 65000:2
ip vrf CUST-C
 rd 65000:3
interface Gi0/1
 ip vrf forwarding CUST-A
 ip address 192.168.1.1 255.255.255.0
interface Gi0/2
 ip vrf forwarding CUST-B
 ip address 192.168.1.1 255.255.255.0
interface Gi0/3
 ip vrf forwarding CUST-C
 ip address 10.5.0.1 255.255.0.0
```

یادآوری مستند: `ip vrf forwarding` IP قبلی Interface را پاک می‌کند؛ ترتیب forwarding سپس address. در IOS-XE جدید سینتکس `vrf definition` + `vrf forwarding` است.

**گام ۲ — خروج هر VRF به فایروال (Zone جدا).**

``` text
interface Gi0/4.101
 encapsulation dot1Q 101
 ip vrf forwarding CUST-A
 ip address 10.255.101.1 255.255.255.252
interface Gi0/4.102
 encapsulation dot1Q 102
 ip vrf forwarding CUST-B
 ip address 10.255.102.1 255.255.255.252
ip route vrf CUST-A 0.0.0.0 0.0.0.0 10.255.101.2
ip route vrf CUST-B 0.0.0.0 0.0.0.0 10.255.102.2
```

در فایروال دو Zone/VDOM و NAT مجزا (هر مشتری Pool خودش)؛ چون هر دو مشتری 192.168.1.0/24 دارند، NAT قبل از خروج لازم است.

**گام ۳ — Verification.**

``` text
show ip vrf
show ip route vrf CUST-A
ping vrf CUST-A 192.168.1.2
show ip arp vrf CUST-B
```

**گام ۴ — آزمون منفی.** از Host مشتری A به 192.168.1.2 (که فقط در B وجود دارد) پینگ کنید: باید به Host خودِ A برسد یا Timeout شود، نه به B. و `ping vrf CUST-A 10.5.0.5` (مشتری C) باید شکست بخورد.

**اشتباهات رایج**
- `ping` بدون `vrf`.
- فراموشی Default Route در VRF.
- Route Leak ناخواسته با Static یا Import/Export اشتباه.

**پرسش‌های مصاحبه**
1. *VRF-lite در برابر MPLS VRF؟* lite بدون MPLS و RD/RT مبتنی بر BGP؛ مقیاس کوچک‌تر.
2. *RD چه کاری می‌کند؟* Prefixهای هم‌آدرس را در BGP/VPNv4 یکتا می‌کند.
3. *آیا VRF امنیت است؟* جداسازی مسیریابی است؛ سیاست فایروال هم لازم است.

### تکمیل عمیق: VRF-lite و Overlap آدرس

#### چرا؟

دو مشتری هر دو 10.1.1.0/24 دارند؛ بدون جداسازی مسیر، تداخل است. VRF (Virtual Routing and Forwarding) جدول مسیر مستقل می‌دهد.

#### مثال ساده

``` text
ip vrf CUST-A
ip vrf CUST-B
interface Gi0/1
 ip vrf forwarding CUST-A
 ip address 10.1.1.1 255.255.255.0
interface Gi0/2
 ip vrf forwarding CUST-B
 ip address 10.1.1.1 255.255.255.0
```

هر دو آدرس یکسان بدون تداخل.

#### مثال متوسط — بررسی

``` text
show ip route vrf CUST-A
ping vrf CUST-A 10.1.1.5
```

#### مثال سخت — پروتکل در VRF

OSPF/BGP باید در هر VRF جدا اجرا شود (`router ospf 1 vrf CUST-A`)؛ فراموشی باعث «مسیر نیست».

#### معادل FortiGate

VDOM (جدا کننده‌ی بیشتر) یا VRF در FortiOS 7.x (محدود). مقایسه تقریبی است.

#### Lab

دو VRF با آدرس یکسان بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| ping نه | VRF نادرست | `vrf` |
| مسیر نیست | پروتکل | در VRF |
| نشت | Leak ناخواسته | بررسی |

#### پرسش‌ها با پاسخ

**۱. VRF چیست؟** جدول مسیر مجازی.
**۲. Overlap؟** مجاز در VRF جدا.
**۳. VRF=VDOM؟** نه دقیقاً.

#### English Corner

- *VRFs allow overlapping address space by separating routing tables.*
- Q: What must you remember when running a routing protocol in a VRF?

## درس 10-6 — Asymmetric Routing: تحلیل رفت و برگشت، اثر بر فایروال و راه‌حل‌ها

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۳، ۱۱-۱، ۱۱-۳ · ≈ 10 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Asymmetric Routing را تعریف و علت‌های رایج را بشمارد.
2. اثر آن بر Stateful Firewall را دقیق توضیح دهد.
3. با traceroute و Capture دو سویه آن را ثابت کند.
4. راه‌حل‌ها (طراحی Symmetric، Policy، Session-pickup، disable check) را مقایسه کند.
5. رفع را اجرا و آزمون کند.
6. طراحی را برای ECMP و چند ISP بازبینی کند.

### ۲) مفهوم پایه: چیست و چرا؟

نامه‌ای را از پست‌خانه‌ی A می‌فرستید ولی جوابش از پست‌خانه‌ی B می‌آید. اگر پست‌خانه‌ی B ثبت نکرده باشد که این نامه جواب کدام درخواست است، آن را دور می‌اندازد. فایروال Stateful دقیقاً همین رفتار را دارد: «Session ندیدم، پس بسته‌ی برگشت را نمی‌پذیرم». ولی لینک‌ها سالم‌اند و کاربر فقط می‌گوید «سایت باز نمی‌شود».

### ۳) توضیح عمیق فنی

#### ۱) علل رایج

- ECMP/Per-packet بین دو فایروال.
- دو ISP با Policy ورودی/خروجی متفاوت (Local-pref در برابر Prepend).
- Redistribution/Route-map ناهمگون.
- HA/Cluster نادرست.
- NAT متفاوت در دو مسیر.

#### ۲) اثر بر فایروال

``` text
Client -> FW1 -> Server       (SYN, FW1 creates session)
Server -> FW2 -> Client       (SYN-ACK arrives at FW2: "no session matched" -> DROP)
```

Stateless: مشکلی ندارد.

#### ۳) اثبات

``` text
FW1 capture: SYN present, no SYN-ACK
FW2 capture: SYN-ACK present, no SYN
traceroute from both ends shows different hops
```

#### ۴) راه‌حل‌ها

| روش | توضیح | ریسک |
|---|---|---|
| طراحی Symmetric | Local-pref/Weight/PBR تا هر دو جهت از یک FW | کمترین |
| Session-pickup/Sync | FGCP Session sync بین Cluster | تأخیر |
| Policy Route | هر جریان را به یک فایروال | پیچیدگی |
| `asymroute enable` | فایروال اجازه‌ی بسته‌ی برگشت بدون SYN | ضعیف‌شدن امنیت |

#### ۵) آزمون

بعد از رفع: ping/TCP، `diagnose sys session list` روی یک فایروال، و Failover قطع لینک.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Symmetric یا Sync | Symmetric ترجیح |
| asymroute | نه (فقط موقت) |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Capture: FW1 فقط SYN، FW2 فقط SYN-ACK ⇒ Asymmetric.

**متوسط (تحلیل):** ISP2 برگشت را از لینک دوم می‌آورد. مراحل: ۱) BGP Local-pref برای خروج ISP1. ۲) Prepend برای ورود. ۳) آزمون traceroute. نتیجه: هر دو جهت از ISP1.

**سخت (Active-Active):** Cluster با Session sync؛ مراحل: ۱) فعال‌سازی session-pickup. ۲) آزمون قطع FW1: Sessionها در FW2 می‌مانند. ۳) اندازه‌گیری Delay. ریسک: Sync تأخیر؛ جایگزین: Active-Standby. معیار: صفر قطع Session.

### ۷) پیاده‌سازی از مسیر CLI

``` text
traceroute 10.20.0.5
show ip route 10.20.0.5
! FortiGate (Unverified): diagnose sniffer packet any "host 10.20.0.5" 4
```

### ۸) Verification (اثبات صحت)

- Capture دو سویه.
- Session روی یک FW.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| برخی Session قطع | Capture | Symmetric/Policy |
| فقط پورت‌های خاص | Hash | ECMP |

### ۱۰) نکات امنیتی

- asymroute امنیت را کم می‌کند.

### ۱۱) جمع‌بندی مفهومی

- Asymmetric=Drop در Stateful.
- Capture اثبات.
- Symmetric ترجیح.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Asymmetric یعنی؟ *(پاسخ: 10-6-ت1)*

**ت2.** (ساده) چرا Stateful Drop می‌کند؟ *(پاسخ: 10-6-ت2)*

**ت3.** (متوسط) سه علت؟ *(پاسخ: 10-6-ت3)*

**ت4.** (متوسط) چگونه ثابت کنیم؟ *(پاسخ: 10-6-ت4)*

**ت5.** (سخت) راه‌حل سازمان. *(پاسخ: 10-6-ت5)*

**ت6.** (سخت، طراحی) Active-Active. *(پاسخ: 10-6-ت6)*

**Q1.** Quick quiz (English): Why do stateful firewalls drop asymmetric flows? *(پاسخ: 10-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Asymmetric | Asymmetric routing | مسیر نامتقارن |

- *Asymmetric paths break stateful inspection.* ← مسیر نامتقارن بازرسی حالت‌دار را خراب می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** Asymmetric (اجرا نشده). **Evidence:** `03-ops/asym.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0: Asymmetric routing

<a id="l-10-7"></a>

### تعمیق: اثبات Asymmetric با Capture دو سمتی و سه راه‌حل

**سناریو.** دو ISP با Local-pref متفاوت برای خروج و Prepend برای ورود؛ دو فایروال FW1 و FW2. کاربر می‌گوید «سایت X باز می‌شود ولی نصف مواقع قطع».

**گام ۱ — ثبت Capture هم‌زمان.** روی هر دو فایروال با فیلتر Host:

``` text
FW1: diagnose sniffer packet any 'host 203.0.113.50 and tcp port 443' 4 20 l
FW2: diagnose sniffer packet any 'host 203.0.113.50 and tcp port 443' 4 20 l
```

**نتیجه:** FW1 فقط `SYN` را می‌بیند؛ FW2 فقط `SYN, ACK` و `ACK` را. FW2 برای SYN-ACK Session ندارد ⇒ Drop. اگر FortiGate است در Debug flow: `no session matched` یا `reverse path check fail`.

**گام ۲ — علت.** مسیر ورود از ISP-B است (Prepend کار نکرد) در حالی که خروج از A است.

**گام ۳ — سه راه‌حل با ریسک**

| راه | کار | ریسک |
|---|---|---|
| طراحی Symmetric | Local-pref + اصلاح اعلام BGP تا ورود هم از A | نتیجه‌ی ورود تضمینی نیست |
| Session sync (Cluster) | FGCP/FGSP | پیچیدگی و Delay |
| `asymroute enable` | پذیرش بسته‌ی بدون SYN | امنیت کم، فقط موقت |

**گام ۴ — آزمون پس از رفع.** سه بار Capture؛ هر دو جهت در یک فایروال؛ Sessionها پایدار؛ آزمون قطع A و Failover.

**نکته‌ی عملی:** Asymmetric همیشه خطا نیست؛ در Stateless یا با FGSP کار می‌کند؛ مشکل با Stateful بدون Sync است.

**اشتباهات رایج**
- Capture فقط روی یک فایروال.
- حل با `asymroute` و فراموشی آن.
- تصور اینکه Prepend ورود را تضمین می‌کند.

**پرسش‌های مصاحبه**
1. *سه علت Asymmetric؟* ECMP، دو ISP با Policy متفاوت، Redistribution ناهمگون.
2. *چرا Stateless مشکل ندارد؟* هر بسته مستقل بررسی می‌شود.
3. *FGSP چیست؟* Session sync بین فایروال‌های مستقل (غیر Cluster) برای Asymmetric.

### تکمیل عمیق: Asymmetric Routing — اثر بر فایروال

#### چرا؟

مسیر نامتقارن برای روتر مشکل نیست، ولی برای فایروال Stateful مرگبار است. این درس رفت و برگشت را تحلیل می‌کند.

#### مثال ساده

``` text
Client -> R1 -> FW-A -> Server
Server -> R2 -> FW-B -> Client
```

FW-B فقط SYN-ACK را می‌بیند ⇒ Session ندارد ⇒ Drop.

#### مثال متوسط — علل

دو ISP، ECMP، Policy Route، Multi-homed server.

#### مثال سخت — شواهد

Sniffer هم‌زمان روی دو فایروال: هر کدام فقط یک جهت. راه‌حل: متقارن‌سازی، SNAT، یا Session Sync.

#### Lab

یک توپولوژی دو مسیره بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| SYN-ACK Drop | نامتقارن | SNAT/طراحی |
| متناوب | ECMP | Hash |
| فقط یک کاربر | Policy Route | تصحیح |

#### پرسش‌ها با پاسخ

**۱. چرا فایروال مشکل دارد؟** Session.
**۲. شاهد؟** Sniffer دوطرفه.
**۳. راه‌حل اول؟** متقارن‌سازی.

#### English Corner

- *Asymmetric paths are harmless for routers but break stateful inspection.*
- Q: How do you prove a flow is asymmetric?

## درس 10-7 — طراحی مسیر چندفایروالی و آزمون جامع فصل ۱۰: پروژه‌ی حل‌شده‌ی کامل

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۱ تا ۱۰-۶ · ≈ 12 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. طرح مسیر سازمان دوفایروالی با دو ISP را با BGP/OSPF/Static کامل بنویسد.
2. هر تصمیم (Redistribution، ECMP، PBR، VRF، NAT) را توجیه کند.
3. پیکربندی نمونه‌ی هر گره را تهیه کند.
4. آزمون پنج‌گانه‌ی مثبت/منفی را با شواهد اجرا کند.
5. ریسک‌ها و Rollback را مستند کند.

### ۲) مفهوم پایه: چیست و چرا؟

این درس نتیجه‌ی فصل ۱۰ است: به‌جای مفاهیم جدا، یک پروژه‌ی کامل را از نیازمندی تا آزمون پیش می‌بریم. نیازمندی: دو ISP، ترافیک مالی از ISP-A با Failover، بقیه از ISP-B، شبکه‌ی مهمان جدا، و بدون مسیر نامتقارن روی فایروال‌های Stateful.

### ۳) توضیح عمیق فنی

#### ۱) نیازمندی

1. اینترنت پایدار با دو ISP.
2. Finance (10.10.20.0/24) ترجیحاً ISP-A، Failover به B.
3. مهمان (192.168.50.0/24) فقط اینترنت؛ بدون دسترسی داخلی.
4. NAT فقط روی Edge.
5. بدون Asymmetric.

#### ۲) طرح

``` text
ISP-A ---BGP---+                         +--- Internal FW --- Servers
               +-- EDGE FW (HA) -- Core(OSPF) --- Users
ISP-B ---BGP---+                         +--- VRF GUEST --- Guest
```

#### ۳) پیکربندی نمونه Edge

``` text
router bgp 65010
 neighbor 192.0.2.1 remote-as 65100
 neighbor 192.0.2.1 route-map FROM-A in
 neighbor 192.0.2.5 remote-as 65200
 neighbor 192.0.2.5 route-map FROM-B in
 neighbor 192.0.2.5 route-map TO-B out
route-map FROM-A permit 10
 set local-preference 200
route-map FROM-B permit 10
 set local-preference 100
route-map TO-B permit 10
 set as-path prepend 65010 65010
router ospf 1
 default-information originate always
```

#### ۴) PBR و Track روی Core

``` text
route-map PBR-FIN permit 10
 match ip address FINANCE
 set ip next-hop verify-availability 192.0.2.1 10 track 1
```

#### ۵) VRF مهمان

``` text
ip vrf GUEST
interface Gi0/5
 ip vrf forwarding GUEST
 ip address 192.168.50.1 255.255.255.0
ip route vrf GUEST 0.0.0.0 0.0.0.0 10.255.9.2
```

#### ۶) آزمون پنج‌گانه

| # | آزمون | انتظار |
|---|---|---|
| 1 | traceroute Users→8.8.8.8 | از ISP-B (Local-pref پایین‌تر برای عادی؟ طبق طرح) |
| 2 | Finance→8.8.8.8 | از ISP-A |
| 3 | قطع ISP-A | Finance به B؛ Failover<15s |
| 4 | Guest→Servers | رد |
| 5 | Capture دو سمت | بدون Asymmetric |

#### ۷) ریسک

Next-hop مرده در PBR (Track)؛ Leak بین VRF؛ Prepend بی‌اثر؛ Rollback: Config قبلی.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Users→Internet: Local-pref 200 برای A و Policy؛ نتیجه traceroute.

**متوسط (Failover):** قطع ISP-A: Track پایین؛ Next-hop دوم؛ شمارنده‌ها؛ مدت Failover اندازه‌گیری شد (۱۲ ثانیه).

**سخت (Asymmetric):** پس از افزودن لینک دوم Capture نشان داد SYN از FW1 و SYN-ACK از FW2؛ رفع: Local-pref/Prepend و Policy؛ آزمون تکرار: Symmetric.

### ۷) پیاده‌سازی از مسیر CLI

``` text
show ip bgp summary
show route-map PBR-FIN
show ip route vrf GUEST
traceroute 8.8.8.8 source 10.10.20.5
```

### ۸) Verification (اثبات صحت)

- آزمون پنج‌گانه.
- Evidence.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Failover کند | Track interval | BFD/کاهش interval |
| Guest به داخل می‌رسد | Leak | حذف Static |

### ۱۰) نکات امنیتی

- VRF+Policy فایروال.

### ۱۱) جمع‌بندی مفهومی

- پروژه‌ی کامل.
- آزمون مثبت/منفی.
- ریسک و Rollback.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا NAT فقط Edge؟ *(پاسخ: 10-7-ت1)*

**ت2.** (ساده) نقش Local-pref؟ *(پاسخ: 10-7-ت2)*

**ت3.** (متوسط) چرا Track در PBR؟ *(پاسخ: 10-7-ت3)*

**ت4.** (متوسط) Guest را چگونه جدا کردید؟ *(پاسخ: 10-7-ت4)*

**ت5.** (سخت) Asymmetric پس از لینک دوم؛ تحلیل. *(پاسخ: 10-7-ت5)*

**ت6.** (سخت، طراحی) طرح را برای سه ISP گسترش دهید. *(پاسخ: 10-7-ت6)*

**Q1.** Quick quiz (English): Which tool ensures PBR stops using a dead next hop? *(پاسخ: 10-7-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HA | High Availability | دسترس‌پذیری بالا |

- *Test negative cases as well as positive ones.* ← علاوه بر مثبت، حالت‌های منفی را هم آزمون کنید.

### ۱۴) کارت Lab

**کارت Lab:** پروژه‌ی فصل ۱۰ (اجرا نشده). **Evidence:** `03-ops/multi-fw.md`.

### ۱۵) منابع

- درس‌های ۱۰-۱ تا ۱۰-۶

### تعمیق: پیکربندی نمونه‌ی کامل Edge و آزمون Failover با اندازه‌گیری

**هدف.** پروژه‌ی جامع فصل ۱۰ را اجرایی کنیم: BGP دو ISP، OSPF داخلی، PBR Finance با Track و VRF مهمان.

**گام ۱ — BGP Edge.**

``` text
router bgp 65010
 bgp log-neighbor-changes
 neighbor 192.0.2.1 remote-as 65100
 neighbor 192.0.2.1 prefix-list BOGONS in
 neighbor 192.0.2.1 route-map FROM-A in
 neighbor 192.0.2.5 remote-as 65200
 neighbor 192.0.2.5 prefix-list BOGONS in
 neighbor 192.0.2.5 route-map FROM-B in
 network 203.0.113.0 mask 255.255.255.0
ip route 203.0.113.0 255.255.255.0 Null0
route-map FROM-A permit 10
 set local-preference 200
route-map FROM-B permit 10
 set local-preference 100
```

**گام ۲ — OSPF.** Default داخل OSPF فقط وقتی BGP Default دارد (Track): `default-information originate` بدون `always`.

**گام ۳ — Finance با PBR** (درس ۱۰-۴) و **مهمان در VRF** (درس ۱۰-۵).

**گام ۴ — جدول آزمون و Evidence**

| # | آزمون | روش | معیار |
|---|---|---|---|
| 1 | Users→Internet | traceroute | از ISP-A (Local-pref 200) |
| 2 | Finance→Internet | traceroute با Source | از ISP-A و شمارنده‌ی PBR بالا |
| 3 | قطع ISP-A | shutdown Session | Failover < 15 s، Finance به B |
| 4 | Guest→Servers | ping vrf | شکست |
| 5 | Asymmetric | Capture دو سمتی | بدون SYN-ACK بی‌SYN |

**گام ۵ — اندازه‌گیری Failover.** ping پیوسته ۲۰۰ms:

``` text
lost packets x 0.2 s = outage seconds
example: 62 lost x 0.2 = 12.4 s
```

اگر > ۱۵ ثانیه: BFD و کاهش interval Track.

**ریسک‌ها:** Next-hop مرده در PBR (Track)، Leak بین VRF (آزمون منفی)، Prepend بی‌اثر (اندازه‌گیری ورودی)، نبود Alert روی Neighbor Down.

**پرسش‌های مصاحبه**
1. *چرا Default داخل OSPF بدون `always`؟* تا وقتی Edge خروجی ندارد Default را اعلام نکند (Black-hole).
2. *Failover را چطور سریع می‌کنید؟* BFD برای BGP/OSPF و Track با Interval کوچک.
3. *گزارش پروژه چه دارد؟* طرح، Configها بدون رمز، Evidence Index، ریسک و Rollback.

### تکمیل عمیق: طراحی مسیر چندفایروالی و آزمون جامع

#### چرا؟

این درس ترکیب مفاهیم فصل است: مسیر، Redistribution، ECMP، PBR و فایروال.

#### مثال ساده — طراحی

``` text
Branch -> Edge FW pair (ECMP) -> ISP A/B
SNAT to egress interface IP so return path = forward path
```

#### مثال متوسط — آزمون

قطع یک لینک؛ ping مداوم؛ شمارش Loss.

#### مثال سخت — خرابی تزریقی

Redistribution حلقه + نامتقارن: ابتدا Tag، سپس SNAT.

#### Rubric

``` text
Design 25 | Routing 25 | Failover 25 | Evidence 15 | Report 10
```

#### Lab

آزمون را اجرا کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| حلقه | Redistribution | Tag |
| Drop | نامتقارن | SNAT |
| Failover کند | Timer | BFD |

#### پرسش‌ها با پاسخ

**۱. چرا SNAT؟** برگشت از همان.
**۲. چرا Tag؟** حلقه.
**۳. شاهد Failover؟** ping.

#### English Corner

- *Source NAT to the egress interface keeps return traffic on the same firewall.*
- Q: What is the first fix for a redistribution loop?

## درس 10-8 — Route Leaking میان VRFها و جدول Global: طراحی کنترل‌شده

**فصل ۱۰ · درس افزوده (تکمیل ۱۰-۵) · پیش‌نیاز: درس‌های ۱۰-۱ تا ۱۰-۵ · ≈ ۶ ساعت**

> **وضعیت:** مفهومی با مثال VRF-lite؛ ویژگی‌های Leaking بسته به پلتفرم فرق دارد (IOS vs IOS-XE vs CSR)؛ Lab «اجرا نشده»؛ برخی دستورها `Unverified` روی vIOS.

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. توضیح دهد VRF چه چیزی را جدا می‌کند و چرا «جداسازی کامل» گاهی باید به‌طور کنترل‌شده شکسته شود.
2. روش‌های Route Leaking را بشناسد و میان آن‌ها بر اساس نیاز انتخاب کند.
3. خطرهای امنیتی و عملیاتی Leaking را نام ببرد (دور زدن فایروال، Overlap، Asymmetric).
4. برای یک سناریوی واقعی (سرویس مشترک مثل DNS/NTP/فایروال) طرح Leaking بنویسد و آن را آزمایش کند.
5. پیوند VRF با Zone و VDOM در FortiGate را بفهمد (فصل ۲۴).

### ۲) پیش‌نیازها

VRF-lite (۱۰-۵)، Static Route و Recursive Lookup (۵-۰، ۵-۲)، Redistribution (۱۰-۱).

### ۳) مفهوم پایه: چرا VRF و چرا Leak؟

**VRF (Virtual Routing and Forwarding)** یک جدول مسیریابی مستقل است. ترافیک VRF-A نمی‌تواند به شبکه‌های VRF-B برسد، حتی اگر IPها هم‌پوشانی داشته باشند. کاربرد: Multi-tenant، جداسازی Guest از Corporate، سرویس‌دهی به چند مشتری.

اما در عمل **سرویس‌های مشترک** هست: DNS، NTP، Monitoring، Update Server، یا فایروال مشترک در لبه. دو راه داریم:

1. **عبور از بیرون (Firewall/Router خارجی):** ترافیک VRFها از یک فایروال بیرونی می‌گذرد (امن‌تر، قابل‌بازرسی).
2. **Route Leaking:** مسیرهای مشخصی را عمداً میان جداول کپی کنیم.

Leak یعنی در جدول A یک Route برای شبکه‌ای در B قرار دهیم (و برعکس برای برگشت). ابزار: Static Route با اشاره به VRF دیگر، یا (در پلتفرم‌های MPLS) Route-Target Import/Export.

> **قانون طلایی:** Leak همیشه باید **حداقلی** (Prefix مشخص، نه شبکه‌ی کامل)، **دوطرفه** (رفت و برگشت) و **قابل‌کنترل** (ACL/Firewall) باشد.

### ۴) توضیح عمیق فنی

#### ۴-۱) روش‌های Leak

| روش | سازوکار | پلتفرم | مزیت/ریسک |
|---|---|---|---|
| Static با `global` | `ip route vrf A <prefix> <mask> <next-hop> global` | IOS/IOS-XE | ساده؛ Next-hop باید در Global قابل‌دسترس باشد |
| Static به Interface | `ip route vrf A <prefix> <mask> <interface> <next-hop>` | IOS/IOS-XE | ساده؛ دقیق |
| Route-Target Import/Export | `route-target import/export` در تعریف VRF (VRF با MPLS-VPN/Multi-Protocol BGP) | IOS-XE (VRF-aware) | مقیاس‌پذیر؛ نیاز به BGP |
| Inter-VRF فایروال | ترافیک از فایروال بیرونی می‌گذرد | هر | امن‌ترین؛ تأخیر بیشتر |
| VRF-aware ACL | محدود کردن عبور | IOS | تکمیل Leak؛ کافی نیست |

(در Lab فقط VRF-lite + Static تمرین می‌شود؛ Route-Target نیاز به MPLS/BGP دارد و خارج از دامنه است.)

#### ۴-۲) نیاز به مسیر برگشت

Leak یک‌طرفه کار نمی‌کند: بسته به مقصد می‌رسد ولی پاسخ مسیر برگشت ندارد (Asymmetric/Drop). پس همیشه **دو Route** لازم است: A→B و B→A.

#### ۴-۳) پیامدهای Leak

- **دور زدن Policy:** اگر VRF مهمان را به VRF سازمانی Leak کنیم، فایروال میانی دیگر عبور را کنترل نمی‌کند.
- **Overlap:** اگر آدرس‌ها هم‌پوشان باشند، Leak ممکن نیست (یا نیاز به NAT).
- **Route ناخواسته:** Leak یک Prefix بزرگ (مثلاً 10.0.0.0/8) همه‌چیز را باز می‌کند.
- **عیب‌یابی پیچیده‌تر:** Route در جدول دیگری است؛ `show ip route vrf X` را فراموش نکنید.

### ۵) مثال حل‌شده

**شرایط:** دو VRF: CORP و GUEST. سرور DNS در VRF SHARED (10.99.0.53). باید هر دو VRF فقط به DNS و نه به هم برسند.

``` text
ip vrf SHARED
ip vrf CORP
ip vrf GUEST

! Leak DNS server host route into CORP and GUEST
ip route vrf CORP  10.99.0.53 255.255.255.255 10.99.0.1 global
ip route vrf GUEST 10.99.0.53 255.255.255.255 10.99.0.1 global

! Return routes in SHARED
ip route vrf SHARED 10.10.0.0 255.255.0.0 10.10.255.1
ip route vrf SHARED 10.20.0.0 255.255.0.0 10.20.255.1
```

**تحلیل:**

- فقط Host Route (/32) سرور DNS leak شده؛ CORP و GUEST به هم دسترسی ندارند.
- برگشت: SHARED باید Subnet هر VRF را بشناسد؛ برای کنترل بیشتر ACL روی Interface بگذارید.

**آزمون‌ها:**

``` text
R1# show ip route vrf CORP
R1# show ip route vrf SHARED
R1# ping vrf CORP 10.99.0.53 source 10.10.1.1
R1# ping vrf GUEST 10.10.1.1
```

آخرین دستور باید **شکست بخورد** (GUEST نباید CORP را ببیند)؛ شکست = اثبات جداسازی.

**مثال سخت:** مدیر سهواً `ip route vrf GUEST 10.0.0.0 255.0.0.0 ... global` نوشته و Guest به شبکه‌ی داخلی دسترسی پیدا کرده است. سه شاهد برای کشف: `show ip route vrf GUEST` (مسیر بزرگ)، `ping vrf GUEST` به یک Host داخلی (موفق)، و بررسی `show running-config | include ip route vrf`. راه‌حل: حذف Route بزرگ، Leak فقط /32، افزودن ACL.

### ۶) طراحی و تصمیم‌گیری

| سؤال | گزینه | معیار |
|---|---|---|
| Leak یا فایروال؟ | Leak / فایروال | اگر ترافیک نیاز به بازرسی/Log دارد: فایروال |
| چه Prefixی؟ | /32 سرویس | حداقل سطح تماس |
| تکرار یا مرکزی؟ | Leak هر VRF | با تعداد VRF زیاد، فایروال/سرویس مرکزی |
| مستندسازی | جدول Leak (Prefix، جهت، دلیل، مسئول) | الزامی |

در **FortiGate** هم همین منطق به شکل Zone/VDOM است: ترافیک بین Zoneها از Policy می‌گذرد؛ بین VDOMها فقط از Inter-VDOM Link (فصل ۲۴). پس ترجیح طراحی «عبور از فایروال» است، نه Leak مستقیم.

### ۷) پیاده‌سازی و Verification

``` text
R1# show ip vrf
R1# show ip route vrf CORP
R1# show ip route vrf SHARED
R1# show ip cef vrf CORP 10.99.0.53
R1# traceroute vrf CORP 10.99.0.53
R1# show running-config | include ip route vrf
```

بعد از هر Leak، **دو آزمون** انجام دهید: مثبت (دسترسی مجاز موفق) و منفی (دسترسی غیرمجاز شکست).

### ۸) Troubleshooting

| علامت | شاهد | علت محتمل |
|---|---|---|
| Leak کار نمی‌کند | `show ip route vrf X` | Route نصب نشده (Next-hop نامعتبر) |
| ارسال هست، پاسخ نه | `show ip route vrf Y` | مسیر برگشت ندارد |
| دسترسی غیرمنتظره | `show ip route vrf` مسیرهای بزرگ | Leak بیش‌ازحد |
| آدرس هم‌پوشان | traceroute | Overlap؛ NAT یا طراحی دوباره |

### ۹) نکات امنیتی

- هر Leak یک «سوراخ در دیوار» است؛ مستند و بازبینی‌شده باشد.
- Leak به Guest را فقط برای سرویس‌های ضروری (DNS) و با ACL.
- تغییر Leak = Change رسمی با Rollback.
- فایروال بین VRFها گزینه‌ی امن‌تر است (Log و Inspection).

### ۱۰) جمع‌بندی مفهومی

- VRF جدول جداگانه است؛ Leak عمدی و حداقلی آن را می‌شکند.
- Leak باید دوطرفه، /32 (یا کوچک) و مستند باشد.
- هر Leak را با آزمون مثبت و منفی بسنجید.
- برای بازرسی/Log، عبور از فایروال بهتر از Leak است.
- در FortiGate، معادل مفهومی: Zone/VDOM با Policy.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) VRF چه چیزی را از هم جدا می‌کند؟ *(پاسخ: 10-8-ت1)*

**ت2.** (ساده) چرا Leak باید دوطرفه باشد؟ *(پاسخ: 10-8-ت2)*

**ت3.** (متوسط) چرا برای DNS مشترک /32 بهتر از /8 است؟ *(پاسخ: 10-8-ت3)*

**ت4.** (متوسط) آزمون منفی در Leak چیست و چرا لازم است؟ *(پاسخ: 10-8-ت4)*

**ت5.** (سخت) دو VRF با آدرس‌های 10.0.0.0/24 هم‌پوشان دارید. Leak ممکن است؟ راه‌حل را شرح دهید. *(پاسخ: 10-8-ت5)*

**ت6.** (سخت، طراحی) برای ۳ VRF (Corp، Guest، Servers) و یک DNS مشترک، جدول Leak و تست‌های مثبت/منفی را بنویسید. *(پاسخ: 10-8-ت6)*

**م1.** تفاوت Leak و عبور از فایروال را بگویید. *(پاسخ: 10-8-م1)*

**Q1.** Quick quiz (English): Why should route leaking be limited to host routes? *(پاسخ: 10-8-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VRF | Virtual Routing and Forwarding | جدول مسیریابی مجازی مستقل |
| RT | Route Target | برچسب Import/Export در VRF با MPLS |
| Leak | Route leaking | نشت عمدی مسیر بین جداول |
| Multi-tenant | Multi-tenancy | چندمستأجری |

- *Route leaking should be minimal, bidirectional and documented.* ← Leak باید حداقلی، دوطرفه و مستند باشد.
- *Always run a negative test to prove isolation.* ← همیشه آزمون منفی برای اثبات جداسازی انجام دهید.

### ۱۳) منابع

- Cisco: «Configuring VRF-lite» و «Route leaking / Inter-VRF routing» (IOS XE IP Routing Configuration Guides).
- RFC 4364 — BGP/MPLS IP VPNs (مفهوم VRF و Route Target).

### تکمیل عمیق: Route Leaking بین VRFها

#### چرا؟

VRFها ایزوله‌اند؛ گاهی باید فقط چند مسیر مشخص (مثلاً DNS مشترک) بین آنها نشت کند. این کار باید کنترل‌شده باشد.

#### مثال ساده — Static Leak

``` text
ip route vrf CUST-A 10.99.0.0 255.255.255.0 10.99.1.1 global
```

مسیر را از VRF به Global نشت می‌دهد.

#### مثال متوسط — Import/Export (VRF-lite با RD/RT)

با Route Target می‌توان مسیر انتخابی را import/export کرد.

#### مثال سخت — ریسک

نشت بی‌قید، ایزولاسیون را می‌شکند و Overlap را خراب می‌کند. فقط Prefix مشخص با Filter.

#### Lab

یک نشت کنترل‌شده بسازید و آزمون منفی بزنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| نشت ناخواسته | Filter ندارد | Prefix-list |
| مسیر نیست | جهت | export/import |
| Overlap | آدرس | NAT |

#### پرسش‌ها با پاسخ

**۱. چرا نشت؟** سرویس مشترک.
**۲. ریسک؟** ایزولاسیون.
**۳. کنترل؟** Prefix-list.

#### English Corner

- *Leak only specific prefixes between VRFs and filter everything else.*
- Q: Why can route leaking undermine isolation?

## درس 10-9 — ECMP: Hashing، Load Balancing واقعی و خرابی‌های پنهان

**فصل ۱۰ · درس افزوده (تکمیل ۱۰-۳ و ۱۰-۶) · پیش‌نیاز: ۱۰-۳، ۱۰-۶، ۵-۰ · ≈ ۵ ساعت**

> **وضعیت:** مفهومی؛ رفتار Hash در Lab vIOS «اجرا نشده» و `Unverified`.

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. شرایط تشکیل ECMP را بگوید.
2. توضیح دهد توزیع بار در ECMP بر پایه‌ی **Flow** است، نه بسته‌ی منفرد، و چرا.
3. بفهمد چرا «دو لینک ۱ گیگ» لزوماً ۲ گیگ نمی‌دهد (Polarization، Elephant Flow).
4. اثر ECMP بر Stateful Firewall و Asymmetric Routing را تحلیل کند.
5. روش بررسی مسیر انتخاب‌شده‌ی یک Flow را بداند.

### ۲) پیش‌نیازها

CEF و Forwarding (۵-۰)، Redistribution و AD/Metric (۵-۱، ۱۰-۱)، Asymmetric (۱۰-۶).

### ۳) مفهوم پایه

وقتی برای یک Prefix چند مسیر **با هزینه‌ی برابر** (Equal-Cost) در RIB نصب شود، روتر می‌تواند ترافیک را بین آن‌ها پخش کند. این **ECMP (Equal-Cost Multi-Path)** است. هدف: استفاده از همه‌ی لینک‌ها و پایداری بالاتر.

چرا ساده نیست؟ اگر بسته‌های یک ارتباط TCP بین دو مسیر پخش شوند، ممکن است با تأخیر متفاوت برسند و **ترتیبشان به‌هم بریزد (Reordering)**؛ TCP این را خرابی می‌پندارد و کند می‌شود. پس روتر مسیر را بر پایه‌ی **Hash** انتخاب می‌کند: همه‌ی بسته‌های یک Flow همیشه یک مسیر را دارند.

### ۴) توضیح عمیق فنی

#### ۴-۱) شرط تشکیل ECMP

- Prefix یکسان و **Metric (و AD) برابر**.
- حداکثر تعداد مسیر موازی محدود است (IOS: حد پیش‌فرض بسته به پلتفرم/نسخه است و با `maximum-paths` تنظیم می‌شود؛ مقدار فعلی را با `show ip protocols` ببینید).
- BGP برای ECMP علاوه بر برابری Attributeها نیاز به `maximum-paths` دارد (و ملاحظات AS_PATH).
- Static Route: دو Route با همان Prefix و AD برابر ← ECMP.

#### ۴-۲) Hashing

CEF مسیر را بر پایه‌ی Hash فیلدهایی از بسته انتخاب می‌کند؛ پیش‌فرض متداول: **IP مبدأ و مقصد** (Per-destination)، و بسته به پلتفرم می‌تواند پورت لایه ۴ را هم شامل شود (`ip cef load-sharing algorithm universal` یا `include-ports`؛ `Unverified`).

``` text
path_index = hash(src_ip, dst_ip [, src_port, dst_port, protocol]) mod number_of_paths
```

نتیجه‌ها:

- یک Flow همیشه یک مسیر؛ **یک Flow بزرگ (Elephant)** نمی‌تواند از دو لینک استفاده کند (حداکثر سرعت یک لینک).
- اگر فقط دو Host با هم صحبت کنند و Hash فقط IP باشد، همه‌ی ترافیک روی یک لینک می‌رود (**Polarization**).
- Hash روی چند Hop پشت‌سرهم با همان الگوریتم ممکن است یک مسیر را بارها انتخاب کند.

#### ۴-۳) ECMP و Stateful Firewall

دو فایروال موازی (فصل ۲۳) یا فایروال با ECMP: ترافیک رفت از FW1 و برگشت از FW2 ← Asymmetric ← Drop (چون Session فقط در FW1 است). راه‌ها: Hash متقارن (هر دو جهت یک مسیر)، یا Session Sync/Active-Passive، یا Policy Routing برای برگشت (فصل ۱۰-۶ و ۲۳).

#### ۴-۴) ECMP و Failure

اگر یک مسیر قطع شود، Flowهای روی آن باید Rehash شوند؛ بعضی Flowها که روی مسیر سالم بودند هم ممکن است جابه‌جا شوند (بسته به الگوریتم) و Session فایروال را بشکنند. «Consistent hashing» در سخت‌افزارهای جدید این اثر را کم می‌کند (خارج از Lab).

#### ۴-۵) Per-packet (ممنوع در عمل)

`ip load-sharing per-packet` بار را دقیق‌تر پخش می‌کند ولی Reordering ایجاد می‌کند و برای TCP مناسب نیست؛ فقط در موارد خاص.

### ۵) مثال حل‌شده

**شرایط:** R1 به R2 با دو لینک 10.0.12.0/30 و 10.0.13.0/30 و Cost برابر. سه Flow:

``` text
F1: 192.168.1.10 -> 172.16.5.20 (TCP 443)
F2: 192.168.1.11 -> 172.16.5.20 (TCP 443)
F3: 192.168.1.12 -> 172.16.5.20 (TCP 443)
```

با Hash فقط IP: توزیع بسته به مقادیر Hash است (ممکن است F1 و F2 هر دو روی لینک ۱ بیفتند). سه Flow هرگز دقیقاً «۱/۲ و ۱/۲» پخش نمی‌شوند؛ توزیع آماری است و با Flow کم نامتوازن است.

**اندازه‌گیری:** `show interfaces | include rate` روی هر دو لینک؛ `show ip cef exact-route 192.168.1.10 172.16.5.20` مسیر F1 را نشان می‌دهد (`Unverified` روی vIOS).

**مثال سخت:** دو فایروال Active/Active پشت ECMP در لبه. چند Flow دچار Drop است ولی Ping معمولی (ICMP) موفق است. توضیح: ICMP تک‌بسته‌ای ممکن است Hash موافق بگیرد؛ TCP با Session روی FW2 برمی‌گردد و Drop می‌شود. شاهد: `diagnose sys session list` فقط روی FW1 و Drop برگشت روی FW2 (فصل ۱۴).

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| ECMP روی چه لینک‌هایی؟ | لینک‌های بدون Stateful میانی؛ یا با Session Sync/Hash متقارن |
| چند مسیر؟ | کم (۲ تا ۴)؛ بیشتر = پیچیدگی عیب‌یابی |
| Hash بر چه پایه؟ | IP + Port برای تنوع بیشتر (اگر پلتفرم بپذیرد) |
| Elephant Flow | LAG/لینک سریع‌تر یا چند Flow موازی در برنامه |

### ۷) پیاده‌سازی و Verification

``` text
R1(config)# ip route 172.16.5.0 255.255.255.0 10.0.12.2
R1(config)# ip route 172.16.5.0 255.255.255.0 10.0.13.2
R1# show ip route 172.16.5.0
R1# show ip cef 172.16.5.0 detail
R1# show ip cef exact-route 192.168.1.10 172.16.5.20
R1# show interfaces GigabitEthernet0/1 | include rate
```

`show ip route` باید دو Next-hop با ستاره‌ی «traffic share» را نشان دهد.

### ۸) Troubleshooting

| علامت | شاهد | علت محتمل |
|---|---|---|
| فقط یک لینک پر است | `show interfaces rate`، Hash | Polarization/Flow کم |
| پخش نامتوازن | `exact-route` برای چند Flow | آماری بودن Hash |
| TCP کند با ECMP | Retransmission (Wireshark) | Per-packet یا Reordering |
| Drop فقط برای بعضی Flowها | Session Table | Asymmetric با Stateful |
| یک مسیر قطع ولی مشکل ماند | `show ip route`، Probe | Route پایدار/Track ندارد |

### ۹) نکات امنیتی

- ECMP می‌تواند مسیر بازرسی را دور بزند (Flow از مسیر بدون فایروال)؛ همه‌ی مسیرهای موازی باید از Policy یکسان عبور کنند.
- Asymmetric ناشی از ECMP، Logهای فایروال را ناقص می‌کند و تحلیل حادثه را سخت می‌کند.

### ۱۰) جمع‌بندی مفهومی

- ECMP نیاز به Metric/AD برابر دارد.
- توزیع بر پایه‌ی Hash و Flow است، نه بسته.
- یک Flow همیشه یک لینک؛ ۲ لینک لزوماً ۲ برابر سرعت یک Flow نمی‌دهد.
- با Stateful Firewall، Asymmetric خطرناک است.
- همیشه توزیع واقعی را اندازه بگیرید.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) شرط ECMP چیست؟ *(پاسخ: 10-9-ت1)*

**ت2.** (ساده) چرا بار بر پایه‌ی Flow است؟ *(پاسخ: 10-9-ت2)*

**ت3.** (متوسط) چرا دو لینک ۱ گیگ برای یک دانلود تک‌Flow ۲ گیگ نمی‌دهند؟ *(پاسخ: 10-9-ت3)*

**ت4.** (متوسط) Polarization یعنی چه؟ *(پاسخ: 10-9-ت4)*

**ت5.** (سخت) ECMP پشت دو فایروال Stateful ایجاد Drop می‌کند. سه راه‌حل را مقایسه کنید. *(پاسخ: 10-9-ت5)*

**ت6.** (سخت) نشان دهید چگونه می‌فهمید یک Flow مشخص از کدام لینک می‌رود. *(پاسخ: 10-9-ت6)*

**م1.** Per-packet load sharing چه ایراد دارد؟ *(پاسخ: 10-9-م1)*

**Q1.** Quick quiz (English): Why does ECMP hash per flow instead of per packet? *(پاسخ: 10-9-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ECMP | Equal-Cost Multi-Path | چند مسیر هم‌هزینه |
| Hash | Hash function | تابع تبدیل فیلدها به شماره‌ی مسیر |
| Flow | Network flow | رشته‌ی بسته‌های یک ارتباط |
| Elephant flow | Elephant flow | Flow بسیار بزرگ |
| Reordering | Packet reordering | به‌هم‌ریختن ترتیب بسته‌ها |

- *ECMP balances flows, not individual packets.* ← ECMP Flowها را متوازن می‌کند، نه بسته‌ها.
- *A single flow never exceeds the speed of one link.* ← یک Flow هرگز از سرعت یک لینک بیشتر نمی‌شود.

### ۱۳) منابع

- Cisco: «Cisco Express Forwarding — Load Balancing» (IP Switching Configuration Guide).
- RFC 2991 — Multipath Issues in Unicast and Multicast Next-Hop Selection.
- RFC 2992 — Analysis of an Equal-Cost Multi-Path Algorithm.

### تکمیل عمیق: ECMP — Hashing و خرابی‌های پنهان

#### چرا؟

ECMP ساده به نظر می‌رسد ولی خطاهای پنهان دارد: Polarization، یک لینک پر و دیگری خالی، قطع هنگام خرابی.

#### مثال ساده — Hash 5-tuple

Hash روی IP منبع/مقصد، پروتکل، پورت‌ها؛ توزیع به تعداد Flow بستگی دارد.

``` text
Flows = 1000 ; paths = 2 -> ~500 each (statistically)
Flows = 2 ; paths = 2 -> might land on the same path
```

#### مثال متوسط — Polarization

دو لایه با Hash یکسان همه‌ی Flowها را روی یک مسیر می‌ریزند. راه: Seed/Algorithm متفاوت.

#### مثال سخت — خرابی

قطع یک لینک: Flowهای آن لینک Rehash می‌شوند؛ Session قطع می‌شود (اگر Stateful بین راه).

#### Lab

توزیع Flow را با iperf چند Stream ببینید.

``` text
iperf3 -c 10.20.0.10 -P 16 -t 20
```

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| یک لینک پر | Flow کم | Stream بیشتر |
| Polarization | Hash یکسان | Seed |
| قطع در خرابی | Rehash | طراحی |

#### پرسش‌ها با پاسخ

**۱. Polarization؟** همه روی یک مسیر.
**۲. چرا Flow بیشتر؟** توزیع.
**۳. خرابی؟** Rehash.

#### English Corner

- *With few flows, hashing may place them all on one path.*
- Q: What is hash polarization?

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

### ۲) مفهوم پایه: چیست و چرا؟

نگهبان ساختمان را تصور کنید. نگهبان نوع اول فقط لیست «مجاز/ممنوع» دارد و هر بار برگه را چک می‌کند (Stateless). نگهبان نوع دوم یادش می‌ماند چه کسی بیرون رفت و فقط جواب او را اجازه‌ی ورود می‌دهد (Stateful). نوع سوم داخل کیف هم نگاه می‌کند (NGFW).

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

### ۲) مفهوم پایه: چیست و چرا؟

فرودگاه را در نظر بگیرید: سالن عمومی، گیت امنیتی، سالن پرواز، باند و اتاق کنترل. هر منطقه سطح اعتماد متفاوت و مرز مشخص دارد؛ عبور از هر مرز فقط با مجوز مخصوص. اگر همه‌ی درها باز باشند، دیوار بی‌معناست.

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

### ۲) مفهوم پایه: چیست و چرا؟

کاربر می‌گوید «سایت باز نمی‌شود». بدون نقشه‌ی مسیر بسته، حدس می‌زنید: Policy؟ Route؟ NAT؟ DNS؟ با نقشه، مرحله‌به‌مرحله می‌پرسید: بسته رسید؟ Session ساخته شد؟ Route دارد؟ Policy؟ NAT؟ خارج شد؟ هر پاسخ «نه» محل خرابی را نشان می‌دهد.

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

### ۲) مفهوم پایه: چیست و چرا؟

سه اشتباه رایج: «NAT گذاشتم ولی کار نمی‌کند»، «Policy گذاشتم ولی ترجمه نمی‌شود»، «ACL گذاشتم ولی دور زده می‌شود». هر سه از یکی‌گرفتن سه ابزار با وظایف متفاوت می‌آید.

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

### ۲) مفهوم پایه: چیست و چرا؟

شکایت رایج: «سایت باز می‌شود ولی بعد از لاگین گیر می‌کند»، «ping جواب می‌دهد ولی دانلود می‌ایستد»، «SSH بعد از چند دقیقه می‌پرد». اینها Policy نیستند؛ MTU یا Timeout‌اند. تشخیصشان نیاز به دانستن این دارد که در لایه‌ی انتقال چه می‌گذرد.

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

### ۲) مفهوم پایه: چیست و چرا؟

این کارگاه آخرین مرحله‌ی فصل ۱۱ است: به‌جای جمله‌های کلی، یک شرکت کوچک را از صفر تا آزمون طراحی می‌کنید. هدف این است که وقتی ممیز پرسید «چرا DB از اینترنت دیده نمی‌شود؟» با Policy، Log و آزمون جواب بدهید.

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

### ۲) پیش‌نیازها

TCP Three-way Handshake و Flagها (SYN، ACK، FIN، RST)، تفاوت UDP/ICMP، Packet Flow پایه (۵-۰).

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

### ۲) مفهوم پایه: چیست و چرا؟

دستگاه جدید را از جعبه درمی‌آورید. پیش از هر Policy باید بدانید چه دستگاهی است، چه نسخه‌ای دارد و لایسنس دارد یا نه؛ چون ویژگی‌ها و دستورها به نسخه وابسته‌اند و «همان‌طور که در دوره نوشته شده» کار نمی‌کند اگر نسخه فرق کند.

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

### ۲) مفهوم پایه: چیست و چرا؟

FortiGate را به شبکه وصل می‌کنید و «کار نمی‌کند». ۷۰٪ مواقع علت در Interface است: کابل در پورت دیگر، VLAN ID اشتباه، یا Allowaccess بسته. و بدتر: مدیر برای راحتی HTTPS را روی WAN باز می‌گذارد و چند روز بعد پنل مدیریت از اینترنت Brute-force می‌شود.

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

### ۲) مفهوم پایه: چیست و چرا؟

Policy بدون Object مثل کدی با عددهای جادویی است: «10.20.0.10» در ۴۰ Policy پخش شده و وقتی سرور عوض شد، باید ۴۰ جا را پیدا کنید. با Object، فقط یک تعریف عوض می‌شود و همه‌ی Policyها به‌روز می‌شوند. Zone همین ایده برای Interfaceهاست.

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

### ۲) مفهوم پایه: چیست و چرا؟

Policy درست و ترافیک نمی‌رسد؟ اغلب Route است. در FortiGate Route قبل از Policy تصمیم می‌گیرد بسته از کدام Interface خارج شود؛ سپس Policy برای همان جفت (ورودی، خروجی) جست‌وجو می‌شود. پس Route اشتباه = Policy بی‌اثر.

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

### ۲) مفهوم پایه: چیست و چرا؟

اگر همه‌ی مدیران Super-admin باشند، یک رمز لورفته یعنی تسلط کامل: پاک‌کردن Policy، دریافت Config و حتی VPN backdoor. RBAC هر نفر را به اندازه‌ی کارش محدود می‌کند؛ MFA و Trusted host لایه‌ی بعدی‌اند.

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

### ۲) مفهوم پایه: چیست و چرا؟

Upgrade بدون Backup مثل جراحی بدون رضایت‌نامه است. یک Upgrade ساده می‌تواند Config را خراب کند یا Boot loop بسازد. تفاوت مهندس حرفه‌ای با تازه‌کار: Backup، Path، Rollback و آزمون پس از تغییر.

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

### ۲) پیش‌نیازها

Packet Flow (۱۲-۰)، Punt و Management Plane (۵-۰)، مدل تهدید (۱۱-۰).

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

### ۲) پیش‌نیازها

Packet Flow (۱۲-۰)، Session (۱۱-۷)، مفهوم CPU و ASIC.

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

### ۲) مفهوم پایه: چیست و چرا؟

«بعد از تغییر Interface نمی‌توانم وارد فایروال شوم.» اگر مدیریت را روی همان Interface تغییر داده باشید، قفل شده‌اید. این آزمون سه خطای واقعی را تمرین می‌کند: قفل‌شدن، Route اشتباه و ناسازگاری VLAN.

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
