# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۵ از ۱۱ — فصل‌های ۱۳ تا ۱۵

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۵ از ۱۱ |
| فصل‌های این فایل | ۱۳ ، ۱۴ ، ۱۵ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۱۳–۱۵ تولید شد؛ Policy/NAT، ابزارهای عیب‌یابی، معماری دوفایروالی.** Labها «اجرا نشده»؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 18.

| Lab | وضعیت |
|---|---|
| 13-1 | اجرا نشده (فقط طراحی) |
| 13-2 | اجرا نشده (فقط طراحی) |
| 13-3 | اجرا نشده (فقط طراحی) |
| 13-4 | اجرا نشده (فقط طراحی) |
| 13-5 | اجرا نشده (فقط طراحی) |
| 13-6 | اجرا نشده (فقط طراحی) |
| 14-1 | اجرا نشده (فقط طراحی) |
| 14-2 | اجرا نشده (فقط طراحی) |
| 14-3 | اجرا نشده (فقط طراحی) |
| 14-4 | اجرا نشده (فقط طراحی) |
| 14-5 | اجرا نشده (فقط طراحی) |
| 14-6 | اجرا نشده (فقط طراحی) |
| 15-1 | اجرا نشده (فقط طراحی) |
| 15-2 | اجرا نشده (فقط طراحی) |
| 15-3 | اجرا نشده (فقط طراحی) |
| 15-4 | اجرا نشده (فقط طراحی) |
| 15-5 | اجرا نشده (فقط طراحی) |
| 15-6 | اجرا نشده (فقط طراحی) |

---

<a id="ch13"></a>

> **نسخه‌ی اصلاح‌شده (v3.9):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۱۳-۷، ۱۴-۷ (دسته A). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

# فصل 13 — FortiGate II: Policy، Session، NAT، VIP، IP Pool و Central NAT (تک‌فایروالی کامل)

> **یادداشت علمی v4.0 — فصل 13:** عمومی: Policy First-Match، NAT، Session. مختص محصول: VIP، IP Pool، Central NAT در FortiOS.
> فرض: اثر تغییر بر Session موجود وابسته به نسخه/Offload/Proxy؛ «Session هرگز دوباره ارزیابی نمی‌شود» تعمیم نادرست است.
> مراجع: Fortinet Docs 7.0؛ جزئیات Session/Route-change نیازمند بررسی.


**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۲ (Baseline)، فصل ۱۱ (G4).
**اهداف:** Firewall Policy (اجزا، ترتیب، Log)؛ NAT (Policy NAT، IP Pool، Central NAT)؛ VIP/Port-forward و Hairpin؛ Session Table؛ مدیریت Policy (Shadow، تداخل Object، Hit Count)؛ سناریوهای خرابی؛ **Gate G5**. هر موضوع با GUI و CLI.
**نسخه:** FortiOS 7.0.3 اسمی؛ همه‌ی دستورها آزمایش‌نشده روی Image شما (در بوت اول مقایسه شوند).
**معیار تسلط:** سناریوی تک‌فایروالی (اینترنت، VIP، Policy محدود) کامل و با Packet Walk اثبات؛ پیدا کردن Policy اشتباه، NAT اشتباه و Shadow با شواهد.
**اشتباهات رایج:** ترتیب Policy؛ `set nat enable` فراموش‌شده؛ VIP بدون Policy؛ Policy «all/all»؛ Log خاموش.

**درس‌های فصل:**
- [درس 13-1 — اجزای Firewall Policy، ترتیب و Log](#l-13-1)
- [درس 13-2 — NAT: Policy NAT، IP Pool و Central NAT](#l-13-2)
- [درس 13-3 — VIP، Port-Forward و Hairpin NAT](#l-13-3)
- [درس 13-4 — Session Table، Timeout و ابزارهای Session](#l-13-4)
- [درس 13-5 — مدیریت Policy: Shadow، تداخل Object، Hit Count و Schedule](#l-13-5)
- [درس 13-6 — سناریوهای خرابی (Policy/NAT/Route) و آزمون G5](#l-13-6)

---

<a id="l-13-1"></a>

## درس 13-1 — Firewall Policy: اجزا، قاعده‌ی First Match، Implicit Deny و Log

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۲، ۱۲-۳، ۱۲-۴ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. اجزای یک Firewall Policy و نقش هرکدام را بگویید.
2. قاعده‌ی First Match، Implicit Deny و Policy 0 را توضیح دهید.
3. ترتیب Policyها را از خاص به عام و بدون Shadow بنویسید.
4. با `iprope lookup` بدون ترافیک Policy مطابق را پیدا کنید.
5. Logging را در سطح Policy و Implicit Deny تنظیم کنید.
6. یک مجموعه‌ی Policy کامل را با آزمون مثبت و منفی اثبات کنید.

### چرا باید یاد بگیریم؟

Policy قلب فایروال است. تقریباً هر حادثه‌ی امنیتی یا قطعی در فایروال به یک Policy برمی‌گردد: یا بیش‌ازحد باز (امنیت)، یا اشتباه/به‌ترتیب نادرست (قطعی). باید Policy را مثل یک جمله‌ی دقیق بخوانید و بنویسید: «چه کسی، از کجا، به کجا، چه سرویسی، چه کاری، چه زمانی، با چه بازرسی و آیا ثبت شود». مثل نگهبانی که فهرست مهمانان را از بالا به پایین می‌خواند و اولین سطر مطابق را اجرا می‌کند؛ اگر نامی نبود، رد می‌کند. جابه‌جایی دو سطر می‌تواند همه را داخل کند یا همه را بیرون.

### اجزای Policy

| جزء | نقش | مثال |
|---|---|---|
| Incoming Interface/Zone | ورودی | port2 / ZN-USERS |
| Outgoing Interface/Zone | خروجی | port1 / ZN-INET |
| Source | چه کسی (آدرس، گروه، کاربر) | NET-USERS |
| Destination | به چه کسی | SRV-ERP / VIP-WEB / all |
| Schedule | چه زمانی | always / WORK-HOURS |
| Service | پورت/پروتکل | HTTPS، DNS |
| Action | عمل | accept / deny |
| NAT | ترجمه | enable + IP Pool |
| Security Profiles | بازرسی | AV، IPS، Web |
| Log | ثبت | all / utm / disable |

### First Match و Implicit Deny

``` text
packet -> Policy 10? match -> apply, stop
       -> Policy 20? match -> apply, stop
       -> ...
       -> no match -> Implicit Deny (policy 0)
```

- **First Match:** از بالا به پایین؛ اولین مطابقت اعمال می‌شود.
- **Implicit Deny (Policy 0):** اگر هیچ Policy مطابق نباشد، بسته رد می‌شود. این قاعده در GUI دیده نمی‌شود و **به‌صورت پیش‌فرض Log ندارد.**
- **Shadow:** Policy که هرگز اجرا نمی‌شود چون Policy بالاتر همه‌ی ترافیکش را می‌گیرد.

### ترتیب درست: از خاص به عام

``` text
10 USERS -> SERVERS  svc HTTPS,SMB       accept log all
20 GUEST -> INTERNET svc HTTP,HTTPS,DNS  accept nat log utm
30 USERS -> INTERNET svc HTTP,HTTPS,DNS  accept nat log utm
90 any   -> any      svc ALL             deny   log all
```

اگر Policy 30 با `dstaddr all` قبل از 10 بود، ترافیک USERS→SERVERS (اگر در Zone اینترنت هم می‌شد دید) را می‌گرفت؛ و اگر 90 (Deny) بالاتر بود، هیچ‌چیز کار نمی‌کرد.

### Lookup بدون ترافیک

``` text
diagnose firewall iprope lookup <src> <sport> <dst> <dport> <proto> <srcintf>
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.10 445 tcp port2
 -> policy 10
diagnose firewall iprope lookup 10.10.0.5 40000 203.0.113.10 22 tcp port2
 -> policy 90 (deny)
```

Lookup بسته‌ی فرضی را مثل بسته‌ی واقعی Policy می‌سنجد بدون اینکه ترافیک بفرستد؛ ابزار اصلی آزمون قبل/بعد از تغییر.

### Logging

سه حالت `logtraffic`: `all` (همه‌ی Sessionها)، `utm` (فقط رویدادهای UTM)، `disable`. Deny ضمنی:

``` text
config log setting
 set fwpolicy-implicit-log enable
end
```

یا بهتر: Policy Deny صریح با `logtraffic all` در انتها.

### مثال‌های حل‌شده

#### مثال ساده — خواندن یک Policy

``` text
edit 30
 set srcintf "port2"
 set dstintf "port1"
 set srcaddr "NET-USERS"
 set dstaddr "all"
 set service "HTTP" "HTTPS" "DNS"
 set action accept
 set nat enable
 set logtraffic all
```

«کاربران NET-USERS که از port2 وارد می‌شوند، به هر مقصد از port1 با HTTP/HTTPS/DNS اجازه دارند، با NAT و ثبت کامل».

#### مثال متوسط — Shadow

``` text
ID 30 USERS -> any  svc ALL  accept
ID 10 USERS -> SRV  svc HTTPS accept log
```

Policy 10 هرگز اجرا نمی‌شود (Hit Count صفر). رفع: `move 10 before 30` و تنگ‌کردن 30 (service محدود).

#### مثال متوسط — اثبات با Lookup

۱) آزمون مثبت: Users→ERP:443 ⇒ policy 10 ۲) آزمون منفی: Users→Mgmt:22 ⇒ policy 90 ۳) آزمون Guest→Servers ⇒ 90. ثبت خروجی‌ها در Evidence.

#### مثال سخت — اسکن دیده نمی‌شود

اسکن پورت از اینترنت: Log ندارد. علت: Deny ضمنی بی‌Log. رفع: `fwpolicy-implicit-log enable` یا Policy 90. شاهد: Log با `policyid=90` و `action=deny` برای هر پورت اسکن‌شده. حجم Log هم مدیریت شود (Rate).

#### مثال سخت — تغییر امن

افزودن Policy جدید: ۱) Backup ۲) Lookup قبل ۳) ایجاد با Disable ۴) Lookup بعد (باید مطابق شود) ۵) Enable ۶) آزمون واقعی و Log ۷) Hit Count افزایش ۸) CHG بسته. اگر Lookup بعد policy 0 دهد، Interface/Address/Service را بازبینی.

### مسیر GUI (مستندی، Unverified)

1. Policy & Objects → Firewall Policy → Create New.
2. Name، Incoming/Outgoing Interface، Source، Destination، Schedule، Service را پر کنید.
3. Action = ACCEPT؛ NAT را بر اساس نیاز؛ Log = All Sessions.
4. Comments را بنویسید؛ OK.
5. با کشیدن (Drag) ترتیب را اصلاح کنید؛ ستون ID و Hit Count را فعال کنید.

### Lab هدایت‌شده (اجرا نشده)

1. چهار Policy بالا را بسازید.
2. چهار Lookup (دو مثبت، دو منفی).
3. Shadow عمدی و مشاهده‌ی Hit Count.
4. Deny بی‌Log و فعال‌سازی Log.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Policy اجرا نمی‌شود | Shadow | ترتیب |
| Deny بی‌Log | implicit | Deny صریح |
| ترافیک رد می‌شود | Interface/Address | Lookup |
| همه باز است | Policy ALL | تنگ‌کردن |

### جمع‌بندی

Policy: Interface، Source، Destination، Service، Schedule، Action، NAT، Profile، Log. First Match از بالا؛ Implicit Deny بی‌Log. خاص به عام، Lookup برای اثبات، Deny صریح با Log در انتها.

### تمرین و ارزیابی

**ت1.** (ساده) First Match یعنی چه؟ *(پاسخ: 13-1-ت1)*

**ت2.** (ساده) چرا Outgoing Interface را خود ما انتخاب می‌کنیم ولی Route تعیین می‌کند؟ *(پاسخ: 13-1-ت2)*

**ت3.** (متوسط) Policy 3 (Deny all) بالای Policy 2 است. چه می‌شود و چطور کشف می‌کنید؟ *(پاسخ: 13-1-ت3)*

**ت4.** (متوسط) تفاوت Log All Sessions و Security Events؟ *(پاسخ: 13-1-ت4)*

**ت5.** (سخت) برای DB فقط از App مجاز باشد. Policyها را بنویسید و آزمون منفی را شرح دهید. *(پاسخ: 13-1-ت5)*

**ت6.** (سخت، طراحی) استاندارد Policy برای سازمان ۳ شعبه‌ای. *(پاسخ: 13-1-ت6)*

