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

> **نسخه‌ی اصلاح‌شده (v3.5):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۱۰-۸، ۱۰-۹، ۱۱-۰، ۱۱-۷، ۱۲-۰، ۱۲-۸، ۱۲-۹ (دسته‌های B و A). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

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

## درس 10-1 — Redistribution: مفهوم و Seed Metric

**فصل 10 - روز 1 · پیش‌نیاز: فصل ۹، ۶ · ۶ ساعت**

### ۱) معرفی درس

Redistribution مسیرهای یک پروتکل (مثلاً Static یا BGP) را وارد پروتکل دیگر (OSPF) می‌کند. در شبکه‌ی واقعی بین مرکز، شعبه‌ها و ISP لازم است؛ اشتباه آن حلقه‌ی مسیریابی می‌سازد.

### ۲) پیش‌نیازها

OSPF، Static، BGP (فصل‌های ۵، ۶، ۹).

### ۳) توضیح مفهومی

- هر پروتکل Metric خودش را دارد؛ هنگام ورود به پروتکل دیگر باید **Seed Metric** داده شود.
- OSPF: `redistribute <proto> subnets metric <n> metric-type <1|2>`؛ بدون `subnets` فقط Classful وارد می‌شود.
- Routeهای خارجی در OSPF: E2 (Metric ثابت) یا E1 (Metric + هزینه‌ی داخلی).
- AD پروتکل مبدأ در پروتکل مقصد اهمیتی ندارد؛ مسیر با AD مقصد نصب می‌شود (E2 = AD 110).
- Redistribution فقط مسیرهای **در Route Table** را وارد می‌کند.

### ۴) مثال ساده

R2 مسیر Static به شبکه‌ی ISP دارد و آن را داخل OSPF پخش می‌کند.

### ۵) مثال سازمانی

Edge مسیر Default را از BGP می‌گیرد و داخل OSPF برای کل Campus پخش می‌کند.

### ۶) تصویر و توپولوژی

```text
ISP --BGP-- Edge --OSPF-- Core --OSPF-- Access
      redistribute bgp into ospf (default only)
```

### ۷) پیکربندی (CLI)

```text
router ospf 1
 redistribute static subnets metric 20 metric-type 2
!
! verify
show ip ospf database external
show ip route ospf
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `redistribute static subnets`: Routeهای Static را به‌صورت External وارد می‌کند.
- `metric 20 metric-type 2`: Seed Metric؛ E2 در همه‌ی مقصدها همان 20 می‌ماند.
- راستی‌آزمایی: روی روتر دیگر `O E2` دیده شود.
- بازگشت: `no redistribute static`.

### ۸) تست عملکرد

- `show ip route` روی Core: `O E2 ...`؛ `show ip ospf database external` LSA نوع ۵.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Route وارد OSPF نمی‌شود |
| شواهد/دستور | `show ip route <prefix>` روی ASBR: نیست؛ `redistribute` بدون `subnets` |
| علت | مسیر مبدأ در Route Table نیست یا subnets فراموش شده |
| رفع | اضافه‌کردن `subnets` و بررسی مسیر مبدأ |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا `subnets` لازم است؟ *(پاسخ: 10-1-ت1)*

**ت2.** E1 و E2؟ *(پاسخ: 10-1-ت2)*

**ت3.** چه چیزی redistribute می‌شود؟ *(پاسخ: 10-1-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Seed Metric لازم است؟ *(پاسخ: 10-1-م1)*

**م2.** سناریو: Route Static در OSPF دیده نمی‌شود؛ دو بررسی؟ *(پاسخ: 10-1-م2)*

**معیار تسلط:** تنظیم و راستی‌آزمایی redistribute با توضیح E1/E2.

**اشتباهات رایج:** فراموشی subnets؛ فرض اینکه Route خودکار می‌آید.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Redistribution | Route redistribution | انتقال مسیر بین پروتکل‌ها | Edge/ASBR |
| ASBR | Autonomous System Boundary Router | روتر Redistribute‌کننده | لبه‌ی OSPF |
| E2 | OSPF External Type 2 | Metric ثابت | Default از ISP |

| English sentence | ترجمه |
|---|---|
| Redistribute static routes into OSPF with a seed metric. | Routeهای Static را با Seed Metric وارد OSPF کنید. |
| Only routes present in the routing table are redistributed. | فقط مسیرهای موجود در Route Table redistribute می‌شوند. |

#### کارت Lab — درس 10-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | redistribute static به OSPF |
| 2 | پیش‌نیاز | فصل ۹، ۶ |
| 3 | توپولوژی | R1-R2-R3 + Static به ISP |
| 4 | تجهیزات | ۳ vIOS |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | 10.0.12.0/30 و ... |
| 7 | وضعیت اولیه | OSPF سالم |
| 8 | صورت مسئله | Static به OSPF |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `show ip route ospf` |
| 11 | سناریوی خرابی | Route وارد OSPF نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | O E2 در R3 |
| 14 | معیار پذیرش | Route E2 دیده شود |
| 15 | مستندات نهایی | `03-ops/redistribution.md` |
| 16 | Cleanup و بازگردانی | حذف redistribute |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-10-2"></a>

## درس 10-2 — Redistribution دوطرفه و جلوگیری از حلقه با Tag

**فصل 10 - روز 2 · پیش‌نیاز: درس ۱۰-۱ · ۶ ساعت**

### ۱) معرفی درس

وقتی دو نقطه‌ی Redistribution بین دو پروتکل داریم، مسیر می‌تواند برگردد و حلقه یا مسیر بد بسازد. Tag + Route-Map راه استاندارد جلوگیری است.

### ۲) پیش‌نیازها

درس ۱۰-۱؛ Route-Map (درس ۹-۴).

### ۳) توضیح مفهومی

- حلقه: مسیر OSPF→BGP و دوباره BGP→OSPF با AD/Metric بدتر.
- راه حل: هنگام ورود **Tag** بزنید و در جهت مقابل مسیرهای Tag‌دار را **deny** کنید.
- `route-map X deny 10 / match tag N` سپس `permit 20`.
- AD را برای مسیرهای ورودی خارجی بالاتر نگه دارید.
- فقط Prefixهای لازم را redistribute کنید (Prefix-List).

### ۴) مثال ساده

دو Edge هر دو بین OSPF و BGP redistribute می‌کنند؛ Tag جلوی بازگشت مسیر را می‌گیرد.

### ۵) مثال سازمانی

مرکز با شعب هم OSPF و هم BGP دارد؛ Tag اطمینان می‌دهد مسیر شعبه دوباره برنگردد.

### ۶) تصویر و توپولوژی

```text
OSPF <--redistribute--> BGP   (E1 and E2 both do it)
 tag 100 set OSPF->BGP ; deny tag 100 BGP->OSPF
```

### ۷) پیکربندی (CLI)

```text
route-map OSPF-TO-BGP permit 10
 set tag 100
route-map BGP-TO-OSPF deny 10
 match tag 100
route-map BGP-TO-OSPF permit 20
!
router bgp 65001
 redistribute ospf 1 route-map OSPF-TO-BGP
