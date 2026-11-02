# گزارش Phase 0A — Read-Only Discovery
**تاریخ:** 2026-11-02  **روش:** خروجی اسکریپت‌های فقط‌خواندنی که کاربر اجرا کرد  **تغییر توسط Claude:** هیچ

## ۱. ESXi
| مورد | مقدار |
|---|---|
| نسخه | VMware ESXi **8.0 Update 2** (build 22380479) |
| سخت‌افزار | HPE ProLiant DL360 Gen9 |
| CPU | 2 سوکت × Xeon E5-2680 v4 @2.4GHz، **28 Core / 56 Thread**، HT فعال، 2 NUMA Node |
| RAM | ≈ **256 GB** (274,741,637,120 B)؛ مصرف فعلی ≈ 6 GB |
| Datastore | `ds01-ssd` 348.8G (آزاد 330.8G) · `ds02-ssd` 476.8G (آزاد 408.2G) · `OSDATA` 119.8G · BootBank |
| شبکه | `vmnic0` روی `vSwitch0` (Port Groupها: `Management Network`، `VM Network`)؛ `vmk0` = `192.168.88.3/24` (Static، GW `192.168.88.1`)؛ **`vSwitch-FGT`** بدون Uplink با `PG-FGT-TRUNK` (VLAN 4095) — CHG-0001 |
| VMها | فقط **PNETLAB** (12 vCPU، 24 GB RAM، 200 GB روی `ds02-ssd`، `nestedHVEnabled=true`) |
| Snapshot | **ندارد** |
| ساعت | همگام (UTC 11:46) |

## ۲. PNetLab
| مورد | مقدار |
|---|---|
| نسخه | `pnetlab 4.2.8` روی Ubuntu 18.04.5 (کرنل `4.15.18-pnetlab2`) |
| Nested | `vmx` فعال، `/dev/kvm` و `kvm_intel` → **QEMU Node قابل اجرا** |
| منابع | RAM 24 GB (≈22.6 GB آزاد)، Swap 4 GB؛ `/` = 97G (80G آزاد) از دیسک 200G؛ **≈100 GB در LVM تخصیص‌داده‌نشده** (`VFree 0` در VG، یعنی باید دیسک/PV گسترش یابد) |
| شبکه | `pnet0` (از `eth1`) = `192.168.88.199/24`، GW `192.168.88.1`؛ `pnet1` (از `eth0`) = لوله `PG-FGT-TRUNK`؛ `nat0` = `10.0.137.254/24`؛ `docker0` = `10.177.0.1/16` (بدون هم‌پوشانی با IP Plan) |
| زمان | **همگام نیست** |
| سرویس‌ها | apache2، mysql، docker، ssh فعال؛ هیچ Node اجرا نیست |
| Imageها | QEMU: IOSv `vios-…159-3.m9`، IOSvL2 `viosl2-…high_iron_20200929`، CSR1000v 17.03.02، **`fortinet-7.0.3`** (هدف) و `fortinet-6.46`. IOL: چند Image. Dynamips: c7200 |
| منبع Image | کاربر تأیید کرد: همه از منابع مجاز؛ **فقط FortiGate به‌صورت Evaluation** (15 روز) — مدیریت تاریخ/بکاپ با خود کاربر |
| ملاحظه | Ubuntu 18.04 دوره پشتیبانی استاندارد را تمام کرده (`Inferred`) → PNetLab فقط ایزوله و بدون Exposure اینترنتی |

## ۳. تحلیل Tier (Inferred — طبق فصل ۱۳)
| معیار | وضعیت | نتیجه |
|---|---|---|
| RAM میزبان ≈ 256 GB | بسیار بیشتر از آستانه T3 (≥ 96 GB) | ✔ **T3 از نظر RAM/CPU** |
| CPU 56 Thread | کافی برای 16–20 vCPU PNetLab + VMهای مستقل | ✔ |
| Storage آزاد ≈ **738 GB** (330.8 + 408.2) | T3 به ≈ 0.8–1.2 TB نیاز دارد (برآورد) | ⚠ **محدودکننده**؛ با Thin Provisioning و بدون FMG/FAZ تقریباً قابل‌قبول |
| PNetLab فعلی (24 GB RAM) | زیر T2 (32 GB) و T3 (48 GB) | نیاز به افزایش منابع (تغییر) |

**پیشنهاد:** Tier **T3 برای محاسبه** (HA مشروط به Image/License) با **مراقبت از Storage** (Thin، حذف FMG/FAZ یا مفهومی). تا تأیید شما، هدف رسمی همان طراحی T3 با علامت «Storage-limited» است.

## ۴. ریسک‌ها / موارد `Unverified`
- شرایط Evaluation FortiGate 7.0.3 و لحظه شروع ساعت 15 روزه (در Boot یا فعال‌سازی) — `Unverified`.
- رفتار IOSvL2 برای DAI/Snooping/SPAN و … — Image Validation.
- `nat0` (NAT Cloud) می‌تواند Lab را به شبکه واقعی وصل کند → استفاده نشود مگر با مرز مستند.
- رمز پیش‌فرض PNetLab (روی بنر) → تغییر در 0B.
- IOL/`CiscoIOUKeygen.py`: در دوره استفاده نمی‌شود.

## ۵. فهرست پیشنهادی Phase 0B (نیازمند تأیید صریح شما)
| # | تغییر | تأثیر/Rollback |
|---|---|---|
| 1 | Snapshot VM PNETLAB (Baseline) قبل از هر تغییر | فضای Datastore؛ حذف Snapshot |
| 2 | تغییر رمزهای پیش‌فرض PNetLab (root و Web) | باید در جای امن ثبت شوند |
| 3 | تنظیم NTP روی PNetLab | برگشت Config |
| 4 | افزایش منابع VM PNETLAB (پیشنهاد: **16 vCPU، 48 GB RAM**) + گسترش دیسک/LVM | **نیاز به Power-off**؛ برگشت با Snapshot |
| 5 | ساخت Lab آزمایشی ایزوله و Boot Nodeهای **IOSv/IOSvL2** و Feature-Probe | حذف Lab |
| 6 | **FortiGate:** Boot/تست **به تعویق تا W9** (برای عدم شروع ساعت Evaluation) — مگر شما خلافش را بگویید | — |
| 7 | تست L2/L3/Capture و Backup/Restore (Export Lab) | — |
| 8 | تست Isolation و ثبت `M0` | — |

**هیچ‌یک از این‌ها اجرا نشده است. برای شروع Phase 0B لطفاً صریح تأیید کنید (کامل یا با اصلاح).**
