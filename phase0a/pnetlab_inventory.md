# PNetLab Inventory (Phase 0B، 2026-11-07؛ ثبت‌شده از خروجی SSH کاربر)

## نسخه و منابع
- PNetLab `4.2.8` روی Ubuntu 18.04.5؛ VM: **16 vCPU، 48 GB RAM، دیسک 200 GB (LVM 196 GB)**؛ Nested (`/dev/kvm`) فعال؛ NTP=`192.168.88.1`؛ Timezone `Asia/Tehran`.

## Imageهای نصب‌شده
| نوع | پوشه/فایل | Template متناظر | یادداشت |
|---|---|---|---|
| QEMU | `vios-adventerprisek9-m.spa.159-3.m9` (55 MB) | `vios` (Cisco vIOS Router) | هدف دوره (Router/ISP-Sim) |
| QEMU | `viosl2-adventerprisek9-m.ssa.high_iron_20200929` (87 MB) | `viosl2` (Cisco vIOS Switch) | هدف دوره (Access/Core L2) |
| QEMU | `fortinet-7.0.3` (76 MB، `virtioa.qcow2`) | `fortinet` | **هدف دوره**؛ Eval؛ Boot تا W9 به تعویق |
| QEMU | `fortinet-6.46` | `fortinet` | استفاده نمی‌شود |
| QEMU | `csr1000vng-universalk9.17.03.02` (1.2 GB) | `csr1000vng` | اختیاری (IOS-XE) |
| IOL | `L2-/L3-ADVENTERPRISEK9…` + `iourc` | `l2_iol` / `l3_iol` | **استفاده نمی‌شود** (طبق قانون پروژه) |
| Dynamips | `c7200-adventerprisek9-mz.152-4.S7.image` | `c7200` | استفاده نمی‌شود |
| Docker | — (خالی) | `docker`/`dockerserver` | — |

## Templateهای مرتبط با دوره (مسیر: `/opt/unetlab/html/templates/intel|amd/`)
`vios`، `viosl2`، `fortinet`، `csr1000vng`، `linux`، `docker`، `generic`، `mikrotik`، `kali`، `slax` و … (بیش از 150 Template عمومی PNetLab؛ فقط بخش کوچکی Image دارد).

## پیش‌فرض‌های Template (از `.yml`)
| Template | CPU | RAM پیش‌فرض | Ethernet | Console | QEMU |
|---|---|---|---|---|---|
| `vios` | 1 | **1024 MB** | 4 | telnet | 2.12.0 |
| `viosl2` | 1 | **1024 MB** | 8 | telnet | 2.12.0 |
| `fortinet` | 1 | **1024 MB** | 4 | telnet | 4.1.0، `virtio-net-pci` |

## پیامدها برای طراحی (به‌روزرسانی فصل ۱۳)
- RAM پیش‌فرض IOSv/IOSvL2 در PNetLab **1 GB** است (نه 0.5/0.75 GB مرجع CML)؛ در حسابداری Tier باید 1 GB برای هر Node در نظر گرفته شود مگر دستی کاهش یابد (برای IOSv حداقل 512 MB در CML؛ `Unverified` برای PNetLab).
- FortiGate: پیش‌فرض 1 GB؛ **برای Capstone باید ≥ 2 GB** (و Eval ممکن است سقف داشته باشد؛ `Unverified`) و **Ethernet = 8** (mgmt، LAN-trunk، WAN1، WAN2، HA، DMZ…).
- برآورد T3 با 5 FGT@2GB + 6 IOSvL2@1GB + 6 IOSv@1GB + 2 Linux ≈ **26 GB** + سربار PNetLab ≈ 4 GB ≈ **30 GB** ≤ 48 GB ✔.
- `ethernet: 8` برای `viosl2` کافی است برای Access/Core (در صورت نیاز به پورت بیشتر Template/Node قابل تغییر است).
