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

> **نسخه v3.9:** این بخش در دسته‌های B/A/C بدون تغییر محتوایی است (فشرده‌تر از فصل‌های توسعه‌یافته؛ در دسته D بازنویسی می‌شود).

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Interoperability؟** سازمان‌ها معمولاً چند سازنده دارند: Cisco در هسته، Fortinet در لبه. اگر «مفهوم» را بدانید، تغییر سازنده فقط تغییر Syntax است؛ اگر فقط دستور حفظ کرده باشید، با هر سازنده از صفر شروع می‌کنید. مثل مترجم: «آب» و «Water» یک مفهوم‌اند.

**نگاشت‌های مهم:** SVI ↔ VLAN Interface؛ ACL ↔ Firewall Policy (با تفاوت Stateless/Stateful)؛ NAT ↔ Policy NAT/VIP؛ VRF ↔ VDOM (تقریبی).

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — ACL به Policy

``` text
Cisco: permit tcp 10.10.0.0 0.0.0.255 host 10.20.0.10 eq 443
FGT  : srcaddr NET-USERS, dstaddr SRV-ERP, service HTTPS, accept
```

Wildcard 0.0.0.255 ⇒ /24؛ برگشت در Stateful خودکار.

#### مثال متوسط — پیش‌فرض‌ها

Reference Bandwidth OSPF هر دو 100 Mbps؛ باید یکسان تنظیم شود.

#### مثال سخت — ترتیب ارزیابی

Policy فورتی‌گیت بعد از DNAT و قبل از SNAT؛ Debug Flow ترتیب را نشان می‌دهد.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: نگاشت مفهوم با یک جدول عملی

| مفهوم | Cisco | FortiGate |
|---|---|---|
| Interface مجازی L3 | SVI | VLAN Interface |
| ACL | access-list | Firewall Policy |
| NAT | ip nat | Policy NAT/VIP |
| Route-map | route-map | Route-map/Policy Route |
| VRF | vrf | VDOM (تقریبی) |

همه‌ی نگاشت‌ها تقریبی‌اند؛ تفاوت Stateful (ACL بدون وضعیت در Cisco) را فراموش نکنید.

**پرسش‌های مصاحبه**
1. *VRF = VDOM؟* ایده مشابه نه یکسان.
2. *ACL Stateful؟* نه.
3. *انتقال Policy؟* بازنویسی نه ترجمه تحت‌اللفظی.

### مثال حل‌شده: انتقال یک ACL سیسکو به Policy فورتی‌گیت

**ورودی (Cisco):**

``` text
ip access-list extended USERS-OUT
 permit tcp 10.10.0.0 0.0.0.255 host 10.20.0.10 eq 443
 permit udp 10.10.0.0 0.0.0.255 host 10.20.0.5 eq 53
 deny   ip any any log
```

**مراحل**
1. Wildcard `0.0.0.255` یعنی ماسک `255.255.255.0`؛ پس منبع 10.10.0.0/24.
2. هر `permit` به یک سطر Policy با Service جدا تبدیل می‌شود.
3. `deny ip any any log` همان Policy Deny صریح با Log است (در FortiGate Implicit Deny بدون Log).
4. تفاوت کلیدی: ACL سیسکو بدون وضعیت است و باید قاعده‌ی برگشت را هم بنویسید؛ Policy فورتی‌گیت Stateful است و برگشت خودکار مجاز می‌شود.

**خروجی (FortiGate):**

``` text
config firewall policy
 edit 10
  set srcintf "port2"
  set dstintf "port3"
  set srcaddr "NET-USERS"
  set dstaddr "SRV-WEB"
  set service "HTTPS"
  set action accept
  set logtraffic all
 next
 edit 11
  set srcintf "port2"
  set dstintf "port3"
  set srcaddr "NET-USERS"
  set dstaddr "SRV-DNS"
  set service "DNS"
  set action accept
 next
 edit 90
  set srcintf "any"
  set dstintf "any"
  set srcaddr "all"
  set dstaddr "all"
  set service "ALL"
  set action deny
  set logtraffic all
 next
end
```

**تأیید:** `diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.10 443 tcp port2` باید Policy 10 را بدهد؛ آزمون منفی: پورت 22 ⇒ Policy 90.

### تکمیل عمیق: Interoperability — چرا زبان مشترک مهم‌تر از برند است؟

#### چرا باید یاد بگیریم؟

سازمان‌ها معمولاً چند سازنده دارند: Cisco در هسته، Fortinet در لبه، شاید Juniper یا MikroTik در شعب. اگر «مفهوم» را بدانید، تغییر سازنده فقط تغییر Syntax است. اگر فقط دستور حفظ کرده باشید، با هر سازنده‌ی جدید از صفر شروع می‌کنید.

#### توضیح ساده

مثل مترجم: «آب» در فارسی و «Water» در انگلیسی یک مفهوم‌اند. در شبکه: «Interface مجازی L3 روی VLAN» در Cisco به آن SVI می‌گویند و در FortiGate «VLAN Interface».

#### جدول نگاشت مفاهیم

| مفهوم | Cisco | FortiGate |
|---|---|---|
| Interface مجازی L3 | SVI | VLAN Interface |
| ACL | access-list | Firewall Policy |
| NAT | ip nat | Policy NAT/VIP |
| Route Policy | route-map | route-map / Policy Route |
| جداسازی Routing | VRF | VDOM (تقریبی) |

VRF = Virtual Routing and Forwarding، یعنی «جدول مسیر مجازی». VDOM علاوه بر Routing، Policy و Admin را هم جدا می‌کند؛ پس «تقریبی» است.

#### مثال ساده — تبدیل ACL به Policy

Cisco:

``` text
ip access-list extended USERS-OUT
 permit tcp 10.10.0.0 0.0.0.255 host 10.20.0.10 eq 443
 deny ip any any log
```

مراحل: ۱) Wildcard 0.0.0.255 یعنی /24 ۲) permit به Policy Accept ۳) deny پایانی به Policy Deny با Log ۴) Stateful بودن: برگشت خودکار.

FortiGate:

``` text
config firewall policy
 edit 10
  set srcintf "port2"
  set dstintf "port3"
  set srcaddr "NET-USERS"
  set dstaddr "SRV-ERP"
  set service "HTTPS"
  set action accept
  set logtraffic all
 next
end
```

#### مثال متوسط — پیش‌فرض‌های متفاوت

OSPF Reference Bandwidth: پیش‌فرض Cisco و FortiGate هر دو 100 Mbps است؛ لینک 1 Gbps و 10 Gbps هر دو Cost=1 می‌شوند. باید دستی یکسان تنظیم شود.

``` text
Cost = Reference BW / Interface BW
100 / 1000 = 0.1 -> 1 (rounded up to minimum)
```

#### مثال سخت — تفاوت رفتاری

در Cisco ACL قبل از NAT یا بعد از NAT ارزیابی می‌شود (بسته به جهت)؛ در FortiGate Policy بر اساس **بعد از DNAT و قبل از SNAT**. یک مهندس که نگاشت را تحت‌اللفظی انجام می‌دهد، Policy با IP اشتباه می‌نویسد. راه: با Debug Flow ترتیب را ببینید.

#### Lab

یک جدول نگاشت ۱۰ ردیفی از دستورهای روزمره‌ی خودتان بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| ترافیک برگشت رد | فرض Stateless | Stateful |
| NAT متفاوت | ترتیب ارزیابی | Debug |
| Cost مغایر | Reference | یکسان‌سازی |

#### پرسش‌ها با پاسخ

**۱. VRF=VDOM؟** نه دقیقاً.
**۲. چرا Wildcard؟** معکوس Mask.
**۳. چرا نگاشت مفهومی؟** جدا از Syntax.

#### English Corner

- *Learn the concept first, then map it to each vendor's syntax.*
- Q: How does a VRF differ from a VDOM?

## درس 25-1 — نگاشت مفاهیم Cisco و Fortinet: برگه‌ی تطبیق دستورها و مدل‌های پردازش

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: فصل ۲ تا ۱۵ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مدل پردازش Cisco (ACL/Route/NAT) و Fortinet (Policy/Route/Session) را مقایسه کند.
2. برگه‌ی تطبیق دستورها (show ↔ get/diagnose) را بسازد.
3. تفاوت‌های مفهومی (Stateless ACL در برابر Stateful Policy) را درست بفهمد.
4. برای هر وظیفه دستور معادل را بنویسد.
5. خطاهای ناشی از «ترجمه‌ی کورکورانه» را بشناسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا برگه‌ی تطبیق؟** کسی که Cisco بلد است و باید با FortiGate تست کند، با یک برگه‌ی «هدف ← دستور Cisco ← دستور FortiGate ← خروجی مورد انتظار» سرعت چند برابر می‌گیرد.

**جمع‌بندی اصلی درس:**

مهندسی که فقط Cisco بلد است FortiGate را با نگاه سیسکویی می‌خواند: «ACL کجاست؟». ولی در FortiGate مفهوم ACL جایش را به Policy داده و مسیر پردازش فرق دارد. نگاشت مفاهیم سریع‌ترین راه یادگیری است، به شرط اینکه تفاوت‌ها را هم بدانید.

### ۳) توضیح عمیق فنی

#### ۱) نگاشت مفهومی

| مفهوم | Cisco IOS | FortiGate |
|---|---|---|
| فیلتر | ACL (Stateless، ترتیبی) | Firewall Policy (Stateful) |
| NAT | `ip nat inside/outside` | NAT در Policy / VIP / IP Pool |
| Interface منطقی | Sub-interface / SVI | VLAN interface / Zone |
| مسیر | `ip route` | `config router static` |
| جدول مسیر | `show ip route` | `get router info routing-table all` |
| ARP | `show ip arp` | `diagnose ip arp list` |
| Session | NAT translations | `diagnose sys session list` |
| Debug | `debug ip ...` | `diagnose debug flow` |
| Capture | EPC/SPAN | `diagnose sniffer packet` |
| ذخیره | `copy run start` | تغییرات خودکار ذخیره می‌شود |

#### ۲) تفاوت‌های مهم

- IOS: Config در RAM تا ذخیره. FortiOS: هر تغییر بلافاصله ذخیره (Revision).
- ACL Stateless و Policy Stateful.
- Policy در FortiGate بین **جفت Interface/Zone** است.
- Default Deny ضمنی در FortiGate (Implicit Deny) و در ACL هم، ولی رفتار Log متفاوت.

#### ۳) مثال معادل

``` text
! Cisco
ip access-list extended OUT
 permit tcp 10.10.0.0 0.0.0.255 any eq 443
interface Gi0/1
 ip access-group OUT in
```

``` text
! FortiGate
config firewall policy
 edit 10
  set srcintf "port2"
  set dstintf "port1"
  set srcaddr "NET-USERS"
  set dstaddr "all"
  set action accept
  set schedule "always"
  set service "HTTPS"
  set nat enable
 next
end
```

#### ۴) خطاهای ترجمه

- فرض «ACL ورودی روی Interface» ⇒ Policy باید جفت Interface باشد.
- فراموشی `nat enable`.
- انتظار `copy run start`.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترجمه | مفهومی نه خط‌به‌خط |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

| هدف | Cisco | FortiGate |
|---|---|---|
| Route | `show ip route` | `get router info routing-table all` |
| OSPF | `show ip ospf neighbor` | `get router info ospf neighbor` |
| BGP | `show ip bgp summary` | `get router info bgp summary` |

#### مثال متوسط — Ping با منبع

`execute ping-options source 10.10.0.1` سپس `execute ping x`.

#### مثال سخت — ترجمه‌ی مسئله

«مسیر 10.30.0.0/24 را از BGP یاد بگیر»: Cisco `network/neighbor`؛ FortiGate `config router bgp` و Route-map در صورت لزوم.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** `show ip route` ⇒ `get router info routing-table all`.

**متوسط (تفاوت):** ACL Cisco باید برگشت را هم مجاز کند (یا established)؛ Policy Fortinet برگشت را خودکار می‌پذیرد.

**سخت (ترجمه‌ی Config):** ACL 10 خطی را به Policy تبدیل: هر خط به یک یا چند Policy با Object؛ ادغام ردیف‌های مشابه؛ Log؛ آزمون با Lookup. ریسک: ترتیب و Implicit Deny.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get router info routing-table all
diagnose ip arp list
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- جدول تطبیق.
- آزمون Lookup.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ترافیک رد می‌شود | Policy جفت Interface | Zone/Interface |

### ۱۰) نکات امنیتی

- Default Deny در هر دو.

### ۱۱) جمع‌بندی مفهومی

- نگاشت+تفاوت.
- Stateless/Stateful.
- خودکار ذخیره.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) معادل show ip route؟ *(پاسخ: 25-1-ت1)*

**ت2.** (ساده) ACL در FortiGate؟ *(پاسخ: 25-1-ت2)*

**ت3.** (متوسط) تفاوت ذخیره؟ *(پاسخ: 25-1-ت3)*

**ت4.** (متوسط) برگشت ترافیک؟ *(پاسخ: 25-1-ت4)*

