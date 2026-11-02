# ۱. Cover و Document Control

# Enterprise Network & Security Engineering — Course Master Blueprint v2.0

**دوره جامع تربیت ادمین حرفه‌ای زیرساخت شبکه و امنیت سازمانی**
Cisco Routing & Switching (سطح مهارتی CCNA) + FortiGate (FortiOS 7.0.3) + Windows/Linux + Monitoring + Blue Team

| مورد | مقدار |
|---|---|
| نام فایل | `Enterprise_Network_Security_Course_Master_Blueprint_v2.0.md` |
| نسخه | **2.0** (تکامل سند v1.0 پس از ممیزی) |
| وضعیت | پیش‌نویس برای بررسی و تأیید کاربر — **فقط طراحی** |
| تاریخ تهیه | 2026-11-02 |
| مدت دوره | ۲۴ هفته × ۶ روز × ۶ ساعت مفید = ۸۶۴ ساعت مفید (جزئیات: فصل ۲۷) |
| محیط Lab | PNetLab روی VMware ESXi (وب PNetLab: `192.168.88.199`؛ مدیریت ESXi: `192.168.88.3`) |
| نسخه هدف Firewall | FortiOS 7.0.3 (تغییر بدون اجازه کاربر ممنوع) |
| مرحله بعد | بررسی و تأیید صریح کاربر → سپس Phase 0 (Discovery، Read-Only) |

### Document Control

| نسخه | تاریخ | شرح | وضعیت |
|---|---|---|---|
| 1.0 | 2026-11-02 | طراحی اولیه (۲۷ فصل) | ممیزی‌شده |
| 2.0 | 2026-11-02 | اعمال اصلاحات ممیزی (زمان‌بندی، معماری Capstone، FortiOS/License، Cisco Spiral، ۵۰ Runbook، Image Matrix، Tierهای منابع، منابع رسمی) | **در انتظار تأیید کاربر** |

### برچسب‌های وضعیت اطلاعات (در سراسر سند)

| برچسب | تعریف |
|---|---|
| `Verified` | با مستند رسمی نسخه مربوط یا آزمایش معتبر تأیید شده؛ منبع و تاریخ در فصل ۳۴ ثبت است |
| `Inferred` | استنباط مهندسی؛ هنوز تأیید نشده |
| `Unverified` | نیازمند بررسی مستندات، Image واقعی یا آزمایش در محیط کاربر |
| 🔎 | وابسته به اطلاعات Discovery (محیط کاربر) |
| **[OPT]** | Optional/Advanced؛ جزو ۸۶۴ ساعت ضروری نیست |

> **قانون حاکم:** هر قابلیت، سازگاری Image یا وضعیت لایسنس که در فصل ۳۴ با «`Verified`» ثبت نشده باشد، قطعی تلقی نمی‌شود.

### فهرست فصل‌ها

| # | فصل | # | فصل |
|---|---|---|---|
| 1 | Cover و Document Control | 20 | VPN، Branch Connectivity و SD-WAN |
| 2 | Executive Overview | 21 | Security، Segmentation و DMZ |
| 3 | Course Vision و Target Competencies | 22 | Monitoring، Logging و Alerting |
| 4 | Scope، Out of Scope و Assumptions | 23 | Wireshark، tcpdump و Packet Analysis |
| 5 | Learner Profile و Prerequisites | 24 | Troubleshooting Methodology |
| 6 | Learning Outcomes و Competency Matrix | 25 | 50 Troubleshooting Runbooks |
| 7 | Teaching Methodology | 26 | 24-Week Detailed Schedule |
| 8 | Overall Architecture و Reference Topology | 27 | Daily/Weekly Time Accounting |
| 9 | Lab Safety، Isolation و Risk Management | 28 | Continuous Cisco Spiral Practice |
| 10 | PNetLab/ESXi Lab Foundation | 29 | Capstone Project |
| 11 | Discovery و Environment Validation | 30 | Assessment و Competency Gates |
| 12 | Image Compatibility Matrix | 31 | Deliverables و Documentation Standards |
| 13 | Lab Resource Tiers | 32 | Backup، Restore، Change و Rollback |
| 14 | IP Addressing، VLAN و Naming Standards | 33 | Operations، Incident Response و Handover |
| 15 | Cisco Routing & Switching Curriculum | 34 | Official Resources و Version References |
| 16 | FortiGate 7.0.3 Curriculum | 35 | Risks، Dependencies و Open Questions |
| 17 | Cisco + FortiGate Integration | 36 | Changelog |
| 18 | Windows Server، AD، DNS، DHCP و RADIUS | 37 | Audit Traceability Matrix |
| 19 | Linux و سرویس‌های زیرساختی | 38 | Appendices (A: Runbooks، B: Labs، C: Go/No-Go، D: Self-Audit) |

---

# ۲. Executive Overview

## ۲.۱ دوره چیست؟

یک مسیر **۲۴ هفته‌ای، پروژه‌محور و مبتنی بر اثبات مهارت** که فردی با درک مفهومی شبکه را به ادمین زیرساخت شبکه و امنیت سازمانی تبدیل می‌کند. دوره یک «دوره آمادگی آزمون» نیست؛ یک **سازمان فرضی** (دفتر مرکزی + ۳ شعبه) در طول دوره به‌تدریج ساخته، ایمن، مانیتور، خراب و عیب‌یابی و مستند می‌شود.

## ۲.۲ ستون‌های دوره

| ستون | توضیح |
|---|---|
| **Cisco R&S** | CLI از صفر، Switching، Routing، IP Services، امنیت مدیریتی، مقدمه Automation |
| **FortiGate 7.0.3** | Administration، Policy/NAT، Security Profiles، Auth، VPN، SD-WAN، HA، Dynamic Routing، مدیریت متمرکز |
| **یکپارچه‌سازی** | ۱۵ سناریوی الزامی که در آن‌ها Cisco و FortiGate در یک معماری واحد کار می‌کنند |
| **Windows/Linux** | فقط در حدی که برای شبکه/امنیت لازم است: AD، DNS/DHCP، NPS، PKI، DMZ Web، rsyslog |
| **Packet Analysis** | در هر هفته حضور دارد (نه فقط یک فصل) |
| **Troubleshooting** | چارچوب ۱۵ مرحله‌ای ثابت + ۵۰ سناریوی خرابی + Fault Injection در Capstone |
| **Monitoring/Logging** | Zabbix + rsyslog (Stack اصلی)، LibreNMS (جایگزین)، FortiAnalyzer (مشروط به لایسنس) |
| **Blue Team** | Segmentation، Hardening، Detection در Lab ایزوله |
| **مستندسازی** | HLD/LLD، As-Built، Runbook، Change/Rollback، Git |

## ۲.۳ زمان: جمع‌بندی صادقانه و بدون تناقض

| پرسش | پاسخ |
|---|---|
| زمان مفید دوره | **ثابت: ۲۴ هفته × ۶ روز × ۳۶۰ دقیقه = ۸۶۴ ساعت مفید**؛ استراحت‌ها و روز هفتم **خارج** از این عدد (فصل ۲۷) |
| آیا محتوا بیش از ظرفیت است؟ | بخش «ضروری» در ۸۶۴ ساعت جا می‌شود **اگر** Phase 0 به‌موقع تمام شود و منابع/Image در دسترس باشند (🔎). مباحث تکمیلی در فصل ۲۶.۲ با برچسب **[OPT]** جدا شده‌اند و جای زمان ضروری را نمی‌گیرند |
| اگر عقب افتادیم؟ | به‌ترتیب: حذف [OPT] ← فشرده‌سازی Labهای Independent کم‌ارزش ← مصرف Buffer هفته ۲۳؛ **مدت دوره و ۸۶۴ ساعت تغییر نمی‌کند** |
| نقد برنامه ۶ ساعت/روز | ۶ ساعت متمرکز پیوسته مناسب نیست؛ الگوی روزانه به بلوک‌های ≤۹۰ دقیقه با استراحت **خارج از ۳۶۰ دقیقه** تقسیم شده و روز ششم هر هفته «سبک» است (قالب R) |

## ۲.۴ یافته‌های مهم طراحی

| # | یافته | وضعیت |
|---|---|---|
| 1 | **FortiOS 7.0.3 قدیمی است** و چند آسیب‌پذیری امنیتی بحرانی نسخه‌های 7.0.x را شامل شده است: CVE-2022-40684 (7.0.0 تا 7.0.6، رفع در 7.0.7+)، CVE-2022-42475 (7.0.0 تا 7.0.8، رفع در 7.0.9+)، CVE-2023-27997 (7.0.0 تا 7.0.11، رفع در 7.0.12+). 7.0.3 در همه این بازه‌ها قرار دارد. **پس Lab کاملاً ایزوله است؛ هیچ Port Forwarding/Exposure به اینترنت مجاز نیست.** این نسخه برای Production توصیه نمی‌شود. | `Verified` (PSIRT، 2026-11-02؛ فصل ۳۴) |
| 2 | **محدودیت‌های Evaluation License FortiGate-VM** (سقف vCPU/RAM، دسترسی FortiGuard، HA، تعداد Interface) | `Unverified` — صفحه رسمی در بررسی خودکار محتوای متنی نداد؛ باید در Discovery/Feature-Matrix (فصل ۱۶.۸) تأیید شود |
| 3 | **دسترسی به Image دقیق 7.0.3** نیازمند حساب Support Fortinet است | `Unverified` 🔎 |
| 4 | **Image Cisco** باید قانونی و متعلق به کاربر باشد؛ هیچ منبع غیرقانونی پیشنهاد نمی‌شود. قابلیت‌های IOSv/IOSvL2 باید در Image Validation اندازه‌گیری شود | `Unverified` 🔎 |
| 5 | **Windows Server 2022 Evaluation**: ۱۸۰ روز | `Verified` (Microsoft Evaluation Center) |
| 6 | معماری Capstone **یکی** است: **FortiGate = Gateway همه VLANهای سازمانی** (فصل ۲۹)؛ مدل Cisco L3 Core Gateway به‌صورت Lab A مستقل (فصل ۱۷) | ✅ تصمیم طراحی (در انتظار تأیید) |
| 7 | **Cisco در هر ۲۴ هفته** تمرین می‌شود (Spiral، فصل ۲۸) | ✅ |
| 8 | ۵۰ سناریوی عیب‌یابی به Runbook اجرایی تبدیل شد؛ ۱۰ مورد تفصیلی | ✅ (فصل ۲۵) |

> **هیچ نصب یا تغییری در محیط واقعی انجام نشده است.**

---

# ۳. Course Vision و Target Competencies

## ۳.۱ شایستگی‌های نهایی (Exit Competencies)

| # | شایستگی | سطح هدف (فصل ۳۰) |
|---|---|---|
| C1 | تحلیل نیازمندی و طراحی HLD/LLD شبکه سازمانی | L4 |
| C2 | IP Plan، Subnetting/VLSM، VLAN Matrix | L4 |
| C3 | پیکربندی Cisco Switch/Router با CLI | L3–L4 |
| C4 | VLAN/Trunk/STP/EtherChannel/Routing (OSPF) | L3–L4 |
| C5 | تحلیل Packet Flow در هر لایه | L4 |
| C6 | جایگذاری درست FortiGate در معماری | L4 |
| C7 | Firewall Policy، NAT/VIP، Security Profiles | L3–L4 |
| C8 | IPsec Site-to-Site و Remote Access VPN | L3 |
| C9 | Auth با AD/LDAP/RADIUS | L3 |
| C10 | Windows/Linux در حد زیرساخت شبکه | L2–L3 |
| C11 | Wireshark/tcpdump/Sniffer/Debug Flow | L3–L4 |
| C12 | Monitoring/Logging راه‌اندازی و تفسیر | L3 |
| C13 | Backup/Restore/Change/Rollback | L3 |
| C14 | RCA و عیب‌یابی سیستماتیک | L4 |
| C15 | Hardening و Blue Team Lab | L3 |
| C16 | مستندسازی فنی و تحویل (As-Built) | L3–L4 |
| C17 | اجرای پروژه از طراحی تا تحویل | L4 |

## ۳.۲ اهداف اندازه‌پذیر

- حداقل **۹۰٪ Labها** با Acceptance Criteria تأییدشده تکمیل شوند.
- حداقل **۵۰ سناریوی Troubleshooting** حل و هرکدام با RCA یک‌صفحه‌ای مستند شود.
- Capstone با **Test Plan** اجرا و **As-Built** تحویل شود.
- آزمون نهایی عملی ۲ روزه با نمره ≥ ۸۰٪ و عدم افت هیچ شایستگی «بحرانی» زیر L3.

# ۴. Scope، Out of Scope و Assumptions

## ۴.۱ Scope (در محدوده)

| حوزه | شامل |
|---|---|
| Cisco R&S | CLI از پایه، VLAN/Trunk/STP/EtherChannel، Inter-VLAN، Static/OSPF/FHRP، IPv6 پایه، DHCP/NAT/ACL/NTP/Syslog/SNMP، Hardening، Automation مقدماتی |
| FortiGate 7.0.3 | Administration، Policy/NAT/VIP، Security Profiles (مشروط به لایسنس)، Auth، IPsec/SSL VPN، SD-WAN، HA (مشروط)، Dynamic Routing پایه، Logging |
| زیرساخت | Windows Server (AD/DNS/DHCP/NPS/CA)، Windows Client، Linux (Web/rsyslog/Zabbix) |
| عملیات | Packet Analysis، Troubleshooting/RCA، Monitoring، Backup/Change/Rollback، Incident Response، Handover |
| پروژه | Capstone: HQ + ۳ Branch |

## ۴.۲ Out of Scope (خارج از محدوده)

| غیرهدف | دلیل |
|---|---|
| آمادگی آزمون CCNA/NSE | هدف مهارت عملی است؛ ولی نگاشت به سرفصل CCNA در Curriculum حفظ شده |
| دوره کامل Windows/Linux Administration | فقط آنچه برای شبکه/امنیت لازم است |
| Offensive Security روی شبکه واقعی | ممنوع؛ فقط در Lab ایزوله و دفاعی |
| Cisco ASA/SD-WAN Viptela/ACI/Wi-Fi Controller | خارج از دامنه (Wi-Fi/WLC [OPT] مفهومی) |

---

## ۴.۳ فرضیات (با شناسه برای ردیابی)

| ID | فرض | وضعیت |
|---|---|---|
| A1 | ESXi و PNetLab نصب و در دسترس‌اند | 🔎 نسخه‌ها نامعلوم |
| A2 | منابع (CPU/RAM/Disk) کافی نیست مگر در Discovery اثبات شود | 🔎 |
| A3 | Image قانونی Cisco در دسترس نیست مگر کاربر تأیید کند | 🔎 |
| A4 | Image FortiGate 7.0.3 قابل تهیه است (حساب Fortinet) | `Unverified` 🔎 |
| A5 | آدرس‌های معلوم: ESXi `192.168.88.3`، وب PNetLab `192.168.88.199`؛ ماسک/Subnet و سایر Subnetهای واقعی **نباید با Lab هم‌پوشان** شوند | `Inferred` (احتمالاً `192.168.88.0/24`)؛ Mask `Unverified` 🔎 |
| A6 | دسترسی اینترنت از Lab فقط کنترل‌شده (برای دانلود Package/Update) لازم است؛ Lab به‌صورت پیش‌فرض Air-Gapped | ✅ |
| A7 | Windows Evaluation استفاده می‌شود (Server ۱۸۰ روز: `Verified`؛ Client: `Unverified`) | ✅ |
| A8 | کاربر روزانه ۶ ساعت متمرکز دارد؛ واقع‌بینانه نیست همه ۶ ساعت یکنواخت باشد → Pattern روزانه فصل ۲۷ | ✅ |
| A9 | هیچ تغییری در شبکه مدیریت ESXi و WireGuard/MikroTik انجام نمی‌شود | ✅ قانون |
| A10 | تمام فعالیت امنیتی در Lab ایزوله | ✅ قانون |

# ۵. Learner Profile و Prerequisites

## ۵.۱ پروفایل هنرجو

| جنبه | وضعیت |
|---|---|
| مفاهیم شبکه (OSI، IP، Subnet، VLAN، Routing) | درک مفهومی دارد |
| Cisco IOS CLI | **نیازمند مرور از سطح مقدماتی** (فرض مهارت نداریم) |
| Windows | مدیر شبکه مایکروسافت است (تجربه کاری Windows Server احتمالی 🔎) |
| محیط کاری | MikroTik + WireGuard برای دسترسی به Lab |
| ESXi | `192.168.88.3` — میزبان اصلی |
| PNetLab | وب: `192.168.88.199` (روی ESXi) |

> **پیامد طراحی:** فصل «مرور مفاهیم» کوتاه و تشخیصی (Diagnostic Quiz) است؛ مطالب مسلط‌شده تکرار نمی‌شوند. ولی CLI، Verification و Troubleshooting از صفر و خط‌به‌خط تدریس می‌شود.


## ۵.۲ پیش‌نیازها و آزمون تشخیصی (Diagnostic)

| پیش‌نیاز | سطح لازم | روش سنجش (روز ۱–۲، ۶۰ دقیقه) |
|---|---|---|
| IPv4/Subnetting | توضیح Subnet/Mask/Gateway | ۱۰ سؤال Subnet/VLSM |
| مفاهیم VLAN/Routing | تعریف و کاربرد | ۸ سؤال مفهومی |
| Windows Server پایه | کار با AD/DNS/DHCP (تجربه کاری) 🔎 | چک‌لیست خوداظهاری |
| Linux پایه | ترمینال، SSH | ۵ دستور پایه |
| CLI Cisco | **فرض صفر** | آموزش از پایه (بدون آزمون) |

> **نتیجه آزمون تشخیصی** فقط برای تنظیم عمق مرور در W1–W2 است، نه حذف مبحث.

---

# ۶. Learning Outcomes و Competency Matrix

## ۶.۱ نتایج یادگیری اندازه‌پذیر (پس از دوره، هنرجو می‌تواند…)

| ID | نتیجه یادگیری (فعل قابل سنجش) | شایستگی | Gate | شاهد |
|---|---|---|---|---|
| LO1 | یک شبکه با ≥۴ VLAN را از صفر در Cisco پیکربندی و Verify کند | C2، C3 | G1–G2 | Config + `show` + Capture |
| LO2 | OSPF Multi-Area و مسیر پشتیبان Static را طراحی/اجرا کند | C4 | G3 | Routing Table + Failover Test |
| LO3 | مسیر Packet را از Client تا Server در ۵ نقطه Capture و توضیح دهد | C5، C11 | G7 | گزارش Capture |
| LO4 | FortiGate را Gateway VLANها کند و Policy/NAT/VIP بسازد | C6، C7 | G4 | Policy Matrix + Hit Count |
| LO5 | احراز هویت AD/RADIUS برای Policy/VPN پیاده کند | C9 | G5 | Test Report + Log |
| LO6 | IPsec Site-to-Site و Remote Access VPN برقرار و عیب‌یابی کند | C8 | G6 | Tunnel Test + RCA |
| LO7 | Monitoring/Alert/Dashboard بسازد و Noise را کاهش دهد | C12 | G7 | Dashboard + Alert Catalog |
| LO8 | ≥۴۰ از ۵۰ سناریوی عیب‌یابی را با RCA مستند حل کند | C14 | G7 | RCAها |
| LO9 | Hardening، Backup/Restore و Change با Rollback اجرا کند | C13، C15 | G7–G8 | Change Records |
| LO10 | پروژه HQ+۳ شعبه را طراحی، پیاده، تحویل (As-Built) و از تصمیم‌ها دفاع کند | C1، C16، C17 | G8 | مستندات + دفاع شفاهی |

## ۶.۲ ماتریس شایستگی × Gate

| شایستگی | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 |
|---|---|---|---|---|---|---|---|---|
| C1 طراحی HLD/LLD | | | | | | | | ✔ |
| C2 IP/VLAN | ✔ | ✔ | | | | | | ✔ |
| C3 Cisco CLI | ✔ | ✔ | ✔ | | | | | ✔ |
| C4 Switching/Routing | | ✔ | ✔ | | | | | ✔ |
| C5 Packet Flow | | | | ✔ | | | ✔ | ✔ |
| C6/C7 FortiGate/Policy | | | | ✔ | ✔ | ✔ | | ✔ |
| C8 VPN | | | | | | ✔ | | ✔ |
| C9 Auth | | | | | ✔ | | | ✔ |
| C10 Windows/Linux | | | | | ✔ | | | ✔ |
| C11 Capture | | | | | | | ✔ | ✔ |
| C12 Monitoring | | | | | | | ✔ | ✔ |
| C13 Backup/Change | | | | | | | ✔ | ✔ |
| C14 RCA | | ✔ | ✔ | | | | ✔ | ✔ |
| C15 Hardening | | | | | ✔ | | ✔ | ✔ |
| C16/C17 Docs/Project | | | | | | | | ✔ |

---

# ۷. Teaching Methodology

## ۷.۱ قالب ثابت ۱۸ بخشی

| # | بخش | شرح |
|---|---|---|
| 1 | عنوان و جایگاه | موقعیت در نقشه راه + پیش‌نیاز |
| 2 | اهداف قابل سنجش | فعل‌های Bloom: «پیکربندی کن، تحلیل کن، عیب‌یابی کن» |
| 3 | پیش‌نیازها | درس/Lab قبلی |
| 4 | مفهوم از پایه | بدون حشو، فارسی + معادل انگلیسی |
| 5 | نمودار/معماری | Mermaid/draw.io |
| 6 | Packet Flow | در صورت ارتباط |
| 7 | دستور و تنظیم | خط‌به‌خط + «چرا» |
| 8 | خروجی نمونه و تفسیر | خروجی واقعی Lab |
| 9 | Demo مدرس | ۱۰–۲۰ دقیقه |
| 10 | Guided Lab | قدم‌به‌قدم، Checkpoint |
| 11 | Independent Lab | بدون راهنما، فقط Requirement |
| 12 | سناریوی خرابی | Fault Injection |
| 13 | Troubleshooting | با چارچوب ۱۵ مرحله‌ای |
| 14 | Active Recall | ۵–۱۰ سؤال بدون نگاه |
| 15 | آزمون عملی | ۱۰–۳۰ دقیقه |
| 16 | تکلیف | مستندسازی/تمرین |
| 17 | چک‌لیست تسلط | Self-check |
| 18 | مستند خروجی | فایل‌های ذخیره‌شونده |

## ۷.۲ اصول تدریس

- ساده به پیچیده؛ هر مفهوم بلافاصله Lab.
- **هرگز Config کامل بدون شرح منطق.**
- مقایسه جایگزین‌ها (مثلاً RoAS vs SVI، Policy NAT vs Central NAT).
- مثال‌های سازمانی (Zagros Logistics).
- تکرار فاصله‌دار (روز ۱، ۳، ۷، ۱۴ مرور).
- Active Recall قبل از نمایش پاسخ.
- Teach-Back: توضیح مفهوم با زبان خود (ضبط یا نوشتن).
- Deliberate Practice: تکرار نقطه‌ضعف‌ها.
- اصطلاح انگلیسی با معادل فارسی و کاربرد فنی (مثلاً *Trunk = لینک چند-VLAN*).

---

# ۸. Overall Architecture و Enterprise Reference Topology

## ۸.۱ نمودار مسیر یادگیری و پیش‌نیازها

```mermaid
flowchart TD
    P0[Phase 0: Discovery + Lab Foundation<br/>W1] --> P1[Phase 1: Cisco CLI + IP Foundation<br/>W1-W2]
    P1 --> P2[Phase 2: Switching<br/>W3-W4]
    P2 --> P3[Phase 3: Routing<br/>W5-W6]
    P3 --> P4[Phase 4: IP Services + Automation + Hardening<br/>W7-W8]
    P4 --> CP1{{CP1: Cisco Campus Checkpoint}}
    CP1 --> F1[Phase 5: FortiGate Core + Policy/NAT<br/>W9-W10]
    F1 --> F2[Phase 6: Security Profiles + Auth + Win Server<br/>W11-W12]
    F2 --> F3[Phase 7: VPN IPsec/SSL<br/>W13-W14]
    F3 --> F4[Phase 8: SD-WAN + Dyn Routing + HA + Central Mgmt<br/>W15-W16]
    F4 --> O1[Phase 9: Monitoring/Logging<br/>W17]
    O1 --> T1[Phase 10: Packet Analysis + Troubleshooting + Blue Team<br/>W18-W19]
    T1 --> C1[Phase 11: Capstone Build<br/>W20-W22]
    C1 --> B1[Buffer + Mock Exam W23]
    B1 --> E1{{Final Practical + Handover W24}}
    P4 -. Packet Analysis & Troubleshooting thread .-> T1
    P1 -. Wireshark from W2 .-> T1
```

## ۸.۲ رشته‌های موازی (Threads)

| Thread | از هفته | هر روز | نقش |
|---|---|---|---|
| Packet Analysis | W2 | ۳۰–۶۰ دقیقه | Capture در هر Lab |
| Troubleshooting Drill | W3 | ۶۰ دقیقه | یک عیب جدید یا مرور |
| Documentation (Git) | W1 | ۲۰–۳۰ دقیقه | Config/Workbook/Runbook |
| Active Recall / Spaced Repetition | W1 | ۱۵ دقیقه | کارت‌های مرور (Anki-style) |
| Security Mindset | W7 | در هر Lab | Secure by default |

## ۸.۳ Enterprise Reference Topology (خلاصه)

معماری مرجع سازمان **Zagros Logistics**: HQ + ۳ Branch؛ **FortiGate = Gateway همه VLANها**؛ Cisco = Access/Core L2 + ISP/WAN-Sim؛ IPsec Hub-and-Spoke؛ DMZ؛ AD/DNS/DHCP/NPS؛ Monitoring. جزئیات و دیاگرام: فصل ۱۷.۲ و ۲۹.۲؛ Lab A (Cisco Gateway) مستقل: فصل ۱۷.۲.۱.

# ۹. Lab Safety، Isolation و Risk Management

## ۹.۱ قوانین ایمنی اجرایی (Safety Rails)

1. **R1 — Snapshot/Backup قبل از هر تغییر روی ESXi/PNetLab.**
2. **R2 — بدون Uplink مستقیم Lab به شبکه واقعی** مگر یک NAT Gateway کنترل‌شده و مستند.
3. **R3 — هیچ DHCP Server یا Routing Protocol Lab نباید به شبکه واقعی نشت کند.**
4. **R4 — مدیریت ESXi (`192.168.88.3`) و Port Group مدیریتی دست‌نخورده می‌ماند.**
5. **R5 — Rollback Plan مکتوب قبل از هر تغییر زیرساختی.**
6. **R6 — Image غیرقانونی/Crack ممنوع.**

---

## ۹.۲ الزامات ایمنی Lab (مختص محیط شما)

| # | الزام | شاهد/تست |
|---|---|---|
| S1 | شبکه Lab تا حد ممکن ایزوله (Air-Gapped پیش‌فرض) | Capture روی Uplink Lab: ترافیکی به شبکه واقعی نیست |
| S2 | مدیریت ESXi (`192.168.88.3`) و رابط وب PNetLab (`192.168.88.199`) **در معرض اینترنت قرار نمی‌گیرند**؛ هیچ Port-Forward روی MikroTik برای آن‌ها ساخته نمی‌شود | بررسی Rule MikroTik (فقط خواندن) 🔎 |
| S3 | **FortiGate 7.0.3 و تجهیزات Lab هیچ Port Forwarding یا دسترسی مستقیم اینترنتی ندارند**؛ خروج اینترنت (در صورت نیاز) فقط NAT کنترل‌شده و موقت از یک مرز مستند | Test T9 |
| S4 | مسیر WireGuard و شبکه مدیریت ESXi دست‌نخورده؛ هر تغییر احتمالی فقط با Snapshot/Backup + Rollback مکتوب + **تأیید صریح کاربر** | Checklist قبل/بعد |
| S5 | هر اتصال Lab↔شبکه واقعی یک **مرز مشخص** دارد (دستگاه، Interface، Rule، مالک) و در `02-design/boundary.md` ثبت می‌شود | سند مرز |
| S6 | Image غیرقانونی ممنوع؛ کاربر Imageهای قانونی خود را فراهم می‌کند | Inventory |
| S7 | Debug/Capture پس از استفاده خاموش و Credentialها در Git ذخیره نمی‌شوند | Review |

### مرز Lab↔Real (الگو)

| مرز | دستگاه/Interface | جهت مجاز | Rule | مالک | وضعیت |
|---|---|---|---|---|---|
| B1 Mgmt Jump | PNetLab `pnet0` | Real→Lab (فقط SSH/HTTPS از Jump) | از MikroTik/WireGuard (بدون تغییر) | کاربر | 🔎 |
| B2 اینترنت کنترل‌شده | (اختیاری) VM NAT | Lab→Internet (HTTP/HTTPS/DNS) | Allow-list موقت | کاربر | 🔎 |
| B3 Data-Plane | — | **هیچ** | — | — | ممنوع |

---

## ۹.۳ مدیریت ریسک

ثبت ریسک کامل (احتمال، اثر، پیشگیری، جایگزین) در **فصل ۳۵.۳** است؛ ریسک‌های ایمنی بحرانی: R06 (FortiOS 7.0.x CVE)، R09 (تداخل Lab/Management)، R10 (از دست رفتن دسترسی ESXi).

# ۱۰. PNetLab/ESXi Lab Foundation

## ۱۰.۱ معماری هدف Lab

```mermaid
flowchart LR
    subgraph REAL[شبکه واقعی - دست نخورده]
        MT[MikroTik + WireGuard]
        ESXiMgmt[ESXi Mgmt 192.168.88.3]
    end
    subgraph ESXi[VMware ESXi]
        PN[PNetLab VM<br/>pnet0 = Mgmt]
        subgraph ISOL[vSwitch ایزوله - بدون Uplink]
            PG1[PG-LAB-TRUNK<br/>VLAN 4095 trunk اختیاری]
            VMs[Windows / Linux VMs - اگر روی ESXi]
        end
    end
    subgraph PNET[PNetLab Topology]
        NODES[Cisco IOSv/IOSvL2 + FortiGate VM + QEMU VMs]
        CLOUD[Cloud pnet1 / pnet2 - اتصال کنترل شده]
    end
    MT -.WireGuard.-> ESXiMgmt
    ESXiMgmt --- PN
    PN --- NODES
    NODES --- CLOUD
    CLOUD --- PG1
    PG1 --- VMs
```

**اصول:**
- مدیریت PNetLab (`pnet0`) فقط به Management Port Group (دست‌نخورده).
- Lab Data-Plane کاملاً درون PNetLab یا vSwitch **بدون Uplink**.
- خروج به اینترنت (در صورت نیاز) فقط از یک مسیر NAT کنترل‌شده مستند، نه از Bridge مستقیم.

> وب PNetLab: `192.168.88.199`؛ مدیریت ESXi: `192.168.88.3` (هر دو فقط از مسیر WireGuard/Mgmt؛ بدون Exposure اینترنتی).

## ۱۰.۲ روش اتصال Windows/Linux به PNetLab — مقایسه

| روش | شرح | مزایا | معایب | پیش‌نیاز | توصیه |
|---|---|---|---|---|---|
| **A) QEMU Node داخل PNetLab** | Win/Linux به‌صورت Node با qcow2 | تمام ترافیک داخل PNetLab، بدون وابستگی به Port Group، Snapshot/Export توپولوژی، مطابق ترجیح کاربر | مصرف CPU/RAM بالا (Nested)، سرعت کمتر Windows | Nested Virt فعال، Disk/RAM کافی | ✅ **پیش‌فرض برای ۱–۳ VM سنگین** 🔎 |
| **B) VM روی ESXi + PNetLab Cloud (pnet1) + vSwitch ایزوله** | VMها روی ESXi؛ یک NIC اضافی PNetLab به Port Group ایزوله | کارایی بهتر، Snapshot ESXi | **به یک Port Group وابسته است** (ولی ایزوله و اختصاصی؛ نه Port Groupهای VLAN موجود)، پیچیدگی VLAN Trunk (4095) | NIC اضافی برای PNetLab VM، Port Group ایزوله | ✅ **Fallback اگر RAM/Performance کافی نبود** |
| **C) Cloud0 (pnet0) / Bridge به شبکه Mgmt** | VMها روی شبکه مدیریت | ساده | **ریسک نشت Lab به شبکه واقعی، تداخل DHCP** | — | ❌ فقط برای Management-Only، با فایروال و بدون Data Plane |
| **D) Hybrid** | Windows DC/Client به‌صورت A؛ Linux سبک‌ها داخل PNetLab؛ Monitoring/Zabbix روی ESXi (B) | تعادل منابع | دو مسیر اتصال | — | ✅ **محتمل‌ترین Final Design** |

> **تصمیم قطعی** در پایان Discovery با تأیید کاربر.

## ۱۰.۳ طراحی عملیاتی Lab

| جنبه | طراحی ✅ |
|---|---|
| Naming Convention | `<SITE>-<ROLE><NN>`: `HQ-CORE-SW1`, `HQ-ACC-SW1`, `HQ-FGT-01/02`, `BR1-RTR1`, `ISP1-R1`, `HQ-DC1`, `HQ-WEB-DMZ1`, `HQ-MON1`, `HQ-CL1` |
| IP Convention | Gateway = `.1` (FortiGate) یا `.254` (SVI/HSRP Virtual)؛ سرورها `.10–.50`؛ DHCP Pool `.100–.200` |
| دسترسی | Console از PNetLab؛ SSH از Jump (Windows Terminal) بر روی Mgmt `10.255.0.0/24` |
| Backup | (۱) Export توپولوژی PNetLab (Lab Archive)؛ (۲) Snapshot ESXi قبل از تغییر PNetLab؛ (۳) Config Backup دستگاه‌ها به Git؛ (۴) Backup VMDK/Qcow2 هفتگی |
| Restore | Runbook مستقل (تست در W1) |
| تخمین منابع | فصل ۱۳ (سه Tier) |

## ۱۰.۴ معیار پذیرش Lab Foundation (M0)

| # | Test | Acceptance Criteria |
|---|---|---|
| T1 | ESXi/PNetLab سلامت | Login، Datastore Healthy، Snapshot قابل ایجاد |
| T2 | Nodeها روشن می‌شوند | IOSv/IOSvL2/FGT Boot موفق، CPU idle < ۳۰٪ |
| T3 | Console | دسترسی Console هر Node |
| T4 | L2 | دو Node در یک VLAN ARP می‌کنند |
| T5 | L3 | ping بین دو Subnet عبوری از Router |
| T6 | Packet Capture | Capture روی لینک PNetLab → Wireshark، ICMP دیده می‌شود |
| T7 | VM↔Lab | Windows/Linux Node با Lab ارتباط کنترل‌شده |
| T8 | Backup/Restore | Export و Import Lab + Restore Snapshot موفق |
| T9 | Isolation | از Lab، **هیچ** Packet به `192.168.88.0/24` (غیر از Jump) نمی‌رسد؛ Capture روی Uplink تایید می‌کند |
| T10 | WireGuard/ESXi Mgmt | دست‌نخورده، دسترسی قبل/بعد برابر |
| T11 | Git | Repo مستندات و Configها با اولین Commit |

