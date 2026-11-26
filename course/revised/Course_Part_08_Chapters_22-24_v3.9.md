# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۸ از ۱۱ — فصل‌های ۲۲ تا ۲۴

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۸ از ۱۱ |
| فصل‌های این فایل | ۲۲ ، ۲۳ ، ۲۴ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۲۲–۲۴ تولید شد؛ HA، Multi-Firewall/Asymmetric، Data Center.** Labها «اجرا نشده»؛ HA/VDOM به لایسنس وابسته؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 13.

| Lab | وضعیت |
|---|---|
| 22-1 | اجرا نشده (فقط طراحی) |
| 22-2 | اجرا نشده (فقط طراحی) |
| 22-3 | اجرا نشده (فقط طراحی) |
| 22-4 | اجرا نشده (فقط طراحی) |
| 22-5 | اجرا نشده (فقط طراحی) |
| 23-1 | اجرا نشده (فقط طراحی) |
| 23-2 | اجرا نشده (فقط طراحی) |
| 23-3 | اجرا نشده (فقط طراحی) |
| 23-4 | اجرا نشده (فقط طراحی) |
| 24-1 | اجرا نشده (فقط طراحی) |
| 24-2 | اجرا نشده (فقط طراحی) |
| 24-3 | اجرا نشده (فقط طراحی) |
| 24-4 | اجرا نشده (فقط طراحی) |

---

<a id="ch22"></a>

> **نسخه‌ی اصلاح‌شده (v3.9):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۲۲-۰، ۲۴-۰ (دسته C). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

# فصل 22 — High Availability: FGCP، Session Sync و Failover

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۲۱.
**اهداف:** مفهوم HA (Active-Passive، Active-Active)؛ FGCP؛ Heartbeat؛ Priority و Override؛ Session Sync؛ Monitor Interface؛ تست Failover.
**هشدار لایسنس:** HA در VM به لایسنس مناسب نیاز دارد (`Needs-License`) و در Evaluation ممکن است محدود باشد؛ همه‌ی دستورها `Unverified`.
**اشتباهات رایج:** Heartbeat روی همان لینک داده؛ Priority/Override نادرست؛ ناهمسانی Firmware؛ نبود Monitor Interface.

