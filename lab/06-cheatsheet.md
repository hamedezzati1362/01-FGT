# برگه‌ی تقلب (ف = فقط‌خواندنی، ت = تغییر)
## شناخت
| ف | `show ?` ، `show vlan brief` ، `show interfaces status` ، `show interfaces status \| include connected` |
|---|---|
| ف | `show running-config \| section interface Gi0/1` ، `show version \| include uptime` |
| ف | `show cdp neighbors [detail]` |
## پیدا کردن
| ف | `show mac address-table address <MAC>` ← `show cdp neighbors` ← `show mac address-table interface <port>` |
|---|---|
## VLAN/VTP/Trunk
| ف | `show vtp status` ، `show vlan id <N>` ، `show interfaces trunk` ، `show interfaces <p> switchport` |
|---|---|
| ت | `vlan N` + `name X` (فقط روی VTP Server) ؛ `switchport trunk allowed vlan add N` (**همیشه add**) |
## DHCP/Phone
| ف | `show running-config interface <gw-subif>` (helper) ، `show ip dhcp ...` روی روتر ، `tail dhcpd.leases` روی سرور |
|---|---|
| ف | `show mac address-table interface <p>` (PC در VLAN داده، Phone در 97) |
## Port-Security / پورت
| ف | `show port-security interface <p>` ، `show interfaces status err-disabled` ، `show logging` |
|---|---|
| ت | `shutdown` ← `no shutdown` ؛ `clear port-security sticky interface <p>` |
## سرعت/دوپلکس
| ف | `show interfaces status` ، `show interfaces <p> \| include duplex\|CRC\|collision\|drops` (تفاضل شمارنده) |
|---|---|
## بکاپ
| ت | `copy running-config flash:<نام>-<تاریخ>.cfg` ، `copy running-config tftp://<IP>/<file>` |
|---|---|
| ف | `dir flash:` ، `show archive` ، `show archive config differences <A> <B>` |
| ت | `configure replace <file> list` (پیش‌نمایش) ← `force` ؛ `copy <file> running-config` (Merge) |
| ت | `reload in 10` ← تغییر ← `reload cancel` ؛ `write memory` |
## قوانین
- همیشه بکاپ + `reload in 10` + راستی‌آزمایی بعد از هر گام.
- `allowed vlan` بدون `add` = فاجعه.
- Native 1 و Root روی سوییچ طبقه = ضعف شناخته‌شده؛ مستند کن و در تغییر بعدی اصلاح کن.
