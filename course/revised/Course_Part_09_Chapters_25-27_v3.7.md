# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۹ از ۱۱ — فصل‌های ۲۵ تا ۲۷

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۹ از ۱۱ |
| فصل‌های این فایل | ۲۵ ، ۲۶ ، ۲۷ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۲۵–۲۷ تولید شد؛ Multi-vendor، FMG/FAZ و جایگزین، Logging/Monitoring/API/Hardening.** Labها «اجرا نشده»؛ FMG/FAZ Needs-License؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 13.

| Lab | وضعیت |
|---|---|
| 25-1 | اجرا نشده (فقط طراحی) |
| 25-2 | اجرا نشده (فقط طراحی) |
| 25-3 | اجرا نشده (فقط طراحی) |
| 25-4 | اجرا نشده (فقط طراحی) |
| 26-1 | اجرا نشده (فقط طراحی) |
| 26-2 | اجرا نشده (فقط طراحی) |
| 26-3 | اجرا نشده (فقط طراحی) |
| 26-4 | اجرا نشده (فقط طراحی) |
| 27-1 | اجرا نشده (فقط طراحی) |
| 27-2 | اجرا نشده (فقط طراحی) |
| 27-3 | اجرا نشده (فقط طراحی) |
| 27-4 | اجرا نشده (فقط طراحی) |
| 27-5 | اجرا نشده (فقط طراحی) |

---

<a id="ch25"></a>

> **نسخه v3.7:** این بخش در دسته‌های B/A/C بدون تغییر محتوایی است (فشرده‌تر از فصل‌های توسعه‌یافته؛ در دسته D بازنویسی می‌شود).

# فصل 25 — Multi-Vendor: FortiGate در کنار Cisco CSR (معماری ۶)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۹، ۱۸، ۱۹.
**اهداف:** اتصال FGT و CSR با BGP/OSPF؛ IPsec چندسازنده؛ تفاوت Terminology؛ Troubleshooting مقایسه‌ای.
**نسخه:** CSR1000v 17.03.02 (IOS-XE) و FortiOS 7.0.3 اسمی؛ آزمایش‌نشده.
**اشتباهات رایج:** پیش‌فرض‌های ناهمسان (Timer، MTU، Lifetime)؛ Router-ID؛ اختلاف Passive-interface.

**درس‌های فصل:**
- [درس 25-1 — تفاوت اصطلاحات Cisco و Fortinet](#l-25-1)
- [درس 25-2 — BGP/OSPF بین FGT و CSR](#l-25-2)
- [درس 25-3 — IPsec چندسازنده و عیب‌یابی مقایسه‌ای](#l-25-3)
- [درس 25-4 — معماری ۶ و آزمون](#l-25-4)

---

<a id="l-25-1"></a>

## درس 25-0 — Interoperability چندسازنده: نگاشت مفاهیم، پیش‌فرض‌های ناهمسان و عیب‌یابی

**فصل ۲۵ · درس افزوده (پیش‌درس ۲۵-۱) · پیش‌نیاز: ۱۸-۰، ۵-۷، ۹-۷ · ≈ ۵ ساعت**

> **وضعیت:** CSR1000v 17.03.02 (IOS-XE) و FortiOS 7.0.3؛ دستورهای CSR/FortiGate `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. نگاشت اصطلاحات Cisco و Fortinet (Interface، Zone، ACL/Policy، Route-map، VRF/VDOM).
2. شناخت **پیش‌فرض‌های ناهمسان** و آثار آن (Timer، MTU، Lifetime، Authentication).
3. اتصال Cisco–FortiGate با OSPF/BGP و IPsec و عیب‌یابی مقایسه‌ای.
4. نوشتن چک‌لیست Interop.

### ۲) مفهوم پایه

پروتکل‌ها استاندارد (RFC) هستند ولی **پیش‌فرض‌ها و محدودیت‌ها** برند-به-برند فرق دارد؛ بیشتر خرابی Interop از «فرض یکسان بودن پیش‌فرض‌ها» می‌آید.

### ۳) توضیح عمیق فنی

#### ۳-۱) نگاشت مفاهیم

| مفهوم | Cisco IOS-XE | FortiOS |
|---|---|---|
| Interface L3 | `interface Gi0/1` + `ip address` | `config system interface` |
| Zone | (Zone-Based Firewall) | `config system zone` |
| ACL/Policy | ACL | Firewall Policy |
| NAT | `ip nat` | Policy NAT/VIP/IP Pool |
| Route-map | `route-map` | `config router route-map` |
| Prefix-list | `ip prefix-list` | `config router prefix-list` |
| VRF | `vrf` | VDOM/VRF |
| نمایش جدول مسیر | `show ip route` | `get router info routing-table all` |
| نمایش Session | `show ip nat translations` | `diagnose sys session list` |

#### ۳-۲) پیش‌فرض‌های ناهمسان (نمونه)

| مورد | Cisco | FortiOS | اثر |
|---|---|---|---|
| OSPF Hello/Dead | 10/40 (Broadcast/P2P) | قابل‌تنظیم؛ باید یکی باشد | Neighbor نمی‌آید |
| OSPF Network Type | Broadcast روی Ethernet | تنظیم دستی | DR/BDR یا P2P ناسازگار |
| MTU | 1500 | 1500؛ Tunnel کمتر | OSPF Exstart |
| IKEv2 | قابل‌تنظیم | IKEv1 پیش‌فرض در 7.0 (CLI Ref) | عدم توافق |
| PFS | Group تنظیم | PFS پیش‌فرض enable | Phase 2 ناسازگار |
| Lifetime | IKE 24h، IPsec 1h (پیش‌فرض‌های متداول؛ `Unverified`) | 86400/43200 | Rekey ناهمسان |
| BGP Hold | 180 | 180 (متداول؛ `Unverified`) | — |

(جدول بر پایه‌ی پیش‌فرض‌های متداول است؛ هر مقدار را در Lab بخوانید.)

#### ۳-۳) استراتژی Interop

1. هر دو سمت را **صریح** پیکربندی کنید؛ به پیش‌فرض‌ها تکیه نکنید.
2. یک «برگه‌ی پارامتر» مشترک (Proposal، DH، PFS، Timer، MTU، MSS، Auth).
3. تست مرحله‌ای: L3 → Routing → IPsec → Policy.
4. عیب‌یابی با Debug **هر دو سو** هم‌زمان.

### ۴) مثال حل‌شده

**OSPF FGT–CSR:** Neighbor در Exstart می‌ماند. شواهد: `show ip ospf neighbor` (CSR) Exstart؛ `get router info ospf neighbor` (FGT). **علت:** MTU متفاوت (Tunnel/VLAN). **رفع:** MTU یکسان یا `ip ospf mtu-ignore` (CSR؛ با ریسک؛ `Unverified`). **تأیید:** Full.

``` text
! CSR
interface Tunnel0
 ip mtu 1400
 ip ospf network point-to-point
router ospf 1
 network 10.255.0.0 0.0.0.3 area 0
```

``` text
# FortiGate
config router ospf
    config ospf-interface
        edit "TO-CSR"
            set interface "TO-CSR"
            set network-type point-to-point
        next
    end
end
```

**IPsec Interop (مثال سخت):** Phase 1 OK، Phase 2 NO_PROPOSAL_CHOSEN. فرضیه‌ها: PFS/DH Group، Transform، Selector. شاهد: Debug هر دو؛ **رفع:** تطبیق PFS Group و Proposal.

### ۵) GUI و CLI

FortiGate: Network → OSPF/BGP؛ VPN → IPsec Tunnels. CSR: CLI. **Verification:** `show ip ospf neighbor`/`get router info ospf neighbor`؛ `show crypto ikev2 sa`/`diagnose vpn ike gateway list`.

### ۶) نکات امنیتی

- Authentication OSPF/BGP هر دو سمت یکسان.
- از الگوریتم‌های قوی مشترک.

### ۷) جمع‌بندی

- پروتکل یکی؛ پیش‌فرض‌ها فرق دارد.
- پیکربندی صریح + برگه‌ی پارامتر.
- Debug دو سمتی.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) معادل `show ip route` در FortiOS؟ *(پاسخ: 25-0-ت1)*

**ت2.** (متوسط) چرا OSPF در Exstart می‌ماند؟ *(پاسخ: 25-0-ت2)*

**ت3.** (سخت) یک برگه‌ی پارامتر IPsec بین FGT و CSR بنویسید. *(پاسخ: 25-0-ت3)*

**Q1.** Quick quiz (English): Why shouldn't you rely on vendor defaults in multi-vendor links? *(پاسخ: 25-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Interop | Interoperability | سازگاری |
| Exstart | OSPF ExStart state | مرحله‌ی تبادل DBD |
| mtu-ignore | OSPF MTU ignore | نادیده‌گرفتن MTU |

- *Configure parameters explicitly on both vendors.* ← پارامترها را روی هر دو سازنده صریحاً تنظیم کنید.

### ۱۰) منابع

- Cisco: IOS XE OSPF/IKEv2 Configuration Guides؛ Fortinet Docs: FortiOS 7.0 CLI Reference (`config router ospf`، `phase1-interface`)؛ RFC 2328، RFC 7296.

## درس 25-1 — نگاشت مفاهیم Cisco و Fortinet: برگه‌ی تطبیق دستورها و مدل‌های پردازش

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۰، ۱۲-۰ · ≈ 5 ساعت**

> **وضعیت:** FortiOS 7.0.3 و CSR1000v 17.03.02 (بوت‌نشده/اجرا نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مدل پردازش بسته را در IOS-XE و FortiOS مقایسه کند.
2. برگه‌ی تطبیق دستورها (نمایش/تنظیم/عیب‌یابی) را بسازد.
3. تفاوت‌های مدل (ACL در برابر Policy، Zone) را در طراحی لحاظ کند.

### ۲) مفهوم پایه: چیست و چرا؟

مهندس چندسازنده باید «ترجمه‌ی مفهومی» بلد باشد، نه فقط دستور. تفاوت اصلی: Cisco روتر/سوئیچ‌محور با ACL/NAT/Zone-Based Firewall؛ Fortinet فایروال‌محور با Policy و Session.

### ۳) توضیح عمیق فنی

#### تطبیق

| کار | Cisco IOS-XE | FortiOS |
|---|---|---|
| جدول مسیر | show ip route | get router info routing-table all |
| Interface | show ip interface brief | get system interface physical / show system interface |
| ARP | show ip arp | get system arp |
| Session/NAT | show ip nat translations | diagnose sys session list |
| Policy/ACL | show access-lists | show firewall policy |
| OSPF | show ip ospf neighbor | get router info ospf neighbor |
| BGP | show ip bgp summary | get router info bgp summary |
| IPsec | show crypto ikev2 sa | diagnose vpn ike gateway list |
| Sniffer | monitor capture | diagnose sniffer packet |
| Debug flow | debug ip packet (خطرناک) | diagnose debug flow |
| Backup | copy running-config tftp | execute backup config tftp |
| CLI mode | enable/conf t | config / edit / next / end |

#### مدل‌ها

- IOS: ACL روی Interface (in/out)؛ NAT ip nat inside/outside؛ Stateful فقط با ZBFW/Inspect.
- FortiOS: Policy بین Interface/Zone؛ Stateful پیش‌فرض؛ NAT در Policy؛ Session Table مرکز تصمیم.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** `show ip route` ⇄ `get router info routing-table all`.

**متوسط:** ACL ورودی IOS ⇄ Policy با srcintf در FortiOS؛ تفاوت: Implicit deny و Stateful.

**سخت:** انتقال یک ACL با ۴۰ خط و NAT به Policy: ترتیب NAT/ACL در IOS با FortiOS فرق دارد؛ تست رفتاری لازم است.

### ۸) Verification (اثبات صحت)

- برگه‌ی تطبیق در Lab امتحان شود.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| دستور شناخته نمی‌شود | پیام CLI | Syntax برند |

### ۱۰) نکات امنیتی

- Backup از هر دو.

### ۱۱) جمع‌بندی مفهومی

- ترجمه‌ی مفهومی؛ مدل پردازش متفاوت.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) معادل show ip arp؟ *(پاسخ: 25-1-ت1)*

**ت2.** (ساده) معادل ACL؟ *(پاسخ: 25-1-ت2)*

**ت3.** (متوسط) تفاوت Stateful؟ *(پاسخ: 25-1-ت3)*

**ت4.** (سخت) انتقال ACL+NAT. *(پاسخ: 25-1-ت4)*

**ت5.** (سخت، طراحی) برگه‌ی تطبیق ۱۵ سطری. *(پاسخ: 25-1-ت5)*

**Q1.** Quick quiz (English): What is the FortiOS equivalent of an interface ACL? *(پاسخ: 25-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ZBFW | Zone-Based Policy Firewall | فایروال مبتنی بر Zone سیسکو |

- *Translate concepts, not just commands.* ← مفاهیم را ترجمه کنید نه فقط دستورها.

### ۱۴) کارت Lab

**Lab:** جدول معادل. **Evidence:** `02-design/vendor-map.md`.

### ۱۵) منابع

- Cisco IOS XE Command Reference
- Fortinet CLI Reference 7.0

<a id="l-25-2"></a>

## درس 25-2 — OSPF و BGP بین FortiGate و CSR: برگه‌ی پارامتر، پیکربندی دوطرفه، Redistribution و عیب‌یابی مقایسه‌ای

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۰، ۲۵-۱، ۶-۱، ۹-۷، ۱۰-۱ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 و CSR1000v 17.03.02 (IOS-XE)؛ بوت‌نشده؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. OSPF و eBGP بین FGT و CSR را با برگه‌ی پارامتر مشترک بسازد.
2. تفاوت پیش‌فرض‌ها (Hello/Dead، Network Type، MTU، Timer، Auth) و اثر ناسازگاری را بگوید.
3. Redistribution دوطرفه و جلوگیری از Loop (Tag/Route-map) را پیاده کند.
4. Verification را با دستورهای هر دو سازنده انجام و مقایسه کند.
5. Neighbor Stuck (Init/Exstart/Active) را با شواهد هر دو سر عیب‌یابی کند.
6. Convergence و Failover را اندازه بگیرد.

### ۲) مفهوم پایه: چیست و چرا؟

بین دو سازنده، پروتکل یکی است ولی هر سازنده «پیش‌فرض‌ها» و «محدودیت‌ها»ی خودش را دارد. بیشتر مشکلات Interop از فرض یکسان بودن پیش‌فرض‌ها می‌آید: Hello/Dead، MTU، Network Type، یا رفتار Redistribution/Metric. روش درست: برگه‌ی پارامتر مشترک، پیکربندی صریح دو سر، و Debug هم‌زمان.

### ۳) توضیح عمیق فنی

#### ۱) برگه‌ی پارامتر (مشترک)

``` text
Link FGT port3 <-> CSR Gi2 : 10.255.0.0/30  (FGT .2, CSR .1)   MTU 1500 both
OSPF : area 0, network type point-to-point, hello 10, dead 40, auth MD5 key 1 <KEY>
BGP  : CSR AS 65001 router-id 1.1.1.1 ; FGT AS 65002 router-id 2.2.2.2
       eBGP over 10.255.0.1/.2, hold 180 (or 9/3 with BFD), prefix-lists both directions
Redistribution: OSPF<->BGP with tags; never both ways without tag
```

#### ۲) پیکربندی

``` text
! CSR (IOS-XE)
interface GigabitEthernet2
 ip address 10.255.0.1 255.255.255.252
 ip ospf network point-to-point
 ip ospf message-digest-key 1 md5 <KEY>
 ip ospf authentication message-digest
 ip mtu 1500
router ospf 1
 router-id 1.1.1.1
 network 10.255.0.0 0.0.0.3 area 0
router bgp 65001
 bgp router-id 1.1.1.1
 neighbor 10.255.0.2 remote-as 65002
 neighbor 10.255.0.2 prefix-list FROM-FGT in
 neighbor 10.255.0.2 prefix-list TO-FGT out
```

``` text
# FortiGate
config router ospf
    set router-id 2.2.2.2
    config area
        edit 0.0.0.0
        next
    end
    config network
        edit 1
            set prefix 10.255.0.0 255.255.255.252
        next
    end
    config ospf-interface
        edit "TO-CSR"
            set interface "port3"
            set network-type point-to-point
            set authentication md5
            set md5-key 1 <KEY>
        next
    end
end
config router bgp
    set as 65002
    set router-id 2.2.2.2
    config neighbor
        edit "10.255.0.1"
            set remote-as 65001
            set prefix-list-in "FROM-CSR"
            set prefix-list-out "TO-CSR"
        next
    end
end
```

(نام فیلدهای FortiOS `Unverified`؛ با CLI Reference 7.0 تطبیق شود.)

#### ۳) Redistribution امن

``` text
FGT: redistribute ospf into bgp with route-map tag 100; redistribute bgp into ospf only routes WITHOUT tag 100
CSR: same tag logic
```

بدون Tag، Prefix بین OSPF و BGP رفت‌وبرگشت می‌کند و حلقه یا Metric بی‌ثبات ایجاد می‌شود (۱۰-۲).

#### ۴) جدول Verification

| سؤال | CSR | FortiGate |
|---|---|---|
| همسایه OSPF | `show ip ospf neighbor` | `get router info ospf neighbor` |
| LSDB | `show ip ospf database` | `get router info ospf database` |
| BGP | `show ip bgp summary` | `get router info bgp summary` |
| Route | `show ip route` | `get router info routing-table all` |
| دریافتی BGP | `show ip bgp neighbors X received-routes` | `get router info bgp neighbors X received-routes` |

#### ۵) ناسازگاری‌های رایج

MTU (Exstart)، Network Type (DR/BDR در یک سر)، Auth، Hello/Dead، Timer BGP، `next-hop` و Filter، AD (eBGP 20 vs OSPF 110؛ مسیر BGP برنده می‌شود).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| OSPF یا BGP | OSPF داخلی/لینک؛ BGP برای مقیاس/Policy |
| AD | دقت AD: BGP 20 (eBGP) vs OSPF 110 |
| Auth | MD5/SHA هر دو سر |
| Tag | اجباری در Redistribution دوطرفه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** OSPF Full و eBGP Established؛ Route 10.10.0.0/16 (CSR) در FGT با AD 20 (BGP)؛ ping از LAN CSR به LAN FGT موفق.

**متوسط (تحلیل):** OSPF در Exstart: CSR Tunnel MTU 1400 و FGT 1500؛ DBD ارسالی بزرگ‌تر از MTU همتا؛ رفع: MTU یکسان یا `ip ospf mtu-ignore` (ریسک: ناپایداری). شواهد: دو سر `neighbor` و Debug OSPF.

**سخت (Redistribution):** پس از Redistribution دوطرفه بدون Tag، Prefix 10.10.0.0/16 مدام تغییر می‌کند (BGP→OSPF→BGP). علت: Loop Redistribution. شواهد: `show ip bgp 10.10.0.0` Path عجیب و Flap؛ رفع: Tag و Route-map؛ تأیید: Route پایدار؛ آزمون: قطع لینک و بازگشت.

### ۸) Verification (اثبات صحت)

- Neighbor Full/Established.
- Route‌ها در هر دو.
- آزمون قطع لینک و Convergence.
- آزمون منفی: Prefix غیرمجاز رد می‌شود.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Exstart | MTU | هم‌سان |
| Init | Hello/Auth/Policy | همسان |
| BGP Active | TCP 179/AS | Policy/AS |
| Route نصب نمی‌شود | Next-hop/AD | Route/Distance |
| Flap مسیر | Redistribution | Tag |

### ۱۰) نکات امنیتی

- Authentication OSPF/BGP.
- Prefix-list ورودی/خروجی.
- Max-prefix.

### ۱۱) جمع‌بندی مفهومی

- برگه‌ی پارامتر مشترک.
- MTU/Network Type/Auth ناسازگاری‌های اصلی.
- Redistribution با Tag.
- Verification دوطرفه.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا OSPF در Exstart می‌ماند؟ *(پاسخ: 25-2-ت1)*

**ت2.** (ساده) AD پیش‌فرض eBGP و OSPF در Cisco؟ *(پاسخ: 25-2-ت2)*

**ت3.** (متوسط) مقایسه‌ی دستور Verification OSPF در دو سازنده. *(پاسخ: 25-2-ت3)*

**ت4.** (متوسط) چرا Tag در Redistribution دوطرفه؟ *(پاسخ: 25-2-ت4)*

**ت5.** (سخت) Prefix بین OSPF و BGP Flap می‌کند؛ تحلیل و رفع. *(پاسخ: 25-2-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی پارامتر برای ۳ Link بین FGT و CSR. *(پاسخ: 25-2-ت6)*

**Q1.** Quick quiz (English): Why can a bidirectional redistribution without tags create a routing loop? *(پاسخ: 25-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DBD | Database Description packet | بسته‌ی توصیف پایگاه |
| Tag | Route tag | برچسب مسیر |
| AD | Administrative Distance | اعتبار منبع مسیر |

- *Match MTU, network type and authentication on both vendors.* ← MTU، Network Type و Auth را در هر دو سازنده یکسان کنید.

### ۱۴) کارت Lab

**کارت Lab:** OSPF/BGP FGT–CSR. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ospf-fgt-csr.md`.

### ۱۵) منابع

- RFC 2328
- RFC 4271
- Cisco IOS XE OSPF/BGP Configuration Guides
- Fortinet CLI Reference 7.0

<a id="l-25-3"></a>

## درس 25-3 — IPsec چندسازنده: روش مقایسه‌ی Debug، جدول مغایرت و Interop آزمایشی FGT–CSR

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۰، ۱۸-۰، ۱۸-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 و CSR1000v 17.03.02 (IOS-XE)؛ بوت‌نشده؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Tunnel IKEv2 بین FGT و CSR را با برگه‌ی پارامتر مشترک بسازد.
2. Debug هر دو سر را هم‌زمان بگیرد و اولین مغایرت را بیابد.
3. پیام‌های خطا را بین دو سازنده نگاشت کند.
4. Rekey/DPD/NAT-T/MTU را آزمایش کند.
5. گزارش Interop (پارامتر، نتیجه، محدودیت) بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

در Interop، هر سازنده خطا را به زبان خودش گزارش می‌کند. «روش مقایسه‌ی دو Debug» سریع‌ترین راه برای پیدا کردن مغایرت است.

### ۳) توضیح عمیق فنی

#### ۱) روش

``` text
1 Same time window: start debug on both peers; trigger negotiation (clear SA / ping)
2 Save logs; align by timestamp
3 Find first divergence: the message where one side rejects/aborts
4 Map to parameter: proposal, DH, PRF, ID, selectors, lifetime, PFS
5 Change ONE parameter; repeat
```

#### ۲) نگاشت پیام‌ها

| وضعیت | CSR (IOS-XE) | FortiGate | علت |
|---|---|---|---|
| Proposal ناسازگار | `no matching proposal` | `NO_PROPOSAL_CHOSEN` | Cipher/PRF/DH |
| Auth | `AUTH FAILED` | `AUTH_FAILED` | PSK/ID |
| Selector | `TS unacceptable` | `TS_UNACCEPTABLE` | Selector |
| DH | `INVALID_KE_PAYLOAD` | `INVALID_KE_PAYLOAD` | گروه DH |
| پایان | `SA deleted` | `delete` | Lifetime/DPD |

#### ۳) آزمون‌های Interop

- Rekey: Lifetime کوتاه (مثلاً 600 s) و مشاهده‌ی Rekey بدون قطع.
- DPD: قطع یک سر؛ زمان کشف.
- NAT-T: Peer پشت NAT.
- MTU: ping DF بزرگ.
- PFS: Group یکسان.

``` text
CSR: show crypto ikev2 sa detailed ; show crypto ipsec sa
FGT: diagnose vpn ike gateway list ; diagnose vpn tunnel list
```

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Up با AES-GCM-256، DH 20؛ `show crypto ipsec sa` pkts encaps/decaps هر دو افزایش.

**متوسط (تحلیل):** Phase 2 شکست: CSR `TS unacceptable`، FGT `TS_UNACCEPTABLE`؛ Selector CSR 10.10.0.0/16↔10.20.0.0/16 و FGT 0.0.0.0/0؛ رفع: any/any روی هر دو (Route-based) یا آینه‌کردن.

**سخت (قطع دوره‌ای):** Tunnel هر ~۶۰ دقیقه قطع می‌شود: CSR Lifetime IPsec 3600 s و FGT 43200؛ هنگام Rekey با Proposal/PFS متفاوت شکست. شواهد: Log هر دو؛ رفع: یکسان‌سازی Lifetime/PFS؛ آزمون ۴ ساعته.

### ۸) Verification (اثبات صحت)

- Evidence Interop: پارامتر/خروجی/نتیجه.
- Rekey بدون قطع.
- DPD آزمایشی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Phase1 شکست | Debug | Proposal/DH/PSK |
| Phase2 شکست | Debug | Selector/PFS |
| قطع دوره‌ای | Log | Lifetime |
| یک جهت | counters | Policy/Route |

### ۱۰) نکات امنیتی

- PSK قوی؛ الگوریتم‌های ضعیف ممنوع.

### ۱۱) جمع‌بندی مفهومی

- مقایسه‌ی Debug دو سر.
- نگاشت پیام‌ها.
- آزمون Rekey/DPD/NAT-T/MTU.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) معادل NO_PROPOSAL_CHOSEN در CSR؟ *(پاسخ: 25-3-ت1)*

**ت2.** (ساده) چرا Debug هم‌زمان؟ *(پاسخ: 25-3-ت2)*

**ت3.** (متوسط) TS unacceptable چگونه رفع می‌شود؟ *(پاسخ: 25-3-ت3)*

**ت4.** (متوسط) آزمون Rekey چگونه؟ *(پاسخ: 25-3-ت4)*

**ت5.** (سخت) Tunnel هر ساعت قطع می‌شود؛ تحلیل. *(پاسخ: 25-3-ت5)*

**ت6.** (سخت، طراحی) گزارش Interop. *(پاسخ: 25-3-ت6)*

**Q1.** Quick quiz (English): How do you locate the cause of an interop IKE failure efficiently? *(پاسخ: 25-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Divergence | First divergence point | اولین نقطه‌ی اختلاف |
| PRF | Pseudo-random function | تابع شبه‌تصادفی |

- *Debug both peers in the same time window.* ← هر دو Peer را در یک بازه‌ی زمانی Debug کنید.

### ۱۴) کارت Lab

**کارت Lab:** IPsec FGT–CSR. **Evidence:** `03-ops/ipsec-mv.md`.

### ۱۵) منابع

- RFC 7296
- Cisco IKEv2 guides
- Fortinet IPsec CLI Reference 7.0

<a id="l-25-4"></a>

## درس 25-4 — آزمون معماری ۶ (FGT+CSR): صورت مسئله، کلید پاسخ و Rubric

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۰ تا ۲۵-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 و CSR1000v 17.03.02 (IOS-XE)؛ بوت‌نشده؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. اتصال FGT–CSR با Routing و IPsec را با شواهد تحویل دهد.
2. سه عیب تزریق‌شده (MTU، Proposal، Redistribution) را رفع کند.
3. Failover و Backup هر دو سازنده را انجام دهد.
4. گزارش Interop و RCA ارائه دهد.

### ۲) مفهوم پایه: چیست و چرا؟

آزمون جامع چندسازنده با شواهد. کلید پاسخ پس از تلاش.

### ۳) توضیح عمیق فنی

#### صورت مسئله

HQ: CSR؛ شعبه: FGT؛ دو لینک (WAN1/WAN2). نیاز: OSPF داخلی، eBGP لبه، IPsec IKEv2 روی هر دو لینک، Failover < ۱۰ ثانیه، Backup هر دو.

عیب‌ها: ۱) MTU Tunnel ناهمسان؛ ۲) PFS Group متفاوت؛ ۳) Redistribution بدون Tag.

#### کلید پاسخ (خلاصه)

- OSPF Exstart ← MTU؛ IPsec Phase2 ← PFS؛ Flap ← Tag.
- Failover با BFD/Local-pref؛ اندازه‌گیری ≈ ۶ ثانیه.
- Backup: `copy running-config` و `execute backup config`.

#### Rubric

اتصال ۲۵؛ عیب‌یابی ۳۰؛ Failover ۱۵؛ Backup ۱۰؛ گزارش/Evidence ۱۵؛ صداقت ۵.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Up و Route‌ها.

**متوسط:** سه عیب رفع.

**سخت:** Failover و گزارش.

### ۸) Verification (اثبات صحت)

- Evidence A6.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Failover کند | Timer | BFD |

### ۱۰) نکات امنیتی

- Secret پاک.

### ۱۱) جمع‌بندی مفهومی

- آزمون با شواهد.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) سه عیب آزمون؟ *(پاسخ: 25-4-ت1)*

