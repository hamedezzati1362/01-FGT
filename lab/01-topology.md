# توپولوژی، آدرس‌دهی، نگاشت پورت‌ها

## نمودار
```
                          [FW-RTR]  Gi0/0.<VLAN> = 192.168.<VLAN>.254   (helper-address -> SRV1)
                              | Gi0/0  (trunk)
                          [CORE]  VTP Server, L2 only
                              | Gi0/1  (trunk)
                          [DIST]  ---- Gi1/0 ---- [SRV1]  192.168.90.11 (DHCP + TFTP, VLAN 90)
                  Gi0/1 /     | Gi0/2      \ Gi0/3
                      /       |             \
                 [ACC1]    [ACC2]        [ACC3]  ---- Gi1/0,Gi1/1 ---- [MINI-SW] (only for two optional faults)
                  |  |       |  |          |  |
               HOST1 AP   HOST2  ...     HOST3  ...
      (PC + simulated phone on ONE cable: eth0 untagged = PC, eth0.97 tagged = phone)
```
## اتصال‌ها (PNETLab: e0/0 = Gi0/0 ، e0/1 = Gi0/1 ، ... ، e1/0 = Gi1/0)
| # | از | به | نوع |
|---|---|---|---|
| 1 | FW-RTR Gi0/0 | CORE Gi0/0 | trunk |
| 2 | CORE Gi0/1 | DIST Gi0/0 | trunk |
| 3 | DIST Gi0/1 | ACC1 Gi0/0 | trunk |
| 4 | DIST Gi0/2 | ACC2 Gi0/0 | trunk |
| 5 | DIST Gi0/3 | ACC3 Gi0/0 | trunk |
| 6 | DIST Gi1/0 | SRV1 eth0 | access VLAN 90 |
| 7 | ACC1 Gi0/1 | HOST1 eth0 | access + voice 97 |
| 8 | ACC2 Gi0/1 | HOST2 eth0 | access + voice 97 |
| 9 | ACC3 Gi0/1 | HOST3 eth0 | access + voice 97 |
| 10 (فقط خرابی‌ها) | MINI-SW Gi0/0 (و Gi0/1) | ACC3 Gi1/0 (و Gi1/1) | طبق فایل خرابی |

## VLANها (شبکه‌ی هر VLAN = `192.168.<VLAN>.0/24`، Gateway = `.254`)
| VLAN | نام | Relay | توضیح |
|---|---|---|---|
| 2 | CAMERA | بله | دوربین |
| 89 | MGMT-OLD | — | در VTP هست ولی عمداً در Trunk مجاز نیست (همان‌طور که در لیست شبکه‌ی شما بود) |
| 90 | SERVERS | — | SRV1 (استاتیک) |
| 97 | VOICE | بله | IP Phone |
| 100 | MGMT-DEV | — | مدیریت سوییچ‌ها (SVI Vlan100، استاتیک) |
| 101-104 | FIN-ADMIN، IT، CALLCENTER، CEO | بله | کاربران |
| 105 | WIFI-AP | بله | Access Point |
| 107 | USERS-GEN | بله | کاربران عمومی |
| 108 | WIFI-CLIENT | بله | کلاینت Wi-Fi |
Trunk: `802.1q`، Native = 1 (ضعف شناخته‌شده)، مجاز: `2,90,97,100-105,107-108`. VTP: CORE=Server، بقیه Client، دامنه `lab.local`، نسخه 2، رمز نمونه.
STP: PVST (نه Rapid) و Root روی ACC1 (ضعف شناخته‌شده؛ در سناریوها نشانش می‌دهیم).

## آدرس مدیریت (Vlan100) و میزبان‌ها
| دستگاه | IP |
|---|---|
| FW-RTR (Gateway هر VLAN) | 192.168.V.254 |
| CORE / DIST | 192.168.100.1 / .2 |
| ACC1 / ACC2 / ACC3 | 192.168.100.11 / .12 / .13 |
| MINI-SW | 192.168.100.99 |
| SRV1 (DHCP + TFTP) | 192.168.90.11 |
| HOST1 (ACC1، VLAN 101)  PC: `02:aa:00:00:01:01`  Phone: `02:bb:00:00:01:97` | رزرو PC: .101.61  ، Phone: 192.168.97.61 |
| HOST2 (ACC2، VLAN 103)  MACها با 02 | رزرو PC: .103.62  ، Phone: .97.62 |
| HOST3 (ACC3، VLAN 107) | رزرو PC: .107.63  ، Phone: .97.63 |
(رزرو PC هر میزبان در VLANهای 101 و 103 و 107 هر سه تعریف است تا «جابه‌جایی میز» جواب بدهد.)

## نگاشت نام پورت: سوییچ واقعی (2960S) ↔ Lab (viosl2)
| واقعی | Lab | نقش |
|---|---|---|
| Gi1/0/1 تا Gi1/0/3 (پورت کاربر) | Gi0/1 تا Gi0/3 | PC+Phone، UNUSED، AP |
| Gi1/0/4 تا Gi1/0/7 | Gi1/0 تا Gi1/3 | UNUSED / DISABLED |
| Uplink به DIS (`UP-DIS-Gi1/0/N`) | Gi0/0 | Trunk |
| `interface range gi1/0/1 - 24` | `interface range gi0/1 - 3 , gi1/0 - 3` | |
قالب توضیح پورت همان است: `PC-<نام>`, `PC-<نام>+Phone`, `Phone-Only`, `UNUSED`, `DISABLED`, `AP-Wifi`, `UP-DIS-Gi1/0/N`.
