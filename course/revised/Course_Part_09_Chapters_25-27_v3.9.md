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

**چرا Interoperability؟** سازمان‌ها معمولاً چند سازنده دارند: Cisco در هسته، Fortinet در لبه، شاید یک سازنده‌ی سوم در شعب. اگر «مفهوم» را بدانید، تغییر سازنده فقط تغییر Syntax است. اگر فقط دستور حفظ کرده باشید، با هر سازنده از صفر شروع می‌کنید. مثل مترجم: «آب» و «Water» یک مفهوم‌اند.

**سه سطح نگاشت**

1. **مفهومی:** SVI ↔ VLAN Interface؛ ACL ↔ Policy؛ NAT ↔ Policy NAT/VIP؛ VRF ↔ VDOM (تقریبی).
2. **رفتاری:** ACL بی‌حافظه است و باید برگشت را بنویسید؛ Policy فورتی‌گیت Stateful است. ترتیب NAT و Policy هم فرق دارد.
3. **پیش‌فرض‌ها:** مثلاً Reference Bandwidth OSPF، Timerها، Admin Distance، Keepalive.

**قاعده‌ی عملی:** هر نگاشت را با آزمون تأیید کنید (Lookup، Debug Flow، show ip route)، نه فقط با خواندن مستند.

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
Cisco:
ip access-list extended USERS-OUT
 permit tcp 10.10.0.0 0.0.0.255 host 10.20.0.10 eq 443
 deny ip any any log

FortiGate:
 srcaddr NET-USERS, dstaddr SRV-ERP, service HTTPS, action accept, log
 + final deny with log
```

مراحل: ۱) Wildcard 0.0.0.255 یعنی /24 ۲) permit به Policy Accept ۳) deny پایانی با Log ۴) برگشت در FortiGate خودکار.

#### مثال متوسط — پیش‌فرض OSPF

``` text
Cost = Reference BW / Interface BW
100 / 1000 = 0.1 -> rounded to 1
```

1G و 10G هر دو Cost=1 ⇒ باید `auto-cost reference-bandwidth` هر دو سر یکسان تنظیم شود.

#### مثال سخت — ترتیب ارزیابی NAT/Policy

مهندسی Policy ورودی VIP را با IP داخلی نوشت و Lookup مطابق نشد، چون در FortiGate Policy بعد از DNAT ارزیابی می‌شود و باید به VIP اشاره کند. با Debug Flow ترتیب را اثبات کنید.

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

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. مفاهیم هم‌ارز Cisco و Fortinet را نگاشت کنید (Interface، Zone، ACL/Policy، NAT، VRF/VDOM، Routing).
2. برگه‌ی تطبیق (Rosetta Sheet) برای تیم بسازید.
3. تفاوت فلسفه‌ی طراحی (ACL ترتیبی در برابر Policy مبتنی بر Zone و Session) را بگویید.
4. دستورهای دیدن وضعیت را در دو سازنده مقایسه کنید.
5. دام‌های رایج مهاجرت/Interop را بشناسید.
6. نگاشت را با مثال واقعی پیکربندی تأیید کنید.

### چرا باید یاد بگیریم؟

مهندسی که فقط Cisco بداند وقتی FortiGate ببیند، مثل کسی است که انگلیسی بلد است و با فرانسوی مواجه می‌شود: مفاهیم یکسان‌اند ولی واژه‌ها و فلسفه‌ی نگارش متفاوت. در شرکت‌های واقعی تقریباً همیشه چند سازنده داریم. «برگه‌ی تطبیق» ساده‌ترین ابزار برای انتقال دانش بین تیم‌هاست و جلوی اشتباه‌های مهاجرت را می‌گیرد.

### فلسفه‌ی طراحی

| ویژگی | Cisco IOS/ASA | FortiGate |
|---|---|---|
| تصمیم | ACL ترتیبی روی Interface | Policy بر پایه‌ی Interface/Zone مبدأ↔مقصد |
| وضعیت | ACL ساده Stateless؛ ASA/Zone-Based FW Stateful | همیشه Stateful |
| NAT | دستور جدا/Object NAT | داخل Policy یا Central NAT |
| UTM | ماژول/دستگاه جدا (FirePOWER) | Profile داخل Policy |
| مجازی‌سازی | VRF/Context | VDOM |

### نگاشت مفاهیم

| مفهوم | Cisco | FortiGate |
|---|---|---|
| Interface مجازی L3 | SVI `interface vlan 10` | VLAN Interface |
| Trunk | `switchport mode trunk` | VLAN sub-interface روی پورت |
| ACL ورودی | `ip access-group ACL in` | Firewall Policy |
| Zone | `zone security` | `config system zone` |
| NAT خروجی | `ip nat inside source list ... overload` | Policy `nat enable` |
| Static NAT | `ip nat inside source static` | VIP |
| Default Route | `ip route 0.0.0.0 0.0.0.0 GW` | `config router static` |
| VRF | `vrf definition` | VDOM |
| ECMP | `maximum-paths` | `v4-ecmp-mode` |
| Floating Static | AD بالاتر | Distance/Priority |
| IP SLA | `ip sla` + `track` | Link Monitor/SD-WAN Health-check |
| FHRP | HSRP/VRRP | FGCP/VRRP |

### نگاشت دستورهای مشاهده

| هدف | Cisco | FortiGate |
|---|---|---|
| جدول مسیر | `show ip route` | `get router info routing-table all` |
| جزئیات مسیر | `show ip route 10.1.1.1` | `get router info routing-table details 10.1.1.1` |
| Interface | `show ip interface brief` | `get system interface physical` |
| Session/NAT | `show ip nat translations` | `diagnose sys session list` |
| ARP | `show ip arp` | `get system arp` |
| OSPF همسایه | `show ip ospf neighbor` | `get router info ospf neighbor` |
| BGP خلاصه | `show ip bgp summary` | `get router info bgp summary` |
| IPsec | `show crypto ikev2 sa` | `diagnose vpn ike gateway list` |
| Packet Capture | `monitor capture` | `diagnose sniffer packet` |
| Config فعلی | `show running-config` | `show full-configuration` |

### ACL در برابر Policy — مثال

Cisco:

``` text
ip access-list extended USERS-IN
 permit tcp 10.10.0.0 0.0.0.255 host 10.20.0.30 eq 443
 deny   ip any any log
interface Gi0/1
 ip access-group USERS-IN in
```

FortiGate معادل:

``` text
config firewall policy
    edit 10
        set name "USERS-to-APP"
        set srcintf "ZN-USERS"
        set dstintf "ZN-SRV"
        set srcaddr "NET-USERS"
        set dstaddr "HOST-APP"
        set service "HTTPS"
        set action accept
        set schedule "always"
        set logtraffic all
    next
end
```

تفاوت مهم: ACL سیسکو Wildcard Mask (`0.0.0.255`) دارد، Fortinet Subnet Mask (`255.255.255.0`). ACL در جهت ورودی Interface؛ Policy بر دو سر (src→dst). پاسخ‌ها در Stateful خودکار مجازند.

### مثال‌های حل‌شده

#### مثال ساده — Wildcard

``` text
Cisco  : 10.10.0.0 0.0.0.255
Fortinet: 10.10.0.0 255.255.255.0 (or 10.10.0.0/24)
Wildcard = 255.255.255.255 - 255.255.255.0 = 0.0.0.255
```

#### مثال متوسط — NAT

Cisco: `ip nat inside source list 10 interface Gi0/0 overload`. Fortinet: Policy خروجی با `set nat enable` (و IP Pool اختیاری). Static NAT Cisco ⇒ VIP در Fortinet همراه Policy؛ فراموش کردن Policy دلیل رایج «VIP کار نمی‌کند».

#### مثال متوسط — ترتیب

Cisco ACL: اولین تطابق؛ Implicit Deny انتها. Fortinet: ترتیب Policy از بالا، اولین تطابق؛ Implicit Deny (Policy 0). Log Deny ضمنی باید روشن شود.

#### مثال سخت — مهاجرت ACL با `established`

Cisco: `permit tcp any any established` برای برگشت. در FortiGate لازم نیست (Stateful). کپی ACL به Policy باعث Policyهای اضافی/ناامن می‌شود. درس: «ترجمه‌ی مفهومی»، نه خط‌به‌خط.

#### مثال سخت — VRF به VDOM

VRF جداسازی L3؛ VDOM جداسازی کامل Policy/Admin/VPN. معادل یک‌به‌یک نیستند: VRF-Lite روی یک Router کافی؛ VDOM سنگین‌تر و لایسنس. تصمیم طبق نیاز Admin جدا.

### Lab هدایت‌شده (اجرا نشده)

1. یک ACL را به Policy ترجمه کنید.
2. NAT/Static NAT را نگاشت کنید.
3. جدول Rosetta تیم را کامل کنید.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Wildcard اشتباه | Mask | تبدیل |
| VIP بی‌اثر | Policy نیست | افزودن |
| ACL کپی | established | Stateful |
| VRF/VDOM | تفاوت | تصمیم |

### نکات امنیتی

ترجمه‌ی مفهومی با بازبینی امنیتی؛ Implicit Deny Log؛ حذف Policyهای اضافی.

### جمع‌بندی

نگاشت مفاهیم (ACL↔Policy، NAT↔Policy/VIP، VRF↔VDOM، IP SLA↔Link Monitor)؛ Wildcard در برابر Mask؛ Stateful؛ Rosetta Sheet برای تیم.

### تمرین و ارزیابی

**ت1.** (ساده) معادل show ip route؟ *(پاسخ: 25-1-ت1)*

**ت2.** (ساده) ACL در FortiGate؟ *(پاسخ: 25-1-ت2)*

**ت3.** (متوسط) تفاوت ذخیره؟ *(پاسخ: 25-1-ت3)*

**ت4.** (متوسط) برگشت ترافیک؟ *(پاسخ: 25-1-ت4)*

**ت5.** (سخت) ACL را به Policy ببرید. *(پاسخ: 25-1-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی تطبیق. *(پاسخ: 25-1-ت6)*

**Q1.** Quick quiz (English): What is the FortiGate equivalent of a Cisco ACL? *(پاسخ: 25-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ACL | Access Control List | فهرست کنترل دسترسی |

- *Do not translate configs line by line.* ← Config را خط‌به‌خط ترجمه نکنید.

### کارت Lab

**کارت Lab:** نگاشت Cisco–Fortinet (اجرا نشده). **Evidence:** `02-design/mapping-sheet.md`.

### منابع

- Cisco IOS docs
- Fortinet FortiOS 7.0 Administration Guide

<a id="l-25-2"></a>

## درس 25-2 — OSPF و BGP بین FortiGate و CSR: برگه‌ی پارامتر، پیکربندی دوطرفه، Redistribution و عیب‌یابی مقایسه‌ای

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۰، ۲۵-۱، ۶-۱، ۹-۷، ۱۰-۱ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 و CSR1000v 17.03.02 (IOS-XE)؛ بوت‌نشده؛ دستورها `Unverified`؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. OSPF بین FortiGate و Cisco CSR را با برگه‌ی پارامتر هماهنگ راه بیندازید.
2. BGP (eBGP) بین FortiGate و CSR را پیکربندی کنید.
3. Network Type، Hello/Dead، MTU، Area و Authentication را هماهنگ کنید.
4. Neighbor و جدول را در هر دو سمت تأیید کنید.
5. Redistribution و Prefix-list را ایمن به‌کار ببرید.
6. خطاهای رایج Interop را رفع کنید.

### چرا باید یاد بگیریم؟

OSPF/BGP استاندارد باز هستند و باید بین دو سازنده کار کنند. ولی پیش‌فرض‌ها متفاوت‌اند: مثلاً Network Type یا MTU، یا Cisco در BGP پیش‌فرض Next-hop را تغییر نمی‌دهد (iBGP). یک پارامتر ناهماهنگ و Neighbor بالا نمی‌آید. برگه‌ی پارامتر مشترک مهم‌ترین ابزار است.

### توپولوژی نمونه

``` text
LAN-FGT 10.10.0.0/16 -- [FGT 198.51.100.2/30] --- [CSR 198.51.100.1/30] -- LAN-CSR 10.20.0.0/16
```

### برگه‌ی پارامتر OSPF

| پارامتر | FortiGate | CSR |
|---|---|---|
| Router-ID | 10.254.0.1 | 10.254.0.2 |
| Area | 0.0.0.0 | 0 |
| Network Type | broadcast/point-to-point | همان |
| Hello/Dead | 10/40 | 10/40 |
| Auth | MD5/SHA | هماهنگ |
| MTU | 1500 | 1500 |

### OSPF — FortiGate

``` text
config router ospf
    set router-id 10.254.0.1
    config area
        edit 0.0.0.0
        next
    end
    config network
        edit 1
            set prefix 198.51.100.0 255.255.255.252
            set area 0.0.0.0
        next
    end
    config interface
        edit "port1"
            set network-type point-to-point
            set hello-interval 10
            set dead-interval 40
        next
    end
end
```

### OSPF — CSR

``` text
router ospf 1
 router-id 10.254.0.2
 network 198.51.100.0 0.0.0.3 area 0
interface GigabitEthernet1
 ip ospf network point-to-point
 ip ospf hello-interval 10
 ip ospf dead-interval 40
