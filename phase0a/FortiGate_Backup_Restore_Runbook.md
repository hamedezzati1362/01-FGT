# Runbook — بکاپ و بازگردانی تنظیمات (FortiGate 7.0.3 و Cisco در PNetLab)

> همه فرمان‌ها/مسیرهای GUI `Unverified` تا اجرا روی Image واقعی (Phase 0B). بکاپ‌ها حاوی رمز/PSK/کلید هستند: **رمزگذاری کنید و داخل Git عمومی نگذارید.**

## ۱. چه چیزی و چه وقت
| چه زمانی | چه چیزی |
|---|---|
| پایان هر Lab | Config هر FortiGate + هر دستگاه Cisco |
| قبل از هر Change | همان (Pre-check) |
| ۳/۲/۱ روز قبل از پایان مهلت هر FortiGate | بکاپ کامل + Export توپولوژی PNetLab |

## ۲. FortiGate — بکاپ
**GUI:** منوی کاربر بالا راست → **Configuration → Backup** → Local PC → **Encryption: Enable** (رمز را جداگانه نگه دارید) → OK.

**CLI (به یک سرور TFTP/SFTP داخل Lab):**
```text
execute backup config tftp <filename.conf> <tftp-server-ip> <encryption-password>
execute backup config sftp <filename.conf> <sftp-server-ip> <user> <password>
```
نام فایل: `<LabID>_<Device>_<YYYYMMDD>_<vN>.conf` (مثلاً `L51_HQ-FGT-01_20261201_v1.conf`).

## ۳. FortiGate — بازگردانی
1. نقطه شروع: همان نسخه Firmware (7.0.3) و **همان تعداد/ترتیب Interfaceها** (port1…portN) که بکاپ از آن گرفته شده.
2. از کنسول PNetLab یک IP مدیریتی حداقلی به یک Interface بدهید تا GUI/SFTP در دسترس شود.
3. **GUI:** Configuration → **Restore** → فایل بکاپ (و رمز رمزگذاری) → OK. **CLI:**
```text
execute restore config tftp <filename.conf> <tftp-server-ip> <encryption-password>
```
4. دستگاه ریبوت می‌شود؛ بعد از بالا آمدن: ورود با رمز Admin **موجود در بکاپ**.
5. Verification: `get system status`، `get system interface physical`، `get router info routing-table all`، Policyها و Hit Count، وضعیت VPN (`diagnose vpn tunnel list`)، لاگ.
6. اگر Interface کمتر/متفاوت بود، تنظیمات آن Interface از بین می‌رود → قبل از Restore Interfaceها را در PNetLab مطابق کنید.

## ۴. Cisco (IOSv/IOSvL2)
- پیش از بکاپ: `copy running-config startup-config`.
- بکاپ: `show running-config` را با Netmiko/اسکریپت یا `copy running-config tftp:` به فایل بریزید (فصل ۳۲).
- بازگردانی: `configure replace` یا چسباندن Config روی Node تازه (بعد از ساخت مجدد Interfaceها). Verification: `show ip interface brief`، `show vlan brief`، `show ip route`.

## ۵. PNetLab
- Export هر Lab از منوی Lab (فایل zip) و ذخیره خارج از ESXi.
- Snapshot VM PNetLab در ESXi قبل از تغییرات بزرگ (با تأیید و Rollback مکتوب).

## ۶. Restore Drill
هر چند هفته یک بار بکاپ را روی یک Node آزمایشی برگردانید و مقایسه کنید (`git diff` روی Config متنی). **بکاپی که Restore نشده باشد، بکاپ نیست.**
