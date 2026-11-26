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

مسیرها با **Metric و AD برابر** و حداکثر `maximum-paths` (OSPF پیش‌فرض 4، EIGRP 4).

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

## درس 10-4 — Policy-Based Routing (PBR): مسیریابی بر اساس سیاست، نه فقط مقصد

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۸-۱ · ≈ 9 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. PBR را در برابر مسیریابی معمولی توضیح دهد.
2. ACL+Route-map با `set ip next-hop` را پیکربندی و روی Interface اعمال کند.
3. Local PBR و ترتیب پردازش را بشناسد.
4. Verification با `show route-map` و Debug محدود را اجرا کند.
5. خطاهای رایج (ACL غلط، Next-hop نامعتبر) را رفع کند.

### ۲) مفهوم پایه: چیست و چرا؟

مسیریابی عادی فقط به «مقصد» نگاه می‌کند. گاهی می‌خواهید ترافیک واحد مالی از ISP-A برود و باقی از ISP-B؛ این «سیاست» است. PBR قبل از جدول مسیریابی تصمیم می‌گیرد.

### ۳) توضیح عمیق فنی

#### ۱) ساختار

``` text
ip access-list extended FINANCE
 permit ip 10.10.20.0 0.0.0.255 any
route-map PBR-ISPA permit 10
 match ip address FINANCE
 set ip next-hop verify-availability 192.0.2.1 10 track 1
route-map PBR-ISPA permit 20
interface GigabitEthernet0/1
 ip policy route-map PBR-ISPA
```

`permit 20` بدون Match = بقیه‌ی ترافیک عادی.

#### ۲) ترتیب

Packet ورودی → PBR (در صورت Match) → Next-hop مشخص؛ در غیر این صورت RIB. `set ip next-hop` در مقابل `set ip default next-hop` (فقط وقتی مسیر ندارد).

#### ۳) Local PBR

``` text
ip local policy route-map LOCAL-PBR
```

برای ترافیک خود روتر.

#### ۴) Track و Failover

با `ip sla` و `track` اگر Next-hop مرده بود، PBR بی‌خبر نماند.

#### ۵) آزمون

``` text
show route-map PBR-ISPA
show ip policy
traceroute 8.8.8.8 source 10.10.20.5
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| next-hop یا default next-hop | default اگر مسیر عادی ترجیح |
| Track | اجباری |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Finance از ISP-A: traceroute از 10.10.20.5 از 192.0.2.1 عبور می‌کند.

**متوسط (تحلیل):** PBR اثر ندارد: ACL روی subnet اشتباه؛ `show route-map` شمارنده‌ی Match صفر؛ رفع ACL.

**سخت (Failover):** ISP-A قطع شد ولی Finance قطع ماند: Track نبود؛ راه: IP SLA+Track با `verify-availability`؛ آزمون: قطع لینک؛ Finance به مسیر عادی می‌رود.

### ۷) پیاده‌سازی از مسیر CLI

``` text
route-map PBR-ISPA permit 10
 match ip address FINANCE
 set ip next-hop verify-availability 192.0.2.1 10 track 1
interface Gi0/1
 ip policy route-map PBR-ISPA
show route-map PBR-ISPA
```

### ۸) Verification (اثبات صحت)

- Match counter بالا می‌رود.
- traceroute مسیر سیاست.
- آزمون Failover.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Match صفر | ACL | Subnet |
| Failover ندارد | Track | verify-availability |
| ترافیک گم | Next-hop | ARP/Reachability |

### ۱۰) نکات امنیتی

- PBR مسیرها را از Firewall دور نکند.

### ۱۱) جمع‌بندی مفهومی

- PBR قبل از RIB.
- ACL+Route-map.
- Track.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) PBR بر چه اساسی تصمیم می‌گیرد؟ *(پاسخ: 10-4-ت1)*

**ت2.** (ساده) `permit 20` خالی یعنی چه؟ *(پاسخ: 10-4-ت2)*

**ت3.** (متوسط) تفاوت next-hop و default next-hop؟ *(پاسخ: 10-4-ت3)*

**ت4.** (متوسط) Local PBR؟ *(پاسخ: 10-4-ت4)*

**ت5.** (سخت) Failover PBR. *(پاسخ: 10-4-ت5)*

**ت6.** (سخت، طراحی) PBR دو ISP. *(پاسخ: 10-4-ت6)*

**Q1.** Quick quiz (English): What is the purpose of the track keyword in PBR? *(پاسخ: 10-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PBR | Policy-Based Routing | مسیریابی سیاست‌محور |
| SLA | Service Level Agreement/IP SLA | پایش |

- *PBR overrides destination-based routing.* ← PBR مسیریابی مبتنی بر مقصد را لغو می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** PBR. **Evidence:** `03-ops/pbr.md`.

### ۱۵) منابع

- Cisco PBR guide

<a id="l-10-5"></a>

## درس 10-5 — VRF-lite: جداسازی جدول مسیریابی

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۶-۱، ۱۰-۴ · ≈ 9 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. VRF را (چند RIB مستقل) توضیح دهد.
2. VRF-lite با Interface و مسیر مستقل پیکربندی کند.
3. Overlap آدرس را مدیریت کند.
4. Verification و Troubleshooting `vrf` را انجام دهد.
5. VRF را برای جداسازی فایروال/مشتریان طراحی کند.

### ۲) مفهوم پایه: چیست و چرا؟

یک ساختمان با دو شرکت: هر کدام آدرس 192.168.1.0/24 دارند و نباید یکدیگر را ببینند. VRF روی همان روتر «چند روتر مجازی» می‌سازد؛ هر کدام RIB جداگانه دارند.

### ۳) توضیح عمیق فنی

#### ۱) پیکربندی

``` text
ip vrf CUST-A
 rd 65000:1
ip vrf CUST-B
 rd 65000:2
interface Gi0/1
 ip vrf forwarding CUST-A
 ip address 192.168.1.1 255.255.255.0
interface Gi0/2
 ip vrf forwarding CUST-B
 ip address 192.168.1.1 255.255.255.0
```

دستور `ip vrf forwarding` آدرس را پاک می‌کند: بعد از آن آدرس را دوباره بزنید.

#### ۲) مسیر

``` text
ip route vrf CUST-A 0.0.0.0 0.0.0.0 10.0.0.1
router ospf 10 vrf CUST-A
```

#### ۳) تست

``` text
show ip vrf
show ip route vrf CUST-A
ping vrf CUST-A 192.168.1.2
```

بدون `vrf` به جدول Global می‌رود.

#### ۴) استفاده با فایروال

هر VRF یک مسیر به Interface فایروال؛ فایروال VDOM/Zone مقابل. Route Leaking: ۱۰-۸.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| VRF-lite یا MPLS VRF | داخلی: lite |
| RD | یکتا |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** CUST-A و B هر دو 192.168.1.0/24؛ هیچ تداخلی.

**متوسط (تحلیل):** ping داخل VRF جواب نمی‌دهد: بدون `vrf` اجرا شده؛ رفع: `ping vrf`.

**سخت (طراحی):** سه مشتری با خروج اینترنت مشترک: VRFهای جدا + Default به Firewall؛ Leak کنترل‌شده؛ NAT جدا؛ آزمون عدم دسترسی متقابل.

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
| آدرس پاک شد | forwarding بعد آدرس | آدرس را دوباره بزنید |
| ping ناموفق | vrf | ping vrf |
| نشت | Leak | حذف |

### ۱۰) نکات امنیتی

- جداسازی ≠ امنیت کامل؛ سیاست فایروال لازم است.

### ۱۱) جمع‌بندی مفهومی

- VRF=چند RIB.
- Overlap.
- ping vrf.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) VRF چیست؟ *(پاسخ: 10-5-ت1)*

**ت2.** (ساده) چرا ip address پاک می‌شود؟ *(پاسخ: 10-5-ت2)*

**ت3.** (متوسط) چگونه ping کنید؟ *(پاسخ: 10-5-ت3)*

**ت4.** (متوسط) RD؟ *(پاسخ: 10-5-ت4)*

**ت5.** (سخت) سه مشتری. *(پاسخ: 10-5-ت5)*

**ت6.** (سخت، طراحی) جداسازی با فایروال. *(پاسخ: 10-5-ت6)*

**Q1.** Quick quiz (English): What does VRF-lite provide? *(پاسخ: 10-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VRF | Virtual Routing and Forwarding | مسیریابی مجازی |
| RD | Route Distinguisher | تمایزدهنده‌ی مسیر |

- *VRF separates routing tables.* ← VRF جدول‌های مسیریابی را جدا می‌کند.

### ۱۴) کارت Lab

**کارت Lab:** VRF. **Evidence:** `03-ops/vrf.md`.

### ۱۵) منابع

- Cisco VRF-lite guide

<a id="l-10-6"></a>

## درس 10-6 — Asymmetric Routing: تحلیل رفت و برگشت و اثر بر فایروال

**فصل 10 · بازنویسی عمیق · پیش‌نیاز: ۱۰-۳، ۱۱-۱ · ≈ 9 ساعت**

> **وضعیت:** Cisco IOSv 15.9/CSR1000v 17.03؛ خروجی‌ها نمونه‌ی آموزشی؛ Lab «اجرا نشده»؛ دستورهای vIOS `Unverified` تا اجرای Lab.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Asymmetric Routing را تعریف و علت‌ها را بگوید.
2. اثر آن بر Stateful Firewall را توضیح دهد.
3. با traceroute و Capture دو سویه آن را ثابت کند.
4. راه‌حل‌ها (Symmetric design، Policy، Session-pickup) را مقایسه کند.
5. رفع را اجرا و آزمون کند.

### ۲) مفهوم پایه: چیست و چرا؟

بسته‌ی رفت از فایروال ۱ می‌گذرد و برگشت از فایروال ۲. فایروال ۲ فقط «برگشت» را می‌بیند، Session نمی‌شناسد و Drop می‌کند. کاربر می‌گوید «سایت باز نمی‌شود»؛ ولی لینک‌ها سالم‌اند.

### ۳) توضیح عمیق فنی

#### ۱) علل

- ECMP/Per-packet
- دو ISP/Policy متفاوت
- Redistribution/BGP Local-pref متفاوت
- HA/Cluster نادرست

#### ۲) اثر بر فایروال

Stateful: SYN-ACK بدون SYN ⇒ "no session matched"/Drop. Stateless: مشکلی ندارد.

#### ۳) اثبات

``` text
Capture on FW1: SYN seen
Capture on FW2: SYN-ACK seen, no SYN
traceroute from both ends shows different hops
```

#### ۴) راه‌حل‌ها

| روش | توضیح |
|---|---|
| طراحی Symmetric | Routing/Weight/Local-pref |
| Policy-route | هر جریان را به یک فایروال |
| Session sync | FGCP session-pickup/Active-Active |
| Disable asymmetric check | فقط موقت (`asymroute`) و ضعیف‌شدن امنیت |

#### ۵) آزمون بعد از رفع

ping/TCP و `diagnose sys session list` روی یک فایروال.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Symmetric یا sync | Symmetric ترجیح |
| asymroute | نه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Capture: FW1 فقط SYN؛ FW2 فقط SYN-ACK؛ تشخیص Asymmetric.

**متوسط (تحلیل):** ISP2 برگشت را از لینک دوم می‌آورد؛ راه: Local-pref/Prepend و PBR.

**سخت (طراحی):** Active-Active با Session sync؛ ریسک: Delay؛ جایگزین: Active-Standby.

### ۷) پیاده‌سازی از مسیر CLI

``` text
traceroute 10.20.0.5
show ip route 10.20.0.5
! on FortiGate (Unverified in lab): diagnose sniffer packet any "host 10.20.0.5" 4
```

### ۸) Verification (اثبات صحت)

- Capture دو سویه.
- Session روی یک FW.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| برخی Sessionها قطع | Capture | Symmetric/Policy |
| فقط پورت‌های خاص | Hash | ECMP |

### ۱۰) نکات امنیتی

- Disable کردن Check امنیت را کم می‌کند.

### ۱۱) جمع‌بندی مفهومی

- Asymmetric=Drop در Stateful.
- اثبات با Capture.
- راه Symmetric.

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

**کارت Lab:** Asymmetric. **Evidence:** `03-ops/asym.md`.

### ۱۵) منابع

- Fortinet admin guide: asymmetric routing

<a id="l-10-7"></a>

## درس 10-7 — طراحی مسیر برای چندفایروالی و آزمون کوچک

**فصل 10 - روز 7 · پیش‌نیاز: درس ۱۰-۵ · ۶ ساعت**

### ۱) معرفی درس

جمع‌بندی: هنگام قرار دادن چند فایروال در مسیر باید جدول مسیر هر دستگاه و جهت Session را طراحی کنید. این درس مرجع ورود به فصل‌های فایروال است.

### ۲) پیش‌نیازها

درس‌های ۱۰-۱ تا ۱۰-۵.

### ۳) توضیح مفهومی

- برای هر فایروال: «Route رفت»، «Route برگشت»، «NAT» و «Policy» را بنویسید.
- قاعده: **Session باید هر دو جهت را از همان فایروال ببیند.**
- Redistribution کنترل‌شده، Metric/Local-Pref برای تقارن، PBR فقط با Return همخوان.
- مستندسازی: جدول «Packet Walk رفت/برگشت».

### ۴) مثال ساده

دو فایروال سری: Client → FW-A → FW-B → Server با Static متقارن.

### ۵) مثال سازمانی

دو فایروال موازی (HA یا Active-Active) با ECMP: Session sync لازم است.

### ۶) تصویر و توپولوژی

```text
Client -> FW-A -> FW-B -> Server
Packet Walk table: hop, route, policy, NAT
```

### ۷) پیکربندی (CLI)

```text
show ip route 10.20.0.10
traceroute 10.20.0.10 source 192.168.1.1
show ip route 192.168.1.0
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- هر Hop را ثبت و تقارن را بررسی کنید.
- نتیجه: جدول Packet Walk.