```

### BGP — eBGP

FortiGate (AS 65001):

``` text
config router bgp
    set as 65001
    set router-id 10.254.0.1
    config neighbor
        edit "198.51.100.1"
            set remote-as 65002
            set password <SECRET>
        next
    end
    config network
        edit 1
            set prefix 10.10.0.0 255.255.0.0
        next
    end
end
```

CSR (AS 65002):

``` text
router bgp 65002
 bgp router-id 10.254.0.2
 neighbor 198.51.100.2 remote-as 65001
 neighbor 198.51.100.2 password <SECRET>
 address-family ipv4
  network 10.20.0.0 mask 255.255.0.0
  neighbor 198.51.100.2 activate
```

نکته: Cisco برای Prefix باید در جدول مسیر وجود داشته باشد (`network` فقط Prefix موجود در RIB را اعلام می‌کند؛ Null0 برای Summary). FortiGate هم همین.

### تأیید

``` text
FortiGate: get router info ospf neighbor ; get router info bgp summary ; get router info routing-table all
CSR      : show ip ospf neighbor ; show ip bgp summary ; show ip route
```

### مثال‌های حل‌شده

#### مثال ساده — OSPF Full

FGT: `get router info ospf neighbor` ⇒ `10.254.0.2 Full`. CSR: `show ip ospf neighbor` ⇒ FULL. Route `O 10.20.0.0/16`.

#### مثال متوسط — MTU

FGT `mtu 1500`؛ CSR `ip mtu 1400` ⇒ Neighbor در ExStart. رفع: هماهنگ یا `ip ospf mtu-ignore` (موقت). علامت: Log `Mismatched MTU`.

#### مثال متوسط — Network Type

FGT broadcast (DR/BDR)، CSR point-to-point: Hello سازگار نیست یا DR انتخاب نمی‌شود. رفع: هر دو point-to-point.

#### مثال سخت — eBGP Multi-hop

Peer روی Loopback (غیر مستقیم) ⇒ eBGP به‌طور پیش‌فرض TTL=1 ⇒ شکست. رفع: `set ebgp-enforce-multihop enable` و `ebgp-multihop-ttl 2` در FGT؛ `neighbor x ebgp-multihop 2` و `update-source Loopback0` در CSR. توصیه: Peer مستقیم برای سادگی.

#### مثال سخت — Redistribution حلقه

دو سازنده هر دو OSPF↔BGP Redistribute می‌کنند ⇒ حلقه‌ی مسیر (Route Feedback). راه: Tag/Route-map، Prefix-list، فقط یک نقطه‌ی Redistribution و AD‌ها را درنظر بگیرید.

### Lab هدایت‌شده (اجرا نشده)

1. OSPF دو سمت.
2. eBGP و Prefix.
3. MTU/Network Type Mismatch.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| ExStart | MTU | هماهنگ |
| Neighbor نیست | Hello/Auth/Area | بررسی |
| BGP Idle/Active | Reachability/TTL | multihop |
| Route نمی‌آید | network/Prefix-list | بررسی |

### نکات امنیتی

Auth OSPF/BGP؛ Prefix-list ورودی؛ Passive Interface؛ `maximum-prefix`.

### جمع‌بندی

OSPF/BGP بین FGT و CSR: برگه‌ی پارامتر؛ Network Type/MTU/Hello؛ eBGP مستقیم یا multihop؛ تأیید دو سمت؛ Redistribution ایمن.

### تمرین و ارزیابی

**ت1.** (ساده) چرا OSPF در Exstart می‌ماند؟ *(پاسخ: 25-2-ت1)*

**ت2.** (ساده) AD پیش‌فرض eBGP و OSPF در Cisco؟ *(پاسخ: 25-2-ت2)*

**ت3.** (متوسط) مقایسه‌ی دستور Verification OSPF در دو سازنده. *(پاسخ: 25-2-ت3)*

**ت4.** (متوسط) چرا Tag در Redistribution دوطرفه؟ *(پاسخ: 25-2-ت4)*

**ت5.** (سخت) Prefix بین OSPF و BGP Flap می‌کند؛ تحلیل و رفع. *(پاسخ: 25-2-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی پارامتر برای ۳ Link بین FGT و CSR. *(پاسخ: 25-2-ت6)*

**Q1.** Quick quiz (English): Why can a bidirectional redistribution without tags create a routing loop? *(پاسخ: 25-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DBD | Database Description packet | بسته‌ی توصیف پایگاه |
| Tag | Route tag | برچسب مسیر |
| AD | Administrative Distance | اعتبار منبع مسیر |

- *Match MTU, network type and authentication on both vendors.* ← MTU، Network Type و Auth را در هر دو سازنده یکسان کنید.

### کارت Lab

**کارت Lab:** OSPF/BGP FGT–CSR. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ospf-fgt-csr.md`.

### منابع

- RFC 2328
- RFC 4271
- Cisco IOS XE OSPF/BGP Configuration Guides
- Fortinet CLI Reference 7.0

<a id="l-25-3"></a>

## درس 25-3 — IPsec چندسازنده: روش مقایسه‌ی Debug، جدول مغایرت و Interop آزمایشی FGT–CSR

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۳، ۲۵-۱، ۲۵-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. IPsec چندسازنده را با جدول معادل (Proposal، DH، PFS، Lifetime، Selector) طراحی کنید.
2. Debug دو سمت (FortiGate و Cisco) را کنار هم بخوانید و Mismatch را بیابید.
3. تفاوت Selector (ACL/Crypto Map در برابر Route-based) را حل کنید.
4. NAT-T، ID و Lifetime را هماهنگ کنید.
5. جدول مغایرت (Mismatch Table) بسازید.
6. روش عیب‌یابی دوسمتی را اجرا کنید.

### چرا باید یاد بگیریم؟

وقتی یک سمت Fortinet و سمت دیگر Cisco است، پیام خطا از هر دو سمت بخشی از حقیقت را می‌گوید؛ مثل دو شاهد که هرکدام نیمی از ماجرا را دیده‌اند. مهارت اصلی خواندن هر دو Debug و مقایسه‌ی «چه پیشنهاد کردم» با «چه پذیرفتی» است. اشتباه رایج: فقط یک سمت را بررسی کردن.

### جدول معادل

| مفهوم | FortiGate | Cisco CSR |
|---|---|---|
| IKE نسخه | `ike-version 2` | `crypto ikev2 ...` |
| رمز P1 | `proposal aes256-sha256` | `encryption aes-cbc-256` + `integrity sha256` |
| DH | `dhgrp 14` | `group 14` |
| PFS | `pfs enable` + `dhgrp` | `set pfs group14` |
| Lifetime P1 | `keylife 86400` | `lifetime 86400` (ikev2 profile) |
| Lifetime P2 | `keylife-seconds 3600` | `set security-association lifetime seconds 3600` |
| Selector | `src-subnet/dst-subnet` | ACL در Crypto Map یا VTI 0.0.0.0/0 |
| ID محلی | `localid` | `identity local` |
| NAT-T | `nattraversal` | خودکار |

### مشکل Selector

حالت‌های ممکن:

| FortiGate | CSR | نتیجه |
|---|---|---|
| 0.0.0.0/0 (Route-based) | Crypto Map با ACL | IKEv2 TS: FGT 0/0 پیشنهاد، CSR ACL را می‌خواهد ⇒ معمولاً CSR جواب می‌دهد با Narrow؛ ممکن ناسازگار |
| دقیقاً 10.10/16↔10.20/16 | ACL همان | سازگار |
| 0.0.0.0/0 | VTI `tunnel mode ipsec` | سازگار (Route-based دو سمت) |

توصیه: هر دو Route-based (VTI) یا هر دو Selector دقیقاً یکسان.

### CSR با Crypto Map (Policy-based)

``` text
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

FortiGate مقابل با Selector دقیق:

``` text
config vpn ipsec phase2-interface
    edit "TO-CSR-P2"
        set phase1name "TO-CSR"
        set proposal aes256-sha256
        set pfs enable
        set dhgrp 14
        set src-subnet 10.10.0.0 255.255.0.0
        set dst-subnet 10.20.0.0 255.255.0.0
    next
end
```

### روش مقایسه‌ی Debug

1. فعال‌سازی هم‌زمان:

``` text
FortiGate: diagnose vpn ike log-filter dst-addr4 203.0.113.2 ; diagnose debug application ike -1 ; diagnose debug enable
CSR      : debug crypto ikev2 ; debug crypto ikev2 error ; terminal monitor
```

2. هم‌زمان ایجاد ترافیک.
3. جدول: «پیشنهاد Initiator» ⇄ «انتخاب Responder» ⇄ «خطا».
4. غیرفعال‌سازی: `diagnose debug disable` و `undebug all`.

### جدول مغایرت

| پارامتر | FGT | CSR | هماهنگ؟ | اقدام |
|---|---|---|---|---|
| Encryption | aes256 | aes-cbc-256 | بله | - |
| Integrity | sha256 | sha256 | بله | - |
| DH | 14 | 14 | بله | - |
| PFS | 14 | بدون | خیر | `set pfs group14` در CSR |
| Selector | 10.10/16↔10.20/16 | ACL مخالف جهت | خیر | اصلاح ACL |
| Lifetime P2 | 3600 | 28800 | کوچک‌تر برنده | هماهنگ |

### مثال‌های حل‌شده

#### مثال ساده — موفق

`show crypto ikev2 sa` ⇒ READY؛ `diagnose vpn ike gateway list` ⇒ established؛ ping 10.10.0.5↔10.20.0.5.

#### مثال متوسط — PFS

Phase2 رد: FGT PFS فعال، CSR بدون. Debug CSR: `Received no_proposal_chosen`. رفع: `set pfs group14` در CSR یا غیرفعال در FGT (ایمن‌تر: فعال در هر دو).

#### مثال متوسط — ACL معکوس

ACL سیسکو برای 10.20↔10.10 (جهت درست) ولی FGT Selector 10.10↔10.20: IKEv2 TS_UNACCEPTABLE. رفع: ACL و Selector آینه‌ای دقیق (Cisco ACL از دید خود: src=LAN محلی، dst=LAN دور).

#### مثال سخت — ID

FGT `localid` خالی (IP). CSR `match identity remote fqdn fgt.example`. `AUTHENTICATION_FAILED`. رفع: `match identity remote address 198.51.100.2` یا `set localid fgt.example` در FGT. Debug دو سمت ID را نشان می‌دهد.

#### مثال سخت — Lifetime و Rekey

FGT 86400؛ CSR 28800. Rekey هر ۸ ساعت، ولی اگر CSR زودتر Rekey کند و DPD/Make-before-break ناسازگار باشد، قطع‌های کوتاه. راه: Lifetime برابر و بررسی Rekey در Log؛ در زمان Rekey اختلال ثانیه‌ای بررسی شود.

### Lab هدایت‌شده (اجرا نشده)

1. IKEv2 FGT↔CSR (Route-based).
2. PFS/Selector Mismatch و رفع.
3. جدول مغایرت.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| no_proposal_chosen | PFS/الگوریتم | هماهنگ |
| TS_UNACCEPTABLE | Selector | آینه |
| AUTH_FAILED | ID/PSK | بررسی |
| قطع دوره‌ای | Lifetime | هماهنگ |

### نکات امنیتی

Debug هم‌زمان ولی کوتاه؛ PSK قوی؛ الگوریتم قوی؛ Log فقط لازم.

### جمع‌بندی

IPsec چندسازنده: جدول معادل، Selector آینه‌ای یا Route-based، ID، PFS و Lifetime؛ Debug دوسمتی و جدول مغایرت.

### تمرین و ارزیابی

**ت1.** (ساده) Mismatch رایج؟ *(پاسخ: 25-3-ت1)*

**ت2.** (ساده) چرا NTP؟ *(پاسخ: 25-3-ت2)*

**ت3.** (متوسط) Rekey قطع؟ *(پاسخ: 25-3-ت3)*

**ت4.** (متوسط) DPD؟ *(پاسخ: 25-3-ت4)*

**ت5.** (سخت) DPD کند. *(پاسخ: 25-3-ت5)*

**ت6.** (سخت، طراحی) Test Plan. *(پاسخ: 25-3-ت6)*

**Q1.** Quick quiz (English): Why synchronize clocks when comparing debugs from two vendors? *(پاسخ: 25-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DPD | Dead Peer Detection | تشخیص همتای مرده |

- *Compare both sides with synchronized clocks.* ← دو سمت را با ساعت‌های هماهنگ مقایسه کنید.

### کارت Lab

**کارت Lab:** Interop FGT–CSR (اجرا نشده). **Evidence:** `03-ops/interop.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: IPsec
- Cisco IOS-XE IKEv2

<a id="l-25-4"></a>

## درس 25-4 — آزمون معماری ۶ (FGT+CSR): IPsec چندسازنده، مقایسه‌ی Debug و جدول مغایرت — کلید پاسخ و Rubric

**فصل 25 · بازنویسی عمیق · پیش‌نیاز: ۲۵-۱ تا ۲۵-۳ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. تونل IKEv2 بین FortiGate و Cisco CSR1000v را طراحی کنید.
2. پارامترهای معادل را جدول‌بندی کنید.
3. Debug هر دو سمت را مقایسه و Mismatch را بیابید.
4. سه خرابی تزریق‌شده را رفع کنید.
5. گزارش و Rubric تحویل دهید.
6. صداقت را ثبت کنید.