**ت5.** (سخت) ACL را به Policy ببرید. *(پاسخ: 25-1-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی تطبیق. *(پاسخ: 25-1-ت6)*

**Q1.** Quick quiz (English): What is the FortiGate equivalent of a Cisco ACL? *(پاسخ: 25-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ACL | Access Control List | فهرست کنترل دسترسی |

- *Do not translate configs line by line.* ← Config را خط‌به‌خط ترجمه نکنید.

### ۱۴) کارت Lab

**کارت Lab:** نگاشت Cisco–Fortinet (اجرا نشده). **Evidence:** `02-design/mapping-sheet.md`.

### ۱۵) منابع

- Cisco IOS docs
- Fortinet FortiOS 7.0 Administration Guide

<a id="l-25-2"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: برگه‌ی تطبیق

برای هر قابلیت: دستور Cisco، دستور FortiGate، دستور Verify هر دو، تفاوت رفتار. مثال: `show ip route` ↔ `get router info routing-table all`; `show ip ospf neighbor` ↔ `get router info ospf neighbor`.

**پرسش‌های مصاحبه**
1. *Verify معادل؟* جدول بالا.
2. *تفاوت Default؟* مثال Admin Distance.
3. *Syntax؟* config tree.

### مثال حل‌شده: ساخت برگه‌ی تطبیق برای OSPF

| هدف | Cisco | FortiGate |
|---|---|---|
| همسایه‌ها | `show ip ospf neighbor` | `get router info ospf neighbor` |
| جدول مسیر | `show ip route ospf` | `get router info routing-table ospf` |
| Interface | `show ip ospf interface` | `get router info ospf interface` |
| Cost | `ip ospf cost 10` | `set cost 10` در ospf-interface |

**مثال:** پیش‌فرض Reference Bandwidth در Cisco برابر 100 Mbps و در FortiGate هم 100 Mbps است؛ لینک 1 Gbps و 100 Mbps هر دو Cost=1 می‌شوند. در دو سر باید یک مقدار یکسان تنظیم شود.

``` text
Cost = Reference BW / Interface BW
100 Mbps / 1000 Mbps = 0.1 -> rounded to 1
```

**نکته:** پیش‌فرض‌های هر نسخه را در مستند رسمی همان نسخه بررسی کنید؛ این جدول «مفهومی» است.

### تکمیل عمیق: برگه‌ی تطبیق دستورها — ساخت و استفاده

#### چرا؟

از کار روزمره: یک نفر Cisco بلد است و باید با FortiGate تست کند. برگه‌ی تطبیق (Cheat Sheet) سرعت را چند برابر می‌کند.

#### برگه‌ی نمونه

| هدف | Cisco | FortiGate |
|---|---|---|
| نمایش Route | `show ip route` | `get router info routing-table all` |
| همسایه OSPF | `show ip ospf neighbor` | `get router info ospf neighbor` |
| همسایه BGP | `show ip bgp summary` | `get router info bgp summary` |
| جدول ARP | `show ip arp` | `get system arp` |
| وضعیت Interface | `show ip interface brief` | `get system interface` |
| Session | `show conn` (ASA) | `diagnose sys session list` |
| Debug بسته | `debug ip packet` | `diagnose debug flow` |
| Ping با منبع | `ping x source y` | `execute ping-options source y` + `execute ping x` |

دقت دستورها را از مستند همان نسخه تأیید کنید.

#### مثال ساده — Ping با منبع

``` text
execute ping-options source 10.10.0.1
execute ping 10.20.0.10
```

#### مثال متوسط — مقایسه‌ی Debug

Cisco `debug ip packet` ممکن است دستگاه را از پا بیندازد؛ در FortiGate `debug flow` با فیلتر محدود و `trace start 20` ایمن‌تر است. قانون: همیشه فیلتر و سقف تعداد.

#### مثال سخت — ترجمه‌ی یک مسئله‌ی کامل

مسئله: «مسیر 10.30.0.0/24 را از BGP یاد بگیر». ترجمه: Cisco `network` و `neighbor`؛ FortiGate `config router bgp ... config neighbor ... config network`. نکته: FortiGate پیش‌فرض Route-map ندارد و اگر Policy لازم است باید `route-map-in/out` بنویسید.

#### Lab

برگه‌ی ۲۰ ردیفی از دستورهای مورد استفاده‌ی خودتان با ستون «خروجی مورد انتظار».

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| دستور کار نمی‌کند | نسخه | مستند |
| خروجی متفاوت | قالب | مقایسه |
| Debug سنگین | بی‌فیلتر | فیلتر |

#### پرسش‌ها با پاسخ

**۱. چرا فیلتر در Debug؟** CPU.
**۲. برگه چه کمکی می‌کند؟** سرعت و دقت.
**۳. چرا ستون خروجی؟** تشخیص موفقیت.

#### English Corner

- *A cheat sheet maps tasks, not just commands.*
- Q: Why limit the scope of debug commands?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا پارامترهای OSPF/BGP؟** شکست Interop در همسایگی رخ می‌دهد: Area، Network Type، MTU، Hello/Dead، Authentication؛ و در BGP: ASN، update-source، Next-hop.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — OSPF ExStart

MTU دو سر را مقایسه کنید.

#### مثال متوسط — BGP Idle

TCP/179 و Local-in.

#### مثال سخت — Next-hop

مسیر یادگرفته ولی ترافیک نمی‌رود ⇒ `next-hop-self`.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: OSPF و BGP بین FGT و CSR

نقاط ناهمخوانی OSPF: Area، Network Type، MTU، Hello/Dead، Authentication. BGP: AS، Update-source، Next-hop، Route-map.

``` text
show ip ospf neighbor
get router info ospf neighbor
show ip bgp summary
get router info bgp summary
```

**پرسش‌های مصاحبه**
1. *گیر در ExStart؟* MTU.
2. *BGP Idle؟* TCP/179.
3. *Policy؟* Route-map دو سر.

### مثال حل‌شده: همسایگی OSPF گیر کرده در ExStart

**علامت:** `get router info ospf neighbor` وضعیت `ExStart` نشان می‌دهد.

**مراحل عیب‌یابی**
1. MTU دو Interface را مقایسه کنید.
2. سمت Cisco: `show ip ospf interface` و `show interface | include MTU`.
3. سمت FortiGate: `get system interface physical`.
4. اگر MTU متفاوت است: برابر کنید یا (موقت) `ip ospf mtu-ignore` در Cisco.

``` text
Cisco  Gi0/0 MTU 1500
FGT    port1 MTU 1496   (VLAN tag overhead)
=> DBD packet size mismatch -> stuck ExStart
```

**رفع:** هر دو سر 1500 یا 1496. **تأیید:** وضعیت `Full/DR`.

**مثال BGP:** Idle ⇒ `telnet 10.99.0.2 179` از فایروال؛ اگر باز نشد Policy/ACL پورت 179 را بررسی کنید و از Local-in Policy فایروال غافل نشوید.

### تکمیل عمیق: OSPF و BGP بین FortiGate و CSR — پارامترهای همسایگی

#### چرا؟

بیشتر شکست‌های Interop در همسایگی رخ می‌دهد؛ دو دستگاه باید روی پارامترها توافق کنند. ما باید بدانیم کدام پارامتر چرا مهم است.

#### OSPF — پارامترهای باید یکسان

| پارامتر | چرا |
|---|---|
| Area ID | همسایگی در یک Area |
| Hello/Dead | 10/40 پیش‌فرض Broadcast |
| Network Type | رفتار DR/BDR |
| MTU | DBD Exchange |
| Authentication | امنیت |
| Subnet Mask | همسایگی |

#### مثال ساده — وضعیت‌ها

``` text
Down -> Init -> 2-Way -> ExStart -> Exchange -> Loading -> Full
```

- گیر در Init: Hello یک‌طرفه (ACL/Policy).
- گیر در 2-Way: طبیعی بین DROther‌ها.
- گیر در ExStart: MTU یا Duplicate Router-ID.

#### مثال متوسط — حل ExStart

``` text
Cisco : show interface Gi0/0 | include MTU
FGT   : get system interface physical
```

MTU دو سر را برابر کنید یا (موقت) `ip ospf mtu-ignore`. تأیید: Full.

#### BGP — نقاط رایج

``` text
show ip bgp summary     (Cisco)
get router info bgp summary   (FGT)
```

State: Idle (TCP/179؟)، Active (تلاش)، OpenSent/Confirm (پارامتر)، Established (PfxRcd عدد). مثال: Idle ⇒ ping/ TCP 179 / Policy Local-in.

#### مثال سخت — Next-hop

پیشوند یاد گرفته شد ولی ترافیک نمی‌رود: Next-hop دست‌نیافتنی. راه: `next-hop-self` یا Route به Next-hop.

#### Lab

دو روتر (یک CSR و یک FortiGate VM) بسازید؛ OSPF را با MTU متفاوت گیر دهید و رفع کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| ExStart | MTU | یکسان‌سازی |
| Init | یک‌طرفه | Policy/ACL |
| BGP Idle | TCP179 | Local-in |

#### پرسش‌ها با پاسخ

**۱. چرا MTU در OSPF؟** DBD اندازه.
**۲. 2-Way طبیعی کجا؟** DROther.
**۳. BGP Idle؟** TCP برقرار نیست.

#### English Corner

- *OSPF neighbors must agree on area, timers and MTU.*
- Q: What does the BGP Idle state indicate?

## درس 25-3 — IPsec چندسازنده: روش مقایسه‌ی Debug، جدول مغایرت و Interop آزمایشی FGT–CSR

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۳، ۲۵-۱، ۲۵-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. پارامترهای دو سازنده را در جدول مغایرت (Mismatch) مقایسه کند.
2. Debug دو سمت را هم‌زمان بخواند و خط متناظر را بیابد.
3. تفاوت پیش‌فرض‌ها (DH، Lifetime، PFS، DPD) را بشناسد.
4. Interop آزمایشی را با Test Plan اجرا کند.
5. نتیجه را مستند و سازگاری را ارزیابی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا روش مقایسه‌ی Debug؟** بین دو سازنده «کار نمی‌کند» یعنی یک تفاوت کوچک. Debug هم‌زمان دو سر و جدول مغایرت آن را پیدا می‌کند.

**جمع‌بندی اصلی درس:**

وقتی دو دستگاه از دو سازنده IPsec می‌زنند، هر کدام «پیش‌فرض‌های» خودشان را دارند و Debug هرکدام به زبان خودش حرف می‌زند. مقایسه‌ی منظم دو سمت، سریع‌ترین راه برای پیدا کردن Mismatch است.

### ۳) توضیح عمیق فنی

#### ۱) جدول مغایرت

| پارامتر | FortiGate | Cisco CSR | بررسی |
|---|---|---|---|
| IKE version | `ike-version 2` | `crypto ikev2` | هر دو v2 |
| Encryption | `proposal aes256-sha256` | `encryption aes-cbc-256` | یکسان |
| Integrity | sha256 | `integrity sha256` | یکسان |
| DH | `dhgrp 14` | `group 14` | یکسان |
| PFS | `pfs enable` + dhgrp | `set pfs group14` | هر دو |
| Lifetime P1 | `keylife` 86400 | `lifetime 86400` | یکسان یا نزدیک |
| Selector | Subnet | ACL | آینه |
| DPD | `dpd on-idle` | `dpd 10 3 on-demand` | سازگار |
| NAT-T | enable | خودکار | UDP 4500 |

#### ۲) Debug دو سمت

| لحظه | FGT | CSR |
|---|---|---|
| شروع | `ike ... initiator: ... SA_INIT` | `IKEv2:Received Packet [From ...] ... IKE_SA_INIT` |
| پیشنهاد | `proposal ...` | `Proposal received` |
| خطا | `no suitable proposal` | `NO_PROPOSAL_CHOSEN` |

نکته: زمان هر دو با NTP هماهنگ باشد تا خطوط متناظر پیدا شوند.

#### ۳) Test Plan Interop

| # | آزمون | معیار |
|---|---|---|
| I-01 | Establish IKEv2 | SA ready |
| I-02 | ping LAN↔LAN | 0٪ Loss |
| I-03 | Rekey P1/P2 | بدون قطع > 1 s |
| I-04 | DPD: قطع یک سر | تشخیص < 60 s |
| I-05 | MTU/MSS | دانلود 100MB |
| I-06 | Failover (در صورت دو WAN) | بازگشت |

#### ۴) ارزیابی

اگر I-03 قطع طولانی: Lifetime/Rekey Margin. I-04 کند: DPD interval.

#### ۵) مستندسازی

برای هر Mismatch: شاهد (خط Debug هر دو سمت)، علت، رفع، تاریخ.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Test Plan | ۶ آزمون |
| Debug | همزمان |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

no proposal chosen ⇒ Proposal.

#### مثال متوسط

AUTH_FAILED ⇒ PSK/Identity.

#### مثال سخت — Lifetime

Tunnel پس از ساعاتی می‌افتد؛ Lifetime متفاوت و Rekey Collision.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Mismatch DH: FGT 14، CSR 5؛ شاهد در هر دو سمت؛ یکسان‌سازی.

**متوسط (Rekey):** پس از ۱ ساعت تونل ۸ ثانیه قطع شد. علت: Lifetime P2 در CSR 3600 و FGT 43200؛ Rekey نامتقارن. رفع: یکسان‌سازی؛ آزمون I-03.

**سخت (DPD):** قطع سر CSR؛ FGT تا ۵ دقیقه تونل را زنده می‌بیند. مراحل: DPD FGT on-idle با interval 10 و retry 3؛ CSR on-demand؛ آزمون: تشخیص ۳۰ ثانیه. درس: DPD دو سر.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose vpn ike gateway list
show crypto ikev2 sa
```

### ۸) Verification (اثبات صحت)

- I-01..I-06.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Rekey قطع | Lifetime | یکسان |

### ۱۰) نکات امنیتی

- PSK در Vault.

### ۱۱) جمع‌بندی مفهومی

- جدول مغایرت.
- Debug دو سمت.
- Test Plan.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Mismatch رایج؟ *(پاسخ: 25-3-ت1)*

**ت2.** (ساده) چرا NTP؟ *(پاسخ: 25-3-ت2)*

**ت3.** (متوسط) Rekey قطع؟ *(پاسخ: 25-3-ت3)*

**ت4.** (متوسط) DPD؟ *(پاسخ: 25-3-ت4)*

**ت5.** (سخت) DPD کند. *(پاسخ: 25-3-ت5)*

**ت6.** (سخت، طراحی) Test Plan. *(پاسخ: 25-3-ت6)*

**Q1.** Quick quiz (English): Why synchronize clocks when comparing debugs from two vendors? *(پاسخ: 25-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DPD | Dead Peer Detection | تشخیص همتای مرده |

- *Compare both sides with synchronized clocks.* ← دو سمت را با ساعت‌های هماهنگ مقایسه کنید.

### ۱۴) کارت Lab

**کارت Lab:** Interop FGT–CSR (اجرا نشده). **Evidence:** `03-ops/interop.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: IPsec
- Cisco IOS-XE IKEv2

<a id="l-25-4"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: IPsec چندسازنده

روش: Proposal یکسان، Selector یکسان، Lifetime، Identity؛ Debug دو سر در یک زمان. مقایسه: `diagnose vpn ike` و `debug crypto ikev2`.

**پرسش‌های مصاحبه**
1. *Lifetime ناهمخوان؟* Rekey ناهماهنگ.
2. *Identity؟* IP/FQDN.
3. *Selector؟* VTI در برابر ACL.

### مثال حل‌شده: Debug دوطرفه‌ی IKEv2

**فرض:** Tunnel بین FortiGate (203.0.113.2) و CSR (198.51.100.2) بالا نمی‌آید.

``` text
FGT: diagnose debug application ike -1 ; diagnose debug enable
CSR: debug crypto ikev2 ; debug crypto ikev2 error
```

**تفسیر نمونه**
- FGT: `no proposal chosen` ⇒ Proposal ناهمخوان.
- CSR: `Failed to find a matching policy` ⇒ هم‌علت.

**مقایسه‌ی پارامترها**

| پارامتر | FGT | CSR |
|---|---|---|
| Encryption | aes256 | aes-cbc-128 |
| DH | 14 | 14 |

علت: AES256 در برابر AES128. با یکسان‌سازی، `show crypto ikev2 sa` وضعیت READY.

پس از تأیید دیباگ را خاموش کنید: `undebug all` و `diagnose debug disable`.

### تکمیل عمیق: IPsec چندسازنده — روش مقایسه‌ی Debug

#### چرا؟

در IPsec بین دو سازنده، «کار نمی‌کند» معمولاً یعنی یک تفاوت کوچک در پارامترها؛ ولی کدام؟ روش مقایسه‌ی سیستماتیک جواب می‌دهد.

#### جدول مقایسه‌ی پارامتر

| پارامتر | FortiGate | Cisco CSR |
|---|---|---|
| IKE نسخه | `ike-version 2` | `crypto ikev2` |
| رمز | `proposal aes256-sha256` | `encryption aes-cbc-256` + `integrity sha256` |
| DH | `dhgrp 14` | `group 14` |
| Lifetime | `keylife` | `lifetime` |
| Identity | `localid` | `identity local` |
| Selector | Phase2 selector | Tunnel/ACL |

#### مثال ساده — Debug دو سر هم‌زمان

``` text
FGT: diagnose debug application ike -1 ; diagnose debug enable
CSR: debug crypto ikev2 ; debug crypto ikev2 error
```

#### مثال متوسط — تفسیر

- FGT: `no proposal chosen`، CSR: `Failed to find a matching policy` ⇒ Proposal ناهمخوان.
- AUTH_FAILED ⇒ PSK/Identity.
- TS_UNACCEPTABLE ⇒ Selector.

#### مثال سخت — شکست پس از چند ساعت

Tunnel بالا می‌آید و بعد از 8 ساعت قطع می‌شود: Lifetime متفاوت و Rekey ناهماهنگ (FGT 28800، CSR 86400). رفع: یکسان‌سازی؛ در IKEv2 هر طرف مستقل Rekey می‌کند ولی Collision ممکن است.

``` text
sh crypto ikev2 sa ; sh crypto ipsec sa
diagnose vpn tunnel list
```

کانترها: `encaps/decaps` در Cisco و `enc/dec pkts` در FGT باید با هم افزایش یابند.

#### Lab

یک Tunnel را عمداً با Proposal متفاوت بسازید و Debug هر دو سر را تفسیر کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| no proposal chosen | رمز | یکسان |
| AUTH_FAILED | PSK | یکسان |
| TS_UNACCEPTABLE | Selector | یکسان |

#### پرسش‌ها با پاسخ

**۱. چرا Debug دو سر؟** دیدن هر دو دید.
**۲. Collision Rekey؟** هم‌زمانی.
**۳. کانتر چه می‌گوید؟** عبور ترافیک.

#### English Corner

- *Debug both peers at the same time and compare.*
- Q: What does TS_UNACCEPTABLE point to?

## درس 25-4 — آزمون معماری ۶ (FGT+CSR): IPsec چندسازنده، مقایسه‌ی Debug و جدول مغایرت — کلید پاسخ و Rubric

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۱ تا ۲۵-۳ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. تونل IKEv2 بین FortiGate و Cisco CSR1000v را طراحی کند.
2. پارامترهای معادل (Proposal، DH، PFS، Lifetime، Selector) را جدول‌بندی کند.
3. Debug هر دو سمت را مقایسه و Mismatch را بیابد.
4. سه خرابی تزریق‌شده را رفع کند.
5. گزارش و Rubric تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا آزمون معماری ۶؟** نشان می‌دهد می‌توانید دو سازنده را کنار هم راه بیندازید و ثابت کنید.

**جمع‌بندی اصلی درس:**

در دنیای واقعی طرف مقابل تونل همیشه Fortinet نیست. اشتباه رایج: فرض اینکه «همه IPsec هستند». ولی نام پارامترها، پیش‌فرض‌ها و Selector (Cisco با ACL، Fortinet با Subnet) متفاوت است. این آزمون مهارت مقایسه‌ی دو CLI را می‌سنجد.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

FGT (198.51.100.2، LAN 10.10.0.0/16) و CSR1000v (203.0.113.2، LAN 10.20.0.0/16). IKEv2، AES-256، SHA-256، DH 14، PFS DH 14، Lifetime P1 86400، P2 3600.

#### ۲) جدول معادل

| مفهوم | FortiGate | Cisco CSR |
|---|---|---|
| Proposal P1 | `set proposal aes256-sha256` | `crypto ikev2 proposal P1 ; encryption aes-cbc-256 ; integrity sha256 ; group 14` |
| Auth | `psksecret` | `crypto ikev2 keyring` |
| Selector | `src-subnet/dst-subnet` | ACL (`access-list` crypto) |
| P2 | `phase2-interface` | `crypto ipsec transform-set esp-aes 256 esp-sha256-hmac` |
| PFS | `set pfs enable` | `set pfs group14` |
| Lifetime | `keylife` | `lifetime` |

#### ۳) CSR نمونه

``` text
crypto ikev2 proposal P1
 encryption aes-cbc-256
 integrity sha256
 group 14
crypto ikev2 policy POL1
 proposal P1
crypto ikev2 keyring KR
 peer FGT
  address 198.51.100.2
  pre-shared-key <FROM-VAULT>
crypto ikev2 profile PROF
 match identity remote address 198.51.100.2 255.255.255.255
 authentication remote pre-share
 authentication local pre-share
 keyring local KR
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac
 mode tunnel
ip access-list extended VPN-ACL
 permit ip 10.20.0.0 0.0.255.255 10.10.0.0 0.0.255.255
crypto map CM 10 ipsec-isakmp
 set peer 198.51.100.2
 set transform-set TS
 set pfs group14
 set ikev2-profile PROF
 match address VPN-ACL
interface GigabitEthernet1
 crypto map CM
```

(`Unverified` در IOS-XE 17.03؛ نام دستورها را با help بررسی.)

نکته (مستند Cisco): نمونه‌ی بالا روش **Crypto-map (Policy-based)** است که در راهنمای IKEv2/FlexVPN به‌عنوان حالت Legacy آمده. روش Route-based مدرن: `crypto ipsec profile` با `set ikev2-profile` و اعمال آن روی Interface Tunnel با `tunnel protection ipsec profile ...` (سازگار با FortiGate Route-based).

#### ۴) خرابی‌ها و کلید

**A:** DH گروه 14 در FGT و 5 در CSR (پیش‌فرض). شاهد CSR: `debug crypto ikev2` NO_PROPOSAL؛ FGT: `no proposal chosen`. رفع: `group 14`.

**B:** Selector نامتقارن: ACL /24 و FGT /16. شاهد: P2 down. رفع: ACL و Selector یکسان.

**C:** Lifetime متفاوت؛ rekey با Flap کوتاه. رفع: یکسان یا Lifetime کوچک‌تر ابتکار.

#### ۵) Verification

``` text
FGT: diagnose vpn ike gateway list ; diagnose vpn tunnel list
CSR: show crypto ikev2 sa ; show crypto ipsec sa
```

#### ۶) Rubric

طراحی جدول ۲۰، پیکربندی ۲۵، تشخیص ۳ خرابی ۳۰، Verify دوطرفه ۱۵، Evidence و صداقت ۱۰. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| IKE | v2 |
| Selector | آینه‌ی دقیق |
| مقایسه Debug | هر دو سمت همزمان |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

IPsec برقرار + OSPF Full.

#### مثال متوسط

Network Type ناهمخوان ⇒ P2P.

#### مثال سخت

MSS Clamp. Rubric: نگاشت ۲۵، IPsec ۲۵، Routing ۲۵، Evidence ۱۵، گزارش ۱۰.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** جدول معادل: Proposal FGT=aes256-sha256؛ CSR=aes-cbc-256+sha256+group14؛ برابر.

**متوسط (خرابی A):** DH متفاوت: FGT group14، CSR پیش‌فرض group5. شاهد در هر دو سمت NO_PROPOSAL. با `group 14` تونل up و `show crypto ikev2 sa` READY.

**سخت (Selector):** P1 up ولی ping نه. مراحل: ۱) `diagnose vpn tunnel list` SA صفر. ۲) CSR: `show crypto ipsec sa` بدون SA. ۳) ACL /24 ≠ /16. ۴) یکسان‌سازی. ۵) ping ok. درس: Selector باید آینه‌ی دقیق باشد.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose vpn ike gateway list
diagnose vpn tunnel list
show crypto ikev2 sa
show crypto ipsec sa
```

### ۸) Verification (اثبات صحت)

- P1 و P2 در هر دو سمت up.
- ping بین LANها.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| NO_PROPOSAL | DH/Proposal | group |
| P2 down | Selector/ACL | آینه‌ی دقیق |

### ۱۰) نکات امنیتی

- PSK در Vault.

### ۱۱) جمع‌بندی مفهومی

- جدول معادل.
- Selector آینه.
- Debug دو سمت.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Selector در Cisco چیست؟ *(پاسخ: 25-4-ت1)*

**ت2.** (ساده) DH گروه 14 یعنی؟ *(پاسخ: 25-4-ت2)*

**ت3.** (متوسط) P1 up و P2 down؛ علت؟ *(پاسخ: 25-4-ت3)*

**ت4.** (متوسط) Debug کجا؟ *(پاسخ: 25-4-ت4)*

**ت5.** (سخت) rekey Flap. *(پاسخ: 25-4-ت5)*

**ت6.** (سخت، طراحی) جدول معادل. *(پاسخ: 25-4-ت6)*

**Q1.** Quick quiz (English): Why must crypto ACL and FortiGate selectors mirror each other? *(پاسخ: 25-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DH | Diffie-Hellman | تبادل کلید |

- *Compare both sides debug output.* ← خروجی Debug دو سمت را مقایسه کنید.

### ۱۴) کارت Lab

**کارت Lab:** معماری ۶ (اجرا نشده). **Evidence:** `03-ops/arch6.md`.

### ۱۵) منابع

- Cisco IOS-XE IKEv2 guide
- Fortinet FortiOS 7.0 Administration Guide: IPsec

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Rubric معماری ۶

نگاشت ۲۵، IPsec ۲۵، Routing ۲۵، Evidence ۱۵، گزارش ۱۰.

**پرسش‌های مصاحبه**
1. *Evidence؟* خروجی دو سر.
2. *آزمون؟* Ping دوطرفه.
3. *ثبت؟* تفاوت‌ها.

### مثال حل‌شده: ارزیابی یک تحویل معماری ۶

برای یک تیم که Tunnel، OSPF و NAT را بین FGT و CSR تحویل داده:

| معیار | وزن | شاهد لازم |
|---|---|---|
| IPsec برقرار | 25 | `diagnose vpn tunnel list`، `show crypto ikev2 sa` |
| OSPF Full | 25 | خروجی هر دو سر |
| نگاشت درست مفاهیم | 25 | جدول تطبیق |
| آزمون منفی | 15 | رد ترافیک غیرمجاز |
| گزارش | 10 | RCA/محدودیت‌ها |

**نمره‌گذاری:** اگر IPsec برقرار ولی آزمون منفی ندارد: 25+25+25+0+10 = 85 از 100؛ ایراد باید در بازخورد ذکر شود.

### تکمیل عمیق: ارزیابی معماری ۶ — حل کامل و Rubric

#### چرا؟

این آزمون نشان می‌دهد می‌توانید دو سازنده را با هم کار بیندازید و ثابت کنید.

#### صورت مسئله

بین FortiGate (HQ) و CSR (Branch): IPsec IKEv2، OSPF روی Tunnel، یک Policy اینترنت و NAT. مدارک: تنظیمات، شواهد، آزمون منفی، گزارش.

#### کلید پاسخ

1. **نگاشت**: جدول مفاهیم.
2. **IPsec**: `diagnose vpn tunnel list`، `show crypto ikev2 sa`.
3. **OSPF**: Full در دو سر.
4. **NAT**: یک نقطه.
5. **آزمون منفی**: Branch→Mgmt رد.
6. **گزارش**: محدودیت‌ها.

#### محاسبه‌ی نمره

``` text
Mapping 25 | IPsec 25 | Routing 25 | Evidence 15 | Report 10
Example: 22 + 25 + 20 + 12 + 8 = 87
```

#### مثال متوسط — خطای رایج

دانشجو OSPF را روی Tunnel با Network Type متفاوت (P2P در Cisco و Broadcast در FGT) تنظیم کرد؛ همسایگی بالا رفت ولی DR انتخاب‌شد و پایدار نبود. شاهد: `get router info ospf interface`. رفع: Point-to-Point هر دو.

#### مثال سخت — اختلاف MSS

پس از Tunnel، HTTPS کند است. MSS Clamp 1360 روی Policy؛ مقایسه‌ی قبل و بعد با iperf.

#### Lab

آزمون را کامل اجرا و Evidence Index بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| OSPF ناپایدار | Network Type | یکسان |
| HTTPS کند | MTU | MSS |
| Tunnel Up بدون ترافیک | Policy/Route | بررسی |

#### پرسش‌ها با پاسخ

**۱. چرا P2P روی Tunnel؟** بدون DR.
**۲. MSS Clamp؟** جلوگیری از Fragmentation.
**۳. Evidence چیست؟** خروجی دو سر.

#### English Corner

- *Use point-to-point network type on tunnel interfaces.*
- Q: Why is MSS clamping useful over IPsec?

## پاسخ‌های فصل 25

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی درس 25-1


### پاسخ‌های بازنویسی عمیق درس 25-1

**25-1-ت1** — get router info routing-table all.

معادل `show ip route`: `get router info routing-table all`.

**25-1-ت2** — Firewall Policy.

ACL در FortiGate: Firewall Policy.

**25-1-ت3** — Cisco دستی؛ Fortinet خودکار.

Cisco Config را دستی ذخیره می‌کند؛ FortiOS تغییرات را خودکار ذخیره می‌کند.

**25-1-ت4** — Fortinet Stateful.

FortiGate Stateful است و برگشت ترافیک را خودکار می‌پذیرد؛ ACL ساده Stateless.

**25-1-ت5** — Object، Policy، Log.

ACL را به Policy ببرید: Object، Policy، Log و آزمون Lookup.

**25-1-ت6** — جدول.

برگه‌ی تطبیق: ستون مفهوم، Cisco، FortiGate و نکته‌ی تفاوت.

**25-1-Q1** — A firewall policy.

### پاسخ‌های بازنویسی عمیق درس 25-2

**25-2-ت1** — معمولاً MTU متفاوت؛ DBD بزرگ‌تر از MTU همتا کنار گذاشته می‌شود.

**25-2-ت2** — eBGP = 20 و OSPF = 110؛ پس BGP برنده است.

eBGP با AD 20 بر OSPF با 110 برنده می‌شود.

**25-2-ت3** — CSR: `show ip ospf neighbor`؛ FGT: `get router info ospf neighbor`.

**25-2-ت4** — تا Prefix دوباره به منبعش بازگردانده نشود؛ از Loop و Flap جلوگیری می‌کند.

**25-2-ت5** — Loop Redistribution؛ افزودن Tag/Route-map، حذف Redistribute یک‌جهته در صورت نیاز؛ آزمون قطع/بازگشت.

**25-2-ت6** — جدول: IP/MTU/Area/Network Type/Auth/Timer/BGP AS/Filter برای هر Link.

**25-2-Q1** — Because routes can be redistributed back into their source protocol repeatedly.


### پاسخ‌های بازنویسی عمیق درس 25-3


### پاسخ‌های بازنویسی عمیق درس 25-3

**25-3-ت1** — DH، Selector، Lifetime.

Mismatch رایج: DH، Selector و Lifetime.

**25-3-ت2** — تطبیق خطوط Debug.

NTP تا خطوط Debug دو سازنده قابل‌تطبیق باشند.

**25-3-ت3** — Lifetime نامتقارن.

Rekey قطع: Lifetime نامتقارن؛ یکسان کنید.

**25-3-ت4** — تشخیص همتای مرده.

DPD همتای مرده را تشخیص می‌دهد و SA را پاک می‌کند.

**25-3-ت5** — interval/retry دو سر.

DPD کند: interval/retry را در دو سر هماهنگ کنید.

**25-3-ت6** — جدول.

Test Plan شش آزمون: Establish، ping، Rekey، DPD، MTU/MSS، Failover.

**25-3-Q1** — To match corresponding events across both logs.

### پاسخ‌های بازنویسی عمیق درس 25-4


### پاسخ‌های بازنویسی عمیق درس 25-4

**25-4-ت1** — ACL crypto.

Selector در Cisco ACL crypto است.

**25-4-ت2** — ۲۰۴۸ بیت MODP.

DH گروه 14 همان MODP 2048 بیت است.

**25-4-ت3** — Selector/PFS/Transform.

P1 up و P2 down: Selector، PFS یا Transform Set.

**25-4-ت4** — هر دو سمت.

Debug را در هر دو سمت هم‌زمان بگیرید.

**25-4-ت5** — Lifetime.

Rekey Flap: Lifetime را یکسان کنید.

**25-4-ت6** — طبق جدول.

جدول معادل Proposal، Auth، Selector، P2، PFS و Lifetime برای FGT و CSR.

**25-4-Q1** — Because mismatched selectors prevent phase 2 from negotiating.

### پاسخ‌های درس افزوده‌ی 25-0 (فصل 25)

**25-0-ت1** — get router info routing-table all.

`show ip route` ↔ `get router info routing-table all`.

**25-0-ت2** — اغلب MTU Mismatch بین دو سر.

اغلب MTU Mismatch بین دو سر (مثلاً در OSPF) علت گیرکردن است.

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا مدیریت مرکزی؟** با ۳ فایروال دستی ممکن است؛ با ۳۰ یک تغییر ساده ۳۰ بار ورود و ۳۰ فرصت خطا. FortiManager پیکربندی و FortiAnalyzer Log را مرکزی می‌کند (هر دو Needs-License). جایگزین بدون لایسنس: Git + rsyslog.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

≤5 دستگاه: Git+rsyslog؛ بیشتر: ارزیابی FMG/FAZ.

#### مثال متوسط — Policy Package

یک Package برای ۱۰ شعبه.

#### مثال سخت — ADOM

جداسازی مشتریان/بخش‌ها.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: چه زمانی FMG/FAZ؟

معیار: بیش از ~۵ دستگاه، نیاز به Policy Package یکسان (FMG) یا Log متمرکز و گزارش (FAZ). هر دو Needs-License.

**ADOM:** جداسازی دامنه‌ی مدیریتی.

**پرسش‌های مصاحبه**
1. *بدون FMG؟* Git/Ansible.
2. *FAZ جایگزین؟* rsyslog/SIEM.
3. *Install Target؟* انتشار Policy.

### مثال حل‌شده: تصمیم FortiManager/FortiAnalyzer یا جایگزین

**شرایط:** ۱۲ فایروال، تیم ۴ نفره، بودجه محدود.

| نیاز | راهکار بدون لایسنس | راهکار Fortinet |
|---|---|---|
| Policy یکسان در ۱۲ دستگاه | قالب Config + Git/Ansible | FortiManager (Needs-License) |
| Log متمرکز | rsyslog/Graylog | FortiAnalyzer (Needs-License) |
| گزارش آماده | SIEM | FAZ Reports |

**تصمیم نمونه:** Log با rsyslog+Graylog، Backup با Git، و ارزیابی FMG وقتی تعداد دستگاه از ۲۰ گذشت یا ممیزی Policy Package لازم شد. هر عدد آستانه در جلسه‌ی خودتان تعیین شود؛ این فقط نمونه است.

### تکمیل عمیق: مدیریت مرکزی — از ۳ دستگاه تا ۳۰ دستگاه

#### چرا باید یاد بگیریم؟

با ۳ فایروال می‌توانید هر کدام را جداگانه مدیریت کنید. با ۳۰ فایروال، یک تغییر ساده (مثلاً افزودن یک Address) یعنی ۳۰ بار ورود، ۳۰ بار خطای احتمالی و ۳۰ مغایرت پنهان. مدیریت مرکزی سه مسئله را حل می‌کند: **یکنواختی** (همه یک Policy)، **دیده‌شدن** (Log یک‌جا) و **کنترل تغییر** (چه کسی چه کرد).

#### توضیح ساده

دو نقش جدا:

- **FortiManager (FMG)**: مدیریت پیکربندی؛ Policy Package، Device Manager، Script.
- **FortiAnalyzer (FAZ)**: مدیریت Log و گزارش؛ جمع‌آوری، جستجو، Event Handler.

هر دو Needs-License و به‌صورت VM یا سخت‌افزار عرضه می‌شوند؛ در این دوره بدون لایسنس نمی‌توان اجرا شان کرد، پس با جایگزین‌های متن‌باز مفهوم را تمرین می‌کنیم.

#### مثال ساده — تصمیم با عدد

| تعداد دستگاه | نیاز | تصمیم پیشنهادی |
|---|---|---|
| ≤ 5 | کم | Git + rsyslog |
| 6–20 | متوسط | ارزیابی FMG/FAZ |
| > 20 | زیاد | FMG/FAZ توجیه‌پذیر |

اعداد آستانه نمونه‌اند؛ هر سازمان بر اساس هزینه‌ی خطای انسانی تصمیم می‌گیرد.

#### مثال متوسط — Policy Package

یک Package «Branch-Standard» شامل Policyهای Users→Internet و Guest. با Install روی ۱۰ شعبه، همه‌ی آنها دقیقاً یکی می‌شوند. Objectهای خاص هر شعبه (مثل IP محلی) با **Metadata Variable/Normalized Interface** جدا می‌شوند.

#### مثال سخت — ADOM و جداسازی

ADOM = Administrative Domain، یعنی «دامنه‌ی مدیریتی». شرکت A و B هر کدام یک ADOM با Policy و Log جدا؛ ادمین A به Log B دسترسی ندارد. از ADOM برای مشتریان MSSP یا بخش‌های بزرگ سازمان استفاده می‌شود.

#### ریسک مدیریت مرکزی

نقطه‌ی مرکزی هدف جذاب مهاجم است؛ Hardening، شبکه‌ی Mgmt جدا، MFA و Backup خود FMG الزامی است.

#### Lab (بدون لایسنس)

یک ساختار Git با Config چند دستگاه بسازید و تغییر یک Address را به همه با اسکریپت اعمال کنید (روی Lab)؛ مزایا/معایب نسبت به FMG را بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Install ناموفق | Object ناهمخوان | Policy Check |
| Device Out-of-sync | تغییر محلی | Retrieve/Re-install |
| FGFM قطع | پورت 541 | بررسی مسیر |

#### پرسش‌ها با پاسخ

**۱. تفاوت FMG و FAZ؟** پیکربندی در برابر Log.
**۲. ADOM چیست؟** دامنه‌ی مدیریتی جدا.
**۳. چرا HA برای FMG؟** نقطه‌ی مرکزی.

#### English Corner

- *Centralized management reduces drift between devices.*
- Q: What is the difference between FortiManager and FortiAnalyzer?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا نقش‌ها و ظرفیت؟** قبل از طراحی باید ظرفیت لازم را بدانید.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

``` text
2 GB/day x 12 x 90 = 2160 GB
```

#### مثال متوسط

سقف GB/Day و کاهش Log.

#### مثال سخت

Revision و Script انبوه با آزمون روی یک دستگاه.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: نقش‌ها

FMG: Config، Policy Package، Device Manager. FAZ: Log، گزارش، Event Handler. ارتباط FGFM (TCP/541). **لایسنس/ظرفیت** بر اساس تعداد دستگاه و GB/Day.

**پرسش‌های مصاحبه**
1. *Revision؟* نسخه‌ی تغییرات.
2. *Script؟* تغییر انبوه.
3. *HA؟* دو FMG.

### مثال حل‌شده: ظرفیت FortiAnalyzer

``` text
Log per device = 2 GB/day
Devices        = 12
Retention      = 90 days
Total          = 2 x 12 x 90 = 2160 GB ~ 2.1 TB
With 30% headroom ~ 2.8 TB
```

مراحل: ۱) حجم روزانه را از `diagnose log device` یا مانیتور واقعی بگیرید؛ ۲) ضرب در دستگاه و روز؛ ۳) حاشیه‌ی ظرفیت؛ ۴) لایسنس بر اساس GB/Day مطابق مستند.

ADOM: برای جداسازی مشتریان/محیط‌ها، هر ADOM Policy و Log جدا.

### تکمیل عمیق: FMG/FAZ — معماری، ظرفیت و لایسنس

#### چرا؟

قبل از خرید یا طراحی باید بدانید چه ظرفیتی لازم است. خطای ظرفیت یعنی Log از دست‌رفته یا هزینه‌ی اضافی.

#### ارتباط‌ها

``` text
FortiGate  <--FGFM TCP/541-->  FortiManager (config)
FortiGate  --OFTP TCP/514-->   FortiAnalyzer (logs)
```

نام پورت‌ها را از مستند همان نسخه تأیید کنید.

#### مثال ساده — ظرفیت

``` text
Log per device = 2 GB/day
Devices        = 12
Retention      = 90 days
Total          = 2 x 12 x 90 = 2160 GB ~ 2.1 TB
With 30% headroom ~ 2.8 TB
```

#### مثال متوسط — GB/Day لایسنس

لایسنس FAZ معمولاً بر پایه‌ی حجم Log روزانه است. اگر روزانه 24 GB تولید می‌شود ولی لایسنس 10 GB/Day است، Log اضافه کنار گذاشته یا رد می‌شود. پس باید Log غیرضروری را (مثلاً Traffic Allow برای Policyهای کم‌اهمیت) کاهش دهید.

#### مثال سخت — طراحی Log

``` text
Policy Internet : log utm only
Policy DMZ-in   : log all
Deny final      : log all
Result          : daily volume drops ~40%, key evidence kept
```

#### Revision و Script

FMG هر تغییر را Revision می‌کند؛ می‌توانید برگردید. Script انبوه برای تغییر یکباره‌ی چندین دستگاه (با آزمون روی یک دستگاه ابتدا).

#### Lab

ظرفیت را برای سناریوی خودتان با جدول محاسبه کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Log رد می‌شود | سقف GB/Day | کاهش Log |
| دیسک پر | Retention | تنظیم |
| FGFM نمی‌رسد | Route/پورت | بررسی |

#### پرسش‌ها با پاسخ

**۱. چرا Headroom؟** رشد.
**۲. Revision چه فایده‌ای؟** بازگشت.
**۳. چرا Script ابتدا روی یکی؟** ریسک.

#### English Corner

- *Size log storage as volume times retention plus headroom.*
- Q: What happens when the daily log quota is exceeded?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Syslog مرکزی؟** اگر بودجه‌ی FAZ نیست، rsyslog پایه‌ی SIEM است.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

``` text
config log syslogd setting
 set status enable
 set server 10.50.0.20
 set mode reliable