**خروجی Phase 0:** Runbook آماده‌سازی Lab، نقشه اتصال (As-Built Lab)، چک‌لیست تأیید (امضا شده)، Inventory.

---

# ۱۱. Discovery و Environment Validation

## ۱۱.۱ Discovery و Inventory — فقط خواندنی (Read-Only)

> در این فاز **هیچ تغییری** روی ESXi/PNetLab/MikroTik/WireGuard انجام نمی‌شود؛ فقط جمع‌آوری اطلاعات.

| # | مورد بررسی | روش (Read-Only) | خروجی |
|---|---|---|---|
| D1 | نسخه/Build ESXi | Host Client: Help>About یا `vmware -vl` | ثبت نسخه |
| D2 | CPU (Sockets/Cores/HT)، RAM، Hardware (Intel VT-x/EPT) | Host Client>Hardware | Inventory |
| D3 | Datastore، فضای آزاد، نوع (SSD/HDD)، Thin/Thick | Storage | Inventory |
| D4 | NIC فیزیکی، vSwitch، Port Group، VLAN ID، Uplink | Networking | **نقشه As-Is** |
| D5 | مسیر اتصال PNetLab (کدام Port Group/NIC) | VM Settings | نقشه |
| D6 | نسخه PNetLab و روش نصب (OVA/ISO)؛ وب `192.168.88.199` | PNetLab Web UI/VM | ثبت |
| D7 | منابع VM PNetLab (vCPU/RAM/Disk)، Nested Virt (`hv.enable…` / «Expose HW assisted virtualization») | VM Settings | Inventory |
| D8 | VMهای موجود، Snapshotها، Backup | VM list | وضعیت Backup |
| D9 | مسیر WireGuard/MikroTik (فقط مستندسازی، **بدون تغییر**) | مستند کاربر | نقشه |
| D10 | Subnetهای شبکه واقعی (برای جلوگیری از Overlap) | کاربر | لیست |
| D11 | دسترسی اینترنت Lab (Proxy/NAT) | کاربر | تصمیم |
| D12 | اکانت‌ها/لایسنس: Fortinet Support، Cisco (CML/DevNet)، Microsoft Evaluation | کاربر | وضعیت |


## ۱۱.۲ مرحله Image Validation (قبل از شروع دوره و قبل از وابسته‌کردن درس‌ها)

> هدف: به‌جای فرض، قابلیت واقعی هر Image اندازه‌گیری و در ماتریس فصل ۱۲ ثبت شود. نتیجه، تعیین‌کننده «اجرایی/مفهومی/جایگزین» بودن هر Lab است.

| گام | کار (Read-Only روی ESXi؛ فقط داخل PNetLab) | خروجی |
|---|---|---|
| IV-1 | کاربر Imageهای **قانونی** خود را فراهم و فهرست می‌کند (نام فایل، منبع لایسنس) | لیست Image |
| IV-2 | هر Image در یک Lab آزمایشی جدا Boot می‌شود؛ ثبت CPU/RAM مصرفی | Boot Log |
| IV-3 | Feature-Probe: برای هر Feature فصل ۱۲.۲ یک دستور/تست حداقلی (نمونه: `?` کمکی IOS، `show` مرتبط، Config/Revert بی‌خطر) | وضعیت Supported/Partial/No |
| IV-4 | تست Data-Plane: ping، VLAN Tag، STP BPDU، OSPF Hello بین دو Node | نتایج |
| IV-5 | FortiGate-VM: ورود، `get system status` (نسخه/لایسنس)، شمارش Interface، آزمون License/FortiGuard/HA/SSL-VPN/UTM (Feature-Probe فصل ۱۶.۸) | Feature Matrix |
| IV-6 | ثبت نتایج با تاریخ، نسخه دقیق Image، `Verified (tested)` یا `Unverified` | `image_validation.md` |
| IV-7 | تصمیم Contingency برای Featureهای ناموجود (فصل ۱۲.۳) | Decision Log |

**معیار پذیرش:** هیچ Lab به Featureای وابسته نیست که در IV-3/IV-5 `Unverified` مانده باشد، مگر اینکه Lab به‌صورت «مفهومی/جایگزین» علامت خورده باشد.

## ۱۱.۳ Discovery Checklist (قبل از انتخاب Tier فصل ۱۳)

> **فقط اندازه‌گیری/خواندن؛ هیچ تغییری در محیط واقعی.**

| # | مورد | روش خواندنی | مقدار (کاربر پر می‌کند) | تأثیر بر Tier |
|---|---|---|---|---|
| 1 | مدل CPU، Core/Thread | ESXi Host Client → Hardware | ☐ | تعداد vCPU قابل تخصیص |
| 2 | RAM کل | همان | ☐ | تعیین Tier |
| 3 | RAM آزاد/قابل تخصیص به Lab | همان + VMهای موجود | ☐ | **تعیین Tier** |
| 4 | Storage کل/آزاد، SSD/HDD، Thin/Thick | Storage | ☐ | Disk/Snapshot |
| 5 | نسخه/Build دقیق ESXi | About | ☐ | سازگاری Nested |
| 6 | نسخه PNetLab (وب `192.168.88.199`) | Web UI → About/Settings | ☐ | Image/Interface Limit |
| 7 | نوع/تعداد NICهای فیزیکی و vNIC قابل‌افزودن به PNetLab VM | Networking | ☐ | مسیر اتصال VMهای ESXi |
| 8 | vSwitch/Port Groupهای موجود؛ امکان ساخت **یک** vSwitch بدون Uplink (فقط اگر کاربر تأیید کند) | Networking (مشاهده) | ☐ | روش B/D فصل ۱۰.۲ |
| 9 | نحوه اتصال PNetLab به VMهای خارج از آن | ترسیم As-Is | ☐ | معماری Hybrid |
| 10 | Imageهای قانونی موجود (Cisco/Fortinet) | کاربر | ☐ | Image Matrix |
| 11 | Nested Virtualization (Expose HW Virtualization روی PNetLab VM؛ CPU feature) | VM Settings | ☐ | امکان QEMU Node |
| 12 | Snapshot/Backup (Datastore، سیاست، آخرین Backup) | کاربر/ESXi | ☐ | R1 ایمنی |
| 13 | روش دسترسی امن و Rollback (WireGuard، دسترسی Out-of-band/کنسول فیزیکی) | کاربر | ☐ | ریسک از دست رفتن دسترسی |
| 14 | Subnetهای واقعی (Overlap با فصل ۱۴) | کاربر | ☐ | IP Plan |
| 15 | دسترسی حساب‌ها: Fortinet Support، Cisco (CML/DevNet)، Microsoft Eval | کاربر | ☐ | Image |

---

# ۱۲. Image Compatibility Matrix

## ۱۲.۱ جدول سازگاری Image

| تجهیز | کاربرد آموزشی | منابع | سازگاری PNetLab/ESXi | محدودیت‌ها `Unverified` | روش قانونی تهیه | تست قبل از ورود |
|---|---|---|---|---|---|---|
| **FortiGate-VM 7.0.3** | نقش اصلی | 1 vCPU/2 GB (Eval `Unverified`) | KVM/QEMU نوع `fortinet` در PNetLab | لایسنس Eval، FortiGuard، HA، تعداد Interface | Fortinet Support (حساب + Evaluation License) | Boot، License Import، `get system status` |
| **Cisco IOSv** | Router | 1/0.5 GB | QEMU | بدون برخی Featureهای سخت‌افزاری | CML-Personal/DevNet/Partner (لایسنس) 🔎 | ping/OSPF/NAT/ACL |
| **Cisco IOSvL2** | L2/L3 Switch | 1/~1 GB | QEMU | محدودیت در EtherChannel/DAI/Snooping/STP Feature `Unverified` | همان | VLAN/Trunk/STP/EtherChannel |
| Win Server 2022 Eval | AD/NPS/CA | 2/4 | QEMU یا ESXi | ۱۸۰ روز (Server: `Verified`) | Microsoft Evaluation Center | Boot، Domain |
| Win 10/11 Client Eval | Client | 2/4 | همان | ۹۰ روز `Unverified`، TPM در Win11 | Microsoft | Join Domain |
| Ubuntu/Debian Server | WEB/MON | 1–2/1–4 | QEMU/ESXi | — | Distro رسمی | SSH، Package |
| FortiManager/FortiAnalyzer VM | مدیریت | 4/8 `Unverified` | ESXi (بهتر از QEMU) | لایسنس Eval، سازگاری نسخه | Fortinet Support | Login، Registration |
| Zabbix | Monitoring | 2/4 | Linux | — | رایگان | Poll SNMP |


## ۱۲.۲ Cisco Feature Compatibility Matrix (Image Validation)

> **هیچ فرمانی صرفاً به‌دلیل آشنایی از IOS واقعی برای Image شبیه‌سازی‌شده قطعی فرض نشده است.** ستون «آزمایش» تا اجرای IV-3 همه `Unverified (Not Tested)` است. «وضعیت مستند» باید از Cisco Configuration Guide/CML Docs بر اساس **Image/Release دقیق** تکمیل شود (فعلاً `Unverified`). نسخه‌ها در IV-2 ثبت می‌شوند.

| # | Feature | Image/Platform هدف | نسخه موردنیاز | فرمان/روش بررسی قابلیت | وضعیت پشتیبانی مستندشده | آزمایش | محدودیت شناخته‌شده | جایگزین معتبر |
|---|---|---|---|---|---|---|---|---|
| 1 | VLAN و Access Port | IOSvL2 | 🔎 | `show vlan brief`؛ `switchport access vlan` | `Unverified` | Not Tested | — | — |
| 2 | 802.1Q Trunk | IOSvL2 | 🔎 | `show interfaces trunk` | `Unverified` | Not Tested | (Encapsulation dot1q ممکن است نیاز به فرمان صریح باشد) | — |
| 3 | STP/RSTP | IOSvL2 | 🔎 | `show spanning-tree summary` | `Unverified` | Not Tested | — | PVST+ مفهومی |
| 4 | EtherChannel LACP/PAgP | IOSvL2 | 🔎 | `show etherchannel summary` | `Unverified` | Not Tested | PAgP ممکن است ناموجود | LACP/مفهومی |
| 5 | Inter-VLAN (RoAS) | IOSv | 🔎 | Sub-interface + `show ip route` | `Unverified` | Not Tested | — | — |
| 6 | SVI/L3 Switching | IOSvL2 | 🔎 | `ip routing`، `show ip route` | `Unverified` | Not Tested | — | RoAS |
| 7 | Static/Default Route | IOSv/IOSvL2 | 🔎 | `show ip route` | `Unverified` | Not Tested | — | — |
| 8 | OSPFv2/v3 | IOSv/IOSvL2 | 🔎 | `show ip ospf neighbor` | `Unverified` | Not Tested | — | — |
| 9 | IPv6 | IOSv | 🔎 | `show ipv6 interface brief` | `Unverified` | Not Tested | — | — |
| 10 | ACL (Std/Ext) | IOSv/IOSvL2 | 🔎 | `show access-lists` | `Unverified` | Not Tested | — | — |
| 11 | DHCP Server/Relay | IOSv/IOSvL2 | 🔎 | `show ip dhcp pool/binding` | `Unverified` | Not Tested | — | Windows/FGT DHCP |
| 12 | HSRP/VRRP/FHRP | IOSv/IOSvL2 | 🔎 | `show standby brief` | `Unverified` | Not Tested | — | FGT VRRP/مفهومی |
| 13 | DHCP Snooping | IOSvL2 | 🔎 | `show ip dhcp snooping` | `Unverified` | Not Tested | احتمال پشتیبانی ناقص | CLI Review/Image دیگر (قانونی) |
| 14 | Dynamic ARP Inspection | IOSvL2 | 🔎 | `show ip arp inspection` | `Unverified` | Not Tested | احتمال ناموجود | همان |
| 15 | Port Security | IOSvL2 | 🔎 | `show port-security` | `Unverified` | Not Tested | — | Storm-control/مفهومی |
| 16 | SPAN/Port Mirroring | IOSvL2 | 🔎 | `show monitor session all` | `Unverified` | Not Tested | احتمال ناموجود | Capture روی لینک PNetLab |
| 17 | Embedded Packet Capture | IOSv | 🔎 | `monitor capture` (وجود فرمان) | `Unverified` | Not Tested | احتمال ناموجود | PNetLab Capture |
| 18 | Syslog | IOSv/IOSvL2 | 🔎 | `show logging` + دریافت در rsyslog | `Unverified` | Not Tested | — | — |
| 19 | SNMP (v2c/v3) | IOSv/IOSvL2 | 🔎 | `show snmp` + `snmpwalk` | `Unverified` | Not Tested | سینتکس v3 | v2c (فقط Lab) |
| 20 | NTP | IOSv/IOSvL2 | 🔎 | `show ntp status` | `Unverified` | Not Tested | — | — |
| 21 | QoS پایه | IOSv/IOSvL2 | 🔎 | `show policy-map` | `Unverified` | Not Tested | — | مفهومی |
| 22 | NAT/PAT | IOSv | 🔎 | `show ip nat translations` | `Unverified` | Not Tested | — | — |
| 23 | IP SLA/Track | IOSv | 🔎 | `show ip sla statistics` | `Unverified` | Not Tested | — | FGT Link Monitor |

**قاعده تصمیم:** Featureای که پس از IV-3 `Supported` شد، به «Verified (tested)» ارتقا و در Reference Log (فصل ۳۴) ثبت می‌شود؛ اگر `No/Partial` بود، Lab مربوط طبق ستون «جایگزین» بازطراحی می‌شود (و در Traceability ثبت).

---

## ۱۲.۳ سناریوهای جایگزین (Contingency)

| مشکل | جایگزین معتبر |
|---|---|
| IOSvL2 فاقد DAI/Snooping | لایه Security در سناریو «مفهومی + CLI Review» + استفاده Cisco **CSR1000v/Catalyst 8000v (لایسنس قانونی)** `Unverified` یا فقط Port-Security/Storm-Control |
| Image Cisco در دسترس نیست | Cisco **Packet Tracer** (رایگان با Netacad) برای Phase 1–2 CLI + سناریوی L2 محدود؛ `Unverified` Packet Tracer شبیه‌ساز است نه IOS واقعی؛ Plan برای CML Personal پیشنهاد می‌شود |
| FortiGate 7.0.3 در دسترس نیست | نزدیک‌ترین 7.0.x (مشروط به تأیید کاربر + ثبت تفاوت) |
| HA در Eval ممکن نیست | HA مفهومی + Lab روی VM لایسنس‌دار (اگر دسترسی) |
| FAZ/FMG ممکن نیست | مفهومی + مستند رسمی |

---

# ۱۳. Lab Resource Tiers

> **همه اعداد «برآورد طراحی (Inferred)» هستند**، نه مشخصات قطعی محیط شما. منابع واقعی در Discovery (فصل ۱۱.۳) اندازه‌گیری می‌شود. فرض‌ها: (۱) مقادیر هر VM بر پایه حداقل‌های متداول مستندات سازنده‌هاست و **باید با مستند رسمی نسخه تأیید شود (`Unverified`)**؛ (۲) Overcommit CPU مجاز ولی RAM به‌صورت Reserve نیست؛ (۳) FortiGate-VM Eval ممکن است سقف vCPU/RAM داشته باشد (`Unverified`).

## ۱۳.۱ تعریف Tierها

| Tier | نام | هدف | RAM آزاد پیشنهادی (تقریبی) | Disk آزاد (تقریبی) |
|---|---|---|---|---|
| **T1** | Minimum / Essential | یادگیری مباحث اصلی؛ Labهای ضروری (Cisco تمام + FGT تک‌دستگاه) | ≈ ۲۴–۳۲ GB | ≈ ۲۰۰ GB |
| **T2** | Standard / Recommended | بیشتر سناریوهای یکپارچه + Capstone مرحله‌ای | ≈ ۴۸–۶۴ GB | ≈ ۴۰۰ GB |
| **T3** | Full / Advanced | HA، چند شعبه هم‌زمان، چند FortiGate، چند Win/Linux، Monitoring کامل | ≈ ۹۶–۱۲۸ GB | ≈ ۸۰۰ GB |

## ۱۳.۲ Tier 1 — Minimum / Essential

| Node/VM | تعداد | vCPU | RAM | Storage | NIC/Interface | مرحله‌ای؟ |
|---|---|---|---|---|---|---|
| PNetLab VM | 1 | 6–8 | 12–16 GB | 80 GB | 1 Mgmt + 1 اختیاری | همیشه روشن |
| IOSvL2 | 2–3 | 1 | ~1 GB | ~1 GB | تا 8 | بله |
| IOSv | 2–3 | 1 | ~0.5 GB | ~0.5 GB | تا 8 | بله |
| FortiGate-VM | 1 | 1 | 2 GB | 2–4 GB | 4–6 | بله |
| Windows Server | 1 | 2 | 4 GB | 60 GB | 1 | روشن فقط در W4/W12 و Capstone |
| Windows Client | 1 | 2 | 4 GB | 50 GB | 1 | بله |
| Linux (WEB/MON ترکیبی) | 1 | 1–2 | 2–4 GB | 30 GB | 1 | بله |
| **جمع هم‌زمان نمونه** | | ≈ 10–14 vCPU | **≈ 24–30 GB** | ≈ 230 GB | | |

- **قابل اجرا:** Cisco کامل (W1–W8)، FGT تک (Policy/NAT/UTM/Auth)، یک IPsec با یک FGT دوم (۲ FGT هم‌زمان با خاموشی بقیه)، Monitoring سبک.
- **غیرقابل اجرا:** HA، Capstone ۴ سایت هم‌زمان، FMG/FAZ، چند Windows هم‌زمان.
- **راهکار کاهش مصرف:** Capstone به‌صورت Tiered (فقط HQ+۱ Branch)، مانیتورینگ با Zabbix سبک، خاموشی VMهای بی‌استفاده، Clone سبک (Linked Clone).
- **ریسک:** RAM دائماً مرزی؛ Swap/Overcommit باعث کندی Boot Node.

## ۱۳.۳ Tier 2 — Standard / Recommended

| Node/VM | تعداد | vCPU | RAM | Storage | NIC/Interface | روشن/خاموش مرحله‌ای |
|---|---|---|---|---|---|---|
| PNetLab VM | 1 | 8–12 | 20–24 GB | 100 GB | 1–2 | همیشه |
| IOSvL2 | 4 | 1 | ~1 GB | ~1 GB | تا 8 | Core/Access/Branch |
| IOSv | 5 | 1 | ~0.5 GB | ~0.5 GB | تا 8 | ISP/WAN/Branch |
| FortiGate-VM | 3 (HQ + BR1 + BR2) | 1–2 | 2–4 GB | 4 GB | 6 | HQ همیشه |
| Windows Server | 1–2 | 2 | 4 GB | 60 GB | 1 | DC همیشه در W12+ |
| Windows Client | 2 | 2 | 4 GB | 50 GB | 1 | بله |
| Linux (WEB-DMZ، MON، SYSLOG) | 3 | 1–2 | 1–4 GB | 15–60 GB | 1 | MON همیشه در W17+ |
| **جمع هم‌زمان نمونه** | | ≈ 22–30 vCPU | **≈ 50–62 GB** | ≈ 500 GB | | |

- **قابل اجرا:** تقریباً همه Labها و Capstone با ۳ سایت (دو شعبه هم‌زمان)؛ VPN، SD-WAN، DMZ، AD، Monitoring.
- **غیرقابل اجرا:** HA کامل با ۴ سایت هم‌زمان، FMG/FAZ هم‌زمان.
- **کاهش مصرف:** BR3 فقط در آزمون‌های مشخص روشن.
- **ریسک:** Disk I/O مشترک؛ CPU Ready.

## ۱۳.۴ Tier 3 — Full / Advanced

| Node/VM | تعداد | vCPU | RAM | Storage | NIC/Interface | یادداشت |
|---|---|---|---|---|---|---|
| PNetLab VM | 1 | 12–16 | 32 GB | 150 GB | 2+ | Nested فعال |
| IOSvL2 | 6 | 1 | ~1 GB | ~1 GB | 8 | HQ Core×2, Access×2, BR×2 |
| IOSv | 6 | 1 | ~0.5 GB | ~0.5 GB | 8 | ISP×2 + BR |
| FortiGate-VM | 5–6 (HQ HA×2 + BR1–3) | 2 | 4 GB | 4 GB | 8 | HA مشروط به Image/License (`Unverified`) |
| Windows Server | 2 | 2–4 | 4–8 GB | 80 GB | 1 | DC + NPS/CA |
| Windows Client | 3 | 2 | 4 GB | 50 GB | 1 | |
| Linux | 4 | 1–2 | 2–4 GB | 20–80 GB | 1 | WEB/MON/SYSLOG/Tools |
| FortiManager/FortiAnalyzer | 0–2 | 4 | 8+ GB (`Unverified`) | 100+ GB | 1 | مشروط به لایسنس/Image |
| **جمع هم‌زمان نمونه** | | ≈ 45–60 vCPU | **≈ 110–135 GB** | ≈ 1 TB | | ESXi میزبان ≥ 128–160 GB RAM پیشنهاد |

- **قابل اجرا:** همه Labها و Capstone کامل، HA (در صورت امکان)، Failure Drill چندسایت.
- **ریسک:** هزینه/نگهداری؛ Nested Virt در PNetLab برای تعداد بالای Node.

## ۱۳.۵ تصمیم Tier

| شرط (پس از Discovery) | Tier |
|---|---|
| RAM آزاد < ۲۴ GB | **تحت T1 هم نمی‌گنجد** → اعلام ریسک و تصمیم کاربر (کاهش دامنه Lab، افزودن RAM، یا زمان اجرای Labها با خاموشی مرحله‌ای) |
| ۲۴–۴۸ GB | T1 |
| ۴۸–۹۶ GB | T2 |
| ≥ ۹۶ GB | T3 |

> **بدون تغییر در ۸۶۴ ساعت:** Tier پایین‌تر فقط Labهای وابسته را به «مفهومی/Tabletop» یا «نوبتی» تبدیل می‌کند (در Traceability ثبت می‌شود).

# ۱۴. IP Addressing، VLAN و Naming Standards

## ۱۴.۱ تفکیک شبکه‌ها و Address Space

| شبکه | کاربرد | آدرس پیشنهادی ✅ | عبور به شبکه واقعی |
|---|---|---|---|
| Real Mgmt | ESXi `192.168.88.3` / PNetLab `192.168.88.199` / MikroTik | `192.168.88.0/24` (`Inferred`؛ Mask `Unverified` 🔎) | — |
| Lab OOB Mgmt | مدیریت تجهیزات Lab | `10.255.0.0/24` | ممنوع (فقط از PNetLab Jump) |
| Lab Loopbacks | RID/Mgmt Loopback | `10.254.0.0/24` | ممنوع |
| HQ | سازمان | `10.10.0.0/16` | ممنوع |
| BR1/BR2/BR3 | شعب | `10.20/30/40.0.0/16` | ممنوع |
| DMZ | سرورهای عمومی | `172.16.10.0/24` | ممنوع |
| ISP1 (شبیه‌سازی) | WAN اصلی | `203.0.113.0/24` (TEST-NET-3) | ممنوع |
| ISP2 (شبیه‌سازی) | WAN پشتیبان | `198.51.100.0/24` (TEST-NET-2) | ممنوع |
| Transit/P2P | لینک بین دستگاه | `10.99.x.x/30` | ممنوع |
| Remote-VPN Pool | کاربران راه دور | `10.250.0.0/24` | ممنوع |

🔎 `Unverified` (Discovery) عدم Overlap با شبکه‌های واقعی کاربر.


## ۱۴.۲ طرح VLAN و Gateway سازمان (معماری اصلی Capstone: FortiGate Gateway)

> **قانون مالکیت:** در Capstone، **FortiGate مالک Default Gateway همه VLANهای سازمانی** است. سوئیچ‌های Cisco فقط L2 هستند (`no ip routing`) و تنها یک SVI مدیریتی (VLAN 10) برای مدیریت دارند.

| VLAN | نام | Subnet HQ | Gateway (مالک) | Zone FGT | DHCP | کاربرد |
|---|---|---|---|---|---|---|
| 10 | MGMT | 10.10.10.0/24 | `.1` — FGT | `Z-MGMT` | Static | مدیریت تجهیزات (SVI فقط روی سوئیچ برای مدیریت) |
| 20 | FINANCE | 10.10.20.0/24 | `.1` — FGT | `Z-FIN` | DHCP (DC/Relay) | مالی |
| 30 | HR | 10.10.30.0/24 | `.1` — FGT | `Z-HR` | DHCP | منابع انسانی |
| 40 | IT | 10.10.40.0/24 | `.1` — FGT | `Z-IT` | DHCP | IT |
| 50 | USERS | 10.10.50.0/24 | `.1` — FGT | `Z-USERS` | DHCP | کاربران عمومی |
| 60 | SERVERS | 10.10.60.0/24 | `.1` — FGT | `Z-SRV` | Static | AD/DNS/DHCP/MON/SYSLOG |
| 80 | GUEST | 10.10.80.0/24 | `.1` — FGT | `Z-GUEST` | DHCP (FGT) | مهمان (Captive) |
| 99 | BLACKHOLE | — | — | — | — | Native/Unused |
| 100 | DMZ | 172.16.10.0/24 | `.1` — FGT | `Z-DMZ` | Static | Web/ERP |

- **Branchها** (هر سایت FGT مالک Gateway): VLAN 10 MGMT `10.X.10.0/24`، VLAN 50 USERS `10.X.50.0/24`، VLAN 80 GUEST `10.X.80.0/24`؛ BR1 دارای VLAN 60 `10.20.60.0/24` (Local Server). با `X=20,30,40` برای BR1–BR3.
- **Gateway در HA:** آدرس `.1` روی Cluster (FGCP، `Unverified` در VM Eval)؛ بدون HA، FGT تکی.
- **DHCP:** VLANهای کاربری از DC (Relay توسط FGT)؛ GUEST از FGT.

## ۱۴.۳ IPAM و مستندسازی آدرس‌ها

| سطح | ابزار/روش | محتوا | مالک |
|---|---|---|---|
| ضروری | جدول IPAM در Git (`02-design/ipam.csv` + Markdown) | Prefix، VLAN، Gateway، Zone، DHCP Range، Reservation، مالک | هنرجو |
| **[OPT]** | NetBox (فصل ۳۴) | همان + Device/Interface | هنرجو |

| فیلد IPAM (حداقل) | مثال |
|---|---|
| Prefix | 10.10.20.0/24 |
| VLAN/Site | 20 / HQ |
| Gateway/Owner | 10.10.20.1 / HQ-FGT |
| Zone | Z-FIN |
| DHCP Range/Reservation | .100–.200 / `.20` پرینتر |
| تاریخ تغییر/شناسه Change | 2026-… / CHG-0007 |

**قوانین:** هر Subnet با Overlap-Check؛ تغییر آدرس فقط با Change Record؛ IPAM هم‌تراز با As-Built.

## ۱۴.۴ Naming Standards

| نوع | الگو | مثال |
|---|---|---|
| دستگاه | `<SITE>-<ROLE><NN>` | `HQ-CORE-SW1`، `HQ-FGT-01`، `BR1-FGT-01`، `ISP1-R1`، `HQ-DC1`، `HQ-WEB-DMZ1`، `HQ-MON1`، `HQ-CL1` |
| Zone FGT | `Z-<NAME>` | `Z-FIN` |
| Policy FGT | `<SRC>-to-<DST>-<SVC>` | `Z-USERS-to-WAN-WEB` |
| Address Obj | `NET-<name>` / `H-<name>` | `NET-FIN` |
| VPN | `VPN-<A>-<B>-<n>` | `VPN-HQ-BR1-1` |
| فایل | `<LabID>_<Topic>_<Device>_<YYYYMMDD>_<vN>.<ext>` | فصل ۳۱.۱ |

# ۱۵. Cisco Routing & Switching Curriculum

> **Cisco در هر ۲۴ هفته حضور دارد** (Spiral، فصل ۲۸). جدول‌های این فصل نماینده فرمان‌ها هستند؛ هر فرمان تا Image Validation (فصل ۱۱.۲) روی IOSv/IOSvL2 `Unverified` است.

## ۱۵.۱ پایه و CLI (W1–W2)

| مبحث | پیش‌نیاز | مفهوم | دستورات کلیدی | Verification | سالم / خراب | Capture | معیار تسلط |
|---|---|---|---|---|---|---|---|
| OSI/TCP-IP عملی | — | Encapsulation واقعی در Wireshark | — | Capture یک ping | ping سالم / ARP بی‌پاسخ | ARP+ICMP | توضیح هر هدر در Capture |
| Ethernet/MAC/ARP | OSI | Frame، ARP Cache | `show mac address-table`, `show ip arp` | جدول ARP/MAC | ARP عادی / Duplicate IP | arp | توضیح مسیر L2 |
| IPv4/Subnet/VLSM | — | تقسیم‌بندی، Summarization | — | کار روی کاغذ+Lab | VLSM صحیح / Mask اشتباه | — | حل ۱۰ مسئله VLSM در ۲۰ دقیقه |
| IPv6 مقدماتی | IPv4 | Global/Link-Local، SLAAC، NDP | `ipv6 address`, `show ipv6 interface brief` | ping6 | سالم / نبود `ipv6 unicast-routing` | ICMPv6 NS/NA | ساخت طرح IPv6 |
| IOS CLI Modes | — | User/Priv/Global/Interface | `enable`, `configure terminal`, `interface`, `exit`, `end` | `show running-config` | — | — | جابه‌جایی سریع بدون خطا |
| مدیریت Config/File | CLI | Running vs Startup | `copy running-config startup-config`, `show startup-config`, `erase`, `reload`, `copy tftp`/`scp` | diff Config | Backup/Restore موفق / فراموشی save | — | Restore کامل از Backup |
| ابزار عیب‌یابی | CLI | Test و Evidence | `ping`, `traceroute`, `show ip interface brief`, `show interfaces`, `show logging`, `debug` (با احتیاط + `undebug all`) | خروجی ping/trace | — | — | استفاده بدون ایجاد Load/ریسک |
| امن‌سازی مدیریت | CLI | Password، SSH، AAA محلی، Banner | `enable secret`, `service password-encryption`, `username … secret`, `ip domain-name`, `crypto key generate rsa`, `ip ssh version 2`, `line vty 0 4`, `transport input ssh`, `login local`, `access-class`, `exec-timeout` | SSH از Linux/Windows | SSH سالم / Telnet فعال | SSH vs Telnet | حذف Telnet و محدودیت Source |

## ۱۵.۲ Switching (W3–W4)

| مبحث | پیش‌نیاز | مفهوم | دستورات کلیدی | Verification | سناریوی خراب | معیار تسلط |
|---|---|---|---|---|---|---|
| CAM/MAC Table | MAC/ARP | Learning/Flooding/Aging | `show mac address-table dynamic` | MAC در پورت درست | Flooding به‌دلیل MAC نشده | توضیح مسیر Frame |
| VLAN/Access | CAM | تفکیک L2 | `vlan 10`, `name`, `switchport mode access`, `switchport access vlan` | `show vlan brief` | VLAN اشتباه روی پورت | ساخت VLAN Matrix |
| Trunk/802.1Q | VLAN | Tag، Native، Allowed | `switchport trunk encapsulation dot1q` (در صورت نیاز)، `switchport mode trunk`, `switchport trunk native vlan`, `switchport trunk allowed vlan`, `switchport nonegotiate` | `show interfaces trunk` | Native Mismatch، Allowed حذف‌شده | رفع در <۵ دقیقه |
| Inter-VLAN: RoAS | Trunk | Sub-interface | `interface g0/0.10`, `encapsulation dot1Q 10`, `ip address` | ping بین VLAN | Encapsulation اشتباه | — |
| SVI / L3 Switch | VLAN | Gateway مجازی هر VLAN روی L3 Switch | `interface vlan 10`, `ip routing` | `show ip route`, `show ip interface brief` | SVI Down (بدون پورت UP در VLAN) | ping بین ۳ VLAN و توضیح شرط Up بودن SVI |
| STP/RSTP | VLAN/Trunk | Root، Port Roles، BPDU | `spanning-tree mode rapid-pvst`, `spanning-tree vlan 1 root primary`, `priority` | `show spanning-tree` | Root اشتباه، Loop | تعیین Root عمدی |
| PortFast/BPDU Guard | STP | Edge Port | `spanning-tree portfast`, `spanning-tree bpduguard enable`, `errdisable recovery` | `show spanning-tree summary` | Err-disable بعد از اتصال سوئیچ | — |
| EtherChannel | Trunk | LACP | `channel-group 1 mode active`, `interface port-channel 1` | `show etherchannel summary` | Mismatch (Mode/Speed/VLAN) | PAgP فقط مفهومی `Unverified` |
| Port Security | Access | MAC Limit | `switchport port-security`, `maximum`, `violation`, `mac-address sticky` | `show port-security interface` | Violation shutdown | — |
| DHCP Snooping / DAI | DHCP | Trusted/Untrusted | `ip dhcp snooping`, `ip dhcp snooping vlan`, `ip dhcp snooping trust`, `ip arp inspection vlan`, `ip arp inspection trust` | `show ip dhcp snooping binding` | Rogue DHCP در Lab `Unverified` پشتیبانی IOSvL2 | — |
| طراحی 3-Tier | همه | Access/Distribution/Core، Collapsed Core | — | HLD | — | توجیه Collapsed Core برای شعبه |

## ۱۵.۳ Routing (W5–W6)