### ۸) تست عملکرد

- ۴ سناریو (ECMP، PBR، Redistribution، دو ISP) با تحلیل تقارن و راه‌حل.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | بعد از افزودن لینک جدید ارتباط TCP قطع شد |
| شواهد/دستور | مسیر برگشت از لینک جدید |
| علت | Metric لینک جدید بهتر است |
| رفع | تنظیم Metric/Local-Pref |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** قاعده‌ی طلایی چندفایروالی؟ *(پاسخ: 10-7-ت1)*

**ت2.** Packet Walk چیست؟ *(پاسخ: 10-7-ت2)*

**ت3.** چه زمانی Session sync لازم است؟ *(پاسخ: 10-7-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا افزودن لینک جدید خطرناک است؟ *(پاسخ: 10-7-م1)*

**م2.** سناریو: دو فایروال موازی؛ چه باید کرد؟ *(پاسخ: 10-7-م2)*

**معیار تسلط:** ساخت Packet Walk برای یک توپولوژی دو فایروالی و ≥ ۴ از ۵ مورد آزمون.

**اشتباهات رایج:** تحلیل بدون جدول؛ فرض تقارن.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Packet Walk | Packet walk | دنبال‌کردن بسته Hop به Hop | عیب‌یابی |
| Session sync | Session synchronization | همگام‌سازی Session | HA |

| English sentence | ترجمه |
|---|---|
| Document the packet walk for both directions. | Packet Walk را برای هر دو جهت مستند کنید. |
| Both directions must traverse the same firewall. | هر دو جهت باید از یک فایروال عبور کنند. |

#### کارت Lab — درس 10-7

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Packet Walk دو فایروالی |
| 2 | پیش‌نیاز | درس ۱۰-۵ |
| 3 | توپولوژی | Client-FW-A-FW-B-Server |
| 4 | تجهیزات | ۴ vIOS |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | جدول آدرس |
| 7 | وضعیت اولیه | Static |
| 8 | صورت مسئله | جدول Packet Walk |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | traceroute |
| 11 | سناریوی خرابی | بعد از افزودن لینک جدید ارتباط TCP قطع شد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول کامل |
| 14 | معیار پذیرش | جهت‌ها متقارن |
| 15 | مستندات نهایی | `03-ops/packet-walk.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="ans-10"></a>

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
- حداکثر تعداد مسیر موازی محدود است (IOS: پیش‌فرض 4، قابل‌تنظیم با `maximum-paths`؛ `Unverified` برای Image).
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


## پاسخ‌های فصل 10

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 10-1

**10-1-ت1** — ۲۰ و نوع E2 (برای BGP مقدار ۱).

**10-1-ت2** — Metric OSPF/BGP قابل تبدیل نیست؛ نبود Metric یعنی بی‌نهایت و مسیر منتقل نمی‌شود؛ باید دستی بدهید.

**10-1-ت3** — E2 فقط Metric خارجی؛ E1 هزینه‌ی داخلی تا ASBR را هم جمع می‌کند.

**10-1-ت4** — فقط مسیرهای classful منتقل می‌شوند؛ زیرشبکه‌ها نمی‌روند.

**10-1-ت5** — E1 برای انتخاب نزدیک‌ترین ASBR؛ آزمون با traceroute.

**10-1-ت6** — فقط Prefixهای لازم با Prefix-list+Route-map، Seed صریح، E1 در صورت چند ASBR و آزمون منفی روی Prefix غیرمجاز.

**10-1-Q1** — The routes are not redistributed because the seed metric is infinite.


### پاسخ‌های بازنویسی عمیق درس 10-2

**10-2-ت1** — مسیری که به پروتکل دیگر رفته دوباره به مبدأ برگردد.

**10-2-ت2** — مبدأ مسیر را علامت می‌زند تا بازگشت آن رد شود.

**10-2-ت3** — وگرنه ASBR بدون Route-map حلقه می‌سازد.

**10-2-ت4** — 110 و 170.

**10-2-ت5** — Route-map فقط روی R-A؛ یکسان‌سازی و آزمون.

**10-2-ت6** — مبدأ، Tag، جهت، Route-map و مالک.

**10-2-Q1** — To prevent routes from being re-redistributed back into their source domain, avoiding loops.


### پاسخ‌های بازنویسی عمیق درس 10-3

**10-3-ت1** — Metric و AD برابر.

**10-3-ت2** — هر جریان همیشه از یک مسیر.

**10-3-ت3** — بسته‌ها نامرتب می‌رسند.

**10-3-ت4** — ۴.

**10-3-ت5** — الگوریتم Hash با پورت؛ آزمون با چند جریان.

**10-3-ت6** — Symmetric hash/Active-Standby.

**10-3-Q1** — It preserves packet order within a flow and works with stateful devices.


### پاسخ‌های بازنویسی عمیق درس 10-4

**10-4-ت1** — Source/Protocol/Port و ...

**10-4-ت2** — بقیه‌ی ترافیک عادی.

**10-4-ت3** — default فقط وقتی مسیر ندارد.

**10-4-ت4** — برای ترافیک خود روتر.

**10-4-ت5** — Track+IP SLA.

**10-4-ت6** — ACL، Track، Failover.

**10-4-Q1** — To remove the policy next hop when it becomes unreachable.


### پاسخ‌های بازنویسی عمیق درس 10-5

**10-5-ت1** — RIB مجازی جدا.

**10-5-ت2** — هنگام forwarding.

**10-5-ت3** — ping vrf NAME.

**10-5-ت4** — شناسه‌ی یکتا برای Route.

**10-5-ت5** — VRF+Default+NAT.

**10-5-ت6** — VRF+Zone.

**10-5-Q1** — Multiple isolated routing tables on a single router without MPLS.


### پاسخ‌های بازنویسی عمیق درس 10-6

**10-6-ت1** — رفت و برگشت از مسیر متفاوت.

**10-6-ت2** — Session ندیده.

**10-6-ت3** — ECMP، دو ISP، Redistribution.

**10-6-ت4** — Capture دو سویه.

**10-6-ت5** — Symmetric یا Session sync.

**10-6-ت6** — Sync+Hash.

**10-6-Q1** — They do not see the initial packet so no session exists.

**10-7-ت1** — قاعده‌ی طلایی چندفایروالی؟

هر دو جهت Session از یک فایروال.

**10-7-ت2** — Packet Walk چیست؟

جدول مسیر و سیاست هر Hop برای رفت و برگشت.

**10-7-ت3** — چه زمانی Session sync لازم است؟

وقتی مسیر ممکن است عوض شود (HA/Active-Active).

**10-7-م1** — چرا افزودن لینک جدید خطرناک است؟

ممکن است مسیر برگشت را عوض کند.

**10-7-م2** — سناریو: دو فایروال موازی؛ چه باید کرد؟

Session sync/HA یا مسیریابی تثبیت‌شده.


---

<a id="ch11"></a>


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

## درس 11-2 — Zone، Trust Boundary، Default Deny و Least Privilege

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱ · ≈ 9 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Zone و سطح اعتماد را تعریف و ماتریس Zone-to-Zone بسازد.
2. Default Deny و Least Privilege را در Policy اعمال کند.
3. Policy را از ماتریس استخراج و ترتیب را رعایت کند.
4. Policy گشاد را با Log شناسایی و تنگ کند.
5. ماتریس را مستند کند.

### ۲) مفهوم پایه: چیست و چرا؟

در یک فرودگاه، مسافر عمومی، کارمند و منطقه‌ی امنیتی سطح اعتماد متفاوت دارند. فایروال هم شبکه را به Zone تقسیم می‌کند و بین Zoneها فقط عبور لازم را مجاز می‌کند؛ بقیه رد می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) Zone

| Zone | اعتماد | مثال |
|---|---|---|
| Internet | صفر | WAN |
| DMZ | کم | وب‌سرور |
| Server | متوسط | DB/App |
| User | متوسط | کاربران |
| Mgmt | بالا | مدیریت |

#### ۲) ماتریس

``` text
          Internet  DMZ   Server  User  Mgmt
User      HTTP/S    -     App     -     -
DMZ       -         -     DB-only -     -
Internet  -         443   -       -     -
Mgmt      -         SSH   SSH     SSH   -
```

هر خانه‌ی خالی = Deny.

#### ۳) Default Deny

Policy آخر `deny all + log`. و Policyها از **خاص به عام**.

#### ۴) Least Privilege

به‌جای `ALL` فقط سرویس لازم؛ به‌جای `any` فقط Host/Subnet لازم؛ زمان‌دار.

#### ۵) ممیزی

``` text
Policy hit-count = 0 (90 days)  -> remove
Policy ALL/ALL      -> narrow
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| تعداد Zone | طبق ریسک؛ نه بیش از حد |
| ترتیب | خاص→عام |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** User→Internet فقط HTTP/HTTPS.

**متوسط (تحلیل):** Policy `User→Server ALL`: Log نشان می‌دهد فقط 443 و 1433 استفاده شده؛ تنگ‌سازی به همان دو.

**سخت (طراحی):** ۵ Zone با ماتریس؛ ۱۲ Policy؛ DMZ به DB مستقیم ممنوع؛ از App؛ آزمون منفی برای هر خانه‌ی Deny؛ معیار: صفر Policy ALL.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! FortiGate (Unverified in lab)
config firewall policy
 edit 10
  set srcintf "port2"
  set dstintf "port1"
  set srcaddr "LAN-NET"
  set dstaddr "all"
  set action accept
  set schedule "always"
  set service "HTTP" "HTTPS"
  set logtraffic all
 next
end
```

### ۸) Verification (اثبات صحت)

- آزمون مثبت و منفی برای هر خانه.
- hit-count.
- Log.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy کار نمی‌کند | ترتیب | خاص قبل عام |
| ALL گشاد | Log | تنگ‌سازی |

### ۱۰) نکات امنیتی

- Default Deny با Log.

### ۱۱) جمع‌بندی مفهومی

- Zone و ماتریس.
- Least Privilege.
- ترتیب.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Default Deny یعنی؟ *(پاسخ: 11-2-ت1)*

**ت2.** (ساده) Least Privilege؟ *(پاسخ: 11-2-ت2)*

**ت3.** (متوسط) چرا ماتریس؟ *(پاسخ: 11-2-ت3)*

**ت4.** (متوسط) ترتیب Policy؟ *(پاسخ: 11-2-ت4)*

**ت5.** (سخت) Policy ALL را چگونه تنگ کنیم؟ *(پاسخ: 11-2-ت5)*

**ت6.** (سخت، طراحی) ماتریس ۵ Zone. *(پاسخ: 11-2-ت6)*

**Q1.** Quick quiz (English): What does default deny mean in firewall policy design? *(پاسخ: 11-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DMZ | Demilitarized Zone | منطقه‌ی حائل |
| ACL | Access Control List | فهرست کنترل دسترسی |

- *Apply least privilege to every rule.* ← به هر Rule حداقل دسترسی را بدهید.

### ۱۴) کارت Lab

**کارت Lab:** ماتریس Zone. **Evidence:** `03-ops/zone-matrix.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policy
- NIST SP 800-41

<a id="l-11-3"></a>

## درس 11-3 — مسیر بسته در فایروال: ترافیک عبوری در برابر ترافیک خود فایروال

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۲-۰ · ≈ 9 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مراحل پردازش را (Ingress، Route، Policy، NAT، Egress) بگوید.
2. Transit، Local-in و Local-out را تفکیک کند.
3. ترتیب DNAT/Route/Policy/SNAT را بداند.
4. سناریو را روی کاغذ شبیه‌سازی کند.
5. Packet-flow را با ابزار تأیید کند.

### ۲) مفهوم پایه: چیست و چرا؟

وقتی «سایت باز نمی‌شود»، بدون نقشه‌ی مسیر بسته فقط حدس می‌زنید. با نقشه می‌پرسید: بسته به Interface رسید؟ Route داشت؟ Policy؟ NAT؟ خارج شد؟

### ۳) توضیح عمیق فنی

#### ۱) مسیر عبوری

``` text
Ingress -> Anti-spoof(RPF) -> Session lookup -> DNAT(VIP) -> Route -> Policy -> SNAT -> Egress
```

#### ۲) سه نوع ترافیک

| نوع | مقصد | کنترل |
|---|---|---|
| Transit | شبکه‌ی پشت | Firewall Policy |
| Local-in | خود فایروال | Local-in policy / Admin access |
| Local-out | از خود فایروال | Routing خود دستگاه |

#### ۳) ترتیب مهم

DNAT قبل از Route و Policy؛ SNAT بعد از Policy. پس Policy با آدرس **بعد از DNAT** نوشته می‌شود.

#### ۴) شبیه‌سازی

کاربر 10.0.0.5 به وب 203.0.113.10:443 ⇒ RPF OK ⇒ Route Default ⇒ Policy User→Internet ⇒ SNAT به WAN ⇒ خروج.

#### ۵) ابزار

``` text
diagnose debug flow filter addr 203.0.113.10
diagnose debug flow trace start 20
diagnose debug enable
```

(در FortiOS 7.0 برای NP-offload قبلاً offload غیرفعال شود؛ `Unverified` تا Lab.)

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Local-in policy | فقط Mgmt |
| SNAT | طبق خروجی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Transit: User→Internet.

**متوسط (تحلیل):** پینگ به آدرس Public VIP از اینترنت؛ Policy باید با آدرس داخلی (بعد DNAT) باشد؛ در غیر این صورت `no policy`.

**سخت (چندمرحله):** ترافیک Admin از Mgmt به فایروال: Local-in؛ شکست: Admin access روی Interface نیست؛ debug flow «local» را نشان می‌دهد.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose debug flow filter addr 203.0.113.10
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
```

### ۸) Verification (اثبات صحت)

- Debug flow مراحل را نشان می‌دهد.
- Policy-id درست.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| no policy | Policy | آدرس بعد DNAT |
| RPF drop | Route برگشت | Route/RPF |

### ۱۰) نکات امنیتی

- Debug را بعد از تست غیرفعال کنید.

### ۱۱) جمع‌بندی مفهومی

- مسیر مرحله‌ای.
- سه نوع.
- DNAT قبل Policy.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) ترتیب DNAT و Policy؟ *(پاسخ: 11-3-ت1)*

**ت2.** (ساده) Local-in چیست؟ *(پاسخ: 11-3-ت2)*

**ت3.** (متوسط) چرا Policy با آدرس داخلی؟ *(پاسخ: 11-3-ت3)*

**ت4.** (متوسط) RPF؟ *(پاسخ: 11-3-ت4)*

**ت5.** (سخت) Admin قطع. *(پاسخ: 11-3-ت5)*

**ت6.** (سخت، طراحی) نقشه‌ی Flow سازمان. *(پاسخ: 11-3-ت6)*

**Q1.** Quick quiz (English): Does DNAT occur before or after the firewall policy lookup? *(پاسخ: 11-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس |
| VIP | Virtual IP | آدرس مجازی DNAT |

- *Trace the packet through each stage.* ← بسته را مرحله‌به‌مرحله ردیابی کنید.

### ۱۴) کارت Lab

**کارت Lab:** Flow. **Evidence:** `03-ops/flow.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0: Packet flow ingress/egress

<a id="l-11-4"></a>

## درس 11-4 — ACL، Policy و NAT: تفاوت‌ها و ارتباط‌ها

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۳ · ≈ 9 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. ACL، Firewall Policy و NAT را از نظر وظیفه تفکیک کند.
2. انواع NAT (Source، Destination، PAT) را بشناسد.
3. NAT و Policy را برای دسترسی از بیرون هماهنگ کند.
4. خطاهای NAT/Policy را عیب‌یابی کند.
5. مثال سناریوی Publish را بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

ACL مثل لیست مهمان، Policy مثل مجوز ورود و NAT مثل تغییر نام‌ها روی تابلو است. هر کدام کار خودش را می‌کند؛ اشتباه گرفتنشان باعث «NAT دارم ولی کار نمی‌کند» می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) تفاوت

