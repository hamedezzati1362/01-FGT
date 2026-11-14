# M02 — پایه، VLAN، VTP، Trunk (40 دقیقه)
قالب: **انجام بده ← با این دستور ثابت کن.** (ف = فقط‌خواندنی، ت = تغییر)

## A) شناخت (8 دقیقه)
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | روی ACC1 در `ACC1>` هستید؛ `enable` | Prompt می‌شود `ACC1#` (EXEC کاربر `>` ← Privileged `#` ← Config `(config)#`) |
| 2 ف | `show ?` سپس `show vl?` و `show vlan ?` | فهرست گزینه‌ها؛ Tab کلمه را کامل می‌کند |
| 3 ف | `show interfaces status` ؛ `show interfaces status \| include connected` | فقط پورت‌های وصل |
| 4 ف | `show running-config \| section interface GigabitEthernet0/1` | فقط همان Interface |
| 5 ف | `show cdp neighbors` ؛ `show cdp neighbors detail \| include Device\|Interface\|IP` | ACC1 فقط DIST را در `Gi0/0` می‌بیند |
| 6 ف | `show version \| include uptime\|Version` | Uptime و نسخه |
**مثال واقعی:** تیکت «میز ۴ اینترنت ندارد» ← اول `show interfaces status | include Gi0/4` (connected/notconnect/err-disabled؟).
**اشتباه رایج:** دستور Config را در `#` زدن؛ بعد از `enable` فقط یک‌بار `configure terminal`. کلمه‌ی اشتباه در EXEC ← DNS Lookup («Translating...»)؛ با `no ip domain-lookup` (در Base هست) این مشکل ندارید.

## B) پیدا کردن دستگاه از روی MAC (7 دقیقه)
سناریو: MAC تلفن/PC میز Ali را داریم (روی HOST1 `ip link show eth0` ← `02:aa:00:00:01:01`) و نمی‌دانیم کجاست.
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | `CORE# show mac address-table address 02aa.0000.0101` | پورت `Gi0/1` (به سمت DIST) |
| 2 ف | `DIST# show mac address-table address 02aa.0000.0101` | پورت `Gi0/1` (به ACC1) |
| 3 ف | `DIST# show cdp neighbors \| include Gi0/1` | همسایه ACC1 |
| 4 ف | `ACC1# show mac address-table address 02aa.0000.0101` | پورت `Gi0/1` و VLAN 101 |
| 5 ف | `ACC1# show running-config interface gi0/1` | توضیح `PC-Ali+Phone` |
قاعده: **از بالا (هسته) به پایین با CDP پیش بروید تا پورتی که MAC روی آن «کابل کاربر» است** (پورتی که پشتش سوییچ دیگری نباشد).

## C) VLAN و VTP (15 دقیقه)
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | `CORE# show vtp status` | Mode Server، Domain lab.local، Version 2، Revision (عدد را یادداشت کنید) |
| 2 ت | **فقط روی CORE:** `vlan 106` ← `name GUEST-NEW` | `show vlan brief` روی CORE |
| 3 ف | `ACC2# show vlan id 106` | VLAN روی کلاینت هم آمد (VTP) و Revision روی CORE یکی بیشتر شد |
| 4 ت | روی ACC2 (Client) `vlan 107` بزنید | خطا: Client اجازه‌ی ساخت VLAN ندارد (`VTP VLAN configuration not allowed when device is in CLIENT mode`) |
| 5 ت | `CORE# no vlan 106` | حذف از همه‌ی کلاینت‌ها |
**نکته‌ی واقعی (2960):** در حالت VTP Server/Client، VLANها در `vlan.dat` ذخیره می‌شوند نه در running-config. پس `show running-config` را برای VLAN نگاه نکنید؛ `show vlan brief` و `dir flash:vlan.dat`.
**چرا سوییچ دست‌دوم خطرناک است؟** اگر Domain/Password یکسان و Revision بالاتر باشد، VLANهای کل شبکه را با دیتابیس خودش جایگزین می‌کند. قبل از وصل: `vtp mode transparent` یا `delete flash:vlan.dat` + `reload`. (تمرینش در M07.)

## D) Trunk و `add` (10 دقیقه)
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | `DIST# show interfaces trunk` | چهار بخش: Mode/Native، Allowed، Allowed&active، Forwarding |
| 2 ف | `DIST# show interfaces gi0/1 trunk` | |
| 3 ت | **قبل از تغییر:** `copy running-config flash:DIST-before-trunk.cfg` | `dir flash:` |
| 4 ت | `reload in 10` (شبکه‌ی ایمنی) | `show reload` |
| 5 ت | `interface gi0/1` ← `switchport trunk allowed vlan add 106` | `show interfaces trunk`: 106 به لیست اضافه شد |
| 6 ت | `reload cancel` | `show reload` = No reload |
**خطای مشهور (آموزشی؛ فقط روی Lab):** `switchport trunk allowed vlan 106` **بدون add** ← کل لیست جایگزین می‌شود و بقیه‌ی VLANها قطع می‌شوند. (در M05 عمداً می‌زنیم و برمی‌گردانیم.)
**Native VLAN 1:** ضعف شناخته‌شده؛ با `show interfaces trunk` ستون Native را ببینید.

## برگشت به حالت اولیه
`CORE(config)# no vlan 106` و اگر allowed را تغییر دادید: `switchport trunk allowed vlan remove 106` سپس `write memory`.
