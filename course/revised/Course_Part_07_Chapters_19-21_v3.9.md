# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۷ از ۱۱ — فصل‌های ۱۹ تا ۲۱

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۷ از ۱۱ |
| فصل‌های این فایل | ۱۹ ، ۲۰ ، ۲۱ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۱۹–۲۱ تولید شد؛ Hub-and-Spoke، Remote Access، Dual-ISP/SD-WAN.** Labها «اجرا نشده»؛ SSL VPN فقط ایزوله به‌دلیل CVE؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 16.

| Lab | وضعیت |
|---|---|
| 19-1 | اجرا نشده (فقط طراحی) |
| 19-2 | اجرا نشده (فقط طراحی) |
| 19-3 | اجرا نشده (فقط طراحی) |
| 19-4 | اجرا نشده (فقط طراحی) |
| 19-5 | اجرا نشده (فقط طراحی) |
| 19-6 | اجرا نشده (فقط طراحی) |
| 20-1 | اجرا نشده (فقط طراحی) |
| 20-2 | اجرا نشده (فقط طراحی) |
| 20-3 | اجرا نشده (فقط طراحی) |
| 20-4 | اجرا نشده (فقط طراحی) |
| 20-5 | اجرا نشده (فقط طراحی) |
| 21-1 | اجرا نشده (فقط طراحی) |
| 21-2 | اجرا نشده (فقط طراحی) |
| 21-3 | اجرا نشده (فقط طراحی) |
| 21-4 | اجرا نشده (فقط طراحی) |
| 21-5 | اجرا نشده (فقط طراحی) |

---

<a id="ch19"></a>

> **نسخه‌ی اصلاح‌شده (v3.9):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۲۰-۷، ۲۱-۷ (دسته C). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

# فصل 19 — Hub-and-Spoke، OSPF/BGP روی FortiGate و Local Breakout

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۹، ۱۸.
**اهداف:** توپولوژی Hub-and-Spoke با چند Tunnel؛ Routing پویا (OSPF/BGP) روی Tunnel؛ Local Breakout؛ معماری ۴ (چندشعبه). Gate: چهار شعبه از مسیر Hub ارتباط دارند و قطع یک Tunnel بقیه را نمی‌شکند.
**نسخه:** FortiOS 7.0.3 اسمی؛ دستورها آزمایش‌نشده؛ ADVPN در `Unverified`.
**اشتباهات رایج:** Route Overlap؛ فراموشی `net-device`/IP Tunnel؛ Policy بین Spokeها؛ Loop مسیر.