| | ACL | Policy | NAT |
|---|---|---|---|
| وظیفه | فیلتر ساده | اجازه/ردّ + بازرسی | تغییر آدرس |
| وضعیت | معمولاً Stateless | Stateful | بسته‌ها را بازنویسی |

#### ۲) انواع NAT

- Source NAT (PAT/Overload): خروج کاربران با یک IP.
- Destination NAT (VIP): انتشار سرور داخلی.
- Static one-to-one.

#### ۳) انتشار وب

``` text
VIP: 203.0.113.10:443 -> 10.20.0.10:443
Policy: Internet -> DMZ, dst = VIP, service HTTPS, accept
```

#### ۴) نکته

NAT بدون Policy یعنی ترافیک رد می‌شود؛ Policy بدون NAT برای VIP یعنی مقصد ترجمه نمی‌شود.

#### ۵) خطاها

- Hairpin NAT: کاربر داخلی به IP عمومی سرور داخلی.
- Overlap NAT.
- SNAT فراموش‌شده ⇒ بدون برگشت.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| DNS داخلی | Split DNS بهتر از Hairpin |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** PAT خروج کاربران.

**متوسط (تحلیل):** VIP ساخته ولی Policy نیست؛ ترافیک رد می‌شود؛ راه: Policy Internet→VIP.

**سخت (Hairpin):** کاربر داخلی به IP Public سرور داخلی: بدون Hairpin کار نمی‌کند؛ راه: DNS داخلی (Split DNS) یا Hairpin.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall vip
 edit "WEB-VIP"
  set extintf "port1"
  set extip 203.0.113.10
  set mappedip "10.20.0.10"
  set portforward enable
  set extport 443
  set mappedport 443
 next
end
```

### ۸) Verification (اثبات صحت)

- Policy hit.
- Session NAT.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| VIP کار نمی‌کند | Policy | dst=VIP |
| برگشت نیست | SNAT/Route | NAT/Route |

### ۱۰) نکات امنیتی

- VIP فقط پورت لازم.

### ۱۱) جمع‌بندی مفهومی

- ACL≠Policy≠NAT.
- VIP+Policy.
- Hairpin.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) NAT چه می‌کند؟ *(پاسخ: 11-4-ت1)*

**ت2.** (ساده) PAT؟ *(پاسخ: 11-4-ت2)*

**ت3.** (متوسط) VIP بدون Policy؟ *(پاسخ: 11-4-ت3)*

**ت4.** (متوسط) Hairpin؟ *(پاسخ: 11-4-ت4)*

**ت5.** (سخت) Split DNS. *(پاسخ: 11-4-ت5)*

**ت6.** (سخت، طراحی) انتشار سه سرویس. *(پاسخ: 11-4-ت6)*

**Q1.** Quick quiz (English): What is the purpose of a VIP on FortiGate? *(پاسخ: 11-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PAT | Port Address Translation | ترجمه‌ی پورت |
| VIP | Virtual IP | آدرس مجازی |

- *NAT alone does not permit traffic.* ← NAT به‌تنهایی ترافیک را مجاز نمی‌کند.

### ۱۴) کارت Lab

**کارت Lab:** NAT. **Evidence:** `03-ops/nat.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0: Virtual IPs

<a id="l-11-5"></a>

## درس 11-5 — Session، Timeout، MTU/MSS و ریشه‌ی خرابی‌های TCP/UDP

**فصل 11 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۴-۲ · ≈ 9 ساعت**

