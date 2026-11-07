# Decisions & Change Log (خلاصه گفتگو و تصمیم‌ها)

> این فایل با هر مرحله به‌روز می‌شود و همراه بقیه تغییرات در `main` ادغام می‌شود. **رمزها هرگز ثبت نمی‌شوند.**

## تصمیم‌های کلیدی
- دوره: ۲۴ هفته × ۶ روز × ۶ ساعت = ۸۶۴ ساعت مفید؛ Cisco CCNA-level + FortiGate 7.0.3 + Windows/Linux + Monitoring + Capstone (HQ + ۳ شعبه). سند: `Enterprise_Network_Security_Course_Master_Blueprint_v2.1.md`.
- معماری اصلی Capstone: FortiGate = Gateway همه VLANها؛ Cisco Core L3 فقط Lab A مستقل.
- Phase 0A (Read-Only) انجام شد: `phase0a/Phase0A_Report.md`. **Phase 0B با تأیید صریح کاربر (2026-11-07: «Phase 0B تأیید است») شروع شد؛ فهرست مجاز: Snapshot Baseline، تغییر رمزهای پیش‌فرض PNetLab، NTP، افزایش منابع VM (16 vCPU، 48 GB) و گسترش LVM، Lab آزمایشی IOSv/IOSvL2، تست Capture/Backup/Isolation. FortiGate تا W9 Boot نمی‌شود.**
- FortiGate: Evaluation؛ کاربر خودش بکاپ/Restore و مدیریت تاریخ پایان را انجام می‌دهد؛ Claude فقط راهنمای بکاپ/بازگردانی و هشدار تاریخ (`phase0a/fortigate_eval_tracker.md`).
- ریسک پذیرفته‌شده (کاربر، 2026-11-02): Lab تستی است؛ اینترنت از MikroTik؛ NAS دوکارته مجاز است.
- ریسک پذیرفته‌شده (کاربر، 2026-11-07): `sshClient` (SSH خروجی ESXi) همیشه باز؛ با خط `esxcli … sshClient --enabled=true` در `/etc/rc.local.d/local.sh` (+ `auto-backup.sh`). Secure Boot غیرفعال است (`Disabled`) پس `local.sh` اجرا می‌شود. بعد از اولین ریبوت واقعی بررسی شود.
- **جایگذاری (تصمیم کاربر، 2026-11-02): Windows/Linux (DC، Client، Web، MON، NAS) روی ESXi به‌صورت VM مستقل؛ فقط Nodeهای شبکه (Cisco، FortiGate، ISP-Sim) داخل PNetLab.** دلیل: کارایی بالاتر و حذف لایه Nested. اتصال به Lab از طریق `PG-FGT-TRUNK` یا Port Group تک‌VLAN در صورت نیاز.
- Golden Image: روی ESXi (VM آماده خاموش، پوشه `_GOLD` در `ds01-ssd`)؛ نسخه Export روی هارد 1 TB. ترتیب: Ubuntu 22.04 → Windows Server 2025 (≈W4) → Windows 10/11 (≈W12). Windows 11 روی ESXi مستقل بدون Key Provider vTPM ندارد → پیشنهاد Windows 10.
- فرمت دیسک خارجی 1 TB: ext4 (برای NAS VM) یا NTFS (اگر مستقیم به ویندوز).
- قالب درس: `course/Enterprise_Network_Course_Lessons.html` (منوی راست، فونت/اندازه، ۳ تم، مرور اشتباهات).

## Change Records
| ID | شرح | وضعیت |
|---|---|---|
| CHG-0001 | `vSwitch-FGT` (بدون Uplink) + `PG-FGT-TRUNK` (VLAN 4095)؛ اتصال ۲ کارت PNetLab | موفق |
| CHG-0002 | VM `NAS-BKP1` (Ubuntu Server 22.04، 2 vCPU، 4 GB، 40 GB Thin، `VM Network` + `PG-FGT-TRUNK`)؛ تلاش با `.vmx` دستی ناموفق؛ ساخت با Wizard | **موفق**: Ubuntu 22.04.5، IP `192.168.88.198`، یوزر `admin1`، کارت دوم بدون IP |
| CHG-0003 | Golden Ubuntu `GOLD-UBU2204` (کپی دیسک NAS، DHCP، پاک‌سازی machine-id؛ Unregister و دیسک `chmod 444` در `ds01-ssd`) | موفق |
| CHG-0004 | هارد A-DATA HD720 (931.5 GB، NTFS برچسب `COURSE-BACKUP`، GPT) → USB Passthrough (USB 3) به `NAS-BKP1`؛ مانت `/srv/backup` با UUID در `fstab` (`nofail`)؛ اشتراک Samba `\\192.168.88.198\backup` (یوزر `admin1`) | موفق؛ تست نوشتن/حذف از ویندوز OK |

## Phase 0B — Change Records
| ID | شرح | وضعیت |
|---|---|---|
| CHG-0005 | Snapshot Baseline VM `PNETLAB` (`baseline-pre-0B`، بدون Memory، VM خاموش) | **موفق** |
| CHG-0006 | افزایش منابع VM PNETLAB (16 vCPU، 48 GB RAM؛ `nproc=16`، `free=47G`، `/dev/kvm` OK) | **موفق** |
| CHG-0007 | گسترش LVM داخل PNetLab (`parted Fix` GPT، `growpart`، `pvresize`، `lvextend -r`؛ `/` از 97G به 196G) | **موفق** |
| CHG-0008 | تغییر رمزهای پیش‌فرض PNetLab (root و Web) + NTP | برنامه |


