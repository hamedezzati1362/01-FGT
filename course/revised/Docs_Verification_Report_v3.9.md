# گزارش تطبیق دستورها با مستندات رسمی Fortinet (نسخه‌ی v3.9)

تاریخ: ۲۰۲۶-۱۱-۲۷ · روش: جست‌وجوی مستندات رسمی (docs.fortinet.com) و Fortinet Community · **هیچ دستگاهی اجرا نشد.**

> **معنی وضعیت «تأیید مستندی»:** دستور/پارامتر در مستندات رسمی (CLI Reference یا Administration Guide) وجود دارد. این **به معنی اجرا روی FortiOS 7.0.3 نیست**؛ فقط یعنی نام و ساختار دستور ساختگی نیست. اجرای واقعی همچنان فقط با Runbook Phase 0B ممکن است.

## ۱) دستورهای تأییدشده در مستندات

| دستور / پارامتر | وضعیت | نکته‌ی مهم | مرجع |
|---|---|---|---|
| `config firewall policy` → `tcp-mss-sender` / `tcp-mss-receiver` | تأیید مستندی | مقدار ۰ تا ۶۵۵۳۵، پیش‌فرض ۰؛ MSS = MTU − ۴۰ | [CLI Reference 7.0.3](https://docs.fortinet.com/document/fortigate/7.0.3/cli-reference/325620/config-firewall-policy) |
| `execute ha failover set / unset / status` | تأیید مستندی | فقط برای آزمون/نگهداری؛ Flag تا `unset` می‌ماند؛ ID خوشه اختیاری | [execute ha](https://docs.fortinet.com/document/fortigate/7.2.13/cli-reference/105234857/execute-ha) |
| `config system vdom-link` (`edit`، `set type ppp\|ethernet\|npupair`) | تأیید مستندی | نام حداکثر ۱۱ نویسه؛ پیش‌فرض ppp؛ Interface با `type vdom-link` ساخته می‌شود | [vdom-link 7.0.11](https://docs.fortinet.com/document/fortigate/7.0.11/cli-reference/5620/config-system-vdom-link) |
| `config log setting` → `fwpolicy-implicit-log` | تأیید مستندی | پیش‌فرض disable؛ جایگزین: Deny صریح با Log | [log setting](https://docs.fortinet.com/document/fortigate/7.2.12/cli-reference/196223761/config-log-setting) |
| `diagnose test authserver ldap <server> <user> <pass>` | تأیید مستندی | نام Object LDAP نه نام میزبان؛ برای جزئیات `diagnose debug application fnbamd 255` | [diagnose test authserver](https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/283783396/diagnose-test-authserver) |
| SD-WAN: `failtime` / `recoverytime` | تأیید مستندی | محدوده ۱ تا ۳۶۰۰؛ پیش‌فرض ۵؛ حداقل توصیه‌ی failtime=۲ | [sdwan 7.0.7](https://docs.fortinet.com/document/fortigate/7.0.7/cli-reference/92620/config-system-sdwan) |
| SD-WAN: `config service` / `mode` | تأیید مستندی با تفاوت نسخه | ۷.۰.۰: `mode priority`؛ ۷.۰.۷ تا ۷.۰.۱۲: auto/manual/priority/sla/load-balance | [sdwan 7.0.12](https://docs.fortinet.com/document/fortigate/7.0.12/cli-reference/74620) |
| `config system global` → `admin-lockout-threshold` / `admin-lockout-duration` | تأیید مستندی | threshold ۱–۱۰ (پیش‌فرض ۳)؛ duration پیش‌فرض ۶۰ ثانیه | [system global 7.0.11](https://docs.fortinet.com/document/fortigate/7.0.11/cli-reference/1620/config-system-global) |
| `cfg-save revert` و `cfg-revert-timeout` | تأیید مستندی | پیش‌فرض timeout ۶۰۰ ثانیه؛ ذخیره‌ی دستی و بازگشت خودکار | [system global](https://docs.fortinet.com/document/fortigate/7.2.3/cli-reference/1620/config-system-global) |
| `diagnose sys ha history read`، `ha checksum cluster`، `get system ha status` | تأیید مستندی | مجموعه‌ی استاندارد عیب‌یابی HA | [diagnose sys](https://docs.fortinet.com/document/fortigate/7.6.2/cli-reference/235530229/diagnose-sys) |
| `config system link-monitor` (`srcintf`، `server`، `gateway-ip`، `failtime`، `recoverytime`، `update-static-route`) | تأیید مستندی | failtime/recoverytime پیش‌فرض ۵؛ update-static-route پیش‌فرض enable | [link-monitor 7.0.10](https://docs.fortinet.com/document/fortigate/7.0.10/cli-reference/120620/config-system-link-monitor) |
| `diagnose vpn ike gateway list`، `diagnose vpn tunnel list`، `diagnose debug application ike -1` | تأیید مستندی | `log-filter` با خط‌تیره تا قبل 7.4.1؛ از 7.4.1 `log filter` با فاصله | [IPsec diagnose](https://docs.fortinet.com/document/fortigate/7.4.9/administration-guide/044240/ipsec-related-diagnose-commands) |
| `diagnose debug flow ...` و Offload | تأیید مستندی | ترافیک Offload‌شده به NP6/NP7 دیده نمی‌شود؛ غیرفعال‌سازی Offload یا آزمون با ICMP | [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.6.4/administration-guide/54688/debugging-the-packet-flow) |
| `config vpn ssl settings` (`tunnel-ip-pools`، `source-interface`، `default-portal`) | تأیید مستندی | نام گزینه‌ها بین پچ‌های ۷.۰ کمی فرق می‌کند | [vpn ssl settings 7.0.3](https://docs.fortinet.com/document/fortigate/7.0.3/cli-reference/363620/config-vpn-ssl-settings) |

## ۲) اصلاحات لازم پس از تطبیق

1. **`diagnose vpn ike log-filter`:** در 7.0.3 با خط‌تیره درست است؛ از 7.4.1 به `log filter` (با فاصله) تغییر کرده. نام فیلتر مبدأ در مستندات جدید `rem-addr4` است (در درس‌ها `dst-addr4` آمده؛ هر دو را با CLI help همان نسخه بررسی کنید).
2. **سطح Debug برای fnbamd:** مستندات 255 را می‌گویند؛ در درس‌ها -1 هم آمده. هر دو رایج‌اند؛ 255 را ترجیح دهید.
3. **`auto-asic-offload` روی Policy:** در جست‌وجو نحو دقیق پیدا نشد؛ با CLI Reference همان نسخه تأیید شود. راه مستند: غیرفعال‌سازی Offload NP یا آزمون با ICMP.
4. **`execute ha failover set`:** فقط برای آزمون است و Flag تا `unset` باقی می‌ماند؛ در Production از `diagnose sys ha reset-uptime` یا روش مستند استفاده شود.
5. **SD-WAN `mode`:** در 7.0.0 نمونه‌ی مستند `mode priority` دارد؛ در پچ‌های بعدی `sla` هم هست. نسخه‌ی دقیق Image را بسنجید.

## ۳) هنوز تأیید نشده (نیازمند جست‌وجوی بعدی یا اجرا)

- `session-pickup-connectionless` / `session-pickup-nat` (درس ۲۲-۳).
- `execute ha synchronize start` (درس ۲۲-۲).
- `diagnose firewall iprope lookup` (در این دور جست‌وجو نشد).
- `diagnose test application dnsproxy 3`.
- نام دقیق پارامترهای SNMPv3 (`auth-proto`، `priv-proto`) در 7.0.3.
- Config IKEv2 سمت Cisco IOS-XE 17.03 (جدا از Fortinet).

## ۴) نتیجه

بیشتر دستورهای پرکاربرد وجود دارند و نام/ساختارشان درست است. تفاوت‌های مهم نسخه (7.4.1 برای IKE log filter و Failtime/Recoverytime SD-WAN، 7.6.3 برای SSL-VPN) در متن درس‌ها آمده است. **هیچ دستور هنوز «اجراشده با شاهد» نیست.**


---

# دور دوم: بررسی مفهومی با منابع رسمی Fortinet و Cisco (۲۰۲۶-۱۱-۲۷)

هدف: درستی **مفاهیم و رفتارها** (نه منوی GUI و تفاوت‌های جزئی نسخه). هر مورد با مستند رسمی/پشتیبانی شده بررسی شد.

## الف) موارد تأییدشده (بدون تغییر)

| موضوع | نتیجه | مرجع |
|---|---|---|
| HSRP: Priority 100، Hello 3/Hold 10، MAC مجازی 0000.0c07.acXX، Preempt پیش‌فرض خاموش | تأیید | [Cisco HSRP](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr3-fwd/fhrp/fhrp-configuration-guide/hsrp.html) |
| BGP: Keepalive 60، Hold 180، eBGP TTL=1، AD eBGP 20 / iBGP 200 | تأیید | [Cisco BGP](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr3-fwd/bgp/bgp-configuration-guide/routing-bgp.html) |
| STP: Hello 2، Forward Delay 15، Max Age 20، Priority 32768 با مضرب 4096، Extended System ID | تأیید | [Cisco STP](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/lan-wan/b-lan-wan/m_lsw-span-tree-prot.html) |
| OSPF: Hello/Dead 10/40 (Broadcast/P2P) و 30/120 (NBMA)، Priority پیش‌فرض 1، DR غیر-Preemptive، Priority 0 = هرگز DR | تأیید | [Cisco OSPF](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13689-17.html) |
| Port Security: Max=1، Violation=shutdown، Sticky پیش‌فرض خاموش، `errdisable recovery cause psecure-violation` | تأیید | [Cisco Port Security](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/16-9/configuration_guide/sec/b_169_sec_9300_cg/b_169_sec_9300_cg_chapter_011011.html) |
| EtherChannel: LACP active/passive، PAgP desirable/auto، `on` فقط با `on`، LACP و PAgP ناسازگارند | تأیید | [Cisco EtherChannel](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960cx_3650cx/software/release/15-2_6_e/configuration_guide/b_1526e_consolidated_3560cx_2960cx_cg/configuring_etherchannels.pdf) |
| FortiGate: DNAT قبل از Route و Policy؛ RPF؛ Policy Route اول؛ Route دو بار در عمر Session | تأیید | [Fortinet Routing concepts](https://docs.fortinet.com/document/fortigate/7.4.1/administration-guide/139692/routing-concepts) |
| FGCP: `hb-interval` پیش‌فرض ۲ (×۱۰۰ms)؛ Session pickup TCP را همگام می‌کند و UDP/ICMP پیش‌فرض نه | تأیید | [Fortinet Session pickup](https://docs.fortinet.com/document/fortigate/8.0.2/administration-guide/955521/session-pickup) |

## ب) اشتباهات پیدا شده و اصلاح‌شده در متن درس‌ها

| # | درس | اشتباه قبلی | اصلاح (طبق مستند) | مرجع |
|---|---|---|---|---|
| 1 | ۱۰-۴ (PBR) | «بسته‌ی غیرمطابق با Route-map بدون Sequence پایانی Drop می‌شود» | بسته‌ی غیرمطابق **با جدول مسیریابی عادی ارسال می‌شود**؛ خطر واقعی Sequence بدون `match` با `set` است | [Cisco PBR](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/configuration/unicast-routing-configuration/cisco-nexus-9000-series-nx-os-unicast-routing-configuration-guide/m_configuring_policy-based_routing_101x.pdf) |
| 2 | ۱۳-۳ (VIP/Hairpin) | `nat-source-vip` به‌عنوان تنظیم Hairpin | `nat-source-vip` برای SNAT ترافیک خروجی سرور نگاشت‌شده با IP خارجی VIP است؛ Hairpin با Policy/`extintf` یا Split DNS حل می‌شود | [Fortinet Hairpin NAT](https://docs.fortinet.com/document/fortigate/8.0.2/administration-guide/736522/hairpin-nat) |
| 3 | ۱۱-۵ و ۱۳-۴ (Timeout) | UDP=۶۰ ثانیه؛ Half-open=۶۰ ثانیه؛ ICMP=۱۰ | مقدار سراسری TCP=۳۶۰۰؛ UDP طبق مستند حدود ۱۸۰ و Service می‌تواند override کند؛ Half-open/ICMP عدد مستند قطعی نیافت (حذف عدد) | [Fortinet session-ttl](https://docs.fortinet.com/document/fortigate/7.6.4/cli-reference/325536976/config-system-session-ttl) |
| 4 | ۱۴-۲ (Sniffer) | جدول Verbosity ناقص/نادقیق (3 = payload) | 1 هدر؛ 2 هدر+IP؛ 3 هدر+Ethernet؛ 4 هدر+Interface؛ 5 هدر+IP+Interface؛ 6 هدر+Ethernet+Interface | [Fortinet sniffer](https://docs.fortinet.com/document/fortigate/8.0.0/administration-guide/680228/performing-a-sniffer-trace-or-packet-capture) |
| 5 | ۱۰-۳ (ECMP) | «پیش‌فرض `maximum-paths` در OSPF = ۴» | عدد ثابت در مستند رسمی نیست؛ بسته به پلتفرم/نسخه؛ با `show ip protocols` | [Cisco IOS Routing Command Reference](https://www.cisco.com/c/en/us/td/docs/ios/iproute_pi/command/reference/iri_book/iri_pi1.html) |
| 6 | ۱۰-۳ (CEF) | `include-ports` بدون Source/Destination | `ip cef load-sharing algorithm include-ports source destination`؛ پیش‌فرض universal | [Cisco CEF load-balancing](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipswitch_cef/configuration/15-mt/isw-cef-15-mt-book/isw-cef-load-balancing.html) |

## ج) محدودیت این بررسی

- این بررسی **نمونه‌ای** است: حدود ۳۰ ادعای پرخطر از ۲۱۳ درس بررسی شد؛ همه‌ی جمله‌های دوره به‌صورت خط‌به‌خط با منبع رسمی تطبیق داده نشده‌اند.
- مفاهیم پایه‌ی رایج (OSI، Subnetting، IPv6، VLAN/Trunk، ACL، NAT، DNS/NTP، Syslog/SNMP، QoS) از دانش استاندارد آمده و در این دور جداگانه با مرجع رسمی چک نشده‌اند.
- دورهای بعدی پیشنهادی: (۱) فصل ۲ تا ۴ Cisco، (۲) فصل ۵ تا ۱۰ مسیریابی، (۳) فصل ۱۱ تا ۱۵ مفاهیم فایروال و FortiGate، (۴) فصل ۱۶ تا ۲۲ (UTM، Auth، IPsec، SD-WAN، HA)، (۵) فصل ۲۳ تا ۳۲.


## دور سوم (۲۰۲۶-۱۱-۲۷)

### تأییدشده
| موضوع | نتیجه | مرجع |
|---|---|---|
| DHCP Snooping: همه‌ی Interfaceها Untrusted؛ Binding Table؛ DAI از Binding استفاده می‌کند؛ DAI Rate-limit پیش‌فرض ۱۵ pps روی Untrusted | تأیید | [Cisco DAI](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/sec-crypto/fhs-sisf/fhs-and-sisf-configuration-guide/dynamic-arp-inspection.html) |
| OSPF Area: Stub بدون LSA 4/5؛ Totally Stubby فقط 1/2 و Default (3)؛ NSSA با LSA 7 | تأیید | [Cisco OSPF Areas](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13703-8.html) |
| NAT: Inside Local/Global، PAT با `overload` و پورت | تأیید | [Cisco NAT](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr3-fwd/nat/nat-configuration-guide/nat.html) |
| QoS: Policing در برابر Shaping؛ EF=46 با LLQ؛ صف اولویت با Policer محدود شود | تأیید | [Cisco Policing vs Shaping](https://www.cisco.com/c/en/us/support/docs/quality-of-service-qos/qos-policing/19645-policevsshape.html) |
| FortiGate SSL Inspection: پروفایل‌های certificate-inspection و deep-inspection؛ CA پیش‌فرض Fortinet_CA_SSL؛ Firefox Trust Store جدا | تأیید | [Fortinet Deep inspection](https://docs.fortinet.com/document/fortigate/7.0.4/administration-guide/122078/deep-inspection) |
| IPsec 7.0: DPD پیش‌فرض on-demand؛ NAT-T پیش‌فرض enable؛ keylife P1=۸۶۴۰۰؛ P2=۴۳۲۰۰؛ PFS پیش‌فرض enable؛ ike-version پیش‌فرض ۱ | تأیید | [phase1-interface 7.0](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/370620/config-vpn-ipsec-phase1-interface) |

### اصلاح/دقیق‌سازی در درس‌ها
| درس | تغییر | مرجع |
|---|---|---|
| ۱۷-۴ (FSSO) | محدودیت «فقط Kerberos» مخصوص FortiGate Polling Connector است؛ Collector Agent در Polling رویدادهای بیشتری (مثلاً 4776) می‌خواند | [Fortinet FSSO polling](https://docs.fortinet.com/document/fortigate/7.4.2/administration-guide/503764/fsso-polling-connector-agent-installation) |
| ۱۴-۶ (Log) | `policyid=0` فقط Implicit Deny نیست؛ ترافیک Local بدون Policy هم policyid=0 دارد؛ `subtype` را بخوانید | [Fortinet: Local traffic logs and policy ID 0](https://community.fortinet.com/t5/FortiGate/Technical-Tip-Local-traffic-logs-and-policy-ID-0/ta-p/196654) |
| ۶-۷ (NSSA) | NSSA برخلاف Stub Default خودکار نمی‌گیرد؛ باید `default-information-originate` روی ABR | [Cisco NSSA](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/6208-nssa.html) |


## دور چهارم — Cisco فصل ۲ تا ۸ (۲۰۲۶-۱۱-۲۷)

### تأییدشده بدون تغییر
| موضوع | نتیجه | مرجع |
|---|---|---|
| `enable secret` (Type 5/8/9، یک‌طرفه) در برابر `enable password`/Type 7 (برگشت‌پذیر)؛ Type 5 منسوخ و مهاجرت به 8/9 توصیه می‌شود | تأیید | [Cisco password types](https://www.cisco.com/c/en/us/support/docs/ios-feature-sets/ios-security-feature-sets/220127-understand-cisco-ios-password-encryption.html) |
| SSH: `ip domain-name`، `crypto key generate rsa` (حداقل 768 بیت برای SSHv2)، `ip ssh version 2` | تأیید (کلید ۲۰۴۸ معتبر؛ `ip ssh dh min size` نکته‌ی تکمیلی) | [Cisco SSHv2](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_ssh/configuration/xe-16/sec-usr-ssh-xe-16-book/sec-secure-shell-v2.html) |
| VLAN: Normal 1–1005؛ 1002–1005 رزرو؛ Extended 1006–4094 | تأیید | [Cisco VLAN](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst6500/ios/15-4SY/config_guide/sup6T/15_3_sy_swcg_6T/vlans.html) |
| IPv6: fe80::/10، ULA fc00::/7 (عملاً fd00::/8)، ff02::1 همه‌ی گره‌ها، ff02::2 روترها، Solicited-node، EUI-64 | تأیید | [Cisco IPv6 white paper](https://www.cisco.com/c/dam/en/us/td/docs/solutions/CVD/Aug2013/CVD-IPv6AddressingWhitePaper-AUG13.pdf) |
| Syslog سطح ۰ تا ۷؛ `logging trap` | تأیید | [Cisco logging](https://www.cisco.com/c/en/us/td/docs/routers/access/wireless/software/guide/SysMsgLogging.html) |
| TACACS+ TCP/49؛ RADIUS UDP 1812/1813؛ Authorization جدا در TACACS+؛ Local Fallback | تأیید | [Cisco TACACS+ vs RADIUS](https://www.cisco.com/c/en/us/support/docs/security-vpn/remote-authentication-dial-user-service-radius/13838-10.pdf) |
| PortFast فقط پورت کاربر؛ BPDU Guard → err-disable؛ Root Guard و Loop Guard هم‌زمان روی یک پورت ممنوع | تأیید | [Cisco Optional STP features](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/16-8/configuration_guide/lyr2_lyr3/b_168_lyr2_lyr3_9300_cg/b_168_lyr2_lyr3_9300_cg_chapter_010.pdf) |

### دقیق‌سازی
| درس | تغییر | مرجع |
|---|---|---|
| ۸-۲ (AAA) | محافظت TACACS+ طبق RFC 8907 «Obfuscation» است نه رمزنگاری مدرن | [Cisco Learning Network](https://learningnetwork.cisco.com/s/question/0D56e0000E3LPXnCQO/radius-vs-tacacs-for-device-administration-with-encryption-requirement) |
| ۳-۴ (RoAS) | `encapsulation dot1Q X native` برای VLAN Native؛ Native دو سر یکسان | [Cisco subinterfaces](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9600/software/release/17-8/configuration_guide/vlan/b_178_vlan_9600_cg/configuring_layer_3_subinterfaces.pdf) |

### هنوز بررسی نشده
شرایط Up شدن SVI، پیام‌ها/Typeهای ICMP، جدول Subnetting (محاسبه‌ای)، نحو دقیق Wireshark، سازوکار Proposal/Agreement در RSTP (تعریف نظری).


## دور پنجم تا هفتم — مسیریابی Cisco و مفاهیم FortiGate (۲۰۲۶-۱۱-۲۷)

### تأییدشده
| موضوع | نتیجه | مرجع |
|---|---|---|
| ترتیب انتخاب Best Path در BGP (Weight، Local-Pref، Locally originated، AS_PATH، Origin، MED، eBGP>iBGP، IGP metric، Router ID) | تأیید با درس ۹-۷ | [Cisco BGP best path](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html) |
| Communityهای well-known (no-export، no-advertise، local-AS) و لزوم `neighbor send-community` | تأیید | [Cisco BGP community](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/26634-bgp-toc.html) |
| Route Reflector: Client/Non-client، ORIGINATOR_ID، CLUSTER_LIST | تأیید | [Cisco RR](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/200153-BGP-Route-Reflection-and-Multiple-Cluste.html) |
| Redistribution: Seed 20 (BGP=1) در OSPF؛ نیاز به Metric در EIGRP؛ ترتیب پارامترهای EIGRP (bandwidth، delay، reliability، load، MTU؛ delay بر حسب ده میکروثانیه) | تأیید | [Cisco Redistribution](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8606-redist.html) |
| `network` در BGP نیاز به Route دقیق در RIB؛ `ip vrf forwarding` آدرس را پاک می‌کند | تأیید | [Cisco VRF-lite](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9600/software/release/17-2/configuration_guide/rtng/b_172_rtng_9600_cg/configuring_vrf_lite.html) |
| FortiOS IP Pool: overload (پیش‌فرض)، one-to-one (PAT خاموش)، fixed-port-range، port-block-allocation | تأیید | [Fortinet ippool](https://docs.fortinet.com/document/fortigate/7.0.2/cli-reference/300620/config-firewall-ippool) |
| Zone `intrazone deny/allow`؛ Local-in policy و Trusted host دو کنترل جدا | تأیید | [Fortinet Zone](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/116821/zone) |
| Flow mode پیش‌فرض 7.0؛ Proxy mode دو Session می‌سازد و ویژگی‌های بیشتر دارد | تأیید | [Fortinet Inspection modes](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/721410/inspection-modes) |
| ADVPN: hub `net-device disable` و `auto-discovery-sender`؛ spoke `auto-discovery-receiver`؛ iBGP | تأیید | [Fortinet ADVPN 7.0.5](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/985659/advpn-and-shortcut-paths) |
| `config system snmp user` با `security-level auth-priv`، `auth-proto sha256`، `priv-proto aes256`؛ پیش‌فرض no-auth-no-priv | تأیید (نام پارامترها) | [Fortinet SNMPv3](https://docs.fortinet.com/document/fortigate/7.0.11/cli-reference/54620/config-system-snmp-user) |
| ADOM Revision در FortiManager (diff و restore) | تأیید | [FortiManager ADOM revisions](https://docs.fortinet.com/document/fortimanager/7.6.6/administration-guide/54616/adom-revisions) |
| محاسبات Subnetting فصل ۲ (۶ مثال Network/Broadcast/Host، Summary، Wildcard) | تأیید با محاسبه‌ی برنامه‌ای | Python `ipaddress` |

### اصلاح/دقیق‌سازی
| درس | تغییر | مرجع |
|---|---|---|
| ۹-۳ | RRهای یک Cluster باید Cluster-ID یکسان داشته باشند (در غیر این صورت Router ID خودشان) | [Cisco RR](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/200153-BGP-Route-Reflection-and-Multiple-Cluste.html) |
| ۱۰-۵ | `ip vrf` قدیمی؛ IOS-XE جدید `vrf definition` + `vrf forwarding`؛ پیام حذف IP | [Cisco VRF-lite](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9600/software/release/17-2/configuration_guide/rtng/b_172_rtng_9600_cg/configuring_vrf_lite.html) |
| ۲۱-۳ | نام‌گذاری Best Quality/Lowest Cost/Maximize Bandwidth؛ از 7.4.1 Load-balance داخل Lowest Cost | [Fortinet SD-WAN strategies](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/342836/lowest-cost-sla-strategy) |
| ۲۴-۳ | Inter-VDOM Link پیش‌فرض ppp؛ برای OSPFv3 نوع ethernet | [Fortinet Inter-VDOM routing](https://docs.fortinet.com/document/fortigate/7.0.2/administration-guide/335646/inter-vdom-routing) |
| ۱۶ (لایسنس) | Signature Application Control جزو FortiCare پایه؛ AV/IPS/Web/DNS لایسنس FortiGuard؛ با انقضا فایروال کار می‌کند و AV/IPS Signature قدیمی را نگه می‌دارند | [Fortinet Services and licensing](https://docs.fortinet.com/document/fortigate/7.4.4/ngfw-atp-deployment-guide/758568/services-and-licensing) |

### هنوز بررسی نشده
نحو دقیق `config log syslogd setting`، `execute ha synchronize start`، `session-pickup-connectionless`، جزئیات DNS Filter و DoS Policy (آستانه‌ها در درس‌ها «نمونه» هستند؛ مرجع: [Fortinet DoS policy](https://docs.fortinet.com/document/fortigate/7.0.14/administration-guide/771644/dos-policy)).
