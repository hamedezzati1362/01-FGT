# ممیزی انطباق دوره با سرفصل رسمی آزمون‌ها (CCNA 200-301 و Fortinet NSE 4 / FortiOS 7.0)

**منابع رسمی خوانده‌شده**
- Cisco: «Implementing and Administering Cisco Solutions (200-301 CCNA) v2.0 — Exam Topics» (PDF رسمی Cisco، دامنه‌های 1.0 تا 5.0).
- Fortinet: «NSE 4 Network Security Professional — Fortinet NSE 4—FortiOS 7.0 (NSE4_FGT-7.0) Exam Description» (PDF؛ نسخه‌ی نمایه‌شده در سایت دیگر، نه صفحه‌ی مستقیم Fortinet).

**روش و محدودیت صادقانه:** هر سرفصل با جست‌وجوی کلیدواژه در متن دوره سنجیده شد (وجود مبحث)، نه با خواندن و نمره‌دادن کیفیت درس‌به‌درس. نتیجه‌ی «پوشش دارد» یعنی مبحث تدریس شده است؛ هنوز ممیزی عمق/صحت هر درس با کتاب رسمی (مثلاً Cisco Press OCG و کتاب‌های درسی Fortinet) انجام نشده و آن کتاب‌ها در دسترس من نبودند. نسخه‌ی v1.1 CCNA (جاری تا Feb 2027) با v2.0 تفاوت دارد؛ دامنه‌ی AI در v2.0 جدید است.

## CCNA 200-301 — جدول پوشش

| سرفصل رسمی | وضعیت پیش از ممیزی | درس‌ها اکنون |
|---|---|---|
| 1.1 عیب‌یابی Interface/کابل (duplex, collisions) | دارد | 3-0، 3-6 |
| 1.2 Hypervisor/VM/Container | **نداشت** | **1-C (جدید)** |
| 1.3 IPv4 و Subnetting | دارد | ف۲ |
| 1.4 IPv6 و Modified EUI-64، اندازه‌ی Prefix | سطحی | ف۶ + **2-7 (جدید)** |
| 1.5 اصول Wireless (باند، RF، امنیت، تداخل) | **نداشت** | **2-8 (جدید)** |
| 1.6 عیب‌یابی کلاینت سیمی/بی‌سیم روی Windows/macOS/Linux | **نداشت** | **2-9 (جدید)** |
| 1.7 DHCPv4 client/server/relay | دارد | 7-1 |
| 2.1 اتصال سوییچ (Trunk, EtherChannel, SVI) | دارد | ف۳، ف۴ |
| 2.2 ویژگی پورت برای دستگاه لبه (VLAN, PoE, LACP) | PoE **نداشت** | 3-x + **3-7 (جدید)** |
| 2.3 CDP/LLDP | دارد (محدود) | ف۳/۸ |
| 2.4 show/ping/traceroute/Capture | دارد | ف۲، ف۳، ف۱۴ |
| 2.5 Rapid PVST+ و Guardها | دارد | 4-1 تا 4-3 |
| 3.1 جدول مسیر، AD، Metric | دارد | ف۵ |
| 3.2 Static/Floating | دارد | ف۵ |
| 3.3 OSPFv2/v3 | دارد | ف۵، ف۶ |
| 3.4 HSRP/VRRP | دارد | ف۶ |
| 4.1 AAA (TACACS+/RADIUS) | دارد | ف۸ |
| 4.2 SFTP/SCP | دارد | ف۸ |
| 4.3 NAT/PAT | دارد | ف۷ |
| 4.4 رکوردهای DNS | سطحی | 7-2 + **7-8 (جدید)** |
| 4.5 IPsec RA/S2S، Transport/Tunnel | سطحی | 18-0 + **18-7 (جدید)** |
| 4.6 ACL | دارد | ف۷ |
| 4.7 Layer 2 Security: DHCP snooping, DAI, Port Security | دارد | 4-4، 4-5 |
| 4.7 Storm Control، RA Guard | **نداشت** | **4-8 (جدید)** |
| 5.1/5.2 Agentic AI و Prompt | **نداشت** | **8-10 (جدید)** |
| 5.3 رویکردهای مدیریت و IaC | دارد | ف۸ |
| 5.4 SNMP | دارد | ف۷/۲۷ |
| 5.5 Ansible | دارد | ف۸ |
| 5.6 Syslog | دارد | ف۷ |

