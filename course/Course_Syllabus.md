# سرفصل آموزشی دوره‌ی «مدیر شبکه و امنیت سازمانی»
**Cisco R&S (در حد CCNA عملی) + FortiGate (FortiOS 7.0.3) + Windows/Linux + پایش + Blue Team + Capstone**
نسخه‌ی سرفصل: ۲۰۲۶-۱۱-۲۵ (بر اساس Blueprint v2.1 و درس‌های تحویل‌شده)

---

## ۱) مشخصات کلی
| مورد | مقدار |
|---|---|
| مدت | ۲۴ هفته ، هر هفته ۶ روز ، هر روز ۶ ساعت = **۸۶۴ ساعت مفید** |
| مخاطب | ادمین شبکه‌ی مایکروسافت که می‌خواهد Cisco و FortiGate را سازمانی یاد بگیرد |
| بستر | ESXi (Windows/Linux) + PNetLab (Cisco vIOS/vIOSL2، FortiGate) ، Lab ایزوله |
| روش | هر روز یک درس کامل: چرا ← توضیح ساده ← مثال ساده/متوسط/سخت ← تمرین ← Lab ← عیب‌یابی ← مرور |
| قالب درس | مقدمه و «چرا»، جدول اصطلاحات (مخفف ← شکل کامل ← معنی)، شکل، مثال‌ها، تمرین، Lab هدایت‌شده و مستقل، عیب‌یابی، سؤال مرور، English Corner، چک‌لیست تسلط |
| خروجی هر هفته | یک یا چند «محصول» مستند (IP Plan، VLAN Matrix، Policy Matrix، As-Built ...) |
| قاعده‌ها | هیچ رمزی در ریپو؛ Claude به تجهیزات وصل نمی‌شود؛ هر تغییر با بکاپ و راه برگشت؛ نتیجه‌ی واقعی Lab ثبت می‌شود («پذیرفته‌شدن دستور ≠ کار کردن») |

## ۲) نقشه‌ی فازها
| فاز | هفته | محتوا |
|---|---|---|
| ۰ | ۱ | کشف زیرساخت (فقط مشاهده) و Lab ایزوله |
| ۱ | ۲ | IP، IPv6، CLI سیسکو، SSH، Wireshark |
| ۲ | ۳ تا ۴ | Switching: VLAN، Trunk، STP، EtherChannel، امنیت L2 |
| ۳ | ۵ تا ۶ | Routing: Static، OSPF، FHRP، Lab A |
| ۴ | ۷ تا ۸ | سرویس‌های IP، Hardening، اتوماسیون |
| ۵ | ۹ تا ۱۷ | FortiGate: مبانی، Policy/NAT، UTM، احراز هویت، VPN، SD-WAN، HA، پایش |
| ۶ | ۱۸ تا ۱۹ | بسته‌ها، عیب‌یابی ترکیبی، Blue Team |
| ۷ | ۲۰ تا ۲۴ | Capstone (مرکز + ۳ شعبه) و تحویل نهایی |

## ۳) سرفصل هفته‌به‌هفته

### فاز ۰ — هفته ۱ (تحویل‌شده)
| بخش | موضوع |
|---|---|
| A | کشف زیرساخت (Phase 0A، فقط مشاهده): ESXi، PNetLab، MikroTik/شبکه |
| B | ساخت Lab ایزوله (Phase 0B): `vSwitch-FGT`، شبکه‌ی PNetLab، Golden Imageها، Image Validation، تست ایزولاسیون |
محصول: Inventory، گزارش Phase 0A، `cisco_feature_probe`، `pnetlab_inventory`.

### فاز ۱ — هفته ۲: IP و CLI (تحویل‌شده) — Gate G1
| درس | موضوع |
|---|---|
| ۲-۱ | IPv4 از صفر: باینری، Mask، Prefix، Subnetting، AND و هم‌شبکه بودن، جدول توان‌های ۲ و Prefix |
| ۲-۲ | VLSM و طراحی IP Plan |
| ۲-۳ | IPv6: ساختار، کوتاه‌نویسی، انواع آدرس، NDP و SLAAC |
| ۲-۴ | CLI سیسکو، پیکربندی، بکاپ و Rollback (`reload in`) |
| ۲-۵ | SSH امن، بستن Telnet، ACL مدیریت |
| ۲-۶ | Wireshark: ARP/ICMP ، فیلترها ، آزمون Gate G1 |
محصول: IP Plan اولیه، بکاپ Config. (Lab مستقل: `02-design/ip-plan-drill.md`، `02-design/ip-plan.md`)

