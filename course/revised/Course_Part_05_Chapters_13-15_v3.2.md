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

> **نسخه‌ی اصلاح‌شده (v3.2):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۱۳-۷، ۱۴-۷ (دسته A). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

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

## درس 13-1 — اجزای Firewall Policy، ترتیب و Log

**فصل 13 - روز 1 · پیش‌نیاز: فصل ۱۲ · ۶ ساعت**

### ۱) معرفی درس

Firewall Policy قلب FortiGate است: چه کسی، به کجا، با چه سرویس و چه عملی. قاعده‌ی «اولین تطابق» و Default Deny را باید با Log اثبات کنید.

### ۲) پیش‌نیازها

Zone/Object/Route (فصل ۱۲).

### ۳) توضیح مفهومی

- اجزا: Incoming/Outgoing Interface، Source، Destination، Schedule، Service، Action، NAT، Security Profiles، Log.
- **First Match:** از بالا؛ اولین Policy مطابق اعمال می‌شود؛ Implicit Deny در پایان.
- `logtraffic all` برای Session کامل؛ Log ضمنی Deny با `fwpolicy-implicit-log` (`Unverified`).
- نام و Comment برای هر Policy الزامی (قابل‌خواندن).
- Policy بدون Route بی‌اثر است؛ مسیر را اول تأیید کنید.

### ۴) مثال ساده

کاربران VLAN20 به اینترنت فقط HTTP/HTTPS/DNS.

### ۵) مثال سازمانی

سازمان: Policy جدا برای کاربران، سرورها و مدیریت؛ ترتیب از خاص به عام.

### ۶) تصویر و توپولوژی

```text
USERS(ZN-USERS) --(HTTP,HTTPS,DNS; NAT)--> WAN(port1)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects > Firewall Policy > Create New.
2. Name Users-to-Internet؛ Incoming ZN-USERS؛ Outgoing port1؛ Source NET-USERS-20؛ Destination all.
3. Schedule always؛ Service HTTP/HTTPS/DNS؛ Action ACCEPT؛ NAT enable.
4. Log Allowed Traffic: All Sessions؛ OK.
5. Log & Report > Forward Traffic: ترافیک را ببینید.

#### روش خط فرمان (CLI)

```text
config firewall policy
    edit 10
        set name "Users-to-Internet"
        set srcintf "ZN-USERS"
        set dstintf "port1"
        set srcaddr "NET-USERS-20"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "HTTP" "HTTPS" "DNS"
        set logtraffic all
        set nat enable
        set comment "users web access"
    next
end
show firewall policy 10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `srcintf/dstintf` می‌توانند Zone باشند.
- `set nat enable`: SNAT با IP Interface خروجی.
- `set logtraffic all`: همه‌ی Sessionها لاگ شوند.
- راستی‌آزمایی: ترافیک تست و Log در Log & Report > Forward Traffic.
- بازگشت: `delete 10`.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | قانون عبور Stateful |
| 2 | مشکلی که حل می‌کند | کنترل جریان بین Zoneها |
| 3 | چه زمانی استفاده شود | هر ارتباط عبوری |
| 4 | چه زمانی استفاده نشود | ترافیک خود فایروال (Local-in) |
| 5 | پیش‌نیازها | Zone/Object/Route |
| 6 | وابستگی به Routing/Policy/NAT | Route و NAT |
| 7 | پیاده‌سازی | GUI/CLI |
| 8 | راستی‌آزمایی | Log/Session |
| 9 | عیب‌یابی | Policy بالاتر/ترتیب |
| 10 | خطاهای رایج | all/all |

### ۸) تست عملکرد

- از VPCS ping/Browser؛ Log را ببینید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ترافیک مجاز Block می‌شود |
| شواهد/دستور | Log: Denied (policy 0) |
| علت | Policy بالاتر مطابق است یا Policy نیست |
| رفع | تغییر ترتیب `move` |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** First Match یعنی چه؟ *(پاسخ: 13-1-ت1)*

**ت2.** Implicit deny؟ *(پاسخ: 13-1-ت2)*