**درس‌های فصل:**
- [درس 19-1 — طراحی Hub-and-Spoke و IP Plan](#l-19-1)
- [درس 19-2 — ساخت Tunnelهای Spoke و OSPF روی Tunnel](#l-19-2)
- [درس 19-3 — BGP روی FortiGate و Failover مسیر](#l-19-3)
- [درس 19-4 — Local Breakout و Policy اینترنت شعبه](#l-19-4)
- [درس 19-5 — ADVPN (مفهومی) و مقیاس‌پذیری](#l-19-5)
- [درس 19-6 — معماری ۴: چندشعبه و آزمون فصل](#l-19-6)

---

<a id="l-19-1"></a>

## درس 19-0 — طراحی Overlay چندشعبه: Hub-and-Spoke، Routing پویا روی Tunnel و ADVPN

**فصل ۱۹ · درس افزوده (پیش‌درس ۱۹-۱) · پیش‌نیاز: ۱۸-۰، ۹-۰، ۹-۷، ۵-۷ · ≈ ۸ ساعت**

> **وضعیت (FortiOS 7.0):** نکات ADVPN/BGP از مستند رسمی ([ADVPN and shortcut paths 7.0.9](https://docs.fortinet.com/document/fortigate/7.0.9/administration-guide/985659/advpn-and-shortcut-paths)، [ADVPN with BGP](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/820072/advpn-with-bgp-as-the-routing-protocol)) بررسی شد. سینتکس روی 7.0.3 `Unverified`؛ برخی گزینه‌ها (مثل Shortcut Override) از 7.0.4 آمده‌اند. Lab «اجرا نشده».

### ۱) هدف آموزشی

1. Overlay و Underlay را تفکیک و **توپولوژی‌های Full-mesh، Hub-and-Spoke و ADVPN** را مقایسه کند.
2. **Routing پویا** (BGP/OSPF) روی Tunnel طراحی کند و تفاوت **iBGP/eBGP** و نقش **Route Reflector** را بگوید.
3. IP Plan بدون Overlap، **Tunnel Interface IP** و **net-device** را درست تنظیم کند.
4. ADVPN را (در صورت پشتیبانی نسخه) با Sender/Receiver و Shortcut بفهمد.
5. رفتار شبکه را هنگام خرابی Tunnel/Hub تحلیل (Convergence) و Failover را طراحی کند.
6. **Local Breakout** را در برابر مسیر مرکزی (Backhaul) با معیار امنیت/Performance انتخاب کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Overlay چندشعبه را «طراحی» کنیم؟** اتصال دو شعبه با یک Tunnel ساده است. اتصال ۳۰ شعبه به‌صورت دستی یعنی ده‌ها Tunnel، ده‌ها Route و کابوس نگهداری. طراحی Overlay یعنی قبل از ساخت درباره‌ی «شکل» (Hub-and-Spoke یا Mesh)، «مسیریابی» (Static یا پویا) و «مقیاس» تصمیم بگیرید. مثل طراحی شبکه‌ی جاده‌ای بین شهرها: اگر هر شهر مستقیم به همه‌ی شهرها جاده بکشد، هزینه‌ی نگهداری انفجاری می‌شود؛ اگر همه از یک مرکز بگذرند، مرکز پرترافیک می‌شود.

**Overlay و Underlay:** Underlay همان اینترنت/ISP است؛ Overlay شبکه‌ی خصوصی مجازی روی آن (Tunnelها). شعبه‌ها فکر می‌کنند در یک شبکه‌ی خصوصی هستند.

**سه الگو**

1. **Full-mesh:** هر دو سایت مستقیم. تعداد Tunnel = N(N−1)/2.
2. **Hub-and-Spoke:** همه به Hub. تعداد Tunnel = N. ترافیک Spoke↔Spoke از Hub می‌گذرد.
3. **ADVPN:** پایه Hub-and-Spoke؛ هنگام نیاز بین دو Spoke Tunnel مستقیم (Shortcut) ساخته می‌شود؛ ارزان‌تر از Mesh و سریع‌تر از Hub-Spoke.

**چرا Routing پویا؟** با Static Route برای هر شعبه‌ی جدید باید همه‌ی دستگاه‌ها ویرایش شوند و Failover خودکار ندارید. OSPF/BGP روی Tunnel مسیرها را خودکار می‌یابد و با قطع Hub به Hub دوم می‌رود.

**جمع‌بندی اصلی درس:**

IPsec (۱۸-۰)، BGP (۹-۰، ۹-۷)، Convergence (۵-۷)، Packet Flow (۱۲-۰)، SD-WAN (۲۱-۷ برای ترکیب).

### ۳) مفهوم پایه

شرکتی با ۲۰ شعبه: Full-mesh یعنی ۱۹۰ Tunnel (n(n−1)/2) که مقیاس‌پذیر نیست. **Hub-and-Spoke:** هر شعبه (Spoke) فقط به مرکز (Hub) Tunnel دارد؛ ترافیک شعبه‌به‌شعبه از Hub می‌گذرد (ساده، مرکزی برای Policy/Inspection، ولی تأخیر و بار روی Hub). **ADVPN:** در Hub-and-Spoke، Spokeها در صورت نیاز **Tunnel مستقیم (Shortcut)** بین هم می‌سازند.

### ۴) توضیح عمیق فنی

#### ۴-۱) مقایسه

| الگو | تعداد Tunnel (n شعبه) | مزیت | عیب |
|---|---|---|---|
| Full-mesh | n(n−1)/2 | کمترین تأخیر | پیچیده/غیرمقیاس‌پذیر |
| Hub-and-Spoke | n (به Hub) | ساده، کنترل مرکزی | Hub گلوگاه/SPOF؛ تأخیر Spoke-to-Spoke |
| ADVPN | n + Shortcutهای پویا | ترکیب مزایا | وابسته به نسخه، پیچیده‌تر |

``` text
Full-mesh tunnels = n(n-1)/2     example: n=20 -> 190
```

#### ۴-۲) Routing روی Tunnel

- **Static** برای شعب کم؛ **OSPF** (point-to-point) یا **BGP** برای مقیاس و Failover.
- **BGP** معمولاً توصیه می‌شود: مقیاس‌پذیر، کنترل Policy. طبق مستند ADVPN: بین Hub و Spokeها **iBGP** استفاده می‌شود؛ Hub می‌تواند **Route Reflector** باشد و Neighbor-group/neighbor-range روی Subnet تونل تعریف کند تا Spokeهای جدید بدون تغییر Hub اضافه شوند.
- IP روی Tunnel: برای Peering BGP (/32 روی Tunnel یا Loopback). Loopback Peering نیاز به Route Static/IKE-installed برای رسیدن به Loopback دارد.
- **Selector** Phase 2: 0.0.0.0/0 تا Routing تصمیم بگیرد (۱۸-۰).

#### ۴-۳) نکات اجرایی

- `net-device`: طبق مستند ADVPN با BGP، روی Hub باید `set net-device disable` (Phase 1) باشد تا یک Interface برای همه‌ی Spokeها و Peering درست کار کند.
- **Route Overlap:** Subnet هر شعبه یکتا (IP Plan فصل ۲).
- **Policy:** Tunnel↔LAN دوطرفه؛ برای Spoke-to-Spoke از Hub: Policy Tunnel→Tunnel روی Hub.
- **Anti-loop:** BGP AS_PATH/Route Reflector؛ OSPF Area.

#### ۴-۴) ADVPN (7.0)

طبق مستند: Hub Phase 1: `set auto-discovery-sender enable`؛ Spoke: `set auto-discovery-receiver enable`. Spoke A→Spoke B: ترافیک اول از Hub؛ Hub به A و B اطلاع می‌دهد (Shortcut)؛ A و B Tunnel مستقیم می‌سازند و Routeها/Next-hop به‌روز می‌شوند. مستند می‌گوید **GUI برخی گزینه‌های ADVPN را ندارد** و فقط CLI. در 7.0.4 «shortcut override» و «tag-match» برای کنترل بهتر نیز آمده است.

#### ۴-۵) Local Breakout در برابر Backhaul

| | Backhaul (همه به Hub) | Local Breakout |
|---|---|---|
| امنیت | Inspection یکپارچه | هر شعبه باید UTM داشته باشد |
| Performance | تأخیر/بار Hub | سریع |
| هزینه | پهنای Hub زیاد | ISP محلی |
| سیاست | یکسان | ممکن است ناهمگون |

معمول: سازمانی ← Tunnel؛ SaaS/اینترنت ← Local Breakout با UTM و SD-WAN (۲۱-۷).

#### ۴-۶) خرابی و Convergence

- قطع Tunnel Spoke–Hub: Hub مسیر را پس از Detect (DPD/BGP Hold/BFD) حذف می‌کند.
- Spoke با دو Hub: Failover بین Hubها (Local-pref/MED).
- Hub fail: Hub دوم + HA؛ زمان Convergence ≈ Detect + BGP.

### ۵) مثال حل‌شده

#### مثال ساده — شمارش Tunnel

``` text
Full mesh = N x (N - 1) / 2
Hub&Spoke = N
N = 10 -> 45 vs 10 ;  N = 50 -> 1225 vs 50
```

#### مثال متوسط — طراحی دو Hub

۱۰ شعبه با دو Hub (Primary/Secondary):

``` text
Tunnels = spokes x hubs = 10 x 2 = 20
```

هر Spoke به هر دو Hub Tunnel دارد؛ Routing پویا Hub اصلی را با Metric بهتر ترجیح می‌دهد.

#### مثال متوسط — زمان Failover

``` text
Failover = detection + convergence
OSPF dead 40 s (default) -> with BFD ~ 1 s
```

برای هدف «کمتر از ۱۰ ثانیه» BFD یا Timerهای کوتاه (با آزمون) لازم است.

#### مثال سخت — Hub گلوگاه

ترافیک Spoke↔Spoke زیاد است و Hub اشباع می‌شود. شاهد: CPU/Throughput Hub و تأخیر. راه: ADVPN یا Tunnel مستقیم Partial بین جفت‌های پرترافیک. اثبات: ping/iperf بین دو Spoke قبل و بعد؛ مسیر traceroute از Hub به مستقیم تغییر می‌کند.

#### مثال‌های اصلی درس (مرور)

**نیاز:** 1 Hub (AS 65000) + Spoke1/Spoke2؛ BGP iBGP. Hub: `set auto-discovery-sender enable`، `set net-device disable`؛ Spokeها: `set auto-discovery-receiver enable`.

``` text
# HUB (sketch)
config vpn ipsec phase1-interface
    edit "HUB-TUN"
        set type dynamic
        set auto-discovery-sender enable
        set net-device disable
        set add-route disable
    next
end
config router bgp
    set as 65000
    config neighbor-group
        edit "SPOKES"
            set remote-as 65000
            set route-reflector-client enable
        next
    end
    config neighbor-range
        edit 1
            set prefix 10.255.0.0 255.255.255.0
            set neighbor-group "SPOKES"
        next
    end
end
```

(سینتکس برگرفته از ساختار مستند 7.0.9؛ جزئیات `Unverified` روی 7.0.3.)

**مثال متوسط:** قطع Tunnel Spoke1: `get router info bgp summary` همسایه Idle؛ Route شعبه از جدول حذف؛ شعب دیگر دیگر ترافیک را به Spoke1 نمی‌فرستند.

**مثال سخت:** ترافیک Spoke1→Spoke2 از Hub می‌گذرد و کند است. با ADVPN Shortcut ساخته می‌شود؛ ولی Shortcut ساخته نشد: بررسی: Sender/Receiver، Policy Spoke→Spoke، Route Next-hop. شاهد: `diagnose vpn tunnel list`.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| تعداد شعب | ≤ ۵: Static/OSPF؛ بیشتر: BGP |
| Hub تکی/دوتایی | دوتایی برای SLA بالا |
| ADVPN | وقتی ترافیک Spoke-to-Spoke زیاد و نسخه پشتیبانی کند |
| Breakout | محلی با UTM برای SaaS |
| Subnet | Summarize و یکتا |

### ۷) GUI و CLI (Verification)

**GUI:** VPN → IPsec Tunnels؛ Network → BGP/OSPF؛ Monitor → IPsec Monitor؛ Routing Monitor. **CLI:**

``` text
get router info bgp summary
get router info routing-table all
diagnose vpn tunnel list
diagnose vpn ike gateway list
```

### ۸) Troubleshooting

| علامت | علت |
|---|---|
| BGP Active | Policy/Route Peer، AS، `net-device` |
| Route نمی‌آید | Filter/RR/Next-hop |
| Spoke-to-Spoke کند | ADVPN فعال نشده/Policy |
| شعبه‌ی جدید وصل نمی‌شود | neighbor-range/Phase 1 dynamic |

### ۹) نکات امنیتی

- Hub هدف حمله است؛ Patch و محدودیت Source.
- Policy Spoke-to-Spoke را حداقلی بنویسید.
- Local Breakout بدون UTM = حفره.

### ۱۰) جمع‌بندی مفهومی

- Full-mesh n(n−1)/2؛ Hub-and-Spoke n؛ ADVPN ترکیب.
- BGP iBGP با RR برای مقیاس.
- IP Plan یکتا؛ Selector باز؛ Policy دوطرفه.
- ADVPN وابسته به نسخه؛ GUI محدود.
- Backhaul در برابر Breakout: امنیت در برابر Performance.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) تعداد Tunnel Full-mesh برای ۲۰ شعبه؟ *(پاسخ: 19-0-ت1)*

**ت2.** (ساده) Overlay و Underlay چیست؟ *(پاسخ: 19-0-ت2)*

**ت3.** (متوسط) چرا BGP برای شعب زیاد بهتر از Static؟ *(پاسخ: 19-0-ت3)*

**ت4.** (متوسط) نقش Route Reflector در Hub چیست؟ *(پاسخ: 19-0-ت4)*

**ت5.** (سخت) ADVPN چگونه Spoke-to-Spoke را بهینه می‌کند و چه پیش‌نیازهایی دارد؟ *(پاسخ: 19-0-ت5)*

**ت6.** (سخت، طراحی) برای ۱۰ شعبه با دو Hub، Failover و Breakout را طراحی کنید. *(پاسخ: 19-0-ت6)*

**Q1.** Quick quiz (English): What is the main drawback of pure hub-and-spoke for spoke-to-spoke traffic? *(پاسخ: 19-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ADVPN | Auto-Discovery VPN | Tunnel پویای Spoke-to-Spoke |
| RR | Route Reflector | بازتاب‌دهنده‌ی مسیر |
| Overlay | Overlay network | شبکه‌ی روی ISP |
| Breakout | Local internet breakout | خروج محلی |

- *Use dynamic routing over tunnels for scalability.* ← برای مقیاس‌پذیری از Routing پویا روی Tunnel استفاده کنید.
- *ADVPN builds on-demand shortcuts between spokes.* ← ADVPN بین Spokeها Shortcut سفارشی می‌سازد.

### ۱۳) منابع

- Fortinet Docs: [ADVPN and shortcut paths](https://docs.fortinet.com/document/fortigate/7.0.9/administration-guide/985659/advpn-and-shortcut-paths)، [ADVPN with BGP](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/820072/advpn-with-bgp-as-the-routing-protocol)، [Enhanced BGP next hop updates and ADVPN shortcut override 7.0.4](https://docs.fortinet.com/document/fortigate/7.0.0/new-features/245878/enhanced-bgp-next-hop-updates-and-advpn-shortcut-override-7-0-4).

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: انتخاب Topology با عدد

**۱۰ شعبه:** Full-mesh = N(N-1)/2 = 45 Tunnel؛ Hub-and-Spoke = 10 Tunnel.

``` text
Full mesh tunnels = N*(N-1)/2 = 10*9/2 = 45
Hub&Spoke tunnels = N = 10
```

ADVPN: Spoke به Spoke فقط در صورت نیاز Shortcut می‌سازد؛ ترکیب ارزان Hub-Spoke و کارایی Mesh.

**پرسش‌های مصاحبه**
1. *Hub نقطه‌ی شکست؟* دو Hub.
2. *Routing پویا چرا؟* Failover و مقیاس.
3. *ADVPN نیازها؟* IKEv2، Routing، تنظیم Hub.

### تکمیل عمیق: طراحی Overlay چندشعبه — از ۳ شعبه تا ۳۰۰ شعبه

#### چرا باید یاد بگیریم؟

اتصال دو شعبه با یک Tunnel ساده است. اتصال ۳۰ شعبه به‌صورت دستی یعنی صدها Tunnel، صدها Route و کابوس نگهداری. طراحی Overlay یعنی تصمیم‌گیری درباره‌ی «ساختار» (Hub-and-Spoke یا Mesh)، «مسیریابی» (Static یا پویا) و «مقیاس» پیش از ساخت.

#### توضیح ساده

Overlay شبکه‌ای مجازی است که روی اینترنت (Underlay) ساخته می‌شود؛ شعبه‌ها با Tunnel به هم وصل‌اند و فکر می‌کنند در یک شبکه‌ی خصوصی هستند.

#### مثال ساده — شمارش Tunnel

``` text
Full mesh tunnels  = N x (N - 1) / 2
Hub-and-Spoke      = N (one per spoke, to hub)
N = 10 -> mesh = 45 ; hub-spoke = 10
N = 50 -> mesh = 1225 ; hub-spoke = 50
```

نتیجه: Mesh با رشد N منفجر می‌شود.

#### مثال متوسط — ADVPN

ADVPN = Auto-Discovery VPN. ساختار پایه Hub-and-Spoke است؛ وقتی Spoke A با Spoke B زیاد ارتباط دارد، Hub به آنها «Shortcut» پیشنهاد می‌کند و Tunnel مستقیم ساخته می‌شود. مزیت: هزینه‌ی Hub-Spoke + کارایی Mesh.

#### مثال سخت — Hub Failure

Hub تنها نقطه‌ی شکست است. طراحی: دو Hub (Primary/Secondary) با Routing پویا؛ Spoke به هر دو Tunnel دارد؛ ترجیح با Metric.

``` text
Failover time ~ detect (BFD/Dead timer) + route convergence
OSPF dead 40 s (default broadcast) ; with BFD ~ <1 s
```

مقادیر پیش‌فرض را از مستند نسخه بخوانید.

#### Lab

نمودار سه‌لایه برای ۱۰ شعبه بکشید و تعداد Tunnel را محاسبه کنید.

#### عیب‌یابی طراحی

| علامت | علت | رفع |
|---|---|---|
| پیچیدگی انفجاری | Mesh کامل | Hub-Spoke/ADVPN |
| Hub bottleneck | ترافیک Spoke-Spoke | ADVPN |
| Failover کند | Timer | BFD |

#### پرسش‌ها با پاسخ

**۱. چند Tunnel برای ۲۰ شعبه Mesh؟** ۱۹۰.
**۲. ADVPN چه مشکلی را حل می‌کند؟** ترافیک Spoke-Spoke.
**۳. چرا دو Hub؟** SPOF.

#### English Corner

- *A full mesh grows quadratically; hub-and-spoke grows linearly.*
- Q: How does ADVPN combine the benefits of both designs?

## درس 19-1 — طراحی آدرس‌دهی چندشعبه: IP Plan، Summarization با محاسبه‌ی باینری، Tunnel IP و ظرفیت Hub

**فصل 19 · بازنویسی عمیق · پیش‌نیاز: ۱۹-۰، ۲-۲ (VLSM)، ۹-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک مرجع؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. IP Plan سلسله‌مراتبی برای ده‌ها شعبه طراحی کنید (HQ، Region، Branch، Tunnel، Loopback).
2. Summary Route (Route Aggregation) را محاسبه و ایمن اعلام کنید.
3. Null Route (blackhole) برای جلوگیری از Loop را بنویسید.
4. Overlap بین شعبه‌ها را تشخیص و رفع کنید.
5. ظرفیت و رشد آینده را در طراحی لحاظ کنید.
6. طراحی را با ابزار (ipaddress در Python) راستی‌آزمایی کنید.

### چرا باید یاد بگیریم؟

شهری را تصور کنید که خیابان‌هایش بدون الگو شماره‌گذاری شده: برای تحویل بسته، هر تپه و کوچه باید جداگانه در نقشه ثبت شود. شهر منظم اما «منطقه ۱، محله ۵، پلاک ۱۲» دارد؛ مأمور فقط منطقه را می‌شناسد و بقیه محلی حل می‌شود. IP Plan سلسله‌مراتبی همین است: Hub فقط یک Route برای هر منطقه نگه می‌دارد، نه ۵۰ Route. جدول مسیر کوچک‌تر یعنی همگرایی سریع‌تر و عیب‌یابی ساده‌تر. اشتباه در این مرحله بعدها تقریباً بدون Renumbering جبران‌پذیر نیست.

### اصول طراحی

1. **بلوک پیوسته و هم‌تراز** برای هر منطقه (Summary ممکن).
2. **جدا کردن نقش‌ها:** LAN شعبه، Tunnel، Loopback، Management.
3. **رشد:** هر منطقه ظرفیت دو برابر اولیه.
4. **یکتایی سراسری:** بدون Overlap حتی بین شرکت‌های ادغام‌شده.
5. **مستندسازی:** جدول واحد (IPAM) نه Excel پراکنده.

### نمونه‌ی IP Plan

``` text
10.0.0.0/8            company
  10.0.0.0/16         HQ (DC, users, mgmt)
  10.1.0.0/16         Region A (branches 10.1.X.0/24)
  10.2.0.0/16         Region B
  10.3.0.0/16         Region C
  10.250.0.0/16       Tunnel interconnect (p2p /30)
  10.254.0.0/24       Loopbacks (/32 each)
  10.255.0.0/16       Reserved
```

برای هر Tunnel یک `/30` از 10.250.0.0/16: ۴۰ شعبه × ۴ آدرس = ۱۶۰ آدرس، بسیار کمتر از ظرفیت ۶۵۵۳۶.

### محاسبه‌ی Summary

قاعده: بلوک مجموعه‌ای از شبکه‌ها باید با مرز توان ۲ هم‌تراز باشد.

``` text
Branches: 10.1.4.0/24, 10.1.5.0/24, 10.1.6.0/24, 10.1.7.0/24
3rd octet: 4,5,6,7  -> binary 000001xx
Common prefix of 3rd octet = 6 bits  -> /16 + 6 = /22
Summary = 10.1.4.0/22   (10.1.4.0 - 10.1.7.255)
```

بررسی هم‌ترازی: عدد 4 باید مضرب 4 باشد (بلوک چهارتایی). اگر شعبه‌ها از 10.1.5.0 شروع شوند، /22 هم‌تراز نیست.

### Null Route برای Summary

``` text
config router static
    edit 100
        set dst 10.1.0.0 255.255.0.0
        set blackhole enable
        set distance 254
    next
end
```

چرا؟ اگر Summary /16 اعلام شده ولی فقط 10.1.4.0/24 موجود است و بسته‌ای به 10.1.9.5 برسد، بدون Null Route ممکن است با Default برگردد و Loop بسازد. Null Route آن را Drop می‌کند.

### Overlap

``` text
python3 -c "import ipaddress as i; print(i.ip_network('10.16.0.0/20').overlaps(i.ip_network('10.16.8.0/24')))"
```

خروجی `True` یعنی هم‌پوشانی. ابزار IPAM و اسکریپت بررسی قبل از اضافه‌کردن شعبه.

### مثال‌های حل‌شده

#### مثال ساده — Summary

چهار شعبه 10.1.4–7.0/24؛ Summary 10.1.4.0/22 + Null Route. Hub یک Route منطقه را به Spoke/Region Router می‌دهد؛ جدول به‌جای ۴ ورودی ۱ ورودی.

#### مثال متوسط — شعبه‌ی پنجم

شعبه‌ی 10.1.8.0/24 اضافه می‌شود؛ /22 آن را پوشش نمی‌دهد. گزینه‌ها: ۱) Summary /21 (10.1.0.0/21) با ظرفیت 8 شعبه ۲) Region /16 کلی. تصمیم: در طراحی اولیه /21 یا /20 رزرو کنید.

``` text
/21 -> 8 x /24 (10.1.0.0 - 10.1.7.255)
/20 -> 16 x /24 (10.1.0.0 - 10.1.15.255)
```

#### مثال متوسط — Tunnel /30

Hub–Spoke1: 10.250.1.0/30 ⇒ Hub .1، Spoke .2. Loopback Hub 10.254.0.1/32. Peering BGP با Loopback (پایدارتر از IP Tunnel).

#### مثال سخت — ادغام شرکت‌ها

دو شرکت هر دو 10.1.0.0/24 دارند. راه‌ها: ۱) NAT 1:1 موقت روی Tunnel و Renumber تدریجی ۲) برای شعبه‌ی جدید آدرس جدید. NAT هزینه‌ی عیب‌یابی دارد (DNS و برنامه‌های Embedded IP). برنامه‌ی Renumber با Change Window و آزمون.

#### مثال سخت — Summary ناقص

Region A /16 ولی شعبه‌ای در منطقه‌ی دیگر 10.1.200.0/24 گرفته؛ Hub ترافیک آن را به Region A می‌فرستد ⇒ قطع. درس: سیاست تخصیص: فقط IPAM تخصیص دهد.

### Lab هدایت‌شده (اجرا نشده)

1. IP Plan برای ۱۶ شعبه بنویسید.
2. Summary را محاسبه و Null Route بنویسید.
3. Overlap را با Python بررسی کنید.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Loop | Summary بدون Null | blackhole |
| قطع منطقه‌ای | تخصیص خارج بلوک | IPAM |
| Overlap | ادغام | NAT/Renumber |
| جدول بزرگ | بدون Summary | طراحی |

### نکات امنیتی

Null Route برای Summary؛ Prefix-list ورودی/خروجی؛ جلوگیری از Leak Summary به اینترنت.

### جمع‌بندی

سلسله‌مراتب (HQ/Region/Branch/Tunnel/Loopback)؛ Summary هم‌تراز و Null Route؛ بررسی Overlap؛ ظرفیت رشد؛ IPAM.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Summary باید «هم‌تراز» باشد؟ *(پاسخ: 19-1-ت1)*

**ت2.** (ساده) Tunnel IP با /30 چند آدرس مصرف می‌کند و چرا؟ *(پاسخ: 19-1-ت2)*

**ت3.** (متوسط) Summary 10.1.0.0/16 اعلام شده ولی فقط 10.1.4.0/24 موجود است. ترافیک 10.1.9.5 چه می‌شود و چرا Null route مهم است؟ *(پاسخ: 19-1-ت3)*

**ت4.** (متوسط) برای ۴۰ شعبه با ۲ Tunnel هر کدام، تعداد SA و Tunnel Hub را حساب کنید. *(پاسخ: 19-1-ت4)*

**ت5.** (سخت) شرکت ادغام‌شده Overlap دارد. طرح گذار سه‌مرحله‌ای بنویسید. *(پاسخ: 19-1-ت5)*

**ت6.** (سخت، طراحی) IP Plan منطقه‌ای را برای ۳ منطقه × ۲۵۰ شعبه بنویسید و خلاصه‌ها را نشان دهید. *(پاسخ: 19-1-ت6)*

**Q1.** Quick quiz (English): Why must a summary prefix be aligned to its block boundary? *(پاسخ: 19-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Summarization | Route summarization | خلاصه‌سازی مسیر |
| Null route | Blackhole route | مسیر دور‌ریز |
| LPM | Longest Prefix Match | بلندترین Prefix مطابق |
| Aligned | Block alignment | هم‌ترازی بلوک |

- *Summarize routes at regional boundaries.* ← مسیرها را در مرز منطقه‌ها خلاصه کنید.
- *Add a null route for every summary.* ← برای هر Summary یک Null route اضافه کنید.

### کارت Lab

**کارت Lab:** IP Plan چندشعبه. **هدف:** طرح ۴۰ شعبه + Summary + Null route. **وضعیت:** اجرا نشده. **مراحل:** (۱) جدول IP Plan؛ (۲) اسکریپت Overlap؛ (۳) تنظیم blackhole Route؛ (۴) آزمون traceroute. **Verification:** مطابق بخش ۸. **Rollback:** حذف Routeها. **Evidence:** `02-design/hub-spoke-plan.md`.

### منابع

- RFC 4632 — CIDR
- RFC 1918
- Fortinet Docs: Static routes (blackhole)؛ FortiOS 7.0 Administration Guide

<a id="l-19-2"></a>

## درس 19-2 — Tunnelهای Hub–Spoke و OSPF روی Tunnel: طراحی، Network Type، Cost، Convergence و عیب‌یابی

**فصل 19 · بازنویسی عمیق · پیش‌نیاز: ۱۹-۰، ۱۹-۱، ۱۸-۲، ۶-۱ (OSPF) · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک مرجع؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Hub-and-Spoke را با IPsec Route-based بسازید.
2. IP Tunnel، Phase1/Phase2 و Static Route اولیه را بنویسید.
3. OSPF را روی Tunnel (point-to-multipoint/point-to-point) تنظیم کنید.
4. Neighbor، LSDB و Route را تأیید کنید.
5. Failover دو Hub را درک کنید.
6. خطاهای رایج (MTU OSPF، Network Type، Passive) را رفع کنید.

### چرا باید یاد بگیریم؟

Static Route برای دو شعبه کافی است؛ برای ۲۰ شعبه، هر تغییر یعنی ۲۰ ویرایش دستی و احتمال اشتباه. OSPF (Open Shortest Path First) مثل سیستم GPS است که خودش تغییر مسیرها را پخش می‌کند: شعبه‌ی جدید اضافه شود یا تونلی قطع شود، جدول به‌روز می‌شود. برای overlay چندشعبه، Routing پویا استاندارد است.

### توپولوژی

``` text
            [HUB 198.51.100.10]
             /        \
   10.250.1.0/30   10.250.2.0/30
           /            \
   [SPOKE1]            [SPOKE2]
   10.1.1.0/24         10.1.2.0/24
```

### تونل (Hub)

``` text
config vpn ipsec phase1-interface
    edit "SPK1"
        set interface "port1"
        set ike-version 2
        set peertype any
        set net-device enable
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 203.0.113.21
        set psksecret <SECRET>
        set dpd on-idle
    next
end
config vpn ipsec phase2-interface
    edit "SPK1-P2"
        set phase1name "SPK1"
        set proposal aes256-sha256
        set pfs enable
        set dhgrp 14
        set src-subnet 0.0.0.0 0.0.0.0
        set dst-subnet 0.0.0.0 0.0.0.0
    next
end
config system interface
    edit "SPK1"
        set ip 10.250.1.1 255.255.255.255
        set remote-ip 10.250.1.2 255.255.255.255
    next
end
```

برای Hub با Spokeهای زیاد از `dialup` (Peer Type با Dynamic) و `net-device enable` استفاده می‌شود تا ایفیس تونل به ازای هر Spoke خودکار ساخته شود.

### OSPF روی Tunnel

``` text
config router ospf
    set router-id 10.254.0.1
    config area
        edit 0.0.0.0
        next
    end
    config network
        edit 1
            set prefix 10.250.0.0 255.255.0.0
            set area 0.0.0.0
        next
    end
    config interface
        edit "SPK1"
            set network-type point-to-point
            set cost 10
            set hello-interval 10
            set dead-interval 40
        next
    end
    config redistribute "connected"
        set status enable
    end
end
```

نکته‌ها:

1. `network-type point-to-point` برای تونل ۱:۱ (بدون DR/BDR).
2. `point-to-multipoint` برای Hub با چند Spoke روی یک Interface.
3. MTU تونل با MTU OSPF هماهنگ؛ عدم تطابق ⇒ Stuck in ExStart.
4. Spoke: LAN با `passive-interface` (فقط Prefix اعلام شود).

### تأیید

``` text
get router info ospf neighbor
get router info ospf database
get router info routing-table ospf
get router info ospf interface SPK1
```

وضعیت مطلوب: Neighbor در `Full`.

### مثال‌های حل‌شده

#### مثال ساده — Neighbor

`get router info ospf neighbor` ⇒ `10.254.1.1 Full/ - ... SPK1`. Route به 10.1.1.0/24 با `O`.

#### مثال متوسط — Network Type

دو سمت یکی broadcast و دیگری point-to-point؛ Neighbor بالا می‌آید ولی Route‌ها ناقص یا Hello Mismatch. رفع: هر دو point-to-point.

#### مثال متوسط — ExStart

Neighbor در ExStart/Exchange گیر کرده. علت: MTU تونل متفاوت. رفع: `set mtu-ignore enable` (موقت/با آگاهی) یا هماهنگ‌کردن MTU.

#### مثال سخت — دو Hub

Spoke به Hub1 و Hub2 تونل دارد؛ OSPF cost: Hub1=10، Hub2=100 ⇒ Primary/Backup. قطع Hub1 ⇒ OSPF طی Dead-interval (۴۰ ثانیه) یا سریع‌تر با BFD (`set bfd enable`) به Hub2 می‌رود. آزمون: قطع Hub1، `get router info routing-table ospf`.

#### مثال سخت — Redistribute خطرناک

Hub `redistribute static` همه‌ی Staticها را اعلام می‌کند، شامل Default به ISP ⇒ Spokeها به اینترنت از Hub می‌روند ناخواسته. راه: Route-map/Prefix-list برای redistribute و Default فقط عمدی.

### Lab هدایت‌شده (اجرا نشده)

1. دو Spoke و Hub؛ OSPF.
2. Failover با دو Hub.
3. MTU Mismatch و رفع.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Neighbor نیست | Tunnel/Network | بررسی |
| ExStart | MTU | هماهنگ |
| Route نیست | network statement | prefix |
| Loop | redistribute | filter |

### نکات امنیتی

احراز OSPF (MD5/SHA) روی Interface؛ Passive در LAN؛ فیلتر Prefix؛ جلوگیری از تزریق Route.

### جمع‌بندی

Hub-and-Spoke با IPsec Route-based؛ OSPF با Network Type مناسب؛ MTU هماهنگ؛ Passive LAN؛ دو Hub با Cost و BFD؛ redistribute با فیلتر.

### تمرین و ارزیابی

**ت1.** (ساده) Hello/Dead پیش‌فرض OSPF روی Tunnel p2p چند ثانیه است و Dead چه رابطه‌ای با Hello دارد؟ *(پاسخ: 19-2-ت1)*

**ت2.** (ساده) چرا Selector 0.0.0.0/0 برای OSPF لازم است؟ *(پاسخ: 19-2-ت2)*

**ت3.** (متوسط) محاسبه کنید: Dead 40 s، BFD 300 ms×3، SPF delay 200 ms. زمان قطع در هر دو حالت؟ *(پاسخ: 19-2-ت3)*

**ت4.** (متوسط) Neighbor در Init مانده؛ سه فرضیه به ترتیب بنویسید. *(پاسخ: 19-2-ت4)*

**ت5.** (سخت) دو Tunnel با Cost 10 و 100. لینک ISP1 ناپایدار است (۳۰ ثانیه Up/۳۰ ثانیه Down). مشکل را شرح دهید و راه‌حل بدهید. *(پاسخ: 19-2-ت5)*

**ت6.** (سخت، طراحی) برای ۴۰ شعبه OSPF یا BGP؟ با ۴ معیار توجیه کنید. *(پاسخ: 19-2-ت6)*

**Q1.** Quick quiz (English): Why do tunnels often need BFD or very short dead timers for fast failover? *(پاسخ: 19-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| p2p | Point-to-point network type | نوع شبکه‌ی نقطه‌به‌نقطه |
| p2mp | Point-to-multipoint | نقطه‌به‌چندنقطه |
| SPF | Shortest Path First | الگوریتم مسیر کوتاه |
| ABR | Area Border Router | روتر مرز Area |
| BFD | Bidirectional Forwarding Detection | تشخیص دوطرفه‌ی خرابی |

- *Set explicit OSPF costs to define primary and backup tunnels.* ← برای تعیین Tunnel اصلی و پشتیبان Cost را صریح تنظیم کنید.
- *Convergence time is dominated by failure detection.* ← زمان Convergence عمدتاً به کشف خرابی بستگی دارد.

### کارت Lab

**کارت Lab:** OSPF روی Tunnel. **هدف:** Neighbor Full + Failover زیر ۲ ثانیه با BFD. **وضعیت:** اجرا نشده. **مراحل:** Tunnel، OSPF، Cost، BFD، قطع لینک. **Verification:** مطابق بخش ۸. **Rollback:** حذف OSPF Interface. **Evidence:** `03-ops/ospf-tunnel.md`.

### منابع

- RFC 2328 — OSPFv2
- RFC 5880 — BFD
- Fortinet Docs: OSPF؛ IPsec VPN with dynamic routing (7.0)

<a id="l-19-3"></a>

## درس 19-3 — BGP روی FortiGate برای Overlay: iBGP، Route Reflector، Next-hop، Local-pref، Failover و Filtering

**فصل 19 · بازنویسی عمیق · پیش‌نیاز: ۱۹-۰، ۹-۰، ۹-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک مرجع؛ Lab «اجرا نشده». از مستند: ADVPN با BGP → iBGP بین Hub و Spoke، `net-device disable` روی Hub.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. چرا و کی BGP را برای Overlay انتخاب کنیم (در برابر OSPF) بگویید.
2. iBGP و eBGP را روی Tunnel تنظیم کنید.
3. Route Reflector را برای Hub به‌کار ببرید.
4. Prefix-list، Route-map و Local-Preference را برای کنترل مسیر بنویسید.
5. Neighbor و جدول BGP را تأیید کنید.
6. عیب‌یابی (Idle/Active، Next-hop، Loop) را انجام دهید.

### چرا باید یاد بگیریم؟

OSPF برای یک «شهر» کوچک عالی است؛ ولی برای ده‌ها شعبه با سیاست‌های مختلف (کدام Prefix از کدام مسیر برود، کدام Hub اول) به ابزار «سیاست‌محور» نیاز دارید. BGP (Border Gateway Protocol) مثل سرویس پستی بین‌شهری است که نه تنها مسیر را پخش می‌کند، بلکه به شما اجازه می‌دهد قوانین بگذارید: «بسته‌ی شعبه‌ی A از Hub1 برود و فقط اگر آن قطع شد Hub2». مقیاس‌پذیری و کنترل، دلیل غالب انتخاب BGP در SD-WAN و ADVPN است.

### iBGP در برابر eBGP

| ویژگی | iBGP | eBGP |
|---|---|---|
| AS | یکسان | متفاوت |
| AD | 200 | 20 |
| Next-hop | تغییر نمی‌کند (`next-hop-self`) | تغییر می‌کند |
| Loop prevention | Split-horizon (Route Reflector لازم) | AS-path |

در Overlay معمولاً iBGP با یک AS (مثلاً 65000) و Hub به‌عنوان Route Reflector.

### پیکربندی Hub (Route Reflector)

``` text
config router bgp
    set as 65000
    set router-id 10.254.0.1
    config neighbor-group
        edit "SPOKES"
            set remote-as 65000
            set route-reflector-client enable
            set next-hop-self enable
            set update-source "Lo0"
        next
    end
    config neighbor-range
        edit 1
            set prefix 10.254.1.0 255.255.255.0
            set neighbor-group "SPOKES"
        next
    end
    config network
        edit 1
            set prefix 10.0.0.0 255.255.0.0
        next
    end
end
```

`neighbor-range` پذیرش خودکار Spokeها از بازه‌ی Loopback (بدون ثبت جدا برای هر کدام).

### پیکربندی Spoke

``` text
config router bgp
    set as 65000
    set router-id 10.254.1.1
    config neighbor
        edit "10.254.0.1"
            set remote-as 65000
            set update-source "Lo0"
        next
    end
    config network
        edit 1
            set prefix 10.1.1.0 255.255.255.0
        next
    end
end
```

Peering با Loopback به‌جای IP Tunnel: پایدارتر (اگر تونل جابه‌جا شود Session نمی‌ماند). Reachability Loopback از طریق Static/OSPF روی Tunnel.

### کنترل مسیر

``` text
config router prefix-list
    edit "PL-BRANCH"
        config rule
            edit 1
                set prefix 10.1.0.0 255.255.0.0
                set ge 24
                set le 24
            next
        end
    next
end
config router route-map
    edit "RM-PREFER-HUB1"
        config rule
            edit 1
                set match-ip-address "PL-BRANCH"
                set set-local-preference 200
            next
        end
    next
end
```

Local-Preference بالاتر = ترجیح بیشتر (فقط داخل AS). Prefix-list ورودی از پذیرش Prefix اشتباه (Leak/Hijack) جلوگیری می‌کند.

### تأیید

``` text
get router info bgp summary
get router info bgp neighbors 10.254.1.1
get router info bgp network
get router info routing-table bgp
```

### مثال‌های حل‌شده

#### مثال ساده — Established

`get router info bgp summary` ⇒ `10.254.1.1 ... Up/Down 00:05:12  State/PfxRcd 1`. یعنی Established و یک Prefix.

#### مثال متوسط — Idle/Active

State=Active: Spoke به Hub وصل نمی‌شود. علت‌ها: Reachability Loopback نیست، `update-source` اشتباه، TCP 179 بسته. آزمون: `execute ping-options source 10.254.1.1; execute ping 10.254.0.1`.

#### مثال متوسط — Next-hop

iBGP Prefix را از Hub به Spoke2 می‌رساند ولی Next-hop آدرس Spoke1 (غیرقابل‌دسترس). رفع: `next-hop-self` روی RR یا Reachability به Next-hop.

#### مثال سخت — دو Hub با Local-Pref

Hub1 با LP=200، Hub2 با LP=100 برای 10.0.0.0/16 (HQ). Spoke Hub1 را ترجیح می‌دهد. قطع Hub1 ⇒ BGP Hold-timer (پیش‌فرض ۱۸۰ ثانیه) یا BFD سریع‌تر. اصلاح: `set bfd enable`، `keepalive 5 holdtime 15`. آزمون Failover.

#### مثال سخت — Leak

Spoke به‌اشتباه Prefix مشتری را اعلام می‌کند و Hub به همه‌ی Spokeها RR می‌کند. راه: Prefix-list ورودی روی Hub (فقط Prefixهای مجاز هر Spoke) و `maximum-prefix`.

### Lab هدایت‌شده (اجرا نشده)

1. iBGP Hub/Spoke با Loopback.
2. Local-Pref و Failover.
3. Prefix-list و آزمون Leak.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Idle/Active | Reachability/179 | Loopback |
| Prefix نمی‌آید | network/RR | بررسی |
| Next-hop نامعتبر | next-hop-self | فعال |
| Failover کند | Timer | BFD |

### نکات امنیتی

Password MD5/TCP-AO؛ Prefix-list ورودی؛ `maximum-prefix`؛ Peer فقط از Loopback مجاز؛ GTSM.

### جمع‌بندی

BGP برای سیاست و مقیاس؛ iBGP با RR روی Hub؛ Peering با Loopback؛ Local-Pref و Prefix-list؛ BFD و Timer برای Failover.

### تمرین و ارزیابی

**ت1.** (ساده) iBGP Split-horizon چیست؟ *(پاسخ: 19-3-ت1)*

**ت2.** (ساده) چرا RR تعداد Session را کم می‌کند؟ *(پاسخ: 19-3-ت2)*

**ت3.** (متوسط) برای Primary Hub Local-pref چه می‌دهید و چرا؟ *(پاسخ: 19-3-ت3)*

**ت4.** (متوسط) Established ولی PfxRcd=0. فرضیه‌ها را بنویسید. *(پاسخ: 19-3-ت4)*

**ت5.** (سخت) Hub1 قطع می‌شود؛ Hold 180 و BFD 300×3 وجود دارد. زمان قطع تقریبی؟ *(پاسخ: 19-3-ت5)*

**ت6.** (سخت، طراحی) Policy BGP را برای جلوگیری از Leak بین شعب بنویسید. *(پاسخ: 19-3-ت6)*

**Q1.** Quick quiz (English): How does a route reflector reduce the number of iBGP sessions? *(پاسخ: 19-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RR | Route Reflector | بازتاب‌دهنده‌ی مسیر |
| Cluster-ID | Route reflector cluster ID | شناسه‌ی خوشه RR |
| MRAI | Minimum Route Advertisement Interval | حداقل فاصله‌ی اعلام |
| Max-prefix | Maximum prefix limit | سقف Prefix |

- *Use route reflectors instead of a full iBGP mesh.* ← به‌جای Full-mesh iBGP از RR استفاده کنید.
- *Filter prefixes on both inbound and outbound.* ← Prefix را هم ورودی و هم خروجی فیلتر کنید.

### کارت Lab

**کارت Lab:** BGP Overlay. **هدف:** iBGP+RR، Failover Hub. **وضعیت:** اجرا نشده/Unverified. **Verification:** مطابق بخش ۸. **Rollback:** حذف BGP. **Evidence:** `03-ops/bgp-tunnel.md`.

### منابع

- [ADVPN with BGP](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/820072/advpn-with-bgp-as-the-routing-protocol)
- [ADVPN and shortcut paths](https://docs.fortinet.com/document/fortigate/7.0.9/administration-guide/985659/advpn-and-shortcut-paths)
- RFC 4271، RFC 4456 (Route Reflection)، RFC 7454

<a id="l-19-4"></a>

## درس 19-4 — Local Breakout و Policy اینترنت شعبه: Backhaul در برابر Breakout، Split مسیر، SaaS، UTM و Failover

**فصل 19 · بازنویسی عمیق · پیش‌نیاز: ۱۹-۰، ۱۲-۰، ۱۶-۰، ۲۱-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک مرجع؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Backhaul (همه‌ی ترافیک به HQ) را با Local Breakout (خروج محلی اینترنت) مقایسه کنید.
2. معیارهای تصمیم (تأخیر، پهنای باند، امنیت، هزینه) را وزن‌دهی کنید.
3. Policy اینترنت شعبه را با UTM حداقلی و SaaS محلی بنویسید.
4. ترافیک داخلی (ERP) را از Tunnel و SaaS را از ISP محلی هدایت کنید.
5. NAT و DNS در Breakout را درست تنظیم کنید.
6. Failover Breakout به Backhaul را طراحی کنید.

### چرا باید یاد بگیریم؟

شعبه‌ی تبریز می‌خواهد Microsoft 365 را باز کند. اگر Backhaul باشد: بسته از تبریز با تونل به تهران می‌رود، از فایروال مرکزی بیرون می‌آید، به ابر می‌رسد و برمی‌گردد؛ تأخیر چند برابر و لینک HQ تحت فشار. Local Breakout یعنی تبریز مستقیم از ISP محلی بیرون برود. ولی هر شعبه‌ی «بیرون‌رو» یک لبه‌ی اینترنتی جدید است که باید امن شود. تصمیم برپایه‌ی ترازوی هزینه–ریسک–کارایی است.

### مقایسه

| معیار | Backhaul | Local Breakout |
|---|---|---|
| تأخیر SaaS | بالا | پایین |
| امنیت | متمرکز (یک نقطه) | توزیع‌شده (هر شعبه) |
| پهنای HQ | فشار زیاد | آزاد |
| پیچیدگی | کم | بیشتر |
| دید/Log | یکجا | باید جمع شود |
| هزینه | لینک HQ بزرگ | UTM در شعبه |

الگوی رایج: **ترکیبی** — ترافیک داخلی از Tunnel؛ SaaS شناخته‌شده Local Breakout؛ بقیه‌ی اینترنت یا Breakout با UTM یا Backhaul بسته به سیاست.

### معماری Policy

``` text
Branch LAN -> ERP (10.0.0.0/16)    -> via IPsec tunnel (Route)
Branch LAN -> M365/Zoom/Teams      -> local ISP (Internet Service DB/SD-WAN rule)
Branch LAN -> other internet       -> local ISP + UTM (or backhaul)
Guest      -> local ISP only (no tunnel, isolated)
```

### پیکربندی

Route:

``` text
config router static
    edit 1
        set gateway 203.0.113.1
        set device "port1"
    next
end
```

Policy اینترنت با NAT و UTM:

``` text
config firewall policy
    edit 90
        set name "LAN-to-INTERNET"
        set srcintf "ZN-LAN"
        set dstintf "port1"
        set srcaddr "NET-BRANCH"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "HTTP" "HTTPS" "DNS"
        set utm-status enable
        set ssl-ssh-profile "certificate-inspection"
        set webfilter-profile "WF-STD"
        set dnsfilter-profile "DNS-STD"
        set nat enable
        set logtraffic all
    next
end
```

Policy تونل (داخلی): بدون NAT.

برای SaaS: در FortiOS 7.0 از Internet Service Database (ISDB) در Policy/SD-WAN Rule استفاده می‌شود (Needs-License برای به‌روزرسانی DB).

### DNS

شعبه باید DNS درست داشته باشد: نام‌های داخلی (corp.example) از DNS مرکزی (از طریق Tunnel)، سایر نام‌ها از DNS محلی/عمومی. `config system dns-database/forwarder` یا Conditional Forwarding روی DNS Server داخلی.

### Failover

اگر ISP محلی قطع شد: ترافیک اینترنت به Backhaul (Default از Tunnel با Distance بالا). 

``` text
config router static
    edit 2
        set dst 0.0.0.0 0.0.0.0
        set device "TO-HUB1"
        set distance 50
        set priority 10
    next
end
```

Route محلی Distance 10 (اولویت)، Route Backhaul Distance 50 (پشتیبان).

### مثال‌های حل‌شده

#### مثال ساده — تصمیم

Teams از تهران با Backhaul 80ms و از تبریز Breakout 15ms. تصمیم: Breakout برای Teams.

#### مثال متوسط — Split

ERP 10.0.0.0/16 ⇒ Tunnel (Route خاص). Default ⇒ ISP محلی. `get router info routing-table details 10.0.5.10` ⇒ TO-HUB1؛ `... 52.96.0.1` ⇒ port1.

#### مثال متوسط — NAT

ترافیک Tunnel: `nat disable`؛ اینترنت: `nat enable`. اگر اشتباه شود ERP مبدأ NAT شده می‌بیند و ACL آن شکست می‌خورد.

#### مثال سخت — امنیت شعبه

بدون UTM در Breakout، یک لپ‌تاپ آلوده مستقیم به اینترنت می‌رود. UTM حداقلی: DNS Filter + Web Filter (Category) + IPS برای سرویس‌های ورودی (اگر VIP). Needs-License. جایگزین: Backhaul برای دسته‌های پرخطر (SD-WAN Rule بر پایه‌ی Application/Category).

#### مثال سخت — Failover و Session

ISP محلی قطع شد؛ Sessionهای اینترنت قطع می‌شوند (NAT منبع عوض شد). توضیح به کاربر: یک بار اتصال دوباره؛ Session Pickup فقط در HA. اندازه‌گیری: Failover زیر ۱۰ ثانیه با Link Monitor.

### Lab هدایت‌شده (اجرا نشده)

1. Split: ERP تونل، اینترنت محلی.
2. NAT صحیح در هر Policy.
3. Failover به Backhaul.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| ERP خراب | NAT روی تونل | nat disable |
| SaaS کند | Backhaul | Breakout |
| اینترنت قطع بعد از قطع ISP | بدون Backup | Route پشتیبان |
| DNS داخلی نه | Forwarder | شرطی |

### نکات امنیتی

Breakout بدون UTM ممنوع؛ Guest ایزوله؛ Log مرکزی؛ بازبینی دسته‌های Breakout.

### جمع‌بندی

Backhaul در برابر Breakout با معیار؛ الگوی ترکیبی؛ NAT صحیح؛ DNS شرطی؛ Failover با Distance/Link Monitor؛ UTM در شعبه.

### تمرین و ارزیابی

**ت1.** (ساده) مزیت اصلی Breakout چیست؟ *(پاسخ: 19-4-ت1)*

**ت2.** (ساده) چرا ERP از Tunnel می‌رود نه Default؟ *(پاسخ: 19-4-ت2)*

**ت3.** (متوسط) Latency را برای Backhaul با 40 ms و 15 ms و Breakout 22 ms مقایسه کنید. *(پاسخ: 19-4-ت3)*

**ت4.** (متوسط) Default Route BGP از Hub و Default محلی هر دو هستند؛ کدام برنده است و چگونه کنترل می‌کنید؟ *(پاسخ: 19-4-ت4)*

**ت5.** (سخت) Breakout بدون UTM باعث آلودگی شد. طرح اصلاح با ۴ لایه بنویسید. *(پاسخ: 19-4-ت5)*

**ت6.** (سخت، طراحی) Failover وقتی هر دو ISP شعبه قطع‌اند چیست؟ *(پاسخ: 19-4-ت6)*

**Q1.** Quick quiz (English): Why does a more specific route to the headquarters win over a local default route? *(پاسخ: 19-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Backhaul | Traffic backhaul | بازگرداندن ترافیک به مرکز |
| ISDB | Internet Service Database | پایگاه سرویس‌های اینترنتی |
| SaaS | Software as a Service | نرم‌افزار به‌عنوان سرویس |
| FQDN | Fully Qualified Domain Name | نام کامل دامنه |

- *Break out trusted SaaS locally and keep sensitive traffic on the tunnel.* ← SaaS مورد اعتماد را محلی خارج کنید و ترافیک حساس را روی Tunnel نگه دارید.

### کارت Lab

**کارت Lab:** Breakout. **هدف:** تفکیک مسیر ERP/اینترنت. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/breakout.md`. **Rollback:** حذف Default محلی.

### منابع

- Fortinet Docs: SD-WAN، Static routes، Internet Service Database (7.0)
- NIST SP 800-41

<a id="l-19-5"></a>

## درس 19-5 — ADVPN در عمل: ساخت، فرایند Shortcut، BGP/OSPF، Policy، محدودیت‌ها و عیب‌یابی

**فصل 19 · بازنویسی عمیق · پیش‌نیاز: ۱۹-۰، ۱۹-۳، ۱۸-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک مرجع؛ Lab «اجرا نشده». طبق مستند: Hub `auto-discovery-sender`، Spoke `auto-discovery-receiver`، GUI برخی گزینه‌ها را ندارد؛ shortcut override از 7.0.4.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ADVPN (Auto-Discovery VPN) را توضیح دهید: چرا و چگونه Spoke-to-Spoke مستقیم ساخته می‌شود.
2. نقش Hub (sender) و Spoke (receiver) را تنظیم کنید.
3. فرایند Shortcut (Shortcut Offer، Query، Tunnel مستقیم) را بخوانید.
4. BGP/OSPF را برای ADVPN درست تنظیم کنید.
5. ترافیک را قبل و بعد از Shortcut اثبات کنید.
6. محدودیت‌ها و خطاها را عیب‌یابی کنید.

### چرا باید یاد بگیریم؟

در Hub-and-Spoke ساده، ترافیک شعبه‌ی تهران به شعبه‌ی تبریز از Hub (مرکز) می‌گذرد: تأخیر زیاد و فشار روی Hub. تونل Full-Mesh برای ۵۰ شعبه ۱۲۲۵ تونل می‌خواهد؛ غیرعملی. ADVPN راه میانی است: ابتدا از Hub، و اگر ترافیک مستقیم بین دو شعبه دیده شد، **خودکار** یک Tunnel مستقیم (Shortcut) می‌سازد. مثل کوچه‌ی میان‌بر: ابتدا از میدان اصلی می‌روید، بعد که الگو معلوم شد، راه مستقیم باز می‌شود.

### مراحل Shortcut

``` text
1 Spoke1 -> Spoke2 traffic goes via Hub (hub-and-spoke path)
2 Hub notices Spoke1/2 pair, sends "shortcut offer" to Spoke1
3 Spoke1 sends query via Hub to Spoke2
4 Spoke1 <-> Spoke2 negotiate a direct IPsec tunnel (shortcut)
5 Later packets use direct tunnel; Hub only for routing/control
```

### پیکربندی Hub

``` text
config vpn ipsec phase1-interface
    edit "HUB-VPN"
        set type dynamic
        set interface "port1"
        set ike-version 2
        set net-device disable
        set proposal aes256-sha256
        set dhgrp 14
        set psksecret <SECRET>
        set auto-discovery-sender enable
        set add-route disable
    next
end
```

`auto-discovery-sender enable`: Hub به Spokeها Shortcut Offer می‌دهد. `net-device disable` همراه ADVPN توصیه می‌شود تا Interface منفرد مشترک بین Spokeها باشد (در 7.0 برای ADVPN با IKEv2 مستند را بررسی کنید).

### پیکربندی Spoke

``` text
config vpn ipsec phase1-interface
    edit "TO-HUB1"
        set interface "port1"
        set ike-version 2
        set net-device enable
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 198.51.100.10
        set psksecret <SECRET>
        set auto-discovery-receiver enable
        set add-route disable
    next
end
```

`auto-discovery-receiver enable`: Spoke پیشنهاد Shortcut را می‌پذیرد.

### Routing برای ADVPN

BGP/OSPF باید **Next-hop** درست را برای Spoke2 بدهد تا Spoke1 بتواند Shortcut را به آن بسازد. با iBGP و RR: `next-hop-self` را روی RR **غیرفعال** نگه دارید تا Next-hop اصلی (Spoke2) حفظ شود؛ در غیر این‌صورت Hub Next-hop می‌شود و Shortcut ساخته نمی‌شود. (جزئیات مستند ADVPN 7.0 را بررسی کنید.)

### تأیید

``` text
diagnose vpn tunnel list
diagnose vpn ike gateway list
get router info routing-table details 10.1.2.5
diagnose sniffer packet any 'host 10.1.2.5' 4 10 a
```

قبل: مسیر از `TO-HUB1`. بعد: Tunnelی جدید (`TO-HUB1_0`) به Spoke2 مستقیم و Route به همان.

### مثال‌های حل‌شده

#### مثال ساده — دیدن Shortcut

پنج بسته‌ی ping ابتدا از Hub می‌گذرد (TTL و Sniffer روی Hub)؛ بعد از Shortcut ping مستقیم: Sniffer Hub بسته‌ها را نمی‌بیند؛ Sniffer Spoke2 از IP عمومی Spoke1.

#### مثال متوسط — Next-hop

Shortcut ساخته نمی‌شود. بررسی: `get router info bgp network` ⇒ Next-hop برای 10.1.2.0/24 = Hub (RR با next-hop-self). رفع: `next-hop-self disable` روی RR یا `next-hop-self-rr`. آزمون: Next-hop = Spoke2.

#### مثال متوسط — NAT

Spoke پشت NAT: Shortcut نیازمند NAT-T و تبادل پورت؛ اگر دو سمت پشت NAT سخت (Symmetric) باشند، Shortcut شکست می‌خورد و ترافیک از Hub ادامه می‌یابد (بدون قطع). این رفتار Fail-safe است.

#### مثال سخت — ترافیک نامتقارن

Spoke1→Spoke2 مستقیم، Spoke2→Spoke1 هنوز از Hub (Shortcut یک‌طرفه) ⇒ Stateful drop. علت: Route نامتقارن/ `add-route`. رفع: هماهنگ Next-hop و `auto-discovery-receiver` در هر دو سمت. آزمون Sniffer هر دو جهت.

#### مثال سخت — مقیاس

۵۰ Spoke با Shortcutهای پویا؛ هر Spoke تا ۴۹ Tunnel پویا ممکن است. محدودیت Tunnel در مدل FortiGate (Datasheet). راه: Idle-timeout Shortcut، یا فقط ترافیک مشخص. پایش تعداد Tunnel.

### Lab هدایت‌شده (اجرا نشده)

1. Hub و دو Spoke با ADVPN.
2. Shortcut را با Sniffer اثبات کنید.
3. Next-hop اشتباه و رفع.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Shortcut نیست | Next-hop | RR |
| یک‌طرفه | receiver/Route | هر دو |
| پشت NAT | Symmetric NAT | از Hub |
| Tunnel زیاد | مقیاس | timeout |

### نکات امنیتی

Policy Spoke-to-Spoke صریح؛ Prefix-list؛ PSK/Certificate؛ Log Shortcut؛ محدودیت Shortcut.

### جمع‌بندی

ADVPN: Hub-and-Spoke اول، Shortcut مستقیم پویا؛ sender/receiver؛ Next-hop درست در BGP/OSPF؛ اثبات با Sniffer؛ NAT سخت و مقیاس محدودیت‌اند.

### تمرین و ارزیابی

**ت1.** (ساده) چه چیزی روی Hub و چه چیزی روی Spoke فعال می‌شود؟ *(پاسخ: 19-5-ت1)*

**ت2.** (ساده) ADVPN چه مشکلی را حل می‌کند؟ *(پاسخ: 19-5-ت2)*

**ت3.** (متوسط) ترافیک Spoke-to-Spoke ۴۰٪ کل است و Hub محدود پهنای‌باند دارد؛ تصمیم؟ *(پاسخ: 19-5-ت3)*

**ت4.** (متوسط) Shortcut ساخته نمی‌شود؛ ۴ علت و آزمون. *(پاسخ: 19-5-ت4)*

**ت5.** (سخت) در 7.0.3 Shortcut ترافیک را کنترل نمی‌کند. چه می‌کنید؟ *(پاسخ: 19-5-ت5)*

**ت6.** (سخت، طراحی) ریسک امنیتی Shortcut و کنترل آن. *(پاسخ: 19-5-ت6)*

**Q1.** Quick quiz (English): What security trade-off does an ADVPN shortcut introduce? *(پاسخ: 19-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Shortcut | ADVPN shortcut tunnel | Tunnel میان‌بر |
| Sender | auto-discovery-sender | فرستنده‌ی اعلان Shortcut (Hub) |
| Receiver | auto-discovery-receiver | گیرنده‌ی اعلان (Spoke) |

- *ADVPN builds shortcut tunnels on demand between spokes.* ← ADVPN در صورت نیاز Tunnel میان‌بر بین Spokeها می‌سازد.
- *Check the exact FortiOS patch level before relying on shortcut override.* ← پیش از اتکا به shortcut override سطح Patch را بررسی کنید.

### کارت Lab

**کارت Lab:** ADVPN. **وضعیت:** اجرا نشده/Unverified؛ نیاز به سه VM FortiGate. **Evidence:** `03-ops/advpn.md`. **Rollback:** غیرفعال‌کردن sender/receiver.

### منابع

- [ADVPN and shortcut paths](https://docs.fortinet.com/document/fortigate/7.0.9/administration-guide/985659/advpn-and-shortcut-paths)
- [ADVPN with BGP](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/820072/advpn-with-bgp-as-the-routing-protocol)
- [Enhanced BGP next hop updates and ADVPN shortcut override 7.0.4](https://docs.fortinet.com/document/fortigate/7.0.0/new-features/245878/enhanced-bgp-next-hop-updates-and-advpn-shortcut-override-7-0-4)

<a id="l-19-6"></a>

## درس 19-6 — آزمون معماری ۴: چندشعبه با Failover — صورت مسئله، کلید پاسخ و Rubric

**فصل 19 · بازنویسی عمیق · پیش‌نیاز: ۱۹-۰ تا ۱۹-۵ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک مرجع؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری ۴ (HQ + سه شعبه + دو Hub) را از نیازمندی تا Evidence تحویل دهید.
2. Convergence (زمان همگرایی) را اندازه‌گیری و با هدف مقایسه کنید.
3. سه عیب تزریق‌شده را فرضیه‌محور رفع کنید.
4. RCA و Evidence Index بنویسید.
5. خود را با Rubric نمره بدهید و ضعف‌ها را ثبت کنید.
6. صداقت در ثبت (اجرا نشده) را رعایت کنید.

### چرا باید یاد بگیریم؟

آزمون مثل «ماراتن کوچک» است: IP Plan، Overlay، Routing، Failover، Breakout و عیب‌یابی را در یک سناریو می‌سنجد. در دنیای واقعی مشتری نمی‌گوید «BGP خراب است»؛ می‌گوید «شعبه‌ی B به ERP نمی‌رسد». توانایی تبدیل علامت به علت در معماری کامل همین مهارت Gate است.

### صورت مسئله

سازمان: HQ (Data Center) + سه شعبه (A، B، C). هر شعبه دو ISP. دو Hub (HQ1، HQ2). نیازمندی‌ها:

1. R1: IP Plan بدون Overlap و Summary منطقه‌ای.
2. R2: Overlay IPsec IKEv2 با iBGP + Route Reflector؛ Failover Hub کمتر از ۱۰ ثانیه.
3. R3: ERP از Tunnel؛ اینترنت Local Breakout با UTM حداقلی؛ SaaS محلی.
4. R4: Guest ایزوله.
5. R5: Backup/Restore و Evidence.

عیب‌های تزریق‌شده (توسط مربی):

1. Policy یک‌طرفه Tunnel↔LAN در شعبه B.
2. Prefix-list خروجی اشتباه در شعبه C.
3. MTU Tunnel در شعبه A.

### کلید پاسخ — طراحی

``` text
HQ        10.0.0.0/16
Region A  10.1.0.0/16 (A=10.1.1.0/24, B=10.1.2.0/24, C=10.1.3.0/24)
Tunnel    10.250.0.0/16 (/30 per tunnel)
Loopback  10.254.0.0/24 (/32 each)
AS        65000 (iBGP), Hub1/Hub2 = RR
Null route 10.1.0.0/16 (distance 254) at hubs
```

Failover: BFD (300 ms × 3) + Local-Pref (Hub1=200، Hub2=100) ⇒ قطع Hub1 در ≈ ۱ ثانیه تشخیص + همگرایی BGP.

### کلید پاسخ — سه عیب

**عیب ۱ (Policy یک‌طرفه در B):**

1. علامت: LAN-B به ERP نمی‌رسد، HQ→B کار می‌کند.
2. Evidence: `diagnose sys session filter dst 10.0.5.10` ⇒ Session نیست؛ Debug Flow: `Denied by forward policy check (policy 0)`.
3. علت: Policy `TO-HUB → LAN` بدون Policy معکوس `LAN → TO-HUB`.
4. رفع: افزودن Policy معکوس.
5. تأیید: `iprope lookup` ⇒ policy؛ ping ERP OK.

**عیب ۲ (Prefix-list C):**

1. علامت: شعبه‌ی C به بقیه نمی‌رسد؛ بقیه C را نمی‌بینند.
2. Evidence: `get router info bgp neighbors <hub> advertised-routes` ⇒ 10.1.30.0/24 به‌جای 10.1.3.0/24.
3. علت: Prefix-list خروجی دارای Prefix اشتباه (تایپ).
4. رفع: اصلاح و `execute router clear bgp ip <hub> soft out`.
5. تأیید: Hub `get router info bgp network` ⇒ 10.1.3.0/24.

**عیب ۳ (MTU در A):**

1. علامت: ping کوچک OK، فایل بزرگ قطع.
2. Evidence: `ping -f -l 1400` شکست؛ Sniffer: SYN `mss 1460`.
3. علت: بدون MSS Clamp، PMTUD بلاک.
4. رفع: Clamp 1360 و MTU تونل 1400.
5. تأیید: SYN با `mss 1360`، دانلود کامل.

### اندازه‌گیری Convergence

``` text
Run: ping -t 10.0.5.10 (from Branch A)
Cut Hub1 link at t0
Measure: first lost reply -> first restored reply
Result example: 4.2 s   (target < 10 s)
```

گزارش: میانگین سه تکرار.

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| طراحی/IP Plan | 15 |
| Overlay/Routing | 20 |
| Breakout/Policy | 15 |
| Failover و اندازه‌گیری | 20 |
| عیب‌یابی سه‌گانه با RCA | 20 |
| Evidence/صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — IP Plan

بدون Overlap؛ Summary /16 با Null route. نمره‌ی کامل بخش طراحی.

#### مثال متوسط — RCA عیب ۲

``` text
Impact   : Branch C isolated from overlay, 25 min
Cause    : outbound prefix-list typo 10.1.30.0/24
Fix      : correct prefix, soft-out clear
Prevent  : config review + route-advertisement test in change checklist
```

#### مثال متوسط — Evidence Index

| عیب | فایل Evidence | دستور |
|---|---|---|
| ۱ | ev1_flow.txt | debug flow |
| ۲ | ev2_bgp.txt | advertised-routes |
| ۳ | ev3_ping_mss.txt | ping DF، sniffer |

#### مثال سخت — دو عیب هم‌زمان

B و C هم‌زمان خراب. ترتیب: اول عیب‌ای که مانع دسترسی HQ می‌شود؛ هر رفع را جدا آزمون و ثبت. اگر هم‌زمان تغییر دهید، علت قابل‌اثبات نیست.

#### مثال سخت — صداقت

Lab اجرا نشده است. گزارش باید بنویسد «خروجی‌ها نمونه‌ی آموزشی/Unverified» نه ادعای اجرا؛ نمره‌ی Evidence/صداقت به همین بستگی دارد.

### Lab هدایت‌شده (اجرا نشده)

1. سناریو را بسازید.
2. سه عیب را رفع و Evidence جمع کنید.
3. Convergence را اندازه‌گیری کنید.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Failover کند | Timer | BFD |
| یک شعبه ایزوله | Prefix/Policy | advertised-routes |
| فایل بزرگ | MTU | Clamp |

### جمع‌بندی

آزمون معماری: طراحی، Overlay، Failover، Breakout و سه عیب. Evidence، RCA و صداقت (اجرا نشده/Unverified).

### تمرین و ارزیابی

**ت1.** (ساده) چرا Summary و Null route در IP Plan آزمون آمده است؟ *(پاسخ: 19-6-ت1)*

**ت2.** (ساده) Evidence Index چه ستون‌هایی دارد؟ *(پاسخ: 19-6-ت2)*

**ت3.** (متوسط) Failover Hub با BFD 300 ms×3 و MRAI iBGP حدود 5 s چقدر است؟ *(پاسخ: 19-6-ت3)*

**ت4.** (متوسط) عیب ۱: Bytes in صفر در شعبه B. مراحل کشف و رفع. *(پاسخ: 19-6-ت4)*

**ت5.** (سخت) عیب ۲: Prefix-list خروجی شعبه C فقط Prefix اشتباه را اجازه می‌دهد. روش کشف و رفع. *(پاسخ: 19-6-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی بهبود پس از آزمون با ۵ اقدام. *(پاسخ: 19-6-ت6)*

**Q1.** Quick quiz (English): What is the purpose of the evidence index in an architecture exam? *(پاسخ: 19-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| A4 | Architecture 4 (multi-branch) | معماری ۴ |
| Rubric | Scoring rubric | ماتریس ارزیابی |
| Evidence index | Evidence index | فهرست شواهد |

- *Measure convergence and compare it with the target.* ← Convergence را اندازه بگیرید و با هدف مقایسه کنید.

### کارت Lab

**کارت Lab:** آزمون A4. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/a4.md`.

### منابع

- درس‌های ۱۹-۱ تا ۱۹-۵
- RFC 4271، RFC 2328

## پاسخ‌های فصل 19

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 19-1

**19-1-ت1** — چون Prefix یک بلوک باینری است؛ شروع بلوک باید مضرب اندازه‌ی آن باشد. 10.1.4.0/22 چهار /24 از 4 تا 7 را پوشش می‌دهد؛ 10.1.3.0–6 چنین بلوکی نمی‌سازد و باید به دو Summary شکسته شود (10.1.3.0/24 و 10.1.4.0/23 + 10.1.6.0/24 یا یک /21 بزرگ‌تر با Black hole بیشتر).

**19-1-ت2** — ۴ آدرس: شبکه، دو Host و Broadcast؛ برای ۴۰ Tunnel = ۱۶۰ آدرس. دو آدرس قابل‌استفاده برای دو سر.

**19-1-ت3** — بسته به Hub می‌رسد؛ Route دقیق‌تر برای 10.1.9.0 نیست؛ اگر Default Route (اینترنت) هست، به اینترنت می‌رود و آدرس خصوصی نشت می‌کند و Log/امنیت دچار مشکل می‌شود. Null route برای 10.1.0.0/16 (distance بالا) باعث می‌شود Longest Prefix Match آن را Drop کند ولی Routeهای دقیق‌تر شعب برنده بمانند.

**19-1-ت4** — Tunnel = 80؛ هر Tunnel یک IKE SA و حداقل یک Child SA ⇒ حدود ۱۶۰ SA (بدون Child SAهای چندگانه). این را با حد مدل مقایسه کنید.

**19-1-ت5** — مرحله ۱: کشف دقیق Overlap (اسکریپت) و ثبت Mapping آدرس واقعی↔مجازی. مرحله ۲: NAT دوطرفه موقت برای شعب Overlapدار + Log/DNS سازگار. مرحله ۳: Re-IP تدریجی هر شعبه در Change Window و حذف NAT. ریسک‌ها: ALG، DNS، Route برگشت، Log؛ برای هرکدام آزمون و Rollback.

**19-1-ت6** — Region A 10.1.0.0/16، B 10.2.0.0/16، C 10.3.0.0/16 (هر کدام تا ۲۵۶ شعبه /24)؛ Tunnel 10.250.0.0/16 (/30 ← تا ۱۶۳۸۴ Tunnel)؛ Loopback 10.254.0.0/24؛ HQ 10.0.0.0/16. Summaryها: سه /16 + HQ؛ جمعاً ۴ Route خلاصه و Null route برای هرکدام.

**19-1-Q1** — Because a prefix covers a binary block whose start address must be a multiple of the block size; otherwise it would cover addresses that are not part of the intended subnets.


### پاسخ‌های بازنویسی عمیق درس 19-2

**19-2-ت1** — Hello 10 و Dead 40 ثانیه؛ Dead چهار برابر Hello است و هر دو سر باید یکی باشند.

**19-2-ت2** — چون Hello/LSA با آدرس Tunnel ارسال می‌شود که ممکن است در Selectorهای Subnet‌های مشخص نباشد؛ Selector باز همه‌ی ترافیک Tunnel را رمز می‌کند و Routing تعیین می‌کند چه چیزی وارد شود.

**19-2-ت3** — بدون BFD ≈ 40.2 s؛ با BFD ≈ 0.9 + 0.2 ≈ 1.1 s (بدون LSA/Install چند ده میلی‌ثانیه).

**19-2-ت4** — ۱) Local-in/Policy بسته OSPF را رد می‌کند؛ ۲) Hello/Dead یا Auth ناهمسان؛ ۳) Network Type/Subnet یکسان نیست. شواهد: Sniffer proto 89، `ospf neighbor` دو سر.

**19-2-ت5** — Failback مکرر باعث Flap و Convergence پی‌درپی (CPU و قطع) می‌شود. راه‌حل: Dampening/Hold-down، افزایش recoverytime در Health-check، یا تثبیت روی پشتیبان تا پایداری، SPF throttle و BFD با Multiplier مناسب.

**19-2-ت6** — BGP: مقیاس (LSDB OSPF با ۴۰ Spoke در Area 0 بزرگ)، کنترل Policy (Local-pref/Filter)، Summary/Route Reflector ساده، Convergence قابل‌تنظیم. OSPF برای ≤ ~۱۵ شعبه یا Area منطقه‌ای قابل‌قبول است.

**19-2-Q1** — Because the tunnel can remain up while the path is broken, so default OSPF dead timers of 40 seconds create a long black hole.


### پاسخ‌های بازنویسی عمیق درس 19-3

**19-3-ت1** — مسیری که از یک iBGP Peer یاد گرفته شده به iBGP Peer دیگر داده نمی‌شود؛ برای همین Full-mesh یا RR لازم است.

**19-3-ت2** — هر Client فقط با RR صحبت می‌کند؛ ۴۲ روتر Full-mesh ۸۶۱ Session ولی RR با ۴۰ Client و ۲ RR حدود ۸۰.

**19-3-ت3** — Local-pref بالاتر (مثلاً 200) برای Hub اصلی؛ Local-pref در کل AS رعایت می‌شود و Weight فقط محلی است.

**19-3-ت4** — Peer مسیر اعلام نمی‌کند (network/redistribute)، Filter خروجی/ورودی، RR Client نبودن، Prefix-list. شاهد: advertised/received-routes و `show` Route-map.

**19-3-ت5** — با BFD ≈ 0.9 s Detect + MRAI iBGP حدود چند ثانیه + Install ≈ ۵–۷ ثانیه؛ بدون BFD تا ۱۸۰ ثانیه (یا کمتر اگر Tunnel Down شود و Session قطع شود).

**19-3-ت6** — Spoke فقط Prefix خودش را اعلام کند (Prefix-list out)؛ Hub به Spoke فقط Summary/Default بدهد؛ RR Route-map با Community برای جلوگیری از بازتاب Prefixهای ناخواسته؛ Max-prefix و Alert.

**19-3-Q1** — Clients peer only with the reflector instead of with every other router, which removes the full mesh.


### پاسخ‌های بازنویسی عمیق درس 19-4

**19-4-ت1** — کاهش Latency (حذف یک Hop تا Hub) و کاهش بار پهنای باند Hub.

Local Breakout تأخیر را کم می‌کند (حذف Hop تا Hub) و بار پهنای باند Hub را کاهش می‌دهد.

**19-4-ت2** — Longest Prefix Match: Route 10.0.0.0/8 از Tunnel دقیق‌تر از 0.0.0.0/0 است.

Longest Prefix Match: Route 10.0.0.0/8 از Tunnel دقیق‌تر از 0.0.0.0/0 است؛ پس ترافیک داخلی از Tunnel و بقیه محلی.

**19-4-ت3** — Backhaul = 55 ms؛ Breakout ≈ 22 ms؛ کاهش ≈ 33 ms (60٪).

Backhaul 55 ms در برابر Breakout 22 ms: کاهش ≈ 33 ms (حدود ۶۰٪).

**19-4-ت4** — Distance کمتر برنده است؛ iBGP پیش‌فرض 200 و Static 10؛ پس Static محلی برنده است. اگر Distance را عوض کنید یا Default محلی نباشد، Backhaul می‌شود؛ کنترل با Distance/Priority.

**19-4-ت5** — Web/DNS/File Filter و IPS سبک در شعبه، SaaS فقط با ISDB، Backhaul برای گروه پرریسک، Log و Alert مرکزی، EDR و Patch.

**19-4-ت6** — Default Route پشتیبان از Tunnel (Distance بالاتر)، Policy LAN→Tunnel→Hub→Internet با UTM مرکزی؛ هشدار؛ Failback خودکار با Hold-down؛ آزمون دوره‌ای.

**19-4-Q1** — Because routers choose the longest matching prefix, so the more specific route is used for matching destinations.


### پاسخ‌های بازنویسی عمیق درس 19-5

**19-5-ت1** — Hub: `auto-discovery-sender enable`؛ Spoke: `auto-discovery-receiver enable`.

**19-5-ت2** — ترافیک شعبه‌به‌شعبه که در Hub-and-Spoke دو بار از Hub می‌گذرد؛ با Shortcut مستقیم Latency و بار Hub کم می‌شود.

**19-5-ت3** — ADVPN یا Full-mesh انتخابی برای زوج‌های پرترافیک؛ چون سهم S2S بالا است و Hub گلوگاه می‌شود.

**19-5-ت4** — Receiver خاموش (Phase1)، Policy بین Tunnelها، Route/BGP ناقص، NAT-T؛ آزمون‌ها: Debug IKE، Log Hub، `bgp network`، Sniffer 4500.

**19-5-ت5** — محدودیت نسخه را ثبت کنید؛ بررسی release notes 7.0.4+ (shortcut override)؛ آزمون ارتقا در Lab؛ در صورت نبود امکان ارتقا: Hub-only یا Static Route برای Pairها.

**19-5-ت6** — Inspection مرکزی دور می‌شود؛ پس UTM در Spoke یا Policy حداقلی Spoke-to-Spoke، Log Shortcut مرکزی، Allow فقط Subnetهای لازم.

**19-5-Q1** — Spoke-to-spoke traffic bypasses the hub, so central inspection and logging are skipped unless the spokes enforce them.


### پاسخ‌های بازنویسی عمیق درس 19-6

**19-6-ت1** — برای کاهش Route و جلوگیری از نشت ترافیک آدرس ناموجود به اینترنت.

Summary Route تعداد Route را کم و نشت ترافیک آدرس ناموجود به اینترنت را کم می‌کند.

**19-6-ت2** — شناسه، نیازمندی، آزمون، دستور/Capture، نتیجه، فایل/زمان.

Evidence Index: شناسه، نیازمندی، آزمون، دستور/Capture، نتیجه، فایل و زمان.

**19-6-ت3** — تقریباً 0.9 s Detect + ≈ 5 s Update + Install ≈ ۶ ثانیه؛ هدف < ۱۰ ثانیه برآورده می‌شود.

**19-6-ت4** — Debug Flow در B: Denied policy 0 برای Tunnel→LAN؛ ساخت Policy؛ آزمون مثبت/منفی؛ RCA: چک‌لیست دوطرفه.

**19-6-ت5** — `advertised-routes` در C و `received-routes` در Hub؛ مقایسه با IP Plan؛ اصلاح Prefix-list (10.3.x.0/24)؛ `clear ip bgp soft`؛ تأیید Route در Spokeها.

**19-6-ت6** — BFD روی همه‌ی Tunnelها، Alert بر Prefix غیرمجاز، چک‌لیست Policy دوطرفه، استاندارد MTU/MSS، ADVPN برای زوج‌های پرترافیک.

**19-6-Q1** — It maps every requirement to the test, the raw output and the result so that the claims can be audited.

### پاسخ‌های درس افزوده‌ی 19-0 (فصل 19)

**19-0-ت1** — 20×19/2 = 190 Tunnel.

Full-mesh برای ۲۰ سایت ۱۹۰ Tunnel دارد (۲۰×۱۹/۲)؛ ADVPN/Hub-Spoke این را کم می‌کند.

**19-0-ت2** — Overlay شبکه‌ی Tunnel روی ISP؛ Underlay خود ISP و لینک‌های فیزیکی.

Overlay شبکه‌ی Tunnel روی ISP و Underlay خود ISP و لینک‌های فیزیکی است.

**19-0-ت3** — مقیاس‌پذیری، Failover خودکار و کنترل Policy؛ اضافه‌کردن شعبه بدون تغییر دستی همه‌ی مسیرها.

**19-0-ت4** — Hub Route Reflector مسیرهای iBGP را بین Spokeها بازتاب می‌دهد تا Full-mesh لازم نباشد.

**19-0-ت5** — Spoke-to-Spoke ابتدا از Hub؛ Hub به دو Spoke اطلاع می‌دهد و Shortcut مستقیم ساخته می‌شود. پیش‌نیاز: Sender روی Hub، Receiver روی Spoke، Routing/Policy مناسب و پشتیبانی نسخه.

**19-0-ت6** — دو Hub، BGP با Local-pref برای Hub اصلی، Failover خودکار، Breakout محلی با UTM برای SaaS، IP Plan یکتا.

**19-0-Q1** — Higher latency and load on the hub because spoke-to-spoke traffic must pass through it.

# فصل 20 — Remote Access VPN: SSL VPN (ایزوله) و Dial-up IPsec

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۷، ۱۸.
**اهداف:** دسترسی راه‌دور کاربران؛ SSL VPN Web/Tunnel؛ Dial-up IPsec؛ MFA مفهومی؛ Split Tunnel.
**هشدار امنیتی:** نسخه‌های 7.0.x دارای CVE شناخته‌شده در SSL VPN هستند (مثل CVE-2022-42475، CVE-2023-27997). **فقط در Lab ایزوله، بدون اتصال به اینترنت.** در تولید باید Patch شود. SSL VPN Tunnel ممکن است Needs-License باشد (`Unverified`).
**اشتباهات رایج:** باز گذاشتن SSL VPN روی WAN؛ بدون MFA؛ Split Tunnel بدون کنترل؛ Subnet Overlap با خانه.

**درس‌های فصل:**
- [درس 20-1 — مفاهیم Remote Access و ریسک](#l-20-1)
- [درس 20-2 — SSL VPN: Portal، Tunnel و Policy](#l-20-2)
- [درس 20-3 — Dial-up IPsec و Split Tunnel](#l-20-3)
- [درس 20-4 — MFA، ثبت رویداد و Hardening VPN](#l-20-4)
- [درس 20-5 — عیب‌یابی Remote Access و آزمون فصل](#l-20-5)

---

<a id="l-20-1"></a>

## درس 20-1 — معماری دسترسی راه‌دور: مدل تهدید، مقایسه‌ی VPN/ZTNA/Bastion، Posture و تصمیم‌گیری

**فصل 20 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰، ۱۷-۰، ۲۰-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده». SSL VPN فقط در Lab ایزوله (CVE).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. مدل تهدید دسترسی راه‌دور (دارایی، مهاجم، مسیر، کنترل) را بنویسید.
2. IPsec Dial-up، SSL VPN، ZTNA/Agentless و Bastion را با معیار مقایسه و برای هر گروه کاربر انتخاب کنید.
3. Posture/Device Trust، MFA و Least Privilege را در معماری وارد کنید.
4. Split tunnel و Full tunnel را با ریسک بسنجید.
5. ظرفیت (کاربر هم‌زمان، Throughput) و دسترس‌پذیری را برآورد کنید.
6. طرح نهایی را با ماتریس ریسک ارزیابی کنید.

### چرا باید یاد بگیریم؟

همه‌گیری ثابت کرد که «محل کار» دیگر یک ساختمان نیست. دسترسی راه‌دور درِ پشتی شرکت است که از اینترنت باز می‌شود؛ مهاجمان هم همین را می‌دانند. بیشتر حوادث مهم سال‌های اخیر (باج‌افزار، نفوذ از VPN آسیب‌پذیر، رمز لورفته) از همین مسیر شروع شده‌اند. انتخاب معماری درست (و نه فقط «VPN بگذاریم») تصمیمی است که ریسک سازمان را مستقیماً تعیین می‌کند. مثل انتخاب قفل برای درِ اصلی: کلید ساده یا قفل هوشمند با دوربین؟

### مدل تهدید

| عنصر | نمونه |
|---|---|
| دارایی | ERP، فایل‌سرور، DC، پایگاه‌داده |
| مهاجم | رمز لورفته، بدافزار روی لپ‌تاپ، Insider، اسکنر اینترنتی |
| مسیر | پورت VPN، Portal، کاربر آلوده، BYOD |
| کنترل | MFA، Posture، Least Privilege، Log، Patch |

سناریوهای واقعی:

1. **رمز لورفته** (Credential Stuffing) ⇒ MFA.
2. **آسیب‌پذیری VPN** (CVE) ⇒ Patch سریع، محدودیت Source، جایگزین.
3. **دستگاه آلوده** ⇒ Posture/EMS.
4. **دسترسی بیش‌ازحد** ⇒ Least Privilege و ZTNA.

### مقایسه‌ی گزینه‌ها

| معیار | IPsec Dial-up | SSL VPN | ZTNA | Bastion/Jump |
|---|---|---|---|---|
| لایه‌ی دسترسی | شبکه (L3) | شبکه/وب | برنامه‌محور | میزبان مشخص |
| Client | FortiClient/OS | Web/FortiClient | FortiClient + EMS | مرورگر/SSH |
| Least Privilege | متوسط | متوسط | بالا | بالا |
| Posture | محدود | محدود | قوی | - |
| ریسک CVE | کمتر (تاریخچه) | بالاتر (تاریخچه) | وابسته | کمتر |
| لایسنس | - | - | EMS (Needs-License) | - |

جمع‌بندی (طبق وضعیت ۷.۰): SSL VPN سابقه‌ی آسیب‌پذیری‌های جدی داشته؛ در طراحی جدید IPsec (IKEv2) یا ZTNA ترجیح دارد؛ SSL VPN فقط با Patch به‌روز و در Lab ایزوله (این دوره). (وضعیت دقیق Patch را در PSIRT فورتی‌نت بررسی کنید.)

### Split در برابر Full Tunnel

| ویژگی | Split | Full |
|---|---|---|
| ترافیک اینترنت | مستقیم از کاربر | از VPN |
| پهنای باند فایروال | کم | زیاد |
| دید امنیتی | کم | کامل |
| ریسک | کلاینت پل بین اینترنت و شبکه | کم |

تصمیم: کاربران پرخطر/BYOD ⇒ Full؛ مدیران/Managed ⇒ Split + Posture.

### ظرفیت

``` text
Concurrent users = employees x remote ratio x peak concurrency
= 400 x 0.5 x 0.8 = 160

Throughput need = users x avg Mbps
= 160 x 2 = 320 Mbps (VPN throughput, not firewall throughput)
```

ظرفیت از Datasheet «IPsec VPN Throughput» و «Concurrent SSL-VPN users» مدل؛ عدد را از مستند بخوانید.

### Posture و MFA

- MFA برای همه‌ی دسترسی (FortiToken/Third-party).
- Posture: آنتی‌ویروس فعال، OS Patch، دیسک رمز (EMS Needs-License).
- Least Privilege: گروه‌ها جدا، دسترسی به سرویس لازم (نه کل شبکه).

### مثال‌های حل‌شده

#### مثال ساده — انتخاب

۱۰ کارمند، لپ‌تاپ سازمانی، نیاز به فایل‌سرور: IPsec Dial-up + MFA کافی است.

#### مثال متوسط — گروه‌ها

| گروه | دسترسی | روش |
|---|---|---|
| مدیران IT | SSH/RDP سرورها | IPsec + MFA + Bastion |
| فروش | CRM | ZTNA یا Portal |
| پیمانکار | یک برنامه | ZTNA/Bastion، موقت |

#### مثال متوسط — ظرفیت

محاسبه بالا: 160 کاربر، 320Mbps؛ مدل باید حداقل ۲ برابر ظرفیت (حاشیه). بررسی Datasheet.

#### مثال سخت — حادثه

CVE جدید SSL VPN با Exploit فعال. اقدام: ۱) Patch فوری ۲) محدودیت Source/Geo ۳) قطع SSL VPN اگر Patch نیست و استفاده از IPsec ۴) بررسی Log برای نفوذ (IoC) ۵) تغییر رمزها. اگر این مراحل از قبل در Runbook نباشد، ساعت‌ها هدر می‌رود.

#### مثال سخت — BYOD

لپ‌تاپ شخصی بدون Posture. گزینه: Agentless/Web (دسترسی محدود به یک برنامه)، یا VDI/Bastion؛ نه VPN کامل شبکه.

### Lab هدایت‌شده (اجرا نشده)

1. مدل تهدید برای شرکت نمونه.
2. انتخاب روش برای سه گروه.
3. محاسبه‌ی ظرفیت.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| کاربران کند | Full tunnel | Split/ظرفیت |
| دسترسی بیش‌ازحد | شبکه کامل | Policy خاص |
| حادثه | Patch نبود | Runbook |

### نکات امنیتی

MFA اجباری؛ Patch؛ محدودیت Source؛ Log و آلارم نفوذ؛ آزمون دوره‌ای.

### جمع‌بندی

مدل تهدید ⇒ انتخاب (IPsec/ZTNA/Bastion)؛ SSL VPN با احتیاط؛ Posture، MFA، Least Privilege؛ ظرفیت با فرمول؛ Runbook حادثه.

### تمرین و ارزیابی

**ت1.** (ساده) چرا دسترسی راه‌دور پرریسک‌ترین مسیر ورود است؟ *(پاسخ: 20-1-ت1)*

**ت2.** (ساده) Split tunnel چه ریسکی دارد؟ *(پاسخ: 20-1-ت2)*

**ت3.** (متوسط) ظرفیت VPN برای ۶۰۰ کاربر با ۴۰٪ هم‌زمانی و ۲ Mbps میانگین چقدر است؟ *(پاسخ: 20-1-ت3)*

**ت4.** (متوسط) چرا پیمانکار نباید Full network access بگیرد؟ *(پاسخ: 20-1-ت4)*

**ت5.** (سخت) Credential stuffing را با ۵ کنترل لایه‌ای مهار کنید. *(پاسخ: 20-1-ت5)*

**ت6.** (سخت، طراحی) طرح دسترسی راه‌دور برای ۳ گروه با ظرفیت و کنترل‌ها. *(پاسخ: 20-1-ت6)*

**Q1.** Quick quiz (English): Why is multi-factor authentication essential for remote access? *(پاسخ: 20-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Posture | Device posture check | بررسی وضعیت امنیتی دستگاه |
| Bastion | Bastion/jump host | سرور واسط مدیریتی |
| ZTNA | Zero Trust Network Access | دسترسی بدون اعتماد پیش‌فرض |
| Credential stuffing | Credential stuffing | آزمون انبوه رمزهای نشت‌یافته |

- *Grant remote users only the access they need.* ← به کاربران راه‌دور فقط دسترسی لازم بدهید.

### کارت Lab

**کارت Lab:** ماتریس دسترسی. **وضعیت:** طراحی. **Evidence:** `02-design/remote-compare.md`.

### منابع

- NIST SP 800-46 Rev.2
- NIST SP 800-207 (Zero Trust)
- Fortinet Docs: IPsec/SSL VPN (7.0)

<a id="l-20-2"></a>

## درس 20-2 — SSL VPN در 7.0.3 (فقط Lab ایزوله): سازوکار، Portal، Realm، Tunnel، Split و Hardening

**فصل 20 · بازنویسی عمیق · پیش‌نیاز: ۲۰-۱، ۲۰-۷، ۱۷-۲ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده». SSL VPN فقط در Lab ایزوله (CVE).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. سازوکار SSL VPN (TLS، Web Mode، Tunnel Mode، Portal، IP Pool) را توضیح دهید.
2. در Lab ایزوله Portal، User Group، Policy و Route را بسازید.
3. Split Tunnel، DNS و Realm را تنظیم کنید.
4. Hardening (Source، MFA، Certificate، Timeout، Lockout) را اجرا کنید.
5. Log و مشکلات اتصال را عیب‌یابی کنید.
6. ریسک CVE و مسیر مهاجرت را ارزیابی کنید.

### چرا باید یاد بگیریم؟

SSL VPN هنوز در بسیاری از سازمان‌ها فعال است و در آزمون‌های NSE4 موضوع رسمی بود. ولی درس مهم‌تر این است: SSL VPN روی پورت عمومی (معمولاً 443) باز می‌ماند و در معرض اسکن جهانی است؛ آسیب‌پذیری‌های جدی تاریخی (مثلاً CVE-2018-13379 و CVE-2022-42475) نشان دادند که Patch‌نکردن به معنای نفوذ است. پس هم باید بدانید چطور ساخته می‌شود، هم چطور سخت‌گیری و در کجا نباید استفاده شود. (در این دوره فقط Lab ایزوله و بدون اتصال به اینترنت.)

### سازوکار

``` text
User -- TLS (443) --> [FortiGate SSL VPN daemon]
   Web Mode   : browser portal, proxied apps (RDP/SSH/HTTP bookmarks)
   Tunnel Mode: FortiClient creates virtual adapter, IP from pool
```

| بخش | کار |
|---|---|
| Portal | چه چیزی کاربر می‌بیند (Bookmark، Tunnel) |
| SSL VPN Settings | Interface، پورت، گواهی، IP Pool |
| User Group | چه کسی |
| Policy | چه چیزی مجاز |

### پیکربندی (Lab)

``` text
config vpn ssl settings
    set servercert "Server_Cert"
    set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
    set port 10443
    set source-interface "port1"
    set source-address "all"
    set default-portal "full-access"
end
config vpn ssl web portal
    edit "PORTAL-STD"
        set tunnel-mode enable
        set web-mode disable
        set split-tunneling enable
        set split-tunneling-routing-address "NET-CORP"
        set dns-server1 10.20.0.10
    next
end
config firewall policy
    edit 100
        set name "SSLVPN-to-CORP"
        set srcintf "ssl.root"
        set dstintf "ZN-SRV"
        set srcaddr "SSLVPN_TUNNEL_ADDR1"
        set dstaddr "NET-CORP"
        set groups "UG-VPN"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end
```

Route برگشت: شبکه‌ی `SSLVPN_TUNNEL_ADDR1` باید برای سرورها به FortiGate برگردد (اگر FortiGate Gateway آن‌ها نیست).

### Realm

Realm امکان چند Portal با نام مسیر متفاوت (`https://vpn.example:10443/staff`) و Portalهای متفاوت می‌دهد.

### Hardening

| اقدام | هدف |
|---|---|
| `source-address` محدود | کاهش اسکن/حمله |
| MFA | رمز لورفته |
| گواهی معتبر | MITM |
| `login-attempt-limit` و `login-block-time` | Brute-force |
| `idle-timeout`، `auth-timeout` | نشست طولانی |
| Patch فوری | CVE |
| `tlsv1-3`، حذف TLS 1.0/1.1 | الگوریتم ضعیف |
| بدون `web-mode` اگر لازم نیست | کاهش سطح |

``` text
config vpn ssl settings
    set ssl-min-proto-ver tls1-2
    set login-attempt-limit 3
    set login-block-time 600
    set idle-timeout 300
    set auth-timeout 28800
end
```

(نام و ارزش‌های دقیق باید با مستند 7.0 بررسی شود؛ Unverified.)

### ریسک CVE و مهاجرت

- نسخه‌ی 7.0.3 اسمی این Lab به آسیب‌پذیری‌های شناخته‌شده‌ی بعدی مبتلا است (مثلاً در 7.0.x قبل از 7.0.9 مشکل Heap Overflow در SSL VPN؛ شناسه CVE-2022-42475 — شماره‌ی نسخه‌ی Patch را از PSIRT رسمی بررسی کنید).
- بنابراین: Lab ایزوله، بدون اتصال اینترنت.
- برنامه‌ی مهاجرت: به IPsec Dial-up (۲۰-۳) یا ZTNA.

### مثال‌های حل‌شده

#### مثال ساده — Portal Tunnel

کاربر با FortiClient به `vpn.example:10443` ⇒ احراز LDAP ⇒ IP از Pool 10.212.134.x ⇒ دسترسی به 10.20.0.0/24.

#### مثال متوسط — Split و DNS

Split: فقط 10.20.0.0/24 از تونل. DNS داخلی 10.20.0.10 برای `corp.example`. آزمون: `nslookup app.corp.example` ⇒ IP داخلی. اگر DNS اشتباه: نام داخلی حل نمی‌شود.

#### مثال متوسط — Hardening

`login-attempt-limit 3`، MFA و Source فقط کشورهای مجاز (Geo). Log حمله Brute-force: `ssl-login-fail`.

#### مثال سخت — Route برگشت

اتصال برقرار، ping سرور ناموفق. Sniffer سرور: درخواست ورودی با Src 10.212.134.5؛ پاسخ به Default Gateway غیر FortiGate. رفع: Route برگشت یا NAT روی Policy (ساده‌تر ولی ردیابی کاربر ضعیف).

#### مثال سخت — CVE

Fortinet Advisory جدید. اقدام: ۱) اگر Patch ندارید، `config vpn ssl settings` را غیرفعال/محدود به Source مدیریتی ۲) بررسی Log برای IoC ۳) Patch ۴) تغییر همه‌ی رمزها و گواهی‌ها در صورت مشکوک بودن نفوذ.

### Lab هدایت‌شده (اجرا نشده)

1. Portal Tunnel با Split.
2. Hardening.
3. Route برگشت.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| اتصال نمی‌شود | پورت/گواهی | بررسی |
| وصل ولی دسترسی نه | Policy/Route | بررسی |
| نام داخلی نه | DNS | dns-server |
| Brute-force | بدون محدودیت | login-limit |

### نکات امنیتی

MFA؛ Source محدود؛ Patch؛ TLS 1.2+؛ پایش Log؛ برنامه‌ی مهاجرت.

### جمع‌بندی

SSL VPN: Portal/Tunnel/Pool؛ Hardening کامل؛ CVE‌های تاریخی؛ Lab ایزوله؛ مهاجرت به IPsec/ZTNA.

### تمرین و ارزیابی

**ت1.** (ساده) Interface مجازی ssl.root چه نقشی دارد؟ *(پاسخ: 20-2-ت1)*

**ت2.** (ساده) چرا SSL VPN 7.0.3 فقط در Lab ایزوله؟ *(پاسخ: 20-2-ت2)*

**ت3.** (متوسط) وصل شده ولی به LAN نمی‌رسد؛ سه علت و آزمون. *(پاسخ: 20-2-ت3)*

**ت4.** (متوسط) تنظیم Lockout چه حمله‌ای را کم می‌کند؟ *(پاسخ: 20-2-ت4)*

**ت5.** (سخت) CVE اعلام شد؛ اقدام فوری ۵ مرحله‌ای. *(پاسخ: 20-2-ت5)*

**ت6.** (سخت، طراحی) Hardening ۸‌مورد. *(پاسخ: 20-2-ت6)*

**Q1.** Quick quiz (English): Why is an unpatched SSL VPN a critical risk? *(پاسخ: 20-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Portal | SSL VPN portal | پروفایل دسترسی |
| Realm | SSL VPN realm | محدوده/آدرس ورود |
| ssl.root | SSL VPN virtual interface | Interface مجازی ترافیک SSL VPN |

- *Never expose an unpatched SSL VPN to the internet.* ← هرگز SSL VPN بدون Patch را در معرض اینترنت قرار ندهید.

### کارت Lab

**کارت Lab:** SSL VPN ایزوله. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/sslvpn.md`. **Rollback:** حذف Portal/Policy.

### منابع

- [SSL VPN tunnel mode replaced (7.6.3)](https://docs.fortinet.com/document/fortigate/7.6.3/fortios-release-notes/173430/ssl-vpn-tunnel-mode-no-longer-supported)
- FortiGuard PSIRT Advisories
- Fortinet Docs: SSL VPN (7.0)

<a id="l-20-3"></a>

## درس 20-3 — IPsec Dial-up (Remote Access): IKEv2، هویت، Mode Config، Split/Full، DNS و Policy

**فصل 20 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۰، ۲۰-۱، ۱۷-۳ · ≈ 9 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده». SSL VPN فقط در Lab ایزوله (CVE).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. IPsec Dial-up IKEv2 را با Phase1 dynamic و Authentication بسازید.
2. Mode Config (IP، DNS، Split) را تنظیم کنید.
3. Policy مبتنی بر گروه و Route برگشت را بنویسید.
4. MFA از طریق RADIUS (EAP) را معماری کنید.
5. مشکلات اتصال، نام و دسترسی را با Debug عیب‌یابی کنید.
6. ظرفیت و Rekey کلاینت‌های هم‌زمان را بسنجید.

### چرا باید یاد بگیریم؟

IPsec Dial-up راه سنتی و بالغ دسترسی راه‌دور است: کاربر (با FortiClient یا کلاینت بومی ویندوز/macOS) به فایروال تونل می‌زند. نسبت به SSL VPN سطح حمله‌ی کوچک‌تری دارد (UDP 500/4500) و تاریخچه‌ی آسیب‌پذیری کمتر. برای بسیاری از سازمان‌ها این گزینه‌ی پیشنهادی جایگزین SSL VPN است.

### سازوکار

``` text
Client (dynamic IP) -- IKEv2 (UDP 500/4500) --> [FortiGate: phase1 type dynamic]
   Authentication: PSK / Certificate / EAP (RADIUS+MFA)
   Mode Config: IP, DNS, split routes assigned to client
```

### Phase 1

``` text
config vpn ipsec phase1-interface
    edit "DIALUP"
        set type dynamic
        set interface "port1"
        set ike-version 2
        set peertype any
        set net-device disable
        set mode-cfg enable
        set proposal aes256-sha256
        set dhgrp 14
        set authmethod psk
        set psksecret <SECRET>
        set eap enable
        set eap-identity send-request
        set ipv4-start-ip 10.212.135.10
        set ipv4-end-ip 10.212.135.200
        set ipv4-netmask 255.255.255.0
        set ipv4-dns-server1 10.20.0.10
        set ipv4-split-include "NET-CORP"
        set dpd on-idle
    next
end
```

`eap enable` + `eap-identity send-request` برای احراز کاربر از RADIUS (NPS با MFA). `ipv4-split-include` Split.

### Phase 2

``` text
config vpn ipsec phase2-interface
    edit "DIALUP-P2"
        set phase1name "DIALUP"
        set proposal aes256-sha256
        set pfs enable
        set dhgrp 14
        set src-subnet 0.0.0.0 0.0.0.0
        set dst-subnet 0.0.0.0 0.0.0.0
    next
end
```

### Policy و Route

``` text
config firewall policy
    edit 110
        set name "DIALUP-to-CORP"
        set srcintf "DIALUP"
        set dstintf "ZN-SRV"
        set srcaddr "all"
        set dstaddr "NET-CORP"
        set groups "UG-VPN"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end
```

Route برگشت: بازه‌ی 10.212.135.0/24 باید برای سرورها به FortiGate اشاره کند.

### هویت

| روش | مزیت | عیب |
|---|---|---|
| PSK مشترک + XAuth/EAP | ساده | PSK مشترک خطرناک |
| Certificate (کاربر/دستگاه) | قوی | PKI لازم |
| EAP + RADIUS + MFA | قوی و مرکزی | NPS لازم |

توصیه: Certificate دستگاه + EAP کاربر (MFA).

### کلاینت‌ها

FortiClient (VPN-only رایگان؛ EMS برای مدیریت Needs-License)، Windows بومی IKEv2، macOS/iOS بومی. جزئیات تنظیم Client در مستند.

### ظرفیت و Rekey

هر کلاینت یک SA؛ تعداد هم‌زمان تابع مدل (Datasheet). `keylife` کوتاه‌تر برای امنیت ولی Rekey زیاد؛ `dpd` برای حذف Sessionهای مرده.

### مثال‌های حل‌شده

#### مثال ساده — اتصال

Windows IKEv2 ⇒ نام کاربر و رمز + OTP ⇒ IP 10.212.135.10 ⇒ ping 10.20.0.30 OK. `diagnose vpn ike gateway list` ⇒ `DIALUP_0`.

#### مثال متوسط — Split و DNS

Split به NET-CORP؛ سایر ترافیک مستقیم. `nslookup app.corp.example` ⇒ DNS 10.20.0.10. اگر Split نباشد: Full tunnel و اینترنت از شرکت.

#### مثال متوسط — EAP/MFA

NPS با Azure MFA Extension؛ Timeout FortiGate کم ⇒ شکست. افزایش Timeout و تنظیم کلاینت. Log NPS 6272/6273.

#### مثال سخت — Route برگشت

اتصال برقرار، فقط Ping به FortiGate OK. پاسخ سرورها به Gateway اشتباه. راه: Route یا NAT روی Policy.

#### مثال سخت — پشت NAT و Fragmentation

کاربر در هتل: UDP 500 بسته. راه‌ها: NAT-T روی UDP 4500؛ بعضی نسخه‌ها/کلاینت‌ها حالت انتقال TCP برای IKE/ESP دارند (در مستند FortiOS 7.0 و FortiClient بررسی شود؛ Unverified). کلاینت‌های بومی ممکن است شکست بخورند و باید گزینه‌ی جایگزین (مثلاً FortiClient) آزمون شود. سیاست: آزمون در شبکه‌های محدود قبل از Rollout.

### Lab هدایت‌شده (اجرا نشده)

1. Dial-up با PSK + EAP.
2. Split و DNS.
3. Route برگشت و آزمون.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| Phase1 رد | PSK/ID | بررسی |
| EAP رد | RADIUS | NPS Log |
| وصل ولی دسترسی نه | Policy/Route | بررسی |
| نام داخلی نه | DNS | ipv4-dns |

### نکات امنیتی

PSK مشترک ممنوع؛ Certificate + EAP؛ MFA؛ Policy گروهی حداقل؛ Log و DPD.

### جمع‌بندی

IPsec Dial-up: dynamic Phase1، Mode Config، EAP/MFA، Policy گروهی، Route برگشت، Split؛ جایگزین پیشنهادی SSL VPN.

### تمرین و ارزیابی

**ت1.** (ساده) type dynamic یعنی چه؟ *(پاسخ: 20-3-ت1)*

**ت2.** (ساده) Mode Config چه چیزهایی به کلاینت می‌دهد؟ *(پاسخ: 20-3-ت2)*

**ت3.** (متوسط) چرا PSK گروهی در تولید ممنوع است؟ *(پاسخ: 20-3-ت3)*

**ت4.** (متوسط) وصل است ولی erp.lab.local resolve نمی‌شود؛ مراحل. *(پاسخ: 20-3-ت4)*

**ت5.** (سخت) ۸۰۰ کلاینت: ظرفیت SA و Rekey را بسنجید. *(پاسخ: 20-3-ت5)*

**ت6.** (سخت، طراحی) معماری Dial-up با MFA برای ۲ گروه. *(پاسخ: 20-3-ت6)*

**Q1.** Quick quiz (English): Why prefer certificates or EAP over a shared pre-shared key for dial-up VPN? *(پاسخ: 20-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| EAP | Extensible Authentication Protocol | پروتکل احراز توسعه‌پذیر |
| mode-cfg | IKE mode configuration | تخصیص آدرس/DNS به کلاینت |
| NAT-T | NAT traversal | عبور از NAT |

- *Authenticate every dial-up user individually.* ← هر کاربر Dial-up را جداگانه احراز کنید.

### کارت Lab

**کارت Lab:** Dial-up. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/dialup.md`.

### منابع

- RFC 7296
- Fortinet Docs: IPsec VPN — remote access (7.0)

<a id="l-20-4"></a>

## درس 20-4 — MFA، پایش و Hardening دسترسی راه‌دور: Detection، Alert، پاسخ و بازبینی

**فصل 20 · بازنویسی عمیق · پیش‌نیاز: ۲۰-۲، ۲۰-۳، ۲۷-۰، ۲۹-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده». SSL VPN فقط در Lab ایزوله (CVE).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. MFA را برای VPN و ادمین معماری کنید (FortiToken، OTP سه‌طرف، Push).
2. Detection (تشخیص): Log، Alert و شاخص‌های حمله به VPN را تعریف کنید.
3. Response (واکنش): قطع نشست، Block IP، Reset رمز را در Runbook بنویسید.
4. Hardening دسترسی راه‌دور را در چک‌لیست جمع کنید.
5. شکست MFA و حساب Break-glass را مدیریت کنید.
6. گزارش دوره‌ای دسترسی راه‌دور را بسازید.

### چرا باید یاد بگیریم؟

رمز سخت‌ترین قفل نیست: لورفته می‌شود، حدس زده می‌شود، فیشینگ می‌شود. MFA (Multi-Factor Authentication، یعنی «احراز چندعاملی») مثل داشتن کلید + اثر انگشت است؛ حتی اگر رمز لو برود، مهاجم عامل دوم را ندارد. ولی MFA بدون پایش کافی نیست: شما باید ببینید چه کسی، از کجا، چه زمانی و چند بار وارد شد. VPN دروازه‌ی عمومی است؛ هر ناهنجاری باید سریع دیده و پاسخ داده شود.

### عامل‌ها

| عامل | مثال |
|---|---|
| چیزی که می‌دانید | رمز |
| چیزی که دارید | توکن/موبایل |
| چیزی که هستید | بیومتریک |

### گزینه‌های MFA در FortiGate

| روش | توضیح | نکته |
|---|---|---|
| FortiToken Mobile | OTP/Push | لایسنس: ۲ توکن رایگان؛ بیشتر Needs-License |
| Email/SMS OTP | کد | SMS ضعیف‌تر |
| RADIUS + MFA Provider (Azure MFA/Duo) | Push | Timeout بلندتر |
| SAML (IdP) | SSO + MFA | بسته به مورد استفاده |

``` text
config user local
    edit "alice"
        set type ldap
        set ldap-server "LDAP-CORP"
        set two-factor fortitoken
        set fortitoken "FTKMOB1234567890"
        set email-to "alice@example.com"
    next
end
```

(سینتکس و محدودیت تعداد توکن‌ها در مستند 7.0 بررسی شود؛ Unverified.)

### Detection

شاخص‌ها:

| شاخص | معنی |
|---|---|
| چندین `login-fail` از یک IP | Brute-force |
| ورود موفق از کشور/ساعت غیرعادی | سوءاستفاده از حساب |
| یک کاربر هم‌زمان از دو مکان | اشتراک/سرقت |
| حجم داده‌ی زیاد | استخراج داده |
| Tunnel پایدار بدون فعالیت | اتصال مشکوک |

Log را به FortiAnalyzer/SIEM بفرستید؛ Alert برای آستانه‌ها.

``` text
execute log filter category 1
execute log filter field subtype vpn
execute log display
diagnose vpn ssl list
diagnose vpn ike gateway list
```

### Response — Runbook

1. تأیید هشدار (کاربر، IP، زمان).
2. قطع نشست: `diagnose vpn ike gateway clear name DIALUP_0` یا `execute vpn sslvpn del-tunnel`.
3. Block: Local-in Policy/Address Group برای IP مشکوک.
4. Reset رمز و Revoke توکن/گواهی.
5. بررسی دسترسی انجام‌شده (Log).
6. گزارش حادثه.

### Hardening چک‌لیست

1. MFA اجباری.
2. Source محدود (Geo/IP).
3. Patch فعال.
4. TLS/IKE الگوریتم قوی.
5. Lockout و Rate-limit.
6. Policy حداقل (نه ALL).
7. Log مرکزی و Alert.
8. حساب Break-glass.
9. بازبینی فصلی کاربران.

### مثال‌های حل‌شده

#### مثال ساده — Brute-force

Log: ۴۰ `login-fail` در ۲ دقیقه از 203.0.113.99. اقدام: Block IP (Local-in) و بررسی هیچ ورود موفق. `login-block-time` به‌صورت خودکار هم کمک می‌کند.

#### مثال متوسط — MFA شکست

کاربر OTP را وارد می‌کند و رد می‌شود. علت: ساعت FortiToken/گوشی اختلاف. رفع: همگام‌سازی زمان؛ در Push: Timeout.

#### مثال متوسط — ورود غیرعادی

alice ساعت ۳ شب از کشور دیگر وارد می‌شود و ۲ ساعت قبل در ایران بود (Impossible Travel). اقدام: Revoke نشست، تماس با کاربر، Reset رمز.

#### مثال سخت — رمز لورفته با MFA Fatigue

مهاجم رمز را دارد و Push را ده‌ها بار می‌فرستد تا کاربر خسته شود و تأیید کند (MFA Fatigue). دفاع: Number Matching، محدودیت تعداد Push، آموزش «هر Push ناخواسته را رد کنید و گزارش دهید»، Alert روی Pushهای رد‌شده.

#### مثال سخت — قطع MFA Provider

Azure MFA/Duo Down. Fail-open یا Fail-close؟ سیاست: ادمین‌ها Break-glass محلی (Fail-close برای کاربران، Fail-open ممنوع)، پایش سرویس، و Runbook ارتباط.

### Lab هدایت‌شده (اجرا نشده)

1. MFA با FortiToken.
2. Alert Brute-force.
3. Runbook Response.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| OTP رد | زمان | همگام |
| Push نمی‌رسد | Provider | بررسی |
| Alert نیست | Log مرکزی | ارسال |
| Brute-force | بدون Limit | Lockout |

### نکات امنیتی

MFA مقاوم به فیشینگ (FIDO2/Certificate) ترجیح؛ Number Matching؛ Break-glass؛ بازبینی دسترسی.

### جمع‌بندی

MFA + Detection + Response + Hardening؛ شاخص‌های Brute-force/Impossible Travel؛ MFA Fatigue؛ Runbook و Break-glass.

### تمرین و ارزیابی

**ت1.** (ساده) Lockout چیست؟ *(پاسخ: 20-4-ت1)*

**ت2.** (ساده) چرا ورود موفق پس از ناموفق‌ها خطرناک‌تر است؟ *(پاسخ: 20-4-ت2)*

**ت3.** (متوسط) آستانه‌ی Alert را چگونه تعیین می‌کنید؟ *(پاسخ: 20-4-ت3)*

**ت4.** (متوسط) پس از Block IP چه چیزی را باید بررسی کنید؟ *(پاسخ: 20-4-ت4)*

**ت5.** (سخت) Playbook ورود مشکوک را در ۶ مرحله بنویسید. *(پاسخ: 20-4-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی بازبینی ماهانه/فصلی دسترسی VPN. *(پاسخ: 20-4-ت6)*

**Q1.** Quick quiz (English): Which VPN log pattern most strongly indicates a successful brute-force attack? *(پاسخ: 20-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MTTD | Mean Time To Detect | میانگین زمان کشف |
| PIR | Post-incident review | بازبینی پس از حادثه |
| Lockout | Account lockout | قفل حساب |

- *Alert on a successful login that follows many failures.* ← روی ورود موفق پس از شکست‌های متعدد هشدار بدهید.

### کارت Lab

**کارت Lab:** Hardening/Detection VPN. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/vpn-hardening.md`.

### منابع

- NIST SP 800-61
- NIST SP 800-63B
- Fortinet Docs: Log and report (7.0)

<a id="l-20-5"></a>

## درس 20-5 — آزمون عملی دسترسی راه‌دور: SSL-VPN/IPsec Dial-up، MFA و Split Tunnel — صورت مسئله، کلید کامل و Rubric

**فصل 20 · بازنویسی عمیق · پیش‌نیاز: ۲۰-۱ تا ۲۰-۴ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. دسترسی راه‌دور را با گروه‌های جدا، MFA و Policy حداقلی طراحی و پیاده کنید.
2. Split Tunnel را در برابر Full Tunnel با ریسک انتخاب و پیکربندی کنید.
3. سه خرابی (Authentication، Policy/Route، DNS/Split) را با Evidence رفع کنید.
4. آزمون منفی (کاربر غیرمجاز، سرویس غیرمجاز) را اجرا کنید.
5. گزارش و RCA تحویل دهید.
6. خود را با Rubric نمره دهید.

### چرا باید یاد بگیریم؟

آزمون چهار ادعا را اثبات می‌کند: ورود مجاز موفق، ورود غیرمجاز رد، Split صحیح، MFA فعال. دورکاری یعنی درِ اصلی شبکه برای کاربران باز است؛ اگر رمز کاربری لو برود و MFA یا Policy حداقلی نباشد، مهاجم به همه‌چیز می‌رسد. این Gate نشان می‌دهد شما هم می‌سازید، هم ثابت می‌کنید.

### صورت مسئله

۱۲۰ کاربر دورکار. گروه‌ها:

1. `GRP-FIN`: فقط به `10.20.0.10:443` و `10.20.0.11:445`.
2. `GRP-IT`: SSH به شبکه‌ی Mgmt (`10.99.0.0/24`).

الزام‌ها: MFA، Log تمام اتصال‌ها، Split Tunnel، DNS داخلی.

عیب‌های تزریق‌شده:

1. کاربران FIN احراز می‌شوند ولی به سرور نمی‌رسند.
2. نام داخلی `erp.corp.example` حل نمی‌شود.
3. GRP-IT به همه‌ی 10.99.0.0/24 می‌رسد در حالی که فقط باید به 10.99.0.10 برسد (Policy بیش‌ازحد).

### طراحی مرجع

| مورد | تصمیم |
|---|---|
| نوع | IPsec Dial-up IKEv2 (ترجیح) یا SSL-VPN Tunnel (7.0.3) |
| احراز | LDAP/AD + FortiToken (EAP/RADIUS) |
| Pool | 10.212.134.0/24 |
| Split | 10.20.0.0/16 و 10.99.0.0/24 |
| DNS | 10.20.0.10 |
| Policy | یک Policy برای هر گروه، سرویس مشخص |

### کلید پاسخ — Policy حداقلی

``` text
config firewall policy
    edit 201
        set name "VPN-FIN-ERP"
        set srcintf "DIALUP"
        set dstintf "ZN-SRV"
        set srcaddr "all"
        set dstaddr "HOST-ERP" "HOST-FS"
        set groups "GRP-FIN"
        set service "HTTPS" "SMB"
        set action accept
        set schedule "always"
        set logtraffic all
    next
    edit 202
        set name "VPN-IT-SSH"
        set srcintf "DIALUP"
        set dstintf "ZN-MGMT"
        set srcaddr "all"
        set dstaddr "HOST-MGMT-BASTION"
        set groups "GRP-IT"
        set service "SSH"
        set action accept
        set schedule "always"
        set logtraffic all
    next
end
```

### کلید پاسخ — سه عیب

**عیب ۱ (FIN نمی‌رسد):**

1. Evidence: `diagnose firewall iprope lookup 10.212.134.5 40000 10.20.0.10 443 tcp DIALUP` ⇒ policy 0.
2. علت: `srcintf` Policy روی `ssl.root` در حالی که کاربران Dial-up‌اند (Interface اشتباه).
3. رفع: srcintf = DIALUP (یا ssl.root برای SSL).
4. تأیید: Lookup ⇒ policy 201.

**عیب ۲ (DNS):**

1. Evidence: `nslookup erp.corp.example` ⇒ Timeout؛ `ipconfig /all` DNS عمومی.
2. علت: `ipv4-dns-server1`/`dns-server1` تنظیم نیست یا Split DNS.
3. رفع: DNS 10.20.0.10 و Policy UDP/53 به DNS برای گروه.
4. تأیید: nslookup ⇒ IP داخلی.

**عیب ۳ (Policy بیش‌ازحد IT):**

1. Evidence: Lookup به 10.99.0.50:22 ⇒ مجاز.
2. علت: dstaddr = NET-MGMT.
3. رفع: dstaddr = HOST-MGMT-BASTION.
4. آزمون منفی: Lookup به 10.99.0.50 ⇒ policy 0.

### آزمون منفی

| آزمون | انتظار |
|---|---|
| کاربر FIN به SSH Mgmt | Deny |
| کاربر IT به ERP | Deny |
| کاربر غیرعضو | Deny/Reject احراز |
| رمز درست و OTP غلط | Reject |
| IP خارج از Geo مجاز | Block (در صورت تنظیم) |

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| طراحی و Policy حداقلی | 20 |
| MFA | 15 |
| Split/DNS | 15 |
| رفع سه عیب با Evidence | 30 |
| آزمون منفی | 10 |
| RCA/صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Lookup

alice(FIN) ⇒ ERP:443: Lookup ⇒ policy 201 ⇒ OK. Log user=alice group=GRP-FIN.

#### مثال متوسط — RCA عیب ۲

``` text
Impact   : internal names unresolved for VPN users, 40 min
Cause    : DNS server not pushed to clients
Fix      : set DNS 10.20.0.10 in mode-config + allow UDP/53
Prevent  : post-change test list includes nslookup
```

#### مثال متوسط — Split

Split فقط 10.20.0.0/16 و 10.99.0.0/24؛ `route print` در کلاینت فقط همین‌ها را از VPN نشان می‌دهد. اینترنت مستقیم.

#### مثال سخت — دو عیب هم‌زمان

DNS و Policy هر دو. ابتدا Policy (قطع دسترسی)، آزمون؛ سپس DNS. اگر یک‌جا تغییر کند و باز هم کار نکند، علت معلوم نیست.

#### مثال سخت — صداقت

Lab اجرا نشده؛ خروجی‌ها آموزشی/Unverified؛ هرگز Evidence جعلی ثبت نشود.

### Lab هدایت‌شده (اجرا نشده)

1. طراحی را پیاده کنید.
2. سه عیب را رفع کنید.
3. آزمون منفی و RCA.

### عیب‌یابی سریع

| علامت | علت | رفع |
|---|---|---|
| policy 0 | Interface/Group | Lookup |
| نام نه | DNS | mode-config |
| بیش‌ازحد | dstaddr | تنگ |
| MFA | زمان | همگام |

### جمع‌بندی

آزمون دورکاری: Policy حداقلی، MFA، Split و DNS، سه عیب با Evidence، آزمون منفی، RCA و صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) چرا MFA؟ *(پاسخ: 20-5-ت1)*

**ت2.** (ساده) Split Tunnel چیست؟ *(پاسخ: 20-5-ت2)*

**ت3.** (متوسط) وصل است ولی به سرور نمی‌رسد؛ مراحل. *(پاسخ: 20-5-ت3)*

**ت4.** (متوسط) چرا گواهی Factory مناسب نیست؟ *(پاسخ: 20-5-ت4)*

**ت5.** (سخت) Split Tunnel ریسک و جبران. *(پاسخ: 20-5-ت5)*

**ت6.** (سخت، طراحی) دو گروه با دسترسی متفاوت. *(پاسخ: 20-5-ت6)*

**Q1.** Quick quiz (English): Why is MFA recommended for remote access VPN? *(پاسخ: 20-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MFA | Multi-Factor Authentication | احراز چندعاملی |
| EDR | Endpoint Detection and Response | تشخیص و پاسخ نقطه‌ی پایانی |

- *Remote access must use multi-factor authentication.* ← دسترسی راه‌دور باید از MFA استفاده کند.

### کارت Lab

**کارت Lab:** آزمون دسترسی راه‌دور (اجرا نشده). **Evidence:** `03-ops/g-remote.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: SSL VPN; IPsec dial-up
- FortiOS 7.0 SSL VPN guide

## درس 20-7 — SSL VPN در برابر IPsec Remote Access: وضعیت نسخه‌ها، ریسک و مهاجرت

**فصل ۲۰ · درس افزوده (پس از ۲۰-۵) · پیش‌نیاز: ۱۸-۰، ۲۰-۱ تا ۲۰-۵ · ≈ ۵ ساعت**

> **وضعیت نسخه (تأییدشده از مستند رسمی):** در **FortiOS 7.6.3** حالت **SSL VPN Tunnel mode حذف شده** و با IPsec VPN (قابل اجرا روی TCP 443) جایگزین شده است؛ پیش از ارتقا باید تنظیمات تبدیل شود و تنظیمات پشتیبانی‌نشده پس از ارتقا حذف می‌شوند؛ **Web mode** با نام **Agentless VPN** باقی می‌ماند؛ IPsec Portal ندارد ([SSL VPN tunnel mode replaced with IPsec VPN](https://docs.fortinet.com/document/fortigate/7.6.3/fortios-release-notes/173430/ssl-vpn-tunnel-mode-no-longer-supported)، [Migration guide](https://docs.fortinet.com/document/fortigate/7.6.3/administration-guide/155142/ssl-vpn-tunnel-mode-to-ipsec-vpn-migration-new)). نسخه‌ی هدف دوره **7.0.3** است که هنوز SSL VPN Tunnel mode دارد؛ این درس «چرخه‌ی عمر» را برای تصمیم طراحی می‌گوید. Lab «اجرا نشده».

### ۱) هدف آموزشی

1. تفاوت **SSL VPN (Web/Tunnel)** و **IPsec Remote Access (Dial-up)** را از نظر سازوکار، کلاینت، عبور از فایروال و امنیت بگوید.
2. بداند چرا Fortinet مسیر را از SSL VPN Tunnel به IPsec برده و پیامد برای طراحی امروز چیست.
3. ریسک‌های امنیتی SSL VPN (CVEهای شناخته‌شده روی 7.0.x) را در تصمیم دخالت دهد.
4. طرح **مهاجرت** از SSL VPN به IPsec را بنویسد.
5. برای نیازهای مختلف (کلاینت مدیریت‌شده، BYOD، مرورگر) گزینه‌ی مناسب را انتخاب کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا جدول تصمیم؟** انتخاب بین SSL-VPN و IPsec بر پایه‌ی ریسک و محدودیت شبکه‌ی کاربر باشد نه عادت. پروژه‌ی جدید: IPsec IKEv2 + MFA؛ SSL-VPN فقط با نسخه‌ی وصله‌شده و دلیل مشخص.

**جمع‌بندی اصلی درس:**

IPsec (۱۸-۰)، Authentication (فصل ۱۷)، مدل تهدید (۱۱-۰).

### ۳) مفهوم پایه

دسترسی راه‌دور دو نیاز دارد: **هویت قوی** و **کانال امن**. SSL VPN روی TLS (معمولاً TCP 443) کار می‌کند و از اغلب فایروال‌ها عبور می‌کند؛ IPsec سنتی روی UDP 500/4500 و ESP است و گاهی مسدود می‌شود. محبوبیت SSL VPN از «عبور آسان» بود؛ ولی چون به‌صورت **سرویس عمومی روی اینترنت** با کد پیچیده‌ی Web در معرض است، هدف اصلی مهاجمان بوده و آسیب‌پذیری‌های متعدد داشته است.

### ۴) توضیح عمیق فنی

| معیار | SSL VPN Web mode | SSL VPN Tunnel mode | IPsec Dial-up (IKEv2) |
|---|---|---|---|
| کلاینت | مرورگر | FortiClient | FortiClient/کلاینت استاندارد IKEv2 |
| پورت | TCP 443 | TCP 443 | UDP 500/4500؛ در نسخه‌های جدید امکان TCP (طبق مستند 7.6.3) |
| لایه | کاربرد (Proxy) | لایه ۳ روی TLS | لایه ۳ |
| دسترسی | وب‌اپ‌ها/Bookmark | کل شبکه | کل شبکه |
| Portal | دارد | دارد | ندارد |
| وضعیت در 7.6.3 | باقی (Agentless VPN) | **حذف** | ادامه، جایگزین |
| سطح حمله | بالا (سرویس وب) | بالا | کمتر (سطح حمله‌ی IKE) |

نکات:

- هیچ‌یک «کاملاً ایمن» نیستند؛ مدیریت Patch، MFA و محدودسازی Source حیاتی است.
- سرور SSL VPN روی WAN همان Interface مدیریت نیست، ولی روی همان سرویس HTTPS دستگاه ممکن است باشد؛ آسیب‌پذیری‌ها (مانند CVE-2022-42475، CVE-2023-27997 در خطوط 7.0 و قبل/بعد) روی این سطح بوده‌اند (در ریپو: Lab ایزوله).
- مهاجرت به IPsec: Portalها، Realm، و برخی Bookmarkها منتقل نمی‌شوند؛ سناریوهای Web mode باید با Agentless VPN یا ZTNA بازطراحی شوند.

### ۵) مثال حل‌شده (تصمیم طراحی)

#### مثال ساده

کاربر هتل با UDP مسدود ⇒ SSL-VPN یا NAT-T/TCP.

#### مثال متوسط

IPsec برای کارمندان؛ SSL فقط پیمانکار.

#### مثال سخت — مهاجرت

Inventory ← پایلوت ← آموزش ← عبور ← خاموش‌کردن ← بازبینی Log.

#### مثال‌های اصلی درس (مرور)

**نیاز:** ۲۰۰ کارمند، لپ‌تاپ مدیریت‌شده، MFA، دسترسی به شبکه‌ی داخلی؛ ۱۰ پیمانکار فقط به یک وب‌اپ.

| گروه | راه‌حل | دلیل |
|---|---|---|
| کارمندان | IPsec Dial-up IKEv2 + گواهی/MFA | سطح حمله کمتر، مسیر پشتیبانی‌شده‌ی آینده |
| پیمانکاران | Agentless VPN/ZTNA برای یک اپ | حداقل دسترسی |
| نسخه‌ی 7.0.3 Lab | SSL VPN فقط ایزوله برای آموزش | CVE، بدون اینترنت |

**مثال مهاجرت (چک‌لیست):** (۱) فهرست کاربران/گروه/Portal. (۲) ساخت IPsec Dial-up و آزمون با گروه کوچک. (۳) Split-tunnel و DNS. (۴) MFA. (۵) آموزش کاربران (کلاینت). (۶) نقطه‌ی بازگشت (Backup Config). (۷) خاموش‌کردن SSL VPN. (۸) آزمون منفی (دسترسی از WAN به پورت SSL VPN بسته).

### ۶) پیاده‌سازی: GUI/CLI (مفهوم)

**GUI (7.0.3):** VPN → IPsec Wizard → Remote Access (Dial-up) برای IPsec؛ VPN → SSL-VPN Settings/Portals برای SSL VPN. **CLI:** `config vpn ipsec phase1-interface` با `type dynamic`؛ `config vpn ssl settings` برای SSL VPN (`Unverified`؛ با درس‌های ۲۰-۲/۲۰-۳ و ۱۸-۰ تطبیق دهید).

### ۷) Troubleshooting

| علامت | علت |
|---|---|
| کلاینت وصل نمی‌شود | Policy/Portal/Port، Certificate |
| وصل می‌شود ولی شبکه نه | Policy/Route/Split-tunnel |
| پس از ارتقا SSL VPN کار نمی‌کند | حذف Tunnel mode در 7.6.3؛ نیاز مهاجرت |

### ۸) نکات امنیتی

- سرویس SSL VPN را به Source مجاز محدود و MFA فعال کنید.
- Patch سریع؛ نسخه‌ی 7.0.x قدیمی است.
- ثبت و هشدار ورود ناموفق.

### ۹) جمع‌بندی مفهومی

- SSL VPN Tunnel در 7.6.3 حذف شده؛ Web mode به Agentless VPN تبدیل شده؛ IPsec Portal ندارد.
- IPsec Dial-up سطح حمله‌ی کمتر و مسیر آینده است.
- طراحی را بر اساس چرخه‌ی عمر ویژگی بگذارید، نه فقط سهولت.
- نسخه‌ی Lab 7.0.3 با تولید امروز یکی نیست؛ آموزش را با یادداشت نسخه همراه کنید.

### ۱۰) تمرین و ارزیابی

**ت1.** (ساده) چه چیزی در FortiOS 7.6.3 از SSL VPN حذف شد؟ *(پاسخ: 20-7-ت1)*

**ت2.** (ساده) Agentless VPN چیست؟ *(پاسخ: 20-7-ت2)*

**ت3.** (متوسط) چرا IPsec سطح حمله‌ی کمتری دارد؟ *(پاسخ: 20-7-ت3)*

**ت4.** (سخت) چک‌لیست مهاجرت ۸ مرحله‌ای را با ریسک هر مرحله بنویسید. *(پاسخ: 20-7-ت4)*

**ت5.** (سخت، طراحی) برای ۳ گروه کاربر گزینه‌ی دسترسی راه‌دور را انتخاب و دلیل بنویسید. *(پاسخ: 20-7-ت5)*

**Q1.** Quick quiz (English): Why is the lifecycle status of a feature part of a design decision? *(پاسخ: 20-7-Q1)*

### ۱۱) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Agentless VPN | Agentless VPN (web mode) | دسترسی مرورگری بدون کلاینت |
| ZTNA | Zero Trust Network Access | دسترسی بدون اعتماد پیش‌فرض |
| Split tunnel | Split tunneling | عبور بخشی از ترافیک از VPN |
| CVE | Common Vulnerabilities and Exposures | شناسه‌ی آسیب‌پذیری |

- *SSL VPN tunnel mode is no longer supported from FortiOS 7.6.3.* ← SSL VPN Tunnel mode از FortiOS 7.6.3 به بعد پشتیبانی نمی‌شود.
- *Plan the migration before upgrading.* ← قبل از ارتقا مهاجرت را برنامه‌ریزی کنید.

### ۱۲) منابع

- Fortinet Docs: [SSL VPN tunnel mode replaced with IPsec VPN (7.6.3)](https://docs.fortinet.com/document/fortigate/7.6.3/fortios-release-notes/173430/ssl-vpn-tunnel-mode-no-longer-supported)، [SSL VPN tunnel mode to IPsec VPN migration](https://docs.fortinet.com/document/fortigate/7.6.3/administration-guide/155142/ssl-vpn-tunnel-mode-to-ipsec-vpn-migration-new).
- FortiGuard PSIRT Advisories (CVE-2022-42475، CVE-2023-27997) — مراجعه‌ی مستقیم.

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: جدول تصمیم SSL VPN در برابر IPsec RA

| معیار | SSL VPN | IPsec Dial-up |
|---|---|---|
| عبور از فایروال مهمان (443) | آسان | سخت‌تر (UDP/500/4500) |
| سطح حمله‌ی تاریخی | بالا | کمتر |
| کلاینت | FortiClient/مرورگر | FortiClient |
| روند مستند | بررسی PSIRT نسخه | — |

توصیه‌ی عملی: برای پروژه‌ی جدید IPsec IKEv2 + MFA؛ SSL VPN فقط با نسخه‌ی وصله‌شده طبق مستند Fortinet.

**پرسش‌های مصاحبه**
1. *چرا مهاجرت؟* ریسک آسیب‌پذیری.
2. *UDP مسدود؟* NAT-T/TCP.
3. *Patch؟* پایش PSIRT.

### تکمیل عمیق: SSL VPN در برابر IPsec RA — جدول تصمیم

#### چرا؟

انتخاب بین دو فناوری باید بر اساس ریسک، محدودیت شبکه‌ی کاربر و عملیات باشد نه عادت.

#### جدول تصمیم

| معیار | SSL VPN | IPsec RA |
|---|---|---|
| عبور از شبکه‌های محدود (443) | آسان | سخت‌تر (UDP 500/4500) |
| سابقه‌ی آسیب‌پذیری | بالا | کمتر |
| Performance | متوسط | بهتر (NPU) |
| مدیریت کلاینت | FortiClient/وب | FortiClient |

#### مثال ساده

کاربران هتل/فرودگاه که UDP مسدود دارند ⇒ SSL VPN یا IPsec over TCP (در صورت پشتیبانی نسخه).

#### مثال متوسط — تصمیم برای پروژه‌ی جدید

IPsec IKEv2 + MFA + گواهی؛ SSL VPN فقط برای سناریوی مشخص و با نسخه‌ی وصله‌شده.

#### مثال سخت — مهاجرت

مراحل: ۱) Inventory کاربران ۲) پایلوت IPsec ۳) آموزش ۴) عبور تدریجی ۵) خاموش‌کردن SSL VPN ۶) بازبینی Log.

#### Lab

جدول تصمیم را برای سازمان فرضی خودتان پر کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| UDP مسدود | شبکه‌ی کاربر | NAT-T/TCP |
| کلاینت قدیمی | نسخه | ارتقا |
| مهاجرت کند | آموزش | پایلوت |

#### پرسش‌ها با پاسخ

**۱. چرا مهاجرت؟** ریسک.
**۲. UDP مسدود چه کنیم؟** NAT-T/TCP.
**۳. پایلوت چرا؟** کاهش ریسک.

#### English Corner

- *Choose the technology by risk and network constraints, not habit.*
- Q: What do you do when UDP 500 and 4500 are blocked?

<a id="l-20-8"></a>

## درس 20-8 — SSL-VPN در FortiGate: Web Mode، Tunnel Mode، Portal، Realm و Split Tunnel

**فصل 20 · درس افزوده برای سرفصل رسمی NSE 4 (FortiOS 7.0): «Configure and implement different SSL-VPN modes to provide secure access to the private network» · پیش‌نیاز: ۲۰-۱، ۲۰-۲**

> **وضعیت:** نظری/مستندی؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ SSL-VPN فقط در Lab ایزوله و با نسخه‌ی وصله‌شده (به PSIRT نگاه کنید)؛ Lab اجرا نشده.

### ۱) این درس درباره چیست و چرا باید یاد بگیریم؟

**چه چیزی یاد می‌گیریم:** دو حالت SSL-VPN (Web Mode و Tunnel Mode)، سه نوع Portal، چطور کاربران به Portal نگاشت می‌شوند، Split Tunnel چه می‌کند و چطور Policy را می‌نویسیم.

**چرا لازم است؟** کاربر دورکار گاهی فقط می‌خواهد یک سامانه‌ی داخلی را در مرورگر ببیند (Web Mode) و گاهی دسترسی کامل شبکه‌ای می‌خواهد (Tunnel Mode). اگر هر دو را یکسان باز کنید، سطح دسترسی بیش‌ازحد می‌شود؛ اگر اشتباه انتخاب کنید، یا کاربر به منبع نمی‌رسد یا مهاجم بیش از لازم می‌بیند. این دقیقاً سؤال آزمون NSE4 است.

### ۲) توضیح از پایه

#### ۲-۱) دو حالت

| حالت | شرح | کلاینت | مثال |
|---|---|---|---|
| Web Mode | فایروال به‌عنوان «پروکسی» عمل می‌کند؛ کاربر در مرورگر صفحه‌ی Portal با **Bookmark** (HTTP/HTTPS، RDP، SSH، VNC، FTP، SMB ...) می‌بیند | فقط مرورگر | سامانه‌ی داخلی وب |
| Tunnel Mode | روی کلاینت یک کارت مجازی و IP از Pool ساخته می‌شود؛ ترافیک شبکه‌ای از تونل می‌گذرد | FortiClient | دسترسی کامل شبکه |

#### ۲-۲) انواع Portal

- **web-access:** فقط Web Mode.
- **tunnel-access:** فقط Tunnel Mode.
- **full-access:** هر دو.

#### ۲-۳) نگاشت کاربر به Portal

در تنظیمات SSL-VPN، **Authentication Rule** کاربر/گروه را به Portal (و Realm) وصل می‌کند.

``` text
config vpn ssl settings
 set servercert "corp-cert"
 set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
 set source-interface "port1"
 set default-portal "web-access"
 config authentication-rule
  edit 1
   set groups "G-VPN-FULL"
   set portal "full-access"
  next
  edit 2
   set groups "G-VPN-WEB"
   set portal "web-access"
  next
 end
end
```

#### ۲-۴) Portal و Bookmark

``` text
config vpn ssl web portal
 edit "web-access"
  set web-mode enable
  config bookmark-group
   edit "Internal"
    config bookmarks
     edit "Portal"
      set apptype web
      set url "https://intranet.example.com"
     next
     edit "Server RDP"
      set apptype rdp
      set host "10.20.0.30"
     next
    end
   next
  end
 next
end
config vpn ssl web portal
 edit "tunnel-access"
  set tunnel-mode enable
  set ip-pools "SSLVPN_TUNNEL_ADDR1"
  set split-tunneling enable
  set split-tunneling-routing-address "INTERNAL-NETS"
  set dns-server1 10.20.0.5
 next
end
```

(نام و ساختار دقیق را در نسخه‌ی خود بررسی کنید.)

#### ۲-۵) Split Tunnel

- **Full Tunnel:** همه‌ی ترافیک کلاینت (از جمله اینترنت) از فایروال می‌گذرد؛ کنترل بیشتر، بار بیشتر.
- **Split Tunnel:** فقط مسیرهای مشخص (شبکه‌ی داخلی) از تونل می‌روند؛ اینترنت مستقیم.

**Split DNS:** نام‌های داخلی را فقط با DNS داخلی حل کند تا نشت (Leak) نشود.

#### ۲-۶) Policy

ترافیک Tunnel Mode از Interface مجازی `ssl.root` وارد می‌شود:

``` text
config firewall policy
 edit 200
  set name "SSLVPN-to-ERP"
  set srcintf "ssl.root"
  set dstintf "port3"
  set srcaddr "all"
  set dstaddr "SRV-ERP"
  set groups "G-VPN-FULL"
  set service "HTTPS"
  set action accept
  set logtraffic all
 next
end
```

Web Mode به Policy مجزا نیاز ندارد؛ دسترسی توسط Bookmarkهای Portal محدود می‌شود، ولی بازرسی و Log هنوز لازم است.

#### ۲-۷) Host Check و امنیت

کنترل وجود آنتی‌ویروس/فایروال در کلاینت (Host Check)، محدودیت مبدأ (`source-address`، Geo)، MFA، Timeout ورود و `login-attempt-limit`.

### ۳) مثال‌های حل‌شده از ساده به سخت

**ساده — انتخاب حالت.** کارمندی فقط به intranet وب نیاز دارد ⇒ Web Mode با Bookmark. مهندس شبکه که با SSH و ابزارهای مدیریتی کار می‌کند ⇒ Tunnel Mode.

**متوسط — محاسبه‌ی Pool.** ۱۵۰ کاربر هم‌زمان ⇒ Pool حداقل ۱۵۰ آدرس + حاشیه ۲۰٪:

``` text
Pool size = 150 x 1.2 = 180  -> use a /24 (254 addresses) e.g. 10.200.0.0/24
```

**متوسط — Split Tunnel.** `INTERNAL-NETS` شامل 10.20.0.0/24 و 10.30.0.0/24. روی کلاینت `route print` نشان می‌دهد این دو شبکه از آداپتور VPN می‌روند و Default Route همچنان محلی است.

**سخت — «Login می‌شود ولی Portal خالی است».**

1. `diagnose firewall auth list` و `get vpn ssl monitor`: کاربر و گروه؟
2. Authentication Rule: گروه به Portal درست نگاشت شده؟ ترتیب Ruleها (اولین مطابقت)؟
3. Portal فعال `web-mode`/`tunnel-mode` درست؟
4. برای Bookmark: Policy/دسترسی از فایروال به مقصد (Web Mode از خود فایروال به سرور وصل می‌شود).

**سخت — Tunnel بالا ولی ping نه.**

1. Policy از `ssl.root` به شبکه‌ی داخلی؟
2. Route برگشت: سرورهای داخلی باید Pool را به فایروال Route کنند.
3. Split Tunnel Address درست؟
4. `diagnose debug application sslvpn -1` (کوتاه).

**سخت — امنیت.** با توجه به سابقه‌ی آسیب‌پذیری‌های SSL-VPN: نسخه‌ی وصله‌شده، MFA، Local-in Policy برای محدودکردن مبدأ، غیرفعال‌سازی Web Mode اگر لازم نیست و پایش Log؛ در محیط جدید IPsec را مقایسه کنید (درس ۲۰-۷).

### ۴) Lab (اجرا نشده)

Portal web-access و tunnel-access؛ دو کاربر؛ مقایسه‌ی تجربه و `get vpn ssl monitor`.

### ۵) اصطلاحات این درس

| اصطلاح | شکل کامل | معنی |
|---|---|---|
| SSL-VPN | Secure Sockets Layer VPN | VPN روی TLS |
| Portal | — | صفحه‌ی ورود/دسترسی |
| Bookmark | — | میانبر منبع در Portal |
| RDP | Remote Desktop Protocol | دسکتاپ راه‌دور |
| PSIRT | Product Security Incident Response Team | تیم امنیتی محصول |

### ۶) تمرین‌ها

**ت1.** (ساده) تفاوت Web Mode و Tunnel Mode؟ *(پاسخ: 20-8-ت1 در بخش «پاسخ‌ها» انتهای فصل)*

**ت2.** (ساده) سه نوع Portal؟ *(پاسخ: 20-8-ت2 در بخش «پاسخ‌ها» انتهای فصل)*

**ت3.** (متوسط) برای ۲۰۰ کاربر هم‌زمان با حاشیه‌ی ۲۰٪ اندازه‌ی Pool؟ *(پاسخ: 20-8-ت3 در بخش «پاسخ‌ها» انتهای فصل)*

**ت4.** (سخت) کاربر Login می‌کند ولی دسترسی ندارد؛ چهار بررسی. *(پاسخ: 20-8-ت4 در بخش «پاسخ‌ها» انتهای فصل)*

### ۷) English Corner

- *In web mode the FortiGate acts as a reverse proxy for the bookmarked resources.*
- *Split tunneling sends only the listed networks through the VPN.*
- **Q1.** Which interface name carries SSL-VPN tunnel traffic in policies? *(پاسخ: 20-8-Q1 در بخش «پاسخ‌ها» انتهای فصل)*

---

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: جدول عیب‌یابی سریع — SSL-VPN

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Portal خالی | Authentication Rule | نگاشت گروه به Portal |
| Tunnel بالا، ping نه | Policy `ssl.root` و Route برگشت | Policy/Route؛ افزودن |
| DNS داخلی حل نمی‌شود | dns-server/Split DNS | تنظیم DNS Portal |
| Web Mode به سرور نمی‌رسد | دسترسی فایروال به مقصد | Policy/Route از فایروال |

## پاسخ‌های فصل 20

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 20-1

**20-1-ت1** — چون سرویسی اینترنتی است که با اعتبارنامه‌ی کاربر باز می‌شود؛ هدف مهاجمان است و در صورت نفوذ مستقیماً به شبکه‌ی داخلی دسترسی می‌دهد.

**20-1-ت2** — دستگاه کلاینت هم‌زمان به اینترنت و شبکه‌ی داخلی وصل است و در صورت آلودگی پل نفوذ می‌شود.

**20-1-ت3** — هم‌زمان ۶۰۰×0.4 = 240؛ Throughput = 240×2 = 480 Mbps؛ با حاشیه ۳۰٪ ≈ 620 Mbps.

**20-1-ت4** — Least Privilege: فقط به سیستم لازم؛ حذف حرکت جانبی؛ Agentless/ZTNA مناسب است.

**20-1-ت5** — MFA، Lockout/Rate limit، Source/Geo Restriction، Alert نسبت ناموفق/موفق، Credential hygiene (رمز نشت‌یافته).

**20-1-ت6** — جدول گروه→روش→کنترل→ظرفیت؛ کارمند IPsec+MFA+Posture؛ پیمانکار Agentless/ZTNA؛ مدیر Bastion+MFA؛ ظرفیت ۶۲۰ Mbps؛ Log و Alert.

**20-1-Q1** — Because stolen or guessed passwords alone would otherwise grant access to the internal network.


### پاسخ‌های بازنویسی عمیق درس 20-2

**20-2-ت1** — Source Interface Policyهای ترافیک کلاینت‌های SSL VPN است.

Source Interface تعیین می‌کند SSL VPN روی کدام Interface گوش دهد (معمولاً WAN).

**20-2-ت2** — CVEهای شناخته‌شده؛ سرویس اینترنتی؛ ریسک نفوذ.

SSL VPN سرویس اینترنتی با CVEهای شناخته‌شده است؛ ریسک نفوذ دارد؛ پچ فوری و محدودکردن.

**20-2-ت3** — Policy ssl.root→LAN، Route/Policy بازگشت، Split networks؛ Debug Flow، `ssl monitor`، Sniffer.

**20-2-ت4** — Brute-force/Credential stuffing؛ با محدودیت تلاش و زمان Block.

Brute-force/Credential stuffing: محدودیت تلاش و Block زمان‌دار و MFA.

**20-2-ت5** — Patch/غیرفعال، محدودسازی Source، بررسی Log retrospective، چرخش اعتبارنامه‌ها، Alert و مهاجرت.

**20-2-ت6** — Source، MFA، Cert، TLS min، Lockout، Timeout، Realm/Portal حداقلی، Patch/Log.

**20-2-Q1** — Because it is an internet-exposed service with known vulnerabilities that can give attackers direct access to the network.


### پاسخ‌های بازنویسی عمیق درس 20-3

**20-3-ت1** — Peer مقابل IP ثابت/شناخته‌شده ندارد و Gateway هر Peer را می‌پذیرد (با Auth).

**20-3-ت2** — IP، DNS و (در صورت تنظیم) Split networks.

Mode Config IP، DNS و (در صورت تنظیم) Split networks را به کلاینت می‌دهد.

**20-3-ت3** — همه یک رمز دارند؛ افشا = دسترسی همه؛ بدون هویت فردی و MFA.

PSK گروهی: همه یک رمز دارند؛ افشا یعنی دسترسی همه، بدون هویت فردی و MFA.

**20-3-ت4** — DNS در Mode Config، Suffix، nslookup با DNS داخلی، Sniffer 53.

DNS در Mode Config، Suffix، `nslookup` با DNS داخلی و Sniffer 53 را بررسی کنید.

**20-3-ت5** — ≈ ۸۰۰ IKE SA + ۸۰۰ Child SA؛ Lifetime را jitter دهید تا Rekey همزمان نشود؛ با Datasheet مدل مقایسه.

**20-3-ت6** — IKEv2+EAP-RADIUS+OTP؛ Finance/IT Policy؛ DNS/Split؛ دو NPS؛ Log و Alert.

طرح: IKEv2+EAP-RADIUS+OTP، Policy Finance/IT، DNS/Split، دو NPS، Log و Alert.

**20-3-Q1** — Because each user is authenticated individually and a leaked shared key would expose all users.


### پاسخ‌های بازنویسی عمیق درس 20-4

**20-4-ت1** — قفل موقت حساب/IP پس از تعداد مشخص تلاش ناموفق.

Lockout قفل موقت حساب/IP پس از تعداد مشخص تلاش ناموفق است.

**20-4-ت2** — نشانه‌ی احتمالی Brute-force موفق؛ مهاجم اکنون دسترسی دارد.

ورود موفق پس از چند شکست یعنی Brute-force احتمالاً موفق شده؛ مهاجم اکنون دسترسی دارد.

**20-4-ت3** — از Baseline رفتار عادی (تعداد ناموفق‌ها به‌ازای کاربر/IP) و ضریب ایمنی؛ آزمون FP.

**20-4-ت4** — آیا از آن IP ورود موفقی بوده؛ کاربران/Sessionها؛ دسترسی‌ها؛ Log حرکت جانبی.

**20-4-ت5** — Triage، Contain، Scope، Eradicate، Recover، PIR با Owner و زمان.

پاسخ: Triage، Contain، Scope، Eradicate، Recover و PIR با Owner و زمان.

**20-4-ت6** — ماهانه کاربران غیرفعال/گروه/Exception؛ فصلی آزمون MFA/Lockout و Patch؛ ثبت.

**20-4-Q1** — Many failed logins followed by a successful login from the same source.


### پاسخ‌های بازنویسی عمیق درس 20-5


### پاسخ‌های بازنویسی عمیق درس 20-5

**20-5-ت1** — رمز لو رفته بدون عامل دوم دسترسی نمی‌دهد.

رمز لورفته بدون عامل دوم (MFA) دسترسی نمی‌دهد.

**20-5-ت2** — فقط ترافیک شبکه‌ی سازمان از Tunnel می‌رود و بقیه مستقیم.

Split Tunnel: فقط ترافیک شبکه‌ی سازمان از Tunnel می‌رود و بقیه مستقیم.

**20-5-ت3** — Policy Lookup، گروه، dstaddr، Route/Tunnel IP.

**20-5-ت4** — عمومی/نامعتبر و هشدار مرورگر و ریسک MITM.

**20-5-ت5** — ترافیک اینترنت بی‌حفاظت؛ EDR/DNS امن/FortiClient.

**20-5-ت6** — دو Policy، دو گروه، مقاصد حداقلی، آزمون منفی متقابل.

**20-5-Q1** — Because stolen passwords alone would not allow access without the second factor.

### پاسخ‌های درس افزوده‌ی 20-7 (فصل 20)

**20-7-ت1** — SSL VPN Tunnel mode حذف شد و با IPsec جایگزین شد.

SSL VPN Tunnel mode حذف شد و با IPsec جایگزین شد (7.6.3).

**20-7-ت2** — نام جدید SSL VPN Web mode (دسترسی مرورگری بدون کلاینت).

نام جدید SSL VPN Web mode: دسترسی مرورگری بدون کلاینت.

**20-7-ت3** — سرویس وب عمومی ندارد؛ سطح حمله‌ی IKE محدودتر است (و CVEهای SSL VPN متعدد بوده).

**20-7-ت4** — ۱) فهرست کاربران؛ ۲) IPsec آزمایشی؛ ۳) Split-tunnel/DNS؛ ۴) MFA؛ ۵) آموزش؛ ۶) Backup؛ ۷) خاموش‌کردن SSL VPN؛ ۸) آزمون منفی. ریسک: قطعی کاربران، ناسازگاری کلاینت.