**Q1.** Quick quiz (English): Why does an explicit deny rule with logging help compared to the implicit deny? *(پاسخ: 13-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Policy | Firewall policy | قاعده‌ی فایروال |
| Shadow | Shadowed rule | قاعده‌ی پنهان‌شده |
| Hit count | Policy hit count | شمارنده‌ی تطابق |

- *The first matching policy wins.* ← اولین Policy مطابق برنده است.
- *Always log denied traffic.* ← ترافیک ردشده را همیشه Log کنید.

### کارت Lab

**کارت Lab:** سه Policy و آزمون ترتیب (اجرا نشده). **Evidence:** `03-ops/policy-review.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- FortiOS 7.0 CLI Reference: config firewall policy

<a id="l-13-2"></a>

## درس 13-2 — NAT در FortiGate: Policy NAT، IP Pool، Central NAT و انتخاب درست

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۴، ۱۳-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. انواع NAT در FortiGate (Interface NAT، IP Pool انواع، Central NAT) را تمایز دهید.
2. ظرفیت NAT/IP Pool را محاسبه کنید.
3. Policy NAT را با IP Pool بسازید و تأیید کنید.
4. Central NAT و تفاوت رفتار آن را بدانید.
5. Pool Exhaustion را تشخیص و رفع کنید.
6. NAT را با Session و Sniffer اثبات کنید.

### چرا باید یاد بگیریم؟

آدرس‌های خصوصی (10.x، 192.168.x) در اینترنت مسیر ندارند. NAT آنها را به آدرس عمومی ترجمه می‌کند. تصمیم اینکه چه نوع NAT، با چند IP عمومی و چطور ردیابی شود، بر ظرفیت، تجربه‌ی کاربر و ممیزی اثر مستقیم دارد. مثل میز پذیرش شرکت که نام داخلی را به شماره‌ی بیرونی تبدیل می‌کند: اگر شماره‌ها کم باشد، صف می‌شود.

### انواع NAT

| نوع | شرح | کاربرد |
|---|---|---|
| Interface NAT | با IP Interface خروجی | ساده‌ترین |
| IP Pool Overload (PAT) | چند IP عمومی با تغییر پورت | ظرفیت بالا |
| IP Pool One-to-One | هر کاربر یک IP | نیاز IP اختصاصی |
| Fixed Port Range | هر کاربر بازه‌ی پورت ثابت | ردیابی |
| Port Block Allocation (PBA) | بلوک پورت به هر کاربر | Log کم‌حجم (CGN) |
| Central NAT | ترجمه از Policy جدا | مدیریت متمرکز |

### ظرفیت

یک IP عمومی حدود ۶۴ هزار پورت دارد (۱۰۲۴ تا ۶۵۵۳۵). پورت **به‌ازای هر مقصد** (IP:Port) جدا شمرده می‌شود؛ پس مقصدهای متنوع فشار را کم می‌کنند و مقصد واحد (CDN) بدترین حالت است.

``` text
Users 1200 x sessions per user 60 = 72000 sessions
Ports per IP ~ 64500
Worst case (one destination): 72000 / 64500 = 1.12 -> 2 IPs
With 50 % headroom: 3 IPs
```

### IP Pool

``` text
config firewall ippool
 edit "POOL-INET"
  set type overload
  set startip 203.0.113.20
  set endip 203.0.113.22
 next
end
config firewall policy
 edit 30
  set nat enable
  set ippool enable
  set poolname "POOL-INET"
 next
end
```

IP Poolها باید توسط ISP به فایروال Route شوند؛ و برای `one-to-one` تعداد IP ≥ تعداد کاربران هم‌زمان.

### Central NAT

وقتی فعال شود (`set central-nat enable` در `config system settings`)، `nat enable` در Policy اثر ندارد و ترجمه با `central-snat-map` انجام می‌شود:

``` text
config firewall central-snat-map
 edit 1
  set srcintf "port2"
  set dstintf "port1"
  set orig-addr "NET-USERS"
  set dst-addr "all"
  set nat-ippool "POOL-INET"
 next
end
```

مزیت: ترجمه از Policy جدا و یک‌جا. اشتباه رایج: پس از فعال‌سازی، «NAT ناگهان کار نمی‌کند» چون map ندارید.

### مشاهده

``` text
diagnose sys session list     (snat field)
diagnose sys session filter src 10.10.0.5
diagnose firewall ippool-all list
diagnose firewall ippool-all stats   (exhaustion)
```

### مثال‌های حل‌شده

#### مثال ساده — Interface NAT

Policy `set nat enable` بدون Pool: Src IP با آدرس port1 ترجمه می‌شود. Session: `snat 10.10.0.5:40000->203.0.113.2:40000`.

#### مثال متوسط — محاسبه‌ی Pool

۱۲۰۰ کاربر؛ هر کدام ۶۰ Session؛ مقصدها متنوع (۵۰۰۰ مقصد متفاوت). کل 72000؛ با مقصد متنوع هر IP عملاً ظرفیت بسیار بیشتر دارد. ولی برای بدترین حالت ۳ IP. شاهد: `ippool-all stats` برای عدد واقعی.

#### مثال متوسط — Central NAT

پس از فعال‌سازی Central NAT کاربران اینترنت ندارند. علت: map ندارد. رفع: `central-snat-map` برای NET-USERS. Lookup و Session تأیید.

#### مثال سخت — «پاسخ نمی‌آید»

Session SNAT به 203.0.113.21 ساخته می‌شود ولی پاسخی نیست. Sniffer WAN: فقط خروج. علت: ISP آن IP را Route نکرده. رفع: هماهنگی ISP/IP Interface. آزمون: `curl --interface` و Session.

#### مثال سخت — Pool Exhaustion

Log: «IP pool exhausted». `ippool-all stats`: Pool پر. علل: Pool کوچک، مقصد واحد، اتصال‌های بی‌پایان (UDP)، DoS. رفع: افزایش IP، PBA، کاهش Timeout، بررسی مبدأ پرمصرف. شاهد: کاهش `exhausted`.

### مسیر GUI (مستندی، Unverified)

1. Policy & Objects → IP Pools → Create New (Type Overload، Start/End IP).
2. Firewall Policy → NAT = Enable → Dynamic IP Pool → انتخاب Pool.
3. برای Central NAT: System → Feature Visibility → Central SNAT را روشن؛ Policy & Objects → Central SNAT → Create New.

### Lab هدایت‌شده (اجرا نشده)

1. Interface NAT و مشاهده‌ی snat.
2. Pool با دو IP و مشاهده‌ی چرخش.
3. Central NAT و خطای «بدون map».
4. محاسبه‌ی ظرفیت و آزمون بار.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| پاسخ نمی‌آید | Pool Route نشده | ISP |
| NAT اعمال نمی‌شود | Central NAT/Policy | map/enable |
| Pool پر | ظرفیت | افزایش/PBA |
| IP ثابت لازم | overload | one-to-one |

### جمع‌بندی

NAT انواع دارد؛ Pool با Overload، One-to-One یا PBA. ظرفیت = Session/پورت به‌ازای مقصد. Central NAT جدول جدا دارد. ISP باید Pool را Route کند.

### تمرین و ارزیابی

**ت1.** (ساده) PAT چیست؟ *(پاسخ: 13-2-ت1)*

**ت2.** (ساده) تفاوت Overload و One-to-One؟ *(پاسخ: 13-2-ت2)*

**ت3.** (متوسط) برآورد ظرفیت یک IP؟ *(پاسخ: 13-2-ت3)*

**ت4.** (متوسط) چرا پس از Central NAT اینترنت قطع شد؟ *(پاسخ: 13-2-ت4)*

**ت5.** (سخت) ۱۰۰۰ کاربر، ۸۰ Session هر نفر. *(پاسخ: 13-2-ت5)*

**ت6.** (سخت، طراحی) NAT برای سه Zone با Poolهای متفاوت. *(پاسخ: 13-2-ت6)*

**Q1.** Quick quiz (English): What happens to the NAT option in policies after Central NAT is enabled? *(پاسخ: 13-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PAT | Port Address Translation | ترجمه‌ی پورت |
| PBA | Port Block Allocation | تخصیص بلوک پورت |
| CGN | Carrier-Grade NAT | NAT مقیاس اپراتور |

- *The pool must be routed to you by the ISP.* ← ISP باید Pool را به شما Route کند.

### کارت Lab

**کارت Lab:** NAT و Pool (اجرا نشده). **Evidence:** `02-design/fgt-nat.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: NAT
- FortiOS 7.0: IP pools
- FortiOS 7.0: Central NAT

<a id="l-13-3"></a>

## درس 13-3 — VIP، Port-Forward و Hairpin NAT: انتشار امن سرویس داخلی

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۱، ۱۳-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. VIP و DNAT را توضیح دهید و فرق One-to-One و Port-forward را بگویید.
2. VIP و Policy ورودی را بسازید.
3. آزمون مثبت و منفی انتشار سرویس را اجرا کنید.
4. مشکل Hairpin و راه‌حل‌های آن را بدانید.
5. نیازمندی‌های Route/ARP برای IP عمومی را بشناسید.
6. امنیت سرویس منتشرشده (WAF/IPS/DoS) را اعمال کنید.

### چرا باید یاد بگیریم؟

برای انتشار سرویس داخلی (وب‌سرور DMZ) به اینترنت، ترافیکی که به **آدرس عمومی** می‌رسد باید به آدرس داخلی ترجمه شود (DNAT). VIP (Virtual IP) این کار را می‌کند: مثل منشی‌ای که تماس را به داخلی مناسب وصل می‌کند. اشتباه در VIP یا Policy یا Route یک سرویس را از دسترس خارج یا بیش‌ازحد در معرض می‌گذارد.

### VIP

``` text
config firewall vip
 edit "VIP-WEB-443"
  set extintf "port1"
  set extip 203.0.113.10
  set mappedip "10.30.0.10"
  set portforward enable
  set extport 443
  set mappedport 443
 next
end
```

- **One-to-One (بدون portforward):** همه‌ی پورت‌ها به سرور داخلی؛ سطح حمله بزرگ.
- **Port-forward:** فقط پورت مشخص؛ توصیه‌شده.

### Policy ورودی

``` text
config firewall policy
 edit 40
  set name "INET-to-WEB"
  set srcintf "port1"
  set dstintf "port3"
  set srcaddr "all"
  set dstaddr "VIP-WEB-443"
  set service "HTTPS"
  set action accept
  set logtraffic all
 next
end
```

`dstaddr` باید خود VIP باشد، نه IP داخلی. VIP بدون Policy ترافیکی را عبور نمی‌دهد.

### پیش‌نیازهای شبکه

- IP عمومی VIP باید به فایروال برسد: ISP آن را Route کند یا (در یک زیرشبکه‌ی مشترک) فایروال به ARP پاسخ دهد (Proxy ARP خودکار برای VIP).
- سرور داخلی Default Gateway را فایروال داشته باشد (برگشت از فایروال).
- DNS خارجی نام را به IP عمومی ببرد.

### Hairpin

کاربر LAN با آدرس/نام عمومی سایت (https://203.0.113.10) می‌رود. ترافیک از Interface داخلی وارد و باید به DMZ برود؛ پاسخ ممکن است مستقیم به کاربر برگردد و Session ناقص بماند.

راه‌ها (ترجیحی ⇒ جایگزین):

1. **Split DNS:** نام داخلی به IP داخلی (ساده‌ترین و کم‌ریسک‌ترین).
2. VIP با `extintf any` و Policy از Interface داخلی + (در صورت لزوم) SNAT.
3. توجه: `nat-source-vip` تنظیم Hairpin نیست و برای SNAT ترافیک خروجی سرور است.

### امنیت

فقط پورت لازم؛ UTM (IPS، AV، WAF، درس 16-8)؛ DoS Policy برای VIP؛ Log کامل؛ Rate Limit؛ Patch سرور.

### مثال‌های حل‌شده

#### مثال ساده — انتشار وب

VIP-WEB-443 + Policy 40. آزمون: `curl -vk https://203.0.113.10` ⇒ 200. Session: DNAT به 10.30.0.10:443.

#### مثال متوسط — آزمون مثبت/منفی

``` text
curl -vk https://203.0.113.10        -> 200 (policy 40)
nmap -p 22,80,3389 203.0.113.10      -> filtered (only 443 exposed)
diagnose sys session list            -> dnat 203.0.113.10:443 -> 10.30.0.10:443
```

#### مثال متوسط — VIP One-to-One در برابر Port-forward

با One-to-One تمام پورت‌های سرور (مثلاً 3389) به اینترنت باز می‌شود (اگر Policy اجازه دهد). با Port-forward فقط 443. محاسبه‌ی سطح حمله: 65535 پورت در برابر 1.

#### مثال سخت — VIP بدون پاسخ

1. Policy با dst=VIP؟ (نه IP داخلی)
2. Default Gateway سرور؟
3. IP عمومی به فایروال Route می‌شود؟ (`diagnose sniffer packet port1 'host 203.0.113.10'`)
4. Debug Flow: «DNAT» دیده می‌شود؟
5. فایروال سرور (Host) 443 را می‌پذیرد؟
6. ISP/ACL بالادست؟

#### مثال سخت — Hairpin

کاربر داخلی به https://203.0.113.10 می‌رود و کار نمی‌کند. روش: Split DNS (ترجیح). اگر ممکن نبود: VIP با extintf any، Policy `ZN-USERS -> ZN-DMZ` و در صورت نیاز SNAT تا پاسخ از فایروال برگردد. آزمون: curl از LAN.

### مسیر GUI (مستندی، Unverified)

1. Policy & Objects → Virtual IPs → Create New.
2. Firewall Policy → Destination = VIP.
3. Service را روی پورت لازم محدود کنید.

### Lab هدایت‌شده (اجرا نشده)

1. VIP و Policy بسازید.
2. آزمون مثبت/منفی با curl/nmap.
3. Policy با IP داخلی بنویسید و خطا را ببینید.
4. Hairpin و Split DNS.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| VIP کار نمی‌کند | Policy dst | VIP |
| پاسخ برنمی‌گردد | GW سرور | تنظیم |
| IP عمومی نمی‌رسد | Route ISP | هماهنگی |
| Hairpin | هم‌شبکه | Split DNS |

### جمع‌بندی

VIP آدرس عمومی را DNAT می‌کند؛ Port-forward امن‌تر از One-to-One است. Policy باید به VIP اشاره کند؛ Route/GW برگشت لازم است. Hairpin با Split DNS حل می‌شود.

### تمرین و ارزیابی

**ت1.** (ساده) VIP چیست؟ *(پاسخ: 13-3-ت1)*

**ت2.** (ساده) Policy باید به چه مقصدی اشاره کند؟ *(پاسخ: 13-3-ت2)*

**ت3.** (متوسط) چرا Port Forward امن‌تر است؟ *(پاسخ: 13-3-ت3)*

**ت4.** (متوسط) علت Hairpin؟ *(پاسخ: 13-3-ت4)*

**ت5.** (سخت) VIP کار نمی‌کند؛ مراحل بررسی. *(پاسخ: 13-3-ت5)*

**ت6.** (سخت، طراحی) انتشار سه سرویس. *(پاسخ: 13-3-ت6)*

**Q1.** Quick quiz (English): Why must the policy destination reference the VIP object? *(پاسخ: 13-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VIP | Virtual IP | آدرس مجازی |
| DNAT | Destination NAT | ترجمه‌ی مقصد |

- *Publish only the required port.* ← فقط پورت لازم را منتشر کنید.

### کارت Lab

**کارت Lab:** VIP (اجرا نشده). **Evidence:** `02-design/fgt-vip.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Virtual IPs

<a id="l-13-4"></a>

## درس 13-4 — Session Table: ساختار، Timeout، فیلتر و پاک‌سازی

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۱-۷، ۱۳-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ساختار Session Table و فیلدهای مهم `session list` را بخوانید.
2. Timeout و expire را تفسیر کنید.
3. با `session filter` Sessionهای خاص را پیدا و پاک کنید.
4. علت «Policy را حذف کردم ولی کار می‌کند» را توضیح دهید.
5. تعداد Session و نشت را پایش کنید.
6. Offload و Session را مرتبط بفهمید.

### چرا باید یاد بگیریم؟

Session نشان می‌دهد «در این لحظه چه چیزی باز است». بسیاری از رفتارهای عجیب (تغییر Policy اثر نمی‌کند، مسیر قدیمی می‌ماند، اتصال بعد از ساعت‌ها قطع می‌شود) با دیدن Session روشن می‌شود. Session Table مثل دفتر نگهبان است: هر ورودی یک اتصال فعال.

### خواندن Session

``` text
session info: proto=6 proto_state=01 duration=35 expire=3565 timeout=3600 flags=00000000
statistic(bytes/packets/allow_err): org=5320/42/1 reply=48200/55/1 tuples=2
orgin->sink: org pre->post, reply pre->post dev=5->3/3->5 gwy=198.51.100.1/10.10.0.5
hook=post dir=org act=snat 10.10.0.5:40000->203.0.113.10:443(198.51.100.2:40000)
hook=pre  dir=reply act=dnat 203.0.113.10:443->198.51.100.2:40000(10.10.0.5:40000)
policy_id=10 auth_info=0 chk_client_info=0 vd=0
```

| فیلد | معنی |
|---|---|
| proto=6 | TCP (17=UDP، 1=ICMP) |
| proto_state=01 | حالت (01 = Established) |
| duration | عمر (ثانیه) |
| expire / timeout | زمان باقی‌مانده / Timeout کل |
| org / reply | بایت/بسته رفت و برگشت |
| act=snat/dnat | ترجمه‌ها (قبل و بعد) |
| policy_id | Policy مجازکننده |
| dev | Interface ورودی/خروجی |

### فیلتر و پاک‌سازی

``` text
diagnose sys session filter clear
diagnose sys session filter src 10.10.0.5
diagnose sys session filter dport 443
diagnose sys session list
diagnose sys session clear
diagnose sys session filter clear
diagnose sys session stat
diagnose sys session full-stat
```

**هشدار:** `clear` بدون فیلتر همه‌ی Sessionها را می‌بندد.

### Timeout

مقدار سراسری TCP ۳۶۰۰ ثانیه (پیش‌فرض)؛ UDP حدود ۶۰ ثانیه. Timeout هر Service/Policy می‌تواند آن را بازنویسی کند؛ برای SSH طولانی یا برنامه‌ی ویژه:

``` text
config system session-ttl
 config port
  edit 22
   set protocol 6
   set timeout 14400
  next
 end
end
```

### Session و تغییر Policy

Session موجود *معمولاً* با تغییر Policy/Route خودبه‌خود عوض نمی‌شود و تا انقضا یا پاک‌سازی همان می‌ماند؛ ولی این یک قاعده‌ی مطلق نیست (به نسخه، Offload، Inspection Mode و تنظیمات Route-change وابسته است؛ جزئیات نسخه‌ای نیازمند بررسی در مستند). پس پس از تغییر، آزمون را با اتصال **جدید** انجام دهید، یا Session‌های مربوط را با فیلتر پاک کنید.

### نشت و پایش

`diagnose sys session stat` تعداد کل/جدید/رد‌شده. روند افزایش بی‌انقطاع ⇒ نشت (DoS، Timeout طولانی، UDP بی‌پایان). بررسی Top مبدأ: `diagnose sys session list | grep ...` یا Log.

### مثال‌های حل‌شده

#### مثال ساده — خواندن

از Session بالا: TCP، Established، ۳۵ ثانیه عمر، Policy 10، SNAT به 198.51.100.2:40000، ۴۲ بسته رفت و ۵۵ بسته برگشت.

#### مثال متوسط — حذف Policy ولی کار می‌کند

FTP (Policy 5) را حذف کردید ولی کاربری هنوز FTP دارد.

``` text
diagnose sys session filter dport 21
diagnose sys session list     -> policy_id=5, expire=3200
diagnose sys session clear
diagnose sys session filter clear
```

پس از پاک‌سازی اتصال جدید رد و Log `policyid=90`.

#### مثال متوسط — محاسبه‌ی Timeout

``` text
expire 3565 s of timeout 3600 -> 35 s since last packet
```

#### مثال سخت — نشت Session

`session stat` تعداد 120,000 (ظرفیت 200,000) و رو به رشد. بررسی: ۱) Top مبدأ ۲) UDP DNS به 8.8.8.8 از یک کلاینت (۳۰ هزار Session؛ DoS ناخواسته/بدافزار) ۳) Timeout UDP ۴) DoS Policy `udp_flood`. اقدام: مهار کلاینت، Policy، و پایش. شاهد: کاهش Session.

#### مثال سخت — SSH قطع می‌شود

SSH بعد از ۱ ساعت بی‌کاری قطع می‌شود: Timeout ۳۶۰۰. راه: Keepalive یا `session-ttl` برای پورت 22 (۴ ساعت) با CHG. شاهد: expire جدید.

### مسیر GUI (مستندی، Unverified)

1. Dashboard → FortiView Sessions (یا Monitor → Firewall User/Session).
2. فیلتر و Kill Session در GUI.

### Lab هدایت‌شده (اجرا نشده)

1. یک اتصال بسازید و Session را بخوانید.
2. Policy را حذف و Session را مشاهده؛ سپس Clear با فیلتر.
3. `session-ttl` سفارشی.
4. نشت آزمایشی UDP و `stat`.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| تغییر بی‌اثر | Session قدیم | Clear با فیلتر |
| قطع بعد از ساعت | Timeout | Keepalive/ttl |
| Session زیاد | DoS/UDP | بررسی/Policy |
| clear همه | بی‌فیلتر | فیلتر |

### جمع‌بندی

Session رکورد اتصال است: حالت، Timeout، NAT، Policy و شمارنده. تغییر Policy معمولاً Session موجود را فوراً عوض نمی‌کند (وابسته به نسخه/حالت)؛ برای اطمینان با فیلتر پاک کنید و با اتصال جدید آزمون بزنید. Timeout و نشت را پایش کنید.

### تمرین و ارزیابی

**ت1.** (ساده) proto=6 یعنی؟ *(پاسخ: 13-4-ت1)*

**ت2.** (ساده) چرا clear فیلترشده؟ *(پاسخ: 13-4-ت2)*

**ت3.** (متوسط) Policy حذف شد ولی ترافیک می‌گذرد؛ چرا؟ *(پاسخ: 13-4-ت3)*

**ت4.** (متوسط) timeout پیش‌فرض TCP؟ *(پاسخ: 13-4-ت4)*

**ت5.** (سخت) SSH قطع می‌شود. *(پاسخ: 13-4-ت5)*

**ت6.** (سخت، طراحی) جدول timeout سازمان. *(پاسخ: 13-4-ت6)*

**Q1.** Quick quiz (English): Why should a session filter be set before running clear? *(پاسخ: 13-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| TTL | Time To Live | زمان زنده‌ماندن |
| NPU | Network Processing Unit | پردازنده‌ی شبکه |

- *Never clear all sessions in production.* ← هرگز همه‌ی Sessionها را در Production پاک نکنید.

### کارت Lab

**کارت Lab:** Session (اجرا نشده). **Evidence:** `03-ops/session-notes.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Session table
- FortiOS 7.0 CLI: diagnose sys session

<a id="l-13-5"></a>

## درس 13-5 — مدیریت Policy در طول زمان: Shadow، Overlap، Hit Count، Schedule و بازبینی فصلی

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۱، ۱۳-۴ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Shadow، Overlap، تکراری و Policy بی‌استفاده را تشخیص دهید.
2. Hit Count را درست تفسیر کنید و محدودیت‌های آن را بدانید.
3. Policy را به‌صورت ایمن (Disable، مشاهده، حذف) پاک‌سازی کنید.
4. Policy بیش‌ازحد باز (ALL) را تدریجی تنگ کنید.
5. گزارش ممیز بنویسید و بازبینی فصلی برنامه‌ریزی کنید.
6. Comment و مالک را الزامی کنید.

### چرا باید یاد بگیریم؟

Policy مثل لباس‌های کمد جمع می‌شود: ۸۰ تا ۸۰۰ Policy که کسی نمی‌داند چرا هستند. هر Policy اضافه یعنی سطح حمله، پیچیدگی عیب‌یابی و ریسک تغییر. ممیزان (Audit) دقیقاً همین را می‌پرسند: «چه کسی مالک این Policy است؟ چرا باز است؟ آخرین استفاده چه زمانی بود؟». بازبینی دوره‌ای مثل مرتب‌کردن کمد است: لازم، ولی باید با احتیاط انجام شود تا لباس مهمی دور ریخته نشود.

### مشکلات رایج

| مشکل | معنی | خطر |
|---|---|---|
| Shadow | Policy هرگز اجرا نمی‌شود چون بالاتر همه را می‌گیرد | بی‌فایده، گمراه‌کننده |
| Overlap | دو Policy ترافیک مشترک دارند | رفتار غیرمنتظره |
| تکراری | دو Policy یکسان | نگهداری |
| بی‌استفاده | Hit=0 | سطح حمله |
| بیش‌ازحد باز | ALL/ALL | ریسک امنیتی |
| بی‌Log | `logtraffic disable` | کوری در حادثه |
| بی‌مالک | بدون comment | ممیزی |

### Hit Count

`Hit Count` تعداد دفعات تطبیق و «آخرین استفاده». ابزار تشخیص بی‌استفاده. محدودیت‌ها:

- با Reset شمارنده یا Reboot (در بعضی نسخه‌ها) صفر می‌شود.
- استفاده‌ی **فصلی** (پایان سال مالی) را در بازه‌ی کوتاه نمی‌بیند.
- پس Log ۱۲ ماهه را هم بررسی کنید.

``` text
diagnose firewall iprope show 100004 <policyid>   (model/version dependent)
```

### روش ایمن پاک‌سازی

``` text
1 Backup + Hash
2 Classify (A: hit 0 & old, B: ALL, C: no log, D: duplicate/shadow)
3 Ask owners (ticket/email) for class A
4 Disable (not delete) approved ones
5 Observe 2 weeks (deny logs, user complaints)
6 Delete after sign-off
7 Report
```

### تنگ‌کردن Policy بیش‌ازحد باز

1. Log ۳۰ روزه روی Policy ALL (`logtraffic all`).
2. فهرست مقصد/سرویس‌های واقعی.
3. Policy خاص برای هر جریان بالاتر از ALL.
4. ALL را Disable.
5. مشاهده؛ سپس حذف.

### گزارش ممیز

| ID | نام | مالک | دلیل | Hit | ریسک | تصمیم |
|---|---|---|---|---|---|---|
| 47 | LEGACY-FTP | NOC | پروژه‌ی تمام‌شده | 0 | متوسط | حذف |
| 55 | USERS-ALL | IT | تنگ‌سازی | 1.2M | بالا | جایگزینی |

### مثال‌های حل‌شده

#### مثال ساده — طبقه‌بندی

Export: ۸۰ Policy؛ ۱۲ با Hit=0؛ ۳ ALL؛ ۵ بی‌Log؛ ۴ تکراری. فهرست کار: A=12، B=3، C=5، D=4.

#### مثال متوسط — اجرای ایمن

مالکان: ۹ مورد حذف تأیید؛ ۳ مورد (فصلی) باقی. Disable ۹ مورد ⇒ دو هفته مشاهده‌ی Deny Log؛ هیچ شکایتی ⇒ حذف. ثبت: CHG-120.

#### مثال متوسط — شناسایی Shadow

``` text
Policy 20: USERS -> any ALL accept (Hit 1.2M)
Policy 30: USERS -> SRV HTTPS accept (Hit 0)
```

30 Shadow است. رفع: جابه‌جایی 30 قبل از 20 یا حذف 30.

#### مثال سخت — تنگ‌کردن ALL

Policy `USERS-ALL` همه‌ی ترافیک را مجاز می‌کند. Log ۳۰ روزه: مقصدها: ۱۴ سرور داخلی، اینترنت (443/80/53)، یک سرویس ناشناخته (tcp/8080 به 10.60.0.5). اقدام: ۱) Policyهای خاص ۲) تماس با مالک 10.60.0.5 ۳) ALL غیرفعال ۴) مشاهده ۱ هفته ۵) حذف. اگر برنامه‌ی فصلی شکست خورد، Rollback (Enable).

#### مثال سخت — Hit Count گمراه‌کننده

Policy «YEAR-END-REPORT» Hit=0 در ۶ ماه؛ حذف شد؛ پایان سال گزارش مالی قطع. درس: Log ۱۲ ماهه و پرسش از مالک؛ برچسب «فصلی» در comment.

### مسیر GUI (مستندی، Unverified)

1. Policy & Objects → Firewall Policy؛ ستون‌ها: Hit Count، Last Used، Bytes را فعال کنید.
2. روی Policy راست‌کلیک → Show Matching Logs.
3. Disable با Status toggle.
4. Schedules: Policy & Objects → Schedules.

### Lab هدایت‌شده (اجرا نشده)

1. Export Policy و طبقه‌بندی.
2. Shadow عمدی و تشخیص.
3. Disable/مشاهده/حذف.
4. گزارش ممیز.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| حذف و قطع | استفاده‌ی فصلی | Disable اول |
| Policy بی‌مالک | comment نیست | ثبت |
| Shadow | ترتیب | مرتب |
| Hit عجیب | Reset | Log |

### جمع‌بندی

بازبینی دوره‌ای: Shadow، Overlap، بی‌استفاده، ALL، بی‌Log. Disable قبل از حذف، مالک و comment، Log ۱۲ ماهه. گزارش ممیز شفاف.

### تمرین و ارزیابی

**ت1.** (ساده) Shadowed Policy چیست؟ *(پاسخ: 13-5-ت1)*

**ت2.** (ساده) چرا Hit Count به‌تنهایی کافی نیست؟ *(پاسخ: 13-5-ت2)*

**ت3.** (متوسط) Schedule تمام شد؛ Session باز چه می‌شود؟ *(پاسخ: 13-5-ت3)*

**ت4.** (متوسط) چرا ابتدا غیرفعال و بعد حذف؟ *(پاسخ: 13-5-ت4)*

**ت5.** (سخت) Policy ALL کاربران→سرورها را تنگ کنید. *(پاسخ: 13-5-ت5)*

**ت6.** (سخت، طراحی) فرایند بازبینی فصلی ۴ هفته‌ای با گزارش. *(پاسخ: 13-5-ت6)*

**Q1.** Quick quiz (English): Why is it safer to disable a policy before deleting it? *(پاسخ: 13-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Shadowed | Shadowed policy | Policy پنهان‌شده |
| Owner | Policy owner | مالک Policy |

- *Review policies quarterly with the business owner.* ← Policyها را فصلی با مالک کسب‌وکار بازبینی کنید.

### کارت Lab

**کارت Lab:** بازبینی Policy (اجرا نشده). **Evidence:** `03-ops/policy-review.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies; Schedules
- NIST SP 800-41 Rev.1 §4.4

<a id="l-13-6"></a>

## درس 13-6 — سناریوهای خرابی Policy/NAT/Route، روش ۱۰ گامی و آزمون G5

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۱ تا ۱۳-۵، ۱۴-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. سه خانواده‌ی خرابی (Policy، NAT، Route/RPF) را تمایز دهید.
2. روش ده‌گامی عیب‌یابی را اجرا کنید.
3. هر خانواده را با Lookup، Session و Debug Flow اثبات کنید.
4. RCA بنویسید.
5. آزمون G5 را با Rubric بشناسید.
6. دو خرابی هم‌زمان را یکی‌یکی رفع کنید.

### چرا باید یاد بگیریم؟

بیشتر خرابی‌های فایروال در سه خانواده‌اند: Policy (مجوز)، NAT (ترجمه)، Route (مسیر). تشخیص «کدام خانواده» نصف کار است. مثل پزشکی که ابتدا می‌پرسد «قلب؟ ریه؟ معده؟» و سپس آزمایش مناسب را درخواست می‌کند. G5 این مهارت را با سه خرابی تزریقی می‌سنجد.

### روش ده‌گامی

1. **علامت:** دقیق (چه، کی، برای چه کسی).
2. **Scope:** یک نفر یا همه؟
3. **Route:** `get router info routing-table details <dst>`.
4. **Policy:** `diagnose firewall iprope lookup ...`.
5. **NAT:** Session (snat/dnat)؛ Pool.
6. **Session:** `diagnose sys session filter ...`.
7. **DNS:** نام درست حل می‌شود؟
8. **MTU:** ping با DF.
9. **Wire:** Sniffer + Debug Flow.
10. **تأیید:** آزمون مثبت و منفی.

### نشانه‌های هر خانواده

| نشانه | خانواده |
|---|---|
| `policy 0` در Lookup/Debug | Policy |
| Session SNAT ولی SYN بی‌پاسخ | NAT/بالادست |
| `reverse path check fail` | Route/RPF |
| `no route to host` | Route |
| فقط بعضی کاربران | Policy منبع/Address |

### سه پرونده‌ی کامل

**پرونده ۱ — Policy:** «کاربران به پورتال داخلی نمی‌رسند». Lookup: `10.10.0.5 → 10.20.0.30:443` ⇒ policy 0. بررسی: Policy 15 با srcintf=port5 (پس از Migration عوض شده). رفع: srcintf=ZN-USERS. تأیید: Lookup ⇒ policy 15؛ `curl -vk https://10.20.0.30` ⇒ 200.

**پرونده ۲ — NAT:** «نیمی از سایت‌ها باز نمی‌شود». Session: SNAT به 203.0.113.21؛ پاسخ نمی‌آید. علت: IP Pool که ISP Route نکرده. رفع: IP درست یا Interface Address. تأیید: Sniffer پاسخ برمی‌گردد.

**پرونده ۳ — Route/RPF:** «پس از افزودن لینک دوم Sessionها قطع می‌شوند». Debug: `reverse path check fail, drop`. Route به مبدأ از port3 در حالی که بسته از port4 آمده. رفع: Route برگشت/Policy Route. تأیید: Debug Flow Allowed.

### قالب RCA

``` text
Title   : Users cannot reach portal 2026-11-27
Impact  : 60 users, 12 min
Cause   : policy 15 srcintf wrong after migration
Fix     : srcintf corrected
Prevent : pre/post-change lookup test list, review of migrated policies
```

### مثال‌های حل‌شده

#### مثال ساده — Lookup

``` text
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.30 443 tcp port2
 -> policy 0 (deny)
```

Policy نیست/Interface نامنطبق. با بررسی GUI: Policy 15 با port5.

#### مثال متوسط — جدا کردن NAT از Route

Sniffer port1: SYN با Src SNAT خروجی؛ SYN-ACK نمی‌آید. نتیجه: Route و Policy و NAT درست؛ مشکل بالادست (Pool/ISP). تأیید: ping از IP Pool به 8.8.8.8 (`execute ping-options source`).

#### مثال متوسط — RPF

Debug `reverse path check fail`. `get router info routing-table details 10.10.0.5` ⇒ via port3؛ بسته از port4. رفع: Route یا Interface صحیح.

#### مثال سخت — دو خرابی هم‌زمان

Policy اشتباه + Route ناقص. اگر هر دو را هم‌زمان تغییر دهید، نمی‌دانید کدام اثر داشت. روش: ۱) ابتدا Route؛ آزمون ۲) سپس Policy؛ آزمون ۳) ثبت. بعد از هر رفع Lookup/Session تازه.

#### مثال سخت — آزمون G5

سه خرابی تزریقی؛ برای هرکدام: Evidence (Lookup/Debug/Session)، علت، رفع، آزمون منفی. **Rubric:** کشف ۳۰، رفع ۳۰، Evidence ۲۰، آزمون ۱۰، صداقت ۱۰.

### Lab هدایت‌شده (اجرا نشده)

1. سه خرابی را بسازید.
2. ده‌گامی را اجرا و Evidence جمع کنید.
3. RCA بنویسید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| policy 0 | Policy | Interface/Address |
| SYN بی‌پاسخ | NAT/بالادست | Pool/ISP |
| RPF fail | Route | تصحیح |
| چند خطا | هم‌زمان | یکی‌یکی |

### جمع‌بندی

سه خانواده: Policy، NAT، Route. ده‌گامی علامت تا تأیید. هر خرابی Evidence و RCA می‌خواهد؛ یک رفع در هر زمان.

### تمرین و ارزیابی

**ت1.** (ساده) اولین گام عیب‌یابی؟ *(پاسخ: 13-6-ت1)*

**ت2.** (ساده) no reply یعنی؟ *(پاسخ: 13-6-ت2)*

**ت3.** (متوسط) RPF fail چیست؟ *(پاسخ: 13-6-ت3)*

**ت4.** (متوسط) چرا یک تغییر هر بار؟ *(پاسخ: 13-6-ت4)*

**ت5.** (سخت) دو عیب هم‌زمان را چگونه جدا می‌کنید؟ *(پاسخ: 13-6-ت5)*

**ت6.** (سخت، طراحی) قالب گزارش حادثه. *(پاسخ: 13-6-ت6)*