**ت3.** چرا Log؟ *(پاسخ: 13-1-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Policy «all/all» خطرناک است؟ *(پاسخ: 13-1-م1)*

**م2.** سناریو: Policy هست ولی ترافیک نمی‌رود؛ دو بررسی؟ *(پاسخ: 13-1-م2)*

**معیار تسلط:** ساخت Policy با GUI/CLI و اثبات با Log.

**اشتباهات رایج:** ترتیب غلط؛ Log خاموش.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Firewall policy | Firewall policy | قانون عبور | FGT |
| Implicit deny | Implicit deny | انکار ضمنی | پایان |
| Schedule | Policy schedule | زمان اعمال | Policy |

| English sentence | ترجمه |
|---|---|
| Rules are evaluated top-down; the first match wins. | قوانین از بالا به پایین ارزیابی می‌شوند؛ اولین تطابق برنده است. |
| Enable logging for every policy you need to troubleshoot. | برای هر Policy که عیب‌یابی می‌کنید Log را روشن کنید. |

#### کارت Lab — درس 13-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Policy کاربران به اینترنت |
| 2 | پیش‌نیاز | فصل ۱۲ |
| 3 | توپولوژی | FGT + VPCS + ISP-Sim |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.20.0/24 |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Policy ایجاد و تست |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Log |
| 11 | سناریوی خرابی | ترافیک مجاز Block می‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Session مجاز |
| 14 | معیار پذیرش | تطابق Log |
| 15 | مستندات نهایی | `02-design/fgt-policy-v1.md` |
| 16 | Cleanup و بازگردانی | حذف Policy |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-13-2"></a>

## درس 13-2 — NAT: Policy NAT، IP Pool و Central NAT

**فصل 13 - روز 2 · پیش‌نیاز: درس ۱۳-۱ · ۶ ساعت**

### ۱) معرفی درس

برای خروج به اینترنت باید آدرس عوض شود. FortiGate چند روش دارد: NAT در خود Policy، IP Pool و Central NAT (جدول جدا). باید انتخاب درست و دلیلش را بدانید.

### ۲) پیش‌نیازها

درس ۱۳-۱.

### ۳) توضیح مفهومی

- **Policy NAT:** `set nat enable` با IP خروجی؛ ساده.
- **IP Pool:** آدرس‌های عمومی مشخص؛ انواع `overload`، `one-to-one`، `fixed-port-range`، `port-block-allocation`.
- **Central NAT:** `config system settings / set central-nat enable` و `central-snat-map`؛ NAT جدا از Policy (برای سازمان‌های بزرگ). فعال‌کردن آن رفتار Policyها را عوض می‌کند (`Unverified` برای 7.0.3).
- NAT اجازه‌ی عبور نمی‌دهد؛ Policy لازم است.
- ترتیب Central SNAT مثل Policy First Match.

### ۴) مثال ساده

Policy NAT با IP Interface خروجی.

### ۵) مثال سازمانی

سازمانی: IP Pool برای دو IP عمومی؛ Central NAT برای سیاست یکپارچه.

### ۶) تصویر و توپولوژی

```text
LAN -> [Policy (accept)] -> [SNAT: pool 203.0.113.10] -> ISP
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects > IP Pools > Create New: Name POOL-OUT؛ Type Overload؛ External IP Range 203.0.113.10-203.0.113.10.
2. Policy مربوطه > Edit: NAT را فعال و Use Dynamic IP Pool را انتخاب کنید.
3. Central NAT (اختیاری): System > Settings > Central NAT فعال؛ Policy & Objects > Central SNAT.
4. Network > Packet Capture روی port1 با فیلتر `icmp`.
5. Dashboard > FortiView Sessions برای Session.

#### روش خط فرمان (CLI)

```text
config firewall ippool
    edit "POOL-OUT"
        set type overload
        set startip 203.0.113.10
        set endip 203.0.113.10
    next
end
config firewall policy
    edit 10
        set nat enable
        set ippool enable
        set poolname "POOL-OUT"
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `type overload`: PAT با پورت.
- `ippool enable`+`poolname`: استفاده از Pool.
- راستی‌آزمایی: `diagnose sys session list` (nat-ip) یا Log (NAT IP).
- بازگشت: `set ippool disable`.
- Central NAT را فقط با Plan تغییر بدهید (اثر کلی).

### ۸) تست عملکرد

- Capture روی WAN: Source = آدرس Pool.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ارتباط ISP با IP Pool نمی‌رود |
| شواهد/دستور | Capture: Source داخلی یا IP دیگر |
| علت | Policy بدون NAT یا Pool |
| رفع | تنظیم nat/ippool |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Policy NAT و Central NAT؟ *(پاسخ: 13-2-ت1)*

**ت2.** انواع IP Pool؟ *(پاسخ: 13-2-ت2)*

**ت3.** NAT اجازه می‌دهد؟ *(پاسخ: 13-2-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Central NAT را با احتیاط فعال می‌کنیم؟ *(پاسخ: 13-2-م1)*

**م2.** سناریو: NAT کار نمی‌کند؛ چه بررسی؟ *(پاسخ: 13-2-م2)*

**معیار تسلط:** تنظیم NAT و اثبات با Capture/Session.

**اشتباهات رایج:** فراموشی nat؛ فعال‌کردن Central NAT بی‌برنامه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| IP Pool | Firewall IP pool | مجموعه IP برای NAT | SNAT |
| Central NAT | Central SNAT | NAT متمرکز | سازمانی |
| PBA | Port block allocation | تخصیص بلوک پورت | Log NAT |

| English sentence | ترجمه |
|---|---|
| NAT does not grant permission; the policy does. | NAT اجازه نمی‌دهد؛ Policy می‌دهد. |
| Use an IP pool to control the translated address. | برای کنترل آدرس ترجمه‌شده از IP Pool استفاده کنید. |

#### کارت Lab — درس 13-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | NAT با IP Pool |
| 2 | پیش‌نیاز | درس ۱۳-۱ |
| 3 | توپولوژی | FGT + ISP-Sim |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 203.0.113.10 |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | Pool overload |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Capture WAN |
| 11 | سناریوی خرابی | ارتباط ISP با IP Pool نمی‌رود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Source=Pool |
| 14 | معیار پذیرش | Source مطابق |
| 15 | مستندات نهایی | `02-design/fgt-nat.md` |
| 16 | Cleanup و بازگردانی | حذف Pool |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-13-3"></a>

## درس 13-3 — VIP، Port-Forward و Hairpin NAT

**فصل 13 - روز 3 · پیش‌نیاز: درس ۱۳-۲ · ۶ ساعت**

### ۱) معرفی درس

برای انتشار سرور داخلی به اینترنت از VIP (DNAT) و یک Policy استفاده می‌کنیم. دسترسی کاربران داخلی به همان VIP (Hairpin) مشکلات ویژه‌ای دارد.

### ۲) پیش‌نیازها

درس‌های ۱۳-۱، ۱۳-۲.

### ۳) توضیح مفهومی

- **VIP:** نگاشت `extip:extport` به `mappedip:mappedport`.
- Policy جداگانه با `dstaddr = <VIP>` لازم است (srcintf=WAN).
- Port-forward: فقط پورت لازم؛ Static VIP (بدون پورت) کل IP را نگاشت می‌کند و خطرناک‌تر است.
- **Hairpin:** کاربران داخلی به IP عمومی سرور داخلی می‌روند؛ نیاز به Policy و NAT صحیح برای جلوگیری از مسیر نامتقارن.
- VIP می‌تواند Return/ARP مرتبط روی Interface ایجاد کند.

### ۴) مثال ساده

VIP-WEB: 203.0.113.20:443 → 192.168.50.10:443.

### ۵) مثال سازمانی

سازمان: VIP برای وب و Mail؛ Policy با Profile امنیتی.

### ۶) تصویر و توپولوژی

```text
Internet -> 203.0.113.20:443 -> [FGT VIP DNAT] -> 192.168.50.10:443 (DMZ)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects > Virtual IPs > Create New > Virtual IP.
2. Name VIP-WEB-HTTPS؛ Interface port1؛ External IP 203.0.113.20؛ Mapped IP 192.168.50.10.
3. Port Forwarding را فعال: TCP؛ External 443؛ Mapped 443.
4. Firewall Policy > Create New: Incoming port1؛ Outgoing DMZ؛ Destination VIP-WEB-HTTPS؛ Service HTTPS؛ NAT غیرفعال.
5. تست از Client بیرونی و Log را ببینید.

#### روش خط فرمان (CLI)

```text
config firewall vip
    edit "VIP-WEB-HTTPS"
        set extintf "port1"
        set extip 203.0.113.20
        set mappedip "192.168.50.10"
        set portforward enable
        set protocol tcp
        set extport 443
        set mappedport 443
    next
end
config firewall policy
    edit 20
        set name "WAN-to-WEB"
        set srcintf "port1"
        set dstintf "DMZ"
        set srcaddr "all"
        set dstaddr "VIP-WEB-HTTPS"
        set action accept
        set schedule "always"
        set service "HTTPS"
        set logtraffic all
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- VIP تنها نگاشت است؛ Policy اجازه‌ی عبور.
- `dstaddr` Policy = نام VIP (نه IP داخلی).
- راستی‌آزمایی: از Client «اینترنت» `curl -k https://203.0.113.20`.
- بازگشت: حذف Policy و VIP.
- هشدار: VIP بدون محدودیت Source همه را اجازه می‌دهد.

#### کارت قابلیت (۱۰ پرسش)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | مفهوم | VIP/DNAT |
| 2 | مشکلی که حل می‌کند | انتشار سرور |
| 3 | چه زمانی استفاده شود | انتشار سرویس |
| 4 | چه زمانی استفاده نشود | همه‌ی پورت‌ها (Static) |
| 5 | پیش‌نیازها | Policy و Route به DMZ |
| 6 | وابستگی به Routing/Policy/NAT | Policy با dstaddr=VIP |
| 7 | پیاده‌سازی | GUI/CLI |
| 8 | راستی‌آزمایی | curl/Log |
| 9 | عیب‌یابی | نبود Policy |
| 10 | خطاهای رایج | Static VIP |

### ۸) تست عملکرد

- curl از Outside؛ Log: WAN-to-WEB.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | VIP تعریف شده ولی دسترسی نیست |
| شواهد/دستور | Log نیست؛ Debug Flow: «Denied by forward policy check» |
| علت | Policy برای VIP نیست |
| رفع | ساخت Policy با dstaddr=VIP |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** VIP چیست؟ *(پاسخ: 13-3-ت1)*

**ت2.** چرا Policy هم لازم است؟ *(پاسخ: 13-3-ت2)*

**ت3.** Hairpin چیست؟ *(پاسخ: 13-3-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Static VIP بدون پورت خطرناک است؟ *(پاسخ: 13-3-م1)*

**م2.** سناریو: از داخل به IP عمومی نمی‌رسم؛ علت؟ *(پاسخ: 13-3-م2)*

**معیار تسلط:** انتشار یک سرور با VIP و Policy و اثبات با Log/Session.

**اشتباهات رایج:** VIP بدون Policy؛ Static VIP.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| VIP | Virtual IP | DNAT | انتشار سرور |
| DNAT | Destination NAT | تغییر مقصد | VIP |
| Hairpin | Hairpin NAT | دسترسی داخلی به VIP | LAN |

| English sentence | ترجمه |
|---|---|
| Create a policy that uses the VIP as the destination. | Policyی بسازید که VIP مقصد آن باشد. |
| Prefer port forwarding over a static one-to-one VIP. | Port-forward را بر VIP یک‌به‌یک ترجیح دهید. |

#### کارت Lab — درس 13-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | انتشار وب با VIP |
| 2 | پیش‌نیاز | درس ۱۳-۲ |
| 3 | توپولوژی | Internet-Sim - FGT - DMZ Web |
| 4 | تجهیزات | FGT + Linux Web + Client |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 203.0.113.20؛ 192.168.50.10 |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | VIP+Policy |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | curl |
| 11 | سناریوی خرابی | VIP تعریف شده ولی دسترسی نیست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | صفحه‌ی وب |
| 14 | معیار پذیرش | Log WAN-to-WEB |
| 15 | مستندات نهایی | `02-design/fgt-vip.md` |
| 16 | Cleanup و بازگردانی | حذف VIP/Policy |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-13-4"></a>

## درس 13-4 — Session Table، Timeout و ابزارهای Session

**فصل 13 - روز 4 · پیش‌نیاز: درس ۱۳-۳ · ۶ ساعت**

### ۱) معرفی درس

Session Table نشان می‌دهد فایروال چه ارتباط‌هایی را می‌شناسد. خواندن آن بهترین راه دیدن «چه Policy/NAT اعمال شد» است.

### ۲) پیش‌نیازها

درس‌های ۱۳-۱ تا ۱۳-۳.

### ۳) توضیح مفهومی

- Session: پروتکل، مبدأ/مقصد، `policy_id`، NAT، Timeout، State.
- فیلتر قبل از list: `diagnose sys session filter ...` (بدون فیلتر خروجی بسیار بزرگ).
- `diagnose sys session list`، `session stat`، `session clear` (با احتیاط).
- Timeout قابل‌تنظیم (`config system session-ttl`) و رفتار TCP/UDP/ICMP.
- Session کثیف: بعد از تغییر Policy/Route گاهی باید Session پاک شود.

### ۴) مثال ساده

یک ping/HTTPS و دیدن ورودی در Session Table.

### ۵) مثال سازمانی

تحلیل «چرا بعد از تغییر Route هنوز مسیر قدیمی؟» Session قدیمی.

### ۶) تصویر و توپولوژی

```text
client -> FGT -> server
session: policy_id=10 nat to 203.0.113.2
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Dashboard > FortiView Sessions: Sessionهای فعال.
2. روی ردیف کلیک و Policy را ببینید.
3. System > Settings: Session TTL (نسبت به نسخه).
4. Monitor (Network) برای وضعیت Interface.
5. از Console `diagnose sys session list` را با فیلتر امتحان کنید.

#### روش خط فرمان (CLI)

```text
diagnose sys session filter clear
diagnose sys session filter src 192.168.20.11
diagnose sys session filter dport 443
diagnose sys session list
diagnose sys session stat
! WARNING: clear impacts users
diagnose sys session clear
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- filter قبل از list مصرف CPU/خروجی را کنترل می‌کند.
- در خروجی `policy_id=` و `hook=post dir=org act=snat` را بخوانید.
- `session clear` فقط با فیلتر یا در Maintenance.
- راستی‌آزمایی: ورودی Session برای ارتباط تست.
- بازگشت: ندارد.

### ۸) تست عملکرد

- ارتباط تست بزنید و Session مربوطه را پیدا کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | بعد از تغییر Policy رفتار قدیمی است |
| شواهد/دستور | Session قدیمی با policy_id قبلی |
| علت | Session موجود |
| رفع | پاک‌کردن Sessionهای مرتبط |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا filter قبل از list؟ *(پاسخ: 13-4-ت1)*

**ت2.** policy_id چیست؟ *(پاسخ: 13-4-ت2)*

**ت3.** چه زمانی clear؟ *(پاسخ: 13-4-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Session تازه از تغییر Policy تأثیر نمی‌گیرد؟ *(پاسخ: 13-4-م1)*

**م2.** سناریو: پس از Route جدید هنوز مسیر قدیمی؛ اقدام؟ *(پاسخ: 13-4-م2)*

**معیار تسلط:** خواندن Session و تفسیر NAT/Policy.

**اشتباهات رایج:** `session clear` بدون فیلتر.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Session table | Session table | جدول اتصال‌ها | عیب‌یابی |
| TTL | Session TTL | Timeout | Session |
| policy_id | Policy ID | شناسه‌ی Policy | Session |

| English sentence | ترجمه |
|---|---|
| Always apply a session filter before listing sessions. | قبل از فهرست‌کردن Sessionها همیشه فیلتر بزنید. |
| Clearing all sessions disconnects users. | پاک‌کردن همه‌ی Sessionها کاربران را قطع می‌کند. |

#### کارت Lab — درس 13-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | خواندن Session |
| 2 | پیش‌نیاز | درس ۱۳-۳ |
| 3 | توپولوژی | FGT + Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | ارتباط تست |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Session list |
| 11 | سناریوی خرابی | بعد از تغییر Policy رفتار قدیمی است |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | policy_id و NAT |
| 14 | معیار پذیرش | تفسیر درست |
| 15 | مستندات نهایی | `03-ops/session-notes.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-13-5"></a>

## درس 13-5 — مدیریت Policy: Shadow، تداخل Object، Hit Count و Schedule

**فصل 13 - روز 5 · پیش‌نیاز: درس ۱۳-۴ · ۶ ساعت**

### ۱) معرفی درس

با رشد سازمان Policyها زیاد و خطادار می‌شوند. باید Policy سایه (Shadowed)، تداخل Object و Policy بی‌استفاده را پیدا کنید.

### ۲) پیش‌نیازها

درس‌های ۱۳-۱ تا ۱۳-۴.

### ۳) توضیح مفهومی

- **Shadowed:** Policy بالاتر همان ترافیک را می‌گیرد و پایینی هرگز Hit نمی‌شود.
- **Hit Count** و Last Used (GUI) برای پاک‌سازی.
- **تداخل Object:** دو Address هم‌پوشان یا نام مشابه؛ ابهام Match.
- **Schedule:** Policy زمان‌دار؛ «always» پیش‌فرض.
- **Policy Lookup (GUI)** و `diagnose firewall iprope lookup` برای پیدا کردن Policy مطابق.

### ۴) مثال ساده

Policy 5 (all→all) بالاتر از Policy 10؛ Policy 10 هرگز Hit نمی‌شود.

### ۵) مثال سازمانی

سازمان: بازبینی فصلی Policy با Hit Count.

### ۶) تصویر و توپولوژی

```text
Policy 5: any->any ACCEPT (above)
Policy 10: users->web (never hit = shadowed)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects > Firewall Policy: ستون Hit Count/Last Used را فعال کنید.
2. Policy Lookup (بالای لیست): مبدأ/مقصد/پورت را وارد و Policy مطابق را ببینید.
3. روی Policy راست‌کلیک > Move > Before.
4. Policy & Objects > Addresses: ستون Ref و Object تکراری را بررسی کنید.
5. در Filter: Policy بدون Hit را فیلتر کنید.

#### روش خط فرمان (CLI)

```text
diagnose firewall iprope lookup 192.168.20.11 51234 8.8.8.8 443 tcp VLAN20
show firewall policy
config firewall policy
    move 10 before 5
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `iprope lookup`: ورودی (src، sport، dst، dport، proto، iif) ← Policy مطابق.
- `move X before Y`: تغییر ترتیب.
- راستی‌آزمایی: Hit Count Policy 10 بعد از ترافیک افزایش یابد.
- بازگشت: `move` برعکس.
- هشدار: جابه‌جایی ترتیب اثر فوری دارد.

### ۸) تست عملکرد

- ترافیک تست و Hit Count را مقایسه کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Policy جدید اثر ندارد |
| شواهد/دستور | Hit=0؛ iprope lookup Policy بالاتر را نشان می‌دهد |
| علت | Policy سایه |
| رفع | move یا تنگ‌کردن بالاتری |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Shadowed Policy؟ *(پاسخ: 13-5-ت1)*

**ت2.** Hit Count چه کمک می‌کند؟ *(پاسخ: 13-5-ت2)*

**ت3.** ابزار پیدا کردن Policy مطابق؟ *(پاسخ: 13-5-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Object هم‌پوشان مشکل می‌سازد؟ *(پاسخ: 13-5-م1)*

**م2.** سناریو: Policy جدید Hit نمی‌شود؛ بررسی؟ *(پاسخ: 13-5-م2)*

**معیار تسلط:** پیدا کردن و رفع یک Policy Shadowed با شواهد.

**اشتباهات رایج:** نادیده‌گرفتن Hit Count.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Shadowed | Shadowed policy | Policy پوشیده‌شده | بازبینی |
| Hit count | Policy hit count | تعداد Match | پاک‌سازی |
| iprope | IPv4 policy lookup | ابزار تطبیق | عیب‌یابی |

| English sentence | ترجمه |
|---|---|
| Review policies periodically using hit counts. | Policyها را به‌صورت دوره‌ای با Hit Count بازبینی کنید. |
| A shadowed policy never matches. | Policy سایه هرگز مطابق نمی‌شود. |

#### کارت Lab — درس 13-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | کشف Shadow |
| 2 | پیش‌نیاز | درس ۱۳-۴ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | دو Policy |
| 8 | صورت مسئله | Shadow بسازید |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | iprope lookup |
| 11 | سناریوی خرابی | Policy جدید اثر ندارد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Policy 5 مطابق |
| 14 | معیار پذیرش | رفع با move |
| 15 | مستندات نهایی | `03-ops/policy-review.md` |
| 16 | Cleanup و بازگردانی | بازگشت ترتیب |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-13-6"></a>

## درس 13-6 — سناریوهای خرابی (Policy/NAT/Route) و آزمون G5

**فصل 13 - روز 6 · پیش‌نیاز: درس‌های ۱۳-۱ تا ۱۳-۵ · ۶ ساعت**

### ۱) معرفی درس

جمع‌بندی: سه خرابی Policy، NAT، Route و Gate G5. هدف تشخیص با شواهد (Log، Session، Route).

### ۲) پیش‌نیازها

درس‌های ۱۳-۱ تا ۱۳-۵.

### ۳) توضیح مفهومی

- خرابی ۱: Policy اشتباه (سرویس/ترتیب).
- خرابی ۲: NAT اشتباه (nat disable یا Pool غلط).
- خرابی ۳: Route اشتباه (Default حذف/Gateway غلط).
- روش: Log ← Session ← Route ← Policy ← NAT.
- Gate G5: ۵ مورد (Policy، NAT، VIP، Session، Shadow).

### ۴) مثال ساده

سه خرابی عمدی و رفع.

### ۵) مثال سازمانی

سازمان: RCA مکتوب بعد از هر خرابی.

### ۶) تصویر و توپولوژی

```text
Symptom -> Log -> Session -> Route -> Policy -> NAT
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Forward Traffic فیلتر Source.
2. FortiView Sessions.
3. Monitor > Routing Monitor.
4. Policy Lookup.
5. Dashboard > Security Fabric ندارد؛ Network > Packet Capture در صورت نیاز.

#### روش خط فرمان (CLI)

```text
diagnose sys session filter src 192.168.20.11
diagnose sys session list
get router info routing-table details 8.8.8.8
diagnose firewall iprope lookup 192.168.20.11 51234 8.8.8.8 443 tcp VLAN20
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- هر دستور یک لایه را می‌سنجد.
- معیار: ≥ ۴ از ۵ مورد.
- گزارش RCA برای هر خرابی.

### ۸) تست عملکرد

- پنج مورد با مدرک.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ارتباط اینترنت کاربر قطع شد |
| شواهد/دستور | Log: Denied؛ Session: نیست؛ Route: S* هست |
| علت | Policy تغییر کرده |
| رفع | بازگرداندن Policy از بکاپ |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** ترتیب عیب‌یابی؟ *(پاسخ: 13-6-ت1)*

**ت2.** RCA چیست؟ *(پاسخ: 13-6-ت2)*

**ت3.** G5 چه می‌سنجد؟ *(پاسخ: 13-6-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا از Log شروع می‌کنیم؟ *(پاسخ: 13-6-م1)*

**م2.** سناریو: Policy Allow ولی ارتباط نه؛ بررسی؟ *(پاسخ: 13-6-م2)*

**معیار تسلط:** G5 ≥ ۴ از ۵.

**اشتباهات رایج:** حدس بدون شواهد.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RCA | Root cause analysis | علت ریشه‌ای | گزارش |
| G5 | Gate 5 | آزمون فصل ۱۳ | — |

| English sentence | ترجمه |
|---|---|
| Prove the root cause with logs and session data. | علت ریشه‌ای را با Log و Session ثابت کنید. |
| Document each fault as an RCA. | هر خرابی را به‌صورت RCA مستند کنید. |

#### کارت Lab — درس 13-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | G5 |
| 2 | پیش‌نیاز | درس‌های ۱۳-۱ تا ۱۳-۵ |
| 3 | توپولوژی | FGT + Client + ISP-Sim + Web |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق فصل |
| 7 | وضعیت اولیه | Baseline + Policy v1 |
| 8 | صورت مسئله | سه خرابی |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | show/diagnose |
| 11 | سناریوی خرابی | ارتباط اینترنت کاربر قطع شد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | RCA |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/rca-fgt-1.md` |
| 16 | Cleanup و بازگردانی | Restore بکاپ |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-13"></a>

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

**13-1-ت1** — First Match یعنی چه؟

اولین Policy مطابق اجرا می‌شود.

**13-1-ت2** — Implicit deny؟

پایان فهرست؛ همه‌ی ترافیک نامجاز Drop.

**13-1-ت3** — چرا Log؟

اثبات و عیب‌یابی.

**13-1-م1** — چرا Policy «all/all» خطرناک است؟

Least Privilege را از بین می‌برد.

**13-1-م2** — سناریو: Policy هست ولی ترافیک نمی‌رود؛ دو بررسی؟

Route و NAT/Session.

**13-2-ت1** — Policy NAT و Central NAT؟

NAT داخل Policy در برابر جدول جدا.

**13-2-ت2** — انواع IP Pool؟

overload، one-to-one، fixed-port-range، port-block-allocation.

**13-2-ت3** — NAT اجازه می‌دهد؟

خیر.

**13-2-م1** — چرا Central NAT را با احتیاط فعال می‌کنیم؟

رفتار NAT همه‌ی Policyها عوض می‌شود.

**13-2-م2** — سناریو: NAT کار نمی‌کند؛ چه بررسی؟

nat در Policy، Pool و Route.

**13-3-ت1** — VIP چیست؟

DNAT: نگاشت IP/پورت خارجی به داخلی.

**13-3-ت2** — چرا Policy هم لازم است؟

VIP فقط نگاشت است.

**13-3-ت3** — Hairpin چیست؟

دسترسی داخلی به IP عمومی سرور داخلی.

**13-3-م1** — چرا Static VIP بدون پورت خطرناک است؟

همه‌ی پورت‌ها نگاشت می‌شوند.

**13-3-م2** — سناریو: از داخل به IP عمومی نمی‌رسم؛ علت؟

Hairpin/Policy/NAT.

**13-4-ت1** — چرا filter قبل از list؟

حجم خروجی/بار CPU.

**13-4-ت2** — policy_id چیست؟

شناسه‌ی Policy که Session را ساخت.

**13-4-ت3** — چه زمانی clear؟

بعد از تغییر مسیر/Policy و با فیلتر.

**13-4-م1** — چرا Session تازه از تغییر Policy تأثیر نمی‌گیرد؟

Session موجود با Policy قبلی مطابق است.

**13-4-م2** — سناریو: پس از Route جدید هنوز مسیر قدیمی؛ اقدام؟

پاک‌کردن Session.

**13-5-ت1** — Shadowed Policy؟

Policy پایینی که هرگز Match نمی‌شود.

**13-5-ت2** — Hit Count چه کمک می‌کند؟

شناسایی Policy بی‌استفاده/سایه.

**13-5-ت3** — ابزار پیدا کردن Policy مطابق؟

iprope lookup / Policy Lookup.

**13-5-م1** — چرا Object هم‌پوشان مشکل می‌سازد؟

ابهام و Policy ناخواسته.

**13-5-م2** — سناریو: Policy جدید Hit نمی‌شود؛ بررسی؟

iprope lookup و ترتیب.

**13-6-ت1** — ترتیب عیب‌یابی؟

Log، Session، Route، Policy، NAT.

**13-6-ت2** — RCA چیست؟

علت ریشه‌ای ثبت‌شده.

**13-6-ت3** — G5 چه می‌سنجد؟

تک‌فایروالی کامل.

**13-6-م1** — چرا از Log شروع می‌کنیم؟

شواهد Deny/Allow را می‌دهد.

**13-6-م2** — سناریو: Policy Allow ولی ارتباط نه؛ بررسی؟

Route و NAT.


---

<a id="ch14"></a>


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

## درس 14-1 — چارچوب ۱۰ پرسش عیب‌یابی و مدل ابزارها

**فصل 14 - روز 1 · پیش‌نیاز: فصل ۱۳ · ۶ ساعت**

### ۱) معرفی درس

عیب‌یابی باید روشمند باشد. ده پرسش از ورود تا برگشت، و برای هر پرسش یک ابزار مشخص.

### ۲) پیش‌نیازها

فصل ۱۱ (مسیر بسته)، فصل ۱۳.

### ۳) توضیح مفهومی

- ۱ ورود؟ (Sniffer روی Interface ورودی). ۲ مبدأ/مقصد واقعی؟ (Sniffer/Log). ۳ Route؟ (routing-table/Debug Flow). ۴ Policy؟ (iprope/Debug Flow). ۵ NAT؟ (Session/Debug Flow). ۶ Session؟ (session list). ۷ خروج؟ (Sniffer خروجی). ۸ دریافت مقصد؟ (Capture مقصد). ۹ برگشت؟ (Sniffer دو جهت). ۱۰ نقطه‌ی شکست؟
- ابزارها: Sniffer، Debug Flow، Session، Routing Table، iprope، Log، Wireshark، ابزار Cisco، Windows/Linux (`ping/tracert/curl/ss`).
- قاعده: اول Sniffer (واقعیت روی سیم)، بعد Debug Flow (تصمیم فایروال).

### ۴) مثال ساده

یک ping شکست‌خورده با ۱۰ پرسش.

### ۵) مثال سازمانی

سازمان: چک‌لیست ۱۰ پرسشی برای هر تیکت.

### ۶) تصویر و توپولوژی

```text
Q1 ingress -> Q3 route -> Q4 policy -> Q5 NAT -> Q7 egress -> Q9 return
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Forward Traffic: ورودی مربوط را پیدا کنید.
2. Network > Packet Capture: Interface و فیلتر را بدهید.
3. Monitor > Routing Monitor.
4. Policy Lookup.
5. FortiView Sessions.

#### روش خط فرمان (CLI)

```text
# 10-question worksheet
# 1 ingress iface   : ?
# 2 src/dst         : ?
# 3 route chosen    : ?
# 4 policy id       : ?
# 5 NAT applied     : ?
# 6 session created : ?
# 7 egress iface    : ?
# 8 dst received    : ?
# 9 return path     : ?
# 10 failure point  : ?
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- برای هر تیکت جدول را پر کنید.
- هر پاسخ با یک خروجی ابزار ثابت شود.
- بازگشت: ندارد.

### ۸) تست عملکرد

- برای ۲ ارتباط (موفق/ناموفق) جدول را پر کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ارتباط ناموفق ولی نمی‌دانیم کجا |
| شواهد/دستور | جدول ناقص |
| علت | عیب‌یابی بدون چارچوب |
| رفع | پر کردن ۱۰ پرسش |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** اولین ابزار؟ *(پاسخ: 14-1-ت1)*

**ت2.** Sniffer یا Debug Flow؟ *(پاسخ: 14-1-ت2)*

**ت3.** چند پرسش داریم؟ *(پاسخ: 14-1-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا از دو جهت Capture می‌کنیم؟ *(پاسخ: 14-1-م1)*

**م2.** سناریو: پاسخ نمی‌رسد؛ اولین بررسی؟ *(پاسخ: 14-1-م2)*

**معیار تسلط:** پرکردن ۱۰ پرسش برای دو ارتباط.

**اشتباهات رایج:** پرش به Debug بدون Sniffer.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Sniffer | Packet sniffer | ضبط بسته | عیب‌یابی |
| Debug flow | Debug flow | ردیابی تصمیم‌ها | عیب‌یابی |
| RCA | Root cause analysis | علت ریشه‌ای | گزارش |

| English sentence | ترجمه |
|---|---|
| Start with a packet capture to see what really happens. | با Capture شروع کنید تا آنچه واقعاً رخ می‌دهد را ببینید. |
| Answer the ten questions with evidence. | به ده پرسش با شواهد پاسخ دهید. |

#### کارت Lab — درس 14-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | کارگاه ۱۰ پرسش |
| 2 | پیش‌نیاز | فصل ۱۳ |
| 3 | توپولوژی | FGT + Client + Server |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق فصل ۱۳ |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | دو ارتباط |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | ارتباط ناموفق ولی نمی‌دانیم کجا |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول کامل |
| 14 | معیار پذیرش | با شواهد |
| 15 | مستندات نهایی | `03-ops/ten-questions.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-14-2"></a>

## درس 14-2 — Packet Sniffer (CLI و GUI) و Wireshark

**فصل 14 - روز 2 · پیش‌نیاز: درس ۱۴-۱ · ۶ ساعت**

### ۱) معرفی درس

Sniffer نشان می‌دهد چه بسته‌ای واقعاً وارد/خارج می‌شود. فیلتر درست و ذخیره برای Wireshark مهم است.

### ۲) پیش‌نیازها

درس ۱۴-۱؛ Wireshark (فصل ۲).

### ۳) توضیح مفهومی

- فرمت: `diagnose sniffer packet <interface|any> "<filter>" <verbose> <count> <a|l>`.
- verbose: 1 سرآیند، 4 با نام Interface، 6 با سرآیند اترنت و hex.
- فیلتر BPF مثل Wireshark Capture Filter: `host`, `port`, `icmp`, `and`.
- `any` همه‌ی Interfaceها (نیاز به دقت).
- GUI: Network > Packet Capture با دانلود PCAP برای Wireshark.

### ۴) مثال ساده

ping از Client و دیدن Echo Request/Reply روی دو Interface.

### ۵) مثال سازمانی

تحلیل «بسته می‌رسد ولی پاسخ نه» با دو Sniffer.

### ۶) تصویر و توپولوژی

```text
client -> [port2 in] FGT [port1 out] -> server
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Packet Capture > Create New: Interface port1؛ Filter host 8.8.8.8.
2. Start و ترافیک بزنید.
3. Stop > Download برای Wireshark.
4. در Wireshark Display Filter: `ip.addr==8.8.8.8`.
5. برای Interface دوم تکرار کنید.

#### روش خط فرمان (CLI)

```text
diagnose sniffer packet any "host 192.168.20.11 and icmp" 4 20 l
diagnose sniffer packet port1 "host 8.8.8.8 and tcp port 443" 4 30 l
! stop with Ctrl+C
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `4`: نام Interface را هم نشان می‌دهد.
- `20`: تعداد بسته؛ `l`: زمان محلی.
- راستی‌آزمایی: Echo Request در Interface ورودی و Reply در همان.
- بازگشت: Ctrl+C.
- هشدار: بدون فیلتر در Production خروجی عظیم.

### ۸) تست عملکرد

- دو Sniffer هم‌زمان (ورودی/خروجی).

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Reply دیده نمی‌شود |
| شواهد/دستور | Sniffer خروجی: Request هست ولی Reply نه |
| علت | مقصد/برگشت |
| رفع | Capture مقصد؛ Route برگشت |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** verbose 4؟ *(پاسخ: 14-2-ت1)*

**ت2.** فیلتر چه کاری می‌کند؟ *(پاسخ: 14-2-ت2)*

**ت3.** ذخیره برای Wireshark؟ *(پاسخ: 14-2-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Sniffer روی دو Interface؟ *(پاسخ: 14-2-م1)*

**م2.** سناریو: SYN رد می‌شود ولی SYN-ACK نه؛ حدس؟ *(پاسخ: 14-2-م2)*

**معیار تسلط:** اجرای Sniffer با فیلتر و تفسیر نتایج.

**اشتباهات رایج:** Sniffer بدون فیلتر؛ فراموشی verbose.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Sniffer | diagnose sniffer | ضبط بسته | CLI |
| BPF | Berkeley Packet Filter | فیلتر Capture | فیلتر |
| PCAP | Packet capture file | فایل Capture | Wireshark |

| English sentence | ترجمه |
|---|---|
| Use a precise capture filter to limit the output. | از فیلتر Capture دقیق برای محدودکردن خروجی استفاده کنید. |
| Capture on both the ingress and egress interfaces. | روی Interface ورودی و خروجی Capture بگیرید. |

#### کارت Lab — درس 14-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Capture ICMP/TCP |
| 2 | پیش‌نیاز | درس ۱۴-۱ |
| 3 | توپولوژی | FGT + Client + Server |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق فصل ۱۳ |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | ping و curl |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | Sniffer |
| 11 | سناریوی خرابی | Reply دیده نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | دو Interface |
| 14 | معیار پذیرش | Request/Reply مشخص |
| 15 | مستندات نهایی | `03-ops/sniffer-notes.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-14-3"></a>

## درس 14-3 — Debug Flow: خواندن تصمیم فایروال

**فصل 14 - روز 3 · پیش‌نیاز: درس ۱۴-۲ · ۶ ساعت**

### ۱) معرفی درس

Debug Flow مسیر تصمیم‌ها را برای هر بسته نشان می‌دهد: Route، Policy، NAT، Drop. مهم‌ترین ابزار FortiOS.

### ۲) پیش‌نیازها

درس ۱۴-۲.

### ۳) توضیح مفهومی

- ترتیب: `diagnose debug reset` ← `flow filter ...` ← `flow show function-name enable` ← `flow trace start N` ← `diagnose debug enable`.
- خروجی‌های مهم: `received a packet`، `allocate a new session`، `find a route`، `Allowed by Policy-N`/`Denied by forward policy check`، `SNAT`.
- خطاهای معمول: `no session matched`، `reverse path check fail`، `denied by forward policy check`.
- بعد از کار: `diagnose debug disable` و `reset`.
- Debug را با فیلتر و تعداد محدود اجرا کنید.

### ۴) مثال ساده

ping از Client و دیدن Policy/NAT.

### ۵) مثال سازمانی

تشخیص «Denied by forward policy check» به‌جای حدس.

### ۶) تصویر و توپولوژی

```text
packet -> route lookup -> policy check -> NAT -> forward
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. GUI Debug Flow ندارد؛ از CLI Console (بالا-راست >_) استفاده کنید.
2. Log & Report > Forward Traffic برای مقایسه.
3. Policy Lookup برای تأیید Policy.
4. Network > Packet Capture برای تکمیل.
5. پایان: حتماً `diagnose debug disable`.

#### روش خط فرمان (CLI)

```text
diagnose debug reset
diagnose debug flow filter addr 192.168.20.11
diagnose debug flow filter proto 1
diagnose debug flow show function-name enable
diagnose debug flow trace start 20
diagnose debug enable
! generate traffic, then:
diagnose debug disable
diagnose debug reset
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `filter addr`: فقط ترافیک آن آدرس.
- `proto 1`: ICMP؛ 6 TCP؛ 17 UDP.
- `trace start 20`: ۲۰ بسته.
- راستی‌آزمایی: «Allowed by Policy-10» و `SNAT`.
- بازگشت: `disable` و `reset`. هشدار: Debug فعال‌مانده CPU را مصرف می‌کند.

### ۸) تست عملکرد

- ping و تفسیر هر خط خروجی.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | ارتباط Drop می‌شود |
| شواهد/دستور | «Denied by forward policy check (policy 0)» |
| علت | Policy نیست/ترتیب |
| رفع | ساخت Policy |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** اولین خط Debug Flow؟ *(پاسخ: 14-3-ت1)*

**ت2.** Policy 0 یعنی؟ *(پاسخ: 14-3-ت2)*

**ت3.** چرا reset؟ *(پاسخ: 14-3-ت3)*

### ۱۱) مرور و ارزیابی

**م1.** تفاوت «no route» و «denied by policy»؟ *(پاسخ: 14-3-م1)*

**م2.** سناریو: «reverse path check fail»؛ چرا؟ *(پاسخ: 14-3-م2)*

**معیار تسلط:** خواندن Debug Flow و تعیین علت.

**اشتباهات رایج:** فراموشی disable/reset.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Debug flow | diagnose debug flow | ردیابی بسته | عیب‌یابی |
| RPF | Reverse path forwarding check | بررسی مسیر برگشت | Drop |
| Policy 0 | Implicit deny | انکار ضمنی | تشخیص |

| English sentence | ترجمه |
|---|---|
| Use debug flow to see which policy and route were selected. | با Debug Flow ببینید کدام Policy و Route انتخاب شده است. |
| Always disable debugging when you finish. | پس از اتمام همیشه Debug را غیرفعال کنید. |

#### کارت Lab — درس 14-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Debug Flow |
| 2 | پیش‌نیاز | درس ۱۴-۲ |
| 3 | توپولوژی | FGT + Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | طبق فصل ۱۳ |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | ping |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | debug flow |
| 11 | سناریوی خرابی | ارتباط Drop می‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Policy-10 + SNAT |
| 14 | معیار پذیرش | تفسیر درست |
| 15 | مستندات نهایی | `03-ops/debug-flow.md` |
| 16 | Cleanup و بازگردانی | disable/reset |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

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

**14-1-ت1** — اولین ابزار؟

Sniffer.

**14-1-ت2** — Sniffer یا Debug Flow؟

Sniffer واقعیت سیم؛ Debug Flow تصمیم فایروال.

**14-1-ت3** — چند پرسش داریم؟

۱۰.

**14-1-م1** — چرا از دو جهت Capture می‌کنیم؟

برای تشخیص مسیر برگشت.

**14-1-م2** — سناریو: پاسخ نمی‌رسد؛ اولین بررسی؟

Sniffer روی Interface خروجی/برگشت.

**14-2-ت1** — verbose 4؟

نمایش نام Interface.

**14-2-ت2** — فیلتر چه کاری می‌کند؟

کاهش خروجی به ترافیک موردنظر.

**14-2-ت3** — ذخیره برای Wireshark؟

GUI Packet Capture > Download.

**14-2-م1** — چرا Sniffer روی دو Interface؟

نشان‌دادن NAT/مسیر.

**14-2-م2** — سناریو: SYN رد می‌شود ولی SYN-ACK نه؛ حدس؟

مسیر برگشت/Policy/مقصد.

**14-3-ت1** — اولین خط Debug Flow؟

received a packet.

**14-3-ت2** — Policy 0 یعنی؟

Implicit deny.

**14-3-ت3** — چرا reset؟

خاموش‌کردن و پاک‌سازی Debug.

**14-3-م1** — تفاوت «no route» و «denied by policy»؟

Route یا Policy مشکل دارد.

**14-3-م2** — سناریو: «reverse path check fail»؛ چرا؟

RPF: مسیر برگشت از Interface دیگر.

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
