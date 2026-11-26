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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. هشت جزء اصلی یک Firewall Policy را نام ببرد و نقش هرکدام را توضیح دهد.
2. قاعده‌ی First Match و Implicit Deny را با یک مثال عددی اثبات کند.
3. ترتیب Policy را برای یک سناریوی واقعی طراحی کند.
4. Logging (all/utm/disable) و Log ضمنی Deny را تنظیم کند.
5. با GUI و CLI یک Policy بسازد و با Session/Log آن را تأیید کند.
6. خطاهای رایج (Policy بدون Route، ترتیب غلط، Service اشتباه) را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

تصور کنید در ورودی یک ساختمان اداری یک دفترچه‌ی قوانین دارید. نگهبان هر مراجعه‌کننده را با قوانین از اولین سطر مقایسه می‌کند؛ به محض اینکه یک سطر با او جور شد، همان سطر اجرا می‌شود و بقیه‌ی دفترچه را نمی‌خواند. اگر هیچ سطری جور نشد، اجازه‌ی ورود نمی‌دهد. Firewall Policy در FortiGate دقیقاً همین دفترچه است.

نتیجه‌ی عملی: «ترتیب» به‌اندازه‌ی «محتوا» مهم است. یک Policy درست که در جای غلط قرار گرفته یا هرگز اجرا نمی‌شود (Shadowed) یا قاعده‌ی دیگری را بی‌اثر می‌کند. در این درس یاد می‌گیرید هر Policy از چه اجزایی ساخته می‌شود، چطور FortiGate بین آن‌ها انتخاب می‌کند و چطور با Log ثابت کنید که چه اتفاقی افتاده است.

### ۳) توضیح عمیق فنی

#### ۱) اجزای Policy

| جزء | نقش | نمونه |
|---|---|---|
| Name | نام قابل‌خواندن | USERS-to-INTERNET |
| Incoming Interface | از کدام Interface/Zone وارد شده | ZN-USERS |
| Outgoing Interface | به کدام Interface/Zone می‌رود (از Route تعیین می‌شود) | port1 |
| Source | آدرس مبدأ (Address، User، Device) | NET-USERS |
| Destination | آدرس مقصد | all |
| Schedule | زمان فعال‌بودن | always |
| Service | پروتکل/پورت | HTTP، HTTPS، DNS |
| Action | ACCEPT یا DENY (یا IPsec) | ACCEPT |
| NAT | ترجمه‌ی مبدأ | Enable (Outgoing Interface Address) |
| Security Profiles | AV/IPS/Web Filter/... | Needs-License |
| Log | چه چیزی ثبت شود | All Sessions |

نکته: Outgoing Interface را FortiGate از **جدول مسیریابی** پیدا می‌کند و بعد دنبال Policyای می‌گردد که برای همین جفت (ورودی، خروجی) باشد. پس اگر Route نباشد، به Policy هم نمی‌رسد.

#### ۲) First Match

``` text
Policy 1: ZN-USERS -> port1  src NET-MGMT        service ALL   ACCEPT
Policy 2: ZN-USERS -> port1  src NET-USERS       service HTTP,HTTPS,DNS  ACCEPT
Policy 3: ZN-USERS -> port1  src all             service ALL   DENY
(implicit) deny all
```

بسته‌ای از NET-USERS با سرویس SSH: Policy 1 نه (مبدأ فرق دارد)، Policy 2 نه (سرویس فرق دارد)، Policy 3 بله ⇒ Deny. اگر Policy 3 بالاتر از 2 بود، همه‌ی ترافیک NET-USERS رد می‌شد و Policy 2 هرگز اجرا نمی‌شد (Shadow).

#### ۳) Implicit Deny و Log آن

در پایان لیست یک Deny ضمنی هست که **Log ندارد** مگر اینکه فعال کنید:

``` text
config log setting
 set fwpolicy-implicit-log enable
end
```

این دستور برای 7.0 گزارش شده ولی روی Image شما `Unverified` است. جایگزین پایدار: یک Policy صریح Deny در انتها با Log All (در GUI به آن Policy ID مشخص می‌دهد).

#### ۴) Log

| گزینه | مقدار | کاربرد |
|---|---|---|
| Disabled | هیچ Log | فقط ترافیک بی‌اهمیت |
| Security Events | فقط رویدادهای UTM | کاهش حجم |
| All Sessions | شروع/پایان هر Session | عیب‌یابی و ممیزی |

Log همه‌ی Sessionها روی سخت‌افزار کوچک CPU/Disk می‌خورد؛ برای Deny و Policyهای حساس همیشه روشن، برای ترافیک وب انبوه با مصرف سنجیده.

#### ۵) ID و Name

ID عددی یکتا و ثابت است (برای Log و Debug)؛ ترتیب با ID یکی نیست. هر Policy باید Name و Comment (چرا ساخته شد، چه کسی) داشته باشد.

#### ۶) Policy Lookup

``` text
diagnose firewall iprope lookup 10.10.0.5 40000 203.0.113.10 443 tcp port2
```

نشان می‌دهد کدام Policy برای این جریان انتخاب می‌شود (`Unverified` تا Lab). در GUI معادل «Policy Lookup» در صفحه‌ی Firewall Policy است.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترتیب | خاص به عام؛ Deny صریح در انتها |
| Log | All برای Deny و حساس؛ کم‌تر برای انبوه |
| نام‌گذاری | SRC-to-DST-SERVICE + Comment |
| Interface | Zone به‌جای Interface برای خوانایی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ورودی: کاربر 10.10.0.5 به 203.0.113.10:443. مراحل: ۱) Route: خروج port1. ۲) Policy 2 را با Source، Service و Interface مطابقت می‌دهیم. ۳) مطابق است ⇒ ACCEPT، Log All. پاسخ: Session ساخته می‌شود و در `diagnose sys session list` با policy_id=2 دیده می‌شود.

**متوسط (تحلیل ترتیب):** سازمان گزارش داد «سایت داخلی باز نمی‌شود». Policy 5 (`USERS→SERVERS HTTPS accept`) پایین‌تر از Policy 3 (`USERS→all DENY`) است. مراحل: ۱) Policy Lookup نشان می‌دهد Policy 3. ۲) hit-count Policy 5 صفر است. ۳) علت: Shadow. رفع: Policy 5 را بالاتر از 3 ببرید (یا Policy 3 را محدود کنید). آزمون: Lookup دوباره ⇒ Policy 5؛ از کلاینت HTTPS موفق.

**سخت (طراحی و Log):** نیاز: کاربران وب را ببینند، سرور DB فقط از App در دسترس، همه‌ی Denyها ثبت شوند و دیسک کوچک است. طراحی: ۱) Policyهای خاص در بالا (App→DB 1433، Users→Web 443). ۲) Users→Internet با Log Security Events + Web/DNS. ۳) Deny صریح انتهایی با Log All برای ممیزی. ۴) Logها به FortiAnalyzer/Syslog (فصل ۲۴). معیار پذیرش: آزمون منفی (Users→DB) رد و در Log ظاهر شود؛ حجم Log روزانه < ظرفیت دیسک.

### ۶) پیاده‌سازی از مسیر GUI

1. Policy & Objects → Firewall Policy → Create New.
2. Name، Incoming/Outgoing Interface، Source، Destination، Schedule، Service را پر کنید.
3. Action = ACCEPT؛ NAT را بر اساس نیاز؛ Log = All Sessions.
4. Comments را بنویسید؛ OK.
5. با کشیدن (Drag) ترتیب را اصلاح کنید؛ ستون ID و Hit Count را فعال کنید.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall policy
 edit 2
  set name "USERS-to-INTERNET"
  set srcintf "ZN-USERS"
  set dstintf "port1"
  set srcaddr "NET-USERS"
  set dstaddr "all"
  set action accept
  set schedule "always"
  set service "HTTP" "HTTPS" "DNS"
  set nat enable
  set logtraffic all
  set comments "Internet browsing; owner NOC"
 next
end
show firewall policy 2
diagnose firewall iprope lookup 10.10.0.5 40000 203.0.113.10 443 tcp port2
```

### ۸) Verification (اثبات صحت)

- Policy Lookup همان ID مورد انتظار را می‌دهد.
- Hit Count بعد از آزمون افزایش می‌یابد.
- Log با policyid و action=accept دیده می‌شود.
- آزمون منفی (سرویس غیرمجاز) در Log با action=deny.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy تطابق نمی‌کند | Route و Interface ورودی/خروجی | Routing/Interface Policy را یکی کنید |
| Policy بالاتر همه چیز را می‌گیرد | Hit Count و Lookup | ترتیب/Shadow |
| Deny در Log نیست | Implicit Deny | Deny صریح با Log |
| Log دیسک را پر می‌کند | حجم Log | Log Security Events یا Syslog |

### ۱۰) نکات امنیتی

- Policy با Source/Destination/Service برابر `all` فقط با دلیل مستند.
- Deny صریح انتهایی با Log.
- تغییر Policy را با Change ticket ثبت کنید.

### ۱۱) جمع‌بندی مفهومی

- Policy = دفترچه‌ی قوانین با First Match.
- Route قبل از Policy انتخاب می‌شود.
- Implicit Deny بی‌Log است؛ Deny صریح بسازید.
- ترتیب، Hit Count و Lookup ابزار اثبات‌اند.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) First Match یعنی چه؟ *(پاسخ: 13-1-ت1)*

**ت2.** (ساده) چرا Outgoing Interface را خود ما انتخاب می‌کنیم ولی Route تعیین می‌کند؟ *(پاسخ: 13-1-ت2)*

**ت3.** (متوسط) Policy 3 (Deny all) بالای Policy 2 است. چه می‌شود و چطور کشف می‌کنید؟ *(پاسخ: 13-1-ت3)*

**ت4.** (متوسط) تفاوت Log All Sessions و Security Events؟ *(پاسخ: 13-1-ت4)*

**ت5.** (سخت) برای DB فقط از App مجاز باشد. Policyها را بنویسید و آزمون منفی را شرح دهید. *(پاسخ: 13-1-ت5)*

**ت6.** (سخت، طراحی) استاندارد Policy برای سازمان ۳ شعبه‌ای. *(پاسخ: 13-1-ت6)*

**Q1.** Quick quiz (English): Why does an explicit deny rule with logging help compared to the implicit deny? *(پاسخ: 13-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Policy | Firewall policy | قاعده‌ی فایروال |
| Shadow | Shadowed rule | قاعده‌ی پنهان‌شده |
| Hit count | Policy hit count | شمارنده‌ی تطابق |

- *The first matching policy wins.* ← اولین Policy مطابق برنده است.
- *Always log denied traffic.* ← ترافیک ردشده را همیشه Log کنید.

### ۱۴) کارت Lab

**کارت Lab:** سه Policy و آزمون ترتیب (اجرا نشده). **Evidence:** `03-ops/policy-review.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- FortiOS 7.0 CLI Reference: config firewall policy

<a id="l-13-2"></a>

## درس 13-2 — NAT در FortiGate: Policy NAT، IP Pool، Central NAT و انتخاب درست

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۴، ۱۳-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Source NAT را با Outgoing Interface Address و IP Pool مقایسه کند.
2. چهار نوع IP Pool را بشناسد و برای هر کدام کاربرد بگوید.
3. Central NAT را در برابر Policy NAT بسنجد و فعال‌سازی آن را بداند.
4. تعداد Sessionهای ممکن با یک IP عمومی را برآورد کند.
5. خطاهای رایج NAT (برگشت نیست، Pool خالی، Central NAT فراموش) را رفع کند.

### ۲) مفهوم پایه: چیست و چرا؟

یک ساختمان ۵۰۰ نفره با یک شماره‌ی تلفن بیرونی را در نظر بگیرید. وقتی کارمندی تماس می‌گیرد، تلفن‌چی شماره‌ی بیرونی را می‌گذارد و یادش می‌ماند «داخلی 214 زنگ زد». جواب برمی‌گردد به همان داخلی. این PAT است. اگر شرکت چند شماره‌ی بیرونی داشته باشد (Pool)، می‌شود شماره را به‌صورت دلخواه یا ثابت به افراد داد.

مسئله‌ی عملی: «اینترنت دارم ولی سرور سازمانی ما را Block کرده چون IP مشترک است»؛ یا «ترافیک برگشت نمی‌رسد». پاسخ در NAT است.

### ۳) توضیح عمیق فنی

#### ۱) NAT داخل Policy (پیش‌فرض)

``` text
config firewall policy
 edit 2
  set nat enable
  ! default: use outgoing interface address
 next
end
```

مبدأ با IP Interface خروجی ترجمه می‌شود (PAT). ساده‌ترین حالت.

#### ۲) IP Pool

| نوع | رفتار | کاربرد |
|---|---|---|
| Overload | چند Host با یک/چند IP، پورت‌ها اشتراکی | پیش‌فرض اینترنت |
| One-to-One | هر IP داخلی یک IP عمومی ثابت | سرویس نیازمند IP اختصاصی |
| Fixed Port Range | هر Host بازه‌ی پورت ثابت | ردیابی قانونی |
| Port Block Allocation | بلوک پورت به هر Host | Log کم‌حجم CGN |

``` text
config firewall ippool
 edit "POOL-WAN"
  set type overload
  set startip 203.0.113.20
  set endip 203.0.113.21
 next
end
config firewall policy
 edit 2
  set ippool enable
  set poolname "POOL-WAN"
 next
end
```

نکته: IP Pool باید آدرسی باشد که **ISP به شما Route می‌کند** و ARP/Proxy-ARP برای آن (در صورت لزوم) تنظیم شود.

#### ۳) ظرفیت

``` text
Ports per IP ~ 65535 - 1024 = ~64500
Max concurrent sessions per public IP (to ONE destination ip:port) ~ 64500
```

فرمول برای همان Destination:Port؛ برای مقاصد متفاوت بیشتر است. با ۱۰۰۰ کاربر و ۵۰ Session هر کدام = ۵۰۰۰۰ ⇒ نزدیک سقف؛ Pool دو IP.

#### ۴) Central NAT

در 7.0 ترجمه از Policy جدا و در جدول جدا (`config firewall central-snat-map`) مدیریت می‌شود:

``` text
config system settings
 set central-nat enable
end
config firewall central-snat-map
 edit 1
  set srcintf "ZN-USERS"
  set dstintf "port1"
  set orig-addr "NET-USERS"
  set dst-addr "all"
  set nat-ippool "POOL-WAN"
 next
end
```

بعد از فعال‌سازی، گزینه‌ی NAT در Policy کار نمی‌کند و باید Central SNAT Map ساخت: «NAT فعال شد ولی اثر نکرد» ⇒ اغلب همین.

#### ۵) انتخاب

| معیار | Policy NAT | Central NAT |
|---|---|---|
| سادگی | بله | نیاز به نگهداری جدول جدا |
| ترجمه‌های پیچیده/چند Pool | سخت | مناسب |

#### ۶) ترتیب

SNAT بعد از Policy (مبدأ در Policy آدرس داخلی است) و DNAT/VIP قبل از Policy.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| PAT ساده یا Pool | Overload Pool برای بیش از ۴۰k Session |
| Central NAT | فقط وقتی ترجمه‌ها زیاد/پیچیده |
| IP Pool | IP تحویلی ISP؛ ARP/Route را هماهنگ کنید |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ۲۰۰ کاربر از یک IP WAN: Policy با `nat enable`؛ `diagnose sys session list` نشان می‌دهد `hook=post dir=org act=snat 10.10.0.5:40000->203.0.113.10:443(198.51.100.2:40000)`. پاسخ: PAT با IP Interface.

**متوسط (ظرفیت):** ۱۰۰۰ کاربر با میانگین ۵۰ Session هم‌زمان به یک سرویس 443. مراحل: ۱) کل Session = 1000×50 = 50000. ۲) سقف هر IP ≈ 64500. ۳) حاشیه‌ی ایمنی کم؛ پاسخ: Pool با دو IP (Overload) تا ظرفیت ≈ 129000 و حاشیه‌ی ۵۰٪. آزمون: بار با iperf/ab و مشاهده‌ی `nat-pool exhausted` در لاگ.

**سخت (Central NAT):** پس از فعال‌سازی Central NAT کاربران اینترنت را از دست دادند. مراحل: ۱) Policy ها `nat enable` دارند ولی Central NAT فعال است. ۲) `show firewall central-snat-map` خالی. ۳) علت: SNAT Map نیست. رفع: ساخت Map برای ZN-USERS→port1. آزمون: Session با snat؛ Log. درس: قبل از فعال‌سازی Central NAT نقشه‌ی ترجمه را آماده کنید و در Maintenance Window.

### ۶) پیاده‌سازی از مسیر GUI