## Fortinet NSE 4 (FortiOS 7.0) — جدول پوشش

| موضوع رسمی | وضعیت پیش از ممیزی | درس‌ها اکنون |
|---|---|---|
| Initial configuration | دارد | 12-1 تا 12-3 |
| Fortinet Security Fabric | **نداشت (۷ اشاره)** | **12-11 (جدید)** |
| Log settings و تشخیص با Log | دارد | 14-6، 27-1 |
| VDOM | دارد | ف۲۴ |
| FGCP HA (modes) | دارد | ف۲۲ |
| عیب‌یابی منابع و اتصال | دارد | ف۱۴ |
| Policy NAT و Central NAT | دارد | ف۱۳ |
| روش‌های Firewall Authentication | دارد | ف۱۷ |
| FSSO | دارد | 17-4 |
| بازرسی ترافیک رمز (گواهی) | دارد | 16-0، 16-5 |
| Inspection modes، Web/DNS filter | دارد | 16-0، 16-2 |
| Application Control | دارد | 16-4 |
| Antivirus modes | دارد | 16-3 |
| IPS و DoS | دارد | 16-4 |
| **WAF** | **ناکافی** | **16-8 (جدید)** |
| Static/Policy routes | دارد | 12-4، 10-4 |
| SD-WAN | دارد | ف۲۱ |
| **Layer 2 (Transparent / Virtual Wire / Software Switch)** | **نداشت** | **12-10 (جدید)** |
| SSL-VPN modes | دارد | ف۲۰ |
| IPsec meshed/partially redundant | دارد | ف۱۸، ۱۹ |

## موارد باقی‌مانده (صادقانه)
1. ممیزی عمق/صحت **هر درس** با کتاب رسمی (Cisco OCG و کتاب‌های NSE4) انجام نشده؛ فقط وجود مبحث سنجیده شد.
2. درس‌های جدید نظری/مستندی‌اند؛ هیچ Labی اجرا نشده و دستورها `Unverified` هستند.
3. مقایسه با سرفصل CCNA v1.1 (نسخه‌ی جاری) جداگانه انجام نشده؛ فقط v2.0 خوانده شد.
4. FortiSwitch/FortiAP/Explicit Proxy در سرفصل 7.0 این آزمون نیستند و در دوره درس مستقل ندارند.

## به‌روزرسانی: درس‌های افزوده‌ی دور دوم (گام‌به‌گام)
| سرفصل | درس جدید |
|---|---|
| CCNA 1.1 کابل/فیبر/Interface/خطاها | 3-8 |
| CCNA 1.7 DHCPv4 روی IOS | 7-9 |
| CCNA 2.1.c / 2.2 EtherChannel و LACP | 4-9 |
| CCNA 2.3 CDP/LLDP | 3-9 |
| CCNA 2.4 show/ping توسعه‌یافته/traceroute/Capture | 3-10 |
| CCNA 3.1/3.2 Static (default/network/host/floating، IPv6) | 5-9 |
| CCNA 3.4 تفسیر HSRP/VRRP | 6-8 |
| CCNA 4.1 AAA (Local/TACACS+/RADIUS) | 8-11 |
| CCNA 4.3 NAT Dynamic/PAT | 7-10 |
| CCNA 5.3/5.5 رویکردهای مدیریت، REST، Ansible، IaC | 8-12 |
| NSE4 HA modes (a-a، vcluster، HA mgmt) | 22-6 |
| NSE4 Firewall authentication (Active/Passive) | 17-8 |
| NSE4 Web filtering (Category/Static URL/Rating) | 16-9 |
| NSE4 Log settings و عیب‌یابی با Log | 27-8 |

**هنوز بررسی‌نشده:** CCNA 2.5 (جزئیات Rapid PVST+)، 3.3 (OSPF تک‌ناحیه)، 4.6 (ACL)، 4.7 (DHCP Snooping/DAI/Port Security) و NSE4 SSL-VPN modes، IPsec mesh، SD-WAN، Antivirus/IPS/DoS و VDOM به‌صورت خواندن زیرمورد‌به‌زیرمورد انجام نشده؛ فقط وجود کلیدواژه سنجیده شده است.