**20-7-ت5** — کارمندان: IPsec+MFA؛ پیمانکار: Agentless/ZTNA به یک اپ؛ مهمان: بدون VPN.

کارمندان: IPsec+MFA؛ پیمانکار: Agentless/ZTNA به یک اپ؛ مهمان: بدون VPN.

**20-7-Q1** — Because the support status of a feature determines how long the design stays supported and secure.

### پاسخ‌های درس افزوده‌ی 20-8 (فصل 20)

**20-8-ت1** — Web Mode: دسترسی بدون کلاینت از مرورگر با Bookmark (فایروال پروکسی است)؛ Tunnel Mode: FortiClient کارت مجازی و IP می‌سازد و ترافیک شبکه‌ای از تونل می‌رود.

**20-8-ت2** — web-access، tunnel-access، full-access.

**20-8-ت3** — 200 × 1.2 = 240 آدرس؛ یک /24 (254 آدرس) کافی است.

**20-8-ت4** — ۱) گروه/کاربر در `auth list` ۲) Authentication Rule و ترتیب ۳) فعال بودن حالت Portal ۴) Policy/Route برگشت و دسترسی فایروال به مقصد Bookmark.

**20-8-Q1** — `ssl.root`.

---

# فصل 21 — Dual-ISP و SD-WAN (G8)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۱۹.
**اهداف:** دو ISP؛ Failover با Link Monitor؛ SD-WAN Zone/Member/Rule/Health-check؛ Performance SLA؛ معماری ۳. Gate G8: قطع ISP1 بدون قطع جلسه‌ی مهم؛ SD-WAN Rule با Health-check.
**نسخه:** FortiOS 7.0.3؛ SD-WAN داخلی (`Unverified` روی Image). **اشتباهات رایج:** Route با Distance ناهمسان؛ Health-check بدون Server قابل‌اتکا؛ Policy به‌جای Zone.