### فاز ۲ — هفته ۳: Switching I (تحویل‌شده)
| درس | موضوع |
|---|---|
| ۳-۱ | سوییچ و جدول MAC (Learning، Flooding، Forwarding، Aging) |
| ۳-۲ | VLAN، Access Port، VLAN Matrix |
| ۳-۳ | Trunk و 802.1Q (Native، Allowed، خطای `add`) |
| ۳-۴ | Router-on-a-Stick |
| ۳-۵ | SVI و سوییچ لایه ۳ |
| ۳-۶ | روش عیب‌یابی لایه‌ای ، TS01 تا TS05 ، آزمون کوچک |
محصول: VLAN Matrix، ۳ RCA.

### هفته ۴: Switching II (تحویل‌شده) — Gate G2
| درس | موضوع |
|---|---|
| ۴-۱ | حلقه در لایه ۲ و STP (Root، BPDU، نقش پورت‌ها) |
| ۴-۲ | Rapid-PVST، تعیین Root، PortFast، BPDU Guard، Root Guard |
| ۴-۳ | EtherChannel و LACP |
| ۴-۴ | Port Security |
| ۴-۵ | DHCP (DORA)، DHCP Snooping، DAI |
| ۴-۶ | طراحی سه‌لایه و Collapsed Core ، TS06 تا TS08 ، آزمون G2 |
محصول: Config کامل L2، ۳ RCA.

### فاز ۳ — هفته ۵: Routing I (تحویل‌شده)
| درس | موضوع |
|---|---|
| ۵-۱ | جدول مسیریابی، Longest Prefix Match، AD و Metric |
| ۵-۲ | Static Route و مسیر برگشت |
| ۵-۳ | Default، Floating Static، IP SLA و Track |
| ۵-۴ | مفهوم OSPF (همسایگی، LSDB، Cost) |
| ۵-۵ | پیاده‌سازی OSPF تک‌ناحیه‌ای |
| ۵-۶ | عیب‌یابی مسیریابی و ۵ دلیل Adjacency نشدن ، آزمون کوچک |

### هفته ۶: Routing II و FHRP (تحویل‌شده) — Gate G3
| درس | موضوع |
|---|---|
| ۶-۱ | DR/BDR، Network Type، Cost |
| ۶-۲ | OSPF چندناحیه‌ای (ABR، ASBR، LSA، Stub) |
| ۶-۳ | OSPFv3 و IPv6 |
| ۶-۴ | HSRP (و VRRP/GLBP) |
| ۶-۵ | پیاده‌سازی Lab A (Cisco L3 Core Gateway) |
| ۶-۶ | عیب‌یابی TS15 تا TS18 و TS09 ، آزمون G3 |
محصول: Lab A As-Built.

### فاز ۴ — هفته ۷: IP Services (تحویل‌شده)
| درس | موضوع |
|---|---|
| ۷-۱ | DHCP Server و Relay |
| ۷-۲ | DNS و NTP |
| ۷-۳ | NAT و PAT |
| ۷-۴ | ACL استاندارد و Extended |
| ۷-۵ | Syslog و SNMP (v2c فقط Lab، v3 امن) |
| ۷-۶ | QoS مقدماتی ، Service Matrix ، آزمون کوچک |
محصول: Service Matrix.

### هفته ۸: Hardening و Automation (تحویل‌شده) — CP1
| درس | موضوع |
|---|---|
| ۸-۱ | Hardening تجهیزات (سه صفحه‌ی دستگاه) |
| ۸-۲ | AAA، Privilege، TACACS+/RADIUS |
| ۸-۳ | JSON، YAML، REST و curl |
| ۸-۴ | Python و Netmiko (بکاپ Read-only) |
| ۸-۵ | Ansible (Idempotency، Check/Diff) |
| ۸-۶ | Git برای Config ، As-Built ، نقطه‌ی بازبینی CP1 |
محصول: Cisco Campus As-Built (CP1).