end
```

#### مثال متوسط

`tcpdump -ni eth0 tcp port 514`.

#### مثال سخت

Source IP/Route/فایروال سرور.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Syslog مرکزی

``` text
config log syslogd setting
 set status enable
 set server 10.50.0.20
 set mode reliable
 set port 514
 set format default
end
```

در rsyslog: `module(load="imtcp") input(type="imtcp" port="514")`. تأیید: `logger` و رسیدن Log.

**پرسش‌های مصاحبه**
1. *UDP/TCP؟* Reliable بهتر.
2. *TLS؟* حفاظت.
3. *Retention؟* سیاست.

### مثال حل‌شده: Syslog TCP تا رسیدن Log

``` text
FGT: config log syslogd setting ; set status enable ; set server 10.50.0.20 ; set mode reliable ; end
Srv: sudo tcpdump -ni eth0 tcp port 514 -c 5
Srv: tail -f /var/log/fgt/*.log
```

**اگر Log نرسید:** ۱) Route/Policy از Mgmt به سرور ۲) پورت 514 روی سرور (`ss -ltn`) ۳) Firewall سرور ۴) Source Interface (`set source-ip`).

**تست دستی از FGT:** با رویداد تغییر Config یا ورود ادمین یک Log ایجاد و رسیدن آن را بررسی کنید.

### تکمیل عمیق: Syslog مرکزی با rsyslog — از FortiGate تا فایل

#### چرا؟

اگر بودجه‌ی FAZ ندارید، یک سرور لینوکس با rsyslog همان کار جمع‌آوری Log را می‌کند و پایه‌ی SIEM هم می‌شود.

#### گام‌ها

1. سرور Syslog: TCP/514 باز.
2. فایروال سرور: فقط IP فایروال‌ها.
3. FortiGate: ارسال با `mode reliable`.
4. تأیید دریافت.
5. چرخش (Rotation) و نگهداری.

#### مثال ساده — سمت سرور

``` text
# /etc/rsyslog.d/10-fgt.conf
module(load="imtcp")
input(type="imtcp" port="514")
template(name="fgt" type="string" string="/var/log/fgt/%fromhost-ip%/%$YEAR%-%$MONTH%-%$DAY%.log")
*.* ?fgt
```

#### مثال متوسط — سمت FortiGate

``` text
config log syslogd setting
 set status enable
 set server 10.50.0.20
 set mode reliable
 set port 514
 set source-ip 10.50.0.1
end
```

تأیید: `tcpdump -ni eth0 tcp port 514 -c 5` روی سرور؛ سپس `tail -f /var/log/fgt/10.50.0.1/*.log`.

#### مثال سخت — Log نمی‌رسد

روش ده‌گامی کوتاه: ۱) Route فایروال به سرور ۲) Policy/Local-out ۳) پورت در `ss -ltn` ۴) فایروال سرور ۵) `source-ip` ۶) TLS (اگر فعال).

#### Rotation

``` text
# /etc/logrotate.d/fgt
/var/log/fgt/*/*.log { daily rotate 90 compress missingok notifempty }
```

#### Lab

یک VM لینوکس با rsyslog بسازید، Log بفرستید و Rotation را تست کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| فایل ساخته نمی‌شود | مجوز | دسترسی پوشه |
| فقط UDP | حالت پیش‌فرض | `reliable` |
| دیسک پر | Rotation | logrotate |

#### پرسش‌ها با پاسخ

**۱. چرا TCP؟** تحویل مطمئن.
**۲. چرا Rotation؟** دیسک.
**۳. TLS Syslog؟** حفاظت محتوا.

#### English Corner

- *Use reliable (TCP) syslog for security logs.*
- Q: How do you confirm logs are arriving?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Git برای Config؟** ردپای تغییرات رایگان؛ ولی Secret نباید به ریپو برود.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — Sanitize

`sed -E 's/(psk|password|secret) .*/\1 REDACTED/'`.

#### مثال متوسط — Diff

`git diff HEAD~1`.

#### مثال سخت

Secret لو رفت: Rotate نه فقط حذف.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Backup با Git

Sanitize: حذف `ENC` و Secret؛ Diff هفتگی.

``` text
execute backup config ftp cfg.conf 10.50.0.30 user ***
git add -A && git commit -m "daily"
git diff HEAD~1 -- cfg.conf
```

هرگز Secret در ریپو.

**پرسش‌های مصاحبه**
1. *Sanitize؟* حذف رمز.
2. *Diff؟* تغییر ناخواسته.
3. *Restore آزمون؟* دوره‌ای.

### مثال حل‌شده: Diff هفتگی Config

``` text
sed -E 's/(set (psk|password|secret) ).*/\1REDACTED/' cfg.conf > cfg.clean
git add cfg.clean && git commit -m weekly
git diff HEAD~1 -- cfg.clean | head -30
```

تفسیر: خطوط `+` افزوده‌شده، `-` حذف‌شده. اگر Policy جدیدی بدون Change Ticket دیدید ⇒ تغییر خارج از فرایند؛ بررسی Log Admin.

**هشدار:** `ENC` هم Secret است؛ فایل Sanitize نشده را در ریپو قرار ندهید.

### تکمیل عمیق: Backup خودکار، Diff و Git بدون نشت Secret

#### چرا؟

تغییر Config بدون ردپا یعنی نمی‌دانید دیشب چه شد. Git + Backup خودکار تاریخچه‌ی تغییرات را رایگان می‌دهد؛ ولی اگر Secret به ریپو برود، فاجعه است.

#### جریان

``` text
Backup -> Sanitize secrets -> Commit -> Diff -> Alert on unexpected change
```

#### مثال ساده — Sanitize

``` text
sed -E 's/(set (psk|password|secret|passwd) ).*/\1REDACTED/; s/ENC [^ ]+/ENC REDACTED/' cfg.conf > cfg.clean
```

هشدار: `ENC` هم یک Secret رمزنگاری‌شده است؛ در ریپوی عمومی/مشترک نگذارید.

#### مثال متوسط — Commit و Diff

``` text
git add cfg.clean && git commit -m "daily backup"
git diff HEAD~1 -- cfg.clean | head -40
```

خطوط `+` افزوده‌شده، `-` حذف‌شده. تغییر بدون CHG ⇒ بررسی.

#### مثال سخت — اتوماسیون

Cron روزانه: Backup با SCP، Sanitize، Commit، و اگر Diff غیرخالی بود ایمیل به Owner.

``` text
0 2 * * * /opt/fgt/backup.sh >> /var/log/fgt-backup.log 2>&1
```

اسکریپت باید خطا را گزارش کند (Exit Code) و Hash را ثبت.

#### Restore آزمایشی

ماهانه یک Config را در Lab Restore کنید و Policy/Route را مقایسه کنید.

#### Lab

یک ریپوی خصوصی محلی بسازید، سه نسخه‌ی Config با تغییر را Commit و Diff را تحلیل کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Secret در Git | Sanitize ناقص | حذف از تاریخچه + تغییر رمز |
| Diff خیلی بزرگ | ترتیب تصادفی | ثابت‌کردن خروجی |
| Backup خالی | دسترسی | بررسی |

#### پرسش‌ها با پاسخ

**۱. اگر Secret به Git رفت؟** آن را چرخش (Rotate) کنید، نه فقط حذف.
**۲. چرا Diff؟** تغییر ناخواسته.
**۳. Restore چرا آزمایشی؟** اعتبار Backup.

#### English Corner

- *Never commit secrets; rotate any that leak.*
- Q: What does an unexpected diff indicate?

## درس 26-4 — طراحی معماری ۹ (مدیریت مرکزی و عملیات): RBAC، Change، Audit و آزمون با Rubric

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۱ تا ۲۶-۳، ۳۲-۱ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری مدیریت مرکزی (FortiManager، FortiAnalyzer، ADOM) را طراحی کند.
2. RBAC چندسطحی (Super، Network، ReadOnly، Auditor) را مدل کند.
3. فرایند Change از طریق Policy Package و Revision را بنویسد.
4. Audit و Alert روی تغییر Config را طراحی کند.
5. آزمون و Rubric را تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا معماری عملیات؟** RBAC، Out-of-band، Audit: هر کس فقط کار لازم.

**جمع‌بندی اصلی درس:**

با ۲۰ فایروال، ورود دستی به هر کدام ناممکن و ناهمگن می‌شود. مدیریت مرکزی یک منبع حقیقت می‌دهد: Policy Package، Revision و Audit. ولی همین مرکز، هدف جذاب مهاجم است؛ پس RBAC و Hardening آن حیاتی است. FMG/FAZ وابسته به لایسنس هستند (Needs-License).

### ۳) توضیح عمیق فنی

#### ۱) معماری

``` text
FortiManager (policy, device DB, revisions)  --FGFM-->  FGT-1..N
FortiAnalyzer (logs, reports, events)        <--logs--  FGT-1..N
ADOM: per region / per customer
```

#### ۲) RBAC

| نقش | دسترسی |
|---|---|
| Super | همه (۲ نفر، MFA) |
| Network Admin | Policy Package ADOM خود |
| ReadOnly (NOC) | مشاهده |
| Auditor | Log و Revision خواندنی |

#### ۳) فرایند Change

1. ایجاد Revision/Backup. 2. ویرایش Policy Package. 3. Review (Workflow Session). 4. Install Preview. 5. Install در Window. 6. Verify. 7. Close.

#### ۴) Audit

Alert: «Config changed» و «Admin login failed» ≥ 5. Retention لاگ ۱ سال.

#### ۵) Hardening مدیریت مرکزی

شبکه‌ی Mgmt جدا؛ Trusted host؛ MFA؛ Backup FMG؛ HA.

#### ۶) آزمون و Rubric

سناریو: افزودن Policy به ۵ شعبه با CHG؛ Install Preview؛ Rollback به Revision قبلی. Rubric: معماری ۲۰، RBAC ۲۰، Change ۲۰، Audit ۲۰، آزمون و صداقت ۲۰.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ADOM | بر اساس منطقه |
| RBAC | حداقل |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

NOC فقط خواندن.

#### مثال متوسط

`accprofile`.

#### مثال سخت

OOB با Console Server.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** ADOM-EU و ADOM-US؛ Network Admin هر ADOM فقط ADOM خودش.

**متوسط (Change):** Install Preview نشان داد Policy ۶۲ در ۵ دستگاه؛ Install در Window؛ Verify؛ Revision ثبت.

**سخت (Rollback):** Install باعث قطع VPN شد. مراحل: Revision قبلی؛ Install مجدد؛ ۸ دقیقه؛ RCA: Object مشترک تغییر کرده بود؛ اقدام: Preview با Diff و آزمون در Lab.

### ۷) پیاده‌سازی از مسیر CLI

``` text
! FMG/FAZ operations are mostly GUI; verify license (Needs-License)
```

### ۸) Verification (اثبات صحت)

- Revision.
- Audit Alert.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Install شکست | Preview/Connectivity | FGFM |

### ۱۰) نکات امنیتی

- MFA.
- Mgmt جدا.

### ۱۱) جمع‌بندی مفهومی

- مرکز=منبع حقیقت.
- RBAC.
- Revision و Rollback.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) ADOM؟ *(پاسخ: 26-4-ت1)*

**ت2.** (ساده) چرا Revision؟ *(پاسخ: 26-4-ت2)*

**ت3.** (متوسط) Install Preview؟ *(پاسخ: 26-4-ت3)*

**ت4.** (متوسط) چرا مرکز هدف است؟ *(پاسخ: 26-4-ت4)*

**ت5.** (سخت) Install قطع کرد؛ رفع. *(پاسخ: 26-4-ت5)*

**ت6.** (سخت، طراحی) RBAC چهارسطحی. *(پاسخ: 26-4-ت6)*

**Q1.** Quick quiz (English): Why use install preview before pushing a policy package? *(پاسخ: 26-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ADOM | Administrative Domain | دامنه‌ی مدیریتی |

- *Review the diff before installing.* ← قبل از Install تفاوت‌ها را بازبینی کنید.

### ۱۴) کارت Lab

**کارت Lab:** معماری ۹ (اجرا نشده؛ Needs-License). **Evidence:** `02-design/arch9.md`.

### ۱۵) منابع

- Fortinet FortiManager Administration Guide
- FortiAnalyzer Administration Guide

### ضمیمه: پرونده‌ی کامل حل‌شده — Install با Preview و Rollback

**سناریو:** افزودن Policy 62 به ۵ شعبه از طریق FortiManager (Needs-License).

1. **Revision:** پیش از تغییر یک Revision/Backup ثبت کنید (برچسب «before-CHG0123»).
2. **تغییر:** در Policy Package شعبه‌ها Policy 62 را اضافه کنید.
3. **Install Preview:** برای هر شعبه فقط ۱ خط تغییر (`+ policy 62`) دیده می‌شود؛ اگر Object مشترک هم تغییر کرده بود باید جدا بررسی می‌شد.
4. **Install در Window:** ساعت 22:00؛ نتیجه: ۴ موفق، ۱ شکست (FGFM).
5. **رفع شکست:** Connectivity/FGFM شعبه‌ی پنجم؛ Install مجدد.
6. **Verify:** Policy Lookup روی هر شعبه؛ Hit Count.
7. **Rollback در صورت نیاز:** نصب Revision قبلی؛ ۸ دقیقه.

``` text
Audit alert: 'Configuration changed' by user net01 at 22:03 -> ticket CHG-0123
```

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: معماری مدیریت و عملیات

Runbook، Change، Monitoring، Backup، RBAC. شاخص: RPO/RTO مستند.

**پرسش‌های مصاحبه**
1. *RBAC؟* Profile.
2. *Out-of-band؟* Mgmt شبکه‌ی جدا.
3. *Audit؟* Log تغییر.

### مثال حل‌شده: RBAC مدیریتی

| نقش | دسترسی |
|---|---|
| NOC | فقط خواندن (super_admin_readonly) |
| Network Eng | Policy/Route |
| Security | Log/UTM |

``` text
config system accprofile
 edit "noc-ro"
  set netgrp read
  set fwgrp read
  set loggrp read
 next