**درس‌های فصل:**
- [درس 22-1 — مفاهیم HA و FGCP](#l-22-1)
- [درس 22-2 — پیکربندی HA Active-Passive](#l-22-2)
- [درس 22-3 — تست Failover و Session Sync](#l-22-3)
- [درس 22-4 — عیب‌یابی HA و Upgrade](#l-22-4)
- [درس 22-5 — آزمون فصل ۲۲](#l-22-5)

---

<a id="l-22-1"></a>

## درس 22-0 — HA در FortiGate (FGCP): Election، Heartbeat، Sync، Failover/Failback و Split-brain

**فصل ۲۲ · درس افزوده (پیش‌درس ۲۲-۱) · پیش‌نیاز: ۱۱-۷، ۱۳-۷، ۵-۷ · ≈ ۱۰ ساعت**

> **وضعیت (FortiOS 7.0.3):** مفاهیم FGCP، Split-brain و Session Pickup از مستند رسمی بررسی شد ([FGCP 7.0.3](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/62403/fgcp)، [Troubleshoot an HA formation](https://docs.fortinet.com/document/fortigate/7.4.0/administration-guide/946059/troubleshoot-an-ha-formation)، [Session pickup](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide/955521/session-pickup)). **دقت نسخه:** بعضی ویژگی‌ها مثل `backup-hbdev` در 7.6 معرفی شده و در 7.0.3 نیست. **Needs-License/محدودیت:** HA روی VM به لایسنس مناسب و دو VM با لایسنس معتبر نیاز دارد؛ در Lab Evaluation ممکن است محدود باشد. Lab «اجرا نشده».

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. تفاوت **Active-Passive** و **Active-Active** را بگوید و بداند چرا Active-Passive رایج‌تر است.
2. توضیح دهد **FGCP** چگونه عضو Primary را انتخاب می‌کند (Election) و چه چیزی هم‌گام می‌شود.
3. **Heartbeat** را درست طراحی کند (اختصاصی، Redundant) و **Split-brain** را تحلیل و پیشگیری کند.
4. **Configuration Sync** و **Session Pickup/Sync** را تفکیک و اثر هرکدام را در Failover بگوید.
5. **Interface Monitoring**، Link Failure و Device Failure را تحلیل کند.
6. **Failover/Failback** و `override` را با پیامدشان بشناسد.
7. محدودیت‌ها و وابستگی‌های نسخه/لایسنس را اعلام کند.

### ۲) پیش‌نیازها

Session/Stateful (۱۱-۷، ۱۳-۷)، Convergence (۵-۷)، Interface/VLAN FortiGate (فصل ۱۲)، ARP/MAC (فصل ۲، ۳).

### ۳) مفهوم پایه

فایروال لبه نقطه‌ی شکست واحد (SPOF) است. **HA** دو (یا بیشتر) دستگاه را در یک **Cluster** قرار می‌دهد تا با خرابی یکی، دیگری ترافیک را ادامه دهد. هدف فقط «یک Cluster ساختن» نیست؛ هدف **پیش‌بینی رفتار سیستم در انواع خرابی** است: خرابی لینک، خرابی دستگاه، قطع Heartbeat، خرابی نیمه‌کاره.

### ۴) توضیح عمیق فنی

#### ۴-۱) FGCP

**FortiGate Clustering Protocol (FGCP)** پروتکل اختصاصی Fortinet برای HA است. اعضا از طریق **Heartbeat** Interfaceها با هم صحبت می‌کنند. طبق مستند، هم‌گام‌سازی روی لینک Heartbeat با TCP/703 و UDP/703 انجام می‌شود. Cluster با **Group Name، Group ID/Password و Mode** هم‌هویت می‌شود.

| Mode | رفتار |
|---|---|
| Active-Passive (a-p) | یک Primary ترافیک می‌برد؛ Secondary آماده است |
| Active-Active (a-a) | Primary بار Inspection (UTM) را بین اعضا پخش می‌کند؛ ترافیک همچنان از Primary ورودی/خروجی می‌شود؛ پیچیده‌تر |

(Active-Active در FGCP «توزیع بار Session/UTM» است، نه ECMP واقعی؛ جزئیات مستند.)

#### ۴-۲) Election (انتخاب Primary)

به‌طور خلاصه (ترتیب دقیق و Age-difference را از مستند همان نسخه بخوانید؛ `Unverified` در جزئیات):

``` text
Default (override disabled):
 1. more monitored interfaces up
 2. longer HA uptime (age)
 3. higher priority
 4. higher serial number
With override enabled: monitored interfaces -> priority -> uptime -> serial
```

نتیجه: با `override disable` عضوی که بیشتر زنده بوده Primary می‌ماند و بعد از بازگشت دستگاه اصلی، **Failback خودکار رخ نمی‌دهد**؛ با `override enable` دستگاه با Priority بالاتر پس از بازگشت Primary می‌شود (Failback) ولی ممکن است باعث قطع کوتاه و Flap شود.

#### ۴-۳) Heartbeat

- Interfaceهای اختصاصی (`hbdev`) با Priority؛ حداقل دو لینک Redundant ترجیحاً مستقیم (Back-to-back).
- ترافیک Heartbeat شامل Hello و Sync (Config، Session). مستند توصیه می‌کند برای کاهش Split-brain: لینک Heartbeat Redundant، مستقیم، و برای سایت‌های دور زمان Lost Interval بیشتر.
- **Heartbeat را روی همان لینک داده/سوئیچ مشترک خراب نگذارید.**

#### ۴-۴) Split-brain

اگر اعضا Heartbeat را از دست بدهند ولی هر دو زنده باشند، **هر دو خود را Primary می‌پندارند**: آدرس IP/MAC تکراری، Sessionهای متناقض، قطعی شدید. طبق مستند علت‌ها: قطع/ناپایداری Heartbeat؛ راه‌های پیشگیری: لینک Back-to-back، Heartbeat Redundant، Lost Interval مناسب. (`backup-hbdev` در 7.6 اضافه شده و در 7.0.3 موجود نیست.) پس از رفع، یک عضو باید دوباره Join شود و Config Sync انجام شود؛ بررسی Config واگرا لازم است.

#### ۴-۵) Sync: Configuration و Session

- **Configuration Sync:** Primary پیکربندی را به Secondary می‌فرستد (به‌جز تنظیمات اختصاصی هر دستگاه مثل Hostname/HA priority). بررسی: `diagnose sys ha checksum cluster`.
- **Session Sync/Pickup:** طبق مستند Session Pickup جدول Session **TCP** را به Secondary هم‌گام می‌کند؛ UDP و ICMP تنظیم جداگانه‌ای دارند و پیش‌نیازشان فعال بودن Pickup TCP است. بدون Pickup، با Failover همه‌ی Sessionها قطع می‌شوند و کلاینت‌ها باید Session بسازند. با Pickup اغلب Sessionهای TCP ادامه می‌یابند. هزینه: پهنای Heartbeat و CPU.
- VPN/IPsec SA و بعضی State‌ها همگام نمی‌شوند یا بسته به نسخه متفاوت‌اند؛ پس از Failover IPsec ممکن است Rekey/Renegotiate کند (`Unverified`).

#### ۴-۶) Monitoring و انواع خرابی

| خرابی | تشخیص | رفتار |
|---|---|---|
| Link failure (Interface مانیتورشده) | Monitor Interface | تعداد Interface سالم کم می‌شود ← Failover |
| Device failure | قطع Heartbeat | Secondary Primary می‌شود |
| Heartbeat failure با دو دستگاه زنده | Split-brain | خطرناک |
| خرابی نرم‌افزار/CPU | Heartbeat/Process | Failover یا Cluster ناپایدار |
| خرابی ISP | Interface Up ولی لینک مرده | HA این را نمی‌بیند؛ نیاز Health-check/SD-WAN (۲۱-۷) |

> **درس مهم:** HA خرابی «فایروال» را پوشش می‌دهد، نه خرابی «سرویس ISP». این‌ها را با SD-WAN/Link Monitor مکمل کنید.

#### ۴-۷) Failover time

Failover معمولاً چند ثانیه (Detect + Election + ARP/MAC Update): بعد از Failover Primary جدید **Gratuitous ARP** می‌فرستد و MAC مجازی Cluster به Primary جدید منتقل می‌شود تا سوئیچ‌ها یاد بگیرند. نتیجه: چند ثانیه قطعی؛ Sessionها فقط با Pickup می‌مانند.

![شکل: HA، Heartbeat، Election و Split-brain.](../figures/ch22-l0-fig1.svg)

*شکل: HA، Heartbeat، Election و Split-brain.*

### ۵) مثال حل‌شده

**هدف:** Active-Passive با Heartbeat روی port3 و port4، Monitor روی port1 و port2.

``` text
config system ha
    set group-name "FGT-HA-LAB"
    set mode a-p
    set password <HA-PASSWORD>
    set hbdev "port3" 100 "port4" 50
    set monitor "port1" "port2"
    set priority 200
    set session-pickup enable
    set override disable
end
```

دستگاه دوم: همان `group-name/password/mode/hbdev`، `priority 100`.

**GUI:** System → HA → Mode: Active-Passive؛ Device Priority؛ Cluster Settings (Group Name، Password)؛ Heartbeat Interfaces (انتخاب و Priority)؛ Monitor Interfaces؛ Session Pickup.

**Verification:**

``` text
get system ha status
diagnose sys ha status
diagnose sys ha checksum cluster
diagnose sys ha history read
```

(`Unverified`.)

**مثال متوسط:** Failover آزمایشی: `execute ha manage` یا Shutdown Interface مانیتورشده؛ ping پیوسته از کلاینت؛ ثبت تعداد بسته‌های از دست‌رفته و زمان.

**مثال سخت (Split-brain):** کابل Heartbeat کشیده می‌شود و لینک داده‌ها سالم‌اند: دو Primary. شواهد: `get system ha status` در هر دستگاه خود را Primary نشان می‌دهد؛ ARP جدول سوئیچ دو MAC برای یک IP. راه‌حل فوری: اتصال دوباره‌ی Heartbeat و تعیین کدام عضو Primary بماند (ریست دیگری)، سپس بررسی Config Checksum. پیشگیری: Heartbeat Redundant و Back-to-back.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| a-p یا a-a؟ | a-p (سادگی)؛ a-a برای بار UTM زیاد |
| Heartbeat | ۲ لینک مجزا، مستقیم |
| `override` | خاموش (پایداری)؛ روشن فقط اگر Failback مطلوب و Flap کنترل شود |
| Session Pickup | روشن برای سرویس‌های حساس به قطع؛ هزینه‌اش را بسنجید |
| Monitor Interface | همه‌ی Interfaceهای حیاتی؛ نه Interface مدیریت |
| Firmware | یکسان؛ ارتقا طبق روال |
| لایسنس | هر دو دستگاه لایسنس معتبر |

### ۷) Troubleshooting

| علامت | شاهد | علت |
|---|---|---|
| Cluster Form نمی‌شود | Group/Password/Mode، لینک HB | ناهمسانی |
| Secondary Out-of-sync | `ha checksum cluster` | Config/Firmware |
| Failover بدون دلیل | `ha history` | Monitor/HB flap |
| دو Primary | `ha status` | Split-brain |
| Session قطع می‌شود | Pickup خاموش | فعال‌سازی/محدودیت UDP |
| بعد از Failover VPN قطع | IKE Log | Renegotiate |

### ۸) نکات امنیتی

- HA Password قوی؛ لینک HB را از شبکه‌ی کاربران جدا نگه دارید.
- Heartbeat روی سوئیچ مشترک قابل جعل/اختلال است؛ ترجیحاً مستقیم.
- نسخه‌ی 7.0.3 دارای CVE؛ HA آسیب‌پذیری را حل نمی‌کند.

### ۹) جمع‌بندی مفهومی

- FGCP: Heartbeat + Sync (Config، Session) + Election.
- Election: Monitor ← Age ← Priority ← Serial (با Override: Priority جلوتر).
- Split-brain از قطع HB با دستگاه‌های زنده؛ با HB Redundant/مستقیم پیشگیری می‌شود.
- Session Pickup TCP را حفظ می‌کند؛ UDP/ICMP جدا.
- HA ≠ حفاظت از خرابی ISP.

### ۱۰) تمرین و ارزیابی

**ت1.** (ساده) Active-Passive و Active-Active را مقایسه کنید. *(پاسخ: 22-0-ت1)*

**ت2.** (ساده) Split-brain یعنی چه؟ *(پاسخ: 22-0-ت2)*

**ت3.** (متوسط) با `override disable` پس از بازگشت Primary اصلی چه می‌شود؟ *(پاسخ: 22-0-ت3)*

**ت4.** (متوسط) چرا Heartbeat Redundant لازم است؟ *(پاسخ: 22-0-ت4)*

**ت5.** (سخت) پس از Failover کاربران باید Session TCP را دوباره بسازند؛ علت و راه‌حل؟ *(پاسخ: 22-0-ت5)*

**ت6.** (سخت، طراحی) برای سایت مرکزی با دو ISP و دو FGT، HA و SD-WAN را کنار هم طراحی و نقش هرکدام را بنویسید. *(پاسخ: 22-0-ت6)*

**م1.** `diagnose sys ha checksum cluster` برای چیست؟ *(پاسخ: 22-0-م1)*

**Q1.** Quick quiz (English): What causes a split-brain scenario in an HA cluster? *(پاسخ: 22-0-Q1)*

### ۱۱) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HA | High Availability | دسترس‌پذیری بالا |
| FGCP | FortiGate Clustering Protocol | پروتکل Cluster |
| HB | Heartbeat | نبض Cluster |
| SPOF | Single Point of Failure | نقطه‌ی شکست واحد |
| GARP | Gratuitous ARP | ARP اعلام‌کننده |
| Pickup | Session pickup | حفظ Session |

- *Split-brain happens when cluster members lose heartbeat and each assumes the primary role.* ← Split-brain وقتی رخ می‌دهد که اعضا Heartbeat را از دست بدهند و هر دو نقش Primary را فرض کنند.
- *HA protects against device failure, not against upstream ISP failure.* ← HA از خرابی دستگاه محافظت می‌کند، نه از خرابی ISP بالادست.

### ۱۲) منابع

- Fortinet Docs: [FGCP](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/62403/fgcp)، [Troubleshoot an HA formation](https://docs.fortinet.com/document/fortigate/7.4.0/administration-guide/946059/troubleshoot-an-ha-formation)، [Session pickup (7.6)](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide/955521/session-pickup) (برای مفهوم؛ تفاوت نسخه را بررسی کنید).

## درس 22-1 — مفاهیم HA برای طراحی: SPOF، سطوح افزونگی، انتخاب مدل و تحلیل خرابی‌ها

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰، ۱۱-۷، ۵-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ HA/VDOM Needs-License؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. SPOF را در توپولوژی تشخیص دهد و ماتریس خرابی بسازد.
2. HA، Redundancy، Load-balancing و DR را تفکیک کند.
3. A-P و A-A و Session Pickup را برای نیاز مشخص انتخاب کند.
4. هزینه/ریسک/محدودیت (لایسنس، Split-brain، Firmware) را بسنجد.
5. دسترس‌پذیری را محاسبه کند (۹۹٫۹ و ...).

### ۲) مفهوم پایه: چیست و چرا؟

HA یعنی «طراحی برای خرابی»، نه «دو دستگاه». باید بدانید HA چه خرابی‌هایی را پوشش می‌دهد و کدام را نه؛ و هزینه‌ی افزونگی چیست.

### ۳) توضیح عمیق فنی

#### ۱) ماتریس خرابی

| خرابی | HA فایروال پوشش می‌دهد؟ | راه مکمل |
|---|---|---|
| دستگاه/برق | بله | — |
| لینک Interface | بله (Monitor) | LAG |
| ISP/لینک بالادست | خیر | Dual-ISP/SD-WAN |
| Config اشتباه | خیر (Sync می‌شود) | Change/Canary |
| CVE مشترک | خیر | Patch/تنوع |
| سایت | خیر | DR |

#### ۲) دسترس‌پذیری

``` text
Availability = MTBF / (MTBF + MTTR)
Serial (both needed): A = A1 x A2        Parallel (either): A = 1 - (1-A1)(1-A2)
Example: single device 99.5%  -> HA pair parallel = 1 - 0.005^2 = 99.9975%
Downtime/year at 99.9% = 8.76 h ; at 99.99% = 52.6 min
```

#### ۳) انتخاب مدل

| نیاز | پاسخ |
|---|---|
| قطع کوتاه قابل‌قبول | A-P |
| تداوم Session | A-P + Session Pickup |
| بار UTM زیاد | A-A (محدودیت) |
| سایت دوم | DR/Multi-site |

#### ۴) هزینه/ریسک

لایسنس دو دستگاه، پیچیدگی، آزمون دوره‌ای، Firmware یکسان، Split-brain، ارتقای کنترل‌شده.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| A-P/A-A | a-p مگر نیاز بار |
| Pickup | حساس |
| DR | سایت |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ماتریس SPOF برای ISP، فایروال، سوئیچ، برق؛ اولویت.

**متوسط (محاسبه):** دستگاه تکی 99.5٪؛ جفت HA ⇒ 1−0.005²=99.9975٪؛ Downtime سالانه ≈ ۲۲ دقیقه؛ ولی با ISP تکی 99.9٪ ⇒ سقف کل 99.9٪ (حلقه ضعیف).

**سخت (قضاوت):** مدیر: «HA داریم پس قطع نداریم». چهار خرابی خارج از پوشش: ISP، Config خراب Sync‌شده، CVE مشترک/ارتقای هم‌زمان، قطع Heartbeat (Split-brain). طرح: Dual-ISP/SD-WAN، Change Canary، Patch مرحله‌ای، HB Redundant.

### ۸) Verification (اثبات صحت)

- ماتریس خرابی امضا‌شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Config خراب | HA status | Change/Rollback |

### ۱۰) نکات امنیتی

- HA آسیب‌پذیری را حل نمی‌کند.

### ۱۱) جمع‌بندی مفهومی

- HA طراحی برای خرابی؛ حلقه‌ی ضعیف سقف را تعیین می‌کند.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) SPOF چیست؟ *(پاسخ: 22-1-ت1)*

**ت2.** (ساده) HA ISP را پوشش می‌دهد؟ *(پاسخ: 22-1-ت2)*

**ت3.** (متوسط) دستگاه 99.5٪ و جفت HA موازی؛ دسترس‌پذیری؟ *(پاسخ: 22-1-ت3)*

**ت4.** (متوسط) چرا حلقه‌ی ضعیف سقف را تعیین می‌کند؟ *(پاسخ: 22-1-ت4)*

**ت5.** (سخت) چهار خرابی خارج از HA. *(پاسخ: 22-1-ت5)*

**ت6.** (سخت، طراحی) ماتریس خرابی برای سایت مرکزی. *(پاسخ: 22-1-ت6)*

**Q1.** Quick quiz (English): Why does the weakest component limit overall availability in a serial chain? *(پاسخ: 22-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SPOF | Single point of failure | نقطه‌ی شکست واحد |
| MTBF | Mean time between failures | میانگین فاصله‌ی خرابی |
| DR | Disaster recovery | بازیابی از فاجعه |

- *HA is not a substitute for change control.* ← HA جایگزین کنترل تغییر نیست.

### ۱۴) کارت Lab

**کارت Lab:** نقشه HA. **Evidence:** `02-design/ha-map.md`.

### ۱۵) منابع

- [FGCP](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/62403/fgcp)
- NIST SP 800-34

<a id="l-22-2"></a>

## درس 22-2 — پیکربندی HA Active-Passive: برگه‌ی طراحی، GUI، CLI و Verification

**فصل ۲۲ · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰ (FGCP، Election، Heartbeat) · ≈ ۶ ساعت**

> **وضعیت (7.0.3):** Needs-License (دو VM با لایسنس معتبر)؛ سینتکس `Unverified`؛ Lab «اجرا نشده». **هر Boot/تغییر فقط با تأیید کاربر.**

### ۱) هدف آموزشی

Cluster Active-Passive را با برگه‌ی طراحی، Heartbeat Redundant، Monitor Interface و Session Pickup بسازد و Verification/Backup/Rollback را اجرا کند.

### ۲) برگه‌ی طراحی

``` text
Units      : FGT-1 (priority 200), FGT-2 (priority 100); same model, same FortiOS, same license type
Group      : name FGT-HA-LAB, mode a-p, password <HA-PASSWORD>
Heartbeat  : port3 (priority 100), port4 (priority 50) back-to-back, no switch
Monitor    : port1 (WAN), port2 (LAN)
Session    : session-pickup enable (TCP)
Override   : disable (prevent flap)  [decision: failback manual]
Mgmt       : dedicated management interface per unit (reserved mgmt ip)
```

### ۳) مراحل

1. Backup هر دو. بررسی نسخه/Serial.
2. تنظیم HA روی FGT-1 (Primary) سپس FGT-2.
3. اتصال Heartbeat Back-to-back.
4. صبر برای Sync؛ بررسی Checksum.

**GUI:** System → HA → Mode Active-Passive؛ Device Priority؛ Group Name؛ Password؛ Heartbeat Interfaces (port3 100، port4 50)؛ Monitor Interfaces (port1، port2)؛ Session Pickup.

**CLI (`Unverified`):**

``` text
config system ha
    set group-name "FGT-HA-LAB"
    set mode a-p
    set password <HA-PASSWORD>
    set hbdev "port3" 100 "port4" 50
    set monitor "port1" "port2"
    set priority 200
    set session-pickup enable
    set override disable
end
```

FGT-2 همان ولی `priority 100`.

### ۴) Verification

``` text
get system ha status
diagnose sys ha status
diagnose sys ha checksum cluster
diagnose sys ha history read
```

انتظار: دو عضو، Primary/Secondary، Checksum یکسان، Heartbeat هر دو لینک Up.

### ۵) مثال‌ها

**ساده:** `ha status`: FGT-1 Primary؛ Hostname و Serial هر دو.

**متوسط:** Secondary «out of sync»: مقایسه‌ی Firmware/Config؛ `checksum cluster` مغایر؛ علت: نسخه‌ی متفاوت؛ رفع: ارتقای یکسان.

**سخت (Flap):** Cluster بین دو عضو سوئیچ می‌کند: History: Monitor Interface خراب مکرر؛ لینک port2 نوسان؛ شواهد Interface Errors؛ رفع: کابل/Duplex، Hold-down، `override disable`.

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| Cluster تشکیل نمی‌شود | Group/Password/Mode/HB |
| Secondary Sync نمی‌شود | Firmware/Config |
| Flap | Monitor/لینک |
| Split-brain | HB قطع |

### ۷) نکات امنیتی

- Password قوی؛ HB جدا از شبکه‌ی کاربران.
- Reserved Mgmt IP برای دسترسی به هر عضو.

### ۸) جمع‌بندی

- برگه‌ی طراحی؛ Heartbeat Redundant؛ Monitor مناسب.
- Firmware یکسان.
- Verification: status/checksum/history.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) چه چیزی در دو عضو باید یکسان باشد؟ *(پاسخ: 22-2-ت1)*

**ت2.** (متوسط) چرا `override disable`؟ *(پاسخ: 22-2-ت2)*

**ت3.** (سخت) Cluster Flap می‌کند؛ تحلیل. *(پاسخ: 22-2-ت3)*

**Q1.** Quick quiz (English): Which command compares configuration consistency between cluster members? *(پاسخ: 22-2-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| hbdev | Heartbeat device | Interface نبض |
| Reserved mgmt | Reserved management interface | مدیریت جدا برای هر عضو |

- *Use identical firmware on all cluster members.* ← روی همه‌ی اعضا Firmware یکسان استفاده کنید.

### ۱۱) Lab

**کارت Lab:** HA A-P. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ha-ap.md`.

### ۱۲) منابع

- Fortinet Docs: [FGCP](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/62403/fgcp).

<a id="l-22-3"></a>

## درس 22-3 — آزمون Failover/Failback و Session Pickup: طراحی تست، اندازه‌گیری و تحلیل

**فصل ۲۲ · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰، ۲۲-۲ · ≈ ۶ ساعت**

> **وضعیت:** آزمون فقط در Lab با تأیید؛ اعداد نمونه؛ `Unverified`.

### ۱) هدف آموزشی

آزمون Failover را برنامه‌ریزی (سناریو، معیار، اندازه‌گیری) و نتایج را تحلیل کند؛ اثر Session Pickup، VPN و ARP را ببیند.

### ۲) ماتریس آزمون

| # | سناریو | انتظار | اندازه‌گیری |
|---|---|---|---|
| 1 | قطع Primary (Power off) | Failover چند ثانیه | بسته‌های از دست‌رفته |
| 2 | قطع port1 (Monitor) | Failover | زمان |
| 3 | قطع یک Heartbeat | Cluster باقی | بدون Failover |
| 4 | قطع هر دو Heartbeat | Split-brain (آزمون کنترل‌شده) | ثبت رفتار |
| 5 | بازگشت Primary | بدون Failback (override disable) | تأیید |
| 6 | Session TCP طولانی (SSH) | با Pickup ادامه | Session |

### ۳) روش اندازه‌گیری

``` text
# client A (continuous)
ping -i 0.2 192.168.20.5 | ts
# session test
ssh user@192.168.20.5   (keep typing)
# FGT
get system ha status
diagnose sys ha history read
diagnose sys session list
```

``` text
Packet loss time ~= lost packets x ping interval
```

### ۴) مثال حل‌شده

**آزمون ۱:** ۱۵ بسته از دست رفته با فاصله 0.2 s = ≈ ۳ ثانیه قطع. SSH با Pickup ادامه یافت یا قطع شد: اگر قطع شد، Pickup/Hash/Interface Monitor را بررسی. **درس:** قطع ۳ ثانیه با Pickup معمولاً برای TCP قابل‌تحمل است؛ UDP/IPsec ممکن است Renegotiate کند.

**آزمون ۴ (Split-brain):** با قطع هر دو HB: هر دو Primary؛ ARP: دو MAC؛ ping ناپایدار. **اقدام:** وصل HB، ریست یک عضو، بررسی Checksum و Config. **پیشگیری:** HB Redundant/Back-to-back.

**مثال سخت:** پس از Failover VPN دوباره برقرار نمی‌شود: بررسی IKE: Peer SPI قدیمی؛ DPD/Rekey؛ در صورت لزوم `diagnose vpn ike gateway clear` (با احتیاط). ثبت.

### ۵) Troubleshooting

| علامت | علت |
|---|---|
| Failover کند | Heartbeat/Lost interval |
| Session قطع | Pickup خاموش/UDP |
| دو Primary | HB قطع |
| بعد از Failover VPN قطع | Renegotiate |

### ۶) نکات امنیتی

- آزمون Split-brain فقط Lab.
- Change و Rollback.

### ۷) جمع‌بندی

- آزمون Failover = سناریو + معیار + اندازه‌گیری.
- Pickup TCP را حفظ می‌کند.
- Split-brain را عمداً فقط در Lab بیازمایید.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) چگونه زمان قطع را اندازه می‌گیرید؟ *(پاسخ: 22-3-ت1)*

**ت2.** (متوسط) SSH پس از Failover قطع شد؛ چرا؟ *(پاسخ: 22-3-ت2)*

**ت3.** (سخت) ماتریس آزمون ۶ سناریویی را با انتظار بنویسید. *(پاسخ: 22-3-ت3)*

**Q1.** Quick quiz (English): How do you measure failover time with a continuous ping? *(پاسخ: 22-3-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Failover | Failover | انتقال به عضو دوم |
| Failback | Failback | بازگشت |
| Hold-down | Hold-down timer | تأخیر پیش از تغییر |

- *Test every failure mode and record the measured downtime.* ← هر حالت خرابی را تست و زمان قطع را ثبت کنید.

### ۱۰) Lab

**کارت Lab:** Failover. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ha-fail.md`.

### ۱۱) منابع

- Fortinet Docs: [Troubleshoot an HA formation](https://docs.fortinet.com/document/fortigate/7.4.0/administration-guide/946059/troubleshoot-an-ha-formation) (مفهوم؛ نسخه‌ی 7.0 را بررسی کنید).

<a id="l-22-4"></a>

## درس 22-4 — عیب‌یابی HA و ارتقای Cluster: روش، Out-of-sync، Flap، Split-brain، Upgrade Path و Rollback

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰، ۲۲-۲، ۲۲-۳، ۲۷-۴ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ HA/VDOM Needs-License؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مشکلات Cluster (Form نشدن، Out-of-sync، Flap، Split-brain) را با شواهد عیب‌یابی کند.
2. ارتقای Cluster را با Upgrade Path، Backup، Pre/Post-check برنامه‌ریزی کند.
3. Rollback را اجرا و اثبات کند.
4. Log/History HA را بخواند.
5. ریسک‌های ارتقا را مستند کند.

### ۲) مفهوم پایه: چیست و چرا؟

ارتقا و عیب‌یابی HA پرخطرترین عملیات‌اند. بدون Plan و Rollback، یک ارتقا می‌تواند هر دو عضو را از کار بیندازد.

### ۳) توضیح عمیق فنی

#### ۱) ابزارها

``` text
get system ha status
diagnose sys ha status
diagnose sys ha checksum cluster
diagnose sys ha history read
diagnose sys ha dump-by group
```

#### ۲) مشکلات و علل

| علامت | علت | رفع |
|---|---|---|
| Form نمی‌شود | Group/Password/Mode/HB | تطبیق |
| Out-of-sync | Firmware/Config/Checksum | Sync/ارتقا |
| Flap | Monitor/لینک/Override | کابل/Hold |
| Split-brain | HB قطع | HB Redundant |
| Session قطع | Pickup | فعال‌سازی |

#### ۳) Plan ارتقا

``` text
1 Release notes + Upgrade path (may require intermediate versions)
2 Backups of both; export certs/licenses info
3 Pre-check: cluster healthy, checksums equal, HB links ok, no pending alerts
4 Upgrade (FGCP typically upgrades secondary, fails over, then upgrades former primary - per doc)
5 Post-check: HA status, sync, sessions, VPN, services
6 Rollback criteria and procedure (firmware + config)
```

#### ۴) Rollback

Firmware قبلی + Config Backup؛ اگر ارتقای مرحله‌ای شکست: بازگشت عضو به نسخه‌ی قبل و Sync؛ تأیید.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Out-of-sync: Firmware متفاوت؛ ارتقای عضو؛ checksum یکسان.

**متوسط (تحلیل):** Flap: History: Monitor port2 down/up هر ۲ دقیقه؛ Interface Errors؛ کابل؛ رفع؛ پایدار.

**سخت (ارتقا):** Upgrade Path نیاز به نسخه‌ی میانی داشت؛ ارتقای مستقیم Secondary را Sync نکرد؛ Rollback با Backup؛ Plan اصلاح با مرحله‌ی میانی؛ RCA و آزمون در Lab.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get system ha status
diagnose sys ha checksum cluster
diagnose sys ha history read
execute backup config sftp pre-upgrade.conf 192.168.90.10 backup-user <PASSWORD>
```

### ۸) Verification (اثبات صحت)

- Pre/Post-check ثبت.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Out-of-sync | checksum | Firmware/Config |
| Flap | history | Monitor/لینک |
| Split-brain | ha status | HB |

### ۱۰) نکات امنیتی

- Change و Backup.

### ۱۱) جمع‌بندی مفهومی

- Plan + Backup + Check + Rollback.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) checksum cluster چیست؟ *(پاسخ: 22-4-ت1)*

**ت2.** (ساده) چرا Upgrade Path؟ *(پاسخ: 22-4-ت2)*

**ت3.** (متوسط) Pre-check چه چیزهایی؟ *(پاسخ: 22-4-ت3)*

**ت4.** (متوسط) Flap؛ علل. *(پاسخ: 22-4-ت4)*

**ت5.** (سخت) ارتقا شکست خورد؛ Rollback. *(پاسخ: 22-4-ت5)*

**ت6.** (سخت، طراحی) Plan ارتقای Cluster. *(پاسخ: 22-4-ت6)*

**Q1.** Quick quiz (English): What must be backed up before a cluster firmware upgrade? *(پاسخ: 22-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Upgrade path | Firmware upgrade path | مسیر ارتقا |

- *Back up before upgrading.* ← قبل از ارتقا Backup بگیرید.

### ۱۴) کارت Lab

**کارت Lab:** Upgrade HA. **Evidence:** `03-ops/ha-upgrade.md`.

### ۱۵) منابع

- Fortinet Docs: FGCP، Firmware upgrade (7.0)
- [Troubleshoot an HA formation](https://docs.fortinet.com/document/fortigate/7.4.0/administration-guide/946059/troubleshoot-an-ha-formation)

<a id="l-22-5"></a>

## درس 22-5 — آزمون عملی HA: طراحی، Failover، Split-brain کنترل‌شده، Upgrade و RCA — صورت مسئله و Rubric

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰ تا ۲۲-۴ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ HA/VDOM Needs-License؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Cluster را بسازد و ۶ آزمون Failover را اندازه بگیرد.
2. Split-brain را در Lab شبیه‌سازی و رفع کند.
3. ارتقا/Rollback آزمایشی را اجرا کند.
4. RCA و Evidence ارائه دهد.

### ۲) مفهوم پایه: چیست و چرا؟

آزمون جامع HA (Lab، Needs-License).

### ۳) توضیح عمیق فنی

#### صورت مسئله

1. HA A-P با HB Redundant و Monitor.
2. ماتریس ۶ آزمون (۲۲-۳).
3. Split-brain کنترل‌شده (قطع HBها) و بازیابی.
4. ارتقا/Rollback.
5. عیب (مربی): Heartbeat تنها یک لینک؛ Monitor اشتباه.

#### کلید

- Failover ≈ ۳–۶ s (اندازه).
- Split-brain: دو Primary؛ بازیابی با ریست یک عضو و Checksum.
- پیشگیری: HB Redundant/Back-to-back.

#### Rubric

ساخت ۲۵؛ آزمون ۳۰؛ Split-brain ۱۵؛ ارتقا ۱۰؛ Evidence ۱۵؛ صداقت ۵.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Cluster Healthy.

**متوسط:** Failover.

**سخت:** Split-brain.

### ۸) Verification (اثبات صحت)

- Evidence HA.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ناقص | Rubric | کسری |

### ۱۰) نکات امنیتی

- Lab فقط.

### ۱۱) جمع‌بندی مفهومی

- شواهد.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) وظایف آزمون؟ *(پاسخ: 22-5-ت1)*

**ت2.** (ساده) چرا Split-brain فقط Lab؟ *(پاسخ: 22-5-ت2)*

**ت3.** (متوسط) Failover را چگونه اندازه می‌گیرید؟ *(پاسخ: 22-5-ت3)*

**ت4.** (متوسط) Monitor اشتباه چه می‌کند؟ *(پاسخ: 22-5-ت4)*

**ت5.** (سخت) RCA Split-brain. *(پاسخ: 22-5-ت5)*

**ت6.** (سخت، طراحی) بهبود. *(پاسخ: 22-5-ت6)*

**Q1.** Quick quiz (English): How is split-brain best avoided? *(پاسخ: 22-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HB | Heartbeat | نبض |

- *Test every failure mode.* ← هر حالت خرابی را تست کنید.

### ۱۴) کارت Lab

**کارت Lab:** آزمون HA. **Evidence:** `03-ops/ha-exam.md`.

### ۱۵) منابع

- درس‌های ۲۲-۰ تا ۲۲-۴

## پاسخ‌های فصل 22

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 22-1

**22-1-ت1** — نقطه‌ی شکست واحد.

**22-1-ت2** — خیر؛ SD-WAN/Dual-ISP.

**22-1-ت3** — 1−0.005×0.005 = 99.9975٪.

**22-1-ت4** — دسترس‌پذیری سری ضرب می‌شود؛ ISP 99.9٪ کل را محدود می‌کند.

**22-1-ت5** — ISP، Config خراب، CVE مشترک، Split-brain.

**22-1-ت6** — جدول با ستون راه مکمل و RTO.

**22-1-Q1** — Because serial availabilities multiply, so the lowest one dominates.

### پاسخ‌های بازنویسی درس 22-2

**22-2-ت1** — مدل، Firmware، نوع لایسنس، Group/Password/Mode و Hbdev سازگار.

**22-2-ت2** — برای جلوگیری از Failback ناخواسته و Flap.

**22-2-ت3** — Monitor Interface نوسان‌دار، لینک/کابل، Hold-down؛ شاهد: ha history و Interface Errors.

**22-2-Q1** — diagnose sys ha checksum cluster.


### پاسخ‌های بازنویسی درس 22-3

**22-3-ت1** — Ping پیوسته با فاصله‌ی مشخص؛ قطع ≈ بسته‌های از دست‌رفته × فاصله.

**22-3-ت2** — Session Pickup خاموش یا ترافیک UDP/IPsec یا تغییر Interface؛ بررسی Pickup.

**22-3-ت3** — قطع Primary، قطع Monitor، قطع یک HB، قطع هر دو HB (Lab)، بازگشت Primary، Session طولانی؛ هر کدام با انتظار و اندازه‌گیری.

**22-3-Q1** — Count lost replies multiplied by the ping interval.


### پاسخ‌های بازنویسی عمیق درس 22-4

**22-4-ت1** — مقایسه‌ی Config اعضا.

**22-4-ت2** — ممکن است ارتقای مستقیم پشتیبانی نشود و نسخه‌ی میانی لازم باشد.

**22-4-ت3** — Cluster سالم، Checksum یکسان، HB، Backup، Alert.

**22-4-ت4** — Monitor/لینک/Override/HB.

**22-4-ت5** — Firmware+Config قبلی، Sync، تأیید.

**22-4-ت6** — مراحل ۱–۶ با زمان و مسئول.

**22-4-Q1** — The configuration of both members and information about licenses and certificates.


### پاسخ‌های بازنویسی عمیق درس 22-5

**22-5-ت1** — Cluster، Failover، Split-brain، Upgrade، Evidence.

**22-5-ت2** — قطعی شدید و Session/آدرس تکراری در تولید.

**22-5-ت3** — ping پیوسته؛ lost×interval.

**22-5-ت4** — Failover بی‌دلیل یا نبود Failover هنگام خرابی لینک.

**22-5-ت5** — HB قطع؛ دو Primary؛ ریست یک عضو؛ HB Redundant.

**22-5-ت6** — HB اضافی، Alert، Pre-check.

**22-5-Q1** — By using redundant, preferably back-to-back, heartbeat links.

### پاسخ‌های درس افزوده‌ی 22-0 (فصل 22)

**22-0-ت1** — Active-Passive: یک دستگاه ترافیک می‌برد؛ Active-Active: بار Inspection بین اعضا پخش می‌شود؛ a-p ساده‌تر.

**22-0-ت2** — قطع Heartbeat با دو دستگاه زنده که هر دو Primary می‌شوند.

**22-0-ت3** — Failback خودکار نمی‌شود؛ عضو فعلی Primary می‌ماند.

**22-0-ت4** — تا خرابی یک لینک باعث Split-brain نشود.

**22-0-ت5** — Session Pickup خاموش است؛ فعال‌کردن آن (TCP) و بررسی محدودیت UDP/ICMP.

**22-0-ت6** — HA از خرابی دستگاه، SD-WAN از خرابی/افت کیفیت ISP؛ هر دو لازم‌اند؛ Heartbeat جدا و Health-check مستقل.

**22-0-م1** — بررسی هم‌خوانی Config بین اعضا.

**22-0-Q1** — Loss of heartbeat between members that are both still running, so each assumes the primary role.

# فصل 23 — Multi-Firewall و Asymmetric Routing (معماری ۵)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۰، ۱۵، ۲۲.
**اهداف:** چند فایروال پشت‌سرهم/موازی؛ Asymmetric Routing و اثر آن بر Stateful؛ `asymroute`؛ Policy Routing؛ عیب‌یابی با Sniffer.
**اشتباهات رایج:** فعال‌کردن asymroute بدون درک؛ نادیده‌گرفتن Session؛ Route دوطرفه ناهمسان.

**درس‌های فصل:**
- [درس 23-1 — چرا Asymmetric برای Stateful مشکل است](#l-23-1)
- [درس 23-2 — رفع Asymmetric: Policy Routing و Source NAT](#l-23-2)
- [درس 23-3 — چند فایروال سری و موازی](#l-23-3)
- [درس 23-4 — مانیتورینگ Session و آزمون معماری ۵](#l-23-4)

---

<a id="l-23-1"></a>

## درس 23-0 — Asymmetric Routing در Stateful Firewall: تحلیل بسته‌به‌بسته، RPF و راه‌حل‌ها

**فصل ۲۳ · درس افزوده (پیش‌درس ۲۳-۱) · پیش‌نیاز: ۱۰-۶، ۱۰-۹، ۱۲-۰، ۱۱-۷ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** رفتار RPF و Session از مستند Packet Flow؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. تعریف دقیق **Asymmetric Routing** و علت‌های پیدایش آن (ISP دوگانه، ECMP، دو فایروال).
2. توضیح بسته‌به‌بسته‌ی علت Drop در فایروال Stateful (نبود Session، RPF، TCP out-of-window).
3. نشانه‌ها در Log و Debug؛ تفکیک از مشکل Policy.
4. راه‌حل‌ها و ریسک هرکدام: طراحی متقارن، Policy Route، SNAT، Session Sync، `asymroute` (بی‌ریسک نیست).
5. طراحی چندفایروال با مسیر متقارن.

### ۲) مفهوم پایه

در مسیر نامتقارن، **رفت** از فایروال A و **برگشت** از فایروال B می‌گذرد. A فقط SYN را دیده؛ B فقط SYN/ACK را. هیچ‌کدام Handshake کامل را ندیده‌اند؛ فایروال Stateful برگشتی را که Session ندارد رد می‌کند.

### ۳) توضیح عمیق فنی

#### ۳-۱) علت‌ها

- **Dual-ISP/ECMP:** مسیر رفت و برگشت بر اساس Hash/BGP متفاوت.
- **دو فایروال موازی** بدون Sync.
- **VPN + Internet:** رفت از Tunnel، برگشت از Internet.
- **Policy Routing/SD-WAN** در یک سر.
- **Route خراب:** Route برگشت به Interface دیگر.

#### ۳-۲) بسته‌به‌بسته

``` text
Client -> FW-A (SYN)            : session created on A
Server -> FW-B (SYN/ACK)        : B has no session -> DROP (or RPF fail)
Client never gets SYN/ACK       : retransmit SYN, timeout
```

دو شکل Drop:

1. **RPF (Reverse Path Check) fail:** بسته‌ی برگشتی از Interfaceای وارد شد که بهترین مسیر به مبدأ آن نیست. Debug Flow: `reverse path check fail, drop`.
2. **No session / Denied policy:** بسته‌ی برگشتی مطابق Policy جدید ارزیابی می‌شود (چون Session نیست) و اگر Policy مجاز نداشته باشد Drop می‌شود؛ یا SYN/ACK بدون SYN را ماشین حالت TCP نمی‌پذیرد.

#### ۳-۳) راه‌حل‌ها

| راه‌حل | چگونه | مزیت | ریسک |
|---|---|---|---|
| طراحی متقارن | Route/Metric برای برگشت از همان مسیر | بهترین | نیاز طراحی |
| Policy Route/SNAT | برگشت را به همان فایروال بکشید | سریع | عیب‌یابی سخت‌تر، Log مبهم |
| Session Sync/HA | Session به فایروال دیگر کپی | حفظ Session | پیچیدگی/لایسنس |
| `asymroute`/غیرفعال‌سازی بررسی‌ها | بسته‌ی بدون Session را عبور می‌دهد | رفع Drop | **امنیت کم**؛ Inspection ناقص؛ فقط موقت |
| Hash متقارن/Anycast | Flow هر دو جهت یک مسیر | مقیاس | وابسته به تجهیزات |

> **اصل:** ابتدا طراحی متقارن؛ سپس Sync؛ آخرین راه غیرفعال‌کردن بررسی.

#### ۳-۴) تشخیص

``` text
diagnose debug flow filter addr <client>
diagnose debug flow trace start 20
diagnose sys session filter src <client>
diagnose sys session list
get router info routing-table details <client>
diagnose sniffer packet any "host <client> and port <p>" 4 20 l
```

سه شاهد: Sniffer SYN فقط در A؛ SYN/ACK فقط در B؛ `session list` فقط در A.

### ۴) مثال حل‌شده

**شرایط:** دو ISP روی یک فایروال، SD-WAN با Load-balance. کاربران گزارش می‌دهند «بعضی اتصال‌ها بعد از Failover قفل می‌شوند». شواهد: Sniffer روی WAN1: SYN؛ روی WAN2: SYN/ACK؛ `session list`: Session با NAT مربوط به WAN1. **تحلیل:** پس از Failover مسیر برگشت پیش از به‌روزشدن Session تغییر کرده؛ پاسخ از Interface دیگری می‌رسد و Session روی Interface قبلی ثبت شده است. **رفع:** Clear فیلترشده‌ی Sessionهای مرتبط (۱۳-۷) و تنظیم Health-check/Timeout (۲۱-۷). **درس:** قبل از نتیجه‌گیری، شواهد را از هر دو Interface و Session جمع کنید.

**مثال متوسط:** دو فایروال موازی با ECMP: Hash رفت و برگشت متفاوت. **رفع:** Hash متقارن یا Active-Passive.

**مثال سخت:** VPN دو‌طرفه: رفت از Tunnel، برگشت از Internet (Route خراب). Debug Flow سمت مقابل: «reverse path check fail». **رفع:** Route برگشت به Tunnel.

### ۵) GUI و CLI

**GUI:** Network → Static Routes/Policy Routes؛ Log & Report → Forward Traffic (Deny)؛ Dashboard → Sessions. **CLI:** مطابق ۳-۴؛ `config router policy`.

### ۶) نکات امنیتی

- غیرفعال‌کردن بررسی‌های RPF/State باعث عبور بسته‌های جعلی می‌شود.
- هر استثنا مستند با تاریخ بازبینی.

### ۷) جمع‌بندی مفهومی

- Asymmetric = رفت و برگشت از دو مسیر؛ Stateful نمی‌پذیرد.
- شواهد: Sniffer در هر دو سمت + Session.
- طراحی متقارن بهترین راه؛ `asymroute` آخرین.
- RPF و Policy دو علت متفاوت Drop‌اند.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) Asymmetric Routing چیست؟ *(پاسخ: 23-0-ت1)*

**ت2.** (ساده) چرا Stateful آن را رد می‌کند؟ *(پاسخ: 23-0-ت2)*

**ت3.** (متوسط) RPF fail چه نشانه‌ای در Debug دارد؟ *(پاسخ: 23-0-ت3)*

**ت4.** (سخت) سه راه‌حل را با ریسک مقایسه کنید. *(پاسخ: 23-0-ت4)*

**ت5.** (سخت، طراحی) دو فایروال موازی با ECMP را متقارن کنید. *(پاسخ: 23-0-ت5)*

**Q1.** Quick quiz (English): Which evidence proves asymmetric routing? *(پاسخ: 23-0-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding | بررسی مسیر معکوس |
| asymroute | Asymmetric routing allowance | اجازه‌ی مسیر نامتقارن |
| SNAT | Source NAT | تغییر مبدأ |

- *Prefer a symmetric design over disabling stateful checks.* ← طراحی متقارن را به غیرفعال‌کردن بررسی‌ها ترجیح دهید.

### ۱۰) منابع

- Fortinet Docs: [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow)؛ FortiOS 7.0 Administration Guide — Asymmetric routing.

## درس 23-1 — Asymmetric Routing برای Stateful: تعریف دقیق، علت‌ها، تحلیل بسته‌به‌بسته و تفکیک RPF از No-session

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰، ۱۰-۶، ۱۱-۷، ۱۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Asymmetric Routing را در توپولوژی‌های واقعی (Dual-ISP، ECMP، دو فایروال، VPN+Internet) تشخیص دهد.
2. رفتار فایروال Stateful را بسته‌به‌بسته توضیح دهد (SYN، SYN/ACK، ACK، داده).
3. دو مکانیزم Drop (RPF fail و No-session/Denied) را تفکیک کند.
4. با Sniffer دو‌نقطه‌ای و Debug Flow و Session ثابت کند.
5. اثر Asymmetric روی NAT، UTM و Log را بگوید.
6. درباره‌ی «نامتقارن مجاز» (Stateless/IPS bypass) قضاوت کند.

### ۲) مفهوم پایه: چیست و چرا؟

در شبکه‌ی ساده یک بسته از A به B می‌رود و پاسخ همان مسیر را برمی‌گردد. در شبکه‌ی واقعی با دو ISP، ECMP، دو فایروال یا ترکیب VPN و اینترنت، رفت و برگشت می‌توانند از دو مسیر مختلف بروند. روتر معمولی اهمیتی نمی‌دهد؛ **فایروال Stateful** می‌دهد، چون تصمیمش بر پایه‌ی Session است و Session فقط روی دستگاهی که اولین بسته را دیده ساخته شده است.

### ۳) توضیح عمیق فنی

#### ۱) علت‌های پیدایش

| الگو | چرا Asymmetric می‌شود |
|---|---|
| Dual-ISP | رفت ISP1 (SNAT IP1)، سرور پاسخ به IP1؛ ولی در SD-WAN/ECMP ممکن است برگشت از مسیر دیگر |
| ECMP دو فایروال | Hash رفت و برگشت متفاوت |
| VPN + Internet | رفت از Tunnel، برگشت از اینترنت (Route برگشت اشتباه) |
| PBR/SD-WAN یک‌طرفه | Policy فقط یک جهت |
| Failover وسط Session | Session روی لینک قدیمی |

#### ۲) تحلیل بسته‌به‌بسته

``` text
Client -> FW-A : SYN              A: new session (SYN_SENT) -> forwards
Server -> FW-B : SYN/ACK          B: no session for this tuple
   case 1: B routing says best path to client is via another interface -> RPF check fails -> drop
   case 2: B accepts by routing but policy lookup for a "new" SYN/ACK -> no policy -> drop (policy 0)
   case 3: B has permissive policy: creates a new session from SYN/ACK -> TCP state machine rejects ACK without SYN
Client retransmits SYN, timeout.
```

#### ۳) دو مکانیزم Drop

| مکانیزم | نشانه‌ی Debug | علت | رفع |
|---|---|---|---|
| RPF (Reverse Path Check) | `reverse path check fail, drop` | بهترین مسیر به مبدأ از Interface ورودی نمی‌گذرد | Route برگشت/Policy Route |
| No-session / Policy | `Denied by forward policy check (policy 0)` یا بدون Session | فایروال دوم Session ندارد | متقارن‌سازی/Sync |

#### ۴) اثر ثانویه

- **NAT:** SNAT روی فایروال اول؛ پاسخ به فایروال دوم می‌رسد که ترجمه را نمی‌شناسد.
- **UTM/IPS:** بازرسی فقط یک جهت را می‌بیند؛ Signatureها ناقص؛ AV/Proxy شکست.
- **Log:** نیمی از Sessionها در هر فایروال؛ تحلیل حادثه ناقص.

#### ۵) نامتقارن عمدی

بعضی طراحی‌ها (ECMP/Anycast) عمداً نامتقارن‌اند؛ آن‌جا فایروال‌ها باید Session Sync داشته باشند یا بررسی Stateful را سبک کنند (ریسک امنیتی). تصمیم آگاهانه، نه پیش‌فرض.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Asymmetric مجاز؟ | فقط با Sync/تصمیم آگاهانه |
| متقارن‌سازی | Route/Metric، Hash، Policy Route |
| Log | هر دو فایروال مرکزی |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** دو ISP: SYN از wan1 خارج و SYN/ACK از wan2 برمی‌گردد. Sniffer: wan1 SYN؛ wan2 SYN/ACK؛ `session list` فقط یک Session با wan1. نتیجه: Asymmetric؛ Drop به‌علت RPF.

**متوسط (تحلیل):** دو فایروال موازی با ECMP: بعضی Flowها سالم، بعضی نه. علت: Hash رفت و برگشت متفاوت؛ برای Flowهایی که Hash یکسان است سالم. آزمون: ۲۰ اتصال و شمارش Success/Fail ≈ ۵۰٪. رفع: Hash متقارن/Active-Passive.

**سخت (تحلیل چندعلتی):** VPN IPsec به‌علاوه‌ی Internet: سرور از دفتر مقابل به IP شما از طریق اینترنت پاسخ می‌دهد چون Route مقصد (IP Tunnel) در سرور نیست. فایروال شما پاسخ را روی Interface wan می‌گیرد؛ RPF: بهترین مسیر به مبدأ (آدرس شبکه‌ی مقابل) Tunnel است ⇒ Drop. دو علت هم‌زمان: Route سرور و Selector. تفکیک: Capture Hop‌به‌Hop؛ Debug Flow: `reverse path check fail`. رفع: Route سرور به Tunnel + بررسی Selector.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sniffer packet any "host 10.1.4.10 and port 443" 4 20 l
diagnose sys session filter src 10.1.4.10
diagnose sys session list
diagnose debug flow filter addr 10.1.4.10
diagnose debug flow trace start 20
diagnose debug enable
diagnose debug disable
diagnose debug reset
get router info routing-table details 10.1.4.10
```

### ۸) Verification (اثبات صحت)

- Sniffer در دو Interface/دو فایروال: محل SYN و SYN/ACK.
- `session list` فقط یک فایروال.
- Debug Flow: پیام RPF/Policy 0.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| SYN بدون ACK | Sniffer | Asymmetric |
| RPF fail | Debug Flow | Route برگشت |
| فقط بعضی Flowها | شمارش | Hash/ECMP |
| VPN+Internet | Routing table | Route برگشت/Selector |

### ۱۰) نکات امنیتی

- غیرفعال‌کردن RPF/State باعث عبور بسته‌ی جعلی می‌شود.
- Asymmetric مجاز باید ثبت و بازبینی شود.

### ۱۱) جمع‌بندی مفهومی

- Asymmetric = رفت/برگشت از دو مسیر.
- Stateful بدون Session Drop می‌کند.
- دو مکانیزم: RPF و No-session.
- NAT/UTM/Log هم آسیب می‌بینند.
- اثبات با Capture دو‌نقطه‌ای.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا روتر معمولی Asymmetric را تحمل می‌کند ولی فایروال Stateful نه؟ *(پاسخ: 23-1-ت1)*

**ت2.** (ساده) دو نشانه‌ی Drop در Debug Flow را نام ببرید. *(پاسخ: 23-1-ت2)*

**ت3.** (متوسط) ECMP دو فایروال: ۵۰٪ Flowها شکست می‌خورند؛ توضیح و رفع. *(پاسخ: 23-1-ت3)*

**ت4.** (متوسط) چرا SNAT بدون Session برگشتی را خراب می‌کند؟ *(پاسخ: 23-1-ت4)*

**ت5.** (سخت) VPN+Internet نامتقارن: دو علت و روش تفکیک. *(پاسخ: 23-1-ت5)*

**ت6.** (سخت، طراحی) چه موقع Asymmetric را می‌پذیریم؟ *(پاسخ: 23-1-ت6)*

**Q1.** Quick quiz (English): What two firewall behaviors commonly cause drops under asymmetric routing? *(پاسخ: 23-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding check | بررسی مسیر معکوس |
| Session sync | Session synchronization | همگام‌سازی Session |
| Anycast | Anycast routing | مسیریابی چندمقصدی |

- *Capture at both firewalls to prove asymmetry.* ← برای اثبات Asymmetric در هر دو فایروال Capture بگیرید.

### ۱۴) کارت Lab

**کارت Lab:** تشخیص Asymmetric. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/asym.md`.

### ۱۵) منابع

- [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow)
- RFC 3704 (Ingress filtering/RPF)

<a id="l-23-2"></a>

## درس 23-2 — رفع Asymmetric: طراحی متقارن، Policy Route، SNAT، Session Sync و ریسک هر راه‌حل

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰، ۲۳-۱، ۱۰-۴، ۲۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. راه‌حل‌ها را با ریسک/هزینه مقایسه و برای سناریو انتخاب کند.
2. Policy Route و SNAT را پیاده و آزمون کند.
3. Hash متقارن/Active-Passive/Session Sync را توضیح دهد.
4. اثر هر راه‌حل را روی Log/Inspection/Troubleshooting بسنجد.
5. پیکربندی را با آزمون‌های مثبت/منفی اثبات کند.

### ۲) مفهوم پایه: چیست و چرا؟

بعد از تشخیص Asymmetric باید راه‌حل را انتخاب کرد. اشتباه رایج: سریع‌ترین راه‌حل (`asymroute`/غیرفعال‌کردن چک‌ها) که امنیت را می‌خرد. ترتیب درست: ۱) طراحی متقارن، ۲) Sync یا Active-Passive، ۳) Policy Route/SNAT، ۴) استثنا با ریسک مستند.

### ۳) توضیح عمیق فنی

#### ۱) مقایسه

| راه‌حل | چگونه | مزیت | ریسک/هزینه |
|---|---|---|---|
| متقارن‌سازی Route | Metric/Distance/BGP برای برگشت | ریشه‌ای | نیاز طراحی؛ کنترل روی Upstream |
| Policy Route | مسیر مبتنی بر مبدأ/Interface | سریع | پیچیدگی؛ عیب‌یابی |
| SNAT به IP یکتا | برگشت به همان فایروال | ساده | Log مبهم؛ Double NAT |
| Session Sync/HA | Session کپی | حفظ Session | لایسنس/پیچیدگی؛ بار |
| Hash متقارن | رفت/برگشت یک مسیر | مقیاس | وابسته به تجهیزات |
| `asymroute` | عبور بدون State | رفع Drop | امنیت کم |

#### ۲) Policy Route

``` text
config router policy
    edit 10
        set input-device "port2"
        set src "10.1.4.0/24"
        set dst "0.0.0.0/0"
        set output-device "wan1"
        set gateway 198.51.100.1
    next
end
```

اصل: Policy Route قبل از Routing Table ارزیابی می‌شود (۱۲-۰)؛ برای ترافیک برگشتی باید Interface ورودی و Source را طوری تعریف کنید که برگشت از همان مسیر برود.

#### ۳) SNAT برای متقارن‌سازی

SNAT خروجی با IP همان لینک باعث می‌شود Upstream پاسخ را به همان لینک بفرستد. در Dual-ISP: IP Pool هر WAN؛ در SD-WAN برای Sessionهای Failover Clear.

#### ۴) Session Sync

در HA A-P، Session به Secondary کپی می‌شود؛ در Active-Active/Cluster ممکن است Session را به همتا بدهند تا Asymmetric تحمل شود (محدودیت و لایسنس `Unverified`).

#### ۵) فهرست بررسی انتخاب

1. آیا می‌شود Route را متقارن کرد؟ (بله ⇒ همین.)
2. اگر نه، آیا Session Sync دارید؟
3. اگر نه، Policy Route/SNAT با مستندسازی.
4. `asymroute` فقط موقت.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترتیب انتخاب | متقارن→Sync→PBR/SNAT→asymroute |
| Log | مبهم نشود؛ NAT مستند |
| Sync | لایسنس/پهنا |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Policy Route برای 10.1.4.0/24 از wan1؛ پس از آن SYN/ACK به همان فایروال/Interface برمی‌گردد؛ آزمون: Sniffer و session list.

**متوسط (تحلیل):** SNAT به IP Pool هر WAN: Dual-ISP؛ تحلیل: Session خروجی wan2 با IP ISP2 SNAT می‌شود و پاسخ به ISP2؛ مشکل: IP ثابت بانک؛ تصمیم: Pool/BGP یا پذیرش Re-login.

**سخت (طراحی):** دو فایروال Active-Active پشت ECMP با ۴۰۰۰ Flow/s؛ نیاز: بدون Drop و با Inspection کامل. تحلیل: Session Sync پهنای HB بالا؛ Hash متقارن بهتر؛ تصمیم: Switch/Router با Hash متقارن (Symmetric hash) روی سمت Upstream/Downstream یا Active-Passive. معیار: Throughput، Complexity، SPOF. اگر Hash متقارن ممکن نیست: Active-Passive.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Policy Routes → Create New.
2. Policy & Objects → IP Pools / NAT در Policy.
3. System → HA (Session pickup).
4. Log & Report → Forward Traffic.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config router policy
    edit 10
        set input-device "port2"
        set src "10.1.4.0/24"
        set output-device "wan1"
        set gateway 198.51.100.1
    next
end
config firewall ippool
    edit "POOL-WAN1"
        set type overload
        set startip 198.51.100.10
        set endip 198.51.100.10
    next
end
diagnose sys session filter src 10.1.4.10
diagnose sys session list
```

### ۸) Verification (اثبات صحت)

- آزمون ۲۰ اتصال: همه موفق.
- Sniffer: رفت/برگشت روی یک مسیر.
- Log: Session کامل در یک فایروال.
- آزمون منفی: Flow نامعتبر Drop.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| هنوز Drop | Sniffer | Policy Route/Match |
| Log مبهم | Log | SNAT مستند |
| بعضی Flowها | شمارش | Hash |

### ۱۰) نکات امنیتی

- ثبت هر استثنا.
- Policy Route را مستند و بازبینی کنید.

### ۱۱) جمع‌بندی مفهومی

- ترتیب انتخاب: متقارن اول.
- Policy Route/SNAT سریع ولی بدهی.
- Sync هزینه دارد.
- `asymroute` موقت.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Policy Route چه کاری می‌کند؟ *(پاسخ: 23-2-ت1)*

**ت2.** (ساده) چرا SNAT برگشت را به همان فایروال می‌کشد؟ *(پاسخ: 23-2-ت2)*

**ت3.** (متوسط) ترتیب انتخاب راه‌حل‌ها را با دلیل بنویسید. *(پاسخ: 23-2-ت3)*

**ت4.** (متوسط) SNAT چه اثر منفی روی Log دارد؟ *(پاسخ: 23-2-ت4)*

**ت5.** (سخت) دو فایروال Active-Active با ECMP؛ طرح را انتخاب کنید و دلیل بیاورید. *(پاسخ: 23-2-ت5)*

**ت6.** (سخت، طراحی) آزمون پذیرش پس از رفع Asymmetric. *(پاسخ: 23-2-ت6)*

**Q1.** Quick quiz (English): Why should symmetric routing be preferred over disabling stateful checks? *(پاسخ: 23-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PBR | Policy-based routing | مسیر مبتنی بر Policy |
| IP Pool | NAT IP pool | مخزن آدرس NAT |
| Symmetric hash | Symmetric hashing | Hash متقارن |

- *Prefer symmetric design over workarounds.* ← طراحی متقارن را به راه‌حل‌های موقت ترجیح دهید.

### ۱۴) کارت Lab

**کارت Lab:** رفع. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/asym-fix.md`.

### ۱۵) منابع

- Fortinet Docs: Policy routes، IP pools (7.0)
- RFC 2992 (ECMP analysis)

<a id="l-23-3"></a>

## درس 23-3 — چند فایروال سری و موازی: الگوها، NAT، Session، Failure Domain و مانیتورینگ

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰، ۱۵-۰، ۲۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. الگوهای سری، موازی Active-Passive، Active-Active و N+1 را مقایسه کند.
2. NAT، Session و Policy را در هر الگو تحلیل کند.
3. Failure Domain و Blast Radius را بسنجد.
4. مانیتورینگ و عیب‌یابی چندفایروالی (Log مرکزی، Correlation) را طراحی کند.
5. Change Management بین چند فایروال (یکنواختی Policy) را بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

با رشد شبکه، «یک فایروال» به چند فایروال تبدیل می‌شود: لبه + داخلی، موازی برای ظرفیت، یا چند سایت. هر الگو مزیت و مشکلی دارد؛ اگر نفهمید، Asymmetric، Double NAT و Policy ناهمگون می‌سازید.

### ۳) توضیح عمیق فنی

#### ۱) الگوها

| الگو | هدف | الزام | ریسک |
|---|---|---|---|
| سری (Edge+Internal) | Defense in Depth | NAT فقط لبه؛ Policy هماهنگ | عیب‌یابی دو لایه |
| موازی A-P | افزونگی | HA/Sync | ظرفیت ۱× |
| موازی A-A | ظرفیت+افزونگی | Hash متقارن/Sync | پیچیدگی |
| N+1 / Pool | مقیاس | Load balancer/ECMP متقارن | Session |
| چندسایت | DR | Routing/Failover سایتی | Split-brain سایتی |

#### ۲) Failure Domain

اگر یک Policy اشتباه روی فایروال لبه بخورد: اثرش؟ (Blast radius). سری: دو لایه، لایه‌ی دوم هنوز محافظ است؛ موازی: اشتباه Sync شده روی هر دو (HA هم همین را کپی می‌کند). برای کاهش: Change مرحله‌ای (Canary)، آزمون Policy در Lab، Rollback.

#### ۳) NAT و Session

- NAT فقط در یک نقطه.
- Session Table هر فایروال را مستقل پایش کنید.
- در Active-Active مطمئن شوید هر Flow هر دو جهت یک فایروال می‌بیند.

#### ۴) مانیتورینگ

Log مرکزی (Syslog reliable) با NTP؛ Correlation بر پایه‌ی Session ID/5-tuple/Policy ID؛ داشبورد: CPU/Session/Interface هر فایروال؛ Alert بر Drift (Policy متفاوت بین جفت).

``` text
Policy drift check: diff(config firewall policy FW1, FW2) after each change window
```

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| الگو | نیاز ظرفیت/افزونگی/دفاع |
| Canary | تغییر روی یک فایروال ابتدا |
| Drift | Diff دوره‌ای |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** سری: Edge Policy WAN→DMZ و Internal Policy DMZ→SRV؛ آزمون: درخواست از اینترنت تا DB؛ Log در هر دو.

**متوسط (تحلیل):** Double NAT: Log سرور همه‌ی مبدأ‌ها 10.20.0.1. رفع: NAT فقط Edge؛ Internal Routing؛ تأیید Log.

**سخت (Failure domain):** تغییر Policy اشتباه روی هر دو فایروال موازی Sync شد و Block کامل. تحلیل: HA/Sync علت کپی خطا؛ پیشگیری: Change Canary (ابتدا یک فایروال در Window)، Backup و Rollback آماده، آزمون مثبت/منفی پس از Push.

### ۸) Verification (اثبات صحت)

- Log هر دو فایروال برای یک Flow.
- Diff Policy بدون Drift.
- Failover آزمایشی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Drop تصادفی | Session | Asymmetric |
| Log مبهم | Log | Double NAT |
| Drift | Diff | Sync/Change |

### ۱۰) نکات امنیتی

- Policy مشابه روی همه‌ی فایروال‌ها؛ Change هماهنگ.

### ۱۱) جمع‌بندی مفهومی

- الگو بر پایه‌ی نیاز.
- NAT یک‌بار.
- Failure domain و Canary.
- Log مرکزی + Drift.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا NAT فقط روی یک فایروال؟ *(پاسخ: 23-3-ت1)*

**ت2.** (ساده) Blast radius چیست؟ *(پاسخ: 23-3-ت2)*

**ت3.** (متوسط) تفاوت Canary و تغییر هم‌زمان؟ *(پاسخ: 23-3-ت3)*

**ت4.** (متوسط) Drift Policy را چگونه کشف می‌کنید؟ *(پاسخ: 23-3-ت4)*

**ت5.** (سخت) Active-Active: ۴ الزام برای عملکرد صحیح. *(پاسخ: 23-3-ت5)*

**ت6.** (سخت، طراحی) الگوی مناسب برای ظرفیت ۳۰ Gbps با Defense in Depth. *(پاسخ: 23-3-ت6)*

**Q1.** Quick quiz (English): What is the main benefit of a canary change on multi-firewall designs? *(پاسخ: 23-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Canary | Canary change | تغییر آزمایشی روی بخش کوچک |
| Blast radius | Blast radius | دامنه‌ی اثر |
| Drift | Configuration drift | انحراف پیکربندی |

- *Test changes on one firewall before rolling out.* ← تغییرات را ابتدا روی یک فایروال آزمایش کنید.

### ۱۴) کارت Lab

**کارت Lab:** سری/موازی. **Evidence:** `02-design/multi-fw.md`.

### ۱۵) منابع

- NIST SP 800-41
- Google SRE Book (Canarying)

<a id="l-23-4"></a>

## درس 23-4 — آزمون معماری ۵: چندفایروالی و Asymmetric — صورت مسئله، کلید پاسخ و Rubric

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰ تا ۲۳-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. توپولوژی دو‌فایروالی با مسیر نامتقارن را بسازد و Drop را بازتولید کند.
2. با Sniffer/Debug Flow/Session علت را اثبات کند.
3. دو راه‌حل (Policy Route و متقارن‌سازی) را پیاده و مقایسه کند.
4. RCA و Evidence را تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟

آزمون عملی با تمرکز بر شواهد؛ کلید پاسخ پس از تلاش.

### ۳) توضیح عمیق فنی

#### صورت مسئله

دو فایروال FW-A و FW-B با دو ISP؛ کلاینت 10.1.4.10 و سرور 203.0.113.80. مسیر برگشت به‌صورت عمدی نامتقارن (Route Upstream).

1. بازتولید: اتصال TCP 443 ناموفق.
2. اثبات علت: Sniffer دو فایروال، `session list`، Debug Flow.
3. رفع: ابتدا Policy Route؛ سپس طراحی متقارن (Route برگشت).
4. آزمون: ۲۰ اتصال موفق؛ آزمون منفی RPF.
5. گزارش: RCA و Evidence Index.

#### کلید پاسخ (خلاصه)

- Sniffer: A دارد SYN، B دارد SYN/ACK؛ session فقط در A.
- Debug Flow B: reverse path check fail.
- رفع ۱: Policy Route/SNAT؛ ریسک: Log مبهم.
- رفع ۲ (ترجیحی): Route برگشت متقارن.
- نتیجه: ۲۰/۲۰؛ آزمون منفی: بسته‌ی جعلی با Source نامعتبر Drop.

#### Rubric

بازتولید ۱۵؛ اثبات علت ۳۰؛ رفع و آزمون ۳۰؛ RCA/Evidence ۱۵؛ صداقت ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** بازتولید Drop.

**متوسط:** اثبات با سه شاهد.

**سخت:** دو راه‌حل و مقایسه.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose sniffer packet any "host 203.0.113.80 and port 443" 4 20 l
diagnose sys session list
diagnose debug flow filter addr 203.0.113.80
diagnose debug flow trace start 20
```

### ۸) Verification (اثبات صحت)

- Evidence Index A5؛ ۲۰ اتصال؛ آزمون منفی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| اثبات ناقص | Sniffer یک‌طرفه | دو نقطه |
| رفع ناپایدار | Session | Clear/Hash |

### ۱۰) نکات امنیتی

- آزمون فقط Lab.

### ۱۱) جمع‌بندی مفهومی

- آزمون: بازتولید، اثبات، رفع، RCA.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) سه شاهد اثبات Asymmetric؟ *(پاسخ: 23-4-ت1)*

**ت2.** (ساده) چرا آزمون منفی RPF لازم است؟ *(پاسخ: 23-4-ت2)*

**ت3.** (متوسط) مقایسه‌ی Policy Route و Route متقارن. *(پاسخ: 23-4-ت3)*

**ت4.** (متوسط) چرا ۲۰ اتصال و نه ۱؟ *(پاسخ: 23-4-ت4)*

**ت5.** (سخت) RCA را بنویسید. *(پاسخ: 23-4-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی پیشگیری از تکرار. *(پاسخ: 23-4-ت6)*

**Q1.** Quick quiz (English): Which command output proves that only one firewall owns the session? *(پاسخ: 23-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| A5 | Architecture 5 | معماری ۵ |

- *Verify the fix with captures and a session list.* ← رفع را با Capture و session list تأیید کنید.

### ۱۴) کارت Lab

**کارت Lab:** A5. **Evidence:** `03-ops/a5.md`.

### ۱۵) منابع

- درس‌های ۲۳-۱ تا ۲۳-۳

## پاسخ‌های فصل 23

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 23-1

**23-1-ت1** — روتر فقط بر پایه‌ی مقصد هر بسته تصمیم می‌گیرد؛ فایروال Stateful تصمیم را به Session وابسته می‌کند که فقط روی دستگاه اول ساخته شده.

**23-1-ت2** — `reverse path check fail, drop` و `Denied by forward policy check (policy 0)`.

**23-1-ت3** — Hash رفت و برگشت متفاوت؛ نیمی از Flowها هر دو جهت را از یک فایروال می‌بینند و نیمی نه. رفع: Hash متقارن (هر دو جهت یکسان)، یا Active-Passive، یا Session Sync.

**23-1-ت4** — ترجمه‌ی مبدأ فقط در Session فایروال اول ثبت شده؛ فایروال دوم نمی‌تواند پاسخ را به آدرس واقعی ترجمه کند.

**23-1-ت5** — Route سرور مقابل (پاسخ از اینترنت) و Selector/Route فایروال؛ Capture Hop‌به‌Hop و Debug Flow RPF؛ رفع Route سرور سپس بررسی Selector.

**23-1-ت6** — وقتی Session Sync/بررسی سبک مدیریت‌شده است (مثلاً Anycast)، ریسک امنیتی پذیرفته‌شده و مستند، و Inspection جای دیگر جبران می‌شود.

**23-1-Q1** — Reverse path check failure and the absence of a matching session or policy for the return packet.


### پاسخ‌های بازنویسی عمیق درس 23-2

**23-2-ت1** — مسیر را بر اساس مبدأ/Interface ورودی/سرویس تعیین می‌کند، قبل از Routing Table.

**23-2-ت2** — چون آدرس مبدأ ترجمه‌شده متعلق به همان لینک است و Upstream پاسخ را به همان مسیر می‌دهد.

**23-2-ت3** — متقارن‌سازی (ریشه‌ای)، Session Sync/Active-Passive، Policy Route/SNAT، `asymroute` (آخرین).

**23-2-ت4** — آدرس واقعی مبدأ در سرور پنهان می‌شود و تحلیل حادثه سخت‌تر می‌شود.

**23-2-ت5** — Hash متقارن یا Active-Passive؛ Session Sync پرهزینه؛ معیار: Throughput، سادگی، SPOF.

**23-2-ت6** — ۲۰ اتصال موفق، Sniffer یک‌مسیره، session list در یک فایروال، Log کامل، آزمون منفی RPF.

**23-2-Q1** — Because disabling checks weakens security, while symmetric routing solves the root cause.


### پاسخ‌های بازنویسی عمیق درس 23-3

**23-3-ت1** — Log و عیب‌یابی ساده می‌ماند و آدرس واقعی حفظ می‌شود.

**23-3-ت2** — دامنه‌ی اثر یک خطا/خرابی.

**23-3-ت3** — Canary ابتدا روی یک دستگاه؛ اگر سالم بود ادامه؛ تغییر هم‌زمان خطا را همه‌جا ایجاد می‌کند.

**23-3-ت4** — Diff پیکربندی دو فایروال پس از هر تغییر و به‌صورت دوره‌ای؛ Alert.

**23-3-ت5** — Hash/Routing متقارن یا Sync، Policy یکسان، Log مرکزی/زمان، Failover آزمایش‌شده.

**23-3-ت6** — سری (Edge+Internal)، هر لایه A-P؛ Edge برای ظرفیت N+1 با ECMP متقارن اگر لازم؛ معیارها: ریسک، هزینه، عملیات.

**23-3-Q1** — It limits the blast radius by testing the change on one device before applying it everywhere.


### پاسخ‌های بازنویسی عمیق درس 23-4

**23-4-ت1** — Sniffer دو فایروال (SYN در یکی/SYN-ACK در دیگری)، session list فقط در یکی، Debug Flow RPF/Policy 0.

**23-4-ت2** — تا نشان دهد بررسی ضدجعل هنوز فعال است و رفع آن را خنثی نکرده.

**23-4-ت3** — Policy Route سریع ولی بدهی (Log، پیچیدگی)؛ Route متقارن ریشه‌ای و ترجیحی.

**23-4-ت4** — تا Hash/تصادفی بودن Asymmetric دیده شود؛ نتیجه‌ی ۲۰/۲۰ اطمینان می‌دهد.

**23-4-ت5** — علامت: TCP 443 ناموفق؛ شواهد: Sniffer/session/Debug؛ علت: Route برگشت Upstream به ISP2؛ رفع: Route/Policy Route؛ پیشگیری: چک‌لیست Route برگشت.

**23-4-ت6** — طراحی Route متقارن، Test Matrix دوره‌ای، Alert بر RPF Drop، Change Canary.

**23-4-Q1** — The session list shows the session only on the firewall that saw the first packet.

### پاسخ‌های درس افزوده‌ی 23-0 (فصل 23)

**23-0-ت1** — رفت و برگشت یک ارتباط از دو مسیر/دستگاه متفاوت.

**23-0-ت2** — چون برگشتی بدون Session مطابق Handshake نیست (و/یا RPF fail) و رد می‌شود.

**23-0-ت3** — پیام reverse path check fail, drop.

**23-0-ت4** — طراحی متقارن (کم‌ریسک)، Policy Route/SNAT (سریع ولی Log مبهم)، Session Sync/HA (حفظ Session ولی پیچیده)، asymroute (امنیت کم).

**23-0-ت5** — Hash متقارن یا Active-Passive، یا Policy Route برای برگشت از همان فایروال، یا Session Sync.

**23-0-Q1** — Sniffer shows SYN on one firewall and SYN/ACK on another, and the session exists only on the first.

# فصل 24 — معماری Data Center و Segmentation (G9)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۵، ۲۲، ۲۳.
**اهداف:** Segmentation Data Center؛ VRF/VDOM (مفهومی)؛ East-West در برابر North-South؛ Micro-segmentation؛ معماری ۷. Gate G9: سه Zone Data Center با Policy حداقلی و تست Isolation.
**نسخه:** VDOM در VM ممکن است محدود به لایسنس باشد (`Needs-License`، `Unverified`).
**اشتباهات رایج:** Policy any-any داخلی؛ ناهمسانی VLAN؛ فراموشی Logging.

**درس‌های فصل:**
- [درس 24-1 — East-West و Segmentation](#l-24-1)
- [درس 24-2 — Policy حداقلی Web/App/DB](#l-24-2)
- [درس 24-3 — VDOM و VRF (مفهومی)](#l-24-3)
- [درس 24-4 — Logging و Gate G9](#l-24-4)

---

<a id="l-24-1"></a>

## درس 24-0 — معماری VDOM: Multi-tenant، Inter-VDOM Link، منابع و جداسازی مدیریتی

**فصل ۲۴ · درس افزوده (پیش‌درس ۲۴-۱) · پیش‌نیاز: ۱۲-۰، ۱۳-۷، ۱۰-۸ · ≈ ۸ ساعت**

> **وضعیت (FortiOS 7.0.x):** مفاهیم Inter-VDOM و منابع از مستند رسمی 7.0 ([Inter-VDOM routing](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/335646/inter-vdom-routing)، [Global and per-VDOM resources](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/538256/global-and-per-vdom-resources)) بررسی شد. **Needs-License/محدودیت:** تعداد VDOM مجاز وابسته به مدل/لایسنس است؛ روی FortiGate-VM Lab `Unverified`. Lab «اجرا نشده».

### ۱) هدف آموزشی

1. VDOM را تعریف و با Zone و VRF مقایسه کند.
2. **حالت‌ها** (No VDOM، Split-Task، Multi VDOM) و نقش **Management VDOM** را بگوید.
3. **Inter-VDOM Link** را طراحی و Routing/Policy بین VDOMها را بنویسد.
4. **منابع (Global و Per-VDOM)** را کنترل و اثر آن را بگوید.
5. **جداسازی مدیریتی (Administrative Separation)** و Multi-tenant را طراحی کند.
6. محدودیت‌ها (Offload، لایسنس، پیچیدگی) را بشناسد.

### ۲) پیش‌نیازها

Packet Flow (۱۲-۰)، VRF و Leak (۱۰-۸)، Zone/Policy.

### ۳) مفهوم پایه

**VDOM (Virtual Domain)** یک فایروال مجازی مستقل درون یک دستگاه فیزیکی است: Interface، Routing Table، Policy، Object، VPN و Admin مخصوص خود. کاربرد: Multi-tenant (چند مشتری)، جداسازی کامل واحدها، فایروال‌های متعدد با هزینه‌ی کمتر. تفاوت با **Zone**: Zoneها در یک Routing Table و یک مجموعه‌ی Policy هستند؛ VDOM Routing Table و Policy جدا دارد و **ترافیک بین VDOMها فقط از طریق Link عبور می‌کند**.

### ۴) توضیح عمیق فنی

#### ۴-۱) حالت‌ها

- **No VDOM (پیش‌فرض):** یک VDOM به نام `root`.
- **Split-Task VDOM:** یک VDOM مدیریتی جدا از VDOM ترافیکی (در برخی مدل‌ها).
- **Multi VDOM:** چند VDOM؛ یک Global برای تنظیمات سراسری (System، Admin Profile، Log، Firmware)، و هر VDOM تنظیمات خودش.

#### ۴-۲) Inter-VDOM Link

طبق مستند، **VDOM Link** یک جفت Interface مجازی است که دو VDOM را بدون پورت فیزیکی اضافی وصل می‌کند؛ نوع پیش‌فرض ppp و برای IPv6 link-local/OSPFv3 باید `ethernet` شود؛ **VDOM Link از Traffic Offload پشتیبانی نمی‌کند** و برای Offload گزینه‌ی NPU-VDOM-LINK هست (مدل‌های دارای NPU). مثال مستند: یک Link برای هر VDOM بخش به VDOM root (مدیریتی). **Policy باید در هر VDOM جدا تعریف شود** و Route/Object هم.

#### ۴-۳) منابع

طبق مستند: در Split-Task/Multi VDOM می‌توان **Global Resources** و **Per-VDOM Resources** تنظیم کرد؛ اگر تغییر ندهید، محدودیت Per-VDOM **نامحدود** است و یک VDOM می‌تواند همه‌ی منابع دستگاه (Session، Policy، ...) را بخورد؛ Fortinet توصیه می‌کند برای منابع حیاتی سقف بگذارید (GUI: System → Global Resources و System → VDOM → Override Maximum/Guaranteed). این جدا‌سازی منابع شرط Multi-tenant ایمن است.

#### ۴-۴) جداسازی مدیریتی

Admin Profile و Admin به VDOM محدود می‌شوند؛ مدیر مشتری A نباید Config مشتری B را ببیند. Super Admin فقط Global. این بخش از اصل Least Privilege است (۱۱-۰).

#### ۴-۵) VDOM در برابر Zone و VRF

| | Zone | VRF (Cisco) | VDOM |
|---|---|---|---|
| Routing Table | مشترک | جدا | جدا |
| Policy/Object | مشترک | — | جدا |
| Admin جدا | نه | نه | بله |
| منابع جدا | نه | — | بله |
| هزینه/پیچیدگی | کم | متوسط | بالا |

#### ۴-۶) الگوی Management VDOM و Transit

مرکز: VDOM `root` (اینترنت، Management). هر مشتری: VDOM جدا + Inter-VDOM Link به root. NAT/اینترنت در root. Policy در هر VDOM فقط ترافیک خود را می‌سنجد؛ ترافیک بین مشتری‌ها **فقط از root** و با Policy.

### ۵) مثال حل‌شده

``` text
config system global
    set vdom-mode multi-vdom
end
config vdom
    edit CUST-A
    next
    edit CUST-B
    next
end
config global
    config system vdom-link
        edit "A-ROOT"
            set type ethernet
        next
    end
end
config global
    config system interface
        edit "A-ROOT0"
            set vdom "CUST-A"
        next
        edit "A-ROOT1"
            set vdom "root"
        next
    end
end
```

(سینتکس `vdom-link`/`vdom-mode`/نام Interface Link با CLI Reference 7.0 تطبیق شود؛ `Unverified`. فعال‌سازی Multi VDOM در Lab با Backup قبلی.)

**GUI:** System → Settings → Virtual Domains (Enable Multi VDOM)؛ System → VDOM → Create New؛ Network → Interfaces → Create New → VDOM Link؛ Global → System → Global Resources؛ System → Administrators → Admin Profile/VDOM.

**مثال متوسط (Resource Limit):** CUST-B سیل Session می‌فرستد و جدول Session کل دستگاه پر می‌شود. با Per-VDOM Maximum Sessions برای CUST-B، فقط CUST-B متأثر می‌شود.

**مثال سخت (طراحی):** سه مشتری، هر یک Subnet 10.0.0.0/24 هم‌پوشان. VDOM جدا (Routing جدا) اجازه‌ی Overlap می‌دهد؛ NAT در root برای اینترنت. بین مشتری‌ها ارتباط ممنوع؛ سرویس مشترک DNS از root با Policy و NAT مناسب. بحث امنیتی: Leak مستقیم بین VDOMها وجود ندارد مگر Link/Policy.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| VDOM یا Zone؟ | VDOM وقتی Admin/Routing/Policy جدا و Multi-tenant لازم است؛ Zone برای تقسیم داخلی ساده |
| تعداد VDOM | مطابق لایسنس/مدل؛ ساده نگه دارید |
| منابع | سقف برای منابع حیاتی |
| Offload | VDOM Link معمولاً Offload ندارد؛ Throughput را بسنجید |
| مدیریت | Admin و Profile محدود به VDOM |

### ۷) Troubleshooting

| علامت | علت |
|---|---|
| بین VDOMها ping نمی‌رود | Link/Route/Policy یکی از VDOMها |
| Policy اثر ندارد | در VDOM اشتباه نوشته شده |
| CPU بالا با VDOM Link | بدون Offload |
| یک VDOM همه‌ی منابع را می‌خورد | Limit تنظیم نشده |

### ۸) نکات امنیتی

- VDOM جداسازی نرم‌افزاری است؛ دارای آسیب‌پذیری Global مشترک می‌ماند.
- Admin Profile Super Admin را محدود نگه دارید.
- Logging جدا و ارسال Log هر VDOM.

### ۹) جمع‌بندی مفهومی

- VDOM = فایروال مجازی با Routing/Policy/Admin/منابع جدا.
- ارتباط بین VDOMها فقط از Inter-VDOM Link.
- منابع Per-VDOM پیش‌فرض نامحدودند؛ سقف بگذارید.
- VDOM Link Offload ندارد (مستند 7.0).
- تعداد مجاز VDOM وابسته به مدل/لایسنس است.

### ۱۰) تمرین و ارزیابی

**ت1.** (ساده) VDOM چیست؟ *(پاسخ: 24-0-ت1)*

**ت2.** (ساده) Inter-VDOM Link برای چیست؟ *(پاسخ: 24-0-ت2)*

**ت3.** (متوسط) چرا Per-VDOM Resource Limit لازم است؟ *(پاسخ: 24-0-ت3)*

**ت4.** (متوسط) تفاوت VDOM و Zone؟ *(پاسخ: 24-0-ت4)*

**ت5.** (سخت) طراحی دو مشتری با Subnet هم‌پوشان و اینترنت مشترک. *(پاسخ: 24-0-ت5)*

**ت6.** (سخت، طراحی) جداسازی مدیریتی برای ۳ نقش (Super Admin، Admin مشتری، Auditor) بنویسید. *(پاسخ: 24-0-ت6)*

**Q1.** Quick quiz (English): Why can an unlimited per-VDOM resource setting be dangerous? *(پاسخ: 24-0-Q1)*

### ۱۱) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VDOM | Virtual Domain | فایروال مجازی |
| root | root VDOM | VDOM پیش‌فرض/مدیریتی |
| Multi-tenant | Multi-tenancy | چندمستأجری |
| Global | Global VDOM | تنظیمات سراسری |

- *VDOM links connect virtual domains without physical ports.* ← VDOM Link بدون پورت فیزیکی VDOMها را وصل می‌کند.
- *Set per-VDOM resource limits to prevent one tenant from exhausting the device.* ← سقف منابع بگذارید تا یک مشتری دستگاه را اشباع نکند.

### ۱۲) منابع

- Fortinet Docs: [Inter-VDOM routing](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/335646/inter-vdom-routing)، [Global and per-VDOM resources](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/538256/global-and-per-vdom-resources).

## درس 24-1 — East-West و Segmentation: طراحی Zone، Trust Level، Flow Discovery و Policy Matrix

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰، ۲۴-۰، ۱۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ HA/VDOM Needs-License؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. East-West را تحلیل و Zoneها/Trust Levelها را طراحی کند.
2. Flow Discovery (Inventory جریان‌ها) را با Log/Learning انجام دهد.
3. Policy Matrix داده‌محور بنویسد.
4. Micro-segmentation را مفهومی بشناسد.
5. Logging/Detection East-West را طراحی کند.

### ۲) مفهوم پایه: چیست و چرا؟

بعد از نفوذ اولیه، مهاجم از طریق East-West حرکت می‌کند. Segmentation بدون «شناخت جریان‌ها» قطع سرویس می‌سازد؛ پس باید ابتدا جریان‌ها را کشف کرد.

### ۳) توضیح عمیق فنی

#### ۱) مراحل

1. Inventory: سرویس‌ها، پورت‌ها، وابستگی‌ها.
2. Flow Discovery: Policy موقت Allow+Log (Learning) و جمع‌آوری ۲–۴ هفته.
3. گروه‌بندی بر اساس نقش/حساسیت.
4. Matrix حداقلی + Deny+Log.
5. Cutover مرحله‌ای (Monitor→Enforce).
6. بازبینی Hit Count.

#### ۲) Trust Level

Management > DB > App > Web > Users > Guest؛ جهت ممنوع/مجاز و Inspection.

#### ۳) Matrix نمونه

``` text
WEB -> APP : 8080   APP -> DB : 1433   MGMT -> all : SSH/HTTPS (jump)
WEB -> DB : none    USERS -> DB : none BACKUP -> DB : 1433 (restricted source/time)
```

#### ۴) Micro-segmentation

کنترل در سطح میزبان/VM (فایروال میزبان/SDN) برای Flowهای داخل یک Zone؛ فراتر از این Lab ولی هدف نهایی.

#### ۵) Detection

Deny بین Zoneهای داخلی، Scan داخلی، Flowهای جدید، حجم غیرعادی.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Learning | قبل از Enforce |
| Zone | نقش/حساسیت |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Zoneهای WEB/APP/DB و Matrix.

**متوسط (تحلیل):** Backup Server به همه دسترسی داشت: محدودسازی منبع/زمان؛ Zone جدا.

**سخت (Learning):** Enforce روزِ اول باعث قطع ERP شد؛ Flow کشف‌نشده (Batch شبانه). راه: Learning ۴ هفته (شامل پایان ماه)، سپس Enforce مرحله‌ای.

### ۸) Verification (اثبات صحت)

- Matrix + آزمون منفی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| سرویس قطع | Log Deny | Flow ناشناخته |

### ۱۰) نکات امنیتی

- Least Privilege.

### ۱۱) جمع‌بندی مفهومی

- Inventory→Learning→Matrix→Enforce.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) East-West؟ *(پاسخ: 24-1-ت1)*

**ت2.** (ساده) چرا Learning؟ *(پاسخ: 24-1-ت2)*

**ت3.** (متوسط) چرا Backup محدود؟ *(پاسخ: 24-1-ت3)*

**ت4.** (متوسط) چرا Learning شامل پایان ماه؟ *(پاسخ: 24-1-ت4)*

**ت5.** (سخت) Enforce باعث قطع شد؛ تحلیل. *(پاسخ: 24-1-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Segmentation. *(پاسخ: 24-1-ت6)*

**Q1.** Quick quiz (English): Why use a learning phase before enforcing segmentation? *(پاسخ: 24-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Micro-segmentation | Micro-segmentation | تقسیم ریز |
| Hit count | Hit count | تعداد Match |

- *Learn flows before blocking.* ← قبل از Block جریان‌ها را بشناسید.

### ۱۴) کارت Lab

**کارت Lab:** Zone. **Evidence:** `02-design/dc-zones.md`.

### ۱۵) منابع

- NIST SP 800-41
- MITRE ATT&CK Lateral Movement

<a id="l-24-2"></a>

## درس 24-2 — Policy حداقلی Web/App/DB: ماتریس، پیاده‌سازی و آزمون Isolation

**فصل ۲۴ · بازنویسی عمیق · پیش‌نیاز: ۱۱-۰، ۲۴-۱، ۱۲-۰ · ≈ ۶ ساعت**

> **وضعیت (7.0.3):** سینتکس `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

سه لایه‌ی Web/App/DB را با Zone و Policy حداقلی پیاده‌سازی و **Isolation** را با آزمون منفی (nmap) اثبات کند.

### ۲) ماتریس Policy

``` text
Users -> WEB : TCP 443              accept + UTM + log
WEB   -> APP : TCP 8080             accept + log
APP   -> DB  : TCP 1433             accept + log
WEB   -> DB  : none                 deny + log
Users -> DB  : none                 deny + log
DB    -> any : only updates (opt)   restricted
any   -> any : implicit deny + log
```

### ۳) پیاده‌سازی

**GUI:** Network → Interfaces → Zone (ZN-WEB، ZN-APP، ZN-DB)؛ Policy & Objects → Addresses/Services (TCP-8080، TCP-1433)؛ Firewall Policy برای هر ردیف؛ Log همه.

**CLI (`Unverified`):**

``` text
config system zone
    edit "ZN-WEB"
        set interface "vlan10"
    next
    edit "ZN-APP"
        set interface "vlan20"
    next
    edit "ZN-DB"
        set interface "vlan30"
    next
end
config firewall service custom
    edit "TCP-8080"
        set tcp-portrange 8080
    next
    edit "TCP-1433"
        set tcp-portrange 1433
    next
end
config firewall policy
    edit 30
        set name "WEB-to-APP"
        set srcintf "ZN-WEB"
        set dstintf "ZN-APP"
        set srcaddr "WEB-SRV"
        set dstaddr "APP-SRV"
        set action accept
        set schedule "always"
        set service "TCP-8080"
        set logtraffic all
    next
    edit 31
        set name "APP-to-DB"
        set srcintf "ZN-APP"
        set dstintf "ZN-DB"
        set srcaddr "APP-SRV"
        set dstaddr "DB-SRV"
        set action accept
        set schedule "always"
        set service "TCP-1433"
        set logtraffic all
    next
end
```

### ۴) آزمون Isolation (مثبت/منفی)

``` text
# positive
from WEB: nc -zv APP-SRV 8080     -> open
from APP: nc -zv DB-SRV 1433      -> open
# negative
from WEB: nc -zv DB-SRV 1433      -> filtered/timeout
from WEB: nmap -Pn -p 1-1024 DB-SRV -> all filtered
from Users: nc -zv DB-SRV 1433    -> filtered
```

ثبت: Log Deny و Hit Count؛ هر آزمون منفی که «باز» شد = شکست طراحی.

### ۵) مثال‌ها

**ساده:** WEB→APP 8080 موفق؛ WEB→APP 22 رد.

**متوسط:** APP به DB نمی‌رسد: Debug Flow: Denied policy 0 چون Service Object اشتباه (UDP)؛ اصلاح.

**سخت:** پس از Compromise WEB، مهاجم Scan می‌کند: Log Deny WEB→DB و WEB→APP (پورت‌های دیگر) → Alert؛ Containment: Quarantine WEB (۲۹-۰).

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| سرویس کار نمی‌کند | Service/Zone اشتباه |
| دسترسی غیرمجاز | Policy گسترده یا Shadow |
| Log کم | logtraffic |

### ۷) نکات امنیتی

- Default Deny؛ هر Policy Source/Destination مشخص.
- بازبینی Hit Count و حذف Policy بی‌استفاده.

### ۸) جمع‌بندی

- Zone + Policy حداقلی + Log.
- Isolation را با آزمون منفی اثبات کنید.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) چرا WEB→DB ممنوع است؟ *(پاسخ: 24-2-ت1)*

**ت2.** (متوسط) آزمون منفی چیست؟ *(پاسخ: 24-2-ت2)*

**ت3.** (سخت) APP به DB نمی‌رسد؛ مراحل بررسی. *(پاسخ: 24-2-ت3)*

**Q1.** Quick quiz (English): Why must isolation be proven with a negative test? *(پاسخ: 24-2-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Tier | Application tier | لایه‌ی برنامه |
| Negative test | Negative test | آزمون ممنوعیت |
| Hit count | Policy hit count | تعداد Match |

- *Prove isolation with negative tests.* ← جداسازی را با آزمون منفی اثبات کنید.

### ۱۱) Lab

**کارت Lab:** Policy لایه‌ای. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/dc-policy.md`.

### ۱۲) منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Firewall policy، Zones؛ NIST SP 800-41.

<a id="l-24-3"></a>

## درس 24-3 — Lab عملی VDOM: ساخت، Inter-VDOM Link، Policy و محدودیت منابع

**فصل ۲۴ · بازنویسی عمیق · پیش‌نیاز: ۲۴-۰ (معماری)، ۱۲-۰ · ≈ ۶ ساعت**

> **وضعیت (7.0.3):** Needs-License/محدودیت VM (`Unverified`)؛ فعال‌سازی Multi VDOM **فقط پس از Backup و تأیید کاربر**؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

یک Lab دو-VDOM بسازد: فعال‌سازی Multi-VDOM، ساخت VDOM، Link، Route، Policy و Resource Limit؛ و جداسازی را آزمایش کند.

### ۲) طرح

``` text
root     : Internet, management, shared services
CUST-A   : 10.1.0.0/24 (port2)         link A-ROOT
CUST-B   : 10.1.0.0/24 (port3)         link B-ROOT   (overlapping on purpose)
NAT/Internet in root; no direct A<->B path
```

### ۳) مراحل

1. Backup. فعال‌سازی: System → Settings → Virtual Domains → Multi VDOM (CLI: `config system global; set vdom-mode multi-vdom`).
2. System → VDOM → Create New: CUST-A، CUST-B.
3. تخصیص Interface: port2→CUST-A، port3→CUST-B.
4. Inter-VDOM Link: Network → Interfaces → Create New → VDOM Link (A-ROOT، B-ROOT).
5. در هر VDOM: IP Link، Route Default به root، Policy LAN→Link.
6. در root: Route به Subnet هر مشتری، Policy Link→WAN با NAT (جدا برای هر Link).
7. System → Global Resources/VDOM: سقف Session برای CUST-B.

``` text
config global
    config system vdom-link
        edit "A-ROOT"
            set type ethernet
        next
    end
end
config vdom
    edit CUST-A
        config router static
            edit 1
                set gateway 172.31.1.1
                set device "A-ROOT0"
            next
        end
    next
end
```

(ساختار نمونه؛ نام Interface لینک (`A-ROOT0/A-ROOT1`) و سینتکس `Unverified`.)

### ۴) آزمون

- Client-A و Client-B با IP هم‌پوشان هر دو اینترنت دارند (NAT در root).
- Client-A به Client-B نمی‌رسد (آزمون منفی).
- CUST-B سیل Session می‌فرستد؛ فقط CUST-B محدود می‌شود (Resource Limit).
- `diagnose sys session list` در هر VDOM جدا (`config vdom; edit CUST-A`).

### ۵) مثال‌ها

**ساده:** Ping از Client-A به Internet موفق.

**متوسط:** Client-A به اینترنت می‌رود ولی B نه: Policy/Route در root برای Link B ناقص.

**سخت:** هر دو مشتری 10.1.0.0/24؛ در root Route برگشت ابهام دارد. **رفع:** Route به Link خاص هر Subnet از طریق Interface Link (نه فقط Subnet) یا NAT در VDOM مشتری قبل از ورود به root (Source NAT به IP یکتای Link).

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| Policy اثر ندارد | VDOM اشتباه |
| ping بین VDOM | Link/Route/Policy یک سمت |
| منابع بی‌حد | Limit تنظیم نشده |
| دستور CLI کار نمی‌کند | داخل `config vdom` نیست |

### ۷) نکات امنیتی

- Admin هر مشتری محدود به VDOM.
- Super Admin فقط Global.
- Log هر VDOM جدا.

### ۸) جمع‌بندی

- VDOM = Routing/Policy/Admin/منابع جدا.
- Link + Route + Policy هر دو سمت.
- Overlap با NAT/Route دقیق.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) برای ارتباط VDOMها چه لازم است؟ *(پاسخ: 24-3-ت1)*

**ت2.** (متوسط) چرا Overlap مشکل Route برگشت می‌سازد؟ *(پاسخ: 24-3-ت2)*

**ت3.** (سخت) آزمون جداسازی A و B را بنویسید. *(پاسخ: 24-3-ت3)*

**Q1.** Quick quiz (English): Where do CLI commands for a specific VDOM have to be run? *(پاسخ: 24-3-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VDOM link | Inter-VDOM link | اتصال VDOMها |
| Global | Global scope | تنظیمات سراسری |
| root | root VDOM | VDOM پیش‌فرض |

- *Run VDOM-specific commands inside the VDOM context.* ← دستورهای اختصاصی VDOM را در Context همان VDOM اجرا کنید.

### ۱۱) Lab

**کارت Lab:** VDOM. **وضعیت:** اجرا نشده (Needs-License؛ تأیید کاربر). **Evidence:** `03-ops/vdom-lab.md`.

### ۱۲) منابع

- Fortinet Docs: [Inter-VDOM routing](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/335646/inter-vdom-routing)، [Global and per-VDOM resources](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/538256/global-and-per-vdom-resources).

<a id="l-24-4"></a>

## درس 24-4 — Logging Data Center و Gate G9: اثبات Isolation، آزمون منفی، Alert و مستندسازی

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۰ تا ۲۴-۳، ۲۷-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ HA/VDOM Needs-License؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Logging East-West را طراحی کند.
2. G9 را اجرا کند و Isolation را با آزمون منفی ثابت کند.
3. Alert بر Deny غیرعادی را بسازد.
4. Evidence و RCA ارائه دهد.

### ۲) مفهوم پایه: چیست و چرا؟

اثبات Segmentation = آزمون منفی + Log + Alert.

### ۳) توضیح عمیق فنی

#### وظایف G9

1. سه Zone + Policy.
2. nmap منفی از هر Zone (فقط Lab).
3. Log Deny و Alert نمونه.
4. VDOM مفهومی/Lab (لایسنس).
5. Evidence.

#### کلید

- نتیجه‌ی nmap WEB→DB: filtered؛ APP→DB 1433 open.
- Log: Deny policyid=0 برای اسکن.
- Alert: >50 Deny از یک srcip به DB.

#### Rubric

Policy ۲۵؛ Isolation ۳۰؛ Log/Alert ۲۰؛ VDOM ۱۰؛ Evidence ۱۰؛ صداقت ۵.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Zoneها.

**متوسط:** nmap.

**سخت:** Policy باز و رفع.

### ۸) Verification (اثبات صحت)

- Evidence G9.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Isolation شکست | nmap | Policy |

### ۱۰) نکات امنیتی

- nmap فقط Lab.

### ۱۱) جمع‌بندی مفهومی

- آزمون منفی + Log.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) وظایف G9؟ *(پاسخ: 24-4-ت1)*

**ت2.** (ساده) آزمون منفی چیست؟ *(پاسخ: 24-4-ت2)*

**ت3.** (متوسط) Alert چه آستانه‌ای؟ *(پاسخ: 24-4-ت3)*

**ت4.** (متوسط) nmap WEB→DB باز بود؛ رفع. *(پاسخ: 24-4-ت4)*

**ت5.** (سخت) RCA Policy باز. *(پاسخ: 24-4-ت5)*

**ت6.** (سخت، طراحی) بازبینی ماهانه. *(پاسخ: 24-4-ت6)*

**Q1.** Quick quiz (English): How is isolation proven? *(پاسخ: 24-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| G9 | Gate 9 | دروازه ۹ |

- *Prove isolation with evidence.* ← جداسازی را با شاهد ثابت کنید.

### ۱۴) کارت Lab

**کارت Lab:** G9. **Evidence:** `03-ops/g9.md`.

### ۱۵) منابع

- درس‌های ۲۴-۰ تا ۲۴-۳

## پاسخ‌های فصل 24

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 24-1

**24-1-ت1** — ترافیک داخلی.

**24-1-ت2** — کشف Flowهای ناشناخته پیش از Block.

**24-1-ت3** — دسترسی گسترده ریسک حرکت جانبی.

**24-1-ت4** — Jobهای دوره‌ای دیده شوند.

**24-1-ت5** — Flow ناشناخته؛ Log Deny؛ افزودن Rule و Monitor.

**24-1-ت6** — Inventory، Learning، Matrix، Cutover، بازبینی.

**24-1-Q1** — To discover legitimate flows and avoid outages.

### پاسخ‌های بازنویسی درس 24-2

**24-2-ت1** — Web نباید مستقیم به DB برسد؛ فقط App مجاز است تا حرکت جانبی محدود شود.

**24-2-ت2** — آزمونی که باید شکست بخورد (مثل WEB→DB) تا جداسازی ثابت شود.

**24-2-ت3** — Debug Flow (Policy 0؟)، Service/Zone، Route، Log Deny، Hit Count.

**24-2-Q1** — Because only a failed forbidden connection proves the boundary actually blocks it.


### پاسخ‌های بازنویسی درس 24-3

**24-3-ت1** — Inter-VDOM Link، Route و Policy در هر دو VDOM.

**24-3-ت2** — Subnet یکسان در دو VDOM باعث ابهام Routeهای برگشت در root می‌شود؛ باید Route به Link/NAT یکتا.

**24-3-ت3** — Client-A به Client-B ping/nc باید رد شود؛ Log Deny؛ Session جدا در هر VDOM؛ Resource Limit فقط B را محدود کند.

**24-3-Q1** — Inside the config vdom / edit <name> context of that VDOM.


### پاسخ‌های بازنویسی عمیق درس 24-4

**24-4-ت1** — Zone/Policy، nmap، Log/Alert، VDOM، Evidence.

**24-4-ت2** — اتصالی که باید بلاک شود.

**24-4-ت3** — >50 Deny از یک srcip به DB در ۵ دقیقه.

**24-4-ت4** — Policy گسترده؛ محدودسازی.

**24-4-ت5** — Any-Any موقت؛ حذف و آزمون.

**24-4-ت6** — Hit Count.

**24-4-Q1** — By negative tests showing blocked connections plus deny logs.

### پاسخ‌های درس افزوده‌ی 24-0 (فصل 24)

**24-0-ت1** — فایروال مجازی مستقل با Routing/Policy/Admin/منابع جدا.

**24-0-ت2** — اتصال دو VDOM بدون پورت فیزیکی.

**24-0-ت3** — تا یک VDOM همه‌ی منابع (Session و ...) را نخورد.

**24-0-ت4** — Zone در یک Routing/Policy مشترک؛ VDOM جدا و با Link ارتباط.

**24-0-ت5** — دو VDOM با Routing جدا (Overlap مجاز)، NAT و اینترنت در root، بدون ارتباط مشتری‌ها، DNS مشترک با Policy.

**24-0-ت6** — Super Admin فقط Global؛ Admin مشتری محدود به VDOM خودش؛ Auditor فقط خواندنی.

**24-0-Q1** — Because one tenant could consume all sessions and resources and disrupt every other VDOM.

# پایان بخش ۸ (فصل‌های ۲۲ تا ۲۴)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- HA FGCP و Failover؛ Asymmetric Routing؛ Segmentation Data Center و Policy حداقلی.

## ۲) آزمون پایان سه فصل
**س1** — Active-Passive چیست؟

**س2** — Heartbeat؟

**س3** — Session Pickup؟

**س4** — چرا Override خاموش؟

**س5** — Asymmetric چرا Drop؟

**س6** — Policy Route؟

**س7** — Double NAT؟

**س8** — East-West؟

**س9** — Least privilege؟

**س10** — VDOM؟

**س11** — VRF؟

**س12** — G9؟


## ۳) پاسخ آزمون
- **س1:** یک دستگاه فعال.
- **س2:** لینک همگام‌سازی.
- **س3:** حفظ Session هنگام Failover.
- **س4:** جلوگیری از Flap.
- **س5:** نبود Session.
- **س6:** مسیر مبتنی بر مبدأ.
- **س7:** پرهیز.
- **س8:** ترافیک داخلی.
- **س9:** حداقل دسترسی.
- **س10:** فایروال مجازی؛ لایسنس.
- **س11:** Routing جدا.
- **س12:** سه Zone با Isolation.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| HA | L2 | آزمون فصل ۲۲ |
| Asymmetric | L3 | A5 |
| Segmentation | L3 | G9 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. Labها اجرا نشده. 2. HA/VDOM به لایسنس وابسته. 3. سینتکس Unverified.

## ۶) پیش‌نیازهای بخش بعد
Backup همه‌ی Gateها؛ آشنایی با FortiManager/Analyzer (لایسنس).

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*`

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۲۴ |
| آخرین درس تکمیل‌شده | ۲۴-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۲۵ |
| فایل تولیدشده | `course/Course_Part_08_Chapters_22-24.md` |
