# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۱۱ از ۱۱ — فصل‌های ۳۱ تا ۳۲

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۱۱ از ۱۱ |
| فصل‌های این فایل | ۳۱ ، ۳۲ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۳۱–۳۲ تولید شد؛ Capstone I تا IV.** پروژه‌ها «اجرا نشده»؛ دستورها آزمایش‌نشده؛ آزمون نهایی بدون شاهد معتبر نیست. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 12.

| Lab | وضعیت |
|---|---|
| 31-1 | اجرا نشده (فقط طراحی) |
| 31-2 | اجرا نشده (فقط طراحی) |
| 31-3 | اجرا نشده (فقط طراحی) |
| 31-4 | اجرا نشده (فقط طراحی) |
| 31-5 | اجرا نشده (فقط طراحی) |
| 31-6 | اجرا نشده (فقط طراحی) |
| 32-1 | اجرا نشده (فقط طراحی) |
| 32-2 | اجرا نشده (فقط طراحی) |
| 32-3 | اجرا نشده (فقط طراحی) |
| 32-4 | اجرا نشده (فقط طراحی) |
| 32-5 | اجرا نشده (فقط طراحی) |
| 32-6 | اجرا نشده (فقط طراحی) |

---

<a id="ch31"></a>

> **نسخه v3.9:** این بخش در دسته‌های B/A/C بدون تغییر محتوایی است (فشرده‌تر از فصل‌های توسعه‌یافته؛ در دسته D بازنویسی می‌شود).

# فصل 31 — Capstone I و II: طراحی و پیاده‌سازی شبکه‌ی سازمانی

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** Gateهای G1 تا G11.
**ماهیت:** پروژه‌ی جامع؛ نه درس جدید. دانشجو طراحی، پیاده‌سازی، تست و مستندسازی می‌کند.
**Capstone I:** طراحی کامل (IP Plan، VLAN، Routing، Firewall، VPN) و سند طراحی.
**Capstone II:** پیاده‌سازی در Lab و Evidence.
**هشدار صداقت:** هر بخش بدون شاهد واقعی «اجرا نشده» ثبت شود؛ ادعای تأییدنشده ممنوع.
**اشتباهات رایج:** طراحی بدون نیازمندی؛ نبود Rollback؛ مستندسازی پس از اتمام.