**درس‌های فصل:**
- [درس 21-1 — Dual-ISP کلاسیک: Static Route و Link Monitor](#l-21-1)
- [درس 21-2 — SD-WAN: Zone، Member و Health-check](#l-21-2)
- [درس 21-3 — SD-WAN Rule و Performance SLA](#l-21-3)
- [درس 21-4 — Failover، Session و معماری ۳](#l-21-4)
- [درس 21-5 — Gate G8 و آزمون فصل](#l-21-5)

---

<a id="l-21-1"></a>

## درس 21-1 — Dual-ISP کلاسیک: Static Route، Distance/Priority، Link Monitor، NAT و تحلیل محدودیت‌ها

**فصل 21 · بازنویسی عمیق · پیش‌نیاز: ۵-۳ (Floating/IP SLA)، ۲۱-۷، ۱۳-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده) و CSR1000v؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Dual-ISP را با دو Default Route، Distance/Priority و Link Monitor پیاده کند.
2. Failover و Failback را اندازه بگیرد و Session/NAT را تحلیل کند.
3. محدودیت‌ها (فقط Up/Down، بدون SLA) را بگوید.
4. Load-balancing ECMP و Policy Route را مقایسه کند.
5. معیار مهاجرت به SD-WAN را بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا فقط «دو Route» کافی نیست؟** فرض کنید دو راه برای رفتن به محل کار دارید: بزرگراه و جاده‌ی فرعی. می‌گویید «همیشه بزرگراه، فقط اگر بسته بود جاده‌ی فرعی». ولی اگر فقط «تابلوی ورودی بزرگراه» را نگاه کنید و ندانید چند کیلومتر جلوتر تصادف شده، پشت ترافیک می‌مانید. Static Route دوم دقیقاً همین است: تا وقتی **لینک** بالاست، فایروال Route اول را معتبر می‌داند، حتی اگر ISP در بالادست قطع باشد. راه‌حل این است که فایروال مدام از «مقصدی دور» (مثلاً 8.8.8.8) سراغ بگیرد: Link Monitor.

**گام‌به‌گام: Dual-ISP کلاسیک چگونه کار می‌کند؟**

1. دو Default Route: ISP1 با Distance 10 و ISP2 با Distance 20. **Distance کمتر = اعتبار بیشتر**؛ فقط Route با Distance کمتر در جدول فعال است.
2. **Link Monitor** برای ISP1: هر `interval` میلی‌ثانیه یک پروب به هدف خارجی می‌فرستد. اگر `failtime` پروب پشت سر هم بی‌پاسخ ماند، Route وابسته غیرفعال می‌شود.
3. با غیرفعال‌شدن Route اول، Route دوم (Distance 20) در جدول می‌نشیند و ترافیک جدید از ISP2 می‌رود.
4. وقتی ISP1 برگشت و `recoverytime` پروب موفق شد، Route اول دوباره فعال می‌شود (Failback).

**چه چیزی هنوز می‌تواند اشتباه شود؟**

- **NAT:** هر خروجی باید با IP همان ISP ترجمه شود (Policy جدا یا NAT روی Interface خروجی).
- **Session قدیمی:** اتصال‌های موجود روی لینک قبلی می‌مانند تا Timeout شوند؛ کاربران می‌گویند «اینترنت قطع است» در حالی که اتصال جدید کار می‌کند.
- **IP عمومی عوض می‌شود:** سرویس‌های وابسته به IP (SSH، VoIP، بانک) قطع می‌شوند.

**فرق Distance و Priority:** Distance Route را انتخاب می‌کند؛ Priority فقط وقتی دو Route هم‌Distance‌اند بین آنها تصمیم می‌گیرد (مثل ECMP با اولویت).

**جمع‌بندی اصلی درس:**

قبل از SD-WAN، روش ساده‌ی Dual-ISP مفید است؛ ولی نمی‌بیند «کیفیت» لینک چطور است. باید بدانید دقیقاً چه می‌کند و کجا کم می‌آورد.

### ۳) توضیح عمیق فنی

#### ۱) Distance و Priority

- Distance کمتر ⇒ Route ترجیحی در RIB.
- Priority (در FortiOS) بین Routeهای هم‌Distance برای ECMP/ترجیح کنترل‌شده (`Unverified` در جزئیات).
- هر دو Route با Distance برابر ⇒ ECMP (توزیع Flow).

``` text
Default via wan1  distance 10   (primary)
Default via wan2  distance 20   (backup) -> inactive in RIB until primary route is removed
```

#### ۲) Link Monitor

Probe (ping/TCP/HTTP) به Server؛ شکست متوالی ⇒ Route آن Interface از RIB حذف ⇒ Backup فعال. پارامترها: `interval`, `failtime`, `recoverytime`, `server`.

#### ۳) NAT

هر WAN SNAT جدا؛ Session روی WAN قبلی با Failover قفل می‌شود (۱۳-۷)؛ سرویس با IP ثابت مشکل دارد.

#### ۴) محدودیت‌ها

- Up/Down؛ کیفیت (Latency/Loss/Jitter) دیده نمی‌شود.
- Failback بدون SLA/Hold-down.
- یک Probe Server = SPOF.
- ECMP Hash نامتقارن و Stateful (۲۳-۱).

#### ۵) معیار مهاجرت به SD-WAN

نیاز به SLA/برنامه‌محور، چند لینک، Overlay، گزارش کیفیت.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Monitor | چند Server/Protocol |
| NAT | Pool هر WAN |
| Failback | Hold-down |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — محاسبه‌ی زمان تشخیص

``` text
Detection time = interval x failtime
interval = 1000 ms, failtime = 5  ->  1 s x 5 = 5 s
```

مراحل: ۱) هر ۱ ثانیه یک پروب ۲) پس از ۵ پروب بی‌پاسخ، Route غیرفعال ⇒ تقریباً ۵ ثانیه تا شروع Failover. اگر هدف «زیر ۳ ثانیه» باشد: `interval 500` و `failtime 5` ⇒ 2.5 s (با هزینه‌ی ترافیک پروب بیشتر).

#### مثال ساده — پیکربندی

``` text
config router static
 edit 1
  set gateway 203.0.113.1
  set device "port1"
  set distance 10
 next
 edit 2
  set gateway 198.51.100.1
  set device "port2"
  set distance 20
 next
end
config system link-monitor
 edit "ISP1"
  set srcintf "port1"
  set server "8.8.8.8"
  set gateway-ip 203.0.113.1
  set interval 1000
  set failtime 5
  set recoverytime 5
 next
end
```

#### مثال متوسط — Failover را اندازه می‌گیریم

``` text
ping -i 0.2 8.8.8.8      # run from a user PC
# disconnect ISP1 upstream at t=0
lost 38 packets x 0.2 s = 7.6 s outage
```

۷٫۶ ثانیه = ۵ ثانیه تشخیص + همگرایی Route و Session جدید. اگر هدف شما ۵ ثانیه است، مقدار را از همین آزمون واقعی می‌بینید، نه حدس.

#### مثال متوسط — Session قدیمی

کاربر SSH به سرور بیرونی داشت. پس از Failover، SSH قطع می‌شود چون IP مبدأ عوض شد (NAT به IP ISP2). این رفتار طبیعی است؛ «IP ثابت» فقط با BGP به دو ISP یا Cloud Anchor ممکن است. برای وب (اتصال جدید) تجربه‌ی کاربر قطع نمی‌شود.

``` text
diagnose sys session filter src 10.10.0.5
diagnose sys session list
diagnose sys session clear
diagnose sys session filter clear
```

#### مثال سخت — Failback ناپایدار

لینک ISP1 هر چند دقیقه یک‌بار ۱۰ ثانیه می‌افتد. با `recoverytime 5` هر بار پس از ۵ ثانیه برگشت، Route دوباره به ISP1 می‌رود و بلافاصله می‌افتد؛ کاربران قطع‌وصل می‌بینند. راه‌حل‌ها: افزایش `recoverytime` (مثلاً 60)، Failback دستی در پنجره‌ی تغییر، یا Route با Priority طوری که Failback نکند. شاهد: Log Link Monitor (`status changed`) و شمارش تغییرات در ساعت.

#### مثال سخت — لینک بالا، ISP بالادست قطع

`get system interface physical` Link Up نشان می‌دهد. بدون Link Monitor Route فعال می‌ماند. با Monitor: `diagnose sys link-monitor status` `dead`. این دقیقاً تفاوت «لینک Up» و «مسیر سالم» است.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** قطع wan1 در Lab؛ پس از ≈ failtime×interval Route wan2؛ ping ادامه.

**متوسط (تحلیل):** ISP قطع ولی Interface Up: بدون Link Monitor Route می‌ماند؛ با Monitor حذف. شاهد: `get router info routing-table all`.

**سخت (طراحی):** ISP با Loss 30٪ ولی Probe Ping با Server نزدیک موفق: Link Monitor نمی‌بیند. راه: Probe چندگانه/HTTP، آستانه‌ی Loss (SD-WAN SLA)، یا Server دورتر؛ تصمیم مهاجرت به SD-WAN.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Static Routes.
2. System → Link Monitor.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config router static
    edit 1
        set gateway 198.51.100.1
        set device "wan1"
        set distance 10
    next
    edit 2
        set gateway 203.0.113.1
        set device "wan2"
        set distance 20
    next
end
config system link-monitor
    edit "LM-WAN1"
        set srcintf "wan1"
        set server "8.8.8.8" "1.1.1.1"
        set protocol ping
        set interval 1000
        set failtime 5
        set recoverytime 10
    next
end
```

### ۸) Verification (اثبات صحت)

- قطع wan1 و اندازه‌گیری.
- routing-table قبل/بعد.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Failover نشد | Routing table | Monitor/Distance |
| Session قفل | session list | Clear |
| Flap | Log | recoverytime |

### ۱۰) نکات امنیتی

- Policy یکسان روی هر دو.

### ۱۱) جمع‌بندی مفهومی

- Distance/Priority + Monitor.
- Up/Down فقط.
- Session/NAT.
- مهاجرت به SD-WAN برای SLA.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Distance کمتر یعنی؟ *(پاسخ: 21-1-ت1)*

**ت2.** (ساده) Link Monitor چه می‌کند؟ *(پاسخ: 21-1-ت2)*

**ت3.** (متوسط) چرا Probe با چند Server؟ *(پاسخ: 21-1-ت3)*

**ت4.** (متوسط) Failover زمانی با interval 1 s و failtime 5؟ *(پاسخ: 21-1-ت4)*

**ت5.** (سخت) Loss 30٪ را روش کلاسیک می‌بیند؟ *(پاسخ: 21-1-ت5)*

**ت6.** (سخت، طراحی) معیار مهاجرت به SD-WAN. *(پاسخ: 21-1-ت6)*

**Q1.** Quick quiz (English): What kind of failure can a plain link monitor not detect? *(پاسخ: 21-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ECMP | Equal-Cost Multi-Path | چند مسیر هم‌هزینه |

- *Use multiple probe servers.* ← از چند Server برای Probe استفاده کنید.

### ۱۴) کارت Lab

**کارت Lab:** Dual-ISP. **Evidence:** `03-ops/dual-isp.md`.

### ۱۵) منابع

- Fortinet Docs: Link health monitor، Static routes

<a id="l-21-2"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Dual-ISP کلاسیک با عدد

``` text
config router static
 edit 1
  set gateway 203.0.113.1
  set device port1
  set distance 10
 next
 edit 2
  set gateway 198.51.100.1
  set device port2
  set distance 20
 next
end
config system link-monitor
 edit "ISP1"
  set srcintf port1
  set server 8.8.8.8
  set interval 1000
  set failtime 5
  set recoverytime 5
 next
end
```

زمان تشخیص ≈ interval × failtime = 1 s × 5 = 5 s. با قطع، Route Distance 10 غیرفعال و Distance 20 فعال می‌شود. NAT برای هر خروجی جدا (Policy برای هر Interface).

**پرسش‌های مصاحبه**
1. *Distance در برابر Priority؟* Distance انتخاب Route؛ Priority تساوی را می‌شکند.
2. *Session قدیم؟* روی ISP قبل می‌ماند.
3. *چرا Monitor؟* قطع بالادستی بدون Down شدن لینک.

### تکمیل عمیق: Dual-ISP کلاسیک — چرا فقط «دو Route» کافی نیست؟

#### چرا باید یاد بگیریم؟

بسیاری از سازمان‌ها دو ISP می‌گیرند و فکر می‌کنند «اگر یکی قطع شد، دیگری خودکار کار می‌کند». ولی قطع واقعی اغلب این‌گونه نیست: کابل سالم است و لینک Up است، اما ISP در بالادست مشکل دارد. فایروال هنوز Route اول را فعال می‌بیند و ترافیک را به چاه می‌فرستد. برای تشخیص چنین قطعی به **Link Monitor** (پایش سلامت مسیر) نیاز داریم.

#### توضیح ساده

دو Static Route پیش‌فرض داریم؛ یکی با Distance کمتر (ترجیح بیشتر) و دیگری با Distance بیشتر (پشتیبان). فقط Route با Distance کمتر در جدول فعال است. Link Monitor مرتب یک هدف خارجی (مثلاً 8.8.8.8) را از آن لینک پینگ می‌کند؛ اگر چند بار پاسخ نیامد، Route آن لینک را غیرفعال می‌کند تا Route دوم فعال شود.

``` text
Route 1: 0.0.0.0/0 via 203.0.113.1 dev port1 distance 10
Route 2: 0.0.0.0/0 via 198.51.100.1 dev port2 distance 20
```

#### مثال ساده — تنظیم و محاسبه‌ی زمان تشخیص

``` text
config system link-monitor
 edit "ISP1"
  set srcintf "port1"
  set server "8.8.8.8"
  set gateway-ip 203.0.113.1
  set interval 1000
  set failtime 5
  set recoverytime 5
 next
end
```

``` text
Detection time = interval x failtime = 1 s x 5 = 5 s
```

یعنی ≈ ۵ ثانیه پس از قطع، Failover آغاز می‌شود. مقادیر پیش‌فرض را از مستند نسخه تأیید کنید.

#### مثال متوسط — NAT برای هر خروجی

باید برای هر ISP یک Policy جدا (یا Policy با NAT خودکار روی Interface خروجی) وجود داشته باشد تا ترافیک با IP همان ISP خارج شود.

#### مثال سخت — Session قدیمی

پس از Failover، Sessionهای موجود روی لینک قدیم می‌مانند تا Timeout شوند؛ کاربران «اینترنت قطع است» می‌گویند، در حالی که اتصال جدید کار می‌کند. راه: `set snat-route-change enable` (برای SNAT)، یا پاک‌سازی Sessionهای مربوط با فیلتر.

``` text
diagnose sys session filter dst 8.8.8.8
diagnose sys session clear
```

هشدار: Clear بدون فیلتر همه‌ی Sessionها را می‌بندد.

#### Lab

دو Interface WAN با دو Route و Link Monitor بسازید؛ Gateway اول را قطع کنید و زمان Failover را بشمارید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Failover نمی‌شود | Monitor ندارد | افزودن |
| پس از Failover هنوز قطع | Session قدیمی | Clear/snat-route-change |
| Failback ناپایدار | recoverytime کم | افزایش |

#### پرسش‌ها با پاسخ

**۱. Distance در برابر Priority؟** Distance انتخاب Route؛ Priority تساوی را می‌شکند.
**۲. چرا Monitor؟** قطع بالادست.
**۳. زمان تشخیص؟** interval × failtime.

#### English Corner

- *Link state alone does not prove that the upstream path works.*
- Q: How do you calculate the failure detection time?

## درس 21-2 — ساخت SD-WAN عملی: Zone، Member، Health-check، Route و Policy

**فصل ۲۱ · بازنویسی عمیق · پیش‌نیاز: ۲۱-۷ (مفاهیم)، ۲۱-۱، ۱۲-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** سینتکس 7.0 (`mode load-balance` برای Maximize Bandwidth)؛ `Unverified` روی Image؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

SD-WAN را از صفر بسازد: انتقال Interface از Policy/Route قدیمی به Zone، تعریف Member، Health-check، Default Route، Policy روی Zone؛ و مهاجرت **بدون قطع** را برنامه‌ریزی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا SD-WAN؟** Dual-ISP فقط می‌فهمد «بالا یا پایین». ولی اغلب مشکل واقعی «بالا ولی بد» است: لینک ISP1 بالاست اما ۸٪ بسته گم می‌شود و تماس تلفنی بریده می‌شود. SD-WAN مثل یک **راهنمای رانندگی هوشمند** است که ترافیک زنده را اندازه می‌گیرد و اگر جاده‌ی اصلی کند بود، تماس تلفنی (حساس) را به جاده‌ی بهتر می‌فرستد و دانلود (غیرحساس) را همان‌جا می‌گذارد.

**اجزای SD-WAN و نقش هرکدام**

| جزء | کار | مثال |
|---|---|---|
| Member | Interface و Gateway هر لینک | port1 → ISP1 |
| Zone | گروه Memberها (یک «لینک منطقی») | `virtual-wan-link` |
| Health-check | اندازه‌گیری تأخیر، Jitter، Loss | ping به 8.8.8.8 |
| Rule (Service) | کدام ترافیک روی کدام Member | Voice روی کم‌تأخیر |
| Route | Default Route به Zone | `0.0.0.0/0 → zone` |
| Policy | از LAN به **Zone** | نه Interface تکی |

**نکته‌ی مهم:** Interfaceهایی که عضو SD-WAN شده‌اند را نمی‌توان مستقیم در Policy استفاده کرد؛ Policyها باید به Zone اشاره کنند. بنابراین مهاجرت از Dual-ISP قدیمی به SD-WAN یعنی «بازنویسی Policyها» و باید با Backup و Lookup انجام شود.

**مراحل ساخت:** ۱) Memberها ۲) Health-check ۳) Rule (در درس بعد) ۴) Route Default به Zone ۵) Policy به Zone ۶) آزمون و Failover.

**جمع‌بندی اصلی درس:**

Interface که عضو SD-WAN می‌شود **نباید در Policy/Route/Object دیگری** مرجع باشد؛ پس: (۱) Policyهای قدیمی که به wan1/wan2 اشاره دارند، (۲) Static Routeهای wan1/wan2، (۳) VIP/DHCP روی این Interfaceها را فهرست و به Zone منتقل کنید. Backup بگیرید.

### ۳) مراحل

1. Backup پیکربندی.
2. Network → SD-WAN → Create New Member: wan1 (Gateway)، wan2.
3. Zone: virtual-wan-link.
4. Performance SLA: HC-DNS (ping 8.8.8.8 و ۱.۱.۱.۱)، interval/failtime/recoverytime.
5. Static Route: 0.0.0.0/0 → Interface SD-WAN Zone.
6. Firewall Policy: LAN → SD-WAN Zone (NAT enable).
7. SD-WAN Rule (در ۲۱-۳).

``` text
config system sdwan
    set status enable
    config zone
        edit "virtual-wan-link"
        next
    end
    config members
        edit 1
            set interface "wan1"
            set gateway 198.51.100.1
        next
        edit 2
            set interface "wan2"
            set gateway 203.0.113.1
        next
    end
    config health-check
        edit "HC-DNS"
            set server "8.8.8.8" "1.1.1.1"
            set protocol ping
            set interval 1000
            set failtime 5
            set recoverytime 10
            set members 1 2
        next
    end
end
config router static
    edit 1
        set sdwan-zone "virtual-wan-link"
    next
end
config firewall policy
    edit 10
        set srcintf "port2"
        set dstintf "virtual-wan-link"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
    next
end
```

(نام فیلد `sdwan-zone` و ساختار `server` چندگانه با CLI Reference 7.0 تطبیق شود؛ `Unverified`.)

### ۴) Verification

``` text
diagnose sys sdwan health-check
diagnose sys sdwan member
get router info routing-table all
diagnose sys session filter dst 8.8.8.8
diagnose sys session list
```

GUI: Network → SD-WAN → Performance SLAs (نمودار Latency/Jitter/Loss).

### ۵) مثال‌ها

#### مثال ساده — ساخت Zone و Member

``` text
config system sdwan
 set status enable
 config zone
  edit "virtual-wan-link"
  next
 end
 config members
  edit 1
   set interface "port1"
   set gateway 203.0.113.1
   set zone "virtual-wan-link"
  next
  edit 2
   set interface "port2"
   set gateway 198.51.100.1
   set zone "virtual-wan-link"
  next
 end
 config health-check
  edit "HC1"
   set server "8.8.8.8"
   set members 1 2
  next
 end
end
```

بررسی: `diagnose sys sdwan member` و `diagnose sys sdwan health-check` باید هر دو Member را `alive` نشان دهد.

#### مثال متوسط — Route و Policy

``` text
config router static
 edit 1
  set sdwan-zone "virtual-wan-link"
 next
end
config firewall policy
 edit 10
  set srcintf "port3"
  set dstintf "virtual-wan-link"
  set srcaddr "all"
  set dstaddr "all"
  set service "ALL"
  set action accept
  set nat enable
 next
end
```

اگر Policy قدیمی `port3 → port1` هنوز هست و Interface عضو SD-WAN شده، GUI اجازه‌ی ویرایش نمی‌دهد؛ باید Policy را به Zone منتقل یا حذف کنید.

#### مثال متوسط — مهاجرت بدون قطع

``` text
1 Backup config + hash
2 Create SDWAN zone/members/health-check (no traffic yet)
3 Create new policies to the zone (placed after old ones)
4 Lookup: diagnose firewall iprope lookup 10.10.0.5 40000 8.8.8.8 53 udp port3
5 Remove old static routes, then old policies
6 Test failover; keep rollback (restore config) ready < 10 min
```

#### مثال سخت — Member همیشه dead

`diagnose sys sdwan health-check` ⇒ `state(dead)`. بررسی:

1. سرور Health-check از آن Interface قابل‌دسترس است؟ (`execute ping-options source` و ping)
2. Gateway درست؟
3. Policy/Local-out اجازه می‌دهد پروب خارج شود؟
4. ISP ICMP را بسته؟ ⇒ پروب HTTP/DNS.
5. پس از رفع: `alive` و `sla_map` درست.

#### مثال‌های اصلی درس (مرور)

**ساده:** هر دو Member Alive؛ ترافیک بین هر دو بر اساس Hash (Implicit rule).

**متوسط:** قطع wan1 (Shutdown در Lab): Health-check پس از ≈ 5 ثانیه Dead؛ ترافیک جدید از wan2؛ Session قدیمی روی wan1 تا Clear می‌ماند (۱۳-۷).

**سخت:** Member همیشه Dead با اینکه اینترنت کار می‌کند: Policy Local-out Probe یا Route Probe؛ Server روی مسیر اشتباه؛ `execute ping-options source` با IP همان WAN؛ شواهد: Sniffer روی wan1: ICMP خارج می‌شود ولی پاسخ نمی‌آید (ISP Block ICMP) → از `protocol dns/http` استفاده کنید.

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| Interface قابل افزودن نیست | هنوز در Policy/Route مرجع دارد |
| ترافیک از Zone نمی‌رود | Default Route روی Zone نیست |
| Member Dead | Probe/Server/Policy |
| Failover بدون اثر | Session قدیمی |

### ۷) نکات امنیتی

- Probe روی Local-out؛ Server مورد اعتماد.
- Policy روی Zone؛ همه‌ی مسیرها Inspect شوند.

### ۸) جمع‌بندی

- پیش‌نیاز: خالی‌کردن مرجع‌های Interface.
- Zone/Member/HC/Route/Policy.
- Verification: HC، Member، Routing، Session.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) چرا Interface قبل از افزودن به SD-WAN باید از Policyها آزاد شود؟ *(پاسخ: 21-2-ت1)*

**ت2.** (متوسط) Default Route در SD-WAN روی چه Interface است؟ *(پاسخ: 21-2-ت2)*

**ت3.** (سخت) Member Dead با اینترنت سالم؛ تحلیل. *(پاسخ: 21-2-ت3)*

**ت4.** (سخت، طراحی) برنامه‌ی مهاجرت بدون قطع از Dual-ISP کلاسیک به SD-WAN. *(پاسخ: 21-2-ت4)*

**Q1.** Quick quiz (English): Where is the default route attached in an SD-WAN design? *(پاسخ: 21-2-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Member | SD-WAN member | عضو Zone |
| Zone | SD-WAN zone | گروه منطقی لینک‌ها |
| Probe | Health-check probe | بسته‌ی سنجش کیفیت |

- *Remove interface references before adding it to SD-WAN.* ← قبل از افزودن Interface به SD-WAN مرجع‌های آن را بردارید.

### ۱۱) Lab

**کارت Lab:** SD-WAN. **وضعیت:** اجرا نشده. **Rollback:** بازگشت Config. **Evidence:** `03-ops/sdwan.md`.

### ۱۲) منابع

- Fortinet Docs: [SD-WAN](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/19246/sd-wan)، [config system sdwan](https://docs.fortinet.com/document/fortigate/7.0.1/cli-reference/94620/config-system-sdwan).

<a id="l-21-3"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: ساخت SD-WAN

``` text
config system sdwan
 set status enable
 config zone
  edit "virtual-wan-link"
  next
 end
 config members
  edit 1
   set interface port1
   set gateway 203.0.113.1
  next
  edit 2
   set interface port2
   set gateway 198.51.100.1
  next
 end
 config health-check
  edit "HC1"
   set server "8.8.8.8"
   set members 1 2
  next
 end
end
```

پس از ایجاد، Policyهای قبلی که به Interface مستقیم اشاره می‌کنند باید به Zone SD-WAN منتقل شوند؛ Static Route به `virtual-wan-link`.

**پرسش‌های مصاحبه**
1. *Member؟* Interface عضو.
2. *Health-check؟* پایش کیفیت.
3. *Route؟* Default روی Zone.

### تکمیل عمیق: ساخت SD-WAN گام‌به‌گام

#### چرا؟

Dual-ISP کلاسیک فقط «بالا/پایین» را می‌فهمد. SD-WAN کیفیت (تأخیر، Jitter، Loss) را اندازه می‌گیرد و بر اساس برنامه مسیر انتخاب می‌کند: Voice روی لینک کم‌تأخیر، دانلود روی لینک ارزان.

#### اجزا

1. **Zone**: گروه Memberها (مثلاً `virtual-wan-link`).
2. **Member**: Interface + Gateway.
3. **Health-check**: پایش کیفیت.
4. **Rule (Service)**: انتخاب مسیر.
5. **Route**: Default Route به Zone.
6. **Policy**: به Zone (نه Interface تکی).

#### مثال ساده — ساخت

``` text
config system sdwan
 set status enable
 config members
  edit 1
   set interface "port1"
   set gateway 203.0.113.1
  next
  edit 2
   set interface "port2"
   set gateway 198.51.100.1
  next
 end
 config health-check
  edit "HC1"
   set server "8.8.8.8"
   set members 1 2
  next
 end
end
```

#### مثال متوسط — Route و Policy

Static Route 0.0.0.0/0 با `sdwan-zone virtual-wan-link`؛ Policy `LAN -> virtual-wan-link`. Policyهای قبلی که به port1/port2 اشاره می‌کنند باید به Zone منتقل شوند؛ Interface عضو SD-WAN را نمی‌توان مستقیم در Policy استفاده کرد.

#### مثال سخت — مهاجرت بدون قطع

مراحل: ۱) Backup ۲) ساخت SD-WAN ۳) انتقال Policyها با آزمون Lookup ۴) حذف Routeهای قدیمی ۵) آزمون Failover ۶) Rollback آماده. در Maintenance Window با Rollback کمتر از ۱۰ دقیقه.

#### Lab

SD-WAN را با دو Member بسازید و `diagnose sys sdwan health-check` را بخوانید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Policy ساخته نمی‌شود | Interface عضو | Zone |
| Member همیشه dead | Server/Gateway | بررسی |
| ترافیک از یک لینک | Rule | بررسی |

#### پرسش‌ها با پاسخ

**۱. Member چیست؟** Interface عضو.
**۲. Zone چرا؟** Policy یکپارچه.
**۳. Health-check؟** پایش کیفیت.

#### English Corner

- *Policies reference the SD-WAN zone, not individual member interfaces.*
- Q: What does a health check measure?

## درس 21-3 — SD-WAN Rule و Performance SLA: انتخاب مسیر بر اساس برنامه و کیفیت

**فصل ۲۱ · بازنویسی عمیق · پیش‌نیاز: ۲۱-۲، ۲۱-۷ · ≈ ۶ ساعت**

> **وضعیت (7.0.3):** `mode sla`/`load-balance`/`manual` مطابق مستند 7.0؛ سینتکس `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. برای هر نوع ترافیک (VoIP، ERP، Backup) استراتژی و SLA مناسب انتخاب کند.
2. Rule ایجاد و **ترتیب Ruleها** (First Match) را درست بچیند.
3. رفتار Rule در Failover/Failback را پیش‌بینی و آزمایش کند.
4. با Log/`diagnose` اثبات کند ترافیک از کدام Member رفت.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا SD-WAN Rule و SLA؟** همه‌ی ترافیک ارزش یکسان ندارد. تماس صوتی با تأخیر 150 ms و Jitter 40 ms «بریده بریده» می‌شود، ولی دانلود فایل به همان شرایط حساس نیست. Rule مشخص می‌کند «کدام ترافیک» روی «کدام لینک» برود؛ SLA «لینک خوب» را با عدد تعریف می‌کند.

**SLA به زبان ساده:** سه آستانه: تأخیر (Latency)، نوسان تأخیر (Jitter) و از دست‌رفتن بسته (Packet Loss). مثال: لینک «مناسب صوت» یعنی تأخیر ≤ 100 ms، Jitter ≤ 30 ms، Loss ≤ 2٪. اگر عددی از آستانه بگذرد، SLA «نقض» می‌شود و Rule لینک دیگری را برمی‌گزیند.

**استراتژی‌های Rule (Mode)**

| Mode | معنی |
|---|---|
| manual | ترتیب دستی Memberها |
| best-quality | بهترین کیفیت طبق معیار |
| lowest-cost (sla) | ارزان‌ترین لینکی که SLA را رعایت کند |
| load-balance | توزیع بار |

**Brownout:** لینک «بالا» ولی «بد». Health-check ساده می‌گوید `alive`؛ SLA می‌گوید «نقض شده». این همان مزیت اصلی SD-WAN است.

اگر هیچ Rule مطابق نبود، **Implicit Rule** (بر اساس Route/Cost) اعمال می‌شود.

**جمع‌بندی اصلی درس:**

- Rule شامل **Match** (Source، Destination، Service، Application/Internet Service) و **Strategy** (`mode`) و **priority-members** است.
- ارزیابی **بالا به پایین**؛ اولین Rule مطابق برنده؛ اگر هیچ Rule مطابق نشد → Implicit Rule (Load-balance پیش‌فرض).
- `mode sla`: اولین Member (به ترتیب priority-members) که SLA Health-check را برآورده کند.
- `mode load-balance`: همه‌ی Memberهای دارای SLA، با Hash.
- `mode manual`: Member ثابت.

``` text
Rule order example
1 VOIP  (UDP 5060, RTP)         mode sla         members 1 2   sla HC-DNS latency<80 jitter<20
2 ERP   (dst 10.50.0.0/16)      mode sla         members 2 1
3 BACKUP(service FTP,SFTP)      mode load-balance members 1 2
4 default                       implicit
```

### ۳) پیاده‌سازی

**GUI:** Network → SD-WAN → SD-WAN Rules → Create New: Name، Source/Destination، Internet Service/Application، Strategy (Lowest Cost (SLA)/Best Quality/Maximize Bandwidth/Manual)، Interface preference، Required SLA target.

**CLI (`Unverified`):**

``` text
config system sdwan
    config health-check
        edit "HC-VOIP"
            set server "8.8.8.8"
            set protocol ping
            set interval 500
            set failtime 3
            set recoverytime 20
            set members 1 2
            config sla
                edit 1
                    set latency-threshold 80
                    set jitter-threshold 20
                    set packetloss-threshold 1
                next
            end
        next
    end
    config service
        edit 1
            set name "VOIP"
            set mode sla
            set dst "all"
            set protocol 17
            set start-port 5060
            set end-port 5060
            config sla
                edit "HC-VOIP"
                    set id 1
                next
            end
            set priority-members 1 2
        next
        edit 3
            set name "BACKUP"
            set mode load-balance
            set dst "all"
            set priority-members 1 2
        next
    end
end
```

### ۴) مثال‌ها

**ساده:** VoIP روی wan1 (Latency 30 ms)؛ wan2 رزرو.

**متوسط:** Latency wan1 به 150 ms می‌رسد؛ SLA نقض؛ VoIP به wan2؛ پس از بازگشت Latency (recoverytime ۲۰×۵۰۰ms=۱۰s) به wan1 برمی‌گردد؛ ثبت Log SLA.

**سخت:** Rule اول «all» گذاشته‌اید؛ Ruleهای VOIP/ERP هرگز Match نمی‌شوند. شاهد: `diagnose sys sdwan service`: Hit فقط Rule 1. **رفع:** ترتیب (مشخص‌ترها بالا).

### ۵) Troubleshooting

#### مثال ساده — تعریف SLA

``` text
config system sdwan
 config health-check
  edit "HC1"
   set server "8.8.8.8"
   set members 1 2
   config sla
    edit 1
     set latency-threshold 100
     set jitter-threshold 30
     set packetloss-threshold 2
    next
   end
  next
 end
end
```

#### مثال ساده — Rule برای Voice

``` text
config system sdwan
 config service
  edit 1
   set name "VOICE"
   set mode sla
   set dst "SIP-PEERS"
   config sla
    edit "HC1"
     set id 1
    next
   end
   set priority-members 1 2
  next
 end
end
```

منطق: Voice روی عضو 1 تا وقتی SLA 1 رعایت شود؛ در نقض، عضو 2.

#### مثال متوسط — خواندن خروجی

``` text
diagnose sys sdwan health-check
Seq(1 port1): state(alive), packet-loss(0.000%) latency(12.3) jitter(0.8) sla_map=0x1
Seq(2 port2): state(alive), packet-loss(8.000%) latency(45.0) jitter(5.1) sla_map=0x0
```

عضو 1: SLA رعایت (`sla_map=0x1`). عضو 2: Loss 8٪ ⇒ SLA نقض (`0x0`). Voice روی عضو 1 می‌ماند؛ حتی اگر عضو 2 `alive` است.

#### مثال متوسط — تزریق Loss در Lab

``` text
tc qdisc add dev eth1 root netem delay 150ms loss 5%
```

اثر: Latency و Loss بالا ⇒ SLA نقض ⇒ Rule Voice عضو دیگر. پاک‌سازی: `tc qdisc del dev eth1 root`.

#### مثال سخت — Flap نزدیک آستانه

تأخیر لینک بین 95 و 105 ms نوسان می‌کند؛ Voice مدام جابه‌جا می‌شود. راه: آستانه‌ی حاشیه‌دار (مثلاً 120 ms)، `recoverytime` بیشتر یا Hysteresis؛ و ثبت دلیل. شاهد: Log تغییر Member.

#### مثال سخت — Rule اعمال نمی‌شود

`diagnose sys sdwan service`. بررسی: `dst` (Address Object) درست؟ ترتیب Ruleها (اولین مطابقت)؟ Rule بدون Service/Dst همه‌چیز را می‌گیرد؟ در نبود تطبیق، Implicit Rule.

#### مثال‌های اصلی درس (مرور)

| علامت | علت |
|---|---|
| Rule Hit ندارد | ترتیب/Match |
| VoIP قطع‌ووصل | آستانه‌ی بدون Hysteresis، recoverytime کم |
| Backup همه‌ی پهنا را می‌خورد | load-balance بدون Shaping |
| Session بعد از Failover قفل | Session قدیمی (۱۳-۷) |

### ۶) نکات امنیتی

- هر مسیر پشتیبان باید Policy/UTM یکسان داشته باشد.
- Internet Service/Application نیاز FortiGuard (Needs-License).

### ۷) جمع‌بندی

- First Match؛ مشخص‌ها بالا.
- SLA برای Real-time؛ load-balance برای حجم.
- اثبات با `diagnose sys sdwan service` و Log.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) ترتیب ارزیابی Ruleها؟ *(پاسخ: 21-3-ت1)*

**ت2.** (متوسط) فرق `mode sla` و `load-balance`؟ *(پاسخ: 21-3-ت2)*

**ت3.** (سخت) چرا Rule VoIP هیچ Hit ندارد؟ *(پاسخ: 21-3-ت3)*

**ت4.** (سخت، طراحی) سه Rule برای VoIP/ERP/Backup با SLA بنویسید. *(پاسخ: 21-3-ت4)*

**Q1.** Quick quiz (English): What happens when no SD-WAN rule matches? *(پاسخ: 21-3-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Rule/Service | SD-WAN rule (service) | قانون انتخاب مسیر |
| Implicit rule | Implicit SD-WAN rule | قانون پیش‌فرض |
| Hysteresis | Hysteresis | تأخیر برای جلوگیری از نوسان |

- *Put the most specific rules first.* ← مشخص‌ترین Ruleها را اول بگذارید.

### ۱۰) Lab

**کارت Lab:** SD-WAN Rule. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/sdwan-rule.md`.

### ۱۱) منابع

- Fortinet Docs: [Maximize bandwidth (SLA) strategy](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/708464/maximize-bandwidth-sla-strategy)، [config system sdwan](https://docs.fortinet.com/document/fortigate/7.0.1/cli-reference/94620/config-system-sdwan).

<a id="l-21-4"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Rule و SLA

``` text
config health-check
 edit "HC1"
  config sla
   edit 1
    set latency-threshold 100
    set jitter-threshold 30
    set packetloss-threshold 2
   next
  end
 next
end
config service
 edit 1
  set name "VOICE"
  set mode sla
  set dst "SIP-PEERS"
  config sla
   edit "HC1"
    set id 1
   next
  end
  set priority-members 1 2
 next
end
```

منطق: Voice روی عضو ۱ تا زمانی که SLA شکسته نشود؛ بعد عضو ۲.

**پرسش‌های مصاحبه**
1. *Strategy‌ها؟* manual، best-quality، lowest-cost، sla.
2. *Failback؟* طبق recoverytime.
3. *Rule بدون Match؟* Implicit Rule.

### تکمیل عمیق: Rule و SLA — انتخاب مسیر بر اساس کیفیت

#### چرا؟

همه‌ی ترافیک ارزش یکسان ندارد؛ تماس VoIP به تأخیر حساس است و Backup شبانه نه. SD-WAN Rule همین تفاوت را اعمال می‌کند.

#### SLA

SLA (Service Level Agreement) در اینجا آستانه‌های کیفیت لینک است:

``` text
config health-check
 edit "HC1"
  config sla
   edit 1
    set latency-threshold 100
    set jitter-threshold 30
    set packetloss-threshold 2
   next
  end
 next
end
```

یعنی لینک «خوب» است اگر تأخیر ≤ 100ms، Jitter ≤ 30ms، Loss ≤ 2٪.

#### استراتژی‌ها

| Mode | معنی |
|---|---|
| manual | ترتیب دستی |
| best-quality | بهترین کیفیت |
| lowest-cost (sla) | ارزان‌ترین لینک که SLA را رعایت کند |
| load-balance | توزیع |

#### مثال ساده — Rule برای Voice

``` text
config service
 edit 1
  set name "VOICE"
  set mode sla
  set dst "SIP-PEERS"
  config sla
   edit "HC1"
    set id 1
   next
  end
  set priority-members 1 2
 next
end
```

Voice روی عضو 1 تا زمانی که SLA شکسته نشود؛ بعد عضو 2.

#### مثال متوسط — Brownout

لینک بالا ولی کیفیت بد (Loss 8٪). Health-check ساده «alive» می‌گوید؛ SLA می‌گوید «violated» و Rule مسیر را عوض می‌کند. همین مزیت SD-WAN است.

#### مثال سخت — Rule Match

اگر هیچ Rule مطابق نیست، ترافیک با **Implicit Rule** (بر اساس Route/Cost) می‌رود. با `diagnose sys sdwan service` ببینید کدام Rule و کدام Member انتخاب شد.

#### Lab

با `tc netem` (روی Lab) تأخیر/Loss به یک لینک تزریق و تغییر مسیر را مشاهده کنید.

``` text
tc qdisc add dev eth1 root netem delay 150ms loss 5%
```

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Rule اعمال نمی‌شود | dst/service | بررسی |
| Flapping | آستانه نزدیک | Hysteresis |
| همه از یک لینک | Rule پایین | ترتیب |

#### پرسش‌ها با پاسخ

**۱. Brownout چیست؟** لینک بالا با کیفیت بد.
**۲. Implicit Rule؟** پیش‌فرض.
**۳. چرا SLA؟** اندازه‌گیری کیفیت.

#### English Corner

- *SLA thresholds let SD-WAN react to brownouts, not just outages.*
- Q: What happens when no SD-WAN rule matches?

## درس 21-4 — Failover عملی، Session و NAT در Dual-ISP/SD-WAN: آزمون، Clear، IP ثابت و معماری ۳

**فصل 21 · بازنویسی عمیق · پیش‌نیاز: ۲۱-۱، ۲۱-۲، ۲۱-۳، ۱۳-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده) و CSR1000v؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. رفتار Session/NAT هنگام Failover را پیش‌بینی و اندازه بگیرد.
2. Clear فیلترشده و Timeout را درست به‌کار ببرد.
3. سرویس‌های حساس به IP (بانک/Partner) را طراحی کند.
4. Failback کنترل‌شده با Hold-down بسازد.
5. معماری ۳ را مستند و آزمون کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Failover را «باید» آزمایش کرد؟** Failover فقط عوض‌شدن Route نیست. وقتی ISP1 قطع می‌شود، پنج چیز تغییر می‌کند: Route، IP عمومی (NAT)، Sessionهای موجود، DNS (اگر وابسته به ISP) و Cache سوییچ/ARP. اگر آزمایش نکرده باشید، در اولین قطع واقعی با «اینترنت دارم ولی برنامه‌ی X قطع است» روبه‌رو می‌شوید.

**چه چیزهایی قطع می‌شود و چه چیزی نه؟**

- **اتصال‌های جدید:** با لینک دوم برقرار می‌شوند.
- **اتصال‌های قدیمی:** به IP ISP1 وابسته‌اند و پس از Failover معمولاً قطع می‌شوند (مگر Session روی لینک قبلی بماند و پاسخ‌ها برنگردند).
- **سرویس‌های ورودی:** اگر IP عمومی VIP به ISP1 وابسته بود، از بیرون در دسترس نیست؛ راه: BGP یا DNS با TTL کم.

**Failback:** بازگشت به لینک اصلی. اگر فوری باشد، یک قطع دوم ایجاد می‌کند؛ بهتر است با تأخیر یا دستی در پنجره‌ی تغییر انجام شود.

**جمع‌بندی اصلی درس:**

Failover ترافیک جدید را جابه‌جا می‌کند؛ Sessionهای موجود با SNAT قدیمی ممکن است قفل شوند و IP خروجی عوض می‌شود که برای Partnerهای Whitelist‌شده مشکل است.

### ۳) توضیح عمیق فنی

#### ۱) رفتار Session

Session TCP روی WAN1 با IP1؛ پس از قطع WAN1 بسته‌های برگشتی نمی‌رسند. تا Timeout یا Clear قفل. ترافیک جدید از WAN2 با IP2.

#### ۲) Clear فیلترشده

``` text
diagnose sys session filter clear
diagnose sys session filter dev <wan1-index>
diagnose sys session list
diagnose sys session clear
diagnose sys session filter clear
```

(یا فیلتر بر `src`/`dst`.) در SD-WAN تنظیماتی برای پاک‌کردن Session هنگام تغییر مسیر هست (`Unverified`).

#### ۳) سرویس‌های حساس به IP

Whitelist Partner: IP خروجی ثابت می‌خواهد. راه‌ها: IP Pool مشترک از PI/BGP، یا Failover فقط برای ترافیک غیرحساس و Policy Route برای سرویس حساس روی ISP ثابت؛ یا هماهنگی Partner برای هر دو IP.

#### ۴) Failback کنترل‌شده

recoverytime بیشتر از failtime؛ Hold-down؛ شاید Failback دستی در ساعات کم‌ترافیک.

#### ۵) ماتریس آزمون

| آزمون | انتظار | اندازه |
|---|---|---|
| قطع WAN1 | Failover ≤ هدف | ping |
| Session TCP طولانی | قفل/Clear | session list |
| بازگشت WAN1 | Failback بدون Flap | Log |
| سرویس Partner | IP صحیح/Re-login | Partner |

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Session | Clear فیلترشده |
| IP ثابت | Rule/Pool/BGP |
| Failback | Hold-down |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — اندازه‌گیری

``` text
ping -i 0.2 8.8.8.8
lost 25 packets x 0.2 s = 5.0 s
```

#### مثال متوسط — جدول قبل/بعد

| مورد | قبل از Failover | بعد از Failover |
|---|---|---|
| Default Route | via ISP1 | via ISP2 |
| IP عمومی کاربر | 203.0.113.2 | 198.51.100.2 |
| Sessionهای باز | روی ISP1 | قطع/جدید |
| IP VIP وب | ISP1 | از بیرون در دسترس نیست |

#### مثال متوسط — پاک‌سازی انتخابی Session

``` text
diagnose sys session filter src 10.10.0.0/24
diagnose sys session clear
diagnose sys session filter clear
```

یا `set snat-route-change enable` در Policy تا Sessionهای SNAT با تغییر Route مسیر را عوض کنند.

#### مثال سخت — VoIP پس از Failover

تماس جاری قطع می‌شود چون IP عمومی عوض شد؛ تماس جدید برقرار می‌شود. برای حفظ تماس: IP ثابت (BGP)، یا Session Border Controller. این ریسک را باید در مستند طراحی بنویسید و با مدیر تصمیم بگیرید.

#### مثال سخت — Failback ناگهانی

پس از برگشت ISP1، Failback فوری، تماس‌ها دوباره قطع. راه: `recoverytime` بالا یا Failback دستی. آزمون: قطع و وصل ISP1 سه بار با ping مداوم و ثبت Loss هر بار.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** قطع wan1: ping 4 ثانیه قطع؛ دانلود قدیمی قفل؛ Clear فیلترشده؛ دانلود جدید OK.

**متوسط (تحلیل):** پس از Failback کاربران قطع‌ووصل می‌شوند: Failback فوری با Session؛ راه: recoverytime بلند، Hold-down، یا ساعت‌محور.

**سخت (IP ثابت):** بانک فقط IP ISP1 را می‌پذیرد؛ Failover ISP2 Login را می‌شکند. تصمیم: Policy Route/SD-WAN Rule برای IP بانک روی ISP1 (و در قطع ISP1 پذیرش Down) یا IP Pool مشترک با BGP؛ ثبت ریسک و RTO.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sys session filter dev 3
diagnose sys session list
diagnose sys session clear
diagnose sys session filter clear
```

### ۸) Verification (اثبات صحت)

- Matrix آزمون.
- Log Failover/Failback.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| قفل | session list | Session قدیمی |
| IP عوض | NAT | Pool |
| Flap | Log | recoverytime |

### ۱۰) نکات امنیتی

- Clear بدون Filter ممنوع.

### ۱۱) جمع‌بندی مفهومی

- Failover ≠ Session ادامه.
- Clear فیلترشده.
- IP ثابت طراحی خاص.
- Failback کنترل‌شده.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا دانلود پس از Failover قفل می‌شود؟ *(پاسخ: 21-4-ت1)*

**ت2.** (ساده) Clear را چگونه فیلتر می‌کنید؟ *(پاسخ: 21-4-ت2)*

**ت3.** (متوسط) چرا recoverytime > failtime؟ *(پاسخ: 21-4-ت3)*

**ت4.** (متوسط) IP ثابت بانک؛ سه راه. *(پاسخ: 21-4-ت4)*

**ت5.** (سخت) Matrix آزمون Failover را کامل کنید. *(پاسخ: 21-4-ت5)*

**ت6.** (سخت، طراحی) معماری ۳. *(پاسخ: 21-4-ت6)*

**Q1.** Quick quiz (English): Why can an ISP failover break connections to partners that whitelist your IP? *(پاسخ: 21-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Whitelist | IP allowlist | فهرست IPهای مجاز |
| Hold-down | Hold-down timer | تأخیر بازگشت |

- *Clear stale sessions with a filter.* ← Sessionهای کهنه را با Filter پاک کنید.

### ۱۴) کارت Lab

**کارت Lab:** Failover. **Evidence:** `03-ops/failover.md`.

### ۱۵) منابع

- درس ۱۳-۷
- Fortinet Docs: SD-WAN

<a id="l-21-5"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Failover و Session

پس از Failover، Sessionهای موجود تا انقضا روی لینک قبلی می‌مانند؛ برای رفتار سریع `set snat-route-change enable` (برای SNAT) یا پاک‌سازی Session محدود. IP عمومی عوض می‌شود ⇒ اتصالات پایدار (مثل SSH/VoIP) قطع می‌شوند؛ برای IP ثابت: BGP با دو ISP یا Cloud Anchor.

**آزمون:** `ping -t` مداوم؛ قطع کابل ISP1؛ ثبت تعداد بسته‌ی گم‌شده × فاصله‌ی ping.

**پرسش‌های مصاحبه**
1. *چرا VoIP قطع؟* IP منبع عوض.
2. *Failback خودکار؟* ممکن است ناپایدار؛ hold-down.
3. *Clear Session؟* با فیلتر.

### تکمیل عمیق: Failover عملی، Session و NAT

#### چرا؟

Failover فقط تغییر Route نیست؛ باید ببینیم Sessionها، NAT و IP عمومی چه می‌شوند.

#### مثال ساده — اندازه‌گیری

``` text
ping -i 0.2 8.8.8.8
# cut ISP1
lost = 25 packets x 0.2 s = 5.0 s
```

#### Session و NAT

پس از Failover IP عمومی تغییر می‌کند؛ اتصال‌هایی که به IP مبدأ وابسته‌اند (SSH، VoIP، بانک) قطع می‌شوند و باید دوباره برقرار شوند. تنها راه‌حل واقعی «IP ثابت» BGP با ISPها یا Cloud Anchor است.

#### مثال متوسط — پاک‌سازی انتخابی

``` text
diagnose sys session filter src 10.10.0.0/24
diagnose sys session filter dst 0.0.0.0/0
diagnose sys session clear
diagnose sys session filter clear
```

یا `set snat-route-change enable` در Policy برای تغییر مسیر Session با SNAT.

#### مثال سخت — Failback

بازگشت ISP1 و Failback فوری ممکن است Session را دوباره قطع کند. راه: `recoverytime` بیشتر یا Failback دستی در Window.

#### مثال: Persist VoIP

در Rule VoIP یک مسیر ثابت با Failover سریع و Failback غیرفعال تا از Flap جلوگیری شود.

#### Lab

Failover را اجرا و جدول «قبل/بعد» (Route، Session، IP عمومی) را پر کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| قطع بعد از Failover | IP عوض شد | BGP/NAT |
| Session قدیم | Timeout | Clear |
| Flap | Failback سریع | recoverytime |

#### پرسش‌ها با پاسخ

**۱. چرا IP عوض می‌شود؟** NAT با IP ISP.
**۲. راه‌حل IP ثابت؟** BGP.
**۳. چرا Failback تأخیری؟** Flap.

#### English Corner

- *A failover that changes the public IP will break sessions that depend on it.*
- Q: Why delay failback?

## درس 21-5 — Gate G8: آزمون عملی Dual-ISP و SD-WAN — صورت مسئله، کلید پاسخ کامل و Rubric

**فصل 21 · بازنویسی عمیق · پیش‌نیاز: ۲۱-۱ تا ۲۱-۴ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. SD-WAN با دو Member (ISP-A و ISP-B)، Health-check و Service Rule را طراحی و پیاده‌سازی کند.
2. Failover و Failback را با اندازه‌گیری (Failtime/Recoverytime) آزمون کند.
3. تفاوت Mode (priority/load-balance/Best Quality) را انتخاب و توجیه کند.
4. سه خرابی (Health-check اشتباه، Policy ناهمخوان، Route) را رفع کند.
5. گزارش و Rubric را تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا G8؟** Gate یعنی ایست بازرسی. G8 ثابت می‌کند Dual-ISP و SD-WAN را از طراحی تا اثبات انجام می‌دهید: Member، Health-check، SLA، Rule، Failover، Failback و گزارش. فقط ساختن کافی نیست؛ باید با عدد نشان دهید Failover زیر هدف است و Brownout شناسایی می‌شود.

**صورت مسئله‌ی نمونه:** شعبه با ISP1 (اصلی) و ISP2 (پشتیبان). Voice باید تأخیر زیر 100 ms و Loss زیر 2٪ داشته باشد؛ Failover زیر 5 ثانیه؛ Failback کنترل‌شده.

**مراحل حل:** ۱) برگه‌ی طراحی ۲) ساخت SD-WAN ۳) SLA ۴) Rule Voice ۵) آزمون قطع کامل ۶) آزمون Brownout با تزریق Loss ۷) Failback ۸) Evidence ۹) گزارش.