**Q1.** Quick quiz (English): Which tool shows the policy that would match a given flow? *(پاسخ: 13-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RCA | Root Cause Analysis | تحلیل ریشه‌ای |

- *Change one variable at a time.* ← هر بار فقط یک متغیر را تغییر دهید.

### کارت Lab

**کارت Lab:** G5 (اجرا نشده). **Evidence:** `03-ops/rca-fgt-1.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Troubleshooting

## درس 13-7 — Session، تغییر Policy/Route و NAT در برابر Routing: چرا «تنظیم را عوض کردم ولی اثر نکرد»؟

**فصل ۱۳ · درس افزوده (تکمیل ۱۳-۶) · پیش‌نیاز: ۱۲-۰، ۱۱-۷، ۱۳-۱ تا ۱۳-۶ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3، `Unverified` روی Image):** رفتارها از مستند Fortinet و دانش عملیاتی است؛ نام دقیق پارامترها با CLI Reference 7.0 تطبیق داده شود. Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. شش علت «تنظیم را عوض کردم ولی اثر نکرد» را بشناسید.
2. فرق نقش Route و NAT (Interface در برابر IP) را بدانید.
3. اثر Session، Offload، DNS/ARP Cache را بفهمید.
4. روش آزمون صحیح پس از تغییر را اجرا کنید.
5. Distance/Priority و `routing-table database` را بخوانید.
6. Central NAT را در این زمینه بشناسید.

### چرا باید یاد بگیریم؟

«تنظیم را عوض کردم ولی اثر نکرد» پرتکرارترین شکایت است. علت‌ها محدودند و قابل‌فهرست‌اند؛ اگر بدانید، به‌جای تغییر بیشتر (و خراب‌تر) علت را پیدا می‌کنید. مثل کلید که می‌چرخانید و ماشین روشن نمی‌شود: اول چک می‌کنید باتری یا دنده، نه اینکه موتور را باز کنید.

### شش علت

1. **Session قدیمی** معمولاً مسیر/Policy/NAT ثبت‌شده‌ی قبلی را نگه می‌دارد (فرض: Session برقرار و Offload/Route-change خاصی در کار نیست؛ رفتار دقیق وابسته به نسخه است).
2. **Shadow:** Policy بالاتر ترافیک را می‌گیرد.
3. **Route بهتر** هنوز فعال است (Distance/Priority).
4. **Central NAT** فعال و تنظیم NAT Policy بی‌اثر.
5. **Offload (NPU):** Sessionهای شتاب‌داده.
6. **Cache:** DNS/ARP/مرورگر.

### نقش Route و NAT

Route **Interface/Next-hop** را تعیین می‌کند؛ NAT فقط **آدرس** را عوض می‌کند. اگر Pool B تنظیم شد ولی خروج هنوز از Interface A است، باید Route/Policy Route عوض شود. بالعکس، تغییر Route بدون NAT متناسب پاسخ را برنمی‌گرداند.

### چه زمانی تغییر بر Session موجود اثر می‌گذارد؟ (استدلال، نه حفظ‌کردن)

برای پاسخ باید پرسید «Session چه چیزی را ذخیره کرده و آن چیز وابسته به چه تغییری است؟»:

| تغییر | وابستگی Session | اثر محتمل | فرض/محدودیت |
|---|---|---|---|
| حذف/Disable Policy | Policy ID ذخیره‌شده | ممکن است Session ادامه یابد یا نسخه/حالت‌بسته قطعش کند | وابسته به نسخه؛ با Session List تأیید شود |
| تغییر Route (Gateway/Interface) | Interface خروجی/NAT ثبت‌شده | اگر Route-check/بازبینی Session فعال نباشد Session قدیمی می‌ماند؛ ممکن است قطع شود چون مقصد پاسخ را به IP قدیم می‌فرستد | نام و رفتار گزینه‌ها نیازمند بررسی |
| تغییر NAT (Pool) | IP ترجمه‌شده ذخیره‌شده | Session قدیمی با IP قدیم؛ Session جدید با Pool جدید | معمولاً قطعی |
| تغییر Profile UTM | Profile هنگام ایجاد Session | Sessionهای موجود ممکن است Profile قدیم را نگه دارند | وابسته به Flow/Proxy |
| Session Offload | وضعیت در NPU | تغییر نرم‌افزاری ممکن است دیرتر دیده شود | وابسته به مدل |

نتیجه‌ی روشی: (۱) «خودکار اثر می‌کند» و «هرگز اثر نمی‌کند» هر دو ادعای مطلق‌اند؛ (۲) آزمون با **اتصال جدید** و مشاهده‌ی Policy ID/NAT در Session؛ (۳) فقط در صورت لزوم و با فیلتر Clear.

سؤال انتقالی: Policy مبدأ کاربران با Web Filter سخت‌گیرانه‌تر شد ولی دانلود در حال انجام ادامه دارد. سه علت محتمل و آزمون تفکیک هرکدام را بنویسید. (راهنما: Session قدیمی، Offload، Profile در Flow-based.)

### روش آزمون صحیح پس از تغییر

1. اتصال **جدید** (نه Session قدیمی).
2. `iprope lookup` برای پیش‌بینی.
3. `session list` برای تأیید Policy/NAT.
4. Log.
5. اگر لازم، Clear با فیلتر.

### بررسی Route

``` text
get router info routing-table all
get router info routing-table database
get router info routing-table details 198.51.100.8
```

`all` فعال‌ها؛ `database` همه‌ی Routeها با Distance/Priority. Route جدید با Distance بیشتر فعال نمی‌شود چون قدیمی بهتر است.

### مثال‌های حل‌شده

#### مثال ساده — Session

Policy FTP حذف شد ولی کار می‌کند ⇒ `session list` (policy_id=5) ⇒ Clear با فیلتر.

#### مثال متوسط — Route

Default جدید (Distance 20) اضافه شد ولی خروج هنوز ISP قدیمی (Distance 10). `routing-table database` هر دو؛ `all` فقط قدیمی. رفع: Distance جدید کمتر یا قدیمی حذف/Priority.

#### مثال متوسط — Central NAT

Policy NAT را به Pool B تغییر دادید و بی‌اثر. `config system settings` ⇒ `central-nat enable`. رفع: `central-snat-map`.

#### مثال سخت — NAT در برابر Route

Policy NAT به Pool B (IP ISP-B) ولی ترافیک از Interface ISP-A خارج می‌شود (Route). ISP-A بسته با IP ISP-B را (Spoofed) رد می‌کند. باید Route/Policy Route هم به ISP-B بروند. اثبات: Sniffer port1 (ISP-A) بسته با Src اشتباه.

#### مثال سخت — Offload

پس از تغییر Policy بسته‌ها هنوز از Session شتاب‌داده می‌روند. `session list` ⇒ npu info؛ Clear Session برای اعمال Policy جدید.

#### مثال سخت — Cache

DNS قدیمی (TTL بالا) ⇒ کاربر هنوز IP قدیمی. `ipconfig /flushdns` و بررسی TTL؛ ARP قدیمی پس از تغییر IP/MAC ⇒ `arp -d`.

### Lab هدایت‌شده (اجرا نشده)

1. شش سناریو را بسازید و ببینید.
2. روش آزمون صحیح را تمرین کنید.
3. جدول «تغییر ← انتظار ← مشاهده».

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| بی‌اثر | Session | Clear |
| بی‌اثر | Route بهتر | Priority/Distance |
| بی‌اثر | Central NAT | map |
| NAT درست ولی خروج اشتباه | Route | Policy Route |

### جمع‌بندی

شش علت: Session، Shadow، Route بهتر، Central NAT، Offload، Cache. Route Interface را تعیین می‌کند و NAT آدرس را. آزمون با اتصال جدید و Lookup/Session.

### تمرین و ارزیابی

**ت1.** (ساده) چرا تغییر Policy روی Session موجود فوراً اثر نمی‌کند؟ *(پاسخ: 13-7-ت1)*

**ت2.** (ساده) چرا Filter قبل از Clear لازم است؟ *(پاسخ: 13-7-ت2)*

**ت3.** (متوسط) تفاوت DNAT و Routing را با مثال VIP بگویید. *(پاسخ: 13-7-ت3)*

**ت4.** (متوسط) از `act=snat` در خروجی session چه می‌فهمید؟ *(پاسخ: 13-7-ت4)*

**ت5.** (سخت) پس از Failover ISP بعضی دانلودها قفل‌اند؛ علت و راه‌حل با شواهد. *(پاسخ: 13-7-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست ۵ مرحله‌ای تغییر Policy در تولید بنویسید. *(پاسخ: 13-7-ت6)*

**م1.** Timeout پیش‌فرض TCP Established به چه قابل تنظیم است؟ *(پاسخ: 13-7-م1)*

**Q1.** Quick quiz (English): Why must you apply a filter before clearing sessions? *(پاسخ: 13-7-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Session TTL | Session time-to-live | عمر Session |
| act=snat | NAT action in session | عمل ترجمه ثبت‌شده |
| Clear | Clear session | حذف Session |
| Pickup | Session pickup | حفظ Session هنگام Failover |

- *Changing a policy does not affect established sessions until they expire or are cleared.* ← تغییر Policy تا پایان یا پاک‌شدن Session روی Sessionهای برقرار اثر ندارد.
- *Never clear all sessions in production without a change window.* ← هرگز در تولید بدون Change Window همه‌ی Sessionها را پاک نکنید.

### منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Session table، NAT؛ CLI Reference `diagnose sys session`.
- Fortinet Community: «Troubleshooting Tip: Central NAT Packet processing» (غیررسمی؛ `Unverified`).

## پاسخ‌های فصل 13

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 13-1

**13-1-ت1** — FortiGate Policyها را از بالا بررسی می‌کند و اولین Policyای که با Interface، Source، Destination، Service و Schedule جور شود اعمال می‌شود؛ بقیه بررسی نمی‌شوند.

**13-1-ت2** — در Policy باید جفت ورودی/خروجی را بنویسیم؛ ولی بسته فقط وقتی به آن Policy می‌رسد که Route همان خروجی را انتخاب کرده باشد؛ اگر Route خروجی دیگری بدهد، Policy تطابق نمی‌کند.

**13-1-ت3** — Policy 2 هرگز اجرا نمی‌شود (Shadowed). Hit Count آن صفر می‌ماند و Policy Lookup ID 3 را نشان می‌دهد؛ رفع با جابه‌جایی.

**13-1-ت4** — All Sessions شروع و پایان هر Session را ثبت می‌کند (مناسب عیب‌یابی، حجم زیاد)؛ Security Events فقط رویدادهای UTM را (حجم کم).

**13-1-ت5** — Policy A: ZN-APP→ZN-DB، Source SRV-APP، Service TCP-1433، ACCEPT، Log All. Policy پایین‌تر: ZN-USERS→ZN-DB Deny با Log. آزمون منفی: از یک کاربر telnet به 1433 ⇒ رد، و در Log action=deny و policyid Deny دیده می‌شود.

**13-1-ت6** — نام‌گذاری یکسان، Comment/Owner، ترتیب خاص→عام، Deny صریح با Log، بازبینی فصلی Hit Count ۰، حذف Policy ALL/ALL، ثبت تغییرات و Backup قبل از تغییر.

**13-1-Q1** — Because the implicit deny does not log by default, while an explicit deny creates auditable log entries.


### پاسخ‌های بازنویسی عمیق درس 13-2

**13-2-ت1** — ترجمه‌ی چند آدرس داخلی به یک آدرس عمومی با استفاده از پورت مبدأ متفاوت.

**13-2-ت2** — Overload چند Host را روی یک/چند IP اشتراکی می‌برد؛ One-to-One هر IP داخلی را به یک IP عمومی ثابت می‌نگارد.

**13-2-ت3** — حدود ۶۴۵۰۰ پورت قابل‌استفاده؛ پس حدود همین تعداد Session هم‌زمان به یک مقصد:پورت.

**13-2-ت4** — Policy NAT نادیده گرفته می‌شود و SNAT Map خالی است.

**13-2-ت5** — ۸۰۰۰۰ Session ⇒ از سقف یک IP بیشتر؛ Pool حداقل دو IP؛ ترجیحاً ۳ برای حاشیه؛ آزمون بار.

**13-2-ت6** — Central SNAT Map جدا برای هر Zone، Pool جدا، ثبت ماتریس و Log.

**13-2-Q1** — It is ignored; translation must be defined in central SNAT map entries.


### پاسخ‌های بازنویسی عمیق درس 13-3

**13-3-ت1** — ترجمه‌ی مقصد (DNAT) از IP عمومی به IP داخلی.

**13-3-ت2** — به شیء VIP.

Policy باید به شیء VIP (نه آدرس داخلی) اشاره کند، چون DNAT قبل از Policy انجام می‌شود و Policy مقصد را با VIP تطبیق می‌دهد؛ اگر آدرس داخلی بنویسید `Denied by forward policy check` می‌بینید.

**13-3-ت3** — فقط پورت‌های لازم را در معرض می‌گذارد.

Port-forward فقط پورت‌های لازم (مثلاً 443) را در معرض می‌گذارد؛ در Static NAT یک‌به‌یک همه‌ی پورت‌های سرور از اینترنت قابل‌دسترس می‌شود که سطح حمله را بزرگ می‌کند.

**13-3-ت4** — سرور و کاربر هم‌شبکه‌اند و پاسخ مستقیم می‌دهد و فایروال دور زده می‌شود.

**13-3-ت5** — Policy، Route، ARP، Session، Log، آزمون منفی.

VIP کار نمی‌کند: ۱) Policy با dst=VIP وجود دارد؟ ۲) Route سرور و Gateway آن به فایروال؟ ۳) ARP/IP عمومی روی WAN؟ ۴) Session و DNAT در `session list`. ۵) Log. ۶) آزمون منفی پورت دیگر.

**13-3-ت6** — سه VIP جدا، Policy جدا، Zone DMZ، Log، آزمون منفی.

انتشار سه سرویس: سه VIP جدا (هر کدام پورت خودش)، سه Policy با Service مشخص، سرورها در Zone DMZ، Log All و آزمون منفی (پورت غیرمجاز رد شود).

**13-3-Q1** — Because DNAT happens before policy lookup and the policy matches the VIP.


### پاسخ‌های بازنویسی عمیق درس 13-4

**13-4-ت1** — TCP.

proto=6 یعنی TCP (17 UDP و 1 ICMP). این فیلد در `session list` نوع پروتکل Session را نشان می‌دهد.

**13-4-ت2** — تا Sessionهای دیگر قطع نشوند.

`session clear` بدون فیلتر همه‌ی Sessionها را می‌بندد و قطعی سراسری می‌سازد؛ با فیلتر src/dst/port فقط Sessionهای مشخص پاک می‌شود.

**13-4-ت3** — با فرض اینکه Session برقرار است و رفتار خاصی (Route-change، Proxy-based) فعال نیست، Session معمولاً تا انقضا با Policy/NAT قدیمی می‌ماند. چون این رفتار به نسخه وابسته است، علت را با `diagnose sys session list` (Policy ID و NAT در Session) اثبات کنید، سپس با فیلتر دقیق Clear کنید و اتصال جدید را آزمون بزنید. پاک‌کردن بدون فیلتر همه‌ی کاربران را قطع می‌کند.

**13-4-ت4** — حدود ۳۶۰۰ ثانیه (طبق نسخه تأیید شود).

Timeout پیش‌فرض TCP Established حدود ۳۶۰۰ ثانیه است، ولی مقدار دقیق بسته به نسخه فرق دارد؛ با `get system session-ttl` تأیید شود (`Unverified` تا Lab).

**13-4-ت5** — timeout پورت 22 افزایش یا Keepalive.

SSH Admin قطع می‌شود چون Timeout Session کوتاه است؛ راه: timeout پورت 22 را در `session-ttl` افزایش دهید یا Keepalive در کلاینت (`ServerAliveInterval`) تنظیم کنید.

**13-4-ت6** — سرویس، پورت، timeout و دلیل.

جدول Timeout سازمان: سرویس، پورت، Timeout و دلیل (مثلاً SSH Admin: 22: 7200: بیکاری طولانی)؛ همه‌ی تغییرات با CHG ثبت شود.

**13-4-Q1** — Without a filter all sessions are cleared causing an outage.


### پاسخ‌های بازنویسی عمیق درس 13-5


### پاسخ‌های بازنویسی عمیق درس 13-5

**13-5-ت1** — Policyای که هرگز اجرا نمی‌شود چون Policy بالاتر همه‌ی ترافیک آن را می‌گیرد. مثلاً ALL بالای HTTPS.

**13-5-ت2** — با Reboot/Reset صفر می‌شود و استفاده‌ی فصلی را نمی‌بیند؛ باید با Log تاریخی و مالک تأیید شود.

Hit Count با Reboot/Reset صفر می‌شود و استفاده‌ی فصلی (مثلاً پایان سال مالی) را نمی‌بیند؛ پس قبل از حذف با Log تاریخی ۱۲ ماهه و تأیید مالک بررسی شود.

**13-5-ت3** — تا انقضا یا پاک‌سازی می‌ماند؛ برای قطع فوری Session را با فیلتر پاک کنید.

پس از پایان Schedule، Sessionهای موجود تا انقضا باقی می‌مانند و فقط Sessionهای جدید رد می‌شوند؛ برای قطع فوری Session را با فیلتر پاک کنید.

**13-5-ت4** — برای Rollback سریع اگر سرویس مخفی وابسته باشد.

ابتدا غیرفعال و بعد حذف: اگر سرویس مخفی به Policy وابسته باشد، با فعال‌کردن دوباره Rollback سریع می‌شود؛ حذف نیازمند بازگرداندن از Backup است.

**13-5-ت5** — Log ۱۴–۳۰ روز، استخراج مقصد/پورت، Policy خاص بالای ALL، غیرفعال‌سازی ALL، مشاهده، حذف؛ همراه Backup و Rollback.

**13-5-ت6** — Export، تأیید مالک، Window با Backup، مشاهده/حذف؛ گزارش: ID، مالک، دلیل، Hit، ریسک، تصمیم.

فرایند فصلی: Export Policy و Hit، تأیید مالک، Window با Backup، مشاهده و حذف؛ گزارش شامل ID، مالک، دلیل، Hit، ریسک و تصمیم است.

**13-5-Q1** — Disabling allows quick rollback if an unknown dependency appears.


### پاسخ‌های بازنویسی عمیق درس 13-6

**13-6-ت1** — تعریف دقیق علامت.

اولین گام تعریف دقیق علامت است: چه کسی، به چه سرویسی، از کجا، از کی و چه پیامی می‌بیند؛ سپس Route و بقیه‌ی گام‌ها.

**13-6-ت2** — پاسخ برنگشته؛ SNAT/Route/سرور.

no reply یعنی Session ساخته شده ولی پاسخ برنگشته: SNAT اشتباه، Route برگشت یا سرور پاسخ نمی‌دهد؛ با Sniffer دو سمت مشخص می‌شود.

**13-6-ت3** — Route معکوس مبدأ از Interface ورودی نیست.

RPF fail یعنی Route برگشت به مبدأ از همان Interface ورودی نیست؛ با `get router info routing-table details <src>` بررسی و Route/Asymmetric رفع شود.

**13-6-ت4** — برای دانستن اثر هر تغییر.

یک تغییر در هر بار تا بدانید کدام تغییر مشکل را حل کرد و ریشه‌ی اصلی پنهان نشود.

**13-6-ت5** — اول یکی را رفع، آزمون، سپس دومی.

دو عیب هم‌زمان: ابتدا یکی را رفع و آزمون کنید، بعد دومی؛ ثبت اثر هر تغییر در Evidence.

**13-6-ت6** — Timeline، Impact، Cause، Fix، Prevention.

قالب گزارش حادثه: Timeline، Impact، Cause، Fix و Prevention؛ هر بخش با شواهد.

**13-6-Q1** — The policy lookup (iprope lookup).

### پاسخ‌های درس افزوده‌ی 13-7 (فصل 13)

**13-7-ت1** — در مدل ساده، Policy برای بسته‌ی اول ارزیابی و نتیجه در Session ذخیره می‌شود؛ بنابراین تغییر بعدی *معمولاً* تا انقضا/Clear روی Session موجود اثر ندارد.

**13-7-ت2** — بدون Filter همه‌ی Sessionها پاک و ارتباط همه‌ی کاربران قطع می‌شود.

**13-7-ت3** — Routing مسیر را تعیین می‌کند؛ VIP/DNAT مقصد را به IP داخلی ترجمه می‌کند؛ هر دو لازم‌اند.

**13-7-ت4** — مبدأ بسته ترجمه (SNAT) شده است؛ آدرس ترجمه‌شده در پرانتز دیده می‌شود.

**13-7-ت5** — Session روی WAN قدیمی با SNAT قدیمی مانده؛ شاهد: session list؛ راه‌حل: Clear فیلترشده و تنظیم Failover/Timeout.

**13-7-ت6** — ۱) Backup؛ ۲) تغییر Policy؛ ۳) Clear فیلترشده‌ی Sessionهای مرتبط؛ ۴) آزمون مثبت/منفی؛ ۵) ثبت Evidence و Rollback.

**13-7-م1** — در Global یا Per-Policy با session-ttl (نام دقیق با CLI Reference تطبیق شود).

**13-7-Q1** — Because clearing without a filter removes every session and disconnects all users.

# فصل 14 — ابزارهای عیب‌یابی FortiOS: Sniffer، Debug Flow، Session، Routing، MTU/MSS و Log

> **یادداشت علمی v4.0 — فصل 14:** عمومی: روش علامت/شاهد/فرضیه، Sniffing. مختص محصول: `diagnose` FortiOS.
> فرض: خروجی‌ها نمونه‌ی آموزشی؛ Offload بر Sniffer اثر می‌گذارد؛ علامت ≠ علت.
> مرجع: Fortinet Docs 7.0؛ Wireshark.


**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳.
**اهداف:** چارچوب ۱۰ پرسش؛ Packet Sniffer؛ Debug Flow؛ Session/Routing/iprope؛ MTU/MSS/DNS/TCP؛ Log Analysis؛ آزمون Packet Walk.
**چرا اینجا؟** عیب‌یابی باید از همین حالا در همه‌ی فصل‌های بعد ابزار شما باشد.
**نسخه:** FortiOS 7.0.3 اسمی (آزمایش‌نشده روی Image).
**معیار تسلط:** با Sniffer و Debug Flow علت موفقیت/شکست یک ارتباط را در ≤ ۱۰ دقیقه با شواهد بگویید.
**اشتباهات رایج:** Sniffer بدون فیلتر؛ فراموشی `diagnose debug disable/reset`؛ Debug روی دستگاه شلوغ؛ نخواندن Route/Policy ID در خروجی.

**درس‌های فصل:**
- [درس 14-1 — چارچوب ۱۰ پرسش عیب‌یابی و مدل ابزارها](#l-14-1)
- [درس 14-2 — Packet Sniffer (CLI و GUI) و Wireshark](#l-14-2)
- [درس 14-3 — Debug Flow: خواندن تصمیم فایروال](#l-14-3)
- [درس 14-4 — Session، Routing و iprope: ابزارهای تکمیلی](#l-14-4)
- [درس 14-5 — MTU/MSS، DNS و مشکلات TCP/UDP](#l-14-5)
- [درس 14-6 — تحلیل Log، Packet Walk و آزمون فصل](#l-14-6)

---

<a id="l-14-1"></a>

## درس 14-1 — چارچوب ۱۰ پرسش عیب‌یابی و نقشه‌ی ابزارها

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۶، ۱۱-۳، ۱۲-۰ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ده پرسش ثابت عیب‌یابی را به ترتیب بپرسید و برای هرکدام ابزار مناسب انتخاب کنید.
2. ابزارها (ping، traceroute، sniffer، debug flow، session، routing، log) را روی نقشه‌ی مسیر بسته جای دهید.
3. از علامت مبهم «کار نمی‌کند» به فرضیه‌ی قابل‌آزمون برسید.
4. هر گام را با Evidence (خروجی دستور + زمان + فیلتر) ثبت کنید.
5. ابزارهای سنگین (debug) را ایمن به‌کار ببرید.
6. بعد از رفع، آزمون مثبت و منفی بزنید.

### چرا باید یاد بگیریم؟

پزشک خوب قبل از نسخه‌نوشتن می‌پرسد: «کجا درد دارد؟ از کی؟ چه کرده‌اید؟ تب دارید؟». سپس آزمایش مناسب می‌خواهد. پزشک بد مستقیم آنتی‌بیوتیک می‌دهد. عیب‌یاب شبکه هم همین است: مهندس تازه‌کار مستقیم `debug flow` می‌زند و در خروجی غرق می‌شود؛ مهندس ارشد اول Scope را می‌پرسد و ۸۰٪ مسیر را حذف می‌کند. چارچوب ده پرسش جلوی «حدس‌زدن» و «تغییر هم‌زمان چند چیز» را می‌گیرد و باعث می‌شود هر ساعت عیب‌یابی Evidence تولید کند.

### مفهوم پایه: چرا ترتیب مهم است؟

هر پرسش یک **فرضیه** را رد یا تأیید می‌کند. مثلاً اگر ثابت شد «بسته اصلاً به FortiGate نمی‌رسد»، دیگر Policy و NAT بی‌ربط‌اند. پرسش‌ها از «ارزان و رد‌کننده‌ی بزرگ» به «گران و جزئی» مرتب شده‌اند:

``` text
Scope  ->  L1/L2  ->  arrives?  ->  route  ->  policy  ->  NAT/session
       ->  leaves?  ->  reply?  ->  DNS/MTU/app  ->  verify
```

### ده پرسش و ابزارها

| # | پرسش | ابزار |
|---|---|---|
| 1 | دقیقاً چه چیزی، از کجا به کجا، برای چه کسی؟ | گفتگو، Ticket |
| 2 | از چه زمانی؟ چه چیزی تغییر کرد؟ | Log، CHG، Config diff |
| 3 | لایه‌ی ۱–۲ سالم است؟ | `get system interface physical`، VLAN، لینک |
| 4 | بسته به FortiGate می‌رسد؟ | sniffer ورودی |
| 5 | Route رفت و برگشت هست؟ | `get router info routing-table details` |
| 6 | Policy مطابق است؟ | `iprope lookup`، Debug Flow |
| 7 | NAT/Session درست است؟ | `diagnose sys session list` |
| 8 | بسته خارج می‌شود؟ | sniffer خروجی |
| 9 | پاسخ برمی‌گردد؟ | sniffer (مقصد به ما) |
| 10 | DNS/MTU/برنامه؟ | nslookup، ping DF، curl |

### نقشه‌ی ابزار روی مسیر بسته

``` text
 [PC] --(1)--> [port2 FGT port1] --(2)--> [ISP] --> [Server]
   ^                |  ^   |
   |                v  |   v
   |            route policy NAT session
 ping/curl      (get router) (iprope) (session list)
 traceroute        sniffer on both interfaces
```

- **ping/traceroute:** از دید کاربر؛ ولی ICMP ممکن است Policy جدا داشته باشد.
- **sniffer:** حقیقت روی سیم؛ مستقل از Policy.
- **debug flow:** تصمیم داخلی فایروال (Route، Policy، NAT).
- **session list:** وضعیت اتصال و NAT واقعی.
- **log:** تاریخچه و الگو.

### قاعده‌ی انتخاب ابزار از روی علامت

| علامت | ابزار اول | تفسیر |
|---|---|---|
| Timeout | Route، sniffer | بسته گم شده |
| Connection refused | Policy/سرویس | پاسخ RST |
| کند | MTU، CPU، Session | مشکل کیفیت |
| فقط بعضی کاربران | Policy/Address | Scope |
| فقط HTTPS | MTU، SSL Inspection | لایه‌ی بالاتر |
| بعد از تغییر | Config diff | علت زمانی |

### ایمنی ابزارهای سنگین

- `debug flow` روی ترافیک زیاد CPU را بالا می‌برد: **حتماً فیلتر** و **محدودیت تعداد**.
- همیشه پایان: `diagnose debug disable` و `diagnose debug reset`.
- sniffer با `count` محدود.
- در ساعت اوج، روی دستگاه Production فقط فیلتر باریک.

### مثال‌های حل‌شده

#### مثال ساده — ثبت Evidence

علامت: «سایت داخلی باز نمی‌شود» (فقط یک کاربر).

``` text
Q1 scope  : user 10.10.0.5 only (others ok)
Q5 route  : via port3 ok
Q6 policy : iprope lookup -> policy 0 (deny)
Cause     : user is in a new subnet not in address group
Fix       : add subnet to ADDR-USERS
Verify    : lookup -> policy 15; curl OK
```

Scope «فقط یک کاربر» فوراً Policy/Address را مشکوک کرد.

#### مثال متوسط — انتخاب ابزار

علامت: Timeout به `app.example.com`.

1. Q5 Route: وجود دارد.
2. Q6 Lookup: policy 30.
3. Q7 Session: فقط `SYN_SENT`.
4. Q8 Sniffer port1: SYN خارج، SYN-ACK نیست.
5. نتیجه: مشکل بالادست یا NAT.

Debug Flow لازم نشد؛ sniffer کافی بود.

#### مثال سخت — دو علت پشت‌سرهم

پس از رفع NAT (Pool اشتباه)، سایت باز می‌شود ولی بارگذاری فایل بزرگ قطع می‌شود. Q10 آزمون کامل شکست خورد ⇒ علت دوم MTU (PMTUD بلاک). درس: بعد از هر رفع، **آزمون کامل** (نه فقط ping)، و هر علت جدا ثبت شود.

### مسیر GUI (مستندی، Unverified)

1. Network → Diagnostics → Packet Capture.
2. Dashboard → FortiView.
3. Log & Report → Forward Traffic.

### Lab هدایت‌شده (اجرا نشده)

1. یک خرابی NAT و یک خرابی Policy بسازید.
2. ده پرسش را برای هرکدام پر کنید.
3. Evidence را در قالب جدول ثبت کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| حدس‌زدن | بی‌چارچوب | ده پرسش |
| چند تغییر هم‌زمان | بی‌انضباط | یکی‌یکی |
| بی‌Evidence | ثبت نشده | الگوی ثبت |
| CPU بالا | debug بدون فیلتر | disable/reset |

### نکات امنیتی

Debug و sniffer ممکن است داده‌ی حساس (رمز، توکن) نشان دهند؛ فایل pcap را ایمن نگه دارید و پس از پایان حذف کنید.

### جمع‌بندی

ده پرسش با ابزار مشخص؛ اول Scope، بعد پایین‌رفتن از لایه‌ها با Evidence؛ ابزار سنگین با فیلتر؛ پایان با آزمون مثبت و منفی.

### تمرین و ارزیابی

**ت1.** (ساده) چرا از لایه‌ی پایین شروع می‌کنیم؟ *(پاسخ: 14-1-ت1)*

**ت2.** (ساده) Sniffer را چرا با شمارنده می‌زنیم؟ *(پاسخ: 14-1-ت2)*

**ت3.** (متوسط) Sniffer ورودی خالی است؛ علت‌های محتمل؟ *(پاسخ: 14-1-ت3)*

**ت4.** (متوسط) تفاوت sniffer و debug flow؟ *(پاسخ: 14-1-ت4)*

**ت5.** (سخت) برخی سایت‌ها باز می‌شوند؛ مسیر عیب‌یابی؟ *(پاسخ: 14-1-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست یک‌صفحه‌ای ده‌پرسشی. *(پاسخ: 14-1-ت6)*

**Q1.** Quick quiz (English): Which tool reveals the policy and route decision made for a packet? *(پاسخ: 14-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DF | Don't Fragment | بدون تکه‌سازی |
| PMTU | Path MTU | MTU مسیر |

- *Start from the lowest layer and move up.* ← از پایین‌ترین لایه شروع کنید و بالا بروید.

### کارت Lab

**کارت Lab:** ده پرسش (اجرا نشده). **Evidence:** `03-ops/ten-questions.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Troubleshooting tools
- FortiOS 7.0 Troubleshooting guide

<a id="l-14-2"></a>

## درس 14-2 — Packet Sniffer در CLI و GUI و تحلیل pcap با Wireshark: از فیلتر تا نتیجه‌گیری

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Sniffer را در CLI و GUI با فیلتر دقیق اجرا کنید.
2. سطوح Verbosity (۱ تا ۶) را بشناسید و انتخاب کنید.
3. pcap بگیرید و در Wireshark تحلیل کنید.
4. با Sniffer ثابت کنید «بسته رسید/نرسید» و «پاسخ آمد/نیامد».
5. دو Interface (ورودی و خروجی) را مقایسه کنید.
6. NAT را روی سیم ببینید.

### چرا باید یاد بگیریم؟

Sniffer مثل دوربین مداربسته‌ی راهرو است: نه نظر می‌دهد نه تفسیر؛ فقط نشان می‌دهد چه کسی از کجا رد شد. وقتی Policy و Route را درست می‌دانید و باز هم کار نمی‌کند، تنها حقیقت مستقل روی سیم است. عبارت مشهور مهندسان: «Packet capture doesn't lie».

### دستور پایه

``` text
diagnose sniffer packet <interface|any> '<filter>' <verbosity> <count> <timestamp>
```

| پارامتر | معنی |
|---|---|
| interface | نام Interface یا any |
| filter | سینتکس BPF مثل host، port، proto |
| verbosity | ۱ تا ۶ |
| count | تعداد بسته (۰ = بی‌پایان) |
| timestamp | `a` = زمان مطلق |

### سطوح Verbosity

| سطح | نمایش |
|---|---|
| 1 | فقط سرآیند IP |
| 2 | سرآیند + payload (hex) |
| 3 | سرآیند + payload + Ethernet |
| 4 | سرآیند + نام Interface |
| 5 | سرآیند + payload + Interface |
| 6 | سرآیند + payload + Ethernet + Interface |

در عمل: **4** برای دیدن مسیر و Interface؛ **6** برای ذخیره و تبدیل به pcap.

### فیلترهای کاربردی

``` text
'host 10.10.0.5'
'host 10.10.0.5 and tcp port 443'
'src 10.10.0.5 and dst 198.51.100.8'
'icmp'
'udp port 53'
'not port 22'
```

### نمونه خروجی سطح ۴

``` text
diagnose sniffer packet any 'host 198.51.100.8 and tcp port 443' 4 20 a
2026-11-27 10:15:01.100 port2 in  10.10.0.5.50000 -> 198.51.100.8.443: syn
2026-11-27 10:15:01.101 port1 out 203.0.113.2.50000 -> 198.51.100.8.443: syn
```

دو چیز دیده می‌شود: ورود روی port2 با IP داخلی و **خروج روی port1 با IP عمومی** (NAT). اگر خط دوم نبود، بسته در FortiGate گم شده؛ اگر SYN-ACK نیامد، مشکل بالادست است.

### pcap و Wireshark

1. در CLI با سطح 6 اجرا و خروجی را در فایل متنی ذخیره کنید.
2. با اسکریپت `fgt2eth.pl` (ابزار Fortinet) به pcap تبدیل کنید یا از GUI: Network > Packet Capture.
3. در Wireshark: `tcp.analysis.retransmission`، `tcp.flags.syn==1`، `ip.addr==...`.

### Packet Capture در GUI

GUI: Network > Packet Capture ⇒ Interface، فیلتر، تعداد ⇒ Start ⇒ Download pcap. مزیت: سنگین نیست و مستقیم pcap می‌دهد.

### خواندن الگوها

| الگو | معنی |
|---|---|
| SYN بدون SYN-ACK | مقصد/بالادست بلاک |
| SYN ⇒ RST | سرویس بسته |
| SYN ورودی ولی خروجی نیست | Policy/Route در FGT |
| تکرار SYN | Retransmission، گم‌شدن |
| ICMP frag needed | MTU |

### مثال‌های حل‌شده

#### مثال ساده — بسته می‌رسد؟

دستور: `diagnose sniffer packet port2 'host 10.10.0.5 and icmp' 4 5 a`. اگر ICMP Echo دیده شد، بسته به FortiGate رسیده؛ اگر نه، مشکل پیش از FGT (کابل/VLAN/Switch).

#### مثال متوسط — SYN بدون جواب

``` text
port2 in  10.10.0.5.50000 -> 198.51.100.8.443: syn
port1 out 203.0.113.2.50000 -> 198.51.100.8.443: syn
(no syn-ack)
```

FGT درست عمل کرد؛ مشکل بالادست (ISP/مقصد بلاک یا Pool مسیر نشده). اقدام: Ticket با این Evidence.

#### مثال متوسط — SYN خارج نمی‌شود

port2 SYN دیده شد، port1 هیچ. پس FGT بسته را گم کرده: Policy deny یا Route ⇒ حالا Debug Flow (درس بعد).

#### مثال سخت — MTU با Sniffer

``` text
port1 in  198.51.100.8 > 203.0.113.2: icmp: 198.51.100.8 unreachable - need to frag (mtu 1400)
```

مقصد/میانی PMTUD پیام داده؛ اگر این پیام به کلاینت نرسد (Policy ICMP) اتصال‌های بزرگ گیر می‌کنند. رفع: اجازه‌ی ICMP یا Clamp MSS.

#### مثال سخت — مقایسه‌ی دو Interface

برای NAT: ورودی بسته با Src داخلی، خروجی با Src Pool. اگر خروجی هنوز Src داخلی است، NAT اعمال نشده (Policy بدون NAT یا Central NAT).

### مسیر GUI (مستندی، Unverified)

1. Network → Diagnostics → Packet Capture → Create New.
2. Interface، Filter، Count را بنویسید؛ Start؛ Download.

### Lab هدایت‌شده (اجرا نشده)

1. ping از PC و Sniffer در دو Interface.
2. ساخت Deny و دیدن نبود بسته‌ی خروجی.
3. ذخیره pcap و بازکردن در Wireshark.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| خروجی خالی | فیلتر اشتباه | ساده‌تر |
| همه‌چیز می‌بینید | بی‌فیلتر | host/port |
| بسته دیده نمی‌شود | Offload | موقتاً unset offload (آزمایشی) |
| CPU بالا | بی‌count | count |

### نکات امنیتی

Sniffer ترافیک رمزنشده را آشکار می‌کند؛ دسترسی را به Admin محدود و pcap را حذف کنید.

### جمع‌بندی

Sniffer حقیقت روی سیم است: فیلتر دقیق، Verbosity 4 برای مسیر، دو Interface، الگوها (SYN بدون پاسخ، RST، frag needed)، و pcap برای Wireshark.

### تمرین و ارزیابی

**ت1.** (ساده) verbosity 4 چه نشان می‌دهد؟ *(پاسخ: 14-2-ت1)*

**ت2.** (ساده) count چیست؟ *(پاسخ: 14-2-ت2)*

**ت3.** (متوسط) SYN بدون SYN-ACK یعنی؟ *(پاسخ: 14-2-ت3)*

**ت4.** (متوسط) چرا Offload اثر دارد؟ *(پاسخ: 14-2-ت4)*

**ت5.** (سخت) Asymmetric را با Sniffer ثابت کنید. *(پاسخ: 14-2-ت5)*

**ت6.** (سخت، طراحی) روش Capture امن. *(پاسخ: 14-2-ت6)*

**Q1.** Quick quiz (English): Which sniffer verbosity includes the interface name? *(پاسخ: 14-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| BPF | Berkeley Packet Filter | فیلتر بسته |
| pcap | Packet capture file | فایل Capture |

- *Capture with a narrow filter.* ← با فیلتر محدود Capture کنید.

### کارت Lab

**کارت Lab:** Sniffer (اجرا نشده). **Evidence:** `03-ops/sniffer-notes.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Packet capture
- Wireshark User Guide

<a id="l-14-3"></a>

## درس 14-3 — Debug Flow: خواندن تصمیم فایروال خط‌به‌خط با مثال‌های Allowed، Denied و RPF

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۱، ۱۴-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Debug Flow را با فیلتر و محدودیت ایمن اجرا کنید.
2. خروجی را خط‌به‌خط بخوانید (Route، Policy، NAT).
3. سه نتیجه‌ی Allowed، Denied، RPF را تشخیص دهید.
4. پیام‌های مهم و معنی آن‌ها را بشناسید.
5. دستورهای پایان‌دادن را بدانید.
6. با Sniffer و Session ترکیب کنید.

### چرا باید یاد بگیریم؟

Sniffer می‌گوید «بسته رسید و نرفت»؛ Debug Flow می‌گوید **چرا**. مثل دیدن گزارش داور بعد از اینکه می‌بینید گل رد شد. بدون آن، مجبورید حدس بزنید. با آن، یک خط مثل `no matching policy` یا `reverse path check fail` علت را مستقیم می‌دهد.

### راه‌اندازی

``` text
diagnose debug reset
diagnose debug flow filter clear
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow filter dport 443
diagnose debug flow show function-name enable
diagnose debug console timestamp enable
diagnose debug flow trace start 20
diagnose debug enable
# ... reproduce ...
diagnose debug disable
diagnose debug reset
```

`trace start 20` فقط ۲۰ بسته را ردیابی می‌کند (ایمنی).

### پیام‌های مهم

| پیام | معنی |
|---|---|
| `vd-root received a packet` | ورود بسته |
| `find a route: gw-... via ...` | Route پیدا شد |
| `no route` / `Denied: failed to find route` | Route نیست |
| `Allowed by Policy-N` | Policy مجاز |
| `Denied by forward policy check (policy 0)` | Policy نیست |
| `reverse path check fail, drop` | RPF |
| `SNAT ...` | ترجمه‌ی مبدأ |
| `DNAT ...` | ترجمه‌ی مقصد |
| `iprope_in_check() check failed` | رد شدن در ورودی خود FGT |

### سه نتیجه‌ی متفاوت

**Allowed:**

``` text
id=20085 trace_id=1 msg="vd-root received a packet(proto=6, 10.10.0.5:50000->198.51.100.8:443) from port2."
id=20085 trace_id=1 msg="allocate a new session-00001a2b"
id=20085 trace_id=1 msg="find a route: flag=00000000 gw-203.0.113.1 via port1"
id=20085 trace_id=1 msg="Allowed by Policy-30: SNAT"
id=20085 trace_id=1 msg="SNAT 10.10.0.5->203.0.113.2:50000"
```

**Denied (policy):**

``` text
msg="Denied by forward policy check (policy 0)"
```

**RPF:**

``` text
msg="reverse path check fail, drop"
```

### روش تفسیر

1. ورود: از کدام Interface (درست است؟).
2. Route: gw و خروجی.
3. Policy: شماره/Deny.
4. NAT: چه ترجمه‌ای.
5. پایان: Allowed یا Drop.

### مثال‌های حل‌شده

#### مثال ساده — Allowed

خطوط بالا: ورود port2، Route از port1، Policy 30 با SNAT. نتیجه: FortiGate سالم است؛ مشکل بعد از آن (بالادست) ⇒ Sniffer SYN-ACK.

#### مثال متوسط — Denied

`Denied by forward policy check (policy 0)`. بررسی: ورود از port5 (نه ZN-USERS). رفع: افزودن Interface به Zone/Policy. پس از رفع Debug تازه: `Allowed by Policy-15`.

#### مثال متوسط — No route

`Denied: failed to find route`. `get router info routing-table details 198.51.100.8` ⇒ خالی. رفع: Default Route یا Static. تأیید: Debug ⇒ `find a route`.

#### مثال سخت — RPF

لینک دوم اضافه شد؛ Sessionها قطع. Debug: `reverse path check fail`. Route به مبدأ از port3؛ بسته از port4. رفع: Route برگشت صحیح یا Policy Route/ `set src-check disable` (فقط موقت و با ریسک).

#### مثال سخت — SNAT ناخواسته

`Allowed by Policy-12: SNAT` ولی انتظار NAT نبود (ترافیک بین Zoneهای داخلی). رفع: `set nat disable`. نکته: Debug قبل از تغییر اثبات می‌کند.

### Lab هدایت‌شده (اجرا نشده)

1. سه حالت را بسازید.
2. Debug را با فیلتر اجرا و پایان دهید.
3. پیام‌ها را جدول کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| خروجی نیست | فیلتر/enable | مرور |
| خروجی طوفانی | بی‌فیلتر | filter و count |
| trace قطع نمی‌شود | disable نشده | reset |
| تغییر Offload | session شتاب | clear session |

### نکات امنیتی

Debug را روی Production با فیلتر باریک و زمان کوتاه اجرا کنید؛ در پایان حتماً disable/reset.

### جمع‌بندی

Debug Flow: ورود، Route، Policy، NAT. سه نتیجه Allowed/Denied/RPF؛ پیام‌ها علت را مستقیم می‌گویند؛ همیشه فیلتر، count و پایان.

### تمرین و ارزیابی

**ت1.** (ساده) trace start 20 چه می‌کند؟ *(پاسخ: 14-3-ت1)*

**ت2.** (ساده) Allowed by Policy-2 یعنی؟ *(پاسخ: 14-3-ت2)*

**ت3.** (متوسط) policy 0 یعنی؟ *(پاسخ: 14-3-ت3)*

**ت4.** (متوسط) RPF fail چیست؟ *(پاسخ: 14-3-ت4)*

**ت5.** (سخت) RPF را رفع کنید. *(پاسخ: 14-3-ت5)*

**ت6.** (سخت، طراحی) الگوی ثبت Debug. *(پاسخ: 14-3-ت6)*

**Q1.** Quick quiz (English): What does "reverse path check fail" indicate? *(پاسخ: 14-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | مسیر معکوس |

- *Always disable debug when finished.* ← پس از اتمام Debug را خاموش کنید.

### کارت Lab

**کارت Lab:** Debug flow (اجرا نشده). **Evidence:** `03-ops/debug-flow.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Debug flow
- FortiOS 7.0 Troubleshooting guide

<a id="l-14-4"></a>

## درس 14-4 — Session، Routing و iprope: ابزارهای تکمیلی برای اثبات تصمیم‌ها

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۱ تا ۱۴-۳ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. `diagnose sys session list` را با فیلتر بخوانید (state، proto_state، NAT).
2. جدول Routing را با سه دستور (all، database، details) بررسی کنید.
3. `iprope lookup` را برای پیش‌بینی Policy به‌کار ببرید.
4. Session، Route و Policy را برای اثبات یک تصمیم ترکیب کنید.
5. Session را با فیلتر ایمن پاک کنید.
6. `get router info kernel` و Policy Route را بشناسید.

### چرا باید یاد بگیریم؟

Sniffer «بسته‌ها» را نشان می‌دهد و Debug Flow «تصمیم لحظه‌ای» را؛ ولی **وضعیت پایدار** (چه Sessionهایی باز است، چه Routeی فعال است، کدام Policy برنده می‌شود) را سه دستور دیگر می‌دهند. مثل پزشکی که علاوه بر نوار قلب، پرونده‌ی پزشکی و آزمایش خون هم می‌بیند. این سه ابزار ارزان و بی‌خطرند و اغلب بدون هیچ debugی علت را نشان می‌دهند.

### Session list

``` text
diagnose sys session filter clear
diagnose sys session filter src 10.10.0.5
diagnose sys session filter dst 198.51.100.8
diagnose sys session filter dport 443
diagnose sys session list
```

نمونه:

``` text
session info: proto=6 proto_state=01 duration=35 expire=3565 timeout=3600
state=may_dirty npu
statistic(bytes/packets/allow_err): org=1540/12/1 reply=9800/11/1
orgin->sink: org pre->post, reply pre->post dev=5->3/3->5 gwy=203.0.113.1/10.10.0.5
hook=post dir=org act=snat 10.10.0.5:50000->198.51.100.8:443(203.0.113.2:50000)
hook=pre dir=reply act=dnat 198.51.100.8:443->203.0.113.2:50000(10.10.0.5:50000)
policy_id=30 auth_info=0 chk_client_info=0 vd=0
```

| فیلد | معنی |
|---|---|
| proto/proto_state | TCP و وضعیت (01=established) |
| timeout/expire | زمان باقی‌مانده |
| act=snat | ترجمه‌ی مبدأ |
| policy_id | Policy تطبیق‌خورده |
| dev=5->3 | Interface ورودی و خروجی (index) |
| npu | شتاب‌داده‌شده |

### Routing

``` text
get router info routing-table all
get router info routing-table database
get router info routing-table details 198.51.100.8
get router info kernel
```

- `all`: Routeهای فعال.
- `database`: همه‌ی Routeها با Distance/Priority (حتی غیرفعال).
- `details <ip>`: Route برنده برای یک مقصد.
- `kernel`: FIB واقعی که Kernel استفاده می‌کند.

### iprope lookup

``` text
diagnose firewall iprope lookup 10.10.0.5 50000 198.51.100.8 443 tcp port2
```

پیش‌بینی می‌کند چه Policyی تطبیق می‌خورد؛ بدون ایجاد ترافیک واقعی. پارامتر آخر Interface ورودی است.

### ترکیب سه ابزار

``` text
Route   -> egress interface (port1)
Policy  -> policy 30 (srcintf->dstintf pair)
Session -> actual NAT & state
```

اگر سه مورد با هم سازگار باشند و باز هم کار نکند، مشکل خارج از FGT است.

### پاک‌کردن Session

``` text
diagnose sys session filter src 10.10.0.5
diagnose sys session clear
diagnose sys session filter clear
```

هشدار: بدون فیلتر، `clear` **همه‌ی** Sessionها را پاک می‌کند و قطعی ایجاد می‌شود.

### مثال‌های حل‌شده

#### مثال ساده — Session باز؟

`filter dst 198.51.100.8` و `list`: `proto_state=01` یعنی Established؛ اتصال برقرار. `proto_state=02` (SYN_SENT) یعنی پاسخی نیامده.

#### مثال متوسط — Policy و NAT واقعی

Session ⇒ `policy_id=30 act=snat ...(203.0.113.2)`. با این Evidence ثابت می‌شود چه Policyی و چه IPی ترجمه کرده؛ حدس لازم نیست.

#### مثال متوسط — Route بهتر

Default جدید اضافه شد ولی ترافیک از مسیر قدیمی می‌رود. `routing-table database` هر دو را نشان می‌دهد؛ `all` فقط قدیمی (Distance کمتر). رفع: Priority/Distance.

#### مثال سخت — Session قدیمی

Policy عوض شد ولی کاربر هنوز با قانون قدیمی کار می‌کند. Session: `policy_id=5` (قدیمی). رفع: `session filter` ⇒ `clear` فقط برای همان کاربر.

#### مثال سخت — Offload

`npu` در Session: ترافیک شتاب‌داده؛ Sniffer ممکن است همه‌ی بسته‌ها را نشان ندهد. برای آزمون: Session را پاک و موقت Offload را محدود کنید (آزمایشی).

### مسیر GUI (مستندی، Unverified)

1. Monitor → Routing Monitor.
2. Network → Policy Routes.

### Lab هدایت‌شده (اجرا نشده)

1. اتصال بزنید و Session را بخوانید.
2. Route دوم اضافه و database/all را مقایسه کنید.
3. Lookup قبل و بعد از تغییر Policy.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Session نیست | بسته نرسیده/Deny | Sniffer/Debug |
| SYN_SENT | پاسخ نیامده | بالادست |
| Policy قدیمی | Session قدیمی | clear با فیلتر |
| Route نامنتظره | Distance | database |

### نکات امنیتی

پاک‌کردن Session کاربران را قطع می‌کند؛ با فیلتر و در پنجره‌ی مجاز. Sessionها اطلاعات IP و ترافیک را نشان می‌دهند؛ دسترسی محدود.

### جمع‌بندی

Session، Routing و iprope سه ابزار بی‌خطر برای اثبات Policy، NAT و Route‌اند؛ ترکیب آن‌ها بسیاری از خرابی‌ها را بدون debug حل می‌کند.

### تمرین و ارزیابی

**ت1.** (ساده) routing-table database چیست؟ *(پاسخ: 14-4-ت1)*

**ت2.** (ساده) ARP incomplete؟ *(پاسخ: 14-4-ت2)*

**ت3.** (متوسط) Policy Route قبل یا بعد از جدول مسیر؟ *(پاسخ: 14-4-ت3)*

**ت4.** (متوسط) iprope lookup؟ *(پاسخ: 14-4-ت4)*

**ت5.** (سخت) ترافیک از ISP اشتباه می‌رود. *(پاسخ: 14-4-ت5)*

**ت6.** (سخت، طراحی) پرونده‌ی شواهد. *(پاسخ: 14-4-ت6)*

**Q1.** Quick quiz (English): Which command lists policy routes? *(پاسخ: 14-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ARP | Address Resolution Protocol | تبدیل IP به MAC |

- *Prove each decision with evidence.* ← هر تصمیم را با شواهد ثابت کنید.

### کارت Lab

**کارت Lab:** ابزارهای تکمیلی (اجرا نشده). **Evidence:** `03-ops/full-picture.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Routing monitor
- FortiOS 7.0 CLI Reference: get router info

<a id="l-14-5"></a>

## درس 14-5 — MTU/MSS، DNS و مشکلات TCP/UDP: عیب‌یابی «نیمه‌کارکرده» با محاسبه و آزمون پایدار

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۵، ۱۴-۱، ۱۴-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. MTU و MSS را تعریف و رابطه‌ی آن‌ها را محاسبه کنید.
2. علائم «نیمه‌کارکرده» (ping بله، فایل بزرگ نه) را تشخیص دهید.
3. با `ping -f -l` (Windows) یا `ping -M do -s` (Linux) MTU مسیر را پیدا کنید.
4. TCP MSS Clamp را روی FortiGate تنظیم کنید.
5. DNS را از چهار زاویه عیب‌یابی کنید.
6. تفاوت مشکلات TCP و UDP را بشناسید.

### چرا باید یاد بگیریم؟

یکی از آزاردهنده‌ترین خرابی‌ها: «ping جواب می‌دهد، سایت باز می‌شود ولی فایل بزرگ یا ایمیل با پیوست قطع می‌شود». علت اغلب MTU است. مثل جاده‌ای که تنها کامیون‌های کوچک را رد می‌کند: ماشین‌های سبک (ping) رد می‌شوند ولی کامیون (بسته‌ی بزرگ) گیر می‌کند. DNS هم «تلفن‌چی» شبکه است؛ اگر خراب باشد، همه‌چیز «اینترنت قطع است» به نظر می‌رسد در حالی که IPها کار می‌کنند.

### MTU و MSS

| اصطلاح | معنی |
|---|---|
| MTU (Maximum Transmission Unit) | بزرگ‌ترین اندازه‌ی بسته‌ی IP در یک لینک (معمولاً ۱۵۰۰) |
| MSS (Maximum Segment Size) | بزرگ‌ترین payload TCP |
| PMTUD | کشف MTU مسیر با ICMP |

``` text
MSS = MTU - IP header (20) - TCP header (20)
MSS = 1500 - 20 - 20 = 1460
```

با تونل (IPsec حدود ۷۰–۷۵ بایت overhead):

``` text
Effective MTU = 1500 - 73 = 1427 (approx)
MSS           = 1427 - 40 = 1387
```

### چرا PMTUD گاهی شکست می‌خورد؟

بسته‌ی بزرگ با بیت DF (Don't Fragment) فرستاده می‌شود؛ مسیر کوچک‌تر ICMP «Fragmentation needed» برمی‌گرداند؛ اگر Firewall این ICMP را بلاک کند، فرستنده هرگز نمی‌فهمد ⇒ اتصال گیر می‌کند (Black hole).

### یافتن MTU مسیر

``` text
Windows: ping -f -l 1472 198.51.100.8
Linux  : ping -M do -s 1472 198.51.100.8
```

1472 + 28 (ICMP+IP) = 1500. اگر شکست خورد، کم کنید (1452، 1400 ...) تا موفق شود؛ MTU = عدد موفق + 28.

### راه‌حل: MSS Clamp

``` text
config firewall policy
    edit 30
        set tcp-mss-sender 1360
        set tcp-mss-receiver 1360
    next
end
```

یا روی Interface: `set tcp-mss 1360`. این کار MSS را در SYN تنظیم می‌کند تا بسته‌ها از ابتدا کوچک باشند.

### DNS — چهار زاویه

| زاویه | آزمون |
|---|---|
| Resolver کاربر | `nslookup name 10.20.0.53` |
| DNS خود FGT | `execute ping name` |
| مسیر DNS | UDP/53 و TCP/53 در Policy |
| پاسخ بزرگ | TCP/53 یا EDNS |

### TCP در برابر UDP

- TCP: Handshake، Retransmission؛ علامت: Timeout/RST.
- UDP: بی‌اتصال؛ علامت: بی‌پاسخ ساکت؛ Session کوتاه (UDP timeout).
- DNS روی UDP؛ پاسخ بزرگ ⇒ TCP.

### مثال‌های حل‌شده

#### مثال ساده — محاسبه‌ی MSS

Ethernet: MTU 1500 ⇒ MSS 1460 (بلوک بالا).

#### مثال متوسط — یافتن MTU مسیر

ping 1472 DF ⇒ «Packet needs to be fragmented». 1452 ⇒ شکست. 1400 ⇒ موفق. 1420 ⇒ موفق؛ 1430 ⇒ شکست. حداکثر موفق 1420 ⇒ MTU = 1420 + 28 = 1448 (محاسبه در بلوک).

``` text
Path MTU = 1420 + 28 = 1448
MSS      = 1448 - 40  = 1408
```

#### مثال متوسط — DNS

نام باز نمی‌شود ولی IP باز می‌شود. `nslookup` به DNS داخلی ⇒ Timeout. Policy UDP/53 به DNS Server وجود نداشت. رفع: افزودن سرویس DNS. تأیید: nslookup جواب.

#### مثال سخت — فایل بزرگ و IPsec

Site-to-Site: وب سبک باز می‌شود، دانلود ۵۰MB قطع. IPsec overhead ⇒ MTU موثر ۱۴۲۷؛ ICMP frag بلاک. رفع: MSS Clamp 1360 روی Policy تونل. تأیید: دانلود کامل و Sniffer: SYN با `mss 1360`.

#### مثال سخت — DNS بزرگ

پاسخ DNSSEC بزرگ (>512 بایت) روی UDP قطع می‌شود؛ fallback TCP/53 بلاک. رفع: TCP/53 مجاز.

### Lab هدایت‌شده (اجرا نشده)

1. MTU مسیر را با ping DF پیدا کنید.
2. MSS Clamp بگذارید و SYN را در Sniffer ببینید.
3. DNS را از چهار زاویه آزمون کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| فایل بزرگ قطع | MTU/PMTUD | Clamp/ICMP |
| نام نه، IP بله | DNS | Policy/Resolver |
| UDP بی‌جواب | Policy/Session | سرویس |
| فقط HTTPS کند | MTU/Inspection | Clamp |

### نکات امنیتی

ICMP را کامل بلاک نکنید؛ نوع 3 کد 4 را مجاز کنید. DNS را فقط به Resolverهای مجاز اجازه دهید.

### جمع‌بندی

MTU/MSS با فرمول؛ علامت نیمه‌کارکرده نشانه‌ی MTU؛ آزمون ping DF؛ Clamp؛ DNS از چهار زاویه؛ TCP و UDP علائم متفاوت دارند.

### تمرین و ارزیابی

**ت1.** (ساده) MSS برای MTU 1400؟ *(پاسخ: 14-5-ت1)*

**ت2.** (ساده) علامت Black-hole؟ *(پاسخ: 14-5-ت2)*

**ت3.** (متوسط) ping IP ok ولی نام no؟ *(پاسخ: 14-5-ت3)*

**ت4.** (متوسط) چرا ICMP لازم است؟ *(پاسخ: 14-5-ت4)*

**ت5.** (سخت) IPsec دانلود می‌ایستد. *(پاسخ: 14-5-ت5)*

**ت6.** (سخت، طراحی) آزمون پایدار. *(پاسخ: 14-5-ت6)*

**Q1.** Quick quiz (English): How do you measure path MTU with ping? *(پاسخ: 14-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| MSS | Maximum Segment Size | حداکثر قطعه |

- *Lower the MSS on tunnels.* ← MSS را روی تونل‌ها کاهش دهید.

### کارت Lab

**کارت Lab:** MTU/DNS (اجرا نشده). **Evidence:** `03-ops/mtu-mss.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Troubleshooting
- RFC 1191

<a id="l-14-6"></a>

## درس 14-6 — تحلیل Log، Packet Walk و آزمون عملی فصل ۱۴: سه پرونده‌ی کامل

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۱ تا ۱۴-۵ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Log ترافیک را برای یافتن الگو فیلتر و تفسیر کنید.
2. Packet Walk را برای یک جریان کامل (داخل → اینترنت) بنویسید.
3. سه پرونده‌ی کامل را با روش ده‌پرسشی حل کنید.
4. Evidence را در جدول ثبت کنید.
5. RCA کوتاه بنویسید.
6. آزمون عملی فصل را بشناسید.

### چرا باید یاد بگیریم؟

عیب‌یابی یعنی ترکیب همه‌ی ابزارها روی یک پرونده. مثل خلبانی که همه‌ی ابزارها را در شرایط واقعی تمرین می‌کند. در این درس سه پرونده‌ی کامل از علامت تا رفع حل می‌شود تا مهارت در عمل جا بیفتد.

### Log ترافیک

GUI: Log & Report > Forward Traffic. فیلدهای مهم: Source، Destination، Policy ID، Action، Result، Sent/Received.

| Action | معنی |
|---|---|
| accept | مجاز |
| deny | رد با Policy |
| close/timeout | پایان Session |
| ip-conn | Session بدون پاسخ |

CLI: `execute log filter category 0`، `execute log filter field dstip 198.51.100.8`، `execute log display`.

### Packet Walk

``` text
1 PC 10.10.0.5 -> DNS 10.20.0.53 (UDP 53)  resolve name
2 PC -> default gateway (ARP)
3 FGT port2 receives SYN (Sniffer in)
4 Route lookup -> port1
5 Policy lookup -> policy 30
6 SNAT 10.10.0.5 -> 203.0.113.2
7 Session created
8 SYN leaves port1 (Sniffer out)
9 SYN-ACK returns, reverse NAT
10 ACK ... data
```

### پرونده ۱ — کاربران به اینترنت نمی‌رسند

1. Scope: همه.
2. L1/L2: port2 up.
3. Sniffer port2: ICMP از PC دیده می‌شود.
4. Route: Default حذف شده (CHG دیروز).
5. Debug: `Denied: failed to find route`.
6. رفع: Default برگشت؛ تأیید: ping، curl.
7. RCA: Static Route اشتباهی حذف شد؛ Change با Peer Review.

### پرونده ۲ — فقط HTTPS کند

1. HTTP سریع، HTTPS کند.
2. Sniffer: `ICMP need to frag`.
3. MTU مسیر ۱۴۴۸؛ Clamp وجود ندارد.
4. رفع: Clamp 1360.
5. تأیید: سرعت و `mss 1360` در SYN.

### پرونده ۳ — یک سرور از اینترنت

1. VIP + Policy وجود دارد.
2. Lookup خارجی: policy 0.
3. علت: Policy از port1 به DMZ ولی Interface مقصد اشتباه (port4).
4. رفع: dstintf DMZ؛ تأیید: Debug `DNAT` و Session.

### قالب Evidence

| گام | دستور | خروجی کلیدی | نتیجه |
|---|---|---|---|
| Route | `routing-table details` | no route | علت |
| Debug | `debug flow` | Denied route | تأیید |
| رفع | Default Route | via port1 | حل |
| Verify | `curl` | 200 | تأیید |

### مثال‌های حل‌شده

#### مثال ساده — خواندن Log

Log: `srcip=10.10.0.5 dstip=198.51.100.8 policyid=30 action=accept sent=1.2KB rcvd=0`. rcvd=0 یعنی پاسخی نیامده ⇒ بالادست.

#### مثال متوسط — الگوی زمانی

خرابی هر شب ۲:۰۰. Log: `action=deny policyid=0` از ۱:۵۹. بررسی: Script پشتیبان Policy را موقت Disable می‌کند. رفع: اصلاح Script.

#### مثال سخت — پرونده‌ی ترکیبی

علامت: «اپلیکیشن کند و گاهی قطع». یافته‌ها: ۱) Route درست ۲) Session `SYN_SENT` تکراری ۳) Sniffer: Retransmission ۴) ICMP frag. دو علت: MTU و پایداری لینک ISP. هر کدام جدا رفع و ثبت.