**درس‌های فصل:**
- [درس 31-1 — نیازمندی‌ها و سند طراحی (HLD)](#l-31-1)
- [درس 31-2 — طراحی تفصیلی (LLD)](#l-31-2)
- [درس 31-3 — پیاده‌سازی مرحله‌ای (Build)](#l-31-3)
- [درس 31-4 — تست و Evidence](#l-31-4)
- [درس 31-5 — Runbook و تحویل](#l-31-5)
- [درس 31-6 — ارزیابی Capstone I و II](#l-31-6)

---

<a id="l-31-1"></a>

## درس 31-0 — Capstone: روش طراحی، معیار پذیرش و ارزیابی قابل‌اندازه‌گیری

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: فصل ۱ تا ۳۰ · ≈ 11 ساعت**

> **وضعیت:** پروژه‌ی Capstone روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ همه‌ی دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. نیازمندی‌های کسب‌وکار را به نیازمندی فنی قابل‌اندازه‌گیری تبدیل کند.
2. مراحل پروژه (Requirements، HLD، LLD، Build، Test، Handover) را با خروجی هر مرحله بشناسد.
3. معیار پذیرش (Acceptance Criteria) SMART بنویسد.
4. ماتریس ردیابی نیازمندی ← طراحی ← آزمون را بسازد.
5. ریسک‌ها و محدودیت‌های Lab (اجرا نشده) را صادقانه ثبت کند.
6. Rubric ارزیابی Capstone را بفهمد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا معیار پذیرش؟** پیمانکار می‌گوید «ساختمان تمام شد»؛ شما می‌پرسید «چه چیزی را چک کنم؟». اگر قبلاً نوشته باشید «فشار آب ≥ 2 بار، برق سه‌فاز»، پذیرش ساده است. معیار پذیرش یعنی هر نیازمندی با یک آزمون قابل‌اندازه‌گیری (SMART) گره بخورد و Traceability: Requirement ← Design ← Test ← Evidence.

**جمع‌بندی اصلی درس:**

تا اینجا هر فصل یک مهارت بود. Capstone یعنی «حالا یک سازمان کوچک را از صفر طراحی کن و ثابت کن کار می‌کند». تفاوت مهندس با کسی که فقط دستور بلد است، همین است: او می‌پرسد «چه چیزی را باید ثابت کنم؟» پیش از اینکه اولین دستور را بزند.

در این درس روش را یاد می‌گیرید، نه فقط موضوع را: چطور نیاز مبهم («اینترنت پایدار می‌خواهیم») به معیار اندازه‌گیری‌شده («Failover زیر ۱۰ ثانیه، ۹۹٫۹٪ در ماه») تبدیل می‌شود و چطور هر معیار به یک آزمون و یک Evidence وصل می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) مراحل پروژه

| مرحله | خروجی | ابزار |
|---|---|---|
| Requirements | فهرست نیازمندی (R-01...) | مصاحبه، جدول |
| HLD | نمودار، Zoneها، IP Plan | draw.io، جدول |
| LLD | Interface/Route/Policy/VPN دقیق | جدول، Config |
| Build | Config و Runbook | CLI/GUI |
| Test | آزمون و Evidence | ماتریس آزمون |
| Handover | As-Built، Runbook، آموزش | سند |

#### ۲) نیاز به معیار (SMART)

| نیاز مبهم | نیازمندی SMART | معیار پذیرش |
|---|---|---|
| اینترنت پایدار | R-01: Failover ISP < 10 s | آزمون قطع ISP-A: بسته‌ی گمشده × 0.2 s < 10 |
| امنیت DMZ | R-02: DMZ→DB ممنوع | ۱۰ آزمون منفی همه Deny و Log |
| دورکاری امن | R-03: MFA برای ۱۰۰٪ کاربران | آزمون ورود بدون OTP رد |
| قابل‌نگهداری | R-04: Backup روزانه + Restore آزمون‌شده | فایل + Hash + Restore در Lab |

#### ۳) ماتریس ردیابی

``` text
R-01 -> HLD §3.2 (Dual-ISP SD-WAN) -> LLD table SDWAN -> Test T-05 -> Evidence E-05
R-02 -> HLD §4.1 (DMZ zone) -> LLD Policy 61 -> Test T-09..T-18 -> Evidence E-09..E-18
```

هر نیازمندی بدون آزمون «ادعا» است و هر آزمون بدون نیازمندی «کار اضافه».

#### ۴) صداقت در Lab

چون Labها اجرا نشده‌اند، هر آزمون در گزارش یکی از وضعیت‌ها را دارد: **طراحی‌شده**، **اجرا نشده**، **اجراشده با شاهد**. ادعای «موفق» بدون Evidence ممنوع است.

#### ۵) ریسک‌ها

| ریسک | احتمال | اثر | کاهش |
|---|---|---|---|
| ناسازگاری Image/لایسنس | متوسط | بالا | Probe پیش از Build |
| زمان ناکافی | بالا | متوسط | اولویت‌بندی R-01..R-04 |
| دستور Unverified | بالا | متوسط | تأیید در Lab پیش از ادعا |

#### ۶) Rubric کلی Capstone

نیازمندی و ردیابی ۱۵، طراحی HLD/LLD ۲۵، پیاده‌سازی/Config ۱۵، آزمون و Evidence ۲۵، Runbook و Handover ۱۰، صداقت ۱۰.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| شروع | نیازمندی نه دستور |
| ردیابی | هر R به T و E |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

بد: «اینترنت سریع». خوب: «۹۵٪ دانلودهای ۵ مگابایتی زیر ۲ ثانیه».

#### مثال متوسط — Failover

``` text
ping -i 1 8.8.8.8 ; cut ISP1 ; lost 3 packets x 1 s = 3 s -> PASS if target < 5 s
```

#### مثال سخت — نیازمندی‌های متعارض

«همه‌ی ترافیک رمزگشایی شود» در برابر «تأخیر کمتر از 20 ms»: Baseline، Inspection فقط روی دسته‌های پرریسک، Exemption، و نشان‌دادن تعارض به مدیر با عدد.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** نیاز «اینترنت پایدار» ⇒ R-01 Failover < 10 s؛ معیار: آزمون قطع ISP با Ping 200 ms و شمارش بسته.

**متوسط (ماتریس):** برای R-03 (MFA) جدول ردیابی بنویسید: HLD §5 دسترسی راه‌دور؛ LLD Policy گروه‌ها و FortiToken؛ Test T-12 ورود بدون OTP رد؛ Evidence E-12 Log و تصویر.

**سخت (ریسک و اولویت):** زمان ۴ هفته است و ۱۲ نیازمندی داریم. مراحل: ۱) اهمیت×ریسک. ۲) R-01..R-04 «باید» و بقیه «بهتر است». ۳) برنامه‌ی هفتگی. ۴) هر هفته Evidence. معیار پذیرش: همه‌ی «باید»ها آزمون شده، بقیه در گزارش با وضعیت صادقانه.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! no CLI: process lesson; commands appear in LLD (lesson 31-2)
```

### ۸) Verification (اثبات صحت)

- ماتریس ردیابی کامل.
- معیارها قابل‌اندازه‌گیری.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| معیار مبهم | SMART نیست | عدد و روش اندازه‌گیری |
| آزمون بی‌نیاز | ردیابی | حذف یا نیازمندی |

### ۱۰) نکات امنیتی

- اطلاعات حساس در Evidence نرود.

### ۱۱) جمع‌بندی مفهومی

- نیاز → معیار → آزمون → Evidence.
- ردیابی.
- صداقت.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) SMART یعنی چه؟ *(پاسخ: 31-0-ت1)*

**ت2.** (ساده) چرا ماتریس ردیابی؟ *(پاسخ: 31-0-ت2)*

**ت3.** (متوسط) «امنیت خوب» را به معیار تبدیل کنید. *(پاسخ: 31-0-ت3)*

**ت4.** (متوسط) وضعیت آزمون‌های اجرانشده؟ *(پاسخ: 31-0-ت4)*

**ت5.** (سخت) ۱۲ نیازمندی در ۴ هفته؛ اولویت‌بندی. *(پاسخ: 31-0-ت5)*

**ت6.** (سخت، طراحی) Rubric خودارزیابی. *(پاسخ: 31-0-ت6)*

**Q1.** Quick quiz (English): Why must each requirement have a test and evidence? *(پاسخ: 31-0-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HLD | High-Level Design | طراحی سطح بالا |
| LLD | Low-Level Design | طراحی تفصیلی |
| SMART | SMART criteria | معیار هوشمند |

- *Every requirement must be traceable to a test.* ← هر نیازمندی باید به یک آزمون قابل‌ردیابی باشد.

### ۱۴) کارت Lab

**کارت Lab:** نیازمندی و ردیابی (اجرا نشده). **Evidence:** `02-design/capstone-requirements.md`.

### ۱۵) منابع

- درس‌های فصل ۱ تا ۳۰
- ISO/IEC/IEEE 29148

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Capstone — معیار پذیرش

هر نیازمندی ← آزمون پذیرش قابل‌اندازه‌گیری (مثلاً «Failover < 5 s»). ماتریس Traceability: Requirement → Design → Test → Evidence.

**پرسش‌های مصاحبه**
1. *چرا Traceability؟* پوشش.
2. *Acceptance؟* تعریف شده.
3. *Out-of-scope؟* ثبت.

### مثال حل‌شده: Traceability

| Req | Design | Test | Evidence |
|---|---|---|---|
| R1 اینترنت Users | Policy 20 | T1 curl | Log+Session |
| R2 DMZ فقط 443 | VIP+Policy | T2 nmap | خروجی nmap |
| R3 Failover < 5 s | HA/SD-WAN | T3 قطع لینک | ping Loss |

### تکمیل عمیق: چرا Capstone بدون «معیار پذیرش» فقط یک نمایش است؟

#### چرا باید یاد بگیریم؟

فرض کنید پیمانکار ساختمان به شما بگوید «ساختمان تمام شد». می‌پرسید: «چه چیزی را چک کنم؟». اگر قبلاً روی کاغذ نوشته باشید «آب هر طبقه فشار ≥ ۲ بار، برق سه‌فاز، آسانسور تا طبقه ۵»، پذیرش ساده است. اگر ننوشته باشید، بحث می‌شود. پروژه‌ی شبکه هم همین است. **معیار پذیرش** (Acceptance Criteria) یعنی هر نیازمندی با یک آزمون قابل‌اندازه‌گیری گره می‌خورد تا «تمام شد» معنای مشخص داشته باشد.

#### توضیح ساده

یک Capstone خوب سه ستون دارد: **نیازمندی** (چه می‌خواهیم)، **طراحی** (چطور) و **اثبات** (چطور نشان می‌دهیم). رشته‌ای که این سه را به هم وصل می‌کند ماتریس ردیابی (Traceability Matrix) است.

``` text
Requirement  ->  Design element  ->  Test  ->  Evidence
R1           ->  Policy 20       ->  T1    ->  curl output + log
R2           ->  VIP + Policy 30 ->  T2    ->  nmap output
R3           ->  SD-WAN/Link mon ->  T3    ->  ping loss count
```

#### مثال ساده — نیازمندی بد و خوب

| نیازمندی بد | نیازمندی خوب |
|---|---|
| «اینترنت سریع باشد» | «۹۵٪ دانلود‌ها زیر ۲ ثانیه برای فایل ۵ مگابایتی» |
| «امن باشد» | «از Users به Mgmt هیچ پورتی باز نباشد (آزمون nmap)» |
| «Failover داشته باشد» | «قطع لینک اول؛ از دست‌رفتن کمتر از ۵ بسته با ping هر ۱ ثانیه» |

قاعده‌ی SMART: Specific، Measurable، Achievable، Relevant، Time-bound.

#### مثال متوسط — آزمون نیازمندی Failover

``` text
ping -i 1 8.8.8.8           # run on a user PC
# at t=30s disconnect ISP1
# count lost replies until reply returns
lost = 3 packets x 1 s = 3 s  -> PASS if target < 5 s
```

مراحل: ۱) Baseline بگیرید ۲) قطع ۳) شمارش ۴) مقایسه با هدف ۵) ثبت.

#### مثال سخت — نیازمندی‌های متعارض

مدیر می‌خواهد «همه‌ی ترافیک رمزگشایی و بازرسی شود» (SSL Inspection) و هم «تأخیر کمتر از ۲۰ میلی‌ثانیه». تحلیل: Inspection CPU می‌خورد؛ آزمون واقعی لازم است.

راه‌حل: Baseline بگیرید، Inspection را فقط روی دسته‌هایی که ریسک بالا دارند فعال کنید و برای بانک/سلامت Exemption بگذارید. نتیجه را با عدد گزارش دهید و تعارض را به مدیر نشان دهید، نه این‌که پنهان کنید.

#### ساختار پروژه‌ی Capstone

1. نیازمندی و فرضیات
2. HLD (High-Level Design، یعنی طراحی سطح بالا)
3. LLD (Low-Level Design، یعنی طراحی تفصیلی)
4. ساخت مرحله‌ای با Checkpoint
5. آزمون و Evidence
6. Runbook و Handover
7. ارائه و دفاع

#### Lab

برای پروژه‌ی خودتان ۸ نیازمندی SMART بنویسید و برای هر کدام یک آزمون و یک خروجی قابل‌ثبت تعریف کنید.

#### عیب‌یابی طراحی پروژه

| علامت | علت | رفع |
|---|---|---|
| آزمون نمی‌توان نوشت | نیازمندی مبهم | بازنویسی SMART |
| نیازمندی بی‌طرح | ماتریس ناقص | افزودن ستون Design |
| طرح بی‌نیازمندی | کار اضافه | حذف یا توجیه |

#### پرسش‌های مرور با پاسخ

**۱. Traceability چه فایده‌ای دارد؟** پوشش کامل و پیدا کردن کار اضافه یا جاافتاده.

**۲. SMART یعنی چه؟** مشخص، قابل‌اندازه‌گیری، دست‌یافتنی، مرتبط، زمان‌دار.

**۳. تعارض نیازمندی‌ها را چه کنیم؟** با عدد نشان دهید و تصمیم را مالک بگیرد.

#### English Corner

- *Every requirement must map to at least one test.* هر نیازمندی باید دست‌کم یک آزمون داشته باشد.
- *Acceptance criteria are agreed before the build starts.*
- Q: What makes a requirement measurable?

## درس 31-1 — Capstone I: نیازمندی‌ها و سند طراحی سطح بالا (HLD) — با نمونه‌ی کامل

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۰، همه‌ی Gateها · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ دستورها `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. نیازمندی عملکردی و غیرعملکردی SMART بنویسید و ابهام را با پرسش‌های شفاف‌ساز رفع کنید.
2. HLD (High-Level Design) کامل تولید کنید.
3. ADR (Architecture Decision Record) برای تصمیم‌های کلیدی بنویسید.
4. معیار پذیرش و برنامه‌ی آزمون سطح بالا را تعریف کنید.
5. ریسک را با احتمال×اثر رتبه‌بندی و کنترل کنید.
6. طرح را با Rubric ارزیابی و بازبینی کنید.

### چرا باید یاد بگیریم؟

مهندس معمار پیش از آنکه آجر بچیند، نقشه‌ی شهر می‌کشد: چه کسی در شهر زندگی می‌کند، چه مسیرهایی لازم است، چه خطراتی (سیل، زلزله) هست. HLD این نقشه برای شبکه است. اگر نیازمندی را مبهم بنویسید («یک شبکه‌ی چندشعبه بساز»)، پروژه با «ولی من فکر می‌کردم...» تمام می‌شود. Capstone اثبات تسلط است؛ و اولین نشانه‌ی تسلط، تبدیل خواسته‌ی مبهم به نیازمندی قابل‌آزمون است.

### پروژه‌ی مرجع

شرکت «لب»: HQ (دیتاسنتر و کاربران)، سه شعبه‌ی A/B/C. ISPهای دوگانه، Hub دوگانه، SaaS (Microsoft 365)، دسترسی راه‌دور، انطباق Log ۱۸۰ روز.

### از خواسته‌ی مبهم به نیازمندی

خواسته‌ی مدیر: «شبکه‌ی شعبه‌ها خوب و امن باشد.»

پرسش‌های شفاف‌ساز:

1. «خوب» یعنی چه Latency/پهنای باند؟ برای کدام برنامه؟
2. دسترس‌پذیری هدف؟ ساعات کاری یا ۲۴×۷؟
3. «امن» یعنی چه تهدیدی؟ الزام قانونی (Log، رمزنگاری)؟
4. بودجه و زمان؟
5. تیم نگهداری چند نفر و چه مهارتی؟
6. سیستم‌های موجود (AD، ERP، IP Plan)؟

### نیازمندی‌ها (SMART)

| ID | نوع | نیازمندی | معیار پذیرش |
|---|---|---|---|
| R1 | عملکردی | ERP از همه‌ی شعب | TCP 443 موفق؛ Latency < 40 ms |
| R2 | غیرعملکردی | دسترس‌پذیری ۹۹٫۹٪ | Failover < 10 s؛ ≤ 8.76 h/سال |
| R3 | امنیتی | Guest ایزوله | nmap منفی: Guest→Internal filtered |
| R4 | امنیتی | دسترسی راه‌دور با MFA | ورود بدون OTP رد می‌شود |
| R5 | عملیاتی | Log ۱۸۰ روز و Alert | فایل Log و Alert آزمایشی |
| R6 | عملیاتی | Backup/Restore RTO ≤ 30 min | Restore Lab زمان‌سنجی‌شده |

``` text
Availability 99.9% -> downtime budget = 0.001 x 8760 h = 8.76 h/year
```

### ساختار HLD

1. هدف/دامنه/فرض‌ها/خارج از دامنه
2. نیازمندی‌ها و معیار پذیرش
3. نمودار معماری
4. IP/VLAN/Zone
5. Routing/Overlay
6. Firewall/UTM/Auth
7. HA/SD-WAN/Dual-ISP
8. مانیتورینگ/Log/Backup
9. تصمیم‌ها (ADR)
10. ریسک‌ها
11. برنامه‌ی آزمون و پذیرش
12. زمان‌بندی و هزینه (در سطح بالا)

### نمودار معماری (مفهومی)

``` text
            Internet (ISP1, ISP2)
                  |
        +---------+----------+
        |  HQ: Hub1  Hub2 (HA/BGP RR)  + DC + Users + Mgmt + DMZ
        +----+---------+-----+
             | IPsec IKEv2 overlay (iBGP, ADVPN)
   +---------+---------+---------+
   Branch A  Branch B  Branch C  (dual ISP, SD-WAN, local breakout for SaaS)
```

### جریان‌ها

| جریان | مسیر |
|---|---|
| F1 Users→Internet | شعبه Breakout (SaaS) یا Hub |
| F2 Internet→DMZ | Hub VIP |
| F3 Mgmt→دستگاه‌ها | Mgmt VLAN، Bastion |
| F4 Branch→ERP | Overlay |
| F5 Remote→ERP | IPsec Dial-up + MFA |
| F6 Log/Monitoring | Syslog TLS، SNMPv3 |

### ADR (نمونه)

``` text
ADR-03: Local breakout for trusted SaaS only
Context: backhaul adds 33 ms to M365; budget limited
Options: A all-backhaul, B all-breakout, C hybrid
Decision: C; SaaS via ISDB/FQDN breakout with Web/DNS/File filter; rest via Hub
Consequences: need UTM at branch; central logging required; review quarterly
```

ADRهای دیگر: ADR-01 IPsec Route-based + BGP؛ ADR-02 دسترسی راه‌دور با IPsec Dial-up (نه SSL VPN) به‌دلیل ریسک CVE؛ ADR-04 Syslog/Git به‌جای FMG/FAZ (هزینه)؛ ADR-05 HA A-P در Hub.

### ریسک

``` text
Risk score = Likelihood (1-5) x Impact (1-5)
```

| ریسک | L | I | امتیاز | کنترل |
|---|---|---|---|---|
| CVE روی Hub | 3 | 5 | 15 | Patch SLA، Source Restriction |
| ISP تک‌شعبه | 4 | 3 | 12 | Dual-ISP + SD-WAN |
| Config خراب Sync | 2 | 5 | 10 | Canary/Rollback |
| فرضیه‌ی غلط | 3 | 4 | 12 | تأیید فرضیه‌ها در Discovery |

### مثال‌های حل‌شده

#### مثال ساده — جریان‌ها

سه جریان F1، F2، F3 را بنویسید؛ هر جریان یک Policy و یک آزمون دارد.

#### مثال متوسط — SMART کردن

«شبکه سریع باشد» ⇒ «RTT شعبه به ERP کمتر از ۴۰ms در ۹۵٪ زمان‌ها در ساعات کاری، اندازه‌گیری با Health-check ۱ ماه». قابل‌آزمون.

#### مثال متوسط — ریسک

ISP outage: 4×3=12 ⇒ Dual-ISP. هزینه‌ی کنترل در برابر ریسک مقایسه می‌شود.

#### مثال سخت — فرضیه‌ی غلط

«ISP IP ثابت می‌دهد» ولی DHCP بود؛ VPN با Peer ثابت شکست خورد. هر فرضیه تا تأیید یک ریسک است؛ در Discovery لیست فرضیه‌ها با تأییدکننده و تاریخ.

#### مثال سخت — تعارض نیازمندی

R2 (۹۹٫۹٪) و محدودیت بودجه (یک ISP). تعارض را مستند و تصمیم مدیریتی بگیرید: ۹۹٫۹٪ فقط با Dual-ISP قابل‌دستیابی؛ یا هدف را ۹۹٪ کنید و پذیرش ریسک را امضا کنید. بدون این، پروژه شکست می‌خورد.

### Lab هدایت‌شده (اجرا نشده)

1. شش نیازمندی SMART برای پروژه‌ی خودتان.
2. نمودار و جدول جریان‌ها.
3. سه ADR و ماتریس ریسک.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| نیازمندی مبهم | بی‌پرسش | شفاف‌ساز |
| بدون معیار | غیر SMART | معیار پذیرش |
| ریسک نادیده | فرضیه | ثبت/تأیید |
| تصمیم بی‌دلیل | ADR نیست | ADR |

### جمع‌بندی

نیازمندی SMART با معیار پذیرش؛ HLD ساختاریافته؛ ADR برای تصمیم‌ها؛ ریسک با امتیاز؛ تعارض‌ها را صریح مستند کنید.

### تمرین و ارزیابی

**ت1.** (ساده) یک نیازمندی SMART مثال بزنید. *(پاسخ: 31-1-ت1)*

**ت2.** (ساده) ADR چیست؟ *(پاسخ: 31-1-ت2)*

**ت3.** (متوسط) 99.9٪ چند ساعت Downtime سالانه می‌دهد؟ *(پاسخ: 31-1-ت3)*

**ت4.** (متوسط) چرا معیار پذیرش از ابتدا؟ *(پاسخ: 31-1-ت4)*

**ت5.** (سخت) تضاد بودجه و دسترس‌پذیری را حل و ثبت کنید. *(پاسخ: 31-1-ت5)*

**ت6.** (سخت، طراحی) HLD ۱۲ بخشی را برای پروژه بنویسید. *(پاسخ: 31-1-ت6)*

**Q1.** Quick quiz (English): Why define acceptance criteria during requirements gathering? *(پاسخ: 31-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HLD | High-Level Design | طراحی سطح بالا |
| ADR | Architecture Decision Record | ثبت تصمیم معماری |
| SMART | Specific, Measurable, Achievable, Relevant, Time-bound | معیارهای نیاز خوب |

- *Define acceptance criteria first.* ← ابتدا معیار پذیرش را تعریف کنید.

### کارت Lab

**کارت Lab:** HLD. **Evidence:** `02-design/capstone-hld.md`.

### منابع

- ISO/IEC/IEEE 29148
- M. Nygard — ADR

<a id="l-31-2"></a>

## درس 31-2 — Capstone I: طراحی تفصیلی (LLD) — جدول Interface/Route/Policy/VPN و ماتریس ردیابی

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۰، ۳۱-۱ · ≈ 11 ساعت**

> **وضعیت:** پروژه‌ی Capstone روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ همه‌ی دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. LLD (Low-Level Design) کامل بنویسید: Interface، IP، VLAN، Route، Policy، VPN، BGP، SD-WAN، HA، Log.
2. جدول‌های قابل‌اجرا بسازید که مهندس دیگر بتواند بدون پرسش پیاده کند.
3. هماهنگی HLD↔LLD (Traceability) را حفظ کنید.
4. پارامترهای VPN/BGP/HA را دقیق و یکسان دو سمت ثبت کنید.
5. ماتریس Policy حداقلی را کامل کنید.
6. LLD را با چک‌لیست بازبینی کنید.

### چرا باید یاد بگیریم؟

HLD نقشه‌ی شهر است؛ LLD نقشه‌ی سیم‌کشی هر ساختمان. بیشتر خطاهای اجرا از LLD مبهم می‌آید: «IP را بعداً می‌گذاریم»، «پارامتر VPN را هماهنگ می‌کنیم». LLD خوب آن‌قدر دقیق است که اگر مهندس دیگری (یا خودتان ۶ ماه بعد) بخواند، بدون حدس بسازد.

### اصول LLD

1. هر مقدار قابل‌اجرا: IP، Mask، Gateway، VLAN، نام Interface.
2. هر Policy: Src/Dst/Service/Action/NAT/Log/Profile/Owner.
3. هر پارامتر هماهنگ‌شونده با Peer: در یک جدول دوطرفه.
4. ردیابی: هر ردیف به R# و ADR# اشاره کند.
5. سازگاری: Subnetها هم‌پوشانی ندارند.

### جدول Interface و IP

| دستگاه | Interface | Zone | IP | VLAN | R# |
|---|---|---|---|---|---|
| HUB1 | port1 | WAN1 | 198.51.100.2/29 | - | R2 |
| HUB1 | port2 | WAN2 | 203.0.113.2/29 | - | R2 |
| HUB1 | port3 | LINK-INT | 10.99.0.1/30 | - | R2 |
| HUB1 | port4 | DMZ | 10.30.0.1/24 | 30 | F2 |
| HUB1 | port5 | HA-HB | - | - | R2 |
| HUB1 | Loopback0 | LOOP | 10.254.0.1/32 | - | BGP |
| BR-A | port1 | WAN1 | DHCP/Static ISP | - | R2 |
| BR-A | port2 | WAN2 | ISP2 | - | R2 |
| BR-A | port3 | LAN | 10.1.1.1/24 | 10 | R1 |
| BR-A | port4 | GUEST | 10.1.101.1/24 | 20 | R3 |
| BR-A | Loopback0 | LOOP | 10.254.1.1/32 | - | BGP |

برای B: 10.1.2.0/24 و C: 10.1.3.0/24، Loopback 10.254.2.1/32 و 10.254.3.1/32.

### برنامه‌ی IP

``` text
10.0.0.0/16     HQ (Users 10.0.10.0/24, Servers 10.0.20.0/24, Mgmt 10.0.50.0/24, DMZ 10.30.0.0/24)
10.1.0.0/16     Branches (A=10.1.1.0/24, B=10.1.2.0/24, C=10.1.3.0/24; Guest 10.1.10X.0/24)
10.250.0.0/16   Tunnel p2p /30
10.254.0.0/24   Loopbacks /32
10.212.135.0/24 Remote-access pool
```

### پارامترهای VPN (دوطرفه)

| پارامتر | HUB | BR-A |
|---|---|---|
| IKE | v2 | v2 |
| P1 | aes256-sha256, DH14, 86400 | همان |
| P2 | aes256-sha256, PFS DH14, 43200 | همان |
| Selector | 0.0.0.0/0 | 0.0.0.0/0 |
| ADVPN | sender | receiver |
| DPD | on-idle 10/3 | همان |
| PSK | Vault: `vpn/hub-bra` | همان |

### BGP

| پارامتر | مقدار |
|---|---|
| AS | 65000 (iBGP) |
| Hub1/Hub2 | RR، Router-ID 10.254.0.1/.2 |
| Peering | Loopback↔Loopback، `update-source` |
| Prefix اعلام‌شده Hub | 10.0.0.0/16، Summary 10.1.0.0/16 |
| Prefix هر شعبه | شبکه‌ی LAN خودش |
| Local-Pref | Hub1=200، Hub2=100 |
| BFD | 300 ms × 3 |
| Prefix-list ورودی | فقط Prefixهای مجاز هر Spoke |
| Null Route | 10.1.0.0/16 distance 254 |

### SD-WAN شعبه

| پارامتر | مقدار |
|---|---|
| Members | port1 (ISP1)، port2 (ISP2) + تونل‌های Overlay |
| Health-check | 8.8.8.8 و 1.1.1.1، ping، interval 500 ms، failtime 5، recoverytime 60 |
| SLA | latency 100 ms، jitter 30 ms، loss 2% |
| Rule Teams | mode sla → ISP محلی |
| Rule ERP | Overlay (Hub) |
| Rule Default | priority ISP1 |

### HA Hub

| پارامتر | مقدار |
|---|---|
| mode | a-p |
| group-name | HUB-HA |
| hbdev | port5 (100)، port6 (50) مستقیم |
| priority | A=200، B=100، override disable |
| monitor | port1، port2، port3 |
| session-pickup | enable |
| ha-mgmt | port8 در Mgmt |

### ماتریس Policy (خلاصه)

| # | از | به | سرویس | Profile | R# |
|---|---|---|---|---|---|
| 10 | Users | ERP (Overlay/HQ) | HTTPS | IPS | R1 |
| 11 | Users | Internet | HTTP/S/DNS | Web+DNS+AV | R1 |
| 12 | Guest | Internet | HTTP/S/DNS | Web+DNS | R3 |
| 13 | Guest | Internal | هیچ | Deny+Log | R3 |
| 20 | Internet | DMZ VIP | HTTPS | IPS/WAF(Needs-License) | F2 |
| 30 | Remote(VPN) | ERP | HTTPS | MFA group | R4 |
| 40 | Mgmt | Devices | SSH/HTTPS | - | F3 |
| 99 | any | any | - | Deny+Log | همه |

### Log/Monitoring/Backup

| مورد | مقدار |
|---|---|
| Syslog | rsyslog TLS 6514، ۱۸۰ روز (R5) |
| SNMP | v3 auth-priv، Zabbix |
| Backup | روزانه، Git + Full رمزگذاری‌شده، Restore RTO ≤ 30 min (R6) |
| NTP | 10.0.50.10 |

### Traceability

| R# | LLD |
|---|---|
| R1 | جدول Interface، Policy 10/11، Rule ERP |
| R2 | HA، Dual-ISP، BFD، Failover |
| R3 | VLAN Guest، Policy 12/13 |
| R4 | Dial-up + MFA، Policy 30 |
| R5 | Syslog، Retention |
| R6 | Backup/Restore |

### مثال‌های حل‌شده

#### مثال ساده — بررسی Overlap

``` text
python3 -c "import ipaddress as i; print(i.ip_network('10.1.1.0/24').overlaps(i.ip_network('10.1.101.0/24')))"
```

False ⇒ OK.

#### مثال متوسط — ردیابی

R3 (Guest ایزوله) ⇒ VLAN 20، Zone Guest، Policy 12 و 13، آزمون nmap. هر R# بدون LLD و هر LLD بدون R# یعنی خطا.

#### مثال متوسط — پارامتر یکسان

جدول دوطرفه نشان داد P2 Lifetime سمت Hub 43200 و Branch 3600؛ رفع قبل از ساخت.

#### مثال سخت — ظرفیت

Hub باید ۳ شعبه + ۵۰ کاربر راه‌دور را تحمل کند. IPsec Throughput لازم:

``` text
Needed = 3 branches x 100 Mbps + 50 users x 5 Mbps = 300 + 250 = 550 Mbps
Choose model with IPsec throughput >= 2 x 550 = 1100 Mbps (headroom)
```

مدل از Datasheet.

#### مثال سخت — LLD ناقص

LLD بدون Policy برای Mgmt؛ در ساخت، تیم به‌صورت موقت ALL باز کرد و فراموش شد. چک‌لیست بازبینی LLD باید «هر Zone Pair Policy یا Deny صریح دارد» را بپرسد.

### Lab هدایت‌شده (اجرا نشده)

1. جدول Interface و IP کامل.
2. پارامترهای VPN/BGP/HA.
3. ماتریس Policy و Traceability.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Overlap | IP Plan | بررسی |
| VPN ناسازگار | جدول یک‌طرفه | دوطرفه |
| R# بی‌پوشش | Traceability | افزودن |
| Policy ناقص | Zone Pair | بازبینی |

### جمع‌بندی

LLD قابل‌اجرا: Interface/IP/VLAN، VPN/BGP/SD-WAN/HA، ماتریس Policy، Log/Backup؛ Traceability با R#؛ بازبینی با چک‌لیست.

### تمرین و ارزیابی

**ت1.** (ساده) LLD چه تفاوتی با HLD؟ *(پاسخ: 31-2-ت1)*

**ت2.** (ساده) چرا ردیف Policy نیازمندی دارد؟ *(پاسخ: 31-2-ت2)*

**ت3.** (متوسط) Overlap pool VPN؟ *(پاسخ: 31-2-ت3)*

**ت4.** (متوسط) NAT کجا؟ *(پاسخ: 31-2-ت4)*

**ت5.** (سخت) Asymmetric در LLD. *(پاسخ: 31-2-ت5)*

**ت6.** (سخت، طراحی) LLD Internal. *(پاسخ: 31-2-ت6)*

**Q1.** Quick quiz (English): Why should every policy row reference a requirement? *(پاسخ: 31-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| LLD | Low-Level Design | طراحی تفصیلی |

- *The LLD must contain exact values.* ← LLD باید مقادیر دقیق داشته باشد.

### کارت Lab

**کارت Lab:** LLD (اجرا نشده). **Evidence:** `02-design/capstone-lld.md`.

### منابع

- درس‌های ۱۵-۱ تا ۱۵-۶، ۲۱-۱

<a id="l-31-3"></a>

## درس 31-3 — Capstone II: ساخت مرحله‌ای (S1–S6) با Checkpoint، دستورهای واقعی، آزمون هر مرحله و Rollback

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۲ · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ساخت را به مراحل S1–S6 با Checkpoint و Rollback بشکنید.
2. در هر مرحله آزمون ورود/خروج (Entry/Exit Criteria) تعریف کنید.
3. ترتیب منطقی (پایه ⇒ HA ⇒ Overlay ⇒ SD-WAN ⇒ هویت/UTM ⇒ عملیات) را رعایت کنید.
4. Evidence هر مرحله را جمع کنید.
5. Backup پیش از هر مرحله بگیرید و تغییرات را ثبت کنید.
6. خطاهای رایج هر مرحله را بشناسید.

### چرا باید یاد بگیریم؟

ساختمان را از سقف شروع نمی‌کنند. ساخت مرحله‌ای (S1–S6) هر لایه را قبل از لایه‌ی بعد ثابت می‌کند؛ اگر در S4 مشکل پیدا شود، می‌دانید S1–S3 سالم‌اند و سطح عیب‌یابی کوچک است. ساخت یک‌جا (Big Bang) یعنی ۲۰ مجهول هم‌زمان.

### مراحل

| مرحله | محتوا | Checkpoint |
|---|---|---|
| S1 پایه | Interface، IP، Zone، Route، NTP، DNS، Hardening Mgmt | ping، `allowaccess`، Mgmt فقط از Mgmt |
| S2 HA | Cluster Hub، ha-mgmt، Failover | `get system ha status`، Reboot Test |
| S3 Overlay | IPsec، BGP، ADVPN | `ike gateway`، `bgp summary`، Failover Hub |
| S4 SD-WAN/Breakout | Health-check، Rule، SaaS | `sdwan health-check`، Brownout |
| S5 هویت/UTM/Remote | LDAP/RADIUS/MFA، Profiles، Dial-up | آزمون ورود/رد، EICAR/Web |
| S6 عملیات | Syslog، SNMP، Backup، Runbook | Log می‌رسد، Alert، Restore |

### قاعده‌ی هر مرحله

``` text
Entry : previous checkpoint passed + backup taken + change approved
Do    : implement only this stage
Test  : checkpoint tests (positive and negative)
Exit  : evidence stored; backup after; go/no-go for next
Rollback: restore backup of this stage entry
```

### S1 — پایه

``` text
config system interface ... config router static ... config system ntp ... config system dns ...
```

Checkpoint:

1. هر Interface IP صحیح (`get system interface physical`).
2. Default Route و DNS (`execute ping 8.8.8.8` و `execute ping google.com`).
3. مدیریت فقط از Mgmt (آزمون منفی از WAN/Users).
4. NTP sync (`diagnose sys ntp status`).

### S2 — HA

Checkpoint: دو عضو، checksum برابر، Reboot Primary ⇒ Failover < 10 ثانیه (R2)، Session Pickup.

### S3 — Overlay

Checkpoint: تونل Hub↔شعبه A/B/C (`diagnose vpn ike gateway list`)، BGP Established (`get router info bgp summary`)، Prefix شعب در Hub، ERP قابل‌دسترس، قطع Hub1 ⇒ Hub2 (BFD) در زمان هدف.

### S4 — SD-WAN و Breakout

Checkpoint: `diagnose sys sdwan health-check` alive، Rule Teams به ISP محلی، قطع ISP1 ⇒ Failover < 5s، Brownout (Loss 5٪) ⇒ مسیر عوض.

### S5 — هویت، UTM، دسترسی راه‌دور

Checkpoint: LDAP Test، گروه‌ها، MFA Dial-up (ورود بدون OTP رد)، Web Filter بلاک، آزمون ایمن AV (EICAR با لایسنس؛ بدون آن File Filter)، Guest→Internal filtered (nmap).

### S6 — عملیات

Checkpoint: Log TLS به rsyslog، Retention ۱۸۰ روز (محاسبه)، SNMPv3 + Alert، Backup خودکار + Restore Lab زمان‌سنجی (R6).

### Backup/Rollback هر مرحله

``` text
execute backup config tftp <name>-S<N>-pre.conf <server> <password>
# after exit
execute backup config tftp <name>-S<N>-post.conf <server> <password>
```

Rollback = Restore فایل «pre» همان مرحله.

### مثال‌های حل‌شده

#### مثال ساده — Checkpoint S1

ping GW، DNS، NTP OK؛ آزمون منفی: SSH از WAN Timeout. Exit؛ Backup post.

#### مثال متوسط — S3 شکست

BGP Active. بررسی: Loopback Reachability ندارد (Static نبود). اضافه کردن Route Loopback روی تونل؛ BGP Established. علت در S3 است؛ S1/S2 سالم؛ سطح عیب‌یابی کوچک.

#### مثال متوسط — Rollback

در S4 SD-WAN Policy قدیمی را حذف کرد و اینترنت قطع شد. Rollback به S4-pre ۵ دقیقه؛ سپس انتقال صحیح Policy به Zone.

#### مثال سخت — وابستگی بین مراحل

S5 Policy گروهی (LDAP) کار نمی‌کرد چون DNS در S1 به DC اشاره نداشت؛ خطا در S5 دیده شد ولی ریشه در S1. درس: Checkpoint S1 باید «DNS داخلی حل می‌شود» را شامل شود؛ در بازبینی Checkpointها وابستگی‌های پنهان را اضافه کنید.

#### مثال سخت — Big Bang

تیم همه‌چیز را یک شب ساخت؛ ۱۴ خطا هم‌زمان؛ ۳ روز عیب‌یابی. مقایسه: S1–S6 ۶ روز ولی هر روز Checkpoint و خطای محدود. زمان کل مشابه، ریسک کمتر، Evidence بیشتر.

### Lab هدایت‌شده (اجرا نشده)

1. S1 و S2 را اجرا و Checkpoint.
2. S3 با Failover.
3. Rollback یک مرحله.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| خطا در مرحله‌ی بالاتر | وابستگی پایین | Checkpoint |
| Rollback شکست | Backup نیست | قبل از هر مرحله |
| زمان طولانی | Big Bang | مرحله‌ای |

### نکات امنیتی

هر مرحله با Hardening؛ Secret در Vault؛ Backup رمزگذاری‌شده؛ ثبت تغییر.

### جمع‌بندی

ساخت S1–S6 با Entry/Exit، Checkpoint (مثبت/منفی)، Backup/Rollback هر مرحله؛ وابستگی‌ها را در Checkpoint بیاورید.

### تمرین و ارزیابی

**ت1.** (ساده) چرا ترتیب پایین به بالا؟ *(پاسخ: 31-3-ت1)*

**ت2.** (ساده) Checkpoint چیست؟ *(پاسخ: 31-3-ت2)*

**ت3.** (متوسط) آزمون منفی S3 چیست؟ *(پاسخ: 31-3-ت3)*

**ت4.** (متوسط) هدف زمان Rollback؟ *(پاسخ: 31-3-ت4)*

**ت5.** (سخت) دو علت هم‌زمان در S4؛ روش جداسازی. *(پاسخ: 31-3-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Build ۶ مرحله‌ای با Go/No-Go. *(پاسخ: 31-3-ت6)*

**Q1.** Quick quiz (English): Why build and test in stages from the bottom layer upward? *(پاسخ: 31-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Go/No-Go | Go/No-Go decision | تصمیم ادامه/توقف |

- *Do not build the next layer until the current one is verified.* ← تا لایه‌ی فعلی تأیید نشده لایه‌ی بعد را نسازید.

### کارت Lab

**کارت Lab:** Build S1–S6. **Evidence:** `03-ops/capstone-build.md`.

### منابع

- درس ۳۱-۲
- Google SRE Book (Release engineering)

<a id="l-31-4"></a>

## درس 31-4 — Capstone II: آزمون کامل، Evidence Index نمونه‌ی پر، تحلیل سه خرابی و Sign-off

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۰ تا ۳۱-۳ · ≈ 11 ساعت**

> **وضعیت:** پروژه‌ی Capstone روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ همه‌ی دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. مجموعه‌ی آزمون پذیرش (مثبت، منفی، خرابی، کارایی) را با شناسه‌ی T-xx بسازید.
2. Evidence Index پر و قابل‌ردیابی به R# و T-xx بنویسید.
3. سه خرابی کنترل‌شده را اجرا و تحلیل کنید.
4. Gapها (آزمون‌های اجرا نشده/Unverified) را صادقانه ثبت کنید.
5. Sign-off با معیار پذیرش انجام دهید.
6. گزارش نهایی آزمون را بنویسید.

### چرا باید یاد بگیریم؟

ساختمان را قبل از تحویل با بازرس می‌گردند: آب، برق، آتش‌نشانی، همه با فهرست و امضا. پروژه‌ی شبکه هم تا وقتی آزمون پذیرش نشده «ساخته‌شده» است نه «تحویل‌شده». فقط مجموعه‌ی آزمونی که به نیازمندی‌ها وصل است و Evidence دارد، اثبات می‌کند طرح درست پیاده شد. و صداقت: آنچه اجرا نشده باید «اجرا نشده» نوشته شود نه «موفق».

### ساختار آزمون

| دسته | هدف | مثال |
|---|---|---|
| مثبت | کار می‌کند | ERP از شعبه |
| منفی | نباید کار کند | Guest→Internal |
| خرابی | رفتار هنگام خطا | قطع ISP |
| کارایی | عدد | Latency، Throughput |
| امنیتی | کنترل‌ها | MFA، Hardening |
| عملیاتی | Log/Backup | Restore |

### مجموعه‌ی آزمون پذیرش (نمونه)

| ID | R# | آزمون | معیار | نتیجه |
|---|---|---|---|---|
| T-01 | R1 | ERP از شعبه A/B/C | TCP 443، Latency < 40 ms | - |
| T-02 | R1 | Users→Internet با UTM | Web بلاک دسته‌ی ممنوع | - |
| T-03 | R2 | Reboot Hub Primary | Failover < 10 s | - |
| T-04 | R2 | قطع ISP1 شعبه | Failover < 5 s | - |
| T-05 | R2 | قطع Hub1 (BGP/BFD) | همگرایی < 10 s | - |
| T-06 | R3 | Guest→Internal | filtered (nmap) | - |
| T-07 | R3 | Guest→Internet | HTTP/S/DNS OK | - |
| T-08 | R4 | Dial-up بدون OTP | رد | - |
| T-09 | F2 | DMZ→DB | Timeout + Log Deny | - |
| T-10 | R4 | Dial-up با OTP | ورود OK، فقط ERP | - |
| T-11 | R5 | Log TLS در rsyslog | ورود Log | - |
| T-12 | R5 | Alert Brute-force | Alert < 5 min | - |
| T-13 | R6 | Restore روی Lab | RTO ≤ 30 min | - |
| T-14 | - | Hardening: scan WAN | مدیریت بسته | - |
| T-15 | R1 | Throughput Overlay | ≥ هدف | - |

### Evidence Index

| E-ID | T-ID | فایل | دستور/روش | زمان | Hash |
|---|---|---|---|---|---|
| E-01 | T-01 | e01_erp.txt | `curl -w`، `ping` | 2026-11-27 10:05 | sha256 |
| E-05 | T-03 | e05_failover.txt | ping 200 ms + شمارش | 10:40 | sha256 |
| E-09 | T-09 | e09_dmz_db.txt | `nc -vz`، Log | 11:10 | sha256 |
| E-13 | T-13 | e13_restore.txt | زمان‌سنجی | 12:00 | sha256 |

قواعد: هر Evidence فایل، زمان، دستور و Hash دارد؛ Secret ماسک.

### سه خرابی کنترل‌شده

| # | خرابی | انتظار | اندازه‌گیری |
|---|---|---|---|
| F-1 | Reboot Hub Primary | Failover + Session Pickup | زمان قطع |
| F-2 | قطع ISP1 شعبه | SD-WAN مسیر دوم | زمان + Session |
| F-3 | قطع Hub1 | BGP/BFD به Hub2 | زمان همگرایی |

روش اندازه‌گیری:

``` text
ping -i 0.2 10.0.20.30    (send every 200 ms)
Outage = lost packets x 0.2 s
Example: 22 lost x 0.2 = 4.4 s
```

### تحلیل نمونه

F-2: قطع ISP1 شعبه A: ۲۲ بسته گم = ۴٫۴ ثانیه (< 5 s) ✔. Sessionهای اینترنت قطع و دوباره برقرار؛ ERP (Overlay از ISP2) پس از ۷ ثانیه (BGP/IPsec Rekey) ✔ زیر 10.

### Gap

| T-ID | وضعیت | دلیل | اقدام |
|---|---|---|---|
| T-02 (AV) | اجرا نشده | بدون لایسنس | File Filter جایگزین؛ Needs-License |
| T-12 | اجرا نشده | SIEM Lab نیست | آزمون با Zabbix Trigger |
| دستورهای | Unverified | FortiOS 7.0.3 بوت‌نشده | تأیید در Lab |

### Sign-off

شرایط: همه‌ی آزمون‌های بحرانی (T-01، T-03، T-06، T-08، T-09، T-13) Pass؛ Gapها مستند و با ریسک پذیرفته‌شده‌ی مدیریتی؛ امضای مالک و مهندس.

``` text
Sign-off: Acceptance PASS (conditional) - Gaps G-1..G-3 accepted until 2027-01-31
Owner: ______  Engineer: ______  Date: ______
```

### مثال‌های حل‌شده

#### مثال ساده — T-06

`nmap -Pn 10.0.20.30` از Guest ⇒ همه filtered ⇒ Pass؛ Evidence: خروجی + Log Deny.

#### مثال متوسط — اندازه‌گیری

``` text
Lost 22 packets at 200 ms interval = 22 x 0.2 = 4.4 s
```

#### مثال متوسط — Evidence Index کامل

هر ردیف به R# و T# وصل است؛ ممیز می‌تواند از R4 به T-08 و E-08 برود.

#### مثال سخت — آزمون شکست‌خورده

T-05 همگرایی ۱۸ ثانیه (> 10). علت: BFD غیرفعال روی Hub2. رفع و تکرار آزمون؛ هر دو نتیجه در گزارش (Fail ⇒ Fix ⇒ Pass).

#### مثال سخت — صداقت

T-12 اجرا نشده. نباید «Pass» نوشت. در Sign-off Conditional با ریسک.

### Lab هدایت‌شده (اجرا نشده)

1. جدول آزمون و Evidence Index.
2. سه خرابی و اندازه‌گیری.
3. Sign-off و Gap.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Evidence بی‌Hash | بی‌روال | sha256 |
| آزمون بی‌R# | Traceability | اتصال |
| Fail | عیب | Fix/Retest |
| Pass کاذب | آزمون نشده | Gap |

### جمع‌بندی

آزمون پذیرش مثبت/منفی/خرابی/کارایی با T-xx؛ Evidence Index با Hash؛ سه خرابی با اندازه‌گیری؛ Gap صادقانه؛ Sign-off مشروط با ریسک.

### تمرین و ارزیابی

**ت1.** (ساده) Evidence Index چیست؟ *(پاسخ: 31-4-ت1)*

**ت2.** (ساده) وضعیت اجرا نشده؟ *(پاسخ: 31-4-ت2)*

**ت3.** (متوسط) Sign-off مشروط؟ *(پاسخ: 31-4-ت3)*

**ت4.** (متوسط) F2؟ *(پاسخ: 31-4-ت4)*

**ت5.** (سخت) دو آزمون اجرا نشده. *(پاسخ: 31-4-ت5)*

**ت6.** (سخت، طراحی) Evidence Index. *(پاسخ: 31-4-ت6)*

**Q1.** Quick quiz (English): What does a conditional sign-off mean? *(پاسخ: 31-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Sign-off | Acceptance sign-off | تأیید نهایی |

- *Record untested items honestly.* ← موارد آزمون‌نشده را صادقانه ثبت کنید.

### کارت Lab

**کارت Lab:** آزمون Capstone (اجرا نشده). **Evidence:** `03-ops/capstone-evidence.md`.

### منابع

- درس‌های فصل ۲۱ و ۳۰

<a id="l-31-5"></a>

## درس 31-5 — Capstone II: Runbook کامل نمونه، Handover و آزمون Runbook توسط همکار

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۴ · ≈ 11 ساعت**

> **وضعیت:** پروژه‌ی Capstone روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ همه‌ی دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Runbook عملیاتی کامل بنویسید (روزانه، هفتگی، ماهانه، رویدادی).
2. Handover (تحویل به تیم عملیات) را با مستندات و آموزش انجام دهید.
3. Runbook را توسط همکار آزمون کنید (Runbook Test).
4. قالب Runbook (Trigger، Pre-check، Steps، Verify، Rollback، Escalation) را رعایت کنید.
5. Contact/Escalation/On-call را تعریف کنید.
6. بازخورد را به Runbook برگردانید.

### چرا باید یاد بگیریم؟

بهترین طراحی بدون Runbook وابسته به حافظه‌ی یک نفر است. ساعت ۳ شب، وقتی آن نفر در دسترس نیست، همکار باید بتواند فقط با خواندن یک سند ۲ صفحه‌ای مشکل را حل یا درست Escalate کند. Runbook نوشته‌ی خوب «بدون فرض دانش قبلی» نوشته می‌شود و با آزمون توسط یک نفر دیگر اعتبار می‌گیرد؛ تا وقتی کس دیگری آن را اجرا نکرده، Runbook فقط ادعاست.

### قالب Runbook

``` text
RB-ID      : RB-07
Title      : Branch ISP failover - verify and escalate
Trigger    : Alert "SDWAN member dead" or user complaint
Owner      : NetOps (backup: SecOps)
Pre-check  : who is affected? time? recent change?
Steps      : numbered commands with expected output
Verify     : how to confirm resolved (positive + negative)
Rollback   : how to undo changes made
Escalation : when and to whom (phone/ticket)
Last test  : date, tester
```

### فهرست Runbookها

| ID | عنوان | نوع |
|---|---|---|
| RB-01 | چک روزانه (Dashboard، HA، VPN، Log، Backup) | روزانه |
| RB-02 | Backup/Restore Config | هفتگی/رویدادی |
| RB-03 | Change: Policy جدید | رویدادی |
| RB-04 | Failover Hub (آزمون/واقعی) | رویدادی |
| RB-05 | VPN شعبه Down | حادثه |
| RB-06 | SD-WAN/ISP | حادثه |
| RB-07 | ورود غیرمجاز Admin | امنیتی |
| RB-08 | Patch/Upgrade Cluster | ماهانه |
| RB-09 | کاربر دسترسی ندارد (۱۰ پرسش) | حادثه |
| RB-10 | بازبینی Policy و Drift | فصلی |

### نمونه‌ی RB-01 — چک روزانه

| گام | دستور/محل | انتظار |
|---|---|---|
| 1 HA | `get system ha status` | دو عضو، Primary درست |
| 2 CPU/Mem | `get system performance status` | CPU < 70٪، Mem < 80٪ |
| 3 VPN | `diagnose vpn ike gateway list` | همه‌ی شعبه‌ها established |
| 4 BGP | `get router info bgp summary` | همه Established |
| 5 SD-WAN | `diagnose sys sdwan health-check` | alive |
| 6 Log | Dashboard Zabbix/rsyslog | Log تازه (< 5 min) |
| 7 Backup | Git commit امروز | وجود |
| 8 Alert باز | Zabbix | بدون Critical باز |

زمان: ≤ ۱۵ دقیقه؛ هر غیرعادی ⇒ Ticket.

### نمونه‌ی RB-05 — VPN شعبه Down

``` text
Trigger : Zabbix "VPN tunnel BR-B down"
Pre     : is ISP up at branch? (ping WAN IP), recent change?
Step 1  : diagnose vpn ike gateway list name BR-B  -> status?
Step 2  : diagnose debug application ike -1 (filter dst-addr4 <BRANCH-WAN-IP>) 2 min
          read: no proposal chosen / AUTH failed / timeout?
Step 3  : act per table (Proposal/PSK/UDP 500-4500)
Verify  : tunnel established; ping 10.1.2.1 from Hub; BGP Established
Rollback: restore last config if change caused it
Escalate: if not resolved in 30 min -> Senior NetOps; ISP ticket if WAN down
```

### Handover

1. مستندات: HLD، LLD، IP Plan، Runbookها، Evidence Index، Gap، ریسک‌ها.
2. آموزش: ۲ جلسه (معماری + اجرای Runbookها).
3. دسترسی: حساب شخصی، MFA، Break-glass در Vault.
4. دوره‌ی Shadow: یک هفته همراهی.
5. امضای تحویل: تیم عملیات تأیید می‌کند می‌تواند Runbookها را اجرا کند.

### آزمون Runbook توسط همکار

روش:

1. همکاری که پروژه را نساخته انتخاب شود.
2. یک سناریو (مثلاً RB-05 با خرابی تزریق‌شده).
3. همکار فقط با Runbook کار کند؛ شما فقط مشاهده.
4. هر ابهام/گام جاافتاده ثبت.
5. Runbook اصلاح و دوباره آزمون.

ثبت: «Last test: 2026-11-27، tester: alice».

``` text
Findings (example):
- Step 2: filter command not shown -> added
- Expected output of Step 1 missing -> added
- Escalation phone outdated -> updated
```

### Contact و Escalation

| سطح | زمان | مخاطب |
|---|---|---|
| L1 | ۰–۳۰ دقیقه | NOC on-call |
| L2 | ۳۰–۶۰ دقیقه | NetOps/SecOps |
| L3 | ۶۰+ دقیقه | معمار/Senior |
| فروشنده | طبق SLA | TAC (FortiCare)، ISP |
| مدیریت | حادثه‌ی High | مدیر IT |

### مثال‌های حل‌شده

#### مثال ساده — بهبود Runbook

آزمون همکار نشان داد گام ۲ «دستور فیلتر» ندارد. افزودن دستور. نتیجه: همکار دوم آن را بدون پرسش اجرا کرد.

#### مثال متوسط — چک روزانه

RB-01 در ۱۲ دقیقه اجرا شد؛ یافته: Backup امروز ناموفق (Token منقضی). Ticket و رفع. ارزش چک روزانه.

#### مثال متوسط — Escalation

VPN Down ۲۵ دقیقه؛ تلاش‌ها بی‌نتیجه؛ طبق Runbook در دقیقه ۳۰ Escalate به L2 با Evidence (Debug). بدون زمان Escalation مهندس ساعت‌ها تنها می‌ماند.

#### مثال سخت — دانش ضمنی

سازنده می‌داند «شعبه C فقط از ISP2 پایدار است». این دانش در Runbook نیست؛ تیم تحویل‌گیرنده مرتب Failover اشتباه می‌دهد. راه: «Known Issues» در Runbook. هر دانش ضمنی باید نوشته شود.

#### مثال سخت — Runbook کهنه

پس از Upgrade، دستور تغییر کرد؛ Runbook قدیمی بود و همکار اشتباه عمل کرد. راه: Runbook نسخه‌دار، بازبینی با هر Upgrade/Change، Owner مشخص و «Last test» ≤ ۶ ماه.

### Lab هدایت‌شده (اجرا نشده)

1. RB-01 و RB-05 را کامل بنویسید.
2. توسط همکار آزمون کنید.
3. Handover Checklist.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| همکار گیر کرد | گام جاافتاده | بازخورد |
| Runbook کهنه | بدون بازبینی | نسخه |
| Escalation دیر | بی‌زمان | جدول |
| دانش ضمنی | ننوشته | Known Issues |

### جمع‌بندی

Runbook با قالب ثابت؛ چک روزانه و حادثه؛ Handover با آموزش و Shadow؛ آزمون توسط همکار؛ Escalation مشخص؛ Runbook نسخه‌دار و به‌روز.

### تمرین و ارزیابی

**ت1.** (ساده) Runbook چیست؟ *(پاسخ: 31-5-ت1)*

**ت2.** (ساده) چرا هر گام یک اقدام؟ *(پاسخ: 31-5-ت2)*

**ت3.** (متوسط) چرا همکار ناآشنا؟ *(پاسخ: 31-5-ت3)*

**ت4.** (متوسط) محتوای Handover؟ *(پاسخ: 31-5-ت4)*

**ت5.** (سخت) Runbook Failover ISP بنویسید. *(پاسخ: 31-5-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی نگهداری Runbook. *(پاسخ: 31-5-ت6)*

**Q1.** Quick quiz (English): Why should a runbook be tested by someone who did not write it? *(پاسخ: 31-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Runbook | Operational runbook | راهنمای عملیاتی |

- *Write runbooks for tired people at 3 AM.* ← Runbook را برای آدم خسته‌ی ساعت ۳ شب بنویسید.

### کارت Lab

**کارت Lab:** Runbook (اجرا نشده). **Evidence:** `03-ops/capstone-runbook.md`.

### منابع

- درس‌های ۲۷-۱، ۳۱-۴

<a id="l-31-6"></a>

## درس 31-6 — ارزیابی Capstone I و II: ارائه، Q&A، سؤال‌های دفاع و Rubric تفصیلی

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۰ تا ۳۱-۵ · ≈ 11 ساعت**

> **وضعیت:** پروژه‌ی Capstone روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ همه‌ی دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ارائه‌ی ۱۵ دقیقه‌ای از پروژه‌ی Capstone را ساختار دهید.
2. به سؤال‌های دفاع با پاسخ قابل‌اثبات (Evidence) جواب دهید.
3. Gap و ریسک را صادقانه و حرفه‌ای ارائه کنید.
4. با Rubric تفصیلی خودارزیابی کنید.
5. از سؤال‌های «چرا؟» و «چطور ثابت می‌کنید؟» نترسید.
6. بازخورد را به برنامه‌ی بهبود تبدیل کنید.

### چرا باید یاد بگیریم؟

پروژه‌ای که نتوانید از آن دفاع کنید مال شما نیست. در ممیزی واقعی، مصاحبه‌ی شغلی ارشد یا جلسه با مدیر، کسی دستورهای شما را نمی‌خواند؛ می‌پرسد «چرا؟ چطور ثابت می‌کنید؟ اگر ... شد چه؟». دفاع خوب یعنی هر ادعا به یک Evidence و هر تصمیم به یک ADR وصل باشد، و صادقانه بگویید چه چیزی را ثابت نکرده‌اید.

### ساختار ارائه (۱۵ دقیقه)

| بخش | زمان | محتوا |
|---|---|---|
| ۱ مسئله و نیازمندی‌ها | ۲ دقیقه | چه می‌خواستیم، R1–R6 |
| ۲ HLD | ۳ دقیقه | معماری، جریان‌ها |
| ۳ LLD و تصمیم‌ها | ۳ دقیقه | ADRها |
| ۴ آزمون و Evidence | ۴ دقیقه | T-xx، E-xx، خرابی‌ها |
| ۵ Gap و ریسک | ۲ دقیقه | صادقانه |
| ۶ جمع‌بندی | ۱ دقیقه | درس‌آموخته، گام بعد |

نکته: یک شکل برای معماری، یک جدول برای آزمون، یک عدد برای هر ادعا (Failover = ۴٫۴ ثانیه).

### سؤال‌های دفاع و پاسخ نمونه

| سؤال | پاسخ قابل‌اثبات |
|---|---|
| چرا NAT فقط روی Edge؟ | ردیابی کاربر، جلوگیری از Double NAT؛ Evidence: Session دو فایروال (E-05) |
| چرا DMZ→DB ممنوع؟ | محدود کردن حرکت جانبی؛ آزمون منفی T-09 و Log Deny (E-09) |
| Failover را چطور اندازه گرفتید؟ | Ping هر 200 ms و شمارش بسته؛ E-05 |
| چرا SSL VPN نه؟ | سابقه‌ی CVE و ADR-02؛ جایگزین IPsec Dial-up + MFA (T-08/T-10) |
| چه چیزی را ثابت نکرده‌اید؟ | T-02 (AV بدون لایسنس) و T-12؛ در جدول Gap با ریسک |
| اگر ISP-A و B هم‌زمان قطع شوند؟ | خارج از طراحی؛ ریسک پذیرفته؛ پیشنهاد: لینک LTE (هزینه) |
| چرا FMG/FAZ نه؟ | ADR-04: هزینه؛ جایگزین Syslog+Git؛ بازبینی سالانه |
| بدترین خطای شما؟ | `override enable` در آزمون که Failback ناخواسته داد؛ اصلاح و Runbook |

### فن پاسخ‌دادن

1. **عبارت‌بندی:** ادعا ← Evidence ← محدودیت.
2. **صداقت:** «این را اندازه نگرفتم؛ چون ...؛ اگر وقت بود ...».
3. **دامنه:** اگر سؤال خارج از طراحی است، بگویید و ریسک را نام ببرید.
4. **نه حدس:** «نمی‌دانم، ولی چطور پیدا می‌کنم: ...» بهتر از حدس غلط.

### Rubric تفصیلی (۱۰۰)

| معیار | امتیاز | توضیح |
|---|---|---|
| نیازمندی/ردیابی | 15 | SMART و ماتریس R↔T |
| طراحی | 25 | HLD/LLD صحیح و بدون Overlap |
| پیاده‌سازی | 15 | Config بدون رمز، Checkpointها |
| آزمون و Evidence | 25 | مثبت/منفی/خرابی با Hash |
| Runbook/Handover | 10 | آزمون توسط همکار |
| دفاع و ارائه | 5 | روشن و صادق |
| صداقت | 5 | Unverified و Gap |

قبولی ۷۵ با حداقل ۲۰ در آزمون/Evidence.

### خودارزیابی نمونه

``` text
Requirements 13/15 ; Design 22/25 ; Build 10/15 ; Test 15/25 (2 tests not run)
Runbook 8/10 ; Defense 4/5 ; Honesty 5/5  => 77/100 (conditional)
Improvement: run T-12/T-15 in lab; verify commands on a booted FortiOS
```

### مثال‌های حل‌شده

#### مثال ساده — پاسخ مستند

سؤال: «Guest واقعاً ایزوله است؟» پاسخ: «بله؛ T-06: nmap از Guest به شبکه‌ی داخلی همه filtered؛ Log Deny با ID E-06؛ Policy 13.»

#### مثال متوسط — پاسخ صادقانه

سؤال: «AV را آزمون کردید؟» پاسخ ضعیف: «بله کار می‌کند.» پاسخ قوی: «لایسنس AV نداشتیم؛ File Filter را آزمون کردیم (T-02b). آزمون AV امضایی اجرا نشد و در Gap ثبت شده است.»

#### مثال متوسط — خارج از دامنه

«اگر دیتاسنتر به‌طور کامل از بین برود؟» ⇒ DR سایت دوم خارج از دامنه‌ی این Capstone (ثبت در «خارج از دامنه»)؛ ریسک شناخته‌شده؛ پیشنهاد فاز بعد.

#### مثال سخت — حمله به تصمیم

«چرا Active-Passive و نه Active-Active؟ ظرفیت هدر می‌رود.» پاسخ: «ظرفیت ۲×نیاز ۵۵۰Mbps کافی بود (محاسبه)؛ Active-Active عیب‌یابی و Asymmetric ریسک می‌آورد؛ ADR-05؛ اگر رشد ۳ برابر شود بازنگری.» (تصمیم + داده + شرط بازنگری).

#### مثال سخت — اشتباه خودتان

داور می‌بیند Lifetime P2 سمت Hub و شعبه فرق دارد. قوی‌ترین پاسخ: «درست است؛ در آزمون دوم کشف شد (E-14) و اصلاح شد؛ Checklist ما اکنون جدول دوطرفه را بازبینی می‌کند.» اعتراف + اصلاح + پیشگیری.

### Lab هدایت‌شده (اجرا نشده)

1. ارائه‌ی ۱۵ دقیقه‌ای را تمرین کنید.
2. به هشت سؤال دفاع پاسخ مکتوب دهید.
3. خودارزیابی با Rubric.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| ارائه طولانی | بی‌ساختار | زمان‌بندی |
| پاسخ بی‌Evidence | ادعا | E-xx |
| دفاعی‌شدن | اشتباه پنهان | اعتراف+اصلاح |
| بی‌Gap | غیرصادق | جدول Gap |

### جمع‌بندی

ارائه‌ی ۱۵ دقیقه‌ای ساختاریافته؛ پاسخ‌های قابل‌اثبات با Evidence؛ Gap صادقانه؛ Rubric ۱۰۰ نمره‌ای؛ اعتراف+اصلاح+پیشگیری قوی‌ترین پاسخ به خطاست.

### تمرین و ارزیابی

**ت1.** (ساده) ساختار ارائه؟ *(پاسخ: 31-6-ت1)*

**ت2.** (ساده) نمره‌ی قبولی؟ *(پاسخ: 31-6-ت2)*

**ت3.** (متوسط) پاسخ به «چه چیزی ثابت نکرده‌اید؟» *(پاسخ: 31-6-ت3)*

**ت4.** (متوسط) خودارزیابی؟ *(پاسخ: 31-6-ت4)*

**ت5.** (سخت) «اگر دو ISP قطع شود؟» *(پاسخ: 31-6-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی بهبود. *(پاسخ: 31-6-ت6)*

**Q1.** Quick quiz (English): Why is honesty about unverified items part of the rubric? *(پاسخ: 31-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Q&A | Questions and Answers | پرسش و پاسخ |

- *Back every claim with evidence.* ← هر ادعا را با شاهد پشتیبانی کنید.

### کارت Lab

**کارت Lab:** ارزیابی Capstone (اجرا نشده). **Evidence:** `03-ops/capstone-eval.md`.

### منابع

- درس‌های ۳۱-۰ تا ۳۱-۵

## پاسخ‌های فصل 31

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 31-1

**31-1-ت1** — Failover شعبه A کمتر از ۱۰ ثانیه با آزمون ping پیوسته.

Failover شعبه کمتر از ۱۰ ثانیه با آزمون ping پیوسته.

**31-1-ت2** — ثبت تصمیم معماری با زمینه، گزینه‌ها، تصمیم و پیامدها.

ADR ثبت تصمیم معماری با زمینه، گزینه‌ها، تصمیم و پیامدها است.

**31-1-ت3** — 8.76 ساعت.

۹۹٫۹٪ در سال ≈ ۸٫۷۶ ساعت قطع مجاز.

``` text
(1 - 0.999) x 8760 h = 8.76 h
```

**31-1-ت4** — تا موفقیت قابل‌اندازه‌گیری باشد و بحث بعدی کم شود.

معیار پذیرش عددی تا موفقیت قابل‌اندازه‌گیری و بحث بعدی کم شود.

**31-1-ت5** — سطح‌بندی دسترس‌پذیری، ADR، پذیرش ریسک مستند.

سطح‌بندی دسترس‌پذیری، ADR و پذیرش ریسک مستند.

**31-1-ت6** — ساختار بالا با محتوای هر بخش.

سند طراحی: نیازمندی (R-xx با معیار)، HLD (نمودار و Zone)، LLD (آدرس، Interface، Route، Policy)، آزمون و ردیابی، ریسک و Gap، وضعیت (طراحی‌شده/اجرا نشده/اجراشده با شاهد).

**31-1-Q1** — So that success is measurable and can be verified objectively later.


### پاسخ‌های بازنویسی عمیق درس 31-2


### پاسخ‌های بازنویسی عمیق درس 31-2

**31-2-ت1** — HLD ساختار؛ LLD مقادیر دقیق.

HLD ساختار؛ LLD مقادیر دقیق.

**31-2-ت2** — برای ردیابی و ممیزی.

ردیف Policy نیازمندی دارد برای ردیابی و ممیزی.

**31-2-ت3** — تغییر Pool.

Overlap Pool VPN با Servers: Pool را تغییر دهید.

**31-2-ت4** — Edge.

NAT فقط روی Edge.

**31-2-ت5** — SD-WAN و Capture.

Asymmetric در LLD: SD-WAN و Capture.

**31-2-ت6** — جدول.

LLD Internal: جدول Interface، Route و Policy.

**31-2-Q1** — For traceability and audit.

### پاسخ‌های بازنویسی عمیق درس 31-3

**31-3-ت1** — تا علت خرابی محلی بماند و لایه‌ی بالا روی لایه‌ی نادرست ساخته نشود.

**31-3-ت2** — نقطه‌ی بازگشت با Backup و Tag.

Snapshot/Backup با Tag نقطه‌ی بازگشت است.

**31-3-ت3** — Guest به Internal باید Block باشد.

Guest به Internal باید Block باشد؛ آزمون منفی.

**31-3-ت4** — ≤ ۱۵ دقیقه؛ باید زمان‌سنجی شود.

Rollback ≤ ۱۵ دقیقه و باید زمان‌سنجی شود.

**31-3-ت5** — شواهد مستقل: ping DF برای MTU؛ زمان Failover برای Timer؛ رفع و اندازه‌گیری جدا.

**31-3-ت6** — جدول بالا با مسئول و زمان.

برنامه‌ی Build: ترتیب (Interface، Route، Policy، VPN، Logging)، مسئول، زمان و Checkpoint پس از هر مرحله با Evidence.

**31-3-Q1** — So a failure can be attributed to the stage just built instead of an unknown layer.


### پاسخ‌های بازنویسی عمیق درس 31-4


### پاسخ‌های بازنویسی عمیق درس 31-4

**31-4-ت1** — فهرست شاهدها با شناسه، فایل، زمان و نتیجه.

Evidence Index فهرست شاهدها با شناسه، فایل، زمان و نتیجه است.

**31-4-ت2** — صادقانه ثبت.

آزمون اجرانشده صادقانه ثبت شود.

**31-4-ت3** — با Gap و تاریخ.

Sign-off مشروط: با Gap و تاریخ.

**31-4-ت4** — Health-check.

F2 (Failover کند): Health-check را به Server خارجی تغییر دهید.

**31-4-ت5** — پذیرفته‌ی مشروط.

دو آزمون اجرانشده: پذیرفته‌ی مشروط.

**31-4-ت6** — جدول.

Evidence Index: جدول شناسه، آزمون، فایل، زمان، نتیجه، وضعیت.

**31-4-Q1** — Acceptance with documented gaps that must be closed later.

### پاسخ‌های بازنویسی عمیق درس 31-5


### پاسخ‌های بازنویسی عمیق درس 31-5

**31-5-ت1** — مجموعه‌ی گام‌های مستند برای وضعیت مشخص.

Runbook گام‌های مستند برای وضعیت مشخص است.

**31-5-ت2** — برای کاهش خطا.

هر گام یک اقدام تا خطا کم شود.

**31-5-ت3** — نقص‌های مبهم آشکار می‌شود.

همکار ناآشنا نقص‌های مبهم را آشکار می‌کند.

**31-5-ت4** — As-Built، LLD، Runbook، دسترسی.

Handover: As-Built، LLD، Runbook و دسترسی.

**31-5-ت5** — قالب بالا.

Runbook Failover ISP: ۸ گام با خروجی مورد انتظار.

**31-5-ت6** — فصلی و پس از حادثه.

نگهداری: بازبینی فصلی و پس از حادثه.

**31-5-Q1** — To reveal ambiguous or missing steps.

### پاسخ‌های بازنویسی عمیق درس 31-6


### پاسخ‌های بازنویسی عمیق درس 31-6

**31-6-ت1** — مسئله، HLD، LLD، آزمون، Gap، جمع‌بندی.

ساختار ارائه: مسئله، HLD، LLD، آزمون، Gap، جمع‌بندی.

**31-6-ت2** — ۷۵ با حداقل ۲۰ در Evidence.

نمره‌ی قبولی ۷۵ با حداقل ۲۰ در Evidence.

**31-6-ت3** — فهرست Unverified و آزمون اجرانشده.

پاسخ به «چه چیزی ثابت نکرده‌اید؟»: فهرست Unverified و آزمون اجرانشده.

**31-6-ت4** — نمره با دلیل.

خودارزیابی: نمره با دلیل برای هر معیار.

**31-6-ت5** — خارج از طراحی؛ ریسک؛ پیشنهاد.

«اگر دو ISP قطع شود؟»: خارج از طراحی؛ ریسک؛ پیشنهاد (LTE).

**31-6-ت6** — اقدام، مالک، تاریخ.

برنامه‌ی بهبود: اقدام، مالک، تاریخ.

**31-6-Q1** — Because claiming unverified results undermines trust and can cause real outages.

### پاسخ‌های درس افزوده‌ی 31-0 (فصل 31)


### پاسخ‌های بازنویسی عمیق درس 31-0

**31-0-ت1** — Specific, Measurable, Achievable, Relevant, Time-bound؛ مشخص، قابل‌اندازه‌گیری، شدنی، مرتبط، زمان‌دار.

**31-0-ت2** — تا هر نیازمندی آزمون و Evidence داشته باشد و هیچ آزمون بی‌هدف نماند.

**31-0-ت3** — مثلاً R-02: DMZ→DB ممنوع با ۱۰ آزمون منفی Deny و Log.

مثلاً R-02: DMZ→DB ممنوع با ۱۰ آزمون منفی Deny و Log.

**31-0-ت4** — «طراحی‌شده/اجرا نشده»، نه «موفق».

آزمون‌های اجرانشده «طراحی‌شده/اجرا نشده» ثبت می‌شوند نه «موفق».

**31-0-ت5** — اهمیت×ریسک؛ «باید»ها اول؛ Evidence هفتگی.

۱۲ نیازمندی در ۴ هفته: اهمیت×ریسک؛ «باید»ها اول؛ Evidence هفتگی.

**31-0-ت6** — جدول بالا با امتیاز و شواهد.

Rubric خودارزیابی: معیار، امتیاز، شاهد.

**31-0-Q1** — Because without a test and evidence the requirement is only an unverified claim.

# فصل 32 — Capstone III و IV: عملیات، حادثه و ارزیابی نهایی

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** Capstone I و II.
**Capstone III:** عملیات: مانیتورینگ، Change، Incident (شبیه‌سازی).
**Capstone IV:** Migration/ارتقا و ارزیابی نهایی دوره.
**هشدار صداقت:** حوادث فقط در Lab شبیه‌سازی شوند؛ نتایج بدون شاهد «اجرا نشده».
**اشتباهات رایج:** Change بدون Rollback؛ RCA سطحی؛ ادعای تسلط بدون شاهد.

**درس‌های فصل:**
- [درس 32-1 — عملیات روزانه و Change](#l-32-1)
- [درس 32-2 — شبیه‌سازی حادثه و RCA](#l-32-2)
- [درس 32-3 — Migration/ارتقا (کاربرد G11)](#l-32-3)
- [درس 32-4 — ارزیابی نهایی و Portfolio](#l-32-4)
- [درس 32-5 — Roadmap یادگیری بعدی](#l-32-5)
- [درس 32-6 — آزمون نهایی دوره](#l-32-6)

---

<a id="l-32-1"></a>

## درس 32-0 — عملیات واقعی: Change Management، ITIL و شبیه‌سازی حادثه (مقدمه‌ی Capstone III/IV)

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: فصل ۲۷ تا ۳۱ · ≈ 11 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. تفاوت «ساختن شبکه» و «اداره‌ی شبکه» را بگوید.
2. فرایندهای ITIL (Incident، Problem، Change، Release) را در یک سازمان شبکه‌ای نگاشت کند.
3. انواع تغییر (Standard، Normal، Emergency) را تفکیک کند.
4. شاخص‌های عملیات (MTTD، MTTR، Change Success Rate) را محاسبه کند.
5. نقش‌ها (Owner، Implementer، Reviewer، CAB) را بشناسد.
6. مسیر چهار Capstone را بفهمد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا عملیات؟** پزشک ماهر که ویزیت و پرونده ندارد، بیمار را از دست می‌دهد. بیشتر قطعی‌های جدی از «تغییر بدون ثبت»، «Backup آزمون‌نشده» و «حادثه بدون نقش» می‌آیند. سه ستون: Run، Change، Respond. Incident برای بازگرداندن سرویس؛ Problem برای حذف علت ریشه‌ای. Change سه نوع: Standard، Normal (CAB)، Emergency.

**جمع‌بندی اصلی درس:**

ساختن شبکه یک پروژه است و تمام می‌شود؛ اداره‌ی آن هر روز ادامه دارد. در سازمان‌های واقعی بیشترین قطعی‌ها بعد از «تغییر» رخ می‌دهد، نه به‌دلیل خرابی سخت‌افزار. پس مهارت اصلی مهندس عملیات این است که تغییر را کنترل‌شده، قابل‌برگشت و مستند انجام دهد و در حادثه آرام و روشمند عمل کند.

این درس چارچوب را می‌دهد و Capstone III (عملیات روزانه و Change، حادثه) و IV (Migration/Upgrade) را معرفی می‌کند.

### ۳) توضیح عمیق فنی

#### ۱) ITIL در یک نگاه

| فرایند | هدف | نمونه در شبکه |
|---|---|---|
| Incident | بازگرداندن سرویس سریع | قطع ISP |
| Problem | یافتن ریشه و جلوگیری از تکرار | Flap تکراری لینک |
| Change | تغییر کنترل‌شده | افزودن Policy |
| Release | استقرار نسخه | Upgrade FortiOS |
| Configuration Mgmt | دانستن وضعیت | As-Built، Git |

#### ۲) انواع Change

| نوع | ویژگی | مثال |
|---|---|---|
| Standard | از پیش تأییدشده، کم‌ریسک | افزودن Address Object |
| Normal | بررسی و تأیید | Policy جدید |
| Emergency | فوری، با ثبت بعدی | رفع قطعی |

در ITIL 4 این رویه **Change Enablement** نام دارد و تصمیم‌گیرنده **Change Authority** است که می‌تواند فرد، تیم (CAB) یا قاعده‌ی خودکار باشد؛ اختیار تأیید بر اساس ریسک تقسیم می‌شود نه همه‌چیز از یک هیئت مرکزی (منبع: خلاصه‌های ITIL 4؛ مرجع رسمی PeopleCert را بررسی کنید).

#### ۳) شاخص‌ها

``` text
MTTD = detection time - incident start
MTTR = recovery time - incident start
Change Success Rate = successful changes / total changes x 100
Example: 47 / 50 = 94 %
```

#### ۴) نقش‌ها

Owner (مالک سرویس)، Implementer (مجری)، Reviewer (بازبین فنی)، CAB (هیئت تأیید تغییر) برای تغییرات پرریسک.

#### ۵) چهار Capstone

| Capstone | موضوع |
|---|---|
| I | طراحی و ساخت |
| II | آزمون و Runbook |
| III | عملیات روزانه، Change، حادثه |
| IV | Migration/Upgrade |

#### ۶) اصل مهم

«قابل‌برگشت»: هیچ تغییری بدون Rollback Plan و Backup. و «قابل‌مشاهده»: پیش‌ و پس‌ از تغییر شاخص‌ها اندازه گرفته شود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| نوع Change | طبق ریسک |
| Rollback | اجباری |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

تغییر بدون ثبت ساعت ۲۳؛ فردا ۴۰ دقیقه جست‌وجو؛ با CHG ۲ دقیقه.

#### مثال متوسط

Standard: افزودن IP به Group؛ Normal: Policy پروژه؛ Emergency: بستن IP مهاجم با بازبینی ۲۴ ساعته.

#### مثال سخت

``` text
MTTR = (20 + 40 + 10 + 30) / 4 = 25 minutes
```

Emergency اشتباه: بلاک کل بلوک مشتری؛ فقط IP مهاجم.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** افزودن Address Object ⇒ Standard Change؛ ثبت در سیستم؛ بدون CAB.

**متوسط (شاخص):** ۵۰ تغییر، ۳ ناموفق: Change Success Rate = ۴۷/۵۰ = ۹۴٪. تحلیل: علت ۳ شکست؟ الگوی مشترک (مثلاً بدون Pre-check)؟ اقدام: چک‌لیست.

**سخت (Emergency):** قطع ISP ساعت ۲ بامداد؛ تغییر Emergency برای Failover دستی. مراحل: تصمیم Owner، ثبت لحظه‌ای، اجرا، Verify، ثبت رسمی تا ۲۴ ساعت، Review بعدی. ریسک: دور زدن فرایند؛ جبران: Review اجباری.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! process lesson
```

### ۸) Verification (اثبات صحت)

- شاخص‌ها محاسبه شد.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| تغییرات ناموفق | Pre-check | چک‌لیست |

### ۱۰) نکات امنیتی

- تغییر بدون تأیید ممنوع.

### ۱۱) جمع‌بندی مفهومی

- ساختن ≠ اداره.
- ITIL.
- Rollback و Verify.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Standard Change چیست؟ *(پاسخ: 32-0-ت1)*

**ت2.** (ساده) MTTR؟ *(پاسخ: 32-0-ت2)*

**ت3.** (متوسط) Change Success Rate برای ۴۷ از ۵۰؟ *(پاسخ: 32-0-ت3)*

**ت4.** (متوسط) CAB چیست؟ *(پاسخ: 32-0-ت4)*

**ت5.** (سخت) Emergency Change در بامداد. *(پاسخ: 32-0-ت5)*

**ت6.** (سخت، طراحی) فرایند Change. *(پاسخ: 32-0-ت6)*

**Q1.** Quick quiz (English): What is an emergency change? *(پاسخ: 32-0-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ITIL | Information Technology Infrastructure Library | چارچوب مدیریت سرویس |
| CAB | Change Advisory Board | هیئت مشاور تغییر |

- *Every change needs a rollback plan.* ← هر تغییر نیاز به Rollback Plan دارد.

### ۱۴) کارت Lab

**کارت Lab:** مقدمه‌ی عملیات (اجرا نشده). **Evidence:** `03-ops/ops-intro.md`.

### ۱۵) منابع

- ITIL 4 Foundation
- NIST SP 800-61

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Change در ITIL

نوع: Standard، Normal، Emergency. CAB برای Normal. هر Change: ریسک، Rollback، آزمون.

**پرسش‌های مصاحبه**
1. *Emergency؟* بازبینی بعدی.
2. *Freeze؟* دوره‌ی حساس.
3. *CMDB؟* منبع حقیقت.

### مثال حل‌شده: دسته‌بندی Change

- افزودن سرور به Address Group: Standard.
- Policy جدید برای پروژه: Normal (CAB).
- بستن IP مهاجم در حادثه: Emergency با بازبینی پس از ۲۴ ساعت.

### تکمیل عمیق: از «مهندس پیکربندی» تا «مهندس عملیات»

#### چرا این بخش را باید یاد بگیریم؟

تصور کنید یک پزشک ماهر دارید که جراحی را عالی بلد است ولی بعد از عمل، بیمار را ویزیت نمی‌کند، پرونده نمی‌نویسد و دارو را ثبت نمی‌کند. بیمار ممکن است بمیرد، نه به‌خاطر ضعف جراحی، بلکه به‌خاطر نبود **فرایند**. شبکه هم همین است. بیشتر قطعی‌های جدی سازمان‌ها نه از ضعف دانش فنی، بلکه از «تغییر بدون ثبت»، «Backup بدون آزمون» و «حادثه بدون نقش مشخص» می‌آید. این فصل شما را از کسی که فقط دستور می‌زند، به کسی تبدیل می‌کند که سازمان به او اعتماد می‌کند.

#### توضیح با زبان ساده

عملیات (Operations) یعنی همه‌ی کارهای تکراری و پیش‌بینی‌پذیر که شبکه را سالم نگه می‌دارد. سه ستون دارد:

1. **Run**: نگهداری روزانه؛ Health Check، Backup، بررسی هشدارها.
2. **Change**: هر تغییر با درخواست، تأیید، اجرا و بستن.
3. **Respond**: وقتی حادثه رخ داد، چه کسی چه می‌کند.

ITIL (Information Technology Infrastructure Library، یعنی «کتابخانه‌ی زیرساخت فناوری اطلاعات») مجموعه‌ی بهترین‌روش‌های صنعتی برای همین سه ستون است. نیازی نیست همه‌ی ITIL را پیاده کنید؛ سه فرایند آن کافی است: Incident Management (مدیریت حادثه)، Change Management (مدیریت تغییر) و Problem Management (مدیریت مسئله‌ی ریشه‌ای).

#### تفاوت Incident و Problem با مثال

صبح کاربران نمی‌توانند به سرور فایل برسند. شما Policy را اصلاح می‌کنید و همه چیز درست می‌شود؛ این **Incident** بود (هدف: برگرداندن سرویس). بعد می‌پرسید «چرا Policy اشتباه شده بود؟ چرا Change Review نکرده بودیم؟»؛ این **Problem** است (هدف: جلوگیری از تکرار).

#### مثال ساده — هزینه‌ی یک تغییر بدون ثبت

یک مهندس شب ساعت ۲۳ برای «رفع سریع» یک Policy را حذف می‌کند. فردا صبح ERP کار نمی‌کند. هیچ‌کس نمی‌داند چه چیزی تغییر کرده. تیم ۴۰ دقیقه Log می‌خواند تا بفهمد. اگر CHG ثبت شده بود، ۲ دقیقه کافی بود: «دیشب Policy 47 حذف شد».

#### مثال متوسط — سه نوع Change

| نوع | تعریف | مثال | تأیید |
|---|---|---|---|
| Standard | تکراری، کم‌ریسک، از پیش تأییدشده | افزودن IP به Address Group | بدون CAB |
| Normal | نیاز به بررسی | Policy جدید برای پروژه | CAB |
| Emergency | حادثه‌ی جاری | بستن IP مهاجم | تأیید سریع + بازبینی بعدی |

CAB = Change Advisory Board، یعنی «هیئت مشورتی تغییر»؛ گروهی که ریسک تغییرات بزرگ را بررسی می‌کند.

#### مثال سخت — تغییر اضطراری که اشتباه شد

حمله‌ی Brute-force به VPN. مهندس Emergency Change می‌زند و کل `203.0.113.0/24` را Block می‌کند. ۱۵ دقیقه بعد مشتری مهم (با IP در همین بلوک) نمی‌تواند وصل شود.

درس: Emergency هم باید حداقل‌های ثبت داشته باشد: چه، چرا، کی، Rollback. مراحل درست:

1. فقط IP مهاجم را Block کنید (نه کل بلوک).
2. زمان و دلیل را در Ticket بنویسید.
3. ظرف ۲۴ ساعت بازبینی کنید و Block اضافی را آزاد کنید.

#### فرمول عملی: اندازه‌گیری سلامت عملیات

``` text
Change success rate = successful changes / total changes x 100
MTTR = total repair time / number of incidents
MTTD = total detection time / number of incidents
```

MTTD = Mean Time To Detect (میانگین زمان تشخیص)، MTTR = Mean Time To Repair (میانگین زمان رفع). مثال: ۴ حادثه با زمان رفع ۲۰، ۴۰، ۱۰ و ۳۰ دقیقه.

``` text
MTTR = (20 + 40 + 10 + 30) / 4 = 25 minutes
```

#### Lab پیشنهادی (روی Lab ایزوله، بدون دست‌زدن به تجهیز واقعی)

1. یک قالب CHG بسازید.
2. یک تغییر فرضی (افزودن Policy) را کامل ثبت کنید: Pre-check، مراحل، Post-check، Rollback.
3. تغییر را در Lab اجرا کنید و زمان واقعی را ثبت کنید.
4. یک‌بار عمداً Rollback را تمرین کنید.

#### عیب‌یابی فرایند

| علامت | علت محتمل | رفع |
|---|---|---|
| CHG‌ها ناقص‌اند | قالب اجباری نیست | فیلدهای الزامی |
| Rollback کار نکرد | آزمون نشده بود | آزمون Rollback در Lab |
| تأیید دیر می‌شود | CAB سنگین | Standard Change برای کارهای تکراری |

#### پرسش‌های مرور با پاسخ

**۱. چرا Emergency Change هم ثبت می‌شود؟** چون بعداً باید بدانید چه چیزی تغییر کرد و آیا اثر جانبی داشت.

**۲. Incident و Problem چه فرقی دارند؟** Incident بازگرداندن سرویس است؛ Problem حذف علت ریشه‌ای.

**۳. چرا Standard Change بدون CAB است؟** ریسک آن قبلاً سنجیده و روش آن ثبت شده است.

**۴. MTTR چه چیزی را نشان می‌دهد؟** سرعت رفع، نه کیفیت پیشگیری.

#### English Corner

- *Change Advisory Board reviews high-risk changes before implementation.* هیئت مشورتی تغییرات پرریسک را قبل از اجرا بررسی می‌کند.
- *Every change must have a rollback plan.* هر تغییر باید برنامه‌ی بازگشت داشته باشد.
- Q: What is the difference between an incident and a problem?
- Q: Why do we measure MTTR?

## درس 32-1 — Capstone III: عملیات روزانه و Change Management (ITIL) — فرایند، قالب CHG و مثال کامل

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۲-۰ · ≈ 11 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. عملیات روزانه/هفتگی/ماهانه‌ی شبکه و فایروال را سازمان‌دهی کنید.
2. Change Management بر مبنای ITIL (Standard، Normal، Emergency) را اجرا کنید.
3. RFC/CHG کامل (دلیل، ریسک، آزمون، Rollback، تأیید) بنویسید.
4. تفاوت Incident، Problem و Change را بدانید و به هم وصل کنید.
5. KPIهای عملیاتی (MTTD، MTTR، Change Success Rate) را اندازه بگیرید.
6. CAB (Change Advisory Board) و Post-Implementation Review را برگزار کنید.

### چرا باید یاد بگیریم؟

یک فرودگاه با ۱۰۰۰ پرواز در روز بدون برج مراقبت و فرایند، هرج‌ومرج است. شبکه‌ی سازمانی هم همین: بیشترین خطاهای قطعی از «تغییرات برنامه‌ریزی‌نشده» می‌آید، نه از خرابی سخت‌افزار. مهندس ارشد مهارتش تنها دانستن دستور نیست؛ بلکه تغییر را کنترل‌شده، قابل‌برگشت و مستند انجام می‌دهد. ITIL چارچوب رایج این کار است.

### عملیات تکرارشونده

| دوره | کار | Runbook |
|---|---|---|
| روزانه | چک سلامت، Alertهای باز، Backup | RB-01 |
| هفتگی | بازبینی Log، Patch Advisory، ظرفیت | RB-02 |
| ماهانه | Patch، گزارش، Drill Failover | RB-08 |
| فصلی | بازبینی Policy/دسترسی، Restore Test | RB-10 |
| سالانه | DR Test، بازنگری معماری، لایسنس | - |

### سه مفهوم ITIL

| مفهوم | هدف | مثال |
|---|---|---|
| Incident | بازگرداندن سرویس سریع | VPN شعبه Down |
| Problem | یافتن و رفع ریشه | چرا VPN هر ماه قطع می‌شود؟ |
| Change | تغییر کنترل‌شده | افزودن Policy، ارتقا |

ارتباط: Incident تکراری ⇒ Problem ⇒ رفع ریشه با Change.

### انواع Change

| نوع | ویژگی | تأیید |
|---|---|---|
| Standard | کم‌ریسک، تکراری، از پیش مصوب | خودکار/Template |
| Normal | نیاز به ارزیابی ریسک | CAB/Reviewer |
| Emergency | فوری (حادثه) | تأیید سریع + Review بعدی |

### قالب CHG (RFC)

``` text
CHG-ID       : CHG-0123
Title        : Add HTTPS policy for new app server
Requester    : AppTeam      Owner: NetOps
Type         : Normal       Window: Sat 22:00-23:00
Reason       : business need REQ-882
Impact/Risk  : low; affects only 10.20.0.50; risk score 3x2=6
Plan         : numbered steps with commands
Test (pre/post): iprope lookup; curl; negative test
Rollback     : delete policy 340; restore backup <file> (<= 10 min)
Approvals    : Reviewer ___ ; Owner ___
Evidence     : paths
Result/PIR   : after execution
```

### فرایند

``` text
Request -> Assess (risk, impact) -> Approve (CAB/peer) -> Schedule (window, freeze)
-> Implement (backup first) -> Verify (tests) -> Close (evidence) -> PIR if failed
```

### Change Freeze و ریسک

``` text
Risk score = Likelihood x Impact
Score <= 6   : Standard/Normal with peer review
Score 7-14   : Normal + CAB + staging test
Score >= 15  : CAB + exec approval + extended rollback test
```

دوره‌ی Freeze (پایان سال، فروش ویژه): فقط Emergency.

### KPIها

| KPI | فرمول | هدف نمونه |
|---|---|---|
| Change Success Rate | موفق / کل | ≥ 95٪ |
| Emergency Change Ratio | Emergency / کل | ≤ 10٪ |
| MTTD | زمان کشف | ≤ 15 دقیقه |
| MTTR | زمان بازگردانی | ≤ 60 دقیقه |
| Backlog Problem | تعداد Problem باز | روند کاهشی |

``` text
Change Success Rate = successful / total x 100
Example: 57 / 60 x 100 = 95 %
```

### CAB

شرکت‌کنندگان: NetOps، SecOps، مالک سرویس، Help Desk. جلسه‌ی کوتاه هفتگی: مرور CHGهای هفته‌ی بعد؛ سؤال‌های کلیدی: «Rollback آزمون شده؟ چه کسی تحت تأثیر؟ پنجره درست؟».

### مثال‌های حل‌شده

#### مثال ساده — Standard Change

«افزودن Address Object جدید» تکراری و کم‌ریسک ⇒ Template Standard؛ بدون CAB؛ فقط Peer Review و ثبت.

#### مثال متوسط — CHG کامل

CHG-0123: Policy HTTPS؛ Plan، Pre-test (Lookup)، اجرای شنبه ۲۲:۰۰، Post-test (curl و آزمون منفی)، Rollback ≤ ۱۰ دقیقه. نتیجه: موفق؛ Evidence `chg-0123/`.

#### مثال متوسط — Incident به Problem

VPN شعبه B سه بار در ماه قطع شد (Incident ×3). Problem: علت ریشه MTU/Rekey. Change: MSS Clamp و Lifetime. بدون Problem تکرار Incident ادامه می‌یابد.

#### مثال سخت — Emergency

۰۲:۰۰: Policy اشتباه Production را قطع کرد. Emergency Change: Rollback فوری با تأیید تلفنی مدیر. فردا: CHG ثبت و Review: چرا تغییر بدون آزمون وارد Production شد؟

#### مثال سخت — شکست Change

Upgrade موفق به‌نظر رسید ولی VPN Phase2 پس از ۲ ساعت Down. KPI: Change Failure. PIR: آزمون Post-change فقط ping بود؛ Test Matrix ناقص. اقدام: Test Matrix کامل در قالب CHG.

### Lab هدایت‌شده (اجرا نشده)

1. CHG-0123 را کامل بنویسید.
2. ریسک و نوع Change را تعیین کنید.
3. KPIهای ماه را محاسبه کنید.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Change شکست | آزمون ناقص | Test Matrix |
| Emergency زیاد | بی‌برنامه | Standard/Template |
| Incident تکراری | Problem نیست | RCA |
| بدون Rollback | بی‌طرح | قالب CHG |

### نکات امنیتی

Change با MFA و Audit؛ جداسازی نقش (درخواست‌کننده ≠ تأییدکننده)؛ ثبت Evidence؛ بازبینی دسترسی.

### جمع‌بندی

عملیات روزانه تا سالانه؛ ITIL: Incident/Problem/Change؛ CHG کامل با ریسک و Rollback؛ CAB و KPI؛ Emergency با Review بعدی.

### تمرین و ارزیابی

**ت1.** (ساده) چه چیزی هر روز بررسی می‌شود؟ *(پاسخ: 32-1-ت1)*

**ت2.** (ساده) Pre-check؟ *(پاسخ: 32-1-ت2)*

**ت3.** (متوسط) CHG ناموفق چطور بسته می‌شود؟ *(پاسخ: 32-1-ت3)*

**ت4.** (متوسط) Window مناسب؟ *(پاسخ: 32-1-ت4)*

**ت5.** (سخت) Post-check Lookup=61. *(پاسخ: 32-1-ت5)*

**ت6.** (سخت، طراحی) قالب CHG. *(پاسخ: 32-1-ت6)*

**Q1.** Quick quiz (English): What should a post-check confirm after a change? *(پاسخ: 32-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| CHG | Change request | درخواست تغییر |

- *Always verify after the change.* ← پس از تغییر همیشه تأیید کنید.

### کارت Lab

**کارت Lab:** عملیات روزانه (اجرا نشده). **Evidence:** `03-ops/chg-0123.md`.

### منابع

- ITIL 4 Change Enablement

<a id="l-32-2"></a>

## درس 32-2 — Capstone III: شبیه‌سازی حادثه کامل — سناریو، نقش‌ها، Timeline نمونه، MTTD/MTTR و PIR

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۲-۰، ۲۹-۴ · ≈ 11 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. یک شبیه‌سازی کامل حادثه (چندمرحله‌ای با Inject) را اجرا کنید.
2. نقش‌ها (Incident Commander، Ops، Comms، Scribe) را تقسیم کنید.
3. ده‌گامی عیب‌یابی و Playbook پاسخ را هم‌زمان به‌کار ببرید.
4. Timeline، Evidence و Communication Log نگه دارید.
5. PIR بدون سرزنش و اقدام‌های SMART بنویسید.
6. MTTD/MTTR را محاسبه و با هدف مقایسه کنید.

### چرا باید یاد بگیریم؟

آتش‌نشان‌ها با تمرین می‌دوند، نه با مطالعه‌ی دستورالعمل در لحظه‌ی آتش. حادثه‌ی واقعی با فشار، ابهام و چند علت هم‌زمان همراه است. شبیه‌سازی (Game Day / Tabletop) این شرایط را بی‌خطر می‌سازد و نقاط ضعف Runbook، ارتباط و تصمیم‌گیری را پیش از حادثه‌ی واقعی نشان می‌دهد.

### نقش‌ها

| نقش | وظیفه |
|---|---|
| Incident Commander (IC) | تصمیم، اولویت، هماهنگی (نه تایپ دستور) |
| Ops Lead | اجرای فنی |
| Comms Lead | اطلاع‌رسانی به مدیر/کاربر |
| Scribe | ثبت Timeline و Evidence |
| SME | کارشناس موضوع (VPN/Firewall) |

اصل: یک نفر تصمیم می‌گیرد؛ یک نفر می‌نویسد؛ همه کار نمی‌کنند.

### سناریو (چندمرحله‌ای با Inject)

شرکت «لب»؛ جمعه ۱۴:۰۰ (اوج).

| زمان | Inject |
|---|---|
| T+0 | Helpdesk: «شعبه B ERP را نمی‌بیند» |
| T+10 | مانیتورینگ: BGP شعبه B Idle؛ تونل B↔Hub1 Down |
| T+20 | Hub1 پایین نمی‌آید ولی CPU 95٪ |
| T+30 | هشدار: ورودهای ناموفق SSH به Hub1 از IP ناشناس |
| T+45 | Log: تغییر Policy `ALL` توسط حساب `svc-tmp` در ساعت ۱۳:۴۰ |
| T+60 | شعبه C هم قطع (BGP) |

### مسیر حل (کلید)

1. **T+0–10 (Scope):** فقط B؟ همه؟ `diagnose vpn ike gateway list`.
2. **T+10–20:** تونل B به Hub1 Down؛ Hub2 چطور؟ (Failover BGP؟).
3. **T+20:** CPU بالا؛ `diagnose sys top` ⇒ `ipsengine`/`sshd`.
4. **T+30:** Brute-force SSH ⇒ احتمال نفوذ؛ **تغییر ماهیت:** حادثه‌ی امنیتی.
5. IC: اولویت دوم: «مهار» نه فقط «بازگرداندن».
6. Containment: Block IP (Local-in)، غیرفعال `svc-tmp` و `admin`، دسترسی Console.
7. Evidence: Snapshot Config + Log + Hash.
8. Eradication: حذف Policy ALL، حساب‌ها، تغییر همه‌ی Secretها (PSK، Admin، API Token).
9. Recovery: Restore Config پاک، تونل‌ها را دوباره، BGP Established، Failover به Hub2 تا اطمینان.
10. Monitor 72 ساعت.

### Communication Log

| زمان | مخاطب | پیام |
|---|---|---|
| T+15 | مدیر IT | «اختلال شعب؛ در حال بررسی؛ ETA بعدی در ۳۰ دقیقه» |
| T+35 | مدیر IT/امنیت | «نشانه‌ی ورود غیرمجاز؛ تیم امنیت درگیر» |
| T+70 | همه | «سرویس‌ها بازگشت؛ تحقیقات ادامه» |
| T+3d | مدیریت | PIR |

قاعده: پیام حقیقی، ساده، با زمان بعدی.

### Timeline نمونه

``` text
13:40 svc-tmp changed policy ALL (root cause start)
14:00 helpdesk: branch B ERP down       (T+0)
14:10 BGP B Idle                         (T+10)
14:30 SSH brute-force alert              (T+30) => security incident declared
14:50 contained (Local-in block, accounts disabled)
15:30 recovered (restore + tunnels up)
MTTD (from 13:40) = 14:30 - 13:40 = 50 min
MTTR (service)    = 15:30 - 14:00 = 90 min
```

### PIR

``` text
Root cause : svc-tmp (created via exposed SSH; weak password) -> policy ALL -> exfil/scan -> VPN instability
Went well  : Local-in block fast; backup clean; roles clear
Failed     : SSH exposed on WAN; Alert at 14:30 only; no config diff alert
Actions    : remove SSH from WAN (24h, NetOps); MFA+trusthost (7d, SecOps); daily config diff + alert (14d, NetOps); incident drill quarterly (SOC)
```

### مثال‌های حل‌شده

#### مثال ساده — نقش‌ها

IC (علی)، Ops (سارا)، Comms (رضا)، Scribe (نیلوفر). در T+30 IC می‌گوید: «سارا، Block IP؛ رضا، پیام امنیتی؛ نیلوفر، ساعت‌ها را ثبت کن.»

#### مثال متوسط — تغییر ماهیت

از «اختلال شبکه» به «حادثه‌ی امنیتی» در T+30. IC تصمیم گرفت: حفظ Evidence قبل از Restore. اگر فقط «تونل را بالا بیاور» اجرا می‌شد، شواهد از بین می‌رفت.

#### مثال متوسط — اولویت

دو کار هم‌زمان: بازگرداندن شعبه C و مهار نفوذ. IC: اول مهار (۱۵ دقیقه)، سپس بازیابی؛ چون بازیابی بدون مهار دوباره آلوده می‌شود.

#### مثال سخت — Inject غافلگیرکننده

T+50: Comms می‌گوید مدیر اجرایی می‌خواهد «همه‌چیز را خاموش کنید». IC: توضیح ریسک (نابودی Evidence، قطع کامل کسب‌وکار) و پیشنهاد جایگزین (ایزوله‌سازی Mgmt و Hub1). تصمیم مستند. این مهارت ارتباط است.

#### مثال سخت — نقد تمرین

Scribe فاصله‌ی ۱۰ دقیقه‌ای در Timeline داشت (همه درگیر بودند). یافته: قالب ثبت ساده‌تر؛ ابزار مشترک (Doc همزمان). آموزش نقش Scribe.

### Lab هدایت‌شده (اجرا نشده)

1. شبیه‌سازی Tabletop با نقش‌ها.
2. Timeline و Communication Log.
3. PIR و اقدام‌ها.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| همه کار می‌کنند | IC نیست | نقش |
| بی‌Timeline | Scribe | ثبت |
| Evidence گم | Restore زود | Snapshot |
| پیام متناقض | بی‌Comms | سخنگو |

### جمع‌بندی

شبیه‌سازی با نقش‌ها و Inject؛ تغییر ماهیت (اختلال ⇒ امنیتی)؛ مهار پیش از بازیابی؛ Timeline و ارتباطات؛ PIR بدون سرزنش و MTTD/MTTR.

### تمرین و ارزیابی

**ت1.** (ساده) Incident Commander؟ *(پاسخ: 32-2-ت1)*

**ت2.** (ساده) MTTD؟ *(پاسخ: 32-2-ت2)*

**ت3.** (متوسط) چرا Status دوره‌ای؟ *(پاسخ: 32-2-ت3)*

**ت4.** (متوسط) Scribe؟ *(پاسخ: 32-2-ت4)*

**ت5.** (سخت) PIR بنویسید. *(پاسخ: 32-2-ت5)*

**ت6.** (سخت، طراحی) Game Day. *(پاسخ: 32-2-ت6)*

**Q1.** Quick quiz (English): Why do we assign explicit roles during an incident? *(پاسخ: 32-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| IC | Incident Commander | فرمانده‌ی حادثه |

- *Communicate regularly during an incident.* ← در حادثه به‌طور منظم اطلاع‌رسانی کنید.

### کارت Lab

**کارت Lab:** شبیه‌سازی حادثه (اجرا نشده). **Evidence:** `03-ops/incident-sim.md`.

### منابع

- NIST SP 800-61 Rev.2 (در ۲۰۲۵ با Rev.3 جایگزین شده؛ مدل ۵ فاز کلاسیک مرجع آموزشی)
- Google SRE: Incident response

<a id="l-32-3"></a>

## درس 32-3 — Capstone IV: مهاجرت/ارتقای کامل در Lab — Plan زمان‌بندی‌شده، Post-check، Rollback و گزارش

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۰-۱ تا ۳۰-۴، ۳۲-۱ · ≈ 11 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. مهاجرت/ارتقای کامل را در Lab (از Plan تا Evidence) اجرا کنید.
2. Upgrade Path و Release Notes را بررسی کنید.
3. ارتقای Cluster HA بدون قطع طولانی (Uninterruptible) را برنامه‌ریزی کنید.
4. Rollback را آزمون و زمان‌سنجی کنید.
5. تست پیش/پس را با Baseline مقایسه کنید.
6. گزارش نهایی و درس‌آموخته بنویسید.

### چرا باید یاد بگیریم؟

ارتقای فایروال لبه از پرخطرترین کارهای دوره‌ای است: ممکن است Default تغییر کند، قابلیتی حذف شود، VPN Peer ناسازگار شود. ولی ارتقا نکردن هم خطرناک‌تر است (CVE). مهارت مهندس ارشد اجرای ارتقا به‌صورت قابل‌پیش‌بینی است: بررسی، Staging، Window، Rollback آزمون‌شده.

### Plan

``` text
T-14d  select target version (Recommended/Mature), read Release Notes + Known Issues
T-10d  upgrade path check (Fortinet Upgrade Path tool), license/hardware compat
T-7d   lab: restore production config into lab VMs, upgrade, run test matrix
T-3d   change request, CAB approval, rollback rehearsal
T-1d   backup full (encrypted) + baseline capture, go/no-go
T0     upgrade (HA: secondary first), verify
T+1d   monitor, close CHG, update inventory/runbooks
```

### بررسی Upgrade Path

- مسیر مستقیم یا میانی (مثلاً ممکن است پرش از ۶٫۴ به ۷٫۰ نیاز به نسخه‌ی میانی داشته باشد؛ در ابزار رسمی بررسی کنید).
- Release Notes: Changes in Default Behavior، Known Issues، تغییر Syntax (مثلاً Policy/VPN/SD-WAN).
- سازگاری سخت‌افزار و Peerها (FortiAP/FortiSwitch/FortiClient نسخه‌ی پشتیبانی).

### ارتقای HA بدون قطع طولانی

``` text
1 backup both members
2 upload image to primary; cluster upgrades secondary first
3 secondary reboots, rejoins, config sync verified (checksum)
4 failover to upgraded unit
5 primary upgrades and reboots, rejoins
6 optional failback (planned)
7 verify: HA status, VPN, BGP, SD-WAN, UTM, logs
```

نتیجه‌ی مورد انتظار: قطع کوتاه هنگام Failover (چند ثانیه)؛ Session Pickup بعضی Sessionها را نگه می‌دارد.

### Test Matrix (Baseline)

| # | آزمون | قبل | بعد |
|---|---|---|---|
| 1 | HA status + checksum | ok | ok |
| 2 | IPsec همه‌ی شعبه‌ها | up | up |
| 3 | BGP Established | ok | ok |
| 4 | SD-WAN Health-check | alive | alive |
| 5 | Policy hit/Deny غیرمنتظره | baseline | مقایسه |
| 6 | UTM (Web/DNS/File) | بلاک | بلاک |
| 7 | Dial-up + MFA | ok | ok |
| 8 | Syslog/SNMP | ok | ok |
| 9 | Throughput/CPU | N | ≈N |

### Rollback

``` text
Option A: reboot to previous firmware partition (execute set-next-reboot primary|secondary)
Option B: restore pre-upgrade config on previous firmware (if config converted)
Target  : <= 15 minutes; rehearsed in lab
```

نکته: پس از ارتقای نسخه‌ی اصلی، Config به قالب جدید تبدیل می‌شود؛ بازگشت به نسخه‌ی قدیمی با Config جدید ممکن است سازگار نباشد ⇒ حتماً Backup پیش از ارتقا.

### مثال‌های حل‌شده

#### مثال ساده — انتخاب نسخه

نسخه‌ی هدف: «Recommended» رسمی (مثلاً از جدول Fortinet «Recommended Release») نه جدیدترین. دلیل: بلوغ و باگ‌های کمتر؛ با ثبت در ADR.

#### مثال متوسط — Release Notes

یافته: در نسخه‌ی جدید Proposal پیش‌فرض IPsec تغییر کرده. اقدام: Proposal صریح در همه‌ی Phase1ها قبل از ارتقا؛ آزمون Lab.

#### مثال متوسط — زمان‌سنجی

``` text
Rollback rehearsal: 11 min (target <= 15) -> OK
Upgrade secondary: 8 min ; failover gap: 4 s ; primary: 8 min
Total window used: 35 min of 90
```

#### مثال سخت — شکست در Lab

Upgrade در Lab VPN Phase2 را شکست داد (Selector). کشف قبل از Production. رفع در Config و Test دوباره. ارزش Lab: هزینه‌ی خطا صفر. بدون آن Production.

#### مثال سخت — HA Out-of-sync پس از ارتقا

Secondary Config Sync نشد (`checksum` متفاوت). علت: اختلاف Build؛ رفع: `execute ha synchronize start` پس از هم‌نسخه‌شدن؛ Failover را تا Sync انجام ندهید. Log و Evidence.

### Lab هدایت‌شده (اجرا نشده)

1. Plan ارتقا و بررسی Upgrade Path.
2. Test Matrix پیش/پس.
3. Rollback Rehearsal.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| VPN بعد از ارتقا Down | Default تغییر | Proposal صریح |
| HA Sync نشد | Build | هم‌نسخه |
| Rollback ناسازگار | Config جدید | Backup قبل |
| Window کم | بی‌زمان‌سنجی | Rehearsal |

### نکات امنیتی

Image از منبع رسمی با Hash؛ Backup رمزگذاری‌شده؛ بعد از ارتقا Patch وضعیت؛ ثبت CHG و Evidence.

### جمع‌بندی

ارتقای کامل: انتخاب نسخه، Upgrade Path، Lab، HA ترتیبی، Test Matrix پیش/پس، Rollback آزمون‌شده، گزارش و درس‌آموخته.

### تمرین و ارزیابی

**ت1.** (ساده) Baseline؟ *(پاسخ: 32-3-ت1)*

**ت2.** (ساده) Checkpoint؟ *(پاسخ: 32-3-ت2)*

**ت3.** (متوسط) چرا Rollback زمان‌دار؟ *(پاسخ: 32-3-ت3)*

**ت4.** (متوسط) Session count ±؟ *(پاسخ: 32-3-ت4)*

**ت5.** (سخت) IPsec بعد Upgrade down؛ تصمیم. *(پاسخ: 32-3-ت5)*

**ت6.** (سخت، طراحی) Plan T-7d تا T+1d. *(پاسخ: 32-3-ت6)*

**Q1.** Quick quiz (English): Why define a rollback time limit before the change window? *(پاسخ: 32-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Cutover | Cutover | لحظه‌ی انتقال |

- *Define checkpoints with go/no-go criteria.* ← Checkpoint با معیار ادامه/توقف تعریف کنید.

### کارت Lab

**کارت Lab:** Capstone IV (اجرا نشده). **Evidence:** `03-ops/capstone-iv.md`.

### منابع

- Fortinet Upgrade Path Tool
- FortiOS 7.0 Release Notes

<a id="l-32-4"></a>

### ضمیمه: مثال کامل — برنامه‌ی ساعت‌به‌ساعت Upgrade

| ساعت | کار | Checkpoint |
|---|---|---|
| 21:30 | Backup هر دو، Hash، تأیید checksum | C1 |
| 22:00 | Upgrade Secondary و Boot | C2: in-sync |
| 22:20 | Failover به Secondary (جدید) | C3: سرویس بدون قطع طولانی |
| 22:25 | Upgrade Primary قبلی | C4: checksum |
| 22:45 | Post-check کامل (Test Matrix) | C5 |
| 23:00 | اعلام پایان و Monitoring | - |

**نقطه‌ی تصمیم Rollback:** اگر تا 22:40 C3 یا C4 موفق نشد ⇒ Rollback (Boot از Partition قبلی).

**گزارش:** مدت ۵۵ دقیقه (Plan ۶۰)، انحراف: Sync ۶ دقیقه کند بود؛ درس: پیش از Failover منتظر in-sync بمانید.

## درس 32-4 — ارزیابی نهایی و Portfolio: ماتریس مهارت، تحلیل شکاف، نگاشت نقش و نمونه‌ی Portfolio

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: کل دوره · ≈ 11 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. ماتریس مهارت (سطح ۱ تا ۴) را صادقانه پر کند.
2. شکاف‌ها را با شواهد تحلیل کند.
3. مهارت‌ها را به نقش‌های شغلی نگاشت کند.
4. Portfolio حرفه‌ای (پروژه، Evidence، Runbook) بسازد.
5. برنامه‌ی تکمیل شکاف بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Portfolio صادقانه؟** کارفرما به گواهی اعتماد نمی‌کند؛ به شواهد اعتماد می‌کند. سه سطح: اجراشده با شاهد، تأیید مستندی، اجرا نشده. بخش «محدودیت‌ها» اعتبار را بالا می‌برد.

**جمع‌بندی اصلی درس:**

پایان دوره یعنی «حالا چه کاری می‌توانم انجام دهم و چه چیزی را نمی‌دانم؟». ارزیابی صادقانه ارزشمندتر از ادعای بزرگ است؛ همان چیزی که در مصاحبه و ممیزی هم دیده می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) سطح‌ها

| سطح | معنی |
|---|---|
| 1 | آشنا (می‌دانم چیست) |
| 2 | با راهنما انجام می‌دهم |
| 3 | مستقل و با شاهد |
| 4 | آموزش می‌دهم و طراحی می‌کنم |

#### ۲) ماتریس نمونه

| مهارت | سطح | شاهد |
|---|---|---|
| Subnetting/VLSM | 3 | آزمون ۲-۱ |
| STP/L2 Security | 3 | Lab 4 (طراحی) |
| OSPF | 2 | Lab 5 (اجرا نشده) |
| FortiGate Policy/NAT | 2 | طراحی؛ Lab اجرا نشده |
| IPsec/SD-WAN | 2 | طراحی |
| Troubleshooting | 3 | پرونده‌های حل‌شده |
| Automation | 2 | Netmiko read-only |

#### ۳) تحلیل شکاف

- شکاف ۱: Labهای اجرا نشده ⇒ شواهد عملی نداریم.
- شکاف ۲: دستورهای Unverified.
- برنامه: اجرای Labها با اجازه، ثبت Evidence.

#### ۴) نگاشت نقش

| نقش | مهارت کلیدی | آمادگی |
|---|---|---|
| Network Admin | VLAN، OSPF، ACL | خوب |
| Firewall Engineer | FortiGate Policy، VPN، HA | متوسط (Lab لازم) |
| NOC Engineer | عیب‌یابی، Log | خوب |
| Security Analyst (Blue) | Log، PCAP، PIR | متوسط |

#### ۵) Portfolio

شامل: ۳ پروژه (Lab A، Capstone I، Capstone III)، Evidence Index، Runbook نمونه، PIR نمونه، توضیح شکاف‌ها (صادقانه)، بدون اطلاعات حساس.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| سطح | با شاهد |
| Portfolio | صادقانه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

ماتریس مهارت.

#### مثال متوسط — محدودیت‌ها

HA اجرا نشده؛ UTM بدون لایسنس؛ اعداد Lab.

#### مثال سخت

«Failover را چگونه اثبات می‌کنی؟» ping مداوم، قطع در ساعت X، ۳ بسته گم، Log.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** OSPF سطح ۲ چون Lab اجرا نشده؛ نه ۳.

**متوسط (شکاف):** شکاف FortiGate: طراحی داریم ولی اجرا نه؛ برنامه: اجرای Lab‌ها با اجازه‌ی صریح و ثبت Evidence.

**سخت (Portfolio):** Portfolio برای نقش Firewall Engineer: Capstone I و Runbook؛ با برچسب «طراحی؛ Lab اجرا نشده»؛ مصاحبه‌گر صداقت را می‌بیند.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! no CLI: evaluation lesson
```

### ۸) Verification (اثبات صحت)

- ماتریس با شاهد.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ادعا بدون شاهد | ماتریس | کاهش سطح |

### ۱۰) نکات امنیتی

- Portfolio بدون اطلاعات حساس.

### ۱۱) جمع‌بندی مفهومی

- صداقت.
- شکاف.
- Portfolio.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) سطح ۳ یعنی؟ *(پاسخ: 32-4-ت1)*

**ت2.** (ساده) شکاف چیست؟ *(پاسخ: 32-4-ت2)*

**ت3.** (متوسط) چرا Lab اجرا نشده سطح را کم می‌کند؟ *(پاسخ: 32-4-ت3)*

**ت4.** (متوسط) محتوای Portfolio؟ *(پاسخ: 32-4-ت4)*

**ت5.** (سخت) Portfolio برای Firewall Engineer. *(پاسخ: 32-4-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی پر کردن شکاف. *(پاسخ: 32-4-ت6)*

**Q1.** Quick quiz (English): Why is honest self-assessment valuable? *(پاسخ: 32-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Portfolio | Portfolio | نمونه‌کارها |

- *Show evidence for every skill you claim.* ← برای هر مهارتی که ادعا می‌کنید شاهد نشان دهید.

### ۱۴) کارت Lab

**کارت Lab:** ارزیابی نهایی (اجرا نشده). **Evidence:** `03-ops/skill-matrix.md`.

### ۱۵) منابع

- درس‌های کل دوره

<a id="l-32-5"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: ارزیابی و Portfolio

ماتریس مهارت: سطح هر حوزه + Evidence. Portfolio فقط شامل کارهای واقعاً اجراشده؛ موارد اجرا نشده صادقانه برچسب.

**پرسش‌های مصاحبه**
1. *Portfolio صادقانه؟* ضروری.
2. *Gap؟* برنامه.
3. *Evidence؟* Link.

### مثال حل‌شده: ماتریس مهارت

| حوزه | سطح | Evidence |
|---|---|---|
| Policy/NAT | تسلط | Lab |
| IPsec | متوسط | مستندی |
| HA | آشنا | اجرا نشده |

### تکمیل عمیق: ارزیابی نهایی و ساخت Portfolio صادقانه

#### چرا؟

کارفرما به «گواهی» اعتماد نمی‌کند؛ به **شواهد** اعتماد می‌کند. Portfolio یعنی پوشه‌ای که ثابت می‌کند «چه کرده‌اید». اما یک Portfolio پر از ادعای بدون اجرا از یک Portfolio کوچک و صادق بی‌اعتبارتر است.

#### سه سطح ادعا

| سطح | معنی | مثال |
|---|---|---|
| اجراشده با شاهد | در Lab اجرا و Log/اسکرین‌شات دارید | Policy+NAT+آزمون منفی |
| تأیید مستندی | از مستند رسمی خوانده و تطبیق داده‌اید | دستور HA |
| اجرا نشده | فقط مفهوم | VDOM بدون لایسنس |

همین سه برچسب را کنار هر مهارت بگذارید.

#### ماتریس مهارت (نمونه‌ی پر)

| حوزه | سطح | Evidence |
|---|---|---|
| Policy/NAT/VIP | اجراشده | CHG-07 + Log |
| IPsec Site-to-Site | اجراشده | `diagnose vpn tunnel list` |
| SD-WAN | تأیید مستندی | مرجع رسمی + برگه |
| HA | اجرا نشده | Needs-License |

#### محتوای Portfolio

1. معماری (HLD + LLD).
2. دو CHG کامل.
3. یک RCA از حادثه‌ی Lab.
4. Runbook.
5. Index شواهد.

#### مثال ساده

یک صفحه‌ی خلاصه: «شبکه‌ی دو فایروالی؛ ۴ Policy؛ ۲ Tunnel؛ ۳ آزمون منفی».

#### مثال متوسط — بخش «محدودیت‌ها»

``` text
Limitations:
 - HA not executed (no second licensed VM)
 - UTM profiles configured but signatures not updated (no FortiGuard license)
 - Performance numbers from Lab only
```

نوشتن محدودیت اعتبار را بالا می‌برد.

#### مثال سخت — مصاحبه

پرسش: «Failover را چطور ثابت می‌کنی؟» پاسخ ضعیف: «کار می‌کرد». پاسخ قوی: «ping مداوم، قطع لینک در ساعت X، ۳ بسته گم شد، Log حاوی رویداد Link-monitor، و اینجا اسکرین‌شات».

#### Lab

ماتریس مهارت را با برچسب سه‌سطحی بسازید و برای هر ردیف اجراشده یک فایل شاهد پیوست کنید.

#### عیب‌یابی Portfolio

| مشکل | رفع |
|---|---|
| ادعا بدون شاهد | برچسب «تأیید مستندی» |
| بیش‌ازحد شلوغ | ۵ کار شاخص |
| اسرار در فایل | Sanitize |

#### پرسش‌ها با پاسخ

**۱. چرا محدودیت‌ها را می‌نویسیم؟** صداقت و اعتماد.
**۲. Evidence خوب چیست؟** قابل‌تکرار و زمان‌دار.
**۳. چه چیزی در Portfolio نباید باشد؟** رمز، IP واقعی مشتری.

#### English Corner

- *Show evidence, not claims.*
- Q: How would you prove failover in an interview?

## درس 32-5 — Roadmap یادگیری بعدی: مسیر گواهی، Labهای اجرا نشده، Automation و برنامه‌ی ۶ ماهه

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۲-۴ · ≈ 11 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مسیرهای گواهی (Cisco، Fortinet، امنیت) را با پیش‌نیاز مقایسه کند.
2. برنامه‌ی ۶ ماهه با هدف، زمان و Evidence بنویسد.
3. Labهای اجرا نشده را اولویت‌بندی کند.
4. Automation و Observability را در برنامه جای دهد.
5. معیار موفقیت اندازه‌گیری‌پذیر تعیین کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا برنامه‌ی ۹۰ روزه؟** یادگیری بدون مقصد مثل رانندگی بدون مقصد است. هدف قابل‌اندازه‌گیری هر هفته؛ ۳۰ روز پایه، ۳۰ روز VPN/SD-WAN/HA، ۳۰ روز عیب‌یابی و Capstone. گواهی‌ها را از سایت رسمی بررسی کنید.

**جمع‌بندی اصلی درس:**

دوره پایان یافت ولی یادگیری نه. بدون برنامه، «بعداً Lab می‌زنم» هرگز اتفاق نمی‌افتد. این درس برنامه‌ی ۶ ماهه‌ی واقع‌بینانه می‌دهد.

### ۳) توضیح عمیق فنی

#### ۱) مسیر گواهی (نمونه؛ شرایط را از وب‌سایت رسمی تأیید کنید)

| مسیر | محتوا | پیش‌نیاز |
|---|---|---|
| Cisco CCNA | شبکه‌ی پایه تا Automation | فصل ۱ تا ۸ |
| Fortinet NSE 4 | FortiGate Security | فصل ۱۲ تا ۲۲ |
| Fortinet NSE 5/6 | FortiAnalyzer/FortiManager | فصل ۲۴، ۲۶ |
| Security (Blue Team) | Log، PCAP، PIR | فصل ۲۸، ۲۹ |

(نام و سطح گواهی‌ها ممکن است تغییر کند؛ `Unverified`.)

#### ۲) اولویت Labها

1. Phase 0B (Lab ایزوله) با اجازه.
2. FortiGate: Interface/Policy/NAT (فصل ۱۳).
3. IPsec و SD-WAN (فصل ۱۸، ۲۱).
4. HA (در صورت لایسنس).

#### ۳) برنامه‌ی ۶ ماهه

| ماه | هدف | Evidence |
|---|---|---|
| 1 | اجرای Lab فصل ۱ تا ۴ | Config + خروجی |
| 2 | OSPF/HSRP Lab | As-Built |
| 3 | FortiGate Policy/NAT/VIP | Evidence Index |
| 4 | IPsec/SD-WAN | Debug |
| 5 | Logging/Monitoring/Automation | Git repo |
| 6 | Capstone و مرور | Portfolio |

#### ۴) Automation

از Read-only (Netmiko) به Ansible `--check` و Git؛ هیچ تغییر خودکار بدون Pilot.

#### ۵) معیار موفقیت

«تا پایان ماه ۳، حداقل ۱۰ Lab با Evidence»؛ «تا پایان ماه ۶، Portfolio با ۳ پروژه».

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| برنامه | ۱۰ ساعت هفتگی |
| Evidence | هر ماه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

هر هفته یک Lab مستند.

#### مثال متوسط

``` text
Progress = 10 / 12 x 100 = 83 %
```

#### مثال سخت

BGP پله‌پله: Peer، Prefix، Policy، عیب‌یابی.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** ماه ۱: ۴ Lab فصل ۱ تا ۴ با خروجی؛ معیار: ۴ فایل Evidence.

**متوسط (اولویت):** منابع محدود؛ FortiGate اول چون هدف شغلی؛ سپس OSPF؛ برنامه‌ی هفتگی ۱۰ ساعت.

**سخت (شکست برنامه):** ماه ۳ نیمه‌کاره ماند؛ تحلیل: ساعت ناکافی؛ برنامه‌ی ماه ۴ با ۶ ساعت هفتگی و کاهش دامنه؛ معیار جدید.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! planning lesson
```

### ۸) Verification (اثبات صحت)

- برنامه با معیار.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| عقب‌افتادن | دامنه | کاهش |

### ۱۰) نکات امنیتی

- Labها فقط در محیط ایزوله.

### ۱۱) جمع‌بندی مفهومی

- برنامه‌ی ۶ ماهه.
- Evidence.
- Automation امن.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا برنامه‌ی ۶ ماهه؟ *(پاسخ: 32-5-ت1)*

**ت2.** (ساده) معیار موفقیت؟ *(پاسخ: 32-5-ت2)*

**ت3.** (متوسط) اولویت Lab؟ *(پاسخ: 32-5-ت3)*

**ت4.** (متوسط) Automation امن؟ *(پاسخ: 32-5-ت4)*

**ت5.** (سخت) برنامه شکست خورد. *(پاسخ: 32-5-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی ۶ ماهه. *(پاسخ: 32-5-ت6)*

**Q1.** Quick quiz (English): Why should a learning plan include measurable evidence? *(پاسخ: 32-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NSE | Network Security Expert | برنامه‌ی گواهی Fortinet |

- *Set measurable goals for each month.* ← برای هر ماه هدف قابل‌اندازه‌گیری تعیین کنید.

### ۱۴) کارت Lab

**کارت Lab:** Roadmap (اجرا نشده). **Evidence:** `03-ops/roadmap.md`.

### ۱۵) منابع

- صفحه‌ی رسمی گواهی Cisco و Fortinet (تأیید در زمان استفاده)

<a id="l-32-6"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Roadmap

مسیر: NSE 4 → NSE 7 (طبق سایت رسمی Fortinet)، CCNA/CCNP برای Cisco؛ Lab روزانه و مستندسازی.

**پرسش‌های مصاحبه**
1. *اولویت؟* هدف شغلی.
2. *Lab؟* منظم.
3. *جامعه؟* مستندات.

### مثال حل‌شده: برنامه‌ی ۹۰ روزه

ماه ۱: مرور مبانی و Lab؛ ماه ۲: VPN/SD-WAN؛ ماه ۳: عیب‌یابی و آزمون؛ هر هفته یک Lab مستند.

### تکمیل عمیق: ساخت برنامه‌ی یادگیری ۹۰ روزه با هدف مشخص

#### چرا؟

یادگیری بدون برنامه مثل رانندگی بدون مقصد است. این درس به شما یاد می‌دهد از «چه بخوانم؟» به «تا ۹۰ روز دیگر چه چیزی را ثابت خواهم کرد؟» برسید.

#### مسیرهای شغلی

| مسیر | مهارت اصلی | گواهی (طبق سایت رسمی) |
|---|---|---|
| Network Engineer | Routing/Switching/SD-WAN | CCNA → CCNP |
| Security Engineer | فایروال/VPN/UTM | NSE 4 → NSE 7 |
| SOC Analyst | Log/Detection | رشته‌ی Blue Team |

نام‌ها و سطوح گواهی را همیشه از سایت رسمی Cisco و Fortinet بررسی کنید؛ تغییر می‌کنند.

#### برنامه‌ی ۹۰ روز (نمونه)

``` text
Days 1-30   foundations: IP, routing, firewall policy/NAT (daily lab 1h)
Days 31-60  VPN, SD-WAN, HA concepts, monitoring
Days 61-90  troubleshooting + capstone + mock interview
Weekly      1 documented lab + 1 review of mistakes
```

#### مثال ساده

هدف هفته: «Policy+NAT+VIP». خروجی: یک CHG و یک آزمون منفی.

#### مثال متوسط — اندازه‌گیری پیشرفت

``` text
Progress = labs completed / labs planned x 100
10 / 12 x 100 = 83%
```

اگر کمتر از ۷۰٪ بود برنامه را کوچک کنید نه ترک.

#### مثال سخت — گیر کردن روی یک موضوع

BGP سخت است. روش: ۱) یک Lab دو‌روتری ۲) فقط Peer ۳) بعد Prefix ۴) بعد Policy ۵) بعد عیب‌یابی؛ هر مرحله یک شاهد.

#### Lab

برنامه‌ی ۹۰ روزه‌ی خودتان را با تاریخ و خروجی بنویسید.

#### عیب‌یابی انگیزه

| مشکل | رفع |
|---|---|
| خواندن بدون Lab | قانون ۵۰٪ Lab |
| فراموشی | مرور اشتباهات هفتگی |
| ترس از Lab | Snapshot قبل از هر تغییر |

#### پرسش‌ها با پاسخ

**۱. چرا خروجی هفتگی؟** مسئولیت‌پذیری.
**۲. چرا Snapshot؟** آزمون بدون ترس.
**۳. گواهی کافی است؟** خیر؛ شواهد.

#### English Corner

- *Set a measurable goal for each week.*
- Q: What will you prove in 90 days?

## درس 32-6 — آزمون نهایی دوره: سناریوی جامع، صورت مسئله، کلید پاسخ و Rubric

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: کل دوره · ≈ 12 ساعت**

> **وضعیت:** عملیات و Capstone III/IV روی Lab نظری (اجرا نشده)؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ هیچ تجهیز واقعی تغییر نمی‌کند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سناریوی جامع (Edge، Internal، VPN، SD-WAN، Logging) را تحلیل کند.
2. سه خرابی چندلایه را با روش ۱۰ گامی رفع کند.
3. طراحی، Policy و آزمون را با Evidence بنویسد.
4. گزارش حادثه و CHG را تحویل دهد.
5. با Rubric نمره‌دهی و صادقانه Gap را بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا راهبرد آزمون؟** آزمون نهایی فقط دانش نمی‌سنجد؛ مدیریت زمان، اولویت، شواهد و صداقت را هم. ۱۸۰ دقیقه: طراحی ۳۰، پیاده ۶۰، عیب‌یابی ۶۰، مستند ۳۰. ابتدا طراحی بعد CLI؛ هر مرحله Evidence؛ سقف ۱۰ دقیقه برای گیر کردن.

**جمع‌بندی اصلی درس:**

آزمون نهایی همه‌ی مهارت‌ها را در یک سناریو می‌سنجد. در دنیای واقعی خرابی تک‌علتی کم است؛ معمولاً دو علت با هم می‌آیند. روش و صبر مهم‌تر از سرعت است.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

شعبه با Edge FW (دو ISP، SD-WAN)، Internal FW، DMZ وب، IPsec به HQ، دورکاری، Syslog. گزارش: «بعضی کاربران اینترنت ندارند، VPN به HQ گاهی قطع می‌شود، وب از بیرون باز نمی‌شود.»

#### ۲) کلید

**علت ۱ (اینترنت):** Health-check فقط Gateway ISP-A. ISP-A قطع ولی Gateway زنده ⇒ Failover نمی‌شود. رفع: Server خارجی 8.8.8.8.

**علت ۲ (VPN):** MTU/MSS تونل؛ دانلود می‌ایستد. PMTU 1400 ⇒ MSS 1360. رفع: MSS-clamp.

**علت ۳ (وب):** Policy dst=IP داخلی نه VIP. رفع: dst=VIP.

#### ۳) روش

``` text
1 define symptom 2 route 3 policy 4 NAT 5 session 6 DNS 7 MTU 8 logs 9 sniffer+debug 10 verify
```

#### ۴) خروجی‌های لازم

- جدول علت/شاهد/رفع.
- CHG برای رفع‌ها (ترتیب، Window، Rollback).
- PIR کوتاه.
- Evidence Index.

#### ۵) Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| تشخیص ۳ علت با شاهد | 30 |
| رفع و آزمون مثبت/منفی | 20 |
| CHG و Rollback | 15 |
| PIR و شاخص‌ها | 15 |
| Evidence Index | 10 |
| صداقت (Unverified، Gap) | 10 |

قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترتیب رفع | لایه‌ی پایین‌تر اول |
| CHG | یک CHG با سه مرحله |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

تقسیم زمان.

#### مثال متوسط — ده‌گامی

scope، route، policy، session/nat، wire، verify.

#### مثال سخت

ادعای «HA را تنظیم کردم» بدون اجرا ⇒ پاسخ برتر: «اجرا نشد؛ طراحی و طرح آزمون ثبت شد».

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** علت ۳: Lookup=0 (no policy)؛ Policy dst=VIP؛ آزمون: HTTPS از بیرون 200.

**متوسط (چندعلتی):** ابتدا علت ۱ (اینترنت) رفع؛ سپس علت ۳؛ هر رفع جدا آزمون؛ در پایان VPN.

**سخت (کامل):** CHG-0301: ۱) Health-check ۲) Policy VIP ۳) MSS. Window شبانه؛ Rollback: Config قبلی. Post-check: Failover 4 s، وب 200، دانلود VPN ۱۰۰MB ok. PIR: ریشه‌ها، MTTD/MTTR، اقدام: چک‌لیست Health-check و MSS استاندارد.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sys sdwan health-check
diagnose firewall iprope lookup 203.0.113.10 40000 10.30.0.10 443 tcp port1
execute ping-options df-bit yes
```

### ۸) Verification (اثبات صحت)

- هر علت Evidence دارد.
- آزمون منفی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| چندعلتی | تفکیک | یکی‌یکی |

### ۱۰) نکات امنیتی

- رمز در گزارش نیاید.

### ۱۱) جمع‌بندی مفهومی

- روش ۱۰ گامی.
- چندعلتی.
- CHG/PIR.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) علت ۱ چیست؟ *(پاسخ: 32-6-ت1)*

**ت2.** (ساده) علت ۳؟ *(پاسخ: 32-6-ت2)*

**ت3.** (متوسط) ترتیب رفع؟ *(پاسخ: 32-6-ت3)*

**ت4.** (متوسط) MSS؟ *(پاسخ: 32-6-ت4)*

**ت5.** (سخت) CHG بنویسید. *(پاسخ: 32-6-ت5)*

**ت6.** (سخت، طراحی) PIR. *(پاسخ: 32-6-ت6)*

**Q1.** Quick quiz (English): Why fix multi-cause failures one at a time? *(پاسخ: 32-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PIR | Post-Incident Review | بازبینی پس از حادثه |

- *Isolate the layers and test after each fix.* ← لایه‌ها را جدا کنید و پس از هر رفع آزمون کنید.

### ۱۴) کارت Lab

**کارت Lab:** آزمون نهایی (اجرا نشده). **Evidence:** `03-ops/final-exam.md`.

### ۱۵) منابع

- کل دوره

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: آزمون نهایی

سناریوی جامع: طراحی، پیاده، عیب‌یابی، مستند. Rubric: طراحی ۲۰، اجرا ۲۰، عیب‌یابی ۲۵، مستندات ۱۵، صداقت ۲۰.

**پرسش‌های مصاحبه**
1. *چه چیز نمره‌ساز؟* Evidence.
2. *ادعای بدون اجرا؟* منفی.
3. *گزارش؟* RCA/Change.

### مثال حل‌شده: مدیریت زمان آزمون

طراحی 30 دقیقه، پیاده 60، عیب‌یابی 60، مستندات 30؛ شواهد را همان لحظه ثبت کنید.

### تکمیل عمیق: آزمون نهایی — راهبرد، زمان‌بندی و نمونه‌ی پاسخ برتر

#### چرا؟

آزمون نهایی فقط دانش را نمی‌سنجد؛ **مدیریت شرایط** را هم می‌سنجد: زمان، اولویت، ثبت شواهد و صداقت درباره‌ی آنچه نمی‌دانید.

#### ساختار پیشنهادی ۱۸۰ دقیقه

| بخش | زمان | وزن |
|---|---|---|
| طراحی (HLD/LLD) | 30 دقیقه | 20 |
| پیاده‌سازی | 60 دقیقه | 20 |
| عیب‌یابی سه خرابی | 60 دقیقه | 25 |
| مستندسازی/CHG/RCA | 30 دقیقه | 15 |
| صداقت و Evidence | در تمام مدت | 20 |

#### راهبرد حل

1. ابتدا صورت مسئله را دو بار بخوانید و نیازها را فهرست کنید.
2. طراحی را قبل از دست‌زدن به CLI بنویسید.
3. هر مرحله را بلافاصله تأیید و Evidence ذخیره کنید.
4. اگر گیر کردید، ۱۰ دقیقه سقف بگذارید و بروید به بخش بعد.

#### مثال: عیب‌یابی خرابی نمونه

«کاربران به DMZ نمی‌رسند». روش ده‌گامی کوتاه:

``` text
1 scope        : all users? one user?
2 route        : get router info routing-table details <dst>
3 policy       : diagnose firewall iprope lookup ...
4 session/nat  : diagnose sys session filter ...
5 wire         : diagnose sniffer packet ...
6 verify fix   : curl + negative test
```

#### نمونه‌ی پاسخ برتر برای «ادعا بدون اجرا»

پاسخ ضعیف: «HA را تنظیم کردم». پاسخ برتر: «HA به‌دلیل نبود دو VM لایسنس‌دار اجرا نشد؛ پیکربندی را از مستند رسمی نوشتم و آزمون Failover را با شاخص «کمتر از ۵ ثانیه» طراحی کردم؛ اجرا نشده.»

#### نمره‌دهی

``` text
Score = design + build + troubleshooting + docs + honesty
20 + 18 + 22 + 12 + 20 = 92
```

#### Lab

یک آزمون ۱۸۰ دقیقه‌ای شبیه‌سازی‌شده بدهید و زمان هر بخش را ثبت کنید.

#### عیب‌یابی عملکرد در آزمون

| مشکل | رفع |
|---|---|
| وقت‌کشی روی یک مسئله | سقف ۱۰ دقیقه |
| بی‌شاهد | ذخیره‌ی خروجی بلافاصله |
| پرش از طراحی | HLD کوتاه اول |

#### پرسش‌ها با پاسخ

**۱. چرا طراحی اول؟** CLI بدون طرح خطا می‌سازد.
**۲. چرا صداقت وزن دارد؟** اعتماد حرفه‌ای.
**۳. اگر وقت کم آمد؟** اولویت با موارد حیاتی و توضیح محدودیت.

#### English Corner

- *State clearly what you did not test.*
- Q: How do you prioritize under time pressure?

## پاسخ‌های فصل 32

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 32-1


### پاسخ‌های بازنویسی عمیق درس 32-1

**32-1-ت1** — سلامت، Alert، Backup، Log غیرعادی.

روزانه: سلامت، Alert، Backup و Log غیرعادی.

**32-1-ت2** — Backup و بررسی‌های قبل.

Pre-check: Backup و بررسی‌های قبل از تغییر.

**32-1-ت3** — Rollback، ثبت علت و درس.

CHG ناموفق: Rollback، ثبت علت و درس.

**32-1-ت4** — کم‌ترافیک با تیم آماده.

Window: زمان کم‌ترافیک با تیم آماده.

**32-1-ت5** — ترتیب Policy؛ Rollback؛ CHG جدید.

Post-check Lookup=61: ترتیب Policy؛ Rollback و CHG جدید.

**32-1-ت6** — قالب بالا.

قالب CHG: شناسه، عنوان، مالک/مجری/بازبین، دلیل، ریسک و اثر، Window، Pre-check، مراحل، Post-check، Rollback و تأیید. هر بخش یک ردیف.

**32-1-Q1** — That the change works as intended and nothing else broke.

### پاسخ‌های بازنویسی عمیق درس 32-2


### پاسخ‌های بازنویسی عمیق درس 32-2

**32-2-ت1** — تصمیم‌گیر و هماهنگ‌کننده.

Incident Commander تصمیم‌گیر و هماهنگ‌کننده است.

**32-2-ت2** — زمان تا کشف.

MTTD زمان تا کشف است.

**32-2-ت3** — اطمینان مدیریت و کاهش تماس‌ها.

Status دوره‌ای اطمینان مدیریت را می‌دهد و تماس‌ها را کم می‌کند.

**32-2-ت4** — ثبت Timeline.

Scribe Timeline را ثبت می‌کند.

**32-2-ت5** — قالب.

PIR: Summary، Impact، Timeline، Root cause، Actions.

**32-2-ت6** — سناریو و نقش‌ها.

Game Day: سناریو (قطع ISP-A و کیفیت پایین ISP-B)، نقش‌ها (IC، Operator، Scribe، Communicator)، Timeline و معیار موفقیت (MTTD < ۵ دقیقه، MTTR < ۴۵ دقیقه) و PIR.

**32-2-Q1** — To avoid confusion and ensure decisions, actions and records are handled.

### پاسخ‌های بازنویسی عمیق درس 32-3


### پاسخ‌های بازنویسی عمیق درس 32-3

**32-3-ت1** — وضعیت پیش از تغییر.

Baseline وضعیت پیش از تغییر است.

**32-3-ت2** — نقطه‌ی تصمیم.

Checkpoint نقطه‌ی تصمیم ادامه/توقف است.

**32-3-ت3** — برای تصمیم به‌موقع.

Rollback زمان‌دار برای تصمیم به‌موقع.

**32-3-ت4** — حدود ±۱۰٪.

Session count حدود ±۱۰٪.

**32-3-ت5** — Debug سریع؛ Rollback اگر در زمان.

IPsec بعد Upgrade down: Debug سریع؛ Rollback اگر در زمان.

**32-3-ت6** — جدول.

Plan: T-7d تا T+1d با Checkpoint C1 تا C5 و نقطه‌ی تصمیم Rollback (مثلاً ساعت ۲۲:۴۰). هر ردیف زمان، کار و معیار ادامه دارد.

**32-3-Q1** — To avoid delaying the decision and extending the outage.

### پاسخ‌های بازنویسی عمیق درس 32-4


### پاسخ‌های بازنویسی عمیق درس 32-4

**32-4-ت1** — مستقل و با شاهد.

سطح ۳: مستقل و با شاهد.

**32-4-ت2** — تفاوت سطح فعلی با هدف.

شکاف تفاوت سطح فعلی با هدف است.

**32-4-ت3** — شاهد عملی نیست.

Lab اجرا نشده شاهد عملی نمی‌دهد و سطح را کم می‌کند.

**32-4-ت4** — پروژه، Evidence، Runbook، PIR.

Portfolio: پروژه، Evidence، Runbook، PIR.

**32-4-ت5** — Capstone I، Runbook، برچسب صادقانه.

Portfolio Firewall Engineer: Capstone I، Runbook و برچسب صادقانه.

**32-4-ت6** — Lab، شاهد، زمان.

برنامه‌ی پر کردن شکاف: مهارت، سطح فعلی، سطح هدف، Lab لازم، Evidence و تاریخ؛ مثلاً FortiGate Policy/NAT سطح ۲→۳ با ۱۰ Lab و Evidence Index تا پایان ماه ۳.

**32-4-Q1** — It shows real skill level and guides focused improvement.

### پاسخ‌های بازنویسی عمیق درس 32-5


### پاسخ‌های بازنویسی عمیق درس 32-5

**32-5-ت1** — تا یادگیری به عمل تبدیل شود.

برنامه‌ی ۶ ماهه تا یادگیری به عمل تبدیل شود.

**32-5-ت2** — اندازه‌گیری‌پذیر.

معیار موفقیت اندازه‌گیری‌پذیر.

**32-5-ت3** — هدف شغلی.

اولویت Lab: هدف شغلی.

**32-5-ت4** — Read-only و Pilot.

Automation امن: Read-only و Pilot.

**32-5-ت5** — کاهش دامنه.

برنامه شکست خورد: دامنه را کم کنید.

**32-5-ت6** — جدول.

برنامه‌ی ۶ ماهه: ماه ۱ Lab فصل ۱ تا ۴؛ ماه ۲ OSPF/HSRP؛ ماه ۳ FortiGate Policy/NAT؛ ماه ۴ IPsec/SD-WAN؛ ماه ۵ Logging/Automation؛ ماه ۶ Capstone و Portfolio؛ هر ماه Evidence مشخص.

**32-5-Q1** — To verify real progress rather than assumed progress.

### پاسخ‌های بازنویسی عمیق درس 32-6


### پاسخ‌های بازنویسی عمیق درس 32-6

**32-6-ت1** — Health-check روی Gateway.

علت ۱: Health-check روی Gateway.

**32-6-ت2** — dst=IP داخلی.

علت ۳: Policy با dst=IP داخلی نه VIP.

**32-6-ت3** — لایه‌ی پایین‌تر اول.

ترتیب رفع: لایه‌ی پایین‌تر اول.

**32-6-ت4** — PMTU−40.

MSS = PMTU − 40.

**32-6-ت5** — سه مرحله با Rollback.

CHG سه‌مرحله‌ای: ۱) Health-check به 8.8.8.8 (Rollback: Config قبلی)، ۲) Policy VIP (Rollback: غیرفعال)، ۳) MSS-clamp (Rollback: حذف). Window شبانه، Post-check: Failover 4 s، وب 200 و دانلود VPN 100MB.

**32-6-ت6** — ریشه، شاخص، اقدام.

PIR: ریشه، شاخص، اقدام.

**32-6-Q1** — To know which change solved which problem.

### پاسخ‌های درس افزوده‌ی 32-0 (فصل 32)


### پاسخ‌های بازنویسی عمیق درس 32-0

**32-0-ت1** — تغییر کم‌ریسک و از پیش تأییدشده.

Standard Change تغییر کم‌ریسک و از پیش تأییدشده است.

**32-0-ت2** — میانگین زمان بازیابی.

MTTR میانگین زمان بازیابی است.

**32-0-ت3** — ۹۴٪.

Change Success Rate = ۴۷/۵۰ = ۹۴٪.

**32-0-ت4** — هیئت تأیید تغییرات پرریسک.

CAB هیئت تأیید تغییرات پرریسک است.

**32-0-ت5** — ثبت، تأیید Owner، اجرا، Verify، ثبت رسمی.

Emergency Change: ثبت، تأیید Owner، اجرا، Verify، ثبت رسمی.

**32-0-ت6** — ثبت، ارزیابی، تأیید، اجرا، Verify، Close.

فرایند Change: ثبت، ارزیابی، تأیید، اجرا، Verify، Close.

**32-0-Q1** — An urgent change to restore service that is documented and reviewed afterwards.

# پایان بخش ۱۱ (فصل‌های ۳۱ تا ۳۲)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- طراحی HLD/LLD، Build مرحله‌ای، Evidence، Runbook، Change/Incident، Migration، Portfolio.

## ۲) آزمون پایان سه فصل
**س1** — HLD؟

**س2** — LLD؟

**س3** — Acceptance Criteria؟

**س4** — Checkpoint؟

**س5** — Evidence؟

**س6** — Runbook؟

**س7** — Change؟

**س8** — RCA؟

**س9** — Post-check؟

**س10** — Cutover؟

**س11** — Portfolio؟

**س12** — Gap Analysis؟


## ۳) پاسخ آزمون
- **س1:** طراحی سطح بالا.
- **س2:** طراحی تفصیلی.
- **س3:** معیار پذیرش.
- **س4:** نقطه‌ی بازگشت.
- **س5:** شاهد.
- **س6:** دستور عملیاتی.
- **س7:** تغییر کنترل‌شده.
- **س8:** علت ریشه‌ای.
- **س9:** تست پس از تغییر.
- **س10:** سوئیچ نهایی.
- **س11:** نمونه‌کارها.
- **س12:** تحلیل شکاف.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| طراحی | L3 | Capstone I |
| عملیات | L3 | Capstone III |
| ارزیابی نهایی | L3 | آزمون نهایی |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. تمام Labها و Capstoneها اجرا نشده. 2. FortiGate بوت‌نشده؛ دستورها Unverified. 3. عمق فصل‌های ۱۰ تا ۳۲ کمتر از فصل‌های ۱ تا ۸ است.

## ۶) پیش‌نیازهای بخش بعد
ممیزی کل دوره؛ سپس تکمیل Phase 0B/FortiGate Boot با تأیید کاربر.

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*` و `02-design/*` (خروجی دانشجو)

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۳۲ |
| آخرین درس تکمیل‌شده | ۳۲-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | — |
| فایل تولیدشده | `course/Course_Part_11_Chapters_31-32.md` |
