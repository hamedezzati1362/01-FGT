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

**فصل ۳۱ · درس افزوده (پیش‌درس ۳۱-۱) · پیش‌نیاز: همه‌ی Gateها · ≈ ۴ ساعت**

> **وضعیت:** قالب ارزیابی؛ بدون شاهد واقعی «اجرا نشده».

### ۱) هدف آموزشی

دانشجو بتواند پروژه‌ی جامع را از **نیازمندی** تا **تحویل** با معیار پذیرش قابل‌اندازه‌گیری، ریسک‌ها و Evidence انجام دهد و کار خود را با **Rubric** ارزیابی کند.

### ۲) مفهوم پایه

Capstone یادگیری جدید نیست؛ **اثبات تسلط** است. مهندس را با «چه ساختی» نمی‌سنجند، با «ثابت کن کار می‌کند، امن است، قابل‌عیب‌یابی است و می‌شود تحویل داد».

### ۳) توضیح عمیق فنی

#### ۳-۱) نیازمندی‌ها

- عملکردی: سرویس‌ها، کاربران، مکان‌ها.
- غیرعملکردی: دسترس‌پذیری (RTO/RPO)، Performance، امنیت، انطباق.
- محدودیت‌ها: بودجه، لایسنس، زمان، تجهیزات Lab.

``` text
Availability % = (uptime / total time) x 100
Allowed downtime per year (99.9%) = 8.76 hours
```

#### ۳-۲) معیار پذیرش (SMART)

هر نیاز → معیار قابل‌آزمایش: «کاربر Finance فقط به SRV-FIN:443 دسترسی دارد؛ آزمون مثبت/منفی؛ Evidence = Log + Capture».

#### ۳-۳) ماتریس ردیابی

``` text
Requirement -> Design element -> Config object -> Test case -> Evidence
```

#### ۳-۴) Rubric ارزیابی (۱۰۰ امتیاز)

| معیار | وزن | سطح عالی |
|---|---|---|
| طراحی و IP Plan | 15 | بدون Overlap، توضیح تصمیم‌ها |
| Routing/Segmentation | 15 | Failover و Zone درست |
| Policy/Security | 20 | Least Privilege، UTM مناسب |
| VPN/SD-WAN/HA | 15 | رفتار خرابی اثبات‌شده |
| Troubleshooting | 15 | RCA با شواهد |
| مستندسازی/Runbook | 10 | تکرارپذیر |
| صداقت (Unverified/اجرا نشده) | 10 | هیچ ادعای بدون شاهد |

#### ۳-۵) ریسک و سناریوهای خرابی

برای هر جزء: «اگر خراب شود؟» (ISP، فایروال، Tunnel، DC، DNS). تست حداقل ۳ خرابی با Evidence.

### ۴) مثال حل‌شده

**نیاز:** شعبه‌ی جدید با دسترسی به ERP؛ 99.9٪. معیار: Tunnel + Failover < 30 s؛ ERP فقط 443؛ Guest ایزوله. ماتریس: Req-3 (Failover) → Dual-ISP SD-WAN → config sdwan → Test: قطع WAN1 → Evidence: ping + Log SLA. نمره‌دهی: Rubric.

**مثال سخت:** طراحی تضاد دارد: Backhaul (UTM مرکزی) در برابر Breakout (Latency). تصمیم با ADR (Architecture Decision Record): گزینه‌ها، معیار، انتخاب، ریسک.

### ۵) GUI و CLI

برای هر آزمون، هر دو مسیر (GUI و CLI) مستند؛ Evidence با خروجی خام.

### ۶) نکات امنیتی

- Secret در تحویل پاک شود.
- هر استثنای امنیتی با تاریخ بازبینی.

### ۷) جمع‌بندی

- نیاز → معیار → ماتریس ردیابی → آزمون → Evidence.
- Rubric شفاف؛ صداقت بخشی از نمره.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) 99.9٪ چقدر Downtime سالانه می‌دهد؟ *(پاسخ: 31-0-ت1)*

**ت2.** (متوسط) ماتریس ردیابی چیست؟ *(پاسخ: 31-0-ت2)*

**ت3.** (سخت) برای ۵ نیاز، معیار پذیرش و Evidence بنویسید. *(پاسخ: 31-0-ت3)*

