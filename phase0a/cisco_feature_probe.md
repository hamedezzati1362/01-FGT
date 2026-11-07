# Cisco Feature Probe — نتایج Image Validation (Phase 0B)

> تاریخ: 2026-11-07. محیط: PNetLab، Lab `L00-ImageValidation` (SW1=viosl2، R1=vios).
> **توجه:** «CLI پذیرفت» ≠ «Feature کار می‌کند». هر ردیف جدا ثبت می‌شود: `Tested-OK` (عملکرد دیده شد)، `CLI-Accepted` (فقط فرمان پذیرفته؛ عملکرد آزمایش‌نشده)، `Rejected` (`% Invalid input`)، `Untested`.

## Image
| Node | Image | نسخه |
|---|---|---|
| SW1 | `viosl2-adventerprisek9-m.ssa.high_iron_20200929` | IOS vios_l2 **15.2(20200924:215240)** Experimental؛ حافظه 935153K/111616K (≈1 GB) |
| R1 | `vios-adventerprisek9-m.spa.159-3.m9` | IOSv **15.9(3)M9** RELEASE (fc1)؛ حافظه 984305K/62464K (≈1 GB) |

## نتایج SW1 (IOSvL2)
| Feature | روش | وضعیت |
|---|---|---|
| VLAN (ساخت/نام‌گذاری) | `vlan 10` + `name TEST` + `show vlan brief` | **Tested-OK** |
| 802.1Q Trunk | `switchport trunk encapsulation dot1q` + `switchport mode trunk` + `show interfaces trunk` (802.1q، allowed 1-4094) | **Tested-OK** (فرمان `encapsulation dot1q` لازم است) |
| STP (PVST) | `show spanning-tree summary`: mode `pvst`، Root برای VLAN 1 و 10 | **Tested-OK** (حالت پیش‌فرض PVST؛ Rapid-PVST آزمایش‌نشده) |
| DHCP Snooping | `ip dhcp snooping` | **CLI-Accepted** (عملکرد: Untested) |
| Dynamic ARP Inspection | `ip arp inspection vlan 10` | **CLI-Accepted** (عملکرد: Untested) |
| SPAN | `monitor session 1 source interface gi0/1` | **CLI-Accepted** (عملکرد: Untested) |

## نتایج SW1 — دور دوم
| Feature | شاهد | وضعیت |
|---|---|---|
| Rapid-PVST | `spanning-tree mode rapid-pvst` در running-config | **Tested-OK** (پیکربندی) |
| PortFast + BPDU Guard | پذیرفته شد؛ در Config به‌صورت `spanning-tree portfast edge`؛ `bpduguard enable` | **CLI-Accepted** (عملکرد: Untested) |
| Port Security | `show port-security`: Gi0/2، Max=2، Action=Restrict | **Tested-OK** (پیکربندی؛ رفتار Violation: Untested) |
| EtherChannel LACP | `channel-group 1 mode active` → Po1 ساخته شد؛ `%EC-5-L3DONTBNDL2: Gi0/3 suspended: LACP currently not enabled on the remote port`؛ `Po1(SD) LACP Gi0/3(s)` | **LACP engine فعال** (مذاکره انجام می‌شود؛ Bundle کامل: Untested؛ نیاز به سوئیچ دوم) |
| SVI / `ip routing` | `ip routing` پذیرفته شد؛ `interface vlan 10` با IP ← `Vlan10 up/up` | **Tested-OK** |
| `no ip routing` + `ip default-gateway` | پذیرفته شد؛ در Config دیده می‌شود | **Tested-OK** (پیکربندی؛ الگوی Management Plane فصل ۱۴.۵) |
| ACL Extended | `permit tcp any any eq 22` پذیرفته شد | **CLI-Accepted** |
| NTP | `ntp server 192.168.88.1` پذیرفته شد | **CLI-Accepted** (Sync: Untested) |
| Syslog | `logging host 10.10.60.20` → `%SYS-6-LOGGINGHOST_STARTSTOP: Logging to host … port 514 started` | **Tested-OK** (راه‌اندازی؛ دریافت در سرور: Untested) |
| SNMP | `snmp-server community TESTRO RO` (خروجی با لاگ قاطی شد؛ خطا دیده نشد) | **CLI-Accepted** (احتمالاً؛ دوباره بررسی شود) |
| IPv6 | `ipv6 unicast-routing` پذیرفته شد | **CLI-Accepted** |