### آزمون عملی فصل

سه خرابی تزریقی؛ ده پرسش، Evidence، رفع، RCA. معیار: Evidence ۳۰، رفع ۳۰، روش ۲۰، RCA ۲۰.

### Lab هدایت‌شده (اجرا نشده)

1. سه پرونده را بسازید.
2. جدول Evidence را کامل کنید.
3. RCA بنویسید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Log خالی | logtraffic disable | all |
| Log زیاد | بی‌فیلتر | فیلتر |
| زمان‌نامنطبق | NTP | همگام‌سازی |

### جمع‌بندی

Log الگو می‌دهد، Packet Walk مسیر را می‌گوید، و سه پرونده نشان می‌دهد ترکیب ابزارها و ثبت Evidence چگونه به رفع می‌رسد.

### تمرین و ارزیابی

**ت1.** (ساده) policyid=0 یعنی؟ *(پاسخ: 14-6-ت1)*

**ت2.** (ساده) rcvdbyte=0 یعنی؟ *(پاسخ: 14-6-ت2)*

**ت3.** (متوسط) چرا Log نیست؟ *(پاسخ: 14-6-ت3)*

**ت4.** (متوسط) Packet Walk را از Log بسازید. *(پاسخ: 14-6-ت4)*

**ت5.** (سخت) سه پرونده را حل کنید. *(پاسخ: 14-6-ت5)*

