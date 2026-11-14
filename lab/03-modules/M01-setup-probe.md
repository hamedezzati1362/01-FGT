# M01 — آماده‌سازی و تست قابلیت‌ها (30 دقیقه)
**هدف:** Lab بالا بیاید و بفهمیم کدام تمرین‌ها «واقعی» و کدام «مفهومی» هستند.
## گام ۱ (۱۵ دقیقه): ساخت — `02-build-guide.md`
**ثابت کن:** `show vlan brief` روی ACC1 همان VLANهای CORE را دارد؛ HOST1 از SRV1 IP گرفته است.
## گام ۲ (۱۰ دقیقه): Probe — هر خط را اجرا و یک ✔ (کار می‌کند) / ~ (فقط Config) / ✖ (نه) بنویسید
| # | آزمون | دستور | نتیجه‌ی واقعی |
|---|---|---|---|
| 1 | CDP | `show cdp neighbors` روی DIST (باید CORE و ACCها بیایند) | |
| 2 | VTP | روی CORE: `vlan 666` ؛ روی ACC1: `show vlan id 666` ؛ بعد روی CORE `no vlan 666` | |
| 3 | VLAN database | `dir flash:` و `show vtp status` | |
| 4 | Voice VLAN | HOST1 فعال؛ `show mac address-table interface gi0/1` روی ACC1: MAC PC در VLAN 101 و MAC تلفن در VLAN 97 | |
| 5 | Archive | `configure terminal` ← `archive` ← `path flash:archive-` ← `end` ؛ `show archive` | |
| 6 | Replace | `copy running-config flash:probe.cfg` ؛ `configure replace flash:probe.cfg list` | |
| 7 | فرق دو نسخه | `show archive config differences flash:probe.cfg system:running-config` | |
| 8 | TFTP | `copy running-config tftp://192.168.90.11/probe-ACC1.cfg` ؛ روی SRV1 `ls -l /srv/tftp` | |
| 9 | PoE | `show power inline` (انتظار: پشتیبانی نمی‌شود) | |
| 10 | Port-Security اجرا | M04 انجام می‌شود؛ اینجا فقط `show port-security` | |
**قاعده تفسیر:** ✖ در 5/6/7 ← M05 را با جایگزین (diff متنی روی Linux) انجام می‌دهیم. ✖ در 2 ← VTP را مفهومی با نمونه‌ی خروجی بخوانید. ✖ در 4 ← M03 مفهومی.
نتیجه‌ی Probe را برای من Paste کنید تا مسیر کارگاه را متناسب کنم.
## برگشت
`write memory` همه؛ `delete flash:probe.cfg` (اختیاری).
