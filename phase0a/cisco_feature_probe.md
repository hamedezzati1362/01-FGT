# Cisco Feature Probe — نتایج Image Validation (Phase 0B)

> تاریخ: 2026-11-07. محیط: PNetLab، Lab `L00-ImageValidation` (SW1=viosl2، R1=vios).
> **توجه:** «CLI پذیرفت» ≠ «Feature کار می‌کند». هر ردیف جدا ثبت می‌شود: `Tested-OK` (عملکرد دیده شد)، `CLI-Accepted` (فقط فرمان پذیرفته؛ عملکرد آزمایش‌نشده)، `Rejected` (`% Invalid input`)، `Untested`.

## Image
| Node | Image | نسخه |
|---|---|---|
| SW1 | `viosl2-adventerprisek9-m.ssa.high_iron_20200929` | IOS vios_l2 **15.2(20200924:215240)** Experimental؛ حافظه 935153K/111616K (≈1 GB) |
| R1 | `vios-adventerprisek9-m.spa.159-3.m9` | (نسخه دقیق هنوز ثبت نشده؛ `show version` روی R1) |

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

## نتایج R1 (IOSv): هنوز Untested