1. Policy & Objects → IP Pools → Create New (Type Overload، Start/End IP).
2. Firewall Policy → NAT = Enable → Dynamic IP Pool → انتخاب Pool.
3. برای Central NAT: System → Feature Visibility → Central SNAT را روشن؛ Policy & Objects → Central SNAT → Create New.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall ippool
 edit "POOL-WAN"
  set type overload
  set startip 203.0.113.20
  set endip 203.0.113.21
 next
end
config firewall policy
 edit 2
  set nat enable
  set ippool enable
  set poolname "POOL-WAN"
 next
end
diagnose sys session filter src 10.10.0.5
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- Session دارای NAT مبدأ جدید است.
- Source IP در سرور مقصد همان Pool است.
- ظرفیت: عدم Pool exhausted در Log.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| برگشت نیست | Route برگشت/NAT | Route و ARP |
| NAT اثر ندارد | Central NAT فعال؟ | SNAT Map |
| Pool exhausted | Session شمار | IP بیشتر/Port block |
| IP Pool کار نمی‌کند | ISP Route | هماهنگی با ISP |

### ۱۰) نکات امنیتی

- اطلاعات NAT برای رد‌یابی ثبت شود.
- Pool را فقط برای Zoneهای لازم.

### ۱۱) جمع‌بندی مفهومی

- PAT پیش‌فرض.
- IP Pool: Overload/One-to-One/Fixed/PBA.
- ظرفیت ≈ 64500 Session به ازای هر IP و مقصد.
- Central NAT جدول جدا و Policy NAT را کنار می‌گذارد.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) PAT چیست؟ *(پاسخ: 13-2-ت1)*

**ت2.** (ساده) تفاوت Overload و One-to-One؟ *(پاسخ: 13-2-ت2)*

**ت3.** (متوسط) برآورد ظرفیت یک IP؟ *(پاسخ: 13-2-ت3)*

**ت4.** (متوسط) چرا پس از Central NAT اینترنت قطع شد؟ *(پاسخ: 13-2-ت4)*

**ت5.** (سخت) ۱۰۰۰ کاربر، ۸۰ Session هر نفر. *(پاسخ: 13-2-ت5)*

**ت6.** (سخت، طراحی) NAT برای سه Zone با Poolهای متفاوت. *(پاسخ: 13-2-ت6)*

**Q1.** Quick quiz (English): What happens to the NAT option in policies after Central NAT is enabled? *(پاسخ: 13-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PAT | Port Address Translation | ترجمه‌ی پورت |
| PBA | Port Block Allocation | تخصیص بلوک پورت |
| CGN | Carrier-Grade NAT | NAT مقیاس اپراتور |

- *The pool must be routed to you by the ISP.* ← ISP باید Pool را به شما Route کند.

### ۱۴) کارت Lab

**کارت Lab:** NAT و Pool (اجرا نشده). **Evidence:** `02-design/fgt-nat.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: NAT
- FortiOS 7.0: IP pools
- FortiOS 7.0: Central NAT

<a id="l-13-3"></a>

## درس 13-3 — VIP، Port-Forward و Hairpin NAT: انتشار امن سرویس داخلی

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۱، ۱۳-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. VIP را (Static NAT/Port Forward) بسازد و تفاوتشان را بگوید.
2. Policy مربوط به VIP را با مقصد صحیح بنویسد.
3. Hairpin NAT و Split DNS را مقایسه و انتخاب کند.
4. آزمون‌های مثبت/منفی و Security را اجرا کند.
5. خطاهای رایج (Policy نبود، Route، ARP) را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

سازمان می‌خواهد وب‌سرور داخلی از اینترنت در دسترس باشد. مثل این است که روی تابلوی ساختمان یک شماره‌ی اینترنتی بنویسید و پشت صحنه به داخلی 214 وصل شود. این کار VIP (Virtual IP) است. اما اگر کارمند داخل ساختمان هم از همان شماره‌ی عمومی استفاده کند، مسیر بسته به خود فایروال برمی‌گردد (Hairpin) و اگر درست طراحی نشود قطع می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) VIP

``` text
config firewall vip
 edit "VIP-WEB-443"
  set extintf "port1"
  set extip 203.0.113.10
  set mappedip "10.20.0.10"
  set portforward enable
  set protocol tcp
  set extport 443
  set mappedport 443
 next
end
```

بدون `portforward`، یک‌به‌یک (Static NAT) برای همه‌ی پورت‌ها؛ خطرناک‌تر. Port Forward حداقل سطح در معرض.

#### ۲) Policy

``` text
config firewall policy
 edit 20
  set name "INET-to-WEB"
  set srcintf "port1"
  set dstintf "ZN-DMZ"
  set srcaddr "all"
  set dstaddr "VIP-WEB-443"
  set action accept
  set schedule "always"
  set service "HTTPS"
  set logtraffic all
 next
end
```

مقصد = **اسم VIP** (نه IP داخلی). بدون این Policy ترافیک رد می‌شود.

#### ۳) ARP/Route

IP عمومی باید به FortiGate برسد: IP روی Interface WAN یا Route ISP؛ برای IP اضافی Proxy-ARP خودکار با VIP.

#### ۴) Hairpin

کاربر داخلی به 203.0.113.10: بسته به فایروال می‌رسد، DNAT می‌شود و به سرور در همان LAN/Zone می‌رود؛ سرور پاسخ مستقیم به کاربر می‌دهد (چون هم‌شبکه‌اند) و فایروال را دور می‌زند ⇒ Session ناقص. راه‌حل‌ها:

| روش | توضیح |
|---|---|
| Split DNS | DNS داخلی نام را به IP داخلی می‌دهد (توصیه) |
| SNAT برای Hairpin | `set nat-source-vip enable` یا Policy با NAT |

#### ۵) آزمون

``` text
curl -vk https://203.0.113.10 (from Internet)
diagnose sys session filter dst 203.0.113.10
diagnose sys session list
```

آزمون منفی: پورت دیگر (22) رد شود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Port Forward یا Static | Port Forward |
| Hairpin یا Split DNS | Split DNS |
| Zone سرور | DMZ جدا |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** VIP-WEB-443 + Policy؛ از اینترنت HTTPS باز می‌شود؛ Session با DNAT.

**متوسط (تحلیل):** VIP ساخته شد ولی سایت باز نمی‌شود: Policy نیست یا مقصد IP داخلی نوشته شده؛ رفع: Policy با dstaddr=VIP.

**سخت (Hairpin):** کاربران داخلی به نام عمومی نمی‌رسند ولی از اینترنت باز است. مراحل: ۱) DNS عمومی IP Public می‌دهد. ۲) Hairpin. رفع پیشنهادی: Split DNS؛ جایگزین: Policy داخلی با VIP و NAT. آزمون: از LAN و اینترنت.

### ۶) پیاده‌سازی از مسیر GUI

1. Policy & Objects → Virtual IPs → Create New.
2. Firewall Policy → Destination = VIP.
3. Service را روی پورت لازم محدود کنید.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall vip
 edit "VIP-WEB-443"
  set extintf "port1"
  set extip 203.0.113.10
  set mappedip "10.20.0.10"
  set portforward enable
  set extport 443
  set mappedport 443
 next
end
```

### ۸) Verification (اثبات صحت)

- آزمون از بیرون موفق.
- پورت‌های دیگر رد.
- Hairpin طبق طرح.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| باز نمی‌شود | Policy dst=VIP؟ | Policy |
| برگشت نیست | Route سرور | Default سرور به FW |
| داخلی نمی‌رسد | Hairpin | Split DNS |

### ۱۰) نکات امنیتی

- فقط پورت لازم.
- IPS/WAF قبل از VIP (Needs-License).

### ۱۱) جمع‌بندی مفهومی

- VIP=DNAT.
- Policy با نام VIP.
- Hairpin مشکل مسیر است نه NAT.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) VIP چیست؟ *(پاسخ: 13-3-ت1)*

**ت2.** (ساده) Policy باید به چه مقصدی اشاره کند؟ *(پاسخ: 13-3-ت2)*

**ت3.** (متوسط) چرا Port Forward امن‌تر است؟ *(پاسخ: 13-3-ت3)*

**ت4.** (متوسط) علت Hairpin؟ *(پاسخ: 13-3-ت4)*

**ت5.** (سخت) VIP کار نمی‌کند؛ مراحل بررسی. *(پاسخ: 13-3-ت5)*

**ت6.** (سخت، طراحی) انتشار سه سرویس. *(پاسخ: 13-3-ت6)*

**Q1.** Quick quiz (English): Why must the policy destination reference the VIP object? *(پاسخ: 13-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VIP | Virtual IP | آدرس مجازی |
| DNAT | Destination NAT | ترجمه‌ی مقصد |

- *Publish only the required port.* ← فقط پورت لازم را منتشر کنید.

### ۱۴) کارت Lab

**کارت Lab:** VIP (اجرا نشده). **Evidence:** `02-design/fgt-vip.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Virtual IPs

<a id="l-13-4"></a>

## درس 13-4 — Session Table: ساختار، Timeout، فیلتر و پاک‌سازی

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۱، ۱۱-۷، ۱۳-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. فیلدهای مهم یک Session را بخواند (proto، state، timeout، policy، NAT، offload).
2. Session را با فیلتر مناسب پیدا و تحلیل کند.
3. Timeout پیش‌فرض و Session-TTL را بشناسد و تنظیم کند.
4. تغییر Policy/Route را با Session قدیمی هماهنگ کند (clear).
5. پاک‌سازی Session را امن (فیلترشده) انجام دهد.
6. Session پر یا Leak را شناسایی کند.

### ۲) مفهوم پایه: چیست و چرا؟

می‌گویید «Policy را عوض کردم ولی اثر نکرد». اغلب Session قدیمی هنوز در جدول است و FortiGate برای بسته‌های ادامه‌دار Policy را دوباره نمی‌پرسد. Session Table حافظه‌ی فایروال است؛ بدون خواندن آن تفسیر رفتار فایروال حدس است.

### ۳) توضیح عمیق فنی

#### ۱) خواندن یک Session

``` text
session info: proto=6 proto_state=01 duration=35 expire=3565 timeout=3600 flags=00000000
origin-shaper= reply-shaper= per_ip_shaper=
class_id=0 ha_id=0 policy_dir=0 tunnel=/ vlan_cos=0/255
state=may_dirty npu
statistic(bytes/packets/allow_err): org=5320/42/1 reply=48200/55/1 tuples=2
orgin->sink: org pre->post, reply pre->post dev=5->3/3->5 gwy=198.51.100.1/10.10.0.5
hook=post dir=org act=snat 10.10.0.5:40000->203.0.113.10:443(198.51.100.2:40000)
hook=pre dir=reply act=dnat 203.0.113.10:443->198.51.100.2:40000(10.10.0.5:40000)
policy_id=2 auth_info=0 chk_client_info=0 vd=0
```

| فیلد | معنی |
|---|---|
| proto | 6=TCP، 17=UDP، 1=ICMP |
| proto_state | وضعیت (TCP: 01=Established) |
| expire/timeout | زمان باقی‌مانده/کل |
| policy_id | Policy که اجازه داد |
| hook/act | SNAT/DNAT انجام‌شده |
| npu | Offload شده |

#### ۲) فیلتر

``` text
diagnose sys session filter clear
diagnose sys session filter src 10.10.0.5
diagnose sys session filter dport 443
diagnose sys session list
diagnose sys session filter clear
```

همیشه فیلتر را قبل از `clear` تنظیم کنید؛ `diagnose sys session clear` بدون فیلتر **همه‌ی** Sessionها را می‌بندد (قطع سراسری).

#### ۳) Timeout

| نوع | پیش‌فرض تقریبی |
|---|---|
| TCP Established | 3600 s |
| TCP Half-open | ثانیه‌ها |
| UDP | 60 s |
| ICMP | ثانیه‌ها |

``` text
config system session-ttl
 set default 3600
 config port
  edit 5000
   set protocol 6
   set timeout 7200
   set end-port 5000
  next
 end
end
```

مقادیر پیش‌فرض `Unverified` برای نسخه‌ی شما؛ با `get system session-ttl` ببینید.

#### ۴) Policy تغییر کرد؛ Session چه می‌شود؟

FortiGate Sessionهای موجود را معمولاً تا انقضا نگه می‌دارد؛ برای اعمال فوری Policy جدید، Session مشخص را پاک کنید (با فیلتر). تنظیم `set auth-timeout` یا «session re-validate» در 7.0 تغییر Policy را بازبینی می‌کند (`Unverified`).

#### ۵) Session Leak

تعداد Session رو به افزایش: `get system performance status` و `diagnose sys session full-stat`. علل: Timeout طولانی، DoS، UDP بی‌پایان.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Timeout | Per-port برای سرویس‌های طولانی |
| Clear | فقط با فیلتر |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Session بالا: `proto=6`، `policy_id=2`، `act=snat`؛ یعنی TCP، Policy 2، SNAT شده. پاسخ: همان انتظار.

**متوسط (Session قدیمی):** Policy 5 (اجازه‌ی FTP) حذف شد ولی FTP کار می‌کند. مراحل: ۱) Session با dport 21 هنوز هست و policy_id=5. ۲) فیلتر dport 21 و `diagnose sys session clear`. ۳) FTP جدید رد می‌شود. درس: بعد از تغییر Policy حساس Session مربوطه را پاک کنید.

**سخت (Timeout و SSH):** SSH ادمین هر ۵ دقیقه قطع می‌شود. مراحل: ۱) Session expire را با `session list` ببینید. ۲) timeout 300 برای port 22 در `session-ttl`. ۳) افزایش ۸۶۴۰۰ برای پورت 22 یا Keepalive سمت کلاینت. ۴) آزمون ۳۰ دقیقه بیکار. معیار: Session نمی‌میرد. ریسک: Sessionهای بیکار منابع می‌گیرند.

### ۶) پیاده‌سازی از مسیر GUI

1. Dashboard → FortiView Sessions (یا Monitor → Firewall User/Session).
2. فیلتر و Kill Session در GUI.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sys session filter clear
diagnose sys session filter src 10.10.0.5
diagnose sys session list
diagnose sys session clear
get system session-ttl
diagnose sys session full-stat
```

### ۸) Verification (اثبات صحت)

- Session با policy درست.
- پس از clear، Session جدید.
- Timeout اعمال‌شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy تازه اثر ندارد | Session قدیمی | clear فیلترشده |
| قطع بعد ۵ دقیقه | expire | session-ttl |
| Session زیاد | full-stat | DoS/Timeout |

### ۱۰) نکات امنیتی

- clear بدون فیلتر ممنوع.

### ۱۱) جمع‌بندی مفهومی

- Session = حافظه.
- فیلتر قبل clear.
- Timeout.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) proto=6 یعنی؟ *(پاسخ: 13-4-ت1)*

**ت2.** (ساده) چرا clear فیلترشده؟ *(پاسخ: 13-4-ت2)*

**ت3.** (متوسط) Policy حذف شد ولی ترافیک می‌گذرد؛ چرا؟ *(پاسخ: 13-4-ت3)*

**ت4.** (متوسط) timeout پیش‌فرض TCP؟ *(پاسخ: 13-4-ت4)*

**ت5.** (سخت) SSH قطع می‌شود. *(پاسخ: 13-4-ت5)*

**ت6.** (سخت، طراحی) جدول timeout سازمان. *(پاسخ: 13-4-ت6)*