| CHG-0009 | ساعت ESXi (2001 → 2026-11-07): تنظیم دستی ساعت، NTP=`192.168.88.1` (MikroTik)، `ntpd` فعال، `auto-backup.sh` | **موفق** (Sync نهایی در انتظار تأیید) |

- `phase0a/pnetlab_inventory.md`: Inventory Imageها/Templateها و پیش‌فرض منابع PNetLab (IOSv/IOSvL2/Fortinet).

- `phase0a/cisco_feature_probe.md`: نتایج Feature-Probe Cisco. SW1: VLAN/Trunk/PVST `Tested-OK`؛ DHCP-Snooping/DAI/SPAN `CLI-Accepted` (عملکرد باید جداگانه تست شود).

## Runbookها
- `phase0a/Golden_W2025_Runbook.md` — ساخت Golden ویندوز سرور 2025 و Clone از آن.

## درس‌های ثبت‌شده برای مرور
Port Group حذف‌شده = کارت بدون شبکه؛ Save با لیست خالی؛ `ethX ≠ Adapter N` (MAC)؛ چسباندن چند خط در ترمینال؛ `<ID>` یعنی مقدار واقعی؛ `.vmx` دستی بدون Slotهای PCI کار نمی‌کند.

## Golden Windows (2026-11-05)
- `GOLD-W2025-GUI` (Vmid 8) و `GOLD-W2025-CORE` (Vmid 9) روی `ds02-ssd`: نصب، VMware Tools، Windows Update، RDP فعال + `SetupComplete.cmd` (شبکه امنیتی RDP پس از Sysprep).
- قبل از Sysprep: کپی `*-PRE` (Thin) روی `ds01-ssd` برای آپدیت‌های بعدی؛ بعد از Sysprep: VM خاموش، Unregister، دیسک‌ها `chmod 444` (فقط‌خواندنی).
- هارد خارجی A-DATA (USB 3) در Passthrough ناپایدار بود (I/O error، Hardware Error)؛ `usb.mangleUsb3Speed` اضافه شد؛ هارد از VM جدا؛ بررسی فیزیکی توسط کاربر (غروب).
- SSH host key ESXi تغییر کرد؛ با `ssh-keyscan` از NAS تأیید شد (ECDSA `vj79w7…`)؛ کلید قدیمی در Nexa حذف شد.

- **2026-11-05:** Sysprep روی `GOLD-W2025-CORE` و `GOLD-W2025-GUI` کامل شد (VM خودکار خاموش شد؛ ارتباط ریموت در حین Sysprep قطع می‌شود و طبیعی است). هر دو Unregister و دیسک‌ها `chmod 444`. نسخه‌های `*-PRE` روی `ds01-ssd` (Thin). Golden‌های آماده: `GOLD-UBU2204`، `GOLD-W2025-GUI` (90 GB)، `GOLD-W2025-CORE` (40 GB). VM `GOLD-Win11` (Vmid 10) توسط کاربر ساخته شده؛ هنوز Golden نشده.
- درس: «Sysprep چند دقیقه طول می‌کشد؛ قطع ریموت یعنی در حال اجرا است؛ ریست نکنید».

- **2026-11-06 — هارد A-DATA HD720:** در ESXi/NAS (Passthrough) `Hardware Error`، Timeout 180s، `0B` ؛ در ویندوز Event 7 (bad block)، 153، 51؛ Spin up کند؛ `clean all`/تعمیر موفق نبود. **نتیجه: دیسک خراب، کنار گذاشته شد.** `NAS-BKP1` خاموش؛ جایگزین: دیسک مجازی روی SSD یا هارد جدید (در انتظار تصمیم).
- `GOLD-Win11` (Vmid 10): نصب، آپدیت و VMware Tools انجام شد؛ مراحل Golden (RDP، SetupComplete، PRE، Sysprep، Unregister، chmod 444) در حال انجام.

- **2026-11-07 — Golden Windows 11 کامل شد:** `GOLD-Win11` (Vmid 10، `ds02-ssd`) Sysprep شد، Unregister و دیسک‌ها `chmod 444`؛ کپی `GOLD-Win11-PRE` روی `ds01-ssd` (Thin، مصرف واقعی ≈26.4 GB، `Disk chain is consistent`). **همه Golden‌ها آماده:** Ubuntu 22.04، Server 2025 GUI، Server 2025 Core، Windows 11. نکته Clone Win11: ساخت حساب محلی در OOBE (`Shift+F10` → `start ms-cxh:localonly`، `Unverified`).

## موارد باز
- Auto-start `NAS-BKP1`؛ پوشه‌های بکاپ (`configs`، `pnetlab-labs`، `vm-exports`، `iso-images`، `captures-logs`)؛ کپی ISOها و Export Golden؛ SFTP برای بکاپ دستگاه‌ها.
تأیید Phase 0B؛ فرمت و اتصال هارد 1 TB (USB Passthrough به `NAS-BKP1`)؛ Samba/SFTP؛ Tier نهایی؛ Image Validation؛ IP واقعی Subnet/ماسک تأییدشده (`192.168.88.0/24`).