> **وضعیت:** مفهومی و مستقل از نسخه؛ مثال‌های FortiOS 7.0.3 نامی (بوت‌نشده)؛ Lab «اجرا نشده»؛ دستورهای FortiGate `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. چرخه‌ی Session و Timeout را توضیح دهد.
2. MTU/MSS/PMTUD و Fragmentation را تحلیل کند.
3. علائم MTU-black-hole را بشناسد.
4. MSS-clamp را محاسبه و اعمال کند.
5. خرابی‌های Timeout را رفع کند.

### ۲) مفهوم پایه: چیست و چرا؟

کاربر می‌گوید «سایت باز می‌شود ولی بعد از لاگین گیر می‌کند» یا «SSH بعد از چند دقیقه می‌پرد». اینها اغلب MTU یا Timeout هستند نه Policy.

### ۳) توضیح عمیق فنی

#### ۱) Timeout

| پروتکل | Timeout تقریبی |
|---|---|
| TCP Established | ساعت‌ها |
| TCP Half-open | ثانیه‌ها |
| UDP | دقیقه‌ها |

Session بیکار حذف می‌شود؛ SSH/DB طولانی ⇒ Keepalive یا افزایش Timeout.

#### ۲) MTU/MSS

``` text
Ethernet MTU = 1500
MSS = MTU - 20 (IP) - 20 (TCP) = 1460
Over PPPoE/IPsec: lower MTU -> MSS ~ 1360-1400
```

#### ۳) علامت Black-hole

TCP Handshake و بسته‌های کوچک کار می‌کنند؛ بسته‌های بزرگ می‌میرند (ICMP Frag-needed فیلتر شده).

#### ۴) راه

``` text
ping -f -l 1472 203.0.113.10
! reduce until success -> path MTU
set tcp-mss-sender 1380   ! (Unverified on 7.0.3)
```

#### ۵) آزمون

بعد از تغییر، فایل بزرگ دانلود شود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| MSS-clamp | روی تونل |
| Timeout | سرویس‌محور |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** MSS = 1500−40 = 1460.

**متوسط (تحلیل):** IPsec: ping 1472 شکست؛ 1372 موفق ⇒ MTU مسیر 1400؛ MSS 1360.

**سخت (Timeout):** SSH بعد از ۵ دقیقه می‌پرد؛ Session Timeout کوتاه؛ Keepalive یا افزایش Timeout برای سرویس.

### ۷) پیاده‌سازی از مسیر CLI

``` text
ping 203.0.113.10 size 1472 df-bit yes
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- دانلود بزرگ موفق.
- Session ماندگار.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| فقط بزرگ می‌میرد | ping DF | MSS/MTU |
| SSH می‌پرد | Timeout | Keepalive |

### ۱۰) نکات امنیتی

- ICMP Frag-needed را کاملاً نبندید.

### ۱۱) جمع‌بندی مفهومی

- MSS=MTU−40.
- Black-hole.
- Timeout.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) MSS چند؟ *(پاسخ: 11-5-ت1)*

**ت2.** (ساده) علامت black-hole؟ *(پاسخ: 11-5-ت2)*

**ت3.** (متوسط) محاسبه برای MTU 1400. *(پاسخ: 11-5-ت3)*

**ت4.** (متوسط) چرا ICMP لازم؟ *(پاسخ: 11-5-ت4)*

**ت5.** (سخت) SSH می‌پرد. *(پاسخ: 11-5-ت5)*

**ت6.** (سخت، طراحی) MSS روی IPsec. *(پاسخ: 11-5-ت6)*