**Q1.** Quick quiz (English): Why should a session filter be set before running clear? *(پاسخ: 13-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| TTL | Time To Live | زمان زنده‌ماندن |
| NPU | Network Processing Unit | پردازنده‌ی شبکه |

- *Never clear all sessions in production.* ← هرگز همه‌ی Sessionها را در Production پاک نکنید.

### ۱۴) کارت Lab

**کارت Lab:** Session (اجرا نشده). **Evidence:** `03-ops/session-notes.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Session table
- FortiOS 7.0 CLI: diagnose sys session

<a id="l-13-5"></a>

## درس 13-5 — مدیریت Policy در طول زمان: Shadow، Overlap، Hit Count، Schedule و بازبینی فصلی

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۱، ۱۳-۴ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Shadow، Overlap و Redundant را تعریف کند و هرکدام را با مثال تشخیص دهد.
2. Hit Count و Last Used را برای تصمیم حذف/غیرفعال‌سازی به‌کار ببرد.
3. Schedule (Recurring و One-time) و اثر آن بر Session را بفهمد.
4. Policy گشاد (ALL) را با Log و داده تنگ کند.
5. فرایند بازبینی فصلی با Backup، Window و Rollback را طراحی کند.
6. گزارش بازبینی برای ممیز بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

شرکتی ۸ سال است فایروال دارد. هر سال چند «Policy موقتی» اضافه شده، مدیران عوض شده‌اند و کسی نمی‌داند Policy شماره‌ی ۴۷ برای چیست. ممیز می‌پرسد «چرا همه‌ی کاربران به DB دسترسی دارند؟» و جواب این است: «یک پروژه بود که تمام شد، ولی Policy ماند.»

Policy فایروال بدهی فنی تولید می‌کند. هر قاعده‌ی اضافه یک سطح حمله، یک احتمال خطا و یک مانع برای عیب‌یابی است. این درس نشان می‌دهد چطور با داده (نه حدس) سیاست‌ها را پاک‌سازی و دائماً سالم نگه دارید.

### ۳) توضیح عمیق فنی

#### ۱) سه بیماری Policy

| نام | تعریف | اثر |
|---|---|---|
| Shadowed | هرگز اجرا نمی‌شود چون Policy بالاتر همه‌ی ترافیکش را می‌گیرد | قاعده بی‌اثر؛ فریب مدیر |
| Overlap | بخشی از ترافیک را دو Policy می‌پوشانند | رفتار وابسته به ترتیب |
| Redundant | دو Policy یکسان | شلوغی |

مثال:

``` text
10  ZN-USERS -> port1  NET-USERS  all  ALL           ACCEPT
20  ZN-USERS -> port1  NET-USERS  all  HTTPS         ACCEPT  log all
```

Policy 20 Shadowed است: همه‌ی HTTPS قبلاً توسط 10 پذیرفته می‌شود و Log همیشه‌ی 20 هرگز تولید نمی‌شود؛ مدیر خیال می‌کند Log فعال است.

#### ۲) Hit Count و Last Used

GUI ستون Hit Count، Bytes و Last Used دارد. قاعده‌ی عملی:

``` text
Hit Count = 0 and age > 90 days  -> candidate: disable, then delete
Hit Count huge and service ALL   -> candidate: narrow
Last Used older than 180 days    -> candidate: review with owner
```

Hit Count با Reboot یا Reset ممکن است صفر شود؛ پس قبل از تصمیم تاریخچه‌ی Log/FortiAnalyzer را هم ببینید.

#### ۳) Schedule

``` text
config firewall schedule recurring
 edit "WORKHOURS"
  set day monday tuesday wednesday thursday friday
  set start 08:00
  set end 18:00
 next
end
config firewall schedule onetime
 edit "VENDOR-MAINT-2026-12"
  set start 22:00 2026/12/05
  set end 02:00 2026/12/06
 next
end
```

وقتی Schedule تمام می‌شود، Sessionهای جدید رد می‌شوند و Sessionهای موجود تا انقضا یا پاک‌سازی می‌مانند. برای دسترسی پیمانکار از Policy One-time به‌جای «فعال می‌کنیم و یادمان می‌ماند خاموش کنیم» استفاده کنید.

#### ۴) تنگ‌سازی Policy ALL (روش گام‌به‌گام)

1. Backup بگیرید.
2. در Policy ALL، Log همه‌ی Sessionها را روشن کنید.
3. ۱۴ تا ۳۰ روز Log جمع کنید (چرخه‌ی ماهانه را هم شامل شود).
4. مقصدها و سرویس‌های واقعی را استخراج کنید.
5. Policyهای خاص بسازید و **بالاتر** از ALL بگذارید.
6. ALL را غیرفعال کنید (نه حذف)؛ ۲ هفته مشاهده.
7. در صورت بی‌شکایتی حذف و مستند کنید.

#### ۵) فرایند بازبینی فصلی

``` text
Week 1: export policies + hit counts + logs, mark candidates
Week 2: owner confirmation (email/ticket)
Week 3: change window: disable candidates, backup before/after
Week 4: monitor, delete or rollback, update documentation
```

#### ۶) گزارش ممیزی

برای هر Policy: ID، نام، مالک، دلیل کسب‌وکاری، تاریخ ایجاد/آخرین بازبینی، Hit Count، ریسک (ALL؟ بدون Log؟)، تصمیم.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| دوره‌ی بازبینی | فصلی؛ مهم‌ها ماهانه |
| حذف یا غیرفعال | اول غیرفعال و مشاهده |
| Policyهای فصلی | Comment+Schedule یا نگه‌داری |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Policy 20 با Hit Count صفر زیر Policy 10 (ALL) قرار دارد. مراحل: ۱) Lookup برای 10.10.0.5→HTTPS ID 10 را می‌دهد. ۲) 20 هرگز نمی‌رسد. ۳) نتیجه: Shadow. رفع: Policy 20 را بالاتر ببرید یا 10 را تنگ کنید. پاسخ: ترتیب اصلاح و Hit Count 20 افزایش می‌یابد.

**متوسط (تنگ‌سازی ALL):** USERS→SERVERS ALL است. ورودی: Log ۱۴ روز. مراحل: ۱) خروجی Log: مقصد 10.20.0.10 پورت 443 و 445؛ 10.20.0.20 پورت 1433. ۲) سه Policy خاص ساخته‌می‌شود. ۳) ALL غیرفعال. ۴) دو هفته بعد هیچ شکایتی. پاسخ: حذف ALL، ثبت تغییر. اگر شکایت می‌آمد از Log Deny سرویس جاافتاده را اضافه می‌کردید.

**سخت (برنامه‌ی کامل):** ۸۰ Policy، ۱۲ با Hit صفر، ۳ ALL، ۵ بدون Log. برنامه: هفته۱ Export و طبقه‌بندی؛ هفته۲ تأیید مالکان (۱۲ مورد صفر: ۹ تأیید حذف، ۳ نگه‌داشتن موقت با Comment)؛ هفته۳ Backup و غیرفعال‌سازی ۹ مورد و روشن‌کردن Log پنج Policy بدون Log؛ هفته۴ بدون Ticket ⇒ حذف ۹ مورد. ریسک: مصرف فصلی (حسابداری پایان سال) که Hit Count آن را نشان نمی‌دهد؛ راه: بررسی Log ۱۲ ماهه یا نگه‌داشتن Policyهای فصلی با Comment. معیار پذیرش: صفر Ticket، تعداد Policy ALL = 0، همه‌ی Policyها دارای Owner/Comment.

### ۶) پیاده‌سازی از مسیر GUI

1. Policy & Objects → Firewall Policy؛ ستون‌ها: Hit Count، Last Used، Bytes را فعال کنید.
2. روی Policy راست‌کلیک → Show Matching Logs.
3. Disable با Status toggle.
4. Schedules: Policy & Objects → Schedules.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config firewall policy
 edit 47
  set status disable
  set comments "disabled 2026-11-26 review Q4; owner NOC; rollback: enable"
 next
end
show firewall policy | grep -f "set name"
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.10 443 tcp port2
```

### ۸) Verification (اثبات صحت)

- Policy Lookup ID مورد انتظار.
- Hit Count Policy جدید افزایش.
- پس از غیرفعال‌سازی هیچ Ticket.
- Backup قبل/بعد موجود.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy جدید هیچ Hit ندارد | Shadow | ترتیب |
| کاربر بعد از حذف شکایت دارد | Log Deny | Policy خاص اضافه |
| Hit Count صفر مشکوک | Reboot/Reset | Log تاریخی |
| Schedule قطع شد ولی Session باقی است | Session | clear فیلترشده |

### ۱۰) نکات امنیتی

- ALL/ALL فقط موقت با تاریخ پایان.
- هر تغییر با Ticket و Backup.

### ۱۱) جمع‌بندی مفهومی

- Policy بدهی فنی تولید می‌کند.
- Shadow/Overlap/Redundant.
- داده (Hit/Log) تصمیم می‌دهد.
- ابتدا غیرفعال، بعد حذف.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Shadowed Policy چیست؟ *(پاسخ: 13-5-ت1)*

**ت2.** (ساده) چرا Hit Count به‌تنهایی کافی نیست؟ *(پاسخ: 13-5-ت2)*

**ت3.** (متوسط) Schedule تمام شد؛ Session باز چه می‌شود؟ *(پاسخ: 13-5-ت3)*

**ت4.** (متوسط) چرا ابتدا غیرفعال و بعد حذف؟ *(پاسخ: 13-5-ت4)*

**ت5.** (سخت) Policy ALL کاربران→سرورها را تنگ کنید. *(پاسخ: 13-5-ت5)*

**ت6.** (سخت، طراحی) فرایند بازبینی فصلی ۴ هفته‌ای با گزارش. *(پاسخ: 13-5-ت6)*

**Q1.** Quick quiz (English): Why is it safer to disable a policy before deleting it? *(پاسخ: 13-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Shadowed | Shadowed policy | Policy پنهان‌شده |
| Owner | Policy owner | مالک Policy |

- *Review policies quarterly with the business owner.* ← Policyها را فصلی با مالک کسب‌وکار بازبینی کنید.

### ۱۴) کارت Lab

**کارت Lab:** بازبینی Policy (اجرا نشده). **Evidence:** `03-ops/policy-review.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies; Schedules
- NIST SP 800-41 Rev.1 §4.4

<a id="l-13-6"></a>

## درس 13-6 — سناریوهای خرابی Policy/NAT/Route، روش ۱۰ گامی و آزمون G5

**فصل 13 · بازنویسی عمیق · پیش‌نیاز: ۱۳-۱ تا ۱۳-۵، ۱۴-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. علائم رایج خرابی را به لایه‌ی علت (Route، Policy، NAT، Session) نگاشت کند.
2. با Debug flow و Session علت را اثبات کند.
3. سه پرونده‌ی کامل را با RCA حل کند.
4. آزمون عملی G5 را با Evidence و Rubric تحویل دهد.
5. گزارش حادثه‌ی کوتاه (Timeline، علت، رفع، پیشگیری) بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

پشتیبانی تماس می‌گیرد: «کاربران نمی‌توانند سایت داخلی را باز کنند». ۱۰ دقیقه‌ی اول تعیین‌کننده است: یا با روش، علت را سریع می‌یابید، یا حدس می‌زنید و Policy را آن‌قدر عوض می‌کنید که خودتان مشکل دوم می‌سازید. این درس یک روش ثابت می‌دهد و با سه پرونده تمرینش می‌کند.

### ۳) توضیح عمیق فنی

#### ۱) روش ۱۰ گامی

``` text
1 Define symptom precisely (who, what, when, from where, to where)
2 Route: does the FW have a route to dst and back?
3 Policy: does a policy match (lookup / debug flow)?
4 NAT: SNAT/DNAT as expected (session list)?
5 Session: exists? state? stale?
6 DNS: name resolves to expected IP?
7 MTU/MSS: large packets fail?
8 Logs: deny logs, policy id
9 Sniffer + debug flow: packet seen? decision?
10 Verify fix + negative test + document
```

#### ۲) نگاشت علامت به علت

| علامت | علت محتمل |
|---|---|
| Debug flow: `no matching policy` | Policy/Interface/Zone |
| Session فقط org بدون reply | SNAT یا Route برگشت یا سرور |
| Debug flow: `reverse path check fail` | RPF/Route نامتقارن |
| TCP برقرار، بسته‌ی بزرگ نه | MTU |
| فقط با نام کار نمی‌کند | DNS |

#### ۳) سه پرونده

**پرونده ۱ (Policy):** کاربران به وب داخلی نمی‌رسند. Lookup: ID 3 (Deny). Policy مجاز ID 15 پایین‌تر است. رفع: جابه‌جایی. 

**پرونده ۲ (NAT/Route):** اینترنت کار می‌کند ولی یک سرویس خاص نه؛ Session `reply` ندارد؛ Sniffer: SYN خارج می‌شود. علت: IP Pool Overload ولی آن IP در لیست مجاز سرویس نیست؛ یا SNAT به IP غلط. رفع: IP Pool مجاز.

**پرونده ۳ (RPF):** بعد از افزودن لینک دوم برخی Sessionها Drop. Debug flow: reverse path check fail. علت: Route برگشت از Interface دیگر. رفع: اصلاح Route/Distance.

#### ۴) آزمون G5

سه عیب تزریق‌شده توسط مربی/خود شما؛ برای هرکدام Evidence (Lookup/Flow/Session)، علت، رفع، آزمون منفی. Rubric: کشف ۳۰، رفع ۳۰، شواهد ۲۰، آزمون منفی ۱۰، صداقت (بیان Unverified) ۱۰.

#### ۵) گزارش حادثه

``` text
Time: 10:05 first report; 10:12 root cause; 10:20 fixed
Impact: 120 users, service X
Cause: policy order
Fix: moved policy 15 above 3
Prevention: policy review checklist
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ابزار اول | Lookup/Flow |
| ثبت | Evidence هر گام |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Lookup=ID 3 Deny؛ Policy 15 پایین‌تر؛ رفع: جابه‌جایی؛ آزمون: Lookup=15 و دسترسی موفق.

**متوسط (No reply):** Session org دارد و reply ندارد. مراحل: ۱) Sniffer خارج: SYN رفته. ۲) Sniffer ورودی: SYN-ACK نیامد. ۳) SNAT IP اشتباه. ۴) اصلاح Pool. پاسخ: reply آمد و Session ESTABLISHED.

**سخت (دو عیب):** دو عیب هم‌زمان: Policy ترتیب + NAT. ابتدا Policy را رفع کنید؛ سپس علائم NAT ظاهر می‌شود؛ اگر هر دو را هم‌زمان تغییر دهید نمی‌دانید کدام اثر کرد. درس: یک تغییر، یک آزمون.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose firewall iprope lookup 10.10.0.5 40000 10.20.0.10 443 tcp port2
diagnose debug flow filter addr 10.20.0.10
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
diagnose sys session filter dst 10.20.0.10
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- Evidence هر گام.
- آزمون منفی.
- گزارش حادثه.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| no matching policy | Lookup | ترتیب |
| no reply | Sniffer | SNAT/Route |
| RPF fail | Flow | Route برگشت |

### ۱۰) نکات امنیتی

- Debug را خاموش کنید.
- Evidence بدون اطلاعات حساس.

### ۱۱) جمع‌بندی مفهومی

- روش ثابت.
- یک تغییر/یک آزمون.
- Evidence و RCA.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) اولین گام عیب‌یابی؟ *(پاسخ: 13-6-ت1)*

**ت2.** (ساده) no reply یعنی؟ *(پاسخ: 13-6-ت2)*

**ت3.** (متوسط) RPF fail چیست؟ *(پاسخ: 13-6-ت3)*

**ت4.** (متوسط) چرا یک تغییر هر بار؟ *(پاسخ: 13-6-ت4)*

**ت5.** (سخت) دو عیب هم‌زمان را چگونه جدا می‌کنید؟ *(پاسخ: 13-6-ت5)*

**ت6.** (سخت، طراحی) قالب گزارش حادثه. *(پاسخ: 13-6-ت6)*