### چرا باید یاد بگیریم؟

در دنیای واقعی طرف مقابل تونل همیشه Fortinet نیست. این آزمون نشان می‌دهد می‌توانید دو سازنده را کنار هم راه بیندازید، ناسازگاری را با Evidence پیدا و رفع کنید و گزارش بنویسید. اشتباه رایج «همه IPsec هستند» است؛ نام پارامترها، پیش‌فرض‌ها و Selector متفاوت است.

### صورت مسئله

FGT (`198.51.100.2`، LAN `10.10.0.0/16`) و CSR1000v (`203.0.113.2`، LAN `10.20.0.0/16`). IKEv2، AES-256، SHA-256، DH 14، PFS DH 14، Lifetime P1 86400، P2 3600.

عیب‌های تزریق‌شده:

1. PFS در FGT فعال و در CSR غیرفعال.
2. ACL CSR جهت معکوس.
3. Lifetime P2 ناسازگار (FGT 3600، CSR 28800) و NAT اشتباه روی Policy تونل در FGT.

### جدول معادل مرجع

| مفهوم | FortiGate | Cisco CSR |
|---|---|---|
| P1 | `proposal aes256-sha256`, `dhgrp 14` | `encryption aes-cbc-256`, `integrity sha256`, `group 14` |
| Auth | `psksecret` | keyring |
| Selector | `src-subnet/dst-subnet` | ACL crypto |
| P2 | `phase2-interface` | transform-set `esp-aes 256 esp-sha256-hmac` |
| PFS | `set pfs enable` | `set pfs group14` |
| Lifetime | `keylife` | `lifetime` |

### کلید پاسخ — تشخیص و رفع

**عیب ۱ (PFS):**

1. Evidence CSR: `debug crypto ikev2` ⇒ no_proposal_chosen در CREATE_CHILD_SA/Phase2.
2. Evidence FGT: Phase1 up، Phase2 down.
3. رفع: `set pfs group14` در CSR.
4. تأیید: `show crypto ipsec sa` ⇒ encaps/decaps.

**عیب ۲ (ACL):**

1. Evidence: TS_UNACCEPTABLE.
2. علت: ACL CSR: `permit ip 10.10.0.0 0.0.255.255 10.20.0.0 0.0.255.255` (جهت اشتباه).
3. رفع: ACL از دید CSR: src=10.20/16 dst=10.10/16.
4. تأیید: `show crypto ipsec sa` ⇒ `local ident (10.20/16) remote ident (10.10/16)`.

**عیب ۳ (Lifetime و NAT):**

1. Evidence: Rekey دوره‌ای قطع کوتاه؛ ترافیک تونل با Src NAT شده.
2. رفع: Lifetime برابر 3600 و `nat disable` در Policy تونل.
3. تأیید: Session بدون `snat`؛ Rekey بدون قطع قابل‌توجه.

### گزارش مقایسه‌ی Debug

| لحظه | FGT می‌گوید | CSR می‌گوید | نتیجه |
|---|---|---|---|
| IKE_SA_INIT | proposal ok | proposal ok | بله |
| IKE_AUTH | auth ok | auth ok | بله |
| CHILD_SA | no proposal | no_proposal_chosen | PFS |

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| جدول معادل | 15 |
| راه‌اندازی تونل | 20 |
| مقایسه‌ی Debug | 20 |
| رفع سه عیب | 25 |
| آزمون و گزارش | 10 |
| صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — ACL آینه

CSR ACL: `permit ip 10.20.0.0 0.0.255.255 10.10.0.0 0.0.255.255`. FGT Selector: src 10.10/16 dst 10.20/16. آینه‌ی هم‌اند.

#### مثال متوسط — RCA

``` text
Impact  : tunnel P2 down 40 min after change
Cause   : PFS mismatch (FGT on, CSR off)
Fix     : enable PFS group14 on CSR
Prevent : pre-change parameter sheet signed by both teams
```

#### مثال متوسط — اثبات NAT

Session FGT برای ping 10.10.0.5→10.20.0.5: `act=snat` ⇒ اشتباه. با `nat disable` Session بدون ترجمه.

#### مثال سخت — دو عیب هم‌زمان

PFS و ACL هر دو؛ Debug یک خطای اولی را نشان می‌دهد (no proposal) و دومی پنهان است تا اولی رفع شود. روش: رفع یکی ⇒ آزمون ⇒ بعدی.

#### مثال سخت — صداقت

Lab اجرا نشده؛ پیام‌های Debug نمونه‌ی آموزشی؛ گزارش «Unverified».

### Lab هدایت‌شده (اجرا نشده)

1. تونل FGT↔CSR.
2. سه عیب را رفع کنید.
3. جدول مقایسه و گزارش.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| P2 down | PFS | هماهنگ |
| TS_UNACCEPTABLE | ACL | آینه |
| Rekey قطع | Lifetime | برابر |
| src NAT | Policy | nat disable |

### جمع‌بندی

آزمون ۶: طراحی FGT↔CSR با جدول معادل؛ مقایسه‌ی Debug؛ سه عیب (PFS، ACL، Lifetime/NAT)؛ گزارش، Rubric و صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) Selector در Cisco چیست؟ *(پاسخ: 25-4-ت1)*

**ت2.** (ساده) DH گروه 14 یعنی؟ *(پاسخ: 25-4-ت2)*

**ت3.** (متوسط) P1 up و P2 down؛ علت؟ *(پاسخ: 25-4-ت3)*

**ت4.** (متوسط) Debug کجا؟ *(پاسخ: 25-4-ت4)*

**ت5.** (سخت) rekey Flap. *(پاسخ: 25-4-ت5)*

**ت6.** (سخت، طراحی) جدول معادل. *(پاسخ: 25-4-ت6)*