**ت6.** (سخت، طراحی) الگوی گزارش. *(پاسخ: 14-6-ت6)*

**Q1.** Quick quiz (English): What does policyid=0 mean in a traffic log? *(پاسخ: 14-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Log | Traffic log | لاگ ترافیک |

- *Logs explain what happened in the past.* ← Log گذشته را توضیح می‌دهد.

### کارت Lab

**کارت Lab:** آزمون ۱۴ (اجرا نشده). **Evidence:** `03-ops/walk-arch2.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Log & Report

### ضمیمه: پرونده‌ی کامل حل‌شده — خواندن Log تا Packet Walk

**ورودی:** کاربر 10.10.0.5 به پورتال 10.20.0.30:443 نمی‌رسد. Log:

``` text
srcip=10.10.0.5 srcintf="port2" dstip=10.20.0.30 dstport=443 dstintf="port3" policyid=0 action="deny"
```

**گام ۱ — تفسیر:** policyid=0 و action=deny ⇒ Implicit Deny؛ هیچ Policy مطابق نیست.

**گام ۲ — Lookup:**

``` text
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.30 443 tcp port2
```

نتیجه: policy 0. بررسی: Policy موجود Users→Servers فقط TCP-8443 است.

**گام ۳ — رفع:** افزودن 443 به Service یا Policy جدید با Service HTTPS؛ Log All.

**گام ۴ — Packet Walk پس از رفع:**

``` text
ingress port2 -> RPF ok -> route 10.20.0.0/24 via port3 -> policy 62 accept -> egress port3
```

**گام ۵ — آزمون:** `curl -vk https://10.20.0.30` ⇒ 200؛ Log: action=accept policyid=62؛ آزمون منفی SSH ⇒ Deny.

**درس:** Log اثبات می‌کند چه شد؛ Lookup نشان می‌دهد چرا.

## درس 14-7 — روش نظام‌مند عیب‌یابی: از علامت تا علت و رفع (با پرونده‌های واقعی)

**فصل ۱۴ · درس افزوده (تکمیل ۱۴-۶) · پیش‌نیاز: ۱۲-۰، ۱۲-۸، ۱۳-۷، ۵-۰ · ≈ ۸ ساعت**

> **وضعیت:** روش مستقل از برند + دستورهای FortiOS 7.0.3 (`Unverified` روی Image). خروجی‌ها نمونه‌ی آموزشی‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. روش نظام‌مند (علامت → فرضیه → آزمون → رفع → تأیید) را اجرا کنید.
2. الگوی «Divide and Conquer» را روی مسیر بسته به‌کار ببرید.
3. Baseline و Change را برای عیب‌یابی استفاده کنید.
4. ارتباط با تیم و مستندسازی (Ticket/RCA) را انجام دهید.
5. دام‌های رایج (Confirmation bias، تغییر هم‌زمان) را بشناسید.
6. قالب Runbook عیب‌یابی بسازید.

### چرا باید یاد بگیریم؟

ابزار بدون روش مثل جعبه‌ابزار بدون نقشه‌ی ساختمان است. روش نظام‌مند باعث می‌شود حتی در ساعت ۳ شب، با فشار مدیر، کارتان قابل‌پیش‌بینی و قابل‌ثبت باشد. همچنین نفر بعدی (یا خودتان فردا) بفهمد چه کردید.

### علامت، شاهد، فرضیه و علت اثبات‌شده — چهار چیز متفاوت

| مفهوم | تعریف | مثال |
|---|---|---|
| **علامت (Symptom)** | آنچه کاربر/ابزار می‌بیند | «سایت باز نمی‌شود»، Timeout |
| **شاهد (Evidence)** | خروجی قابل‌تکرار با زمان و دستور | Sniffer: SYN بدون SYN-ACK |
| **فرضیه (Hypothesis)** | علتی که با شاهد سازگار است | NAT اشتباه، Route برگشت، فیلتر بالادست |
| **علت اثبات‌شده (Proven cause)** | فرضیه‌ای که آزمایش آن را تأیید و فرضیه‌های رقیب را رد کرده | تغییر X نتیجه را بر می‌گرداند و بازگرداندنش دوباره خراب می‌کند |

**چرا یک علامت علت یکتا ندارد؟** «Timeout» با ده فرضیه سازگار است (Route، Policy، NAT، MTU، سرور، ISP، DNS، Asymmetric، RPF، Session). نسبت‌دادن مستقیم علامت به علت (مثلاً «Timeout یعنی ISP») خطای مفهومی رایج است.

**روش تفکیک فرضیه‌ها (استدلال نظری):**
1. هر فرضیه یک **پیش‌بینی قابل‌آزمون** تولید می‌کند (اگر NAT خراب است، Sniffer خروجی Src اشتباه نشان می‌دهد).
2. آزمونی را اول بزنید که **فرضیه‌های زیادی را هم‌زمان رد کند** و ارزان باشد (Sniffer دو نقطه، `iprope lookup`).
3. برای هر آزمون «نتیجه‌ی مورد انتظار اگر فرضیه درست باشد» و «اگر نادرست باشد» را از قبل بنویسید تا تعصب تأیید (Confirmation Bias) کم شود.
4. علت وقتی «اثبات‌شده» است که: شاهد مستقیم دارد، فرضیه‌های رقیب رد شده‌اند، و رفع نتیجه را برمی‌گرداند (و در صورت امکان بازگرداندن رفع، علامت را برمی‌گرداند).
5. جداول «علامت ⇒ علت» در این دوره **فهرست فرضیه‌های محتمل‌اند نه حکم**؛ ستون علت را همیشه «محتمل» بخوانید.

### حلقه‌ی عیب‌یابی

``` text
1 Define symptom (who/what/when)
2 Collect facts (logs, baseline, changes)
3 Hypothesize (ranked by likelihood x cost)
4 Test one hypothesis (tool -> evidence)
5 Fix (minimal change)
6 Verify (positive + negative test)
7 Document (RCA, prevent)
```

### Divide and Conquer

مسیر را نصف کنید: «بسته به FGT می‌رسد؟» اگر بله، نیمه‌ی مبدأ سالم؛ بعد «از FGT خارج می‌شود؟». هر آزمون نصف فضا را حذف می‌کند.

``` text
PC -- SW -- [FGT] -- ISP -- Server
 Q: arrives at FGT?   yes -> left half ok
 Q: leaves FGT?       yes -> FGT ok
 Q: reply returns?    no  -> right half/upstream
```

### Baseline و Change

- **Baseline:** وضعیت سالم (Config backup، Session count، CPU، Route table).
- **Change:** `execute backup`/Config diff، CHG، لیست تغییرات اخیر.
- «چه چیزی تغییر کرد؟» ارزان‌ترین پرسش با بیشترین نتیجه است.

### دام‌ها

| دام | معنی | درمان |
|---|---|---|
| Confirmation bias | فقط شواهد موافق فرضیه | آزمون رد‌کننده |
| تغییر هم‌زمان | معلوم نیست چه اثر کرد | یکی‌یکی |
| بی‌Evidence | حدس | ثبت خروجی |
| رفع موقت | علت اصلی باقی | RCA |
| عجله در Debug | CPU/نویز | فیلتر |

### ارتباط با تیم

- هر ۳۰ دقیقه به‌روزرسانی Ticket.
- جملات خروجی: «Scope، Impact، Hypothesis، Next step».
- Escalation با Evidence (نه «کار نمی‌کند»).

### قالب Runbook عیب‌یابی

``` text
Title   : Users cannot reach <service>
Scope   : who/what
Checks  : Q1..Q10 with commands
Decision: if X -> do Y
Rollback: how to undo
Owner   : team
```

### مثال‌های حل‌شده

#### مثال ساده — Divide and Conquer

PC به سرور نمی‌رسد. Sniffer port2: ICMP ورودی دیده شد. Sniffer port1: خروجی دیده شد؛ پاسخ نه. نتیجه: FGT سالم؛ مشکل در نیمه‌ی راست.

#### مثال متوسط — Change

«دیروز اینترنت کار می‌کرد». Config diff: Policy 30 `set nat disable` شده. رفع: enable. ثبت.

#### مثال متوسط — Confirmation bias

فرضیه «DNS خراب است»؛ nslookup خوب بود ولی گفت «پس DNS Cache». آزمون رد‌کننده: `ping 8.8.8.8` هم Timeout ⇒ مشکل Route نه DNS. درس: به‌دنبال شواهد مخالف باشید.

#### مثال سخت — فشار مدیریت

ساعت ۳ شب، ۲۰۰ کاربر قطع. روش: ۱) اعلام Scope/Impact ۲) Rollback آخرین Change (۵ دقیقه) ۳) پس از بازگشت سرویس، RCA بدون فشار. اصل: اول بازگردانی سرویس، بعد ریشه‌یابی.

#### مثال سخت — رفع موقت در برابر دائمی

Session پاک‌شد و کار کرد؛ ولی هر ساعت تکرار شد. RCA: Timeout پایین Session Helper. رفع دائمی: تنظیم Timeout. ثبت: Prevent با پایش.

### Lab هدایت‌شده (اجرا نشده)

1. چهار خرابی بسازید؛ حلقه‌ی هفت‌گامی را اجرا کنید.
2. Runbook بنویسید.
3. RCA کوتاه بنویسید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| هر روز تکرار | رفع موقت | RCA |
| تیم نمی‌داند | ثبت نشده | Ticket |
| Rollback ندارید | Change بی‌طرح | طرح |

### جمع‌بندی

روش نظام‌مند: علامت، حقایق، فرضیه، آزمون، رفع، تأیید، ثبت. Divide and Conquer، Baseline و Change، پرهیز از دام‌ها، و اولویت بازگردانی سرویس سپس ریشه‌یابی.

### تمرین و ارزیابی

**ت1.** (ساده) هشت مرحله‌ی عیب‌یابی را بنویسید. *(پاسخ: 14-7-ت1)*

**ت2.** (ساده) کدام ابزار نشان می‌دهد بسته به Interface رسیده؟ *(پاسخ: 14-7-ت2)*

**ت3.** (متوسط) تفاوت «علامت» و «علت» را با مثال بگویید. *(پاسخ: 14-7-ت3)*

**ت4.** (متوسط) چرا یک تغییر در هر زمان؟ *(پاسخ: 14-7-ت4)*

**ت5.** (سخت) کاربری می‌گوید نیمی از سایت‌ها کند است. فرضیه‌ها را به ترتیب بنویسید و برای هرکدام یک شاهد ارزان. *(پاسخ: 14-7-ت5)*

**ت6.** (سخت، طراحی) یک قالب RCA یک‌صفحه‌ای برای پرونده‌ی ۲ بنویسید. *(پاسخ: 14-7-ت6)*

**م1.** Confirmation bias چیست؟ *(پاسخ: 14-7-م1)*