| مبحث | مفهوم | دستورات کلیدی | Verification | سناریوی خراب | معیار تسلط |
|---|---|---|---|---|---|
| Routing Table / LPM | کدام Route انتخاب می‌شود | `show ip route`, `show ip route <net>` | توضیح AD/Metric/Prefix | Route بهتر اشتباه | پیش‌بینی مسیر بدون Lab |
| Static/Default/Floating | AD، Backup Path | `ip route`, `ip route 0.0.0.0 0.0.0.0`, `ip route … 200` | Failover با قطع لینک | مسیر برگشت نبود | Return-path Thinking |
| OSPFv2 | LSA، SPF، DR/BDR | `router ospf 1`, `network … area`, `passive-interface`, `ip ospf cost`, `default-information originate` | `show ip ospf neighbor`, `show ip ospf interface brief`, `show ip route ospf` | Hello/Dead/MTU/Area/Auth Mismatch | رفع ۵ نوع عدم تشکیل Adjacency |
| OSPF Multi-Area | ABR، Summarization | `area x range`, `area x stub` | LSDB | Virtual-link (مفهومی) | طراحی ۲ Area |
| OSPFv3 / IPv6 Routing | Address-Family | `ipv6 router ospf`, `ipv6 ospf 1 area 0` | `show ipv6 ospf neighbor` | — | — |
| HSRP/VRRP | Gateway Redundancy | `standby 1 ip`, `standby 1 priority`, `preempt` (`Unverified` در IOSv/IOSvL2 تأیید شود) | `show standby brief` | Active دوگانه | Failover کمتر از ۵ ثانیه |
| Troubleshooting Routing | مسیر رفت/برگشت | `show ip route`, `traceroute`, `debug ip ospf adj` (با احتیاط) | | Asymmetric | روش سیستماتیک |

## ۱۵.۴ IP Services (W7)

| مبحث | دستورات کلیدی | Verification | خراب |
|---|---|---|---|
| DHCP + Relay | `ip dhcp pool`, `ip dhcp excluded-address`, `ip helper-address` | `show ip dhcp binding` | Relay فراموش‌شده |
| DNS | `ip name-server`, `ip domain lookup` | `nslookup` از Client | DNS غلط |
| NTP | `ntp server`, `clock timezone` | `show ntp associations` | اختلاف ساعت → Log بی‌ارزش |
| NAT/PAT | `ip nat inside/outside`, `ip nat inside source list … overload` | `show ip nat translations` | NAT دوگانه |
| ACL استاندارد/Extended | `ip access-list extended`, `permit/deny`, `ip access-group` | `show access-lists` (Hit Count) | ترتیب اشتباه، Implicit Deny |
| Syslog | `logging host`, `logging trap`, `service timestamps` | دریافت در rsyslog | عدم دریافت |
| SNMP | `snmp-server group/user` (v2c فقط Lab؛ v3 `Unverified` سینتکس تأیید شود) | Zabbix Poll موفق | Community لو رفته |
| QoS مقدماتی | Class-map/Policy-map (مفهومی + یک Lab ساده) | `show policy-map interface` | — |

## ۱۵.۵ Automation و مدیریت (W8)

| مبحث | محتوا | Lab | معیار |
|---|---|---|---|
| JSON/YAML/REST | ساختار، `curl`، Postman | فراخوانی API یک سرویس Lab | خواندن JSON |
| Python برای ادمین | `netmiko` برای `show` و Backup | اسکریپت Backup همه سوئیچ‌ها | اجرای ایمن (فقط read) |
| Ansible (مقدماتی) | Inventory/Playbook ساده (`ios_command`, `ios_config`) | استقرار Banner/NTP روی ۵ دستگاه | Idempotency |
| Git | commit/diff/branch برای Config | Versioning Configها | مشاهده تغییر با `git diff` |
| دستی vs خودکار | مقایسه ریسک/سرعت | گزارش یک‌صفحه‌ای | قضاوت مستدل |

---

# ۱۶. FortiGate 7.0.3 Curriculum

> نسخه هدف **FortiOS 7.0.3** (بدون اجازه کاربر تغییر نمی‌کند). این نسخه قدیمی است و فقط در Lab ایزوله؛ استفاده آموزشی ≠ توصیه Production (فصل ۱۶.۹).

## ۱۶.۱ Fundamentals & Administration (W9)

| مبحث | مفهوم | CLI/GUI | Verification | خراب | معیار تسلط |
|---|---|---|---|---|---|
| معماری | Kernel/Proxy-Flow، Packet Flow Ingress→Egress | `diagnose debug flow` | توضیح مسیر | — | رسم Packet Flow |
| Interface | Physical/VLAN/Aggregate/Loopback | `config system interface` / Network>Interfaces | `get system interface` | Role/Allowaccess اشتباه | VLAN Sub-interface روی Trunk |
| Management Access | HTTPS/SSH/PING Allowaccess، Trusted Hosts، Admin Port | `set allowaccess`, `set trusthost1` | دسترسی از Mgmt VLAN | قفل شدن از GUI | **Backup قبل از تغییر** |
| Routing/Static/Policy Route | RPF، ECMP، Distance/Priority | `config router static`, `config router policy` | `get router info routing-table all` | Route غلط | — |
| Zone/Address/Service | Object Model | `config firewall address/addrgrp/service` | — | Object اشتباه | Naming استاندارد |
| Admin/RBAC | Profile، 2FA (مشروط)، Trusted Host | `config system accprofile`, `config system admin` | Login محدود | Admin بدون Trusthost | Least Privilege |
| Backup/Restore/Firmware | Config Backup، Revision، Firmware Upgrade Path | `execute backup config …`, GUI | Restore در VM جدید | Upgrade بدون Backup | `Unverified` مسیر Upgrade طبق Release Notes |

## ۱۶.۲ Firewall Policy & NAT (W10)

| مبحث | مفهوم | Verification | خراب |
|---|---|---|---|
| Policy Evaluation | Top-Down، First Match، Implicit Deny | `diagnose firewall iprope lookup`, Hit Count | Shadow Policy |
| Policy Elements | Interface/Source/Dest/Service/Schedule/Action/Log | Log در Forward Traffic | Log Disabled |
| NAT (Policy NAT) vs Central NAT | تفاوت، محدودیت، انتخاب | `diagnose sys session list` | NAT اشتباه |
| IP Pool | Overload، One-to-One، Fixed Port Block | NAT IP در Capture | Pool مصرف‌شده |
| VIP/Port Forward | DNAT + Policy | از Client خارجی تست | VIP بدون Policy |
| Hairpin NAT | داخلی به VIP | تست از LAN | Reply مستقیم |
| Session Table | State، Timeout، Clear | `diagnose sys session filter …` | Session exhaustion |
| Policy Troubleshooting | روش ۶ مرحله‌ای | `diagnose debug flow` | — |

## ۱۶.۳ Security Profiles (W11)

| Feature | وابستگی | راه‌حل آموزشی در صورت نبود لایسنس FortiGuard `Unverified` 🔎 |
|---|---|---|
| Antivirus | FortiGuard AV | تست با EICAR + Local Signature محدود؛ توضیح مفهومی Engine/Proxy-vs-Flow |
| IPS | FortiGuard IPS | Custom IPS Signature محلی + Log؛ DoS Policy (محلی) |
| Web Filter | FortiGuard Rating | Static URL Filter + FQDN/Wildcard + Web Rating Override |
| DNS Filter | FortiGuard | Static Domain Filter + Local DNS Sinkhole |
| Application Control | FortiGuard App DB | بسته به DB موجود در VM؛ در صورت نبود → Port-based + مفهوم |
| File Filter | بدون FortiGuard (بسیاری موارد) | آزمایش با نوع فایل |
| SSL/SSH Inspection | CA/Certificate | Certificate-Inspection در برابر Deep-Inspection؛ Import CA به Windows Client از Windows CA |
| Logging/Analysis | — | Log Traffic/UTM در FortiGate محلی |

> **نکته مهم:** درس شامل «چرا Deep Inspection مشکل ایجاد می‌کند»: Pinning، Mobile Apps، Trust Store، Performance، حریم خصوصی/قانون.

## ۱۶.۴ Authentication (W12)

| مبحث | Lab | Verification | خراب |
|---|---|---|---|
| Local User/Group | Policy با User Group | `diagnose firewall auth list` | Group اشتباه |
| LDAP/AD | Bind DN، Base DN، LDAPS (CA) | `diagnose test authserver ldap` | Bind Fail، Cert Trust |
| RADIUS/NPS | Shared Secret، Attributes، Network Policy | `diagnose test authserver radius …` | Secret Mismatch/Client ثبت نشده |
| FSSO | Collector Agent (Windows) — `Unverified` دسترسی دانلود | `diagnose debug authd fsso list` | Collector/Port/Group |
| Captive Portal | Guest/User | تست مرورگر | Redirect/HTTPS |
| Authentication Policy | Identity-based Policy | Log User | Fallback |
| Certificate Auth | در صورت پشتیبانی/زمان | — | Expiry/CRL |

## ۱۶.۵ VPN (W13–W14)

| مبحث | Lab | Verification | خراب |
|---|---|---|---|
| IPsec Site-to-Site Route-Based | HQ↔BR1 با Cisco داخلی | `diagnose vpn tunnel list`, `get vpn ipsec tunnel summary` | Proposal Mismatch، PSK، Selectors |
| Policy-Based در برابر Route-Based | مقایسه نظری + Lab ساده | — | — |
| Phase 1/2، IKEv1/v2، Proposal | Hands-on | `diagnose debug application ike -1` (با احتیاط) | Mismatch |
| Routing/Policy برای VPN | Static/OSPF روی Tunnel | `get router info routing-table` | Tunnel UP ولی Traffic Block |
| NAT-T / DPD | WAN پشت NAT | Capture UDP 500/4500 | NAT-T غیرفعال |
| Remote Access | **SSL VPN (7.0.3)** — Web/Tunnel mode؛ `Unverified` نیاز FortiClient، محدودیت‌ها، **آسیب‌پذیری‌های شناخته‌شده در این نسخه → فقط Lab**؛ Dial-up IPsec (جایگزین) | اتصال از Windows Client | Cert، Split-Tunnel، Routing |
| Multi-Site / Backup Path | Hub-Spoke، Dual Tunnel | Failover | — |

## ۱۶.۶ Advanced (W15–W16)

| مبحث | Lab | Verification | وابستگی/محدودیت |
|---|---|---|---|
| SD-WAN | Members، Health-Check (Performance SLA)، Rule | `diagnose sys sdwan …` `Unverified` مسیر دقیق CLI 7.0.3 | تفاوت GUI نسخه‌ها |
| Link Monitor / Failover | Dual-WAN | Failover ≤ هدف | — |
| HA Active-Passive | FGCP، Heartbeat، Monitor Interface، Session Pickup | `get system ha status` | `Unverified` لایسنس Eval/HA در VM 🔎 |
| VDOM | فقط مفهومی ([OPT] عملی) | — | `Unverified` تعداد VDOM در VM Eval |
| OSPF/BGP | Interop با Cisco | `get router info ospf neighbor` | `Unverified` Feature set |
| DoS Policy | Anomaly Threshold در Lab | Log | — |
| FortiView/Logging | تحلیل Log | — | `Unverified` ممکن است محدود |

## ۱۶.۷ مدیریت متمرکز (W16 — مشروط)

| محصول | Lab ایده‌آل | محدودیت | جایگزین آموزشی |
|---|---|---|---|
| FortiManager | Device Manager، Policy Package، Install | `Unverified` منابع (VM سنگین)، لایسنس Eval، سازگاری نسخه با 7.0.3 | **مفهومی + Demo/مستند رسمی** + مدیریت تغییر با Git+CLI |
| FortiAnalyzer | Log Collection، Event/Report | `Unverified` منابع/لایسنس | rsyslog + Zabbix + FortiGate Local Log |

🔎 `Unverified` (Discovery) اگر RAM/لایسنس نبود، این بخش «مفهومی + حداقل Lab» می‌شود، نه «حذف».

---


## ۱۶.۸ Feature / Licensing / Dependency Matrix (FortiOS 7.0.3 — FortiGate-VM)

> **هیچ ویژگی یا محدودیت لایسنس بدون سند رسمی نسخه‌محور قطعی اعلام نشده است.** در این مرحله منبع رسمی نسخه 7.0.3 به‌صورت کامل بررسی نشد؛ ستون «وضعیت» برای همه `Unverified` است مگر خلاف آن ذکر شود. «جایگزین آموزشی» **معادل کامل** قابلیت اصلی نیست و تفاوت آن صریح ذکر شده است.

| Feature | هدف آموزشی | نیازمندی نسخه | نیازمندی لایسنس/Subscription | محدودیت احتمالی FortiGate-VM | روش بررسی/آزمایش | وضعیت | جایگزین آموزشی (و تفاوت با اصلی) |
|---|---|---|---|---|---|---|---|
| Firewall Policy/NAT/VIP | هسته دوره | 7.0.3 | بدون Subscription (فرض) | سقف Interface/Policy؟ | IV-5 + Policy ساخت | `Unverified` | — (کامل) |
| Routing Static/OSPF/BGP | Interop | 7.0.3 | بدون Subscription (فرض) | — | IV-5 | `Unverified` | — |
| Antivirus (FortiGuard) | آموزش AV Profile | 7.0.3 | **FortiGuard AV** | نبود Update با Eval/ایزوله | تست EICAR + وضعیت DB (`get system status`/GUI) | `Unverified` | **مفهومی + EICAR/Log**؛ تفاوت: Signature DB واقعی/به‌روز ندارد |
| IPS (FortiGuard) | آموزش IPS | 7.0.3 | **FortiGuard IPS** | همان | تست Signature/Log | `Unverified` | Custom IPS Signature محلی؛ تفاوت: بدون DB رسمی/به‌روز، پوشش محدود |
| Web Filter | آموزش Filtering | 7.0.3 | **FortiGuard Web Filtering** | Rating نیازمند اینترنت/Subscription | تست Category | `Unverified` | Static URL/FQDN/Wildcard + Override؛ تفاوت: بدون Category Rating |
| DNS Filter | آموزش | 7.0.3 | FortiGuard | همان | تست | `Unverified` | Static Domain Filter؛ تفاوت: بدون DB دامنه |
| Application Control | آموزش | 7.0.3 | FortiGuard App DB | DB داخلی/Update؟ | تست دسته App | `Unverified` | Port-based Policy + مفهومی |
| File Filter | آموزش | 7.0.3 | احتمالاً بدون Subscription | — | تست نوع فایل | `Unverified` | — |
| SSL/SSH Inspection | CA/Trust | 7.0.3 | بدون Subscription (فرض) | Performance | IV-5 + تست CA | `Unverified` | — |
| SSL VPN (Web/Tunnel) | RA-VPN | 7.0.3 | بدون Subscription (فرض) | Client (FortiClient)، **آسیب‌پذیری‌های Verified در این نسخه** | IV-5 + اتصال Client | `Unverified` (وجود Feature)؛ آسیب‌پذیری: `Verified` | Dial-up IPsec؛ تفاوت: کلاینت/پروتکل |
| IPsec S2S/Dial-up | VPN | 7.0.3 | بدون Subscription (فرض) | — | IV-5 | `Unverified` | — |
| SD-WAN | WAN | 7.0.3 | بدون Subscription (فرض) | — | IV-5 | `Unverified` | Static+Link Monitor؛ تفاوت: بدون Rule/SLA یکپارچه |
| HA (FGCP) | افزونگی | 7.0.3 | **لایسنس هر Node** | **ممکن است در Eval ممنوع/محدود** | IV-5: `config system ha` | `Unverified` | **مفهومی + Tabletop**؛ تفاوت: بدون Failover واقعی |
| VDOM | Multi-Tenancy | 7.0.3 | تعداد پیش‌فرض/لایسنس | سقف VDOM در Eval | `config system global` (مشاهده) | `Unverified` | مفهومی (**[OPT]**) |
| FortiView/Logging | تحلیل | 7.0.3 | Log محلی (Disk)/FAZ | Disk کوچک VM | IV-5 | `Unverified` | rsyslog + Zabbix |
| FortiManager | مدیریت | سازگار با 7.0.3؟ | **لایسنس FMG** | منابع | Registration | `Unverified` | مفهومی/Demo مستند |
| FortiAnalyzer | لاگ | همان | **لایسنس FAZ** | منابع | Registration | `Unverified` | rsyslog/Zabbix |

> **قاعده بررسی:** هر ردیف تا ثبت منبع رسمی (Release Notes / Administration Guide نسخه 7.0.3 / مستند VM) و/یا نتیجه IV-5، `Unverified` می‌ماند.

## ۱۶.۹ Lifecycle، Patch و Vulnerability Management (مبحث عملیاتی)

- **چرا 7.0.3 فقط در Lab:** `Verified`: CVE-2022-40684 (7.0.0–7.0.6)، CVE-2022-42475 (7.0.0–7.0.8)، CVE-2023-27997 (7.0.0–7.0.11) — فصل ۳۴.
- **Lab ایزوله:** هیچ مدیریتی/SSL-VPN/Port Forward از اینترنت؛ Management فقط از Jump/Mgmt-VLAN.
- **درس W9/W19 (Lifecycle):** (۱) Inventory نسخه‌ها؛ (۲) PSIRT Subscription؛ (۳) Risk-Rating؛ (۴) مسیر ارتقا طبق Release Notes (`Unverified` مسیر دقیق 7.0.3→بالاتر)؛ (۵) Backup قبل از Upgrade؛ (۶) Test Plan + Rollback Firmware؛ (۷) Post-Upgrade Verification.
- **آموزش ≠ توصیه Production:** هنرجو یاد می‌گیرد «چه نسخه‌ای را نباید Production کرد و چرا».
- **Lab Exercise:** مقایسه Advisory ها با نسخه Lab و تهیه «Vulnerability Assessment Memo» یک‌صفحه‌ای.

# ۱۷. Cisco + FortiGate Integration

## ۱۷.۱ اصل طراحی

دو فناوری یک معماری واحدند. **در هر توپولوژی مالک Gateway و نقطه اجرای Policy باید صریح باشد.** برای حذف ابهام، دو الگو جدا تعریف می‌شود (۱۷.۲).

## ۱۷.۲ دو الگوی Gateway — تصمیم آموزشی و حدود مالکیت

> **هر توپولوژی دقیقاً یک الگو دارد.** ترکیب مبهم ممنوع. **الگوی اصلی Capstone = الگوی B (FortiGate Gateway)**؛ الگوی A به‌صورت **Lab مستقل** (Lab A) آموزش داده می‌شود. تفاوت‌ها:

| جنبه | **Lab A:** Cisco L3 Core = Gateway، FGT = Perimeter | **Lab B / Capstone:** FGT = Gateway همه VLANها، Cisco = L2 |
|---|---|---|
| Default Gateway هر VLAN | SVI روی Core (HSRP در Lab A-HA) | VLAN Sub-interface روی FGT |
| Inter-VLAN Routing | Core (L3 Switch) | FGT |
| FGT کجاست؟ | بین Core و ISP؛ Transit /30 یا VLAN Transit | مرکز شبکه، Trunk به Core/Access |
| Policy بین VLANها | **Cisco ACL (Stateless)** | **FGT Policy (Stateful، UTM، Identity، Log)** |
| Policy Internet/DMZ | FGT | FGT |
| Routing Cisco↔FGT | Static یا OSPF (Core↔FGT) | Static/Default روی FGT؛ Cisco فقط Mgmt Default |
| NAT/VIP | FGT (مالک) | FGT (مالک) |
| Return Path | باید روی Core به FGT برای Default و روی FGT Route شبکه‌های داخلی | ساده (تک‌Hop) |
| Asymmetric Risk | بالاتر (Dual Core/Dual WAN) | پایین‌تر (تنها در Dual-WAN/HA/VPN) |
| Troubleshooting | Cisco + FGT هر دو | بیشتر در FGT (Debug Flow) |
| مزیت | مهارت L3 Cisco عمیق، مقیاس‌پذیر، رایج در Campus | Policy/Logging واحد، Segmentation ساده، Capstone امن‌تر |
| محدودیت | East-West بدون Inspection | بار روی FGT، Single Choke Point |
| امنیت | ACL Stateless؛ ریسک Policy گسترده | Least Privilege قوی‌تر |

**توجیه انتخاب B برای Capstone:** (۱) هدف دوره «زیرساخت شبکه و **امنیت** سازمانی» و Policy Matrix بین VLANها است؛ (۲) نقطه اجرای Policy و Log یکی است؛ (۳) Asymmetric Routing کمتر؛ (۴) عیب‌یابی با Debug Flow یکنواخت؛ (۵) مهارت L3 Cisco در Lab A و در Cisco ISP/WAN-Sim و در Spiral حفظ می‌شود (فصل ۲۸).

### ۱۷.۲.۱ Lab A — Cisco L3 Core Gateway + FortiGate Perimeter (W6/W10/W16؛ مستقل از Capstone)

| بخش | شرح |
|---|---|
| هدف یادگیری | SVI/Inter-VLAN، OSPF با FGT، HSRP، ACL، تفاوت Stateless/Stateful، Return Path |
| توپولوژی | VLAN10/20/50 → Access → `LabA-CORE-SW1/2` (SVI + HSRP) → روتد P2P `/30` → `LabA-FGT-01` → ISP-Sim |
| Gateway هر VLAN | **Cisco Core (HSRP Virtual IP `.254`)** |
| Policy | East-West: ACL روی SVI؛ North-South و DMZ: FGT |
| Packet Flow | Client→Access→Core(SVI)→(Route)→FGT→NAT→ISP؛ بازگشت: ISP→FGT→Core (Route داخلی روی FGT) |
| Return Path | FGT Static/OSPF به Subnetهای VLAN از طریق Core؛ Core Default به FGT |
| ملاحظات امنیتی | ACL بین VLANها، Mgmt Plane، FGT Policy Internet |
| سناریوهای TS | TS09، TS15–TS16، TS17–TS20، TS21، TS23 |
| محدودیت | East-West بدون UTM؛ Image: SVI/HSRP نیازمند تأیید IV-3 |

```mermaid
flowchart LR
    PC[PC VLAN10/20/50] --- ACC[LabA-ACC-SW1]
    ACC ---|Trunk| COREA[LabA-CORE-SW1 SVI+HSRP]
    ACC ---|Trunk| COREB[LabA-CORE-SW2 SVI+HSRP]
    COREA ---|Routed /30 OSPF| FGT[LabA-FGT-01 Perimeter]
    COREB ---|Routed /30 OSPF| FGT
    FGT --- ISP[ISP-Sim]
    FGT --- DMZ[DMZ]
```

### ۱۷.۲.۲ Lab B — FortiGate Gateway + Cisco Access/Switching (W10، معماری اصلی Capstone)

| بخش | شرح |
|---|---|
| هدف یادگیری | VLAN Sub-interface روی FGT، Zone/Policy، Segmentation، Debug Flow، Log |
| توپولوژی | VLANها → Access (L2) → Core (L2) → Trunk (یا LACP، `Unverified`) → `HQ-FGT-01` → ISP-Sim |
| Gateway هر VLAN | **FortiGate** |
| Policy | همه East-West و North-South در FGT |
| Packet Flow | Client→Access→Core→FGT Sub-if (Policy+UTM)→(Route)→ مقصد؛ بین دو VLAN: ورود/خروج از **همان** Trunk با Hairpin (VLAN تگ متفاوت) |
| Return Path | یک Hop L3 → متقارن |
| ملاحظات امنیتی | Trunk Allowed محدود، Native=99، DHCP Snooping/DAI در Cisco |
| TS | TS03–TS05، TS24، TS26، TS27، TS28 |
| محدودیت | Single Choke Point؛ ظرفیت Throughput VM |

```mermaid
flowchart TB
    subgraph HQ[HQ — معماری اصلی]
        PC[Users VLAN10–60] --- ACC[HQ-ACC-SW1/2 - L2]
        ACC ---|Trunk 802.1Q| CORE[HQ-CORE-SW1/2 - L2 Only]
        CORE ---|Trunk allowed 10,20,30,40,50,60,80,100| FGT[HQ-FGT-01/02 Gateway + Policy]
    end
    FGT ---|WAN1| ISP1[ISP1-R1]
    FGT ---|WAN2| ISP2[ISP2-R1]
    FGT ---|IPsec| BR[BR1..BR3 FGT]
```

### ۱۷.۲.۳ Packet Flow معماری اصلی

```mermaid
sequenceDiagram
    participant PC as HQ-CL1 (VLAN50)
    participant ACC as HQ-ACC-SW1 (L2)
    participant CORE as HQ-CORE-SW1 (L2)
    participant FGT as HQ-FGT-01 (GW .1)
    participant DNS as HQ-DC1 (VLAN60)
    participant WEB as Web (DMZ/Internet-Sim)
    PC->>ACC: ARP/TCP to GW MAC (VLAN50 untagged)
    ACC->>CORE: 802.1Q tag 50
    CORE->>FGT: Trunk (tag 50)
    FGT->>DNS: Policy USERS→SRV (DNS) via VLAN60 sub-if
    FGT->>WEB: Policy USERS→WAN + SNAT (FGT owns NAT)
    WEB-->>FGT: Return (session match)
    FGT-->>PC: Reverse NAT, tag 50
```

## ۱۷.۳ نقش‌ها بر حسب لایه (Capstone)

| لایه | Cisco | FortiGate |
|---|---|---|
| Access (L2) | VLAN، Port-Security، Snooping/DAI، STP | — |
| Core (L2) | Trunk/EtherChannel، STP Root | — |
| L3 + Gateway + Policy | — (Mgmt SVI فقط) | **همه** |
| WAN/ISP-Sim | **Cisco Router: OSPF/Static/IP SLA، ACL** | SD-WAN/Policy |
| NAT | — | **مالک NAT/VIP** |

## ۱۷.۴ ۱۵ سناریوی الزامی (با تعیین الگو)

> برچسب الگو: **[A]** Cisco Gateway، **[B]** FGT Gateway، **[N/A]** مستقل از Gateway. در هر سناریو مالک Gateway و نقطه Policy مشخص است.

| # | سناریو | الگو | مالک Gateway / نقطه Policy | نقش Cisco | نقش FGT | مسیر Packet کلیدی | تست | خرابی نمونه | هفته |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Access Switch + FGT Gateway | **B** | FGT / FGT | L2 Access/Trunk | Gateway VLANها | PC→Access→Trunk→FGT→Policy→WAN | Policy Hit | TS04 | W10 |
| S2 | L3 Switch Inter-VLAN + FGT Internet GW | **A** | Core / ACL (E-W) + FGT (N-S) | SVI + Default به FGT | Internet GW + NAT | PC→SVI→/30→FGT→NAT→ISP | Internet-Sim | TS16 | W10 |
| S3 | Router-on-a-Stick + Policy | **A (Router GW)** | Cisco Router / ACL + FGT | RoAS | Perimeter Policy | PC→RoAS→FGT→ISP | Allow/Deny | TS03 | W10 |
| S4 | VLAN Trunk Switch↔FGT | **B** | FGT / FGT | Trunk | VLAN Interface | Tag روی لینک | Sniffer | TS05 | W10 |
| S5 | Route-Based IPsec بین ۲ سایت | N/A | FGT هر سایت | L2 داخل/ISP-Sim | VTI | HQ→Tunnel→BR | Capture ESP | TS33–TS34 | W13 |
| S6 | OSPF Cisco↔FGT | **A** | Core / — | OSPF Core | OSPF Neighbor | Route Exchange | Table | TS17–TS18 | W15 |
| S7 | Static Routing + Return Path | N/A | هر دو | Static | Static | رفت/برگشت | traceroute | TS15–TS16 | W5/W10 |
| S8 | ACL Cisco در برابر Policy FGT | A+B مقایسه | — | ACL | Policy | — | Hit Count | TS21، TS24 | W10 |
| S9 | NAT Cisco در برابر FGT (Double NAT) | N/A | FGT=مالک NAT | NAT (مقایسه فقط) | NAT | Capture Pre/Post | تک‌NAT | TS23 | W10 |
| S10 | Dual WAN + Failover | N/A | FGT | ISP-Sim×2 + IP SLA | SD-WAN/Link-Monitor | Failover | قطع ISP1 | TS43 | W15 |
| S11 | HA FGT + Switch Redundancy | **B** | FGT Cluster | Dual Switch + EC/STP | FGCP | Failover Session | قطع Primary | TS44 | W16 |
| S12 | DMZ و تفکیک سرور | **B** | FGT | VLAN 100 Trunk | DMZ + VIP | Internet→VIP→Web | تست خارجی | TS27 | W11 |
| S13 | Authentication با AD | N/A | FGT | — | LDAP/NPS/FSSO | User→FGT→AD | Log User | TS37–TS40 | W12 |
| S14 | Centralized Logging/Monitoring | N/A | — | Syslog/SNMP | Syslog/SNMP | Log→rsyslog→Zabbix | Dashboard | TS45–TS47 | W17 |
| S15 | Packet Flow End-to-End | **B** | FGT | همه | همه | Capture ۵ نقطه | PA18 | TS50 | W18 |

### ۱۷.۴.۱ نمودارهای Archetype (B: IPsec و C: HA/Dual WAN)

```mermaid
flowchart LR
    HQLAN[HQ LAN 10.10.0.0/16] --- HQFGT[HQ-FGT-01]
    HQFGT ===|IPsec Route-Based VTI| BR1FGT[BR1-FGT-01]
    BR1FGT --- BR1LAN[BR1 LAN 10.20.0.0/16]
    HQFGT --- ISP[(ISP Sim - Cisco)]
    BR1FGT --- ISP
```

```mermaid
flowchart TB
    FGTA[HQ-FGT-01 Active] --- FGTB[HQ-FGT-02 Standby]
    FGTA ---|HA Heartbeat| FGTB
    SW1[Core SW1] --- FGTA
    SW2[Core SW2] --- FGTB
    FGTA --- ISP1
    FGTA --- ISP2
    FGTB --- ISP1
    FGTB --- ISP2
```

> **قانون Capture:** در S15 در ۵ نقطه Capture گرفته می‌شود: NIC Client، Access→Core، Core→FGT، FGT WAN، Server.

# ۱۸. Windows Server، AD، DNS، DHCP و RADIUS

## ۱۸.۱ نگاشت VM ← سناریو

| VM | چرا لازم است | منابع پیشنهادی `Unverified` | محل نصب | اتصال | هفته |
|---|---|---|---|---|---|
| Win Server 2022 (DC1) | AD DS، DNS، DHCP، NPS، PKI | 2 vCPU / 4 GB / 60 GB | (الف) QEMU در PNetLab یا (ب) ESXi — فصل ۱۰.۲ | VLAN Servers | W4، W12 |
| Win Server 2022 (SRV2 optional) | CA/NPS جدا یا Collector | 2 / 2–4 / 40 | همانند بالا | Servers | W12 |
| Win Client 10/11 (CL1,CL2) | Domain Join، Policy Test، Capture | 2 / 4 / 50 | همانند بالا | Users VLAN | W12–W22 |
| Ubuntu/Debian Server (WEB-DMZ) | Web Server DMZ | 1 / 1 / 15 | همانند بالا | DMZ | W11 |
| Linux (SYSLOG/MON) | rsyslog + Zabbix | 2 / 4 / 60 | همانند بالا | Mgmt/Servers | W17 |
| Linux Tools (KALI-LITE/utility) | Nmap/tcpdump در Lab | 1 / 2 / 20 | همانند بالا | Test VLAN | W19 |

> Win11 نیازمند TPM/Secure Boot است؛ پیشنهاد: Windows 10 Eval یا پیکربندی VM مطابق مستند مایکروسافت `Unverified`.

## ۱۸.۲ Windows Server — محتوا (فقط آنچه شبکه نیاز دارد)

| مبحث | Lab | تست/Verification |
|---|---|---|
| نصب VM و تنظیم IP/DNS | Static IP، Hostname | `ipconfig /all`, `Test-NetConnection` |
| DNS/DHCP | Scope، Reservation، Option 003/006 | `ipconfig /renew`، Capture DORA |
| AD DS | Forest/Domain، OU، Users/Groups | `dcdiag`, `nltest` |
| Domain Join | Client به Domain | Login دامنه‌ای |
| GPO (حد نیاز) | Windows Firewall، CA Trust Distribution | `gpresult /r` |
| LDAP/LDAPS | Bind Account، Certificate | `ldp.exe` / FortiGate test |
| NPS/RADIUS | Client (FortiGate)، Network Policy | Event Viewer (۶۲۷۲/۶۲۷۳) |
| AD CS / PKI | Root/Issuing CA (Lab: Enterprise Root تک‌لایه) | Cert Template، توزیع CA |
| Windows Firewall | Rule مدیریتی | Block/Allow تست |
| Event Viewer / Logging | Security Log، Forward (Optional) | Event ID 4624/4625 |

## ۱۸.۳ Windows Client

نصب، IP/DNS، Domain Join، تست Policy، ابزارها (`ping`, `tracert`, `pathping`, `nslookup`, `netstat`, `Test-NetConnection`)، Wireshark، FortiClient (VPN)، تست Auth.

# ۱۹. Linux و سرویس‌های زیرساختی

## ۱۹.۱ Linux — محتوا

| مبحث | Lab |
|---|---|
| نصب و Netplan/NetworkManager | Static IP/VLAN Sub-if |
| Routing/DNS | `ip route`, `systemd-resolved`/`bind9` اختیاری |
| SSH | Key-based، `sshd_config` Hardening |
| Web DMZ | nginx/apache + TLS |
| Linux Firewall | `nftables`/`ufw` |
| Syslog | `rsyslog` Receiver (UDP/TCP 514) + Filtering |
| ابزار | `ping`, `traceroute`, `curl`, `dig`, `ss`, `tcpdump`, `mtr` |

---

# ۲۰. VPN، Branch Connectivity و SD-WAN

> جزئیات Curriculum در فصل ۱۶.۵–۱۶.۶ است؛ این فصل **طراحی Branch و WAN** را برای Capstone تعریف می‌کند. همه Featureها تا Image Validation `Unverified` هستند.

## ۲۰.۱ مدل اتصال شعب (Hub-and-Spoke)

| سایت | نقش | WAN | Underlay | Overlay | مسیر داخلی |
|---|---|---|---|---|---|
| HQ | Hub | ISP1 (`203.0.113.0/24` Sim) + ISP2 (`198.51.100.0/24` Sim) | ISP-Sim Cisco | IPsec VTI به هر Branch | Static/OSPF روی VTI |
| BR1 | Spoke | ISP1 | ISP-Sim | VTI → HQ | Local VLAN 10/50/60/80 |
| BR2 | Spoke | ISP1 (+ISP2 اختیاری) | ISP-Sim | VTI → HQ | VLAN 10/50/80 |
| BR3 | Spoke | ISP2 | ISP-Sim | VTI → HQ | VLAN 10/50/80 |

> بین Branchها ترافیک از HQ (Hub) عبور می‌کند؛ Spoke-to-Spoke مستقیم **[OPT]**.

## ۲۰.۲ VPN Matrix (الگو)