end
```

آزمون: کاربر NOC تلاش به تغییر Policy ⇒ رد؛ Log رویداد ثبت شود.

### تکمیل عمیق: معماری عملیات — RBAC، Out-of-band، Audit

#### چرا؟

عملیات مقیاس‌پذیر یعنی «هر کس فقط همان کاری را بتواند انجام دهد که باید». این‌جا RBAC (Role-Based Access Control، یعنی «کنترل دسترسی نقش‌محور»)، شبکه‌ی مدیریتی جدا و ممیزی را کنار هم می‌گذاریم.

#### مثال ساده — نقش‌ها

| نقش | دسترسی | مثال |
|---|---|---|
| NOC | فقط‌خواندنی | بررسی Health |
| Network Eng | Policy/Route | تغییر با CHG |
| Security | Log/UTM | تحلیل |
| Super Admin | کامل | 2 نفر |

#### مثال متوسط — Profile

``` text
config system accprofile
 edit "noc-ro"
  set netgrp read
  set fwgrp read
  set loggrp read
  set sysgrp read
 next
end
```

آزمون: کاربر NOC تلاش به تغییر Policy ⇒ رد و Log رویداد.

#### مثال سخت — Out-of-band

اگر مدیریت از همان شبکه‌ی Production برود و فایروال یا لینک خراب شود، دسترسی هم قطع می‌شود. راه: شبکه‌ی Mgmt جدا (OOB) با Console Server/LTE.

#### Audit

Log تغییرات: چه کسی، کی، چه چیزی (`config log eventfilter`). هفتگی با CHGها تطبیق دهید؛ تغییر بدون CHG یعنی خارج از فرایند.

``` text
Unmatched changes = total config changes - changes with CHG
```

#### Lab

سه پروفایل بسازید و رفتار هر کدام را تست کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| همه Super Admin | سهل‌انگاری | RBAC |
| تغییر بدون ردپا | Log غیرفعال | eventfilter |
| قطع مدیریت | Inband | OOB |

#### پرسش‌ها با پاسخ

**۱. RBAC چیست؟** دسترسی بر اساس نقش.
**۲. OOB چرا؟** مدیریت هنگام خرابی.
**۳. چرا Audit؟** ردگیری.

#### English Corner

- *Apply least privilege through role-based profiles.*
- Q: Why keep a separate out-of-band management path?

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

Syslog روی TCP تضمین تحویل بهتر دارد و برای Extended Logging لازم است.

**26-2-ت2** — مبدأ یکتا و قابل‌کنترل برای ACL/مسیر و شناسایی دستگاه در سرور.

**26-2-ت3** — ≈ 3.6 GB/روز؛ ×90 ≈ 324 GB؛ با فشرده‌سازی 10:1 ≈ 32 GB.

حجم Log ≈ 3.6 GB/روز؛ ۹۰ روز ≈ 324 GB؛ با فشرده‌سازی ۱۰:۱ ≈ 32 GB.

``` text
3.6 GB x 90 = 324 GB ; 324 / 10 = 32.4 GB
```

**26-2-ت4** — `execute ping` با source-ip، Sniffer روی Interface خروجی FGT، tcpdump روی سرور و بررسی Firewall سرور.

**26-2-ت5** — reliable، دو مقصد/سرور HA، Alert بدون Log، ذخیره‌ی محلی Retention برای رویدادهای حیاتی، آزمون قطع.

**26-2-ت6** — TCP reliable به دو سرور، rsyslog+Parser، ایندکس، حجم و فضا محاسبه، چرخش، Alert Loss، دسترسی RBAC.

**26-2-Q1** — Because UDP does not guarantee delivery, so events can be lost during network or server problems.


### پاسخ‌های بازنویسی عمیق درس 26-3

**26-3-ت1** — چون نمی‌دانیم فایل کامل/سازگار است و RTO واقعی چقدر است.

Backup را باید Restore کرد تا مطمئن شویم فایل کامل است و RTO واقعی معلوم شود.

**26-3-ت2** — تفاوت پیکربندی واقعی دستگاه با نسخه‌ی مرجع در Git.

Drift یعنی تفاوت Config واقعی دستگاه با نسخه‌ی مرجع در Git.

**26-3-ت3** — `password`، `psksecret`، `secret`، `passwd`، گواهی/کلید خصوصی و توکن API.

**26-3-ت4** — نقطه‌ی بازگشت مشخص برای Rollback و مقایسه.

Revision/Tag نقطه‌ی بازگشت مشخص برای Rollback و مقایسه است.

**26-3-ت5** — حذف از تاریخچه، چرخش همه‌ی اعتبارنامه‌ها، بازبینی دسترسی، Pre-commit scan، PIR؛ فرض افشا.

**26-3-ت6** — Backup روزانه، Lab هم‌نسخه، Runbook Restore، آزمون فصلی، اندازه‌گیری RTO و اصلاح.

**26-3-Q1** — Because it may already have been copied or exposed, so credentials must be rotated.


### پاسخ‌های بازنویسی عمیق درس 26-4


### پاسخ‌های بازنویسی عمیق درس 26-4

**26-4-ت1** — دامنه‌ی مدیریتی جدا.

ADOM دامنه‌ی مدیریتی جدا برای گروهی از دستگاه‌ها است.

**26-4-ت2** — Rollback.

Revision امکان Rollback می‌دهد.

**26-4-ت3** — نمایش تغییرات پیش از اعمال.

Install Preview تغییرات را پیش از اعمال نشان می‌دهد.

**26-4-ت4** — دسترسی به همه‌ی دستگاه‌ها.

مرکز مدیریت هدف جذاب است چون دسترسی به همه‌ی دستگاه‌ها دارد.

**26-4-ت5** — Revision قبلی.

Install قطع کرد: به Revision قبلی برگردید و Install مجدد.

**26-4-ت6** — جدول.

RBAC چهارسطحی: Super، Network، ReadOnly، Auditor با مثال دسترسی.

**26-4-Q1** — To review the changes that will be applied and avoid unintended impact.

### پاسخ‌های درس افزوده‌ی 26-0 (فصل 26)

**26-0-ت1** — FMG پیکربندی/Policy مرکزی؛ FAZ جمع‌آوری و تحلیل Log.

FMG پیکربندی/Policy مرکزی؛ FAZ جمع‌آوری و تحلیل Log.

**26-0-ت2** — دامنه‌ی مدیریتی مجزا برای دستگاه‌ها/مدیران با Policy Package و Object خودش.

**26-0-ت3** — تا تأثیر نصب پیش از اعمال دیده شود و خطای گسترده رخ ندهد.

Install Preview تا اثر نصب پیش از اعمال دیده شود.

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Baseline؟** بدون «نرمال»، «غیرعادی» معنا ندارد. P95 و ضریب آستانه‌ی هشدار را می‌سازند.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

``` text
CPU P95 41% x 1.5 = 61% warn
```

#### مثال متوسط

``` text
Session warn = 0.5 x 200000 = 100000
```

#### مثال سخت

Baseline فصلی.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Baseline با عدد

Baseline: میانگین CPU 18٪، Session 25k، Throughput Peak 400 Mbps. هشدار: CPU > 70٪ برای ۱۰ دقیقه؛ Session > 80٪ ظرفیت.

**پرسش‌های مصاحبه**
1. *چرا Baseline؟* تشخیص غیرعادی.
2. *آستانه؟* درصدی از Peak.
3. *Alert Fatigue؟* آستانه‌ی دقیق.

### مثال حل‌شده: ساخت Baseline و آستانه

**داده‌ی ۷ روزه:** CPU میانگین 18٪، P95 = 41٪؛ Session میانگین 25000، Peak 38000؛ ظرفیت Session مدل = 200000.

``` text
Session alert warn = 0.5 x 200000 = 100000
Session alert crit = 0.8 x 200000 = 160000
CPU warn = P95 x 1.5 = 61%
```

مراحل: ۱) Baseline از دورهٔ نرمال ۲) آستانه بر اساس ظرفیت و P95 ۳) بازبینی ماهانه. هشدار با Duration (مثلاً ۱۰ دقیقه) برای کاهش Alert Fatigue.

### تکمیل عمیق: Baseline — بدون «نرمال»، «غیرعادی» معنا ندارد

#### چرا باید یاد بگیریم؟

پزشک وقتی می‌گوید «فشار خون ۱۶۰ بالاست» که بداند فشار نرمال شما ۱۲۰ است. اگر فشار همیشگی کسی ۱۶۰ باشد، همین عدد نرمال اوست. در شبکه هم «CPU ۶۰٪» برای یک دستگاه عادی و برای دستگاه دیگر فاجعه است. **Baseline** یعنی ثبت رفتار عادی تا انحراف را تشخیص دهید.

#### توضیح ساده

سه سؤال: چه چیزی را اندازه بگیریم (CPU، Session، پهنای باند، خطا)؟ هر چند وقت یک‌بار؟ چه عددی «هشدار» است؟

#### مثال ساده — ساخت Baseline

داده‌ی ۷ روز: CPU میانگین ۱۸٪، P95 برابر ۴۱٪؛ Session میانگین ۲۵,۰۰۰ و Peak ۳۸,۰۰۰؛ ظرفیت مدل ۲۰۰,۰۰۰ Session.

P95 یعنی ۹۵٪ زمان مقدار کمتر یا مساوی این عدد بود (۵٪ بالاترین‌ها حذف می‌شود تا اوج‌های لحظه‌ای گمراه نکنند).

#### مثال متوسط — تعیین آستانه

``` text
Session warn = 50% of capacity = 0.5 x 200000 = 100000
Session crit = 80% of capacity = 0.8 x 200000 = 160000
CPU warn     = P95 x 1.5      = 41 x 1.5 ~ 61 %
```

مراحل: ۱) ظرفیت از مستند مدل ۲) درصد ۳) P95 ۴) ضریب ۵) مدت پایداری (مثلاً ۱۰ دقیقه) تا هشدار کاذب کم شود.

#### مثال سخت — فصل‌بندی

پایان ماه مالی ترافیک ۳ برابر می‌شود. Baseline یک ماه عادی هشدار کاذب می‌دهد. راه: Baseline جدا برای «روز عادی» و «پایان ماه» یا آستانه‌ی وابسته به تقویم.

#### Alert Fatigue

اگر روزی ۲۰۰ هشدار بیاید، هیچ‌کس نمی‌خواند. قاعده: هشدار باید **اقدام‌پذیر** باشد؛ اگر کسی کاری نمی‌کند، حذفش کنید یا به گزارش تبدیلش کنید.

#### Lab

یک هفته داده‌ی Zabbix یا SNMP جمع کنید و جدول Baseline را بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| هشدار زیاد | آستانه‌ی نزدیک به نرمال | P95 × ضریب |
| هشدار دیر | آستانه بالا | کاهش |
| نویز شبانه | کار Backup | Maintenance window |

#### پرسش‌ها با پاسخ

**۱. P95 چیست؟** ۹۵٪ مقادیر زیر آن.
**۲. چرا مدت پایداری؟** حذف اوج لحظه‌ای.
**۳. Alert Fatigue؟** هشدار زیاد و بی‌اقدام.

#### English Corner

- *A baseline tells you what normal looks like.*
- Q: Why use the 95th percentile instead of the maximum?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Logging درست؟** Log حافظه‌ی شبکه است؛ ناقص یعنی کوری در حادثه، بیش‌ازحد یعنی دیسک پر.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

`logtraffic all`.

#### مثال متوسط

`fwpolicy-implicit-log enable`.

#### مثال سخت

دیسک پر ⇒ Syslog/FAZ.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: انواع Log

Traffic، Event، UTM، Local. `config log setting; set fwpolicy-implicit-log enable`.

``` text
config log setting
 set fwpolicy-implicit-log enable
 set local-in-allow enable