router ospf 1
 redistribute bgp 65001 subnets route-map BGP-TO-OSPF
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Tag 100 هنگام ورود به BGP زده می‌شود.
- در برگشت به OSPF مسیرهای با Tag 100 رد می‌شوند.
- راستی‌آزمایی: `show ip route <prefix>` Tag؛ Next-hop پایدار.
- بازگشت: حذف route-map و redistribute.

### ۸) تست عملکرد

- `show ip bgp <prefix>` Tag؛ نبود نوسان در `show ip route`.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | مسیر نوسان می‌کند (Flap) |
| شواهد/دستور | `show ip route` مسیر بین دو پروتکل جابه‌جا می‌شود |
| علت | Redistribution دوطرفه بدون Tag |
| رفع | Tag + deny؛ AD |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** هدف Tag چیست؟ *(پاسخ: 10-2-ت1)*

**ت2.** چرا `permit 20` پایانی؟ *(پاسخ: 10-2-ت2)*

**ت3.** آیا یک نقطه‌ی Redistribution حلقه می‌سازد؟ *(پاسخ: 10-2-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Route-Map بدون permit پایانی خطرناک است؟ *(پاسخ: 10-2-م1)*

**م2.** سناریو: Flap مسیر؛ اولین اقدام؟ *(پاسخ: 10-2-م2)*

**معیار تسلط:** ساخت Redistribution دوطرفه ایمن با Tag.

**اشتباهات رایج:** Tag فراموش‌شده؛ permit پایانی فراموش‌شده.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Tag | Route tag | برچسب مسیر | جلوگیری از حلقه |
| Route-Map | Route-map | شرط/عمل روی مسیر | سیاست مسیریابی |
| Flap | Route flap | نوسان مسیر | نشانه‌ی حلقه |

| English sentence | ترجمه |
|---|---|
| Tag the routes at redistribution to prevent routing loops. | مسیرها را هنگام redistribution Tag کنید تا حلقه ایجاد نشود. |
| Deny tagged routes in the reverse direction. | مسیرهای Tag‌دار را در جهت مقابل deny کنید. |

#### کارت Lab — درس 10-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Redistribution دوطرفه با Tag |
| 2 | پیش‌نیاز | درس ۱۰-۱ |
| 3 | توپولوژی | E1/E2 بین OSPF و BGP |
| 4 | تجهیزات | E1،E2،ISP |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | طبق قبل |
| 7 | وضعیت اولیه | OSPF+BGP |
| 8 | صورت مسئله | حلقه را بسازید و با Tag رفع کنید |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `show ip route` |
| 11 | سناریوی خرابی | مسیر نوسان می‌کند (Flap) |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | مسیر پایدار |
| 14 | معیار پذیرش | بدون Flap |
| 15 | مستندات نهایی | `03-ops/redistribution-tags.md` |
| 16 | Cleanup و بازگردانی | حذف سیاست‌ها |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-10-3"></a>

## درس 10-3 — ECMP و توزیع بار

**فصل 10 - روز 3 · پیش‌نیاز: درس ۱۰-۱ · ۶ ساعت**

### ۱) معرفی درس

وقتی چند مسیر هم‌هزینه به یک مقصد داریم، ECMP ترافیک را بین آن‌ها پخش می‌کند. FortiGate هم ECMP دارد و رفتار آن روی Session مهم است.

### ۲) پیش‌نیازها

OSPF Cost (فصل ۵).

### ۳) توضیح مفهومی

- **ECMP** در OSPF: تا `maximum-paths` (پیش‌فرض ۴) مسیر هم‌هزینه نصب می‌شود.
- CEF توزیع را **Per-flow** (Hash بر پایه‌ی IP/پورت) انجام می‌دهد، نه Per-packet؛ پس یک Session از یک لینک می‌رود.
- `ip cef load-sharing algorithm` برای تغییر Hash.
- ECMP با Stateful Firewall باید Session را روی یک مسیر نگه دارد وگرنه نامتقارن می‌شود.
- FortiGate: `config system settings / set v4-ecmp-mode source-ip-based` (پیش‌فرض) و حالت‌های دیگر (`weight-based`, `usage-based`, `source-dest-ip-based`) — `Unverified` برای 7.0.3.

### ۴) مثال ساده

دو لینک هم‌هزینه از R1 به R3 دارند؛ هر دو در Route Table.

### ۵) مثال سازمانی

دو ISP/دو مسیر به Hub با ECMP؛ Session هر کاربر روی یک مسیر می‌ماند.

### ۶) تصویر و توپولوژی

```text
R1 ==(cost 10)== R2 ==
   \==(cost 10)== R3 == Server
ECMP: two equal-cost next hops
```

### ۷) پیکربندی (CLI)

```text
router ospf 1
 maximum-paths 4
!
show ip route 192.168.3.0
show ip cef 192.168.3.1 internal
traceroute 192.168.3.1 source 192.168.1.1
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `maximum-paths`: سقف مسیرهای هم‌هزینه.
- `show ip route`: دو Next-hop برای یک Prefix.
- Per-flow یعنی دو Flow مختلف می‌توانند مسیر متفاوت بگیرند.
- بازگشت: `maximum-paths 1`.

### ۸) تست عملکرد

- دو traceroute با مبدأ مختلف مسیر متفاوت را نشان دهد.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ترافیک یک Flow نامتعادل است |
| شواهد/دستور | `show interfaces` بار یک لینک بیشتر |
| علت | Hash یک Flow را به یک لینک می‌دهد |
| رفع | تنوع Flow یا تغییر الگوریتم؛ انتظار واقع‌بینانه |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** ECMP Per-flow یا Per-packet؟ *(پاسخ: 10-3-ت1)*

**ت2.** چرا Session باید روی یک مسیر بماند؟ *(پاسخ: 10-3-ت2)*

**ت3.** maximum-paths پیش‌فرض؟ *(پاسخ: 10-3-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا یک انتقال فایل از دو لینک سرعت دو برابر نمی‌گیرد؟ *(پاسخ: 10-3-م1)*

**م2.** سناریو: ECMP با فایروال و Drop تصادفی؛ حدس؟ *(پاسخ: 10-3-م2)*

**معیار تسلط:** نمایش ECMP و توضیح Per-flow.

**اشتباهات رایج:** انتظار Per-packet؛ نادیده‌گرفتن اثر روی فایروال.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| ECMP | Equal-Cost Multi-Path | چند مسیر هم‌هزینه | توزیع بار |
| CEF | Cisco Express Forwarding | موتور ارسال سریع | Hash مسیر |
| Per-flow | Per-flow load sharing | توزیع بر پایه‌ی Flow | پایداری Session |

| English sentence | ترجمه |
|---|---|
| Load sharing is done per flow, not per packet. | توزیع بار بر پایه‌ی Flow است نه بسته. |
| Keep both directions of a session on one path. | هر دو جهت Session را روی یک مسیر نگه دارید. |

#### کارت Lab — درس 10-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | دو مسیر ECMP |
| 2 | پیش‌نیاز | درس ۱۰-۱ |
| 3 | توپولوژی | R1-R2/R3-Server |
| 4 | تجهیزات | ۴ vIOS |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | جدول لینک‌ها |
| 7 | وضعیت اولیه | OSPF |
| 8 | صورت مسئله | دو Next-hop |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `show ip route` |
| 11 | سناریوی خرابی | ترافیک یک Flow نامتعادل است |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | دو مسیر |
| 14 | معیار پذیرش | دو Flow با مسیر مختلف |
| 15 | مستندات نهایی | `03-ops/ecmp.md` |
| 16 | Cleanup و بازگردانی | maximum-paths 1 |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-10-4"></a>

## درس 10-4 — Policy-Based Routing (PBR)

**فصل 10 - روز 4 · پیش‌نیاز: درس ۱۰-۳ · ۶ ساعت**

### ۱) معرفی درس

PBR به‌جای مقصد، بر اساس مبدأ/پروتکل/پورت مسیر را انتخاب می‌کند؛ مثلاً ترافیک یک VLAN از ISP2 برود. در فایروال هم مشابه «Policy Route» وجود دارد.

### ۲) پیش‌نیازها

ACL (فصل ۷)، Route-Map (فصل ۹).

### ۳) توضیح مفهومی

- PBR **قبل** از Route Table روی ترافیک ورودی به Interface اعمال می‌شود.
- ساختار: ACL ترافیک را مشخص می‌کند ← `route-map` با `match ip address` ← `set ip next-hop` ← `ip policy route-map` روی Interface **ورودی**.
- `set ip next-hop verify-availability` با Track برای Failover.
- ترافیک تولیدشده توسط خود روتر: `ip local policy route-map`.
- برگشت: PBR فقط یک جهت را عوض می‌کند؛ جهت دیگر باید همخوان باشد.

### ۴) مثال ساده

کاربران VLAN 20 به ISP2 و بقیه به ISP1 بروند.

### ۵) مثال سازمانی

مدیر ترافیک بک‌آپ شب را از لینک ارزان‌تر می‌فرستد.

### ۶) تصویر و توپولوژی

```text
VLAN20 -> R1 (PBR) -> ISP2
others -> R1 -> ISP1 (default)
```

### ۷) پیکربندی (CLI)

```text
ip access-list extended VLAN20-TRAFFIC
 permit ip 10.10.20.0 0.0.0.255 any
route-map PBR permit 10
 match ip address VLAN20-TRAFFIC
 set ip next-hop 10.0.2.2
interface gi0/0.20
 ip policy route-map PBR
!
show route-map PBR
show ip policy
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `ip policy route-map` روی Interface ورودی.
- `show route-map` شمارنده‌ی Policy routed packets.
- برگشت: `no ip policy route-map`.
- هشدار: PBR اشتباه می‌تواند مسیر پیش‌فرض را بشکند؛ با `reload in`/Console کار کنید.

### ۸) تست عملکرد

- `traceroute` از VLAN20: Hop اول ISP2؛ از VLAN دیگر ISP1.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | PBR اعمال نمی‌شود |
| شواهد/دستور | `show route-map`: شمارنده 0؛ `show ip policy` |
| علت | Interface/ACL اشتباه |
| رفع | اعمال روی Interface ورودی درست؛ اصلاح ACL |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** PBR کجا اعمال می‌شود؟ *(پاسخ: 10-4-ت1)*

**ت2.** PBR چه زمانی اجرا می‌شود؟ *(پاسخ: 10-4-ت2)*

**ت3.** Verify-availability چیست؟ *(پاسخ: 10-4-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا PBR باید با Return Path همخوان باشد؟ *(پاسخ: 10-4-م1)*

**م2.** سناریو: شمارنده PBR صفر است؛ چه بررسی؟ *(پاسخ: 10-4-م2)*

**معیار تسلط:** پیاده‌سازی PBR و اثبات با traceroute.

**اشتباهات رایج:** اعمال روی Interface خروجی؛ فراموشی برگشت.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| PBR | Policy-Based Routing | مسیر بر اساس سیاست | لینک مخصوص |
| Next-hop | Next hop | روتر بعدی | set ip next-hop |
| Verify | Verify availability | بررسی در دسترس بودن | Failover PBR |

| English sentence | ترجمه |
|---|---|
| Apply the policy on the ingress interface. | سیاست را روی Interface ورودی اعمال کنید. |
| PBR is evaluated before the routing table. | PBR قبل از جدول مسیریابی ارزیابی می‌شود. |

#### کارت Lab — درس 10-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | PBR برای VLAN20 |
| 2 | پیش‌نیاز | درس ۱۰-۳ |
| 3 | توپولوژی | R1 + دو ISP |
| 4 | تجهیزات | R1،ISP1،ISP2 |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | 10.0.1.0/30 و 10.0.2.0/30 |
| 7 | وضعیت اولیه | Default به ISP1 |
| 8 | صورت مسئله | VLAN20 از ISP2 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `show route-map` |
| 11 | سناریوی خرابی | PBR اعمال نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Hop اول ISP2 |
| 14 | معیار پذیرش | traceroute مطابق |
| 15 | مستندات نهایی | `03-ops/pbr.md` |
| 16 | Cleanup و بازگردانی | حذف policy |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-10-5"></a>

## درس 10-5 — VRF-lite: جداسازی جدول مسیریابی

**فصل 10 - روز 5 · پیش‌نیاز: درس ۱۰-۱ · ۶ ساعت**

### ۱) معرفی درس

VRF چند جدول مسیریابی مستقل روی یک دستگاه می‌سازد؛ مثل چند روتر مجازی. برای جداسازی مشتری/بخش و برای درک VDOM/Zone فایروال مفید است.

### ۲) پیش‌نیازها

Route Table و Interface (فصل ۵).

### ۳) توضیح مفهومی

- هر VRF جدول مسیریابی و Interfaceهای خودش را دارد؛ آدرس‌های هم‌پوشان مجازند.
- IOS: `vrf definition NAME` + `address-family ipv4`؛ `vrf forwarding NAME` روی Interface.
- دستورها با VRF: `ping vrf X`، `show ip route vrf X`.
- ارتباط بین VRFها فقط با Leak (مثلاً Static با `global`) و مسیر/فیلتر کنترل‌شده.
- VRF-lite = بدون MPLS؛ جداسازی محلی.

### ۴) مثال ساده

دو VRF (RED، BLUE) روی یک روتر با آدرس هم‌پوشان.

### ۵) مثال سازمانی

مرکز داده: VRF Management جدا از VRF Production.

### ۶) تصویر و توپولوژی

```text
R1: [VRF RED] gi0/1 10.0.0.1/24   [VRF BLUE] gi0/2 10.0.0.1/24
Same IP, separate tables
```

### ۷) پیکربندی (CLI)

```text
vrf definition RED
 address-family ipv4
 exit-address-family
interface gi0/1
 vrf forwarding RED
 ip address 10.0.0.1 255.255.255.0
show ip route vrf RED
ping vrf RED 10.0.0.2
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `vrf forwarding` قبل از `ip address` (با تغییر VRF آدرس پاک می‌شود).
- `show ip route vrf RED` جدول جدا.
- Leak مثال: `ip route vrf RED 0.0.0.0 0.0.0.0 10.9.9.1 global`.
- بازگشت: `no vrf forwarding`.

### ۸) تست عملکرد

- ping داخل VRF؛ ping بدون VRF شکست.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ping در VRF شکست می‌خورد |
| شواهد/دستور | `ping` بدون vrf؛ `show ip route vrf X` خالی |
| علت | Interface در VRF دیگر/آدرس بعد از vrf forwarding |
| رفع | تنظیم دوباره‌ی آدرس |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** VRF چیست؟ *(پاسخ: 10-5-ت1)*

**ت2.** چرا آدرس هم‌پوشان در دو VRF مجاز است؟ *(پاسخ: 10-5-ت2)*

**ت3.** Leak چیست؟ *(پاسخ: 10-5-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا بعد از `vrf forwarding` آدرس پاک می‌شود؟ *(پاسخ: 10-5-م1)*

**م2.** سناریو: ping Gateway شکست؛ اشتباه رایج؟ *(پاسخ: 10-5-م2)*

**معیار تسلط:** ساخت دو VRF و اثبات جداسازی.

**اشتباهات رایج:** ping بدون vrf؛ ترتیب vrf forwarding/ip address.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| VRF | Virtual Routing and Forwarding | جدول مسیریابی مجازی | جداسازی |
| VRF-lite | VRF-lite | VRF بدون MPLS | Campus/DC |
| Leak | Route leaking | عبور کنترل‌شده بین VRF | سرویس مشترک |

| English sentence | ترجمه |
|---|---|
| Each VRF has its own routing table. | هر VRF جدول مسیریابی خودش را دارد. |
| Overlapping addresses are allowed in different VRFs. | آدرس‌های هم‌پوشان در VRFهای مختلف مجازند. |

#### کارت Lab — درس 10-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | دو VRF با آدرس هم‌پوشان |
| 2 | پیش‌نیاز | درس ۱۰-۱ |
| 3 | توپولوژی | R1 + دو میزبان |
| 4 | تجهیزات | R1،۲ VPCS |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | 10.0.0.0/24 در هر دو |
| 7 | وضعیت اولیه | بدون VRF |
| 8 | صورت مسئله | RED/BLUE |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `ping vrf` |
| 11 | سناریوی خرابی | ping در VRF شکست می‌خورد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جداسازی کامل |
| 14 | معیار پذیرش | ping داخل VRF موفق، بین VRF شکست |
| 15 | مستندات نهایی | `03-ops/vrf.md` |
| 16 | Cleanup و بازگردانی | حذف VRF |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-10-6"></a>

## درس 10-6 — Asymmetric Routing: تحلیل مسیر رفت و برگشت

**فصل 10 - روز 6 · پیش‌نیاز: درس ۱۰-۳، ۱۰-۴ · ۶ ساعت**

### ۱) معرفی درس

مسیر رفت و برگشت بسته می‌تواند متفاوت باشد. روتر مشکلی ندارد ولی فایروال Stateful فقط یک جهت را می‌بیند و برگشت را Drop می‌کند. این یکی از شایع‌ترین خرابی‌های چندفایروالی است.

### ۲) پیش‌نیازها

ECMP، PBR، VRF (درس‌های قبل).

### ۳) توضیح مفهومی

- Asymmetric: Forward از Path A و Return از Path B.
- Stateful Firewall بدون Session مطابق، بسته‌ی برگشت (SYN-ACK) را Drop می‌کند.
- علت‌ها: ECMP، PBR یک‌طرفه، Multi-homing، Redistribution/Metric ناسازگار، دو ISP.
- تشخیص: traceroute از هر دو طرف؛ Capture در هر فایروال؛ جدول Session.
- رفع: متقارن‌سازی مسیر (Metric/PBR)، یا قرار دادن هر Session روی یک مسیر، یا فایروال‌های همگام (HA).

### ۴) مثال ساده

دو مسیر از LAN به سرور؛ رفت از FW1 و برگشت از FW2.

### ۵) مثال سازمانی

Hub با دو ISP؛ پاسخ از ISP دیگر برمی‌گردد و فایروال Drop می‌کند.

### ۶) تصویر و توپولوژی

```text
Client -> FW1 -> Server
Client <- FW2 <- Server   (return differs -> FW1 never sees SYN-ACK)
```

### ۷) پیکربندی (CLI)

```text
traceroute 10.20.0.10 source 192.168.1.1
! from server side
traceroute 192.168.1.1 source 10.20.0.10
show ip route 192.168.1.0
show ip cef 192.168.1.0
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- دو traceroute (هر جهت) مقایسه شود.
- `show ip route` مسیر برگشت روی هر روتر.
- در فایروال: `diagnose sys session list` (فصل‌های بعد) Session ناقص.
- بازگشت: تغییر Metric/PBR را بازگردانید.

### ۸) تست عملکرد

- Hopهای رفت و برگشت را در جدول بنویسید؛ تفاوت را نشان دهید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ping کار می‌کند ولی TCP نمی‌بندد |
| شواهد/دستور | SYN دیده می‌شود ولی SYN-ACK به فایروال اول نمی‌رسد |
| علت | مسیر برگشت متفاوت |
| رفع | متقارن‌سازی مسیر یا Session روی یک مسیر |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Asymmetric یعنی چه؟ *(پاسخ: 10-6-ت1)*

**ت2.** چرا Stateful آن را نمی‌پذیرد؟ *(پاسخ: 10-6-ت2)*

**ت3.** دو ابزار تشخیص؟ *(پاسخ: 10-6-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا ping ممکن است کار کند ولی TCP نه؟ *(پاسخ: 10-6-م1)*

**م2.** سناریو: دو ISP و Drop تصادفی؛ چه می‌کنید؟ *(پاسخ: 10-6-م2)*

**معیار تسلط:** تحلیل مسیر دو جهت و پیشنهاد رفع.

**اشتباهات رایج:** بررسی فقط یک جهت.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Asymmetric | Asymmetric routing | مسیر رفت/برگشت متفاوت | خرابی فایروال |
| Return path | Return path | مسیر برگشت | تحلیل ارتباط |
| Stateful | Stateful inspection | بازرسی با حافظه‌ی Session | Firewall |

| English sentence | ترجمه |
|---|---|
| Check both forward and return paths. | هر دو مسیر رفت و برگشت را بررسی کنید. |
| A stateful firewall drops traffic it has no session for. | فایروال Stateful ترافیکی را که Session ندارد Drop می‌کند. |

#### کارت Lab — درس 10-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | مشاهده و رفع Asymmetric |
| 2 | پیش‌نیاز | درس ۱۰-۳، ۱۰-۴ |
| 3 | توپولوژی | Client-FW1/FW2-Server (روتر) |
| 4 | تجهیزات | ۴ vIOS |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | طبق شکل |
| 7 | وضعیت اولیه | Metric مساوی |
| 8 | صورت مسئله | ایجاد نامتقارن و رفع |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | traceroute دوطرفه |
| 11 | سناریوی خرابی | ping کار می‌کند ولی TCP نمی‌بندد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | مسیرها متفاوت؛ بعد از رفع یکسان |
| 14 | معیار پذیرش | هر دو جهت از یک مسیر |
| 15 | مستندات نهایی | `03-ops/asymmetric.md` |
| 16 | Cleanup و بازگردانی | بازگشت Metric |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

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

**10-1-ت1** — چرا `subnets` لازم است؟

بدون آن فقط Prefixهای Classful وارد می‌شوند.

**10-1-ت2** — E1 و E2؟

E2 Metric ثابت؛ E1 با افزودن هزینه‌ی داخلی.

**10-1-ت3** — چه چیزی redistribute می‌شود؟

فقط مسیرهای موجود در Route Table.

**10-1-م1** — چرا Seed Metric لازم است؟

Metric پروتکل‌ها قابل‌مقایسه نیستند و مقصد باید مقدار اولیه بداند.

**10-1-م2** — سناریو: Route Static در OSPF دیده نمی‌شود؛ دو بررسی؟

Route مبدأ و subnets.

**10-2-ت1** — هدف Tag چیست؟

علامت‌گذاری مسیر برای جلوگیری از بازگشت.

**10-2-ت2** — چرا `permit 20` پایانی؟

Implicit deny وگرنه همه‌ی مسیرها رد می‌شوند.

**10-2-ت3** — آیا یک نقطه‌ی Redistribution حلقه می‌سازد؟

معمولاً خیر؛ دو نقطه خطرناک‌اند.

**10-2-م1** — چرا Route-Map بدون permit پایانی خطرناک است؟

Implicit deny همه را حذف می‌کند.

**10-2-م2** — سناریو: Flap مسیر؛ اولین اقدام؟

پیدا کردن نقطه‌های Redistribution و اعمال Tag.

**10-3-ت1** — ECMP Per-flow یا Per-packet؟

Per-flow.

**10-3-ت2** — چرا Session باید روی یک مسیر بماند؟

Stateful Firewall باید هر دو جهت را ببیند.

**10-3-ت3** — maximum-paths پیش‌فرض؟

۴

**10-3-م1** — چرا یک انتقال فایل از دو لینک سرعت دو برابر نمی‌گیرد؟

Per-flow؛ یک Flow یک لینک.

**10-3-م2** — سناریو: ECMP با فایروال و Drop تصادفی؛ حدس؟

هر جهت Session از مسیر متفاوت؛ نامتقارن.

**10-4-ت1** — PBR کجا اعمال می‌شود؟

روی Interface ورودی.

**10-4-ت2** — PBR چه زمانی اجرا می‌شود؟

قبل از Route Table.

**10-4-ت3** — Verify-availability چیست؟

Failover با Track.

**10-4-م1** — چرا PBR باید با Return Path همخوان باشد؟

برگشت از مسیر دیگر می‌تواند نامتقارن شود.

**10-4-م2** — سناریو: شمارنده PBR صفر است؛ چه بررسی؟

Interface ورودی و تطابق ACL.

**10-5-ت1** — VRF چیست؟

جدول مسیریابی مستقل.

**10-5-ت2** — چرا آدرس هم‌پوشان در دو VRF مجاز است؟

جدول‌ها جدا هستند.

**10-5-ت3** — Leak چیست؟

اتصال کنترل‌شده بین VRFها.

**10-5-م1** — چرا بعد از `vrf forwarding` آدرس پاک می‌شود؟

Interface به جدول دیگر رفته؛ آدرس قبلی نامعتبر است.

**10-5-م2** — سناریو: ping Gateway شکست؛ اشتباه رایج؟

ping بدون `vrf`.

**10-6-ت1** — Asymmetric یعنی چه؟

رفت و برگشت از مسیرهای متفاوت.

**10-6-ت2** — چرا Stateful آن را نمی‌پذیرد؟

Session فقط یک جهت را دارد.

**10-6-ت3** — دو ابزار تشخیص؟

traceroute دوطرفه و Capture/Session.

**10-6-م1** — چرا ping ممکن است کار کند ولی TCP نه؟

ICMP ممکن است Session جداگانه/قوانین متفاوت داشته باشد؛ TCP Stateful سخت‌گیر است.

**10-6-م2** — سناریو: دو ISP و Drop تصادفی؛ چه می‌کنید؟

مسیر برگشت را بررسی و متقارن کنید.

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

## درس 11-1 — فایروال چیست؟ Stateless در برابر Stateful

**فصل 11 - روز 1 · پیش‌نیاز: فصل ۷ · ۶ ساعت**

### ۱) معرفی درس

فایروال ترافیک بین بخش‌های شبکه را بر اساس قانون اجازه یا ممنوع می‌کند. فرق Stateless (مثل ACL) و Stateful (فایروال واقعی) مبنای همه‌ی طراحی‌هاست.

### ۲) پیش‌نیازها

ACL و NAT (فصل ۷).

### ۳) توضیح مفهومی

- **Stateless:** هر بسته مستقل بررسی می‌شود (ACL)؛ برگشت را باید جدا مجاز کنید.
- **Stateful:** اتصال را به‌صورت **Session** نگه می‌دارد؛ بسته‌های پاسخ خودکار مجاز می‌شوند.
- Session شامل مبدأ/مقصد/پروتکل/پورت و حالت (State) و Timeout است.
- فقط اولین بسته با Policy بررسی می‌شود؛ بقیه با Session (سرعت بیشتر).
- فایروال نسل جدید (NGFW) علاوه بر L3/L4 لایه‌ی ۷ را هم می‌بیند (App، IPS، SSL).

### ۴) مثال ساده

کامپیوتر ۱۰.۱۰.۲۰.۱۱ به وب ۸.۸.۸.۸ می‌رود؛ پاسخ خودکار مجاز است.

### ۵) مثال سازمانی

سرور وب در DMZ فقط به درخواست‌های کاربران پاسخ می‌دهد؛ کسی نمی‌تواند از بیرون اتصال تازه به داخل بزند.

### ۶) تصویر و توپولوژی

```text
Client --SYN--> [FW: new session] --> Server
Client <--SYN-ACK-- [FW: matches session] <-- Server
```

### ۷) پیکربندی (CLI)

```text
# Linux stateful demo (on a Linux VM acting as a router/firewall)
sudo iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -i eth1 -o eth0 -p tcp --dport 443 -j ACCEPT
sudo iptables -P FORWARD DROP
sudo conntrack -L
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- قانون اول: پاسخ‌های Session موجود مجاز.
- قانون دوم: فقط اتصال جدید به پورت 443 از eth1 به eth0.
- `-P FORWARD DROP`: Default Deny.
- `conntrack -L`: جدول Session.
- بازگشت: `iptables -F FORWARD` و `-P FORWARD ACCEPT`.

### ۸) تست عملکرد

- از Client curl به سرور 443؛ `conntrack -L` ورودی ESTABLISHED نشان دهد.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | اتصال برقرار نمی‌شود با اینکه ACL مجاز است |
| شواهد/دستور | قانون ESTABLISHED نیست؛ برگشت Drop می‌شود |
| علت | Stateless بدون قانون برگشت |
| رفع | قانون Stateful یا Policy مناسب |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Stateless و Stateful چه فرقی دارند؟ *(پاسخ: 11-1-ت1)*

**ت2.** چرا فقط اولین بسته با Policy بررسی می‌شود؟ *(پاسخ: 11-1-ت2)*

**ت3.** Session چه فیلدهایی دارد؟ *(پاسخ: 11-1-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا ACL به‌تنهایی فایروال Stateful نیست؟ *(پاسخ: 11-1-م1)*

**م2.** سناریو: پاسخ‌ها Drop می‌شوند؛ چرا؟ *(پاسخ: 11-1-م2)*

**معیار تسلط:** توضیح Stateful با مثال و جدول Session.

**اشتباهات رایج:** خلط ACL با Firewall؛ فکر اینکه همه‌ی بسته‌ها Policy می‌خورند.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Stateful | Stateful inspection | بازرسی با Session | Firewall |
| Session | Connection/session entry | ورودی اتصال | Session Table |
| NGFW | Next-Generation Firewall | فایروال با لایه ۷ | FortiGate |

| English sentence | ترجمه |
|---|---|
| A stateful firewall tracks connections in a session table. | فایروال Stateful اتصال‌ها را در جدول Session دنبال می‌کند. |
| Return traffic of an allowed session is permitted automatically. | ترافیک برگشت Session مجاز خودکار مجاز است. |

#### کارت Lab — درس 11-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | مشاهده‌ی Stateful با Linux |
| 2 | پیش‌نیاز | فصل ۷ |
| 3 | توپولوژی | Client - Linux FW - Server |
| 4 | تجهیزات | ۳ Linux |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | ۱۰.۱۰.۱/۲۴ و ۱۰.۲۰.۱/۲۴ |
| 7 | وضعیت اولیه | Forward فعال |
| 8 | صورت مسئله | Default Deny + 443 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `conntrack -L` |
| 11 | سناریوی خرابی | اتصال برقرار نمی‌شود با اینکه ACL مجاز است |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Session ESTABLISHED |
| 14 | معیار پذیرش | فقط 443 رد شود |
| 15 | مستندات نهایی | `03-ops/stateful-demo.md` |
| 16 | Cleanup و بازگردانی | flush iptables |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-11-2"></a>

## درس 11-2 — Zone، Trust Boundary، Default Deny و Least Privilege

**فصل 11 - روز 2 · پیش‌نیاز: درس ۱۱-۱ · ۶ ساعت**

### ۱) معرفی درس

سازمان را به ناحیه‌های اعتماد (Zone) تقسیم می‌کنیم و بین ناحیه‌ها فقط آنچه لازم است مجاز می‌شود. این اساس طراحی Policy است.

### ۲) پیش‌نیازها

درس ۱۱-۱.

### ۳) توضیح مفهومی

- **Zone:** گروهی از Interface/VLAN با سطح اعتماد یکسان (Inside، DMZ، Outside، Mgmt).
- **Trust Boundary:** مرزی که اعتماد در آن عوض می‌شود؛ ترافیک عبوری از آن باید بازرسی شود.
- **Default Deny:** همه چیز ممنوع مگر صریحاً مجاز.
- **Least Privilege:** حداقل دسترسی لازم (مبدأ، مقصد، سرویس، زمان).
- **Segmentation:** جداسازی برای محدودکردن گسترش حمله (Lateral Movement).

### ۴) مثال ساده

کاربران به اینترنت؛ اینترنت به داخل ممنوع.

### ۵) مثال سازمانی

Zoneهای Users، Servers، DMZ، Mgmt؛ هر مسیر یک Policy مشخص.

### ۶) تصویر و توپولوژی

```text
Outside --(deny by default)--> DMZ --(limited)--> Inside
Inside --(allow web/dns)--> Outside
```

### ۷) پیکربندی (CLI)

```text
# Policy Matrix (example)
# SRC zone  DST zone  SERVICE        ACTION
# Users     Outside   HTTP,HTTPS,DNS allow
# Users     Servers   SMB,HTTPS      allow (limited hosts)
# Outside   DMZ       HTTPS          allow (VIP only)
# any       any       any            DENY (implicit)
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- ماتریس: هر خط یک جریان مجاز است.
- خط آخر Default Deny است.
- راستی‌آزمایی: برای هر جریان مجاز یک آزمایش و برای چند جریان ممنوع آزمایش منفی.
- بازگشت: ماتریس نسخه‌دار.

### ۸) تست عملکرد

- برای هر ردیف یک تست مثبت و منفی بنویسید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | کاربر به سرور حساس دسترسی دارد |
| شواهد/دستور | Policy گسترده‌ی «Users→Servers any» |
| علت | تجمیع بی‌دقت |
| رفع | تنگ‌کردن مبدأ/سرویس |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Zone چیست؟ *(پاسخ: 11-2-ت1)*

**ت2.** Default Deny یعنی چه؟ *(پاسخ: 11-2-ت2)*

**ت3.** Least Privilege؟ *(پاسخ: 11-2-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Segmentation خطر حمله را کم می‌کند؟ *(پاسخ: 11-2-م1)*

**م2.** سناریو: یک Policy «any any» اضافه شده؛ خطر؟ *(پاسخ: 11-2-م2)*

**معیار تسلط:** ساخت Policy Matrix با Least Privilege.

**اشتباهات رایج:** Policy «any» موقت و فراموش‌شده.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Zone | Security zone | ناحیه‌ی اعتماد | Policy |
| Trust boundary | Trust boundary | مرز اعتماد | طراحی |
| Least privilege | Least privilege | حداقل دسترسی | Policy |

| English sentence | ترجمه |
|---|---|
| Apply the principle of least privilege to every rule. | اصل حداقل دسترسی را برای هر قانون اعمال کنید. |
| Everything is denied unless explicitly allowed. | همه چیز ممنوع است مگر صریحاً مجاز شود. |

#### کارت Lab — درس 11-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Policy Matrix برای سازمان نمونه |
| 2 | پیش‌نیاز | درس ۱۱-۱ |
| 3 | توپولوژی | نمودار Zoneها |
| 4 | تجهیزات | کاغذ/Markdown |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | VLAN 10/20/30/DMZ |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | ماتریس ≥ ۱۰ جریان |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | تست مثبت/منفی |
| 11 | سناریوی خرابی | کاربر به سرور حساس دسترسی دارد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | ماتریس کامل |
| 14 | معیار پذیرش | Default Deny دارد |
| 15 | مستندات نهایی | `02-design/policy-matrix-fw.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-11-3"></a>

## درس 11-3 — مسیر بسته در فایروال و ترافیک عبوری در برابر ترافیک خود فایروال

**فصل 11 - روز 3 · پیش‌نیاز: درس ۱۱-۲ · ۶ ساعت**

### ۱) معرفی درس

برای عیب‌یابی باید بدانید بسته در فایروال چه مراحلی را طی می‌کند: Route، Policy، NAT، Session. و تفاوت ترافیک عبوری با ترافیک مقصد خود فایروال.

### ۲) پیش‌نیازها

درس‌های ۱۱-۱ و ۱۱-۲.

### ۳) توضیح مفهومی

- ترتیب مفهومی (ساده): ورود ← بررسی Session ← **DNAT/VIP** ← **Route** ← **Policy** ← **SNAT** ← خروج.
- ترافیک **عبوری** با Policy؛ ترافیک **به خود فایروال** (SSH/HTTPS مدیریت، Ping) با «Local-in/Allow-access» کنترل می‌شود.
- Routing تعیین می‌کند «از کجا»؛ Policy تعیین می‌کند «اجازه‌ی عبور».
- NAT مبدأ/مقصد را عوض می‌کند؛ نه اجازه می‌دهد نه منع.
- ترتیب دقیق NAT/Policy در FortiOS در فصل ۱۳–۱۴ با Debug Flow ثابت می‌شود.

### ۴) مثال ساده

Client → اینترنت: Route (default)، Policy (allow web)، SNAT.

### ۵) مثال سازمانی

Web در DMZ از اینترنت: VIP (DNAT) ← Policy Outside→DMZ ← Route.

### ۶) تصویر و توپولوژی

```text
IN -> Session? -> DNAT -> Route -> Policy -> SNAT -> OUT
to-firewall traffic: Local policy, not forwarding policy
```

### ۷) پیکربندی (CLI)

```text
# Packet walk template
# 1 ingress interface / zone
# 2 existing session?
# 3 DNAT / VIP?
# 4 route lookup (egress)
# 5 policy match (id)
# 6 SNAT?
# 7 egress and return path
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- برای هر ارتباط قالب را پر کنید.
- برای FortiGate ابزار واقعی: Debug Flow (فصل ۱۴).
- بازگشت: ندارد (تحلیل).

### ۸) تست عملکرد

- ۳ ارتباط را روی کاغذ دنبال کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ارتباط کار نمی‌کند و نمی‌دانید کجا |
| شواهد/دستور | هیچ مرحله‌ای ثبت نشده |
| علت | عیب‌یابی بدون چارچوب |
| رفع | قالب ۷ مرحله‌ای |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Routing و Policy چه فرقی دارند؟ *(پاسخ: 11-3-ت1)*

**ت2.** کدام ترافیک Local-in است؟ *(پاسخ: 11-3-ت2)*

**ت3.** NAT اجازه می‌دهد؟ *(پاسخ: 11-3-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا ping به فایروال با Policy عبوری کار نمی‌کند؟ *(پاسخ: 11-3-م1)*

**م2.** سناریو: Policy هست ولی ارتباط نیست؛ بررسی؟ *(پاسخ: 11-3-م2)*

**معیار تسلط:** دنبال‌کردن مسیر بسته برای ۳ سناریو با قالب.

**اشتباهات رایج:** خلط Policy عبوری با دسترسی مدیریتی.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Local-in | Local-in policy | کنترل ترافیک به خود فایروال | Mgmt |
| DNAT | Destination NAT | تغییر مقصد | VIP |
| SNAT | Source NAT | تغییر مبدأ | اینترنت |

| English sentence | ترجمه |
|---|---|
| Management traffic to the firewall is not covered by forwarding policies. | ترافیک مدیریت به فایروال توسط Policyهای عبوری پوشش داده نمی‌شود. |
| Routing decides the path; policy decides the permission. | Routing مسیر را تعیین می‌کند؛ Policy اجازه را. |

#### کارت Lab — درس 11-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Packet Walk کاغذی |
| 2 | پیش‌نیاز | درس ۱۱-۲ |
| 3 | توپولوژی | ۳ ارتباط نمونه |
| 4 | تجهیزات | کاغذ |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | سه ارتباط |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | قالب ۷ مرحله‌ای |
| 11 | سناریوی خرابی | ارتباط کار نمی‌کند و نمی‌دانید کجا |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سه جدول |
| 14 | معیار پذیرش | هر مرحله مستند |
| 15 | مستندات نهایی | `03-ops/packet-walk-paper.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-11-4"></a>

## درس 11-4 — ACL، Policy و NAT: تفاوت‌ها و ارتباط‌ها

**فصل 11 - روز 4 · پیش‌نیاز: درس ۱۱-۳ · ۶ ساعت**

### ۱) معرفی درس

سه مفهوم که اغلب قاطی می‌شوند. این درس مرز آن‌ها را روشن و ارتباط با Routing را بیان می‌کند.

### ۲) پیش‌نیازها

درس ۱۱-۳.

### ۳) توضیح مفهومی

- **ACL (Cisco):** Stateless، روی Interface، Allow/Deny.
- **Policy (فایروال):** Stateful، بین Zone/Interface، با Profile و Log.
- **NAT:** تبدیل آدرس؛ جدا از Policy (ولی در فایروال با Policy مرتبط).
- ارتباط با Routing: Policy بدون Route بی‌فایده است؛ Route بدون Policy ترافیک را Drop می‌کند.
- NAT امنیت نیست؛ فقط پنهان‌سازی/تبدیل.

### ۴) مثال ساده

ACL مهمان را از سرورها جدا می‌کند؛ در فایروال همان یک Policy با Log است.

### ۵) مثال سازمانی

سازمان: ACL روی Core برای East-West ساده؛ Policy فایروال برای North-South و UTM.

### ۶) تصویر و توپولوژی

```text
ACL: stateless | Policy: stateful+profiles | NAT: address translation
```

### ۷) پیکربندی (CLI)

```text
# Compare (cheat table)
# Feature      ACL       Firewall Policy
# State        no        yes
# Layer 7      no        yes (UTM)
# Logging      limited   rich
# Placement    interface zone/interface
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- جدول مقایسه برای انتخاب ابزار.
- در Lab A از ACL و در Lab B از Policy استفاده می‌شود.
- بازگشت: ندارد.

### ۸) تست عملکرد

- ۵ نیازمندی را به ابزار مناسب نگاشت کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ACL اضافی بعد از Policy اجرا نمی‌شود |
| شواهد/دستور | انتظار اجرای ACL روی ترافیک عبوری فایروال |
| علت | خلط ابزار |
| رفع | طراحی واضح: کدام لایه کنترل می‌کند |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** آیا NAT امنیت می‌دهد؟ *(پاسخ: 11-4-ت1)*

**ت2.** Policy بدون Route؟ *(پاسخ: 11-4-ت2)*

**ت3.** ACL در برابر Policy؟ *(پاسخ: 11-4-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Lab A و B مالک Policy متفاوت دارند؟ *(پاسخ: 11-4-م1)*

**م2.** سناریو: Policy مجاز ولی ارتباط ناموفق؛ علت؟ *(پاسخ: 11-4-م2)*

**معیار تسلط:** جدول مقایسه و ۵ نگاشت نیاز به ابزار.

**اشتباهات رایج:** تکیه بر NAT به‌عنوان امنیت.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| ACL | Access Control List | فیلتر ساده | Cisco |
| Policy | Firewall policy | قانون Stateful | FortiGate |
| NAT | Network Address Translation | تبدیل آدرس | اینترنت |

| English sentence | ترجمه |
|---|---|
| NAT is not a security control. | NAT یک کنترل امنیتی نیست. |
| A policy without a route has no effect. | Policy بدون Route اثری ندارد. |

#### کارت Lab — درس 11-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | نگاشت نیازمندی به ابزار |
| 2 | پیش‌نیاز | درس ۱۱-۳ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | کاغذ |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | ۵ نیاز |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | جدول |
| 11 | سناریوی خرابی | ACL اضافی بعد از Policy اجرا نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | نگاشت درست |
| 14 | معیار پذیرش | با دلیل |
| 15 | مستندات نهایی | `03-ops/tool-mapping.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

<a id="l-11-5"></a>

## درس 11-5 — Session، Timeout، MTU/MSS و ریشه‌ی خرابی‌های TCP/UDP

**فصل 11 - روز 5 · پیش‌نیاز: درس ۱۱-۴ · ۶ ساعت**

### ۱) معرفی درس

رفتار Session برای TCP/UDP/ICMP و اثر MTU/MSS و Timeout را بدانید. بسیاری از «ارتباط قطع می‌شود» ریشه‌اش Timeout یا MTU است.

### ۲) پیش‌نیازها

درس ۱۱-۴.

### ۳) توضیح مفهومی

- TCP: Session با SYN ساخته و با FIN/RST بسته می‌شود؛ Timeout طولانی‌تر دارد.
- UDP/ICMP: «شبه‌Session» با Timeout کوتاه.
- MTU: بزرگ‌ترین بسته؛ **MSS** = MTU − 40 (IPv4 TCP).
- مشکل: Tunnel/VPN MTU را کم می‌کند؛ بسته‌ی بزرگ با DF Drop می‌شود.
- نشانه: ping کوچک OK، انتقال بزرگ قفل.

### ۴) مثال ساده

ping با اندازه‌های مختلف نقطه‌ی شکست MTU را نشان می‌دهد.

### ۵) مثال سازمانی

VPN شعبه: کلاینت‌ها صفحه‌ی بزرگ باز نمی‌کنند؛ MSS Clamp راه‌حل است.

### ۶) تصویر و توپولوژی

```text
MTU 1500 - IP 20 - TCP 20 = MSS 1460
VPN overhead lowers MTU (e.g. 1400)
```

### ۷) پیکربندی (CLI)

```text
ping -f -l 1472 10.20.0.10    # Windows: find the largest unfragmented size
ping -M do -s 1472 10.20.0.10  # Linux
# MSS = MTU - 40
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- بزرگ‌ترین `-s` که بدون Fragment رد می‌شود.
- MSS = MTU − 40 (برای TCP/IPv4).
- راستی‌آزمایی: انتقال بزرگ بعد از تنظیم.
- بازگشت: ندارد.

### ۸) تست عملکرد

- ۳ اندازه ping را امتحان و نتیجه را ثبت کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | صفحه‌ی کوچک باز می‌شود، بزرگ نه |
| شواهد/دستور | ping 1472 با DF شکست؛ 1372 OK |
| علت | MTU مسیر کوچک‌تر |
| رفع | کاهش MSS/MTU |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** MSS چگونه حساب می‌شود؟ *(پاسخ: 11-5-ت1)*

**ت2.** چرا ICMP Timeout کوتاه است؟ *(پاسخ: 11-5-ت2)*

**ت3.** نشانه‌ی MTU؟ *(پاسخ: 11-5-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا VPN مشکل MTU می‌سازد؟ *(پاسخ: 11-5-م1)*

**م2.** سناریو: SSH کار می‌کند ولی scp قفل؛ علت؟ *(پاسخ: 11-5-م2)*

**معیار تسلط:** پیدا کردن MTU مؤثر و محاسبه‌ی MSS.

**اشتباهات رایج:** فرض MTU = 1500 در Tunnel.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| MTU | Maximum Transmission Unit | بزرگ‌ترین بسته | Tunnel |
| MSS | Maximum Segment Size | بزرگ‌ترین بخش TCP | Clamp |
| DF | Don't Fragment | عدم تکه‌تکه شدن | ping آزمون |

| English sentence | ترجمه |
|---|---|
| The MSS is the MTU minus 40 bytes for IPv4 TCP. | MSS برابر MTU منهای ۴۰ بایت برای TCP/IPv4 است. |
| Large packets with DF set are dropped when the MTU is smaller. | بسته‌های بزرگ با DF وقتی MTU کوچک‌تر است Drop می‌شوند. |

#### کارت Lab — درس 11-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | اندازه‌گیری MTU |
| 2 | پیش‌نیاز | درس ۱۱-۴ |
| 3 | توپولوژی | دو میزبان با Tunnel/MTU کم |
| 4 | تجهیزات | ۲ Linux + روتر |
| 5 | نسخه نرم‌افزار | vIOS-L2 15.2(20200924، Experimental)؛ vIOS 15.9(3)M9؛ CSR1000v 17.03.02 (IOS-XE)؛ VPCS؛ PNetLab 4.2.8 |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | MTU 1400 روی روتر |
| 8 | صورت مسئله | ping با DF |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping -M do |
| 11 | سناریوی خرابی | صفحه‌ی کوچک باز می‌شود، بزرگ نه |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | MTU مؤثر |
| 14 | معیار پذیرش | محاسبه‌ی MSS |
| 15 | مستندات نهایی | `03-ops/mtu.md` |
| 16 | Cleanup و بازگردانی | برگرداندن MTU |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** روی Image شما اجرا نشده؛ خروجی‌ها پیش‌بینی هستند.

---

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

**11-1-ت1** — Stateless و Stateful چه فرقی دارند؟

Stateless هر بسته را جدا می‌بیند؛ Stateful Session نگه می‌دارد.

**11-1-ت2** — چرا فقط اولین بسته با Policy بررسی می‌شود؟

بقیه با Session تطبیق می‌شوند.

**11-1-ت3** — Session چه فیلدهایی دارد؟

مبدأ، مقصد، پروتکل، پورت‌ها، State، Timeout.

**11-1-م1** — چرا ACL به‌تنهایی فایروال Stateful نیست؟

حافظه‌ی Session ندارد.

**11-1-م2** — سناریو: پاسخ‌ها Drop می‌شوند؛ چرا؟

قانون برگشت/Session نیست.

**11-2-ت1** — Zone چیست؟

گروه Interface/VLAN با اعتماد یکسان.

**11-2-ت2** — Default Deny یعنی چه؟

هر چه مجاز نشده ممنوع است.

**11-2-ت3** — Least Privilege؟

حداقل دسترسی لازم.

**11-2-م1** — چرا Segmentation خطر حمله را کم می‌کند؟

گسترش جانبی را محدود می‌کند.

**11-2-م2** — سناریو: یک Policy «any any» اضافه شده؛ خطر؟

Default Deny بی‌اثر می‌شود.

**11-3-ت1** — Routing و Policy چه فرقی دارند؟

Route مسیر؛ Policy اجازه.

**11-3-ت2** — کدام ترافیک Local-in است؟

مقصد خود فایروال.

**11-3-ت3** — NAT اجازه می‌دهد؟

خیر؛ فقط آدرس را عوض می‌کند.

**11-3-م1** — چرا ping به فایروال با Policy عبوری کار نمی‌کند؟

مقصد خود فایروال است؛ Local-in/Allow-access.

**11-3-م2** — سناریو: Policy هست ولی ارتباط نیست؛ بررسی؟

Route و Session و NAT.

**11-4-ت1** — آیا NAT امنیت می‌دهد؟

خیر.

**11-4-ت2** — Policy بدون Route؟

بی‌فایده؛ ترافیک مسیر ندارد.

**11-4-ت3** — ACL در برابر Policy؟

Stateless در برابر Stateful.

**11-4-م1** — چرا Lab A و B مالک Policy متفاوت دارند؟

Gateway/Policy جایگاه متفاوت.

**11-4-م2** — سناریو: Policy مجاز ولی ارتباط ناموفق؛ علت؟

Route/NAT/Session.

**11-5-ت1** — MSS چگونه حساب می‌شود؟

MTU − 40 برای TCP/IPv4.

**11-5-ت2** — چرا ICMP Timeout کوتاه است؟

Session کوتاه‌مدت.

**11-5-ت3** — نشانه‌ی MTU؟

بسته‌ی کوچک OK و بزرگ قفل.

**11-5-م1** — چرا VPN مشکل MTU می‌سازد؟

سربار Tunnel MTU مؤثر را کم می‌کند.

**11-5-م2** — سناریو: SSH کار می‌کند ولی scp قفل؛ علت؟

MTU/MSS.

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
