# Decisions & Change Log (خلاصه گفتگو و تصمیم‌ها)

> این فایل با هر مرحله به‌روز می‌شود و همراه بقیه تغییرات در `main` ادغام می‌شود. **رمزها هرگز ثبت نمی‌شوند.**

## تصمیم‌های کلیدی
- دوره: ۲۴ هفته × ۶ روز × ۶ ساعت = ۸۶۴ ساعت مفید؛ Cisco CCNA-level + FortiGate 7.0.3 + Windows/Linux + Monitoring + Capstone (HQ + ۳ شعبه). سند: `Enterprise_Network_Security_Course_Master_Blueprint_v2.1.md`.
- معماری اصلی Capstone: FortiGate = Gateway همه VLANها؛ Cisco Core L3 فقط Lab A مستقل.
- Phase 0A (Read-Only) انجام شد: `phase0a/Phase0A_Report.md`. **Phase 0B هنوز با تأیید صریح کاربر شروع نشده.**
- FortiGate: Evaluation؛ کاربر خودش بکاپ/Restore و مدیریت تاریخ پایان را انجام می‌دهد؛ Claude فقط راهنمای بکاپ/بازگردانی و هشدار تاریخ (`phase0a/fortigate_eval_tracker.md`).
- ریسک پذیرفته‌شده (کاربر، 2026-11-02): Lab تستی است؛ اینترنت از MikroTik؛ NAS دوکارته مجاز است.
- فرمت دیسک خارجی 1 TB: ext4 (برای NAS VM) یا NTFS (اگر مستقیم به ویندوز).
- قالب درس: `course/Enterprise_Network_Course_Lessons.html` (منوی راست، فونت/اندازه، ۳ تم، مرور اشتباهات).

## Change Records
| ID | شرح | وضعیت |
|---|---|---|
| CHG-0001 | `vSwitch-FGT` (بدون Uplink) + `PG-FGT-TRUNK` (VLAN 4095)؛ اتصال ۲ کارت PNetLab | موفق |
| CHG-0002 | VM `NAS-BKP1` (Ubuntu Server 22.04، 2 vCPU، 4 GB، 40 GB Thin، `VM Network` + `PG-FGT-TRUNK`)؛ تلاش با `.vmx` دستی ناموفق؛ ساخت با Wizard | نصب در حال انجام (IP `192.168.88.198`، یوزر `admin1`) |

## درس‌های ثبت‌شده برای مرور
Port Group حذف‌شده = کارت بدون شبکه؛ Save با لیست خالی؛ `ethX ≠ Adapter N` (MAC)؛ چسباندن چند خط در ترمینال؛ `<ID>` یعنی مقدار واقعی؛ `.vmx` دستی بدون Slotهای PCI کار نمی‌کند.

## موارد باز
تأیید Phase 0B؛ فرمت و اتصال هارد 1 TB (USB Passthrough به `NAS-BKP1`)؛ Samba/SFTP؛ Tier نهایی؛ Image Validation؛ IP واقعی Subnet/ماسک تأییدشده (`192.168.88.0/24`).