**جمع‌بندی اصلی درس:**

دو ISP داریم. اگر ISP-A قطع شد، ترافیک مالی باید خودکار به ISP-B برود و پس از بازگشت A ظرف زمان مشخص برگردد. «قطع شد ولی Failover نشد» رایج‌ترین گزارش است و علتش اغلب Health-check نادرست یا Policy بدون SD-WAN است. این Gate سنجش همین است.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

FortiGate شعبه: port1 (ISP-A، 198.51.100.2/30، GW 198.51.100.1) و port4 (ISP-B، 203.0.113.2/30، GW 203.0.113.1). LAN 10.10.0.0/24. نیاز: ترافیک عادی از A؛ Failover به B ظرف زیر ۱۰ ثانیه؛ Failback پس از ۳۰ ثانیه پایداری A؛ ترافیک ویدئو (Microsoft Teams) ترجیحاً با کمترین Latency.

#### ۲) طراحی مرجع (FortiOS 7.0)

| مورد | مقدار |
|---|---|
| Members | port1 (seq 1)، port4 (seq 2) |
| Health-check | HC-GLOBAL: server 8.8.8.8 و 1.1.1.1، ping، interval 1000 ms |
| failtime / recoverytime | 5 / 10 |
| Rule 1 | Teams: Mode best-quality (latency) |
| Rule 2 | Default: priority-mode (member 1 اول) |