end
```

**پرسش‌های مصاحبه**
1. *Log دیسک؟* پر شدن.
2. *Log All در برابر UTM؟* حجم.
3. *زمان؟* NTP.

### مثال حل‌شده: چرا Log ترافیک ثبت نمی‌شود؟

1. Policy را باز کنید: `logtraffic` اگر `disable` است ⇒ `utm` یا `all`.
2. `config log setting` و `fwpolicy-implicit-log`.
3. مقصد Log: `config log disk setting` یا syslog.
4. `execute log filter category 0 ; execute log display`.

``` text
date=2026-11-27 srcip=10.10.0.5 dstip=198.51.100.8 policyid=30 action=accept
```

اگر Disk Log پر است، به Syslog/FAZ منتقل کنید.

### تکمیل عمیق: Logging در FortiGate — چه چیزی، کجا و با چه هزینه‌ای؟

#### چرا؟

Log‌ها حافظه‌ی شبکه‌اند. Log ناقص یعنی در حادثه کور هستید؛ Log بیش‌ازحد یعنی دیسک پر و CPU درگیر. تعادل لازم است.

#### انواع Log

| نوع | محتوا | مثال |
|---|---|---|
| Traffic | Sessionها | accept/deny |
| Event | سیستم/ادمین/VPN | ورود ادمین |
| UTM | AV/IPS/Web | virus blocked |
| Local | ترافیک به خود فایروال | Local-in |

#### مثال ساده — Log در Policy

``` text
config firewall policy
 edit 30
  set logtraffic all     # or utm
 next