**ت2.** (ساده) Backup هر دو سازنده چگونه؟ *(پاسخ: 25-4-ت2)*

**ت3.** (متوسط) چگونه Failover < ۱۰ s را اثبات می‌کنید؟ *(پاسخ: 25-4-ت3)*

**ت4.** (متوسط) عیب PFS را از Debug چگونه می‌فهمید؟ *(پاسخ: 25-4-ت4)*

**ت5.** (سخت) RCA برای Flap Redistribution. *(پاسخ: 25-4-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی بهبود. *(پاسخ: 25-4-ت6)*

**Q1.** Quick quiz (English): What artifacts must be backed up in a multi-vendor design? *(پاسخ: 25-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| A6 | Architecture 6 | معماری ۶ |

- *Back up both vendors.* ← از هر دو سازنده Backup بگیرید.

### ۱۴) کارت Lab

**کارت Lab:** A6. **Evidence:** `03-ops/a6.md`.

### ۱۵) منابع

- درس‌های ۲۵-۱ تا ۲۵-۳

## پاسخ‌های فصل 25

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی درس 25-1

**25-1-ت1** — get system arp.

**25-1-ت2** — Firewall Policy.

**25-1-ت3** — FortiOS پیش‌فرض Stateful؛ ACL ساده نه.

**25-1-ت4** — تست رفتاری.

**25-1-ت5** — جدول بالا بسط داده شود.

**25-1-Q1** — A firewall policy between interfaces or zones.


### پاسخ‌های بازنویسی عمیق درس 25-2

**25-2-ت1** — معمولاً MTU متفاوت؛ DBD بزرگ‌تر از MTU همتا کنار گذاشته می‌شود.

**25-2-ت2** — eBGP = 20 و OSPF = 110؛ پس BGP برنده است.

**25-2-ت3** — CSR: `show ip ospf neighbor`؛ FGT: `get router info ospf neighbor`.

**25-2-ت4** — تا Prefix دوباره به منبعش بازگردانده نشود؛ از Loop و Flap جلوگیری می‌کند.

**25-2-ت5** — Loop Redistribution؛ افزودن Tag/Route-map، حذف Redistribute یک‌جهته در صورت نیاز؛ آزمون قطع/بازگشت.

**25-2-ت6** — جدول: IP/MTU/Area/Network Type/Auth/Timer/BGP AS/Filter برای هر Link.

**25-2-Q1** — Because routes can be redistributed back into their source protocol repeatedly.


### پاسخ‌های بازنویسی عمیق درس 25-3

**25-3-ت1** — `no matching proposal`.

**25-3-ت2** — هر سمت بخش دیگری از مذاکره را می‌بیند؛ مقایسه اولین مغایرت را نشان می‌دهد.

**25-3-ت3** — Selector آینه یا any/any در Route-based.

**25-3-ت4** — Lifetime کوتاه و ping پیوسته؛ باید بدون قطع Rekey شود.

**25-3-ت5** — Lifetime/PFS ناهمسان؛ Log دو سر؛ یکسان‌سازی؛ آزمون طولانی.

**25-3-ت6** — جدول پارامتر/نتیجه/محدودیت/تاریخ/نسخه.

**25-3-Q1** — Capture debug from both peers in the same time window and find the first diverging message.


### پاسخ‌های بازنویسی عمیق درس 25-4

**25-4-ت1** — MTU ناهمسان، PFS Group متفاوت، Redistribution بدون Tag.

**25-4-ت2** — CSR: copy running-config tftp/scp؛ FGT: execute backup config tftp/sftp.

**25-4-ت3** — قطع لینک و ping پیوسته؛ شمارش بسته‌ها × فاصله؛ ثبت.

**25-4-ت4** — `INVALID_KE_PAYLOAD`/`NO_PROPOSAL_CHOSEN` در Phase 2؛ مقایسه‌ی PFS Group دو سر.

**25-4-ت5** — علامت: Flap Prefix؛ شواهد: Path/Route؛ علت: Loop بدون Tag؛ رفع: Tag؛ پیشگیری: استاندارد Route-map.

**25-4-ت6** — برگه‌ی پارامتر مشترک، استاندارد MTU، قالب Redistribution با Tag، BFD، آزمون دوره‌ای.

**25-4-Q1** — Configurations of both vendors, including routing and VPN settings, stored without secrets in version control.

### پاسخ‌های درس افزوده‌ی 25-0 (فصل 25)

**25-0-ت1** — get router info routing-table all.

**25-0-ت2** — اغلب MTU Mismatch بین دو سر.

**25-0-ت3** — IKEv2، AES-256-GCM، SHA-256، DH 20 (یا ≥ 14)، PFS روشن با همان Group، Lifetime یکسان، DPD، MTU/MSS مشترک، Authentication PSK/Cert.

**25-0-Q1** — Because defaults differ between vendors and cause subtle mismatches.

# فصل 26 — FortiManager و FortiAnalyzer (معماری ۹) و جایگزین‌های بدون لایسنس

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۲۲، ۲۵.
**هشدار لایسنس:** FortiManager (FMG) و FortiAnalyzer (FAZ) VM به لایسنس/Evaluation نیاز دارند (`Needs-License`). این فصل **مفهوم و طراحی** را آموزش می‌دهد و **جایگزین عملی بدون لایسنس** (rsyslog/Zabbix و Backup خودکار) را در Lab اجرا می‌کند. هیچ ادعای اجرا روی FMG/FAZ نشده است.
**اهداف:** مدیریت مرکزی؛ Policy Package؛ Log مرکزی؛ جایگزین.
**اشتباهات رایج:** انتظار FMG/FAZ رایگان؛ نبود Backup.

**درس‌های فصل:**
- [درس 26-1 — مفهوم FMG/FAZ و لایسنس](#l-26-1)
- [درس 26-2 — Syslog مرکزی (جایگزین FAZ)](#l-26-2)
- [درس 26-3 — Backup خودکار و Config Management](#l-26-3)
- [درس 26-4 — طراحی معماری ۹ و آزمون](#l-26-4)

---

<a id="l-26-1"></a>

## درس 26-0 — مدیریت مرکزی: معماری FortiManager و FortiAnalyzer، ADOM، Policy Package و محدودیت لایسنس

**فصل ۲۶ · درس افزوده (پیش‌درس ۲۶-۱) · پیش‌نیاز: ۱۲-۰، ۱۳-۷، ۲۲-۰ · ≈ ۵ ساعت**

> **وضعیت (FortiManager/FortiAnalyzer 7.0):** مفهوم ADOM، Install Wizard، افزودن FAZ و تداخل Log Forwarding از مستند رسمی بررسی شد ([Device Manager](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/478145/device-manager)، [Add FortiAnalyzer](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/654379/add-fortianalyzer)، [Installing policy packages](https://docs.fortinet.com/document/fortimanager/7.0.7/administration-guide/153046/installing-policy-packages-and-device-settings)). **Needs-License:** FMG/FAZ VM به لایسنس/Evaluation نیاز دارند؛ **هیچ ادعای اجرا روی آن‌ها نشده است.** جزئیات لایسنس VM باید از مستند/فروشنده تأیید شود (`Unverified`). Lab: جایگزین عملی با rsyslog و Backup.

### ۱) هدف آموزشی

1. نقش **FMG** (مدیریت پیکربندی) و **FAZ** (Log/Report) را تفکیک کند.
2. **ADOM، Device Manager، Policy Package، Install** و **Revision** را توضیح دهد.
3. معماری مدیریت مرکزی برای ۱۰ تا ۱۰۰ دستگاه را طراحی و ریسک‌ها را بگوید.
4. **جایگزین بدون لایسنس** (Syslog مرکزی + Git/Backup + Ansible/API) را طراحی کند.
5. RBAC و Audit مدیریت مرکزی را بنویسد.

### ۲) مفهوم پایه

مدیریت ۲۰ فایروال یکی‌یکی = ناهمگونی، خطا، بی‌Audit. **FMG** پیکربندی/Policy را مرکزی نگه می‌دارد و به دستگاه‌ها «نصب» می‌کند؛ **FAZ** Logها را جمع و تحلیل می‌کند. مرکزی‌سازی هم **سطح حمله** و هم **نقطه‌ی شکست** جدید است.

### ۳) توضیح عمیق فنی

#### ۳-۱) اجزا

- **Device Manager:** ثبت دستگاه‌ها و گروه‌ها، وضعیت Sync.
- **ADOM (Administrative Domain):** بخش مجزا برای دستگاه‌ها/مدیران؛ هر ADOM Policy Package و Object خودش را دارد (برای Multi-tenant یا نسخه‌های مختلف).
- **Policy Package:** مجموعه‌ی Policy/Object که به یک یا چند دستگاه **نصب (Install)** می‌شود؛ مستند: Install Wizard → انتخاب Package و مقصد و زمان‌بندی اختیاری.
- **Device Settings:** تنظیمات مختص دستگاه (Interface، Route).
- **Revision History:** نسخه‌ی تنظیمات؛ بازگشت (Revert).

#### ۳-۲) FAZ

- FAZ Logهای FortiGate را جمع می‌کند (Log Forwarding/Fetching).
- طبق مستند: در FMG با ADOM فعال می‌توان یک FAZ به هر ADOM وصل کرد؛ نام ADOM باید در هر دو یکی باشد؛ و **وقتی ویژگی‌های FAZ در FMG فعال است، Log Forwarding/Fetching/Aggregation پشتیبانی نمی‌شود**؛ افزودن FAZ، قابلیت‌های FAZ را خودکار فعال می‌کند و غیرفعال‌شدنی نیست.

#### ۳-۳) ریسک‌های مرکزی‌سازی

| ریسک | کاهش |
|---|---|
| FMG هدف حمله/نقطه‌ی شکست | شبکه‌ی مدیریت جدا، HA، RBAC، MFA |
| Install اشتباه روی همه | Staging/ADOM آزمایشی، Install Preview، Revision |
| Sync نامنظم | بررسی وضعیت Sync، Install زمان‌بندی‌شده |
| لایسنس | برنامه‌ریزی/جایگزین |

#### ۳-۴) جایگزین بدون لایسنس (برای Lab)

``` text
Config backup : execute backup config tftp/sftp (daily) -> Git repo (no secrets)
Logs          : config log syslogd setting -> rsyslog -> (Zabbix/ELK)
Monitoring    : SNMPv3 + Zabbix
Automation    : REST API/Ansible (read-first)
Change record : ticket + diff of configs
```

#### ۳-۵) Syslog (جایگزین FAZ)

طبق CLI Reference 7.0: `config log syslogd setting` گزینه‌های `server`، `port` (پیش‌فرض 514)، `mode` (udp، reliable، legacy-reliable)، `facility`، `source-ip`، `format` (default، csv، cef، rfc5424) و TLS را دارد؛ **حالت reliable** برای Extended Logging لازم است (مستند Log Message Reference).

### ۴) مثال حل‌شده

**نیاز:** Log مرکزی بدون FAZ.

``` text
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set mode reliable
    set port 514
    set format rfc5424
    set facility local7
end
```

(ممکن است برای TCP/TLS پورت دیگری لازم باشد؛ سینتکس `Unverified`.) سمت rsyslog: Listener TCP، قالب RFC5424، چرخش Log. **آزمون:** تولید رویداد (Login ناموفق) و دیدن آن در سرور؛ بررسی Timestamp و NTP.

**مثال متوسط:** پس از Install Policy Package به ۳ دستگاه، یکی خطا می‌دهد؛ روش: Install Preview، Revision Diff، Rollback، بررسی وابستگی (Interface Mapping).

**مثال سخت (طراحی):** ۴ شعبه + HQ؛ ADOM برای هر واحد؟ تصمیم: ADOM بر اساس نسخه FortiOS یا مستأجر؛ نه صرفاً جغرافیا؛ Policy Package پایه + Override محلی.

### ۵) GUI و CLI

**GUI FMG:** Device Manager → Add Device؛ Policy & Objects → Policy Package → Install. **GUI FGT:** Security Fabric/Central Management. **CLI FGT:**

``` text
config system central-management
    set type fortimanager
    set fmg "192.168.90.30"
end
```

(`Unverified`.)

### ۶) نکات امنیتی

- مدیریت مرکزی فقط از شبکه‌ی مدیریت؛ Admin جدا با MFA.
- Log شامل داده‌ی حساس است؛ رمزنگاری انتقال/ذخیره.
- بدون Audit تغییرات، Change ثبت نمی‌شود.

### ۷) جمع‌بندی

- FMG پیکربندی؛ FAZ Log؛ ADOM جداسازی؛ Policy Package نصب.
- مرکزی‌سازی ریسک جدید ایجاد می‌کند.
- جایگزین بدون لایسنس: Syslog، Git، SNMPv3، API.
- ادعای اجرا بدون دستگاه ممنوع.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) FMG و FAZ چه فرقی دارند؟ *(پاسخ: 26-0-ت1)*

**ت2.** (ساده) ADOM چیست؟ *(پاسخ: 26-0-ت2)*

**ت3.** (متوسط) چرا Install Preview لازم است؟ *(پاسخ: 26-0-ت3)*

**ت4.** (سخت) معماری جایگزین بدون لایسنس را برای ۱۰ فایروال بنویسید. *(پاسخ: 26-0-ت4)*

**Q1.** Quick quiz (English): What is an ADOM used for? *(پاسخ: 26-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FMG | FortiManager | مدیریت مرکزی |
| FAZ | FortiAnalyzer | تحلیل Log |
| ADOM | Administrative Domain | دامنه‌ی مدیریتی |
| RBAC | Role-Based Access Control | دسترسی نقش‌محور |

- *Preview before installing a policy package.* ← قبل از نصب Policy Package پیش‌نمایش بگیرید.

### ۱۰) منابع

- Fortinet Docs: [Device Manager](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/478145/device-manager)، [Add FortiAnalyzer](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/654379/add-fortianalyzer)، [Installing policy packages](https://docs.fortinet.com/document/fortimanager/7.0.7/administration-guide/153046/installing-policy-packages-and-device-settings)، [config log syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting).

## درس 26-1 — FMG و FAZ: نقش‌ها، معماری، ADOM، لایسنس و تصمیم «ابزار یا جایگزین» با تحلیل هزینه و ریسک

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۰، ۲۲-۰، ۲۷-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 / FortiManager-FortiAnalyzer 7.0 (Needs-License؛ بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. نقش FortiManager (پیکربندی) و FortiAnalyzer (Log/Report) را از نظر معماری و جریان داده تفکیک کند.
2. ADOM، Policy Package، Device Manager، Install و Revision را توضیح دهد.
3. محدودیت‌های مستند (تداخل Log Forwarding با FAZ features، یک FAZ برای هر ADOM) را بگوید.
4. برای سازمان‌های با اندازه‌ی مختلف تصمیم «FMG/FAZ یا جایگزین» را با معیار کمی بگیرد.
5. ریسک مرکزی‌سازی (SPOF، هدف حمله) و کنترل آن را بنویسد.
6. سند تصمیم معماری (ADR) تولید کند.

### ۲) مفهوم پایه: چیست و چرا؟

وقتی تعداد فایروال‌ها از چند دستگاه بیشتر می‌شود، مدیریت دستی خطا، ناهمگونی و بی‌Audit می‌سازد. دو محصول مکمل وجود دارد: **FortiManager (FMG)** پیکربندی/Policy را مرکزی نگه می‌دارد و **FortiAnalyzer (FAZ)** Logها را جمع، نگه‌داری و تحلیل می‌کند. ولی این‌ها لایسنس و منابع می‌خواهند؛ و مرکزی‌سازی خود یک هدف حمله و نقطه‌ی شکست است. تصمیم «ابزار یا جایگزین» باید کمی و ریسک‌محور باشد.

### ۳) توضیح عمیق فنی

#### ۱) جریان داده و نقش‌ها

``` text
FortiGate x N  --(FGFM: config/policy install)-->  FortiManager (FMG)
FortiGate x N  --(logs: OFTP/syslog)------------>  FortiAnalyzer (FAZ)
FMG <--> FAZ   (FMG can manage FAZ; ADOM-aligned)
Admins -> FMG (RBAC, ADOM scoped) ; Analysts -> FAZ (reports, event handlers)
```

#### ۲) مفاهیم FMG (طبق مستند 7.0)

- **Device Manager:** ثبت دستگاه/گروه، وضعیت Sync، تنظیمات مختص دستگاه.
- **ADOM:** دامنه‌ی مدیریتی؛ جداسازی دستگاه‌ها/مدیران/Policy (چندمستأجر یا نسخه‌ی FortiOS).
- **Policy Package:** Policy/Object قابل‌نصب روی یک یا چند دستگاه؛ Install Wizard: انتخاب Package، هدف و زمان‌بندی اختیاری؛ **Install Preview** تغییرات را قبل از اعمال نشان می‌دهد.
- **Revision History:** نسخه‌ی تنظیمات؛ Revert.
- **Template/Provisioning:** Interface/Routing/SD-WAN Template.

#### ۳) محدودیت‌ها (از مستند)

- با ADOM فعال، **هر ADOM یک FAZ** را می‌پذیرد و نام ADOM باید در دو سو یکی باشد.
- هنگام فعال بودن ویژگی‌های FAZ روی FMG، **Log Forwarding/Fetching/Aggregation پشتیبانی نمی‌شود**؛ افزودن FAZ، ویژگی‌های FAZ را خودکار فعال می‌کند و قابل‌غیرفعال‌شدن نیست.
- ظرفیت دستگاه/لایسنس VM باید با مستند و قرارداد بررسی شود (`Unverified`).

#### ۴) تصمیم کمی

``` text
Operational cost of manual mgmt ~= N firewalls x changes per month x minutes per change x error rate x incident cost
Tool cost = license + hosting + admin time
```

معیارها: تعداد دستگاه، فراوانی تغییر، تنوع Policy، الزام انطباق/Audit، مهارت تیم، بودجه.

| وضعیت | پیشنهاد |
|---|---|
| ≤ ۳ فایروال، تغییر کم | Backup + Git + Syslog |
| ۴ تا ۱۰، Policy مشابه | Ansible/API + Git؛ FMG اختیاری |
| > ۱۰ یا چندمستأجر | FMG |
| الزام Log/گزارش انطباق | FAZ یا SIEM |

#### ۵) ریسک مرکزی‌سازی

FMG/FAZ هدف ارزشمند (دسترسی به همه‌ی فایروال‌ها) و SPOF مدیریتی‌اند. کنترل: شبکه‌ی مدیریت جدا، HA/Backup، MFA، RBAC، Patch، Audit تغییرات، و برنامه‌ی «مدیریت بدون FMG» (Break-glass).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| FMG لازم است؟ | بر اساس تعداد دستگاه/تغییر/چندمستأجر/Audit |
| ADOM | مشتری/نسخه؛ نه صرفاً جغرافیا |
| FAZ یا Syslog | الزام گزارش و ظرفیت Log |
| Break-glass | دسترسی مستقیم اضطراری |
| HA | برای FMG/FAZ تولید |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** سازمان با ۳ فایروال: نیاز اصلی Backup، Log و ثبت تغییر؛ تصمیم: rsyslog + Git + Backup روزانه؛ FMG توجیه ندارد. ثبت ADR با دلیل.

**متوسط (تحلیل):** ۱۲ فایروال با ۲۰ تغییر Policy در ماه؛ خطای دستی ۳٪. تحلیل: ۲۴۰ تغییر/سال × ۳٪ ≈ ۷ خطا/سال؛ هر خطا ۲ ساعت قطع/رفع. FMG با Install Preview و Revert خطا را کم می‌کند؛ هزینه‌ی لایسنس را با هزینه‌ی ساعت‌های رفع مقایسه کنید. تصمیم: FMG یا Ansible+Git با Review.

**سخت (معماری):** چهار مشتری مجزا با ۳۰ فایروال؛ الزام جداسازی مدیریتی و گزارش جدا. تحلیل: ADOM به ازای هر مشتری؛ هر ADOM یک FAZ (طبق مستند)؛ RBAC سطح ADOM؛ Policy Package پایه + Override؛ ریسک: FMG نقطه‌ی مرکزی؛ HA، Backup، شبکه‌ی OOB، MFA؛ Break-glass روی هر فایروال. معیار موفقیت: آزمون Revert و Install Preview در Lab.

### ۶) پیاده‌سازی از مسیر GUI

1. FMG: Device Manager → Add Device/Group.
2. FMG: Policy & Objects → Policy Package → Install Wizard (Preview).
3. FMG: System Settings → Administrators/ADOMs.
4. FGT: Security Fabric → Fabric Connectors / System → Central Management.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system central-management
    set type fortimanager
    set fmg "192.168.90.30"
end
get system central-management
```

### ۸) Verification (اثبات صحت)

- ADR امضا‌شده.
- در Lab: افزودن یک FGT، Install Preview، Revert.
- برنامه‌ی Break-glass.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| دستگاه Out-of-sync | Device Manager وضعیت | Install/Retrieve Config |
| FAZ اضافه نمی‌شود | نام ADOM/نسخه | هم‌نام‌کردن ADOM؛ سازگاری نسخه |
| Log Forwarding کار نمی‌کند | تنظیمات FMG | تداخل با FAZ features (مستند) |

### ۱۰) نکات امنیتی

- شبکه‌ی OOB، MFA، RBAC، Audit.
- Backup رمزشده و HA.
- Patch فوری.

### ۱۱) جمع‌بندی مفهومی

- FMG = پیکربندی؛ FAZ = Log.
- ADOM، Policy Package، Install Preview، Revision.
- محدودیت‌های مستند را بشناسید.
- تصمیم بر پایه‌ی هزینه/ریسک.
- مرکزی‌سازی = ریسک جدید.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) تفاوت FMG و FAZ؟ *(پاسخ: 26-1-ت1)*

**ت2.** (ساده) ADOM چه کاری می‌کند؟ *(پاسخ: 26-1-ت2)*

**ت3.** (متوسط) چرا Install Preview لازم است؟ *(پاسخ: 26-1-ت3)*

**ت4.** (متوسط) دو محدودیت مستند FMG/FAZ؟ *(پاسخ: 26-1-ت4)*

**ت5.** (سخت) ۱۲ فایروال و ۲۰ تغییر در ماه با ۳٪ خطا؛ هزینه‌ی خطا چقدر است و تصمیم؟ *(پاسخ: 26-1-ت5)*

**ت6.** (سخت، طراحی) معماری برای ۴ مشتری ۳۰ فایروال. *(پاسخ: 26-1-ت6)*

**Q1.** Quick quiz (English): Why is a central manager both a benefit and a risk? *(پاسخ: 26-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FMG | FortiManager | مدیریت مرکزی |
| FAZ | FortiAnalyzer | تحلیل Log |
| ADOM | Administrative Domain | دامنه‌ی مدیریتی |
| Break-glass | Break-glass access | دسترسی اضطراری |

- *Preview changes before installing a policy package.* ← قبل از نصب Policy Package تغییرات را پیش‌نمایش کنید.

### ۱۴) کارت Lab

**کارت Lab:** سند تصمیم FMG/FAZ. **وضعیت:** طراحی (Needs-License). **Evidence:** `02-design/fmg-faz.md`.

### ۱۵) منابع

- [Device Manager](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/478145/device-manager)
- [Add FortiAnalyzer](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/654379/add-fortianalyzer)
- [Installing policy packages](https://docs.fortinet.com/document/fortimanager/7.0.7/administration-guide/153046/installing-policy-packages-and-device-settings)

<a id="l-26-2"></a>

## درس 26-2 — Syslog مرکزی (جایگزین FAZ): FortiGate → rsyslog با TCP/TLS، قالب، Parse، Retention و آزمون

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۰، ۲۶-۱، ۲۷-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 / FortiManager-FortiAnalyzer 7.0 (Needs-License؛ بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Syslog reliable را روی FortiGate و rsyslog پیکربندی و آزمون کند.
2. قالب (default/CSV/CEF/RFC5424)، Facility و `source-ip` را انتخاب کند.
3. Parse فیلدهای Log (key=value) و ساخت فایل‌های ساختارمند را انجام دهد.
4. Retention، چرخش، فضا و دسترسی را برنامه‌ریزی کند.
5. از دست رفتن Log (UDP، قطع TCP) را تشخیص و مدیریت کند.
6. Logهای حیاتی (Deny، Event، VPN) را مرتب و Alert بسازد.

### ۲) مفهوم پایه: چیست و چرا؟

FAZ همه‌چیز نیست؛ برای Audit، Correlation و نگهداری Log، یک Syslog مرکزی خوب (rsyslog/Elastic/Zabbix) کافی و ارزان است. ولی «Syslog خوب» یعنی: انتقال مطمئن، قالب پایدار، زمان همگام، نگهداری مشخص و دسترسی کنترل‌شده.

### ۳) توضیح عمیق فنی

#### ۱) پیکربندی FortiGate (طبق CLI Reference 7.0)

``` text
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set mode reliable
    set port 514
    set facility local7
    set source-ip 192.168.90.1
    set format rfc5424
end
```

- `mode`: udp / reliable / legacy-reliable؛ **reliable** برای Extended Logging لازم است (مستند Log Message Reference).
- `format`: default، csv، cef، rfc5424.
- `source-ip`: برای مسیر/ACL و یکتایی مبدأ.
- TLS (در صورت پشتیبانی نسخه): `enc-algorithm` و گواهی (`Unverified`).

#### ۲) rsyslog (سرور)

``` text
module(load="imtcp")
input(type="imtcp" port="514")
template(name="FGT" type="string" string="/var/log/fgt/%fromhost-ip%/%$YEAR%-%$MONTH%-%$DAY%.log")
if $fromhost-ip startswith '192.168.90.' then ?FGT
& stop
```

چرخش: `logrotate` روزانه، فشرده‌سازی، حذف پس از N روز.

#### ۳) Parse

Logهای FortiOS به‌صورت `key=value` هستند:

``` text
date=2026-11-26 time=19:20:01 devname="FGT-A" type="traffic" subtype="forward" srcip=10.1.4.10 dstip=203.0.113.80 dstport=443 action="deny" policyid=0 service="HTTPS"
```

با `grep`/`awk` یا Logstash/Fluent Bit به JSON تبدیل و فیلدها را ایندکس کنید (`srcip`, `dstip`, `action`, `policyid`).

#### ۴) اطمینان

UDP ممکن است Log از دست بدهد؛ TCP reliable؛ **صف محلی** در FortiGate هنگام قطع سرور محدود است؛ پس سرور Syslog باید HA/Monitor داشته باشد. پایش «آخرین Log دریافتی» برای هر دستگاه Alert بدهد.

#### ۵) ظرفیت

``` text
Daily volume ~= events/day x avg bytes/event    e.g. 8M x 450 B = 3.6 GB/day
Storage = daily volume x retention days x compression factor
```

مثال: ۳٫۶ GB × ۱۸۰ روز = ۶۴۸ GB؛ با فشرده‌سازی ۱۰:۱ ≈ ۶۵ GB.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| UDP یا TCP | TCP reliable (+TLS در صورت پشتیبانی) |
| قالب | RFC5424/CEF برای ابزار |
| Retention | محاسبه‌ی حجم×روز |
| HA | دو مقصد/سرور |
| زمان | NTP |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Log Event «admin login» از FGT در `/var/log/fgt/192.168.90.1/…log` دیده می‌شود؛ `tcpdump -i eth0 port 514` TCP.

**متوسط (تحلیل):** Log نمی‌رسد: بررسی به ترتیب: Route/Local-out به 192.168.90.20؛ Firewall سرور TCP 514؛ `mode`/`port`؛ `source-ip`؛ `diagnose log test`. شواهد: Sniffer روی Interface خروجی FGT و tcpdump سرور. نمونه علت: Policy Local-out/ACL.

**سخت (از دست رفتن Log):** پس از قطع ۱۰ دقیقه‌ای سرور، Logهای آن بازه موجود نیست. تحلیل: صف محلی محدود؛ UDP؛ حل: reliable + سرور HA یا دو Syslog؛ Alert «بدون Log ۲ دقیقه»؛ برای رویدادهای حیاتی ذخیره‌ی محلی روی دیسک FGT با Retention. طراحی: دو مقصد (Primary/Secondary) و آزمون قطع.

### ۶) پیاده‌سازی از مسیر GUI

1. Log & Report → Log Settings → Remote Logging and Archiving → Send Logs to Syslog.
2. Log & Report → Forward Traffic/Events برای بررسی.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set mode reliable
    set port 514
    set format rfc5424
end
diagnose log test
execute ping-options source 192.168.90.1
execute ping 192.168.90.20
```

### ۸) Verification (اثبات صحت)

- `tcpdump` روی سرور: TCP 514 از FGT.
- فایل Log روزانه با رویداد آزمایشی.
- Alert «بدون Log».
- آزمون قطع/وصل سرور و اندازه‌گیری Loss.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Log نمی‌رسد | Sniffer/tcpdump | Route/Firewall/mode/port |
| Log ناقص | شمارش | UDP/قطع |
| فیلدها Parse نمی‌شوند | فرمت | format/Parser |
| دیسک پر | df | Retention/Rotate |

### ۱۰) نکات امنیتی

- TLS/شبکه‌ی مدیریت.
- دسترسی خواندنی Log محدود.
- Log تغییرناپذیر برای حادثه.

### ۱۱) جمع‌بندی مفهومی

- reliable + قالب پایدار.
- Parse key=value.
- Retention محاسبه‌شده.
- Alert «بدون Log».
- HA برای Syslog.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا `mode reliable`؟ *(پاسخ: 26-2-ت1)*

**ت2.** (ساده) `source-ip` چه کمکی می‌کند؟ *(پاسخ: 26-2-ت2)*

**ت3.** (متوسط) حجم 8M رویداد در روز با 450 B و Retention 90 روز چقدر است؟ *(پاسخ: 26-2-ت3)*

**ت4.** (متوسط) Log نمی‌رسد؛ سه آزمون به ترتیب. *(پاسخ: 26-2-ت4)*

**ت5.** (سخت) قطع ۱۰ دقیقه‌ای سرور Logهای آن بازه را از بین برد؛ راه‌حل. *(پاسخ: 26-2-ت5)*

**ت6.** (سخت، طراحی) معماری Log برای ۱۰ فایروال با ۱۸۰ روز Retention. *(پاسخ: 26-2-ت6)*

**Q1.** Quick quiz (English): Why is UDP syslog unsuitable for critical firewall logs? *(پاسخ: 26-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| rsyslog | rsyslog | سرویس Syslog لینوکس |
| RFC5424 | Syslog protocol format | قالب استاندارد Syslog |
| CEF | Common Event Format | قالب رویداد مشترک |

- *Alert when a device stops sending logs.* ← وقتی دستگاه Log نمی‌فرستد هشدار بدهید.

### ۱۴) کارت Lab

**کارت Lab:** Syslog. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/syslog.md`.

### ۱۵) منابع

- [config log syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting)
- RFC 5424
- rsyslog documentation

<a id="l-26-3"></a>

## درس 26-3 — Backup خودکار و مدیریت Config با Git: Sanitize، Diff، Audit، Restore و Drift

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۰، ۲۷-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 / FortiManager-FortiAnalyzer 7.0 (Needs-License؛ بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Backup دوره‌ای و ایمن (SFTP/SCP) را طراحی و اجرا کند.
2. Sanitizer برای حذف Secret بنویسد و آزمون کند.
3. Git (commit، diff، tag، branch) را برای Config به‌کار ببرد.
4. Drift بین نسخه‌ی مرجع و دستگاه را کشف کند.
5. Restore را در Lab اثبات و RTO را ثبت کند.
6. Audit تغییرات (چه کسی/چه زمانی/چرا) را پیاده کند.

### ۲) مفهوم پایه: چیست و چرا؟

Config مرجع حقیقت دستگاه است. سه خطای رایج: (۱) Backup نداریم، (۲) Backup داریم ولی Restore نشده، (۳) Backup در Git با Secret ذخیره شده. روش درست: Backup خودکار → Sanitize → Git → Diff/Audit → آزمون Restore.

### ۳) توضیح عمیق فنی

#### ۱) جریان

``` text
FGT --(execute backup config sftp)--> backup server (restricted)
  -> sanitize (remove/tokenize secrets) -> git commit (author=system, message=ticket)
  -> diff vs previous -> alert on unexpected change
  -> periodic restore test in lab (same firmware)
```

#### ۲) Backup از FortiGate

``` text
execute backup config sftp fgt-A-daily.conf 192.168.90.10 backup-user <PASSWORD>
```

(روش دقیق و رمز: کاربر محدود، کلید SSH در صورت پشتیبانی؛ `Unverified`.) Backup شامل Hash/رمزهای رمزشده است؛ **حساس** حساب کنید.

#### ۳) Sanitize

الگوها: `set password ENC ...`، `set psksecret ENC ...`، `set secret ...`، گواهی/کلید خصوصی. استراتژی: جایگزینی با `<REDACTED>` در نسخه‌ی Git، و نگهداری نسخه‌ی کامل رمزشده جداگانه (Vault).

``` text
sed -E 's/(set (password|psksecret|secret|passwd) ).*/\1<REDACTED>/' fgt.conf > fgt.sanitized.conf
```

#### ۴) Git

- Branch/Tag: `daily/YYYY-MM-DD`، Tag قبل از Change.
- Diff روزانه: تغییرات ناشناس ⇒ Alert.
- Pre-commit hook: اسکن Secret (جلوگیری از Commit).

#### ۵) Drift

Drift = تفاوت بین Config مرجع (Git) و دستگاه. Diff خودکار و اعلان؛ دلیل: تغییر مستقیم روی دستگاه بدون Ticket.

#### ۶) Restore و RTO

آزمون: Lab هم‌نسخه، Restore، مقایسه (`show full-configuration`)، اندازه‌گیری RTO. نسخه‌ی Firmware باید یکسان/سازگار باشد.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| مقصد Backup | سرور محدود+رمزنگاری |
| Secret | Sanitize + Vault |
| Retention | روزانه ۳۰، هفتگی ۱۲، ماهانه ۱۲ |
| Restore test | فصلی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Backup شبانه با cron؛ Sanitize؛ `git commit`؛ `git log --stat` تغییرات.

**متوسط (تحلیل):** Diff نشان می‌دهد Policy جدید ساعت ۲ بامداد اضافه شده بدون Ticket. بررسی: Log Event Admin؛ کاربر؛ مستند؛ در صورت نامجاز: Revert و تحقیق. درس: Audit و Alert Drift.

**سخت (حادثه‌ی Secret):** Backup خام با PSK به مخزن Commit شد. اقدام: (۱) حذف از تاریخچه (git filter-repo/BFG) و Force-push با تأیید، (۲) چرخش همه‌ی رمزها/PSKها/توکن‌ها، (۳) بازبینی دسترسی به مخزن، (۴) افزودن Pre-commit و اسکن Secret، (۵) PIR. توجه: حذف از تاریخچه کافی نیست؛ فرض کنید افشا شده است ⇒ چرخش اعتبارنامه‌ها اجباری.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute backup config sftp fgt-A-daily.conf 192.168.90.10 backup-user <PASSWORD>
# on backup server (shell)
sed -E 's/(set (password|psksecret|secret|passwd) ).*/\1<REDACTED>/' fgt-A-daily.conf > fgt-A.sanitized.conf
git add -A && git commit -m "fgt-A daily backup"
git diff HEAD~1 -- fgt-A.sanitized.conf
```

### ۸) Verification (اثبات صحت)

- Diff روزانه تولید و بررسی.
- Restore در Lab و RTO ثبت.
- Pre-commit Secret scan آزمایشی (باید Block کند).

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Backup خالی | لاگ/مجوز | دسترسی/مسیر |
| Diff نویزی | Diff | Sanitize/ترتیب |
| Restore ناسازگار | نسخه | Firmware برابر |

### ۱۰) نکات امنیتی

- Secret هرگز در Git عمومی.
- Backup رمزشده و دسترسی محدود.
- چرخش رمز پس از افشا.

### ۱۱) جمع‌بندی مفهومی

- Backup خودکار + Sanitize + Git + Diff.
- Drift و Audit.
- Restore اثبات‌شده.
- افشای Secret = چرخش رمز.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Backup بدون Restore کافی نیست؟ *(پاسخ: 26-3-ت1)*

**ت2.** (ساده) Drift یعنی چه؟ *(پاسخ: 26-3-ت2)*

**ت3.** (متوسط) Sanitizer باید چه الگوهایی را پاک کند؟ *(پاسخ: 26-3-ت3)*

**ت4.** (متوسط) چرا Tag قبل از Change؟ *(پاسخ: 26-3-ت4)*

**ت5.** (سخت) Secret در Git Commit شد؛ مراحل اقدام. *(پاسخ: 26-3-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Backup/Restore با RTO هدف ۳۰ دقیقه. *(پاسخ: 26-3-ت6)*

**Q1.** Quick quiz (English): Why is removing a secret from Git history not enough after it was committed? *(پاسخ: 26-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Drift | Configuration drift | انحراف پیکربندی |
| Sanitize | Sanitize config | پاک‌سازی Secret |
| RTO | Recovery Time Objective | زمان هدف بازیابی |

- *Never commit secrets to a repository.* ← هرگز Secret را در مخزن Commit نکنید.

### ۱۴) کارت Lab

**کارت Lab:** Backup/Git. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/backup.md`.

### ۱۵) منابع

- Git documentation
- NIST SP 800-53 CM-2/CM-3
- Fortinet Docs: Backup and restore (7.0)

<a id="l-26-4"></a>

## درس 26-4 — طراحی معماری ۹ (مدیریت مرکزی و عملیات): RBAC، Change، Audit و آزمون با Rubric

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۱ تا ۲۶-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 / FortiManager-FortiAnalyzer 7.0 (Needs-License؛ بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری مدیریت مرکزی (FMG یا جایگزین) را از نیازمندی تا طرح اجرایی تولید کند.
2. RBAC (Super، Operator، Auditor، Read-only) و Separation of Duties را بنویسد.
3. فرایند Change/Approval/Audit را با ابزار انتخابی هماهنگ کند.
4. ریسک‌ها، Break-glass و DR را طراحی کند.
5. طرح را ارائه و با Rubric ارزیابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

آزمون طراحی معماری ۹: «چه ابزار، با چه نقش‌ها، چه فرایند و چه شواهد». کلید پاسخ پس از تلاش.

### ۳) توضیح عمیق فنی

#### صورت مسئله

شرکت: HQ + ۱۲ شعبه، ۱۵ FortiGate، دو تیم (شبکه، امنیت)، Audit فصلی، بودجه محدود. نیازمندی‌ها:
- R1: Policy یکسان و Audit تغییر.
- R2: Log ۱۸۰ روزه و Alert.
- R3: Backup/Restore و DR.
- R4: جداسازی نقش‌ها.
- R5: ریسک مرکزی‌سازی مدیریت.

#### خروجی‌ها

ADR ابزار، نمودار، جدول RBAC، فرایند Change، برنامه‌ی Audit، Break-glass، آزمون Restore.

#### کلید پاسخ (خلاصه‌ی مورد انتظار)

- ابزار: FMG برای Policy مرکزی (۱۵ دستگاه) + Syslog/SIEM برای Log یا FAZ؛ جایگزین: Ansible+Git+rsyslog؛ تصمیم با هزینه/ریسک.
- RBAC: Super (۲ نفر، MFA)، Operator (Policy در ADOM)، Auditor (Read-only)، Network (Interface/Routing).
- Change: Ticket→Review→Install Preview→Window→Post-check→Close.
- Audit: Revision diff ماهانه، Drift، Admin log.
- Break-glass: حساب محلی با رمز Vault و MFA فیزیکی.
- DR: HA/Backup رمزشده، آزمون فصلی.

#### Rubric (۱۰۰)

ADR/تصمیم ۲۰؛ RBAC ۲۰؛ Change/Audit ۲۰؛ ریسک/DR ۲۰؛ شواهد ۱۰؛ صداقت (لایسنس/Unverified) ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** جدول RBAC چهارنقشه.

**متوسط:** فرایند Change با Preview.

**سخت:** ریسک مرکزی‌سازی و Break-glass.

### ۸) Verification (اثبات صحت)

- سند A9.
- آزمون Revert/Restore در Lab (در صورت لایسنس).

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| دسترسی بیش‌ازحد | RBAC | Least privilege |
| Audit ناقص | Revision | Diff/Log |

### ۱۰) نکات امنیتی

- MFA Admin؛ Break-glass در Vault؛ OOB.

### ۱۱) جمع‌بندی مفهومی

- معماری = ابزار + نقش + فرایند + شواهد.
- Separation of Duties.
- ریسک مرکزی‌سازی را بپذیرید و کنترل کنید.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Separation of Duties چیست؟ *(پاسخ: 26-4-ت1)*

**ت2.** (ساده) Break-glass برای چیست؟ *(پاسخ: 26-4-ت2)*

**ت3.** (متوسط) چرا Auditor باید Read-only باشد؟ *(پاسخ: 26-4-ت3)*

**ت4.** (متوسط) مراحل Change با FMG؟ *(پاسخ: 26-4-ت4)*

**ت5.** (سخت) ریسک‌های مرکزی‌سازی را با کنترل‌ها بنویسید. *(پاسخ: 26-4-ت5)*

**ت6.** (سخت، طراحی) طرح کامل برای ۱۵ فایروال. *(پاسخ: 26-4-ت6)*

**Q1.** Quick quiz (English): Why is a break-glass account required in a centrally managed environment? *(پاسخ: 26-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| A9 | Architecture 9 | معماری ۹ |
| SoD | Separation of Duties | تفکیک وظایف |
| ADR | Architecture Decision Record | ثبت تصمیم معماری |

- *Design central management with least privilege and audit trails.* ← مدیریت مرکزی را با حداقل دسترسی و ردپای Audit طراحی کنید.

### ۱۴) کارت Lab

**کارت Lab:** A9. **وضعیت:** طراحی. **Evidence:** `02-design/a9.md`.

### ۱۵) منابع

- NIST SP 800-53 (AC، AU، CM)
- درس‌های ۲۶-۱ تا ۲۶-۳

## پاسخ‌های فصل 26

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 26-1

**26-1-ت1** — FMG پیکربندی و Policy را مرکزی مدیریت و روی دستگاه‌ها Install می‌کند؛ FAZ Log را جمع و تحلیل و گزارش می‌دهد.

**26-1-ت2** — دستگاه‌ها، مدیران و Policyها را در دامنه‌های مدیریتی جدا نگه می‌دارد (مشتری/نسخه).

**26-1-ت3** — تا دیفِ تغییرات قبل از اعمال دیده شود و خطای گسترده روی چند دستگاه رخ ندهد.

**26-1-ت4** — هر ADOM یک FAZ؛ و هنگام فعال بودن ویژگی‌های FAZ روی FMG، Log Forwarding/Fetching/Aggregation پشتیبانی نمی‌شود.

**26-1-ت5** — ۲۴۰ تغییر × ۳٪ ≈ ۷ خطا/سال؛ هر خطا مثلاً ۲ ساعت ⇒ ۱۴ ساعت قطع/رفع + اثر کسب‌وکار؛ با لایسنس/میزبانی FMG مقایسه کنید؛ اگر اثر کسب‌وکار بالا است FMG یا Ansible+Review توجیه دارد.

**26-1-ت6** — ADOM برای هر مشتری؛ FAZ برای هر ADOM؛ RBAC؛ Policy Package پایه+Override؛ HA/Backup/OOB/MFA؛ Break-glass؛ آزمون Revert.

**26-1-Q1** — It simplifies consistent management but becomes a high-value target and single point of failure.


### پاسخ‌های بازنویسی عمیق درس 26-2

**26-2-ت1** — TCP؛ از دست رفتن Log کمتر و برای Extended Logging لازم است.

**26-2-ت2** — مبدأ یکتا و قابل‌کنترل برای ACL/مسیر و شناسایی دستگاه در سرور.

**26-2-ت3** — ≈ 3.6 GB/روز؛ ×90 ≈ 324 GB؛ با فشرده‌سازی 10:1 ≈ 32 GB.

**26-2-ت4** — `execute ping` با source-ip، Sniffer روی Interface خروجی FGT، tcpdump روی سرور و بررسی Firewall سرور.

**26-2-ت5** — reliable، دو مقصد/سرور HA، Alert بدون Log، ذخیره‌ی محلی Retention برای رویدادهای حیاتی، آزمون قطع.

**26-2-ت6** — TCP reliable به دو سرور، rsyslog+Parser، ایندکس، حجم و فضا محاسبه، چرخش، Alert Loss، دسترسی RBAC.

**26-2-Q1** — Because UDP does not guarantee delivery, so events can be lost during network or server problems.


### پاسخ‌های بازنویسی عمیق درس 26-3

**26-3-ت1** — چون نمی‌دانیم فایل کامل/سازگار است و RTO واقعی چقدر است.

**26-3-ت2** — تفاوت پیکربندی واقعی دستگاه با نسخه‌ی مرجع در Git.

**26-3-ت3** — `password`، `psksecret`، `secret`، `passwd`، گواهی/کلید خصوصی و توکن API.

**26-3-ت4** — نقطه‌ی بازگشت مشخص برای Rollback و مقایسه.

**26-3-ت5** — حذف از تاریخچه، چرخش همه‌ی اعتبارنامه‌ها، بازبینی دسترسی، Pre-commit scan، PIR؛ فرض افشا.

**26-3-ت6** — Backup روزانه، Lab هم‌نسخه، Runbook Restore، آزمون فصلی، اندازه‌گیری RTO و اصلاح.

**26-3-Q1** — Because it may already have been copied or exposed, so credentials must be rotated.


### پاسخ‌های بازنویسی عمیق درس 26-4

**26-4-ت1** — تفکیک نقش‌ها تا یک نفر هم درخواست‌دهنده و هم تأییدکننده/Auditor نباشد.

**26-4-ت2** — دسترسی اضطراری وقتی ابزار مرکزی در دسترس نیست؛ با کنترل و Audit شدید.

**26-4-ت3** — تا بتواند Audit کند بدون امکان تغییر و محو شواهد.

**26-4-ت4** — Ticket، Review، Install Preview، Window، Install، Post-check، Close.

**26-4-ت5** — هدف حمله/SPOF: OOB، MFA، RBAC، HA/Backup، Patch، Break-glass؛ خطای گسترده: Preview/Canary/Revert.

**26-4-ت6** — ADR، RBAC جدول، Change/Audit، Log (FAZ/Syslog)، Backup/DR، آزمون‌ها و ریسک.

**26-4-Q1** — So devices can still be managed if the central manager or its authentication is unavailable.

### پاسخ‌های درس افزوده‌ی 26-0 (فصل 26)

**26-0-ت1** — FMG پیکربندی/Policy مرکزی؛ FAZ جمع‌آوری و تحلیل Log.

**26-0-ت2** — دامنه‌ی مدیریتی مجزا برای دستگاه‌ها/مدیران با Policy Package و Object خودش.

**26-0-ت3** — تا تأثیر نصب پیش از اعمال دیده شود و خطای گسترده رخ ندهد.

**26-0-ت4** — Syslog مرکزی (rsyslog)، Backup روزانه به Git/SFTP بدون Secret، SNMPv3 + Zabbix، Ansible/API خواندنی، ثبت Change با Diff.

**26-0-Q1** — To separate devices, administrators and policy sets into administrative domains (for example per tenant or version).

# فصل 27 — Logging، Monitoring، Performance، API، Hardening و Backup (G10)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۴، ۲۶.
**اهداف:** Logging؛ SNMP و Zabbix؛ Performance Baseline؛ REST API؛ Hardening؛ Backup/Restore. Gate G10: مانیتورینگ+Log+Hardening+Backup با شاهد.
**اشتباهات رایج:** SNMP v2c باز؛ API Token بی‌محدودیت؛ Admin روی WAN؛ Backup بدون تست Restore.

**درس‌های فصل:**
- [درس 27-1 — Logging و Log Settings](#l-27-1)
- [درس 27-2 — SNMP و مانیتورینگ Zabbix](#l-27-2)
- [درس 27-3 — REST API و Automation](#l-27-3)
- [درس 27-4 — Hardening و Backup/Restore](#l-27-4)
- [درس 27-5 — Gate G10 و آزمون](#l-27-5)

---

<a id="l-27-1"></a>

## درس 27-0 — Logging، Monitoring و Baseline: چه چیزی را، چرا و چگونه ثبت و پایش کنیم

**فصل ۲۷ · درس افزوده (پیش‌درس ۲۷-۱) · پیش‌نیاز: ۱۴-۷، ۲۶-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0):** انواع Log و گزینه‌های Syslog از مستند رسمی ([Sample logs by log type](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/986892/sample-logs-by-log-type)، [syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting)) تأیید شد. SNMPv3 و REST API روی FortiGate در این دور تأیید نشد و `Unverified` است.

### ۱) هدف آموزشی

1. انواع Log (Traffic، Event، UTM) و **سطح ثبت** را بشناسد و بر اساس هدف انتخاب کند.
2. **Baseline** عملکرد (CPU، Memory، Session، Throughput) بسازد و انحراف را تشخیص دهد.
3. معیارهای مانیتورینگ و **آستانه‌ی هشدار** معنادار تعیین کند (نه فقط «روشن/خاموش»).
4. Log را با NTP همگام و در مقصد مرکزی نگه دارد (Retention).
5. از Log به **تحلیل حادثه** برسد.

### ۲) مفهوم پایه

Log بدون هدف = انبار داده؛ Monitoring بدون Baseline = «همه چیز نرمال است» یا «همه چیز بد است» بدون مرجع. سه سؤال: **چه چیزی ثبت شود؟ برای چه تصمیمی؟ چه کسی می‌بیند و چه زمانی؟**

### ۳) توضیح عمیق فنی

#### ۳-۱) انواع Log

| نوع | محتوا | کاربرد |
|---|---|---|
| Traffic (Forward/Local) | Sessionها: Source/Dest/Service/Action/Policy | تحلیل جریان، حادثه |
| Event | Login مدیر، تغییر Config، VPN، HA، System | Audit، تغییر |
| UTM/Security | AV، Web، DNS، App، IPS، DLP | تهدید |

طبق مستند: Log امنیتی نیاز دارد که Policy دارای UTM باشد و `logtraffic` روی `utm` یا `all`. **Policyهای Deny** را هم Log کنید؛ Policy 0 (Implicit deny) با تنظیم جدا قابل Log است (`Unverified`).

#### ۳-۲) سطح Log و هزینه

`logtraffic all` همه‌ی Session‌ها (حجم زیاد)؛ `utm` فقط Sessionهای دارای رویداد UTM. تصمیم: Allow مهم و همه‌ی Deny؛ سرویس‌های پرحجم بی‌اهمیت: خاموش. **حجم Log = Session × اندازه‌ی رکورد.**

#### ۳-۳) Baseline

قبل از مشکل، در یک هفته‌ی عادی اندازه بگیرید و نگه دارید: CPU/Memory میانگین و پیک، تعداد Session، Throughput، Interface Errors، تعداد VPN، حجم Log. «CPU 70٪» بدون Baseline معنی ندارد: برای یک دستگاه عادی و برای دیگری اوج حمله.

#### ۳-۴) آستانه‌ها (نمونه؛ برای محیط خود تنظیم کنید)

| معیار | هشدار | بحرانی | دلیل |
|---|---|---|---|
| CPU | > 70٪ ۵ دقیقه | > 90٪ | ظرفیت |
| Memory | > 80٪ | > 90٪ (Conserve mode) | ظرفیت |
| Session | > 70٪ حد | > 90٪ | Exhaustion |
| Interface Error | رشد مداوم | — | کابل/Duplex |
| HA | عضو Out-of-sync | Failover | دسترس‌پذیری |
| VPN | Tunnel Down | — | وصل نبودن |
| Disk Log | > 80٪ | > 90٪ | از دست رفتن Log |

#### ۳-۵) ابزارها

- **Syslog:** ارسال Log به سرور مرکزی (UDP/TCP/TLS؛ `format rfc5424`/`cef`)؛ حالت reliable ضروری برای Extended Logging.
- **SNMP** (ترجیحاً v3): پایش Interface/CPU/Memory با Zabbix.
- **API/CLI:** جمع‌آوری وضعیت (`get system performance status`، `diagnose sys top`).
- **NTP:** بدون زمان یکسان Log چند دستگاه قابل Correlation نیست.

#### ۳-۶) از Log به حادثه

مثال تحلیل: «Deny زیاد از 198.51.100.7 به پورت‌های متعدد» ← Port Scan. Correlation: همان IP در Log DNS/Web؟ آیا موفق شد؟ اقدام: Block، بازبینی. این پایه‌ی فصل ۲۹ است.

### ۴) مثال حل‌شده

``` text
config firewall policy
    edit 10
        set logtraffic all
    next
end
config log syslogd setting
    set status enable
    set server "192.168.90.20"
    set mode reliable
    set format rfc5424
end
get system performance status
diagnose sys top 2 20
```

(`Unverified`.) **برنامه‌ی Baseline:** هر ۵ دقیقه ۷ روز؛ جدول میانگین/پیک؛ آستانه‌ها = Baseline × ضریب.

**مثال متوسط:** CPU ناگهان 85٪: تقسیم مسیر: Session جدید (حمله؟)، Profile/UTM، Local-in (Scan مدیریتی)، Log. شواهد: `sys top`، `session statistics`، Log Deny.

**مثال سخت:** Log دیسک پر و Log حادثه از دست رفت: راه‌حل: Syslog مرکزی reliable + Retention + هشدار Disk.

### ۵) GUI و CLI

**GUI:** Log & Report → Log Settings؛ Forward Traffic؛ Events؛ Dashboard → Performance؛ FortiView. **CLI:** `get log ...`، `get system performance status`.

### ۶) نکات امنیتی

- Log حاوی IP/User است؛ دسترسی محدود و رمزنگاری انتقال.
- از Log پاک نکردن برای مخفی‌کردن؛ Immutable storage.
- Timestamp دقیق (NTP) برای ارزش قانونی.

### ۷) جمع‌بندی

- ثبت هدفمند؛ Baseline قبل از مشکل؛ آستانه‌ی مبتنی بر Baseline.
- Log مرکزی reliable، NTP هماهنگ.
- Log→Correlation→حادثه.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) سه نوع Log را بگویید. *(پاسخ: 27-0-ت1)*

**ت2.** (متوسط) چرا Baseline لازم است؟ *(پاسخ: 27-0-ت2)*

**ت3.** (سخت) آستانه‌های هشدار برای ۶ معیار با دلیل بنویسید. *(پاسخ: 27-0-ت3)*

**ت4.** (سخت، طراحی) برنامه‌ی Retention برای ۱۸۰ روز Log با حجم ۲ GB/روز. *(پاسخ: 27-0-ت4)*

**Q1.** Quick quiz (English): Why must firewall clocks be synchronized with NTP? *(پاسخ: 27-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Baseline | Performance baseline | مرجع وضعیت عادی |
| SNMP | Simple Network Management Protocol | پروتکل پایش |
| Retention | Log retention | مدت نگهداری |
| Correlation | Log correlation | همبستگی Log |

- *Establish a baseline before setting alert thresholds.* ← قبل از آستانه‌ها Baseline بسازید.

### ۱۰) منابع

- Fortinet Docs: [Sample logs by log type](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/986892/sample-logs-by-log-type)، [config log syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting)؛ NIST SP 800-92 — Guide to Log Management.

## درس 27-1 — Logging در FortiGate: انواع Log، سطح ثبت، Policy Logging، ذخیره‌ی محلی و طراحی حجم/Retention

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۰، ۲۶-۲، ۱۴-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Log انواع Traffic، Event و UTM و فیلدهای مهم هر کدام را بشناسد.
2. `logtraffic` (all/utm/disable) و Policy Logging را با هدف انتخاب کند.
3. Log Settings (Disk/Memory/FortiAnalyzer/Syslog) و رفتار هنگام پر شدن را بفهمد.
4. حجم و Retention را محاسبه و طراحی کند.
5. Log را برای عیب‌یابی و Detection فیلتر و تفسیر کند.
6. Log Deny/Implicit deny و Local traffic را مدیریت کند.

### ۲) مفهوم پایه: چیست و چرا؟

Log سه کاربرد دارد: **عیب‌یابی** (چرا بسته Drop شد؟)، **امنیت** (چه حمله‌ای دیدیم؟)، **انطباق/Audit** (چه کسی چه کرد؟). «همه چیز را Log کن» هم حجم عظیم و هم نویز می‌سازد؛ «هیچ چیز» هم کورشدن. باید بر اساس هدف تصمیم گرفت.

### ۳) توضیح عمیق فنی

#### ۱) انواع Log (طبق مستند 7.0)

| نوع | محتوا | کاربرد |
|---|---|---|
| Traffic (forward/local) | Session: src/dst/port/action/policy | جریان، حادثه |
| Event | Admin، System، VPN، HA، Router، User | Audit/تغییر |
| Security (UTM) | virus، webfilter، dns، app-ctrl، ips، DLP | تهدید |

طبق مستند نمونه‌ی Log: Log امنیتی نیاز دارد Policy دارای UTM باشد و `logtraffic` روی `utm` یا `all`.

#### ۲) سطوح `logtraffic`

- `all`: همه‌ی Sessionها (Start/End) — حجم زیاد.
- `utm`: فقط Sessionهای دارای رویداد UTM.
- `disable`: هیچ.

تصمیم: Policyهای Allow مهم (سرور حیاتی، مدیریت) `all`؛ Allow عمومی کاربران `utm`؛ Deny: Log فعال؛ Implicit deny (Policy 0) با تنظیم جدا Log (`Unverified`).

#### ۳) فیلدهای کلیدی

``` text
date time devname type subtype level srcip srcintf dstip dstintf srcport dstport proto service action policyid sentbyte rcvdbyte duration
```

`action`: accept/deny/close/timeout؛ `policyid`: همبستگی با Policy؛ `sentbyte/rcvdbyte`: Exfiltration.

#### ۴) مقصدها و رفتار پر شدن

Memory (کم، غیرپایدار)، Disk (محدود؛ Overwrite قدیمی‌ها)، FortiAnalyzer/Syslog (مرکزی). **ذخیره‌ی محلی را مرجع نگیرید.** رفتار دیسک پر: Overwrite/توقف؛ هشدار.

#### ۵) حجم و Retention

``` text
Daily volume = events/day x avg record size
Retention storage = Daily volume x days x 1.2 (headroom)
```

مثال: ۵ میلیون Session × ۰٫۵ KB = ۲٫۵ GB/روز؛ ۹۰ روز = ۲۷۰ GB (+۲۰٪ = ۳۲۴ GB).

#### ۶) خواندن Log برای عیب‌یابی

``` text
execute log filter category 0          (traffic)
execute log filter field srcip 10.1.4.10
execute log filter field dstport 443
execute log display
```

(نام زیردستورها `Unverified`؛ GUI: Log & Report → Forward Traffic با فیلتر.)

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| logtraffic | بر اساس هدف: حیاتی all، عمومی utm، Deny فعال |
| مقصد | Syslog مرکزی؛ Local کوتاه |
| Retention | محاسبه و انطباق |
| NTP | اجباری |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** کاربر به `10.20.30.7:1433` نمی‌رسد؛ Log Forward Traffic: `action=deny policyid=0` ⇒ Implicit deny؛ علت: Policy نیست. رفع: Policy؛ تأیید با Log `accept policyid=31`.

**متوسط (محاسبه):** ۱۲ میلیون Session/روز، ۴۵۰ بایت/Session؛ Retention ۱۸۰ روز ⇒ ۵٫۴ GB/روز، ≈ ۹۷۲ GB؛ با فشرده‌سازی ۸:۱ ≈ ۱۲۱ GB؛ تصمیم: Syslog مرکزی و Local فقط ۷ روز.

**سخت (تحلیل):** Log پر از نویز Allow وب است و حادثه‌ی نفوذ کشف نشد. تحلیل: `logtraffic all` روی Policy کاربران؛ تصمیم: `utm` برای Allow عمومی و `all` برای مدیریت/سرور؛ Deny همیشه؛ Correlation: `policyid`/`srcip`/Bytes؛ Alert روی Deny پورت‌های مدیریتی و حجم خروجی غیرعادی. نتیجه: Log کم‌حجم‌تر و معنادارتر.

### ۶) پیاده‌سازی از مسیر GUI

1. Log & Report → Log Settings: Local logging، Disk، Remote.
2. Policy & Objects → Firewall Policy → Logging Options (Log Allowed Traffic: All/Security Events).
3. Log & Report → Forward Traffic / Events / AntiVirus / Web Filter.
4. Dashboard → Log widgets.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall policy
    edit 31
        set logtraffic all
    next
end
config log setting
    set local-in-allow enable
    set local-in-deny-broadcast enable
end
execute log filter category 0
execute log filter field policyid 31
execute log display
```

### ۸) Verification (اثبات صحت)

- Log رویداد آزمایشی Allow/Deny.
- حجم Log هفتگی اندازه‌گیری.
- Retention محاسبه‌شده با مقدار واقعی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Log امنیتی نیست | Policy: utm-status/logtraffic | فعال‌سازی Profile و logtraffic |
| Disk پر | Dashboard | Retention/Syslog |
| Log زیاد | حجم | logtraffic all روی Allow عمومی |
| زمان اشتباه | Log timestamp | NTP |

### ۱۰) نکات امنیتی

- Log حاوی IP/User است؛ دسترسی و رمزنگاری انتقال.
- Log را محو/حذف نکنید؛ Immutable.

### ۱۱) جمع‌بندی مفهومی

- سه نوع Log و سه سطح logtraffic.
- طراحی بر اساس هدف.
- حجم=رویداد×اندازه×روز.
- Local مرجع نیست.
- NTP برای Correlation.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) سه نوع Log در FortiOS؟ *(پاسخ: 27-1-ت1)*

**ت2.** (ساده) تفاوت `logtraffic all` و `utm`؟ *(پاسخ: 27-1-ت2)*

**ت3.** (متوسط) محاسبه کنید: 12M Session، 450 B، 180 روز. *(پاسخ: 27-1-ت3)*

**ت4.** (متوسط) چرا Deny باید Log شود؟ *(پاسخ: 27-1-ت4)*

**ت5.** (سخت) نویز Log مانع کشف نفوذ شد؛ طرح اصلاح. *(پاسخ: 27-1-ت5)*

**ت6.** (سخت، طراحی) استاندارد Logging سازمان را در ۸ بند بنویسید. *(پاسخ: 27-1-ت6)*

**Q1.** Quick quiz (English): Why should the local firewall log not be the only copy of the logs? *(پاسخ: 27-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Forward traffic | Forward traffic log | Log ترافیک عبوری |
| Implicit deny | Implicit deny policy | رد ضمنی |
| Retention | Log retention | مدت نگهداری |

- *Log denied traffic to detect scans.* ← Deny را برای کشف Scan Log کنید.

### ۱۴) کارت Lab

**کارت Lab:** Logging. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/log.md`.

### ۱۵) منابع

- [Sample logs by log type](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/986892/sample-logs-by-log-type)
- [Log message fields](https://docs.fortinet.com/document/fortigate/7.0.0/fortios-log-message-reference/357866/log-message-fields)
- NIST SP 800-92

<a id="l-27-2"></a>

## درس 27-2 — مانیتورینگ با SNMP و Zabbix: معیارها، Template، Trigger، Baseline و کاهش Alert نویزی

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۰، ۲۷-۱ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. SNMPv3 را (در صورت پشتیبانی) ایمن فعال و Source را محدود کند.
2. Host/Template در Zabbix بسازد و معیارهای کلیدی FortiGate را بگیرد.
3. Trigger بر پایه‌ی Baseline و Hysteresis بنویسد.
4. Alert نویزی و Flapping را کاهش دهد.
5. Dashboard عملیاتی و SLA بسازد.
6. مانیتورینگ HA/VPN/Interface/Session را پوشش دهد.

### ۲) مفهوم پایه: چیست و چرا؟

مانیتورینگ بدون آستانه‌ی معنادار فقط نمودار است. سه خطای رایج: SNMPv2c با Community ضعیف و باز، Triggerهای ثابت بدون Baseline، و Alertهای بی‌شمار که تیم را «کور» می‌کنند (Alert fatigue). هدف: **کم‌تر ولی دقیق‌تر**.

### ۳) توضیح عمیق فنی

#### ۱) SNMP

- **v2c:** Community متن آشکار؛ فقط Lab/شبکه‌ی مدیریت؛ Source محدود.
- **v3:** `authPriv` (احراز + رمزنگاری)؛ کاربر جدا. روش دقیق فیلدها در 7.0.3 `Unverified`.
- فعال‌سازی روی Interface مدیریتی (`allowaccess snmp`) و محدودسازی Host مجاز.

#### ۲) معیارها (نمونه OID/موضوع)

| معیار | موضوع | کاربرد |
|---|---|---|
| CPU/Memory | سلامت | ظرفیت |
| Session count/CPS | بار | Exhaustion |
| Interface in/out/error | لینک | کابل/ظرفیت |
| HA status/Sync | دسترس‌پذیری | Failover |
| VPN tunnel up/down | سرویس | قطع Tunnel |
| Disk/Log | Log | از دست‌رفتن Log |

#### ۳) Trigger هوشمند

``` text
CPU high:     avg(5m) > baseline_p95 x 1.3  for 10m   (not instant spike)
Interface err: delta(errors,10m) > 100  and  rate rising
Session:      > 80% of max for 5m
Tunnel down:  last(status)=down for 2 consecutive checks (avoid flap)
Hysteresis:   recover when value < 0.9 x threshold
```

#### ۴) کاهش نویز

Dependency (اگر Tunnel Down، Alert سرویس‌های پشت آن را سرکوب کن)، Maintenance window، گروه‌بندی، شدت (Warning/High)، Escalation. معیار کیفیت Alert: درصد Alertهایی که اقدام لازم داشتند (Actionable rate).

#### ۵) SLA/Dashboard

Availability = uptime/total؛ نمودار روند CPU/Session، وضعیت Tunnelها، HA، Top Interface.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| SNMP نسخه | v3 در تولید |
| Trigger | Baseline + Hysteresis |
| Dependency | برای کاهش Storm |
| Escalation | سطوح |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Host FGT با Template SNMP؛ `snmpwalk` پاسخ؛ نمودار CPU/Interface در Zabbix.

**متوسط (تحلیل):** Trigger CPU>80٪ هر شب ساعت ۲ (Backup/Scan) Alert می‌دهد. تحلیل: الگوی عادی (Baseline)؛ راه: آستانه با ضریب Baseline و Maintenance window؛ نتیجه: Alert کاذب ≈ صفر.

**سخت (طراحی):** ۱۰ فایروال، ۴۰ Tunnel؛ Alert Storm هنگام قطع ISP (۴۰ Alert). طراحی: Dependency (ISP down → سرکوب Tunnel/Session Alerts)، یک Alert مرکزی «ISP down site X» با Escalation، Trigger Flap با ۲ بررسی متوالی، و Dashboard سایت. معیار: ≤ ۳ Alert برای یک قطع.

### ۶) پیاده‌سازی از مسیر GUI

1. System → SNMP: SNMPv3 users/Communities (Source Hosts).
2. Network → Interfaces → Administrative Access: SNMP روی Interface مدیریت.
3. Zabbix: Configuration → Hosts → Templates → Triggers.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system snmp sysinfo
    set status enable
    set description "FGT-A"
end
config system interface
    edit "mgmt"
        set allowaccess ping https ssh snmp
    next
end
# from monitoring server
snmpwalk -v3 -l authPriv -u <USER> -a SHA -A <AUTHPASS> -x AES -X <PRIVPASS> 192.168.90.1 1.3.6.1.2.1.1
```

### ۸) Verification (اثبات صحت)

- snmpwalk موفق؛ داده در Zabbix.
- Trigger آزمایشی (افزایش مصنوعی CPU در Lab).
- Dependency: Alert Storm آزمون‌شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| SNMP timeout | Firewall/allowaccess/Source | ACL/Interface |
| Alert نویزی | Trigger | Baseline/Hysteresis |
| داده ناقص | Template/OID | Template صحیح |

### ۱۰) نکات امنیتی

- v3 با Source محدود؛ v2c Community ساده ممنوع.
- شبکه‌ی مدیریت.

### ۱۱) جمع‌بندی مفهومی

- SNMPv3 + Source.
- Trigger بر Baseline با Hysteresis.
- Dependency و Maintenance window.
- Actionable rate.
- Dashboard/SLA.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا v3 بهتر از v2c است؟ *(پاسخ: 27-2-ت1)*

**ت2.** (ساده) Hysteresis چیست؟ *(پاسخ: 27-2-ت2)*

**ت3.** (متوسط) CPU>80٪ هر شب Alert می‌دهد؛ چگونه کاهش می‌دهید؟ *(پاسخ: 27-2-ت3)*

**ت4.** (متوسط) Dependency در Zabbix چه می‌کند؟ *(پاسخ: 27-2-ت4)*

**ت5.** (سخت) Alert Storm هنگام قطع ISP؛ طرح. *(پاسخ: 27-2-ت5)*

**ت6.** (سخت، طراحی) ۶ Trigger کلیدی FortiGate با آستانه و دلیل. *(پاسخ: 27-2-ت6)*

**Q1.** Quick quiz (English): What is alert fatigue and how can it be reduced? *(پاسخ: 27-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Baseline | Performance baseline | مرجع عادی |
| Hysteresis | Hysteresis | تأخیر برگشت |
| Actionable rate | Actionable alert rate | نسبت Alertهای نیازمند اقدام |

- *Prefer SNMPv3 and restrict polling sources.* ← SNMPv3 را ترجیح دهید و منابع Poll را محدود کنید.

### ۱۴) کارت Lab

**کارت Lab:** SNMP/Zabbix. **وضعیت:** اجرا نشده (`Unverified` برای v3). **Evidence:** `03-ops/snmp.md`.

### ۱۵) منابع

- Zabbix documentation (SNMP templates)
- Fortinet Docs: SNMP (7.0)
- NIST SP 800-137 (Continuous monitoring)

<a id="l-27-3"></a>

## درس 27-3 — REST API و Automation امن: احراز هویت، Trusted Host، GET/PUT، Idempotency، Rollback و آزمون

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۱، ۲۶-۳، ۲۷-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده». مسیر دقیق Token/Endpoint 7.0.3 `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. اصول API امن (Token، Least Privilege، Trusted Host، TLS) را اجرا کند.
2. فراخوانی‌های GET برای مانیتورینگ و PUT/POST برای تغییر کنترل‌شده بنویسد.
3. Idempotency، Dry-run، Backup و Rollback را در Script اعمال کند.
4. خطاهای HTTP (401/403/404/424) را تفسیر کند.
5. Log/Audit تماس‌های API را بسازد.
6. ریسک‌های Automation (تغییر گسترده، Token لو رفته) را مهار کند.

### ۲) مفهوم پایه: چیست و چرا؟

Automation سرعت و تکرارپذیری می‌دهد و خطا را هم سریع و گسترده تکثیر می‌کند. اصل: **اول خواندن، بعد تغییر؛ هر تغییر با Backup و Rollback؛ هر Token با حداقل دسترسی و منبع محدود.**

### ۳) توضیح عمیق فنی

#### ۱) اصول امنیتی

``` text
1 Dedicated API admin, minimal accprofile (read-only for monitoring)
2 Trusted hosts: only the automation server IP
3 HTTPS with valid cert (verify TLS; avoid -k in production)
4 Token stored in a secret manager, never in repo/logs
5 Rotate tokens; revoke on staff change
6 Log every call (who/what/when)
```

#### ۲) الگوی فراخوانی (نمونه؛ مسیر دقیق `Unverified`)

``` text
GET  https://fgt/api/v2/monitor/system/status
GET  https://fgt/api/v2/cmdb/firewall/policy
PUT  https://fgt/api/v2/cmdb/firewall/policy/31     (change)
Header: Authorization: Bearer <API-TOKEN>
```

#### ۳) Idempotency و Dry-run

Script باید «وضعیت مطلوب» را بیان کند، نه «دنباله‌ی دستور». قبل از تغییر: بخوان، مقایسه کن، فقط اگر تفاوت بود اعمال کن. Dry-run: فقط Diff چاپ شود.

``` text
desired = {policy 31: service HTTPS, action accept}
current = GET policy 31
if current != desired: backup(current); PUT desired; verify(GET); else: no-op
```

#### ۴) خطاها

401 (Token/Trusthost)، 403 (Profile کم)، 404 (Object)، 424 (وابستگی/Reference)، 500. هرگز خطا را نادیده نگیرید؛ در Script Stop.

#### ۵) ریسک و کنترل

تغییر گسترده با یک Script اشتباه: Canary (۱ دستگاه)، Review کد، Change، Rollback خودکار، Rate limit، Scope محدود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Read-only یا Write | Monitoring فقط Read |
| Canary | یک دستگاه ابتدا |
| Rollback | Backup+Revert |
| TLS | تأیید گواهی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** GET وضعیت سیستم با Token؛ خروجی JSON: version، hostname؛ ثبت در Log.

**متوسط (تحلیل):** 401 با Token درست: Trusthost IP سرور را شامل نمی‌شود؛ رفع: افزودن IP. یا Token لغو شده.

**سخت (Idempotency):** Script هر اجرا یک Address جدید می‌ساخت و ۵۰ Object تکراری شد. تحلیل: عدم بررسی وجود؛ اصلاح: GET نام، مقایسه، PUT یا POST شرطی؛ تست دو بار اجرا ⇒ بدون تغییر؛ Dry-run و Backup قبل از تغییر.

### ۶) پیاده‌سازی از مسیر GUI

1. System → Administrators → Create New → REST API Admin (Profile، Trusted Hosts، توکن).
2. Log & Report → Events → System برای Audit.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system api-user
    edit "monitor-api"
        set accprofile "readonly-api"
        config trusthost
            edit 1
                set ipv4-trusthost 192.168.90.50 255.255.255.255
            next
        end
    next
end
# from automation host (secrets from environment)
curl --cacert fgt-ca.pem -H "Authorization: Bearer $FGT_TOKEN" https://192.168.90.1/api/v2/monitor/system/status
```

### ۸) Verification (اثبات صحت)

- GET موفق و JSON.
- آزمون 401 با IP غیرمجاز (منفی).
- اجرای دو‌بارهٔ Script بدون تغییر (Idempotent).
- Log تماس‌ها.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| 401 | Trusthost/Token | تنظیم |
| 403 | Profile | accprofile |
| 424 | Reference | وابستگی |
| Script تغییر زیاد | Dry-run | Scope/Canary |

### ۱۰) نکات امنیتی

- Token در Vault؛ TLS verify.
- Least privilege؛ Trusthost.
- Review و Canary.

### ۱۱) جمع‌بندی مفهومی

- اول بخوان بعد تغییر.
- Idempotent + Dry-run + Backup.
- Least privilege و Trusthost.
- Canary و Rollback.
- Audit تماس‌ها.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Trusthost برای API؟ *(پاسخ: 27-3-ت1)*

**ت2.** (ساده) Idempotent یعنی چه؟ *(پاسخ: 27-3-ت2)*

**ت3.** (متوسط) 401 با Token درست؛ علل؟ *(پاسخ: 27-3-ت3)*

**ت4.** (متوسط) Dry-run چه فایده‌ای دارد؟ *(پاسخ: 27-3-ت4)*

**ت5.** (سخت) Script ۵۰ Object تکراری ساخت؛ تحلیل و اصلاح. *(پاسخ: 27-3-ت5)*

**ت6.** (سخت، طراحی) طرح امن Automation برای مانیتورینگ و تغییر Policy. *(پاسخ: 27-3-ت6)*

**Q1.** Quick quiz (English): Why should automation scripts support a dry-run mode? *(پاسخ: 27-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| API | Application Programming Interface | رابط برنامه‌نویسی |
| Idempotent | Idempotent operation | عملیات تکرارپذیر بدون اثر اضافه |
| Canary | Canary deployment | اعمال آزمایشی روی بخش کوچک |

- *Never store API tokens in a repository.* ← هرگز توکن API را در مخزن ذخیره نکنید.

### ۱۴) کارت Lab

**کارت Lab:** API. **وضعیت:** اجرا نشده/Unverified. **Evidence:** `03-ops/api.md`.

### ۱۵) منابع

- Fortinet Docs: REST API / API user (7.0)
- OWASP API Security Top 10

<a id="l-27-4"></a>

## درس 27-4 — Hardening مدیریتی عملی و Backup/Restore: اجرای چک‌لیست، آزمون منفی و اثبات بازیابی

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۷، ۱۲-۸، ۲۶-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. چک‌لیست Hardening را با دستور/GUI اجرا و برای هر مورد شاهد ثبت کند.
2. آزمون‌های منفی (دسترسی غیرمجاز) را اجرا کند.
3. Restore را در Lab اثبات و RTO ثبت کند.
4. Audit/Change را با Hardening هماهنگ کند.
5. انحراف (Drift) از استاندارد را بسنجد.

### ۲) مفهوم پایه: چیست و چرا؟

Hardening بدون آزمون «تنظیمات تزئینی» است. هر کنترل باید با یک آزمون منفی ثابت شود: «از IP غیرمجاز ورود نمی‌شود»، «Telnet بسته است»، «بعد از ۳ تلاش قفل می‌شود».

### ۳) توضیح عمیق فنی

#### ۱) چک‌لیست با آزمون

| کنترل | تنظیم | آزمون منفی |
|---|---|---|
| Admin حداقلی/Trusthost | `trusthost` | ورود از IP دیگر رد شود |
| Telnet/HTTP | `allowaccess` بدون telnet/http | `nc` به 23/80 رد |
| HTTPS/SSH | TLS/Cipher مناسب | اسکن Cipher ضعیف نداشته باشد |
| MFA | RADIUS/Token | ورود با رمز تنها رد |
| Lockout | `admin-lockout-*` | ۴ رمز غلط ⇒ قفل |
| Timeout | `admintimeout` | بعد از 10 دقیقه Logout |
| Local-in | Policy | پورت مدیریتی از WAN بسته (nmap) |
| NTP | امن | زمان درست |
| Patch | نسخه | مقایسه با PSIRT |
| Log | Event Admin | تغییر تستی ثبت شود |

#### ۲) آزمون‌ها (نمونه)

``` text
nmap -Pn -p 22,23,80,443,8443 203.0.113.1      # from outside: expect filtered/closed
ssh admin@192.168.90.1 (from non-trusted IP)    # expect refusal
```

#### ۳) Restore

``` text
1 Backup (encrypted) 2 Lab FGT same firmware 3 Restore 4 Compare interfaces/policies/routes
5 Measure RTO 6 Document gaps (certs/keys/licenses)
```

نکته: گواهی/کلید خصوصی/لایسنس/FortiGuard معمولاً جداگانه بازیابی می‌شوند.

#### ۴) Drift از استاندارد

اسکریپت مقایسه‌ی Config با «Baseline Hardening» (الگوهای مجاز) و گزارش انحراف ماهانه.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| آزمون منفی | برای هر کنترل |
| Restore test | فصلی |
| Baseline Hardening | نسخه‌دار |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** nmap از بیرون: 443/22 بسته؛ ورود از IP غیرمجاز رد؛ Log رد ثبت شد.

**متوسط (تحلیل):** Lockout کار نمی‌کند: تنظیم روی Global ولی کاربر API/Local متفاوت؛ بررسی `admin-lockout-threshold`؛ آزمون تکرار؛ ثبت.

**سخت (Restore ناقص):** Restore موفق ولی VPN کار نمی‌کند: گواهی/کلید و PSK بازیابی نشد؛ سند Gap: «Secrets جدا»؛ اصلاح Runbook: بازیابی گواهی/لایسنس. RTO واقعی ۴۵ دقیقه (هدف ۳۰) ⇒ اتوماسیون گام‌ها.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system global
    set admintimeout 10
    set admin-lockout-threshold 3
    set admin-lockout-duration 300
end
config system interface
    edit "port1"
        set allowaccess ping
    next
end
execute backup config sftp hardening-test.conf 192.168.90.10 backup-user <PASSWORD>
```

### ۸) Verification (اثبات صحت)

- جدول کنترل→آزمون→نتیجه.
- Restore و RTO ثبت.
- Drift report.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Lockout نه | تنظیم | Global/Per-user |
| Restore ناقص | VPN/Cert | Secrets جدا |
| Port باز | nmap | Local-in/allowaccess |

### ۱۰) نکات امنیتی

- آزمون فقط از IP مجاز/Lab.
- Evidence بدون Secret.

### ۱۱) جمع‌بندی مفهومی

- هر کنترل = تنظیم + آزمون منفی.
- Restore شامل Secrets/لایسنس.
- Drift ماهانه.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) آزمون منفی چیست؟ *(پاسخ: 27-4-ت1)*

**ت2.** (ساده) چرا `admintimeout`؟ *(پاسخ: 27-4-ت2)*

**ت3.** (متوسط) پس از Restore VPN کار نمی‌کند؛ چرا؟ *(پاسخ: 27-4-ت3)*

**ت4.** (متوسط) چگونه RTO را اندازه می‌گیرید؟ *(پاسخ: 27-4-ت4)*

**ت5.** (سخت) ۱۰ کنترل Hardening با آزمون منفی بنویسید. *(پاسخ: 27-4-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی کاهش RTO از ۴۵ به ۳۰ دقیقه. *(پاسخ: 27-4-ت6)*

**Q1.** Quick quiz (English): Why must every hardening control be accompanied by a negative test? *(پاسخ: 27-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RTO | Recovery Time Objective | زمان هدف بازیابی |
| Negative test | Negative test | آزمون ممنوعیت |

- *Prove each control with a negative test.* ← هر کنترل را با آزمون منفی ثابت کنید.

### ۱۴) کارت Lab

**کارت Lab:** Hardening. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/hardening.md`.

### ۱۵) منابع

- CIS FortiGate Benchmark
- NIST SP 800-53
- Fortinet: Hardening your FortiOS

<a id="l-27-5"></a>

## درس 27-5 — Gate G10: آزمون عملی Logging، Monitoring، Hardening و Backup — صورت مسئله، کلید و Rubric

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۰ تا ۲۷-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Syslog مرکزی، Baseline/Trigger، Hardening و Backup/Restore را با شواهد تحویل دهد.
2. سه عیب (Log نمی‌رسد، Alert کاذب، Restore ناقص) را رفع کند.
3. Detection یک رویداد (Login ناموفق مکرر) را از Log تا Alert نشان دهد.
4. Evidence و RCA ارائه دهد.

### ۲) مفهوم پایه: چیست و چرا؟

آزمون جامع عملیات. کلید پاسخ پس از تلاش.

### ۳) توضیح عمیق فنی

#### صورت مسئله

1. Syslog reliable از FGT به rsyslog؛ فایل روزانه.
2. Baseline ۷ روز (شبیه‌سازی) و ۶ Trigger با Hysteresis.
3. Hardening: ۱۰ کنترل با آزمون منفی.
4. Backup→Sanitize→Git→Restore در Lab، RTO.
5. Detection: ۲۰ Login ناموفق ⇒ Alert.

عیب‌ها (مربی): Route Syslog اشتباه؛ Trigger CPU بدون Baseline؛ Restore بدون گواهی.

#### کلید (خلاصه)

- عیب ۱: `execute ping` از source-ip و Sniffer؛ رفع Route.
- عیب ۲: آستانه=Baseline×1.3 و Maintenance window.
- عیب ۳: Runbook Secrets/گواهی.
- Detection: Alert بر 20 ناموفق/5m؛ Block مشروط.

#### Rubric (۱۰۰)

Log ۲۰؛ Monitoring ۲۵؛ Hardening ۲۰؛ Backup/Restore ۲۰؛ Detection/RCA ۵؛ صداقت ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Syslog و فایل.

**متوسط:** Trigger و Hardening.

**سخت:** Restore و RCA.

### ۸) Verification (اثبات صحت)

- Evidence G10: جدول دستور/خروجی/نتیجه.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Alert نیامد | Syslog/Trigger | مسیر/آستانه |

### ۱۰) نکات امنیتی

- Secret در Evidence نیست.

### ۱۱) جمع‌بندی مفهومی

- آزمون عملیات = Log + Monitoring + Hardening + Restore + Detection.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) شواهد لازم برای Log مرکزی؟ *(پاسخ: 27-5-ت1)*

**ت2.** (ساده) چرا Trigger باید Baseline داشته باشد؟ *(پاسخ: 27-5-ت2)*

**ت3.** (متوسط) عیب Route Syslog را چگونه کشف می‌کنید؟ *(پاسخ: 27-5-ت3)*

**ت4.** (متوسط) RTO را چگونه گزارش می‌کنید؟ *(پاسخ: 27-5-ت4)*

**ت5.** (سخت) Detection Brute-force از Log تا Alert را شرح دهید. *(پاسخ: 27-5-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی بهبود پس از آزمون. *(پاسخ: 27-5-ت6)*

**Q1.** Quick quiz (English): What evidence proves central logging works? *(پاسخ: 27-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| G10 | Gate 10 | دروازه ۱۰ |

- *Collect evidence for every gate.* ← برای هر Gate شاهد جمع کنید.

### ۱۴) کارت Lab

**کارت Lab:** G10. **Evidence:** `03-ops/g10.md`.

### ۱۵) منابع

- درس‌های ۲۷-۰ تا ۲۷-۷

## درس 27-7 — Hardening، Backup/Restore و API: امن‌سازی مدیریتی و بازیابی قابل‌اثبات

**فصل ۲۷ · درس افزوده (پس از ۲۷-۵) · پیش‌نیاز: ۱۲-۸، ۲۶-۰، ۲۷-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** اصول از دانش عملیاتی و Local-in (۱۲-۸)؛ دستورهای `Unverified`؛ **REST API و SNMPv3 در این دور با مستند رسمی تأیید نشد** (به مرجع 7.0 مراجعه شود). Lab «اجرا نشده».

### ۱) هدف آموزشی

1. چک‌لیست Hardening مدیریتی (Admin، Access، سرویس‌ها، زمان‌بندی) را اجرا و دلیل هر مورد را بگوید.
2. **Backup/Restore** را طوری انجام دهد که «بازیابی‌شدنی بودن» اثبات شود.
3. **API/Automation** را با Least Privilege و Trusted Host محدود و ایمن به‌کار بگیرد.
4. تغییرات مدیریتی را Audit و Rollback کند.

### ۲) مفهوم پایه

فایروال لبه با پیش‌فرض‌های «راحت» ایمن نیست. Hardening یعنی کاهش سطح حمله: هر سرویس/حساب/پورت غیرضروری را ببندید و هر چه باقی ماند محافظت و پایش شود. Backup بدون **تست Restore** ادعاست، نه تضمین.

### ۳) توضیح عمیق فنی

#### ۳-۱) چک‌لیست Hardening

| حوزه | اقدام | دلیل |
|---|---|---|
| Admin | تغییر رمز/نام admin پیش‌فرض، حساب شخصی، حذف حساب مشترک | Accountability |
| دسترسی | `allowaccess` حداقل، Trusted Host، Local-in Policy | سطح حمله (۱۲-۸) |
| پروتکل | غیرفعال Telnet/HTTP؛ HTTPS/SSH با TLS/Cipher مناسب | رمزنگاری |
| MFA | برای Admin | سرقت رمز |
| Timeout/Lockout | `admintimeout`، `admin-lockout-*` | Brute-force |
| Profile | Admin Profile حداقلی (Read-only برای Audit) | Least Privilege |
| زمان | NTP امن | Log معتبر |
| Banner/Log | Log تغییر Config و Login | Audit |
| Patch | پیگیری PSIRT؛ نسخه‌ی 7.0.3 قدیمی است | CVE |

#### ۳-۲) Backup

- **چه چیزی:** Config (کامل)، Certificate/Key (جدا و رمزشده)، لیست نسخه/Serial/لایسنس.
- **کجا:** مقصد خارج از دستگاه (SFTP/Git)، رمزنگاری، Retention (روزانه/هفتگی).
- **امنیت:** فایل Config شامل Hash/رمز رمزگذاری‌شده است ولی حساس؛ هرگز در مخزن عمومی؛ پاک‌کردن Secret قبل از Git.
- **تست Restore:** در Lab با همان نسخه و Interface؛ بازیابی و مقایسه `show` پیکربندی؛ ثبت زمان RTO.

#### ۳-۳) API و Automation

اصول: حساب/Token **فقط** با Profile لازم؛ **Trusted Host** (IP مبدأ)؛ Token در Vault/متغیر محیطی؛ شروع با GET (خواندنی)؛ هر POST/PUT با Change؛ Log تماس‌های API. `Unverified`: روش ایجاد Token و مسیرهای `/api/v2/...` در 7.0.3 را با مرجع تأیید کنید.

#### ۳-۴) Audit و Rollback

- هر تغییر: Ticket، Diff Config، تأییدکننده.
- Rollback: Config قبلی + Session (۱۳-۷) + تست مثبت/منفی.
- «تغییر اضطراری» هم ثبت شود.

### ۴) مثال حل‌شده

``` text
config system global
    set admintimeout 10
    set admin-lockout-threshold 3
    set admin-lockout-duration 300
end
config system admin
    edit "mgr-hamed"
        set accprofile "super_admin_readonly"
        set trusthost1 192.168.90.0 255.255.255.0
    next
end
execute backup config sftp fgt-daily.conf 192.168.90.10 backup-user <PASSWORD>
```

(نام فیلدها/سینتکس `Unverified`.) **تست Restore:** Lab FGT هم‌نسخه، `execute restore config ...`، مقایسه Interface/Policy، ثبت RTO.

**مثال متوسط:** Backup با رمز در ریپو Commit شد. اقدام: حذف از تاریخچه، چرخش رمزها، Scan Secret (ابزار)، Prevention (pre-commit).

**مثال سخت:** پس از ارتقا Config ناسازگار؛ Rollback: Backup قبل از ارتقا، Firmware قبلی، تست.

### ۵) GUI و CLI

**GUI:** System → Administrators؛ System → Settings؛ System → Config → Backup/Restore؛ Log & Report → Events. **CLI:** مطابق مثال.

### ۶) نکات امنیتی

- حساب مشترک و رمز ضعیف ممنوع.
- Token API هرگز در Log/ریپو.
- Backup رمزشده.

### ۷) جمع‌بندی

- Hardening = کاهش سطح حمله + Least Privilege + MFA + Patch.
- Backup بدون تست Restore بی‌اعتبار.
- API با Trusted Host و Profile حداقلی.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) چرا Telnet/HTTP غیرفعال شود؟ *(پاسخ: 27-7-ت1)*

**ت2.** (متوسط) تست Restore چگونه انجام می‌شود؟ *(پاسخ: 27-7-ت2)*

**ت3.** (سخت) چک‌لیست ۱۰ مورد Hardening با دلیل. *(پاسخ: 27-7-ت3)*

**ت4.** (سخت، طراحی) Token API برای مانیتورینگ را ایمن طراحی کنید. *(پاسخ: 27-7-ت4)*

**Q1.** Quick quiz (English): Why is an untested backup unreliable? *(پاسخ: 27-7-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RTO | Recovery Time Objective | زمان هدف بازیابی |
| Hardening | System hardening | امن‌سازی |
| Trusted host | Trusted host | IP مجاز |

- *Backups must be tested by restoring them.* ← Backupها باید با Restore تست شوند.

### ۱۰) منابع

- Fortinet: «Hardening your FortiOS» (مرجع رسمی؛ نسخه‌ی 7.0 را بررسی کنید)؛ CIS Fortinet FortiGate Benchmark؛ NIST SP 800-53 (CM، AU).

## پاسخ‌های فصل 27

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 27-1

**27-1-ت1** — Traffic، Event و Security/UTM.

**27-1-ت2** — all همه‌ی Sessionها را ثبت می‌کند؛ utm فقط Sessionهایی را که رویداد UTM دارند.

**27-1-ت3** — 12M×450B = 5.4 GB/روز؛ ×180 ≈ 972 GB؛ با 20٪ حاشیه ≈ 1.17 TB؛ فشرده‌سازی کاهش می‌دهد.

**27-1-ت4** — برای کشف Scan/حمله و عیب‌یابی Policy.

**27-1-ت5** — Allow عمومی utm، Allow حیاتی all، Deny همیشه، Alert روی Deny مدیریتی و Bytes غیرعادی، Syslog مرکزی.

**27-1-ت6** — انواع، سطح، مقصد، قالب، Retention، NTP، دسترسی، Alert/بازبینی.

**27-1-Q1** — Because local storage is limited and may be overwritten or lost during an incident.


### پاسخ‌های بازنویسی عمیق درس 27-2

**27-2-ت1** — احراز و رمزنگاری؛ v2c Community را متن آشکار می‌فرستد.

**27-2-ت2** — تفاوت آستانه‌ی ورود و خروج Alert برای جلوگیری از نوسان.

**27-2-ت3** — آستانه از Baseline با ضریب، Maintenance window، Trigger مدت‌دار (10m).

**27-2-ت4** — Alert وابسته را وقتی وابستگی اصلی Down است سرکوب می‌کند.

**27-2-ت5** — Dependency، Alert مرکزی سایت، Flap با بررسی متوالی، Escalation؛ هدف ≤ ۳ Alert.

**27-2-ت6** — CPU، Memory، Session، Interface error، Tunnel down، HA؛ هر کدام با Baseline/Hysteresis.

**27-2-Q1** — Excessive low-value alerts cause operators to ignore them; baselines, dependencies and hysteresis reduce them.


### پاسخ‌های بازنویسی عمیق درس 27-3

**27-3-ت1** — تا Token فقط از IP مجاز قابل‌استفاده باشد و سرقت Token کم‌اثر شود.

**27-3-ت2** — اجرای مکرر همان نتیجه را بدهد، بدون ایجاد تغییر یا Object تکراری.

**27-3-ت3** — Trusthost، Token لغو/منقضی، API user غیرفعال.

**27-3-ت4** — Diff تغییرات را بدون اعمال نشان می‌دهد و خطای گسترده را قبل از وقوع کشف می‌کند.

**27-3-ت5** — نبود بررسی وجود؛ GET نام، مقایسه، PUT/POST شرطی؛ تست دو بار اجرا؛ پاک‌سازی تکراری‌ها با Backup.

**27-3-ت6** — حساب Read-only برای مانیتورینگ؛ حساب Write جدا با Canary؛ Trusthost، Vault، TLS، Review، Backup/Rollback، Audit.

**27-3-Q1** — To show the planned changes without applying them and catch mistakes before they spread.


### پاسخ‌های بازنویسی عمیق درس 27-4

**27-4-ت1** — آزمونی که باید شکست بخورد تا اثبات شود دسترسی غیرمجاز بسته است.

**27-4-ت2** — کاهش خطر Session رهاشده.

**27-4-ت3** — گواهی/کلید/PSK یا لایسنس جداگانه بازیابی نشده؛ باید در Runbook باشد.

**27-4-ت4** — زمان از شروع Restore تا سرویس‌های حیاتی تأییدشده؛ در Lab با زمان‌سنج.

**27-4-ت5** — جدول بالا؛ هر کنترل یک آزمون منفی.

**27-4-ت6** — اتوماسیون Restore، Runbook مرحله‌ای، Secrets از Vault، آزمون فصلی.

**27-4-Q1** — Because only a failed unauthorized attempt proves the control actually works.


### پاسخ‌های بازنویسی عمیق درس 27-5

**27-5-ت1** — فایل Log روزانه روی سرور با رویداد آزمایشی و tcpdump TCP 514.

**27-5-ت2** — تا آستانه با رفتار عادی تنظیم شود و Alert کاذب کم شود.

**27-5-ت3** — `execute ping` با source-ip، Sniffer روی Interface خروجی، tcpdump سرور.

**27-5-ت4** — زمان‌بندی مراحل Restore و Verification؛ مقایسه با هدف؛ Gap.

**27-5-ت5** — Event Login failed در Syslog؛ Parser؛ Trigger 20/5m؛ Alert؛ Playbook Block؛ ثبت.

**27-5-ت6** — Alert Dependency، HA Syslog، Restore خودکار، Drift report.

**27-5-Q1** — A log file on the server containing a test event, plus a packet capture of the syslog session.

### پاسخ‌های درس افزوده‌ی 27-0 (فصل 27)

**27-0-ت1** — Traffic، Event، UTM/Security.

**27-0-ت2** — تا انحراف را با مرجع عادی تشخیص دهیم و آستانه‌ی معنادار بگذاریم.

**27-0-ت3** — CPU>70٪ هشدار/90٪ بحرانی؛ Memory>80٪/90٪؛ Session>70٪/90٪ حد؛ Interface Error رشد؛ Tunnel/HA Down؛ Disk Log>80٪؛ همه بر پایه‌ی Baseline.

**27-0-ت4** — ۱۸۰ روز × ۲ GB = ۳۶۰ GB؛ + ۲۰٪ حاشیه؛ مرکزی با فشرده‌سازی و چرخش؛ هشدار فضا.

**27-0-Q1** — So events from different devices can be correlated reliably in time.


### پاسخ‌های درس افزوده‌ی 27-7 (فصل 27)

**27-7-ت1** — رمز و داده را بدون رمزنگاری می‌فرستند و قابل شنودند.

**27-7-ت2** — در Lab هم‌نسخه Restore، مقایسه Interface/Policy/Route، اندازه‌گیری RTO و ثبت.

**27-7-ت3** — تغییر admin پیش‌فرض، حساب شخصی، Trusted Host، allowaccess حداقل، غیرفعال Telnet/HTTP، MFA، Timeout/Lockout، Profile حداقلی، NTP، Patch.

**27-7-ت4** — حساب API با Profile Read-only، Trusted Host فقط مانیتورینگ، Token در Vault، چرخش دوره‌ای، Log تماس‌ها.

**27-7-Q1** — Because a backup that was never restored may be corrupt or incomplete, so recovery is not proven.

# پایان بخش ۹ (فصل‌های ۲۵ تا ۲۷)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- اتصال FGT-CSR؛ مدیریت مرکزی و جایگزین بدون لایسنس؛ Syslog، SNMP، API، Hardening، Backup.

## ۲) آزمون پایان سه فصل
**س1** — Exstart در OSPF؟

**س2** — معادل show در FGT؟

**س3** — FMG؟

**س4** — FAZ؟

**س5** — جایگزین FAZ؟

**س6** — Backup بدون Secret؟

**س7** — SNMP امن؟

**س8** — Trusthost؟

**س9** — API Token؟

**س10** — Hardening؟

**س11** — Restore تست؟

**س12** — G10؟


## ۳) پاسخ آزمون
- **س1:** اغلب MTU mismatch.
- **س2:** get/diagnose.
- **س3:** مدیریت مرکزی.
- **س4:** Log مرکزی.
- **س5:** rsyslog.
- **س6:** حذف رمز.
- **س7:** v3.
- **س8:** محدودسازی IP.
- **س9:** کلید دسترسی.
- **س10:** ایمن‌سازی.
- **س11:** برای اعتبار Backup.
- **س12:** Monitoring+Log+Hardening+Backup.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| Multi-vendor | L3 | A6 |
| مدیریت مرکزی | L2 | A9 |
| Ops/Hardening | L3 | G10 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. Labها اجرا نشده. 2. FMG/FAZ لایسنس. 3. API/SNMP سینتکس Unverified.

## ۶) پیش‌نیازهای بخش بعد
Backup همه‌ی Gateها؛ Wireshark/Sniffer مسلط.

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*`

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۲۷ |
| آخرین درس تکمیل‌شده | ۲۷-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۲۸ |
| فایل تولیدشده | `course/Course_Part_09_Chapters_25-27.md` |