## یادداشت‌های یادگیری (برای «مرور اشتباهات»)
- روی کنسول ابتدا در **User EXEC** (`Switch>`) بودید و `configure terminal` خطا داد؛ قبلش `enable` لازم است.
- `configure terminal` را وسط حالت Config دوباره زدید → `% Invalid input` (فقط یک بار لازم است).
- بعد از Probe فقط `no ip dhcp snooping` و `no monitor session 1` برگردانده شد؛ `ip arp inspection vlan 10` هنوز مانده (Lab آزمایشی؛ مهم نیست).

## نتایج R1 (IOSv)
| Feature | شاهد | وضعیت |
|---|---|---|
| Router-on-a-Stick (Sub-interface + 802.1Q) با SW1 | `interface gi0/0.10`، `encapsulation dot1Q 10`، `ip address 10.10.10.1/24`؛ `ping 10.10.10.2` (SVI سوئیچ): ابتدا 80٪ (ARP)، بار دوم **100٪** (RTT 5–10 ms) | **Tested-OK** (Trunk + 802.1Q + SVI + RoAS؛ تست داده واقعی) |
| IP SLA (icmp-echo) | `show ip sla statistics`: RTT 7 ms، return code OK، 2 موفقیت | **Tested-OK** |
| HSRP | `standby 1 ip 10.10.10.254` → `%HSRP-5-STATECHANGE … Standby -> Active`؛ `show standby brief`: Active local | **Tested-OK** (موتور State؛ Failover: Untested، نیاز به روتر دوم) |
| SSH/RSA | `crypto key generate rsa modulus 2048` → `%SSH-5-ENABLED: SSH 1.99 has been enabled` | **Tested-OK** (`ip ssh version 2`: دوباره، در حالت Config) |
| OSPFv2 | `router ospf 1` + `network … area 0` پذیرفته شد؛ `show ip ospf neighbor` خالی (همسایه‌ای نیست) | **CLI-Accepted** (Adjacency: Untested) |
| IPv6 | `ipv6 unicast-routing` | **CLI-Accepted** |
| DHCP Server | `ip dhcp pool TEST` + `network` | **CLI-Accepted** (Lease: Untested) |
| ACL | `permit tcp any any eq 22` | **CLI-Accepted** |
| NAT | `ip nat outside` / `ip nat inside` (NVI0 up) | **CLI-Accepted** (Translation: Untested) |
| Embedded Packet Capture | `monitor capture buffer BUF size 256` **در حالت Config** → `% Invalid input` | **Untested** (دستور EPC در **Privileged EXEC** است؛ دوباره در `R1#` امتحان شود) |

## یادداشت‌های یادگیری (دور R1)
- `interface gi0/0.10` در `R1#` (EXEC) خطا داد؛ باید در حالت Config باشید (`configure terminal`).
- `ip ssh version 2` در EXEC زده شد → خطا؛ فرمان Config است.
- در EXEC هر کلمه ناشناخته (`end`، `Xconf`) به‌عنوان نام میزبان **DNS Lookup** می‌شود («Translating…») و کنسول گیر می‌کند؛ با `no ip domain-lookup` (در Config) خاموش می‌شود. `end` فقط در Config معنی دارد.
- `crypto key generate rsa` دو بار زده شد (دومی کلید را جایگزین کرد).
- `monitor capture` یک فرمان **EXEC** است نه Config.