end
```

`all` هر Session؛ `utm` فقط رویدادهای UTM. برای Policy Deny پایانی همیشه `all`.

#### مثال متوسط — Implicit Deny

``` text
config log setting
 set fwpolicy-implicit-log enable
end
```

بدون آن ترافیک رد‌شده‌ی Implicit Deny ثبت نمی‌شود و نشانه‌ای از اسکن نمی‌بینید.

#### مثال سخت — دیسک پر

Log روی دیسک محلی در ۴۸ ساعت پر می‌شود و Rolling فعال است؛ حادثه‌ی هفته‌ی قبل از بین رفته. راه: ارسال به Syslog/FAZ با نگهداری ۹۰ روز و محاسبه‌ی ظرفیت.

``` text
Storage = log_per_day x days x devices
2 GB x 90 x 12 = 2160 GB
```

#### Lab

یک Policy با Log all بسازید، ترافیک تولید و در GUI/CLI Log را فیلتر کنید.

``` text
execute log filter category 0
execute log filter field srcip 10.10.0.5
execute log display
```

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Log نیست | logtraffic disable | فعال‌سازی |
| Log ناقص | دیسک/Rate | Syslog |
| زمان اشتباه | NTP/Timezone | تنظیم |

#### پرسش‌ها با پاسخ

**۱. تفاوت all و utm؟** تمام Session در برابر فقط UTM.
**۲. چرا Syslog؟** ماندگاری و تحلیل.
**۳. چرا NTP؟** ترتیب رویدادها.

#### English Corner

- *Enable logging on the final deny policy.*
- Q: Why send logs off the device?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا SNMP/Zabbix؟** مانیتورینگ عدد می‌گیرد، ذخیره و با آستانه مقایسه و خبر می‌دهد. SNMPv3 ترجیح.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

`snmpwalk -v2c -c ro-comm 10.50.0.1`.

#### مثال متوسط

Trigger `avg(...,10m)>70`.

#### مثال سخت

Trigger «No data».

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: SNMP و Zabbix

``` text
config system snmp sysinfo
 set status enable
end
config system snmp community
 edit 1
  set name "ro-comm"
  config hosts
   edit 1
    set ip 10.50.0.20 255.255.255.255
   next
  end
 next
end
```

ترجیح SNMPv3. OIDها: CPU، Memory، Session، Interface. **پرسش‌های مصاحبه**
1. *v2c ریسک؟* رمز متن‌ساده.
2. *Trigger؟* آستانه.
3. *Template؟* آماده‌ی Fortinet.

### مثال حل‌شده: پایش CPU با SNMP

``` text
snmpwalk -v2c -c ro-comm 10.50.0.1 1.3.6.1.4.1.12356.101.4.1.3
```

OID بالا از MIB فورتی‌نت (fgSysCpuUsage؛ مسیر را از MIB رسمی نسخه تأیید کنید). تفسیر عدد: درصد CPU.

در Zabbix: Item ← Trigger `avg(/FGT/cpu,10m)>70` ← Action ایمیل. آزمون: بار مصنوعی با iperf و دیدن Trigger.

### تکمیل عمیق: SNMP و Zabbix — از نیاز تا هشدار واقعی

#### چرا؟

نمی‌شود صبح‌ها وارد ۱۰ فایروال شد و CPU را دید. مانیتورینگ این کار را خودکار می‌کند: عدد را می‌گیرد، ذخیره می‌کند، با آستانه مقایسه می‌کند و خبر می‌دهد.

#### SNMP

SNMP = Simple Network Management Protocol، یعنی «پروتکل ساده‌ی مدیریت شبکه». نسخه‌ها: v1/v2c (رمز Community به‌صورت متن ساده) و v3 (احراز هویت و رمزنگاری). در محیط واقعی v3 را ترجیح دهید.

#### مثال ساده — فعال‌سازی

``` text
config system snmp sysinfo
 set status enable
end
config system snmp community
 edit 1
  set name "ro-comm"
  config hosts
   edit 1
    set ip 10.50.0.20 255.255.255.255
   next
  end
 next
end
```

فقط IP سرور مانیتورینگ مجاز است؛ و Interface مدیریتی باید SNMP را مجاز کند (`allowaccess snmp`).

#### مثال متوسط — خواندن

``` text
snmpwalk -v2c -c ro-comm 10.50.0.1 1.3.6.1.2.1.1.1
```

اگر خروجی بیاید، SNMP کار می‌کند. OIDهای اختصاصی Fortinet (CPU، Memory، Session) را از MIB رسمی همان نسخه بگیرید.

#### مثال سخت — Trigger در Zabbix

``` text
avg(/FGT-1/system.cpu.util,10m) > 70
```

یعنی میانگین CPU در ۱۰ دقیقه بیش از ۷۰٪. آزمون: بار مصنوعی با iperf و دیدن Trigger. همچنین Trigger «No data for 5m» برای تشخیص قطع SNMP.

#### SNMPv3 (نمونه)

``` text
config system snmp user
 edit "mon"
  set security-level auth-priv
  set auth-proto sha256
  set priv-proto aes256
 next
end
```

رمزها را در Vault نگه دارید.

#### Lab

SNMP را در Lab فعال، با snmpwalk تست و یک Trigger بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Timeout | allowaccess/ACL | بررسی |
| Community اشتباه | نام | تطبیق |
| داده‌ی نامعتبر | OID اشتباه | MIB رسمی |

#### پرسش‌ها با پاسخ

**۱. چرا v3؟** رمزنگاری.
**۲. چرا Host محدود؟** سطح حمله.
**۳. No data Trigger؟** تشخیص قطع پایش.

#### English Corner

- *Prefer SNMPv3 with authentication and privacy.*
- Q: Why restrict SNMP to the monitoring host?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا API امن؟** اتوماسیون بدون امنیت در پشتی است: حداقل دسترسی، Trusted Host، توکن در Vault.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

GET status.

#### مثال متوسط

403 ⇒ Trusted Host/Profile.

#### مثال سخت

POST با Rollback.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: API امن

``` text
config system api-user
 edit "zabbix"
  set accprofile "ro-profile"
  set trusthost1 10.50.0.20 255.255.255.255
 next
end
```

Trusted Host اجباری؛ فقط GET؛ توکن در Vault.

**پرسش‌های مصاحبه**
1. *Accprofile؟* حداقل دسترسی.
2. *Rate limit؟* حفاظت.
3. *Log API؟* ممیزی.

### مثال حل‌شده: GET امن به API

``` text
curl -sk -H "Authorization: Bearer $TOKEN" https://10.50.0.1/api/v2/monitor/system/status
```

نتیجه‌ی مورد انتظار: JSON با `version`. اگر از IP غیرمجاز زده شود ⇒ خطای دسترسی (Trusted Host). توکن را در متغیر محیطی/Vault نگه دارید نه در Script.

آزمون منفی: Profile فقط‌خواندنی با روش PUT ⇒ رد.

### تکمیل عمیق: REST API و Automation امن

#### چرا؟

کارهای تکراری (Backup، گزارش، افزودن Address) را با دست انجام ندهید؛ ولی API بدون امنیت یک در پشتی است. این درس خودکارسازی را با کمترین ریسک نشان می‌دهد.

#### اصول

1. **حداقل دسترسی**: Profile فقط‌خواندنی برای مانیتورینگ.
2. **Trusted Host**: فقط IP مجاز.
3. **توکن در Vault** نه در Script.
4. **Log و ممیزی** درخواست‌ها.

#### مثال ساده — ساخت کاربر API

``` text
config system api-user
 edit "zabbix"
  set accprofile "ro-profile"
  config trusthost
   edit 1
    set type ipv4-trusthost
    set ipv4-trusthost 10.50.0.20 255.255.255.255
   next
  end
 next
end
```

#### مثال متوسط — GET

``` text
curl -sk -H "Authorization: Bearer $TOKEN" https://10.50.0.1/api/v2/monitor/system/status
```

نتیجه JSON با نسخه. اگر از IP غیرمجاز زده شود ⇒ رد.

#### مثال سخت — تغییر خودکار با Rollback

افزودن Address با POST، سپس آزمون، سپس در صورت شکست حذف؛ و همیشه قبل از تغییر Backup بگیرید.

``` text
curl -sk -X POST -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"name":"SRV-RPT","subnet":"10.30.2.50 255.255.255.255"}' \
  https://10.50.0.1/api/v2/cmdb/firewall/address
```

پاسخ باید `status: success` باشد. خطاها را بخوانید و Script را متوقف کنید.

#### Lab

یک Script کوتاه Backup روزانه با API بنویسید؛ توکن را از متغیر محیطی بخوانید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| 403 | Trusted Host/Profile | اصلاح |
| 401 | توکن | تجدید |
| 424/خطای وابستگی | ترتیب ساخت | رفع ترتیب |

#### پرسش‌ها با پاسخ

**۱. چرا Trusted Host؟** محدودکردن منبع.
**۲. چرا Profile فقط‌خواندنی؟** حداقل دسترسی.
**۳. توکن کجا؟** Vault.

#### English Corner

- *Use least-privilege API users bound to trusted hosts.*
- Q: Why not hard-code tokens in scripts?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Hardening و Restore؟** مدیریت آسیب‌پذیرترین سطح است؛ Backup بدون آزمون Restore فقط امید است.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

`admintimeout`.

#### مثال متوسط

`nmap` از Users.

#### مثال سخت

Restore در Lab، RTO.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Hardening

چک‌لیست: Admin Trusted Host، 2FA، غیرفعال HTTP، Timeout، Banner، Backup رمزگذاری‌شده.

``` text
config system global
 set admintimeout 10
 set admin-https-ssl-versions tlsv1-2 tlsv1-3