**Q1.** Quick quiz (English): Why start with a sniffer before a debug flow? *(پاسخ: 14-7-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RCA | Root Cause Analysis | تحلیل علت ریشه‌ای |
| Hypothesis | Hypothesis | فرضیه |
| Evidence | Evidence | شاهد |
| Scope | Scope | دامنه‌ی مشکل |
| MTTR | Mean Time To Repair | میانگین زمان رفع |

- *Change one thing at a time and record the evidence.* ← هر بار یک چیز را تغییر دهید و شاهد را ثبت کنید.
- *The symptom is not the root cause.* ← علامت همان علت ریشه‌ای نیست.

### منابع

- Fortinet Docs: [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow)؛ FortiOS 7.0 Administration Guide — Troubleshooting.
- ITIL 4 — Incident and Problem Management (مفهومی).

## پاسخ‌های فصل 14

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 14-1

**14-1-ت1** — چون اگر لینک/VLAN خراب باشد بالاتر هیچ‌چیز معنا ندارد و آزمایش بیهوده است.

از لایه‌ی پایین‌تر شروع می‌کنیم چون اگر لینک/VLAN خراب باشد بالاتر هیچ‌چیز معنا ندارد؛ آزمون‌های بالاتر بی‌فایده و گمراه‌کننده می‌شود.

**14-1-ت2** — تا حجم Capture و بار CPU کنترل شود و دستگاه پر نشود.

count تعداد بسته‌ها را محدود می‌کند تا حجم Capture و CPU کنترل شود و دستگاه Production پر نشود؛ count=0 بی‌پایان و خطرناک است.

**14-1-ت3** — لینک، VLAN، فیلتر اشتباه، یا Interface نادرست. با ARP و وضعیت لینک بررسی می‌شود.

Sniffer ورودی خالی: لینک/VLAN، فیلتر اشتباه یا Interface نادرست؛ با `get system interface physical` و `diagnose ip arp list` بررسی می‌شود.

**14-1-ت4** — Sniffer بسته‌ها را می‌بیند؛ Debug flow تصمیم FortiGate (Policy، Route، NAT) را نشان می‌دهد.

Sniffer خودِ بسته‌ها را می‌بیند؛ Debug flow تصمیم FortiGate (Route، Policy، NAT، Drop) را نشان می‌دهد؛ هر دو مکمل‌اند.

**14-1-ت5** — ping، debug flow، sniffer، تست DF با اندازه‌ی مختلف، PMTU، MSS-clamp، آزمون.

برخی سایت‌ها باز می‌شوند: ping، Debug flow، Sniffer، تست DF با اندازه‌های مختلف، تعیین PMTU، MSS-clamp و آزمون دانلود بزرگ.

**14-1-ت6** — جدول پرسش/ابزار/خروجی مورد انتظار/اقدام بعدی.

چک‌لیست ده‌پرسشی: جدول پرسش، ابزار، خروجی مورد انتظار و اقدام بعدی؛ برای ثبت Evidence هر گام.

**14-1-Q1** — Debug flow.


### پاسخ‌های بازنویسی عمیق درس 14-2


### پاسخ‌های بازنویسی عمیق درس 14-2

**14-2-ت1** — هدر بسته همراه نام Interface.

verbosity 4 هدر بسته را همراه نام Interface نشان می‌دهد؛ برای دیدن اینکه بسته از کدام Interface آمده/رفته مناسب است.

**14-2-ت2** — تعداد بسته‌ها تا توقف؛ برای کنترل حجم.

count تعداد بسته تا توقف است؛ برای کنترل حجم و CPU استفاده می‌شود.

**14-2-ت3** — مقصد/مسیر پاسخ نمی‌دهد؛ با Capture ورودی/خروجی محل را مشخص کنید.

SYN بدون SYN-ACK یعنی مقصد یا مسیر پاسخ نمی‌دهد؛ Capture ورودی و خروجی محل را مشخص می‌کند.

**14-2-ت4** — بسته‌ی Offload‌شده ممکن است در sniffer دیده نشود.

بسته‌ی Offload‌شده روی NPU ممکن است در sniffer CPU دیده نشود؛ برای Lab Offload غیرفعال شود (`Unverified`).

**14-2-ت5** — Capture چند Interface، مقایسه‌ی جهت‌ها و Interfaceها.

Asymmetric: Sniffer روی چند Interface؛ SYN در یکی، SYN-ACK در دیگری؛ مقایسه‌ی جهت‌ها آن را ثابت می‌کند.

**14-2-ت6** — فیلتر باریک، count، حذف pcap، ثبت زمان/Evidence.

Capture امن: فیلتر باریک، count محدود، حذف pcap پس از تحلیل و ثبت زمان/Evidence بدون داده‌ی حساس.

**14-2-Q1** — Verbosity 4.

### پاسخ‌های بازنویسی عمیق درس 14-3


### پاسخ‌های بازنویسی عمیق درس 14-3

**14-3-ت1** — ۲۰ بسته را Trace می‌کند و سپس متوقف می‌شود.

`trace start 20` فقط ۲۰ بسته را Trace می‌کند و سپس متوقف می‌شود؛ برای محدود کردن بار.

**14-3-ت2** — Policy 2 اجازه داد و NAT طبق همان اعمال شد.

«Allowed by Policy-2» یعنی Policy 2 اجازه داد و NAT طبق همان Policy اعمال شد.

**14-3-ت3** — Implicit Deny؛ هیچ Policyای مطابق نبود.

policy 0 یعنی Implicit Deny؛ هیچ Policyای مطابق نبود؛ Interface/Zone، Src/Dst (بعد DNAT)، Service و Schedule را بررسی کنید.

**14-3-ت4** — Route معکوس Source از Interface ورودی نیست.

RPF fail یعنی Route معکوس مبدأ از Interface ورودی نیست؛ Route/Asymmetric را بررسی کنید.

**14-3-ت5** — Route را اصلاح، Asymmetric را بررسی، آزمون Allowed.

رفع RPF: Route را اصلاح کنید، Asymmetric را بررسی کنید و با Debug flow Allowed را تأیید کنید.

**14-3-ت6** — فیلتر، زمان، خروجی، تفسیر، رفع، آزمون.

الگوی ثبت Debug: فیلتر، زمان، خروجی، تفسیر، رفع و آزمون؛ بدون اطلاعات حساس.

**14-3-Q1** — The route back to the source does not use the ingress interface.

### پاسخ‌های بازنویسی عمیق درس 14-4

**14-4-ت1** — همه‌ی مسیرها حتی غیرفعال.

`routing-table database` همه‌ی مسیرها را (حتی غیرفعال) نشان می‌دهد؛ برای فهم اینکه چرا مسیر بهتر استفاده نمی‌شود.

**14-4-ت2** — لایه‌ی ۲ پاسخ نمی‌دهد.

ARP incomplete یعنی لایه‌ی ۲ پاسخ نمی‌دهد (کابل، VLAN، سوییچ).

**14-4-ت3** — قبل.

Policy Route قبل از جدول مسیر اعمال می‌شود؛ مسیر «عجیب» اغلب از آن است.

**14-4-ت4** — Policy مطابق جریان.

`iprope lookup` Policy مطابق جریان را نشان می‌دهد و شماره را برای Evidence می‌دهد.

**14-4-ت5** — proute، routing-table، رفع.

ترافیک از ISP اشتباه می‌رود: `proute list` و `routing-table`؛ حذف/اصلاح Policy Route و آزمون traceroute.

**14-4-ت6** — Route، ARP، Lookup، Session با زمان.

پرونده‌ی شواهد: خروجی Route، ARP، Lookup و Session همراه زمان.

**14-4-Q1** — diagnose firewall proute list.


### پاسخ‌های بازنویسی عمیق درس 14-5


### پاسخ‌های بازنویسی عمیق درس 14-5

**14-5-ت1** — 1360.

MSS برای MTU 1400 برابر 1360 است (MTU−40).

**14-5-ت2** — Handshake و بسته‌ی کوچک ok؛ بزرگ بی‌پاسخ.

Black-hole: Handshake و بسته‌ی کوچک ok؛ بسته‌ی بزرگ بی‌پاسخ و Retransmission.

**14-5-ت3** — DNS/Resolver/Policy 53.

ping IP ok ولی نام no: DNS/Resolver یا Policy پورت 53؛ با `nslookup` و Capture بررسی شود.

**14-5-ت4** — PMTUD برای اطلاع از MTU مسیر.

ICMP Frag-needed برای PMTUD لازم است؛ بستن آن Black-hole می‌سازد.

**14-5-ت5** — PMTU، MSS-clamp، ICMP، آزمون.

IPsec دانلود می‌ایستد: PMTU را اندازه بگیرید، MSS-clamp کنید، ICMP مجاز، آزمون دانلود بزرگ.

**14-5-ت6** — دانلود ۱۰۰MB سه بار + DNS.

آزمون پایدار: دانلود ۱۰۰MB سه بار و ۲۰ پرس‌وجوی DNS بدون خطا.

**14-5-Q1** — Use the DF bit and vary the packet size until it passes.

### پاسخ‌های بازنویسی عمیق درس 14-6


### پاسخ‌های بازنویسی عمیق درس 14-6

**14-6-ت1** — Implicit Deny.

policyid=0 یعنی Implicit Deny؛ Policy مطابق نبود.

**14-6-ت2** — پاسخی دریافت نشده.

rcvdbyte=0 یعنی هیچ پاسخی دریافت نشد؛ سرور/Route برگشت/ISP.

**14-6-ت3** — Log Policy خاموش است.

Log نیست چون `logtraffic` در Policy خاموش است؛ برای Policy مهم Log All.

**14-6-ت4** — srcintf/dstintf/policy/NAT.

Packet Walk از Log: srcintf، dstintf، policy، NAT و نتیجه.

**14-6-ت5** — Deny، rcvdbyte=0، Drop بی‌Log.

سه پرونده: Deny، rcvdbyte=0 و Drop بی‌Log؛ هر کدام Evidence Log+Flow+Sniffer.

**14-6-ت6** — Log، Flow، علت، رفع، آزمون.

الگوی گزارش: Log، Flow، علت، رفع و آزمون.

**14-6-Q1** — The implicit deny policy.

### پاسخ‌های درس افزوده‌ی 14-7 (فصل 14)

**14-7-ت1** — Symptom، Scope، Hypotheses، Evidence، Test، Root cause، Fix+Verify، Document.

**14-7-ت2** — Sniffer/Packet Capture روی Interface ورودی.

**14-7-ت3** — علامت: «Drop شد»؛ علت: RPF/Policy/Route. علامت چیزی است که می‌بینیم؛ علت چیزی که آن را توضیح می‌دهد.

**14-7-ت4** — تا بدانید کدام تغییر اثر کرده و بتوانید Rollback کنید.

**14-7-ت5** — DNS، MTU/MSS، CPU/Profile، لینک (خطا)، ISP، Policy. شاهد: nslookup/Sniffer، ping -f، sys top، خطای Interface، traceroute، Debug Flow.

**14-7-ت6** — عنوان، زمان، اثر، Timeline، شواهد (Bytes out/in، Denied policy)، علت (نبود Policy سمت مقابل)، اقدام فوری (Policy)، پیشگیری (چک‌لیست دوطرفه).

**14-7-م1** — فقط به‌دنبال شاهدی بودن که فرضیه‌ی اول را تأیید کند.

**14-7-Q1** — Because a sniffer is cheaper and tells you whether the packet arrived before you inspect policy and route behavior.

# فصل 15 — دوفایروالی با DMZ (Edge و Internal) — معماری ۲

> **یادداشت علمی v4.0 — فصل 15:** عمومی: DMZ، دوفایروالی، Double NAT. مختص محصول: FortiGate.
> فرض: آدرس‌دهی نمونه؛ NAT فقط Edge یک توصیه‌ی طراحی است نه قانون.
> مرجع: Fortinet Docs 7.0.


**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۱۴.
**اهداف:** طراحی و ساخت دو FortiGate (Edge و Internal) با DMZ (Web) و Zone سرورها (App/DB)؛ Routing بین فایروال‌ها؛ NAT در دو نقطه؛ Packet Walk در هر دو فایروال؛ عیب‌یابی؛ **Gate G6**.
**نسخه:** FortiOS 7.0.3 اسمی؛ آزمایش‌نشده. هر FortiGate به ≥ 2 GB RAM نیاز دارد (طبق Inventory).
**معیار تسلط:** کاربر به اینترنت؛ اینترنت به Web (VIP)؛ Web به App؛ App به DB؛ همه با Packet Walk و Log دو فایروال.
**اشتباهات رایج:** Route برگشت در فایروال دوم؛ NAT مضاعف ناخواسته؛ Policy فقط در یک فایروال؛ ترتیب Policy؛ مسیر نامتقارن.

**درس‌های فصل:**
- [درس 15-1 — طراحی معماری دوفایروالی](#l-15-1)
- [درس 15-2 — ساخت Edge: WAN، DMZ، NAT و VIP](#l-15-2)
- [درس 15-3 — ساخت Internal: Users و Servers و Routing به Edge](#l-15-3)
- [درس 15-4 — DMZ سه‌لایه: Web، App، DB و Policy بین لایه‌ها](#l-15-4)
- [درس 15-5 — Packet Walk دو فایروال و NAT در دو نقطه](#l-15-5)
- [درس 15-6 — خرابی‌ها و آزمون G6](#l-15-6)

---

<a id="l-15-1"></a>

## درس 15-0 — چرا دو فایروال؟ طراحی لبه، DMZ و لایه‌ی داخلی با تحلیل جریان و خرابی

**فصل ۱۵ · درس افزوده (پیش‌درس ۱۵-۱) · پیش‌نیاز: ۱۱-۰، ۱۲-۰، ۱۳-۷ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** مفهوم و طراحی؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. توضیح دهد چه موقع یک فایروال کافی است و چه موقع دو فایروال (Edge + Internal) توجیه دارد.
2. **DMZ**، Zoneها و مسیر هر نوع ترافیک (Users→Internet، Internet→DMZ، DMZ→Internal) را طراحی کند.
3. **NAT** را در دو فایروال (Double NAT) تحلیل و از مشکل‌هایش پرهیز کند.
4. جریان یک درخواست از اینترنت تا DB را از میان هر دو فایروال با Packet Flow بنویسد.
5. رفتار سیستم را در خرابی هر فایروال تحلیل کند.
6. تفاوت **دو فایروال از دو سازنده** (تنوع) با **دو فایروال هم‌سازنده** را بداند.

### ۲) پیش‌نیازها

مدل تهدید و Defense in Depth (۱۱-۰)، Packet Flow (۱۲-۰)، Session و NAT (۱۳-۷)، Asymmetric (۱۰-۶).

### ۳) مفهوم پایه

DMZ (ناحیه‌ی واسط) جایی است که سرورهای در معرض اینترنت (وب، ایمیل، Reverse Proxy) قرار می‌گیرند تا اگر نفوذ شد، مهاجم مستقیماً در شبکه‌ی داخلی نباشد. با یک فایروال سه‌پایه (Inside، Outside، DMZ) این کار ممکن است. دو فایروال پشت‌سرهم **لایه‌ی کنترل دوم** اضافه می‌کند: لبه (Edge) اینترنت را کنترل می‌کند و فایروال داخلی (Internal) فقط ورودی به شبکه‌ی داخلی را؛ حتی اگر Edge آسیب ببیند (یک Zero-day یا خطای Policy)، Internal جداگانه دفاع می‌کند.

> **تشبیه:** ورودی ساختمان (Edge) و درب اتاق سرور (Internal) دو کنترل مستقل‌اند؛ اگر نگهبان ورودی فریب بخورد، درب اتاق سرور هنوز قفل است.

### ۴) توضیح عمیق فنی

#### ۴-۱) سه الگو

| الگو | توضیح | مزیت | هزینه/ریسک |
|---|---|---|---|
| تک‌فایروال سه‌پایه | Inside، Outside، DMZ روی یک دستگاه | ساده، ارزان | نقطه‌ی شکست/آسیب واحد |
| دوفایروال سری (Sandwich) | Edge ← DMZ ← Internal | Defense in Depth، DMZ بین دو فایروال | پیچیدگی، هزینه، Double NAT |
| دوفایروال با تنوع سازنده | دو برند | کاهش آسیب‌پذیری مشترک | مدیریت دو ابزار، مهارت بیشتر |

#### ۴-۲) توپولوژی Sandwich

``` text
Internet --- [FW-EDGE] --- DMZ switch --- [FW-INT] --- Internal LAN
                              |
                         web / mail / proxy
```

قواعد:

- Edge: Internet→DMZ فقط پورت‌های سرویس (VIP)؛ DMZ→Internet محدود (Update)؛ Users→Internet از Edge یا از مسیر DMZ-proxy (تصمیم طراحی).
- Internal: DMZ→Internal فقط پورت‌های لازم (مثلاً Web→App 8080)؛ **Internal→DMZ مجاز و Internet→Internal مستقیم ممنوع**.
- هیچ مسیر مستقیم Internet→Internal بدون عبور از هر دو.

#### ۴-۳) NAT در دو فایروال

- **Edge:** DNAT (VIP) برای سرویس‌های عمومی؛ SNAT خروجی کاربران.
- **Internal:** ترجیحاً **بدون NAT** (Routing خالص) تا Log اصلی حفظ شود. Double NAT عیب‌یابی را سخت می‌کند و آدرس واقعی کاربر را در لاگ سرور پنهان می‌کند.
- اگر شبکه‌ی داخلی RFC 1918 است و DMZ هم، Edge باید مسیر برگشت به Internal داشته باشد (مسیر Static از طریق Internal) یا Source NAT انجام دهد؛ طراحی روتینگ را روی کاغذ بکشید.

#### ۴-۴) جریان یک درخواست

``` text
1. Client(Internet) -> 203.0.113.50:443            (VIP on EDGE)
2. EDGE: session lookup -> new; DNAT to 10.10.10.20 (DMZ web)
3. EDGE: route to DMZ; policy "WAN->DMZ HTTPS" accept; UTM; session
4. DMZ web -> App 10.20.20.5:8080                  (via FW-INT)
5. INT: policy "DMZ->Servers 8080" accept; session (no NAT)
6. App -> DB 10.20.30.7:1433 (inside Internal, same or another zone)
7. Replies follow the same sessions back (symmetric path)
```

شرط حیاتی: مسیر **برگشت** از همان فایروال‌ها (Stateful).

#### ۴-۵) خرابی

| خرابی | اثر | کاهش ریسک |
|---|---|---|
| Edge از کار بیفتد | اینترنت قطع؛ داخل سالم | HA یا Edge دوم |
| Internal بیفتد | DMZ→Internal قطع؛ اینترنت سالم | HA |
| Policy اشتباه Edge | سرویس‌های DMZ آسیب‌پذیر | Internal هنوز محافظ داخلی است |
| Asymmetric | Drop | طراحی مسیر + Session Sync/Policy Route |
| FW هر دو CVE مشترک | هر دو آسیب‌پذیر | تنوع سازنده/Patch سریع |

#### ۴-۶) سیاست‌های مدیریتی

Management VLAN جدا، Admin روی هر دو فقط از مدیریت، Syslog مرکزی از هر دو، تغییرات هماهنگ (Change مشترک)، Backup هر دو.

![شکل: دوفایروال با DMZ.](../figures/ch15-l0-fig1.svg)

*شکل: دوفایروال با DMZ.*

### ۵) مثال حل‌شده

**نیاز:** وب‌سایت عمومی، API داخلی، DB. طراحی: Edge: VIP 203.0.113.50:443→10.10.10.20 (DMZ). Internal: DMZ→10.20.20.5:8080 (App)؛ App→DB فقط داخل Internal. Policy Matrix:

``` text
EDGE    : WAN  -> DMZ      : VIP web  TCP 443        accept + IPS + log
EDGE    : DMZ  -> WAN      : DNS, updates only        accept + log
EDGE    : INT  -> WAN      : users HTTP/HTTPS/DNS     accept + UTM + NAT
INT     : DMZ  -> SRV      : 10.10.10.20 -> 10.20.20.5 TCP 8080   accept + log
INT     : SRV  -> DMZ      : established only (implicit via session)
INT     : any  -> any      : implicit deny + log
```

**مثال متوسط:** `ping` از Internet به DB داخلی ناکام است؛ Debug Flow روی Edge: «Denied policy 0» ← درست (هیچ Policy). نشان‌دهنده‌ی طراحی سالم است.

**مثال سخت:** پس از Compromise وب‌سرور DMZ، مهاجم سعی می‌کند به DB وصل شود: DMZ→SRV فقط 8080 مجاز است، بقیه deny+log؛ Alert بر پایه‌ی «Denied از DMZ به SRV» می‌تواند نشانه‌ی نفوذ باشد (Detection).

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| دوفایروال یا تک؟ | ریسک بالا/دارایی حساس ← دو؛ سازمان کوچک ← یک با DMZ و UTM |
| NAT | Edge فقط؛ Internal Routing |
| HA | هر دو HA (فصل ۲۲) |
| تنوع سازنده | در صورت بودجه/مهارت |
| Log | مرکزی، با Timestamp همگام (NTP) |

### ۷) پیاده‌سازی و Verification (GUI/CLI)

**GUI:** Policy & Objects → Virtual IPs (VIP)؛ Firewall Policy (WAN→DMZ)؛ Network → Static Routes (DMZ→Internal)؛ Log & Report → Forward Traffic.

**CLI:**

``` text
config firewall vip
    edit "VIP-WEB"
        set extip 203.0.113.50
        set mappedip "10.10.10.20"
        set extintf "wan1"
        set portforward enable
        set extport 443
        set mappedport 443
    next
end
get router info routing-table all
diagnose debug flow filter addr 10.10.10.20
diagnose sys session filter dst 10.10.10.20
```

(نام فیلدها `Unverified`.) **آزمون‌ها:** مثبت: اینترنت→VIP؛ منفی: اینترنت→DB، DMZ→DB، Internal→Internet مستقیم (بدون Policy).

### ۸) Troubleshooting

| علامت | علت |
|---|---|
| VIP از بیرون کار نمی‌کند | Policy مقصد (post-DNAT)، Route، ARP |
| DMZ به Internal نمی‌رسد | Policy Internal، مسیر، NAT اشتباه |
| فقط بعضی ارتباط‌ها Drop | Asymmetric/Session |
| Log مبدأ همه یک IP | Double NAT |

### ۹) نکات امنیتی

- Internal هرگز Internet را به‌طور مستقیم به‌رسمیت نشناسد.
- سرورهای DMZ نباید اعتبار (Credential) شبکه‌ی داخلی داشته باشند.
- تغییرات هر دو فایروال Change یکپارچه.

### ۱۰) جمع‌بندی مفهومی

- DMZ اثر نفوذ را محدود می‌کند؛ دو فایروال لایه‌ی کنترل مستقل است.
- NAT را فقط لبه؛ Internal ترجیحاً Routing.
- مسیر برگشت متقارن؛ Policy در جهت درست.
- طراحی را با «اگر لایه‌ی اول بشکند» ارزیابی کنید.
- مدیریت و Log را متمرکز کنید.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) DMZ چیست؟ *(پاسخ: 15-0-ت1)*

**ت2.** (ساده) چرا Internal NAT نمی‌کند؟ *(پاسخ: 15-0-ت2)*

**ت3.** (متوسط) مسیر یک درخواست Internet→App را بنویسید. *(پاسخ: 15-0-ت3)*

**ت4.** (متوسط) Double NAT چه مشکلی در Log دارد؟ *(پاسخ: 15-0-ت4)*

**ت5.** (سخت) پس از Compromise وب‌سرور، کدام سه کنترل جلوی حرکت جانبی را می‌گیرد؟ *(پاسخ: 15-0-ت5)*

**ت6.** (سخت، طراحی) برای سازمانی با بودجه‌ی محدود تصمیم دو فایروال در برابر تک‌فایروال+DMZ را با معیار ریسک بگیرید. *(پاسخ: 15-0-ت6)*

**Q1.** Quick quiz (English): Why avoid NAT on the internal firewall? *(پاسخ: 15-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DMZ | Demilitarized Zone | ناحیه‌ی واسط |
| Edge | Edge firewall | فایروال لبه |
| Sandwich | Firewall sandwich | دو فایروال با DMZ بین آن‌ها |
| VIP | Virtual IP | آدرس مجازی DNAT |

- *Place public servers in a DMZ between two firewalls.* ← سرورهای عمومی را در DMZ بین دو فایروال بگذارید.
- *Preserve original source addresses for logging.* ← آدرس مبدأ اصلی را برای Log حفظ کنید.

### ۱۳) منابع

- NIST SP 800-41 Rev.1 — Guidelines on Firewalls (DMZ designs).
- Fortinet Docs: FortiOS 7.0 Administration Guide — Virtual IPs، Firewall policy.

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: مقایسه‌ی یک‌فایروالی و دوفایروالی با عدد

**سناریو.** ۲۰۰ کاربر، ۱۵ سرور داخلی، ۳ سرور DMZ.

| معیار | یک فایروال | دو فایروال |
|---|---|---|
| نقطه‌ی شکست | ۱ | ۲ (با HA هر کدام ۱ جفت) |
| سطح حمله به داخل | یک Policy اشتباه کافی | باید دو لایه شکسته شود |
| تفکیک مسئولیت | ندارد | Edge=امنیت، Internal=شبکه |
| هزینه/پیچیدگی | کم | بیشتر |

**جریان:** Internet → Edge (NAT+VIP) → DMZ؛ Users → Internal → Edge → Internet. DMZ هرگز مستقیم به داخل Session نمی‌گشاید.

**تحلیل خرابی:** اگر Edge بیفتد اینترنت و DMZ قطع؛ Internal با Policy Route/Default به Edge همچنان داخلی کار می‌کند. اگر Internal بیفتد فقط ارتباط داخلی.

**پرسش‌های مصاحبه**
1. *چرا دو سازنده‌ی متفاوت؟* ضعف مشترک کم می‌شود (بحث Defense in Depth).
2. *DMZ به داخل؟* فقط جریان‌های حداقلی و آغاز از داخل.
3. *هزینه‌ی عملیاتی؟* دو مجموعه Policy و Backup.

### تکمیل عمیق: چرا دو فایروال؟ تحلیل جریان و خرابی

#### چرا باید یاد بگیریم؟

یک قلعه‌ی با یک دیوار، با شکسته‌شدن آن دیوار، همه‌چیز در دسترس است. قلعه‌ی با دو دیوار و حیاط میانی (DMZ) مهاجم را مجبور می‌کند دو بار نفوذ کند و در هر مرحله دیده شود. طراحی دو فایروالی همین «دفاع در عمق» (Defense in Depth) است.

#### توضیح ساده

- **Edge FW**: رو به اینترنت؛ NAT، VIP، DMZ.
- **Internal FW**: رو به شبکه‌ی داخلی؛ Users، Servers، Mgmt.
- بین آنها یک لینک /30 (LINK).

``` text
Internet -- Edge FW -- DMZ
               |
            LINK /30
               |
           Internal FW -- Users / Servers / Mgmt
```

#### مثال ساده — مقایسه با عدد

| معیار | یک فایروال | دو فایروال |
|---|---|---|
| دفعات نفوذ لازم برای رسیدن به داخل | 1 | 2 |
| تفکیک مسئولیت | ندارد | دارد |
| هزینه/پیچیدگی | کم | بیشتر |

#### مثال متوسط — جریان‌ها

``` text
F1 Users -> Internet : Internal(accept) -> Edge(accept + SNAT) -> ISP
F2 Internet -> DMZ    : Edge(VIP + policy) -> DMZ
F3 DMZ -> Internal    : denied by default (only minimal exceptions)
```

#### مثال سخت — تحلیل خرابی

| خرابی | اثر |
|---|---|
| Edge | اینترنت و DMZ قطع؛ داخلی سالم |
| Internal | ارتباط داخلی/به اینترنت قطع؛ DMZ سالم |
| لینک LINK | Users بی‌اینترنت |

با HA برای هر کدام این اثرها کم می‌شود.

#### Lab

نمودار را با نام Interface بکشید و سه جریان را ردیابی کنید.

#### عیب‌یابی طراحی

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| DMZ به داخل باز | Policy | Deny |
| دو NAT | طراحی | یکی |
| مسیر ناقص | Route | کامل |

#### پرسش‌ها با پاسخ

**۱. چرا DMZ جدا؟** سرورهای در معرض اینترنت.
**۲. DMZ به داخل؟** ممنوع مگر استثنا.
**۳. NAT کجا؟** Edge.

#### English Corner

- *Defense in depth forces an attacker to defeat multiple independent layers.*
- Q: Why should DMZ hosts be unable to initiate sessions to the internal network?

## درس 15-1 — طراحی معماری دوفایروالی: نقش‌ها، Zoneها، آدرس‌دهی و جدول مسیر

**فصل 15 · بازنویسی عمیق · پیش‌نیاز: ۱۵-۰، ۱۲-۲، ۱۳-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. نقش Edge و Internal را در معماری دوفایروالی تعریف کنید.
2. Interfaceها، Zoneها و آدرس‌دهی را (با /30 برای Transit) طراحی کنید.
3. جدول مسیر دو دستگاه را بنویسید و Route برگشت را فراموش نکنید.
4. ماتریس Policy بین Zoneها را طراحی کنید.
5. Asymmetric، Double NAT و Rule Drift را به‌عنوان خطر بشناسید.
6. طراحی را با Packet Walk اثبات کنید.

### چرا باید یاد بگیریم؟

یک ساختمان اداری را در نظر بگیرید: نگهبان در ورودی ساختمان (Edge) و کارت‌خوان جلوی اتاق سرور (Internal). اگر مهاجم از نگهبان رد شود، هنوز مانع دوم دارد. دو فایروال هم همین «دفاع لایه‌ای» است. ولی دو دستگاه یعنی دو برابر Route، دو برابر Policy و دو برابر نقطه‌ی خطا؛ بدون طراحی دقیق، خود پیچیدگی تبدیل به آسیب‌پذیری می‌شود. این درس نقشه‌ی ساختمان را قبل از اجرا می‌کشد.

### نقش‌ها

| دستگاه | نقش | قابل‌دسترس از |
|---|---|---|
| Edge | اتصال به ISP، NAT، DMZ، VIP | اینترنت |
| Internal | Users، Servers، Mgmt | فقط از Edge و داخل |

اصل: **هر ترافیک ورودی از اینترنت ابتدا در Edge متوقف و فقط مجاز به DMZ می‌رود؛ هیچ مسیر مستقیمی از اینترنت به Internal وجود ندارد.**

### توپولوژی

``` text
 Internet
    |
 [ISP 203.0.113.1]
    |
 port1 WAN 203.0.113.2/29
 +-------+
 | EDGE  |-- port2 DMZ 10.30.0.1/24 -- [Web]
 +-------+
 port3 LINK 10.99.0.1/30
    |
 port1 LINK 10.99.0.2/30
 +----------+
 | INTERNAL |-- port2 USERS 10.10.0.1/24
 +----------+-- port3 SRV   10.20.0.1/24
              -- port4 MGMT  10.50.0.1/24
```

### جدول Interface

| دستگاه | Interface | Zone | آدرس |
|---|---|---|---|
| Edge | port1 | WAN | 203.0.113.2/29 |
| Edge | port2 | DMZ | 10.30.0.1/24 |
| Edge | port3 | LINK | 10.99.0.1/30 |
| Internal | port1 | LINK | 10.99.0.2/30 |
| Internal | port2 | USERS | 10.10.0.1/24 |
| Internal | port3 | SRV | 10.20.0.1/24 |
| Internal | port4 | MGMT | 10.50.0.1/24 |

### چرا /30 برای Transit؟

``` text
/30 -> 4 addresses - network - broadcast = 2 usable hosts
```

دو آدرس قابل‌استفاده برای دو فایروال کافی است و هیچ Host سوم نمی‌تواند در آن لینک قرار بگیرد (سطح حمله‌ی کمینه).

### جدول مسیر

``` text
Internal: 0.0.0.0/0     via 10.99.0.1
Edge    : 0.0.0.0/0     via 203.0.113.1
Edge    : 10.10.0.0/24  via 10.99.0.2
Edge    : 10.20.0.0/24  via 10.99.0.2
Edge    : 10.50.0.0/24  via 10.99.0.2
```

Internal فقط یک Default به Edge دارد. Edge باید «برگشت» به سه شبکه‌ی داخلی را بداند؛ وگرنه پاسخ‌ها از Default (WAN) خارج و گم می‌شوند.

### ماتریس Policy

| از ↓ به → | Internet | DMZ | Users | Servers | Mgmt |
|---|---|---|---|---|---|
| Internet | - | HTTPS (VIP) | - | - | - |
| DMZ | - | - | - | DB 1433 از App | - |
| Users | HTTP/S/DNS (SNAT) | HTTPS | - | App 443 | - |
| Servers | Updates | - | - | - | - |
| Mgmt | - | SSH | - | SSH | - |

خالی (-) یعنی Deny. هر خانه یک Policy مشخص دارد؛ هیچ ALL/ALL.

### خطرها

| خطر | علت | کاهش |
|---|---|---|
| Asymmetric | دو مسیر بین Edge و Internal | یک Link، Route واحد |
| Double NAT | NAT در هر دو | NAT فقط در Edge |
| Rule Drift | اختلاف Policy دو دستگاه | بازبینی فصلی |
| SPOF | هر دستگاه یک نقطه‌ی خطا | HA/DR (فصل بعد) |

### مثال‌های حل‌شده

#### مثال ساده — Transit

چرا 10.99.0.0/30 و نه /24؟ فقط دو Host لازم است؛ /24 ۲۵۴ آدرس بی‌دلیل در معرض ورود می‌گذارد.

#### مثال متوسط — Summary Route

سه شبکه‌ی 10.10.0.0/24، 10.20.0.0/24 و 10.50.0.0/24 پیوسته نیستند (10.30 و 10.40 بین‌شان است). Summary 10.0.0.0/16 DMZ (10.30) را هم پوشش می‌دهد و Edge را به اشتباه برای DMZ به Internal می‌فرستد. پس سه Route جدا.

``` text
10.10.0.0/24 + 10.20.0.0/24 + 10.50.0.0/24 -> not contiguous
Summary 10.0.0.0/16 would also cover DMZ 10.30.0.0/24 -> WRONG
```

#### مثال سخت — Route برگشت فراموش‌شده

Users به اینترنت می‌روند؛ پاسخ به Edge می‌رسد؛ Edge Route به 10.10.0.0/24 ندارد و از Default به ISP می‌فرستد ⇒ گم. علامت: کاربر Timeout؛ Sniffer روی port1 Edge پاسخ ورودی را می‌بیند ولی SYN-ACK به داخل نمی‌رسد؛ `get router info routing-table details 10.10.0.5` (Edge) ⇒ Default. رفع: Route برگشت. تأیید: همان دستور ⇒ via 10.99.0.2.

### مسیر GUI (مستندی، Unverified)

1. هر فایروال: Network → Interfaces برای Transit و Zoneها.
2. Network → Static Routes.
3. Policy & Objects برای ماتریس.

### Lab هدایت‌شده (اجرا نشده)

1. جدول Interface و Route را بنویسید.
2. ماتریس Policy را روی کاغذ پر کنید.
3. برای سه جریان Packet Walk Hop-by-hop بنویسید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| پاسخ گم | Route برگشت | افزودن در Edge |
| IP تکراری | Overlap | بازبینی |
| Mgmt از Users قابل‌دسترس | Policy | Deny |
| دو NAT | تنظیم اشتباه | NAT فقط Edge |

### نکات امنیتی

Mgmt را هرگز از اینترنت یا Users باز نکنید؛ لینک Transit را فقط برای همین دو دستگاه نگه دارید.

### جمع‌بندی

Edge ورودی عمومی و DMZ؛ Internal شبکه‌های داخلی؛ Transit /30؛ Route برگشت در Edge الزامی؛ NAT فقط Edge؛ ماتریس Policy بدون ALL؛ خطرها: Asymmetric و Rule Drift.

### تمرین و ارزیابی

**ت1.** (ساده) چرا NAT فقط روی Edge؟ *(پاسخ: 15-1-ت1)*

**ت2.** (ساده) Default Internal به کجاست؟ *(پاسخ: 15-1-ت2)*

**ت3.** (متوسط) چرا Edge باید Route شبکه‌های داخلی را داشته باشد؟ *(پاسخ: 15-1-ت3)*

**ت4.** (متوسط) DMZ→DB مستقیم چرا ممنوع؟ *(پاسخ: 15-1-ت4)*

**ت5.** (سخت) طرح ممیزی‌پذیر را بنویسید. *(پاسخ: 15-1-ت5)*

**ت6.** (سخت، طراحی) ریسک Rule drift را چگونه کنترل می‌کنید؟ *(پاسخ: 15-1-ت6)*

**Q1.** Quick quiz (English): Why configure NAT only on the edge firewall? *(پاسخ: 15-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DMZ | Demilitarized Zone | منطقه‌ی حائل |

- *Edge handles north-south traffic.* ← Edge ترافیک شمال-جنوب را کنترل می‌کند.

### کارت Lab

**کارت Lab:** طراحی دوفایروالی (اجرا نشده). **Evidence:** `02-design/arch2.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies; Routing
- NIST SP 800-41

<a id="l-15-2"></a>

## درس 15-2 — ساخت Edge: WAN، DMZ، NAT، VIP و Policy ورودی

**فصل 15 · بازنویسی عمیق · پیش‌نیاز: ۱۵-۱، ۱۳-۲، ۱۳-۳ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. WAN، DMZ و Transit را روی Edge پیکربندی کنید.
2. Default Route و Routeهای برگشت را بنویسید.
3. SNAT (خروجی) و VIP (ورودی) را روی Edge بسازید.
4. Policyهای ورودی (Internet→DMZ) را ایمن بنویسید.
5. با Lookup، Session و Sniffer آزمون کنید.
6. چهار خطای رایج Edge را رفع کنید.

### چرا باید یاد بگیریم؟

Edge «دروازه‌ی شهر» است: همه‌ی ترافیک عمومی از آن رد می‌شود. یک اشتباه در VIP یا Policy یعنی سرور داخلی را در معرض اینترنت گذاشتن. در این درس Edge را قدم‌به‌قدم می‌سازیم و با آزمون مثبت و منفی ثابت می‌کنیم فقط همان چیزی باز است که می‌خواهیم.

### قدم ۱ — Interfaceها

``` text
config system interface
    edit "port1"
        set alias WAN
        set mode static
        set ip 203.0.113.2 255.255.255.248
        set allowaccess ping
    next
    edit "port2"
        set alias DMZ
        set ip 10.30.0.1 255.255.255.0
    next
    edit "port3"
        set alias LINK
        set ip 10.99.0.1 255.255.255.252
    next
end
```

روی WAN فقط `ping` (و در صورت نیاز) مجاز؛ هرگز `http`، `ssh`، `telnet` از اینترنت.

### قدم ۲ — Routeها

``` text
config router static
    edit 1
        set gateway 203.0.113.1
        set device port1
    next
    edit 2
        set dst 10.10.0.0 255.255.255.0
        set gateway 10.99.0.2
        set device port3
    next
    edit 3
        set dst 10.20.0.0 255.255.255.0
        set gateway 10.99.0.2
        set device port3
    next
    edit 4
        set dst 10.50.0.0 255.255.255.0
        set gateway 10.99.0.2
        set device port3
    next
end
```

### قدم ۳ — خروجی (SNAT)

``` text
config firewall policy
    edit 10
        set name "LINK-to-WAN"
        set srcintf "port3"
        set dstintf "port1"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "HTTP" "HTTPS" "DNS"
        set nat enable
        set logtraffic all
    next
end
```

NAT فقط اینجا (Edge). با `nat enable` مبدأ به 203.0.113.2 (یا Pool) ترجمه می‌شود.

### قدم ۴ — ورودی (VIP + Policy)

``` text
config firewall vip
    edit "VIP-WEB"
        set extip 203.0.113.3
        set mappedip 10.30.0.10
        set extintf port1
        set portforward enable
        set protocol tcp
        set extport 443
        set mappedport 443
    next
end
config firewall policy
    edit 20
        set name "WAN-to-DMZ-WEB"
        set srcintf "port1"
        set dstintf "port2"
        set srcaddr "all"
        set dstaddr "VIP-WEB"
        set action accept
        set schedule "always"
        set service "HTTPS"
        set logtraffic all
    next
end
```

نکته: `dstaddr` باید خود VIP باشد، نه IP داخلی.

### Policyهای DMZ

| Policy | مسیر | سرویس | توضیح |
|---|---|---|---|
| 20 | WAN→DMZ | HTTPS (VIP) | انتشار |
| 30 | DMZ→WAN | DNS/NTP/Updates | حداقل |
| 99 | any→any | - | Deny + Log (Implicit) |

اصل: DMZ نباید آزادانه به داخل ابتکار اتصال بزند؛ این مسیر فقط از Internal با Policy مشخص.

### آزمون

``` text
diagnose firewall iprope lookup 198.51.100.50 40000 203.0.113.3 443 tcp port1
diagnose sys session filter dst 10.30.0.10
diagnose sniffer packet any 'host 10.30.0.10 and tcp port 443' 4 10 a
```

آزمون منفی: از اینترنت به پورت 22 همان VIP ⇒ باید Deny (Lookup ⇒ policy 0).

### مثال‌های حل‌شده

#### مثال ساده — VIP

کاربر اینترنت به 203.0.113.3:443 ⇒ Edge DNAT به 10.30.0.10:443. Session: `act=dnat`. Sniffer port2: بسته با مقصد 10.30.0.10.

#### مثال متوسط — آزمون منفی

اینترنت → 203.0.113.3:22: Lookup ⇒ policy 0؛ Log: deny. ثابت می‌کند فقط HTTPS باز است.

#### مثال متوسط — Route برگشت

Web (10.30.0.10) پاسخ را به Edge می‌دهد (Gateway Edge). برای Users: پاسخ از Edge به Internal باید Route داشته باشد؛ Route 10.10.0.0/24 via 10.99.0.2 موجود است ⇒ OK.

#### مثال سخت — VIP و Policy اشتباه

`dstaddr` Policy برابر `all` و VIP هم باز؛ ظاهراً کار می‌کند ولی Policy برای هر آدرس عمومی ناخواسته باز است. رفع: `dstaddr "VIP-WEB"`. آزمون: Lookup به 203.0.113.4:443 ⇒ policy 0.

#### مثال سخت — Hairpin

Users داخلی با IP عمومی 203.0.113.3 به سایت می‌روند: ترافیک از Internal به Edge و برگشت به DMZ. نیاز به Policy LINK→DMZ و گاهی NAT؛ ساده‌تر: DNS داخلی نام را به 10.30.0.10 حل کند (Split DNS).

### مسیر GUI (مستندی، Unverified)

1. Network → Interfaces.
2. Static Routes.
3. Virtual IPs.
4. Firewall Policy.

### Lab هدایت‌شده (اجرا نشده)

1. Interface/Route/Policy را اعمال کنید.
2. VIP و آزمون مثبت/منفی.
3. Sniffer در دو Interface.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| VIP کار نمی‌کند | dstaddr اشتباه | VIP |
| پاسخ نمی‌آید | Gateway سرور | Edge |
| NAT نمی‌شود | nat disable | enable |
| از اینترنت پورت دیگر باز | Policy باز | تنگ |

### نکات امنیتی

Policy ورودی فقط پورت لازم؛ IPS/WAF در صورت لایسنس (Needs-License)؛ مدیریت Edge فقط از Mgmt.

### جمع‌بندی

Edge: Interface، Route (با برگشت)، SNAT، VIP + Policy با dstaddr=VIP، آزمون مثبت و منفی. DMZ حداقل دسترسی.

### تمرین و ارزیابی

**ت1.** (ساده) Policy 99؟ *(پاسخ: 15-2-ت1)*

**ت2.** (ساده) VIP چه می‌کند؟ *(پاسخ: 15-2-ت2)*

**ت3.** (متوسط) چرا port1 بدون Admin access؟ *(پاسخ: 15-2-ت3)*

**ت4.** (متوسط) آزمون منفی؟ *(پاسخ: 15-2-ت4)*

**ت5.** (سخت) VIP جواب نمی‌دهد. *(پاسخ: 15-2-ت5)*

**ت6.** (سخت، طراحی) ماتریس Edge. *(پاسخ: 15-2-ت6)*

**Q1.** Quick quiz (English): Which policy should end the Edge rule list? *(پاسخ: 15-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VIP | Virtual IP | آدرس مجازی |

- *Test denied flows too.* ← جریان‌های ردشده را هم آزمون کنید.

### کارت Lab

**کارت Lab:** Edge (اجرا نشده). **Evidence:** `02-design/fgt-edge.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Virtual IPs

<a id="l-15-3"></a>

### ضمیمه: پرونده‌ی کامل حل‌شده — «VIP وب از اینترنت باز نمی‌شود»

**ورودی:** VIP-WEB-443 (203.0.113.10 → 10.30.0.10) ساخته شده؛ از اینترنت Timeout.

**گام ۱ — Debug flow:**

``` text
diagnose debug flow filter addr 203.0.113.10
diagnose debug flow trace start 20
diagnose debug enable
 -> "Denied by forward policy check (policy 0)"
```

**گام ۲ — علت:** Policy 2 با dstaddr=10.30.0.10 (آدرس داخلی) نوشته شده؛ باید VIP باشد (DNAT قبل از Policy).

**گام ۳ — رفع:** dstaddr را به VIP-WEB-443 تغییر دهید.

**گام ۴ — Verify:** Debug: «Allowed by Policy-2»؛ `session list`: DNAT 203.0.113.10:443 → 10.30.0.10:443.

**گام ۵ — آزمون منفی:** SSH به 203.0.113.10 ⇒ Deny (policyid=99 با Log).

**گام ۶ — پایان:** `diagnose debug disable` و `diagnose debug reset`.

## درس 15-3 — ساخت Internal: Users، Servers، Mgmt و Routing به Edge با آزمون کامل

**فصل 15 · بازنویسی عمیق · پیش‌نیاز: ۱۵-۱، ۱۵-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Interface و Zoneهای Internal (Users، Servers، Mgmt) را پیکربندی کنید.
2. Default Route به Edge را بگذارید و NAT را فقط روی Edge نگه دارید.
3. Policyهای Users، Servers و Mgmt را بر اساس حداقل دسترسی بنویسید.
4. آزمون کامل (مثبت/منفی/Hop-by-hop) انجام دهید.
5. مدیریت (SSH/HTTPS) را فقط از Mgmt مجاز کنید.
6. خطاهای رایج Internal را رفع کنید.

### چرا باید یاد بگیریم؟

Internal «کارت‌خوان اتاق سرور» است. مهاجمی که یک لپ‌تاپ آلوده در Users دارد، نباید بتواند مستقیم به پایگاه‌داده یا Mgmt برسد. Internal با Policy سخت‌گیرانه بین Zoneهای داخلی از حرکت جانبی (Lateral Movement) جلوگیری می‌کند.

### Interface و Zone

``` text
config system zone
    edit "ZN-USERS"
        set interface "port2"
    next
    edit "ZN-SRV"
        set interface "port3"
    next
    edit "ZN-MGMT"
        set interface "port4"
        set intrazone deny
    next
end
```

`intrazone deny` یعنی Hostهای داخل یک Zone هم بدون Policy نمی‌توانند به هم برسند.

### Default Route

``` text
config router static
    edit 1
        set gateway 10.99.0.1
        set device port1
    next
end
```

Internal هیچ NAT خروجی ندارد؛ NAT فقط در Edge.

### Policyها

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
    edit 20
        set name "USERS-to-NET"
        set srcintf "ZN-USERS"
        set dstintf "port1"
        set srcaddr "NET-USERS"
        set dstaddr "all"
        set service "HTTP" "HTTPS" "DNS"
        set action accept
        set schedule "always"
        set logtraffic all
    next
    edit 30
        set name "MGMT-to-ALL-SSH"
        set srcintf "ZN-MGMT"
        set dstintf "ZN-SRV"
        set srcaddr "HOST-ADMIN"
        set dstaddr "all"
        set service "SSH"
        set action accept
        set schedule "always"
        set logtraffic all
    next
end
```

مدیریت FortiGate: `set allowaccess https ssh` فقط روی port4 (Mgmt) و `trusthost` برای Admin.

### مثال‌های حل‌شده

#### مثال ساده — Users به اپ

PC 10.10.0.5 → 10.20.0.30:443: Lookup (ورودی port2) ⇒ policy 10 ⇒ OK.

#### مثال متوسط — آزمون منفی

Users → Servers پورت 1433 (DB): Lookup ⇒ policy 0 ⇒ Deny؛ Log deny. ثابت می‌کند Users مستقیم به DB دسترسی ندارند.

#### مثال متوسط — اینترنت

Users → 8.8.8.8:53: Policy 20 ⇒ Internal Route به Edge ⇒ Edge SNAT ⇒ اینترنت. Session Internal بدون NAT؛ Session Edge با SNAT.

#### مثال سخت — حرکت جانبی

PC آلوده در Users به SSH سرور 10.20.0.30 تلاش می‌کند. Policy SSH فقط از ZN-MGMT است ⇒ Deny؛ Log هشدار. مقایسه: بدون Zone و با ALL، حمله موفق می‌شد.

#### مثال سخت — Default Route اشتباه

Default روی port1 ولی Gateway اشتباه (10.99.0.9). علامت: Users اینترنت ندارند. `get router info routing-table details 8.8.8.8` ⇒ via 10.99.0.9؛ ARP ناموفق. رفع: Gateway درست 10.99.0.1. تأیید: ping به 10.99.0.1 و Debug.

### آزمون کامل

``` text
get router info routing-table details 8.8.8.8
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.30 443 tcp port2
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.30 1433 tcp port2
diagnose sys session filter src 10.10.0.5
diagnose sys session list
```

### مسیر GUI (مستندی، Unverified)

1. Network → Interfaces برای هر پورت.
2. Network → Static Routes → Default به 10.255.0.1.
3. Policy & Objects → Firewall Policy با ماتریس.
4. Log & Report → Forward Traffic برای آزمون منفی.

### Lab هدایت‌شده (اجرا نشده)

1. Zoneها و Policyها را بسازید.
2. آزمون مثبت/منفی را اجرا کنید.
3. Mgmt را محدود و SSH را از Users تست کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| اینترنت ندارند | Default/Gateway | تصحیح |
| Users به DB می‌رسند | Policy باز | تنگ |
| Mgmt از Users باز | allowaccess | محدود |
| Zone Policy کار نمی‌کند | Interface عضو نیست | عضویت |

### نکات امنیتی

Admin با MFA و `trusthost`؛ SSH فقط Key؛ Log همه‌ی Policyها؛ DB فقط از App.

### جمع‌بندی

Internal: Zone با `intrazone deny`، Default به Edge، NAT فقط Edge، Policy حداقل دسترسی (Users→App، Mgmt→SSH)، آزمون منفی برای اثبات.

### تمرین و ارزیابی

**ت1.** (ساده) چرا NAT روی Internal خاموش است؟ *(پاسخ: 15-3-ت1)*

**ت2.** (ساده) Default Internal به کجا؟ *(پاسخ: 15-3-ت2)*

**ت3.** (متوسط) چرا Servers→Internet باید محدود باشد؟ *(پاسخ: 15-3-ت3)*

**ت4.** (متوسط) چرا Mgmt جدا؟ *(پاسخ: 15-3-ت4)*

**ت5.** (سخت) اینترنت ندارند ولی Servers ok؛ مسیر عیب‌یابی؟ *(پاسخ: 15-3-ت5)*

**ت6.** (سخت، طراحی) ماتریس Internal برای ۱۵۰ کاربر و ۱۰ سرور. *(پاسخ: 15-3-ت6)*

**Q1.** Quick quiz (English): Why is NAT not enabled on the internal firewall in this design? *(پاسخ: 15-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Lateral movement | Lateral movement | حرکت جانبی مهاجم |
| Transit | Transit network | شبکه‌ی ارتباطی دو فایروال |

- *Internal firewall limits lateral movement.* ← فایروال داخلی حرکت جانبی را محدود می‌کند.

### کارت Lab

**کارت Lab:** Internal (اجرا نشده). **Evidence:** `02-design/fgt-internal.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies; Routing
- NIST SP 800-41 Rev.1

<a id="l-15-4"></a>

## درس 15-4 — DMZ سه‌لایه: Web، App، DB؛ Policy، آزمون منفی و پایش

**فصل 15 · بازنویسی عمیق · پیش‌نیاز: ۱۵-۱ تا ۱۵-۳ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری سه‌لایه (Web، App، DB) را در DMZ و Servers طراحی کنید.
2. Policy بین لایه‌ها را با اصل «فقط لایه‌ی مجاور» بنویسید.
3. آزمون منفی (Web به DB مستقیم ممنوع) را اجرا کنید.
4. Log و پایش هر لایه را تنظیم کنید.
5. اثر نفوذ به Web را با و بدون تفکیک مقایسه کنید.
6. خطاهای رایج سه‌لایه را رفع کنید.

### چرا باید یاد بگیریم؟

اگر وب‌سرور هک شود و DB در همان شبکه با دسترسی آزاد باشد، مهاجم در چند دقیقه همه‌ی داده را می‌برد. در سه‌لایه، Web فقط با App حرف می‌زند و App فقط با DB: مهاجم برای رسیدن به داده باید دو مانع را رد کند و در هر مانع Log و آلارم دارد. مثل بانک: سالن (Web)، کارمند (App)، خزانه (DB)؛ مشتری مستقیم به خزانه نمی‌رود.

### معماری

``` text
Internet -> [Edge] -> DMZ: Web (10.30.0.10)
                         |  HTTPS 8443
                         v
              [Internal] SRV: App (10.20.0.30)
                         |  TCP 1433
                         v
                         DB  (10.20.0.40)
```

### ماتریس سه‌لایه

| از | به | سرویس | اجازه |
|---|---|---|---|
| Internet | Web | HTTPS 443 (VIP) | بله |
| Web | App | TCP 8443 | بله |
| App | DB | TCP 1433 | بله |
| Web | DB | هر | **خیر** |
| Internet | App/DB | هر | **خیر** |
| DB | Internet | هر | **خیر** |

### Policyها (Internal و Edge)

``` text
config firewall policy
    edit 40
        set name "WEB-to-APP"
        set srcintf "LINK"
        set dstintf "ZN-SRV"
        set srcaddr "HOST-WEB"
        set dstaddr "HOST-APP"
        set service "TCP-8443"
        set action accept
        set schedule "always"
        set logtraffic all
    next
    edit 41
        set name "APP-to-DB"
        set srcintf "ZN-SRV"
        set dstintf "ZN-SRV"
        set srcaddr "HOST-APP"
        set dstaddr "HOST-DB"
        set service "TCP-1433"
        set action accept
        set schedule "always"
        set logtraffic all
    next
end
```

نکته: App و DB در یک Zone‌اند؛ پس `intrazone deny` باعث می‌شود Policy صریح لازم باشد (و Web به DB اصلاً مسیر ندارد). برای تفکیک قوی‌تر DB را در Zone/VLAN جدا بگذارید.

### مثال‌های حل‌شده

#### مثال ساده — مسیر مجاز

کاربر اینترنت ← Edge VIP ← Web ← Internal Policy 40 ← App ← Policy 41 ← DB. هر گام Log دارد؛ Session در هر فایروال جدا.

#### مثال متوسط — آزمون منفی

``` text
diagnose firewall iprope lookup 10.30.0.10 40000 10.20.0.40 1433 tcp port3
 -> policy 0 (deny)
```

Web به DB مستقیم ممنوع؛ Log deny. اگر Policy 0 نبود و مجاز شد، خطای طراحی است.

#### مثال متوسط — پایش

برای هر Policy: `logtraffic all`؛ هشدار: تعداد Deny از Web به DB > 0 ⇒ Alert (نشانه‌ی تلاش حرکت جانبی). فهرست Dashboard: Top Denied.

#### مثال سخت — نفوذ به Web

مهاجم با آسیب‌پذیری Web کنترل سرور را گرفت. تلاش: اسکن شبکه‌ی داخلی ⇒ Deny (Edge/Internal)، فقط 8443 به App مجاز. تلاش Exploit روی App از طریق 8443 ممکن است (باید IPS/WAF)؛ تلاش به DB ⇒ Deny. اثر: دامنه‌ی خسارت محدود به Web و (در صورت آسیب‌پذیری App) App.

#### مثال سخت — DB با اینترنت

برای به‌روزرسانی DB، تیم موقتاً DB→Internet را باز کرد و فراموش شد. ممیزی: Policy بدون Owner/Expiry، Hit Count فعال ⇒ DB به C2 وصل شد (در سناریو). درس: Policy موقت با Comment و تاریخ انقضا، بازبینی فصلی (۱۳-۵).

### مسیر GUI (مستندی، Unverified)

1. Policy & Objects → Firewall Policy → ترتیب Policyها.
2. Log & Report → Forward Traffic → Filter policyid=61.

### Lab هدایت‌شده (اجرا نشده)

1. Policy 40 و 41 را بسازید.
2. آزمون منفی Web→DB و Internet→App.
3. Alert برای Deny غیرعادی.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| App به DB نمی‌رسد | Policy/Port | 41 |
| Web به DB می‌رسد | Policy بیش‌ازحد | حذف |
| Log نیست | logtraffic | all |
| DB اینترنت دارد | Policy موقت | حذف |

### نکات امنیتی

DB فقط TLS و حساب سرویس؛ IPS روی مسیر Web→App (Needs-License)؛ Backup DB خارج از شبکه.

### جمع‌بندی

سه‌لایه با «فقط مجاور»؛ آزمون منفی الزامی؛ Log و Alert روی Deny غیرعادی؛ Policy موقت ممنوع بدون انقضا.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Web→DB ممنوع است؟ *(پاسخ: 15-4-ت1)*

**ت2.** (ساده) چرا Deny صریح با وجود Implicit Deny؟ *(پاسخ: 15-4-ت2)*

**ت3.** (متوسط) DB→Internet چرا ممنوع؟ *(پاسخ: 15-4-ت3)*

**ت4.** (متوسط) آزمون منفی چیست؟ *(پاسخ: 15-4-ت4)*

**ت5.** (سخت) Web آلوده Scan می‌زند؛ پاسخ؟ *(پاسخ: 15-4-ت5)*

**ت6.** (سخت، طراحی) ماتریس و Alertها. *(پاسخ: 15-4-ت6)*

**Q1.** Quick quiz (English): Why use three tiers instead of placing web and database together? *(پاسخ: 15-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Tier | Application tier | لایه‌ی برنامه |
| SOC | Security Operations Center | مرکز عملیات امنیت |

- *The web tier must not reach the database directly.* ← لایه‌ی وب نباید مستقیماً به DB برسد.

### کارت Lab

**کارت Lab:** سه‌لایه (اجرا نشده). **Evidence:** `02-design/fgt-3tier.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- NIST SP 800-41; OWASP

<a id="l-15-5"></a>

## درس 15-5 — Packet Walk در دو فایروال: NAT در دو نقطه، Session در هر سمت و اثبات

**فصل 15 · بازنویسی عمیق · پیش‌نیاز: ۱۵-۱ تا ۱۵-۴، ۱۴-۳ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Packet Walk کامل Users→اینترنت و اینترنت→Web را در دو فایروال بنویسید.
2. نقاط NAT (SNAT در Edge، DNAT در Edge) را مشخص کنید.
3. Session در هر فایروال را بخوانید و تفاوت‌ها را توضیح دهید.
4. با Sniffer در چهار نقطه مسیر را اثبات کنید.
5. تفاوت Asymmetric و Symmetric را روی دو دستگاه بشناسید.
6. نبود NAT در Internal را اثبات کنید.

### چرا باید یاد بگیریم؟

وقتی دو فایروال دارید، عیب‌یابی «کدام فایروال بسته را گم کرد؟» سخت‌تر می‌شود. Packet Walk مثل نقشه‌ی مسیر پستی است: بسته از کدام Hub می‌گذرد، کجا برچسب آدرس عوض می‌شود. با آن، هر خرابی را به یک نقطه‌ی مشخص نسبت می‌دهید.

### Packet Walk — Users به اینترنت

``` text
PC 10.10.0.5 -> 8.8.8.8:53 (UDP)
 1 PC -> Internal port2  (src 10.10.0.5 dst 8.8.8.8)
 2 Internal: route default -> port1 (10.99.0.1)
 3 Internal: policy 20 accept, NO NAT
 4 Internal port1 -> Edge port3  (src 10.10.0.5 unchanged)
 5 Edge: route default -> port1 (203.0.113.1)
 6 Edge: policy 10 accept, SNAT 10.10.0.5 -> 203.0.113.2
 7 Edge port1 -> ISP -> 8.8.8.8
 8 Reply: 8.8.8.8 -> 203.0.113.2
 9 Edge: reverse NAT -> 10.10.0.5, route -> port3 via 10.99.0.2
10 Internal: session match -> PC
```

### Packet Walk — اینترنت به Web

``` text
Client 198.51.100.50 -> 203.0.113.3:443
 1 Edge port1: VIP DNAT 203.0.113.3 -> 10.30.0.10
 2 Edge: policy 20 (WAN->DMZ), session created
 3 Edge port2 -> Web 10.30.0.10
 4 Web replies -> Edge (gateway)
 5 Edge: reverse DNAT, src 203.0.113.3 -> client
```

### Session در دو فایروال

| دستگاه | Session | NAT |
|---|---|---|
| Internal | 10.10.0.5:5353 → 8.8.8.8:53 | ندارد |
| Edge | 10.10.0.5:5353 → 8.8.8.8:53 | `act=snat → 203.0.113.2` |

``` text
Internal: diagnose sys session filter src 10.10.0.5 ; session list  (no snat)
Edge    : diagnose sys session filter src 10.10.0.5 ; session list  (act=snat)
```

### Sniffer در چهار نقطه

``` text
A: Internal port2  src 10.10.0.5
B: Internal port1  src 10.10.0.5  (still private)
C: Edge     port3  src 10.10.0.5
D: Edge     port1  src 203.0.113.2 (NATed)
```

اگر A دیده شود ولی B نه ⇒ Internal Policy/Route. B دیده شود ولی C نه ⇒ لینک Transit. C دیده شود ولی D نه ⇒ Edge Policy/Route.

### Asymmetric

اگر Internal چند لینک به Edge داشت و پاسخ از لینک دیگری برمی‌گشت، Session در Internal وجود نداشت و RPF/State fail می‌شد. طراحی تک‌لینک این را حذف می‌کند.

### مثال‌های حل‌شده

#### مثال ساده — کجا NAT؟

فقط Edge. Sniffer B: src هنوز 10.10.0.5. اگر 203.0.113.2 دیده شود، Internal هم NAT می‌کند (اشتباه: Double NAT).

#### مثال متوسط — گم‌شدن در Transit

A و B دیده شد، C نه. بررسی: VLAN لینک Transit اشتباه. رفع: VLAN/کابل. تأیید: C دیده شد.

#### مثال متوسط — Session نیمه

Edge Session با `SYN_SENT`؛ D دیده شد؛ پاسخ نیامد ⇒ بالادست.

#### مثال سخت — Double NAT ناخواسته

کاربران به اینترنت می‌روند ولی Log Edge همه را 10.99.0.2 (Internal) نشان می‌دهد؛ ممیزی نمی‌داند کدام کاربر. علت: `nat enable` در Policy Internal. رفع: `nat disable` در Internal. درس: NAT فقط Edge تا Log و ردیابی کاربر حفظ شود.

#### مثال سخت — Route برگشت Edge

پاسخ به D می‌آید ولی C دیده نمی‌شود: Edge Route به 10.10.0.0/24 ندارد ⇒ پاسخ از Default خارج. `routing-table details 10.10.0.5` در Edge. رفع: Route برگشت.

### Lab هدایت‌شده (اجرا نشده)

1. چهار Sniffer هم‌زمان.
2. Session هر دو فایروال را مقایسه کنید.
3. Double NAT را عمدی بسازید و رفع کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| A ولی B نه | Internal | Policy/Route |
| B ولی C نه | Transit | VLAN |
| C ولی D نه | Edge | Policy |
| Src نادرست در Log | Double NAT | nat disable |

### جمع‌بندی

Packet Walk با چهار نقطه‌ی Sniffer؛ NAT فقط Edge؛ Session هر دو فایروال؛ Route برگشت در Edge؛ Double NAT ردیابی را خراب می‌کند.

### تمرین و ارزیابی

**ت1.** (ساده) NAT کجا انجام می‌شود؟ *(پاسخ: 15-5-ت1)*

**ت2.** (ساده) در جریان B، Internal نقش دارد؟ *(پاسخ: 15-5-ت2)*

**ت3.** (متوسط) Hairpin چرا مشکل می‌سازد؟ *(پاسخ: 15-5-ت3)*

**ت4.** (متوسط) Split DNS چیست؟ *(پاسخ: 15-5-ت4)*

**ت5.** (سخت) Session فقط در Internal است؛ علت؟ *(پاسخ: 15-5-ت5)*

**ت6.** (سخت، طراحی) Runbook سه‌جریانی. *(پاسخ: 15-5-ت6)*

**Q1.** Quick quiz (English): How can internal users reach an internal web server by its public name? *(پاسخ: 15-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Un-NAT | Reverse translation | ترجمه‌ی معکوس |

- *Document the packet walk in a runbook.* ← Packet Walk را در Runbook مستند کنید.

### کارت Lab

**کارت Lab:** Walk (اجرا نشده). **Evidence:** `03-ops/walk-arch2.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Packet flow
- FortiOS 7.0: Virtual IPs

<a id="l-15-6"></a>

## درس 15-6 — خرابی‌ها و آزمون G6: Edge، Internal، DMZ و گزارش RCA

**فصل 15 · بازنویسی عمیق · پیش‌نیاز: ۱۵-۱ تا ۱۵-۵ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. خرابی‌های Edge، Internal و DMZ را تفکیک کنید.
2. با ده‌گامی و Packet Walk علت را محلی‌سازی کنید.
3. RCA بنویسید.
4. آزمون G6 را با Rubric بشناسید.
5. نقش Rollback و Change را بدانید.
6. اثر خرابی هر دستگاه را تحلیل کنید (بدون HA).

### چرا باید یاد بگیریم؟

دو دستگاه یعنی دو نقطه‌ی خطا. سؤال اول در بحران: «مشکل از Edge است یا Internal یا بین‌شان؟». بدون محلی‌سازی، هر دو را زیر و رو می‌کنید و تغییرات تصادفی خطای جدید می‌سازد. G6 این مهارت را می‌سنجد.

### اثر خرابی هر دستگاه

| خرابی | اثر |
|---|---|
| Edge Down | اینترنت و DMZ قطع؛ داخلی بین Zoneها ادامه |
| Internal Down | Users/Servers قطع؛ DMZ و Edge سالم |
| لینک Transit | Users بدون اینترنت؛ DMZ سالم |
| Policy اشتباه Edge | DMZ یا اینترنت |
| Route برگشت | پاسخ گم |

### روش محلی‌سازی

1. Scope: کدام Zone/سرویس؟
2. Sniffer A–D (درس قبل): نقطه‌ی قطع.
3. در همان فایروال: Route، Policy، NAT، Session.
4. رفع و آزمون.

### پرونده‌ها

**پرونده ۱ — Users اینترنت ندارند:** Sniffer: A، B، C دیده؛ D نه. Edge Policy 10 Disable (CHG شب). رفع: Enable. RCA: Change بدون آزمون پس از اجرا.

**پرونده ۲ — Web از اینترنت قابل‌دسترس نیست:** Lookup ⇒ policy 0. VIP درست؛ Policy 20 dstintf=port3 (اشتباه). رفع: port2. تأیید: Session DNAT.

**پرونده ۳ — Users به App نمی‌رسند:** Internal Lookup ⇒ policy 0؛ HOST-APP IP قدیمی. رفع: آدرس. آزمون منفی DB هنوز Deny.

**پرونده ۴ — ترکیبی:** Route برگشت پاک شد + Policy تغییر. یکی‌یکی رفع.

### قالب RCA

``` text
Incident : Users no internet, 40 users, 25 min
Detect   : helpdesk call 09:05
Localize : Sniffer A-C ok, D missing -> Edge policy 10
Cause    : policy 10 disabled during change CHG-310
Fix      : enable policy 10
Prevent  : post-change smoke test, peer review
```

### آزمون G6

سه خرابی تزریقی (Edge Policy، Internal Route، DMZ VIP).

| معیار | امتیاز |
|---|---|
| محلی‌سازی با Sniffer | 25 |
| Evidence (Lookup/Session) | 25 |
| رفع صحیح | 25 |
| آزمون منفی/RCA | 15 |
| صداقت (ثبت اشتباه) | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Zone

«فقط DMZ قطع». Sniffer Edge port2: نه Internal؛ Edge Policy 20 بررسی.

#### مثال متوسط — Transit

همه‌ی Zoneهای داخلی بی‌اینترنت، DMZ سالم. Sniffer B ولی C نه ⇒ Transit (VLAN/کابل). رفع و تأیید.

#### مثال متوسط — Rollback

Policy جدید Edge اینترنت را قطع کرد. Rollback ۲ دقیقه‌ای (Revision) سرویس را برگرداند؛ سپس RCA.

#### مثال سخت — دو خرابی

Edge Policy 20 اشتباه + Internal Route پاک. ترتیب: ۱) Route (Users) ۲) آزمون ۳) Policy (DMZ) ۴) آزمون؛ ثبت جدا. اگر هم‌زمان تغییر دهید، نمی‌دانید کدام اثر داشت.

#### مثال سخت — Edge Down

Edge قطع؛ DMZ و اینترنت رفت. داخلی بین Zone‌ها کار می‌کند. نتیجه: بدون HA، Edge SPOF. توصیه: HA/ISP دوم (فصل بعد).

### Lab هدایت‌شده (اجرا نشده)

1. سه خرابی را بسازید.
2. محلی‌سازی با A–D.
3. RCA.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| همه‌جا تغییر | بی‌محلی‌سازی | Sniffer |
| Rollback ندارید | Change بی‌طرح | Backup |
| خطای دوباره | آزمون ناقص | Smoke test |

### جمع‌بندی

محلی‌سازی با Sniffer چهارنقطه‌ای؛ رفع یکی‌یکی؛ RCA و Rollback؛ دو فایروال بدون HA دو SPOF دارد.

### تمرین و ارزیابی

**ت1.** (ساده) Route برگشت چرا مهم است؟ *(پاسخ: 15-6-ت1)*

**ت2.** (ساده) policy 0 یعنی؟ *(پاسخ: 15-6-ت2)*

**ت3.** (متوسط) NAT دوباره چه علامتی دارد؟ *(پاسخ: 15-6-ت3)*

**ت4.** (متوسط) چرا Evidence از هر دو فایروال؟ *(پاسخ: 15-6-ت4)*

**ت5.** (سخت) دو عیب هم‌زمان را چگونه جدا می‌کنید؟ *(پاسخ: 15-6-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست پیشگیری. *(پاسخ: 15-6-ت6)*

**Q1.** Quick quiz (English): Why should faults be fixed one at a time? *(پاسخ: 15-6-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RCA | Root Cause Analysis | تحلیل ریشه‌ای |

- *Collect evidence from both firewalls.* ← از هر دو فایروال شواهد جمع کنید.

### کارت Lab

**کارت Lab:** G6 (اجرا نشده). **Evidence:** `03-ops/rca-arch2.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Troubleshooting

## پاسخ‌های فصل 15

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 15-1

**15-1-ت1** — تا Session و عیب‌یابی ساده بماند و NAT دوباره پیچیدگی نسازد.

**15-1-ت2** — به Edge (Transit).

**15-1-ت3** — تا بسته‌ی برگشتی/پاسخ را به Internal برگرداند.

**15-1-ت4** — اگر وب‌سرور هک شود، مهاجم مستقیم به DB نرسد؛ فقط App.

**15-1-ت5** — نمودار، آدرس، ماتریس، مسیر، آزمون.

**15-1-ت6** — بازبینی فصلی، Config مقایسه‌ی خودکار، Comment/Owner.

**15-1-Q1** — To keep traffic analysis simple and avoid double translation.


### پاسخ‌های بازنویسی عمیق درس 15-2

**15-2-ت1** — Deny با Log.

Policy 99 آخرین قاعده با Deny و Log است؛ Implicit Deny Log ندارد و برای Alert/ممیزی نیاز به Deny صریح است.

**15-2-ت2** — DNAT.

VIP ترجمه‌ی مقصد (DNAT) از IP عمومی به IP داخلی سرور را انجام می‌دهد؛ Policy باید به آن اشاره کند.

**15-2-ت3** — سطح حمله.

port1 (WAN) بدون Admin access تا مدیریت از اینترنت قابل‌دسترس نباشد و سطح حمله کم شود.

**15-2-ت4** — SSH به VIP.

آزمون منفی: SSH به VIP (پورت 22) باید رد شود و Log با policyid=99 ثبت شود.

**15-2-ت5** — Policy، Route، Session.

VIP جواب نمی‌دهد: Policy dst=VIP، Route داخلی سرور، Session و DNAT و Log را بررسی کنید.

**15-2-ت6** — جدول.

ماتریس Edge: Transit→WAN (SNAT)، WAN→DMZ (VIP)، DMZ→Transit (فقط App) و Deny صریح.

**15-2-Q1** — An explicit deny with logging.

An explicit deny with logging should end the Edge rule list.

### پاسخ‌های بازنویسی عمیق درس 15-3

**15-3-ت1** — NAT دوباره Log و رد‌یابی را خراب می‌کند و Edge IP واقعی را نمی‌بیند؛ ترجمه یک‌بار روی Edge کافی است.

**15-3-ت2** — به Edge از طریق Transit (10.255.0.1).

Default Internal به Edge از طریق Transit (10.255.0.1) است.

**15-3-ت3** — سرور آلوده نباید به C2 اینترنت وصل شود؛ فقط مقاصد Update و HTTPS لازم باز می‌ماند.

**15-3-ت4** — تا فقط Admin به مدیریت برسد و سطح حمله کم شود.

**15-3-ت5** — Lookup، Debug flow، Sniffer port1 Internal و port2 Edge، Route برگشت، Transit؛ Evidence هر دو سمت.

**15-3-ت6** — طبق جدول: Users→Internet، Users→App 443، Mgmt→SSH، Servers→Update، Deny با Log.

**15-3-Q1** — Because translating twice hides real source addresses and complicates logging and troubleshooting.


### پاسخ‌های بازنویسی عمیق درس 15-4

**15-4-ت1** — اگر وب‌سرور هک شود، مهاجم مستقیم به DB نرسد؛ فقط App مجاز است.

**15-4-ت2** — Implicit Deny Log ندارد؛ Deny صریح برای Log و Alert لازم است.

**15-4-ت3** — تا سرور آلوده نتواند داده خارج کند یا به C2 وصل شود.

**15-4-ت4** — تلاش برای ارتباط ممنوع و تأیید اینکه رد می‌شود و Log ثبت می‌شود.

**15-4-ت5** — Alert، Quarantine، بررسی Log، حذف دسترسی؛ مستند.

**15-4-ت6** — طبق جدول؛ Alert بر policyid=61.

ماتریس سه‌لایه: Internet→Web 443، Web→App 8443، App→DB 1433، Web→DB ممنوع و Alert روی Deny Web→DB (policyid=61).

**15-4-Q1** — To limit lateral movement and expose the database to fewer systems.


### پاسخ‌های بازنویسی عمیق درس 15-5

**15-5-ت1** — فقط روی Edge.

NAT فقط روی Edge انجام می‌شود تا Log و Session ساده بماند.

**15-5-ت2** — خیر؛ ترافیک فقط از Edge به DMZ می‌رود.

در جریان Internet→Web فقط Edge دخیل است؛ Internal نقشی ندارد.

**15-5-ت3** — پاسخ سرور مستقیم به کاربر می‌رود یا مسیر برگشت از فایروال دور می‌زند.

**15-5-ت4** — DNS داخلی IP داخلی را برای کاربران داخلی می‌دهد.

**15-5-ت5** — بسته به Edge نمی‌رسد؛ Transit/Route/ACL.

**15-5-ت6** — قالب بالا.

Runbook سه‌جریانی: برای هر جریان مسیر، Policyها، NAT و دستورهای اثبات.

**15-5-Q1** — Use split DNS so the name resolves to the internal address.


### پاسخ‌های بازنویسی عمیق درس 15-6

**15-6-ت1** — Edge باید پاسخ را به Internal برگرداند؛ بدون Route به Default و ISP می‌رود و Drop می‌شود.

**15-6-ت2** — Implicit Deny؛ Policy مطابق نیست.

**15-6-ت3** — IP مبدأ همه‌ی کاربران در Edge Log یکسان است.

**15-6-ت4** — تا معلوم شود بسته به کدام فایروال می‌رسد و کجا گم می‌شود.

**15-6-ت5** — یکی‌یکی رفع و آزمون؛ ثبت اثر هر تغییر.

**15-6-ت6** — Route، Policy، NAT، Backup، آزمون منفی، Monitoring Transit.

**15-6-Q1** — To know which change solved the problem and avoid masking the root cause.

### پاسخ‌های درس افزوده‌ی 15-0 (فصل 15)

**15-0-ت1** — ناحیه‌ی واسط برای سرورهای در معرض اینترنت تا نفوذ به آن‌ها مستقیماً به شبکه‌ی داخلی نرسد.

**15-0-ت2** — برای حفظ آدرس واقعی در Log و جلوگیری از Double NAT و عیب‌یابی سخت؛ Internal فقط Routing می‌کند.

**15-0-ت3** — Client→VIP روی Edge (DNAT به وب DMZ)→Policy WAN→DMZ→وب به App از Internal (Policy DMZ→SRV 8080)→App به DB داخل Internal؛ برگشت از همان Sessionها.

**15-0-ت4** — آدرس مبدأ همه یک IP می‌شود و منبع واقعی در Log سرور پنهان می‌ماند.

**15-0-ت5** — Policy حداقلی DMZ→SRV (فقط 8080)، Deny+Log و Alert روی تلاش‌های ممنوع، Segmentation/Least Privilege و نداشتن اعتبارنامه‌ی داخلی روی DMZ.

**15-0-ت6** — دارایی‌های حساس و بودجه کافی: دو فایروال؛ بودجه کم: تک‌فایروال با DMZ، UTM، HA و Patch دقیق؛ تصمیم با ریسک × اثر.

**15-0-Q1** — To keep the original source address in logs and avoid double-NAT troubleshooting problems.

# پایان بخش ۵ (فصل‌های ۱۳ تا ۱۵)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- Policy/NAT/VIP/Session/Shadow؛ Sniffer، Debug Flow، iprope، MTU/MSS؛ معماری دوفایروالی با DMZ و سه‌لایه.

## ۲) آزمون پایان سه فصل
**س1** — First Match و Implicit deny؟

**س2** — Policy NAT در برابر Central NAT؟

**س3** — انواع IP Pool؟

**س4** — VIP چه می‌کند و چرا Policy لازم است؟

**س5** — چرا filter قبل از session list؟

**س6** — Policy 0 در Debug Flow؟

**س7** — Sniffer verbose 4؟

**س8** — دو ابزار شناسایی Policy مطابق؟

**س9** — MSS Clamp برای چیست؟

**س10** — چرا Web به DB نه؟

**س11** — NAT کجا در معماری ۲؟

**س12** — خرابی «Return Route» علامت؟


## ۳) پاسخ آزمون
- **س1:** اولین Policy مطابق؛ Deny ضمنی در پایان.
- **س2:** NAT داخل Policy در برابر جدول جدا.
- **س3:** overload، one-to-one، fixed-port-range، port-block-allocation.
- **س4:** DNAT؛ VIP فقط نگاشت است.
- **س5:** حجم خروجی/CPU.
- **س6:** Implicit deny.
- **س7:** با نام Interface.
- **س8:** iprope lookup و Policy Lookup.
- **س9:** حل بسته‌ی بزرگ در Tunnel/MTU کم.
- **س10:** Least Privilege.
- **س11:** Edge.
- **س12:** TCP برقرار نمی‌شود.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| Policy/NAT | L3-L4 | G5 |
| عیب‌یابی FortiOS | L3 | آزمون فصل ۱۴ |
| معماری ۲ | L3 | G6 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. همه‌ی Labها اجرا نشده. 2. سینتکس `central-snat-map`، `tcp-mss-*`، `execute log filter` و `fwpolicy-implicit-log` در 7.0.3 `Unverified`. 3. VM FortiGate با ≥ 2 GB لازم است؛ دو FGT همزمان فشار RAM.

## ۶) پیش‌نیازهای بخش بعد
Lab معماری ۲ ساخته و Backup؛ لایسنس UTM (Needs-License) بررسی؛ Windows Server AD (فصل ۱۷).

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab ، `02-design/arch2.md` (خروجی دانشجو)

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۱۵ |
| آخرین درس تکمیل‌شده | ۱۵-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۱۶ |
| فایل تولیدشده | `course/Course_Part_05_Chapters_13-15.md` |