| Tunnel | Peer A | Peer B | IKE | Phase1/2 | Selector | Routing | Policy |
|---|---|---|---|---|---|---|---|
| VPN-HQ-BR1-1 | HQ-FGT-01 WAN1 | BR1-FGT-01 WAN | IKEv2 (`Unverified` پشتیبانی) | AES256-SHA256 / DH ۱۴+ (نمونه؛ تأیید در Lab) | 0.0.0.0/0 (Route-Based) | OSPF/Static روی VTI | HQ↔BR1 Matrix |
| VPN-HQ-BR2-1 | همان | BR2-FGT-01 | همان | همان | همان | همان | همان |
| VPN-HQ-BR3-1 | همان | BR3-FGT-01 | همان | همان | همان | همان | همان |
| VPN-HQ-BR1-2 (Backup) | HQ WAN2 | BR1 | همان | همان | همان | Metric/Priority بالاتر | همان |

## ۲۰.۳ Remote Access

| مورد | طراحی |
|---|---|
| روش اول | Dial-up IPsec (FortiClient) — `Unverified` |
| روش دوم | SSL VPN (7.0.3) — **فقط Lab ایزوله به‌دلیل آسیب‌پذیری‌های Verified**؛ Web-mode/Tunnel-mode `Unverified` |
| Pool | `10.250.0.0/24` |
| Auth | AD/LDAP + MFA (در صورت امکان/لایسنس `Unverified`) |
| Policy | Least Privilege: فقط سرویس‌های مشخص |
| Return Route | Route Pool روی FGT؛ در Lab A روی Core |

## ۲۰.۴ SD-WAN Design

| مورد | طراحی |
|---|---|
| Members | WAN1، WAN2 (و تونل‌های VPN به‌عنوان Member **[OPT]**) |
| Health-Check | Target داخل ISP-Sim (ICMP/HTTP) با Threshold Latency/Loss |
| Rules | Business-Critical → Lowest-Latency؛ Default → Cost/Priority |
| Failover | زیر ۳۰ ثانیه هدف (`Unverified`) |
| ریسک Asymmetric | Return Route در ISP-Sim همسو؛ Sticky Session |
| Verification | `diagnose sys sdwan …` (`Unverified` سینتکس 7.0.3)، Capture |
| Fallback | Static + Link-Monitor |

# ۲۱. Security، Segmentation و DMZ

## ۲۱.۱ موضوعات و Labهای Blue Team (Lab ایزوله، دفاعی)

> **همه در Lab ایزوله؛ هدف دفاع و یادگیری. ممنوع: اسکن/حمله به شبکه واقعی، استفاده از ابزار مخرب.**

| موضوع | Lab | Verification |
|---|---|---|
| Segmentation | Zone×Zone Matrix | Test Allow/Deny |
| Least Privilege | RBAC FGT/Cisco/AD | Login محدود |
| Management Plane | SSH/HTTPS، Trusthost، Mgmt VLAN، Disable Telnet/HTTP | Port Scan داخلی Lab |
| ACL + Policy | Edge ACL + FGT | Hit Count |
| IPS/Profiles | Custom IPS (محلی) | Log |
| Web/App Control | Static URL | Log |
| DNS Security | DNS Filter (مشروط) | — |
| DMZ Hardening | Least Port، Linux `nftables`، TLS | `nmap` از Lab |
| VPN Security | Strong Proposal، MFA مشروط، DPD، Split-Tunnel ریسک | Capture |
| Certificate/TLS | CA، Expiry | — |
| Incident Investigation | از Log تا Timeline | Report |
| Port Scan Detection | `nmap` از VM Lab → Detect (IPS/Log/Zabbix) | Alert |
| Unwanted Service | `ss -tulpn`, `nmap` Inventory | لیست |
| Traffic Anomaly | Baseline | — |
| Hardening Baselines | Cisco/FGT checklist (مثلاً CIS/Vendor Guide `Unverified`) | Audit Score |
| Backup Protection | رمزگذاری Backup، دسترسی Git | — |
| **Patch/Firmware Management** | مطالعه موردی CVEهای FortiOS 7.0.x `Unverified` → چرا 7.0.3 Exposed ممنوع است | Policy |

---

## ۲۱.۲ مدل Zone و Segmentation (Capstone)

Zoneها: `Z-MGMT، Z-FIN، Z-HR، Z-IT، Z-USERS، Z-SRV، Z-GUEST، Z-DMZ، Z-WAN`؛ Matrix در فصل ۲۹.۵. اصول: Default-Deny بین Zoneها؛ Least Privilege؛ مدیریت فقط از Z-MGMT/Z-IT؛ DMZ بدون دسترسی آزاد به Z-SRV؛ Guest ایزوله؛ همه Policy با Log؛ Secure Management (SSH/HTTPS، Trusthost، MFA مشروط)؛ مدیریت Credential/Secret در Vault (نه Git).

# ۲۲. Monitoring، Logging و Alerting

## ۲۲.۱ مقایسه ابزارها و تصمیم

| ابزار | هزینه | منابع | پیچیدگی | محدودیت | مناسب Lab |
|---|---|---|---|---|---|
| **Zabbix** | رایگان | 2 vCPU/4 GB | متوسط | منحنی یادگیری Template | ✅ **اصلی** |
| **rsyslog (Central Syslog)** | رایگان | ناچیز | کم | UI ندارد | ✅ **اصلی (Syslog)** |
| LibreNMS | رایگان | 2/2–4 | کم (Auto-Discovery) | Syslog/Alert محدودتر از Zabbix | ✅ **جایگزین واحد** |
| PRTG | رایگان ≤۱۰۰ Sensor (`Unverified` تأیید) | Windows | کم | Windows-only | ❌ وارد نمی‌شود (تکراری) |
| FortiView | داخلی FGT | — | کم | محدود به FGT | ✅ بخشی از FGT |
| FortiAnalyzer | تجاری | `Unverified` سنگین | متوسط | لایسنس | مشروط |
| Wireshark | رایگان | — | — | — | ✅ تحلیل Packet |

**تصمیم ✅:** Stack = **Zabbix (SNMP/ICMP/Template) + rsyslog (Syslog Central) + FortiGate Local Log/FortiView + Wireshark**. جایگزین: LibreNMS. FAZ فقط در صورت امکان.

## ۲۲.۲ مباحث و ابزار

| موضوع | ابزار | Lab |
|---|---|---|
| SNMPv2c/v3 | Zabbix | v3 (authPriv) در مقابل v2c Risk |
| Syslog + NTP | rsyslog | Cisco/FGT/Windows/Linux → Central |
| Interface Util/Error | Zabbix | Graph + Alert |
| CPU/Memory | Zabbix | Threshold |
| Latency/Loss | Zabbix ICMP | Alert |
| Device Availability | Zabbix | Trigger |
| Link State/Error | SNMP Trap | Down Event |
| Routing Neighbor | Template/Script | OSPF Down |
| VPN Status | SNMP/Syslog FGT | Tunnel Down |
| Firewall Sessions | SNMP FGT | Session Count |
| Security Events | FGT Log → rsyslog | Failed Login |
| Retention/Backup | logrotate | ۹۰ روز |
| Baseline | Zabbix History | Anomaly |
| Correlation | rsyslog + Time | هم‌زمانی ۴ منبع |

## ۲۲.۳ سناریوهای مانیتورینگ (۱۰ مورد — L92)

قطع لینک · افزایش CPU · Interface Errors · قطع VPN · تغییر غیرمنتظره Routing · افزایش Drop · تلاش ورود ناموفق · افزایش Session · از دست رفتن Syslog · اختلاف ساعت.

---


## ۲۲.۴ Dashboardهای واقعی (W17)

| Dashboard | ویجت‌ها | منبع | مخاطب |
|---|---|---|---|
| Network Health | Up/Down دستگاه‌ها، Link State، Latency/Loss به Gateway/ISP | Zabbix ICMP/SNMP | NOC |
| Interface & Capacity | Utilization، Errors/Discards، Top Links | SNMP | شبکه |
| Firewall | Session Count، CPU/Mem FGT، Policy Deny Top، VPN Status | SNMP/Syslog FGT | امنیت |
| Security Events | Failed Login، Port-Scan Alert، Config Change | rsyslog | امنیت |
| Services | AD/DNS/DHCP/Web Availability (Port/HTTP Check) | Zabbix | IT |
| Time/Log Health | NTP Offset، Syslog Rate هر Source | Zabbix/rsyslog | عملیات |

## ۲۲.۵ طراحی Alert و Threshold

| اصل | قاعده |
|---|---|
| Severity | Info/Warning/Average/High/Disaster؛ فقط High+ تماس/Notification فوری |
| Threshold | مبتنی بر **Baseline** (Mean+Δ)، نه عدد حدسی؛ Hysteresis برای جلوگیری از Flap |
| Dependency | Trigger وابسته (Core Down ← خاموشی Alertهای پشت آن) |
| Time Window | شرط پایدار (مثلاً Loss>۵٪ برای ۵ دقیقه) |
| Owner/Runbook | هر Alert → Runbook (فصل ۳۳) |

### کاهش Noise (Alert Fatigue)
معیار: نسبت Alert Actionable ≥ ۸۰٪؛ Alertهایی که ۲ هفته بدون اقدام می‌مانند → حذف/اصلاح؛ Maintenance Window؛ Dedup؛ Review هفتگی (۳۰ دقیقه در روز R).

## ۲۲.۶ Syslog، SNMP و Flow Monitoring (در حد لازم)

| مبحث | حدود | Verified؟ |
|---|---|---|
| Syslog (UDP/TCP 514) | Cisco، FGT، Windows (Forwarder/NXLog **[OPT]**)، Linux | `Unverified` برای FGT 7.0.3 جزئیات |
| SNMP | v2c (فقط Lab)، v3 (authPriv) هدف | `Unverified` سینتکس |
| Flow (NetFlow/sFlow/IPFIX) | مفهومی + Lab اگر Image/FGT پشتیبانی کرد | `Unverified` |
| Capture | Wireshark/tcpdump برای تحقیق نقطه‌ای | — |

## ۲۲.۷ نگهداری و Rotation لاگ

| مورد | سیاست پیشنهادی (Lab) |
|---|---|
| Retention | ۹۰ روز قابل جستجو؛ Archive فشرده ۱۸۰ روز (Capacity-dependent) |
| Rotation | `logrotate` روزانه، فشرده‌سازی، حداکثر حجم |
| ظرفیت | محاسبه: Rate (MB/روز) × Retention؛ هشدار ۸۰٪ Disk |
| امنیت | دسترسی خواندنی محدود؛ Backup رمزگذاری‌شده |
| زمان | همه منابع با NTP (فصل ۲۲.۸) |

## ۲۲.۸ NTP و هم‌زمانی

| مورد | طراحی |
|---|---|
| منبع | NTP Server داخلی (`HQ-MON1` یا DC) |
| Clientها | همه Cisco/FGT/Windows/Linux |
| بررسی | Offset < ۱ ثانیه؛ Zabbix Item |
| Fault | TS46 |

## ۲۲.۹ Capacity Planning، Baseline و Health Check

| فعالیت | دوره | خروجی |
|---|---|---|
| Baseline عملکرد | هفته ۱۷ + بعد از Capstone | میانگین/پیک CPU، Session، Link Util |
| Capacity Report | ماهانه (Lab: هفتگی) | روند، پیش‌بینی ۳ ماه، Headroom |
| Health Check | روزانه/هفتگی | چک‌لیست: Backup، Log، Time، Disk، Cert Expiry، Firmware PSIRT |
| Review دوره‌ای | فصلی | Alert Tuning، Policy Review، Cert Review |

# ۲۳. Wireshark، tcpdump و Packet Analysis

## ۲۳.۱ ابزارها (فقط آنچه واقعاً قابل استفاده است)

| ابزار | محل | کاربرد | نکته |
|---|---|---|---|
| PNetLab Capture (Wireshark) | روی لینک بین Nodeها | Capture در Lab | ✅ ابزار اصلی |
| Wireshark (Windows Jump) | Jump | تحلیل `.pcap` | ✅ |
| tcpdump | Linux VM | سریع | ✅ |
| FortiGate Sniffer | `diagnose sniffer packet any '<filter>' 4 0 l` | روی خود FGT | ✅ |
| FortiGate Debug Flow | `diagnose debug flow …` | سیاست/NAT/Route | با `diagnose debug reset` |
| Cisco | `show`, `debug` (با احتیاط)، Embedded Packet Capture (EPC) `Unverified` پشتیبانی IOSv | محدود | `Unverified` |
| SPAN/RSPAN | IOSvL2 | Mirror | `Unverified` |

## ۲۳.۲ تمرین‌های Capture (۱۸ مورد)

| ID | موضوع | محل Capture | Display Filter | بسته‌های مهم | انتظار صحیح | نشانه خرابی | نتیجه‌گیری |
|---|---|---|---|---|---|---|---|
| PA01 | Ethernet Frame | NIC Client | `eth` | Header | MAC src/dst درست | Dst نامعتبر | مسیر L2 |
| PA02 | ARP | Client↔GW | `arp` | Req/Reply | Reply سریع | No Reply | ARP/VLAN |
| PA03 | VLAN Tag | Trunk | `vlan` | 802.1Q Tag | VLAN ID درست | Tag اشتباه/نبود | Trunk |
| PA04 | IPv4/IPv6 | Client | `ip`/`ipv6` | TTL، NS/NA | عادی | — | L3 |
| PA05 | ICMP/TTL | Hop‌ها | `icmp` | Echo، Time Exceeded | TTL افت | Unreachable | Routing |
| PA06 | TCP Handshake/Teardown | Client+Server | `tcp.flags.syn==1` | SYN, SYN/ACK, ACK | کامل | بدون SYN/ACK | Policy/Route |
| PA07 | UDP | Client | `udp` | — | — | — | — |
| PA08 | DHCP DORA | Client/Server | `dhcp` | DISCOVER..ACK | کامل | Discover بدون Offer | Relay/Snooping |
| PA09 | DNS | Client/DNS | `dns` | Query/Response | Response سریع | NXDOMAIN/Timeout | DNS/Policy |
| PA10 | HTTP/TLS Handshake | Client | `http`/`tls.handshake` | ClientHello، Cert | Handshake کامل | Alert | SSL Inspection |
| PA11 | Routing/TTL | Multi-hop | `ip.ttl` | TTL | — | Loop | Loop |
| PA12 | MTU/Fragmentation | Path | `ip.flags.mf==1`, `icmp.type==3` | Frag Needed | PMTUD OK | Black Hole | MSS Clamp |
| PA13 | Retransmission/RST | Client | `tcp.analysis.retransmission`, `tcp.flags.reset==1` | — | کم | زیاد | Loss/Policy |
| PA14 | IPsec | WAN | `isakmp`, `esp` | IKE، ESP | ESP دو طرفه | ESP فقط یک‌طرفه | Policy/Route |
| PA15 | NAT قبل/بعد | دو سمت FGT | host filter | Src IP | تبدیل | بدون NAT | NAT |
| PA16 | FW Allow/Deny | Ingress/Egress | — | Pkt رسید/نرفت | — | Ingress بله Egress نه | Policy Drop |
| PA17 | Drop/Partial Path | چند نقطه | — | — | — | قطع در Hop | محل مشکل |
| PA18 | Capture چندنقطه S15 | ۵ نقطه | — | — | هماهنگ | — | End-to-End |

---

## ۲۳.۳ tcpdump — فرمان‌های پایه (Linux)

```bash
sudo tcpdump -i eth0 -nn -s0 'host 10.10.50.20 and port 443' -w /tmp/c.pcap   # Capture با Filter
sudo tcpdump -i eth0 -nn icmp                                                   # فقط ICMP
sudo tcpdump -r /tmp/c.pcap -nn 'tcp[tcpflags] & tcp-syn != 0'                  # SYNها در فایل
```

`Unverified` تا اجرا در VM واقعی؛ Capture فقط در Lab مجاز و فایل‌ها بدون Credential نگهداری شوند.

# ۲۴. Troubleshooting Methodology

## ۲۴.۱ چارچوب ثابت (۱۵ مرحله)

1. تعریف دقیق Symptom (چه کسی، چه چیزی، از کی، تغییر اخیر؟)
2. جمع‌آوری اطلاعات و Scope (یک کاربر؟ یک VLAN؟ کل شعبه؟)
3. رسم مسیر End-to-End (Hop-by-Hop)
4. Physical/Link (Interface، Error، Duplex)
5. Layer 2 (VLAN، Trunk، MAC، STP)
6. IP و ARP (Mask، Gateway، Duplicate)
7. Routing و Return Path
8. ACL و Firewall Policy
9. NAT
10. DNS و سرویس
11. Packet Capture و Log Correlation
12. فرضیه‌سازی و آزمایش (یک تغییر در هر بار)
13. رفع با Change Control (Backup + Rollback)
14. Verification (از دید کاربر + Monitoring)
15. مستندسازی RCA و Preventive Action

> **قالب RCA یک‌صفحه‌ای:** Timeline، Impact، Root Cause، Contributing Factors، Fix، Verification، Preventive Action، Lesson.


## ۲۴.۲ Packet Flow و Debug Flow در FortiGate

| ابزار | کاربرد | نکته |
|---|---|---|
| `diagnose sniffer packet <if> '<filter>' 4 0 l` (`Unverified` سینتکس 7.0.3) | دیدن بسته روی Interface | ورودی/خروجی را جدا Capture کن |
| `diagnose debug flow filter …` / `trace start N` / `diagnose debug enable` | مسیر تصمیم: Route lookup، Policy-ID، NAT | **پس از کار:** `diagnose debug disable` + `diagnose debug reset` |
| `diagnose sys session list` / filter | وضعیت Session، NAT، Policy | بررسی Timeout/State |
| `diagnose firewall iprope lookup …` | کدام Policy Match می‌شود | |
| `get router info routing-table all` | Route انتخابی | AD/Priority |
| `get system status` | نسخه/لایسنس | |

### ۲۴.۲.۱ چرخه حیات Session (Session Lifecycle)
SYN → Policy Lookup → Session ایجاد (NAT) → Established → FIN/RST یا Timeout → Session حذف. **نشانه‌ها:** Session بدون Reply = مشکل Return/مقصد؛ Session نیست = Drop قبل از Policy (Route/RPF/Ingress).

## ۲۴.۳ تشخیص تفاوت Routing / Policy / NAT / سرویس مقصد

| علامت | Routing | Policy | NAT | سرویس مقصد |
|---|---|---|---|---|
| Debug Flow | `no route`/RPF fail | `denied by forward policy check`/Policy-ID=0 | NAT نشان داده نمی‌شود/Src اشتباه | Session برقرار ولی Reply/RST از مقصد |
| Sniffer | ورودی بله، خروجی نه | ورودی بله، خروجی نه | خروجی با Src اشتباه | SYN رفت، RST/بدون پاسخ |
| تست | `get router info routing-table` | Hit Count/Log | `session list` | از خود سرور `ss -tulpn` |

## ۲۴.۴ Return Path و Asymmetric Routing

| موضوع | روش |
|---|---|
| تشخیص | Capture هم‌زمان ورودی/خروجی؛ Sessionهای Half-open؛ RPF Drop |
| پیشگیری | یک Choke Point (معماری B)، Return Route همسو، SD-WAN Sticky، `show ip route`/`get router info routing-table` |
| Route Selection | Longest Prefix → AD/Priority → Metric |
| Management/Control/Data Plane | Management (SSH/SNMP/Syslog)، Control (OSPF/STP/IKE)، Data (کاربر)؛ عیب‌یابی را در **همان Plane** شروع کن |

## ۲۴.۵ MTU، MSS، Fragmentation و PMTUD
مسیر: Size-test (`ping -f -l`) → ICMP Frag-Needed → Capture TCP MSS → MSS Clamp/MTU. (TS31، PA12).

# ۲۵. ۵۰ Troubleshooting Runbooks

## ۲۵.۱ فهرست و توزیع

> ۵۰ سناریو از ساده (تک‌لایه) به دشوار (چندلایه/چندمحصولی). **Runbook ۲۱ فیلدی هر سناریو در پیوست A** است؛ ۱۰ سناریوی نماینده در ۲۵.۳ تفصیلی‌اند. حوزه‌های پوشش‌داده‌شده: VLAN، Trunk، STP، EtherChannel، Routing، OSPF، ACL، DHCP، DNS، NAT، Firewall Policy، VIP، VPN، MTU/MSS، Asymmetric Routing، HA، SD-WAN، AD/LDAP، RADIUS، PKI، DNS Resolution، Monitoring، Logging، Time/NTP، Packet Loss، Performance، Human-Error/Change Management. سناریوهای وابسته به Feature تأییدنشده (TS02، TS11، TS16 Debug Flow، TS40، TS43، TS44، TS48) `Unverified` هستند.

