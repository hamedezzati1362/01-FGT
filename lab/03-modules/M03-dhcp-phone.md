# M03 — DHCP و IP Phone (30 دقیقه)

## A) DHCP Relay، Scope، رزرو (15 دقیقه)
مسیر: PC (VLAN 101) ← DISCOVER Broadcast ← Gateway FW-RTR (`helper-address`) ← Unicast به SRV1 ← OFFER برمی‌گردد.
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ف | `FW-RTR# show running-config interface gi0/0.101` | `ip helper-address 192.168.90.11` |
| 2 ف | SRV1: `tcpdump -ni eth0 port 67 or port 68` (یک ترمینال) | |
| 3 ت | HOST1: `bash /opt/lab/pc-phone/pc-only.sh` | DISCOVER/OFFER در tcpdump؛ IP همان رزرو `192.168.101.61` |
| 4 ف | SRV1: `grep -A3 "lease 192.168.101" /var/lib/dhcp/dhcpd.leases \| tail` | Lease و MAC |
| 5 ف | SRV1: `grep -n "pc1" /etc/dhcp/dhcpd.conf` | سه رزرو برای PC1 (VLAN 101، 103، 107): «رزرو در هر Scope» |
**Lease قدیمی:** اگر میز عوض شد ولی کلاینت همان IP قبلی را می‌خواهد: `ip addr flush dev eth0` سپس دوباره `pc-only.sh`. (Lease Lab عمداً ۱۰ دقیقه است؛ واقعی: روز.)
**169.254:** Windows وقتی DHCP جواب نگیرد 169.254 می‌سازد. در Lab Linux «بدون آدرس» است؛ معادل آن همین است. VLAN بدون Relay = علامت کلاسیک.
**چهار علت «IP نمی‌گیرم»:** ۱) پورت در VLAN اشتباه ۲) VLAN در Trunk مجاز نیست ۳) Relay/Scope ندارد ۴) سرور/Lease پر.

## B) IP Phone (شبیه‌سازی‌شده) (15 دقیقه)
**ایده:** یک کابل، دو MAC: `eth0` بدون تگ (PC) و `eth0.97` تگ‌دار (Phone). سوییچ با `switchport voice vlan 97` تلفن را در VLAN 97 و PC را در VLAN داده (101) می‌بیند.
| قدم | انجام بده | ثابت کن |
|---|---|---|
| 1 ت | HOST1: `bash /opt/lab/pc-phone/phone-pc-sim.sh 1` | دو خط `[PC]` و `[PHONE]`؛ `ip -br addr` دو آدرس: eth0=192.168.101.61 ، eth0.97=192.168.97.61 |
| 2 ف | `ACC1# show mac address-table interface gi0/1` | دو MAC: `02aa.0000.0101` در VLAN 101 و `02bb.0000.0197` در VLAN 97 |
| 3 ف | `ACC1# show interfaces gi0/1 switchport \| include Voice\|Access` | Voice VLAN: 97 ، Access Mode VLAN: 101 |
| 4 ف | `ACC1# show port-security interface gi0/1` | Total MAC = 2 (حداکثر 3) |
| 5 ف | HOST1: `ping -c3 192.168.97.254` و `ping -c3 192.168.101.254` | هر دو Gateway جواب می‌دهند |
**چرا ۳ MAC؟** PC + Phone + یک جای خالی برای تعویض دستگاه. ۲ می‌گذاشتید با اولین تعویض Violation می‌خورید.
**اگر MAC تلفن در VLAN 97 دیده نشد:** این یعنی voice VLAN در این Image اجرا نمی‌شود (Probe #4). مفهومش همین است؛ نمونه‌ی واقعی بالا را بخوانید و بروید جلو.

### PoE — فقط مفهومی (نمونه‌ی واقعی `show power inline` روی 2960)
```
Switch# show power inline
Available:370.0(w)  Used:15.4(w)  Remaining:354.6(w)
Interface Admin  Oper       Power   Device              Class Max
                             (Watts)
--------- ------ ---------- ------- ------------------- ----- ----
Gi1/0/5   auto   on         15.4    Cisco IP Phone 7960  3    30.0
Gi1/0/6   auto   off        0.0     n/a                  n/a  30.0
```
- `Oper on` = تلفن برق دارد؛ `off` = دستگاهی نیست/PoE خاموش.
- تلفن بالا نمی‌آید؟ اول `show power inline` (برق)، بعد `show cdp neighbors` (تلفن خودش را معرفی می‌کند)، بعد voice VLAN و Trunk.
- `power inline never` روی پورت دوربین/Wi-Fi اگر نباید برق بگیرد. در Lab PoE نداریم.