end
```

**پرسش‌های مصاحبه**
1. *چرا admintimeout؟* Session رها.
2. *Restore آزمون؟* در Lab.
3. *Default Admin؟* تغییر نام/غیرفعال.

### مثال حل‌شده: چک‌لیست و اسکن

``` text
nmap -p 22,23,80,443,8443 10.50.0.1   (from Users VLAN)
```

انتظار: همه filtered/closed. از Mgmt: فقط 443 و 22 (در صورت نیاز). هر مورد باز ⇒ Local-in Policy/allowaccess را اصلاح کنید.

Backup: `execute backup config tftp ...` و آزمون Restore در Lab با Diff.

### تکمیل عمیق: Hardening مدیریتی و Backup/Restore — با آزمون واقعی

#### چرا؟

قوی‌ترین Policy فایروال بی‌فایده است اگر پنل مدیریت از اینترنت با رمز admin/admin باز باشد. Hardening یعنی بستن «در پشتی»‌های مدیریتی.

#### چک‌لیست

1. Admin فقط از Trusted Host و Mgmt VLAN.
2. غیرفعال HTTP/Telnet؛ فقط HTTPS/SSH.
3. MFA برای ادمین.
4. Timeout.
5. تغییر/غیرفعال Admin پیش‌فرض.
6. TLS قوی.
7. Banner قانونی.
8. Backup رمزگذاری‌شده.

#### مثال ساده — تنظیمات

``` text
config system global
 set admintimeout 10
 set admin-https-ssl-versions tlsv1-2 tlsv1-3
 set admin-lockout-threshold 5
 set admin-lockout-duration 300
end
```

#### مثال متوسط — اسکن پورت

``` text
nmap -p 22,23,80,443,8443 10.50.0.1   # from Users VLAN
```

انتظار: همه filtered/closed. از Mgmt فقط 443/22 (در صورت نیاز). مورد باز اضافی ⇒ `allowaccess`/Local-in را اصلاح کنید.

#### مثال سخت — Restore واقعی

Backup بدون آزمون Restore ارزشی ندارد.

``` text
execute backup config tftp prod.conf 10.50.0.30
# in Lab:
execute restore config tftp prod.conf 10.50.0.30
diff before.txt after.txt    # compare 'show' outputs
```

مراحل: ۱) Backup ۲) Restore در Lab ۳) مقایسه‌ی Policy/Route ۴) ثبت زمان Restore (RTO) ۵) مستندسازی.

``` text
RTO = restore time ; RPO = time since last backup
```

#### Lab

Restore را در Lab اجرا و زمان بگیرید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Lockout ادمین | آستانه | حساب اضطراری Console |
| Restore شکست | نسخه‌ی ناسازگار | همان نسخه |
| پورت باز | allowaccess | بستن |

#### پرسش‌ها با پاسخ

**۱. RTO و RPO؟** زمان بازیابی/حداکثر داده‌ی از دست‌رفته.
**۲. چرا Console اضطراری؟** در Lockout.
**۳. Backup رمزگذاری؟** Secretها.

#### English Corner

- *A backup that has never been restored is only a hope.*
- Q: What do RTO and RPO measure?

## درس 27-5 — Gate G10: آزمون عملی Logging، Monitoring، Hardening و Backup — کلید پاسخ کامل و Rubric

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۱ تا ۲۷-۴ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Syslog/FortiAnalyzer، SNMPv3 و Alert را پیکربندی و Verify کند.
2. Hardening مدیریتی را چک‌لیست و Evidence کند.
3. Backup/Restore را اجرا و Hash ثبت کند.
4. سه خرابی (Log نمی‌رسد، SNMP، Backup) را رفع کند.
5. گزارش و Rubric تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا G10؟** ثابت می‌کند عملیات را سر پا نگه می‌دارید: Log، مانیتور، API امن، Backup.

**جمع‌بندی اصلی درس:**

نظارت بدون Log و Hardening بدون Backup نصفه است. G10 چهار پایه‌ی عملیات را با هم می‌سنجد: دیدن (Log)، شنیدن (Monitoring)، سخت‌کردن (Hardening) و بازگشت (Backup).

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

FortiGate Edge باید: Syslog به 10.99.0.20؛ SNMPv3 به NMS؛ Alert روی ورود ناموفق Admin؛ Hardening طبق چک‌لیست؛ Backup روزانه و آزمون Restore.

#### ۲) پیکربندی مرجع

``` text
config log syslogd setting
 set status enable
 set server 10.99.0.20
 set port 514
end
config system snmp sysinfo
 set status enable
end
config system snmp user
 edit "nms"
  set security-level auth-priv
  set auth-proto sha256
  set priv-proto aes256
  set auth-pwd <FROM-VAULT>
  set priv-pwd <FROM-VAULT>
 next
end
config system global
 set admintimeout 10
 set admin-lockout-threshold 3
end
```

(`Unverified`؛ نام پارامترهای SNMPv3 با CLI help تأیید شود.)

#### ۳) خرابی‌ها و کلید

**A: Log نمی‌رسد.** شاهد: Sniffer روی port مدیریت: UDP 514 خارج می‌شود ولی سرور نمی‌گیرد؛ Firewall سرور یا Route. رفع: Policy/Route و `source-ip`.

**B: SNMP Timeout.** شاهد: `snmpwalk` timeout؛ علت: `allowaccess snmp` روی Interface نیست یا Host مجاز نیست. رفع.

**C: Backup ناقص.** فایل ۰ بایت؛ علت: TFTP سرور/Route. رفع و Hash.

#### ۴) چک‌لیست Hardening

MFA، Trusted host، TLS 1.2+، Telnet/HTTP off، Timeout/Lockout، Backup رمزگذاری، Log خارجی.

#### ۵) آزمون

``` text
execute log filter category 1
execute log display
snmpwalk -v3 -l authPriv -u nms <fgt-ip>
execute backup config tftp f.conf 10.99.0.5
sha256sum f.conf
```

#### ۶) Rubric

Logging ۲۰، Monitoring ۲۰، Hardening ۲۰، Backup/Restore ۲۰، تشخیص ۳ خرابی و Evidence ۲۰. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| SNMP | v3 authPriv |
| Backup | رمزگذاری و Hash |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

شاهد هر بخش.

#### مثال متوسط

Syslog Source.

#### مثال سخت

آزمون منفی API. Rubric: Logging ۲۰، Monitoring ۲۰، API ۱۵، Hardening ۲۵، Backup ۲۰.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Syslog: Event ورود Admin در سرور دیده می‌شود با زمان صحیح (NTP).

**متوسط (SNMP):** snmpwalk Timeout. مراحل: ۱) `show system interface mgmt` allowaccess بدون snmp. ۲) افزودن snmp و Host مجاز. ۳) snmpwalk موفق. پاسخ: allowaccess و Host.

**سخت (Restore):** Restore در Lab: Backup گرفته؛ Config عمدی خراب؛ Restore؛ بوت؛ مقایسه Policy count و Hash اولیه. معیار: همه‌ی Policyها و Routeها بازگردانده؛ زمان Restore ثبت. ریسک: Backup حاوی رمز؛ رمزگذاری.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute log filter category 1
execute log display
execute backup config tftp f.conf 10.99.0.5
```

### ۸) Verification (اثبات صحت)

- Log در سرور.
- SNMP پاسخ.
- Backup و Hash.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Log نمی‌رسد | Sniffer | Route/Policy |
| SNMP timeout | allowaccess | snmp |

### ۱۰) نکات امنیتی

- رمزها در Vault.

### ۱۱) جمع‌بندی مفهومی

- Log+Monitoring+Hardening+Backup.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا SNMPv3؟ *(پاسخ: 27-5-ت1)*

**ت2.** (ساده) چرا Hash Backup؟ *(پاسخ: 27-5-ت2)*

**ت3.** (متوسط) Log نمی‌رسد؛ مراحل. *(پاسخ: 27-5-ت3)*

**ت4.** (متوسط) allowaccess snmp؟ *(پاسخ: 27-5-ت4)*