| ID | عنوان | حوزه/مهارت هدف | سطح | هفته | فایل‌های ثابت |
|---|---|---|---|---|---|
| TS01 | Interface Shutdown | Physical/Link | ★ | W3 | [Runbook → پیوست A](#appendix-a-ts01) |
| TS02 | Duplex/Speed Mismatch (امکان‌سنجی Unverified) | Physical/Link | ★★ | W3 | [Runbook → پیوست A](#appendix-a-ts02) |
| TS03 | VLAN اشتباه روی Access | VLAN | ★ | W3 | [Runbook → پیوست A](#appendix-a-ts03) |
| TS04 | Allowed VLAN حذف‌شده روی Trunk | Trunk | ★★ | W3 | [Runbook → پیوست A](#appendix-a-ts04) |
| TS05 | Human Error: جایگزینی Allowed List (Change Mgmt) | Trunk/Change | ★★ | W3 | [Runbook → پیوست A](#appendix-a-ts05) |
| TS06 | STP Loop / Broadcast Storm | STP | ★★★ | W4 | [Runbook → پیوست A](#appendix-a-ts06) |
| TS07 | Root Bridge اشتباه | STP | ★★ | W4 | [Runbook → پیوست A](#appendix-a-ts07) |
| TS08 | EtherChannel Mismatch | EtherChannel | ★★ | W4 | [Runbook → پیوست A](#appendix-a-ts08) |
| TS09 | SVI Down/Down (Lab A) | Inter-VLAN | ★★ | W3 | [Runbook → پیوست A](#appendix-a-ts09) |
| TS10 | DHCP Relay فراموش‌شده | DHCP | ★★ | W7 | [Runbook → پیوست A](#appendix-a-ts10) |
| TS11 | DHCP Snooping Untrusted Uplink | DHCP/L2 Security | ★★ | W4 | [Runbook → پیوست A](#appendix-a-ts11) |
| TS12 | Duplicate IP | ARP/IP | ★★ | W2 | [Runbook → پیوست A](#appendix-a-ts12) |
| TS13 | Subnet Mask اشتباه | IP | ★ | W2 | [Runbook → پیوست A](#appendix-a-ts13) |
| TS14 | Default Gateway اشتباه | IP | ★ | W2 | [Runbook → پیوست A](#appendix-a-ts14) |
| TS15 | Static Route با Next-Hop اشتباه | Routing | ★★ | W5 | [Runbook → پیوست A](#appendix-a-ts15) |
| TS16 | Asymmetric Routing (رفت ok، برگشت ندارد) | Asymmetric Routing | ★★★ | W5 | [Runbook → پیوست A](#appendix-a-ts16) |
| TS17 | OSPF MTU Mismatch | OSPF | ★★ | W5 | [Runbook → پیوست A](#appendix-a-ts17) |
| TS18 | OSPF Timer/Area/Auth Mismatch | OSPF | ★★ | W5 | [Runbook → پیوست A](#appendix-a-ts18) |
| TS19 | OSPF Cost/Reference-BW | OSPF | ★★★ | W6 | [Runbook → پیوست A](#appendix-a-ts19) |
| TS20 | HSRP Priority/Preempt | FHRP | ★★ | W6 | [Runbook → پیوست A](#appendix-a-ts20) |
| TS21 | ACL Extended ترتیب اشتباه | ACL | ★★ | W7 | [Runbook → پیوست A](#appendix-a-ts21) |
| TS22 | NAT Inside/Outside جابه‌جا | NAT | ★★ | W7 | [Runbook → پیوست A](#appendix-a-ts22) |
| TS23 | Double NAT | NAT | ★★★ | W10 | [Runbook → پیوست A](#appendix-a-ts23) |
| TS24 | FGT Policy: Interface/Service/Order | Firewall Policy | ★★ | W10 | [Runbook → پیوست A](#appendix-a-ts24) |
| TS25 | Packet Loss روی لینک WAN | Packet Loss/Performance | ★★★ | W15 | [Runbook → پیوست A](#appendix-a-ts25) |
| TS26 | Shadow Policy | Firewall Policy | ★★★ | W10 | [Runbook → پیوست A](#appendix-a-ts26) |
| TS27 | VIP بدون Policy | VIP/DNAT | ★★ | W11 | [Runbook → پیوست A](#appendix-a-ts27) |
| TS28 | Hairpin NAT | NAT | ★★ | W10 | [Runbook → پیوست A](#appendix-a-ts28) |
| TS29 | IP Pool/Central NAT | NAT | ★★ | W10 | [Runbook → پیوست A](#appendix-a-ts29) |
| TS30 | DNS Resolve Fail | DNS | ★★ | W12 | [Runbook → پیوست A](#appendix-a-ts30) |
| TS31 | MTU/MSS (PMTUD) | MTU/MSS | ★★★ | W13 | [Runbook → پیوست A](#appendix-a-ts31) |
| TS32 | VPN Phase1 Down | VPN | ★★ | W13 | [Runbook → پیوست A](#appendix-a-ts32) |
| TS33 | Phase2 Down | VPN | ★★ | W13 | [Runbook → پیوست A](#appendix-a-ts33) |
| TS34 | Tunnel UP ولی Traffic Block | VPN/Routing/Policy | ★★★ | W13 | [Runbook → پیوست A](#appendix-a-ts34) |
| TS35 | NAT-T Block | VPN | ★★ | W13 | [Runbook → پیوست A](#appendix-a-ts35) |
| TS36 | Tunnel Flap/DPD | VPN | ★★ | W13 | [Runbook → پیوست A](#appendix-a-ts36) |
| TS37 | LDAP Bind Fail | AD/LDAP | ★★ | W12 | [Runbook → پیوست A](#appendix-a-ts37) |
| TS38 | LDAPS Certificate Trust | AD/PKI | ★★★ | W12 | [Runbook → پیوست A](#appendix-a-ts38) |
| TS39 | RADIUS Reject | RADIUS | ★★ | W12 | [Runbook → پیوست A](#appendix-a-ts39) |
| TS40 | FSSO/Group Mapping | AD/Identity | ★★★ | W12 | [Runbook → پیوست A](#appendix-a-ts40) |
| TS41 | Deep Inspection CA غیرمعتمد | PKI/SSL | ★★★ | W11 | [Runbook → پیوست A](#appendix-a-ts41) |
| TS42 | Certificate منقضی/Time Skew | PKI/Time | ★★ | W12 | [Runbook → پیوست A](#appendix-a-ts42) |
| TS43 | SD-WAN Health-Check | SD-WAN | ★★★ | W15 | [Runbook → پیوست A](#appendix-a-ts43) |
| TS44 | HA Failover Session Drop | HA | ★★★ | W16 | [Runbook → پیوست A](#appendix-a-ts44) |
| TS45 | Syslog Gap | Logging | ★★ | W17 | [Runbook → پیوست A](#appendix-a-ts45) |
| TS46 | NTP/Time Skew | NTP | ★★ | W17 | [Runbook → پیوست A](#appendix-a-ts46) |
| TS47 | Zabbix بدون SNMP | Monitoring | ★★ | W17 | [Runbook → پیوست A](#appendix-a-ts47) |
| TS48 | Session Exhaustion/Performance (Lab) | Performance | ★★★ | W19 | [Runbook → پیوست A](#appendix-a-ts48) |
| TS49 | Remote User دسترسی ندارد | RA-VPN | ★★★ | W14 | [Runbook → پیوست A](#appendix-a-ts49) |
| TS50 | Fault Chain چندلایه | Multi-Layer | ★★★ | W19 | [Runbook → پیوست A](#appendix-a-ts50) |

## ۲۵.۲ فیلدهای مشترک همه ۵۰ Runbook (CF-1 تا CF-6)

| کد | فیلد | تعریف مشترک |
|---|---|---|
| CF-1 | Baseline سالم (۷) | Config مرجع در Git با Tag `baseline-<LabID>`؛ خروجی `show`/`get` مرجع ذخیره؛ تست End-to-End سبز؛ Snapshot PNetLab/ESXi قبل از تزریق |
| CF-2 | سرنخ‌های مجاز/غیرمجاز (۱۰) | **مجاز:** Symptom، Scope، زمان شروع، دسترسی CLI/Capture/Log. **غیرمجاز:** نام دستگاه/پارامتر خراب، Diff مستقیم با Baseline قبل از جمع‌آوری شواهد، حدس بدون آزمون |
| CF-3 | شواهد (۱۲) | خروجی دستورات تشخیصی با Timestamp، Capture/Log مرتبط، Screenshot، Config Diff پس از رفع |
| CF-4 | تحلیل Root Cause (۱۳) | چارچوب ۱۵ مرحله‌ای (فصل ۲۴)، هر فرضیه یک آزمون، «یک تغییر در هر بار» |
| CF-5 | معیار ارزیابی (۲۰) | ۱۰۰ امتیاز: Scope و شواهد ۲۰ · RCA ۲۵ · Fix+Verification ۲۰ · Rollback/ریسک ۱۰ · امنیت/Change (Pre/Post-check) ۱۰ · گزارش ۱۵ |
| CF-6 | تحویلی/درس‌آموخته (۲۱) | RCA یک‌صفحه‌ای: Timeline، Impact، Root Cause، Contributing Factors، Fix، Verification، Preventive Action، Lesson + Diff Config + فایل Capture |

> **قاعده امتیاز:** عبور = ≥ ۷۰ امتیاز و هیچ نقض ایمنی (مثلاً Debug روشن‌مانده، Verify غیرفعال‌شده به‌عنوان راه‌حل). **مرور مجدد (Re-take)** شامل سناریوی هم‌خانواده با Fault متفاوت است.

## ۲۵.۳ ۱۰ Runbook تفصیلی نماینده

> **همه فرمان‌های این بخش «نمونه» و `Unverified` هستند** تا Image Validation (فصل ۱۱) روی IOSv/IOSvL2 و FortiOS 7.0.3 واقعی انجام شود. نام Interfaceها نمونه است.

### DR-01 — TS06 STP Loop / Broadcast Storm (★★★، W4)
- **توپولوژی:** `HQ-ACC-SW1`، `HQ-ACC-SW2` ↔ `HQ-CORE-SW1` (Trunk)، VLAN 50 با دو PC.
- **Baseline:** Root=Core، لینک Access2→Core Blocking/Alternate؛ `show spanning-tree summary` بدون TCN مکرر؛ ping PC1↔PC2 سبز.
- **Fault Injection:** اتصال یک کابل (لینک) بین Access1 و Access2 با PortFast روی هر دو پورت و بدون BPDU Guard.
- **Symptom:** ping با Loss/Latency بالا؛ CPU سوئیچ‌ها بالا؛ LEDها در حال چشمک سریع (Console log: `%SW_MATM-4-MACFLAP_NOTIF`).
- **تشخیص نمونه:**
```text
show spanning-tree vlan 50
show mac address-table | include <MAC-PC1>
show processes cpu sorted
show interfaces counters
```
- **شواهد:** MAC یک Host روی دو پورت متناوب؛ شمارنده Broadcast/Multicast بالا؛ Capture روی Trunk: Frame Broadcast تکراری (`eth.dst==ff:ff:ff:ff:ff:ff`، افزایش نرخ).
- **تحلیل:** Loop L2 ← بررسی لینک جدید ← مقایسه Topology با Baseline.
- **Root Cause:** لینک اضافی + PortFast بدون Guard، STP (RSTP) روی پورت Edge Loop را نمی‌بیند تا BPDU برسد.
- **رفع:** (۱) قطع لینک اضافی (۲) صبر برای Stabilize (۳) `spanning-tree bpduguard enable` روی پورت‌های Access (۴) `show spanning-tree summary`.
- **Verification:** MAC پایدار؛ CPU عادی؛ ping Loss=۰؛ Capture بدون Storm.
- **Rollback:** اگر رفع باعث قطع یک مسیر مشروع شد، لینک را برگردان **فقط پس از** فعال‌سازی Guard/تایید Topology.
- **امتیاز:** مطابق CF-6 (فصل ۲۵.۲)؛ نمره ویژه برای «قطع لینک قبل از تغییر Config».

### DR-02 — TS16 Asymmetric Routing (★★★، W5)
- **توپولوژی:** Client (VLAN50) ← FGT ← دو مسیر WAN (ISP1، ISP2) ← Server در Internet-Sim؛ Return Route ISP-Sim فقط از ISP2.
- **Baseline:** SD-WAN/Static فقط ISP1؛ Session TCP کامل (`SYN`, `SYN/ACK`, `ACK`).
- **Fault Injection:** افزودن Static Route برگشت به Client-Subnet روی ISP2-Sim (Next-hop FGT-WAN2) و حذف مسیر برگشت ISP1.
- **Symptom:** ping (ICMP) گاهی OK؛ TCP/HTTPS Time-out؛ Session در FGT ناقص.
- **تشخیص نمونه:**
```text
# FortiGate (Unverified در 7.0.3)
diagnose sniffer packet any 'host <server> and port 443' 4 0 l
diagnose sys session list
diagnose debug flow filter addr <server>
diagnose debug flow trace start 20
diagnose debug enable
# Cisco ISP-Sim
show ip route <client-subnet>
```
- **شواهد:** در Sniffer، SYN روی `wan1` خارج و SYN/ACK روی `wan2` وارد؛ Debug Flow: «reverse path check fail» یا Drop به‌دلیل Session mismatch.
- **تحلیل:** مسیر رفت ≠ مسیر برگشت → بررسی Route/SD-WAN Rule/Policy Route دو‌طرف.
- **Root Cause:** Return Route در ISP-Sim از Interface دیگر؛ FGT با Strict RPF/Stateful Session ترافیک را Drop می‌کند.
- **رفع:** هم‌سو‌سازی Route برگشت با مسیر خروج (یا SD-WAN Rule/Policy-Route متقارن)؛ `diagnose debug reset`.
- **Verification:** TCP Handshake کامل روی یک Interface؛ Session Table پایدار.
- **Rollback:** Route قبلی ISP-Sim از Backup؛ Debug خاموش (`diagnose debug disable`).
- **نکته ایمنی:** Debug Flow را پس از کار حتماً خاموش کن.

### DR-03 — TS23 Double NAT (★★★، W10)
- **توپولوژی:** (Lab A) Client ← Core ← Cisco Edge Router (NAT) ← FGT (NAT) ← ISP-Sim.
- **Baseline:** NAT فقط روی FGT؛ Client Source اصلی در Log سرور دیده می‌شود (WAN-IP FGT).
- **Fault Injection:** فعال کردن `ip nat inside source … overload` روی Cisco Edge.
- **Symptom:** برخی پروتکل‌ها (مثلاً SIP/IPsec/برخی Web Appها) خراب؛ Logهای FGT Source = IP Cisco (نه Client).
- **تشخیص نمونه:** Capture در ۳ نقطه (Client، بین Cisco و FGT، WAN FGT)؛ `show ip nat translations`; `diagnose sys session list`.
- **شواهد:** Src IP در هر Hop متفاوت؛ Translation دوبار.
- **Root Cause:** دو مالک NAT برای یک جریان (نقض Policy مالکیت NAT).
- **رفع:** تعیین «مالک NAT» (در معماری اصلی: FGT) و حذف NAT از Cisco؛ تنظیم Route.
- **Verification:** Src واحد؛ سرویس‌ها OK؛ Log دقیق.
- **Rollback:** Restore Config Cisco (Git) اگر Route وابسته بود.
- **درس:** قانون «یک Flow = یک مالک NAT».

### DR-04 — TS26 Shadow Policy (★★★، W10)
- **توپولوژی:** LAN (VLAN20 Finance) → WAN؛ Policy #5 Allow-All برای LAN، Policy #12 Deny Finance→Social.
- **Baseline:** Policy ترتیب صحیح، Deny Finance بالاتر.
- **Fault Injection:** جابه‌جایی Policy Allow-All به بالاتر از Deny.
- **Symptom:** Finance به سایت ممنوع دسترسی دارد (Log: Allow به Policy #5).
- **تشخیص نمونه:** `diagnose firewall iprope lookup <src> <sport> <dst> <dport> <proto> <iif>` (Unverified)؛ Hit Count هر Policy؛ `diagnose debug flow`.
- **Root Cause:** First-Match + ترتیب نادرست.
- **رفع:** Reorder + اضافه‌کردن توضیح Policy؛ Review Hit Count.
- **Verification:** تست Allow/Deny با دو Source.
- **Rollback:** Policy Package قبلی (Backup Config).
- **ریسک:** تغییر ترتیب، ترافیک مجاز دیگر را قطع کند → Pre-check با Policy Matrix.

### DR-05 — TS31 MTU/MSS و PMTUD روی IPsec (★★★، W13)
- **توپولوژی:** HQ-FGT ⇄ BR1-FGT با IPsec Route-Based؛ Client BR1 → Web HQ.
- **Baseline:** ping با اندازه ۱۴۷۲ OK؛ HTTPS بزرگ OK.
- **Fault Injection:** کاهش MTU لینک Underlay (۱۴۰۰) و Block ICMP Type3 Code4 در Transit.
- **Symptom:** صفحات کوچک OK؛ دانلود/HTTPS بزرگ Hang.
- **تشخیص نمونه:**
```text
ping -f -l 1400 <dst>     # Windows
tracepath <dst>           # Linux
# Capture: icmp.type==3 && icmp.code==4 ; tcp.analysis.retransmission
```
- **Root Cause:** PMTUD شکست (ICMP Block) + MSS بزرگ‌تر از Path MTU.
- **رفع:** اجازه ICMP Frag-Needed **یا** MSS Clamp روی Policy/Tunnel Interface (Unverified مسیر GUI/CLI).
- **Verification:** دانلود بزرگ OK؛ Capture MSS تنظیم‌شده.
- **Rollback:** حذف Clamp (کاهش بازدهی).

### DR-06 — TS34 Tunnel UP ولی Traffic Block (★★★، W13)
- **توپولوژی:** مانند DR-05.
- **Baseline:** Tunnel up، Route به `10.20.0.0/16` از طریق VTI، Policy HQ→BR1.
- **Fault Injection:** حذف Route/یا Policy برگشت.
- **Symptom:** `get vpn ipsec tunnel summary` up؛ ping شکست.
- **تشخیص:** Route Table، Policy، Sniffer، `diagnose vpn tunnel list` (Counter encrypt/decrypt).
- **شواهد:** Encrypt افزایش، Decrypt ثابت (یا برعکس) → عدم بازگشت.
- **Root Cause:** Tunnel up ≠ Routing/Policy برقرار.
- **رفع:** Route Static/OSPF روی VTI + دو Policy.
- **Verification:** ping + ESP دو‌طرفه + Log Allow.
- **Rollback:** حذف Route/Policy اضافه.

### DR-07 — TS38 LDAPS Certificate Trust (★★★، W12)
- **توپولوژی:** FGT ← DC (LDAPS 636).
- **Baseline:** LDAP (389) تست موفق؛ LDAPS با CA Import موفق.
- **Fault Injection:** حذف CA از FGT یا تغییر ساعت DC (+۲ روز) یا Hostname اشتباه در Server.
- **Symptom:** Test Authserver خطا؛ Login کاربران دامنه شکست.
- **تشخیص:** `diagnose test authserver ldap <server> <user> <pass>` (Unverified)، Capture TLS (Alert `unknown_ca`/`bad_certificate`)، بررسی NTP.
- **Root Cause:** زنجیره اعتماد/زمان/نام.
- **رفع:** Import Root CA، همگام‌سازی NTP، تصحیح FQDN.
- **Verification:** Test Login؛ Log کاربر.
- **Rollback:** حذف CA آزمایشی؛ ثبت Cert در Inventory.
- **ریسک:** غیرفعال‌کردن Verify = ضعف امنیتی؛ **ممنوع** به‌عنوان راه‌حل.

### DR-08 — TS44 HA Failover Session Drop (★★★، W16، مشروط به امکان HA در Image)
- **توپولوژی:** HQ-FGT-01/02 (FGCP A-P) + Core×2؛ **`Unverified`: امکان HA در FortiGate-VM Eval**.
- **Baseline:** `get system ha status` عادی، Heartbeat دو لینک، Session Pickup (در صورت پشتیبانی).
- **Fault Injection:** قطع Monitor Interface Primary یا HA Heartbeat تکی.
- **Symptom:** Failover رخ می‌دهد اما Session‌های TCP قطع می‌شوند یا Split-Brain.
- **تشخیص:** `get system ha status`، Log HA، Capture HA Heartbeat.
- **Root Cause:** Monitor/Heartbeat/Priority/Session-Pickup نامناسب.
- **رفع:** Heartbeat دو لینک مجزا، Monitor Interface درست، Override مناسب.
- **Verification:** Failover کنترل‌شده: Session ادامه یا RTO مستند.
- **Rollback:** بازگردانی Config HA از Backup (Cluster را با احتیاط، یک‌یکی).
- **اگر HA در Image ممکن نیست:** سناریو به «مفهومی + Tabletop» تبدیل می‌شود و در Runbook با `Unverified/NotExecutable` ثبت می‌شود.

### DR-09 — TS47 Zabbix بدون SNMP Data (★★، W17)
- **توپولوژی:** `HQ-MON1` ↔ Core/Access/FGT.
- **Baseline:** `snmpwalk` موفق؛ Item ها Data دارند.
- **Fault Injection:** تغییر Community/ACL یا Block UDP/161 در Policy.
- **Symptom:** Zabbix `No data`/`Timeout`.
- **تشخیص:**
```text
snmpwalk -v2c -c <community> <ip> 1.3.6.1.2.1.1   # از Monitoring
# Cisco: show snmp ; show access-lists
# Capture: udp.port==161
```
- **Root Cause:** مسیر/ACL/Policy/Community.
- **رفع:** Allow Source Monitoring؛ **انتقال به SNMPv3 (`Unverified` سینتکس)** در Lab.
- **Verification:** Data در Zabbix؛ Trigger تست.
- **Rollback:** حذف Community موقت (v2c فقط Lab).
- **ریسک:** Community v2c قابل شنود → فقط Lab.

### DR-10 — TS50 Fault Chain چندلایه (★★★، W19)
- **توپولوژی:** End-to-End: Client VLAN50 → Access → FGT → DMZ Web.
- **Baseline:** Client به Web DMZ HTTPS OK.
- **Fault Injection (هم‌زمان، توسط مربی):** (۱) Allowed VLAN شامل 100 نیست (۲) Route DMZ روی FGT اشتباه (۳) Policy Client→DMZ سرویس HTTPS ندارد.
- **Symptom:** «Web DMZ باز نمی‌شود».
- **روش:** Divide & Conquer — ۱) Scope ۲) ping GW ۳) ARP ۴) Trunk ۵) Route ۶) Policy (Debug Flow) ۷) سرویس؛ **هر رفع را جداگانه Verify کن**.
- **شواهد:** سه Evidence مجزا (Trunk Output، Route Table، Debug Flow Policy-ID).
- **Root Cause:** سه علت مستقل (Fault Chain).
- **رفع:** سه Fix با Change Record جداگانه.
- **Verification:** Test End-to-End + Capture ۳ نقطه.
- **Rollback:** مرحله‌ای (برعکس ترتیب Fix).
- **امتیاز:** تأکید بر «یک تغییر در هر بار» و مستندسازی هر Fix.

## ۲۵.۴ زمان‌بندی TS

W3–W8: TS01–TS23 (Cisco Drill) · W9–W17: TS24–TS49 (در هفته مربوط) · W18–W19: TS-Block مرور تصادفی (Blind) و TS50 · **G7:** ≥ ۴۰ از ۵۰ حل‌شده با RCA.

# ۲۶. 24-Week Detailed Schedule

> الگوی روز هر هفته (S/L/X/R/A/C) و دقیقه‌های دقیق در فصل ۲۷ است؛ این فصل «محتوا» را تعیین می‌کند. شناسه Labها (Lxx) در پیوست B تعریف شده‌اند. موارد `Optional/Advanced` با علامت **[OPT]** مشخص‌اند و هرگز جای زمان ضروری را نمی‌گیرند.

## ۲۶.۱ جدول هفته‌به‌هفته

| هفته | موضوع | Gate | Cisco (جدید/مرور) | FortiGate | Windows/Linux/Tools | تمرکز Packet Analysis | Labs | خروجی تحویلی |
|---|---|---|---|---|---|---|---|---|
| W1 | Phase 0 + CLI Boot | — | جدید: Modes، show/ping، save | فقط Image Validation (Boot + License Import، بدون Policy) | PNetLab، Jump، Git | NIC→Wireshark smoke test | L01–L04 | Inventory، M0 Checklist، Commit اول |
| W2 | IP/IOS Mgmt/Wireshark | **G1** | جدید: IPv4/IPv6، VLSM، SSH، Backup | — | Wireshark/Windows Terminal | ARP/ICMP/DNS | L05–L10 | IP Plan اولیه، Backup Config |
| W3 | Switching I | — | جدید: VLAN/Trunk/RoAS/SVI؛ مرور: SSH/Backup | Demo-only: VLAN Sub-if روبه‌روی Trunk سیسکو | Linux VM | 802.1Q Tag | L11–L16 | VLAN Matrix، ۳ RCA |
| W4 | Switching II | **G2** | جدید: STP/EC/Port-Sec/Snooping/DAI | Demo-only: LACP/Trunk Uplink به FGT | Windows Server (DNS/DHCP) | DHCP DORA، STP BPDU | L17–L23 | Config L2 کامل، ۳ RCA |
| W5 | Routing I | — | جدید: Static/Floating/OSPFv2؛ مرور: VLAN/Trunk | Demo-only: Static+Return-Path | — | TTL/Routing | L24–L27 | Routing Table Analysis |
| W6 | Routing II + FHRP | **G3** | جدید: OSPF Multi-Area/OSPFv3/HSRP؛ مرور: STP | Demo-only: OSPF Neighbor با IOSv | — | OSPF Hello/LSA | L28–L33 | **Lab A طراحی/پیاده‌سازی (فصل ۱۷)** |
| W7 | IP Services | — | جدید: DHCP-Relay/NAT/ACL/NTP/SNMP/Syslog | Demo-only: NAT/ACL در برابر Policy | Linux rsyslog | NAT قبل/بعد | L34–L41 | Service Matrix |
| W8 | Automation/Hardening | CP1 | جدید: Hardening، Netmiko/Ansible، Git؛ مرور: همه | — | Ansible مقدماتی | Syslog/SNMP | L42–L46 | Cisco Campus As-Built (CP1) |
| W9 | FortiGate I | — | مرور: Trunk/VLAN/L2-Verification | معماری/Interface/Zone/Object/Admin/Routing/Backup | — | Debug Flow مقدماتی | L47–L50 | FGT Baseline Config + Backup |
| W10 | Policy/NAT | **G4** | مرور: ACL/NAT؛ Integration S1–S4، S8–S9 | Policy، NAT/VIP/Pool، Session | — | Sniffer + Flow | L51–L56 | Policy Matrix v1، Lab B (فصل ۱۷) |
| W11 | UTM/DMZ | — | جدید: SPAN (در صورت Image)؛ مرور: Port-Sec | AV/IPS/WebF/AppCtrl/SSL-Insp (مشروط به ماتریس لایسنس) | Linux Web، CA | TLS Handshake | L57–L61 | DMZ Design + Feature/License Log |
| W12 | Authentication | **G5** | مرور: DHCP-Relay/Snooping؛ AAA محلی | LDAP/RADIUS/FSSO/Captive | AD/NPS/Client | LDAP/RADIUS | L62–L67 | Auth Design + Test Report |
| W13 | IPsec/Branch | — | مرور: OSPF/Static داخل Branch، ACL | S2S Route-Based، Selector | — | IKE/ESP | L68–L72 | VPN Matrix |
| W14 | RA-VPN | — | مرور: Return Route به Pool، ACL | SSL VPN (7.0.3؛ فقط ایزوله) + Dial-up IPsec | FortiClient، Windows Client | TLS/ESP | L73–L77 | RA Design + Risk Note |
| W15 | SD-WAN/Dyn Routing | — | جدید: IP SLA/Track (در صورت Image)؛ مرور: OSPF | SD-WAN، Link-Monitor، OSPF، BGP مقدماتی | — | Health-Check | L78–L83 | WAN Design |
| W16 | HA/Central | **G6** | مرور: EtherChannel/STP برای HA | HA A-P (مشروط)، DoS، DMZ Hardening، FMG/FAZ (مفهومی) | — | HA Heartbeat | L84–L88 | HA Test Report |
| W17 | Monitoring | — | مرور: SNMP/Syslog/NTP | Logging/FortiView | Zabbix/rsyslog | Syslog/SNMP | L89–L92 | Dashboard Plan + Alert Catalog |
| W18 | Packets + TS-1 | — | مرور همه (Fault Mix) | مرور همه | Wireshark عمیق | PA01–PA18 | L93–L100 | RCAهای TS |
| W19 | Blue Team + TS-2 | **G7** | Hardening Audit | Hardening/IPS | Nmap (Lab-only) | Scan/Anomaly | L101–L103 | Hardening Report |
| W20 | Capstone-1 | — | Campus/WAN Build | — | IPAM/Doc | Capture Plan | L104–L107 | HLD/LLD/IP Plan |
| W21 | Capstone-2 | — | Cisco Support | Security/VPN | AD/Linux | Capture | L108–L111 | Policy/VPN Matrix |
| W22 | Capstone-3 | — | Fault Mix | HA/Mon | Monitoring | Capture | L112–L115 | Test Plan Results |
| W23 | Buffer/Mock | — | Remediation | Remediation | — | Blind Capture | L116 | Gap Closure Report |
| W24 | Final/Handover | **G8** | Final | Final | Final | Final | L117 | As-Built، Handover |

## ۲۶.۲ محتوای Optional/Advanced (بدون تغییر در ۸۶۴ ساعت)

| ID | محتوا | اولویت | در صورت وجود زمان/منابع |
|---|---|---|---|
| OPT-1 | BGP عمیق + Redistribution | بالا | در Buffer W23 یا خارج از دوره |
| OPT-2 | VDOM + Multi-Tenancy | متوسط | هفته‌های سبک (روز R) |
| OPT-3 | FortiManager/FortiAnalyzer Hands-on | بالا (اگر لایسنس/منابع) | W16 به‌جای Demo |
| OPT-4 | QoS عمیق + Multicast | پایین | پس از دوره |
| OPT-5 | NetBox (IPAM) | متوسط | W20 Optional |
| OPT-6 | Ansible/Nornir عمیق | متوسط | W8 Optional |
| OPT-7 | ZTNA/FortiClient EMS (مشروط به 7.0.3) | پایین | پس از دوره |
| OPT-8 | IPv6 کامل روی FortiGate | متوسط | W15 Optional |

> **قاعده:** اگر تأخیر ایجاد شد، ابتدا OPT حذف، سپس Lab‌های Independent کم‌ارزش فشرده و در نهایت Buffer (W23) مصرف می‌شود؛ هیچ‌وقت «استراحت» به ساعت مفید تبدیل نمی‌شود.

# ۲۷. Daily/Weekly Time Accounting

> **اصل:** هر روز دقیقاً **۳۶۰ دقیقه مفید**؛ استراحت جدا از آن؛ هفته = ۶ روز = ۲۱۶۰ دقیقه = ۳۶ ساعت؛ دوره = ۲۴ هفته = **۸۶۴ ساعت**. تناقض v1 (جمع ۳۰۰ دقیقه) برطرف شد.

## ۲۷.۱ تعریف قالب‌های روز (هر قالب دقیقاً ۳۶۰ دقیقه مفید)

| قالب | نام | Theory | Demo | Guided Lab | Independent Lab | Troubleshooting | Packet Analysis | Documentation | Active Recall/Review | Assessment | جمع (دقیقه) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **S** | Standard (مفهوم+Lab) | 60 | 40 | 90 | 60 | 40 | 30 | 15 | 25 | 0 | **360** |
| **L** | Lab-heavy | 20 | 20 | 90 | 120 | 50 | 30 | 15 | 15 | 0 | **360** |
| **X** | Troubleshooting-heavy | 15 | 15 | 30 | 60 | 165 | 45 | 15 | 15 | 0 | **360** |
| **R** | Review/Light | 0 | 0 | 0 | 45 | 75 | 30 | 90 | 120 | 0 | **360** |
| **A** | Assessment/Gate | 0 | 0 | 0 | 0 | 0 | 30 | 60 | 30 | 240 | **360** |
| **C** | Capstone/Project | 10 | 10 | 30 | 210 | 45 | 15 | 30 | 10 | 0 | **360** |

> **قانون:** استراحت‌ها (حدود ۶۰–۹۰ دقیقه در روز؛ بلوک‌های ۱۵ دقیقه‌ای بین بخش‌ها + یک وقفه ناهار) **خارج** از این ۳۶۰ دقیقه‌اند و در هیچ جمعی احتمال نمی‌شوند. «پنجره روز» پیشنهادی ≈ ۷.۵ تا ۸ ساعت ساعت دیواری.

## ۲۷.۲ نمونه چیدمان ساعتی روز قالب S (۳۶۰ دقیقه مفید)

| ردیف | بلوک | دقیقه | تجمعی |
|---|---|---|---|
| 1 | Active Recall (مرور روز قبل + کارت‌ها) | 25 | 25 |
| 2 | Theory | 60 | 85 |
| 3 | Demo | 40 | 125 |
| — | — استراحت (غیرمفید) — | 0 | 125 |
| 4 | Guided Lab | 90 | 215 |
| — | — وقفه ناهار (غیرمفید) — | 0 | 215 |
| 5 | Independent Lab | 60 | 275 |
| 6 | Packet Analysis (Capture/تحلیل) | 30 | 305 |
| — | — استراحت (غیرمفید) — | 0 | 305 |
| 7 | Troubleshooting Drill | 40 | 345 |
| 8 | Documentation + Git Commit | 15 | 360 |
| **جمع** | | **360** | **360** |

## ۲۷.۳ الگوی روزها در هر هفته و جمع دقیقه هفتگی

> ترتیب روزها: روز ۱ تا ۶. روز ۷ هر هفته استراحت کامل و **خارج از ۸۶۴ ساعت** است.

| هفته | الگوی روزها | Theory | Demo | Guided Lab | Independent Lab | Troubleshooting | Packet Analysis | Documentation | Active Recall/Review | Assessment | جمع دقیقه | ساعت |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W1 | `L-L-S-S-L-R` | 180 | 140 | 450 | 525 | 305 | 180 | 165 | 215 | 0 | 2160 | 36 |
| W2 | `S-S-L-S-A-R` | 200 | 140 | 360 | 345 | 245 | 180 | 210 | 240 | 240 | 2160 | 36 |
| W3 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W4 | `S-S-L-X-A-R` | 155 | 115 | 300 | 345 | 370 | 195 | 210 | 230 | 240 | 2160 | 36 |
| W5 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W6 | `S-L-S-X-A-R` | 155 | 115 | 300 | 345 | 370 | 195 | 210 | 230 | 240 | 2160 | 36 |
| W7 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W8 | `S-L-S-L-A-R` | 160 | 120 | 360 | 405 | 255 | 180 | 210 | 230 | 240 | 2160 | 36 |
| W9 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W10 | `S-S-L-X-A-R` | 155 | 115 | 300 | 345 | 370 | 195 | 210 | 230 | 240 | 2160 | 36 |
| W11 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W12 | `S-L-S-X-A-R` | 155 | 115 | 300 | 345 | 370 | 195 | 210 | 230 | 240 | 2160 | 36 |
| W13 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W14 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W15 | `S-L-S-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W16 | `S-L-S-X-A-R` | 155 | 115 | 300 | 345 | 370 | 195 | 210 | 230 | 240 | 2160 | 36 |
| W17 | `S-S-L-S-X-R` | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| W18 | `S-X-L-X-X-R` | 125 | 105 | 270 | 405 | 660 | 225 | 165 | 205 | 0 | 2160 | 36 |
| W19 | `S-L-X-X-A-R` | 110 | 90 | 240 | 345 | 495 | 210 | 210 | 220 | 240 | 2160 | 36 |
| W20 | `C-C-C-C-X-R` | 55 | 55 | 150 | 945 | 420 | 135 | 225 | 175 | 0 | 2160 | 36 |
| W21 | `C-C-C-C-X-R` | 55 | 55 | 150 | 945 | 420 | 135 | 225 | 175 | 0 | 2160 | 36 |
| W22 | `C-C-C-X-C-R` | 55 | 55 | 150 | 945 | 420 | 135 | 225 | 175 | 0 | 2160 | 36 |
| W23 | `X-C-X-A-C-R` | 50 | 50 | 120 | 585 | 495 | 180 | 240 | 200 | 240 | 2160 | 36 |
| W24 | `C-A-A-C-C-R` | 30 | 30 | 90 | 675 | 210 | 135 | 300 | 210 | 480 | 2160 | 36 |
| **جمع ۲۴ هفته** | | **3730** | **2810** | **7350** | **11490** | **9465** | **4425** | **4710** | **5220** | **2640** | **51840** | **864** |
| نسبت | | 7.2٪ | 5.4٪ | 14.2٪ | 22.2٪ | 18.3٪ | 8.5٪ | 9.1٪ | 10.1٪ | 5.1٪ | ۱۰۰٪ | |

## ۲۷.۴ جمع‌بندی به تفکیک Phase (ماژول)

> ماژول‌ها هفته‌-تراز هستند (هر ماژول مضرب صحیحی از هفته)، پس جمع ماژول‌ها دقیقاً با جدول هفتگی هم‌خوان است.

| Phase | هفته‌ها | Theory | Demo | Guided Lab | Independent Lab | Troubleshooting | Packet Analysis | Documentation | Active Recall/Review | Assessment | جمع دقیقه | ساعت |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Phase 0 — Discovery/Lab | W1 | 180 | 140 | 450 | 525 | 305 | 180 | 165 | 215 | 0 | 2160 | 36 |
| Phase 1 — Cisco CLI/IP | W2 | 200 | 140 | 360 | 345 | 245 | 180 | 210 | 240 | 240 | 2160 | 36 |
| Phase 2 — Switching | W3–W4 | 370 | 270 | 690 | 750 | 780 | 390 | 375 | 455 | 240 | 4320 | 72 |
| Phase 3 — Routing | W5–W6 | 370 | 270 | 690 | 750 | 780 | 390 | 375 | 455 | 240 | 4320 | 72 |
| Phase 4 — IP Services/Automation/Hardening | W7–W8 | 375 | 275 | 750 | 810 | 665 | 375 | 375 | 455 | 240 | 4320 | 72 |
| Phase 5 — FortiGate Core/Policy | W9–W10 | 370 | 270 | 690 | 750 | 780 | 390 | 375 | 455 | 240 | 4320 | 72 |
| Phase 6 — UTM/Auth/Windows | W11–W12 | 370 | 270 | 690 | 750 | 780 | 390 | 375 | 455 | 240 | 4320 | 72 |
| Phase 7 — VPN/Branch | W13–W14 | 430 | 310 | 780 | 810 | 820 | 390 | 330 | 450 | 0 | 4320 | 72 |
| Phase 8 — SD-WAN/HA/Central | W15–W16 | 370 | 270 | 690 | 750 | 780 | 390 | 375 | 455 | 240 | 4320 | 72 |
| Phase 9 — Monitoring | W17 | 215 | 155 | 390 | 405 | 410 | 195 | 165 | 225 | 0 | 2160 | 36 |
| Phase 10 — Packets/TS/Blue Team | W18–W19 | 235 | 195 | 510 | 750 | 1155 | 435 | 375 | 425 | 240 | 4320 | 72 |
| Phase 11 — Capstone | W20–W22 | 165 | 165 | 450 | 2835 | 1260 | 405 | 675 | 525 | 0 | 6480 | 108 |
| Phase 12 — Buffer/Final | W23–W24 | 80 | 80 | 210 | 1260 | 705 | 315 | 540 | 410 | 720 | 4320 | 72 |
| **جمع** | | **3730** | **2810** | **7350** | **11490** | **9465** | **4425** | **4710** | **5220** | **2640** | **51840** | **864** |

## ۲۷.۵ جدول کنترل محاسباتی نهایی

| کنترل | محاسبه | نتیجه | وضعیت |
|---|---|---|---|
| دقیقه مفید روزانه | هر قالب روز (جدول ۲۷.۱) | ۳۶۰ | ✅ مجموع هر ستون-ردیف در کد کنترل شد |
| دقیقه مفید هفتگی | ۳۶۰ × ۶ روز | **۲۱۶۰** | ✅ |
| ساعت مفید هفتگی | ۲۱۶۰ ÷ ۶۰ | **۳۶** | ✅ |
| ساعت مفید دوره | ۳۶ × ۲۴ هفته | **۸۶۴** | ✅ |
| دقیقه کل دوره | ۲۱۶۰ × ۲۴ | **51840** = 864h | ✅ (جمع جدول ۲۷.۳ = 51840) |
| روز هفتم | استراحت | ۰ دقیقه مفید | خارج از محاسبه |
| استراحت‌های درون روز | ≈ ۶۰–۹۰ دقیقه/روز | ۰ دقیقه مفید | خارج از محاسبه |

# ۲۸. Continuous Cisco Spiral Practice

> **اصل Spiral:** هر هفته Cisco در ۳ شکل حضور دارد: (۱) مهارت جدید یا (۲) مرور سطح‌بالاتر مهارت قبلی (Active Recall بدون نگاه به Config + Fault Injection) و (۳) یک سناریوی مشترک با FortiGate. سختی صعودی: **حفظ‌کردن ← اجرا ← عیب‌یابی ← طراحی ← دفاع از تصمیم**. فرمان‌های Cisco در IOSv/IOSvL2 تا پایان Image Validation (فصل ۱۱) `Unverified` هستند.

| هفته | موضوع Cisco (جدید / مرور) | فرمان‌ها و عملیات CLI | سناریوی مشترک Cisco + FortiGate | Active Recall (۱۰ دقیقه، بدون Config) | Troubleshooting / Fault Injection | خروجی قابل ارزیابی |
|---|---|---|---|---|---|---|
| 1 | جدید: Modes، Help، save | `enable`, `configure terminal`, `show running-config`, `copy running-config startup-config`, `?` | هر دو دستگاه Boot و Console (بدون Policy) | نام ۴ Mode و دستور ورود/خروج | Interface `shutdown` عمدی (TS-Warmup) | Screenshot/Log Boot + Inventory |
| 2 | جدید: IPv4/IPv6، SSH؛ مرور: Modes | `ip address`, `ipv6 address`, `crypto key generate rsa`, `line vty`, `transport input ssh`, `show ip interface brief` | SSH از Jump به Cisco و FGT (Mgmt Reachability) | ترتیب ۶ دستور SSH | Mask اشتباه + VTY Telnet فعال | Mgmt Plan + Backup Config |
| 3 | جدید: VLAN/Trunk/RoAS/SVI؛ مرور: SSH/IP | `vlan`, `switchport mode access/trunk`, `switchport trunk allowed vlan`, `interface g0/0.10`, `show interfaces trunk` | Demo: VLAN Sub-if FGT روبه‌روی Trunk؛ هنرجو سمت Cisco را Verify می‌کند | رسم Frame Tag/Untag روی کاغذ | TS03/TS04/TS05 (VLAN غلط، Allowed، Human-Error) | VLAN Matrix + ۳ RCA |
| 4 | جدید: STP/EC/Port-Sec؛ مرور: Trunk | `spanning-tree mode rapid-pvst`, `channel-group … mode active`, `switchport port-security`, `show etherchannel summary` | طراحی کاغذی Uplink Cisco→FGT (Trunk تکی یا LACP) | تفاوت Root/Designated/Blocked | TS06/TS07/TS08 | Config L2 + Root Plan |
| 5 | جدید: Static/Floating/OSPF؛ مرور: SVI/RoAS | `ip route`, `router ospf`, `show ip route`, `show ip ospf neighbor` | Demo: Static + Return Route در FGT | LPM روی ۵ مثال | TS13–TS16 | Routing Analysis |
| 6 | جدید: OSPF Multi-Area/HSRP؛ مرور: STP | `area range`, `default-information originate`, `standby 1 priority`, `show standby brief` | **Lab A:** Cisco L3 Core Gateway + FGT Edge (OSPF/Default) | ۴ شرط Adjacency | TS17–TS20 | Lab A As-Built |
| 7 | جدید: DHCP-Relay/NAT/ACL/SNMP/Syslog؛ مرور: OSPF | `ip helper-address`, `ip nat inside source`, `ip access-list extended`, `logging host`, `snmp-server` | مقایسه NAT/ACL سیسکو با Policy/NAT FGT (Demo) | ترتیب ACL و Implicit Deny | TS10/TS21/TS22 | Service Matrix |
| 8 | جدید: Hardening/Automation؛ مرور: همه | `service password-encryption`, `login local`, `access-class`, Netmiko `show`، `git diff` | Baseline مشترک: NTP/Syslog/SNMP به Monitoring | ۵ مورد Hardening بدون نگاه | **CP1:** ۳ عیب ناشناخته Campus | CP1 Practical + As-Built |
| 9 | مرور: Trunk/VLAN (سطح طراحی) | `show vlan brief`, `show interfaces trunk`, `show mac address-table` | FGT VLAN Sub-if روی Trunk Cisco واقعی (Lab B بخش ۱) | Native VLAN و اثر آن | Allowed VLAN حذف‌شده + FGT Interface غلط | Trunk Design Doc |
| 10 | مرور: ACL/NAT/SVI | `show access-lists`, `show ip nat translations`, `debug` با احتیاط | **Lab B** (FGT Gateway) و مقایسه با Lab A؛ S8/S9 (Double NAT) | تفاوت Packet Flow A در برابر B | TS23/TS24/TS26 | Packet Flow Comparison Doc |
| 11 | جدید: SPAN/Port-Mirror (اگر Image)؛ مرور: Port-Sec | `monitor session`, `show monitor session`, `show port-security` | Capture از Access برای DMZ/UTM | محل Capture برای ۳ مسئله | Rogue Host در VLAN + TS27 | Capture Report |
| 12 | مرور: DHCP-Relay/Snooping/AAA | `ip dhcp snooping`, `ip helper-address`, `aaa new-model` (Unverified) | DHCP Relay به DC در VLAN Servers؛ Auth Client | DORA و نقش Trust | TS10/TS11 + Auth Failure | Auth/DHCP Test Report |
| 13 | مرور: OSPF/Static/ACL در Branch | `show ip route`, `traceroute`, ACL روی Transit | Cisco ISP-Sim + IPsec FGT؛ Underlay/Overlay | تفاوت Underlay/Overlay | TS32–TS36 | Underlay Test Plan |
| 14 | مرور: Return Route/ACL | `ip route <pool>`, `show access-lists` | RA-VPN Pool Route از Core/ISP-Sim | مسیر برگشت VPN Pool | TS49 | RA Path Doc |
| 15 | جدید: IP SLA/Track؛ مرور: OSPF | `ip sla`, `track`, `ip route … track` (Unverified) | Dual-WAN با ISP-Sim Cisco + SD-WAN Health-Check | تفاوت Static-Track و SD-WAN | TS43 + Cisco Static Track | Failover Test Report |
| 16 | مرور: EtherChannel/STP/HSRP برای HA | `show etherchannel`, `show spanning-tree root`, `show standby` | HA FGT + Dual Switch (S11) | Failure Domain ۳ نقطه | TS44 + STP Reconvergence | HA Failover Report |
| 17 | مرور: SNMP/Syslog/NTP | `snmp-server`, `logging`, `ntp server`, `show ntp status` | Cisco+FGT → Zabbix/rsyslog (S14) | مسیر Log از Source تا Dashboard | TS45–TS47 | Monitoring Catalog |
| 18 | مرور: Fault-Mix سطح بالا | همه show/debug | Packet Flow End-to-End (S15) با Capture ۵ نقطه | ۱۰ Filter Wireshark | TS-Block (Blind) | PA Reports |
| 19 | مرور: Hardening/Port-Sec | `show run` (فیلتر Section), ACL Management Plane | Hardening Audit دو‌طرفه | چک‌لیست Hardening | TS48/TS50 | Hardening Report |
| 20 | طراحی: Capstone Campus Cisco | همه | Build HQ Access/Distribution + FGT | Failure Domain HQ | Pre/Post-check | HLD/LLD + Config |
| 21 | پیاده‌سازی: Cisco Support Capstone | همه | Policy/VPN/AD Integration | Return Path ۳ Flow | Mini Fault Mix | Policy/VPN Matrix |
| 22 | Fault Mix Capstone | همه | Fault Injection نهایی | RCA Format | ۵ Fault چندلایه | Test Results |
| 23 | Remediation | نقاط ضعف G1–G7 | Remediation Lab | کارت‌های ضعف | Blind TS | Gap Closure Report |
| 24 | آزمون نهایی Cisco | همه | G8 | — | ۳ Fault ناشناخته | Final Practical |

# ۲۹. Capstone Project

## ۲۹.۱ سازمان فرضی: «Zagros Logistics Co.»

| ویژگی | مقدار |
|---|---|
| صنعت | حمل‌ونقل و لجستیک |
| کارکنان | ≈ ۲۵۰ (HQ: ۱۸۰، BR1: ۳۵، BR2: ۲۰، BR3: ۱۵) |
| نیاز تجاری | دسترسی ۲۴/۷ به ERP (در DMZ/Server)، VPN بین شعب، کار از راه دور، تفکیک مالی/منابع انسانی، گزارش‌پذیری امنیتی |
| محدودیت بودجه | تجهیزات متوسط؛ FortiGate HA فقط در HQ |
| الزامات امنیتی | Segmentation، MFA برای VPN (در صورت امکان)، Logging ۹۰ روزه، Backup |


## ۲۹.۲ معماری اصلی Capstone (تصمیم: FortiGate = Gateway همه VLANها)

| پرسش معماری | پاسخ قطعی |
|---|---|
| Default Gateway هر VLAN | **FortiGate** (`.1` هر Subnet؛ فصل ۱۴.۲) |
| Inter-VLAN Routing کجا؟ | **روی FortiGate** (VLAN Sub-interface)؛ سوئیچ‌های Cisco L2-only (`no ip routing`) |
| FGT در کدام نقطه؟ | مرکز HQ؛ همه VLANها به آن Trunk می‌شوند؛ WAN1/WAN2 به ISP-Sim؛ DMZ روی Sub-if |
| اتصال Core↔FGT | Trunk 802.1Q (Allowed محدود، Native=99)؛ در صورت پشتیبانی LACP/Aggregate (`Unverified`) |
| Routing | **HQ:** Default به ISP (SD-WAN/Static)؛ شبکه‌های Branch از طریق VTI (Static یا OSPF روی تونل). **Cisco Core:** Default Gateway مدیریتی فقط برای SVI مدیریت. **ISP-Sim (Cisco):** Static/OSPF برای شبیه‌سازی اینترنت |
| مسیر رفت/برگشت | Client→Access→Core(L2)→FGT→(Policy/NAT)→WAN؛ بازگشت همان مسیر؛ بین VLAN: Hairpin روی همان Trunk با Policy |
| Asymmetric: پیشگیری/تشخیص | پیشگیری: یک Choke Point، Return Route همسو در ISP-Sim، SD-WAN Sticky. تشخیص: Capture دوسر، Session ناقص، Debug Flow (TS16) |
| Policy بین VLANها | **FGT** (Stateful، UTM در صورت لایسنس، Log، Identity) |
| Internet/DMZ/Server/User/Branch | Internet: Policy+SNAT در FGT. DMZ: VIP+Policy. Server VLAN: Policy از Users/IT. User VLAN: Least Privilege. Branch: IPsec + Policy Matrix |
| مسئول NAT/VIP/Policy/Route | **FortiGate**؛ Cisco فقط L2 + ISP-Sim Routing |

### ۲۹.۲.۱ دیاگرام فیزیکی/منطقی

```mermaid
flowchart TB
    subgraph HQ[HQ]
        ACC1[HQ-ACC-SW1] --- CORE1[HQ-CORE-SW1]
        ACC2[HQ-ACC-SW2] --- CORE1
        ACC1 --- CORE2[HQ-CORE-SW2]
        ACC2 --- CORE2
        CORE1 --- CORE2
        CORE1 ---|Trunk| FGT1[HQ-FGT-01]
        CORE2 ---|Trunk| FGT2[HQ-FGT-02 HA - مشروط]
        FGT1 --- FGT2
        DC[HQ-DC1] --- CORE1
        MON[HQ-MON1] --- CORE2
        WEB[HQ-WEB-DMZ1] --- FGT1
    end
    FGT1 --- ISP1[ISP1-R1 Cisco]
    FGT1 --- ISP2[ISP2-R1 Cisco]
    ISP1 --- BR1[BR1-FGT-01 + BR1-SW1]
    ISP1 --- BR2[BR2-FGT-01 + BR2-SW1]
    ISP2 --- BR3[BR3-FGT-01 + BR3-SW1]
    FGT1 === BR1
    FGT1 === BR2
    FGT1 === BR3
    RA[Remote Users] -.IPsec/SSL.-> FGT1
```

> **نقش‌های Cisco در Capstone:** Access/Core L2 (STP، EC، Port-Security، Snooping/DAI)، ISP/WAN-Sim (OSPF/Static/IP SLA)، Hardening/AAA/SNMP/Syslog/NTP، SPAN. این‌ها Cisco را در Capstone و در Spiral فعال نگه می‌دارند.

## ۲۹.۳ جدول VLAN / Gateway / Network / Zone / Policy (HQ)

| VLAN | Network | Gateway | Zone | Policy اصلی (خلاصه) |
|---|---|---|---|---|
| 10 MGMT | 10.10.10.0/24 | FGT `.1` | Z-MGMT | فقط IT→MGMT (SSH/HTTPS)؛ MGMT→MON (Syslog/SNMP) |
| 20 FINANCE | 10.10.20.0/24 | FGT `.1` | Z-FIN | →SRV (ERP/AD/DNS)؛ →WAN (Web محدود+UTM)؛ بدون HR |
| 30 HR | 10.10.30.0/24 | FGT `.1` | Z-HR | →SRV؛ →WAN؛ بدون FIN |
| 40 IT | 10.10.40.0/24 | FGT `.1` | Z-IT | →MGMT/SRV (مدیریتی)؛ →WAN |
| 50 USERS | 10.10.50.0/24 | FGT `.1` | Z-USERS | →SRV (DNS/AD/File)؛ →WAN؛ →DMZ (HTTPS) |
| 60 SERVERS | 10.10.60.0/24 | FGT `.1` | Z-SRV | ←Users/IT؛ →WAN (Update)؛ بدون Inbound آزاد |
| 80 GUEST | 10.10.80.0/24 | FGT `.1` | Z-GUEST | فقط WAN (Captive)؛ ممنوع→Z-* |
| 100 DMZ | 172.16.10.0/24 | FGT `.1` | Z-DMZ | ←WAN (VIP HTTPS)، ←Users (HTTPS)؛ DMZ→SRV فقط پورت‌های لازم |

## ۲۹.۴ Routing Table و مالکیت (خلاصه)

| دستگاه | Default | Routes مهم | مالک |
|---|---|---|---|
| HQ-FGT | به ISP1 (Primary)/ISP2 (Backup) | 10.20/30/40.0.0/16 از VTI؛ Connected VLANها | FGT |
| BR-FGT | به ISP محلی | 10.10.0.0/16 از VTI؛ Connected | FGT |
| HQ-CORE/ACC | Default → `10.10.10.1` (فقط Mgmt) | — | Cisco (L2) |
| ISP-Sim | — | WAN Subnetها (Static/OSPF) | Cisco |

## ۲۹.۵ Security Zone و Policy Matrix (نمونه)

| از \ به | MGMT | FIN | HR | IT | USERS | SRV | GUEST | DMZ | WAN |
|---|---|---|---|---|---|---|---|---|---|
| MGMT | — | ✗ | ✗ | ✗ | ✗ | MON/Syslog | ✗ | ✗ | ✗ |
| FIN | ✗ | — | ✗ | ✗ | ✗ | ERP/AD/DNS | ✗ | HTTPS | Web+UTM |
| HR | ✗ | ✗ | — | ✗ | ✗ | AD/DNS/File | ✗ | HTTPS | Web+UTM |
| IT | SSH/HTTPS | ✗ | ✗ | — | ✗ | Admin | ✗ | Admin | Web |
| USERS | ✗ | ✗ | ✗ | ✗ | — | AD/DNS/File | ✗ | HTTPS | Web+UTM |
| SRV | ✗ | ✗ | ✗ | ✗ | ✗ | — | ✗ | ✗ | Update |
| GUEST | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | — | ✗ | Web |
| DMZ | ✗ | ✗ | ✗ | ✗ | ✗ | محدود | ✗ | — | ✗ |
| WAN | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | VIP HTTPS | — |

## ۲۹.۶ Packet Flowهای مهم

| Flow | مسیر | نقطه Policy | NAT | Return |
|---|---|---|---|---|
| F1 User→Internet | PC→ACC→CORE→FGT→WAN | Z-USERS→WAN | SNAT | همان |
| F2 User→AD | PC→FGT→Z-SRV | Z-USERS→SRV | بدون | همان |
| F3 Branch→HQ-SRV | BR-LAN→BR-FGT→VTI→HQ-FGT→SRV | Policy هر دو سمت | بدون | VTI |
| F4 Internet→DMZ | WAN→FGT VIP→DMZ | WAN→DMZ | DNAT | همان |
| F5 Remote→SRV | RA→FGT→SRV | RA→SRV (Auth) | بدون | همان |
| F6 MON→Devices | MON→FGT→MGMT | SRV→MGMT (SNMP) | بدون | همان |
| F7 Dual-WAN Failover | Client→FGT→(WAN2) | همان | SNAT WAN2 | Sticky/Return Route |

## ۲۹.۷ Acceptance Tests (AT)

| AT | آزمون | معیار |
|---|---|---|
| AT01 | Inter-VLAN Policy | Allow/Deny مطابق Matrix؛ Hit Count |
| AT02 | DHCP هر VLAN | Lease صحیح؛ Relay |
| AT03 | AD Login/GPO | Domain Join + Login |
| AT04 | Auth FGT | LDAP/RADIUS موفق؛ Log کاربر |
| AT05 | DMZ از Internet-Sim | HTTPS Web OK؛ بدون دسترسی DMZ→Z-* |
| AT06 | Site-to-Site | هر ۳ Tunnel up؛ Ping/ESP؛ Policy |
| AT07 | Remote Access | اتصال Client؛ دسترسی Least Privilege (مشروط) |
| AT08 | Dual WAN Failover | Failover زیر هدف؛ Session Impact مستند |
| AT09 | HA (مشروط) | Failover؛ RTO/RPO ثبت |
| AT10 | Monitoring | Dashboard؛ Alert تست؛ Syslog از ۴ منبع |
| AT11 | Backup/Restore | Restore یک دستگاه از Backup؛ مقایسه Config |
| AT12 | Hardening Audit | Score ≥ ۸۰٪ چک‌لیست |
| AT13 | Packet Capture | PA18 با ۵ نقطه |
| AT14 | Time Sync | همه Offset<۱s |
| AT15 | Rollback Drill | اجرای Rollback Plan یک Change |

## ۲۹.۸ Fault Injectionهای نهایی (آزمون ناشناخته؛ ۸ مورد پایه — ۳ مورد در آزمون نهایی انتخاب می‌شوند)

| FI | Fault | حوزه |
|---|---|---|
| FI-1 | VLAN 50 از Trunk حذف | Trunk/VLAN |
| FI-2 | Shadow Policy برای Finance | Policy |
| FI-3 | Return Route ISP-Sim نادرست (Asymmetric) | Routing |
| FI-4 | Double NAT (NAT اضافه روی ISP-Sim/Cisco) | NAT |
| FI-5 | IPsec Selector Mismatch + MTU | VPN/MTU |
| FI-6 | LDAPS CA Trust/Time Skew | PKI/AD |
| FI-7 | Syslog/SNMP Block + NTP Drift | Monitoring/Time |
| FI-8 | Human-Error Change (Allowed VLAN replace) بدون Pre-check | Change Mgmt |

## ۲۹.۹ Milestoneهای هفتگی Capstone

| هفته | Milestone | شاهد |
|---|---|---|
| W8 | CM1: Cisco Campus HQ (Lab A + L2 Baseline) | CP1 + As-Built |
| W10 | CM2: FGT Gateway + Policy Base (Lab B) | G4 |
| W12 | CM3: AD/Auth + UTM + DMZ | G5 |
| W14–16 | CM4: IPsec Branches + RA + SD-WAN + HA(مشروط) | G6 |
| W17 | CM5: Monitoring/Logging | Dashboard |
| W20 | CM6a: HLD/LLD/IP/VLAN/Policy Matrix نهایی + Build HQ | Review |
| W21 | CM6b: Branchها + VPN + Security | AT01–AT07 |
| W22 | CM6c: HA/Monitoring/Fault Injection | AT08–AT15 |
| W23 | Remediation + Mock Practical | Gap Closure |
| W24 | Final Practical + As-Built + Handover | G8 |

## ۲۹.۱۰ معیار پایان دوره و شواهد تحویلی

| معیار | حداقل |
|---|---|
| توانایی مستقل | Final Practical بدون راهنما؛ ۳ Fault ناشناخته با RCA |
| تکمیل AT | ≥ ۱۳ از ۱۵ (AT09 و AT07 مشروط به امکان) |
| شواهد | Config Git، Capture، Policy/VPN Matrix، As-Built، Runbook، Handover Checklist، Test Report |
| دفاع | ۳۰ دقیقه توضیح و دفاع از ۳ تصمیم معماری |
| نقض ایمنی | صفر (R/S قوانین) |

## ۲۹.۱۱ مستندات الزامی Capstone

| سند | محتوا |
|---|---|
| Business Requirements | نیازها و محدودیت‌ها |
| Assumptions | فرضیات |
| HLD | معماری کلان، Zoneها، افزونگی |
| LLD | VLAN/IP/Routing/Policy/VPN/Server |
| Diagrams | Physical/Logical/L3/Security Zones |
| IP Plan | مطابق ۹.۳/۱۲.۳ |
| VLAN Matrix | مطابق ۱۲.۳ |
| Routing Plan | OSPF Areas، Static، Default، VPN |
| Firewall Policy Matrix | Zone×Zone با Service و Profile |
| VPN Matrix | Peer، Phase1/2، Selector، Routing |
| Server/Service Matrix | سرویس، پورت، مالک |
| Security Baseline | Hardening چک‌لیست Cisco/FGT/Win/Linux |
| Implementation Plan | ترتیب و وابستگی |
| Test Plan | Test Case + Acceptance |
| Rollback Plan | هر تغییر |
| Monitoring Plan | Item/Trigger/Dashboard |
| As-Built | وضعیت نهایی واقعی |
| Handover Checklist | تحویل Runbookها، دسترسی‌ها، Backup |

---

# ۳۰. Assessment و Competency Gates

## ۳۰.۱ سطوح مهارت

| سطح | نام | تعریف |
|---|---|---|
| L1 | آشنایی مفهومی | توضیح می‌دهد، اجرا نمی‌کند |
| L2 | اجرا با راهنما | با Runbook اجرا می‌کند |
| L3 | اجرای مستقل | بدون راهنما، با Verification صحیح |
| L4 | طراحی و عیب‌یابی مستقل | سناریوی جدید، طراحی + RCA |

## ۳۰.۲ نگاشت مهارت ← سطح هدف و Gate ارزیابی

| مهارت | سطح هدف | ارزیابی (هفته) | بحرانی؟ |
|---|---|---|---|
| IP/VLSM Design | L4 | W2، W20 | ✅ |
| Cisco CLI/Verification | L3 | W2، G1 | ✅ |
| VLAN/Trunk/Inter-VLAN | L4 | W3، G2 | ✅ |
| STP/EtherChannel | L3 | W4، G2 | |
| Routing (Static/OSPF) | L4 | W5–W6، G3 | ✅ |
| IP Services/ACL/NAT | L3 | W7 | ✅ |
| Cisco Hardening | L3 | W8 | ✅ |
| Automation | L2 | W8 | |
| FortiGate Admin/Interfaces | L3 | W9، G4 | ✅ |
| Policy/NAT/VIP | L4 | W10، G4 | ✅ |
| Security Profiles/SSL Inspection | L3 | W11 | |
| AD/LDAP/RADIUS | L3 | W12، G5 | ✅ |
| IPsec S2S | L4 | W13، G6 | ✅ |
| Remote Access VPN | L3 | W14، G6 | |
| SD-WAN/Dual-WAN | L3 | W15، G6 | |
| HA | L3 | W16، G6 | (مشروط) |
| Packet Analysis | L4 | W18، G7 | ✅ |
| Troubleshooting/RCA | L4 | G7، G8 | ✅ |
| Monitoring/Logging | L3 | W17 | |
| Blue Team/Hardening | L3 | W19 | ✅ |
| Backup/Change/Rollback | L3 | W8، Capstone | ✅ |
| Documentation/As-Built | L3–L4 | Capstone | ✅ |

## ۳۰.۳ ماتریس مهارت × هفته (معرفی I / تمرین P / ارزیابی A / Capstone C)

| مهارت | I | P | A | C |
|---|---|---|---|---|
| CLI/Mgmt | W1 | W2–W8 | G1 | W20 |
| VLAN/Trunk | W3 | W3–W4 | G2 | W20 |
| STP/EtherChannel | W4 | W4 | G2 | W20 |
| OSPF/Static | W5 | W5–W6 | G3 | W20 |
| ACL/NAT/DHCP | W7 | W7 | W7 | W20 |
| FGT Interfaces/Policy | W9 | W9–W10 | G4 | W21 |
| NAT/VIP/DMZ | W10 | W10–W11 | G4 | W21 |
| UTM/SSL Inspection | W11 | W11 | W11 | W21 |
| AD/LDAP/RADIUS | W12 | W12 | G5 | W21 |
| IPsec/RA-VPN | W13 | W13–W14 | G6 | W21 |
| SD-WAN/Dual WAN | W15 | W15 | G6 | W22 |
| HA | W16 | W16 | G6 | W22 |
| Monitoring | W17 | W17 | W17 | W22 |
| Packet Analysis | W2 | W2–W19 | G7 | W22 |
| Troubleshooting | W3 | W3–W19 | G7 | W22 |
| Hardening/Blue Team | W7 | W8، W19 | W19 | W22 |
| Documentation | W1 | همه | هر Milestone | W24 |

## ۳۰.۴ آزمون نهایی (۲ روز × ۶ ساعت — Gate G8)

| روز | بخش | مدت | شرح |
|---|---|---|---|
| ۱ | تحلیل نیازمندی + طراحی | 1.5h | شرح نیاز جدید (مثلاً شعبه جدید + DMZ + VPN) → IP/VLAN/Topology |
| ۱ | پیاده‌سازی Cisco | 1.5h | VLAN/Trunk/Routing |
| ۱ | پیاده‌سازی FortiGate | 1.5h | Policy/NAT/AD Auth/VPN |
| ۱ | Monitoring/Security Baseline | 1.5h | Zabbix/Hardening |
| ۲ | عیب‌یابی ۳ خرابی ناشناخته (Fault Injection) | 3h | با RCA |
| ۲ | تحلیل Capture + Log | 1h | یک مسئله |
| ۲ | As-Built + گزارش تحویل | 2h | |

## ۳۰.۵ معیار قبولی نهایی

| معیار | وزن |
|---|---|
| معماری و Packet Flow | ۱۰٪ |
| پیکربندی مستقل | ۲۵٪ |
| Verification | ۱۰٪ |
| عیب‌یابی سیستماتیک | ۲۰٪ |
| Packet/Log Analysis | ۱۰٪ |
| Security Baseline | ۱۰٪ |
| Backup/Rollback | ۵٪ |
| مستندسازی | ۱۰٪ |

**قبولی:** ≥ ۸۰٪ **و** هیچ مهارت «بحرانی» زیر L3 **و** عدم نقض Safety Rails (S1–S7 و R1–R6) **و** حضور/تکمیل صرفاً غیرمؤثر.

---


## ۳۰.۶ Rubric عملکرد

| معیار | L1 (ناکافی) | L2 (با راهنما) | L3 (مستقل) | L4 (طراحی/دفاع) | شاهد قابل مشاهده |
|---|---|---|---|---|---|
| دانش مفهومی | تعریف ناقص | توضیح با کمک | توضیح صحیح Packet Flow | مقایسه گزینه‌ها و توجیه | Teach-Back، پاسخ شفاهی |
| اجرای عملی | ناتمام | با Runbook | مستقل + Verification | بهینه/امن + جایگزین | Config + `show` |
| عیب‌یابی مستقل | حدس | با Hint | چارچوب ۱۵ مرحله‌ای | RCA عمیق + Prevent | RCA + Evidence |
| تحلیل Packet/Log | بدون ابزار | Capture بدون تحلیل | تحلیل صحیح | Correlation چند منبع | pcap + Report |
| امنیت و اصول عملیاتی | نقض | رعایت ناقص | رعایت کامل Baseline | بهبود Baseline | Audit Score |
| مستندسازی | ناقص | الگو پر شده | As-Built دقیق | قابل‌استفاده توسط دیگران | Docs در Git |
| توضیح/دفاع تصمیم | نمی‌تواند | تکرار | دفاع مستدل | تحلیل Trade-off | جلسه دفاع |

## ۳۰.۷ Competency Gates (G1 تا G8)

| Gate | هفته | حوزه | محتوای آزمون عملی | مدت | حد قبولی |
|---|---|---|---|---|---|
| **G1** | W2 | مقدمات و Cisco Basics | CLI Modes، IP/VLSM، SSH، Backup/Restore، ۱ عیب IP | ۴h | ≥۷۰٪ و CLI L3 |
| **G2** | W4 | Switching و VLAN | VLAN/Trunk/STP/EC/Port-Sec Build + ۲ عیب | ۴h | ≥۷۵٪ |
| **G3** | W6 | Routing | Static/Floating/OSPF Multi-Area/HSRP + ۲ عیب | ۴h | ≥۷۵٪ |
| **G4** | W10 | FortiGate Fundamentals | Interface/Zone/Policy/NAT/VIP + Debug Flow + ۲ عیب | ۴h | ≥۷۵٪ |
| **G5** | W12 | Integrated Network Security | Policy+UTM(مشروط)+AD/RADIUS+DMZ + Cisco Integration + ۲ عیب | ۴h | ≥۸۰٪ |
| **G6** | W16 | VPN/Branch | S2S + RA + SD-WAN + HA(مشروط) + ۲ عیب | ۴h | ≥۸۰٪ |
| **G7** | W19 | Monitoring/Troubleshooting | Dashboard/Alert + ۴۰/۵۰ TS + Capture + Blue Team | ۴h+ | ≥۸۰٪ و TS≥۴۰ |
| **G8** | W24 | Capstone | آزمون نهایی ۲ روزه (فصل ۳۰.۴) | ۲×۶h | ≥۸۰٪ و بحرانی ≥L3 |

> غیر Gate: **CP1** (W8) Cisco Campus Checkpoint (۴h) — بازخورد، بدون مردودی رسمی؛ **Mock Practical** (W23).

## ۳۰.۸ سیاست عدم قبولی، تمرین جبرانی و آزمون مجدد

| وضعیت | اقدام جبرانی | آزمون مجدد | سقف |
|---|---|---|---|
| ۶۰–۶۹٪ (نزدیک) | ۲ روز Remediation (از بافر هفته/روز R) + Labهای ضعف | بخش ناموفق (نیمه) با Fault متفاوت | ۲ بار |
| < ۶۰٪ | ۳–۴ روز Remediation + Lab‌های Guided مرتبط + Active Recall | آزمون کامل با Scenario جدید | ۲ بار |
| نقض ایمنی | Review Safety + تکلیف Change/Rollback | آزمون ویژه ایمنی | — |
| پس از ۲ شکست | بازنگری برنامه با کاربر: افزایش تمرین، کاهش [OPT]؛ **مدت ۲۴ هفته ثابت می‌ماند** | تصمیم کاربر | — |

> زمان Remediation از Buffer هفته ۲۳ و ساعات R/TS کسر می‌شود؛ ساعات مفید کل ۸۶۴ ثابت است.

## ۳۰.۹ معیار پذیرش (Exit Criteria) هر فاز

| فاز | هفته | معیار پذیرش (Exit Criteria) | شاهد |
|---|---|---|---|
| Phase 0 | W1 | T1–T11 سبز، Isolation اثبات شد | چک‌لیست امضا |
| Phase 1 | W2 | SSH/Backup/IPv4/IPv6 Design، ۱۰ مسئله VLSM | Workbook |
| Phase 2 | W3–W4 | VLAN/Trunk/STP/EC/Port-Sec، ۶ TS حل‌شده | Verification + RCA |
| Phase 3 | W5–W6 | OSPF Multi-Area، FHRP، ۷ TS | Verification |
| Phase 4 | W7–W8 | NAT/ACL/DHCP/Syslog/SNMP، Automation Backup، CP1 (بازخورد) | CP1 |
| Phase 5 | W9–W10 | Policy/NAT/VIP/Session، S1–S4/S8/S9 | Capture + Hit |
| Phase 6 | W11–W12 | UTM (با محدودیت)، AD Auth، **G5** | G5 |
| Phase 7 | W13–W14 | S2S + RA-VPN، ۷ TS | Capture ESP |
| Phase 8 | W15–W16 | SD-WAN/Dual-WAN/HA (مشروط)، **G6** | G6 |
| Phase 9 | W17 | Zabbix+Syslog+Dashboard+۱۰ سناریو | Dashboard |
| Phase 10 | W18–W19 | ۴۰/۵۰ TS، PA01–PA18، Blue Team | **G7** |
| Phase 11 | W20–W22 | Capstone با Test Plan | **Capstone Delivered (AT01–AT15)** |
| Final | W24 | ≥ ۸۰٪، بحرانی ≥ L3 | **G8** |

---

# ۳۱. Deliverables و Documentation Standards

## ۳۱.۱ ساختار پوشه (Git Repo)

```
zagros-lab/
├── 00-governance/        # Blueprint, ChangeLog, RiskRegister
├── 01-discovery/         # Inventory, As-Is, Lab Runbook
├── 02-design/            # HLD, LLD, IP-Plan, VLAN-Matrix, Diagrams
├── 03-cisco/
│   ├── configs/          # <device>_<yyyymmdd>_<tag>.cfg
│   ├── labs/             # Lxx-<topic>/ (workbook, outputs, pcap)
│   └── reference/        # Command Reference
├── 04-fortigate/
│   ├── configs/          # <device>_<yyyymmdd>_<tag>.conf
│   ├── labs/
│   └── reference/        # CLI/GUI Reference (7.0.3)
├── 05-windows-linux/
├── 06-monitoring/        # Zabbix templates, dashboards
├── 07-troubleshooting/   # TSxx-RCA.md
├── 08-capstone/
├── 09-assessment/        # Answer-key (instructor), results
└── 10-handover/          # As-Built, Handover checklist
```

**Naming:** `<LabID>_<Topic>_<Device>_<YYYYMMDD>_<vN>.<ext>` (مثال: `L19_EtherChannel_HQ-CORE-SW1_20261201_v1.cfg`).
**Commit Message:** `[Lxx] <what> — <result>`.
**Secrets:** هیچ Password/PSK/Key در Git (فقط Placeholder + Vault/فایل رمزگذاری‌شده).

## ۳۱.۲ فهرست Deliverableهای دوره

Course Master Blueprint · Curriculum Map · Lab Inventory · Image Compatibility Matrix · Physical/Logical Topology · IP Addressing Plan · VLAN Matrix · Device Configuration Templates · Cisco Command Reference · FortiGate CLI/GUI Reference · Firewall Policy Matrix · VPN Design · Troubleshooting Runbooks · Monitoring Dashboard Plan · Backup/Restore Procedure · Change Management Template · Rollback Template · Test & Acceptance Plan · Weekly Progress Report · Lab Workbook · Answer Key (مدرس) · Final Project Documentation · As-Built Documentation.

## ۳۱.۳ خروجی ذخیره‌شونده هر Lab

| فایل | محتوا |
|---|---|
| `workbook.md` | اهداف، مراحل، یادداشت‌ها |
| `configs/` | Config قبل/بعد |
| `verification.txt` | خروجی `show`/`diagnose` |
| `capture.pcapng` | در صورت لزوم |
| `diagram.drawio/.png` | Topology |
| `rca.md` | برای Fault Labs |
| `recall.md` | ۵ سؤال + پاسخ خود |

## ۳۱.۴ قالب Change Management / Rollback (کوتاه)

| فیلد | مقدار |
|---|---|
| Change ID/تاریخ/مجری | — |
| هدف و ریسک (Low/Med/High) | — |
| Backup انجام‌شده | مسیر |
| مراحل | ۱..n |
| Test بعد از تغییر | — |
| **Rollback Trigger** | شرط مشخص |
| **Rollback Steps** | دستورات دقیق |
| نتیجه | Success/Rolled-back |

---

# ۳۲. Backup، Restore، Change و Rollback

> قالب Change/Rollback کوتاه در فصل ۳۱.۴ است؛ این فصل فرایند کامل را تعریف می‌کند. اصل: **هیچ تغییری بدون Backup + Pre-check + Rollback Plan.**

## ۳۲.۱ چرخه تغییر (Change Lifecycle)

```mermaid
flowchart LR
    R[Request] --> A[Assess Risk] --> P[Plan + Rollback]
    P --> PRE[Pre-check] --> I[Implement] --> POST[Post-check]
    POST -->|OK| C[Close + Document]
    POST -->|Fail| RB[Rollback] --> V[Verify Baseline] --> C
```

## ۳۲.۲ Pre-check / Post-check

| مرحله | Cisco | FortiGate | Server |
|---|---|---|---|
| Pre-check | `show run`/Backup؛ `show interfaces trunk`؛ Baseline Git Tag | `execute backup config …` (`Unverified` سینتکس)؛ Policy Hit قبل؛ HA Status | Snapshot/Backup؛ AD Health |
| Post-check | همان `show` + Ping/Trace | Policy/Route/Session؛ Log | سرویس‌ها |
| زمان | هر Change در Window | | |

## ۳۲.۳ Backup و Restore Verification

| مورد | تکرار | روش | Verification |
|---|---|---|---|
| Config Cisco | قبل از Change + روزانه خودکار (Netmiko) | Git | `git diff` با Running |
| Config FGT | قبل از Change + روزانه | Backup فایل → Git (رمزگذاری‌شده؛ Secrets مراقبت) | Restore روی VM جدید (Quarterly/Lab: ۱ بار) |
| PNetLab Lab | هفتگی | Export | Import در Lab تست |
| VM Windows/Linux | Snapshot قبل از Change | ESXi | Restore Test |
| Restore Drill | AT11 | یک دستگاه | مقایسه Config + سرویس |

> **قانون:** Backup بدون Restore-Test «Backup» محسوب نمی‌شود.

## ۳۲.۴ Rollback Plan (الگو)

| فیلد | مقدار |
|---|---|
| Trigger | معیار مشخص (مثلاً Ping GW شکست تا ۵ دقیقه) |
| روش | بازگردانی Config/Snapshot (دستور دقیق) |
| زمان هدف | ≤ N دقیقه |
| Verification | Test سیاهه Post-check |
| تصمیم‌گیر | نقش |
| Fail-safe | دسترسی Out-of-band/کنسول؛ **Safe-mode/Timer** (Cisco: `reload in N` با احتیاط؛ FGT: Scheduled Revert `Unverified`) |

## ۳۲.۵ تغییر در Management Plane (ESXi/PNetLab/WireGuard)

**ممنوع** مگر: Snapshot/Backup + Rollback مکتوب + تأیید صریح کاربر + Window + دسترسی جایگزین (کنسول فیزیکی/OOB) 🔎.

# ۳۳. Operations، Incident Response و Handover

## ۳۳.۱ Operations روزانه/هفتگی

| فعالیت | دوره | مالک | خروجی |
|---|---|---|---|
| بررسی Dashboard/Alert | روزانه | Operator | Ticket/یادداشت |
| Backup Verification | روزانه/هفتگی | Operator | Log |
| Log Review (Security) | روزانه | امنیت | Report |
| PSIRT/Firmware Review | هفتگی | امنیت | Risk Note |
| Capacity/Baseline | ماهانه | شبکه | Report |
| Cert Expiry Review | ماهانه | PKI | لیست |
| DR/Restore Drill | فصلی | تیم | Report |

## ۳۳.۲ Incident Response (IR)

| فاز | اقدام | ابزار | خروجی |
|---|---|---|---|
| Detect | Alert/گزارش کاربر | Zabbix/Log | Ticket |
| Triage | Severity (P1–P4)، Scope | Dashboard | Incident Record |
| Contain | محدودسازی (Block/Isolate) با Change اضطراری | FGT/Cisco | لاگ اقدام |
| Eradicate/Recover | رفع علت، Restore | Runbook | Verification |
| Communicate | به‌روزرسانی ذینفع‌ها | Template | پیام |
| Post-Incident Review | Blameless، RCA | قالب RCA | Action Items |

| Severity | تعریف | هدف پاسخ (Lab) |
|---|---|---|
| P1 | قطع سرویس HQ/VPN کلیدی | فوری |
| P2 | قطع جزئی/Degraded | ساعت |
| P3 | تک‌کاربر | روز |
| P4 | درخواست | برنامه |

### Post-Incident Review (قالب)
Timeline · Impact · Root Cause · Contributing Factors · چه خوب کار کرد · چه بد · Action Items (Owner/Due) · تغییر Runbook/Monitoring.

## ۳۳.۳ Incident Drills در دوره

| Drill | هفته | سناریو |
|---|---|---|
| D1 | W19 | قطع VPN شعبه (TS32–TS36) + IR کامل |
| D2 | W22 | Failover/Dual-WAN + Communication |
| D3 | W23 | Fault Chain (TS50) با PIR |

## ۳۳.۴ Handover

| مورد | محتوا |
|---|---|
| As-Built | دیاگرام، Config نهایی (Git Tag `as-built`)، IP/VLAN/Policy/VPN Matrix |
| Runbookها | Backup/Restore، Change، IR، TS Top-10، Monitoring |
| دسترسی‌ها | حساب‌ها (Least Privilege)، Rotation Credential، Break-glass |
| Monitoring | Dashboard، Alert Catalog، Owner |
| Backup | محل، Restore Test نتیجه |
| ریسک‌ها | Known Issues، Open Items (از جمله FortiOS 7.0.3 و Patch Plan) |
| آموزش | Walkthrough ۱ ساعته + Q&A |
| Sign-off | امضای Handover Checklist |

**Handover Checklist:** ☐ As-Built ☐ Git Tag ☐ Runbooks ☐ Credentials Vault ☐ Backup+Restore Test ☐ Monitoring Owners ☐ Risk Register ☐ Walkthrough ☐ Sign-off.

# ۳۴. Official Resources و Version References

> **تاریخ بررسی همه ردیف‌ها: 2026-11-02.** بررسی به‌صورت Fetch محتوا انجام شد؛ در بعضی صفحات رسمی (Fortinet Administration Guide) محتوای متنی کامل بازگردانده نشد و ادعا `Unverified` ماند. هیچ URL ساختگی ثبت نشده؛ URLها فقط همان‌هایی‌اند که واقعاً باز شدند.

## ۳۴.۱ Reference Log (نتایج بررسی)

| # | ادعا / بخش طراحی | منبع (عنوان، نسخه/محصول) | URL | تاریخ | نتیجه |
|---|---|---|---|---|---|
| R1 | CVE-2022-40684: FortiOS 7.0.0 تا 7.0.6 آسیب‌پذیر؛ ارتقا به 7.0.7+ | Fortinet PSIRT FG-IR-22-377 | https://www.fortiguard.com/psirt/FG-IR-22-377 | 2026-11-02 | **Verified** |
| R2 | CVE-2022-42475: SSL-VPN، 7.0.0 تا 7.0.8؛ رفع 7.0.9+ | PSIRT FG-IR-22-398 | https://www.fortiguard.com/psirt/FG-IR-22-398 | 2026-11-02 | **Verified** (مقدار از سلول جدول Advisory) |
| R3 | CVE-2023-27997: 7.0.0 تا 7.0.11؛ رفع 7.0.12+ | PSIRT FG-IR-23-097 | https://www.fortiguard.com/psirt/FG-IR-23-097 | 2026-11-02 | **Verified** |
| R4 | وجود Release Notes FortiOS 7.0.3 (Build 0237) و فهرست SKU مجازی‌سازی (KVM/HV/XEN/VMX/Cloud) | FortiOS 7.0.3 Release Notes | https://docs.fortinet.com/document/fortigate/7.0.3/fortios-release-notes | 2026-11-02 | **Verified (وجود)**؛ نسخه‌های hypervisor و حداقل منابع روی همان صفحه یافت نشد → `Unverified` |
| R5 | Windows Server 2022 Evaluation ۱۸۰ روز | Microsoft Evaluation Center | https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022 | 2026-11-02 | **Verified** (Microsoft Evaluation Center، نه Learn) |
| R6 | محدودیت‌های Evaluation License FortiGate-VM | FortiOS 7.0 Admin Guide («Evaluation license») | https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/954635/evaluation-license | 2026-11-02 | **Unverified** — صفحه باز شد ولی فقط فهرست‌مطالب برگشت |
| R7 | SSL-VPN Web/Tunnel mode و سینتکس `diagnose debug flow`/`sniffer` در 7.0 | FortiOS 7.0 Admin Guide | https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide | 2026-11-02 | **Unverified** — متن کامل دریافت نشد |
| R8 | ویژگی‌ها/محدودیت‌های IOSvL2 و لایسنس Image در CML | Cisco DevNet CML Docs | https://developer.cisco.com/docs/modeling-labs/ | 2026-11-02 | **Unverified** — صفحه عمومی، بیانیه مشخصی ندارد |
| R9 | روش افزودن Image Fortinet/Interfaceها/Nested در PNetLab | PNetLab Documentation | https://pnetlab.com/pages/documentation | 2026-11-02 | **Unverified** — فقط عناوین («Supported Images»، «Supported virtualization platforms and software»، «NAT Cloud») دیده شد |
| R10 | Zabbix: مستند SNMP Items | Zabbix Documentation (current) | https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmp | 2026-11-02 | **Verified (صفحه باز می‌شود)** — نسخه Zabbix مقصد در Discovery انتخاب می‌شود |
| R11 | rsyslog: دریافت Syslog TCP (`imtcp`) | rsyslog Docs | https://www.rsyslog.com/doc/configuration/modules/imtcp.html (→ ریدایرکت 301 به `docs.rsyslog.com`) | 2026-11-02 | **Unverified** — مقصد ریدایرکت باز نشد |

## ۳۴.۲ منابع رسمی هدف (برای تکمیل در Phase 0 / Lesson Build)

| موضوع | منبع رسمی | بخش/ادعای تحت پوشش | وضعیت |
|---|---|---|---|
| Cisco IOS/IOS-XE | Cisco Configuration Guides و Command Reference (cisco.com) | سینتکس و رفتار فرمان‌ها (فصل ۱۵، ۱۲.۲) | `Unverified` — Release دقیق Image پس از IV-2 |
| Cisco CML/IOSv/IOSvL2 | CML Documentation / Release Notes | Featureهای Image (فصل ۱۲) | `Unverified` |
| FortiOS 7.0.3 | Fortinet Docs: Administration Guide 7.0، CLI Reference 7.0، Release Notes 7.0.3 | همه فصل ۱۶/۲۰ | `Unverified` (R4 وجود دارد) |
| FortiGate-VM | FortiGate-VM Install/Eval/Licensing Guide | منابع/لایسنس (فصل ۱۳، ۱۶.۸) | `Unverified` |
| FortiGuard PSIRT | fortiguard.com/psirt | آسیب‌پذیری‌ها | `Verified` برای R1–R3 |
| PNetLab | docs رسمی PNetLab | Node/Cloud/Image (فصل ۱۰) | `Unverified` |
| VMware ESXi | Broadcom/VMware Docs نسخه مربوط | Nested Virt، vSwitch (فصل ۱۰–۱۱) | `Unverified` |
| Microsoft | Microsoft Learn: AD DS، NPS، AD CS، DNS/DHCP | فصل ۱۸ | `Unverified` (Learn بررسی نشد) |
| Wireshark | wireshark.org/docs | فصل ۲۳ | `Unverified` |
| Zabbix | zabbix.com/documentation | فصل ۲۲ | `Verified` (R10: باز شدن صفحه SNMP) |
| rsyslog | rsyslog docs | فصل ۲۲ | `Unverified` (R11) |
| RFCها | RFC 791, 792, 826, 1918, 2328, 4271, 4301–4307, 7296, 5424, 3411+ | مفهومی | `Unverified` (متن بررسی نشد) |
| Hardening | CIS Benchmarks / Vendor Hardening Guide | فصل ۲۱ | `Unverified` |

> منابع عمومی/وبلاگ فقط برای توضیح تکمیلی و **جایگزین مستند رسمی نمی‌شوند**.

## ۳۴.۳ ابزارها

| ابزار | کاربرد | محل نصب | منابع | رایگان/تجاری | لایسنس/محدودیت | مبحث | جایگزین |
|---|---|---|---|---|---|---|---|
| VMware ESXi | میزبان | سرور | — | بسته به لایسنس 🔎 | `Unverified` نسخه رایگان/Broadcom 🔎 | همه | — |
| PNetLab | Lab شبکه | VM روی ESXi | 8+ vCPU/16+ GB | رایگان (`Unverified`) | `Unverified` شرایط | همه | EVE-NG، CML |
| Cisco IOSv/IOSvL2 | روتر/سوئیچ | PNetLab | فصل ۱۳ | تجاری (CML/DevNet) | `Unverified` لایسنس | Cisco | Packet Tracer (محدود) |
| FortiGate-VM 7.0.3 | Firewall | PNetLab | 1/2 | Eval | `Unverified` سقف Eval | Forti | — |
| Wireshark | Packet | Jump (Windows) | کم | رایگان | GPL | همه | tcpdump |
| tcpdump | Packet | Linux | کم | رایگان | — | همه | — |
| Nmap | Inventory/Detection | Linux Lab | کم | رایگان | **فقط Lab** | Blue Team | — |
| Windows Server/Client | AD، Client | QEMU/ESXi | جدول ۸.۱ | Eval | Server ۱۸۰ روز `Verified`؛ Client `Unverified` | Win | — |
| Linux (Ubuntu/Debian LTS) | WEB/MON/Syslog | همانند بالا | سبک | رایگان | — | Linux | Rocky/Alma |
| Windows Terminal (+PuTTY/SecureCRT) | CLI | Jump | — | رایگان (Terminal/PuTTY) | — | Cisco/Forti | SecureCRT (تجاری) |
| diagrams.net | نمودار | Jump | — | رایگان | — | Doc | Visio |
| Git | نسخه‌بندی | Jump/Linux | — | رایگان | — | Doc/Config | — |
| Zabbix | Monitoring | Linux | 2/4 | رایگان | — | Monitoring | LibreNMS |
| rsyslog | Syslog | Linux | کم | رایگان | — | Logging | Graylog [OPT] |
| Python + Netmiko / Ansible | Automation | Jump/Linux | کم | رایگان | — | W8 | Nornir |
| NetBox (IPAM) | IPAM | [OPT] | 2/4 | رایگان | — | [OPT] | جدول IPAM در Git (ضروری) |

**قاعده:** هیچ ابزار اضافه‌ای بدون دلیل وارد نمی‌شود؛ PRTG وارد نشد چون با Zabbix هم‌پوشان است؛ NetBox به [OPT] رفت چون برنامه ضروری بدون آن کامل است.

---

# ۳۵. Risks، Dependencies و Open Questions

## ۳۵.۱ وابستگی‌ها (Dependencies)

| # | وابستگی | اثر اگر نباشد | وضعیت |
|---|---|---|---|
| DEP1 | Image قانونی Cisco (IOSv/IOSvL2) | Labهای Cisco به Packet Tracer/مفهومی تبدیل می‌شوند (فصل ۱۲.۳) | 🔎 Open |
| DEP2 | FortiGate-VM 7.0.3 + License | هسته دوره | 🔎 Open |
| DEP3 | منابع ESXi (Tier) | Labهای نوبتی/مفهومی | 🔎 Open |
| DEP4 | Windows Eval ISO | AD/NPS | 🔎 Open |
| DEP5 | امکان vSwitch ایزوله (در صورت روش B/D) | Hybrid ممکن نیست؛ QEMU Node | 🔎 Open |
| DEP6 | حساب Fortinet Support | Image/Docs | 🔎 Open |
| DEP7 | Internet کنترل‌شده موقت | دانلود Package/ISO | 🔎 Open |

## ۳۵.۲ پرسش‌های باز (Open Questions) و تصمیم‌های نیازمند تأیید

| ID | پرسش/تصمیم | پیشنهاد من | وضعیت |
|---|---|---|---|
| Q1 | تأیید معماری اصلی Capstone = FGT Gateway (B) و Lab A مستقل | تأیید | Open |
| Q2 | روش اتصال VM (A QEMU / B vSwitch ایزوله / D Hybrid) | D بعد از Discovery | Open |
| Q3 | Tier هدف | بعد از اندازه‌گیری | Open |
| Q4 | FortiManager/FortiAnalyzer: Hands-on یا مفهومی | مفهومی اگر منابع/لایسنس نبود | Open |
| Q5 | اگر 7.0.3 در دسترس نبود: نزدیک‌ترین 7.0.x یا توقف؟ **(تغییر نسخه بدون اجازه شما ممنوع)** | سؤال از شما | Open |
| Q6 | Stack مانیتورینگ: Zabbix + rsyslog | تأیید | Open |
| Q7 | Windows 10 در برابر 11 | Win 10 (TPM) | Open |
| Q8 | الگوی روزانه (بلوک ۹۰ دقیقه‌ای) و ساعت‌های واقعی روز | تأیید | Open |
| Q9 | امکان ساخت vSwitch ایزوله بدون Uplink (فقط با تأیید صریح) | سؤال از شما | Open |
| Q10 | BR2 با Cisco Router برای Interop IPsec (Image `Unverified`) | [OPT] | Open |

## ۳۵.۳ ثبت ریسک (Risk Register)

| # | ریسک | احتمال | اثر | پیشگیری | برنامه جایگزین |
|---|---|---|---|---|---|
| R01 | کمبود RAM/CPU/Storage | 🔎 متوسط | بالا | Discovery + Tiered Lab | Capstone Tiered، Monitoring سبک |
| R02 | ناسازگاری Image | متوسط | بالا | Test Matrix فصل ۱۲ | Image جایگزین |
| R03 | Feature پشتیبانی‌نشده در Virtual Image | بالا (DAI/EPC/…) | متوسط | `Unverified` Test قبل از Lesson | CLI Review/Contingency ۱۰.۲ |
| R04 | لایسنس FortiGate/FortiGuard | بالا | بالا | تعریف راه‌حل آموزشی فصل ۱۶.۳ | Local Signature/Static Filter |
| R05 | محدودیت 7.0.3 (قدیمی) | قطعی | متوسط | ثبت Release Notes | **سؤال از کاربر (Q5)**؛ تغییر نسخه بدون اجازه ممنوع |
| R06 | **آسیب‌پذیری‌های FortiOS 7.0.x (`Verified`: CVE-2022-40684/42475، CVE-2023-27997)** | قطعی | بحرانی در صورت Exposure | **Air-Gap، عدم Port-forward، بدون ارتباط به Internet** | Snapshot، مطالعه موردی CVE |
| R07 | محدودیت Windows Evaluation (Server ۱۸۰ روز `Verified`) | قطعی | کم | Snapshot قبل از انقضا | Rebuild Script |
| R08 | Nested Virtualization | متوسط | بالا | بررسی D7 | Hybrid (B/D) |
| R09 | تداخل Lab با Management | متوسط | بحرانی | قوانین R2–R4، Test T9 | Disconnect فوری، Rollback |
| R10 | از دست رفتن دسترسی ESXi | کم | بحرانی | عدم تغییر Mgmt، Console/IPMI | دسترسی فیزیکی/Out-of-band 🔎 |
| R11 | آسیب VM/Config | متوسط | بالا | Snapshot + Git | Restore |
| R12 | نبود Backup | متوسط | بالا | Task W1، Backup خودکار | — |
| R13 | وابستگی به Internet (Download) | متوسط | متوسط | Offline Repo/ISO قبلی | Cache محلی |
| R14 | زمان بیش از ظرفیت | بالا | بالا | Buffer W23، حذف [OPT]، فشرده‌سازی Lab Independent | **مدت ثابت می‌ماند**؛ اولویت‌بندی |
| R15 | خستگی ۶ ساعته | بالا | بالا | فصل ۲۷ | روز سبک |
| R16 | فراموشی | بالا | متوسط | Spaced Repetition | Mini-Assessment |
| R17 | سقف محدودیت HA/Interface در Eval | 🔎 | متوسط | تست در Discovery | HA مفهومی |

---

## ۳۵.۴ فهرست ادعاهای `Unverified` برای بررسی

محدودیت‌های Eval FortiGate-VM · امکان HA/VDOM در Eval · دسترسی FortiGuard · سینتکس دقیق SD-WAN/FSSO/Debug-Flow در 7.0.3 · وجود SSL-VPN Web/Tunnel در 7.0.3 · پشتیبانی IOSv/IOSvL2 (DAI/Snooping/EPC/HSRP/SPAN/LACP) · سینتکس SNMPv3 · منابع FortiManager/FortiAnalyzer VM · حداقل منابع PNetLab · سازگاری ESXi/Nested · Windows Client Eval.

# ۳۶. Changelog (v1.0 → v2.0)

| # | تغییر نسبت به v1.0 | چرا | فصل/پیوست در v2.0 | اثر بر قابلیت اجرا/کیفیت |
|---|---|---|---|---|
| 1 | حذف تناقض ۳۰۰ در برابر ۳۶۰ دقیقه؛ قالب‌های روز (S/L/X/R/A/C) هر کدام ۳۶۰ دقیقه، استراحت خارج از محاسبه، جدول کنترل محاسباتی | ایراد ممیزی: جمع روزانه ۳۰۰ ≠ ۳۶۰ | ۲۷ (و ۲.۳) | زمان‌بندی بدون تناقض؛ ۲۱۶۰ دقیقه/هفته؛ ۸۶۴ ساعت |
| 2 | جدول هفته‌به‌هفته v1 (۳۶ ساعت با ارقام گرد) جایگزین شد با جدول محتوایی + جمع دقیقه تولیدشده از قالب‌ها | تناقض ارقام | ۲۶، ۲۷ | کنترل‌پذیری |
| 3 | حذف Plan B (۳۲ هفته) به‌عنوان جایگزین مدت؛ تبدیل به فهرست [OPT] داخل ۲۴ هفته | مدت دوره ثابت است | ۲۶.۲ | مدت ثابت؛ اولویت‌بندی صریح |
| 4 | معماری اصلی Capstone یکپارچه: FGT Gateway همه VLANها؛ Cisco L2 | ایراد ممیزی: ابهام Gateway | ۱۷، ۲۹، ۱۴.۲ | بدون ابهام؛ Policy/Return Path روشن |
| 5 | Lab A (Cisco L3 Core Gateway) به‌عنوان Lab مستقل با Packet Flow، مزایا/محدودیت‌ها | حفظ ارزش آموزشی | ۱۷.۲.۱ | درک هر دو مدل |
| 6 | ۱۵ سناریو با برچسب الگو [A]/[B] و مالک Gateway | ابهام ترکیب | ۱۷.۴ | شفافیت |
| 7 | بازنویسی ریسک FortiOS 7.0.3 با CVEهای Verified + قوانین Air-Gap/No-PortForward | ایراد ممیزی | ۲.۴، ۹.۲، ۱۶.۹، ۳۴ | ایمنی |
| 8 | Feature/Licensing/Dependency Matrix با وضعیت و جایگزین (بدون ادعای معادل کامل) | ایراد ممیزی | ۱۶.۸ | شفافیت لایسنس |
| 9 | Cisco Spiral ۲۴ ردیفی | تمرکز زیاد Cisco در ابتدا | ۲۸، ۲۶ | حفظ مهارت Cisco |
| 10 | ۵۰ Runbook اجرایی (۲۱ فیلد) + ۱۰ Runbook تفصیلی | ایراد ممیزی | ۲۵، پیوست A | قابل اجرا |
| 11 | TS02/TS05/TS25 اصلاح: Human-Error/Change، Packet-Loss، Duplex Unverified | پوشش حوزه‌های لازم | ۲۵ | پوشش کامل |
| 12 | Cisco Feature Compatibility Matrix + Image Validation | ایراد ممیزی | ۱۲.۲، ۱۱.۲ | کاهش ریسک ناسازگاری |
| 13 | سه Tier منابع (T1/T2/T3) + Discovery Checklist + تصمیم Tier | منابع نامشخص | ۱۳، ۱۱.۳ | واقع‌بینانه |
| 14 | افزودن IPAM، Planeها، Asymmetric، Debug Flow، MTU/MSS، Monitoring، Change، IR، PIR، Handover | کمبود جزئیات | ۱۴.۳، ۲۴، ۲۲.۴–۲۲.۹، ۳۲، ۳۳ | کامل‌تر |
| 15 | Gateهای G1–G8، Rubric، سیاست مردودی و Remediation | الزام جدید | ۳۰ | ارزیابی مبتنی بر مهارت |
| 16 | آدرس وب PNetLab `192.168.88.199` و قیود ایمنی کاربر | اطلاعات جدید | ۱، ۹.۲، ۱۱.۳ | هم‌خوانی با محیط |
| 17 | جایگزینی برچسب‌های قدیمی (هشدار/جستجو) با `Verified/Inferred/Unverified` | الزام جدید | سراسر | شفافیت |
| 18 | Reference Log با URL و تاریخ بررسی؛ ۶ ردیف Verified یا قابل‌باز شدن، بقیه Unverified | الزام منابع | ۳۴ | قابل ردیابی |
| 19 | ادعای «۹۰ روز Windows Client» به `Unverified` تنزل یافت | Verified نشد | ۱۸، ۳۴ | صداقت |
| 20 | ساختار ۳۸ بخشی؛ بخش‌های جدید 1، 6، 13، 20، 25–28، 32، 33، 36–38 | الزام ساختار | سراسر | کامل |

# ۳۷. Audit Traceability Matrix

| Audit Finding ID | ایراد/پیشنهاد ممیزی | اقدام اصلاحی انجام‌شده | فصل/بخش دقیق در v2.0 | وضعیت | توضیح/دلیل باقی ماندن موارد باز |
|---|---|---|---|---|---|
| AF-01 | تناقض ۵ ساعت/۶ ساعت (جمع روزانه ۳۰۰ دقیقه در v1) | قالب‌های روز ۳۶۰ دقیقه؛ استراحت خارج؛ جدول کنترل؛ هفته‌ها و Phaseها هم‌خوان؛ محاسبه با اسکریپت تأیید شد | ۲۷.۱–۲۷.۵، ۲.۳ | **Resolved** | — |
| AF-02 | ابهام در مالکیت Default Gateway و معماری Capstone | معماری B (FGT Gateway) به‌عنوان اصلی؛ ۱۰ پرسش معماری پاسخ؛ جدول VLAN/Gateway/Zone/Policy؛ Lab A مستقل | ۱۷.۲، ۲۹.۲–۲۹.۶، ۱۴.۲ | **Partially Resolved** | **تأیید کاربر** برای انتخاب B لازم است (Q1) و پشتیبانی LACP/Trunk روی FGT-VM باید تست شود |
| AF-03 | ریسک و قدیمی بودن FortiOS 7.0.3 و محدودیت لایسنس | CVEهای Verified، قوانین ایزولاسیون، درس Lifecycle/Patch، Feature/License Matrix | ۲.۴، ۹.۲، ۱۶.۸–۱۶.۹، ۳۴ | **Partially Resolved** | محدودیت‌های Evaluation License (R6) و HA/SSL-VPN/FortiGuard `Unverified`؛ نیاز به IV-5 و سند رسمی |
| AF-04 | تمرکز بیش از حد Cisco در هفته‌های ابتدایی | Cisco Spiral برای ۲۴ هفته؛ Cisco در Capstone (L2، ISP-Sim) | ۲۸، ۲۶، ۲۹.۲ | **Resolved** (طراحی) | اجرا وابسته به Image Cisco (DEP1) |
| AF-05 | ناقص بودن ۵۰ سناریوی Troubleshooting | ۵۰ Runbook با ۲۱ فیلد + ۱۰ تفصیلی + فیلدهای مشترک | ۲۵، پیوست A | **Partially Resolved** | دستورات/Faults `Unverified` تا Image Validation؛ TS02/TS11/TS44 وابسته به Feature |
| AF-06 | تأییدنشده بودن سازگاری IOSv/IOSvL2 | Cisco Feature Matrix (۲۳ ردیف) + Image Validation IV-1…IV-7 | ۱۱.۲، ۱۲.۲ | **Open** | آزمایش واقعی لازم است؛ منبع رسمی R8 Unverified |
| AF-07 | نامشخص بودن منابع و ظرفیت Lab | سه Tier + Discovery Checklist + تصمیم Tier | ۱۳، ۱۱.۳ | **Partially Resolved** | مقادیر برآورد (Inferred)؛ اندازه‌گیری محیط کاربر لازم |
| AF-08 | کمبود جزئیات IPAM، Planeها، Asymmetric Routing، Debug Flow، Monitoring، Change، IR | بخش‌های اختصاصی با Lab/Deliverable | ۱۴.۳، ۲۴.۲–۲۴.۵، ۲۲.۴–۲۲.۹، ۳۲، ۳۳ | **Resolved** (طراحی) | اجرا/تست دستورات در Lesson Build |
| AF-09 | نیاز به تأیید رسمی نسخه‌ها و قابلیت‌ها | Reference Log با URL/تاریخ؛ ۴ مورد Verified قطعی (R1–R3, R5) + وجود R4/R10 | ۳۴ | **Partially Resolved** | R6–R9، R11 و سایر ادعاها `Unverified`؛ نیاز به بررسی مستقیم مستندات/آزمایش |

# ۳۸. Appendices

## پیوست A — ۵۰ Runbook اجرایی (۲۱ فیلد)

> فیلدهای مشترک CF-1…CF-6 (فصل ۲۵.۲) برای همه سناریوها صادق است. دستورات `Unverified` تا Image Validation.

<a id="appendix-a-ts01"></a>
#### TS01 — Interface Shutdown

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS01 |
| ۲. عنوان | Interface Shutdown |
| ۳. حوزه فنی/مهارت هدف | Physical/Link |
| ۴. سطح دشواری | ★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W2؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access↔Core |
| ۸. Symptom برای هنرجو | PC1 آفلاین؛ ping به GW پاسخ نمی‌دهد |
| ۹. Fault Injection دقیق (توسط مربی) | `shutdown` روی پورت Access |
| ۱۱. ابزار/دستورات تشخیصی | `show ip interface brief`, `show interfaces status` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Interface administratively down |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Scope=یک PC 2) Link پورت 3) دیدن admin down 4) `no shutdown` |
| ۱۶. Verification | LED/Status up/up؛ ping GW؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | باز شدن پورت اشتباه (رخنه امنیتی) اگر پورت عمداً بسته بود |
| ۱۸. Rollback | `shutdown` مجدد + بازگرداندن Baseline؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts02"></a>
#### TS02 — Duplex/Speed Mismatch (امکان‌سنجی Unverified)

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS02 |
| ۲. عنوان | Duplex/Speed Mismatch (امکان‌سنجی Unverified) |
| ۳. حوزه فنی/مهارت هدف | Physical/Link |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W2؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access↔Core |
| ۸. Symptom برای هنرجو | Throughput پایین؛ شمارنده خطا بالا |
| ۹. Fault Injection دقیق (توسط مربی) | تنظیم دستی Speed/Duplex یک‌طرفه (در صورت پشتیبانی Image) یا جایگزین: تزریق خطای لینک با Linux netem |
| ۱۱. ابزار/دستورات تشخیصی | `show interfaces` (CRC/late collision)، iperf — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Mismatch/Link Quality |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) مقایسه Counter 2) دو سر لینک 3) هماهنگ‌سازی |
| ۱۶. Verification | Counter ثابت؛ iperf عادی؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | قطع لحظه‌ای لینک |
| ۱۸. Rollback | بازگردانی `speed/duplex auto`؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts03"></a>
#### TS03 — VLAN اشتباه روی Access

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS03 |
| ۲. عنوان | VLAN اشتباه روی Access |
| ۳. حوزه فنی/مهارت هدف | VLAN |
| ۴. سطح دشواری | ★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W2؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access |
| ۸. Symptom برای هنرجو | PC فقط محلی ping می‌شود؛ GW در دسترس نیست |
| ۹. Fault Injection دقیق (توسط مربی) | پورت در VLAN 50 به‌جای 20 |
| ۱۱. ابزار/دستورات تشخیصی | `show vlan brief`, `show mac address-table`, `arp -a` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | VLAN Assignment غلط |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) VLAN پورت 2) MAC در VLAN اشتباه 3) تصحیح |
| ۱۶. Verification | ARP/ping GW؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | قطع اتصال همان پورت |
| ۱۸. Rollback | برگرداندن `switchport access vlan`؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: ARP بدون Reply |

<a id="appendix-a-ts04"></a>
#### TS04 — Allowed VLAN حذف‌شده روی Trunk

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS04 |
| ۲. عنوان | Allowed VLAN حذف‌شده روی Trunk |
| ۳. حوزه فنی/مهارت هدف | Trunk |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W2؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access↔Core |
| ۸. Symptom برای هنرجو | VLAN20 در Access دیده نمی‌شود |
| ۹. Fault Injection دقیق (توسط مربی) | حذف VLAN20 از `allowed vlan` |
| ۱۱. ابزار/دستورات تشخیصی | `show interfaces trunk` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Allowed list ناقص |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Trunk Allowed/Active 2) Pruned? 3) `allowed vlan add 20` |
| ۱۶. Verification | `show interfaces trunk` شامل 20؛ ping؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | حذف مجدد Baseline؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Tag 20 روی Trunk ناپدید |

<a id="appendix-a-ts05"></a>
#### TS05 — Human Error: جایگزینی Allowed List (Change Mgmt)

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS05 |
| ۲. عنوان | Human Error: جایگزینی Allowed List (Change Mgmt) |
| ۳. حوزه فنی/مهارت هدف | Trunk/Change |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W2؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access↔Core |
| ۸. Symptom برای هنرجو | پس از Change، چند VLAN هم‌زمان قطع |
| ۹. Fault Injection دقیق (توسط مربی) | `allowed vlan 30` به‌جای `add 30` (بدون Pre-check) |
| ۱۱. ابزار/دستورات تشخیصی | `show run interface`, Change Log, `show interfaces trunk` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | نبود Pre/Post-check و Peer Review |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Timeline Change 2) Diff Config با Baseline در Git 3) Restore Allowed کامل 4) فرایند Pre/Post-check |
| ۱۶. Verification | VLANهای Baseline برقرار؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | بازگردانی ناقص → Outage بیشتر |
| ۱۸. Rollback | Rollback از Config Backup آخر؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts06"></a>
#### TS06 — STP Loop / Broadcast Storm

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS06 |
| ۲. عنوان | STP Loop / Broadcast Storm |
| ۳. حوزه فنی/مهارت هدف | STP |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W3؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access×2↔Core |
| ۸. Symptom برای هنرجو | شبکه کند/قطع، CPU بالا، MAC Flapping |
| ۹. Fault Injection دقیق (توسط مربی) | کابل اضافی بین دو Access + BPDU Guard غیرفعال |
| ۱۱. ابزار/دستورات تشخیصی | `show spanning-tree`, `show mac address-table` (Flap)، Capture — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Loop L2 |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Scope VLAN 2) CPU/Counters 3) یافتن لینک 4) قطع لینک 5) BPDU Guard/PortFast |
| ۱۶. Verification | Stable MAC؛ CPU عادی؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | قطع موقت سرویس |
| ۱۸. Rollback | برگرداندن کابل + Guard؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Broadcast مکرر |

<a id="appendix-a-ts07"></a>
#### TS07 — Root Bridge اشتباه

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS07 |
| ۲. عنوان | Root Bridge اشتباه |
| ۳. حوزه فنی/مهارت هدف | STP |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W3؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access/Core |
| ۸. Symptom برای هنرجو | مسیر Trafic از Access به‌جای Core |
| ۹. Fault Injection دقیق (توسط مربی) | Priority Access کمتر از Core |
| ۱۱. ابزار/دستورات تشخیصی | `show spanning-tree root` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Root Placement |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Root فعلی 2) Priority ها 3) `root primary` روی Core |
| ۱۶. Verification | Core=Root؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Reconvergence کوتاه |
| ۱۸. Rollback | برگرداندن Priority؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts08"></a>
#### TS08 — EtherChannel Mismatch

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS08 |
| ۲. عنوان | EtherChannel Mismatch |
| ۳. حوزه فنی/مهارت هدف | EtherChannel |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W3؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core↔Access |
| ۸. Symptom برای هنرجو | Port-Channel Down/Suspended |
| ۹. Fault Injection دقیق (توسط مربی) | Mode/VLAN/Speed متفاوت یک عضو |
| ۱۱. ابزار/دستورات تشخیصی | `show etherchannel summary` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Config ناهماهنگ |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Flagهای P/s/D 2) مقایسه اعضا 3) یکسان‌سازی |
| ۱۶. Verification | Po(SU) Members(P)؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Flap Port-Channel |
| ۱۸. Rollback | Restore Config؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts09"></a>
#### TS09 — SVI Down/Down (Lab A)

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS09 |
| ۲. عنوان | SVI Down/Down (Lab A) |
| ۳. حوزه فنی/مهارت هدف | Inter-VLAN |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W2؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | L3 Core (Lab A) |
| ۸. Symptom برای هنرجو | ping بین VLAN شکست؛ SVI Down |
| ۹. Fault Injection دقیق (توسط مربی) | VLAN فاقد پورت Active/Trunk |
| ۱۱. ابزار/دستورات تشخیصی | `show ip interface brief`, `show vlan brief` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | شرط Up بودن SVI |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) وضعیت SVI 2) VLAN روی Trunk 3) رفع |
| ۱۶. Verification | SVI up/up؛ ping؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | حذف Config آزمایشی؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts10"></a>
#### TS10 — DHCP Relay فراموش‌شده

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS10 |
| ۲. عنوان | DHCP Relay فراموش‌شده |
| ۳. حوزه فنی/مهارت هدف | DHCP |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W6؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Users VLAN↔DC |
| ۸. Symptom برای هنرجو | Client APIPA 169.254 |
| ۹. Fault Injection دقیق (توسط مربی) | نبود Relay/`helper-address` یا DHCP Relay در FGT |
| ۱۱. ابزار/دستورات تشخیصی | Capture DHCP، `show run interface` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Broadcast عبور نمی‌کند |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Discover بدون Offer 2) مسیر تا Server 3) Relay |
| ۱۶. Verification | Lease صحیح؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | حذف Relay آزمایشی؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Discover فقط یک‌سو |

<a id="appendix-a-ts11"></a>
#### TS11 — DHCP Snooping Untrusted Uplink

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS11 |
| ۲. عنوان | DHCP Snooping Untrusted Uplink |
| ۳. حوزه فنی/مهارت هدف | DHCP/L2 Security |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W3؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Access↔Core |
| ۸. Symptom برای هنرجو | DHCP کار نمی‌کند پس از فعال‌سازی Snooping (Unverified در IOSvL2) |
| ۹. Fault Injection دقیق (توسط مربی) | Uplink Trusted نشده |
| ۱۱. ابزار/دستورات تشخیصی | `show ip dhcp snooping` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Trust Model |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Counters Drop 2) Trust Uplink |
| ۱۶. Verification | Lease موفق؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Rogue DHCP پذیرفته در Trust اشتباه |
| ۱۸. Rollback | Trust اصلاحی/غیرفعال‌سازی Snooping؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts12"></a>
#### TS12 — Duplicate IP

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS12 |
| ۲. عنوان | Duplicate IP |
| ۳. حوزه فنی/مهارت هدف | ARP/IP |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W1؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Users VLAN |
| ۸. Symptom برای هنرجو | قطع‌وصلی Client؛ هشدار IP Conflict |
| ۹. Fault Injection دقیق (توسط مربی) | دو Host با IP یکسان |
| ۱۱. ابزار/دستورات تشخیصی | `arp -a`, Capture ARP, `show ip arp` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | ARP Conflict |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) MAC ها 2) تعیین دستگاه 3) Reservation |
| ۱۶. Verification | ثبات ARP؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | تغییر IP سرویس |
| ۱۸. Rollback | برگرداندن IP؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: ARP دو MAC |

<a id="appendix-a-ts13"></a>
#### TS13 — Subnet Mask اشتباه

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS13 |
| ۲. عنوان | Subnet Mask اشتباه |
| ۳. حوزه فنی/مهارت هدف | IP |
| ۴. سطح دشواری | ★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W1؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Users VLAN |
| ۸. Symptom برای هنرجو | فقط بخشی از Subnet قابل‌دسترسی |
| ۹. Fault Injection دقیق (توسط مربی) | Mask /25 به‌جای /24 |
| ۱۱. ابزار/دستورات تشخیصی | `ipconfig /all` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Mask |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Mask 2) Gateway در Subnet؟ 3) اصلاح |
| ۱۶. Verification | ping همه Hostها؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | برگرداندن Mask؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts14"></a>
#### TS14 — Default Gateway اشتباه

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS14 |
| ۲. عنوان | Default Gateway اشتباه |
| ۳. حوزه فنی/مهارت هدف | IP |
| ۴. سطح دشواری | ★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W1؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Users VLAN |
| ۸. Symptom برای هنرجو | فقط Subnet محلی در دسترس |
| ۹. Fault Injection دقیق (توسط مربی) | GW روی IP نادرست |
| ۱۱. ابزار/دستورات تشخیصی | `route print` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | GW |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) GW 2) ARP GW 3) اصلاح |
| ۱۶. Verification | ping خارج؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | برگرداندن GW؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts15"></a>
#### TS15 — Static Route با Next-Hop اشتباه

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS15 |
| ۲. عنوان | Static Route با Next-Hop اشتباه |
| ۳. حوزه فنی/مهارت هدف | Routing |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W4؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core↔Router |
| ۸. Symptom برای هنرجو | مقصد Unreachable |
| ۹. Fault Injection دقیق (توسط مربی) | Next-hop یک IP اشتباه |
| ۱۱. ابزار/دستورات تشخیصی | `show ip route`, `traceroute` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Route غلط |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Route 2) NH Reachable؟ 3) اصلاح |
| ۱۶. Verification | traceroute کامل؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Blackhole موقت |
| ۱۸. Rollback | حذف Route؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts16"></a>
#### TS16 — Asymmetric Routing (رفت ok، برگشت ندارد)

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS16 |
| ۲. عنوان | Asymmetric Routing (رفت ok، برگشت ندارد) |
| ۳. حوزه فنی/مهارت هدف | Asymmetric Routing |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W4؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core/Router×2↔FGT |
| ۸. Symptom برای هنرجو | TCP SYN رفت می‌رود؛ SYN/ACK از مسیر دیگر؛ Session ناقص |
| ۹. Fault Injection دقیق (توسط مربی) | Return Route نبود/نادرست روی یک مسیر |
| ۱۱. ابزار/دستورات تشخیصی | Capture دو‌سر، `diagnose sys session list`, `diagnose debug flow` (Unverified) — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Return Path |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Capture ورودی/خروجی 2) Return Route 3) اصلاح |
| ۱۶. Verification | TCP کامل؛ Session یک‌سره؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | تغییر مسیر ترافیک موجود |
| ۱۸. Rollback | حذف Route اصلاحی؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: SYN بدون SYN/ACK |

<a id="appendix-a-ts17"></a>
#### TS17 — OSPF MTU Mismatch

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS17 |
| ۲. عنوان | OSPF MTU Mismatch |
| ۳. حوزه فنی/مهارت هدف | OSPF |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W4؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core↔Router |
| ۸. Symptom برای هنرجو | Neighbor در EXSTART/EXCHANGE |
| ۹. Fault Injection دقیق (توسط مربی) | MTU متفاوت |
| ۱۱. ابزار/دستورات تشخیصی | `show ip ospf neighbor`, `show interfaces` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | MTU |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) State 2) MTU دو سر 3) یکسان‌سازی |
| ۱۶. Verification | FULL؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Reset Adjacency |
| ۱۸. Rollback | MTU Baseline؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts18"></a>
#### TS18 — OSPF Timer/Area/Auth Mismatch

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS18 |
| ۲. عنوان | OSPF Timer/Area/Auth Mismatch |
| ۳. حوزه فنی/مهارت هدف | OSPF |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W4؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core↔Router |
| ۸. Symptom برای هنرجو | Neighbor نمی‌زند |
| ۹. Fault Injection دقیق (توسط مربی) | Hello/Dead/Area/Auth متفاوت |
| ۱۱. ابزار/دستورات تشخیصی | `show ip ospf interface` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Parameter Mismatch |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Param 2) یکسان‌سازی |
| ۱۶. Verification | FULL؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Baseline؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts19"></a>
#### TS19 — OSPF Cost/Reference-BW

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS19 |
| ۲. عنوان | OSPF Cost/Reference-BW |
| ۳. حوزه فنی/مهارت هدف | OSPF |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W5؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Triangle Routers |
| ۸. Symptom برای هنرجو | ترافیک از لینک گران‌تر |
| ۹. Fault Injection دقیق (توسط مربی) | Cost دستی/Reference-BW نادرست |
| ۱۱. ابزار/دستورات تشخیصی | `show ip ospf interface` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Metric |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Cost 2) مسیر انتخابی 3) اصلاح |
| ۱۶. Verification | مسیر مطلوب؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Reconvergence |
| ۱۸. Rollback | Baseline Cost؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts20"></a>
#### TS20 — HSRP Priority/Preempt

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS20 |
| ۲. عنوان | HSRP Priority/Preempt |
| ۳. حوزه فنی/مهارت هدف | FHRP |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W5؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core×2 (Lab A) |
| ۸. Symptom برای هنرجو | Failover نمی‌کند/Active دوگانه |
| ۹. Fault Injection دقیق (توسط مربی) | Priority/Preempt/Track اشتباه |
| ۱۱. ابزار/دستورات تشخیصی | `show standby brief` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | FHRP Config |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Roles 2) Config 3) اصلاح |
| ۱۶. Verification | Failover<5s؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Flap |
| ۱۸. Rollback | Baseline؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: HSRP Hello |

<a id="appendix-a-ts21"></a>
#### TS21 — ACL Extended ترتیب اشتباه

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS21 |
| ۲. عنوان | ACL Extended ترتیب اشتباه |
| ۳. حوزه فنی/مهارت هدف | ACL |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W6؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Router/Core |
| ۸. Symptom برای هنرجو | ترافیک مجاز Block |
| ۹. Fault Injection دقیق (توسط مربی) | Deny قبل از Permit |
| ۱۱. ابزار/دستورات تشخیصی | `show access-lists` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Order/Implicit Deny |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Hit Count 2) ترتیب 3) اصلاح |
| ۱۶. Verification | Hit روی Permit؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | دسترسی ناخواسته موقت |
| ۱۸. Rollback | Baseline ACL؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts22"></a>
#### TS22 — NAT Inside/Outside جابه‌جا

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS22 |
| ۲. عنوان | NAT Inside/Outside جابه‌جا |
| ۳. حوزه فنی/مهارت هدف | NAT |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W6؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Router (ISP-Sim/Edge) |
| ۸. Symptom برای هنرجو | Internet قطع |
| ۹. Fault Injection دقیق (توسط مربی) | Roleهای NAT معکوس |
| ۱۱. ابزار/دستورات تشخیصی | `show ip nat translations` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | NAT Roles |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Roles 2) Translation خالی 3) اصلاح |
| ۱۶. Verification | Translation فعال؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Baseline؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Src بدون ترجمه |

<a id="appendix-a-ts23"></a>
#### TS23 — Double NAT

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS23 |
| ۲. عنوان | Double NAT |
| ۳. حوزه فنی/مهارت هدف | NAT |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W9؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Core/Router+FGT |
| ۸. Symptom برای هنرجو | بعضی سرویس‌ها کار نمی‌کنند؛ Log گمراه‌کننده |
| ۹. Fault Injection دقیق (توسط مربی) | NAT هم روی Cisco و هم FGT |
| ۱۱. ابزار/دستورات تشخیصی | Capture Pre/Post، `diagnose sys session list` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Double NAT |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Src در هر Hop 2) مالک NAT 3) حذف NAT اضافی |
| ۱۶. Verification | Src واحد؛ سرویس OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Session ها Reset |
| ۱۸. Rollback | Restore NAT؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: دو Src متفاوت |

<a id="appendix-a-ts24"></a>
#### TS24 — FGT Policy: Interface/Service/Order

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS24 |
| ۲. عنوان | FGT Policy: Interface/Service/Order |
| ۳. حوزه فنی/مهارت هدف | Firewall Policy |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W9؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | LAN↔WAN |
| ۸. Symptom برای هنرجو | کاربر Block |
| ۹. Fault Injection دقیق (توسط مربی) | Policy اشتباه در Interface/Service |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose debug flow` (Unverified), Hit Count — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Policy Lookup |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Flow 2) Policy ID 3) اصلاح |
| ۱۶. Verification | Allow + Log؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | دسترسی گسترده |
| ۱۸. Rollback | Revert Policy؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Log: Deny |

<a id="appendix-a-ts25"></a>
#### TS25 — Packet Loss روی لینک WAN

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS25 |
| ۲. عنوان | Packet Loss روی لینک WAN |
| ۳. حوزه فنی/مهارت هدف | Packet Loss/Performance |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W14؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔ISP-Sim |
| ۸. Symptom برای هنرجو | کندی و Retransmission |
| ۹. Fault Injection دقیق (توسط مربی) | Loss ۵٪ با Linux netem در مسیر (Inferred) |
| ۱۱. ابزار/دستورات تشخیصی | `ping`, iperf, Capture `tcp.analysis.retransmission` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Link Quality |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Loss Measure 2) Hop-by-Hop 3) Link Monitor |
| ۱۶. Verification | Loss<1٪؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | تغییر Failover |
| ۱۸. Rollback | حذف netem؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Retransmission |

<a id="appendix-a-ts26"></a>
#### TS26 — Shadow Policy

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS26 |
| ۲. عنوان | Shadow Policy |
| ۳. حوزه فنی/مهارت هدف | Firewall Policy |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W9؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | LAN↔WAN |
| ۸. Symptom برای هنرجو | Policy جدید بی‌اثر |
| ۹. Fault Injection دقیق (توسط مربی) | Policy بالاتر Deny/Allow |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose firewall iprope lookup` (Unverified), Hit — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Order |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Policy مؤثر 2) Reorder |
| ۱۶. Verification | Policy مورد انتظار Hit؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | تغییر دسترسی |
| ۱۸. Rollback | Reorder قبلی؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts27"></a>
#### TS27 — VIP بدون Policy

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS27 |
| ۲. عنوان | VIP بدون Policy |
| ۳. حوزه فنی/مهارت هدف | VIP/DNAT |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W10؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Internet-Sim→DMZ |
| ۸. Symptom برای هنرجو | Web DMZ در دسترس نیست |
| ۹. Fault Injection دقیق (توسط مربی) | VIP تنظیم؛ Policy ندارد |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose debug flow` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | VIP+Policy |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Flow 2) Policy 3) اضافه |
| ۱۶. Verification | Web OK از خارج؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Exposure — Lab ایزوله |
| ۱۸. Rollback | حذف Policy؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: SYN بدون پاسخ |

<a id="appendix-a-ts28"></a>
#### TS28 — Hairpin NAT

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS28 |
| ۲. عنوان | Hairpin NAT |
| ۳. حوزه فنی/مهارت هدف | NAT |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W9؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | LAN→VIP |
| ۸. Symptom برای هنرجو | از داخل به VIP کار نمی‌کند |
| ۹. Fault Injection دقیق (توسط مربی) | نبود SNAT/Policy داخلی |
| ۱۱. ابزار/دستورات تشخیصی | Capture — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Reply مستقیم |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Reply Path 2) Policy+SNAT |
| ۱۶. Verification | دسترسی داخلی؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Reply با Src واقعی |

<a id="appendix-a-ts29"></a>
#### TS29 — IP Pool/Central NAT

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS29 |
| ۲. عنوان | IP Pool/Central NAT |
| ۳. حوزه فنی/مهارت هدف | NAT |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W9؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT |
| ۸. Symptom برای هنرجو | NAT IP اشتباه |
| ۹. Fault Injection دقیق (توسط مربی) | Pool/Rule اشتباه |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose sys session list` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Pool |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Session NAT 2) Pool |
| ۱۶. Verification | NAT صحیح؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts30"></a>
#### TS30 — DNS Resolve Fail

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS30 |
| ۲. عنوان | DNS Resolve Fail |
| ۳. حوزه فنی/مهارت هدف | DNS |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W11؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Client↔DC |
| ۸. Symptom برای هنرجو | نام‌ها Resolve نمی‌شوند |
| ۹. Fault Injection دقیق (توسط مربی) | Policy UDP/TCP53 Block یا DNS Server اشتباه |
| ۱۱. ابزار/دستورات تشخیصی | `nslookup`, Capture 53 — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | DNS Path |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) IP ping؟ 2) DNS Query 3) Policy/Server |
| ۱۶. Verification | Resolve OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Query بدون Response |

<a id="appendix-a-ts31"></a>
#### TS31 — MTU/MSS (PMTUD)

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS31 |
| ۲. عنوان | MTU/MSS (PMTUD) |
| ۳. حوزه فنی/مهارت هدف | MTU/MSS |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W12؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | HQ↔BR via IPsec |
| ۸. Symptom برای هنرجو | سایت‌های بزرگ باز نمی‌شوند؛ ping کوچک OK |
| ۹. Fault Injection دقیق (توسط مربی) | MTU تونل/PMTUD Block |
| ۱۱. ابزار/دستورات تشخیصی | `ping -f -l`, Capture — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | MSS/MTU |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Size-test 2) ICMP Frag-Needed 3) MSS Clamp |
| ۱۶. Verification | HTTPS بزرگ OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Overhead |
| ۱۸. Rollback | حذف Clamp؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: ICMP Type3 Code4 |

<a id="appendix-a-ts32"></a>
#### TS32 — VPN Phase1 Down

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS32 |
| ۲. عنوان | VPN Phase1 Down |
| ۳. حوزه فنی/مهارت هدف | VPN |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W12؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔FGT |
| ۸. Symptom برای هنرجو | Tunnel Down |
| ۹. Fault Injection دقیق (توسط مربی) | PSK/Proposal/Peer متفاوت |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose vpn ike gateway list`, IKE Debug — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Ph1 Mismatch |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Log IKE 2) Param 3) اصلاح |
| ۱۶. Verification | Ph1 up؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: IKE بدون Reply |

<a id="appendix-a-ts33"></a>
#### TS33 — Phase2 Down

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS33 |
| ۲. عنوان | Phase2 Down |
| ۳. حوزه فنی/مهارت هدف | VPN |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W12؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔FGT |
| ۸. Symptom برای هنرجو | Ph1 up, Ph2 down |
| ۹. Fault Injection دقیق (توسط مربی) | Selector/Proposal |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose vpn tunnel list` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Ph2 Mismatch |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Selectors 2) اصلاح |
| ۱۶. Verification | Tunnel up؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts34"></a>
#### TS34 — Tunnel UP ولی Traffic Block

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS34 |
| ۲. عنوان | Tunnel UP ولی Traffic Block |
| ۳. حوزه فنی/مهارت هدف | VPN/Routing/Policy |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W12؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | HQ↔BR |
| ۸. Symptom برای هنرجو | Tunnel up؛ ping شکست |
| ۹. Fault Injection دقیق (توسط مربی) | Route/Policy برای VTI نبود |
| ۱۱. ابزار/دستورات تشخیصی | `get router info routing-table`, Policy — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Route/Policy |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Route 2) Policy 3) اصلاح |
| ۱۶. Verification | ping + ESP؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: ESP یک‌طرفه |

<a id="appendix-a-ts35"></a>
#### TS35 — NAT-T Block

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS35 |
| ۲. عنوان | NAT-T Block |
| ۳. حوزه فنی/مهارت هدف | VPN |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W12؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | پشت NAT |
| ۸. Symptom برای هنرجو | VPN پشت NAT Down |
| ۹. Fault Injection دقیق (توسط مربی) | UDP4500 Block |
| ۱۱. ابزار/دستورات تشخیصی | Capture 500/4500 — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | NAT-T |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Capture 2) Allow 4500 |
| ۱۶. Verification | up؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: 4500 Drop |

<a id="appendix-a-ts36"></a>
#### TS36 — Tunnel Flap/DPD

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS36 |
| ۲. عنوان | Tunnel Flap/DPD |
| ۳. حوزه فنی/مهارت هدف | VPN |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W12؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔FGT |
| ۸. Symptom برای هنرجو | Tunnel قطع‌وصل |
| ۹. Fault Injection دقیق (توسط مربی) | DPD/لینک ناپایدار |
| ۱۱. ابزار/دستورات تشخیصی | Log IKE — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | DPD |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Timeline 2) DPD/Link |
| ۱۶. Verification | پایدار؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts37"></a>
#### TS37 — LDAP Bind Fail

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS37 |
| ۲. عنوان | LDAP Bind Fail |
| ۳. حوزه فنی/مهارت هدف | AD/LDAP |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W11؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔DC |
| ۸. Symptom برای هنرجو | Login ناموفق |
| ۹. Fault Injection دقیق (توسط مربی) | Bind DN/Password/Base DN |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose test authserver ldap` (Unverified) — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | LDAP Param |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Test 2) Param |
| ۱۶. Verification | Login OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Lockout حساب |
| ۱۸. Rollback | Reset؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: LDAP Bind Err |

<a id="appendix-a-ts38"></a>
#### TS38 — LDAPS Certificate Trust

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS38 |
| ۲. عنوان | LDAPS Certificate Trust |
| ۳. حوزه فنی/مهارت هدف | AD/PKI |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W11؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔DC |
| ۸. Symptom برای هنرجو | LDAPS Fail |
| ۹. Fault Injection دقیق (توسط مربی) | CA/Hostname/Time |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose test authserver ldap`, Capture TLS — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Trust |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) TLS Alert 2) CA Import 3) NTP |
| ۱۶. Verification | OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: TLS Alert |

<a id="appendix-a-ts39"></a>
#### TS39 — RADIUS Reject

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS39 |
| ۲. عنوان | RADIUS Reject |
| ۳. حوزه فنی/مهارت هدف | RADIUS |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W11؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔NPS |
| ۸. Symptom برای هنرجو | Reject |
| ۹. Fault Injection دقیق (توسط مربی) | Secret/Client NPS |
| ۱۱. ابزار/دستورات تشخیصی | Event Viewer 6273, Test — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Secret |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Event 2) Secret |
| ۱۶. Verification | Accept؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: Access-Reject |

<a id="appendix-a-ts40"></a>
#### TS40 — FSSO/Group Mapping

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS40 |
| ۲. عنوان | FSSO/Group Mapping |
| ۳. حوزه فنی/مهارت هدف | AD/Identity |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W11؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT↔DC/Collector |
| ۸. Symptom برای هنرجو | Auth می‌شود؛ Policy Match نمی‌شود |
| ۹. Fault Injection دقیق (توسط مربی) | Group/Collector |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose debug authd fsso list` (Unverified) — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Identity |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Group 2) Policy |
| ۱۶. Verification | Match؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts41"></a>
#### TS41 — Deep Inspection CA غیرمعتمد

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS41 |
| ۲. عنوان | Deep Inspection CA غیرمعتمد |
| ۳. حوزه فنی/مهارت هدف | PKI/SSL |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W10؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Client↔FGT |
| ۸. Symptom برای هنرجو | HTTPS Warning/Break |
| ۹. Fault Injection دقیق (توسط مربی) | CA در Trust Store نیست |
| ۱۱. ابزار/دستورات تشخیصی | مرورگر، Log — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Trust |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Cert Chain 2) Import/Exempt |
| ۱۶. Verification | OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | حریم خصوصی |
| ۱۸. Rollback | Disable Inspection؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: TLS Cert Issuer |

<a id="appendix-a-ts42"></a>
#### TS42 — Certificate منقضی/Time Skew

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS42 |
| ۲. عنوان | Certificate منقضی/Time Skew |
| ۳. حوزه فنی/مهارت هدف | PKI/Time |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W11؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT/DC |
| ۸. Symptom برای هنرجو | Cert Expired |
| ۹. Fault Injection دقیق (توسط مربی) | Expiry/NTP |
| ۱۱. ابزار/دستورات تشخیصی | `get system status` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Time |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Time 2) Renew |
| ۱۶. Verification | Valid؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert Time؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts43"></a>
#### TS43 — SD-WAN Health-Check

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS43 |
| ۲. عنوان | SD-WAN Health-Check |
| ۳. حوزه فنی/مهارت هدف | SD-WAN |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W14؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT Dual-WAN |
| ۸. Symptom برای هنرجو | Failover نمی‌کند |
| ۹. Fault Injection دقیق (توسط مربی) | Target/Threshold |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose sys sdwan …` (Unverified) — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | SLA |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Health 2) SLA |
| ۱۶. Verification | Failover OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Flap |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Log SLA |

<a id="appendix-a-ts44"></a>
#### TS44 — HA Failover Session Drop

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS44 |
| ۲. عنوان | HA Failover Session Drop |
| ۳. حوزه فنی/مهارت هدف | HA |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W15؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT HA |
| ۸. Symptom برای هنرجو | Failover Session Drop |
| ۹. Fault Injection دقیق (توسط مربی) | Heartbeat/Monitor Interface (Unverified) |
| ۱۱. ابزار/دستورات تشخیصی | `get system ha status` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | HA Config |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Status 2) Monitor 3) HB |
| ۱۶. Verification | Session ادامه؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Failover ناخواسته |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | HA Log |

<a id="appendix-a-ts45"></a>
#### TS45 — Syslog Gap

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS45 |
| ۲. عنوان | Syslog Gap |
| ۳. حوزه فنی/مهارت هدف | Logging |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W16؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Devices→rsyslog |
| ۸. Symptom برای هنرجو | Log نمی‌رسد |
| ۹. Fault Injection دقیق (توسط مربی) | Source/Filter/Firewall |
| ۱۱. ابزار/دستورات تشخیصی | Capture 514 — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Log Path |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Capture 2) Filter |
| ۱۶. Verification | Log رسید؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: 514 |

<a id="appendix-a-ts46"></a>
#### TS46 — NTP/Time Skew

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS46 |
| ۲. عنوان | NTP/Time Skew |
| ۳. حوزه فنی/مهارت هدف | NTP |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W16؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | همه |
| ۸. Symptom برای هنرجو | Log ناهماهنگ |
| ۹. Fault Injection دقیق (توسط مربی) | NTP Down |
| ۱۱. ابزار/دستورات تشخیصی | `show ntp status` — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Time |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) NTP 2) Fix |
| ۱۶. Verification | Sync؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | — |

<a id="appendix-a-ts47"></a>
#### TS47 — Zabbix بدون SNMP

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS47 |
| ۲. عنوان | Zabbix بدون SNMP |
| ۳. حوزه فنی/مهارت هدف | Monitoring |
| ۴. سطح دشواری | ★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W16؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Zabbix↔Devices |
| ۸. Symptom برای هنرجو | No Data |
| ۹. Fault Injection دقیق (توسط مربی) | Community/ACL/Policy |
| ۱۱. ابزار/دستورات تشخیصی | `snmpwalk`, Capture 161 — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | SNMP Path |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Walk 2) ACL/Policy |
| ۱۶. Verification | Data؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Exposure Community |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture: 161 |

<a id="appendix-a-ts48"></a>
#### TS48 — Session Exhaustion/Performance (Lab)

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS48 |
| ۲. عنوان | Session Exhaustion/Performance (Lab) |
| ۳. حوزه فنی/مهارت هدف | Performance |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W18؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | FGT |
| ۸. Symptom برای هنرجو | CPU/Session بالا |
| ۹. Fault Injection دقیق (توسط مربی) | Traffic Generator Lab |
| ۱۱. ابزار/دستورات تشخیصی | `diagnose sys session stat`, `get system performance status` (Unverified) — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | Capacity |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Session Stat 2) DoS/Timeout |
| ۱۶. Verification | Normal؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | Drop Legit |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Log |

<a id="appendix-a-ts49"></a>
#### TS49 — Remote User دسترسی ندارد

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS49 |
| ۲. عنوان | Remote User دسترسی ندارد |
| ۳. حوزه فنی/مهارت هدف | RA-VPN |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W13؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | Client↔FGT |
| ۸. Symptom برای هنرجو | Connect OK؛ Server نه |
| ۹. Fault Injection دقیق (توسط مربی) | Split-Tunnel/Route/Policy |
| ۱۱. ابزار/دستورات تشخیصی | Client Route, Policy — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | RA Path |
| ۱۵. راه‌حل مرحله‌به‌مرحله | 1) Route 2) Policy |
| ۱۶. Verification | OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | — |
| ۱۸. Rollback | Revert؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture |

<a id="appendix-a-ts50"></a>
#### TS50 — Fault Chain چندلایه

| فیلد | مقدار |
|---|---|
| ۱. شناسه | TS50 |
| ۲. عنوان | Fault Chain چندلایه |
| ۳. حوزه فنی/مهارت هدف | Multi-Layer |
| ۴. سطح دشواری | ★★★ (از ساده‌تر تک‌لایه تا چندلایه) |
| ۵. پیش‌نیازها | درس‌ها/Labهای تا W18؛ چارچوب ۱۵ مرحله‌ای (فصل ۲۴) |
| ۶. توپولوژی/بخش مورد استفاده | End-to-End |
| ۸. Symptom برای هنرجو | Client به Web DMZ نمی‌رسد |
| ۹. Fault Injection دقیق (توسط مربی) | VLAN+Route+Policy هم‌زمان |
| ۱۱. ابزار/دستورات تشخیصی | همه — (دستورات `Unverified` تا Image Validation) |
| فیلدهای مشترک (۷، ۱۰، ۱۲، ۱۳، ۲۰، ۲۱) | طبق «فیلدهای مشترک CF-1…CF-6» در بخش ۲۵.۲ |
| ۱۴. علت اصلی | سه علت |
| ۱۵. راه‌حل مرحله‌به‌مرحله | Divide & Conquer؛ هر Fix با Verification |
| ۱۶. Verification | End-to-End OK؛ + بررسی Monitoring/Log |
| ۱۷. اثر جانبی/ریسک راه‌حل | تداخل Fixها |
| ۱۸. Rollback | Rollback مرحله‌ای؛ سپس Verification Baseline |
| ۱۹. Packet Capture/Log مورد انتظار | Capture ۵ نقطه |


## پیوست B — فهرست Labها

> هر Lab: شناسه، هدف، توپولوژی، Acceptance Criteria، فایل خروجی (فصل ۳۱.۳). «G»=Guided، «I»=Independent، «F»=Fault.

| هفته | Labها |
|---|---|
| W1 | L01 Discovery Inventory (G) · L02 Lab Foundation Test T1–T11 (G) · L03 اولین Console/CLI (G) · L04 Git Repo مستندات (G) |
| W2 | L05 IOS Modes/Config Mgmt (G) · L06 SSH/Hardening مدیریتی (G) · L07 Backup/Restore Config (G) · L08 IPv4/VLSM Design (I) · L09 IPv6 Addressing (G) · L10 Wireshark: ARP/ICMP/DNS (G) |
| W3 | L11 VLAN/Access (G) · L12 Trunk/Native/Allowed (G) · L13 RoAS (G) · L14 SVI Inter-VLAN (I) · L15 Linux VM+VLAN (G) · L16 F: VLAN/Trunk faults (F×۳) |
| W4 | L17 STP/RSTP Root (G) · L18 PortFast/BPDU Guard (G) · L19 EtherChannel LACP (G) · L20 Port-Security (G) · L21 DHCP Snooping/DAI (G، `Unverified`) · L22 Windows Server DNS/DHCP (G) · L23 F: STP/EtherChannel faults (F×۳) |
| W5 | L24 Static/Default/Floating (G) · L25 OSPFv2 Single Area (G) · L26 OSPF Neighbor Faults (F×۴) · L27 Return-path Analysis (I) |
| W6 | L28 OSPF Multi-Area/Cost (G) · L29 OSPF Default-Prop (G) · L30 OSPFv3 (G) · L31 HSRP/VRRP (G) · L32 IPv6 Routing (I) · L33 F: OSPF/FHRP faults (F×۳) |
| W7 | L34 DHCP Relay (G) · L35 NTP/Syslog (G) · L36 NAT/PAT (G) · L37 ACL Std/Ext (G) · L38 SNMPv3 (G) · L39 QoS مقدماتی (G) · L40 Linux rsyslog Server (G) · L41 F: ACL/NAT faults (F×۳) |
| W8 | L42 Python Netmiko Backup (G) · L43 Ansible مقدماتی (G) · L44 Git Config Versioning (G) · L45 Cisco Hardening Baseline (I) · L46 **CP1 Practical** (A) |
| W9 | L47 FGT Initial Setup/Interfaces/Zone (G) · L48 Admin/RBAC/Backup (G) · L49 Static/Policy Route (G) · L50 Packet Flow با `diagnose debug flow` (G) |
| W10 | L51 Policy/NAT Basic (G) · L52 Central NAT vs Policy NAT (G) · L53 VIP/IP Pool (G) · L54 Integration S1–S4 (G) · L55 S8/S9 ACL+NAT (I) · L56 F: Policy faults (F×۴) |
| W11 | L57 AV/IPS/WebFilter با محدودیت لایسنس (G) · L58 App Control/File Filter (G) · L59 SSL Inspection + CA Trust (G) · L60 DMZ Web + VIP (S12) (G) · L61 F: SSL/UTM faults (F×۳) |
| W12 | L62 AD DS Build (G) · L63 Domain Join (G) · L64 LDAP/LDAPS با FGT (G) · L65 NPS/RADIUS با FGT (G) · L66 FSSO/Captive (G) · L67 F: Auth faults (F×۳) |
| W13 | L68 IPsec S2S Route-Based (G) · L69 IPsec با Cisco داخلی (S5) (G) · L70 NAT-T/DPD (G) · L71 Hub-Spoke (I) · L72 F: VPN faults (F×۴) |
| W14 | L73 SSL VPN Web/Tunnel (G، Lab-only) · L74 Dial-up IPsec (G) · L75 Split-Tunnel/Policy (I) · L76 VPN Backup Path (I) · L77 F: RA-VPN faults (F×۳) |
| W15 | L78 SD-WAN Basics (G) · L79 Health-Check/SLA (G) · L80 Dual-WAN Failover S10 (G) · L81 OSPF Cisco↔FGT S6 (G) · L82 BGP مقدماتی (G) · L83 F: SD-WAN/Routing faults (F×۳) |
| W16 | L84 HA A-P S11 (G، مشروط) · L85 DoS Policy (G) · L86 DMZ Hardening (G) · L87 FortiManager/FAZ Demo (D) · L88 **G6 Practical** (A) |
| W17 | L89 Zabbix Install/SNMP (G) · L90 Syslog Correlation (G) · L91 Dashboard/Alert (I) · L92 Monitoring Scenarios×10 (F) |
| W18 | L93–L100 Packet Analysis Labs (جدول فصل ۲۳) · TS-01..25 |
| W19 | L101 Nmap Detection (G، Lab-only) · L102 Blue Team Investigation (G) · L103 Hardening Audit (I) · TS-26..50 |
| W20–22 | L104–L115 Capstone Build Tasks (I) + Fault Injection (F×۱۰) |
| W23 | L116 Mock Practical (A) · Remediation Labs |
| W24 | L117 **Final Practical** (A) · As-Built/Handover |

---

> **Gate Labs:** G1 (W2)، G2 (W4)، G3 (W6)، CP1 (W8)، G4 (W10)، G5 (W12)، G6 (W16)، G7 (W19)، G8 (W24) — آزمون‌های عملی فصل ۳۰.۷؛ Lab-ID آن‌ها در Lesson Build تخصیص می‌یابد.

## پیوست C — چک‌لیست آمادگی برای شروع اجرا (Go/No-Go)

| # | مورد | وضعیت |
|---|---|---|
| ☐ | سند حاضر توسط کاربر تأیید صریح شد | منتظر |
| ☐ | ممیزی v2.0 و اعمال نکات | منتظر |
| ☐ | Inventory ESXi (CPU/RAM/Disk/NIC) ارائه شد | 🔎 |
| ☐ | نسخه ESXi و PNetLab مشخص شد | 🔎 |
| ☐ | Image Cisco قانونی تأیید شد | 🔎 |
| ☐ | Image FortiGate 7.0.3 + License Eval تأیید شد | 🔎 |
| ☐ | Win Server/Client Eval ISO | 🔎 |
| ☐ | Subnet واقعی (Overlap Check) | 🔎 |
| ☐ | Snapshot/Backup ESXi و PNetLab گرفته شد | 🔎 |
| ☐ | تایید «عدم تغییر Mgmt/WireGuard» | ✅ |
| ☐ | روش اتصال VM (A/B/D) تصمیم | 🔎 |
| ☐ | تأیید Gateway اصلی Capstone = FGT (Q1) | منتظر |
| ☐ | آدرس‌های `192.168.88.3` و `192.168.88.199` تأیید و Mask ثبت شد | 🔎 |
| ☐ | Tier هدف (T1/T2/T3) | 🔎 |
| ☐ | زمان واقعی روزانه تأیید | 🔎 |
| ☐ | Git Repo آماده | 🔎 |

---

## پیوست D — بازبینی داخلی کنترل کیفیت (پیش از تحویل)

| کنترل | نتیجه | یادداشت |
|---|---|---|
| محتوای مفید v1 حفظ شده؟ | ✅ (به‌جز جدول‌های جایگزین‌شده: زمان‌بندی، Plan B (حذف‌شده)، TS جدول کوتاه) | Plan B حذف شد چون مدت ثابت است |
| تصمیم ثابت کاربر بی‌اجازه تغییر نکرده؟ | ✅ | مدت/ساعت/FortiOS 7.0.3/HQ+۳ شعبه ثابت |
| زمان روزانه ۳۶۰ دقیقه؟ | ✅ | تأیید با اسکریپت |
| جمع هفتگی ۳۶ ساعت؟ | ✅ | |
| جمع دوره ۸۶۴ ساعت؟ | ✅ | |
| معماری اصلی Capstone بدون ابهام؟ | ✅ (طراحی)؛ تأیید کاربر Open | |
| معماری جایگزین Lab مستقل؟ | ✅ | Lab A |
| مالک Gateway هر VLAN مشخص؟ | ✅ | |
| Cisco در هر ۲۴ هفته؟ | ✅ | فصل ۲۸ |
| ۵۰ TS مشخصات کافی؟ | ✅ | |
| ≥۱۰ Runbook تفصیلی؟ | ✅ | ۱۰ مورد |
| قابلیت Imageها Verified/Unverified؟ | ✅ | همه Unverified مگر خلاف ذکر شده |
| سه Tier؟ | ✅ | |
| محدودیت FortiOS/لایسنس صریح؟ | ✅ | |
| هیچ قابلیت تأییدنشده‌ای قطعی نیست؟ | ✅ (طبق بررسی داخلی) | |
| امنیت ESXi/PNetLab/WireGuard؟ | ✅ | |
| خروجی‌ها/معیارهای Capstone؟ | ✅ | |
| منابع رسمی و تاریخ؟ | جزئی | بسیاری Unverified |
| Traceability همه یافته‌ها؟ | ✅ | ۹ ردیف |
| سند مستقل؟ | ✅ | |

### محدودیت‌های شناخته‌شده v2.0
1. اغلب ادعاهای وابسته به Image/نسخه `Unverified` هستند و نیاز به IV-3/IV-5 و مستند رسمی دارند.
2. دستورات Cisco/FortiGate اجرا نشده‌اند.
3. جدول‌های Curriculum (فصل ۱۵–۱۶) نماینده‌اند؛ شرح خط‌به‌خط در Lesson Build.
4. منابع وب فقط به‌صورت محدود بررسی شد (فصل ۳۴).

---

**پایان سند v2.0 — هیچ درس، نصب، اجرا یا تغییری در محیط کاربر انجام نشده است. در انتظار بررسی و تأیید صریح کاربر.**