``` text
config system sdwan
 set status enable
 config zone
  edit "virtual-wan-link"
  next
 end
 config members
  edit 1
   set interface "port1"
   set gateway 198.51.100.1
  next
  edit 2
   set interface "port4"
   set gateway 203.0.113.1
  next
 end
 config health-check
  edit "HC-GLOBAL"
   set server "8.8.8.8" "1.1.1.1"
   set protocol ping
   set interval 1000
   set failtime 5
   set recoverytime 10
   set members 1 2
  next
 end
 config service
  edit 1
   set name "Teams"
   set mode sla
   set dst "Microsoft-Teams"
   config sla
    edit "HC-GLOBAL"
     set id 1
    next
   end
   set priority-members 1 2
  next
  edit 2
   set name "Default"
   set mode manual
   set dst "all"
   set priority-members 1 2
  next
 end
end
```

نکته‌ی 7.0: `mode` و گزینه‌های `sla`/`manual`/`priority`/`load-balance` با CLI help تأیید شود؛ تغییرات 7.4.1 در Failtime/Recoverytime مرتبط نیست؛ `Unverified`.

Policy باید `srcintf LAN` و `dstintf virtual-wan-link` (Zone SD-WAN) داشته باشد، نه Interface فیزیکی.

#### ۳) خرابی‌ها و کلید