**ت5.** (سخت) Restore آزمایشی. *(پاسخ: 27-5-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست G10. *(پاسخ: 27-5-ت6)*

**Q1.** Quick quiz (English): Why should backups be encrypted? *(پاسخ: 27-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NMS | Network Management System | سامانه‌ی مدیریت |

- *Test the restore, not only the backup.* ← Restore را هم آزمون کنید نه فقط Backup.

### ۱۴) کارت Lab

**کارت Lab:** G10 (اجرا نشده). **Evidence:** `03-ops/g10.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Logging; SNMP; Backup

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Rubric G10

Log ۲۰، Monitoring ۲۰، API ۱۵، Hardening ۲۵، Backup/Restore ۲۰.

**پرسش‌های مصاحبه**
1. *Evidence Restore؟* Diff Config.
2. *Alert نمونه؟* CPU.
3. *API آزمون؟* GET موفق/رد.

### مثال حل‌شده: نمره‌دهی G10

| بخش | وزن | شاهد |
|---|---|---|
| Logging | 20 | Log رسیده به Syslog |
| Monitoring | 20 | Trigger فعال شد |
| API | 15 | GET موفق + رد منفی |
| Hardening | 25 | اسکن پورت |
| Backup/Restore | 20 | Diff پس از Restore |

مثال: همه موفق جز Restore آزمون‌نشده ⇒ 80 از 100.

### تکمیل عمیق: آزمون G10 — سناریوی کامل با نمره‌گذاری

#### چرا؟

G10 ثابت می‌کند می‌توانید «عملیات» را سر پا نگه دارید: Log می‌بینید، مانیتور دارید، API امن است و Backup قابل‌اتکا.

#### صورت مسئله

برای Lab: ۱) Log به Syslog برسد ۲) Zabbix CPU و Session بخواند و Trigger بسازد ۳) کاربر API فقط‌خواندنی ۴) Hardening چک‌لیست ۵) Backup و Restore آزمایشی.

#### کلید پاسخ

| بخش | شاهد |
|---|---|
| Logging | فایل Log روی سرور + زمان |
| Monitoring | اسکرین‌شات Trigger یا خروجی snmpwalk |
| API | GET موفق + رد منفی از IP دیگر |
| Hardening | خروجی nmap و `show system global` |
| Backup/Restore | Diff پس از Restore |

#### محاسبه‌ی نمره

``` text
Logging 20 | Monitoring 20 | API 15 | Hardening 25 | Backup/Restore 20
Example: 20 + 18 + 15 + 22 + 10 = 85
```

Restore آزمون‌نشده ۱۰ نمره از دست می‌دهد.

#### مثال متوسط — خطای رایج

دانشجو Syslog را فعال کرد ولی Source Interface درست نبود؛ Log نرسید. شاهد: tcpdump روی سرور بدون بسته. رفع: `set source-ip` یا Route.

#### مثال سخت — آزمون منفی API

درخواست با Profile فقط‌خواندنی و متد PUT باید رد شود؛ اگر موفق شد، Profile اشتباه است.

#### Lab

آزمون را کامل انجام دهید و Evidence را در Index ثبت کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Log نمی‌رسد | Route/Source IP | بررسی |
| SNMP Timeout | ACL | اصلاح |
| Restore ناموفق | نسخه | هم‌نسخه |

#### پرسش‌ها با پاسخ

**۱. چرا آزمون منفی API؟** اثبات محدودیت.
**۲. Evidence Restore؟** Diff.
**۳. Syslog چه چیزی لازم دارد؟** Route و Source.

#### English Corner

- *Run a negative test to prove the restriction works.*
- Q: How do you verify a restore?

## درس 27-7 — Hardening، Backup/Restore و API: امن‌سازی مدیریتی و بازیابی قابل‌اثبات

**فصل ۲۷ · درس افزوده (پس از ۲۷-۵) · پیش‌نیاز: ۱۲-۸، ۲۶-۰، ۲۷-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** اصول از دانش عملیاتی و Local-in (۱۲-۸)؛ دستورهای `Unverified`؛ **REST API و SNMPv3 در این دور با مستند رسمی تأیید نشد** (به مرجع 7.0 مراجعه شود). Lab «اجرا نشده».

### ۱) هدف آموزشی

1. چک‌لیست Hardening مدیریتی (Admin، Access، سرویس‌ها، زمان‌بندی) را اجرا و دلیل هر مورد را بگوید.
2. **Backup/Restore** را طوری انجام دهد که «بازیابی‌شدنی بودن» اثبات شود.
3. **API/Automation** را با Least Privilege و Trusted Host محدود و ایمن به‌کار بگیرد.
4. تغییرات مدیریتی را Audit و Rollback کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا ادمین ناشناس را بررسی کنیم؟** مدیریت سطح اصلی حمله است.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده

`show system admin`.

#### مثال متوسط

Local-in deny از WAN.

#### مثال سخت

ورود 03:10 از IP خارجی: غیرفعال، تغییر رمز، diff، Persistence، PIR.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: امن‌سازی مدیریتی

Mgmt جدا، Local-in Policy، Syslog، API Trusted Host، رمز Backup. تأیید با اسکنر پورت از Users: پورت‌های مدیریت باید بسته باشند.

**پرسش‌های مصاحبه**
1. *Out-of-band؟* شبکه‌ی جدا.
2. *نسخه؟* وصله‌ی PSIRT.
3. *اسکن؟* nmap از Users.

### مثال حل‌شده: مدیریت Admin ناخواسته

``` text
show system admin
config log eventfilter ; set system enable ; end
```

Backup قبل از تغییر، سپس حذف ادمین بلااستفاده و ثبت Evidence از `show system admin` قبل/بعد.

### تکمیل عمیق: امن‌سازی مدیریتی — پرونده‌ی «ادمین ناشناس» و اسکن پورت

#### چرا؟

مدیریت آسیب‌پذیرترین سطح است؛ مهاجم با ادمین شدن، همه‌چیز دارد.

#### مثال ساده — ممیزی ادمین‌ها

``` text
show system admin
config log eventfilter
 set system enable
end
```

فهرست ادمین‌ها را با فهرست مجاز مقایسه کنید؛ هر مورد اضافی را بررسی.

#### مثال متوسط — Local-in Policy

``` text
config firewall local-in-policy
 edit 1
  set intf "port1"
  set srcaddr "all"
  set dstaddr "all"
  set service "HTTPS" "SSH"
  set action deny
  set schedule "always"
 next
end
```

یعنی از WAN ورود مدیریتی رد شود؛ استثنای IP مجاز را بالاتر بگذارید.

#### مثال سخت — ادمین ناشناس

بررسی Log Event: ورود ادمین «backup2» از IP خارجی در ساعت ۰۳:۱۰. اقدام: ۱) غیرفعال‌سازی ۲) تغییر رمز همه ۳) بررسی تغییرات Config (`diff` با Backup) ۴) بررسی Persistence (Script، SSH Key) ۵) PIR.

#### Lab

یک ادمین آزمایشی بسازید، ورود را Log کنید و مسیر هشدار را تست کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| ورود مدیریتی از اینترنت | allowaccess | بستن |
| ادمین ناشناس | کنترل ضعیف | ممیزی |
| Log ادمین ندارد | eventfilter | فعال |

#### پرسش‌ها با پاسخ

**۱. Local-in چیست؟** ترافیک به خود فایروال.
**۲. چرا diff Config؟** کشف تغییر ناخواسته.
**۳. چرا PIR؟** جلوگیری از تکرار.

#### English Corner

- *Management access should never be exposed to the internet.*
- Q: What do you check after finding an unknown admin?

<a id="l-27-8"></a>

## درس 27-8 — Log در FortiGate: مقصدها، سطح‌ها، مشاهده و عیب‌یابی

**فصل 27 · درس افزوده برای سرفصل رسمی NSE 4 (FortiOS 7.0): «Configure log settings and diagnose problems using the logs» · پیش‌نیاز: ۲۷-۱، ۲۶-۲**

> **وضعیت:** نظری/مستندی؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ FortiAnalyzer Needs-License؛ Lab اجرا نشده.

### ۱) این درس درباره چیست و چرا باید یاد بگیریم؟

**چه چیزی یاد می‌گیریم:** Logها کجا ذخیره می‌شوند (Memory، Disk، FortiAnalyzer، Syslog، FortiCloud)، چه سطحی ثبت شود، چطور مشاهده کنیم و چطور از Log علت یک خرابی را بیابیم.

**چرا لازم است؟** Log دوربین مدار بسته‌ی شبکه است. اگر روی Memory ثبت شود، با ریبوت گم می‌شود؛ اگر Disk کوچک باشد، پس از چند روز بازنویسی می‌شود؛ اگر هیچ‌چیز ثبت نشود، در حادثه کور هستید. آزمون NSE4 «تشخیص مشکل با Log» می‌خواهد؛ پس باید بدانید در Log کدام فیلد را بخوانید.

### ۲) توضیح از پایه

#### ۲-۱) مقصدها

| مقصد | ماندگاری | نکته |
|---|---|---|
| Memory | موقت (ریبوت = حذف) | فقط رویدادهای اخیر |
| Disk | محلی؛ در بعضی مدل‌ها/VM پیش‌فرض خاموش | ظرفیت کم، Rolling |
| FortiAnalyzer | متمرکز | تحلیل و گزارش (Needs-License) |
| Syslog | سرور مرکزی (rsyslog/SIEM) | درس ۲۶-۲ |
| FortiCloud | ابر Fortinet | طبق لایسنس |

#### ۲-۲) نوع Log

- **Traffic:** Sessionها (Forward/Local).
- **Event:** سیستم، ادمین، VPN، HA، Router.
- **Security (UTM):** AV، IPS، Web، App.

#### ۲-۳) سطح (Severity)

0 Emergency، 1 Alert، 2 Critical، 3 Error، 4 Warning، 5 Notification، 6 Information، 7 Debug. Log را با آستانه‌ی حداقل (مثلاً Information) ثبت کنید.

``` text
config log memory filter
 set severity information
end
config log disk setting
 set status enable
 set max-log-file-size 20
 set diskfull overwrite
end
config log fortianalyzer setting
 set status enable
 set server 10.50.0.30
 set reliable enable
end
config log syslogd setting
 set status enable
 set server 10.50.0.20
 set mode reliable
end
```

#### ۲-۴) Log در Policy

``` text
config firewall policy
 edit 30
  set logtraffic all
 next
end
```

`all` همه‌ی Sessionها؛ `utm` فقط رویداد UTM؛ `disable` هیچ.

### ۳) مشاهده و جست‌وجو

``` text
execute log filter category 0
execute log filter field srcip 10.10.0.5
execute log filter field dstport 443
execute log filter start-line 1
execute log filter view-lines 20
execute log display
diagnose log test
```

`diagnose log test` Logهای نمونه تولید می‌کند تا مسیر ارسال را بیازمایید.

نمونه Log Traffic و فیلدهای مهم:

``` text
date=2026-11-27 time=10:12:01 logid=0000000013 type=traffic subtype=forward level=notice
srcip=10.10.0.5 dstip=198.51.100.8 dstport=443 action=deny policyid=0 service=HTTPS
sentbyte=0 rcvdbyte=0 srcintf="port2" dstintf="port1"
```

فیلدها: `action` (accept/deny/close/timeout)، `policyid` (0 = Deny ضمنی)، `srcintf/dstintf`، `sentbyte/rcvdbyte`، `duration`.

### ۴) مثال‌های حل‌شده از ساده به سخت

**ساده.** `policyid=0 action=deny` ⇒ ترافیک مطابق هیچ Policy نشد؛ Policy یا Interface اشتباه.

**متوسط — «Log نمی‌رسد».**

1. Policy `logtraffic` فعال؟
2. مقصد فعال (`config log disk setting`)؟
3. Syslog: `execute ping`، Route، Source IP، پورت و `tcpdump` روی سرور.
4. FAZ: در GUI وضعیت Connection و (طبق نسخه) `execute log fortianalyzer test-connectivity` (Unverified).
5. سطح Severity بسیار بالا (فقط Critical) ⇒ Log کم.

**متوسط — حجم Log.** 2 GB در روز ×۱۲ دستگاه × ۹۰ روز = 2160 GB؛ پس برای نگهداری ۹۰ روزه ≈ 2.1 TB (درس ۲۶-۱).

**سخت — حادثه‌ی «اتصال دیشب قطع شد».**

1. فیلتر زمانی روی Traffic با `dstip` سرور.
2. `action=timeout` و `rcvdbyte=0` ⇒ بدون پاسخ از سرور.
3. Event Log: تغییر Config/Link/HA در همان ساعت؟
4. `date/time` با NTP هم‌گام (Timezone).
5. نتیجه: لینک ISP در ۰۲:۱۰ قطع (Event Log: `Link-monitor status changed`).

### ۵) Lab (اجرا نشده)

Logging به Syslog را فعال، یک Deny ایجاد و Log را در سرور و `execute log display` مقایسه کنید.

### ۶) اصطلاحات این درس

| اصطلاح | شکل کامل | معنی |
|---|---|---|
| FAZ | FortiAnalyzer | تحلیل‌گر Log فورتی‌نت |
| Syslog | System Logging Protocol | ارسال Log شبکه‌ای |
| UTM | Unified Threat Management | مدیریت یکپارچه‌ی تهدید |
| SIEM | Security Information and Event Management | جمع‌آوری و همبستگی رویداد |

### ۷) تمرین‌ها

**ت1.** (ساده) چرا Memory Log کافی نیست؟ *(پاسخ: 27-8-ت1 در بخش «پاسخ‌ها» انتهای فصل)*

**ت2.** (ساده) `policyid=0` یعنی چه؟ *(پاسخ: 27-8-ت2 در بخش «پاسخ‌ها» انتهای فصل)*

**ت3.** (متوسط) پنج گام وقتی Log به Syslog نمی‌رسد. *(پاسخ: 27-8-ت3 در بخش «پاسخ‌ها» انتهای فصل)*

**ت4.** (سخت) از Log علت قطع شبانه را چگونه می‌یابید؟ *(پاسخ: 27-8-ت4 در بخش «پاسخ‌ها» انتهای فصل)*

### ۸) English Corner

- *Send logs to a central server so they survive a reboot or disk overwrite.*
- *A traffic log with policy ID 0 means the session was denied by the implicit deny rule.*
- **Q1.** Which log type records administrator logins? *(پاسخ: 27-8-Q1 در بخش «پاسخ‌ها» انتهای فصل)*

---

## پاسخ‌های فصل 27

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 27-1

**27-1-ت1** — Traffic، Event و Security/UTM.

سه نوع Log: Traffic، Event و Security/UTM.

**27-1-ت2** — all همه‌ی Sessionها را ثبت می‌کند؛ utm فقط Sessionهایی را که رویداد UTM دارند.

**27-1-ت3** — 12M×450B = 5.4 GB/روز؛ ×180 ≈ 972 GB؛ با 20٪ حاشیه ≈ 1.17 TB؛ فشرده‌سازی کاهش می‌دهد.

**27-1-ت4** — برای کشف Scan/حمله و عیب‌یابی Policy.

Log Deny برای کشف Scan/حمله و عیب‌یابی Policy.

**27-1-ت5** — Allow عمومی utm، Allow حیاتی all، Deny همیشه، Alert روی Deny مدیریتی و Bytes غیرعادی، Syslog مرکزی.

**27-1-ت6** — انواع، سطح، مقصد، قالب، Retention، NTP، دسترسی، Alert/بازبینی.

**27-1-Q1** — Because local storage is limited and may be overwritten or lost during an incident.


### پاسخ‌های بازنویسی عمیق درس 27-2

**27-2-ت1** — احراز و رمزنگاری؛ v2c Community را متن آشکار می‌فرستد.

SNMPv3 احراز و رمزنگاری دارد؛ v2c Community را متن آشکار می‌فرستد.

**27-2-ت2** — تفاوت آستانه‌ی ورود و خروج Alert برای جلوگیری از نوسان.

Hysteresis: تفاوت آستانه‌ی ورود و خروج Alert برای جلوگیری از نوسان.

**27-2-ت3** — آستانه از Baseline با ضریب، Maintenance window، Trigger مدت‌دار (10m).

**27-2-ت4** — Alert وابسته را وقتی وابستگی اصلی Down است سرکوب می‌کند.

Dependency suppression Alert وابسته را وقتی وابستگی اصلی Down است سرکوب می‌کند.

**27-2-ت5** — Dependency، Alert مرکزی سایت، Flap با بررسی متوالی، Escalation؛ هدف ≤ ۳ Alert.

**27-2-ت6** — CPU، Memory، Session، Interface error، Tunnel down، HA؛ هر کدام با Baseline/Hysteresis.

**27-2-Q1** — Excessive low-value alerts cause operators to ignore them; baselines, dependencies and hysteresis reduce them.


### پاسخ‌های بازنویسی عمیق درس 27-3

**27-3-ت1** — تا Token فقط از IP مجاز قابل‌استفاده باشد و سرقت Token کم‌اثر شود.

**27-3-ت2** — اجرای مکرر همان نتیجه را بدهد، بدون ایجاد تغییر یا Object تکراری.

**27-3-ت3** — Trusthost، Token لغو/منقضی، API user غیرفعال.

API Token: Trusthost، لغو/انقضا و غیرفعال‌کردن API user.

**27-3-ت4** — Diff تغییرات را بدون اعمال نشان می‌دهد و خطای گسترده را قبل از وقوع کشف می‌کند.

**27-3-ت5** — نبود بررسی وجود؛ GET نام، مقایسه، PUT/POST شرطی؛ تست دو بار اجرا؛ پاک‌سازی تکراری‌ها با Backup.

**27-3-ت6** — حساب Read-only برای مانیتورینگ؛ حساب Write جدا با Canary؛ Trusthost، Vault، TLS، Review، Backup/Rollback، Audit.

**27-3-Q1** — To show the planned changes without applying them and catch mistakes before they spread.


### پاسخ‌های بازنویسی عمیق درس 27-4

**27-4-ت1** — آزمونی که باید شکست بخورد تا اثبات شود دسترسی غیرمجاز بسته است.

**27-4-ت2** — کاهش خطر Session رهاشده.

Idle timeout خطر Session رهاشده را کم می‌کند.

**27-4-ت3** — گواهی/کلید/PSK یا لایسنس جداگانه بازیابی نشده؛ باید در Runbook باشد.

**27-4-ت4** — زمان از شروع Restore تا سرویس‌های حیاتی تأییدشده؛ در Lab با زمان‌سنج.

**27-4-ت5** — جدول بالا؛ هر کنترل یک آزمون منفی.

چک‌لیست Hardening با آزمون منفی برای هر کنترل.

**27-4-ت6** — اتوماسیون Restore، Runbook مرحله‌ای، Secrets از Vault، آزمون فصلی.

**27-4-Q1** — Because only a failed unauthorized attempt proves the control actually works.


### پاسخ‌های بازنویسی عمیق درس 27-5


### پاسخ‌های بازنویسی عمیق درس 27-5

**27-5-ت1** — احراز هویت و رمزگذاری.

SNMPv3 احراز هویت و رمزگذاری دارد.

**27-5-ت2** — تأیید صحت.

Hash Backup صحت فایل را تأیید می‌کند.

**27-5-ت3** — Sniffer، Route، Policy، سرور.

Log نمی‌رسد: Sniffer، Route، Policy و سرور.

**27-5-ت4** — لازم برای پاسخ SNMP.

allowaccess snmp برای پاسخ SNMP لازم است.

**27-5-ت5** — Backup، خراب، Restore، مقایسه.

Restore آزمایشی در Lab: ۱) Backup بگیرید و Hash ثبت کنید. ۲) Config را عمداً خراب کنید (مثلاً Policy حذف). ۳) Restore. ۴) پس از Boot: تعداد Policy/Route/Interface و Hash/Diff با نسخه‌ی اصلی. ۵) زمان Restore را ثبت کنید (RTO). ریسک: Backup حاوی رمز؛ رمزگذاری و محدودیت دسترسی.

**27-5-ت6** — ۷ مورد.

چک‌لیست G10: Log، SNMP، Alert، Hardening، Backup، Restore، Evidence.

**27-5-Q1** — Because they contain passwords and keys.

### پاسخ‌های درس افزوده‌ی 27-0 (فصل 27)

**27-0-ت1** — Traffic، Event، UTM/Security.

سه نوع Log: Traffic، Event، UTM.

**27-0-ت2** — تا انحراف را با مرجع عادی تشخیص دهیم و آستانه‌ی معنادار بگذاریم.

**27-0-ت3** — CPU>70٪ هشدار/90٪ بحرانی؛ Memory>80٪/90٪؛ Session>70٪/90٪ حد؛ Interface Error رشد؛ Tunnel/HA Down؛ Disk Log>80٪؛ همه بر پایه‌ی Baseline.

**27-0-ت4** — ۱۸۰ روز × ۲ GB = ۳۶۰ GB؛ + ۲۰٪ حاشیه؛ مرکزی با فشرده‌سازی و چرخش؛ هشدار فضا.

**27-0-Q1** — So events from different devices can be correlated reliably in time.


### پاسخ‌های درس افزوده‌ی 27-7 (فصل 27)

**27-7-ت1** — رمز و داده را بدون رمزنگاری می‌فرستند و قابل شنودند.

Telnet/HTTP/SNMPv1-2c رمز و داده را بدون رمزنگاری می‌فرستند و قابل شنودند.

**27-7-ت2** — در Lab هم‌نسخه Restore، مقایسه Interface/Policy/Route، اندازه‌گیری RTO و ثبت.

**27-7-ت3** — تغییر admin پیش‌فرض، حساب شخصی، Trusted Host، allowaccess حداقل، غیرفعال Telnet/HTTP، MFA، Timeout/Lockout، Profile حداقلی، NTP، Patch.

**27-7-ت4** — حساب API با Profile Read-only، Trusted Host فقط مانیتورینگ، Token در Vault، چرخش دوره‌ای، Log تماس‌ها.

**27-7-Q1** — Because a backup that was never restored may be corrupt or incomplete, so recovery is not proven.

### پاسخ‌های درس افزوده‌ی 27-8 (فصل 27)

**27-8-ت1** — چون با ریبوت پاک می‌شود و ظرفیت محدود است؛ برای ممیزی باید Log به Disk/FAZ/Syslog برود.

**27-8-ت2** — Deny ضمنی؛ ترافیک با هیچ Policy مطابق نشد (Interface/Address/Service نامنطبق).

**27-8-ت3** — ۱) `logtraffic` روی Policy ۲) فعال بودن مقصد ۳) Route/Source IP/پورت ۴) `tcpdump` و فایروال سرور ۵) سطح Severity.

**27-8-ت4** — فیلتر زمانی روی Traffic، بررسی `action/rcvdbyte`، سپس Event Log همان ساعت (Link/HA/Config) و تطبیق زمان با NTP.

**27-8-Q1** — Event log (system/admin events).

---

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
