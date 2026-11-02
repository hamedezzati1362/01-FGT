# Revision Report — Course Master Blueprint v2.0 → v2.1

**سند مبنا:** `Enterprise_Network_Security_Course_Master_Blueprint_v2.0.md`  **خروجی:** `Enterprise_Network_Security_Course_Master_Blueprint_v2.1.md`
**تاریخ:** 2026-11-02  **نوع:** اصلاح هدفمند (نه بازطراحی)  **اقدام روی زیرساخت:** هیچ

## ۱. یافته‌های ممیزی قبلی و اصلاحات

| ID | یافته | اصلاح | بخش‌های v2.1 | وضعیت |
|---|---|---|---|---|
| R21-01 | محیط مرجع و ارجاعات منسوخ | جدول «محیط مرجع» (ESXi `192.168.88.3`، PNetLab `192.168.88.199`، FortiGate فقط Node PNetLab)؛ تفکیک MikroTik/WireGuard از WAN/VPN/توپولوژی. **در v2.0 هیچ ارجاعی به FortiGate حذف‌شده یا Firewall پلتفرم دیگر نبود** (بررسی متنی) | 10.0، 9.2، 14.1 | **Resolved** |
| R21-02 | تناقض Phase 0 | Phase 0A (Read-Only) و 0B (Lab Foundation) با مرز تأیید صریح؛ قالب روز D؛ W1: D-D-L-L-S-R | 11.0–11.3، 10.4، 26، 27 | **Resolved** (0B هنوز تأیید نشده؛ عمدی) |
| R21-03 | عدم تطابق Capstone/Tier | Completion Class (C-SEQ/C-DUAL/C-FULL)، AT تفکیک‌شده، AT06 (و AT09/10/14، جزئی AT08/12/13)، Stage/متوقف‌سازی | 29.7، 29.10، 29.12 | **Resolved** (طراحی) |
| R21-04 | شمارش منابع | بازنویسی فصل ۱۳: دید ESXi و دید PNetLab-Internal؛ بدون شمارش مضاعف نِستد؛ فرض‌ها/Reserve/Headroom | 13 | **Partially Resolved** (اعداد برآورد) |
| R21-05 | Runbookهای اجرایی | ۵۰ سناریو با ۲۳ فیلد اختصاصی؛ TS42/43/44/48 بسط؛ ۱۰ تفصیلی با پاورقی | 25، پیوست A | **Partially Resolved** |
| R21-06 | Management Plane Cisco | VLAN10، IP سوئیچ‌ها، SVI، `ip default-gateway`، مالک GW=FGT، Jump، Console، دیاگرام | 14.5 | **Resolved** (طراحی) |
| R21-07 | منابع/Featureهای نسخه‌محور | Reference Log 15 ردیف با ناشر/محصول/ادعا؛ ماتریس FortiOS و Cisco دسته‌بندی‌شده | 34، 16.8، 12.2 | **Partially Resolved** |

## ۲. تغییرات مهم محتوایی
- **تغییر نسخه/Document Control/Changelog** (فصل ۱ و ۳۶) و Traceability جدید (۳۷).
- **زمان‌بندی:** فقط روز D اضافه شد (۳۶۰ دقیقه)؛ جمع هفتگی ۲۱۶۰ و جمع دوره ۸۶۴ ساعت **با اسکریپت** دوباره تأیید شد.
- **Verified تازه:** CML FAQ v2.10 (IOSv 512 MB، IOSv-L2 768 MB؛ لایسنس CML)، PNETLAB «VMware ESXi 6.0 or later»، روش Expose Hardware-Assisted Virtualization (vSphere 7.0 Broadcom). پشتیبانی رسمی VMware از Nested Hypervisor ثالث `Inferred` ثبت شد.

## ۳. مسائل حل‌نشده / نیازمند تأیید واقعی
- منابع واقعی میزبان؛ Tier؛ RAM واقعی FortiGate/Windows؛ نسخه‌های ESXi/PNetLab (0A).
- محدودیت‌های Evaluation FortiGate-VM 7.0.3؛ HA/VDOM/FortiGuard؛ سینتکس 7.0.3 (SD-WAN، Debug-Flow، NTP، HA، FSSO)؛ SSL-VPN Modes — همه `Unverified`.
- Featureهای IOSvL2 (Snooping/DAI/SPAN/EPC/LACP/HSRP) و رفتار `ip default-gateway` در Image.
- افزودن Image FortiGate در PNetLab؛ Nested (اجرای QEMU روی ESXi) و لایسنس Image Cisco خارج CML.
- ۱۹ فیلد کوتاه در Runbookها (از ۱۰۵۰) باید در Lesson Build با خروجی واقعی کامل شود؛ خروجی‌های «مورد انتظار» **مثال** هستند، نه نتیجه Lab.