### فاز ۵ — FortiGate (هفته ۹ تا ۱۷؛ هنوز نوشته نشده)
| هفته | موضوع | Gate | محتوا |
|---|---|---|---|
| ۹ | FortiGate I | — | معماری، Interface/VLAN، Zone/Object، Admin/RBAC، Routing، Backup/Restore؛ Debug Flow مقدماتی؛ FGT Baseline Config |
| ۱۰ | Policy و NAT | G4 | Policy (First Match)، NAT/VIP/IP Pool، Session، Lab B؛ Sniffer و Flow؛ Policy Matrix v1 |
| ۱۱ | UTM و DMZ | — | AV، IPS، Web Filter، App Control، SSL Inspection (مشروط به لایسنس)؛ DMZ Design |
| ۱۲ | Authentication | G5 | LDAP، RADIUS، FSSO، Captive Portal؛ AD/NPS |
| ۱۳ | IPsec و Branch | — | Site-to-Site Route-Based، Selector؛ IKE/ESP؛ VPN Matrix |
| ۱۴ | RA-VPN | — | SSL VPN (فقط Lab ایزوله)، Dial-up IPsec، FortiClient |
| ۱۵ | SD-WAN و Routing پویا | — | SD-WAN، Link-Monitor، OSPF/BGP مقدماتی؛ WAN Design |
| ۱۶ | HA و مدیریت مرکزی | G6 | HA Active-Passive (مشروط)، DoS، FortiManager/FortiAnalyzer (مفهومی) |
| ۱۷ | Monitoring | — | Logging، FortiView، Zabbix، rsyslog؛ Dashboard Plan و Alert Catalog |

### فاز ۶ — هفته ۱۸ تا ۱۹
| هفته | موضوع | Gate | محتوا |
|---|---|---|---|
| ۱۸ | تحلیل بسته و TS-1 | — | Wireshark عمیق (PA01 تا PA18)، مرور همه با Fault Mix، RCA |
| ۱۹ | Blue Team و TS-2 | G7 | Hardening Audit، IPS، Nmap (فقط Lab)، تشخیص Scan و Anomaly؛ ≥ ۴۰ از ۵۰ TS با RCA |

### فاز ۷ — Capstone (هفته ۲۰ تا ۲۴)
| هفته | موضوع | محصول |
|---|---|---|
| ۲۰ | Capstone-1: Campus/WAN Build | HLD، LLD، IP Plan |
| ۲۱ | Capstone-2: Security و VPN | Policy Matrix، VPN Matrix |
| ۲۲ | Capstone-3: Fault Mix، HA و Monitoring | نتیجه‌ی Test Plan |
| ۲۳ | Buffer و Mock | Gap Closure Report |
| ۲۴ | Final و Handover (G8) | As-Built، Handover |
معماری اصلی Capstone: **FortiGate = Gateway همه‌ی VLANها**، سوییچ‌های Cisco فقط L2 (Lab A به‌صورت جدا و مکمل).

## ۴) Gateها (آزمون‌های عملی)
| Gate | پایان | موضوع |
|---|---|---|
| G1 | هفته ۲ | Subnetting/VLSM، IPv6، CLI، SSH، Wireshark |
| G2 | هفته ۴ | Switching کامل (STP، EtherChannel، Port-Sec، Snooping) |
| G3 | هفته ۶ | OSPF، HSRP، Lab A |
| CP1 | هفته ۸ | As-Built بخش Cisco (آغاز فاز FortiGate) |
| G4 | هفته ۱۰ | Policy و NAT |
| G5 | هفته ۱۲ | Authentication |
| G6 | هفته ۱۶ | HA و Hardening |
| G7 | هفته ۱۹ | عیب‌یابی و Blue Team |
| G8 | هفته ۲۴ | Capstone و تحویل |

## ۵) کارگاه کمکی (بیرون از ۲۴ هفته)
| کارگاه | مدت | محتوا |
|---|---|---|
| Cisco Daily Ops (پوشه‌ی `lab/`) | ۴ ساعت | شبکه‌ی سه‌لایه‌ی شبیه سازمان: VLAN، VTP، Trunk، DHCP Relay، IP Phone (شبیه‌سازی‌شده)، Port-Security، جابه‌جایی میز، بکاپ/بازیابی، ۱۲ خرابی پنهان |

## ۶) وضعیت اجرا
| بخش | وضعیت |
|---|---|
| هفته ۱ تا ۸ (Cisco) | درس‌ها در فایل `course/Enterprise_Network_Course_Lessons.html` (نسخه ۱.۲) |
| هفته ۹ تا ۲۴ | سرفصل طراحی‌شده؛ درس‌ها نوشته نشده |
| FortiGate | Image آماده، بوت تا هفته ۹ به تعویق افتاده (برای حفظ ساعت Evaluation) |
| کارگاه Cisco Daily Ops | تحویل‌شده؛ آزمایش روی PNetLab بعد از اجرای M01 (Probe) |

## ۷) مراجع
`Enterprise_Network_Security_Course_Master_Blueprint_v2.1.md` (طرح کامل) ، `DECISIONS_LOG.md` ، `phase0a/` ، `lab/`
