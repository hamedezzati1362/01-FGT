# Manifest وابستگی‌های بخش ۱ (فصل ۱–۳) — نسخه ۱٫۱
تاریخ: ۲۰۲۶-۱۱-۲۵. مسیرها نسبت به ریشه‌ی مخزن `01-FGT` هستند؛ ساختار پوشه‌ها در ZIP عیناً حفظ شده تا لینک‌های نسبی کار کنند.

## الف) فایل‌های تحویلی
| فایل | نقش |
|---|---|
| `course/Course_Part_01_Chapters_01-03.md` | فایل اصلی بخش ۱ |
| `Enterprise_Network_Security_Course_Master_Blueprint_v3.0.md` | Blueprint اصلی |
| `course/Part01_MANIFEST.md` | همین فایل |

## ب) شکل‌ها (۱۳ فایل SVG، همه در ZIP؛ همه‌ی لینک‌های تصویر معتبرند)
`course/figures/`: ch02-l1-fig1، ch02-l1-fig2، ch02-l2-fig1، ch02-l2-fig2، ch02-l3-fig1، ch02-l5-fig1، ch02-l6-fig1، ch03-l1-fig1، ch03-l2-fig1، ch03-l3-fig1، ch03-l4-fig1، ch03-l5-fig1، ch03-l6-fig1 (پسوند `.svg`).

## ج) وابستگی‌های موجود در مخزن (در ZIP)
| فایل | چرا لازم است |
|---|---|
| `02-design/ip-plan-drill.md` ، `02-design/ip-plan.md` | پاسخ Labهای مستقل ۲-۱ و ۲-۲ |
| `phase0a/cisco_feature_probe.md` | شواهد وضعیت راستی‌آزمایی Labها |
| `phase0a/pnetlab_inventory.md` ، `phase0a/Phase0A_Report.md` | شواهد درس‌های ۱-۰ و ۱-A |
| `phase0a/lab_inventory.md` | Inventory (IP/نام کاربری، **بدون رمز**؛ در صورت اشتراک خارجی بسنجید) |
| `phase0a/esxi_phase0a_readonly.sh` ، `phase0a/pnetlab_phase0a_readonly.sh` | اسکریپت‌های فقط‌خواندنی درس ۱-A |
| `phase0a/FortiGate_Backup_Restore_Runbook.md` ، `phase0a/fortigate_eval_tracker.md` | منابع مرتبط (در پایان بخش ۱ فهرست شده) |
| `course/Enterprise_Network_Course_Lessons.html` | منبع محتوای تبدیل‌شده (فصل ۱–۸؛ اختیاری برای خواندن) |
| `Enterprise_Network_Security_Course_Master_Blueprint_v2.1.md` | مرجع Blueprint v3.0 (اختیاری) |
| `DECISIONS_LOG.md` ، `CLAUDE.md` | تصمیم‌ها و قوانین |
| `tools/check_part.py` | اسکریپت کنترل |

## د) فایل‌هایی که **هنوز وجود ندارند** (خروجی‌هایی که دانشجو در Labها می‌سازد؛ در ریپو نیستند و عمداً در ZIP نیستند)
`01-discovery/as-is.drawio` ، `01-discovery/as-is.md` ، `inventory.md` ، `02-design/ipv6-plan.md` ، `02-design/vlan-matrix.md` ، `03-ops/change-and-rollback.md` ، `03-ops/secure-mgmt-standard.md` ، `03-ops/ts14-gateway-wrong.md` ، `03-ops/l2-cam-notes.md` ، `03-ops/trunk-change.md` ، `03-ops/add-vlan-runbook.md` ، `03-ops/roas-vs-svi.md` ، `03-ops/rca-w3.md`.
این‌ها «مستندات نهایی» کارت‌های Lab هستند و پس از اجرای Lab توسط شما تولید می‌شوند.

## هـ) ارجاع‌های کوتاه
`cisco_feature_probe.md` ، `lab_inventory.md` ، `pnetlab_inventory.md` ، `fortigate_eval_tracker.md` داخل متن بدون پوشه آمده‌اند؛ همگی در `phase0a/` هستند.

## و) وضعیت کنترل
`python3 tools/check_part.py course/Course_Part_01_Chapters_01-03.md` ← لینک داخلی: ۳۹ ، شکل: ۱۳ ، پاسخ: ۱۲۰ از ۱۲۰ ، HTML خام: ۰ ، حرف فارسی در بلوک کد: ۰ ← **OK**.
