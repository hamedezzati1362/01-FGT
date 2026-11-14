# M06 — سناریوهای جابه‌جایی میز و تغییر (40 دقیقه)
**قالب تغییر امن (هر سناریو):** یادداشت قبل ← بکاپ ← `reload in 10` ← تغییر ← تست ← `write memory` ← `reload cancel`.

## S1) جابه‌جایی میز: کامپیوتر+تلفن Ali از ACC1 به ACC2 (15 دقیقه)
وضعیت: HOST1 روی ACC1 Gi0/1 (VLAN 101). بعد از جابه‌جایی: ACC2 Gi0/2 (VLAN 103 کال‌سنتر؛ IP عوض می‌شود). رزرو HOST1 در Scope 103 از قبل `192.168.103.61` است.
| گام | انجام بده | ثابت کن |
|---|---|---|
| 1 | یادداشت قبل: `ACC1# show running-config interface gi0/1` ؛ `show mac address-table interface gi0/1` ؛ HOST1 `ip -br addr` | متن را ذخیره کنید |
| 2 | بکاپ: `ACC1# copy running-config flash:ACC1-before-move.cfg` ؛ همین روی ACC2 | `dir flash:` |
| 3 | پورت جدید روی ACC2 (Gi0/2 همین حالا UNUSED/shutdown است): `interface gi0/2` ← `description PC-Ali+Phone` ← `switchport mode access` ← `switchport access vlan 103` ← `switchport voice vlan 97` ← `switchport port-security` ← `maximum 3` ← `mac-address sticky` ← `spanning-tree portfast` ← `no shutdown` | `show running-config interface gi0/2` |
| 4 | کابل: در PNETLab لینک HOST1 به ACC1 Gi0/1 را حذف و HOST1 را به ACC2 Gi0/2 وصل کنید | `show interfaces status \| include Gi0/2` = connected |
| 5 | HOST1: `bash /opt/lab/pc-phone/pc-only.sh` سپس `phone-pc-sim.sh 1` | PC=192.168.103.61 ، Phone=192.168.97.61 |
| 6 | `ACC2# show mac address-table interface gi0/2` | PC در VLAN 103، Phone در VLAN 97 |
| 7 | **تمیزکاری پورت قدیمی ACC1 Gi0/1:** `shutdown` ← `description UNUSED` ← `no switchport port-security mac-address sticky` (پاک‌کردن Sticky: `clear port-security sticky interface gi0/1`) | `show interfaces status \| include Gi0/1` = disabled |
| 8 | `write memory` روی ACC1 و ACC2 ؛ `reload cancel` | |
**برگرداندن:** همین مراحل برعکس؛ یا `configure replace flash:ACC2-before-move.cfg force` روی ACC2.
**نکته‌ی واقعی:** «توضیح پورت قدیمی با دستگاه واقعی نمی‌خواند» ← حتماً در تمیزکاری توضیح را `UNUSED` کنید؛ همین باعث می‌شود بعداً کسی پورت `PC-Ali` را در میز خالی ببیند و گمراه شود.
**رزرو در دو Scope:** `grep pc1 /etc/dhcp/dhcpd.conf` روی SRV1: سه بلوک (101، 103، 107). اگر رزرو در Scope جدید نباشد، IP تصادفی می‌گیرید.

## S2) ساخت VLAN جدید «کامل» (VLAN 106 = GUEST-NEW) (15 دقیقه)
هر مرحله را بزنید و **علامت فراموشی** را نگاه کنید:
| مرحله | دستور | اگر فراموش شود |
|---|---|---|
| 1 | CORE: `vlan 106` ← `name GUEST-NEW` | VLAN روی کلاینت‌ها نیست؛ پورت `inactive` |
| 2 | همه‌ی Trunkهای مسیر: CORE Gi0/0 و Gi0/1 ، DIST Gi0/0-3 ، ACC3 Gi0/0: `switchport trunk allowed vlan add 106` | پورت‌ها up ولی ترافیک VLAN 106 رد نمی‌شود |
| 3 | FW-RTR: `interface gi0/0.106` ← `encapsulation dot1Q 106` ← `ip address 192.168.106.254 255.255.255.0` ← `ip helper-address 192.168.90.11` | Gateway نیست (ping .254 جواب نمی‌دهد) |
| 4 | SRV1: در `/etc/dhcp/dhcpd.conf` یک `subnet 192.168.106.0 ...` با `range 50-200` و `routers .254` ← `systemctl restart isc-dhcp-server` | DISCOVER می‌رسد ولی جواب نیست (`journalctl -u isc-dhcp-server`: no subnet declaration) |
| 5 | پورت: ACC3 Gi0/2 ← `switchport access vlan 106` ← `no shutdown`؛ HOST3 را به آن وصل کنید | `show interfaces status` |
**ثابت کن:** HOST3 در 192.168.106.x و `ping 192.168.106.254` موفق. **برگشت:** `no interface gi0/0.106` ، حذف از `allowed` (remove)، `no vlan 106` روی CORE، حذف Scope.

## S3) تغییر VLAN یک پورت و بررسی ۵ شرط (10 دقیقه)
سناریو: ACC2 Gi0/1 (HOST2) از VLAN 103 به 102 (IT).
| # | شرط | بررسی | علامت خرابی |
|---|---|---|---|
| 1 | VLAN روی سوییچ هست | `show vlan id 102` | port inactive |
| 2 | در همه‌ی Trunkهای مسیر مجاز است | `show interfaces trunk` روی ACC2 و DIST و CORE | IP نمی‌گیرد |
| 3 | Relay دارد | `FW-RTR# show running-config interface gi0/0.102` | 169.254 / بدون آدرس |
| 4 | Scope دارد | SRV1: `grep "subnet 192.168.102" /etc/dhcp/dhcpd.conf` | DISCOVER بی‌جواب |
| 5 | پورت Access است | `show interfaces gi0/1 switchport` | VLAN را نمی‌پذیرد/Trunk |
**اجرا:** بکاپ ← `reload in 10` ← `interface gi0/1` ← `switchport access vlan 102` ← HOST2 `pc-only.sh` ← `show mac address-table interface gi0/1` (VLAN 102) ← `reload cancel` ← `write memory`. **برگشت:** `switchport access vlan 103`.
