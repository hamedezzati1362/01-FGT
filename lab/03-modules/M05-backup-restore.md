# M05 — بکاپ و بازیابی کانفیگ (25 دقیقه)
**هدف:** قبل از هر تغییر بکاپ؛ تفاوت دو نسخه را ببینم؛ در لحظه‌ی خطا برگردم.
**هشدار:** این بخش عمداً خطا می‌سازد. فقط روی **Console** کار کنید (نه SSH) و همیشه اول `reload in 10` بگذارید.

## 1) بکاپ دستی (3 دقیقه)
| انجام بده | ثابت کن |
|---|---|
| `CORE# show running-config` و `show startup-config` | دو نسخه؛ `show running-config \| include hostname` |
| تفاوت Running و Startup: `show archive config differences nvram:startup-config system:running-config` | اگر چیزی تغییر کرده بود و `write memory` نشده، تفاوت دیده می‌شود |
| `CORE# write memory` ( = `copy running-config startup-config`) | `[OK]` |
| ذخیره‌ی متن: در Console PNETLab همه‌ی خروجی را کپی و در یک فایل متنی بگذارید. راه تمیزتر از SRV1: `ssh -o KexAlgorithms=+diffie-hellman-group14-sha1 -o HostKeyAlgorithms=+ssh-rsa netadmin@192.168.100.1 "show running-config" > /srv/tftp/CORE-$(date +%Y%m%d-%H%M).txt` | فایل در `/srv/tftp` (گزینه‌های قدیمی لازم‌اند چون IOS قدیمی است) |

## 2) بکاپ داخل دستگاه (4 دقیقه)
```
CORE# copy running-config flash:CORE-20261114-1000.cfg
CORE# dir flash:
CORE# show flash:
CORE# copy flash:vlan.dat flash:vlan.dat.bak      ! VLAN database (VTP Server/Client keeps VLANs here)
```
**ثابت کن:** `dir flash:` هر دو فایل را نشان می‌دهد. اگر `flash:` یا `vlan.dat` وجود ندارد (Probe #3) جایگزین: `show vlan brief` را در فایل متنی ذخیره کنید و VLANها را از روی `configs/base/CORE.cfg` بسازید.

## 3) بکاپ روی سرور TFTP (3 دقیقه)
```
CORE# copy running-config tftp://192.168.90.11/CORE-20261114-1000.cfg
CORE# copy tftp://192.168.90.11/CORE-20261114-1000.cfg flash:restored.cfg
```
**ثابت کن:** روی SRV1 `ls -l /srv/tftp`. (مسیر شبکه‌ای: CORE ← Gateway ← VLAN 90؛ اگر خطا داد مسیر `ip default-gateway 192.168.100.254` را ببینید.)

## 4) مقایسه‌ی دو نسخه (3 دقیقه)
```
CORE# show archive config differences flash:CORE-20261114-1000.cfg system:running-config
```
(خطوط با `+` اضافه شده، با `-` حذف‌شده.) جایگزین روی SRV1: `diff -u /srv/tftp/old.cfg /srv/tftp/new.cfg`.

## 5) بازیابی ایمن: Merge در برابر Replace (4 دقیقه)
| روش | دستور | رفتار | کی؟ |
|---|---|---|---|
| Merge | `copy flash:file running-config` | خطوط فایل **اضافه/روی هم** می‌شود؛ چیزهایی که در فایل نیست **نمی‌ماند حذف شود** | اضافه‌کردن بخش تنظیم؛ بازگرداندن چند خط |
| Replace | `configure replace flash:file force` | running-config **دقیقاً مثل فایل** می‌شود (هرچه نیست پاک) | برگشت کامل بعد از اشتباه |
| Replace امن | `configure replace flash:file force time 5` سپس `configure confirm` | اگر تأیید نکنید خودش برمی‌گردد | تغییر راه‌دور |
**شبکه‌ی ایمنی همیشگی:** `reload in 10` قبل از کار خطرناک؛ اگر درست شد `reload cancel`.
(اگر `configure replace` پذیرفته نشد [Probe #6]: `copy flash:file startup-config` سپس `reload` یا Merge دستی.)

## 6) Config Archive (3 دقیقه)
```
CORE(config)# archive
CORE(config-archive)# path flash:archive/CORE-
CORE(config-archive)# maximum 10
CORE(config-archive)# time-period 1440
CORE(config-archive)# write-memory
CORE# show archive
```
هر `write memory` یک نسخه‌ی شماره‌دار می‌سازد؛ `archive config` دستی هم می‌شود.

## 7) نام‌گذاری و نگهداری
`<سوییچ>-<yyyyMMdd-HHmm>.cfg` (مثل `ACC1-20261114-1000.cfg`)؛ حداکثر ۱۰ نسخه؛ **بیرون از مخزن کد** (در واقعیت Hash رمز، Community و کلید دارد). در این ریپو فقط نمونه‌ی Lab (رمز نمونه) هست.

## سناریو (25 دقیقه کل بخش، ترتیب انجام)
**الف) بکاپ:** از CORE و ACC1: `copy running-config flash:...` + TFTP.
**ب) اشتباه عمدی:** روی DIST (Console):
```
DIST# copy running-config flash:DIST-before-mistake.cfg
DIST# show interfaces trunk | include Gi0/1          ! notes: allowed list BEFORE
DIST# reload in 10
DIST(config)# interface gi0/1
DIST(config-if)# switchport trunk allowed vlan 150     ! NO "add": replaces the list
DIST# show interfaces trunk                          ! only 150 allowed -> ACC1 and its users lose everything
```
**ثابت کن:** `show vlan brief` در ACC1 هنوز VLANها را دارد ولی HOST1 دیگر IP ندارد و `ping 192.168.100.11` از CORE جواب نمی‌دهد.
**پ) برگشت:**
```
DIST# configure replace flash:DIST-before-mistake.cfg list    ! preview of changes
DIST# configure replace flash:DIST-before-mistake.cfg force
DIST# show interfaces trunk                          ! compare with "BEFORE"
DIST# reload cancel
```
**ت) VTP/VLAN:** روی CORE حذف اشتباهی `no vlan 105` (AP ها inactive می‌شوند). بازسازی: (۱) `vlan 105` ← `name WIFI-AP` (از بکاپ/Config) یا (۲) `copy flash:vlan.dat.bak flash:vlan.dat` سپس `reload`. ثابت کن: `show vlan id 105` روی ACC1. (سناریوی «Revision بالا» همین را در M07 با سوییچ دست‌دوم می‌سازد.)
**ث) ثبت دو خطی:** `show archive config differences flash:DIST-before-mistake.cfg system:running-config` ← بنویسید: «چه چیزی عوض شد؟ کی برگشتم؟».

## چک‌لیست «قبل از هر تغییر» (۶ مورد)
1. وضعیت فعلی را یادداشت کن (`show ...` مربوطه + ذخیره‌ی متن).
2. بکاپ بگیر: `copy running-config flash:<نام>-<تاریخ>.cfg` (+ TFTP).
3. راه برگشت را بنویس (دستور معکوس یا فایل بکاپ).
4. `reload in 10` اگر ممکن است ارتباط خودت قطع شود؛ از Console/موازی کار کن.
5. تغییر را مرحله‌به‌مرحله و با راستی‌آزمایی بعد از هر گام بزن.
6. تست نهایی؛ سپس `write memory` و `reload cancel`.