**Q1.** Quick quiz (English): Why must crypto ACL and FortiGate selectors mirror each other? *(پاسخ: 25-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DH | Diffie-Hellman | تبادل کلید |

- *Compare both sides debug output.* ← خروجی Debug دو سمت را مقایسه کنید.

### کارت Lab

**کارت Lab:** معماری ۶ (اجرا نشده). **Evidence:** `03-ops/arch6.md`.

### منابع

- Cisco IOS-XE IKEv2 guide
- Fortinet FortiOS 7.0 Administration Guide: IPsec

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

**چرا مدیریت مرکزی؟** با ۳ فایروال دستی ممکن است؛ با ۳۰ یک تغییر ساده ۳۰ ورود و ۳۰ فرصت خطا است. FortiManager پیکربندی (Policy Package) و FortiAnalyzer Log را مرکزی می‌کند. هر دو Needs-License؛ جایگزین بدون لایسنس: Git + rsyslog.

**ریسک:** نقطه‌ی مرکزی هدف جذاب مهاجم است؛ Hardening، شبکه‌ی Mgmt جدا، MFA و Backup خود FMG الزامی.

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

#### مثال ساده — تصمیم

≤5 دستگاه: Git+rsyslog؛ 6 تا 20: ارزیابی؛ بیش از 20: FMG/FAZ.

#### مثال متوسط — Policy Package

یک Package «Branch-Standard» روی ۱۰ شعبه؛ Object خاص هر شعبه با Meta Variable.

#### مثال سخت — ADOM

جداسازی مشتریان: ادمین A به Log B دسترسی ندارد.

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

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. نقش FortiManager (FMG) و FortiAnalyzer (FAZ) را تفکیک کنید.
2. معماری، ADOM، Device Manager، Policy Package و Provisioning Template را توضیح دهید.
3. وابستگی لایسنس (Device License، VM در برابر Hardware) را بشناسید.
4. تصمیم «ابزار یا جایگزین» (Syslog + Git + Ansible) را با تحلیل هزینه و ریسک بگیرید.
5. مدل استقرار (HA، فاصله‌ی شبکه، Fabric) را بشناسید.
6. ریسک‌های مدیریت مرکزی (SPOF، دسترسی بالا) را کنترل کنید.

### چرا باید یاد بگیریم؟

اگر ۵ فایروال دارید، مدیریت تک‌تک ممکن است. با ۵۰ فایروال، هر تغییر Policy ۵۰ ورود و ۵۰ احتمال اشتباه است. FortiManager مثل «دفتر مرکزی» است که یک Policy را برای همه توزیع می‌کند؛ FortiAnalyzer «بایگانی و تحلیل‌گر» است که Logها را جمع می‌کند. ولی هر دو لایسنس و هزینه دارند و خودشان هدف حمله‌ی پرارزش‌اند (کنترل همه‌ی فایروال‌ها). تصمیم باید آگاهانه باشد: گاهی Syslog + Git + Ansible کافی و ارزان‌تر است.

### نقش‌ها

| ابزار | وظیفه | خروجی |
|---|---|---|
| FortiManager (FMG) | مدیریت Config مرکزی، Policy Package، Template، Firmware | یک نقطه‌ی تغییر |
| FortiAnalyzer (FAZ) | جمع‌آوری Log، گزارش، رویداد، IOC | دید و Compliance |
| FortiGate | اجرا | ترافیک |

### مفاهیم FMG

| مفهوم | معنی |
|---|---|
| ADOM | Administrative Domain؛ جداسازی دستگاه‌ها/Tenantها |
| Device Manager | فهرست دستگاه‌ها و وضعیت |
| Policy Package | مجموعه Policy که روی چند دستگاه اعمال می‌شود |
| Provisioning/System Template | قالب Interface/DNS/NTP |
| Install | ارسال Config به دستگاه |
| Revision | نسخه‌ی تاریخی Config |
| Firmware Management | ارتقا مرکزی |

جریان کار:

``` text
Edit Policy Package -> Install Preview -> Install -> Verify on device -> Revision saved
```

### مفاهیم FAZ

| مفهوم | معنی |
|---|---|
| Log Storage | آنلاین/آرشیو |
| ADOM | تفکیک Logها |
| FortiView/Reports | تحلیل |
| Event Handler | هشدار |
| Fabric/Security Rating | نمای سازمانی |

### لایسنس (کلیات؛ مدل را در مستند بررسی کنید)

| مورد | نکته |
|---|---|
| FMG/FAZ Hardware یا VM | VM بر اساس تعداد Device/ظرفیت لاگ لایسنس می‌شود |
| Device License | تعداد دستگاه مدیریت‌شده |
| ADOM | تعداد ADOM به لایسنس/مدل |
| Log GB/Day | ظرفیت FAZ |
| Support (FortiCare) | به‌روزرسانی/Patch |

(Needs-License؛ در این دوره Lab بدون FMG/FAZ، همه‌ی بخش‌ها «اجرا نشده».)

### تصمیم: ابزار یا جایگزین

| معیار | FMG/FAZ | Syslog + Git + Ansible |
|---|---|---|
| هزینه | لایسنس | کمتر (زمان مهندسی) |
| یکپارچگی با Fortinet | کامل | نیازمند توسعه |
| Policy Package | آماده | دستی/Template |
| Log Analytics | FortiView | ELK/Graylog |
| Compliance گزارش | آماده | ساخت |
| مهارت | Fortinet | DevOps |
| مقیاس | زیاد | بسته به پروژه |

قاعده‌ی تجربی: زیر ~۱۰ دستگاه، با تیم DevOps ⇒ جایگزین؛ ۵۰+ دستگاه یا Compliance سخت ⇒ FMG/FAZ.

### مثال‌های حل‌شده

#### مثال ساده — تغییر Policy

۲۰ شعبه، یک Policy جدید: در FMG یک بار Policy Package، Install Preview و Install؛ ۲۰ دستگاه. بدون FMG: ۲۰ ورود.

#### مثال متوسط — ADOM

MSP با ۳ مشتری: ADOM جدا برای هر مشتری، Admin جدا؛ مشتری A Config B را نمی‌بیند.

#### مثال متوسط — هزینه

۱۲ دستگاه؛ لایسنس FMG-VM + FAZ-VM سالانه X؛ جایگزین: rsyslog + Git + Ansible (۱۰ نفر-روز راه‌اندازی + ۱ نفر-روز در ماه). تصمیم: جایگزین، با طرح مهاجرت.

``` text
Break-even = license cost per year / (engineer cost per day x maintenance days)
```

#### مثال سخت — ریسک FMG

FMG هک می‌شود ⇒ مهاجم Config ۵۰ دستگاه را تغییر می‌دهد. کنترل‌ها: MFA، دسترسی فقط از Mgmt، Trusted Host، Log Audit، Backup آفلاین، RBAC، Install فقط با Approval (Workflow Mode).

#### مثال سخت — HA

FMG تک ⇒ SPOF مدیریتی (ترافیک اثر ندارد ولی مدیریت قطع). راه: FMG HA، Backup دوره‌ای، دسترسی مستقیم اضطراری (Break-glass) به فایروال‌ها. FAZ: Log Forward/HA برای عدم از دست‌رفتن Log.

### Lab هدایت‌شده (اجرا نشده)

1. معماری FMG/FAZ را رسم کنید.
2. Break-even را محاسبه کنید.
3. ریسک و کنترل را جدول کنید.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Install ناموفق | Conflict/Revision | Preview |
| Log نمی‌رسد | Reliable/FW | بررسی |
| دستگاه Out of Sync | تغییر مستقیم | Retrieve/Import |
| هزینه بالا | لایسنس | جایگزین |

### نکات امنیتی

دسترسی FMG/FAZ به شبکه‌ی Mgmt؛ MFA؛ Workflow؛ Backup؛ Break-glass؛ Audit Log.

### جمع‌بندی

FMG مدیریت Config، FAZ Log؛ ADOM/Policy Package؛ لایسنس؛ تصمیم با هزینه و ریسک؛ FMG خودش هدف حمله است و باید سخت شود.

### تمرین و ارزیابی

**ت1.** (ساده) تفاوت FMG و FAZ؟ *(پاسخ: 26-1-ت1)*

**ت2.** (ساده) ADOM چه کاری می‌کند؟ *(پاسخ: 26-1-ت2)*

**ت3.** (متوسط) چرا Install Preview لازم است؟ *(پاسخ: 26-1-ت3)*

**ت4.** (متوسط) دو محدودیت مستند FMG/FAZ؟ *(پاسخ: 26-1-ت4)*

**ت5.** (سخت) ۱۲ فایروال و ۲۰ تغییر در ماه با ۳٪ خطا؛ هزینه‌ی خطا چقدر است و تصمیم؟ *(پاسخ: 26-1-ت5)*

**ت6.** (سخت، طراحی) معماری برای ۴ مشتری ۳۰ فایروال. *(پاسخ: 26-1-ت6)*

**Q1.** Quick quiz (English): Why is a central manager both a benefit and a risk? *(پاسخ: 26-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FMG | FortiManager | مدیریت مرکزی |
| FAZ | FortiAnalyzer | تحلیل Log |
| ADOM | Administrative Domain | دامنه‌ی مدیریتی |
| Break-glass | Break-glass access | دسترسی اضطراری |

- *Preview changes before installing a policy package.* ← قبل از نصب Policy Package تغییرات را پیش‌نمایش کنید.

### کارت Lab

**کارت Lab:** سند تصمیم FMG/FAZ. **وضعیت:** طراحی (Needs-License). **Evidence:** `02-design/fmg-faz.md`.

### منابع

- [Device Manager](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/478145/device-manager)
- [Add FortiAnalyzer](https://docs.fortinet.com/document/fortimanager/7.0.0/administration-guide/654379/add-fortianalyzer)
- [Installing policy packages](https://docs.fortinet.com/document/fortimanager/7.0.7/administration-guide/153046/installing-policy-packages-and-device-settings)

<a id="l-26-2"></a>

## درس 26-2 — Syslog مرکزی (جایگزین FAZ): FortiGate → rsyslog با TCP/TLS، قالب، Parse، Retention و آزمون

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۰، ۲۶-۱، ۲۷-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 / FortiManager-FortiAnalyzer 7.0 (Needs-License؛ بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. FortiGate را به‌عنوان Syslog Client با TCP/TLS (Reliable) تنظیم کنید.
2. rsyslog را به‌عنوان Collector (دریافت، قالب، ذخیره) پیکربندی کنید.
3. قالب Log FortiGate (Key=Value) را Parse کنید.
4. Retention، Rotation و حجم را برنامه‌ریزی کنید.
5. آزمون انتها‌به‌انتها (ارسال → دریافت → جست‌وجو) را اجرا کنید.
6. محدودیت‌های جایگزین FAZ را بدانید.

### چرا باید یاد بگیریم؟

Log فقط روی دستگاه، مثل دفتر ثبت پشت در که اگر مهاجم در را بشکند، دفتر را هم می‌سوزاند. Log باید فوراً به جای امن دیگری برود. وقتی FAZ لایسنس نیست، rsyslog و Syslog روی Linux راه‌حل ارزان و قدرتمندی است؛ فقط باید قابل‌اعتماد (TCP/TLS)، قابل‌جست‌وجو و با Retention مشخص باشد.

### جریان

``` text
FortiGate --(TCP 6514 TLS)--> rsyslog (Linux) --> files / Elasticsearch / Graylog
```

UDP 514 ساده ولی بدون تضمین؛ در شبکه‌ی شلوغ Log گم می‌شود. TCP/TLS (Reliable) برای Production.

### FortiGate (Client)

``` text
config log syslogd setting
    set status enable
    set server "10.50.0.20"
    set mode reliable
    set port 6514
    set facility local7
    set format default
    set enc-algorithm high
end
config log syslogd filter
    set severity information
    set forward-traffic enable
    set local-traffic enable
    set anomaly enable
end
```

(TLS در FortiOS 7.0 با `mode reliable` و `enc-algorithm`؛ CA/Certificate را در مستند بررسی کنید؛ Unverified.)

### rsyslog (Collector)

``` text
# /etc/rsyslog.d/10-fortigate.conf
module(load="imtcp"
       StreamDriver.Name="gtls"
       StreamDriver.Mode="1"
       StreamDriver.AuthMode="x509/name")
global(
  DefaultNetstreamDriver="gtls"
  DefaultNetstreamDriverCAFile="/etc/rsyslog.d/ca.pem"
  DefaultNetstreamDriverCertFile="/etc/rsyslog.d/server.pem"
  DefaultNetstreamDriverKeyFile="/etc/rsyslog.d/server.key")
input(type="imtcp" port="6514")

template(name="FgtPerHost" type="string"
         string="/var/log/fortigate/%HOSTNAME%/%$YEAR%-%$MONTH%-%$DAY%.log")
if $fromhost-ip startswith '10.' then {
   action(type="omfile" dynaFile="FgtPerHost")
   stop
}
```

(حداقل نمونه؛ در Production AuthMode و Firewall دقیق‌تر.)

### قالب Log

``` text
date=2026-11-27 time=10:15:01 devname="FGT-A" logid="0000000013" type="traffic" subtype="forward" level="notice"
srcip=10.10.0.5 srcport=50000 dstip=198.51.100.8 dstport=443 policyid=30 action="accept" proto=6 sentbyte=1200 rcvdbyte=9800
```

ساختار Key=Value ⇒ با Grok/Regex/Logstash قابل Parse.

``` text
grep 'policyid=30' /var/log/fortigate/FGT-A/2026-11-27.log | grep 'action="deny"'
```

### Retention و حجم

``` text
Daily volume = events/sec x avg bytes x 86400
Example: 500 ev/s x 500 B x 86400 = 21.6 GB/day
90 days = 1.94 TB (before compression)
```

با فشرده‌سازی ۸:۱ حدود ۲۴۰ گیگابایت. `logrotate` روزانه + `compress` + حذف پس از N روز؛ آرشیو سرد برای الزامات حقوقی.

``` text
# /etc/logrotate.d/fortigate
/var/log/fortigate/*/*.log {
    daily
    rotate 90
    compress
    missingok
    notifempty
}
```

### آزمون انتها‌به‌انتها

1. FortiGate: `execute log test`/ترافیک واقعی.
2. Collector: `ss -tnp | grep 6514`.
3. `tail -f /var/log/fortigate/FGT-A/...`.
4. جست‌وجوی سیاست خاص.
5. قطع Collector و بازگشت: آیا Log بافر می‌شود؟ (FortiGate بافر محدود دارد.)

### مثال‌های حل‌شده

#### مثال ساده — گرفتن Log

ترافیک Policy 30 ⇒ خط Log در فایل روز. جست‌وجو با policyid.

#### مثال متوسط — حجم

۵۰۰ ev/s ⇒ ۲۱٫۶GB در روز؛ فضا برای ۹۰ روز بعد از فشرده‌سازی ≈ ۲۴۰GB. دیسک ۵۰۰GB با حاشیه OK.

#### مثال متوسط — UDP یا TCP

UDP: در ازدحام ۵٪ Log گم شد. با TCP/TLS: بدون گم‌شدن (تا بافر). برای ممیزی TCP/TLS.

#### مثال سخت — قطع Collector

Collector ۲ ساعت Down؛ FortiGate Log را فقط تا ظرفیت بافر نگه می‌دارد؛ بخشی از دست می‌رود. راه: دو Collector (`server` و `second-server`)، ذخیره‌ی محلی به‌عنوان پشتیبان، آلارم قطع.

#### مثال سخت — محدودیت جایگزین

FAZ تحلیل آماده (FortiView، IOC، Compliance) می‌دهد؛ rsyslog فقط ذخیره. برای تحلیل: Graylog/ELK و Dashboard. هزینه‌ی مهندسی را حساب کنید. همچنین Time-sync و Parse نسخه‌ها.

### Lab هدایت‌شده (اجرا نشده)

1. rsyslog Collector.
2. FortiGate Reliable.
3. آزمون و Logrotate.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Log نمی‌رسد | Firewall/پورت | 6514 |
| TLS خطا | CA/زمان | همگام |
| فایل رشد | rotate | logrotate |
| گم‌شدن | UDP | TCP |

### نکات امنیتی

TLS؛ دسترسی Collector محدود؛ Log فقط‌خواندنی؛ Integrity (Hash)؛ Retention طبق قانون؛ جدا از سیستم عملیاتی.

### جمع‌بندی

Syslog مرکزی با TCP/TLS و rsyslog؛ قالب Key=Value و Parse؛ Retention با محاسبه‌ی حجم؛ آزمون انتها‌به‌انتها؛ جایگزین FAZ بدون تحلیل آماده.

### تمرین و ارزیابی

**ت1.** (ساده) چرا `mode reliable`؟ *(پاسخ: 26-2-ت1)*

**ت2.** (ساده) `source-ip` چه کمکی می‌کند؟ *(پاسخ: 26-2-ت2)*

**ت3.** (متوسط) حجم 8M رویداد در روز با 450 B و Retention 90 روز چقدر است؟ *(پاسخ: 26-2-ت3)*

**ت4.** (متوسط) Log نمی‌رسد؛ سه آزمون به ترتیب. *(پاسخ: 26-2-ت4)*

**ت5.** (سخت) قطع ۱۰ دقیقه‌ای سرور Logهای آن بازه را از بین برد؛ راه‌حل. *(پاسخ: 26-2-ت5)*

**ت6.** (سخت، طراحی) معماری Log برای ۱۰ فایروال با ۱۸۰ روز Retention. *(پاسخ: 26-2-ت6)*

**Q1.** Quick quiz (English): Why is UDP syslog unsuitable for critical firewall logs? *(پاسخ: 26-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| rsyslog | rsyslog | سرویس Syslog لینوکس |
| RFC5424 | Syslog protocol format | قالب استاندارد Syslog |
| CEF | Common Event Format | قالب رویداد مشترک |

- *Alert when a device stops sending logs.* ← وقتی دستگاه Log نمی‌فرستد هشدار بدهید.

### کارت Lab

**کارت Lab:** Syslog. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/syslog.md`.

### منابع

- [config log syslogd setting](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/456620/config-log-syslogd-setting)
- RFC 5424
- rsyslog documentation

<a id="l-26-3"></a>

## درس 26-3 — Backup خودکار و مدیریت Config با Git: Sanitize، Diff، Audit، Restore و Drift

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۰، ۲۷-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 / FortiManager-FortiAnalyzer 7.0 (Needs-License؛ بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Backup خودکار Config را (API/SSH/Scheduler) طراحی کنید.
2. Sanitize (حذف Secret) را قبل از ذخیره در Git اجرا کنید.
3. Diff و Audit را برای کشف تغییر غیرمجاز به‌کار ببرید.
4. Restore و تأیید آن را آزمون کنید.
5. Config Drift (انحراف از Baseline) را تشخیص دهید.
6. برنامه‌ی نگهداری (Retention، رمزگذاری، دسترسی) را بنویسید.

### چرا باید یاد بگیریم؟

Backup قدیمی مثل بیمه‌ای است که هرگز ادعا نکرده‌اید: تا وقتی نیاز نشده، نمی‌دانید کار می‌کند یا نه. دو مشکل رایج: Backup دستی که فراموش می‌شود، و Backup که در Git می‌رود و رمز/PSK را لو می‌دهد. ترکیب Backup خودکار + Sanitize + Git + Diff، هم ردپای تغییرات را می‌دهد و هم کشف تغییر غیرمجاز را ممکن می‌کند. این Pattern «Config as Code» است.

### جریان

``` text
Scheduler -> backup script (API/SSH) -> sanitize -> git commit -> diff report -> alert on unexpected change
                                   \-> encrypted full backup (offline vault)
```

### دو نوع Backup

| نوع | محتوا | محل |
|---|---|---|
| Full (با Secret) | برای Restore واقعی | رمزگذاری‌شده، آفلاین/Vault |
| Sanitized | بدون Secret | Git برای Diff/Audit |

هیچ‌گاه Full را در Git ننویسید.

### Backup با API

``` text
curl -sk -H "Authorization: Bearer <API_TOKEN>" \
  "https://10.50.0.1/api/v2/monitor/system/config/backup?scope=global" -o fgt-a.conf
```

توکن در Vault؛ API User با Profile فقط برای Backup و Trusted Host فقط سرور Backup.

### Sanitize

مواردی که باید حذف/ماسک شوند: `set password ENC ...`، `set psksecret ENC ...`، `set secret`، `set passwd`، گواهی خصوصی.

``` text
sed -E 's/(set (password|psksecret|passwd|secret|private-key) ).*/\1<REDACTED>/' fgt-a.conf > fgt-a.sanitized.conf
```

بررسی: `grep -E 'ENC |private-key' fgt-a.sanitized.conf` باید خالی باشد.

### Git و Diff

``` text
cd /srv/fgt-config
cp /tmp/fgt-a.sanitized.conf ./fgt-a.conf
git add fgt-a.conf
git diff --stat HEAD
git commit -m "backup 2026-11-27 FGT-A"
git diff HEAD~1 -- fgt-a.conf
```

Diff روزانه می‌گوید «چه چیزی عوض شد». اگر تغییر با Ticket (CHG) مطابقت نداشت: هشدار.

### Drift

Baseline: Config تأییدشده (Golden). Drift: هر تفاوت از Baseline.

``` text
diff <(grep -v '^#' baseline.conf) <(grep -v '^#' current.conf)
```

نکته: خطوط غیرقطعی (timestamp، uuid) فیلتر شوند.

### Restore و آزمون

``` text
# GUI: System > Configuration > Restore
# CLI:
execute restore config tftp fgt-a.conf <server>
```

آزمون دوره‌ای (فصلی) Restore روی دستگاه Lab: بوت، Policy، Route، VPN. «Backup که Restore نشده، Backup نیست».

### مثال‌های حل‌شده

#### مثال ساده — Diff

``` text
+ edit 305
+     set name "TEMP-ANY"
+     set srcaddr "all"
+     set dstaddr "all"
+     set service "ALL"
```

تغییر ناخواسته (Policy ALL). Alert ⇒ بررسی ⇒ حذف.

#### مثال متوسط — Sanitize

PSK در فایل Git ماند ⇒ حادثه‌ی نشت. راه: pre-commit hook که `ENC ` را پیدا کند و Commit را رد کند.

``` text
# .git/hooks/pre-commit
if grep -qE 'ENC |private-key' *.conf; then echo "secret found"; exit 1; fi
```

#### مثال متوسط — Retention

۳۰ روز روزانه + ۱۲ ماه ماهانه؛ رمزگذاری با GPG؛ کپی خارج از سایت.

#### مثال سخت — Restore ناموفق

Restore Config روی نسخه‌ی متفاوت FortiOS شکست یا بخشی از Config ردشد. راه: Backup همراه نسخه؛ Restore روی همان نسخه؛ آزمون فصلی؛ ثبت نسخه در نام فایل.

#### مثال سخت — Drift هدفمند

تیم عملیات در اضطرار روی فایروال Policy اضافه کرد (بدون CHG). Diff شبانه تشخیص داد. فرایند: ثبت بعدی CHG، بازبینی، یا Rollback. Policy: «Break-glass تغییر» با گزارش بعدی.

### Lab هدایت‌شده (اجرا نشده)

1. اسکریپت Backup و Sanitize.
2. Git و Diff.
3. Restore در Lab.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Secret در Git | Sanitize ناقص | hook |
| Diff پر از نویز | timestamp | فیلتر |
| Restore شکست | نسخه | هم‌نسخه |
| Backup نشد | Token/Trusted | بررسی |

### نکات امنیتی

Full رمزگذاری و آفلاین؛ Git خصوصی با MFA؛ دسترسی Read-only؛ Audit؛ تست Restore فصلی.

### جمع‌بندی

Config as Code: Backup خودکار + Sanitize + Git + Diff؛ Full رمزگذاری‌شده؛ Drift و Audit؛ Restore آزمون‌شده.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Backup بدون Restore کافی نیست؟ *(پاسخ: 26-3-ت1)*

**ت2.** (ساده) Drift یعنی چه؟ *(پاسخ: 26-3-ت2)*

**ت3.** (متوسط) Sanitizer باید چه الگوهایی را پاک کند؟ *(پاسخ: 26-3-ت3)*

**ت4.** (متوسط) چرا Tag قبل از Change؟ *(پاسخ: 26-3-ت4)*

**ت5.** (سخت) Secret در Git Commit شد؛ مراحل اقدام. *(پاسخ: 26-3-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Backup/Restore با RTO هدف ۳۰ دقیقه. *(پاسخ: 26-3-ت6)*

**Q1.** Quick quiz (English): Why is removing a secret from Git history not enough after it was committed? *(پاسخ: 26-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Drift | Configuration drift | انحراف پیکربندی |
| Sanitize | Sanitize config | پاک‌سازی Secret |
| RTO | Recovery Time Objective | زمان هدف بازیابی |

- *Never commit secrets to a repository.* ← هرگز Secret را در مخزن Commit نکنید.

### کارت Lab

**کارت Lab:** Backup/Git. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/backup.md`.

### منابع

- Git documentation
- NIST SP 800-53 CM-2/CM-3
- Fortinet Docs: Backup and restore (7.0)

<a id="l-26-4"></a>

## درس 26-4 — طراحی معماری ۹ (مدیریت مرکزی و عملیات): RBAC، Change، Audit و آزمون با Rubric

**فصل 26 · بازنویسی عمیق · پیش‌نیاز: ۲۶-۱ تا ۲۶-۳، ۳۲-۱ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری مدیریت مرکزی و عملیات (RBAC، Change، Audit، Backup، Log) را طراحی کنید.
2. نقش‌ها و Admin Profile حداقلی تعریف کنید.
3. فرایند Change (Request، Review، Window، Rollback، Verify) را بنویسید.
4. Audit و گزارش را مستند کنید.
5. سه عیب تزریق‌شده را در Gate رفع کنید.
6. Rubric را اجرا و صداقت را ثبت کنید.

### چرا باید یاد بگیریم؟

بیشتر حوادث امنیتی/قطعی از «عملیات» می‌آید نه از فناوری: دسترسی زیاد، تغییر بدون Review، بی‌Audit، بی‌Backup. معماری مدیریت یعنی قانون‌گذاری برای همین‌ها. مثل قانون ساختمان: هر کارگر کلید همه‌ی اتاق‌ها را ندارد، هر تغییر مجوز می‌خواهد، و دفتری ثبت می‌کند چه کسی چه کرد.

### RBAC — نقش‌ها

| نقش | دسترسی | Profile (مثال) |
|---|---|---|
| NOC-Read | فقط خواندن | `prof_readonly` |
| Net-Ops | Policy/Route غیرحساس | `prof_netops` |
| Sec-Admin | UTM/VPN/Auth | `prof_secadmin` |
| Super-Admin | همه (کم و با MFA) | `super_admin` |
| Auditor | Log و Config فقط‌خواندنی | `prof_audit` |
| Automation | API فقط Backup | `prof_api_backup` |

``` text
config system accprofile
    edit "prof_readonly"
        set secfabgrp read
        set ftviewgrp read
        set authgrp read
        set sysgrp read
        set netgrp read
        set loggrp read
        set fwgrp read
        set vpngrp read
        set utmgrp read
        set wifi read
    next
end
config system admin
    edit "noc-alice"
        set accprofile "prof_readonly"
        set trusthost1 10.50.0.0 255.255.255.0
        set two-factor fortitoken
    next
end
```

اصل: Least Privilege، `trusthost`، MFA، حساب شخصی (نه مشترک)، Break-glass فقط یکی با رمز در Vault.

### فرایند Change

``` text
1 Request (ticket CHG-xxx: what, why, risk, rollback)
2 Review/Approval (peer + owner)
3 Window (approved time)
4 Pre-check + Backup
5 Implement
6 Verify (test list)
7 Close (evidence, update docs)
8 Post-implementation review (if failed)
```

Change اضطراری (Emergency) با تأیید سریع و Review بعدی.

### Audit

| سؤال | منبع |
|---|---|
| چه کسی؟ | Admin Log (`logid` Config change) |
| چه چیزی؟ | Diff در Git |
| چرا؟ | Ticket |
| چه زمانی؟ | Log |
| نتیجه؟ | Verify |

گزارش ماهانه: تغییرات، Break-glass، ورودهای ناموفق، Policy بدون Owner.

### Gate — صورت مسئله

سازمان ۱۵ فایروال، ۸ ادمین، بدون فرایند. باید: RBAC، Change، Backup/Audit، Log مرکزی طراحی و ثابت شود.

عیب‌های تزریق‌شده:

1. همه‌ی ادمین‌ها `super_admin` و حساب مشترک `admin`.
2. تغییر در Production بدون Ticket (Policy ALL موقت).
3. Backup فقط دستی و Restore آزمون‌نشده.

### کلید پاسخ

| عیب | Evidence | رفع |
|---|---|---|
| ۱ | `show system admin` | Profile حداقلی، حساب شخصی، MFA، Trusthost |
| ۲ | Diff Git و Log Admin | Policy حذف؛ فرایند Change؛ Alert روی Policy جدید |
| ۳ | تاریخ آخرین Backup | Backup خودکار + آزمون Restore فصلی |

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| RBAC | 20 |
| فرایند Change | 20 |
| Audit/Log | 15 |
| Backup/Restore | 15 |
| رفع سه عیب | 20 |
| مستندسازی/صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Profile

NOC فقط می‌خواند. تلاش `config firewall policy` ⇒ Permission denied. آزمون منفی RBAC.

#### مثال متوسط — Change

CHG-601: افزودن Policy HTTPS به سرور جدید. Review، Window شنبه ۲۲:۰۰، Backup، اجرا، Verify (`iprope lookup`)، Close.

``` text
Rollback plan: delete policy 340; restore backup fgt-a-2026-11-27.conf
```

#### مثال متوسط — Audit

Log: `user=bob action=Edit cfgpath=firewall.policy cfgobj=305`. Ticket نیست ⇒ بررسی. نتیجه: تغییر اضطراری؛ ثبت بعدی و Review.

#### مثال سخت — حساب مشترک

سه نفر با `admin`. حادثه: Policy ALL ایجاد شد؛ نمی‌توان فهمید چه کسی. راه: حساب شخصی، حذف/غیرفعال admin (یا Break-glass)، Audit.

#### مثال سخت — Emergency Change

قطعی ساعت ۲ شب؛ Emergency Change با تأیید تلفنی مدیر؛ انجام؛ فردا Review و مستند. بدون این، یا قطعی طولانی یا تغییر پنهان.

### Lab هدایت‌شده (اجرا نشده)

1. Profile و Admin.
2. فرایند Change و یک CHG نمونه.
3. گزارش Audit.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| همه Super | RBAC نیست | Profile |
| تغییر بی‌Ticket | فرایند | Alert/Policy |
| Restore نشد | آزمون نیست | فصلی |
| حساب مشترک | ردگیری | شخصی |

### نکات امنیتی

MFA، Trusthost، Break-glass، Log مرکزی، Backup رمزگذاری‌شده، بازبینی فصلی دسترسی.

### جمع‌بندی

معماری مدیریت: RBAC حداقلی، Change با Ticket/Review/Rollback، Audit، Backup آزمون‌شده، Log مرکزی؛ سه عیب و Rubric؛ صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) ADOM؟ *(پاسخ: 26-4-ت1)*

**ت2.** (ساده) چرا Revision؟ *(پاسخ: 26-4-ت2)*

**ت3.** (متوسط) Install Preview؟ *(پاسخ: 26-4-ت3)*

**ت4.** (متوسط) چرا مرکز هدف است؟ *(پاسخ: 26-4-ت4)*

**ت5.** (سخت) Install قطع کرد؛ رفع. *(پاسخ: 26-4-ت5)*

**ت6.** (سخت، طراحی) RBAC چهارسطحی. *(پاسخ: 26-4-ت6)*

**Q1.** Quick quiz (English): Why use install preview before pushing a policy package? *(پاسخ: 26-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ADOM | Administrative Domain | دامنه‌ی مدیریتی |

- *Review the diff before installing.* ← قبل از Install تفاوت‌ها را بازبینی کنید.

### کارت Lab

**کارت Lab:** معماری ۹ (اجرا نشده؛ Needs-License). **Evidence:** `02-design/arch9.md`.

### منابع

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

**چرا Baseline؟** پزشک وقتی می‌گوید «فشار 160 بالاست» که بداند فشار نرمال شما 120 است. در شبکه هم «CPU 60٪» برای یک دستگاه عادی و برای دستگاه دیگر فاجعه است. Baseline یعنی ثبت رفتار عادی تا انحراف را تشخیص دهید.

**سه پرسش:** چه چیزی را اندازه بگیریم (CPU، Session، پهنای باند، خطا)؟ هر چند وقت؟ چه عددی «هشدار» است؟ آستانه‌ی خوب از دو چیز می‌آید: ظرفیت دستگاه (دیتاشیت) و رفتار واقعی (P95). P95 یعنی ۹۵٪ زمان مقدار کمتر یا مساوی آن بود؛ ۵٪ اوج‌های لحظه‌ای حذف می‌شوند تا گمراه نکنند.

**Alert Fatigue:** اگر روزی ۲۰۰ هشدار بیاید هیچ‌کس نمی‌خواند. هر هشدار باید **اقدام‌پذیر** باشد و دوره‌ی تحمل داشته باشد (مثلاً ۱۰ دقیقه).

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

#### مثال ساده — ساخت Baseline

داده‌ی ۷ روز: CPU میانگین 18٪، P95 = 41٪؛ Session میانگین 25,000 و Peak 38,000؛ ظرفیت 200,000.

#### مثال متوسط — آستانه

``` text
Session warn = 0.5 x 200000 = 100000
Session crit = 0.8 x 200000 = 160000
CPU warn     = P95 x 1.5   = 41 x 1.5 ~ 61 %
```

مراحل: ظرفیت ← درصد ← P95 ← ضریب ← مدت پایداری.

#### مثال سخت — فصلی

پایان ماه ترافیک ۳ برابر است. Baseline جدا برای «روز عادی» و «پایان ماه» یا آستانه‌ی وابسته به تقویم؛ وگرنه هر ماه هشدار کاذب.

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

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. انواع Log (Traffic، Event، Security/UTM، Local Traffic) را تفکیک کنید.
2. سطح ثبت Policy (`logtraffic all/utm/disable`) را درست انتخاب کنید.
3. ذخیره‌ی محلی (Memory/Disk) و مقصدهای ارسال را بشناسید.
4. حجم و Retention را محاسبه و طراحی کنید.
5. Implicit Deny و Local-in Log را فعال کنید.
6. Log را فیلتر و تفسیر کنید.

### چرا باید یاد بگیریم؟

Log «جعبه‌ی سیاه» شبکه است. بعد از حادثه، تنها منبع حقیقت است. ولی Log زیاد، دیسک را پر می‌کند و CPU می‌خورد؛ Log کم، شما را کور می‌کند. تعادل: چه چیز با چه سطحی، کجا، تا کی. بدون این طراحی، «Log همه‌چیز» و «هیچ‌چیز پیدا نمی‌شود» هر دو اتفاق می‌افتد.

### انواع Log

| نوع | محتوا | مثال |
|---|---|---|
| Traffic (Forward) | Sessionهای عبوری | accept/deny، بایت |
| Local Traffic | ترافیک به/از خود FortiGate | SSH به FGT، DNS |
| Event | رویداد سیستم | ورود Admin، تغییر Config، HA، VPN |
| Security (UTM) | AV، Web Filter، IPS، App Control | بلاک، شناسایی |
| Anomaly | DoS Policy | SYN Flood |

### سطح ثبت

| تنظیم Policy | معنی |
|---|---|
| `logtraffic all` | همه‌ی Sessionها (شروع/پایان) |
| `logtraffic utm` | فقط رویدادهای UTM |
| `logtraffic disable` | هیچ |

``` text
config firewall policy
    edit 30
        set logtraffic all
        set logtraffic-start disable
    next
end
config log setting
    set fwpolicy-implicit-log enable
    set local-in-allow disable
    set local-in-deny-unicast enable
    set local-in-deny-broadcast disable
end
```

`logtraffic-start`: Log هنگام شروع Session (بار بیشتر)؛ معمولاً فقط پایان کافی.

### سطح Severity

Emergency، Alert، Critical، Error، Warning، Notification، Information، Debug. برای مقصد: `severity information` مناسب؛ `debug` فقط موقت.

### ذخیره‌ی محلی

``` text
config log disk setting
    set status enable
    set ullogd-ram-cache enable
    set max-log-file-size 100
    set storage ...
end
config log memory setting
    set status enable
end
```

(مدل‌ها بدون دیسک فقط Memory محدود دارند؛ Log را به مرکز بفرستید.)

``` text
execute log filter category 0
execute log filter field action deny
execute log filter start-line 1
execute log display
get log disk setting
```

### محاسبه‌ی حجم

``` text
Events/day = sessions per second x 86400
Volume/day = events/day x avg log size

500 sessions/s x 86400 = 43.2 M events/day
43.2 M x 450 B       = 19.4 GB/day (traffic only)
```

Retention ۹۰ روز: ≈ ۱٫۷۵TB خام؛ با فشرده‌سازی ≈ ۲۲۰GB (نسبت ۸:۱ تقریبی).

### Log Deny ضمنی

``` text
config log setting
    set fwpolicy-implicit-log enable
end
```

بدون آن، ترافیک Denied توسط Implicit Deny Log نمی‌شود و در حادثه کور می‌شوید.

### مثال‌های حل‌شده

#### مثال ساده — انتخاب

Policy اینترنت کاربران: `logtraffic all`؛ Policy مرکز داده‌ی داخلی حجیم Backup: `utm` یا Log اختصاصی با نمونه‌برداری.

#### مثال متوسط — خواندن Log

``` text
date=2026-11-27 time=10:15:01 type="traffic" subtype="forward" srcip=10.10.0.5 dstip=198.51.100.8
dstport=443 policyid=30 action="close" sentbyte=1200 rcvdbyte=9800 duration=35
```

`action=close` یعنی Session تمام شد؛ `deny` یعنی مسدود؛ `timeout` یعنی انقضا. `rcvdbyte=0` یعنی پاسخی نبود.

#### مثال متوسط — حجم

۵۰۰ session/s ⇒ ≈ ۱۹٫۴GB/روز. دیسک محلی ۱۲۰GB فقط ۶ روز. راه: ارسال به مرکز (۲۶-۲)، یا کاهش (Backup بدون Log).

#### مثال سخت — Log همه‌چیز و CPU

`logtraffic all` روی ۱۰۰ Policy پرترافیک + Syslog + FAZ ⇒ CPU log daemon بالا، تأخیر. راه: Log فقط Policyهای مهم، `logtraffic-start disable`، Offload Log به مرکز، `log-invalid-packet disable`.

#### مثال سخت — ممیز و Retention

ممیز Log ۶ ماه پیش می‌خواهد؛ شما ۹۰ روز دارید. Retention باید از الزام قانونی/Dwell Time تعیین شود؛ آرشیو سرد ارزان.

### Lab هدایت‌شده (اجرا نشده)

1. Policy با سطوح مختلف.
2. فیلتر Log و خواندن.
3. محاسبه‌ی حجم.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Log نیست | logtraffic disable | all |
| Deny دیده نمی‌شود | implicit log | enable |
| دیسک پر | حجم | Retention/مرکز |
| CPU بالا | Log زیاد | کاهش |

### نکات امنیتی

Log حاوی IP/User است؛ دسترسی محدود؛ انتقال رمزگذاری‌شده؛ Integrity؛ حذف طبق سیاست.

### جمع‌بندی

انواع Log؛ سطح ثبت و Implicit Deny Log؛ محاسبه‌ی حجم و Retention؛ ذخیره‌ی محلی محدود و ارسال مرکزی.

### تمرین و ارزیابی

**ت1.** (ساده) سه نوع Log در FortiOS؟ *(پاسخ: 27-1-ت1)*

**ت2.** (ساده) تفاوت `logtraffic all` و `utm`؟ *(پاسخ: 27-1-ت2)*

**ت3.** (متوسط) محاسبه کنید: 12M Session، 450 B، 180 روز. *(پاسخ: 27-1-ت3)*

**ت4.** (متوسط) چرا Deny باید Log شود؟ *(پاسخ: 27-1-ت4)*

**ت5.** (سخت) نویز Log مانع کشف نفوذ شد؛ طرح اصلاح. *(پاسخ: 27-1-ت5)*

**ت6.** (سخت، طراحی) استاندارد Logging سازمان را در ۸ بند بنویسید. *(پاسخ: 27-1-ت6)*

**Q1.** Quick quiz (English): Why should the local firewall log not be the only copy of the logs? *(پاسخ: 27-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Forward traffic | Forward traffic log | Log ترافیک عبوری |
| Implicit deny | Implicit deny policy | رد ضمنی |
| Retention | Log retention | مدت نگهداری |

- *Log denied traffic to detect scans.* ← Deny را برای کشف Scan Log کنید.

### کارت Lab

**کارت Lab:** Logging. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/log.md`.

### منابع

- [Sample logs by log type](https://docs.fortinet.com/document/fortigate/7.0.5/administration-guide/986892/sample-logs-by-log-type)
- [Log message fields](https://docs.fortinet.com/document/fortigate/7.0.0/fortios-log-message-reference/357866/log-message-fields)
- NIST SP 800-92

<a id="l-27-2"></a>

## درس 27-2 — مانیتورینگ با SNMP و Zabbix: معیارها، Template، Trigger، Baseline و کاهش Alert نویزی

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۰، ۲۷-۱ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. SNMP (v2c و v3) را روی FortiGate ایمن تنظیم کنید.
2. معیارهای کلیدی (CPU، Memory، Session، Interface، HA، VPN) و OIDها را بشناسید.
3. Zabbix Host/Template/Trigger را بسازید.
4. Baseline و آستانه‌ی معنادار تعیین کنید.
5. Alert نویزی را کاهش دهید (Dependency، Hysteresis، Maintenance).
6. مانیتورینگ را با آزمون Alert تأیید کنید.

### چرا باید یاد بگیریم؟

مانیتورینگ مثل چراغ‌های داشبورد ماشین است: قبل از خراب‌شدن موتور هشدار می‌دهد. ولی چراغی که هر لحظه چشمک بزند، دیگر دیده نمی‌شود (Alert Fatigue). مهندس خوب «چه چیزی، با چه آستانه‌ای، به چه کسی» را بر اساس Baseline تعیین می‌کند، نه عدد دلخواه.

### SNMP ایمن

| نسخه | امنیت |
|---|---|
| v1/v2c | Community متن ساده، ضعیف |
| v3 | احراز (SHA) + رمزگذاری (AES) |

``` text
config system snmp sysinfo
    set status enable
    set description "FGT-A"
    set location "DC1"
end
config system snmp user
    edit "zbx-monitor"
        set security-level auth-priv
        set auth-proto sha
        set auth-pwd <SECRET>
        set priv-proto aes
        set priv-pwd <SECRET>
        set queries enable
        set query-port 161
    next
end
config system interface
    edit "port8"
        set allowaccess ping https ssh snmp
    next
end
```

اصل: SNMP فقط روی Interface مدیریتی و با Local-in Policy/Trusted برای IP سرور Zabbix.

### معیارها و OID (نمونه؛ با MIB بررسی شود)

| معیار | OID (FORTINET-FORTIGATE-MIB) |
|---|---|
| CPU % | `1.3.6.1.4.1.12356.101.4.1.3.0` |
| Memory % | `1.3.6.1.4.1.12356.101.4.1.4.0` |
| Session Count | `1.3.6.1.4.1.12356.101.4.1.8.0` |
| Interface in/out | IF-MIB `ifHCInOctets` (`1.3.6.1.2.1.31.1.1.1.6`) |
| Uptime | `1.3.6.1.2.1.1.3.0` |

(OIDها از MIB رسمی فورتی‌نت؛ Unverified در این Lab.)

آزمون:

``` text
snmpwalk -v3 -l authPriv -u zbx-monitor -a SHA -A <SECRET> -x AES -X <SECRET> 10.50.0.1 1.3.6.1.4.1.12356.101.4.1.3
```

### Zabbix

1. Host: IP مدیریتی، Interface SNMP v3.
2. Template: «Template Net Fortinet FortiGate SNMP» (از Zabbix Templates، نسخه‌ی مناسب).
3. Macro: `{$SNMP_USER}` ... (Secret در Vault Macro).
4. Trigger ها.

### Baseline و آستانه

``` text
Baseline: 14 days, same hour-of-day
CPU normal 20-35%, peak 60%
Warning  > 80% for 10 min
Critical > 90% for 5 min
```

شرط «برای N دقیقه» جلوی Spike کوتاه را می‌گیرد (Hysteresis).

### کاهش نویز

| تکنیک | توضیح |
|---|---|
| Duration | فقط وقتی مدت ادامه یافت |
| Dependency | اگر Interface پایین است، Alert سرویس وابسته ارسال نشود |
| Maintenance | در Window تغییر خاموش |
| Severity | Warning ⇒ ایمیل؛ Critical ⇒ Page |
| Deduplicate | گروه‌بندی Alertها |
| Hysteresis | آستانه‌ی بازیابی کمتر از آستانه‌ی هشدار |

### Triggerهای ضروری

| Trigger | شرط |
|---|---|
| CPU High | >90٪ برای 5 دقیقه |
| Memory High/Conserve | >85٪ |
| Session Count | >80٪ ظرفیت |
| Interface Down | ifOperStatus != up |
| HA Failover | تغییر Primary |
| VPN Tunnel Down | تونل کلیدی Down |
| Log Disk | >85٪ |

### مثال‌های حل‌شده

#### مثال ساده — CPU

Baseline ۲۵٪؛ Trigger ۹۰٪ برای ۵ دقیقه. Spike ۳۰ ثانیه ⇒ Alert نمی‌دهد.

#### مثال متوسط — Session Capacity

ظرفیت ۱ میلیون Session؛ Warning در ۸۰۰ هزار.

``` text
Threshold = capacity x 0.8 = 1,000,000 x 0.8 = 800,000
```

SYN Flood سریع Session را پر می‌کند؛ همراه DoS Policy.

#### مثال متوسط — Dependency

لینک ISP پایین ⇒ ۲۰ Alert از سرویس‌های پشت آن. Dependency: Trigger اصلی «ISP Down»، بقیه سرکوب. نتیجه‌ی یک Alert معنی‌دار.

#### مثال سخت — Alert Fatigue

۲۰۰ Alert در هفته، ۹۵٪ بی‌اهمیت؛ تیم نادیده می‌گیرد؛ یک Alert واقعی گم شد. اصلاح: بازبینی هر Trigger (چه کسی؟ چه اقدامی؟)، حذف بی‌اقدام‌ها، Duration، Severity. KPI: درصد Alertهای عملی.

#### مثال سخت — SNMP v2c لورفته

Community `public` در اینترنت باز بود؛ مهاجم اطلاعات گرفت. راه: v3، Local-in محدود، حذف v2c، تغییر Community. Alert روی SNMP از IP ناشناخته.

### Lab هدایت‌شده (اجرا نشده)

1. SNMPv3 و snmpwalk.
2. Host/Template/Trigger.
3. آزمون Alert و کاهش نویز.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Timeout | allowaccess/Local-in | بررسی |
| Auth خطا | پروتکل/رمز | هماهنگ |
| Alert زیاد | آستانه | Duration |
| داده نیست | OID/Template | بررسی |

### نکات امنیتی

SNMPv3 auth+priv؛ Secret در Vault؛ فقط IP سرور؛ بدون v2c؛ Log دسترسی.

### جمع‌بندی

SNMPv3 ایمن؛ معیارها و OID؛ Zabbix؛ آستانه از Baseline با Duration؛ کاهش نویز (Dependency، Hysteresis، Maintenance).

### تمرین و ارزیابی

**ت1.** (ساده) چرا v3 بهتر از v2c است؟ *(پاسخ: 27-2-ت1)*

**ت2.** (ساده) Hysteresis چیست؟ *(پاسخ: 27-2-ت2)*

**ت3.** (متوسط) CPU>80٪ هر شب Alert می‌دهد؛ چگونه کاهش می‌دهید؟ *(پاسخ: 27-2-ت3)*

**ت4.** (متوسط) Dependency در Zabbix چه می‌کند؟ *(پاسخ: 27-2-ت4)*

**ت5.** (سخت) Alert Storm هنگام قطع ISP؛ طرح. *(پاسخ: 27-2-ت5)*

**ت6.** (سخت، طراحی) ۶ Trigger کلیدی FortiGate با آستانه و دلیل. *(پاسخ: 27-2-ت6)*

**Q1.** Quick quiz (English): What is alert fatigue and how can it be reduced? *(پاسخ: 27-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Baseline | Performance baseline | مرجع عادی |
| Hysteresis | Hysteresis | تأخیر برگشت |
| Actionable rate | Actionable alert rate | نسبت Alertهای نیازمند اقدام |

- *Prefer SNMPv3 and restrict polling sources.* ← SNMPv3 را ترجیح دهید و منابع Poll را محدود کنید.

### کارت Lab

**کارت Lab:** SNMP/Zabbix. **وضعیت:** اجرا نشده (`Unverified` برای v3). **Evidence:** `03-ops/snmp.md`.

### منابع

- Zabbix documentation (SNMP templates)
- Fortinet Docs: SNMP (7.0)
- NIST SP 800-137 (Continuous monitoring)

<a id="l-27-3"></a>

## درس 27-3 — REST API و Automation امن: احراز هویت، Trusted Host، GET/PUT، Idempotency، Rollback و آزمون

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۱، ۲۶-۳، ۲۷-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده». مسیر دقیق Token/Endpoint 7.0.3 `Unverified`.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. REST API فورتی‌نت (CMDB و Monitor) را بشناسید.
2. API User با Profile حداقلی و Trusted Host بسازید.
3. GET/PUT/POST/DELETE را با curl اجرا کنید.
4. Idempotency و Rollback را در Automation رعایت کنید.
5. Secret را ایمن نگه دارید و Log API را بررسی کنید.
6. Automation (Ansible/Python) را امن طراحی کنید.

### چرا باید یاد بگیریم؟

اگر هر تغییر را با کلیک انجام دهید، تکرارپذیر و قابل‌ممیزی نیست و با رشد شبکه فرسوده می‌شوید. API امکان «زیرساخت به‌صورت کد» می‌دهد: تغییر یک بار تعریف، چندبار اجرا. ولی API یک در دیگر به فایروال است؛ Token لورفته یعنی ادمین لورفته. امنیت API به اندازه‌ی خود Automation اهمیت دارد.

### دو شاخه‌ی API

| شاخه | مسیر | کاربرد |
|---|---|---|
| CMDB | `/api/v2/cmdb/...` | پیکربندی (Policy، Address) |
| Monitor | `/api/v2/monitor/...` | وضعیت/Backup/Session |

### ساخت API User

``` text
config system accprofile
    edit "prof_api_ro"
        set secfabgrp read
        set fwgrp read
        set netgrp read
        set sysgrp read
        set loggrp read
    next
end
config system api-user
    edit "api-automation"
        set accprofile "prof_api_ro"
        set vdom "root"
        config trusthost
            edit 1
                set type ipv4-trusthost
                set ipv4-trusthost 10.50.0.30 255.255.255.255
            next
        end
    next
end
execute api-user generate-key api-automation
```

Key فقط یک‌بار نمایش داده می‌شود؛ در Vault. Profile حداقلی (Read-only برای مانیتورینگ؛ Write فقط در Pipeline تأییدشده).

### GET

``` text
curl -sk -H "Authorization: Bearer <API_TOKEN>" \
  "https://10.50.0.1/api/v2/cmdb/firewall/policy?filter=policyid==30"
curl -sk -H "Authorization: Bearer <API_TOKEN>" \
  "https://10.50.0.1/api/v2/monitor/system/status"
```

### PUT / POST / DELETE

``` text
# update (idempotent): set comments on policy 30
curl -sk -X PUT -H "Authorization: Bearer <API_TOKEN>" -H "Content-Type: application/json" \
  -d '{"comments":"owner=NetOps; chg=CHG-701"}' \
  "https://10.50.0.1/api/v2/cmdb/firewall/policy/30"

# create
curl -sk -X POST -H "Authorization: Bearer <API_TOKEN>" -H "Content-Type: application/json" \
  -d '{"name":"HOST-NEW","subnet":"10.20.0.50 255.255.255.255"}' \
  "https://10.50.0.1/api/v2/cmdb/firewall/address"

# delete
curl -sk -X DELETE -H "Authorization: Bearer <API_TOKEN>" \
  "https://10.50.0.1/api/v2/cmdb/firewall/address/HOST-NEW"
```

`-k` فقط در Lab؛ در Production با CA معتبر (`--cacert`).

### Idempotency

عملیاتی که چندبار اجرا شود همان نتیجه را بدهد. PUT معمولاً Idempotent (مقدار نهایی)، POST ایجاد می‌کند و تکرار آن Duplicate/خطا. الگو: «GET ⇒ اگر وجود ندارد POST ⇒ وگرنه PUT».

### Rollback

1. قبل از تغییر: Backup (GET config).
2. اجرای تغییر.
3. Verify (GET + آزمون).
4. در شکست: بازگرداندن (PUT مقدار قبلی/Restore).

``` text
before=$(curl -sk -H "Authorization: Bearer $T" ".../firewall/policy/30")
# change ...
# verify ...
# rollback: curl -X PUT -d "$before_json" ...
```

### مثال‌های حل‌شده

#### مثال ساده — وضعیت

`monitor/system/status` ⇒ نسخه و Hostname. برای Inventory خودکار.

#### مثال متوسط — Comment

PUT روی Policy 30 برای افزودن Owner/Ticket. اجرای دوباره همان نتیجه (Idempotent).

#### مثال متوسط — Trusted Host

Token از IP دیگر: پاسخ 403. ثابت می‌کند Trusted Host کار می‌کند (آزمون منفی).

#### مثال سخت — Token لورفته

Token در Git عمومی افتاد. اقدام: ۱) Revoke (`execute api-user generate-key` جدید یا حذف User) ۲) بررسی Log API (چه دسترسی‌هایی؟) ۳) Scan مخزن (gitleaks) و pre-commit hook ۴) RCA. پیشگیری: Vault، Profile Read-only، Trusted Host.

#### مثال سخت — Automation بی‌کنترل

Pipeline با Write Profile Policy را تغییر داد و اشتباه Deny All شد. اصلاح: Dry-run/Preview، Approval، Canary (یک دستگاه)، Rollback خودکار با Verify، Rate-limit.

### Lab هدایت‌شده (اجرا نشده)

1. API User و Trusted Host.
2. GET/PUT و Verify.
3. آزمون منفی Token.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| 401 | Token | بررسی |
| 403 | Trusted/Profile | بررسی |
| 424/خطا | وابستگی Object | ترتیب |
| تغییر دوباره | Idempotency | GET قبل |

### نکات امنیتی

Token در Vault؛ Profile حداقلی؛ Trusted Host؛ HTTPS با CA معتبر؛ Log و Alert روی API؛ چرخش Token.

### جمع‌بندی

CMDB/Monitor؛ API User حداقلی و Trusted Host؛ GET/PUT/POST/DELETE؛ Idempotency و Rollback؛ مدیریت Secret.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Trusthost برای API؟ *(پاسخ: 27-3-ت1)*

**ت2.** (ساده) Idempotent یعنی چه؟ *(پاسخ: 27-3-ت2)*

**ت3.** (متوسط) 401 با Token درست؛ علل؟ *(پاسخ: 27-3-ت3)*

**ت4.** (متوسط) Dry-run چه فایده‌ای دارد؟ *(پاسخ: 27-3-ت4)*

**ت5.** (سخت) Script ۵۰ Object تکراری ساخت؛ تحلیل و اصلاح. *(پاسخ: 27-3-ت5)*

**ت6.** (سخت، طراحی) طرح امن Automation برای مانیتورینگ و تغییر Policy. *(پاسخ: 27-3-ت6)*

**Q1.** Quick quiz (English): Why should automation scripts support a dry-run mode? *(پاسخ: 27-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| API | Application Programming Interface | رابط برنامه‌نویسی |
| Idempotent | Idempotent operation | عملیات تکرارپذیر بدون اثر اضافه |
| Canary | Canary deployment | اعمال آزمایشی روی بخش کوچک |

- *Never store API tokens in a repository.* ← هرگز توکن API را در مخزن ذخیره نکنید.

### کارت Lab

**کارت Lab:** API. **وضعیت:** اجرا نشده/Unverified. **Evidence:** `03-ops/api.md`.

### منابع

- Fortinet Docs: REST API / API user (7.0)
- OWASP API Security Top 10

<a id="l-27-4"></a>

## درس 27-4 — Hardening مدیریتی عملی و Backup/Restore: اجرای چک‌لیست، آزمون منفی و اثبات بازیابی

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۷، ۱۲-۸، ۲۶-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ Log/Syslog از مستند 7.0؛ SNMPv3 و REST API روی 7.0.3 `Unverified`؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. چک‌لیست Hardening مدیریتی را اجرا کنید و دلیل هر مورد را بگویید.
2. آزمون منفی (از IP غیرمجاز، با پروتکل غیرفعال) برای اثبات Hardening بزنید.
3. Backup/Restore را طوری انجام دهید که «بازیابی‌شدنی بودن» ثابت شود.
4. Timeoutها، Lockout، Banner و Password Policy را تنظیم کنید.
5. NTP/Syslog/SNMP را امن و هماهنگ کنید.
6. گزارش Hardening بنویسید.

### چرا باید یاد بگیریم؟

فایروال با پیش‌فرض‌های راحت ایمن نیست. Hardening یعنی بستن همه‌ی درهایی که لازم نیست. ولی کار نیمه‌تمام دو خطر دارد: ادعای «سخت‌سازی شد» بدون آزمون، و قفل شدن خودتان از دستگاه (Lockout). این درس هم اجرا و هم اثبات را (با آزمون منفی) و هم برنامه‌ی بازگشت را آموزش می‌دهد.

### چک‌لیست

| حوزه | اقدام | دلیل |
|---|---|---|
| Admin | حساب شخصی، تغییر نام `admin`، MFA، حذف حساب مشترک | Accountability |
| دسترسی | `allowaccess` حداقل، `trusthost`، Local-in Policy | کاهش سطح حمله |
| پروتکل | غیرفعال Telnet/HTTP؛ HTTPS/SSH قوی | رمزنگاری |
| پورت | تغییر پورت پیش‌فرض (اختیاری) + محدودیت Source | کاهش اسکن |
| Timeout | `admintimeout` کوتاه | نشست رها شده |
| Lockout | `admin-lockout-threshold/duration` | Brute-force |
| Password | حداقل طول، پیچیدگی، انقضا | رمز ضعیف |
| Banner | هشدار حقوقی | حقوقی |
| زمان | NTP امن | Log و گواهی |
| سرویس‌ها | غیرفعال بی‌استفاده‌ها | سطح حمله |
| Log | ارسال مرکزی | شواهد |
| Backup | رمزگذاری، خودکار | بازیابی |

### پیکربندی نمونه

``` text
config system global
    set admintimeout 10
    set admin-lockout-threshold 3
    set admin-lockout-duration 600
    set admin-https-ssl-versions tlsv1-2 tlsv1-3
    set admin-ssh-v1 disable
    set strong-crypto enable
    set pre-login-banner enable
    set post-login-banner enable
end
config system password-policy
    set status enable
    set min-lower-case-letter 1
    set min-upper-case-letter 1
    set min-number 1
    set min-non-alphanumeric 1
    set minimum-length 14
    set expire-status enable
    set expire-day 90
end
config system interface
    edit "port1"
        unset allowaccess
        set allowaccess ping
    next
    edit "port8"
        set allowaccess https ssh
    next
end
config system admin
    edit "net-bob"
        set trusthost1 10.50.0.0 255.255.255.0
    next
end
config system ntp
    set type custom
    set ntpsync enable
    config ntpserver
        edit 1
            set server "10.50.0.10"
        next
    end
end
```

(نام و مقدار گزینه‌ها با مستند 7.0 بررسی شود؛ Unverified.)

### Local-in Policy

``` text
config firewall local-in-policy
    edit 1
        set intf "port1"
        set srcaddr "all"
        set dstaddr "all"
        set service "ALL"
        set schedule "always"
        set action deny
    next
end
```

مدیریت از اینترنت ممنوع؛ اجازه فقط از Mgmt (Local-in Allow برای MGMT قبل از Deny).

### آزمون منفی

| آزمون | انتظار |
|---|---|
| `ssh` به Interface WAN | Timeout/Refused |
| HTTP به مدیریت | Redirect/Refused |
| Login از IP غیر Trusted | رد |
| سه رمز غلط | Lockout |
| TLS 1.0 | رد (`openssl s_client -tls1`) |

``` text
nmap -p 22,80,443,23 <WAN-IP>
openssl s_client -connect 10.50.0.1:443 -tls1
```

### Backup/Restore قابل‌اثبات

1. Backup رمزگذاری‌شده (Password):

``` text
execute backup config tftp fgt-a.conf <server> <backup-password>
```

2. بررسی Hash فایل و ثبت.
3. Restore روی دستگاه Lab هم‌نسخه.
4. آزمون: Route، Policy، VPN، HA، Log.
5. ثبت زمان Restore (RTO واقعی).

### مثال‌های حل‌شده

#### مثال ساده — Lockout

سه رمز غلط ⇒ ۱۰ دقیقه قفل. آزمون ✓. هشدار: Break-glass قبل از اعمال تنظیم Lockout.

#### مثال متوسط — اسکن WAN

`nmap` از اینترنت فقط ICMP/VPN پورت‌ها را نشان می‌دهد؛ 22/443 مدیریت بسته. گزارش Evidence.

#### مثال متوسط — Restore واقعی

Restore روی Lab ۱۲ دقیقه؛ ۲ مورد (گواهی/Secret) دستی. نتیجه: RTO بازیابی ≈ ۱۵ دقیقه؛ Runbook به‌روز.

#### مثال سخت — Lockout خودمان

`trusthost` اشتباه؛ همه‌ی Adminها قفل. راه: Console، `config system admin edit ... unset trusthost1`؛ درس: Change با Console آماده و آزمون با یک حساب قبل از اعمال برای همه.

#### مثال سخت — Restore Secret

Backup بدون رمز، Secret (PSK) ENC به کلید دستگاه وابسته است؛ Restore روی دستگاه دیگر PSK شکسته. راه: Backup رمزگذاری‌شده با `backup-password` (که Secretها را منتقل‌پذیر می‌کند) و ثبت PSK در Vault.

### Lab هدایت‌شده (اجرا نشده)

1. اجرای چک‌لیست.
2. آزمون‌های منفی.
3. Backup/Restore و زمان.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| قفل شدید | trusthost | Console |
| اسکن پورت باز | allowaccess | حذف |
| Restore شکست | نسخه/Secret | هم‌نسخه |
| TLS قدیمی | ssl-versions | تنظیم |

### نکات امنیتی

MFA؛ Break-glass؛ Backup رمزگذاری‌شده؛ تغییرات با Ticket؛ Evidence بعد از هر آزمون.

### جمع‌بندی

Hardening با چک‌لیست و آزمون منفی؛ Lockout/Trusthost/TLS؛ Backup رمزگذاری‌شده و Restore آزمون‌شده؛ Break-glass و Console برای جلوگیری از قفل.

### تمرین و ارزیابی

**ت1.** (ساده) آزمون منفی چیست؟ *(پاسخ: 27-4-ت1)*

**ت2.** (ساده) چرا `admintimeout`؟ *(پاسخ: 27-4-ت2)*

**ت3.** (متوسط) پس از Restore VPN کار نمی‌کند؛ چرا؟ *(پاسخ: 27-4-ت3)*

**ت4.** (متوسط) چگونه RTO را اندازه می‌گیرید؟ *(پاسخ: 27-4-ت4)*

**ت5.** (سخت) ۱۰ کنترل Hardening با آزمون منفی بنویسید. *(پاسخ: 27-4-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی کاهش RTO از ۴۵ به ۳۰ دقیقه. *(پاسخ: 27-4-ت6)*

**Q1.** Quick quiz (English): Why must every hardening control be accompanied by a negative test? *(پاسخ: 27-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RTO | Recovery Time Objective | زمان هدف بازیابی |
| Negative test | Negative test | آزمون ممنوعیت |

- *Prove each control with a negative test.* ← هر کنترل را با آزمون منفی ثابت کنید.

### کارت Lab

**کارت Lab:** Hardening. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/hardening.md`.

### منابع

- CIS FortiGate Benchmark
- NIST SP 800-53
- Fortinet: Hardening your FortiOS

<a id="l-27-5"></a>

## درس 27-5 — Gate G10: آزمون عملی Logging، Monitoring، Hardening و Backup — کلید پاسخ کامل و Rubric

**فصل 27 · بازنویسی عمیق · پیش‌نیاز: ۲۷-۱ تا ۲۷-۴ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Logging، Monitoring، Hardening و Backup را در یک سناریوی Gate پیاده و اثبات کنید.
2. سه عیب تزریق‌شده را با Evidence رفع کنید.
3. آزمون‌های منفی و Evidence Index بسازید.
4. گزارش و Rubric تحویل دهید.
5. RTO واقعی Restore را اندازه بگیرید.
6. صداقت (اجرا نشده/Unverified) را رعایت کنید.

### چرا باید یاد بگیریم؟

Gate G10 اثبات می‌کند «عملیات امن» دارید نه فقط «تنظیمات». عملیات امن یعنی: Log می‌رسد، Alert به‌موقع می‌آید، دسترسی بسته است، و Backup واقعاً بازیابی می‌شود. هرکدام را باید با شاهد نشان دهید.

### صورت مسئله

FortiGate شعبه (`FGT-A`، Mgmt: `port8` 10.50.0.1). نیازمندی‌ها:

1. Log Traffic/Event به rsyslog (TCP/TLS) برسد.
2. Zabbix با SNMPv3 CPU/Memory/Session/Interface را بگیرد؛ Alert CPU>90٪ برای ۵ دقیقه.
3. Hardening: مدیریت فقط از Mgmt، MFA، Lockout، TLS≥1.2.
4. Backup خودکار رمزگذاری‌شده و Restore آزمون‌شده (RTO ≤ ۲۰ دقیقه).

عیب‌های تزریق‌شده:

1. `allowaccess https ssh` روی `port1` (WAN) فعال.
2. `fwpolicy-implicit-log` غیرفعال؛ Deny دیده نمی‌شود.
3. Backup بدون رمز و SNMP v2c با Community `public`.

### کلید پاسخ

**عیب ۱ (مدیریت روی WAN):**

1. Evidence: `nmap -p 22,443 <WAN-IP>` ⇒ open.
2. رفع: `set allowaccess ping` روی port1؛ Local-in Deny.
3. تأیید: nmap ⇒ filtered/closed.

**عیب ۲ (Implicit Log):**

1. Evidence: آزمون Deny بدون Log.
2. رفع: `set fwpolicy-implicit-log enable`.
3. تأیید: Log `policyid=0 action=deny`.

**عیب ۳ (Backup/SNMP):**

1. Evidence: فایل Backup متن ساده؛ `snmpwalk -v2c -c public` موفق.
2. رفع: Backup با `backup-password`؛ حذف v2c؛ SNMPv3 auth-priv؛ Local-in برای 161 فقط Zabbix.
3. تأیید: `snmpwalk -v2c` Timeout؛ v3 موفق.

### آزمون Restore

1. Backup رمزگذاری‌شده + Hash.
2. Restore روی Lab هم‌نسخه.
3. زمان‌سنجی:

``` text
RTO measured = t(device serving traffic) - t(restore start)
Example: 14 min  (target <= 20 min)
```

4. Verify: Route، Policy، VPN، Log، SNMP.

### Evidence Index

| مورد | فایل | دستور |
|---|---|---|
| WAN scan before/after | ev1_nmap.txt | nmap |
| Deny log | ev2_deny.txt | execute log display |
| SNMPv3 | ev3_snmp.txt | snmpwalk |
| Restore | ev4_restore.txt | زمان‌ها |
| Backup hash | ev5_hash.txt | sha256sum |

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| Logging مرکزی | 15 |
| Monitoring/Alert | 15 |
| Hardening با آزمون منفی | 25 |
| Backup/Restore و RTO | 20 |
| رفع سه عیب | 15 |
| Evidence/صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Trigger

CPU 95٪ برای ۶ دقیقه ⇒ Alert؛ Spike ۳۰ ثانیه ⇒ ندارد. Evidence: Zabbix event.

#### مثال متوسط — RCA

``` text
Impact  : management plane reachable from internet 3 weeks (exposure, no breach found)
Cause   : allowaccess https/ssh on WAN since commissioning
Fix     : allowaccess ping only + local-in deny; MFA enforced
Prevent : post-commissioning hardening checklist + external scan monthly
```

#### مثال متوسط — اندازه‌گیری RTO

۱۴ دقیقه (۸ Restore + ۶ تأیید دستی گواهی/VPN). ثبت و هدف ≤ ۲۰ دقیقه برآورده.

#### مثال سخت — ترتیب رفع

۱) مدیریت روی WAN (فوری امنیتی) ۲) SNMP v2c ۳) Backup رمز ۴) Implicit Log. اولویت بر اساس ریسک نه ترتیب لیست.

#### مثال سخت — صداقت

Lab اجرا نشده؛ زمان RTO و خروجی nmap نمونه‌ی آموزشی؛ گزارش «Unverified».

### Lab هدایت‌شده (اجرا نشده)

1. سه عیب را رفع کنید.
2. Restore و RTO.
3. گزارش و Evidence Index.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| مدیریت باز در WAN | allowaccess | حذف |
| Deny بدون Log | implicit | enable |
| SNMP v2c | ضعیف | v3 |
| Backup متن ساده | بدون رمز | backup-password |

### جمع‌بندی

G10: Log مرکزی، Monitoring با Alert معنادار، Hardening با آزمون منفی، Backup/Restore با RTO، سه عیب، Evidence و صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) چرا SNMPv3؟ *(پاسخ: 27-5-ت1)*

**ت2.** (ساده) چرا Hash Backup؟ *(پاسخ: 27-5-ت2)*

**ت3.** (متوسط) Log نمی‌رسد؛ مراحل. *(پاسخ: 27-5-ت3)*

**ت4.** (متوسط) allowaccess snmp؟ *(پاسخ: 27-5-ت4)*

**ت5.** (سخت) Restore آزمایشی. *(پاسخ: 27-5-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست G10. *(پاسخ: 27-5-ت6)*

**Q1.** Quick quiz (English): Why should backups be encrypted? *(پاسخ: 27-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NMS | Network Management System | سامانه‌ی مدیریت |

- *Test the restore, not only the backup.* ← Restore را هم آزمون کنید نه فقط Backup.

### کارت Lab

**کارت Lab:** G10 (اجرا نشده). **Evidence:** `03-ops/g10.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Logging; SNMP; Backup

## درس 27-7 — Hardening، Backup/Restore و API: امن‌سازی مدیریتی و بازیابی قابل‌اثبات

**فصل ۲۷ · درس افزوده (پس از ۲۷-۵) · پیش‌نیاز: ۱۲-۸، ۲۶-۰، ۲۷-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** اصول از دانش عملیاتی و Local-in (۱۲-۸)؛ دستورهای `Unverified`؛ **REST API و SNMPv3 در این دور با مستند رسمی تأیید نشد** (به مرجع 7.0 مراجعه شود). Lab «اجرا نشده».

### ۱) هدف آموزشی

1. چک‌لیست Hardening مدیریتی (Admin، Access، سرویس‌ها، زمان‌بندی) را اجرا و دلیل هر مورد را بگوید.
2. **Backup/Restore** را طوری انجام دهد که «بازیابی‌شدنی بودن» اثبات شود.
3. **API/Automation** را با Least Privilege و Trusted Host محدود و ایمن به‌کار بگیرد.
4. تغییرات مدیریتی را Audit و Rollback کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا ممیزی ادمین؟** مهاجمی که ادمین شود همه‌چیز دارد. فهرست ادمین‌ها را مرتب با فهرست مجاز مقایسه کنید و Log ورود را هشدار بدهید.

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

``` text
show system admin
```

#### مثال متوسط — Local-in

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

#### مثال سخت — ادمین ناشناس

ورود «backup2» ساعت 03:10 از IP خارجی: غیرفعال‌سازی، تغییر رمز همه، diff Config با Backup، بررسی Persistence (SSH Key/Script)، PIR.

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