**Q1.** Quick quiz (English): What is an acceptance criterion? *(پاسخ: 31-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ADR | Architecture Decision Record | ثبت تصمیم معماری |
| RTO/RPO | Recovery Time/Point Objective | هدف زمان/نقطه‌ی بازیابی |
| Rubric | Rubric | ماتریس ارزیابی |

- *Every requirement needs a testable acceptance criterion.* ← هر نیاز معیار پذیرش قابل‌آزمایش می‌خواهد.

### ۱۰) منابع

- ISO/IEC/IEEE 29148 (Requirements)؛ Google SRE Book (SLO/Availability)؛ ADR (M. Nygard).

## درس 31-1 — Capstone I: نیازمندی‌ها و سند طراحی سطح بالا (HLD) — با نمونه‌ی کامل

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۰، همه‌ی Gateها · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ دستورها `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. نیازمندی عملکردی/غیرعملکردی SMART بنویسد و ابهام را با پرسش‌های شفاف‌ساز رفع کند.
2. HLD کامل (دامنه، معماری، IP/VLAN/Zone، Routing/VPN/Firewall/HA، تصمیم‌ها، ریسک، پذیرش) تولید کند.
3. ADR برای تصمیم‌های کلیدی بنویسد.
4. معیار پذیرش و برنامه‌ی آزمون سطح بالا را تعریف کند.
5. طرح را با Rubric ارزیابی و بازبینی کند.

### ۲) مفهوم پایه: چیست و چرا؟

Capstone اثبات تسلط است. اولین قدم: نیازمندی‌ها. «شبکه‌ی چندشعبه بساز» نیازمندی نیست؛ «شعبه‌ی A باید ERP را با Latency زیر ۴۰ms و دسترس‌پذیری ۹۹٫۹٪ ببیند» نیازمندی است.

### ۳) توضیح عمیق فنی

#### ۱) پروژه‌ی مرجع

شرکت «لب»: HQ (دیتاسنتر و کاربران)، سه شعبه A/B/C. ISPهای دوگانه، Hub دوگانه، SaaS، دسترسی راه‌دور، انطباق Log ۱۸۰ روز.

#### ۲) نیازمندی‌ها (نمونه)

| ID | نوع | نیازمندی | معیار پذیرش |
|---|---|---|---|
| R1 | عملکردی | ERP از همه‌ی شعب | ping/TCP 443 موفق؛ Latency < 40 ms |
| R2 | غیرعملکردی | دسترس‌پذیری ۹۹٫۹٪ | Failover < 10 s؛ ≤ 8.76 h/سال |
| R3 | امنیتی | Guest ایزوله | nmap منفی: Guest→Internal filtered |
| R4 | امنیتی | دسترسی راه‌دور با MFA | ورود بدون OTP رد می‌شود |
| R5 | عملیاتی | Log ۱۸۰ روز و Alert | فایل Log و Alert آزمایشی |
| R6 | عملیاتی | Backup/Restore RTO ≤ 30 min | Restore Lab زمان‌سنجی‌شده |

``` text
Availability 99.9% -> downtime budget = 0.001 x 8760 h = 8.76 h/year
```

#### ۳) ساختار HLD

1) هدف/دامنه/فرض‌ها 2) نیازمندی‌ها 3) نمودار معماری 4) IP/VLAN/Zone 5) Routing/Overlay 6) Firewall/UTM/Auth 7) HA/SD-WAN 8) مانیتورینگ/Log/Backup 9) تصمیم‌ها (ADR) 10) ریسک‌ها 11) برنامه‌ی آزمون 12) پذیرش.

#### ۴) ADR (نمونه)

``` text
ADR-03: Local breakout for trusted SaaS only
Context: backhaul adds 33 ms to M365; budget limited
Options: A all-backhaul, B all-breakout, C hybrid
Decision: C; SaaS via ISDB/FQDN breakout with Web/DNS/File filter; rest via Hub
Consequences: need UTM at branch; central logging required; review quarterly
```

#### ۵) ریسک (نمونه)

| ریسک | احتمال | اثر | کنترل |
|---|---|---|---|
| CVE روی Hub | متوسط | بالا | Patch، Source Restriction |
| ISP تک‌شعبه | بالا | متوسط | Dual-ISP |
| Config خراب Sync | کم | بالا | Canary/Rollback |

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| SMART | هر نیاز معیار دارد |
| ADR | تصمیم‌های بزرگ |
| ریسک | احتمال×اثر |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** نیازمندی R1 تبدیل به معیار قابل‌آزمایش؛ جدول.

**متوسط (تحلیل):** تضاد بودجه/دسترس‌پذیری: ۹۹٫۹۹٪ نیاز به HA همه‌ی سایت‌ها؛ هزینه ×۲. تصمیم: ۹۹٫۹٪ شعب، ۹۹٫۹۹٪ HQ؛ ثبت در ADR و پذیرش ریسک.

**سخت (طراحی):** HLD کامل ۱۲ بخشی برای پروژه‌ی مرجع با نمودار و ADR؛ بازبینی با Rubric؛ ردیابی هر R به عنصر طراحی.

### ۸) Verification (اثبات صحت)

- HLD امضا‌شده.
- ماتریس ردیابی ابتدایی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| نیاز مبهم | بازبینی | SMART |

### ۱۰) نکات امنیتی

- ریسک امنیتی در HLD.

### ۱۱) جمع‌بندی مفهومی

- HLD = نیاز + معماری + تصمیم + ریسک + پذیرش.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) یک نیازمندی SMART مثال بزنید. *(پاسخ: 31-1-ت1)*

**ت2.** (ساده) ADR چیست؟ *(پاسخ: 31-1-ت2)*

**ت3.** (متوسط) 99.9٪ چند ساعت Downtime سالانه می‌دهد؟ *(پاسخ: 31-1-ت3)*

**ت4.** (متوسط) چرا معیار پذیرش از ابتدا؟ *(پاسخ: 31-1-ت4)*

**ت5.** (سخت) تضاد بودجه و دسترس‌پذیری را حل و ثبت کنید. *(پاسخ: 31-1-ت5)*

**ت6.** (سخت، طراحی) HLD ۱۲ بخشی را برای پروژه بنویسید. *(پاسخ: 31-1-ت6)*

**Q1.** Quick quiz (English): Why define acceptance criteria during requirements gathering? *(پاسخ: 31-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HLD | High-Level Design | طراحی سطح بالا |
| ADR | Architecture Decision Record | ثبت تصمیم معماری |
| SMART | Specific, Measurable, Achievable, Relevant, Time-bound | معیارهای نیاز خوب |

- *Define acceptance criteria first.* ← ابتدا معیار پذیرش را تعریف کنید.

### ۱۴) کارت Lab

**کارت Lab:** HLD. **Evidence:** `02-design/capstone-hld.md`.

### ۱۵) منابع

- ISO/IEC/IEEE 29148
- M. Nygard — ADR

<a id="l-31-2"></a>

## درس 31-2 — Capstone I: طراحی تفصیلی (LLD) — جدول Interface/Route/Policy/VPN و ماتریس ردیابی

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۱ · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ دستورها `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. LLD قابل‌اجرا (جداول Interface، Route، Policy، VPN، HA/SD-WAN، Object) بنویسد.
2. Test Plan با آزمون‌های مثبت/منفی/عملکرد/Failover بنویسد.
3. ماتریس ردیابی Req→Design→Config→Test→Evidence بسازد.
4. خروجی را با مهندس دیگر بازبینی (Peer Review) کند.

### ۲) مفهوم پایه: چیست و چرا؟

LLD باید طوری باشد که مهندس دیگری بتواند فقط با آن بسازد، بدون حدس.

### ۳) توضیح عمیق فنی

#### ۱) جدول Interface (نمونه)

| دستگاه | Interface | Zone | IP | نقش |
|---|---|---|---|---|
| FGT-HQ1 | port1 | WAN1 | 203.0.113.1/29 | ISP1 |
| FGT-HQ1 | port2 | LAN | 10.0.0.1/24 | Users |
| FGT-HQ1 | port3 | HA-HB | — | Heartbeat |
| FGT-A | wan1 | WAN | 198.51.100.2/30 | ISP1 |
| FGT-A | lan | LAN | 10.1.4.1/24 | Branch A |

#### ۲) Policy Matrix (نمونه)

``` text
Users->Internet : HTTP/HTTPS/DNS accept + UTM + log
Users->ERP      : TCP 443 to 10.0.20.10 accept + log
BranchA->ERP    : via IPsec TO-HUB accept + log
Guest->Internet : HTTP/HTTPS/DNS only, no internal
any->any        : deny + log
```

#### ۳) VPN/Routing

IKEv2 AES-GCM-256، DH20، PFS؛ iBGP RR در Hub؛ Local-pref Hub1 200/Hub2 100؛ Prefix-list؛ MTU 1400/MSS 1360؛ BFD 300×3.

#### ۴) Test Plan

| ID | Req | آزمون | نوع | معیار |
|---|---|---|---|---|
| T1 | R1 | TCP 443 A→ERP | مثبت | Latency < 40 ms |
| T2 | R3 | nmap Guest→Internal | منفی | filtered |
| T3 | R2 | قطع Hub1 | Failover | < 10 s |
| T4 | R4 | VPN بدون OTP | منفی | Reject |
| T5 | R6 | Restore Lab | RTO | ≤ 30 min |

#### ۵) ماتریس ردیابی

``` text
R1 -> HLD §5 overlay -> FGT-A tunnel+policy 120 -> T1 -> evidence E-01
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| سطح جزئیات | قابل‌اجرا |
| Review | Peer |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** جدول Interface برای ۲ دستگاه.

**متوسط (تحلیل):** Review: Policy بدون Log و Matrix با any؛ اصلاح؛ ثبت.

**سخت (کامل):** LLD کامل HQ+۳ شعبه با ۵ جدول و Test Plan؛ Peer Review؛ ردیابی ۶ نیاز.

### ۸) Verification (اثبات صحت)

- LLD بازبینی‌شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ناقص | Review | تکمیل |

### ۱۰) نکات امنیتی

- Least privilege.

### ۱۱) جمع‌بندی مفهومی

- LLD جداول+Test Plan+ردیابی.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) LLD چیست؟ *(پاسخ: 31-2-ت1)*

**ت2.** (ساده) ماتریس ردیابی چه چیزهایی را وصل می‌کند؟ *(پاسخ: 31-2-ت2)*

**ت3.** (متوسط) چرا Test Plan در LLD؟ *(پاسخ: 31-2-ت3)*

**ت4.** (متوسط) چرا Peer Review؟ *(پاسخ: 31-2-ت4)*

**ت5.** (سخت) Policy Matrix برای ۵ جریان بنویسید. *(پاسخ: 31-2-ت5)*

**ت6.** (سخت، طراحی) LLD کامل پروژه. *(پاسخ: 31-2-ت6)*

**Q1.** Quick quiz (English): What is the purpose of a traceability matrix? *(پاسخ: 31-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| LLD | Low-Level Design | طراحی تفصیلی |

- *Write the test plan together with the design.* ← Test Plan را همراه طراحی بنویسید.

### ۱۴) کارت Lab

**کارت Lab:** LLD. **Evidence:** `02-design/capstone-lld.md`.

### ۱۵) منابع

- ISO/IEC/IEEE 29148

<a id="l-31-3"></a>

## درس 31-3 — Capstone II: ساخت مرحله‌ای (S1–S6) با Checkpoint، دستورهای واقعی، آزمون هر مرحله و Rollback

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۲ · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Build را در شش مرحله با Checkpoint، Backup و Tag انجام دهد.
2. برای هر مرحله دستورهای پیاده‌سازی، آزمون‌های مثبت/منفی و معیار Go/No-Go را بنویسد و اجرا کند.
3. Rollback یک مرحله را اثبات و زمان آن را ثبت کند.
4. تغییرات را با Git و CHG ثبت کند.
5. خطاهای رایج هر مرحله را بشناسد.

### ۲) مفهوم پایه: چیست و چرا؟

ساخت یک‌جا یعنی وقتی خرابی دیده شد نمی‌دانید از کدام لایه است. ساخت مرحله‌ای (از پایین به بالا) و آزمون پس از هر مرحله علت را محلی نگه می‌دارد. اصل: **هیچ لایه‌ای بالا ساخته نمی‌شود تا لایه‌ی پایین‌تر آزمون نشده باشد.**

### ۳) توضیح عمیق فنی

#### جدول مراحل

| مرحله | کار | آزمون مثبت | آزمون منفی | Go/No-Go |
|---|---|---|---|---|
| S1 | L2/L3: VLAN، IP، SVI، DHCP/DNS/NTP | ping محلی، DHCP، NTP sync | VLAN Guest به LAN دسترسی ندارد | همه‌ی ping/DHCP OK |
| S2 | Routing: OSPF/BGP، Default | Route بین سایت‌ها | Prefix غیرمجاز رد | Route Count مطابق |
| S3 | Firewall: Zone، Policy، NAT، UTM پایه | Matrix مثبت | Guest→Internal block | همه‌ی T مثبت/منفی |
| S4 | IPsec/SD-WAN/Breakout | Tunnel Up، ERP OK | بدون Policy ⇒ block | Failover ≤ هدف |
| S5 | HA | Cluster، Failover | Split-brain کنترل‌شده Lab | Sync/Checksum |
| S6 | Monitoring، Log، Backup، Hardening | Alert، Restore | دسترسی غیرمجاز مدیریتی | Restore زمان‌سنجی |

#### دستورهای نمونه (S2 — روی Cisco و FortiGate)

``` text
! Cisco
router ospf 1
 router-id 1.1.1.1
 network 10.255.0.0 0.0.255.255 area 0
 passive-interface default
 no passive-interface GigabitEthernet0/1
show ip ospf neighbor ; show ip route ospf
```

``` text
# FortiGate
config router bgp
    set as 65000
    config neighbor-range
        edit 1
            set prefix 10.250.0.0 255.255.0.0
            set neighbor-group "SPOKES"
        next
    end
end
get router info bgp summary
```

#### Checkpoint

``` text
backup config -> git add/commit -m "S2 done" -> git tag s2 -> run tests T-S2 -> save evidence E-S2 -> record time
```

#### Rollback

``` text
restore config from tag s1 -> verify S1 tests -> record rollback duration (target <= 15 min)
```

#### خطاهای رایج

S1: Native/VLAN غایب؛ S2: MTU/Timer/Passive؛ S3: Policy any، Implicit rules؛ S4: Selector/MTU/Next-hop؛ S5: Heartbeat/Firmware؛ S6: Secret در Backup.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترتیب | پایین به بالا |
| Checkpoint | Tag+Backup |
| Rollback | ≤ ۱۵ دقیقه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** S1: VLAN 10/20/30، SVI، DHCP؛ ping محلی؛ tag s1.

**متوسط (تحلیل):** S3 شکست: Policy Guest→Servers باز بود. آزمون منفی T2 شکست؛ Rollback به s2؛ اصلاح Source؛ تکرار S3؛ زمان Rollback ۹ دقیقه.

**سخت (RCA چندمرحله‌ای):** S4: Tunnel Up ولی ERP کند. شواهد: ping DF 1372 شکست؛ Retransmission. علت: MTU. رفع: MSS Clamp/MTU؛ همچنین Failover 14 s (>10 s) ⇒ BFD؛ دو علت جدا با دو شاهد؛ هر کدام رفع و اندازه‌گیری؛ Evidence E-S4a/b.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute backup config sftp stage-s3.conf 192.168.90.10 backup-user <PASSWORD>
git add -A && git commit -m "S3 firewall done" && git tag s3
```

### ۸) Verification (اثبات صحت)

- Evidence هر مرحله.
- زمان Rollback ثبت.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| مرحله خراب | Test | Rollback به Tag قبلی |
| Evidence ناقص | Index | تکمیل |

### ۱۰) نکات امنیتی

- Secret پاک.
- CHG برای هر مرحله.

### ۱۱) جمع‌بندی مفهومی

- مرحله‌ای + Checkpoint.
- آزمون مثبت/منفی.
- Rollback اثبات‌شده.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا ترتیب پایین به بالا؟ *(پاسخ: 31-3-ت1)*

**ت2.** (ساده) Checkpoint چیست؟ *(پاسخ: 31-3-ت2)*

**ت3.** (متوسط) آزمون منفی S3 چیست؟ *(پاسخ: 31-3-ت3)*

**ت4.** (متوسط) هدف زمان Rollback؟ *(پاسخ: 31-3-ت4)*

**ت5.** (سخت) دو علت هم‌زمان در S4؛ روش جداسازی. *(پاسخ: 31-3-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Build ۶ مرحله‌ای با Go/No-Go. *(پاسخ: 31-3-ت6)*

**Q1.** Quick quiz (English): Why build and test in stages from the bottom layer upward? *(پاسخ: 31-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Go/No-Go | Go/No-Go decision | تصمیم ادامه/توقف |

- *Do not build the next layer until the current one is verified.* ← تا لایه‌ی فعلی تأیید نشده لایه‌ی بعد را نسازید.

### ۱۴) کارت Lab

**کارت Lab:** Build S1–S6. **Evidence:** `03-ops/capstone-build.md`.

### ۱۵) منابع

- درس ۳۱-۲
- Google SRE Book (Release engineering)

<a id="l-31-4"></a>

## درس 31-4 — Capstone II: آزمون کامل، Evidence Index نمونه‌ی پر، تحلیل سه خرابی و Sign-off

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۳ · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Test Plan را کامل اجرا و Evidence Index (≥ ۲۰ ردیف) بسازد.
2. سه خرابی (ISP، Tunnel/Hub، فایروال HQ) را زمان‌سنجی و تحلیل کند.
3. انحراف از معیار را RCA و اصلاح کند.
4. Sign-off با مالکان نیاز بگیرد.
5. محدودیت‌ها و «اجرا نشده»ها را صریح اعلام کند.

### ۲) مفهوم پایه: چیست و چرا؟

Evidence Index قلب ارزیابی است: هر ادعا به یک آزمون و یک خروجی خام وصل است. اگر ردیفی خالی است، یعنی آن ادعا هنوز تأییدنشده است.

### ۳) توضیح عمیق فنی

#### Evidence Index (نمونه‌ی پر)

``` text
ID    Req Test                           Command/Capture                     Result      P/F  File     Time
E-01  R1  Branch A -> ERP TCP 443        curl -w "%{time_connect}" ...       31 ms       P    e01.txt  19:30
E-02  R3  Guest -> Internal (negative)   nmap -Pn -p 1-1024 10.0.20.10       filtered    P    e02.txt  19:34
E-03  R2  Cut Hub1 (continuous ping)     ping -i 0.2 + timestamps            lost 31 pk  P    e03.txt  19:42   (6.2 s)
E-04  R4  VPN login without OTP          FortiClient attempt                 rejected    P    e04.png  19:50
E-05  R5  Syslog 180d / alert test       tail + alert screenshot             received    P    e05.txt  19:55
E-06  R6  Restore in lab                 execute restore ... stopwatch       27 min      P    e06.txt  20:20
E-07  R2  Cut ISP1 at Branch A           SD-WAN health-check + ping          8.4 s       P    e07.txt  20:31
E-08  R2  HQ FW1 power-off               ha status + ping                    4.1 s       P    e08.txt  20:40
```

#### سه خرابی

| خرابی | زمان | Session | اثر | Log |
|---|---|---|---|---|
| ISP1 شعبه A | 8.4 s | TCP قدیمی قفل ⇒ Clear | ERP | SLA event |
| Hub1 | 6.2 s | iBGP Reconverge | Spoke-to-Spoke | BGP reset |
| FW1 HQ | 4.1 s | Pickup TCP | ERP | HA event |

#### انحراف و RCA

اگر E-03 = 14 s (>10 s): علت BGP Hold 180؛ BFD 300×3 و MRAI؛ تکرار؛ ثبت دو آزمون.

#### Sign-off

مالک نیاز (ERP)، امنیت، شبکه؛ امضا با تاریخ.

#### محدودیت‌ها

فهرست آنچه اجرا نشده (مثلاً HA چون Needs-License)؛ آن ردیف‌ها «اجرا نشده» و Pass نیستند.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** E-01..E-08 همه Pass.

**متوسط (تحلیل):** E-03 = 14 s: علت Hold؛ BFD؛ E-03b = 6.2 s.

**سخت (جامع):** تفکیک «Pass» با شاهد از «اجرا نشده»؛ ۲ ردیف HA اجرا نشده (لایسنس)؛ گزارش صادقانه و ریسک باقی‌مانده.

### ۸) Verification (اثبات صحت)

- Index کامل؛ Sign-off.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| شاهد ناقص | Index | تکمیل |

### ۱۰) نکات امنیتی

- Secret.

### ۱۱) جمع‌بندی مفهومی

- شاهد و RCA و Sign-off.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Evidence Index چه ستون‌هایی دارد؟ *(پاسخ: 31-4-ت1)*

**ت2.** (ساده) ردیف بدون خروجی چه وضعیتی دارد؟ *(پاسخ: 31-4-ت2)*

**ت3.** (متوسط) E-03=14 s؛ اقدام؟ *(پاسخ: 31-4-ت3)*

**ت4.** (متوسط) چرا Sign-off؟ *(پاسخ: 31-4-ت4)*

**ت5.** (سخت) HA اجرا نشده؛ چگونه گزارش می‌کنید؟ *(پاسخ: 31-4-ت5)*

**ت6.** (سخت، طراحی) Index ۲۰ ردیفی برای پروژه. *(پاسخ: 31-4-ت6)*

**Q1.** Quick quiz (English): What status should an untested requirement receive in the evidence index? *(پاسخ: 31-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Sign-off | Acceptance sign-off | تأیید پذیرش |

- *Report untested items as not executed.* ← موارد آزمون‌نشده را «اجرا نشده» گزارش کنید.

### ۱۴) کارت Lab

**کارت Lab:** Evidence. **Evidence:** `03-ops/capstone-evidence.md`.

### ۱۵) منابع

- درس ۳۱-۰

<a id="l-31-5"></a>

## درس 31-5 — Capstone II: Runbook کامل نمونه، Handover و آزمون Runbook توسط همکار

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۴ · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Runbook ۳ سرویس (VPN شعبه، فایروال HQ/HA، Log/Backup) با قالب کامل بنویسد.
2. جلسه‌ی Handover را برنامه‌ریزی و اجرا کند.
3. Runbook را با «آزمون همکار» اعتبارسنجی کند.
4. Escalation و تماس‌ها را مشخص کند.

### ۲) مفهوم پایه: چیست و چرا؟

Runbook خوب یعنی کسی که طراح نبوده بتواند عیب را در ساعت ۳ بامداد رفع کند. معیار کیفیت: «آزمون همکار».

### ۳) توضیح عمیق فنی

#### Runbook نمونه: VPN شعبه A

``` text
SERVICE: Branch-A VPN to Hub (TO-HUB1/TO-HUB2)
Owner: net-team   On-call: +98-xxx   Escalation: L1 net-ops -> L2 senior -> vendor TAC
HEALTHY: IKE SA established; tunnel counters rising; BGP Established; latency <40 ms to ERP
VERIFY:
  get router info bgp summary
  diagnose vpn tunnel list
  execute ping 10.0.20.10
COMMON FAILURES:
  Symptom                     Check                         Fix
  Tunnel down                 diagnose vpn ike gateway list ISP/NAT-T/PSK -> see TS-VPN-01
  Up but no traffic           debug flow, policy            policy both ways -> TS-VPN-02
  Large transfers hang        ping DF 1372                  MSS clamp 1360 -> TS-VPN-03
ROLLBACK: restore tag s4 (git) ; expected 10 min
BACKUP/RESTORE: nightly sftp; restore procedure RB-02
CHANGE: CHG ticket required; window Tue 22:00
```

#### آزمون همکار

دریافت‌کننده یک عیب تزریق‌شده (مثلاً Policy حذف‌شده) را فقط با Runbook رفع می‌کند؛ زمان و نقطه‌های مبهم ثبت می‌شود؛ Runbook اصلاح می‌شود.

#### Handover (۹۰ دقیقه)

۱۰ دقیقه معماری، ۲۰ Runbook، ۳۰ Demo دو عیب، ۲۰ آزمون همکار، ۱۰ پرسش‌وپاسخ.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Runbook VPN بالا.

**متوسط (تحلیل):** همکار گام «Policy دوطرفه» را نفهمید؛ اصلاح با دستور دقیق و خروجی انتظار.

**سخت (سه سرویس):** Runbookهای VPN، HA، Log/Backup با لینک TS؛ آزمون همکار: ۳ عیب، زمان رفع ۸/۱۲/۱۵ دقیقه؛ بازخورد و نسخه‌ی ۲.

### ۸) Verification (اثبات صحت)

- Runbook آزمون‌شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ناقص | آزمون همکار | تکمیل |

### ۱۰) نکات امنیتی

- Secret در Runbook نیست.

### ۱۱) جمع‌بندی مفهومی

- Runbook = قابل‌انتقال و آزمون‌شده.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Healthy state چرا؟ *(پاسخ: 31-5-ت1)*

**ت2.** (ساده) Escalation؟ *(پاسخ: 31-5-ت2)*

**ت3.** (متوسط) آزمون همکار چیست؟ *(پاسخ: 31-5-ت3)*

**ت4.** (متوسط) چه چیزی Runbook را بد می‌کند؟ *(پاسخ: 31-5-ت4)*

**ت5.** (سخت) Runbook HA را بنویسید. *(پاسخ: 31-5-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Handover. *(پاسخ: 31-5-ت6)*

**Q1.** Quick quiz (English): How do you validate that a runbook is usable? *(پاسخ: 31-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Runbook | Operational runbook | دستور عملیاتی |

- *Hand over a tested runbook.* ← Runbook آزمون‌شده را تحویل دهید.

### ۱۴) کارت Lab

**کارت Lab:** Runbook. **Evidence:** `03-ops/capstone-runbook.md`.

### ۱۵) منابع

- Google SRE Book

<a id="l-31-6"></a>

## درس 31-6 — ارزیابی Capstone I و II: ارائه، Q&A، سؤال‌های دفاع و Rubric تفصیلی

**فصل 31 · بازنویسی عمیق · پیش‌نیاز: ۳۱-۱ تا ۳۱-۵ · ≈ 8 ساعت**

> **وضعیت:** پروژه‌ی Capstone (HQ + ۳ شعبه)؛ FortiOS 7.0.3 و Cisco (بوت‌نشده)؛ بدون شاهد واقعی «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. ارائه‌ی ۱۵ دقیقه‌ای ساختارمند انجام دهد.
2. سؤال‌های دفاع (طراحی، ریسک، شاهد، محدودیت) را پاسخ دهد.
3. Rubric تفصیلی را خودارزیابی کند.
4. برنامه‌ی بهبود از بازخورد بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

ارزیابی نهایی بخش اول؛ هدف سنجش فهم، شاهد و صداقت است.

### ۳) توضیح عمیق فنی

#### ساختار ارائه

نیاز/معیار (۲) → معماری (۳) → ADR (۲) → ساخت/Evidence (۳) → خرابی/RCA (۳) → محدودیت‌ها و «اجرا نشده» (۱) → درس‌آموخته (۱).

#### Rubric تفصیلی (۱۰۰)

| معیار | وزن | عالی | ضعیف |
|---|---|---|---|
| طراحی/ADR | 15 | تصمیم با معیار و ریسک | بدون دلیل |
| Routing/Segmentation | 15 | Failover/Zone اثبات‌شده | فقط پیکربندی |
| Policy/Security | 20 | Least privilege + منفی | any-any |
| VPN/SD-WAN/HA | 15 | زمان‌سنجی | ادعا |
| Troubleshooting | 15 | RCA با شاهد | حدس |
| مستندات | 10 | Runbook آزمون‌شده | ناقص |
| صداقت | 10 | «اجرا نشده» صریح | ادعای بی‌شاهد |

#### سؤال‌های دفاع

۱) چرا Breakout فقط برای SaaS؟ ۲) اگر Hub1 آسیب‌پذیر شود؟ ۳) کدام ادعا شاهد ندارد؟ ۴) هزینه‌ی HA در برابر ریسک؟ ۵) اگر ISP1 و ISP2 هم‌زمان قطع شوند؟

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** ارائه ۱۰ دقیقه.

**متوسط:** پاسخ به ۳ سؤال.

**سخت:** دفاع از ADR با ریسک.

### ۸) Verification (اثبات صحت)

- نمره.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| کسری | Rubric | برنامه‌ی بهبود |

### ۱۰) نکات امنیتی

- Secret.

### ۱۱) جمع‌بندی مفهومی

- ارائه، دفاع، صداقت.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) بخش‌های ارائه؟ *(پاسخ: 31-6-ت1)*