**Q1.** Quick quiz (English): What causes an MTU black hole? *(پاسخ: 11-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MTU | Maximum Transmission Unit | حداکثر اندازه‌ی بسته |
| MSS | Maximum Segment Size | حداکثر قطعه |

- *Lower the MSS on tunnels.* ← MSS را روی تونل‌ها کاهش دهید.

### ۱۴) کارت Lab

**کارت Lab:** MTU. **Evidence:** `03-ops/mtu.md`.

### ۱۵) منابع

- RFC 1191
- RFC 4821

<a id="l-11-6"></a>

## درس 11-6 — کارگاه طراحی Policy و ۱۰ پرسش مسیر بسته + Gate G4

**فصل 11 - روز 6 · پیش‌نیاز: درس‌های ۱۱-۱ تا ۱۱-۵ · ۶ ساعت**

### ۱) معرفی درس

جمع‌بندی فصل با طراحی Policy برای یک سازمان و پاسخ به ۱۰ پرسش مسیر بسته. این آزمون ورود به FortiGate است.

### ۲) پیش‌نیازها

درس‌های ۱۱-۱ تا ۱۱-۵.

### ۳) توضیح مفهومی

- ۱۰ پرسش: ورود؟ مبدأ/مقصد؟ Route؟ Policy؟ NAT؟ Session؟ خروج؟ دریافت؟ برگشت؟ نقطه‌ی شکست؟
- Policy Matrix با Least Privilege و Default Deny.
- Packet Walk رفت/برگشت برای ۳ جریان.
- تحلیل ۳ خرابی کاغذی (Route، Policy، NAT).

### ۴) مثال ساده

سازمان کوچک: Users/Servers/DMZ/Outside.

### ۵) مثال سازمانی

سازمان دو‌فایروالی (پیش‌نمایش فصل ۱۵).

### ۶) تصویر و توپولوژی

```text
Users | Servers | DMZ | Outside
matrix + walk + tests
```

### ۷) پیکربندی (CLI)

```text
# G4 deliverables
# 1 policy-matrix.md
# 2 packet-walk-3flows.md
# 3 fault-analysis-3cases.md
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- هر خروجی یک فایل.
- معیار قبولی: ≥ ۴ از ۵ مورد آزمون.

### ۸) تست عملکرد

- آزمون: ۵ مورد (Matrix، ۳ Walk، ۳ تحلیل، ۱۰ پرسش، MTU).

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Matrix دارای any-any |
| شواهد/دستور | Default Deny بی‌اثر |
| علت | Policy گسترده |
| رفع | تنگ‌کردن |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** هدف G4؟ *(پاسخ: 11-6-ت1)*

**ت2.** Default Deny چه شکلی دارد؟ *(پاسخ: 11-6-ت2)*

**ت3.** Packet Walk چند مرحله دارد؟ *(پاسخ: 11-6-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا قبل از FortiGate این فصل لازم است؟ *(پاسخ: 11-6-م1)*

**م2.** سناریو: ارتباط نیست؛ اولین سؤال؟ *(پاسخ: 11-6-م2)*

**معیار تسلط:** G4 ≥ ۴ از ۵.

**اشتباهات رایج:** حفظ‌کردن Policy بدون فهم.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| G4 | Gate 4 | آزمون فصل ۱۱ | ورود به FortiGate |
| Walk | Packet walk | مسیر بسته | عیب‌یابی |

| English sentence | ترجمه |
|---|---|
| Define a default deny at the end of the policy list. | در انتهای فهرست Policy یک Default Deny تعریف کنید. |
| Prove each rule with a positive and a negative test. | هر قانون را با تست مثبت و منفی ثابت کنید. |

#### کارت Lab — درس 11-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون G4 |
| 2 | پیش‌نیاز | درس‌های ۱۱-۱ تا ۱۱-۵ |
| 3 | توپولوژی | کاغذ/Markdown |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | ۵ مورد |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | Matrix دارای any-any |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | تحویل‌ها |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/g4.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="ans-11"></a>

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

**11-2-ت1** — هرچه مجاز نشده رد می‌شود.

**11-2-ت2** — حداقل دسترسی لازم.

**11-2-ت3** — تا هر مسیر مجاز مستند و قابل ممیزی باشد.

**11-2-ت4** — خاص قبل از عام.

**11-2-ت5** — Log، سرویس‌های واقعی، جایگزینی.

**11-2-ت6** — طبق جدول.

**11-2-Q1** — Any traffic not explicitly permitted is dropped.


### پاسخ‌های بازنویسی عمیق درس 11-3

**11-3-ت1** — DNAT اول.

**11-3-ت2** — ترافیک به خود فایروال.

**11-3-ت3** — چون DNAT قبل Policy انجام شده.

**11-3-ت4** — بررسی مسیر معکوس Source.

**11-3-ت5** — Admin access/Local-in.

**11-3-ت6** — طبق مراحل.

**11-3-Q1** — Before; policies match the translated destination.


### پاسخ‌های بازنویسی عمیق درس 11-4

**11-4-ت1** — آدرس را بازنویسی.

**11-4-ت2** — چند Host با یک IP.

**11-4-ت3** — رد می‌شود.

**11-4-ت4** — دسترسی داخلی به IP Public.

**11-4-ت5** — پاسخ داخلی IP داخلی.

**11-4-ت6** — VIP+Policy هرکدام.

**11-4-Q1** — To perform destination NAT for inbound access to internal servers.


### پاسخ‌های بازنویسی عمیق درس 11-5

**11-5-ت1** — 1460.

**11-5-ت2** — بسته بزرگ می‌میرد.

**11-5-ت3** — 1360.

**11-5-ت4** — PMTUD.

**11-5-ت5** — Timeout.

**11-5-ت6** — کاهش MSS.

**11-5-Q1** — Large packets with DF set are dropped and ICMP fragmentation-needed messages are blocked.

**11-6-ت1** — هدف G4؟

ورود به FortiGate با مبانی.

**11-6-ت2** — Default Deny چه شکلی دارد؟

آخرین خط deny/Implicit deny.

**11-6-ت3** — Packet Walk چند مرحله دارد؟

۷ مرحله‌ی قالب.

**11-6-م1** — چرا قبل از FortiGate این فصل لازم است؟

تا منو/دستور را بفهمیم.

**11-6-م2** — سناریو: ارتباط نیست؛ اولین سؤال؟

ورود؟ مبدأ/مقصد؟


---

<a id="ch12"></a>


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

## درس 12-1 — معماری FortiGate، اولین بوت و تأیید نسخه

**فصل 12 - روز 1 · پیش‌نیاز: فصل ۱۱ (G4) · ۶ ساعت**

### ۱) معرفی درس

FortiGate فایروال نسل جدید Fortinet با سیستم‌عامل FortiOS است. قبل از هر کار باید نسخه‌ی واقعی Image را بدانیم (چون قابلیت‌ها و دستورها به نسخه وابسته‌اند) و راه‌های دسترسی (Console، GUI، SSH) را بشناسیم.

### ۲) پیش‌نیازها

مبانی فایروال (فصل ۱۱)؛ Lab ایزوله و `vSwitch-FGT`؛ تأیید شما برای بوت اول.

### ۳) توضیح مفهومی

- FortiOS: سیستم‌عامل؛ **FortiGate-VM** نسخه‌ی مجازی (بدون ASIC سخت‌افزاری؛ کارایی پایین‌تر).
- دو حالت بازرسی: **Flow-based** (پیش‌فرض؛ سریع) و **Proxy-based** (ژرف‌تر).
- **VDOM** فایروال مجازی؛ در Lab فقط `root`.
- ورودی‌ها: Console (Telnet از PNetLab)، GUI (HTTPS)، SSH. VM به‌طور معمول روی `port1` آدرس 192.168.1.99/24 می‌گیرد (`Unverified` در 7.0.3).
- ورود اول: کاربر `admin` با رمز خالی؛ سیستم رمز جدید می‌خواهد.
- ویژگی‌های وابسته به لایسنس (UTM/FortiGuard، HA، FortiManager) در Evaluation محدود/نامعلوم است.

### ۴) مثال ساده

بوت FortiGate و دیدن نسخه، سریال و وضعیت لایسنس.

### ۵) مثال سازمانی

سازمان قبل از هر ارتقا یا طراحی نسخه و لایسنس را ثبت می‌کند (Inventory).

### ۶) تصویر و توپولوژی

```text
PC -> [mgmt net] -> FGT port1 (GUI/SSH)
PNetLab console -> FGT console (telnet)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. در مرورگر `https://<IP-port1>` را باز کنید (هشدار Certificate را در Lab بپذیرید).
2. با `admin` و رمز خالی وارد و رمز جدید (نمونه: Lab-Only-123) تعیین کنید.
3. Dashboard > Status: ویجت System Information را بخوانید (Firmware، Serial، Uptime).
4. System > Firmware: نسخه‌ی فعلی را ثبت کنید.
5. بالا-راست: `>_` Console CLI را باز کنید و `get system status` را اجرا کنید.

#### روش خط فرمان (CLI)

```text
get system status
get system performance status
get hardware status
show full-configuration | grep -f hostname
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `get system status`: Version، Build، Serial، License Status، Hostname، Operation Mode.
- `get system performance status`: CPU/Memory/Sessions.
- راستی‌آزمایی: نسخه‌ی چاپ‌شده را با «7.0.3» مقایسه و در Decision Log ثبت کنید.
- بازگشت: ندارد (فقط مشاهده).
- **هرگز** در Production `execute factoryreset` نزنید؛ بخش ۱۲-۶.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | فایروال نسل جدید با FortiOS |
| 2 | مشکلی که حل می‌کند | کنترل ترافیک و امنیت لایه ۷ |
| 3 | چه زمانی استفاده شود | لبه‌ی شبکه/بین Zoneها |
| 4 | چه زمانی استفاده نشود | وقتی فقط L3 لازم است یا لایسنس/منابع نیست |
| 5 | پیش‌نیازها | Lab ایزوله، Image |
| 6 | وابستگی به Routing/Policy/NAT | به Routing/Policy/NAT برای عبور ترافیک |
| 7 | پیاده‌سازی | Console/GUI/SSH |
| 8 | راستی‌آزمایی | `get system status` |
| 9 | عیب‌یابی | بررسی IP/allowaccess/Route |
| 10 | خطاهای رایج | تکیه بر نسخه‌ی اسمی |

### ۸) تست عملکرد

- `get system status` نسخه و `License Status` را نشان دهد؛ GUI در https://192.168.1.99 باز شود.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | GUI باز نمی‌شود |
| شواهد/دستور | Ping از PC ناموفق؛ `get system interface physical` روی کنسول: IP/وضعیت |
| علت | IP/VLAN مدیریت یا allowaccess |
| رفع | تنظیم آدرس port1 و `set allowaccess https ping ssh` |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا اول نسخه را ثبت می‌کنیم؟ *(پاسخ: 12-1-ت1)*

**ت2.** Flow-based و Proxy-based؟ *(پاسخ: 12-1-ت2)*

**ت3.** VDOM چیست؟ *(پاسخ: 12-1-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا FortiGate-VM در Evaluation محدودیت دارد؟ *(پاسخ: 12-1-م1)*

**م2.** سناریو: نسخه‌ی چاپ‌شده با 7.0.3 فرق دارد؛ چه می‌کنید؟ *(پاسخ: 12-1-م2)*

**معیار تسلط:** بوت امن، ثبت نسخه و توضیح ورودی‌های مدیریت.

**اشتباهات رایج:** تکیه بر نسخه‌ی اسمی؛ بوت بدون Snapshot/Backup.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| FortiOS | Fortinet Operating System | سیستم‌عامل FortiGate | همه‌ی دستورها |
| VDOM | Virtual Domain | فایروال مجازی | Multi-tenant |
| Flow-based | Flow-based inspection | بازرسی جریانی | پیش‌فرض |

| English sentence | ترجمه |
|---|---|
| Record the exact firmware version before any change. | قبل از هر تغییر نسخه‌ی دقیق Firmware را ثبت کنید. |
| Flow-based inspection is faster than proxy-based. | بازرسی Flow-based سریع‌تر از Proxy-based است. |

#### کارت Lab — درس 12-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | بوت اول و تأیید نسخه |
| 2 | پیش‌نیاز | فصل ۱۱ (G4) |
| 3 | توپولوژی | FGT با port1 به مدیریت |
| 4 | تجهیزات | FortiGate-VM + PC |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.1.99/24 (port1، `Unverified`) |
| 7 | وضعیت اولیه | Image دست‌نخورده |
| 8 | صورت مسئله | ثبت نسخه/سریال/لایسنس |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `get system status` |
| 11 | سناریوی خرابی | GUI باز نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | نسخه ثبت‌شده |
| 14 | معیار پذیرش | Snapshot قبل از بوت؛ نسخه در Decision Log |
| 15 | مستندات نهایی | `phase0a/fortigate_eval_tracker.md` به‌روز |
| 16 | Cleanup و بازگردانی | بازگرداندن Snapshot |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-12-2"></a>

## درس 12-2 — Interface، VLAN، Role و Administrative Access

**فصل 12 - روز 2 · پیش‌نیاز: درس ۱۲-۱ · ۶ ساعت**

### ۱) معرفی درس

هر ارتباط از یک Interface شروع می‌شود. باید Interface فیزیکی، VLAN Sub-interface، Role و دسترسی مدیریتی (allowaccess) را درست تنظیم کنیم. Gateway هر VLAN در معماری اصلی ما روی FortiGate است.

### ۲) پیش‌نیازها

درس ۱۲-۱؛ VLAN/Trunk (فصل ۳).

### ۳) توضیح مفهومی

- `port1…` Interfaceهای فیزیکی؛ VLAN Interface روی یک Interface والد با `vlanid`.
- Gateway هر VLAN = IP همان VLAN Interface (طبق طرح: `.254`).
- **Role** (LAN/WAN/DMZ/Undefined) راهنمای GUI؛ **allowaccess** مشخص می‌کند چه سرویس مدیریتی روی Interface پاسخ دهد (ping/https/ssh…).
- روی WAN فقط حداقل (ترجیحاً هیچ) allowaccess بگذارید.
- Trunk از سوییچ Cisco به یک Interface فیزیکی FortiGate وصل می‌شود؛ VLANهای مجاز و Native باید یکسان باشد.

### ۴) مثال ساده

ساخت VLAN20 با آدرس 192.168.20.254/24 روی port2.

### ۵) مثال سازمانی

چند VLAN (۱۰ مدیریت، ۲۰ کاربران، ۹۰ سرور) روی یک Trunk به سوییچ هسته.

### ۶) تصویر و توپولوژی

```text
Cisco Core --(802.1Q trunk)-- FGT port2
  VLAN20 192.168.20.254/24 ; VLAN90 192.168.90.254/24
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces > Create New > Interface.
2. Name: VLAN20؛ Type: VLAN؛ Interface: port2؛ VLAN ID: 20.
3. Role: LAN؛ Addressing mode: Manual؛ IP/Netmask: 192.168.20.254/255.255.255.0.
4. Administrative Access: فقط PING را تیک بزنید.
5. OK و سپس در لیست Interface وضعیت (Link up) را ببینید.
6. برای port2: Edit و Role را LAN و Alias را TRUNK-CORE بگذارید.

#### روش خط فرمان (CLI)

```text
config system interface
    edit "port2"
        set mode static
        set allowaccess ping
        set alias "TRUNK-CORE"
        set role lan
    next
    edit "VLAN20"
        set vdom "root"
        set interface "port2"
        set vlanid 20
        set ip 192.168.20.254 255.255.255.0
        set allowaccess ping
        set role lan
    next
end
! verify
get system interface physical
show system interface VLAN20
diagnose ip address list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `edit "VLAN20"`: نام اینترفیس VLAN؛ `set interface` والد؛ `set vlanid` شماره‌ی 802.1Q.
- `set allowaccess ping`: فقط ping (بدون مدیریت) روی VLAN کاربران.
- `get system interface physical`: وضعیت پورت‌ها (up/down، سرعت).
- بازگشت: `delete "VLAN20"` (اگر Policy/Zone ارجاع ندهد).
- نکته: حذف/تغییر Interface مورد ارجاع Policy خطا می‌دهد.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | Interface/VLAN با IP و Role |
| 2 | مشکلی که حل می‌کند | ورود ترافیک و Gateway هر VLAN |
| 3 | چه زمانی استفاده شود | هر شبکه‌ای که از FGT عبور می‌کند |
| 4 | چه زمانی استفاده نشود | Gateway روی سوییچ (Lab A) |
| 5 | پیش‌نیازها | Trunk سوییچ و VLAN در Core |
| 6 | وابستگی به Routing/Policy/NAT | Routing/Policy به همین IP وابسته‌اند |
| 7 | پیاده‌سازی | GUI Network>Interfaces یا CLI config system interface |
| 8 | راستی‌آزمایی | get system interface physical؛ ping |
| 9 | عیب‌یابی | VLAN مجاز نیست؛ ID اشتباه |
| 10 | خطاهای رایج | allowaccess روی WAN |

### ۸) تست عملکرد

- از Cisco Core ping 192.168.20.254؛ در FGT `get system arp` MAC کلاینت.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Gateway جواب نمی‌دهد |
| شواهد/دستور | `get system interface physical` پورت down؛ Cisco: Trunk allowed VLAN 20؟ |
| علت | VLAN مجاز نیست یا Native/ID اشتباه |
| رفع | اصلاح Allowed/Native؛ `set vlanid` درست |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Gateway هر VLAN روی چیست؟ *(پاسخ: 12-2-ت1)*

**ت2.** allowaccess چیست؟ *(پاسخ: 12-2-ت2)*

**ت3.** چرا WAN را سخت‌گیر می‌کنیم؟ *(پاسخ: 12-2-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا VLAN باید در Trunk Cisco مجاز باشد؟ *(پاسخ: 12-2-م1)*

**م2.** سناریو: ping از Core شکست؛ چه می‌بینید؟ *(پاسخ: 12-2-م2)*

**معیار تسلط:** ساخت VLAN Interface با GUI و CLI و اثبات با ping/get system arp.

**اشتباهات رایج:** فعال‌کردن https روی WAN؛ ناهمسانی VLAN ID.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| VLAN Interface | 802.1Q sub-interface | Interface مجازی هر VLAN | Gateway |
| allowaccess | Administrative access | سرویس‌های مدیریتی مجاز | Hardening |
| Role | Interface role | برچسب GUI | LAN/WAN |

| English sentence | ترجمه |
|---|---|
| Set the interface role and restrict administrative access. | Role Interface را تنظیم و دسترسی مدیریتی را محدود کنید. |
| Create a VLAN interface on the trunk port. | روی پورت Trunk یک VLAN Interface بسازید. |

#### کارت Lab — درس 12-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | ساخت VLANهای 20 و 90 روی FGT |
| 2 | پیش‌نیاز | درس ۱۲-۱ |
| 3 | توپولوژی | Core Cisco ↔ FGT port2 |
| 4 | تجهیزات | FGT + 1 سوییچ + VPCS |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.20.0/24 و 192.168.90.0/24 |
| 7 | وضعیت اولیه | port2 بدون IP |
| 8 | صورت مسئله | دو VLAN Interface |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping از VPCS |
| 11 | سناریوی خرابی | Gateway جواب نمی‌دهد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Gateway ‌های .254 |
| 14 | معیار پذیرش | ping Gateway موفق |
| 15 | مستندات نهایی | `02-design/fgt-interfaces.md` |
| 16 | Cleanup و بازگردانی | حذف VLAN Interfaceها |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-12-3"></a>

## درس 12-3 — Zone و Objectها: Address، Service، Group و استاندارد نام‌گذاری

**فصل 12 - روز 3 · پیش‌نیاز: درس ۱۲-۲ · ۶ ساعت**

### ۱) معرفی درس

Objectها «قطعات سازنده»ی Policy هستند. نام‌گذاری و مدل منظم Object، مدیریت Policy و عیب‌یابی را ساده می‌کند. Zone چند Interface را در یک ناحیه‌ی اعتماد جمع می‌کند.

### ۲) پیش‌نیازها

درس ۱۲-۲؛ Zone/Trust (فصل ۱۱).

### ۳) توضیح مفهومی

- **Zone:** گروه Interface؛ Policy می‌تواند بین Zone ها نوشته شود. `intrazone` ترافیک درون Zone را کنترل می‌کند.
- **Address:** Subnet/Range/FQDN؛ **Address Group**؛ **Service** (پورت‌ها) و Service Group.
- **استاندارد نام:** `NET-<نام>-<VLAN>` ، `HOST-<نام>` ، `SRV-<سرویس>` ، `GRP-…` تا Policy خوانا بماند.
- Object تکراری یا هم‌پوشان باعث خطای تحلیل می‌شود.
- Object را قبل از Policy بسازید.

### ۴) مثال ساده

Address NET-USERS-20 و Zone ZN-USERS شامل VLAN20.

### ۵) مثال سازمانی

سازمان: Zoneهای USERS، SERVERS، DMZ، WAN؛ Objectها با نام استاندارد.

### ۶) تصویر و توپولوژی

```text
ZN-USERS = {VLAN20, VLAN30}
NET-USERS-20 = 192.168.20.0/24
GRP-INTERNAL = NET-USERS-20 + NET-SERVERS-90
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces > Create New > Zone؛ Name: ZN-USERS؛ Interface Members: VLAN20.
2. Policy & Objects > Addresses > Create New > Address: Name NET-USERS-20، Type Subnet، 192.168.20.0/24.
3. Policy & Objects > Addresses > Create New > Address Group: GRP-INTERNAL.
4. Policy & Objects > Services > Create New > Service: TCP-8443 (TCP 8443).
5. هر Object را با «References» (آیکن) بررسی کنید.

#### روش خط فرمان (CLI)

```text
config system zone
    edit "ZN-USERS"
        set interface "VLAN20"
    next
end
config firewall address
    edit "NET-USERS-20"
        set subnet 192.168.20.0 255.255.255.0
    next
end
config firewall addrgrp
    edit "GRP-INTERNAL"
        set member "NET-USERS-20"
    next
end
config firewall service custom
    edit "TCP-8443"
        set tcp-portrange 8443
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Zone فقط Interfaceهای بدون Policy فعلی را می‌پذیرد (اگر خطا داد Policyهای ارجاع‌دهنده را بررسی کنید).
- Address با `set subnet`؛ Group با `set member`.
- Service سفارشی با `set tcp-portrange` (سینتکس `Unverified` در 7.0.3).
- راستی‌آزمایی: `show firewall address` و GUI > Policy & Objects.
- بازگشت: `delete` مورد نظر.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | Zone/Object برای Policy |
| 2 | مشکلی که حل می‌کند | ساده و خوانا کردن Policy |
| 3 | چه زمانی استفاده شود | همیشه قبل از Policy |
| 4 | چه زمانی استفاده نشود | با Object هم‌پوشان یا نامنظم |
| 5 | پیش‌نیازها | Interfaceها |
| 6 | وابستگی به Routing/Policy/NAT | Policy و Routing به Object ارجاع می‌دهند |
| 7 | پیاده‌سازی | GUI Policy&Objects یا CLI config firewall |
| 8 | راستی‌آزمایی | show firewall address |
| 9 | عیب‌یابی | References؛ حذف نمی‌شود |
| 10 | خطاهای رایج | نام‌گذاری ناهمگون |

### ۸) تست عملکرد

- `show system zone`؛ `show firewall address` ورودی‌ها را نشان دهد.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | نمی‌توان Interface را به Zone اضافه کرد |
| شواهد/دستور | پیام «referenced by policy» |
| علت | Interface در Policy استفاده شده |
| رفع | Policyها را به Zone منتقل کنید یا Interface را آزاد کنید |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Zone چه فایده‌ای دارد؟ *(پاسخ: 12-3-ت1)*

**ت2.** چرا نام‌گذاری استاندارد؟ *(پاسخ: 12-3-ت2)*

**ت3.** intrazone؟ *(پاسخ: 12-3-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Object هم‌پوشان خطرناک است؟ *(پاسخ: 12-3-م1)*

**م2.** سناریو: Interface در Zone اضافه نمی‌شود؛ چرا؟ *(پاسخ: 12-3-م2)*

**معیار تسلط:** ساخت Zone و Object با GUI/CLI و نام‌گذاری استاندارد.

**اشتباهات رایج:** Object بدون استاندارد؛ تداخل Subnet.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Zone | Security zone | گروه Interface | Policy |
| Address object | Firewall address | تعریف Subnet/Host | Policy |
| Service | Firewall service | تعریف پورت/پروتکل | Policy |

| English sentence | ترجمه |
|---|---|
| Use a consistent naming standard for all objects. | برای همه‌ی Objectها استاندارد نام‌گذاری ثابت به‌کار ببرید. |
| Zones group interfaces with the same trust level. | Zoneها Interfaceهای هم‌سطح اعتماد را گروه می‌کنند. |

#### کارت Lab — درس 12-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Zone و Objectهای استاندارد |
| 2 | پیش‌نیاز | درس ۱۲-۲ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | VLAN20/90 |
| 7 | وضعیت اولیه | Interfaces موجود |
| 8 | صورت مسئله | Zone/Address/Service |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `show firewall address` |
| 11 | سناریوی خرابی | نمی‌توان Interface را به Zone اضافه کرد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Objectها ساخته |
| 14 | معیار پذیرش | نام‌ها استاندارد |
| 15 | مستندات نهایی | `02-design/fgt-objects.md` |
| 16 | Cleanup و بازگردانی | حذف Objectها |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-12-4"></a>

## درس 12-4 — Static Route، Default Route و Policy Route

**فصل 12 - روز 4 · پیش‌نیاز: درس ۱۲-۳ · ۶ ساعت**

### ۱) معرفی درس

FortiGate هم مثل روتر باید مسیر داشته باشد. Default به سمت ISP، Static برای شبکه‌های دور و Policy Route برای استثناها. تفاوت Distance و Priority را باید بدانید.

### ۲) پیش‌نیازها

درس‌های ۱۲-۲، ۱۲-۳؛ Routing (فصل‌های ۵ و ۱۰).

### ۳) توضیح مفهومی

- **Static Route**: مقصد، Gateway، Interface خروجی.
- **Distance** (AD) کمتر = بهتر؛ **Priority** برای انتخاب بین مسیرهای هم‌Distance (کمتر بهتر) — با Priority یکسان ECMP.
- **Policy Route:** بر اساس مبدأ/سرویس، قبل از جدول معمولی (مثل PBR).
- جدول مسیر واقعی: `get router info routing-table all` (فقط Active)؛ `show router static` (Config).
- RPF/Asymmetric: مسیر برگشت را حتماً بررسی کنید (فصل ۱۰).

### ۴) مثال ساده

Default 0.0.0.0/0 به Gateway ISP 203.0.113.1 از port1.

### ۵) مثال سازمانی

Static برای شبکه‌ی داخلی پشت Core؛ Default برای اینترنت.

### ۶) تصویر و توپولوژی

```text
FGT port1(WAN) -> ISP 203.0.113.1
FGT VLAN20 -> Core -> 10.20.0.0/16
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Static Routes > Create New.
2. Destination: Subnet 0.0.0.0/0.0.0.0؛ Gateway Address: 203.0.113.1؛ Interface: port1؛ Administrative Distance 10؛ Priority 1.
3. Comments: default-to-ISP؛ OK.
4. Monitor > Routing Monitor: ردیف Static را ببینید.
5. Network > Policy Routes (اگر لازم): Incoming Interface/Source/Destination و Gateway.

#### روش خط فرمان (CLI)

```text
config router static
    edit 1
        set dst 0.0.0.0 0.0.0.0
        set gateway 203.0.113.1
        set device "port1"
        set distance 10
        set priority 1
        set comment "default-to-ISP"
    next
    edit 2
        set dst 10.20.0.0 255.255.0.0
        set gateway 192.168.20.1
        set device "VLAN20"
    next
end
! verify
get router info routing-table all
get router info routing-table details 10.20.0.5
show router static
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `set dst`+`set gateway`+`set device`: مسیر.
- `distance` و `priority`: انتخاب مسیر؛ مقدار کمتر بهتر.
- راستی‌آزمایی: `routing-table all` ردیف `S*` برای Default.
- بازگشت: `delete 1`.
- هشدار: حذف Default از راه دور اتصال را قطع می‌کند.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | Static/Default/Policy Route |
| 2 | مشکلی که حل می‌کند | هدایت ترافیک به مقصد |
| 3 | چه زمانی استفاده شود | هر FGT نیاز به Default/مسیر دارد |
| 4 | چه زمانی استفاده نشود | وقتی Routing پویا مناسب‌تر است |
| 5 | پیش‌نیازها | Interfaceهای بالا |
| 6 | وابستگی به Routing/Policy/NAT | Policy و NAT بدون Route کار نمی‌کنند |
| 7 | پیاده‌سازی | Network>Static Routes یا config router static |
| 8 | راستی‌آزمایی | get router info routing-table all |
| 9 | عیب‌یابی | Gateway ناقابل‌دسترس |
| 10 | خطاهای رایج | Distance/Priority اشتباه |

### ۸) تست عملکرد

- `execute ping 8.8.8.8` از FGT؛ `execute traceroute`.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Default در جدول نیست |
| شواهد/دستور | `get router info routing-table all`: ردیف S* نیست |
| علت | Interface خروجی down یا Gateway ناقابل‌دسترس |
| رفع | اصلاح Gateway/Interface؛ `set distance` |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Distance و Priority؟ *(پاسخ: 12-4-ت1)*

**ت2.** کدام دستور جدول واقعی را می‌دهد؟ *(پاسخ: 12-4-ت2)*

**ت3.** Policy Route چه زمانی؟ *(پاسخ: 12-4-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا `show router static` همان جدول مسیر نیست؟ *(پاسخ: 12-4-م1)*

**م2.** سناریو: Default Static هست ولی Down؛ چرا؟ *(پاسخ: 12-4-م2)*

**معیار تسلط:** تنظیم Default/Static با GUI و CLI و اثبات با routing-table و ping.

**اشتباهات رایج:** اشتباه Distance/Priority؛ حذف Default.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Distance | Administrative distance | اعتبار مسیر | انتخاب مسیر |
| Priority | Route priority | تای‌بریک مسیرهای هم‌Distance | ECMP |
| Policy route | Policy route | مسیر بر اساس سیاست | استثنا |

| English sentence | ترجمه |
|---|---|
| Verify the active routing table, not only the configuration. | جدول مسیر فعال را بررسی کنید، نه فقط Config را. |
| A lower distance wins. | Distance کمتر برنده است. |

#### کارت Lab — درس 12-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Default و Static |
| 2 | پیش‌نیاز | درس ۱۲-۳ |
| 3 | توپولوژی | FGT + Core + ISP-Sim |
| 4 | تجهیزات | FGT،R-ISP،Core |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 203.0.113.0/30؛ 192.168.20.0/24 |
| 7 | وضعیت اولیه | Interfaces بالا |
| 8 | صورت مسئله | Default + Static |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `execute ping` |
| 11 | سناریوی خرابی | Default در جدول نیست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | S* در جدول |
| 14 | معیار پذیرش | ping 8.8.8.8 از FGT |
| 15 | مستندات نهایی | `02-design/fgt-routing.md` |
| 16 | Cleanup و بازگردانی | حذف مسیرها |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-12-5"></a>

## درس 12-5 — Admin، RBAC و سخت‌سازی مدیریت

**فصل 12 - روز 5 · پیش‌نیاز: درس ۱۲-۴ · ۶ ساعت**

### ۱) معرفی درس

دسترسی مدیریتی به فایروال حساس‌ترین دسترسی است. با Admin Profile، Trusted Host، Timeout و محدودیت allowaccess آن را امن می‌کنیم. اشتباه می‌تواند خودتان را بیرون بگذارد.

### ۲) پیش‌نیازها

درس‌های ۱۲-۲، ۱۲-۴؛ AAA (فصل ۸).

### ۳) توضیح مفهومی

- **Admin Profile (accprofile):** سطح دسترسی هر گروه (Read-only، Super-admin).
- **Trusted Host:** فقط از آدرس‌های مشخص ورود مجاز است.
- `admintimeout`، قفل بعد از تلاش‌های ناموفق (`admin-lockout-*`)، تغییر پورت/غیرفعال‌سازی HTTP.
- **اصل حداقل دسترسی:** Admin روزمره Super-admin نباشد.
- قبل از Trusted Host بکاپ + راه جایگزین (Console).

### ۴) مثال ساده

کاربر netadmin فقط از 192.168.100.0/24.

### ۵) مثال سازمانی

سازمان: گروه‌های NetAdmin، SecAdmin، ReadOnly؛ ۲FA مفهومی.

### ۶) تصویر و توپولوژی

```text
Admin PC (192.168.100.x) --https/ssh--> FGT mgmt (trusted host only)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Admin Profiles > Create New: PROF-READONLY با Read برای Network/Firewall/System/Log.
2. System > Administrators > Create New > Administrator: Username auditor؛ Type Local User؛ Password نمونه؛ Administrator Profile PROF-READONLY.
3. Restrict login to trusted hosts را فعال و 192.168.100.0/24 را وارد کنید.
4. System > Settings: Idle timeout را 10 دقیقه کنید.
5. با کاربر جدید از Subnet مجاز وارد و تغییر را امتحان کنید.

#### روش خط فرمان (CLI)

```text
config system accprofile
    edit "PROF-READONLY"
        set sysgrp read
        set netgrp read
        set fwgrp read
        set loggrp read
    next
end
config system admin
    edit "auditor"
        set accprofile "PROF-READONLY"
        set trusthost1 192.168.100.0 255.255.255.0
        set password <SAMPLE-PASSWORD>
    next
end
config system global
    set admintimeout 10
    set admin-lockout-threshold 3
    set admin-lockout-duration 300
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Profile با گروه‌های مجوز (`sysgrp`, `netgrp`, `fwgrp` ...).
- `trusthost1`: فقط آن Subnet؛ **هشدار:** اشتباه = قفل شدن؛ Console نجات می‌دهد.
- `admintimeout 10`: خروج خودکار بعد از ۱۰ دقیقه.
- راستی‌آزمایی: ورود با `auditor` از Subnet مجاز موفق و از دیگر شبکه‌ها ناموفق.
- بازگشت: `delete "auditor"` و حذف trusthost.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | Admin/Profile/Trusted Host |
| 2 | مشکلی که حل می‌کند | کنترل دسترسی مدیریت |
| 3 | چه زمانی استفاده شود | همیشه |
| 4 | چه زمانی استفاده نشود | Super-admin روزمره |
| 5 | پیش‌نیازها | Console برای نجات |
| 6 | وابستگی به Routing/Policy/NAT | وابسته به allowaccess Interface |
| 7 | پیاده‌سازی | GUI System>Administrators |
| 8 | راستی‌آزمایی | ورود موفق/ناموفق |
| 9 | عیب‌یابی | Trusted host اشتباه |
| 10 | خطاهای رایج | رمز ضعیف |

### ۸) تست عملکرد

- ورود SSH/GUI با کاربر read-only؛ تلاش تغییر باید رد شود.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | بعد از Trusted Host بیرون ماندم |
| شواهد/دستور | ورود از آدرس دیگر رد می‌شود |
| علت | Trusted Host فقط یک Subnet |
| رفع | Console: `config system admin / edit X / unset trusthost1` |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Trusted Host چیست؟ *(پاسخ: 12-5-ت1)*

**ت2.** چرا Admin روزمره Super-admin نباشد؟ *(پاسخ: 12-5-ت2)*

**ت3.** Profile چه می‌کند؟ *(پاسخ: 12-5-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا قبل از Trusted Host راه جایگزین لازم است؟ *(پاسخ: 12-5-م1)*

**م2.** سناریو: auditor می‌تواند Config تغییر دهد؛ علت؟ *(پاسخ: 12-5-م2)*

**معیار تسلط:** ساخت Admin محدود با GUI/CLI و اثبات عدم دسترسی خارج از Trusted Host.

**اشتباهات رایج:** قفل‌شدن؛ رمز ساده؛ ماندن روی Super-admin.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Trusted host | Admin trusted host | آدرس مجاز ورود | مدیریت |
| accprofile | Access profile | پروفایل مجوز | RBAC |
| RBAC | Role-Based Access Control | دسترسی بر اساس نقش | Least privilege |

| English sentence | ترجمه |
|---|---|
| Restrict administrator logins to trusted hosts. | ورود ادمین را به Trusted Hostها محدود کنید. |
| Never use a super-admin account for daily work. | هرگز از حساب Super-admin برای کار روزمره استفاده نکنید. |

#### کارت Lab — درس 12-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Admin محدود |
| 2 | پیش‌نیاز | درس ۱۲-۴ |
| 3 | توپولوژی | FGT + PC |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.100.0/24 |
| 7 | وضعیت اولیه | Admin پیش‌فرض |
| 8 | صورت مسئله | auditor read-only |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ورود |
| 11 | سناریوی خرابی | بعد از Trusted Host بیرون ماندم |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | دسترسی محدود |
| 14 | معیار پذیرش | رد تغییر و رد آدرس نامجاز |
| 15 | مستندات نهایی | `03-ops/fgt-admin-standard.md` (بدون رمز) |
| 16 | Cleanup و بازگردانی | حذف کاربر |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-12-6"></a>

## درس 12-6 — Backup/Restore، Firmware و Lifecycle

**فصل 12 - روز 6 · پیش‌نیاز: درس ۱۲-۴ · ۶ ساعت**

### ۱) معرفی درس

پیش از هر تغییر بکاپ و بعد از آن بازیابی آزموده‌شده. ارتقای Firmware و آسیب‌پذیری‌های نسخه‌ی ۷٫۰ را هم باید بشناسید. راهنمای شما در `phase0a/FortiGate_Backup_Restore_Runbook.md` است.

### ۲) پیش‌نیازها

درس ۱۲-۵.

### ۳) توضیح مفهومی

- **Backup**: GUI (Admin menu > Configuration > Backup) یا CLI `execute backup config ...`.
- **Restore**: `execute restore config ...`؛ بعد از Restore دستگاه Reboot می‌شود.
- Config شامل Hash رمز است؛ فایل را در جای امن و **بیرون Git** نگه دارید.
- نسخه 7.0.3 در بازه‌ی چند CVE شناخته‌شده است (CVE-2022-40684، 2022-42475، 2023-27997) ← فقط Lab ایزوله.
- قبل از ارتقا: Release Notes، Upgrade Path، Backup، Test Plan، Rollback Plan (`Unverified` مسیر دقیق).

### ۴) مثال ساده

بکاپ به TFTP و Restore.

### ۵) مثال سازمانی

سازمان: بکاپ شبانه + بعد از هر Change + نسخه‌ی خارج از سایت.

### ۶) تصویر و توپولوژی

```text
FGT --backup--> TFTP/USB/GUI download
Restore -> reboot -> verify
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Admin menu (بالا-راست) > Configuration > Backup؛ Backup to: Local PC.
2. نام فایل را دریافت و در مسیر امن (غیر Git) نگه دارید.
3. Admin menu > Configuration > Restore برای بازیابی (Reboot می‌شود).
4. System > Firmware: نسخه‌ی فعلی؛ **ارتقا را بدون بکاپ نزنید.**
5. System > Config > Revisions (اگر فعال باشد) را بررسی کنید.

#### روش خط فرمان (CLI)

```text
execute backup config tftp FGT-HQ-20261126-1000.conf 192.168.90.11
! restore (WARNING: reboots; test in lab first)
execute restore config tftp FGT-HQ-20261126-1000.conf 192.168.90.11
! compare
show full-configuration | grep -c config
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `execute backup config tftp <file> <server>`: Config را روی سرور TFTP ذخیره می‌کند.
- نام فایل = دستگاه + تاریخ + ساعت.
- `execute restore config ...`: جایگزین‌کننده؛ **اثر:** Reboot و بازنویسی کامل Config؛ پیش‌نیاز: بکاپ از وضع فعلی.
- راستی‌آزمایی: بعد از Restore `get system status` و بررسی Policyها.
- بازگشت: Restore بکاپ قبلی.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | Backup/Restore/Firmware |
| 2 | مشکلی که حل می‌کند | برگشت امن |
| 3 | چه زمانی استفاده شود | قبل از هر تغییر و ارتقا |
| 4 | چه زمانی استفاده نشود | Restore بدون بکاپ فعلی |
| 5 | پیش‌نیازها | Backup سالم |
| 6 | وابستگی به Routing/Policy/NAT | Config وابسته به نسخه |
| 7 | پیاده‌سازی | GUI/CLI |
| 8 | راستی‌آزمایی | Restore آزمایشی |
| 9 | عیب‌یابی | Version mismatch |
| 10 | خطاهای رایج | فایل بکاپ در Git |

### ۸) تست عملکرد

- بکاپ بگیرید، یک Object تست بسازید، Restore کنید و ناپدید شدن Object را ثابت کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Restore ناموفق |
| شواهد/دستور | Reboot ولی Config جدید نیست/خطای Version |
| علت | نسخه‌ی فایل بکاپ سازگار نیست |
| رفع | Restore روی همان نسخه؛ مراجعه به Release Notes |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا فایل بکاپ را بیرون از Git می‌گذاریم؟ *(پاسخ: 12-6-ت1)*

**ت2.** Restore چه اثری دارد؟ *(پاسخ: 12-6-ت2)*

**ت3.** چرا نسخه‌ی 7.0.3 فقط در Lab؟ *(پاسخ: 12-6-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا بکاپ آزموده‌نشده بکاپ نیست؟ *(پاسخ: 12-6-م1)*

**م2.** سناریو: بعد از ارتقا مشکل؛ اولین اقدام؟ *(پاسخ: 12-6-م2)*

**معیار تسلط:** بکاپ/Restore موفق و ثبت مراحل؛ Plan ارتقا.

**اشتباهات رایج:** Restore بدون بکاپ از وضع فعلی؛ فایل بکاپ در Git.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Backup | Configuration backup | ذخیره‌ی Config | Change |
| Firmware | Firmware | نرم‌افزار دستگاه | Lifecycle |
| PSIRT | Product Security Incident Response Team | هشدارهای امنیتی | Patch |

| English sentence | ترجمه |
|---|---|
| Always back up the configuration before an upgrade. | همیشه قبل از ارتقا از Config بکاپ بگیرید. |
| Test the restore procedure regularly. | روش Restore را مرتب آزمایش کنید. |

#### کارت Lab — درس 12-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | بکاپ و Restore |
| 2 | پیش‌نیاز | درس ۱۲-۴ |
| 3 | توپولوژی | FGT + TFTP |
| 4 | تجهیزات | FGT + Linux TFTP |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.90.11 |
| 7 | وضعیت اولیه | Baseline آماده |
| 8 | صورت مسئله | بکاپ/Restore |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `get system status` |
| 11 | سناریوی خرابی | Restore ناموفق |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Object ناپدید می‌شود |
| 14 | معیار پذیرش | Restore موفق |
| 15 | مستندات نهایی | `03-ops/fgt-backup-log.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-12-7"></a>

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

## درس 12-7 — آزمون پایان فصل ۱۲ و تحلیل خطا (مدیریت قفل‌شده)

**فصل 12 - روز 7 · پیش‌نیاز: درس‌های ۱۲-۱ تا ۱۲-۵ · ۶ ساعت**

### ۱) معرفی درس

ساخت Baseline کامل FortiGate و عیب‌یابی خطایی که شایع است: قفل‌شدن از GUI. این درس ارزیابی فصل است.

### ۲) پیش‌نیازها

درس‌های ۱۲-۱ تا ۱۲-۵.

### ۳) توضیح مفهومی

- Baseline: Interface/VLAN، Zone/Object، Default/Static، Admin امن، بکاپ.
- سناریوی خرابی: Trusted Host اشتباه، allowaccess بسته، Route Default حذف‌شده.
- روش: Console ← `show` ← اصلاح ← بکاپ.
- مستندسازی As-Built FortiGate (جدول Interface/Zone/Object/Route/Admin).

### ۴) مثال ساده

ساخت Baseline و ثبت As-Built.

### ۵) مثال سازمانی

سازمان: Baseline استاندارد برای هر FortiGate جدید.

### ۶) تصویر و توپولوژی

```text
Baseline: Interfaces + Zones + Objects + Routes + Admin + Backup
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces: همه‌ی Interfaceها را مرور.
2. Policy & Objects > Addresses و Zones را مرور.
3. Network > Static Routes؛ System > Administrators.
4. Admin menu > Configuration > Backup برای نسخه‌ی As-Built.
5. Dashboard > Status برای ثبت نسخه.

#### روش خط فرمان (CLI)

```text
! as-built collection
show system interface
show system zone
show firewall address
show router static
show system admin
get system status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خروجی هر دستور در As-Built ثبت می‌شود (بدون رمز/Hash در Git).
- معیار: ≥ ۴ از ۵ مورد آزمون.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | Baseline |
| 2 | مشکلی که حل می‌کند | پایه‌ی هر پروژه |
| 3 | چه زمانی استفاده شود | همیشه |
| 4 | چه زمانی استفاده نشود | بدون بکاپ |
| 5 | پیش‌نیازها | تکمیل درس‌های قبل |
| 6 | وابستگی به Routing/Policy/NAT | — |
| 7 | پیاده‌سازی | GUI+CLI |
| 8 | راستی‌آزمایی | get/show |
| 9 | عیب‌یابی | بیرون‌ماندن |
| 10 | خطاهای رایج | رمز در فایل |

### ۸) تست عملکرد

- آزمون: ۵ مورد (Interface/VLAN، Zone/Object، Route، Admin، Backup/Restore).

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | از GUI بیرون ماندم |
| شواهد/دستور | HTTPS رد می‌شود؛ ping OK |
| علت | allowaccess/Trusted host |
| رفع | Console و اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Baseline چیست؟ *(پاسخ: 12-7-ت1)*

**ت2.** As-Built چیست؟ *(پاسخ: 12-7-ت2)*

**ت3.** اولین گام وقتی GUI قفل است؟ *(پاسخ: 12-7-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا As-Built بدون رمز؟ *(پاسخ: 12-7-م1)*

**م2.** سناریو: Default حذف شد؛ چه می‌کنید؟ *(پاسخ: 12-7-م2)*

**معیار تسلط:** Baseline + As-Built + رفع یک قفل مدیریت.

**اشتباهات رایج:** As-Built ناقص؛ رمز در فایل.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| As-Built | As-built documentation | مستند وضعیت نهایی | تحویل |
| Baseline | Configuration baseline | پیکربندی مرجع | استاندارد |

| English sentence | ترجمه |
|---|---|
| Document the final configuration as-built. | پیکربندی نهایی را به‌صورت As-Built مستند کنید. |
| Use the console when remote access is lost. | وقتی دسترسی از راه دور از دست رفت از Console استفاده کنید. |

#### کارت Lab — درس 12-7

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Baseline FortiGate (G-FGT1) |
| 2 | پیش‌نیاز | درس‌های ۱۲-۱ تا ۱۲-۵ |
| 3 | توپولوژی | FGT + Core + PC |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق درس‌های قبل |
| 7 | وضعیت اولیه | FGT تازه |
| 8 | صورت مسئله | Baseline کامل |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | show … |
| 11 | سناریوی خرابی | از GUI بیرون ماندم |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | As-Built |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/fgt-asbuilt-1.md` |
| 16 | Cleanup و بازگردانی | Snapshot/Restore |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-12"></a>

## پاسخ‌های فصل 12

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**12-1-ت1** — چرا اول نسخه را ثبت می‌کنیم؟

قابلیت‌ها و دستورها به نسخه بستگی دارد؛ ثبت مبنای عیب‌یابی و ارتقاست.

**12-1-ت2** — Flow-based و Proxy-based؟

Flow سریع و بدون بافر کامل؛ Proxy عمیق‌تر و کندتر.

**12-1-ت3** — VDOM چیست؟

فایروال مجازی مستقل داخل یک دستگاه.

**12-1-م1** — چرا FortiGate-VM در Evaluation محدودیت دارد؟

لایسنس/Trial؛ بعضی قابلیت‌ها (UTM، HA) وابسته به Subscription هستند.

**12-1-م2** — سناریو: نسخه‌ی چاپ‌شده با 7.0.3 فرق دارد؛ چه می‌کنید؟

نسخه‌ی واقعی را مبنا قرار دهید و دستورها را با Release Notes همان نسخه تطبیق دهید.

**12-2-ت1** — Gateway هر VLAN روی چیست؟

روی VLAN Interface فایروال (معماری اصلی).

**12-2-ت2** — allowaccess چیست؟

سرویس‌های مدیریتی مجاز روی آن Interface.

**12-2-ت3** — چرا WAN را سخت‌گیر می‌کنیم؟

سطح حمله به اینترنت.

**12-2-م1** — چرا VLAN باید در Trunk Cisco مجاز باشد؟

وگرنه فریم تگ‌دار نمی‌رسد.

**12-2-م2** — سناریو: ping از Core شکست؛ چه می‌بینید؟

Trunk/VLAN مجاز و وضعیت پورت FGT.

**12-3-ت1** — Zone چه فایده‌ای دارد؟

سیاست‌گذاری گروهی بین ناحیه‌های اعتماد.

**12-3-ت2** — چرا نام‌گذاری استاندارد؟

خوانایی Policy و کاهش خطا.

**12-3-ت3** — intrazone؟

کنترل ترافیک بین Interfaceهای داخل یک Zone.

**12-3-م1** — چرا Object هم‌پوشان خطرناک است؟

Match نامنتظر و تحلیل مبهم.

**12-3-م2** — سناریو: Interface در Zone اضافه نمی‌شود؛ چرا؟

Policy به آن ارجاع دارد.

**12-4-ت1** — Distance و Priority؟

Distance بین منابع؛ Priority بین Staticهای هم‌Distance.

**12-4-ت2** — کدام دستور جدول واقعی را می‌دهد؟

get router info routing-table all.

**12-4-ت3** — Policy Route چه زمانی؟

استثنا بر اساس مبدأ/سرویس.

**12-4-م1** — چرا `show router static` همان جدول مسیر نیست؟

Config است؛ جدول واقعی فقط مسیرهای Active را دارد.

**12-4-م2** — سناریو: Default Static هست ولی Down؛ چرا؟

Gateway/Interface ناقابل‌دسترس.

**12-5-ت1** — Trusted Host چیست؟

محدودیت آدرس مبدأ ورود Admin.

**12-5-ت2** — چرا Admin روزمره Super-admin نباشد؟

Least Privilege.

**12-5-ت3** — Profile چه می‌کند؟

سطح دسترسی هر ادمین.

**12-5-م1** — چرا قبل از Trusted Host راه جایگزین لازم است؟

احتمال قفل‌شدن.

**12-5-م2** — سناریو: auditor می‌تواند Config تغییر دهد؛ علت؟

Profile اشتباه/Super-admin.

**12-6-ت1** — چرا فایل بکاپ را بیرون از Git می‌گذاریم؟

Hash رمز و کلیدها در آن است.

**12-6-ت2** — Restore چه اثری دارد؟

بازنویسی کامل Config و Reboot.

**12-6-ت3** — چرا نسخه‌ی 7.0.3 فقط در Lab؟

CVEهای شناخته‌شده.

**12-6-م1** — چرا بکاپ آزموده‌نشده بکاپ نیست؟

ممکن است Restore نشود.

**12-6-م2** — سناریو: بعد از ارتقا مشکل؛ اولین اقدام؟

Rollback به Firmware/Config قبلی طبق Plan.

**12-7-ت1** — Baseline چیست؟

پیکربندی استاندارد اولیه.

**12-7-ت2** — As-Built چیست؟

مستند وضعیت ساخته‌شده.

**12-7-ت3** — اولین گام وقتی GUI قفل است؟

Console.

**12-7-م1** — چرا As-Built بدون رمز؟

امنیت و اشتراک‌پذیری.

**12-7-م2** — سناریو: Default حذف شد؛ چه می‌کنید؟

Console + بازگرداندن Route.


---

<a id="end4"></a>


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
