# M04 — Port-Security، پورت‌های بلااستفاده، سرعت/دوپلکس (25 دقیقه)

## A) Port-Security (12 دقیقه)
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | `ACC3# show port-security interface gi0/1` | Max=3، Violation=Shutdown، Sticky، MAC فعلی |
| 2 ف | `ACC3# show port-security address` | MACهای Sticky (PC و Phone) |
| 3 ت | روی HOST3 MAC سومی اضافه کنید (دستگاه مهمان): `ip link add link eth0 name eth0.5 type macvlan` سپس `ip link set eth0.5 address 02:cc:00:00:03:55` و `ip link set eth0.5 up` و `arping -I eth0.5 -c3 192.168.107.254` (یا ping) | هنوز زیر سقف 3 هستید: `show port-security interface gi0/1` ← Total MAC = 3 |
| 4 ت | یک MAC چهارم: `ip link add link eth0 name eth0.6 type macvlan` ؛ `ip link set eth0.6 address 02:cc:00:00:03:56` ؛ `ip link set eth0.6 up` ؛ `arping -I eth0.6 -c3 192.168.107.254` | **Violation** ← `show interfaces status err-disabled` و لاگ `%PORT_SECURITY-2-PSECURE_VIOLATION` |
| 5 ت | بازیابی: مهمان‌ها را حذف کنید `ip link del eth0.5; ip link del eth0.6` ؛ روی سوییچ `interface gi0/1` ← `shutdown` ← `no shutdown` | `show interfaces status \| include Gi0/1` = connected |
| 6 ت | `clear port-security sticky interface gi0/1` | MACهای Sticky قدیمی پاک؛ با ترافیک دوباره یاد می‌گیرد |
**جابه‌جایی میز:** پورت جدید MAC قدیمی را ندارد (مشکلی نیست)؛ پورت قدیمی `clear port-security sticky` و `shutdown`.
**اگر Violation رخ نداد (Probe #10):** در این Image اجرا نمی‌شود؛ مفهوم و دستورها را همین است؛ نمونه‌ی واقعی: `%PM-4-ERR_DISABLE: psecure-violation error detected on Gi0/1, putting Gi0/1 in err-disable state`.
**رفع خودکار (اختیاری، با احتیاط):** `errdisable recovery cause psecure-violation` و `errdisable recovery interval 300`.

## B) پورت‌های بلااستفاده (5 دقیقه)
| وضعیت `show interfaces status` | معنی | علت رایج |
|---|---|---|
| `connected` | کابل و دستگاه | سالم |
| `notconnect` | پورت روشن، کابلی نیست | میز خالی/کابل جدا |
| `disabled` | `shutdown` شده (Admin down) | پورت DISABLED/UNUSED |
| `inactive` | VLAN پورت **وجود ندارد** | VLAN اشتباه/پاک‌شده |
| `err-disabled` | سوییچ خودش خاموش کرد | Port-Security، BPDU Guard، Loop |
**ثابت کن:** `ACC1# show interfaces status` ؛ `ACC1# show running-config interface gi1/0` ← UNUSED و `shutdown`.
**قالب توضیح:** `UNUSED` (آماده‌ی میز جدید، shutdown) و `DISABLED` (عمداً بسته).

## C) سرعت/دوپلکس (8 دقیقه)
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | `ACC2# show interfaces status` | ستون Duplex/Speed: `a-full` `a-1000` (a = auto) |
| 2 ف | `ACC2# show interfaces gi0/1 \| include duplex\|CRC\|collision\|drops` | |
| 3 ف | **روش تفاضل شمارنده (بدون clear):** `show interfaces gi0/1 \| include input errors\|CRC` را بنویسید ؛ ۲ دقیقه صبر ؛ دوباره بنویسید ؛ **تفاضل** مهم است نه عدد کل | اگر تفاضل در حال رشد است، مشکل «الان» است |
**نمونه‌ی واقعی Duplex Mismatch:**
```
Switch# show interfaces status | include Gi1/0/9
Gi1/0/9   PC-Sara    connected  103   a-half  a-100  10/100/1000BaseTX
Switch# show interfaces gi1/0/9 | include CRC|collision
     4821 input errors, 4821 CRC, 0 frame, ...   |   312 late collision
```
`a-half`/`a-100` = یک سمت Force و سمت دیگر Auto. راه‌حل: هر دو Auto (یا هر دو یکسان Force).
**چرا Clear نمی‌کنیم؟** `clear counters` سوابق را پاک می‌کند و بقیه‌ی همکاران هم نمی‌توانند تاریخچه را ببینند.
**در Lab:** فقط `speed`/`duplex` پذیرفته می‌شود؛ شمارنده‌ی CRC تولید نمی‌شود (برخی خرابی‌های سرعت/دوپلکس مفهومی‌اند).