**ت2.** (ساده) چرا صداقت وزن دارد؟ *(پاسخ: 31-6-ت2)*

**ت3.** (متوسط) پاسخ به «اگر Hub1 آسیب‌پذیر شود؟» *(پاسخ: 31-6-ت3)*

**ت4.** (متوسط) پاسخ به «اگر هر دو ISP قطع شوند؟» *(پاسخ: 31-6-ت4)*

**ت5.** (سخت) کدام ادعاها شاهد ندارند؟ *(پاسخ: 31-6-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی بهبود از Rubric. *(پاسخ: 31-6-ت6)*

**Q1.** Quick quiz (English): What is the purpose of the defense questions? *(پاسخ: 31-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Rubric | Scoring rubric | ماتریس ارزیابی |

- *Be honest about what is not verified.* ← درباره‌ی آنچه تأیید نشده صادق باشید.

### ۱۴) کارت Lab

**کارت Lab:** ارزیابی. **Evidence:** `03-ops/capstone-eval.md`.

### ۱۵) منابع

- درس ۳۱-۰

## پاسخ‌های فصل 31

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 31-1

**31-1-ت1** — Failover شعبه A کمتر از ۱۰ ثانیه با آزمون ping پیوسته.

**31-1-ت2** — ثبت تصمیم معماری با زمینه، گزینه‌ها، تصمیم و پیامدها.

**31-1-ت3** — 8.76 ساعت.

**31-1-ت4** — تا موفقیت قابل‌اندازه‌گیری باشد و بحث بعدی کم شود.

**31-1-ت5** — سطح‌بندی دسترس‌پذیری، ADR، پذیرش ریسک مستند.

**31-1-ت6** — ساختار بالا با محتوای هر بخش.

**31-1-Q1** — So that success is measurable and can be verified objectively later.


### پاسخ‌های بازنویسی عمیق درس 31-2

**31-2-ت1** — طراحی تفصیلی قابل‌اجرا.

**31-2-ت2** — نیاز، طراحی، Config، آزمون، Evidence.

**31-2-ت3** — تا ساخت با آزمون هم‌راستا باشد.

**31-2-ت4** — کشف ابهام و خطا پیش از ساخت.

**31-2-ت5** — طبق نمونه با Log و Deny پایانی.

**31-2-ت6** — جداول Interface/Route/Policy/VPN/Test.

**31-2-Q1** — To show that every requirement is designed, built, tested and evidenced.


### پاسخ‌های بازنویسی عمیق درس 31-3

**31-3-ت1** — تا علت خرابی محلی بماند و لایه‌ی بالا روی لایه‌ی نادرست ساخته نشود.

**31-3-ت2** — نقطه‌ی بازگشت با Backup و Tag.

**31-3-ت3** — Guest به Internal باید Block باشد.

**31-3-ت4** — ≤ ۱۵ دقیقه؛ باید زمان‌سنجی شود.

**31-3-ت5** — شواهد مستقل: ping DF برای MTU؛ زمان Failover برای Timer؛ رفع و اندازه‌گیری جدا.

**31-3-ت6** — جدول بالا با مسئول و زمان.

**31-3-Q1** — So a failure can be attributed to the stage just built instead of an unknown layer.


### پاسخ‌های بازنویسی عمیق درس 31-4

**31-4-ت1** — ID، Req، Test، دستور، نتیجه، Pass/Fail، فایل، زمان.

**31-4-ت2** — تأییدنشده/اجرا نشده.

**31-4-ت3** — RCA (BGP Hold)، BFD، تکرار و ثبت.

**31-4-ت4** — تا مالکان نیاز پذیرش را تأیید کنند.

**31-4-ت5** — صریحاً «اجرا نشده (لایسنس)»، نه Pass؛ ریسک باقی‌مانده و برنامه.

**31-4-ت6** — طبق نمونه.

**31-4-Q1** — Not executed/unverified, never pass.


### پاسخ‌های بازنویسی عمیق درس 31-5

**31-5-ت1** — تعریف حالت عادی برای مقایسه.

**31-5-ت2** — مسیر ارجاع.

**31-5-ت3** — حل عیب تزریق‌شده فقط با Runbook.

**31-5-ت4** — گام مبهم، بدون خروجی انتظار، Secret.

**31-5-ت5** — Healthy/Verify/Failures/Rollback/Escalation.

**31-5-ت6** — ۹۰ دقیقه.

**31-5-Q1** — By having someone else resolve an injected fault using only the runbook.


### پاسخ‌های بازنویسی عمیق درس 31-6

**31-6-ت1** — نیاز، معماری، ADR، ساخت/Evidence، خرابی/RCA، محدودیت، درس‌آموخته.

**31-6-ت2** — ادعای بی‌شاهد خطرناک است.

**31-6-ت3** — Patch/Source Restriction/Hub دوم/Segmentation/Detection.

**31-6-ت4** — Failover به Backhaul/LTE (در صورت وجود)، هشدار، پذیرش ریسک.

**31-6-ت5** — Labهای اجرا نشده/HA/Unverified.

**31-6-ت6** — معیارهای ضعیف→اقدام→مسئول→تاریخ.

**31-6-Q1** — To verify understanding, risk awareness and honesty about what is proven.

### پاسخ‌های درس افزوده‌ی 31-0 (فصل 31)

**31-0-ت1** — ۸٫۷۶ ساعت در سال.

**31-0-ت2** — جدولی که هر نیاز را به عنصر طراحی، Config، آزمون و Evidence وصل می‌کند.

**31-0-ت3** — مثال: Finance→SRV-FIN:443 (Evidence: Log+Capture)؛ Guest ایزوله (nmap)؛ Failover<30s (ping+Log SLA)؛ Backup (Restore)؛ MFA (Login test).

**31-0-Q1** — A testable condition that must be met for a requirement to be considered satisfied.

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

## درس 32-0 — عملیات واقعی: Change Management، ITIL و شبیه‌سازی حادثه (Capstone III/IV)

**فصل ۳۲ · درس افزوده (پیش‌درس ۳۲-۱) · پیش‌نیاز: ۲۹-۰، ۳۰-۰، ۳۱-۰ · ≈ ۴ ساعت**

> **وضعیت:** قالب عملیات؛ حادثه فقط در Lab شبیه‌سازی؛ نتیجه بدون شاهد «اجرا نشده».

### ۱) هدف آموزشی

1. فرایند **Change** (Standard/Normal/Emergency) و ۱۰ مرحله‌ی تغییر را اجرا کند.
2. **Incident، Problem، Change، Release** را در چرخه‌ی ITIL تفکیک کند.
3. حادثه‌ی شبیه‌سازی‌شده را از Detection تا Post-Incident Review (PIR) بدون سرزنش اجرا کند.
4. معیارهای عملیاتی (MTTD، MTTR، Change Failure Rate) را اندازه بگیرد.
5. Runbook و Handover بنویسد.

### ۲) مفهوم پایه

بیشتر قطعی‌ها از **تغییر** می‌آیند، نه سخت‌افزار. عملیات حرفه‌ای = تغییر کنترل‌شده + پاسخ سریع + یادگیری. ITIL زبان مشترک است؛ هدف اجرای سبک و موثر است نه بروکراسی.

### ۳) توضیح عمیق فنی

#### ۳-۱) انواع Change

| نوع | مثال | تأیید |
|---|---|---|
| Standard | افزودن Address Object تأییدشده | از پیش تأیید |
| Normal | Policy جدید، تغییر Route | CAB/مدیر + Window |
| Emergency | رفع قطعی/حمله | سریع + ثبت بعدی |

#### ۳-۲) ده مرحله‌ی تغییر

``` text
1 Request   2 Risk/Impact   3 Plan (steps, tests, rollback)   4 Approve
5 Schedule  6 Pre-checks+Backup   7 Implement   8 Post-checks (positive/negative)
9 Close + evidence   10 Review (PIR if failed)
```

#### ۳-۳) Incident در برابر Problem

- **Incident:** اختلال فعلی؛ هدف بازگرداندن سرویس سریع.
- **Problem:** ریشه‌ی تکرارشونده؛ هدف حذف علت (RCA).
- Incident Priority = Impact × Urgency.

#### ۳-۴) معیارها

``` text
MTTD = mean time to detect
MTTR = mean time to restore
Change failure rate = failed changes / total changes
```

#### ۳-۵) PIR (بدون سرزنش)

Timeline، اثر، علت‌های مؤثر (فرایند/ابزار/انسان)، چه خوب بود، چه بد، اقدام (Owner، تاریخ). تمرکز بر سیستم، نه فرد.

#### ۳-۶) Runbook/Handover

برای هر سرویس: وضعیت سالم، Verificationها، خطاهای رایج، Rollback، تماس، Escalation.

### ۴) مثال حل‌شده

**Change:** افزودن Policy برای سرور جدید. Plan: Backup، Policy با Source دقیق، Log، Window، Rollback = حذف Policy؛ Pre-check: Route/DNS؛ Post-check: مثبت (443 OK) و منفی (22 Block)؛ Evidence: Log+Capture؛ Close.

**Incident (Lab):** تزریق عیب: Policy اشتباه Deny. Detection: Alert کاربران؛ Triage: Sev2؛ Debug Flow: Denied policy؛ رفع: Rollback؛ MTTR=۱۸ دقیقه؛ PIR: نبود Post-check منفی؛ اقدام: چک‌لیست Post-check.

**مثال سخت:** Emergency Change هنگام حمله: Block IP بدون CAB؛ ثبت بعدی ظرف ۲۴ ساعت؛ بازبینی؛ PIR.

### ۵) GUI و CLI

GUI/CLI برای Evidence؛ Ticketing؛ Config diff (`show full-configuration` و Diff).

### ۶) نکات امنیتی

- Emergency Change سوءاستفاده نشود؛ بازبینی اجباری.
- Secret در Ticket/Runbook ذخیره نشود.

### ۷) جمع‌بندی

- تغییر کنترل‌شده، ۱۰ مرحله، Rollback.
- Incident بازگرداندن؛ Problem ریشه‌کنی.
- معیارها و PIR بدون سرزنش.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) Incident و Problem چه فرقی دارند؟ *(پاسخ: 32-0-ت1)*

**ت2.** (متوسط) ۱۰ مرحله‌ی تغییر را بنویسید. *(پاسخ: 32-0-ت2)*

**ت3.** (سخت) PIR برای حادثه‌ی نمونه بنویسید. *(پاسخ: 32-0-ت3)*

**Q1.** Quick quiz (English): Why is a blameless post-incident review recommended? *(پاسخ: 32-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| CAB | Change Advisory Board | هیئت تأیید تغییر |
| MTTR | Mean Time To Restore | میانگین زمان بازیابی |
| PIR | Post-Incident Review | بازبینی پس از حادثه |
| ITIL | IT Infrastructure Library | چارچوب مدیریت خدمات IT |

- *A blameless review focuses on process, not individuals.* ← بازبینی بدون سرزنش روی فرایند تمرکز می‌کند نه افراد.

### ۱۰) منابع

- ITIL 4 Foundation؛ Google SRE Book (Postmortem Culture)؛ NIST SP 800-61.

## درس 32-1 — Capstone III: عملیات روزانه و Change Management (ITIL) — فرایند، قالب CHG و مثال کامل

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۲-۰، ۳۱-۵، ۲۷-۷ · ≈ 8 ساعت**

> **وضعیت:** عملیات و Capstone III/IV؛ حادثه فقط در Lab شبیه‌سازی؛ FortiOS 7.0.3 (بوت‌نشده)؛ بدون شاهد «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. انواع Change (Standard/Normal/Emergency) و فرایند ده‌مرحله‌ای را اجرا کند.
2. CHG کامل (ریسک، Plan، Pre/Post-check، Rollback) بنویسد.
3. CAB/Approval و Window را مدیریت کند.
4. معیارها (Change Failure Rate، Lead time) را اندازه بگیرد.
5. Emergency Change و بازبینی پس از آن را درست انجام دهد.

### ۲) مفهوم پایه: چیست و چرا؟

بیشتر قطعی‌های شبکه از تغییرات است. Change Management یعنی هر تغییر قابل‌پیش‌بینی، آزمون‌شده و برگشت‌پذیر باشد. هدف ITIL «سنگین‌کردن» نیست؛ «ایمن و سریع‌کردن» است.

### ۳) توضیح عمیق فنی

#### ۱) انواع Change

| نوع | مثال | تأیید |
|---|---|---|
| Standard | افزودن Address Object تأییدشده | از پیش تأیید |
| Normal | Policy جدید، Route | Review/CAB + Window |
| Emergency | Block IP در حمله | سریع؛ ثبت و بازبینی پس از آن |

#### ۲) ده مرحله

Request → Risk/Impact → Plan (مراحل، آزمون، Rollback) → Approve → Schedule → Pre-check+Backup → Implement → Post-check (مثبت/منفی) → Close → Review.

#### ۳) قالب CHG (نمونه‌ی پر)

``` text
CHG-0042  Add policy for new ERP server 10.0.20.11
Risk: low (single host, TCP 443)   Impact: ERP users
Plan: 1 backup  2 add address  3 add policy (log all)  4 test  5 close
Pre-check: policy list diff clean ; backup ok
Post-check positive: users->10.0.20.11:443 OK ; negative: guest->10.0.20.11 blocked
Rollback: delete policy 142 ; restore tag pre-CHG-0042
Window: Tue 22:00-22:30 ; Owner: net-team ; Approver: sec-lead
```

#### ۴) معیارها

``` text
Change failure rate = failed changes / total changes
Lead time = implement date - request date
```

#### ۵) Emergency

اقدام فوری برای مهار (Block)، ثبت CHG پس از آن ظرف ۲۴ ساعت، بازبینی و حذف Ruleهای موقت.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** CHG Standard افزودن Address.

**متوسط (تحلیل):** Normal Change با Post-check منفی شکست خورد (Guest دسترسی داشت)؛ Rollback؛ RCA: Source=all؛ اصلاح؛ CHG جدید.

**سخت (Emergency):** حمله‌ی Brute-force؛ Block IP فوری؛ ثبت بعدی؛ Rule موقت با انقضا؛ بازبینی؛ درس: Playbook.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute backup config sftp pre-CHG-0042.conf 192.168.90.10 backup-user <PASSWORD>
show firewall policy 142
```

### ۸) Verification (اثبات صحت)

- CHG امضا‌شده؛ Post-check.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Change خراب | Post-check | Rollback |

### ۱۰) نکات امنیتی

- Emergency بازبینی.

### ۱۱) جمع‌بندی مفهومی

- ده مرحله + قالب + معیار.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Standard Change؟ *(پاسخ: 32-1-ت1)*

**ت2.** (ساده) Post-check منفی چیست؟ *(پاسخ: 32-1-ت2)*

**ت3.** (متوسط) Change failure rate؟ *(پاسخ: 32-1-ت3)*

**ت4.** (متوسط) چرا Emergency بازبینی دارد؟ *(پاسخ: 32-1-ت4)*

**ت5.** (سخت) CHG را برای Policy جدید بنویسید. *(پاسخ: 32-1-ت5)*

**ت6.** (سخت، طراحی) Pre-check خودکار. *(پاسخ: 32-1-ت6)*

**Q1.** Quick quiz (English): What distinguishes an emergency change? *(پاسخ: 32-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| CAB | Change Advisory Board | هیئت تأیید |
| CHG | Change request | درخواست تغییر |

- *Plan every change with rollback.* ← هر Change را با Rollback برنامه‌ریزی کنید.

### ۱۴) کارت Lab

**کارت Lab:** Change. **Evidence:** `03-ops/chg-01.md`.

### ۱۵) منابع

- ITIL 4 Change Enablement

<a id="l-32-2"></a>

## درس 32-2 — Capstone III: شبیه‌سازی حادثه کامل — سناریو، نقش‌ها، Timeline نمونه، MTTD/MTTR و PIR

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۲۹-۰ تا ۲۹-۴، ۳۲-۱ · ≈ 8 ساعت**

> **وضعیت:** عملیات و Capstone III/IV؛ حادثه فقط در Lab؛ FortiOS 7.0.3 (بوت‌نشده)؛ بدون شاهد «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. حادثه‌ی دومرحله‌ای را در Lab اجرا و با نقش‌های IC/Operator/Comms/Scribe مدیریت کند.
2. Timeline، MTTD/MTTR و کیفیت Detection را اندازه بگیرد.
3. RCA و PIR بدون سرزنش با اقدام‌های قابل‌پیگیری بنویسد.
4. Playbookها را به‌روز کند.

### ۲) مفهوم پایه: چیست و چرا؟

حادثه را باید «تمرین» کرد تا زیر فشار واقعی اشتباه نشود. این درس یک سناریوی کامل با Timeline نمونه می‌دهد.

### ۳) توضیح عمیق فنی

#### سناریو (Lab)

Inject 1 (T0): Change اشتباه، Policy Deny ERP.
Inject 2 (T0+10): Scan خارجی و ۲۰ Login ناموفق VPN.

#### نقش‌ها

IC (تصمیم/اولویت)، Operator (دستورها)، Comms (ارتباطات)، Scribe (Timeline).

#### Timeline نمونه

``` text
19:00 T0   Change CHG-0050 applied (policy 150 deny)
19:04      users report ERP down (detect via ticket)        MTTD = 4 min
19:06      IC assigns Sev1; Operator runs debug flow -> "Denied policy 150"
19:09      Rollback of CHG-0050 (tag pre-CHG-0050)
19:11      ERP verified (positive+negative tests)             MTTR = 7 min from detect
19:10      Alert: 20 failed VPN logins from 198.51.100.7 -> block IP (Sev3) after ERP restored
19:30      Close; PIR scheduled in 48 h
```

``` text
MTTD = detect - fault start = 4 min ; MTTR = restore - detect = 7 min
```

#### PIR (نمونه)

علت‌ها: نبود Post-check منفی/مثبت در CHG؛ Alert ERP وجود نداشت (کشف از Ticket). اقدام: Alert Synthetic Test ERP (Owner، تاریخ)، چک‌لیست Post-check، آموزش.

#### اولویت‌بندی

دو رویداد: اثر کسب‌وکار (ERP) Sev1 اول؛ Scan Sev3 بعد.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Rollback و بازگشت ERP؛ MTTD 4، MTTR 7.

**متوسط (تحلیل):** دو رویداد هم‌زمان: تصمیم IC بر پایه‌ی اثر؛ ثبت دلیل.

**سخت (بهبود):** MTTD بالاست چون کشف با Ticket؛ اقدام: Synthetic monitoring ERP هر ۱ دقیقه؛ هدف MTTD ≤ 1 min.

### ۸) Verification (اثبات صحت)

- PIR تکمیل.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| MTTD بالا | Timeline | Alert/Synthetic |

### ۱۰) نکات امنیتی

- Lab فقط.

### ۱۱) جمع‌بندی مفهومی

- تمرین IR + Metrics + PIR.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) MTTD و MTTR در Timeline مثال؟ *(پاسخ: 32-2-ت1)*

**ت2.** (ساده) نقش Scribe؟ *(پاسخ: 32-2-ت2)*

**ت3.** (متوسط) چرا ERP قبل از Scan؟ *(پاسخ: 32-2-ت3)*

**ت4.** (متوسط) چه اقدامی MTTD را کم می‌کند؟ *(پاسخ: 32-2-ت4)*

**ت5.** (سخت) PIR مثال را بنویسید. *(پاسخ: 32-2-ت5)*

**ت6.** (سخت، طراحی) سناریوی دوم (Tunnel+Policy). *(پاسخ: 32-2-ت6)*

**Q1.** Quick quiz (English): Why are roles such as incident commander assigned during an incident? *(پاسخ: 32-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| IC | Incident Commander | فرمانده‌ی حادثه |
| Synthetic monitoring | Synthetic monitoring | پایش با آزمون مصنوعی |

- *Learn from every incident.* ← از هر حادثه بیاموزید.

### ۱۴) کارت Lab

**کارت Lab:** Incident. **Evidence:** `03-ops/incident-lab.md`.

### ۱۵) منابع

- NIST SP 800-61
- Google SRE Book (Incident management)

<a id="l-32-3"></a>

## درس 32-3 — Capstone IV: مهاجرت/ارتقای کامل در Lab — Plan زمان‌بندی‌شده، Post-check، Rollback و گزارش

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۰-۰ تا ۳۰-۴، ۳۲-۱ · ≈ 8 ساعت**

> **وضعیت:** عملیات و Capstone III/IV؛ حادثه فقط در Lab؛ FortiOS 7.0.3 (بوت‌نشده)؛ بدون شاهد «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Plan Cutover را دقیقه‌به‌دقیقه اجرا کند.
2. Post-check Matrix را اجرا و اختلاف‌ها را RCA کند.
3. Rollback آزمایشی را زمان‌سنجی کند.
4. گزارش نهایی مهاجرت و Hypercare بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

آخرین Capstone: یک مهاجرت/ارتقا را مثل تولید اجرا کنید: Plan، Go/No-Go، Cutover، Post-check، Rollback، گزارش.

### ۳) توضیح عمیق فنی

#### Plan زمان‌بندی‌شده (نمونه)

``` text
T-60  Go/No-Go (backup ok, OOB ok, team, test matrix)
T-30  final backups both devices, tag pre-cutover
T+00  announce start
T+05  switch gateway/route to new FGT
T+10  smoke tests (3 critical services)
T+20  full test matrix (15 tests)
T+35  decision: continue / rollback (criteria: any critical test fails after fix attempt 10 min)
T+45  monitoring + comms
T+60  close window / hypercare start
```

#### Post-check

Matrix ۱۵ آزمون + Session/Log/CPU؛ مقایسه با Baseline.

#### Rollback آزمایشی

``` text
restore tag pre-cutover on old path -> run smoke tests -> record time (<= 15 min)
```

#### گزارش

خلاصه، Timeline، نتایج Matrix، اختلاف‌ها و RCA، Rollback time، Hypercare plan (۷ روز)، درس‌آموخته.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Cutover موفق؛ همه‌ی Smoke Pass.

**متوسط (تحلیل):** T+20: ۲ آزمون Fail (NAT Partner)؛ ۱۰ دقیقه رفع؛ Pass.

**سخت (تصمیم):** پس از ۱۰ دقیقه یک آزمون حیاتی هنوز Fail ⇒ طبق Trigger Rollback؛ زمان ۱۲ دقیقه؛ RCA بعد از Window.

### ۸) Verification (اثبات صحت)

- گزارش و Evidence.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| شکست | Post-check | Rollback |

### ۱۰) نکات امنیتی

- Change.

### ۱۱) جمع‌بندی مفهومی

- Plan زمان‌بندی‌شده + Post-check + Rollback.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Go/No-Go چه زمانی؟ *(پاسخ: 32-3-ت1)*

**ت2.** (ساده) Trigger Rollback مثال؟ *(پاسخ: 32-3-ت2)*

**ت3.** (متوسط) چرا Rollback آزمایشی؟ *(پاسخ: 32-3-ت3)*

**ت4.** (متوسط) Hypercare چیست؟ *(پاسخ: 32-3-ت4)*

**ت5.** (سخت) Plan زمان‌بندی را بنویسید. *(پاسخ: 32-3-ت5)*

**ت6.** (سخت، طراحی) گزارش نهایی. *(پاسخ: 32-3-ت6)*

**Q1.** Quick quiz (English): Why define the rollback trigger before the cutover begins? *(پاسخ: 32-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Hypercare | Hypercare | پایش ویژه |

- *Test the rollback path.* ← مسیر Rollback را آزمایش کنید.

### ۱۴) کارت Lab

**کارت Lab:** Cutover. **Evidence:** `03-ops/cutover-lab.md`.

### ۱۵) منابع

- درس ۳۰-۲

<a id="l-32-4"></a>

## درس 32-4 — ارزیابی نهایی و Portfolio: ماتریس مهارت، تحلیل شکاف، نگاشت نقش و نمونه‌ی Portfolio

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: همه‌ی Gateها · ≈ 8 ساعت**

> **وضعیت:** عملیات و Capstone III/IV؛ حادثه فقط در Lab؛ FortiOS 7.0.3 (بوت‌نشده)؛ بدون شاهد «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Portfolio قابل‌ارائه با شواهد بسازد.
2. ماتریس مهارت و Gap Analysis را صادقانه بنویسد.
3. مهارت‌ها را به نقش‌های شغلی نگاشت کند.

### ۲) مفهوم پایه: چیست و چرا؟

Portfolio، نمونه‌کار با شاهد است؛ Gap Analysis نشان می‌دهد کدام ادعاها هنوز شاهد ندارند.

### ۳) توضیح عمیق فنی

#### ساختار Portfolio

``` text
01-overview.md        architecture summary (1 page)
02-design/            HLD, LLD, IP plan, ADRs
03-ops/               runbooks, change records, RCAs, PIR
04-evidence/          evidence index + raw files (sanitized)
05-gates/             G1..G11 status (verified/partial/not executed)
06-limitations.md     Unverified / not executed / license-dependent
```

#### ماتریس مهارت

| حوزه | سطح ادعایی | شاهد | Gap |
|---|---|---|---|
| Switching/STP | L3 | G1–G2 | — |
| Routing | L3 | G3/A4 | BGP Lab |
| Firewall/NAT | L3 | G5/G6 | FortiGate اجرا نشده |
| UTM | L2 | طراحی | Needs-License |
| VPN/SD-WAN | L3 | G7/G8 | Lab اجرا نشده |
| HA | L2 | طراحی | لایسنس |
| Ops/IR | L3 | G10/IR Lab | — |

#### نگاشت نقش

Network Engineer: Routing/Switching/VPN؛ Security Engineer: Firewall/UTM/IR؛ SOC L1/L2: Detection/Response؛ Architect: HLD/ADR/Risk.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Portfolio با ۶ پوشه.

**متوسط (تحلیل):** Gap: FortiGate اجرا نشده؛ سطح ادعا از L3 به L2؛ برنامه‌ی Lab.

**سخت (قضاوت):** کارفرما می‌پرسد «HA کار می‌کند؟»؛ پاسخ صادقانه: طراحی/مفهومی با منبع؛ اجرا نشده؛ برنامه‌ی آزمون.

### ۸) Verification (اثبات صحت)

- Portfolio کامل.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| شاهد کم | Index | Lab بیشتر |

### ۱۰) نکات امنیتی

- Secret پاک.

### ۱۱) جمع‌بندی مفهومی

- Portfolio + Gap + نقش.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Portfolio شامل چیست؟ *(پاسخ: 32-4-ت1)*

**ت2.** (ساده) Gap چیست؟ *(پاسخ: 32-4-ت2)*

**ت3.** (متوسط) چرا فایل محدودیت‌ها؟ *(پاسخ: 32-4-ت3)*

**ت4.** (متوسط) FortiGate اجرا نشده؛ سطح ادعا؟ *(پاسخ: 32-4-ت4)*

**ت5.** (سخت) پاسخ به «HA کار می‌کند؟» *(پاسخ: 32-4-ت5)*

**ت6.** (سخت، طراحی) ماتریس مهارت. *(پاسخ: 32-4-ت6)*

**Q1.** Quick quiz (English): Why include a limitations file in a portfolio? *(پاسخ: 32-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Gap analysis | Gap analysis | تحلیل شکاف |

- *Be transparent about limitations.* ← درباره‌ی محدودیت‌ها شفاف باشید.

### ۱۴) کارت Lab

**کارت Lab:** Portfolio. **Evidence:** `03-ops/portfolio.md`.

### ۱۵) منابع

- درس ۳۲-۰

<a id="l-32-5"></a>

## درس 32-5 — Roadmap یادگیری بعدی: مسیر گواهی، Labهای اجرا نشده، Automation و برنامه‌ی ۶ ماهه

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: ۳۲-۴ · ≈ 8 ساعت**

> **وضعیت:** عملیات و Capstone III/IV؛ حادثه فقط در Lab؛ FortiOS 7.0.3 (بوت‌نشده)؛ بدون شاهد «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Roadmap ۶ ماهه با اولویت از Gap بنویسد.
2. مسیر گواهی/تخصص را انتخاب کند.
3. Labهای اجرا نشده را زمان‌بندی کند.

### ۲) مفهوم پایه: چیست و چرا؟

برنامه‌ی ادامه باید از Gap شروع شود: اول آنچه شاهد ندارد.

### ۳) توضیح عمیق فنی

#### برنامه‌ی ۶ ماهه (قالب)

| ماه | هدف | خروجی/شاهد |
|---|---|---|
| ۱ | اجرای Labهای اجرا نشده (FortiGate Boot با تأیید، Packet Flow Debug) | Evidence G5/G6 |
| ۲ | VPN/SD-WAN واقعی | G7/G8 |
| ۳ | Automation (Ansible/Python) روی Lab | CP1+ |
| ۴ | گواهی هدف (مثلاً Fortinet NSE 4 یا Cisco CCNA) | آزمون |
| ۵ | Blue Team/Detection پروژه | Playbook+PIR |
| ۶ | پروژه‌ی واقعی/مشارکت + بازنگری Portfolio | Portfolio نسخه 2 |

#### مسیرها

Fortinet NSE 4/5/6، Cisco CCNA→CCNP ENCOR (در صورت نیاز)، Linux/Windows Admin، Python/Ansible، SIEM/SOC.

#### معیار پیشرفت

هر ماه: شاهد جدید در Portfolio و کاهش Gap.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Roadmap جدول.

**متوسط (تحلیل):** وقت محدود؛ اولویت با Gap بیشترین ریسک (VPN/HA).

**سخت (بودجه):** بدون گواهی پولی: Labهای رایگان + Evidence؛ جایگزین: پروژه‌ی متن‌باز.

### ۸) Verification (اثبات صحت)

- Roadmap.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| مبهم | بازبینی | اولویت |

### ۱۰) نکات امنیتی

- —

### ۱۱) جمع‌بندی مفهومی

- Roadmap از Gap.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Roadmap از کجا شروع می‌شود؟ *(پاسخ: 32-5-ت1)*

**ت2.** (ساده) معیار پیشرفت؟ *(پاسخ: 32-5-ت2)*

**ت3.** (متوسط) اولویت‌بندی با وقت محدود؟ *(پاسخ: 32-5-ت3)*

**ت4.** (متوسط) چرا Labهای اجرا نشده اول؟ *(پاسخ: 32-5-ت4)*

**ت5.** (سخت) برنامه‌ی ۶ ماهه. *(پاسخ: 32-5-ت5)*

**ت6.** (سخت، طراحی) بدون بودجه‌ی گواهی چه؟ *(پاسخ: 32-5-ت6)*

**Q1.** Quick quiz (English): How should the roadmap prioritize topics? *(پاسخ: 32-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NSE | Network Security Expert | برنامه‌ی گواهی Fortinet |

- *Plan your next learning steps.* ← گام‌های بعدی را برنامه‌ریزی کنید.

### ۱۴) کارت Lab

**کارت Lab:** Roadmap. **Evidence:** `03-ops/roadmap.md`.

### ۱۵) منابع

- Fortinet Training Institute
- Cisco Learning Network

<a id="l-32-6"></a>

## درس 32-6 — آزمون نهایی دوره: سناریوی جامع، صورت مسئله، کلید پاسخ و Rubric

**فصل 32 · بازنویسی عمیق · پیش‌نیاز: همه · ≈ 8 ساعت**

> **وضعیت:** عملیات و Capstone III/IV؛ حادثه فقط در Lab؛ FortiOS 7.0.3 (بوت‌نشده)؛ بدون شاهد «اجرا نشده»؛ مثال‌ها آموزشی‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سناریوی جامع را از طراحی تا عیب‌یابی حل کند.
2. سه عیب چندلایه را با روش فرضیه‌محور رفع کند.
3. Evidence و RCA ارائه دهد.
4. صادقانه محدودیت‌ها را اعلام کند.

### ۲) مفهوم پایه: چیست و چرا؟

آزمون نهایی همه‌ی مهارت‌ها.

### ۳) توضیح عمیق فنی

#### صورت مسئله

سازمان: HQ + ۳ شعبه، دو ISP، IPsec، SD-WAN، HA، UTM، Auth (LDAP/MFA)، Log/Monitoring، Backup.

بخش ۱ طراحی (HLD/IP Plan/ADR). بخش ۲ پیاده‌سازی (Evidence). بخش ۳ سه عیب تزریق‌شده: (۱) MTU/Policy VPN؛ (۲) Asymmetric یا Prefix-list BGP؛ (۳) Auth/Policy گروهی. بخش ۴ IR کوتاه. بخش ۵ گزارش و محدودیت‌ها.

#### کلید (خلاصه)

- عیب ۱: ping DF/Debug Flow؛ MSS/Policy.
- عیب ۲: Sniffer دو‌نقطه‌ای/advertised-routes.
- عیب ۳: `authserver`، fsso list، Debug Flow.
- IR: Detect، Contain، Evidence، PIR.

#### Rubric (۱۰۰)

طراحی ۲۰؛ پیاده‌سازی ۲۵؛ عیب‌یابی ۳۰؛ مستندات ۱۵؛ صداقت ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** طراحی.

**متوسط:** پیاده‌سازی.

**سخت:** سه عیب و IR.

### ۸) Verification (اثبات صحت)

- Evidence.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ناقص | Rubric | کسری |

### ۱۰) نکات امنیتی

- Secret.

### ۱۱) جمع‌بندی مفهومی

- آزمون جامع.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) بخش‌های آزمون؟ *(پاسخ: 32-6-ت1)*

**ت2.** (ساده) Rubric وزن عیب‌یابی؟ *(پاسخ: 32-6-ت2)*

**ت3.** (متوسط) عیب ۱ را چگونه جداسازی می‌کنید؟ *(پاسخ: 32-6-ت3)*

**ت4.** (متوسط) عیب ۳ را چگونه؟ *(پاسخ: 32-6-ت4)*

**ت5.** (سخت) سه عیب را با RCA کوتاه بنویسید. *(پاسخ: 32-6-ت5)*

**ت6.** (سخت، طراحی) گزارش نهایی با محدودیت‌ها. *(پاسخ: 32-6-ت6)*

**Q1.** Quick quiz (English): What will the final exam evaluate? *(پاسخ: 32-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Final | Final exam | آزمون نهایی |

- *Review all gates before the final exam.* ← قبل از آزمون نهایی همه‌ی Gateها را مرور کنید.

### ۱۴) کارت Lab

**کارت Lab:** آزمون نهایی. **Evidence:** `03-ops/final.md`.

### ۱۵) منابع

- همه‌ی فصل‌ها

## پاسخ‌های فصل 32

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 32-1

**32-1-ت1** — تغییر کم‌ریسک از پیش تأییدشده.

**32-1-ت2** — آزمون مسدود بودن ترافیک غیرمجاز.

**32-1-ت3** — نسبت Changeهای ناموفق به کل.

**32-1-ت4** — برای جلوگیری از سوءاستفاده و حذف Ruleهای موقت.

**32-1-ت5** — قالب بالا.

**32-1-ت6** — Diff Policy، Backup، Health.

**32-1-Q1** — It is applied urgently and documented/reviewed afterwards.


### پاسخ‌های بازنویسی عمیق درس 32-2

**32-2-ت1** — MTTD=4 دقیقه، MTTR=7 دقیقه.

**32-2-ت2** — ثبت Timeline و تصمیم‌ها.

**32-2-ت3** — اثر کسب‌وکار بالاتر (Sev1).

**32-2-ت4** — Synthetic monitoring/Alert خودکار.

**32-2-ت5** — خلاصه، Timeline، علت‌ها، خوب/بد، اقدام Owner/Date، Metrics.

**32-2-ت6** — Inject، Detect، Contain، Fix، PIR.

**32-2-Q1** — To avoid confusion and ensure decisions, actions, communication and records are handled in parallel.


### پاسخ‌های بازنویسی عمیق درس 32-3

**32-3-ت1** — قبل از شروع (T-60).

**32-3-ت2** — آزمون حیاتی پس از ۱۰ دقیقه رفع همچنان Fail.

**32-3-ت3** — اثبات مسیر بازگشت.

**32-3-ت4** — پایش تشدیدشده پس از تغییر.

**32-3-ت5** — طبق بالا.

**32-3-ت6** — بخش‌های بالا.

**32-3-Q1** — So the decision is objective and not influenced by pressure during the change.


### پاسخ‌های بازنویسی عمیق درس 32-4

**32-4-ت1** — طراحی، عملیات، Evidence، Gateها، محدودیت‌ها.

**32-4-ت2** — فاصله‌ی ادعا با شاهد.

**32-4-ت3** — صداقت و جلوگیری از ادعای بی‌شاهد.

**32-4-ت4** — کاهش به L2 تا آزمون اجرا شود.

**32-4-ت5** — صادقانه: اجرا نشده؛ طراحی با مرجع؛ برنامه‌ی آزمون.

**32-4-ت6** — جدول.

**32-4-Q1** — To be transparent about what is unverified and avoid unsupported claims.


### پاسخ‌های بازنویسی عمیق درس 32-5

**32-5-ت1** — از Gap.

**32-5-ت2** — شاهد جدید.

**32-5-ت3** — بیشترین ریسک/Gap.

**32-5-ت4** — تا ادعاها شاهد داشته باشند.

**32-5-ت5** — جدول.

**32-5-ت6** — Lab/پروژه/Evidence.

**32-5-Q1** — By the largest gaps between claimed skills and available evidence.


### پاسخ‌های بازنویسی عمیق درس 32-6

**32-6-ت1** — طراحی، پیاده‌سازی، سه عیب، IR، گزارش.

**32-6-ت2** — ۳۰.

**32-6-ت3** — ping DF برای MTU و Debug Flow برای Policy.

**32-6-ت4** — `authserver`، `fsso list`، Debug Flow.

**32-6-ت5** — علامت/شاهد/علت/رفع.

**32-6-ت6** — بخش‌های Portfolio.

**32-6-Q1** — Design, implementation, troubleshooting, documentation and honesty.

### پاسخ‌های درس افزوده‌ی 32-0 (فصل 32)

**32-0-ت1** — Incident بازگرداندن سرویس؛ Problem حذف علت ریشه‌ای تکرارشونده.

**32-0-ت2** — Request، Risk، Plan، Approve، Schedule، Pre-check+Backup، Implement، Post-check، Close، Review.

**32-0-ت3** — Timeline، اثر، علت (نبود Post-check منفی)، چه خوب/بد، اقدام با Owner و تاریخ.

**32-0-Q1** — Because it exposes process weaknesses without people hiding information.

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