**خرابی A:** Health-check فقط Gateway ISP را می‌زند؛ ISP قطع ولی Gateway زنده ⇒ Failover نمی‌شود. شاهد: `diagnose sys sdwan health-check` وضعیت alive. رفع: Server خارجی (8.8.8.8).

**خرابی B:** Policy `dstintf port1` است نه Zone SD-WAN ⇒ Service Rule اعمال نمی‌شود. شاهد: `diagnose sys sdwan service` و Session: خروجی ثابت port1. رفع: Policy به Zone.

**خرابی C:** Route Static Default هنوز با Distance کمتر از SD-WAN ⇒ ترافیک از Static. شاهد: `get router info routing-table all`. رفع: حذف Static Default یا Distance بزرگ‌تر.

#### ۴) آزمون Failover

``` text
diagnose sys sdwan health-check
diagnose sys sdwan member
diagnose sys sdwan service
# 1 ping -t to 8.8.8.8 from LAN host
# 2 disable ISP-A (cable or interface down)
# 3 measure packets lost -> time to failover
# 4 enable ISP-A; measure failback after recoverytime
```

معیار: Failover ≤ 10 s، Failback ≈ 10–30 s، بدون قطع Sessionهای فعال مهم (Session Pickup/Preserve برای Session موجود طبق Rule).

#### ۵) Rubric

طراحی ۱۵، پیکربندی ۲۵، تشخیص ۳ خرابی ۳۰، آزمون Failover/Failback با اندازه‌گیری ۲۰، Evidence و صداقت ۱۰. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Mode | priority برای Failover ساده؛ SLA برای حساس به Latency |
| Health-check | Server خارجی نه Gateway |
| Policy | به Zone SD-WAN |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — کلید پاسخ

| بخش | شاهد |
|---|---|
| Build | `diagnose sys sdwan member` |
| SLA | `health-check` با `sla_map` |
| Failover | ping + Log |
| Failback | زمان و روش |

#### مثال متوسط — محاسبه‌ی نمره

``` text
Build 20 | SLA 20 | Failover 25 | Failback 10 | Evidence 15 | Report 10
Example: 20 + 18 + 22 + 8 + 12 + 8 = 88
```

#### مثال سخت — نتیجه‌ی مرزی

Failover 5.2 ثانیه در حالی که هدف کمتر از ۵ بود. تصمیم صادقانه: «مردود» یا «شرطی قبول» با برنامه‌ی بهبود (کاهش interval/failtime) و آزمون مجدد؛ هرگز عدد را گرد نکنید.

#### مثال سخت — دو خرابی تزریقی

قطع ISP1 + Loss 8٪ روی ISP2. انتظار: Voice روی بهترین لینک موجود با اعلام نقض SLA؛ شاهد: `health-check` و Log. اگر هر دو لینک SLA را نقض کنند، رفتار Rule و هشدار باید مستند شود.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Health-check به 8.8.8.8 با failtime 5 و interval 1000 ms: زمان تشخیص ≈ 5 ثانیه؛ پس Failover حدود ۵–۷ ثانیه. محاسبه: failtime × interval = 5 × 1 s = 5 s.

**متوسط (خرابی B):** Policy dstintf=port1. مراحل: ۱) `diagnose sys sdwan service` نشان می‌دهد Rule ساخته شده ولی Hit ندارد. ۲) `session list` ⇒ خروجی port1. ۳) تغییر dstintf به Zone. ۴) Hit افزایش و Session از member انتخابی. پاسخ: Policy باید Zone SD-WAN را هدف بگیرد.