## ۴. نیازمند تأیید کاربر
Q1 (Gateway اصلی Capstone=FGT)، Q11 (گزارش 0A و اجازه 0B)، Q12 (کلاس‌های تکمیل Capstone)، Tier هدف، روش اتصال VM، پذیرش Plan B حذف‌شده (مدت ثابت).

## ۵. فرض‌ها
Subnet واقعی `192.168.88.0/24` (`Inferred`)؛ اعداد منابع Nodeها برآورد؛ IPهای مدیریتی سوئیچ‌ها (`.11/.12/.21/.22`) و Jump (`10.10.40.10`) طراحی پیشنهادی.

## ۶. نتایج چک‌لیست QC (۱۷ مورد)
| # | نتیجه | وضعیت |
|---|---|---|
| 1 | جستجوی `192.168.88.4` در کل سند: 0 مورد | PASS |
| 2 | ارجاع به FortiGate جداگانه/مستقل: 3 خط، همه «بیان نبودن/حذف‌شدن» (جدول محیط مرجع، Changelog، Traceability) | PASS |
| 3 | جستجوی OPNsense: 0 مورد | PASS |
| 4 | IPهای 192.168.88.x: ['192.168.88.0/24', '192.168.88.199', '192.168.88.3']؛ همه ارجاعات .199 مربوط به PNetLab: False | PASS |
| 5 | ESXi=192.168.88.3 (11 ارجاع) بدون مقدار دیگر | PASS |
| 6 | MikroTik/WireGuard: جدول 10.0 مسیر مدیریتی خارجی و جدا از WAN/VPN/توپولوژی؛ تغییر ممنوع | PASS |
| 7 | جمع هفتگی همه ۲۴ هفته=۲۱۶۰ دقیقه؛ جمع کل=864 ساعت | PASS |
| 8 | تعداد Runbook در پیوست A: 50 | PASS |
| 9 | هر Runbook {23} فیلد؛ فیلدهای اختصاصی بسیار کوتاه (<14 نویسه، به‌جز حوزه/دشواری): 19 مورد از 1050 — محتوا اجرایی ولی بخشی مختصر؛ خروجی‌ها بدون تأیید Lab | PASS |
| 10 | Runbook تفصیلی (DR): 10 | PASS |
| 11 | فصل ۱۳: دو دید جدا؛ Σ نودها داخل PNetLab فقط در «دید داخلی»؛ بررسی دستی جمع‌ها: T1 18.25+3.5=21.75→×1.2=26.1≤28؛ T2 21+3.5=24.5→29.4≤32؛ T3 30.5+4=34.5→41.4≤48؛ میزبان: 35/48/83–110 GB | PASS |
| 12 | فصل ۲۹.۱۲: T1=C-SEQ، T2=C-DUAL، T3=C-FULL؛ AT06/09/10/14 تعیین‌شده | PASS |
| 13 | Phase 0A/0B با مرز تأیید جدا در 11.0 و قالب روز D | PASS |
| 14 | Management Plane: VLAN10، مالک GW=FGT `10.10.10.1`، `ip default-gateway`، `.254` مدیریتی ندارد | PASS |
| 15 | ماتریس‌ها و منابع: تعداد `Unverified` در سند = 234؛ هیچ ردیف Lab-Verified نیست | PASS |
| 16 | تناقض IP/دستگاه: Gateway مدیریتی یکتا (FGT)؛ `.254` فقط Lab A؛ سوئیچ‌ها .11/.12/.21/.22 | PASS |
| 17 | هیچ اقدام عملیاتی روی زیرساخت انجام نشد (فقط خواندن/نوشتن فایل Markdown و Fetch مستندات عمومی) | PASS |

**تأیید:** هیچ نصب، اتصال، Boot، Import یا تغییری در ESXi/PNetLab/MikroTik/WireGuard انجام نشد. تنها Fetch مستندات عمومی و نوشتن فایل Markdown انجام شد. هیچ درس/Phase 0B شروع نشده است.