**Q1.** Quick quiz (English): Which tool shows the policy that would match a given flow? *(پاسخ: 13-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RCA | Root Cause Analysis | تحلیل ریشه‌ای |

- *Change one variable at a time.* ← هر بار فقط یک متغیر را تغییر دهید.

### ۱۴) کارت Lab

**کارت Lab:** G5 (اجرا نشده). **Evidence:** `03-ops/rca-fgt-1.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Troubleshooting

## درس 13-7 — Session، تغییر Policy/Route و NAT در برابر Routing: چرا «تنظیم را عوض کردم ولی اثر نکرد»؟

**فصل ۱۳ · درس افزوده (تکمیل ۱۳-۶) · پیش‌نیاز: ۱۲-۰، ۱۱-۷، ۱۳-۱ تا ۱۳-۶ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3، `Unverified` روی Image):** رفتارها از مستند Fortinet و دانش عملیاتی است؛ نام دقیق پارامترها با CLI Reference 7.0 تطبیق داده شود. Lab «اجرا نشده».

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. توضیح دهد چرا تغییر Policy/Route روی Sessionهای **موجود** فوراً اثر نمی‌کند.
2. Sessionها را ببیند، فیلتر کند و (با احتیاط) پاک کند.
3. Timeout Session را بشناسد و برای سرویس خاص تنظیم کند.
4. **NAT را از Routing** جدا بفهمد و بگوید هرکدام چه می‌کنند.
5. رفتار Session در مسیرهای نامتقارن و Failover را تحلیل کند.
6. «سناریوی تغییر» را درست اجرا کند: تغییر → Clear Session مرتبط → تست.

### ۲) پیش‌نیازها

Packet Flow (۱۲-۰)، Stateful (۱۱-۷)، Policy/NAT/VIP (۱۳-۱ تا ۱۳-۶).

### ۳) مفهوم پایه

در FortiGate، Policy و Route برای **بسته‌ی اول** Session بررسی می‌شوند؛ نتیجه در Session ذخیره می‌شود. بسته‌های بعدی فقط Session را می‌بینند. پس اگر Session برقرار است و شما Policy را به deny تغییر دهید، آن Session ممکن است تا انقضا یا پاک‌شدن ادامه یابد (بسته به نسخه/تنظیمات Session re-evaluation؛ رفتار دقیق `Unverified`). به همین دلیل:

> **«سرویس را بستم ولی هنوز کار می‌کند»** = Session قدیمی هنوز زنده است.
> **«Route را عوض کردم ولی ترافیک هنوز از مسیر قبلی می‌رود»** = Session روی مسیر قبلی است.

### ۴) توضیح عمیق فنی

#### ۴-۱) کدام تغییرات بر Session موجود اثر می‌گذارند؟

| تغییر | اثر بر Session موجود | اقدام |
|---|---|---|
| Policy جدید/تغییر Action | معمولاً خیر (تا پایان Session) | پاک‌کردن Session مرتبط |
| تغییر Route | ممکن است نه؛ بستگی به `session-route-check`/تنظیمات (`Unverified`) | پاک‌کردن Session یا تنظیم مناسب |
| تغییر Profile (AV/Web) | ممکن است برای Sessionهای جدید | Clear یا انتظار |
| تغییر NAT/IP Pool | Session قدیمی ترجمه‌ی قبلی را حفظ می‌کند | Clear |
| قطع لینک | Session روی لینک مرده می‌ماند تا Timeout | Clear/Health-check (فصل ۲۱) |

#### ۴-۲) مشاهده و فیلتر Session

``` text
diagnose sys session filter clear
diagnose sys session filter src 192.168.10.5
diagnose sys session filter dst 8.8.8.8
diagnose sys session filter dport 443
diagnose sys session list
diagnose sys session clear
```

نکات:

- **همیشه Filter را بگذارید** قبل از `clear`؛ `diagnose sys session clear` بدون Filter **همه‌ی Sessionها** را پاک می‌کند و ارتباط همه‌ی کاربران را قطع می‌کند.
- خروجی `session list` شامل: Protocol، State، Timeout (expire)، Policy ID، NAT (`hook=pre/post` و آدرس‌های ترجمه‌شده)، Interface ورودی/خروجی، شمارنده‌ها.

``` text
session info: proto=6 proto_state=01 duration=45 expire=3555 timeout=3600 ...
orgin->sink: org pre->post, reply pre->post dev=4->3/3->4 gwy=203.0.113.1/192.168.10.5
hook=post dir=org act=snat 192.168.10.5:51200->8.8.8.8:443(203.0.113.10:51200)
hook=pre dir=reply act=dnat 8.8.8.8:443->203.0.113.10:51200(192.168.10.5:51200)
policy_id=10
```

(نمونه‌ی ساده‌شده؛ فرمت واقعی را در Lab بخوانید.)

خواندن: `act=snat` ترجمه‌ی مبدأ؛ `dir=reply` جهت برگشت؛ `policy_id` همان Policy؛ `expire` زمان باقی‌مانده.

#### ۴-۳) Timeout

- Session TCP Established: پیش‌فرض طولانی (مثلاً ۳۶۰۰ ثانیه)؛ Half-open کوتاه.
- UDP/ICMP کوتاه‌تر.
- قابل تنظیم در سطح Global (`config system session-ttl`) یا Per-Policy (`set session-ttl`)؛ نام‌ها `Unverified`.
- Timeout کوتاه ← کاربران بی‌فعالیت قطع؛ Timeout بلند ← جدول Session بزرگ.

#### ۴-۴) NAT در برابر Routing (تکرار هدفمند)

| | Routing | NAT |
|---|---|---|
| وظیفه | انتخاب مسیر/Interface خروجی | تغییر آدرس (و پورت) در هدر |
| چه چیزی را عوض می‌کند | Next-hop/Interface | IP/پورت مبدأ (SNAT) یا مقصد (DNAT) |
| زمان | بعد از DNAT، قبل از Policy | DNAT قبل از Route؛ SNAT بعد از Policy |
| بدون آن چه می‌شود | بسته مسیر ندارد | آدرس خصوصی در اینترنت قابل برگشت نیست |
| خطای رایج | Route ناقص | Policy مقصد قبل از DNAT |

**مثال تمایز:** سرور داخلی 10.1.1.10 با VIP 203.0.113.50 منتشر شده. Routing فقط می‌گوید 10.1.1.10 پشت port3 است؛ NAT (VIP) است که مقصد 203.0.113.50 را به 10.1.1.10 تبدیل می‌کند. اگر Route 10.1.1.0/24 نبود، DNAT انجام می‌شود ولی بسته مسیر ندارد؛ اگر VIP نبود، مسیر هست ولی مقصد (آدرس عمومی) روی فایروال مسیر مناسبی ندارد.

#### ۴-۵) Session و Asymmetric/Failover

- Asymmetric: برگشت از Interface/فایروال دیگر ← Session نیست یا RPF ← Drop.
- HA بدون Session Pickup: Sessionها قطع (درس ۲۲-۰). با Pickup: TCP همگام می‌شود (UDP/ICMP نیاز به تنظیم جدا، طبق مستند 7.x).

### ۵) مثال حل‌شده

**مسئله:** تا ساعت ۱۰ کاربران به یک سایت دسترسی دارند. مدیر Policy deny می‌نویسد ولی کاربر به دانلود ادامه می‌دهد.

``` text
FGT # diagnose sys session filter clear
FGT # diagnose sys session filter src 192.168.10.5
FGT # diagnose sys session filter dst 198.51.100.7
FGT # diagnose sys session list
FGT # diagnose sys session clear
FGT # diagnose sys session filter clear
```

**تحلیل:** Session دانلود قبل از Policy جدید ساخته شده؛ با Clear فقط Sessionهای همان کاربر/مقصد پاک شده و بقیه‌ی کاربران دست نخورده‌اند. پس از Clear، بسته‌ی بعدی دوباره Policy می‌سنجد و deny می‌شود.

**مثال متوسط:** تغییر IP Pool: Session قدیمی هنوز IP قدیمی را دارد. بعد از Clear Sessionهای مرتبط، IP جدید دیده می‌شود.

**مثال سخت (Failover ISP):** پس از قطع WAN1، ترافیک جدید از WAN2 می‌رود ولی دانلودهای قبلی قفل شده‌اند. Session روی WAN1 مانده با SNAT قدیمی. راه‌حل: Clear Sessionهای مرتبط با WAN1 هنگام Failover (در SD-WAN با تنظیمات `Unverified` در فصل ۲۱) و Timeout مناسب.

### ۶) طراحی و تصمیم‌گیری

| تصمیم | معیار |
|---|---|
| Clear کامل یا Filter شده | Filter شده؛ Clear کامل فقط با Change Window |
| Timeout Per-Policy | سرویس‌های طولانی (DB/SSH) |
| بعد از هر تغییر Policy | چک‌لیست: Policy → Session → Test |

### ۷) پیاده‌سازی: GUI و CLI

**GUI:** Dashboard → Add Widget → «Sessions»؛ Log & Report → Forward Traffic؛ در FortiView → Sessions (7.0) امکان مشاهده/Kill Session (نام و محل `Unverified`).

**CLI:**

``` text
diagnose sys session filter clear
diagnose sys session filter dst 198.51.100.7
diagnose sys session list
diagnose sys session clear
get system session-info statistics
```

### ۸) Troubleshooting

| علامت | علت | شاهد |
|---|---|---|
| Policy جدید اثر ندارد | Session قدیمی | `session list` (قبل از تغییر) |
| IP NAT قدیمی باقی است | Session | `hook=post` |
| Failover ترافیک را نبرد | Session قفل | `session list` به WAN قبلی |
| Session زیاد | Timeout بلند/حمله | `get system session-info statistics` |

### ۹) نکات امنیتی

- `diagnose sys session clear` بدون Filter ممنوع در تولید.
- Timeout بسیار بلند + حمله = Exhaustion.
- بعد از Policy deny برای حادثه، Sessionهای فعال مهاجم را حتماً Clear کنید.

### ۱۰) جمع‌بندی مفهومی

- Policy/Route برای بسته‌ی اول؛ تغییر روی Session موجود فوراً نیست.
- قبل از Clear Filter بگذارید.
- NAT آدرس را عوض می‌کند؛ Routing مسیر را.
- Timeout تعادل است.
- همیشه پس از تغییر: Clear مرتبط + تست.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) چرا تغییر Policy روی Session موجود فوراً اثر نمی‌کند؟ *(پاسخ: 13-7-ت1)*

**ت2.** (ساده) چرا Filter قبل از Clear لازم است؟ *(پاسخ: 13-7-ت2)*

**ت3.** (متوسط) تفاوت DNAT و Routing را با مثال VIP بگویید. *(پاسخ: 13-7-ت3)*

**ت4.** (متوسط) از `act=snat` در خروجی session چه می‌فهمید؟ *(پاسخ: 13-7-ت4)*

**ت5.** (سخت) پس از Failover ISP بعضی دانلودها قفل‌اند؛ علت و راه‌حل با شواهد. *(پاسخ: 13-7-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست ۵ مرحله‌ای تغییر Policy در تولید بنویسید. *(پاسخ: 13-7-ت6)*

**م1.** Timeout پیش‌فرض TCP Established به چه قابل تنظیم است؟ *(پاسخ: 13-7-م1)*

**Q1.** Quick quiz (English): Why must you apply a filter before clearing sessions? *(پاسخ: 13-7-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Session TTL | Session time-to-live | عمر Session |
| act=snat | NAT action in session | عمل ترجمه ثبت‌شده |
| Clear | Clear session | حذف Session |
| Pickup | Session pickup | حفظ Session هنگام Failover |

- *Changing a policy does not affect established sessions until they expire or are cleared.* ← تغییر Policy تا پایان یا پاک‌شدن Session روی Sessionهای برقرار اثر ندارد.
- *Never clear all sessions in production without a change window.* ← هرگز در تولید بدون Change Window همه‌ی Sessionها را پاک نکنید.

### ۱۳) منابع

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

**13-3-ت3** — فقط پورت‌های لازم را در معرض می‌گذارد.

**13-3-ت4** — سرور و کاربر هم‌شبکه‌اند و پاسخ مستقیم می‌دهد و فایروال دور زده می‌شود.

**13-3-ت5** — Policy، Route، ARP، Session، Log، آزمون منفی.

**13-3-ت6** — سه VIP جدا، Policy جدا، Zone DMZ، Log، آزمون منفی.

**13-3-Q1** — Because DNAT happens before policy lookup and the policy matches the VIP.


### پاسخ‌های بازنویسی عمیق درس 13-4

**13-4-ت1** — TCP.

**13-4-ت2** — تا Sessionهای دیگر قطع نشوند.

**13-4-ت3** — Session موجود تا انقضا باقی است؛ Session را با فیلتر پاک کنید.

**13-4-ت4** — حدود ۳۶۰۰ ثانیه (طبق نسخه تأیید شود).

**13-4-ت5** — timeout پورت 22 افزایش یا Keepalive.

**13-4-ت6** — سرویس، پورت، timeout و دلیل.

**13-4-Q1** — Without a filter all sessions are cleared causing an outage.


### پاسخ‌های بازنویسی عمیق درس 13-5


### پاسخ‌های بازنویسی عمیق درس 13-5

**13-5-ت1** — Policyای که هرگز اجرا نمی‌شود چون Policy بالاتر همه‌ی ترافیک آن را می‌گیرد. مثلاً ALL بالای HTTPS.

**13-5-ت2** — با Reboot/Reset صفر می‌شود و استفاده‌ی فصلی را نمی‌بیند؛ باید با Log تاریخی و مالک تأیید شود.

**13-5-ت3** — تا انقضا یا پاک‌سازی می‌ماند؛ برای قطع فوری Session را با فیلتر پاک کنید.

**13-5-ت4** — برای Rollback سریع اگر سرویس مخفی وابسته باشد.

**13-5-ت5** — Log ۱۴–۳۰ روز، استخراج مقصد/پورت، Policy خاص بالای ALL، غیرفعال‌سازی ALL، مشاهده، حذف؛ همراه Backup و Rollback.

**13-5-ت6** — Export، تأیید مالک، Window با Backup، مشاهده/حذف؛ گزارش: ID، مالک، دلیل، Hit، ریسک، تصمیم.

**13-5-Q1** — Disabling allows quick rollback if an unknown dependency appears.


### پاسخ‌های بازنویسی عمیق درس 13-6

**13-6-ت1** — تعریف دقیق علامت.

**13-6-ت2** — پاسخ برنگشته؛ SNAT/Route/سرور.

**13-6-ت3** — Route معکوس مبدأ از Interface ورودی نیست.

**13-6-ت4** — برای دانستن اثر هر تغییر.

**13-6-ت5** — اول یکی را رفع، آزمون، سپس دومی.

**13-6-ت6** — Timeline، Impact، Cause، Fix، Prevention.

**13-6-Q1** — The policy lookup (iprope lookup).

### پاسخ‌های درس افزوده‌ی 13-7 (فصل 13)

**13-7-ت1** — Policy برای بسته‌ی اول ارزیابی و نتیجه در Session ذخیره می‌شود؛ تغییر بعدی تا انقضا/Clear روی Session موجود اثر ندارد.

**13-7-ت2** — بدون Filter همه‌ی Sessionها پاک و ارتباط همه‌ی کاربران قطع می‌شود.

**13-7-ت3** — Routing مسیر را تعیین می‌کند؛ VIP/DNAT مقصد را به IP داخلی ترجمه می‌کند؛ هر دو لازم‌اند.

**13-7-ت4** — مبدأ بسته ترجمه (SNAT) شده است؛ آدرس ترجمه‌شده در پرانتز دیده می‌شود.

**13-7-ت5** — Session روی WAN قدیمی با SNAT قدیمی مانده؛ شاهد: session list؛ راه‌حل: Clear فیلترشده و تنظیم Failover/Timeout.

**13-7-ت6** — ۱) Backup؛ ۲) تغییر Policy؛ ۳) Clear فیلترشده‌ی Sessionهای مرتبط؛ ۴) آزمون مثبت/منفی؛ ۵) ثبت Evidence و Rollback.

**13-7-م1** — در Global یا Per-Policy با session-ttl (نام دقیق با CLI Reference تطبیق شود).

**13-7-Q1** — Because clearing without a filter removes every session and disconnects all users.

# فصل 14 — ابزارهای عیب‌یابی FortiOS: Sniffer، Debug Flow، Session، Routing، MTU/MSS و Log

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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. ده پرسش ثابت عیب‌یابی فایروال را به ترتیب بپرسد و برای هرکدام ابزار مناسب را انتخاب کند.
2. ابزارها (ping، traceroute، sniffer، debug flow، session، routing، log) را در نقشه‌ی مسیر بسته جای دهد.
3. از علامت «کار نمی‌کند» به فرضیه‌ی قابل‌آزمون برسد.
4. هر گام را با Evidence ثبت کند.
5. از ابزارهای سنگین (debug) ایمن استفاده کند.

### ۲) مفهوم پایه: چیست و چرا؟

پزشکی که بیمار را می‌بیند اول ده سؤال استاندارد می‌پرسد: چه علامتی؟ از کی؟ تب هست؟ ... بعد آزمایش مناسب می‌فرستد. عیب‌یابی شبکه هم همین است. بدون چارچوب، هر مهندس از جایی شروع می‌کند، آزمایش‌های تکراری می‌گیرد و گاهی Policy سالم را خراب می‌کند. این درس «ده پرسش» را به ابزار نگاشت می‌کند.

### ۳) توضیح عمیق فنی

#### ۱) ده پرسش

| # | پرسش | ابزار |
|---|---|---|
| 1 | دقیقاً چه چیزی کار نمی‌کند، از کجا به کجا؟ | گفتگو، ticket |
| 2 | آیا لایه‌ی ۱–۲ سالم است؟ | `get system interface physical`، لینک، VLAN |
| 3 | آیا بسته به FortiGate می‌رسد؟ | sniffer ورودی |
| 4 | آیا Route به مقصد و برگشت وجود دارد؟ | `get router info routing-table details` |
| 5 | آیا Policy مطابق است؟ | policy lookup، debug flow |
| 6 | آیا NAT درست انجام شد؟ | `diagnose sys session list` |
| 7 | آیا Session ساخته شد و وضعیتش چیست؟ | session filter |
| 8 | آیا بسته خارج می‌شود؟ | sniffer خروجی |
| 9 | آیا پاسخ برمی‌گردد؟ | sniffer ورودی (مقصد→ما) |
| 10 | آیا نام/MTU/سرویس‌های جانبی مشکل دارند؟ | DNS test، ping DF |

#### ۲) نقشه‌ی ابزار روی مسیر بسته

``` text
Client -> [sniffer in] -> RPF/Route -> Policy -> NAT -> [sniffer out] -> Server
             ^debug flow shows each decision^         ^session list shows result^
```

#### ۳) ابزارهای اصلی

``` text
execute ping 8.8.8.8
execute ping-options source 10.10.0.1
execute traceroute 8.8.8.8
diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow trace start 20
diagnose debug enable
get router info routing-table details 203.0.113.10
diagnose sys session list
```

#### ۴) ایمنی ابزار

Debug روی Production CPU مصرف می‌کند؛ همیشه فیلتر، محدودیت تعداد (`trace start 20`) و در پایان `diagnose debug disable` و `diagnose debug reset`. Sniffer را با شمارنده بزنید (مثلاً 20 بسته) نه بی‌پایان.

#### ۵) از علامت تا فرضیه

علامت: «سایت باز نمی‌شود». فرضیه‌ها: Route، Policy، NAT، DNS، MTU. هر فرضیه یک آزمایش و یک نتیجه‌ی صریح دارد؛ فرضیه‌ای که نتوان رد/تأیید کرد، بد تعریف شده است.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترتیب | پایین به بالا |
| ابزار | کم‌هزینه‌تر اول |
| ثبت | Evidence هر گام |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** «کاربر 10.10.0.5 به 203.0.113.10:443 نمی‌رسد». پرسش ۳: Sniffer ورودی SYN را نشان می‌دهد ⇒ می‌رسد. پرسش ۴: Route Default هست. پرسش ۵: Lookup ID 2. پرسش ۸: SYN خارج می‌شود. پرسش ۹: SYN-ACK نمی‌آید ⇒ مشکل بیرون از فایروال (سرور/ISP). پاسخ: تیم سرور.

**متوسط (تحلیل):** بسته در Sniffer ورودی دیده نمی‌شود. پرسش ۲ و ۳: لینک up؛ VLAN اشتباه سوییچ. اثبات: `get system interface physical` و MAC در ARP: `diagnose ip arp list`. رفع: VLAN سوییچ. درس: همیشه از پایین‌ترین لایه شروع کنید.

**سخت (چندلایه):** «بعضی سایت‌ها باز می‌شوند، بعضی نه». ۱) ping همه موفق. ۲) Debug flow: Policy و NAT صحیح. ۳) Sniffer: بسته‌های کوچک عبور می‌کنند؛ بزرگ نه. ۴) `execute ping-options df-bit yes` با `data-size 1472` شکست؛ 1372 موفق ⇒ PMTU≈1400. علت: لینک تونل با MTU کمتر و فیلتر ICMP. رفع: MSS-clamp/MTU. معیار: بارگیری صفحه‌ی بزرگ موفق.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Diagnostics → Packet Capture.
2. Dashboard → FortiView.
3. Log & Report → Forward Traffic.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute ping 8.8.8.8
execute traceroute 8.8.8.8
diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

### ۸) Verification (اثبات صحت)

- هر گام Evidence دارد.
- فرضیه‌ی نهایی با آزمایش تأیید شده.
- Debug خاموش شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Sniffer خالی | فیلتر | Host/پورت و Interface |
| Debug خروجی ندارد | offload/filter | offload را موقتاً غیرفعال (Lab) |
| CPU بالا | Debug | disable |

### ۱۰) نکات امنیتی

- Capture حاوی داده‌ی حساس است؛ محدود و حذف.
- Debug را خاموش کنید.

### ۱۱) جمع‌بندی مفهومی

- ده پرسش ثابت.
- ابزار هر پرسش.
- Debug با فیلتر و شمارنده.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا از لایه‌ی پایین شروع می‌کنیم؟ *(پاسخ: 14-1-ت1)*

**ت2.** (ساده) Sniffer را چرا با شمارنده می‌زنیم؟ *(پاسخ: 14-1-ت2)*

**ت3.** (متوسط) Sniffer ورودی خالی است؛ علت‌های محتمل؟ *(پاسخ: 14-1-ت3)*

**ت4.** (متوسط) تفاوت sniffer و debug flow؟ *(پاسخ: 14-1-ت4)*

**ت5.** (سخت) برخی سایت‌ها باز می‌شوند؛ مسیر عیب‌یابی؟ *(پاسخ: 14-1-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست یک‌صفحه‌ای ده‌پرسشی. *(پاسخ: 14-1-ت6)*

**Q1.** Quick quiz (English): Which tool reveals the policy and route decision made for a packet? *(پاسخ: 14-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| DF | Don't Fragment | بدون تکه‌سازی |
| PMTU | Path MTU | MTU مسیر |

- *Start from the lowest layer and move up.* ← از پایین‌ترین لایه شروع کنید و بالا بروید.

### ۱۴) کارت Lab

**کارت Lab:** ده پرسش (اجرا نشده). **Evidence:** `03-ops/ten-questions.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Troubleshooting tools
- FortiOS 7.0 Troubleshooting guide

<a id="l-14-2"></a>

## درس 14-2 — Packet Sniffer در CLI/GUI و تحلیل با Wireshark

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۱ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. دستور sniffer را با verbosity و فیلتر BPF بنویسد.
2. Capture را در GUI بگیرد و دانلود کند.
3. خروجی verbosity 6 را به pcap تبدیل کند.
4. در Wireshark Handshake، Retransmission، RST و ICMP را بخواند.
5. محدودیت Offload و ایمنی را بداند.

### ۲) مفهوم پایه: چیست و چرا؟

Sniffer شاهد عینی است: بحث «بسته رسید/نرسید» را با یک خط جواب می‌دهد. ولی اگر فیلتر را غلط بنویسید یا Offload را در نظر نگیرید، چیزی نمی‌بینید و نتیجه‌ی غلط می‌گیرید.

### ۳) توضیح عمیق فنی

#### ۱) دستور

``` text
diagnose sniffer packet <interface> '<filter>' <verbosity> <count> <timestamp>
diagnose sniffer packet port2 'host 10.10.0.5 and tcp port 443' 4 20 l
```

| Verbosity | محتوا |
|---|---|
| 1 | هدر کوتاه |
| 3 | هدر + payload hex |
| 4 | هدر + نام Interface |
| 6 | هدر+payload+Ethernet و قابل تبدیل به pcap |

`any` همه‌ی Interfaceها؛ `l` زمان محلی.

#### ۲) فیلتر

``` text
'host 10.10.0.5'
'net 10.20.0.0/24'
'tcp and port 443'
'icmp'
'host 10.10.0.5 and not port 22'
```

#### ۳) GUI

Network → Diagnostics → Packet Capture: Interface، Filter، Count؛ دانلود pcap.

#### ۴) تبدیل verbosity 6

خروجی را در فایل ذخیره و با اسکریپت `fgt2eth.pl` (ابزار عمومی Fortinet/اجتماع؛ `Unverified` در محیط شما) به pcap تبدیل کنید، یا مستقیماً از GUI pcap بگیرید.

#### ۵) خواندن در Wireshark

``` text
tcp.flags.syn==1 and tcp.flags.ack==0       SYN only
tcp.analysis.retransmission                   retransmissions
tcp.flags.reset==1                            resets
icmp.type==3 and icmp.code==4                 frag needed
```

الگوها: SYN بدون SYN-ACK ⇒ مقصد/مسیر؛ SYN-ACK ولی ACK نیامده ⇒ Asymmetric؛ RST ⇒ پورت بسته/Policy سرور.

#### ۶) Offload

بسته‌های Offload‌شده به NPU ممکن است در sniffer دیده نشوند؛ برای Lab با Policy مربوطه `auto-asic-offload disable` (Unverified). در Production با احتیاط.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| verbosity | 4 برای عمومی؛ 6 برای pcap |
| فیلتر | دقیق و محدود |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Sniffer 20 بسته: SYN از 10.10.0.5 و SYN-ACK برگشتی ⇒ مسیر سالم.

**متوسط (تحلیل):** SYN بارها ارسال و SYN-ACK نیامد: Sniffer خروجی SYN را می‌بیند؛ مقصد پاسخ نمی‌دهد؛ تیم سرور.

**سخت (Asymmetric):** Sniffer ورودی `port2`: SYN؛ Sniffer `port3`: SYN-ACK؛ ولی در `port1` ACK نیست ⇒ ترافیک برگشت از Interface دیگر و RPF/Session؛ رفع Route.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Diagnostics → Packet Capture → New.
2. Interface/Filter/Count؛ Start؛ Download.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l
diagnose sniffer packet port2 'icmp' 6 10 l
```

### ۸) Verification (اثبات صحت)

- بسته‌ها با Timestamp.
- Handshake کامل.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| چیزی دیده نمی‌شود | فیلتر/Interface | any |
| بسته ناقص | Offload | auto-asic-offload (Lab) |

### ۱۰) نکات امنیتی

- Capture حاوی داده‌ی حساس است.

### ۱۱) جمع‌بندی مفهومی

- Sniffer شاهد.
- فیلتر دقیق.
- Offload.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) verbosity 4 چه نشان می‌دهد؟ *(پاسخ: 14-2-ت1)*

**ت2.** (ساده) count چیست؟ *(پاسخ: 14-2-ت2)*

**ت3.** (متوسط) SYN بدون SYN-ACK یعنی؟ *(پاسخ: 14-2-ت3)*

**ت4.** (متوسط) چرا Offload مهم است؟ *(پاسخ: 14-2-ت4)*

**ت5.** (سخت) Asymmetric را با Sniffer ثابت کنید. *(پاسخ: 14-2-ت5)*

**ت6.** (سخت، طراحی) روش Capture امن. *(پاسخ: 14-2-ت6)*

**Q1.** Quick quiz (English): Which verbosity includes the interface name? *(پاسخ: 14-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| BPF | Berkeley Packet Filter | فیلتر بسته |

- *Capture with a narrow filter.* ← با فیلتر محدود Capture کنید.

### ۱۴) کارت Lab

**کارت Lab:** Sniffer (اجرا نشده). **Evidence:** `03-ops/sniffer-notes.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Packet capture
- Wireshark User Guide

<a id="l-14-3"></a>

## درس 14-3 — Debug Flow: خواندن تصمیم فایروال خط به خط

**فصل 14 · بازنویسی عمیق · پیش‌نیاز: ۱۴-۱، ۱۴-۲ · ≈ 10 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. فیلتر Debug flow را بسازد.
2. خروجی را (Route، Policy، NAT، Drop) خط‌به‌خط تفسیر کند.
3. پیام‌های رایج (no matching policy، reverse path check fail، denied by forward policy check) را بشناسد.
4. Debug را امن اجرا و خاموش کند.
5. با Lookup و Session تأیید کند.

### ۲) مفهوم پایه: چیست و چرا؟

Debug flow مثل فیلم «چرا فایروال تصمیم گرفت» است: می‌گوید بسته آمد، مسیر پیدا شد یا نه، Policy کدام بود، NAT چه شد. اگر بتوانید آن را بخوانید، ۸۰٪ پرونده‌ها در ده دقیقه حل می‌شوند.

### ۳) توضیح عمیق فنی

#### ۱) اجرا

``` text
diagnose debug reset
diagnose debug flow filter clear
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow filter port 443
diagnose debug flow show function-name enable
diagnose debug flow trace start 20
diagnose debug enable
...
diagnose debug disable
diagnose debug reset
```

در FortiOS 7.0 برای مدل‌های NP4/NP6 قبلاً Offload را غیرفعال کنید (طبق مستند Fortinet).

#### ۲) خروجی نمونه

``` text
id=20085 trace_id=1 func=print_pkt_detail line=5777 msg="vd-root:0 received a packet(proto=6, 10.10.0.5:40000->203.0.113.10:443) from port2. flag [S], seq ..."
id=20085 trace_id=1 func=init_ip_session_common msg="allocate a new session-00001234"
id=20085 trace_id=1 func=vf_ip_route_input_common msg="find a route: flag=00000000 gw-198.51.100.1 via port1"
id=20085 trace_id=1 func=fw_forward_handler msg="Allowed by Policy-2: SNAT"
id=20085 trace_id=1 func=__ip_session_run_tuple msg="SNAT 10.10.0.5->198.51.100.2:40000"
```

| خط | معنی |
|---|---|
| received a packet | ورود بسته |
| allocate a new session | شروع Session |
| find a route | Route و Interface خروجی |
| Allowed by Policy-2 | Policy و NAT |
| SNAT | ترجمه |

#### ۳) پیام‌های Drop

| پیام | معنی | رفع |
|---|---|---|
| `no session matched` | بسته میانه‌ی Session بدون SYN | Asymmetric/Timeout |
| `Denied by forward policy check (policy 0)` | Implicit Deny | Policy بسازید |
| `reverse path check fail, drop` | RPF | Route |
| `iprope_in_check() check failed` | Local-in | Local-in policy/Admin access |

#### ۴) ایمنی

Debug سنگین است؛ `trace start 20` تعداد را محدود می‌کند؛ همیشه خاموش و `reset`.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| فیلتر | Addr+Port |
| trace | ۲۰ بسته |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** خط «Allowed by Policy-2: SNAT» یعنی Policy 2 و NAT؛ مسیر سالم.

**متوسط (Deny):** `Denied by forward policy check (policy 0)`: Policy مطابق نیست؛ Lookup؛ Policy بسازید یا اصلاح Interface/Zone.

**سخت (RPF):** `reverse path check fail`: مبدأ 10.30.0.5 از port4 آمده ولی Route به 10.30.0.0 از port3؛ رفع Route یا Asymmetric design؛ آزمون: Debug flow بعدی Allowed.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose debug reset
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow show function-name enable
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

### ۸) Verification (اثبات صحت)

- خط Allowed/Denied.
- Policy-ID.
- پس از رفع، Allowed.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| خروجی خالی | فیلتر/Offload | فیلتر؛ offload |
| no session matched | Handshake | Asymmetric |
| RPF fail | Route | Route |

### ۱۰) نکات امنیتی

- Debug را خاموش کنید.

### ۱۱) جمع‌بندی مفهومی

- Debug flow=تصمیم.
- پیام‌های Drop.
- فیلتر و شمارنده.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) trace start 20؟ *(پاسخ: 14-3-ت1)*