**سخت (Failback ناپایدار):** A هر چند دقیقه Flap می‌کند و ترافیک مرتب بین دو ISP می‌پرد. تحلیل: recoverytime کوتاه؛ A ناپایدار برمی‌گردد. رفع: افزایش recoverytime به 30–60، Health-check با دو Server، و در صورت نیاز Hold. آزمون: ۳ بار قطع/وصل؛ حداکثر یک Failback. ریسک: Failback دیرتر ⇒ مصرف ISP گران‌تر.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → SD-WAN → Interface Members: افزودن port1 و port4.
2. Performance SLA: ساخت HC-GLOBAL.
3. SD-WAN Rules: Teams و Default.
4. Policy & Objects: خروجی Zone SD-WAN.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sys sdwan health-check
diagnose sys sdwan member
diagnose sys sdwan service
get router info routing-table all
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- Health-check alive برای هر دو.
- Failover ≤ 10 s.
- Failback پس از recoverytime.
- Rule Hit و Session روی member درست.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Failover نمی‌شود | Health-check | Server خارجی |
| Rule اثر ندارد | Policy dstintf | Zone SD-WAN |
| ترافیک از Static | routing-table | Distance/حذف Static |
| Flap | recoverytime | افزایش |

### ۱۰) نکات امنیتی

- Policy حداقلی.
- ثبت تغییرات.

### ۱۱) جمع‌بندی مفهومی

- SD-WAN=Member+Health-check+Rule.
- Policy به Zone.
- Failover/Failback اندازه‌گیری.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Health-check به Gateway کافی نیست؟ *(پاسخ: 21-5-ت1)*

**ت2.** (ساده) Failtime و Recoverytime چیست؟ *(پاسخ: 21-5-ت2)*

**ت3.** (متوسط) زمان تقریبی Failover با failtime 5 و interval 1000 ms؟ *(پاسخ: 21-5-ت3)*

**ت4.** (متوسط) چرا Policy باید به Zone SD-WAN باشد؟ *(پاسخ: 21-5-ت4)*

**ت5.** (سخت) Flap باعث پرش ترافیک می‌شود؛ تحلیل و رفع. *(پاسخ: 21-5-ت5)*

**ت6.** (سخت، طراحی) Rule برای Teams. *(پاسخ: 21-5-ت6)*

**Q1.** Quick quiz (English): Why should the policy destination be the SD-WAN zone? *(پاسخ: 21-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SD-WAN | Software-Defined WAN | شبکه‌ی گسترده‌ی نرم‌افزاری |
| SLA | Service Level Agreement | توافق سطح سرویس |

- *A health check should probe a remote target.* ← Health-check باید مقصد دور را پایش کند.

### ۱۴) کارت Lab

**کارت Lab:** G8 Dual-ISP/SD-WAN (اجرا نشده). **Evidence:** `03-ops/g8-sdwan.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: SD-WAN
- FortiOS 7.0 SD-WAN guide

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Rubric G8

مراحل: ساخت SD-WAN ۲۰، SLA ۲۰، Failover ۲۵، Failback ۱۰، Evidence ۱۵، گزارش ۱۰. قطع لینک تزریقی با ثبت زمان.

**پرسش‌های مصاحبه**
1. *Evidence Failover؟* `diagnose sys sdwan health-check` و Log.
2. *Brownout؟* لینک بالا ولی کیفیت بد.
3. *SLA Target؟* از نیاز اپلیکیشن.

### تکمیل عمیق: آزمون G8 — صورت مسئله و کلید

#### چرا؟

G8 ثابت می‌کند Dual-ISP و SD-WAN را از طراحی تا اثبات انجام می‌دهید.

#### صورت مسئله

شعبه با ISP1 (اصلی) و ISP2 (پشتیبان)؛ Voice باید زیر 100ms و Loss زیر 2٪ باشد؛ Failover زیر 5 ثانیه.

#### کلید

1. SD-WAN با دو Member و Health-check.
2. SLA (100ms/30ms/2٪).
3. Rule Voice با mode sla.
4. آزمون: قطع ISP1 ⇒ Failover < 5 s.
5. آزمون Brownout با `tc netem`.
6. Failback کنترل‌شده.

#### محاسبه‌ی نمره

``` text
Build 20 | SLA 20 | Failover 25 | Failback 10 | Evidence 15 | Report 10
Example: 20 + 18 + 22 + 8 + 12 + 8 = 88
```

#### مثال سخت — مرز SLA

تأخیر 98ms (حاشیه‌ی بسیار کم): Flap ممکن است رخ دهد. راه: آستانه‌ی حاشیه‌دار یا Hysteresis؛ مستند.

#### Lab

آزمون را اجرا و Evidence Index بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Failover دیر | failtime بالا | کاهش |
| Flap | آستانه نزدیک | حاشیه |
| Evidence ناقص | ثبت نشد | الگو |

#### پرسش‌ها با پاسخ

**۱. Evidence Failover؟** ping + Log + health-check.
**۲. Hysteresis؟** جلوگیری از Flap.
**۳. آزمون Brownout؟** تزریق تأخیر.

#### English Corner

- *Test brownouts, not only hard failures.*
- Q: How do you avoid flapping near a threshold?

## درس 21-7 — SD-WAN از درون: Health-check، SLA، استراتژی‌ها، Failover/Failback و تفاوت با Routing

**فصل ۲۱ · درس افزوده (تکمیل ۲۱-۳) · پیش‌نیاز: ۱۲-۰، ۱۳-۷، ۵-۷ · ≈ ۸ ساعت**

> **وضعیت (FortiOS 7.0.3):** سینتکس و استراتژی‌ها از مستند رسمی 7.0 ([config system sdwan](https://docs.fortinet.com/document/fortigate/7.0.1/cli-reference/94620/config-system-sdwan)، [Link health monitor](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/580649/link-health-monitor)، [Maximize bandwidth (SLA)](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/708464/maximize-bandwidth-sla-strategy)) بررسی شد. **دقت نسخه:** مستند 7.0 استراتژی «Maximize Bandwidth» را معادل `mode load-balance` می‌داند؛ در نسخه‌های بعد از 7.4.1 این به Lowest Cost (SLA) با `load-balance enable` منتقل شده است؛ پس سینتکس 7.0 را با نسخه‌های جدید مخلوط نکنید. Failback/Preemption به‌صورت مستقل در منابع جست‌وجوشده تأیید نشد (`Unverified`). Lab «اجرا نشده».

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. توضیح دهد **SD-WAN چه چیزی را به Routing معمولی اضافه می‌کند** و چه چیزی را عوض نمی‌کند.
2. **Zone، Member، Health-check (Performance SLA)، SD-WAN Rule (Service)** را تعریف و ارتباطشان را بگوید.
3. Health-check را درست طراحی کند (Server قابل‌اتکا، Protocol، `interval`، `failtime`، `recoverytime`، آستانه‌های Latency/Jitter/Packet Loss).
4. **استراتژی‌های انتخاب مسیر** (Manual، Best Quality، Lowest Cost (SLA)، Maximize Bandwidth/Load-balance) را انتخاب کند.
5. **Failover و Failback** را تحلیل کند و بگوید با Sessionهای موجود چه می‌شود.
6. تفاوت **تصمیم Routing** با **تصمیم Firewall Policy** را در SD-WAN بیان کند.

### ۲) پیش‌نیازها

Packet Flow (۱۲-۰)، Session (۱۳-۷)، Convergence (۵-۷)، Dual-ISP کلاسیک (۲۱-۱).

### ۳) مفهوم پایه

با دو ISP، Routing ساده فقط «مسیر اصلی/پشتیبان» می‌داند و لینک را تا وقتی Interface Up است سالم فرض می‌کند. اما ISP می‌تواند **Up باشد و خراب** (Latency بالا، Packet Loss، بدون پاسخ). **SD-WAN** کیفیت لینک را اندازه می‌گیرد (Health-check) و مسیر را بر اساس **کیفیت و برنامه** انتخاب می‌کند؛ همه‌ی لینک‌ها (Members) در یک **Zone منطقی** جمع می‌شوند و Policy روی Zone نوشته می‌شود.

### ۴) توضیح عمیق فنی

#### ۴-۱) اجزا

``` text
SD-WAN Zone (virtual-wan-link or custom)
  +- Member 1: wan1 (gateway, cost, priority)
  +- Member 2: wan2
Health-check (performance SLA): probes a server per member -> latency/jitter/loss
SD-WAN Rule (service): match traffic -> choose member by strategy + SLA
Firewall policy: srcintf LAN -> dstintf SD-WAN zone (NOT individual wan ports)
Static route: default route via the SD-WAN interface
```

#### ۴-۲) Health-check

طبق مستند: Performance SLA/Health-check کیفیت لینک را می‌سنجد و می‌تواند مسیرها را حذف کند یا ترافیک را جابه‌جا کند. پارامترهای مهم CLI:

- `server`: هدف Probe (باید قابل‌اتکا، مستقل از ISP؛ مثلاً DNS عمومی یا سرور سازمان).
- `protocol`: ping / tcp-echo / udp-echo / http / dns و ...
- `interval` (میلی‌ثانیه): فاصله‌ی Probe.
- `failtime`: تعداد شکست متوالی برای Dead؛ مستند حداقل ۲ را توصیه می‌کند.
- `recoverytime`: تعداد موفقیت متوالی برای بازگشت به Alive (اثر مستقیم بر **Failback**).
- `sla`: آستانه‌ها (`latency-threshold`، `jitter-threshold`، `packetloss-threshold`).
- اگر یک Member چند Health-check دارد، طبق مستند **همه** باید شکست بخورند تا مسیرهای آن از Load-balancing حذف شود.

``` text
Detect time ~= interval x failtime
Recovery time ~= interval x recoverytime
```

مثال: interval 1000 ms و failtime 5 ← Detect ≈ 5 s؛ recoverytime 10 ← Recovery ≈ 10 s. **ترکیب failtime/recoverytime** تعیین می‌کند شبکه چقدر سریع و چقدر پایدار تغییر کند: failtime بسیار کم = Flap؛ recoverytime کم = بازگشت زودهنگام به لینک ناپایدار.

#### ۴-۳) Rule و استراتژی‌ها (7.0)

| استراتژی (GUI) | `mode` CLI | رفتار |
|---|---|---|
| Manual | `manual` | عضو مشخص، بدون کیفیت |
| Best Quality | `priority`/`quality` (بسته به نسخه) | بهترین کیفیت طبق معیار (latency/jitter/loss/bandwidth) |
| Lowest Cost (SLA) | `sla` | اولین عضو (به ترتیب Priority) که SLA را برآورده کند |
| Maximize Bandwidth (SLA) | `load-balance` | همه‌ی اعضایی که SLA را برآورده می‌کنند، با Hash توزیع می‌شوند |

(نام‌های دقیق CLI/GUI در 7.0.3 با مستند تطبیق شود.) `priority-members` ترتیب اعضا را مشخص و `sla` Rule را به Health-check وصل می‌کند.

#### ۴-۴) Routing در برابر Policy در SD-WAN

- **Routing/SD-WAN Rule** تصمیم می‌گیرد **از کدام Member** بسته خارج شود.
- **Firewall Policy** تصمیم می‌گیرد **مجاز است یا نه** (و Profile/NAT).
- ترتیب (۱۲-۰): Policy Route ← SD-WAN Rule ← Routing Table. اگر Rule مطابق نباشد، Default به Implicit Rule (Load-balancing بر اساس Cost/Hash) می‌افتد.
- Policy باید روی **Zone SD-WAN** نوشته شود؛ اگر روی Interface فیزیکی بنویسید، Failover Policy را از بین می‌برد.

#### ۴-۵) Failover و Failback

- **Failover:** وقتی Health-check Member فعلی را Dead/ناقض SLA کند، Rule عضو بعدی را برمی‌گزیند.
- **Failback:** وقتی Member اصلی دوباره Alive/موفق SLA شد (بعد از `recoverytime`)، ترافیک **جدید** به آن برمی‌گردد.
- **Sessionهای موجود** معمولاً روی مسیر قبلی می‌مانند تا تمام شوند یا Clear شوند (۱۳-۷)؛ NAT/IP عوض می‌شود و ممکن است Sessionها در مقصد (مثلاً بانک با IP ثابت) بشکنند. تنظیمات مرتبط با «کشتن Session هنگام تغییر مسیر» نسخه‌ای است (`Unverified`).
- Failback می‌تواند خود Flap‌زا باشد: با `recoverytime` مناسب و Hold-down طراحی شود.

#### ۴-۶) SD-WAN و IPsec

Tunnelهای IPsec (۱۸-۰) به‌عنوان Member عضو Zone می‌شوند؛ Health-check از طریق Tunnel برای مسیرهای Overlay. ترکیب: Underlay (ISPها) + Overlay (Tunnelها).

![شکل: اجزای SD-WAN و ارتباط Rule، Policy و Health-check.](../figures/ch21-l7-fig1.svg)

*شکل: اجزای SD-WAN و ارتباط Rule، Policy و Health-check.*

### ۵) مثال حل‌شده

**هدف:** VoIP روی لینک با Latency < 80 ms و Jitter < 20 ms؛ سایر ترافیک Load-balance.

``` text
config system sdwan
    set status enable
    config zone
        edit "virtual-wan-link"
        next
    end
    config members
        edit 1
            set interface "wan1"
            set gateway 198.51.100.1
        next
        edit 2
            set interface "wan2"
            set gateway 203.0.113.1
        next
    end
    config health-check
        edit "HC-DNS"
            set server "8.8.8.8"
            set protocol ping
            set interval 1000
            set failtime 5
            set recoverytime 10
            set members 1 2
            config sla
                edit 1
                    set latency-threshold 80
                    set jitter-threshold 20
                    set packetloss-threshold 2
                next
            end
        next
    end
    config service
        edit 1
            set name "VOIP"
            set mode sla
            set dst "all"
            set internet-service-app-ctrl 0
            config sla
                edit "HC-DNS"
                    set id 1
                next
            end
            set priority-members 1 2
        next
    end
end
```

(`internet-service-app-ctrl` در مثال بالا نمونه‌ی ساختاری است و باید با Application/Internet Service واقعی جایگزین یا حذف شود؛ سینتکس کامل `Unverified`.)

**GUI:** Network → SD-WAN → SD-WAN Zones/Members؛ Network → SD-WAN → Performance SLAs (Health-check)؛ SD-WAN Rules؛ Policy & Objects → Firewall Policy با Outgoing Interface = Zone. Static Route: مقصد 0.0.0.0/0 با Interface = SD-WAN Zone.

**مثال متوسط:** WAN1 Latency 150 ms شد: Health-check SLA را نقض می‌کند و Rule ترافیک VoIP را به WAN2 می‌برد، بقیه Load-balance؛ Log SLA: Latency.

**مثال سخت (Flap):** لینک ناپایدار هر ۳۰ ثانیه از SLA می‌افتد/برمی‌گردد. با failtime 2 و recoverytime 3 مسیر ۲۰ بار در دقیقه عوض می‌شود. راه‌حل: افزایش recoverytime (مثلاً 30)، افزودن Hysteresis در آستانه‌ی SLA (اجازه‌ی نوسان)، یا Manual برای VoIP.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| Server Health-check | مستقل از ISP، چند Server (قابل‌اتکا) |
| failtime | ≥ 2 (طبق مستند)؛ بالاتر برای لینک نویزی |
| recoverytime | بیشتر از failtime برای جلوگیری از Failback زودهنگام |
| استراتژی | SLA برای Real-time؛ load-balance برای حجم |
| Policy | روی Zone |
| Session | تصمیم درباره‌ی Clear هنگام Failover |

### ۷) Verification

``` text
diagnose sys sdwan health-check
diagnose sys sdwan member
diagnose sys sdwan service
diagnose sys session list
get router info routing-table all
```

(نام زیردستورها `Unverified`.) GUI: Network → SD-WAN → Performance SLAs (نمودار Latency/Jitter/Loss).

### ۸) Troubleshooting

| علامت | شاهد | علت |
|---|---|---|
| Member همیشه Dead | health-check | Server غیرقابل‌دسترس/Policy/Route Probe |
| Rule اثر ندارد | `diagnose sys sdwan service` | Match/Priority؛ Rule بعد از Default |
| Failover انجام شد ولی Session قفل | `session list` | Session قدیمی |
| Flap | Log SLA | failtime/recoverytime/آستانه |
| ترافیک از Interface فیزیکی می‌رود | Policy روی Interface | Policy روی Zone نیست |

### ۹) نکات امنیتی

- Health-check به سرور خارجی = ترافیک Local-out؛ Policy/Source را کنترل کنید.
- مسیر پشتیبان هم باید از Policy و Profile عبور کند.
- Failover می‌تواند ترافیک را از Inspection عبور ندهد اگر Policyها یکسان نباشند.

### ۱۰) جمع‌بندی مفهومی

- SD-WAN = Zone + Member + Health-check + Rule.
- Detect ≈ interval × failtime؛ Failback با recoverytime.
- Rule مسیر را انتخاب می‌کند؛ Policy اجازه می‌دهد؛ هر دو لازم‌اند.
- Sessionهای موجود با Failover تغییر مسیر نمی‌دهند.
- سینتکس 7.0 را با نسخه‌های جدید (۷.۴+) مخلوط نکنید.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) Health-check برای چیست؟ *(پاسخ: 21-7-ت1)*

**ت2.** (ساده) Policy را روی کدام Interface می‌نویسیم؟ *(پاسخ: 21-7-ت2)*

**ت3.** (متوسط) Detect و Recovery با interval 500 ms، failtime 4، recoverytime 20 چقدر است؟ *(پاسخ: 21-7-ت3)*

**ت4.** (متوسط) فرق Lowest Cost (SLA) و Maximize Bandwidth؟ *(پاسخ: 21-7-ت4)*

**ت5.** (سخت) Flap لینک ناپایدار را با تنظیمات Health-check کاهش دهید. *(پاسخ: 21-7-ت5)*

**ت6.** (سخت، طراحی) برای VoIP، ERP و Backup استراتژی و SLA جداگانه طراحی کنید. *(پاسخ: 21-7-ت6)*

**م1.** چرا Server Health-check باید مستقل از ISP باشد؟ *(پاسخ: 21-7-م1)*

**Q1.** Quick quiz (English): What does recoverytime control? *(پاسخ: 21-7-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SD-WAN | Software-Defined WAN | WAN نرم‌افزاری |
| SLA | Service Level Agreement | آستانه‌ی کیفیت |
| Failback | Failback | بازگشت به مسیر اصلی |
| Jitter | Jitter | نوسان تأخیر |
| Overlay/Underlay | Overlay / Underlay | شبکه‌ی روی ISP / خود ISP |

- *Health checks decide when a member is alive and meeting its SLA.* ← Health-check تعیین می‌کند Member زنده است و SLA را رعایت می‌کند.
- *Write firewall policies on the SD-WAN zone, not on member interfaces.* ← Policy را روی Zone بنویسید نه Interface اعضا.

### ۱۳) منابع

- Fortinet Docs: [SD-WAN](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/19246/sd-wan)، [Link health monitor](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/580649/link-health-monitor)، [Maximize bandwidth (SLA) strategy](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/708464/maximize-bandwidth-sla-strategy)، [config system sdwan](https://docs.fortinet.com/document/fortigate/7.0.1/cli-reference/94620/config-system-sdwan).

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: خواندن Health-check

``` text
diagnose sys sdwan health-check
 Seq(1 port1): state(alive), packet-loss(0.000%) latency(12.3) jitter(0.8)
 Seq(2 port2): state(dead)
diagnose sys sdwan service
```

`state(dead)` پس از failtime شکست متوالی. Failback پس از recoverytime موفقیت. اگر هر دو alive ولی SLA بد: Rule به SLA متوسل می‌شود.

**پرسش‌های مصاحبه**
1. *مقدار پیش‌فرض failtime؟* ۵.
2. *Probe پروتکل؟* ping/http/tcp-echo/dns.
3. *Weight/Cost؟* برای lowest-cost.

### تکمیل عمیق: SD-WAN از درون — Health-check، SLA و Failback

#### چرا؟

بدون فهمیدن اینکه Health-check چطور کار می‌کند، نمی‌توانید رفتار عجیب (مثلاً تغییر مسیر بی‌دلیل) را توضیح دهید.

#### خواندن خروجی

``` text
diagnose sys sdwan health-check
Health Check(HC1):
Seq(1 port1): state(alive), packet-loss(0.000%) latency(12.31) jitter(0.82) sla_map=0x1
Seq(2 port2): state(dead)
```

تفسیر: Member 1 زنده با کیفیت خوب و `sla_map=0x1` (SLA 1 را رعایت می‌کند)؛ Member 2 مرده.

#### پارامترها

| پارامتر | معنی |
|---|---|
| interval | فاصله‌ی پروب (ms) |
| failtime | تعداد شکست متوالی برای dead |
| recoverytime | تعداد موفقیت متوالی برای alive |
| probe-timeout | مهلت پاسخ |

مقادیر پیش‌فرض را از مستند نسخه بخوانید.

#### مثال ساده — زمان‌ها

``` text
Down detection = interval x failtime ; Up detection = interval x recoverytime
500 ms x 5 = 2.5 s ; 500 ms x 5 = 2.5 s
```

#### مثال متوسط — Probe پروتکل

ping، http، tcp-echo، dns؛ برای وب از http مفیدتر است چون ping ممکن است مسدود/Rate-limit شود.

#### مثال سخت — اشتباه رایج

یک سرور واحد برای Health-check (مثلاً 8.8.8.8) اگر مقصد مشکل پیدا کند، هر دو لینک را «dead» می‌کند. راه: دو سرور متفاوت و `update-static-route`/`members` هوشمند.

#### Lab

Health-check را با دو پروب مختلف مقایسه کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| هر دو dead | یک سرور | دو سرور |
| ping مسدود | Rate limit | http |
| flap | آستانه | تنظیم |

#### پرسش‌ها با پاسخ

**۱. sla_map؟** وضعیت SLAها.
**۲. چرا دو سرور؟** SPOF Health-check.
**۳. failtime؟** شمارش شکست.

#### English Corner

- *Use more than one probe target so a remote outage does not mark all links dead.*
- Q: What do interval and failtime determine together?

## پاسخ‌های فصل 21

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 21-1

**21-1-ت1** — Route ترجیحی.

Static با Priority/Distance بهتر Route ترجیحی است.

**21-1-ت2** — با Probe کشف قطع ISP و حذف Route.

Probe (Link-monitor/Health-check) قطع ISP را کشف و Route را حذف می‌کند.

**21-1-ت3** — تا خرابی Server با خرابی لینک اشتباه نشود.

چند Server پایش شود تا خرابی یک Server با خرابی لینک اشتباه نشود.

**21-1-ت4** — ≈ 5 ثانیه (به‌علاوه‌ی Convergence).

زمان تشخیص تقریباً failtime × interval ≈ ۵ ثانیه به‌علاوه‌ی Convergence.

**21-1-ت5** — خیر؛ SLA/Loss Threshold در SD-WAN.

خیر؛ در SD-WAN SLA/Loss Threshold برای کیفیت وجود دارد.

**21-1-ت6** — SLA، چند لینک، Overlay، گزارش کیفیت.

طرح: SLA، چند لینک، Overlay و گزارش کیفیت.

**21-1-Q1** — A degraded link with high loss or latency that still answers probes.

### پاسخ‌های بازنویسی درس 21-2

**21-2-ت1** — چون Interface عضو SD-WAN نباید مستقیم در Policy/Route/Object مرجع داشته باشد.

**21-2-ت2** — روی Zone SD-WAN.

Policy روی Zone SD-WAN نوشته می‌شود، نه Interface فیزیکی.

**21-2-ت3** — Server/Protocol Probe، ICMP توسط ISP بلاک؛ Route/Source Probe؛ شاهد Sniffer؛ رفع: dns/http Probe.

**21-2-ت4** — Backup، فهرست مرجع‌ها، ساخت Zone/Member، انتقال Policy/Route به Zone در Change Window، آزمون و Rollback.

**21-2-Q1** — On the SD-WAN zone interface.


### پاسخ‌های بازنویسی درس 21-3

**21-3-ت1** — بالا به پایین؛ اولین Rule مطابق.

SD-WAN Rule از بالا به پایین و اولین Rule مطابق اعمال می‌شود.

**21-3-ت2** — sla: اولین عضو دارای SLA؛ load-balance: توزیع بین همه‌ی اعضای دارای SLA.

Mode sla اولین عضو دارای SLA؛ load-balance توزیع بین همه‌ی اعضای دارای SLA. نام‌گذاری مستند Fortinet: Best Quality (حالت priority)، Lowest Cost (حالت sla) و Maximize Bandwidth (load-balance)؛ از 7.4.1 Load-balance داخل Lowest Cost (SLA) ادغام شده است.

**21-3-ت3** — Rule عمومی بالاتر Match می‌شود؛ ترتیب را اصلاح کنید.

Rule عمومی بالاتر Match می‌شود؛ ترتیب را اصلاح کنید.

**21-3-ت4** — VoIP: sla با Latency<80/Jitter<20؛ ERP: sla با ترجیح لینک پایدار؛ Backup: load-balance.

**21-3-Q1** — Traffic is handled by the implicit rule, which load-balances across members.


### پاسخ‌های بازنویسی عمیق درس 21-4

**21-4-ت1** — Session با SNAT/Interface قدیمی ادامه نمی‌یابد.

با Failover، Session با SNAT/Interface قدیمی ادامه نمی‌یابد؛ باید Session پاک یا Pickup شود.

**21-4-ت2** — `filter dev/src/dst` سپس `clear`.

`diagnose sys session filter dev/src/dst` سپس `clear` برای پاک‌سازی انتخابی.

**21-4-ت3** — تا بازگشت زودهنگام به لینک ناپایدار رخ ندهد.

recoverytime/Hold برای جلوگیری از بازگشت زودهنگام به لینک ناپایدار.

**21-4-ت4** — Rule روی ISP ثابت، IP Pool/BGP، هماهنگی Partner.

Rule روی ISP ثابت، IP Pool/BGP و هماهنگی Partner برای IP مبدأ.

**21-4-ت5** — قطع/Session/بازگشت/Partner با اندازه‌گیری.

Evidence Failover: قطع، Session، بازگشت و Partner با اندازه‌گیری.

**21-4-ت6** — Dual-ISP SD-WAN HA با Rule/SLA و Clear.

طرح Dual-ISP SD-WAN HA با Rule/SLA و Clear.

**21-4-Q1** — The outgoing source IP changes to the other ISP address.


### پاسخ‌های بازنویسی عمیق درس 21-5


### پاسخ‌های بازنویسی عمیق درس 21-5

**21-5-ت1** — Gateway ممکن است زنده باشد ولی ISP قطع؛ باید مقصد خارجی را پایش کرد.

**21-5-ت2** — تعداد شکست پشت‌سرهم برای Dead و تعداد موفقیت برای بازگشت (Alive).

**21-5-ت3** — حدود ۵ ثانیه (۵ × ۱ ثانیه) به‌علاوه‌ی چند صد میلی‌ثانیه.

**21-5-ت4** — Rule و انتخاب Member فقط برای ترافیک وارد Zone SD-WAN اعمال می‌شود.

**21-5-ت5** — recoverytime کوتاه؛ افزایش و Health-check دو-Server؛ آزمون ۳ قطع/وصل.

**21-5-ت6** — Mode SLA با Latency و Health-check؛ Default priority؛ آزمون اندازه‌گیری Latency.

**21-5-Q1** — Because SD-WAN rules only apply to traffic that goes to the SD-WAN zone.

### پاسخ‌های درس افزوده‌ی 21-7 (فصل 21)

**21-7-ت1** — سنجش کیفیت لینک (Latency/Jitter/Loss) و تشخیص Dead.

Performance SLA سنجش کیفیت لینک (Latency/Jitter/Loss) و تشخیص Dead است.

**21-7-ت2** — روی Zone SD-WAN.

Rule SD-WAN روی ترافیک Zone SD-WAN اعمال می‌شود.

**21-7-ت3** — Detect = 500 ms × 4 = 2 s؛ Recovery = 500 ms × 20 = 10 s.

Detect = 500 ms × 4 = 2 s؛ Recovery = 500 ms × 20 = 10 s.

``` text
Detect = 500 ms x 4 = 2 s ; Recovery = 500 ms x 20 = 10 s
```

**21-7-ت4** — Lowest Cost (SLA): اولین عضو دارای SLA؛ Maximize Bandwidth: توزیع بین همه‌ی اعضای دارای SLA.

**21-7-ت5** — افزایش recoverytime، افزودن Hysteresis در آستانه‌ها، failtime متناسب، Probe چندگانه، Manual برای ترافیک حساس.

**21-7-ت6** — VoIP: SLA با Latency/Jitter کم؛ ERP: Best Quality؛ Backup: Lowest Cost یا Load-balance با SLA آسان.

**21-7-م1** — تا خرابی ISP با خرابی خود Probe اشتباه گرفته نشود؛ مستقل بودن نتیجه‌ی قابل‌اتکا می‌دهد.

**21-7-Q1** — The number of consecutive successful probes required before a link is considered alive again (failback behavior).

# پایان بخش ۷ (فصل‌های ۱۹ تا ۲۱)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- Hub-and-Spoke با OSPF/BGP؛ SSL VPN/Dial-up؛ Dual-ISP، SD-WAN Rule/SLA.

## ۲) آزمون پایان سه فصل
**س1** — چرا Selector 0.0.0.0/0 برای پویا؟

**س2** — network-type OSPF روی Tunnel؟

**س3** — iBGP یا eBGP؟

**س4** — Local Breakout؟

**س5** — ADVPN وضعیت؟

**س6** — چرا SSL VPN ایزوله؟

**س7** — Split Tunnel؟

**س8** — MFA چرا؟

**س9** — Link Monitor؟

**س10** — SD-WAN Zone؟

**س11** — SLA Strategy؟

**س12** — Session پس از Failover؟


## ۳) پاسخ آزمون
- **س1:** تا Routing از Tunnel عبور کند.
- **س2:** point-to-point.
- **س3:** iBGP همان AS؛ eBGP AS متفاوت.
- **س4:** خروج محلی به اینترنت.
- **س5:** Unverified.
- **س6:** CVEهای 7.0.x.
- **س7:** فقط ترافیک سازمانی.
- **س8:** لایه‌ی دوم.
- **س9:** تشخیص قطع ISP.
- **س10:** گروه منطقی Memberها.
- **س11:** انتخاب بر اساس کیفیت.
- **س12:** می‌ماند مگر Clear.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| Hub-and-Spoke | L3 | آزمون فصل ۱۹ |
| Remote Access | L2 | آزمون فصل ۲۰ |
| SD-WAN | L3 | G8 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. Labها اجرا نشده. 2. SD-WAN/ADVPN/sslvpn سینتکس Unverified. 3. SSL VPN فقط ایزوله.

## ۶) پیش‌نیازهای بخش بعد
Dual-ISP پایدار؛ آشنایی با HA؛ لایسنس HA بررسی.

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*`

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۲۱ |
| آخرین درس تکمیل‌شده | ۲۱-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۲۲ |
| فایل تولیدشده | `course/Course_Part_07_Chapters_19-21.md` |