**ت2.** (ساده) Allowed by Policy-2؟ *(پاسخ: 14-3-ت2)*

**ت3.** (متوسط) policy 0 یعنی؟ *(پاسخ: 14-3-ت3)*

**ت4.** (متوسط) RPF fail؟ *(پاسخ: 14-3-ت4)*

**ت5.** (سخت) RPF را رفع کنید. *(پاسخ: 14-3-ت5)*

**ت6.** (سخت، طراحی) الگوی ثبت Debug. *(پاسخ: 14-3-ت6)*

**Q1.** Quick quiz (English): What does "reverse path check fail" indicate? *(پاسخ: 14-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | مسیر معکوس |

- *Always disable debug when finished.* ← پس از اتمام Debug را خاموش کنید.

### ۱۴) کارت Lab

**کارت Lab:** Debug flow (اجرا نشده). **Evidence:** `03-ops/debug-flow.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Debug flow
- FortiOS 7.0 Troubleshooting: packet flow

<a id="l-14-4"></a>

## درس 14-4 — Session، Routing و iprope: ابزارهای تکمیلی

**فصل 14 - روز 4 · پیش‌نیاز: درس ۱۴-۲ · ۶ ساعت**

### ۱) معرفی درس

ترکیب Session، Routing و iprope تصویر کامل می‌دهد: Route انتخاب‌شده، Policy، NAT.

### ۲) پیش‌نیازها

درس‌های ۱۴-۱ تا ۱۴-۳.

### ۳) توضیح مفهومی

- `get router info routing-table details <ip>`: Route برای مقصد.
- `diagnose ip route list`/`get router info kernel`: جدول کرنل (`Unverified`).
- `diagnose firewall iprope lookup`: Policy.
- `get system arp`: ARP.
- `diagnose sys session list`: NAT و Policy واقعی.

### ۴) مثال ساده

ping از Client؛ هر ابزار یک قطعه از تصویر.

### ۵) مثال سازمانی

تحلیل Session نیمه‌کاره.

### ۶) تصویر و توپولوژی

```text
route + policy + NAT + session = full picture
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Monitor > Routing Monitor.
2. Dashboard > FortiView Sessions.
3. Policy Lookup.
4. Network > Interfaces > ARP (در صورت وجود).
5. CLI برای iprope.

#### روش خط فرمان (CLI)

```text
get router info routing-table details 8.8.8.8
get system arp
diagnose firewall iprope lookup 192.168.20.11 51234 8.8.8.8 443 tcp VLAN20
diagnose sys session filter dst 8.8.8.8
diagnose sys session list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- هر دستور را با نتیجه‌ی Debug Flow مقایسه کنید.
- راستی‌آزمایی: Route/Policy/NAT با Debug Flow یکی باشد.
- بازگشت: ندارد.

### ۸) تست عملکرد

- برای یک ارتباط چهار ابزار را مقایسه کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Policy درست ولی ارتباط نه |
| شواهد/دستور | Session نیمه‌کاره (SYN) |
| علت | مقصد پاسخ نمی‌دهد/برگشت |
| رفع | Capture مقصد |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** ARP چه کمک می‌کند؟ *(پاسخ: 14-4-ت1)*

**ت2.** Session نیمه‌کاره؟ *(پاسخ: 14-4-ت2)*

**ت3.** چرا چند ابزار؟ *(پاسخ: 14-4-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا `get system arp` مفید است؟ *(پاسخ: 14-4-م1)*

**م2.** سناریو: Session SYN_SENT؛ چه می‌کنید؟ *(پاسخ: 14-4-م2)*

**معیار تسلط:** ترکیب ابزارها و ثبت تصویر کامل.

**اشتباهات رایج:** تکیه بر یک ابزار.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| ARP | Address Resolution Protocol | نگاشت IP-MAC | L2 |
| iprope | IPv4 policy lookup | تطبیق Policy | عیب‌یابی |
| Kernel route | Kernel routing table | جدول مسیر کرنل | — |

| English sentence | ترجمه |
|---|---|
| Combine several tools to build the full picture. | برای ساختن تصویر کامل چند ابزار را ترکیب کنید. |
| The session table shows the applied NAT and policy. | جدول Session NAT و Policy اعمال‌شده را نشان می‌دهد. |

#### کارت Lab — درس 14-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | تصویر کامل یک ارتباط |
| 2 | پیش‌نیاز | درس ۱۴-۲ |
| 3 | توپولوژی | FGT + Client + Server |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | یک ارتباط |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ۴ ابزار |
| 11 | سناریوی خرابی | Policy درست ولی ارتباط نه |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول Walk |
| 14 | معیار پذیرش | همخوانی |
| 15 | مستندات نهایی | `03-ops/full-picture.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-14-5"></a>

## درس 14-5 — MTU/MSS، DNS و مشکلات TCP/UDP

**فصل 14 - روز 5 · پیش‌نیاز: درس ۱۴-۴ · ۶ ساعت**

### ۱) معرفی درس

نشانه‌های «سایت‌های بزرگ باز نمی‌شود» یا «نام حل نمی‌شود» را با ابزار FortiOS ثابت می‌کنیم.

### ۲) پیش‌نیازها

فصل ۱۱ (MTU/MSS)؛ درس ۱۴-۱.

### ۳) توضیح مفهومی

- MSS Clamp در Policy: `set tcp-mss-sender` / `tcp-mss-receiver` (`Unverified` برای 7.0.3).
- MTU Interface: `set mtu-override enable` و `set mtu`.
- DNS: `show system dns`, `execute ping <name>`؛ Policy باید UDP/TCP 53 را اجازه دهد.
- TCP: Sniffer برای SYN/Retransmission؛ UDP: بدون Handshake.
- ICMP «Fragmentation needed» اگر Drop شود MTU Discovery می‌شکند.

### ۴) مثال ساده

ping با اندازه‌ی بزرگ و تنظیم MSS.

### ۵) مثال سازمانی

VPN: MSS Clamp برای حل بسته‌ی بزرگ.

### ۶) تصویر و توپولوژی

```text
big packet + DF -> blocked by smaller MTU
fix: MSS clamp / MTU
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces > port1 > Edit: Override default MTU value را فعال و 1400 را بگذارید.
2. Firewall Policy: ویژگی TCP MSS (در CLI) — GUI محدود است.
3. Network > DNS: سرورها.
4. Log & Report برای DNS Deny.
5. CLI برای tcp-mss-*.

#### روش خط فرمان (CLI)

```text
config system interface
    edit "port1"
        set mtu-override enable
        set mtu 1400
    next
end
config firewall policy
    edit 10
        set tcp-mss-sender 1360
        set tcp-mss-receiver 1360
    next
end
execute ping www.example.com
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- MSS = MTU − 40 (در بلوک مستقل محاسبه کنید: 1400 − 40 = 1360).
- بعد از تغییر، انتقال بزرگ را تست کنید.
- بازگشت: `unset`/مقدار پیش‌فرض.
- هشدار: MTU اشتباه ارتباط را می‌شکند.

### ۸) تست عملکرد

- آزمایش ping با DF و انتقال فایل بزرگ.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | صفحه‌ی کوچک باز، بزرگ نه |
| شواهد/دستور | ping با DF ۱۴۷۲ شکست |
| علت | MTU مسیر کم |
| رفع | MSS clamp/MTU |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** MSS چگونه؟ *(پاسخ: 14-5-ت1)*

**ت2.** DNS Policy؟ *(پاسخ: 14-5-ت2)*

**ت3.** نشانه MTU؟ *(پاسخ: 14-5-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا ICMP فرگمنت را نباید Drop کرد؟ *(پاسخ: 14-5-م1)*

**م2.** سناریو: HTTPS باز نمی‌شود ولی ping OK؛ حدس؟ *(پاسخ: 14-5-م2)*

**معیار تسلط:** اثبات و رفع مشکل MTU/MSS و DNS.

**اشتباهات رایج:** تنظیم MSS بدون محاسبه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| MSS clamp | TCP MSS clamping | تنظیم MSS | VPN |
| PMTUD | Path MTU Discovery | کشف MTU مسیر | ICMP |
| DNS | Domain Name System | حل نام | سرویس |

| English sentence | ترجمه |
|---|---|
| Clamp the TCP MSS on the tunnel. | MSS را روی Tunnel Clamp کنید. |
| Do not block ICMP fragmentation-needed messages. | پیام‌های ICMP «Fragmentation needed» را مسدود نکنید. |

#### کارت Lab — درس 14-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | MTU/MSS |
| 2 | پیش‌نیاز | درس ۱۴-۴ |
| 3 | توپولوژی | FGT + Client + Server |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | MTU 1400 |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | MTU کم |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping/ curl |
| 11 | سناریوی خرابی | صفحه‌ی کوچک باز، بزرگ نه |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | بسته بزرگ رد نمی‌شود/ بعد از MSS رد |
| 14 | معیار پذیرش | انتقال موفق |
| 15 | مستندات نهایی | `03-ops/mtu-mss.md` |
| 16 | Cleanup و بازگردانی | برگشت MTU |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-14-6"></a>

## درس 14-6 — تحلیل Log، Packet Walk و آزمون فصل

**فصل 14 - روز 6 · پیش‌نیاز: درس‌های ۱۴-۱ تا ۱۴-۵ · ۶ ساعت**

### ۱) معرفی درس

خواندن Log ترافیک و دنبال‌کردن کامل یک ارتباط با Packet Walk. آزمون فصل ارزیابی عملی است.

### ۲) پیش‌نیازها

درس‌های ۱۴-۱ تا ۱۴-۵.

### ۳) توضیح مفهومی

- Log: Forward Traffic فیلدها: srcip, dstip, policyid, action, nat, sentbyte.
- CLI (`Unverified`): `execute log filter category 0` + `execute log filter field srcip X` + `execute log display`.
- Packet Walk: جدول ۱۰ پرسش + خروجی ابزارها.
- آزمون: ۳ ارتباط ناشناخته (موفق/ناموفق) با Walk کامل.

### ۴) مثال ساده

تحلیل یک Log Deny.

### ۵) مثال سازمانی

سازمان: گزارش RCA با Log.

### ۶) تصویر و توپولوژی

```text
Log -> Session -> Route -> Policy -> NAT -> Walk table
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Forward Traffic: فیلتر.
2. Add Filter: Source/Policy ID.
3. Download Log.
4. FortiView.
5. Packet Capture.

#### روش خط فرمان (CLI)

```text
execute log filter category 0
execute log filter field srcip 192.168.20.11
execute log display
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Log باید قبل از تحلیل روشن باشد (`logtraffic all`).
- تحلیل: action/policyid/nat.
- معیار: ≥ ۴ از ۵ مورد.

### ۸) تست عملکرد

- ۳ ارتباط ناشناخته را تحلیل کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Log خالی است |
| شواهد/دستور | Policy بدون logtraffic |
| علت | Log خاموش |
| رفع | روشن‌کردن Log |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** کدام فیلد Policy را نشان می‌دهد؟ *(پاسخ: 14-6-ت1)*

**ت2.** Action deny یعنی؟ *(پاسخ: 14-6-ت2)*

**ت3.** Packet Walk شامل؟ *(پاسخ: 14-6-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Log اولین قدم است؟ *(پاسخ: 14-6-م1)*

**م2.** سناریو: Log نیست؛ چرا؟ *(پاسخ: 14-6-م2)*

**معیار تسلط:** آزمون ≥ ۴ از ۵ با Packet Walk.

**اشتباهات رایج:** تحلیل بدون Log.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Forward traffic | Forward traffic log | Log ترافیک عبوری | تحلیل |
| policyid | Policy ID | شناسه‌ی Policy | Log |

| English sentence | ترجمه |
|---|---|
| Analyze the forward traffic logs. | Logهای ترافیک عبوری را تحلیل کنید. |
| Document the packet walk with evidence. | Packet Walk را با شواهد مستند کنید. |

#### کارت Lab — درس 14-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون فصل ۱۴ |
| 2 | پیش‌نیاز | درس‌های ۱۴-۱ تا ۱۴-۵ |
| 3 | توپولوژی | FGT + Client + Server |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق فصل |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | ۳ ارتباط |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ابزارها |
| 11 | سناریوی خرابی | Log خالی است |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Walk |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/g-fgt2.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-14"></a>

## درس 14-7 — روش نظام‌مند عیب‌یابی: از علامت تا علت و رفع (با پرونده‌های واقعی)

**فصل ۱۴ · درس افزوده (تکمیل ۱۴-۶) · پیش‌نیاز: ۱۲-۰، ۱۲-۸، ۱۳-۷، ۵-۰ · ≈ ۸ ساعت**

> **وضعیت:** روش مستقل از برند + دستورهای FortiOS 7.0.3 (`Unverified` روی Image). خروجی‌ها نمونه‌ی آموزشی‌اند.

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. یک **فرایند عیب‌یابی ثابت** را اجرا کند (علامت، دامنه، فرضیه، شاهد، آزمون، رفع، تأیید، مستندسازی).
2. با «تقسیم مسیر» (Divide and Conquer) مرحله‌ی خرابی را در Packet Flow پیدا کند.
3. ابزارها را به سؤال درست وصل کند: Sniffer، Debug Flow، Session، Routing، ARP، Log، CPU/Memory، Interface Errors، DNS/DHCP/Auth.
4. از شواهد به **علت ریشه‌ای** برسد و دو علت هم‌زمان را از هم جدا کند.
5. پیش از «رفع»، اثر تغییر را پیش‌بینی و پس از آن اندازه‌گیری کند.

### ۲) پیش‌نیازها

Packet Flow (۱۲-۰)، Local-in/out (۱۲-۸)، Session (۱۳-۷)، ابزارهای Linux/Wireshark (فصل ۲، ۲۸).

### ۳) مفهوم پایه

عیب‌یابی ضعیف = «دستورها را حفظ کردن و پشت‌سرهم زدن». عیب‌یابی قوی = **فرضیه‌محور**: هر دستور برای پاسخ به یک سؤال مشخص است. اگر نتیجه فرضیه را رد کرد، فرضیه‌ی بعد.

### ۴) توضیح عمیق فنی

#### ۴-۱) فرایند هشت‌مرحله‌ای

``` text
1. Symptom      : what exactly fails? who? since when? what changed?
2. Scope        : one user / one subnet / everyone? one app / all apps?
3. Hypotheses   : list likely causes by layer (L1..L7, route, policy, NAT, profile, DNS, auth)
4. Evidence     : choose the cheapest test that splits the hypothesis space
5. Test         : run it with a narrow filter; record raw output
6. Root cause   : the change/condition that explains ALL evidence
7. Fix + verify : minimal change; positive and negative test; measure
8. Document     : symptom, evidence, cause, fix, prevention
```

#### ۴-۲) تقسیم مسیر روی Packet Flow

مسیر: کلاینت → سوئیچ → FortiGate Ingress → Route → Policy → NAT/Profile → Egress → ISP/سرور → برگشت. **در نقطه‌ی میانی** آزمون بگذارید:

- بسته در Ingress دیده می‌شود؟ (`diagnose sniffer packet <port> "host X" 4`)
- اگر نه: مشکل قبل از فایروال (کابل، VLAN، ARP، کلاینت).
- اگر بله: Debug Flow (Route/Policy/Drop؟).
- اگر Allowed و Egress دیده می‌شود: مشکل بعد از فایروال یا مسیر برگشت.

#### ۴-۳) نقشه‌ی «سؤال → ابزار»

| سؤال | ابزار |
|---|---|
| بسته به Interface رسید؟ | Sniffer/Packet Capture |
| ARP/Neighbor درست است؟ | `diagnose ip arp list`، `get system arp` |
| Route چیست؟ | `get router info routing-table details <ip>` |
| Policy کدام است؟ | Debug Flow، `diagnose firewall iprope lookup`، Log Forward |
| NAT چه شد؟ | `diagnose sys session list` |
| Session هست؟ | `diagnose sys session filter ...` |
| Interface خطا دارد؟ | `get system interface physical`، `diagnose hardware deviceinfo nic <port>` |
| CPU/Memory؟ | `get system performance status`، `diagnose sys top` |
| DNS؟ | `execute nslookup` (Local-out)، Sniffer روی 53 |
| DHCP؟ | Sniffer روی 67/68، `diagnose ... dhcp` |
| Auth؟ | `diagnose test authserver`، `diagnose debug application fnbamd -1` |
| VPN؟ | `diagnose vpn ike log filter`، `diagnose vpn tunnel list` |
| HA؟ | `get system ha status` |

(نام و فرمت دستورها با CLI Reference 7.0 تطبیق شود؛ `Unverified`.)

#### ۴-۴) خطاهای فکری

- **Confirmation bias:** فقط دنبال شاهد برای فرضیه‌ی اول بودن.
- **Fix-first:** تغییر چند چیز هم‌زمان؛ نمی‌دانید کدام اثر کرد.
- **Symptom ≠ cause:** «Drop شد» علامت است؛ علت Route/Policy/RPF است.
- **Debug طولانی:** Debug بدون Filter CPU را می‌خورد.

#### ۴-۵) مستندسازی RCA

قالب یک‌صفحه‌ای: عنوان، زمان، اثر، Timeline، شواهد (خروجی خام)، علت ریشه‌ای، اقدام فوری، اقدام پیشگیرانه.

### ۵) پرونده‌های حل‌شده

**پرونده ۱: «سایت X باز نمی‌شود»**

علامت: کاربر 192.168.10.5 به www.example.com نمی‌رسد؛ دیگران می‌رسند. دامنه: فقط یک کاربر.

``` text
FGT # diagnose sniffer packet any "host 192.168.10.5 and port 53" 4 10 l
FGT # diagnose debug flow filter addr 192.168.10.5
FGT # diagnose debug flow trace start 20
```

شاهد: کلاینت از DNS داخلی 192.168.10.2 درخواست می‌دهد؛ پاسخ NXDOMAIN. نتیجه: DNS ✓ فایروال بی‌تقصیر؛ سمت DNS Server/Cache. رفع: پاک کردن Cache، بررسی Record.

**پرونده ۲: «VPN بالاست ولی ترافیک نیست»**

شواهد: `diagnose vpn tunnel list` نشان می‌دهد Bytes out زیاد، in صفر. Debug Flow در سایت مقابل: «Denied by forward policy check (policy 0)». علت: Policy سمت مقابل نیست. رفع: Policy دوطرفه (فصل ۱۸).

**پرونده ۳: «کند است»**

شواهد: `get system performance status` CPU 85٪؛ `diagnose sys top` فرایند ipsengine/wad. علت: Profile روی همه‌ی ترافیک. رفع: Profile انتخابی و اندازه‌گیری قبل/بعد (فصل ۱۶). **علت دوم** هم‌زمان: Interface خطا (CRC) روی لینک — شواهد `get system interface physical`. پس «دو علت هم‌زمان» جدا مستند شوند.

**پرونده ۴ (سخت): «فقط وب‌های بزرگ باز نمی‌شود»**

شواهد: ping معمولی OK؛ `ping -f` اندازه‌ی بزرگ شکست؛ Capture: Retransmission دانلودهای بزرگ. علت: MTU/MSS در Tunnel (فصل ۱۸). رفع: `tcp-mss` و MTU Tunnel؛ بازبینی با Capture.

### ۶) طراحی و تصمیم‌گیری

| تصمیم | معیار |
|---|---|
| Debug یا Sniffer اول؟ | Sniffer ارزان‌تر؛ Debug برای Policy/Route/NAT |
| چقدر Capture؟ | Filter باریک، تعداد محدود |
| چه کسی تغییر می‌دهد؟ | Change مجاز، یک تغییر در هر زمان |
| Evidence | خروجی خام، زمان، دستور؛ در تیکت |

### ۷) پیاده‌سازی: GUI و CLI

**GUI:** Log & Report → Forward Traffic / System Events؛ Network → Diagnostics → Packet Capture؛ Dashboard → Performance؛ FortiView.

**CLI:** مطابق جدول ۴-۳؛ مثال الگو:

``` text
diagnose sniffer packet any "host 192.168.10.5" 4 20 l
diagnose debug reset
diagnose debug flow filter addr 192.168.10.5
diagnose debug flow show function-name enable
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

### ۸) Troubleshooting خود فرایند

| مشکل | اصلاح |
|---|---|
| Debug بسیار طولانی | Filter + `trace start N` محدود |
| خروجی نامفهوم | اول Sniffer؛ سپس Debug |
| علت مبهم | فرضیه را رد/تأیید کنید؛ دو علت ممکن است |
| بعد از رفع هنوز خراب | Session قدیمی (۱۳-۷) |

### ۹) نکات امنیتی

- Capture/Debug ممکن است داده‌ی حساس (رمز، توکن) ثبت کند؛ فایل را رمز/حذف کنید.
- Debug را همیشه Disable/Reset کنید.
- تغییر موقت (any-any) ممنوع؛ Policy موقت با Source دقیق و زمان.

### ۱۰) جمع‌بندی مفهومی

- عیب‌یابی = فرضیه + شاهد، نه حفظ دستور.
- تقسیم مسیر روی Packet Flow سریع‌ترین راه است.
- یک تغییر در هر زمان؛ شواهد خام ثبت شود.
- علت ریشه‌ای باید همه‌ی شواهد را توضیح دهد.
- پس از رفع: آزمون مثبت/منفی و مستندسازی.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) هشت مرحله‌ی عیب‌یابی را بنویسید. *(پاسخ: 14-7-ت1)*

**ت2.** (ساده) کدام ابزار نشان می‌دهد بسته به Interface رسیده؟ *(پاسخ: 14-7-ت2)*

**ت3.** (متوسط) تفاوت «علامت» و «علت» را با مثال بگویید. *(پاسخ: 14-7-ت3)*

**ت4.** (متوسط) چرا یک تغییر در هر زمان؟ *(پاسخ: 14-7-ت4)*

**ت5.** (سخت) کاربری می‌گوید نیمی از سایت‌ها کند است. فرضیه‌ها را به ترتیب بنویسید و برای هرکدام یک شاهد ارزان. *(پاسخ: 14-7-ت5)*

**ت6.** (سخت، طراحی) یک قالب RCA یک‌صفحه‌ای برای پرونده‌ی ۲ بنویسید. *(پاسخ: 14-7-ت6)*

**م1.** Confirmation bias چیست؟ *(پاسخ: 14-7-م1)*

**Q1.** Quick quiz (English): Why start with a sniffer before a debug flow? *(پاسخ: 14-7-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RCA | Root Cause Analysis | تحلیل علت ریشه‌ای |
| Hypothesis | Hypothesis | فرضیه |
| Evidence | Evidence | شاهد |
| Scope | Scope | دامنه‌ی مشکل |
| MTTR | Mean Time To Repair | میانگین زمان رفع |

- *Change one thing at a time and record the evidence.* ← هر بار یک چیز را تغییر دهید و شاهد را ثبت کنید.
- *The symptom is not the root cause.* ← علامت همان علت ریشه‌ای نیست.

### ۱۳) منابع

- Fortinet Docs: [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow)؛ FortiOS 7.0 Administration Guide — Troubleshooting.
- ITIL 4 — Incident and Problem Management (مفهومی).

## پاسخ‌های فصل 14

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 14-1

**14-1-ت1** — چون اگر لینک/VLAN خراب باشد بالاتر هیچ‌چیز معنا ندارد و آزمایش بیهوده است.

**14-1-ت2** — تا حجم Capture و بار CPU کنترل شود و دستگاه پر نشود.

**14-1-ت3** — لینک، VLAN، فیلتر اشتباه، یا Interface نادرست. با ARP و وضعیت لینک بررسی می‌شود.

**14-1-ت4** — Sniffer بسته‌ها را می‌بیند؛ Debug flow تصمیم FortiGate (Policy، Route، NAT) را نشان می‌دهد.

**14-1-ت5** — ping، debug flow، sniffer، تست DF با اندازه‌ی مختلف، PMTU، MSS-clamp، آزمون.

**14-1-ت6** — جدول پرسش/ابزار/خروجی مورد انتظار/اقدام بعدی.

**14-1-Q1** — Debug flow.


### پاسخ‌های بازنویسی عمیق درس 14-2

**14-2-ت1** — هدر به همراه نام Interface.

**14-2-ت2** — تعداد بسته‌ها تا توقف.

**14-2-ت3** — مقصد یا مسیر پاسخ نمی‌دهد.

**14-2-ت4** — ممکن است بسته در sniffer دیده نشود.

**14-2-ت5** — Capture چند Interface و مقایسه‌ی جهت‌ها.

**14-2-ت6** — فیلتر، تعداد، حذف pcap.

**14-2-Q1** — Verbosity 4.


### پاسخ‌های بازنویسی عمیق درس 14-3

**14-3-ت1** — ۲۰ بسته را Trace می‌کند.

**14-3-ت2** — Policy 2 اجازه داد.

**14-3-ت3** — Implicit Deny.

**14-3-ت4** — Route معکوس نامعتبر.

**14-3-ت5** — Route را اصلاح؛ Asymmetric؛ آزمون.

**14-3-ت6** — فیلتر، زمان، خروجی، تفسیر، رفع.

**14-3-Q1** — The route back to the source does not use the ingress interface.

**14-4-ت1** — ARP چه کمک می‌کند؟

تأیید L2 مقصد.

**14-4-ت2** — Session نیمه‌کاره؟

فقط SYN دیده شده.

**14-4-ت3** — چرا چند ابزار؟

هر کدام لایه‌ای را می‌بیند.

**14-4-م1** — چرا `get system arp` مفید است؟

نشان می‌دهد Gateway/مقصد L2 دیده شده یا نه.

**14-4-م2** — سناریو: Session SYN_SENT؛ چه می‌کنید؟

Capture مقصد.

**14-5-ت1** — MSS چگونه؟

MTU − 40.

**14-5-ت2** — DNS Policy؟

UDP/TCP 53.

**14-5-ت3** — نشانه MTU؟

بسته کوچک OK، بزرگ قفل.

**14-5-م1** — چرا ICMP فرگمنت را نباید Drop کرد؟

PMTUD می‌شکند.

**14-5-م2** — سناریو: HTTPS باز نمی‌شود ولی ping OK؛ حدس؟

MSS/MTU.

**14-6-ت1** — کدام فیلد Policy را نشان می‌دهد؟

policyid.

**14-6-ت2** — Action deny یعنی؟

ترافیک مسدود شد.

**14-6-ت3** — Packet Walk شامل؟

۱۰ پرسش با شواهد.

**14-6-م1** — چرا Log اولین قدم است؟

سریع‌ترین راه دیدن Allow/Deny.

**14-6-م2** — سناریو: Log نیست؛ چرا؟

logtraffic خاموش.


---

<a id="ch15"></a>


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

## درس 15-1 — طراحی معماری دوفایروالی

**فصل 15 - روز 1 · پیش‌نیاز: فصل ۱۳، ۱۴ · ۶ ساعت**

### ۱) معرفی درس

دو فایروال دو لایه‌ی دفاعی می‌دهند: Edge لبه‌ی اینترنت و DMZ؛ Internal شبکه‌ی داخلی. مدل طراحی و IP Plan را اول می‌نویسیم.

### ۲) پیش‌نیازها

فصل‌های ۱۱ تا ۱۴.

### ۳) توضیح مفهومی

- Edge: WAN، DMZ (Web)، Transit به Internal. Internal: Transit، Users، Servers (App/DB).
- قاعده: هیچ ترافیک اینترنتی مستقیم به Servers؛ Web فقط به App؛ App فقط به DB.
- Routing: Edge Default به ISP؛ Edge Static به شبکه‌های داخلی از Transit؛ Internal Default به Edge.
- NAT: SNAT اینترنت در Edge؛ VIP برای Web در Edge؛ Internal معمولاً بدون NAT (مسیردهی).
- هر دو فایروال Policy مستقل دارند؛ Packet Walk باید هر دو را شامل شود.

### ۴) مثال ساده

کاربر داخلی به اینترنت از دو فایروال می‌گذرد.

### ۵) مثال سازمانی

سازمان: Edge مدیریت‌شده توسط تیم امنیت؛ Internal توسط تیم شبکه.

### ۶) تصویر و توپولوژی

```text
ISP -- Edge(port1 203.0.113.2) -- DMZ 192.168.50.0/24 (Web .10)
         |port3 transit 10.255.0.1/30
         Internal(port1 10.255.0.2) -- Users 192.168.20.0/24
                                    -- Servers 192.168.90.0/24 (App .20, DB .30)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces برای هر FGT: طبق جدول.
2. Policy & Objects > Addresses.
3. Zones.
4. Static Routes.
5. VIP.

#### روش خط فرمان (CLI)

```text
# IP plan (example)
# WAN      203.0.113.0/29  ISP .1  EDGE .2  VIP web .3
# DMZ      192.168.50.0/24 EDGE .254  WEB .10
# TRANSIT  10.255.0.0/30   EDGE .1  INT .2
# USERS    192.168.20.0/24 INT .254
# SERVERS  192.168.90.0/24 INT .254  APP .20  DB .30
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- جدول IP مرجع همه‌ی Labهای فصل است.
- راستی‌آزمایی: هر Subnet هم‌پوشانی ندارد.
- بازگشت: ندارد.

### ۸) تست عملکرد

- جدول را با Subnet Calculator بدون ابزار بررسی کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | هم‌پوشانی Subnet |
| شواهد/دستور | Routeهای متناقض |
| علت | طراحی بی‌دقت |
| رفع | اصلاح IP Plan |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا دو فایروال؟ *(پاسخ: 15-1-ت1)*

**ت2.** Web چه چیزی را می‌بیند؟ *(پاسخ: 15-1-ت2)*

**ت3.** NAT کجا؟ *(پاسخ: 15-1-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Internal NAT نمی‌خواهد؟ *(پاسخ: 15-1-م1)*

**م2.** سناریو: کاربر به اینترنت نمی‌رسد؛ کدام فایروال؟ *(پاسخ: 15-1-م2)*

**معیار تسلط:** IP Plan و Policy Matrix هر دو فایروال.

**اشتباهات رایج:** هم‌پوشانی؛ Policy فقط در یک فایروال.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Edge firewall | Edge firewall | فایروال لبه | Internet |
| DMZ | Demilitarized zone | ناحیه‌ی حائل | Web |
| Transit | Transit network | لینک بین فایروال‌ها | /30 |

| English sentence | ترجمه |
|---|---|
| Place public services in the DMZ. | سرویس‌های عمومی را در DMZ بگذارید. |
| Each firewall enforces its own policy. | هر فایروال Policy خودش را اعمال می‌کند. |

#### کارت Lab — درس 15-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | طراحی معماری ۲ |
| 2 | پیش‌نیاز | فصل ۱۳، ۱۴ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | کاغذ |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | جدول IP |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | Plan + Matrix |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | هم‌پوشانی Subnet |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | فایل طراحی |
| 14 | معیار پذیرش | کامل |
| 15 | مستندات نهایی | `02-design/arch2.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-15-2"></a>

## درس 15-2 — ساخت Edge: WAN، DMZ، NAT و VIP

**فصل 15 - روز 2 · پیش‌نیاز: درس ۱۵-۱ · ۶ ساعت**

### ۱) معرفی درس

Edge اینترنت را به DMZ و Internal وصل می‌کند و NAT/VIP را انجام می‌دهد.

### ۲) پیش‌نیازها

درس ۱۵-۱؛ فصل ۱۳.

### ۳) توضیح مفهومی

- Interfaces: port1 WAN، port2 DMZ، port3 Transit.
- Default به ISP؛ Static به Users/Servers از Transit (10.255.0.2).
- Policy: DMZ→WAN (به‌روزرسانی)، WAN→DMZ (VIP Web HTTPS)، Transit→WAN (کاربران با NAT)، DMZ→Transit (محدود به App).
- VIP: 203.0.113.3:443 → 192.168.50.10:443.
- Log همه‌ی Policyها.

### ۴) مثال ساده

اینترنت به Web از VIP.

### ۵) مثال سازمانی

Edge سازمانی با Policy فهرست‌شده.

### ۶) تصویر و توپولوژی

```text
Internet -> VIP -> DMZ Web ; Transit(Users) -> NAT -> Internet
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Interfaces: port1/2/3.
2. Static Routes: Default + دو مسیر.
3. Virtual IPs: VIP-WEB.
4. Policy: WAN-to-WEB, USERS-to-WAN, DMZ-to-APP.
5. Log & Report.

#### روش خط فرمان (CLI)

```text
config router static
    edit 1
        set gateway 203.0.113.1
        set device "port1"
    next
    edit 2
        set dst 192.168.20.0 255.255.255.0
        set gateway 10.255.0.2
        set device "port3"
    next
    edit 3
        set dst 192.168.90.0 255.255.255.0
        set gateway 10.255.0.2
        set device "port3"
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Static به داخلی‌ها از Transit.
- VIP و Policy مثل درس ۱۳-۳.
- Policy کاربران: Transit→WAN با NAT.
- راستی‌آزمایی: `get router info routing-table all` و تست‌ها.
- بازگشت: حذف مسیرها/Policy.

### ۸) تست عملکرد

- ping از Edge به Transit و DMZ؛ curl به VIP.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Web از اینترنت نمی‌رسد |
| شواهد/دستور | Debug Flow: denied policy |
| علت | Policy WAN→DMZ نیست |
| رفع | ساخت Policy |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Edge چه مسئولیتی دارد؟ *(پاسخ: 15-2-ت1)*

**ت2.** Static به داخل چرا؟ *(پاسخ: 15-2-ت2)*

**ت3.** VIP کجا؟ *(پاسخ: 15-2-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Edge باید Route به Users داشته باشد؟ *(پاسخ: 15-2-م1)*

**م2.** سناریو: Return Path ناقص؛ علامت؟ *(پاسخ: 15-2-م2)*

**معیار تسلط:** ساخت Edge با GUI/CLI و تست.

**اشتباهات رایج:** فراموشی Route برگشت.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Transit | Transit link | لینک بین فایروال‌ها | — |
| Return path | Return route | مسیر برگشت | Edge |

| English sentence | ترجمه |
|---|---|
| Add static routes for the internal networks on the edge firewall. | برای شبکه‌های داخلی روی فایروال Edge مسیر Static اضافه کنید. |
| Publish the web server using a VIP. | سرور وب را با VIP منتشر کنید. |

#### کارت Lab — درس 15-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Edge |
| 2 | پیش‌نیاز | درس ۱۵-۱ |
| 3 | توپولوژی | FGT-EDGE + ISP + DMZ Web |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق جدول |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Edge کامل |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | curl/ping |
| 11 | سناریوی خرابی | Web از اینترنت نمی‌رسد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | دسترسی Web |
| 14 | معیار پذیرش | Log Edge |
| 15 | مستندات نهایی | `02-design/fgt-edge.md` |
| 16 | Cleanup و بازگردانی | Restore |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-15-3"></a>

## درس 15-3 — ساخت Internal: Users و Servers و Routing به Edge

**فصل 15 - روز 3 · پیش‌نیاز: درس ۱۵-۲ · ۶ ساعت**

### ۱) معرفی درس

Internal ارتباط کاربران و سرورها را کنترل می‌کند. Default آن Edge است.

### ۲) پیش‌نیازها

درس ۱۵-۲.

### ۳) توضیح مفهومی

- Interfaces: port1 Transit، port2 Users، port3 Servers.
- Default به Edge (10.255.0.1).
- Policy: Users→Servers (SMB/HTTPS محدود)، Users→Transit (اینترنت)، Servers→Transit (به‌روزرسانی محدود).
- بدون NAT در Internal.
- Zone و Objectهای استاندارد.

### ۴) مثال ساده

کاربران به اینترنت از Internal→Edge.

### ۵) مثال سازمانی

Internal Policy مجزای امنیت داخلی.

### ۶) تصویر و توپولوژی

```text
Users -> Internal -> (Transit) -> Edge -> Internet
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Interfaces/Zones.
2. Static Route Default به 10.255.0.1.
3. Policy.
4. Log.
5. Monitor.

#### روش خط فرمان (CLI)

```text
config router static
    edit 1
        set gateway 10.255.0.1
        set device "port1"
    next
end
config firewall policy
    edit 10
        set name "Users-to-Transit"
        set srcintf "ZN-USERS"
        set dstintf "port1"
        set srcaddr "NET-USERS-20"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "HTTP" "HTTPS" "DNS"
        set logtraffic all
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- NAT غیرفعال: Edge SNAT می‌کند.
- Policy فقط سرویس‌های لازم.
- راستی‌آزمایی: از Users ping/Browser؛ Log در هر دو فایروال.
- بازگشت: حذف Policy/Route.

### ۸) تست عملکرد

- Users به اینترنت و Servers.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Users اینترنت ندارند |
| شواهد/دستور | Log Internal: Allow؛ Edge: Deny |
| علت | Policy در Edge نیست (Transit→WAN) |
| رفع | ساخت Policy در Edge |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Default Internal کجاست؟ *(پاسخ: 15-3-ت1)*

**ت2.** NAT Internal؟ *(پاسخ: 15-3-ت2)*

**ت3.** Policy مضاعف؟ *(پاسخ: 15-3-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا هر دو Log را می‌خوانیم؟ *(پاسخ: 15-3-م1)*

**م2.** سناریو: Internal Allow ولی ارتباط نه؛ چه می‌کنید؟ *(پاسخ: 15-3-م2)*

**معیار تسلط:** ساخت Internal و اثبات با Log دو فایروال.

**اشتباهات رایج:** Policy فقط در یک فایروال.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Internal firewall | Internal firewall | فایروال داخلی | Users/Servers |
| Default route | Default route | مسیر پیش‌فرض | Edge |

| English sentence | ترجمه |
|---|---|
| Check the logs on both firewalls. | Logهای هر دو فایروال را بررسی کنید. |
| Do not NAT twice unless you must. | مگر ناچار نباشید دو بار NAT نکنید. |

#### کارت Lab — درس 15-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Internal |
| 2 | پیش‌نیاز | درس ۱۵-۲ |
| 3 | توپولوژی | FGT-INT + Users + Servers |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق جدول |
| 7 | وضعیت اولیه | Edge آماده |
| 8 | صورت مسئله | Internal کامل |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Log |
| 11 | سناریوی خرابی | Users اینترنت ندارند |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | اینترنت کاربران |
| 14 | معیار پذیرش | Log دو فایروال |
| 15 | مستندات نهایی | `02-design/fgt-internal.md` |
| 16 | Cleanup و بازگردانی | Restore |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-15-4"></a>

## درس 15-4 — DMZ سه‌لایه: Web، App، DB و Policy بین لایه‌ها

**فصل 15 - روز 4 · پیش‌نیاز: درس ۱۵-۳ · ۶ ساعت**

### ۱) معرفی درس

Web در DMZ فقط با App حرف می‌زند؛ App فقط با DB. این با Policy در هر دو فایروال تضمین می‌شود.

### ۲) پیش‌نیازها

درس‌های ۱۵-۲، ۱۵-۳.

### ۳) توضیح مفهومی

- Web (DMZ) → App (Servers) پورت 8080 از Edge Transit و Internal.
- App → DB پورت 3306 فقط در Internal.
- Internet → Web فقط 443.
- هیچ مسیر Internet→App/DB.
- تست منفی: Web→DB مسدود.

### ۴) مثال ساده

Web به App.

### ۵) مثال سازمانی

سازمان: Policy هر لایه با Profile امنیتی (فصل ۱۶).

### ۶) تصویر و توپولوژی

```text
Internet -> Web(DMZ) -> App -> DB   (only adjacent layers)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy Edge.
2. Policy Internal.
3. Objects.
4. Log.
5. Policy Lookup.

#### روش خط فرمان (CLI)

```text
# Edge: DMZ -> TRANSIT  : WEB -> APP tcp/8080
# Internal: TRANSIT -> SERVERS: WEB -> APP tcp/8080
# Internal: SERVERS -> SERVERS: APP -> DB tcp/3306 (same zone: intrazone or separate zones)
# Negative test: WEB -> DB must be DENIED
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Policy هر لایه یک ماتریس است.
- Intrazone بین App و DB اگر در یک Zone باشند: بهتر Zone جدا.
- راستی‌آزمایی: تست مثبت/منفی.
- بازگشت: حذف Policy.

### ۸) تست عملکرد

- curl از Web به App؛ تلاش Web→DB.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Web به DB دسترسی دارد |
| شواهد/دستور | Debug Flow: Allowed by Policy |
| علت | Policy گسترده |
| رفع | تنگ‌کردن |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا Web به DB نه؟ *(پاسخ: 15-4-ت1)*

**ت2.** تست منفی؟ *(پاسخ: 15-4-ت2)*

**ت3.** Policy در کدام فایروال؟ *(پاسخ: 15-4-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Zone جدا برای DB؟ *(پاسخ: 15-4-م1)*

**م2.** سناریو: Web به DB می‌رسد؛ چرا؟ *(پاسخ: 15-4-م2)*

**معیار تسلط:** ساخت سه‌لایه با تست مثبت/منفی.

**اشتباهات رایج:** Policy any بین Servers.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Three-tier | Three-tier architecture | Web/App/DB | — |
| Intrazone | Intrazone traffic | ترافیک درون Zone | Policy |

| English sentence | ترجمه |
|---|---|
| Allow only adjacent tiers to communicate. | فقط لایه‌های مجاور اجازه‌ی ارتباط دارند. |
| Test the negative cases as well. | موارد منفی را هم تست کنید. |

#### کارت Lab — درس 15-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | سه‌لایه |
| 2 | پیش‌نیاز | درس ۱۵-۳ |
| 3 | توپولوژی | Edge+Internal+Web/App/DB |
| 4 | تجهیزات | ۲ FGT + 3 Linux |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | جدول IP |
| 7 | وضعیت اولیه | Edge/Internal |
| 8 | صورت مسئله | Policy لایه‌ها |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | curl |
| 11 | سناریوی خرابی | Web به DB دسترسی دارد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | مثبت/منفی |
| 14 | معیار پذیرش | Web→DB رد |
| 15 | مستندات نهایی | `02-design/fgt-3tier.md` |
| 16 | Cleanup و بازگردانی | حذف Policy |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-15-5"></a>

## درس 15-5 — Packet Walk دو فایروال و NAT در دو نقطه

**فصل 15 - روز 5 · پیش‌نیاز: درس ۱۵-۴ · ۶ ساعت**

### ۱) معرفی درس

برای هر ارتباط باید Walk کامل از Client تا Server در هر دو فایروال بنویسید.

### ۲) پیش‌نیازها

درس ۱۵-۴.

### ۳) توضیح مفهومی

- برای هر جهت: Interface ورودی، Route، Policy، NAT، Interface خروجی در Edge و Internal.
- NAT: فقط Edge (SNAT) و VIP؛ آدرس‌ها در هر Hop تغییر می‌کنند.
- Sniffer در Transit برای دیدن آدرس‌های مقدماتی.
- Debug Flow در هر دو.
- جدول Walk محصول اصلی است.

### ۴) مثال ساده

Users به اینترنت.

### ۵) مثال سازمانی

Internet به Web.

### ۶) تصویر و توپولوژی

```text
Users -> INT -> EDGE -> ISP ; INTERNET -> EDGE(VIP) -> WEB
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Packet Capture Transit.
2. Log هر دو.
3. Policy Lookup.
4. FortiView.
5. Routing Monitor.

#### روش خط فرمان (CLI)

```text
# Walk table
# hop  device  in-if  route  policy  NAT  out-if
# 1    INT     port2  default-> p10   none  port1
# 2    EDGE    port3  default-> p31   snat  port1
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- هر ردیف با خروجی ابزار.
- راستی‌آزمایی: Sniffer روی Transit آدرس اصلی کاربر را نشان دهد.
- بازگشت: ندارد.

### ۸) تست عملکرد

- دو Walk کامل.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | آدرس مبدأ در Transit NAT شده |
| شواهد/دستور | Sniffer Transit: مبدأ ≠ کاربر |
| علت | NAT در Internal |
| رفع | حذف NAT |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** NAT کجا؟ *(پاسخ: 15-5-ت1)*

**ت2.** Walk چند ردیف؟ *(پاسخ: 15-5-ت2)*

**ت3.** Sniffer Transit چه می‌گوید؟ *(پاسخ: 15-5-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا جدول Walk؟ *(پاسخ: 15-5-م1)*

**م2.** سناریو: NAT مضاعف؛ علامت؟ *(پاسخ: 15-5-م2)*

**معیار تسلط:** دو Walk کامل با شواهد.

**اشتباهات رایج:** Walk ناقص.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Walk | Packet walk | مسیر بسته | — |
| SNAT | Source NAT | تغییر مبدأ | Edge |

| English sentence | ترجمه |
|---|---|
| Build a packet walk table across both firewalls. | جدول Packet Walk را روی هر دو فایروال بسازید. |
| Check the addresses on the transit link. | آدرس‌ها را روی لینک Transit بررسی کنید. |

#### کارت Lab — درس 15-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Walk دوفایروالی |
| 2 | پیش‌نیاز | درس ۱۵-۴ |
| 3 | توپولوژی | کل معماری |
| 4 | تجهیزات | ۲ FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | جدول IP |
| 7 | وضعیت اولیه | آماده |
| 8 | صورت مسئله | دو Walk |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Sniffer/Debug |
| 11 | سناریوی خرابی | آدرس مبدأ در Transit NAT شده |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول |
| 14 | معیار پذیرش | همخوانی |
| 15 | مستندات نهایی | `03-ops/walk-arch2.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-15-6"></a>

## درس 15-6 — خرابی‌ها و آزمون G6

**فصل 15 - روز 6 · پیش‌نیاز: درس‌های ۱۵-۱ تا ۱۵-۵ · ۶ ساعت**

### ۱) معرفی درس

سه خرابی (Route برگشت، Policy فایروال دوم، NAT مضاعف) و Gate G6.

### ۲) پیش‌نیازها

درس‌های ۱۵-۱ تا ۱۵-۵.

### ۳) توضیح مفهومی

- خرابی A: Route برگشت در Edge حذف.
- خرابی B: Policy Transit→WAN در Edge حذف.
- خرابی C: NAT فعال در Internal.
- روش: ۱۰ پرسش + Log هر دو + Sniffer Transit.
- G6: ۵ مورد (طراحی، Edge، Internal، سه‌لایه، Walk).

### ۴) مثال ساده

رفع خرابی A.

### ۵) مثال سازمانی

RCA برای خرابی B/C.

### ۶) تصویر و توپولوژی

```text
fault A,B,C -> evidence -> fix
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log هر دو.
2. Policy Lookup.
3. Routing Monitor.
4. Packet Capture.
5. Backup/Restore.

#### روش خط فرمان (CLI)

```text
get router info routing-table details 192.168.20.11
diagnose sniffer packet port3 "host 192.168.20.11" 4 20 l
diagnose debug flow filter addr 192.168.20.11
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- علت را با شواهد ثابت کنید.
- معیار: ≥ ۴ از ۵.
- Restore بکاپ بعد از آزمون.

### ۸) تست عملکرد

- سه خرابی با RCA.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Users اینترنت ندارند |
| شواهد/دستور | Log Edge: Denied (Transit→WAN) |
| علت | Policy Edge نیست |
| رفع | ساخت Policy |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** اولین قدم؟ *(پاسخ: 15-6-ت1)*

**ت2.** NAT مضاعف علامت؟ *(پاسخ: 15-6-ت2)*

**ت3.** G6 چه می‌سنجد؟ *(پاسخ: 15-6-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Log هر دو؟ *(پاسخ: 15-6-م1)*

**م2.** سناریو: TCP نمی‌بندد؛ بررسی؟ *(پاسخ: 15-6-م2)*

**معیار تسلط:** G6 ≥ ۴ از ۵.

**اشتباهات رایج:** حدس بدون شواهد.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| G6 | Gate 6 | آزمون فصل ۱۵ | — |
| RCA | Root cause analysis | علت ریشه‌ای | گزارش |

| English sentence | ترجمه |
|---|---|
| Verify the return route on the edge firewall. | مسیر برگشت را روی فایروال Edge بررسی کنید. |
| Prove the fault with evidence. | خرابی را با شواهد ثابت کنید. |

#### کارت Lab — درس 15-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | G6 |
| 2 | پیش‌نیاز | درس‌های ۱۵-۱ تا ۱۵-۵ |
| 3 | توپولوژی | Arch2 |
| 4 | تجهیزات | ۲ FGT + میزبان‌ها |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | جدول IP |
| 7 | وضعیت اولیه | آماده |
| 8 | صورت مسئله | سه خرابی |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Log/Sniffer |
| 11 | سناریوی خرابی | Users اینترنت ندارند |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | RCA |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/rca-arch2.md` |
| 16 | Cleanup و بازگردانی | Restore بکاپ |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-15"></a>

## پاسخ‌های فصل 15

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**15-1-ت1** — چرا دو فایروال؟

دو لایه‌ی دفاعی و جداسازی DMZ.

**15-1-ت2** — Web چه چیزی را می‌بیند؟

فقط App.

**15-1-ت3** — NAT کجا؟

Edge.

**15-1-م1** — چرا Internal NAT نمی‌خواهد؟

داخلی از مسیردهی کافی است و رد‌پایی ساده‌تر.

**15-1-م2** — سناریو: کاربر به اینترنت نمی‌رسد؛ کدام فایروال؟

هر دو را با Walk بررسی کنید.

**15-2-ت1** — Edge چه مسئولیتی دارد؟

NAT/VIP و ارتباط با ISP.

**15-2-ت2** — Static به داخل چرا؟

Edge باید بداند داخلی‌ها کجا هستند.

**15-2-ت3** — VIP کجا؟

Edge.

**15-2-م1** — چرا Edge باید Route به Users داشته باشد؟

برای برگشت ترافیک.

**15-2-م2** — سناریو: Return Path ناقص؛ علامت؟

TCP برقرار نمی‌شود.

**15-3-ت1** — Default Internal کجاست؟

Edge.

**15-3-ت2** — NAT Internal؟

معمولاً ندارد.

**15-3-ت3** — Policy مضاعف؟

هر دو فایروال لازم است.

**15-3-م1** — چرا هر دو Log را می‌خوانیم؟

Allow در یکی و Deny در دیگری شایع است.

**15-3-م2** — سناریو: Internal Allow ولی ارتباط نه؛ چه می‌کنید؟

Log Edge.

**15-4-ت1** — چرا Web به DB نه؟

کاهش سطح حمله.

**15-4-ت2** — تست منفی؟

تلاش برای ارتباط ممنوع.

**15-4-ت3** — Policy در کدام فایروال؟

هر دو.

**15-4-م1** — چرا Zone جدا برای DB؟

کنترل Policy دقیق‌تر.

**15-4-م2** — سناریو: Web به DB می‌رسد؛ چرا؟

Policy گسترده/Intrazone.

**15-5-ت1** — NAT کجا؟

Edge.

**15-5-ت2** — Walk چند ردیف؟

هر Hop یک ردیف.

**15-5-ت3** — Sniffer Transit چه می‌گوید؟

آدرس واقعی قبل از SNAT.

**15-5-م1** — چرا جدول Walk؟

تحلیل و مستند.

**15-5-م2** — سناریو: NAT مضاعف؛ علامت؟

آدرس مبدأ در Transit تغییر کرده.

**15-6-ت1** — اولین قدم؟

Log هر دو فایروال.

**15-6-ت2** — NAT مضاعف علامت؟

مبدأ در Transit NAT شده.

**15-6-ت3** — G6 چه می‌سنجد؟

معماری دوفایروالی.

**15-6-م1** — چرا Log هر دو؟

خرابی ممکن در هر کدام.

**15-6-م2** — سناریو: TCP نمی‌بندد؛ بررسی؟

Route برگشت.


---

<a id="end5"></a>


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
