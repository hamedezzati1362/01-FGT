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

> **یادداشت علمی v4.0 — فصل 22:** عمومی: SPOF، RTO/RPO. مختص محصول: FGCP. زمان‌ها و Election نیازمند تطبیق با مستند نسخه.
> فرض: A-P، Heartbeat جدا؛ Failover زمانی تضمین نیست.
> مرجع: Fortinet FGCP docs (در این بازنگری بازخوانی نشد).
> **وضعیت منبع v4.1:** صفحه‌های FGCP و FGSP در Administration Guide 7.0.0 یافت شد ولی بدنه‌ی آن‌ها قابل‌خواندن نبود؛ ترتیب Election، `ha-uptime-diff-margin`، Timerهای Heartbeat، دامنه‌ی `session-pickup` و سینتکس FGSP تأیید نشدند → از حافظه و `Unverified`.


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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Election و Failover با سناریو

دو FG: A priority 200، B priority 100، override غیرفعال. A ریبوت و برمی‌گردد ⇒ چون override خاموش، ترتیب Monitored Interface > Age > Priority؛ B (قدیمی‌تر) Primary می‌ماند؛ برای بازگشت A: `override enable` یا تغییر Age (محاسبه‌ی مستند).

``` text
get system ha status
diagnose sys ha history read
```

Heartbeat روی دو لینک (Redundant) و VLAN/Interface جدا. **پرسش‌های مصاحبه**
1. *Split-brain؟* دو Primary.
2. *Monitor Port؟* قطع ⇒ Failover.
3. *Session Pickup؟* حفظ TCP در Failover (Needs-License ندارد، قابلیت پایه).

### تکمیل عمیق: FGCP — چطور دو فایروال یکی می‌شوند؟

#### چرا باید یاد بگیریم؟

یک فایروال تکی یعنی یک نقطه‌ی شکست؛ اگر بسوزد، کل سازمان از اینترنت جدا می‌شود. HA (High Availability، یعنی «دسترس‌پذیری بالا») دو دستگاه را طوری به هم وصل می‌کند که اگر یکی بیفتد، دیگری بی‌وقفه کار را ادامه دهد. پروتکل FortiGate برای این کار FGCP (FortiGate Clustering Protocol) است.

#### توضیح ساده

دو دستگاه یک Cluster می‌سازند. یکی **Primary** (ترافیک را پردازش می‌کند) و دیگری **Secondary** (آماده‌باش). بین آنها یک یا چند لینک **Heartbeat** هست که مدام «من زنده‌ام» می‌گویند و Config و Session را همگام می‌کنند.

#### انتخاب Primary (Election)

طبق مستند Fortinet وقتی `override` غیرفعال است ترتیب مقایسه چنین است:

1. تعداد Monitored Interface سالم (بیشتر بهتر)
2. Age (مدت زمان بالا بودن؛ با Margin 300 ثانیه)
3. Priority (بالاتر بهتر؛ پیش‌فرض 128)
4. Serial Number (بزرگ‌تر)

وقتی `override` فعال باشد، Priority پیش از Age بررسی می‌شود.

#### مثال ساده

A با Priority 200 و B با 100. اگر هر دو هم‌زمان بوت شوند و Override خاموش باشد، به دلیل برابری Age (در Margin) Priority تعیین‌کننده است ⇒ A Primary. اگر A بعد از قطع برگردد و B حالا Primary است و override خاموش، B Primary می‌ماند (Age بیشتر).

#### مثال متوسط — Failover با Monitor

Port1 (WAN) در Monitor است. با قطع کابل WAN در Primary، تعداد Monitored سالم کمتر می‌شود ⇒ Secondary (با WAN سالم) Primary می‌شود.

``` text
get system ha status
diagnose sys ha history read
```

#### مثال سخت — Split-brain

اگر همه‌ی لینک‌های Heartbeat قطع شوند، هر دو دستگاه خود را Primary می‌پندارند (Split-brain) و IP/MAC تکراری ایجاد می‌شود. جلوگیری: دو Heartbeat Interface مستقل (کابل مستقیم/دو سوئیچ)، و Monitor.

#### همگام‌سازی

Config از Primary به Secondary کپی می‌شود؛ `Configuration Status: in-sync`. Session Pickup: Sessionهای TCP نیز همگام می‌شوند تا هنگام Failover قطع نشوند (قابلیت پایه؛ مستند نسخه را بخوانید).

#### Lab

دو FortiGate VM (لایسنس معتبر) را در HA قرار دهید؛ این Lab برای ما «اجرا نشده» است و Needs-License.

#### عیب‌یابی

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| out-of-sync | تغییر محلی | `execute ha synchronize start` |
| Failover بی‌دلیل | Heartbeat ناپایدار | لینک‌ها |
| Split-brain | همه‌ی HB قطع | چندلینک |

#### پرسش‌ها با پاسخ

**۱. ترتیب Election (override خاموش)؟** Monitor، Age، Priority، Serial.
**۲. Heartbeat چرا دو لینک؟** افزونگی.
**۳. Split-brain؟** دو Primary.

#### English Corner

- *The primary is elected by monitored interfaces, age, priority and serial number.*
- Q: What causes a split-brain and how can you prevent it?

## درس 22-1 — مفاهیم HA برای طراحی: SPOF، سطوح افزونگی، انتخاب مدل و تحلیل خرابی‌ها

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰، ۱۱-۷، ۵-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ HA/VDOM Needs-License؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. SPOF (Single Point of Failure) را در یک معماری پیدا کنید.
2. سطوح افزونگی (لینک، دستگاه، سایت) را تفکیک کنید.
3. RTO و RPO و اثر آن‌ها بر انتخاب HA را محاسبه کنید.
4. FGCP Active-Passive و Active-Active را از نظر طراحی مقایسه کنید.
5. جایگزین‌ها (VRRP، Standalone + Backup، Cloud Redundancy) را بشناسید.
6. هزینه‌ی افزونگی در برابر هزینه‌ی قطعی را ارزیابی کنید.

### چرا باید یاد بگیریم؟

اگر فروشگاه شما فقط یک صندوق دارد و آن خراب شود، فروش متوقف می‌شود. دو صندوق (Active-Passive) یعنی دومی منتظر است. ولی اگر هر دو به یک پریز وصل باشند، پریز SPOF است. HA فقط «دو دستگاه» نیست؛ یعنی حذف تمام نقاط تک‌خطایی از مسیر: برق، لینک، سوئیچ، ISP، فایروال. بسیاری از پروژه‌ها دو فایروال می‌خرند ولی هر دو را به یک سوئیچ می‌زنند؛ سوئیچ می‌شود SPOF و HA بی‌فایده.

### SPOF — جست‌وجو

``` text
Users -- [SW] -- [FGT-A] -- [SW] -- ISP1
                 [FGT-B]
```

SPOFهای ممکن: سوئیچ تک، کابل تک، منبع تغذیه‌ی تک، ISP تک، دیسک (لاگ)، لایسنس، آدمی که فقط او رمز را می‌داند.

### سطوح افزونگی

| سطح | روش |
|---|---|
| لینک | LAG/Redundant Interface، دو کابل |
| دستگاه | HA Cluster (FGCP) |
| ISP | Dual-ISP/SD-WAN |
| سایت | DR (سایت دوم)، DNS/GSLB |
| برق | دو منبع، دو مسیر UPS |

### RTO و RPO

- **RTO** (Recovery Time Objective): حداکثر زمان قطع قابل‌قبول.
- **RPO** (Recovery Point Objective): حداکثر داده/وضعیت از دست‌رفته‌ی قابل‌قبول.

برای فایروال: RPO یعنی Sessionها و پیکربندی؛ FGCP پیکربندی را Sync می‌کند و (با session-pickup) Session TCP را.

``` text
Availability = Uptime / (Uptime + Downtime)
99.9%  -> ~8.76 h downtime / year
99.99% -> ~52.6 min / year
```

``` text
Downtime/year (99.9%) = 365 x 24 x 0.001 = 8.76 h
Downtime/year (99.99%) = 365 x 24 x 0.0001 = 0.876 h = 52.6 min
```

### FGCP: Active-Passive در برابر Active-Active

| ویژگی | Active-Passive | Active-Active |
|---|---|---|
| ترافیک | Primary | هر دو (UTM توزیع) |
| سادگی | بالا | کمتر |
| ظرفیت | یک دستگاه | بیشتر (فقط بعضی ترافیک‌ها) |
| عیب‌یابی | ساده | پیچیده |
| پیشنهاد | بله (عمومی) | موارد خاص |

### جایگزین‌ها

| روش | توضیح | محدودیت |
|---|---|---|
| VRRP | Gateway مجازی بین دو FGT مستقل | بدون Sync Config/Session |
| Standalone + Backup + Cold Spare | ارزان | RTO ساعت‌ها |
| Cloud/ VM Redundancy | بسته به پلتفرم | معماری ابری |
| دو سایت (DR) | سایت دوم | RTO/RPO تعریف |

### هزینه در برابر قطعی

``` text
Cost of outage = revenue/hour x hours + SLA penalties + reputation
Cost of HA     = 2nd device + licenses + support + complexity
```

مثال: فروشگاه آنلاین 10M در ساعت؛ قطع ۴ ساعت ⇒ 40M؛ HA سالانه 8M ⇒ توجیه‌پذیر.

### مثال‌های حل‌شده

#### مثال ساده — پیدا کردن SPOF

دو FGT در HA ولی هر دو به یک سوئیچ ⇒ سوئیچ SPOF. راه: دو سوئیچ (Stack یا جدا) با اتصال متقاطع.

#### مثال متوسط — RTO

نیاز: RTO < 10 s برای Sessionها. FGCP Failover معمولاً چند ثانیه؛ با Session Pickup اتصال‌های TCP می‌مانند. قابل‌قبول. ولی اگر برنامه‌ی Voice حساس است، تماس ممکن است Glitch ثانیه‌ای داشته باشد.

#### مثال متوسط — VRRP یا FGCP

شعبه‌ی کوچک با دو FGT مستقل: VRRP ساده ولی Config دوباره باید دستی؛ FGCP Sync خودکار. تصمیم: FGCP (اگر دو دستگاه هم‌مدل).

#### مثال سخت — Availability

نیاز 99.99٪؛ فایروال HA 99.99٪ ولی ISP 99.5٪. کل سیستم محدود به ضعیف‌ترین حلقه: ISP تک ⇒ سایت 99.5٪. راه: دو ISP. محاسبه‌ی ترکیبی:

``` text
Serial availability  = A1 x A2 = 0.9999 x 0.995 = 0.99490
Parallel (2 ISPs)    = 1 - (1-0.995) x (1-0.995) = 0.999975
```

#### مثال سخت — HA و Config نادرست

Cluster سالم ولی Policy ناقص ⇒ HA هم همان ناقص را Sync می‌کند. HA خطاهای پیکربندی را حل نمی‌کند، تکثیر می‌کند.

### Lab هدایت‌شده (اجرا نشده)

1. معماری موجود را رسم و SPOF علامت بزنید.
2. RTO/RPO تعریف و روش انتخاب کنید.
3. هزینه‌ی HA در برابر قطعی را بنویسید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| HA بی‌فایده | SPOF دیگر | حذف |
| Failover کند | Timer | تنظیم |
| Config خراب Sync | تکثیر | Change Control |
| ISP تک | Availability پایین | Dual-ISP |

### نکات امنیتی

HA لینک Heartbeat را ایزوله و رمزگذاری‌شده نگه دارد؛ دسترسی مدیریتی جدا برای هر عضو؛ آزمون دوره‌ای.

### جمع‌بندی

HA یعنی حذف SPOFها؛ RTO/RPO و Availability با فرمول؛ FGCP Active-Passive پیش‌فرض عملی؛ VRRP و DR جایگزین؛ هزینه‌ی افزونگی را با هزینه‌ی قطعی بسنجید.

### تمرین و ارزیابی

**ت1.** (ساده) SPOF چیست؟ *(پاسخ: 22-1-ت1)*

**ت2.** (ساده) HA ISP را پوشش می‌دهد؟ *(پاسخ: 22-1-ت2)*

**ت3.** (متوسط) دستگاه 99.5٪ و جفت HA موازی؛ دسترس‌پذیری؟ *(پاسخ: 22-1-ت3)*

**ت4.** (متوسط) چرا حلقه‌ی ضعیف سقف را تعیین می‌کند؟ *(پاسخ: 22-1-ت4)*

**ت5.** (سخت) چهار خرابی خارج از HA. *(پاسخ: 22-1-ت5)*

**ت6.** (سخت، طراحی) ماتریس خرابی برای سایت مرکزی. *(پاسخ: 22-1-ت6)*

**Q1.** Quick quiz (English): Why does the weakest component limit overall availability in a serial chain? *(پاسخ: 22-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SPOF | Single point of failure | نقطه‌ی شکست واحد |
| MTBF | Mean time between failures | میانگین فاصله‌ی خرابی |
| DR | Disaster recovery | بازیابی از فاجعه |

- *HA is not a substitute for change control.* ← HA جایگزین کنترل تغییر نیست.

### کارت Lab

**کارت Lab:** نقشه HA. **Evidence:** `02-design/ha-map.md`.

### منابع

- [FGCP](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/62403/fgcp)
- NIST SP 800-34

<a id="l-22-2"></a>

## درس 22-2 — پیکربندی HA Active-Passive: برگه‌ی طراحی، GUI، CLI، Heartbeat، Monitor و Verification

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۰، ۲۲-۱، ۱۲-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. پیش‌نیازهای HA (هم‌مدل، هم‌نسخه، هم‌لایسنس، پورت‌ها، دیسک) را بررسی کنید.
2. برگه‌ی طراحی (Group، Mode، Priority، hbdev، monitor، session-pickup) را بنویسید.
3. HA را از GUI و CLI روی دو دستگاه پیکربندی کنید.
4. وضعیت Cluster و Sync را با دستورهای Verification تأیید کنید.
5. Management Interface اختصاصی (ha-mgmt) را تنظیم کنید.
6. خطاهای رایج ساخت Cluster را رفع کنید.

### چرا باید یاد بگیریم؟

ساختن Cluster مثل ازدواج دو دستگاه است: باید کاملاً هم‌خوان باشند (مدل، نسخه، لایسنس) و روی «قوانین زندگی مشترک» توافق کنند (Group، Password، Heartbeat). یک اختلاف کوچک (مثلاً نسخه‌ی FortiOS) و Cluster تشکیل نمی‌شود یا Sync نمی‌شود. چون HA روی دستگاه Production اعمال می‌شود، یک اشتباه می‌تواند اینترنت را قطع کند؛ پس برگه‌ی طراحی و ترتیب اجرا حیاتی است.

### پیش‌نیازها

| مورد | چرا |
|---|---|
| هم‌مدل و هم‌سخت‌افزار | Sync و Offload |
| هم‌نسخه و Build | رفتار و Sync |
| لایسنس FortiGuard هر دو | خدمات هر عضو |
| پورت‌های Heartbeat | حداقل ۲ لینک مستقیم |
| Interfaceهای یکسان | Monitor/Failover |
| زمان (NTP) | Log و Certificate |

### برگه‌ی طراحی

| پارامتر | FGT-A | FGT-B |
|---|---|---|
| group-name | FGT-HA | FGT-HA |
| mode | a-p | a-p |
| password | <SECRET> | <SECRET> |
| hbdev | port3 (100)، port4 (50) | port3 (100)، port4 (50) |
| priority | 200 | 100 |
| override | disable | disable |
| monitor | port1، port2 | port1، port2 |
| session-pickup | enable | enable |
| ha-mgmt | port8 | port8 |
| hostname | FGT-A | FGT-B |

### پیکربندی CLI (FGT-A)

``` text
config system ha
    set group-id 10
    set group-name "FGT-HA"
    set mode a-p
    set password <SECRET>
    set hbdev "port3" 100 "port4" 50
    set session-pickup enable
    set session-pickup-connectionless enable
    set priority 200
    set override disable
    set monitor "port1" "port2"
    set ha-mgmt-status enable
    config ha-mgmt-interfaces
        edit 1
            set interface "port8"
            set gateway 10.50.0.254
        next
    end
end
```

FGT-B: همان با `priority 100`. نکات:

1. `group-id` برای MAC مجازی (VMAC) استفاده می‌شود؛ دو Cluster در یک L2 باید Group-ID متفاوت داشته باشند.
2. `override disable`: عضو با Priority بالاتر پس از بازگشت به‌صورت خودکار Primary نمی‌شود (ثبات).
3. Hostname هر عضو باید جدا باشد (Sync نمی‌شود).

### ترتیب اجرا

1. Backup پیکربندی.
2. نسخه و لایسنس را بررسی کنید.
3. کابل Heartbeat را وصل کنید.
4. HA را روی FGT-A (که Config اصلی دارد) فعال کنید.
5. HA را روی FGT-B با همان پارامتر و Priority پایین‌تر فعال کنید؛ FGT-B Config خود را از A می‌گیرد.
6. Cluster Sync را تأیید کنید.

اجرا روی B قبل از A می‌تواند Config را بازنویسی کند؛ همیشه دستگاه حاوی Config درست Primary بماند.

### Verification

``` text
get system ha status
diagnose sys ha status
diagnose sys ha checksum cluster
diagnose sys ha history read
execute ha manage 1 admin
```

نمونه:

``` text
HA Health Status: OK
Mode: HA A-P
Primary : FGT-A, FG...A, HA cluster index = 0
Secondary: FGT-B, FG...B, HA cluster index = 1
```

`checksum cluster` باید در دو عضو برابر باشد (Config Sync).

### مثال‌های حل‌شده

#### مثال ساده — Cluster تشکیل شد

`get system ha status` ⇒ دو عضو؛ Primary=FGT-A. `diagnose sys ha checksum cluster` ⇒ checksum یکسان.

#### مثال متوسط — Out-of-sync

Checksum متفاوت. علت: Config دستی روی B (تنظیم ممنوع). راه: `execute ha synchronize start` یا از Primary تغییر دهید؛ هرگز روی Secondary تغییر ندهید (به‌جز ha-mgmt).

#### مثال متوسط — Monitor

`monitor port1 port2`: اگر لینک port1 در Primary Down شود، Failover. اگر Monitor نباشد، Failover فقط با خرابی کامل دستگاه.

#### مثال سخت — نسخه‌ی متفاوت

B نسخه‌ی 7.0.2 و A 7.0.3. Cluster اولیه ممکن است تشکیل شود ولی Sync مشکل دارد. رفع: ارتقای B به همان Build قبل از HA. توصیه: Upgrade روی هر دو قبل از Cluster.

#### مثال سخت — Heartbeat روی لینک مشترک

hbdev روی port1 (که ترافیک کاربر هم دارد). در ازدحام Heartbeat Loss ⇒ Failover اشتباه (Flapping). رفع: لینک اختصاصی و Redundant. نمونه‌ی هشدار: `HA heartbeat lost`.

### مسیر GUI (مستندی، Unverified)

1. System → HA را باز کنید.
2. Mode و Priority را تنظیم کنید.
3. Heartbeat و Monitor Interfaces را انتخاب کنید.
4. Apply و بررسی Cluster Members.

### Lab هدایت‌شده (اجرا نشده)

1. برگه‌ی طراحی را کامل کنید.
2. Cluster بسازید و Verify کنید.
3. Out-of-sync عمدی و رفع.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Cluster تشکیل نمی‌شود | Group/Password/Mode | هماهنگ |
| Out-of-sync | تغییر روی Secondary | Sync |
| Flapping | Heartbeat | لینک اختصاصی |
| B Config را بازنویسی | ترتیب | Primary درست |

### نکات امنیتی

Password HA قوی؛ لینک Heartbeat ایزوله؛ `ha-mgmt` فقط در Mgmt؛ Backup قبل از تغییر.

### جمع‌بندی

HA با پیش‌نیاز و برگه‌ی طراحی؛ A-P، hbdev دو لینک، monitor و session-pickup؛ ترتیب فعال‌سازی؛ تأیید با `get system ha status` و `checksum cluster`.

### تمرین و ارزیابی

**ت1.** (ساده) پیش‌نیازهای HA؟ *(پاسخ: 22-2-ت1)*

**ت2.** (ساده) چرا دو hbdev؟ *(پاسخ: 22-2-ت2)*

**ت3.** (متوسط) override disable چه می‌کند؟ *(پاسخ: 22-2-ت3)*

**ت4.** (متوسط) Out-of-sync یعنی؟ *(پاسخ: 22-2-ت4)*

**ت5.** (سخت) عضو دوم Join نمی‌شود. *(پاسخ: 22-2-ت5)*

**ت6.** (سخت، طراحی) برگه‌ی HA. *(پاسخ: 22-2-ت6)*

**Q1.** Quick quiz (English): Why should changes be made on the primary unit only? *(پاسخ: 22-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FGCP | FortiGate Clustering Protocol | پروتکل خوشه‌بندی |

- *Heartbeat links must be dedicated.* ← لینک‌های Heartbeat باید اختصاصی باشند.

### کارت Lab

**کارت Lab:** پیکربندی HA (اجرا نشده؛ Needs-License). **Evidence:** `03-ops/ha-config.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: HA (FGCP)
- FortiOS 7.0 HA guide

<a id="l-22-3"></a>

## درس 22-3 — آزمون Failover/Failback و Session Pickup: طراحی تست، اندازه‌گیری و تحلیل

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. برنامه‌ی تست Failover (Reboot، قطع لینک، قطع Monitor، قطع برق) را طراحی کنید.
2. زمان قطع را با Ping/Probe دقیق اندازه بگیرید.
3. Session Pickup را برای TCP، UDP و NAT آزمون و محدودیت‌ها را بدانید.
4. Failback کنترل‌شده را اجرا کنید.
5. Election را در حالت `override` با و بدون آن تحلیل کنید.
6. گزارش آزمون (Evidence) را بنویسید.

### چرا باید یاد بگیریم؟

HA آزمون‌نشده «امیدوارانه» است. ماشینی که هرگز چرخ یدکش را عوض نکرده‌اید، در جاده نمی‌دانید جک کجاست. آزمون Failover باید در Change Window با برنامه انجام شود و عدد (زمان قطع) داشته باشد، نه «به نظر خوب بود». همچنین Session Pickup همه‌چیز را نجات نمی‌دهد؛ باید دقیقاً بدانید چه چیزی حفظ می‌شود.

> **حدود اعتبار (v4.0) — Failover/Failback در HA:** زمان‌ها و رفتار Failover (چند ثانیه، حفظ Session، Failback خودکار یا نه) در این دوره **توصیف مدل‌اند نه تضمین**. به مدل سخت‌افزار، نسخه‌ی FortiOS، تعداد/نوع Session، UTM/Proxy، Offload، لینک Heartbeat، `override`، Monitor و رفتار برنامه بستگی دارند. ترتیب Election در این درس باید با مستند FGCP همان نسخه تطبیق داده شود (در این بازنگری منبع رسمی مستقل برای آن بازخوانی نشد → نیازمند بررسی). «Failover = ۴ ثانیه» را فقط به‌عنوان نمونه‌ی اندازه‌گیری فرضی بخوانید.

### الگوریتم Election

بدون `override`:

``` text
1 monitored interfaces up count   (more is better)
2 HA uptime (age)                 (greater is better; diff < margin ignored)
3 priority                        (higher is better)
4 serial number                   (higher wins)
```

با `override`:

``` text
1 monitored interfaces
2 priority
3 HA uptime
4 serial number
```

پیامد: با `override disable`، عضوی که تازه برگشته (Uptime کم) Primary نمی‌شود؛ عضو فعلی می‌ماند (Failback خودکار نیست). با `override enable` عضو با Priority بالا بلافاصله پس از Sync دوباره Primary می‌شود (ممکن است قطع دوباره بسازد).

### برنامه‌ی آزمون

| # | آزمون | انتظار |
|---|---|---|
| 1 | Reboot Primary | Failover < N ثانیه |
| 2 | قطع کابل port1 (Monitor) | Failover |
| 3 | قطع Heartbeat یک لینک | بدون Failover |
| 4 | قطع هر دو Heartbeat | Split-brain (آزمون کنترل‌شده، ۲۲-۵) |
| 5 | Failback | کنترل‌شده |
| 6 | Session Pickup | اتصال‌های TCP حفظ |

### اندازه‌گیری

``` text
ping -t 8.8.8.8   (from LAN)            -> loss window = outage
ssh to server + long command           -> TCP session survival
iperf3 -c SRV -t 120                   -> throughput interruption
```

``` text
Outage = (lost pings) x (ping interval)
Example: 4 lost x 1 s = 4 s
```

### Session Pickup

| ترافیک | حفظ می‌شود؟ |
|---|---|
| TCP (با session-pickup) | بله (عموماً) |
| UDP/ICMP | فقط با `session-pickup-connectionless enable` |
| NAT | بله (Session شامل NAT) |
| IPsec SA | تونل دوباره برقرار می‌شود (SA Sync بسته به مدل/نسخه) |
| UTM/Proxy Session | معمولاً حفظ نمی‌شود (Flow-based محدود) |
| Sessionهای Offload | بسته به مدل |

بدون Session Pickup: Sessionها قطع و کاربر دوباره اتصال می‌گیرد.

### Failback کنترل‌شده

``` text
execute ha failover set 1
```

(یا Priority عوض کنید) در پنجره‌ی کم‌ترافیک؛ اگر `override disable`، Failover دستی لازم است. ثبت زمان و Session.

### مثال‌های حل‌شده

#### مثال ساده — Reboot

`execute reboot` روی Primary. ping پایدار: ۳ بسته قطع (۳ ثانیه) ⇒ Failover ≈ ۳ ثانیه. `diagnose sys ha history read` دلیل: `HA state changed: ... reboot`.

#### مثال متوسط — Session Pickup

SSH به سرور و `ping` طولانی. Failover: SSH ادامه می‌یابد؛ `iperf3` چند ثانیه توقف و ادامه. نتیجه: Session TCP حفظ شد.

#### مثال متوسط — UDP

Voice روی UDP: بدون `session-pickup-connectionless` پس از Failover تماس قطع و دوباره برقرار می‌شود. با آن: بسته‌ها ادامه (با Glitch کوتاه).

#### مثال سخت — Override

`override enable` و Priority A=200: پس از reboot A و بازگشت، A فوراً Primary می‌شود ⇒ قطع دوم. رفع: `override disable` یا Failback در زمان برنامه‌ریزی‌شده.

#### مثال سخت — Monitor و Failover اشتباه

Monitor port2 (داخلی) در Primary Down (سوئیچ داخلی خراب). Failover به B ولی B هم به همان سوئیچ وصل است ⇒ خرابی ادامه. درس: Monitor باید معنی‌دار باشد و SPOF مشترک را در طراحی حذف کنید.

### Lab هدایت‌شده (اجرا نشده)

1. شش آزمون جدول را اجرا و زمان بگیرید.
2. Session Pickup TCP/UDP.
3. Failback کنترل‌شده.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Failover کند | Heartbeat Timer | تنظیم |
| Session قطع | pickup غیرفعال | enable |
| Failback ناخواسته | override | disable |
| Voice قطع | UDP | connectionless |

### نکات امنیتی

آزمون فقط در پنجره‌ی مجاز؛ Backup پیش از آزمون؛ Log HA مرکزی؛ آلارم Failover.

### جمع‌بندی

آزمون Failover با عدد؛ Election بدون/با override؛ Session Pickup (TCP، UDP، NAT) و محدودیت‌ها؛ Failback کنترل‌شده؛ Monitor معنی‌دار.

### تمرین و ارزیابی

**ت1.** (ساده) قطع چگونه محاسبه می‌شود؟ *(پاسخ: 22-3-ت1)*

**ت2.** (ساده) pickup؟ *(پاسخ: 22-3-ت2)*

**ت3.** (متوسط) کدام Sessionها ریست می‌شوند؟ *(پاسخ: 22-3-ت3)*

**ت4.** (متوسط) چرا Failback کنترل‌شده؟ *(پاسخ: 22-3-ت4)*

**ت5.** (سخت) Failover ۱۲ ثانیه؛ تحلیل. *(پاسخ: 22-3-ت5)*

**ت6.** (سخت، طراحی) ماتریس تست. *(پاسخ: 22-3-ت6)*

**Q1.** Quick quiz (English): How do you calculate the outage duration with a continuous ping? *(پاسخ: 22-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| HB | Heartbeat | ضربان |

- *Measure failover time, do not assume it.* ← زمان Failover را اندازه بگیرید، فرض نکنید.

### کارت Lab

**کارت Lab:** تست Failover (اجرا نشده). **Evidence:** `03-ops/ha-failover.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: HA failover

<a id="l-22-4"></a>

## درس 22-4 — عیب‌یابی HA و ارتقای Cluster: Out-of-sync، Flap، Split-brain، Upgrade Path و Rollback

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۲، ۲۲-۳، ۱۲-۶ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. علائم و علل Out-of-sync، Flapping، Split-brain و Join‌نشدن را بشناسید.
2. با `get system ha status`، `checksum`، `history` علت را پیدا کنید.
3. Split-brain را رفع و پیشگیری کنید.
4. Upgrade Cluster را با حداقل قطعی (Uninterruptible Upgrade) برنامه‌ریزی و Rollback را آزمون کنید.
5. دسترسی به عضو Secondary را بدانید (`execute ha manage`).
6. Runbook عیب‌یابی HA بنویسید.

### چرا باید یاد بگیریم؟

HA وقتی خراب شود معمولاً در بدترین زمان است: ساعت ۳ شب یا وسط حمله. دو دستگاه هر دو خود را «اصلی» می‌دانند (Split-brain)، Primary مدام عوض می‌شود، یا Config یکی نیست. اگر ابزار و ترتیب را از قبل ندانید، با تغییرات تصادفی وضع را بدتر می‌کنید. این درس Runbook آماده می‌دهد.

### علائم و علل

| علامت | علت | شاهد |
|---|---|---|
| Out-of-sync | تغییر مستقیم Secondary، Heartbeat ضعیف | checksum متفاوت |
| Flapping | override، Monitor ناپایدار، HB | `history read` |
| Split-brain | قطع همه‌ی Heartbeatها | دو Primary |
| عضو Join نمی‌شود | نسخه/Group/Password | status |
| لایسنس/UTM متفاوت | FortiGuard یک عضو | System > FortiGuard |

### ابزارها

``` text
get system ha status
diagnose sys ha status
diagnose sys ha checksum cluster
diagnose sys ha checksum show
diagnose sys ha history read
execute ha synchronize start
execute ha manage 1 admin
```

`ha manage` ورود به Secondary از Primary (CLI).

### Split-brain

وقتی هیچ Heartbeat بین دو عضو نمی‌رسد ولی هر دو زنده‌اند، هر دو Primary می‌شوند ⇒ MAC مجازی تکراری ⇒ قطعی و آشفتگی ARP.

پیشگیری:

1. حداقل دو Heartbeat مستقل (کابل مستقیم، پورت‌های متفاوت).
2. `ha-mgmt` برای دسترسی جدا.
3. Monitor Interface برای Failover منطقی.
4. در صورت نیاز لینک Heartbeat از طریق سوئیچ ایزوله با VLAN اختصاصی.

رفع:

1. تشخیص: هر دو عضو `HA state: primary`.
2. بازگرداندن Heartbeat.
3. Primary درست را حفظ و Secondary را Restart/Rejoin کنید؛ اگر Config متفاوت شده، بررسی کنید کدام Config درست است.
4. Backup و ثبت.

### Upgrade Cluster

``` text
# on primary
execute restore image tftp <file> <server>
# cluster upgrades secondary first, then fails over, then upgrades old primary
```

مراحل رسمی (Uninterruptible Upgrade، مستند FortiOS):

1. Backup همه‌ی Config.
2. بررسی مسیر Upgrade (Upgrade Path Tool).
3. آپلود Image روی Primary.
4. Secondary ارتقا و Reboot؛ Cluster Sync.
5. Failover به Secondary (جدید)؛ ارتقای Primary قدیمی.
6. بازگشت (اختیاری).
7. آزمون کامل.

Rollback: Image قبلی (Backup Partition) یا Restore Config.

### Runbook

``` text
1 get system ha status           (who is primary?)
2 diagnose sys ha history read   (why did it change?)
3 diagnose sys ha checksum cluster (config equal?)
4 check heartbeat links physical state
5 check monitor interfaces
6 sync / restart secondary if needed
7 record evidence + RCA
```

### مثال‌های حل‌شده

#### مثال ساده — Out-of-sync

Checksum متفاوت: `diagnose sys ha checksum show` بخش `firewall.policy` متفاوت است. کسی روی B تغییر داده. رفع: `execute ha synchronize start` از Primary و جلوگیری از ورود مستقیم به B.

#### مثال متوسط — Flapping

`history read` ⇒ هر ۲ دقیقه `monitor interface port2 failed`. لینک port2 ناپایدار (کابل). رفع کابل؛ اگر Monitor به SFP ناپایدار وابسته است، Hold-down.

#### مثال متوسط — Join نشد

B به Cluster نمی‌پیوندد. `get system ha status` ⇒ تنها یک عضو. بررسی: group-name متفاوت، یا Password، یا `group-id`. رفع و آزمون.

#### مثال سخت — Split-brain

هر دو Heartbeat روی یک سوئیچ بودند و سوئیچ ریبوت شد ⇒ هر دو Primary و IP تکراری. رفع: کابل Heartbeat مستقیم؛ طراحی اصلاح. RCA: SPOF مشترک.

#### مثال سخت — Upgrade ناموفق

Secondary پس از ارتقا Boot Loop. Rollback: Boot به Partition قبلی (`execute set-next-reboot primary/secondary`)، Restore Config، بررسی Upgrade Path (پرش نسخه‌ی غیرمجاز). درس: Lab/Staging قبل از Production، Console دسترسی.

### Lab هدایت‌شده (اجرا نشده)

1. Out-of-sync عمدی و Sync.
2. Flapping با کابل ناپایدار.
3. Upgrade با Rollback.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| دو Primary | Heartbeat | کابل/طراحی |
| checksum | تغییر Secondary | sync |
| Flap | Monitor/override | تنظیم |
| Boot Loop | Upgrade | Rollback |

### نکات امنیتی

Image از منبع رسمی و بررسی Hash؛ Backup رمزگذاری‌شده؛ Console ایمن؛ ثبت Change.

### جمع‌بندی

ابزارهای HA (status، checksum، history)؛ Split-brain با پیشگیری و رفع؛ Upgrade بدون قطع طولانی و Rollback؛ Runbook.

### تمرین و ارزیابی

**ت1.** (ساده) Split-brain چیست؟ *(پاسخ: 22-4-ت1)*

**ت2.** (ساده) ha history read؟ *(پاسخ: 22-4-ت2)*

**ت3.** (متوسط) Out-of-sync علت؟ *(پاسخ: 22-4-ت3)*

**ت4.** (متوسط) Upgrade ترتیب؟ *(پاسخ: 22-4-ت4)*

**ت5.** (سخت) Split-brain رفع. *(پاسخ: 22-4-ت5)*

**ت6.** (سخت، طراحی) برنامه Rollback. *(پاسخ: 22-4-ت6)*

**Q1.** Quick quiz (English): Which command shows the reason for a recent HA failover? *(پاسخ: 22-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Split-brain | Split brain | دو Primary |

- *Upgrade the secondary unit first.* ← ابتدا Secondary را ارتقا دهید.

### کارت Lab

**کارت Lab:** عیب‌یابی HA (اجرا نشده). **Evidence:** `03-ops/ha-troubleshoot.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: HA troubleshooting; Upgrade

<a id="l-22-5"></a>

## درس 22-5 — آزمون عملی HA: طراحی، Failover، Split-brain کنترل‌شده، Upgrade و RCA — کلید پاسخ و Rubric

**فصل 22 · بازنویسی عمیق · پیش‌نیاز: ۲۲-۱ تا ۲۲-۴ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Cluster Active-Passive FGCP را با پارامتر درست طراحی و Verify کنید.
2. Failover و Failback را اندازه‌گیری و Session Pickup را آزمون کنید.
3. Split-brain را در Lab کنترل‌شده تولید، تشخیص و رفع کنید.
4. Upgrade Cluster و Rollback را برنامه‌ریزی کنید.
5. RCA و Evidence Index بنویسید.
6. Rubric را اجرا و صداقت را ثبت کنید.

### چرا باید یاد بگیریم؟

Gate HA همه‌ی مهارت‌های فصل را یکجا می‌سنجد: طراحی، ساخت، آزمون Failover، Split-brain و Upgrade. در دنیای واقعی مشتری می‌گوید «ما دو فایروال داریم ولی دیشب همه چیز قطع شد». شما باید بتوانید بگویید چرا و چگونه جلوگیری کنیم.

### صورت مسئله

سازمان دو FortiGate هم‌مدل دارد. نیازمندی‌ها:

1. Active-Passive با Failover زیر ۱۰ ثانیه.
2. Session Pickup برای TCP.
3. Management جدا برای هر عضو.
4. آزمون Split-brain کنترل‌شده.
5. برنامه‌ی Upgrade بدون قطع طولانی.

عیب‌های تزریق‌شده:

1. Heartbeat فقط یک لینک و روی پورت مشترک با ترافیک.
2. `override enable` با Priority بالا روی A، باعث Failback ناخواسته.
3. B Config دستی دارد (Out-of-sync).

### طراحی مرجع

| پارامتر | مقدار |
|---|---|
| mode | a-p |
| hbdev | port3 (100)، port4 (50) مستقیم |
| priority | A=200، B=100 |
| override | disable |
| monitor | port1، port2 |
| session-pickup | enable (+connectionless) |
| ha-mgmt | port8 |

### کلید پاسخ — سه عیب

**عیب ۱ (Heartbeat مشترک):**

1. Evidence: `history read` ⇒ `heartbeat lost` در ساعات اوج؛ Flapping.
2. علت: hbdev روی لینک شلوغ و تکی.
3. رفع: دو لینک اختصاصی مستقیم.
4. تأیید: بدون Flapping در ۲۴ ساعت.

**عیب ۲ (override):**

1. Evidence: پس از Reboot A، A فوراً Primary؛ Session قطع.
2. علت: `override enable`.
3. رفع: `override disable` + Failback دستی در پنجره.
4. تأیید: Reboot A ⇒ B Primary می‌ماند.

**عیب ۳ (Out-of-sync):**

1. Evidence: `checksum cluster` متفاوت (policy).
2. علت: تغییر مستقیم روی B.
3. رفع: `execute ha synchronize start`؛ دسترسی ادمین B محدود.
4. تأیید: checksum برابر.

### آزمون Split-brain کنترل‌شده

``` text
1 backup both configs
2 disconnect all heartbeat links (lab only, maintenance window)
3 observe: both primary? (get system ha status on both via console/ha-mgmt)
4 reconnect heartbeat
5 observe re-election, check which config wins
6 verify checksum, session, traffic
```

نتیجه: Cluster پس از اتصال دوباره بر اساس Election (monitored interfaces ⇒ uptime ⇒ priority ⇒ serial) یک Primary انتخاب می‌کند. ثبت: چه Sessionهایی قطع شد.

### Upgrade و Rollback

1. Backup + Upgrade Path.
2. Secondary ارتقا؛ Failover؛ Primary ارتقا.
3. آزمون: Ping، Session، Policy، UTM.
4. Rollback آزمایشی (Boot Partition قبلی) در Lab.

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| طراحی/پارامتر | 15 |
| ساخت و Verify | 15 |
| Failover و Session Pickup با اندازه‌گیری | 20 |
| سه عیب با Evidence | 25 |
| Split-brain و Upgrade | 15 |
| RCA/صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Evidence Index

| مورد | فایل | دستور |
|---|---|---|
| وضعیت | ev1_ha.txt | `get system ha status` |
| Sync | ev2_cs.txt | `checksum cluster` |
| تاریخچه | ev3_hist.txt | `history read` |

#### مثال متوسط — RCA

``` text
Impact  : outage 12 s + session loss at 02:10
Cause   : override enabled, A returned and took over
Fix     : override disable, planned failback
Prevent : HA change checklist; test reboot in window
```

#### مثال متوسط — اندازه‌گیری

Reboot Primary: ۴ ping قطع (۴ ثانیه) و SSH باقی ماند ⇒ زیر هدف ۱۰ ثانیه.

#### مثال سخت — Split-brain ناخواسته

در Production Heartbeat قطع شد. هر دو Primary؛ ARP آشفته. اقدام: ۱) Console به B ۲) Shutdown پورت‌های داده‌ی B ۳) اصلاح Heartbeat ۴) Rejoin ۵) RCA. درس: دو Heartbeat مستقل.

#### مثال سخت — صداقت

Lab اجرا نشده؛ زمان‌ها مدل‌اند؛ گزارش باید «Unverified» بنویسد.

### مسیر GUI (مستندی، Unverified)

1. System → HA: Mode، Group name، Password، Heartbeat Interfaces، Priority.
2. Monitor Interfaces را انتخاب کنید.
3. System → Firmware برای Upgrade.

### Lab هدایت‌شده (اجرا نشده)

1. Cluster، سه عیب را رفع کنید.
2. Split-brain کنترل‌شده.
3. Upgrade با Rollback.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Flapping | Heartbeat | اختصاصی |
| Failback ناخواسته | override | disable |
| checksum | Config | sync |
| دو Primary | HB | کابل |

### جمع‌بندی

G-HA: طراحی، ساخت، Failover، Session Pickup، Split-brain، Upgrade/Rollback، سه عیب، RCA و Evidence با صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) Heartbeat چیست؟ *(پاسخ: 22-5-ت1)*

**ت2.** (ساده) override disable چه می‌کند؟ *(پاسخ: 22-5-ت2)*

**ت3.** (متوسط) چرا دو لینک HB؟ *(پاسخ: 22-5-ت3)*

**ت4.** (متوسط) Session pickup چه می‌کند؟ *(پاسخ: 22-5-ت4)*

**ت5.** (سخت) Split-brain را شرح و رفع کنید. *(پاسخ: 22-5-ت5)*

**ت6.** (سخت، طراحی) برنامه‌ی Upgrade Cluster. *(پاسخ: 22-5-ت6)*

**Q1.** Quick quiz (English): What causes a split-brain in an HA cluster? *(پاسخ: 22-5-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FGCP | FortiGate Clustering Protocol | پروتکل خوشه‌بندی |
| HB | Heartbeat | ضربان |

- *Use two independent heartbeat links.* ← از دو لینک Heartbeat مستقل استفاده کنید.

### کارت Lab

**کارت Lab:** آزمون HA (اجرا نشده؛ Needs-License). **Evidence:** `03-ops/g-ha.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: HA (FGCP)
- FortiOS 7.0 HA guide

## درس 22-6 — HA در عمق: Active-Active، Load Balancing، Virtual Cluster و Management Interface

**فصل 22 · درس افزوده برای سرفصل رسمی NSE 4 (FortiOS 7.0): «Identify and configure different operation modes for an FGCP HA cluster» · پیش‌نیاز: ۲۲-۰ تا ۲۲-۵**

> **وضعیت:** نظری/مستندی؛ FortiOS 7.0.3 نامی (بوت نشده)؛ دستورها `Unverified`؛ HA به دو دستگاه لایسنس‌دار نیاز دارد (Needs-License)؛ Lab اجرا نشده.

### ۱) این درس درباره چیست و چرا باید یاد بگیریم؟

**چه چیزی یاد می‌گیریم:** دو حالت FGCP (Active-Passive و Active-Active)، اینکه در Active-Active واقعاً چه چیزی تقسیم می‌شود، Virtual Cluster، Interface مدیریتی اختصاصی و کدام حالت را چه وقت انتخاب کنیم.

**چرا لازم است؟** تصور «Active-Active یعنی ظرفیت دو برابر» اشتباه رایجی است. اگر آن را اشتباه بفهمید، فایروال را کم‌ظرفیت می‌خرید و Cluster بعد از Failover از بار پر می‌شود. سؤال آزمون هم دقیقاً همین تفاوت‌هاست.

### ۲) توضیح از پایه

| معیار | Active-Passive (a-p) | Active-Active (a-a) |
|---|---|---|
| ترافیک | فقط Primary پردازش می‌کند | Primary بخشی را به Subordinate می‌دهد |
| ظرفیت پس از Failover | همان یک دستگاه | یک دستگاه (باید برای بار کامل طراحی شود) |
| پیچیدگی | کم | بیشتر |
| کاربرد | رایج‌ترین | بار UTM سنگین |

#### ۲-۱) در Active-Active دقیقاً چه چیزی تقسیم می‌شود؟

طبق مستند FortiOS، به‌صورت پیش‌فرض Primary ترافیکی را که **بازرسی عمیق (UTM/Proxy-based)** می‌خواهد بین اعضا پخش می‌کند؛ ترافیک عادی (بدون Profile) همچنان از Primary می‌گذرد، مگر اینکه گزینه‌ی `load-balance-all` فعال شود. Primary همیشه تمام ترافیک ورودی را دریافت می‌کند و بخشی را به Subordinate می‌فرستد؛ پس Primary نقطه‌ی عبور اصلی می‌ماند.

``` text
config system ha
 set mode a-a
 set schedule round-robin
 set load-balance-all disable
end
```

الگوریتم‌های Schedule (نمونه): `round-robin`، `weight-round-robin`، `least-connection`، `random`، `ip`، `ipport`، `hub`، `none`.

#### ۲-۲) Virtual Cluster

وقتی چند VDOM دارید، می‌توان VDOMها را به دو Virtual Cluster تقسیم کرد: Cluster 1 در عضو A Primary و Cluster 2 در عضو B Primary. بدین ترتیب هر دستگاه برای بخشی از VDOMها Active است و بار توزیع می‌شود (در عین حال هر دو Failover‌پذیرند). نیاز به Multi-VDOM (درس ۲۴).

#### ۲-۳) Management Interface اختصاصی

``` text
config system ha
 set ha-mgmt-status enable
 config ha-mgmt-interfaces
  edit 1
   set interface "mgmt"
   set gateway 10.50.0.1
  next
 end
end
```

با این تنظیم می‌توانید به **هر عضو** مستقیماً (حتی Secondary) از شبکه‌ی Mgmt وصل شوید؛ بدون آن، مدیریت فقط به Primary می‌رسد.

#### ۲-۴) سایر تنظیمات مرتبط

``` text
config system ha
 set group-name "FGT-HA"
 set hbdev "port7" 50 "port8" 50
 set session-pickup enable
 set monitor "port1" "port2"
 set override disable
end
```

### ۳) مثال‌های حل‌شده از ساده به سخت

**ساده — انتخاب حالت.** شعبه‌ی کوچک با ترافیک 300 Mbps و بدون UTM سنگین ⇒ Active-Passive.

**متوسط — محاسبه‌ی ظرفیت.** مرکز با 3 Gbps ترافیک؛ هر دستگاه با UTM می‌تواند 2 Gbps. اگر Active-Active فرض شود ولی `load-balance-all` خاموش باشد، Primary همچنان همه‌ی ترافیک را می‌پذیرد.

``` text
Required capacity after failover = 3 Gbps
Single unit capacity (UTM)       = 2 Gbps
2 < 3  ->  after failover one unit is overloaded
```

نتیجه: باید مدل بزرگ‌تر یا Profileهای سبک‌تر؛ A-A ظرفیت را حل نمی‌کند، چون پس از Failover باز یک دستگاه می‌ماند.

**متوسط — دسترسی به Secondary.** برای ارتقا باید به Subordinate وصل شوید؛ بدون Management Interface اختصاصی ممکن نیست. با `ha-mgmt-status enable` از Mgmt مستقیم.

**سخت — Virtual Cluster.** دو VDOM: `VD-A` و `VD-B`. تنظیم: VD-A در vcluster1 با Priority بالاتر روی FGT-1 و VD-B در vcluster2 با Priority بالاتر روی FGT-2.

``` text
get system ha status
diagnose sys ha history read
```

انتظار: هر دستگاه برای یک VDOM Primary است. در Failover یک دستگاه، VDOMهای او نیز به دستگاه دیگر می‌روند.

**سخت — «A-A فعال است ولی Subordinate کم‌کار است».** علت: Policy بدون Profile ⇒ ترافیک تقسیم نمی‌شود. راه: `load-balance-all enable` (با سنجش اثر) یا اعمال Profileها طبق نیاز.

### ۴) Lab (اجرا نشده)

دو FortiGate VM لایسنس‌دار؛ a-p و سپس a-a؛ `get system ha status` و Session را مقایسه کنید.

### ۵) اصطلاحات این درس

| اصطلاح | شکل کامل | معنی |
|---|---|---|
| FGCP | FortiGate Clustering Protocol | پروتکل Cluster فورتی‌گیت |
| a-p / a-a | Active-Passive / Active-Active | حالت‌های HA |
| vcluster | Virtual Cluster | Cluster مجازی برای VDOM |
| HBdev | Heartbeat Device | Interface ضربان‌قلب |

### ۶) تمرین‌ها

**ت1.** (ساده) تفاوت a-p و a-a؟ *(پاسخ: 22-6-ت1 در بخش «پاسخ‌ها» انتهای فصل)*

**ت2.** (ساده) Virtual Cluster به چه چیزی نیاز دارد؟ *(پاسخ: 22-6-ت2 در بخش «پاسخ‌ها» انتهای فصل)*

**ت3.** (متوسط) چرا A-A ظرفیت پس از Failover را حل نمی‌کند؟ *(پاسخ: 22-6-ت3 در بخش «پاسخ‌ها» انتهای فصل)*

**ت4.** (سخت) چگونه به Subordinate مستقیم وصل شویم؟ *(پاسخ: 22-6-ت4 در بخش «پاسخ‌ها» انتهای فصل)*

### ۷) English Corner

- *In active-active mode the primary unit distributes only certain sessions to the subordinate units.*
- *Size the cluster so that one unit can carry the full load after a failover.*
- **Q1.** What does load-balance-all change? *(پاسخ: 22-6-Q1 در بخش «پاسخ‌ها» انتهای فصل)*

---

## پاسخ‌های فصل 22

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 22-1

**22-1-ت1** — نقطه‌ی شکست واحد.

نقطه‌ی شکست واحد (SPOF) جزئی است که خرابی آن کل سرویس را قطع می‌کند؛ فایروال تکی SPOF کلاسیک است و HA آن را حذف می‌کند.

**22-1-ت2** — خیر؛ SD-WAN/Dual-ISP.

خیر؛ HA فایروال خرابی ISP را پوشش نمی‌دهد؛ برای آن Dual-ISP/SD-WAN لازم است.

**22-1-ت3** — 1−0.005×0.005 = 99.9975٪.

دو فایروال موازی با دسترس‌پذیری ۹۹٫۵٪ هر کدام: احتمال خرابی هم‌زمان 0.005×0.005=0.000025 ⇒ دسترس‌پذیری 99.9975٪ (با فرض استقلال).

``` text
A = 1 - (0.005 x 0.005) = 99.9975 %
```

**22-1-ت4** — دسترس‌پذیری سری ضرب می‌شود؛ ISP 99.9٪ کل را محدود می‌کند.

در اجزای سری دسترس‌پذیری ضرب می‌شود؛ ISP با ۹۹٫۹٪ سقف کل سیستم را محدود می‌کند، هرقدر فایروال HA باشد.

**22-1-ت5** — چهار خرابی خارج از دامنه‌ی HA

**استدلال کلی:** HA فقط خرابی «یک دستگاه از دو دستگاه یکسان» را پوشش می‌دهد؛ خطاهایی که هر دو دستگاه یکسان تجربه می‌کنند یا خارج از دستگاه‌اند پوشش داده نمی‌شوند.

1. **خرابی ISP/لینک بیرونی:** هر دو فایروال همان لینک را دارند ⇒ مکمل: Dual-ISP/SD-WAN.
2. **Config خراب:** FGCP پیکربندی را همگام می‌کند، پس خطای Policy روی هر دو عضو اعمال می‌شود ⇒ مکمل: Change Management، Backup، Rollback.
3. **CVE یا باگ نرم‌افزاری مشترک:** هر دو عضو همان نسخه را اجرا می‌کنند ⇒ مکمل: Patch Management، Segmentation، تنوع/Staging.
4. **Split-brain:** خود HA می‌تواند در قطع Heartbeat خطا بسازد ⇒ مکمل: Heartbeat مستقل و Monitor مناسب.

(موارد دیگر: SPOF سوئیچ/برق مشترک، خطای انسانی.)

**22-1-ت6** — ماتریس خرابی سایت مرکزی

**روش ساخت:** برای هر جزء بپرسید «اگر این خراب شود چه می‌شود؟» و مکمل و RTO هدف را بنویسید.

| جزء | ریسک | راه مکمل | RTO هدف |
|---|---|---|---|
| فایروال | قطع کامل | HA A-P | ثانیه تا ده‌ها ثانیه |
| ISP | قطع اینترنت | Dual-ISP + SD-WAN | چند ثانیه |
| سوئیچ هسته | قطع داخلی | Stack/دو سوئیچ + LAG | ثانیه |
| برق | قطع کل | دو منبع + دو UPS/مسیر | بدون وقفه |
| Config | تغییر خراب | Backup، Change، Rollback | دقیقه |
| سایت | فاجعه | DR سایت دوم | ساعت (طبق RTO/RPO) |

**تحلیل:** عدد RTO از نیاز کسب‌وکار می‌آید نه از قابلیت دستگاه؛ اگر RTO هدف از توان راه‌حل کمتر است، یا راه‌حل را ارتقا دهید یا هدف را با مدیریت بازنگری کنید.

**22-1-Q1** — Because serial availabilities multiply, so the lowest one dominates.

### پاسخ‌های بازنویسی درس 22-2


### پاسخ‌های بازنویسی عمیق درس 22-2

**22-2-ت1** — هم‌مدل، هم‌نسخه، لایسنس، Heartbeat، پورت‌های مشابه.

پیش‌نیاز HA: هم‌مدل، هم‌نسخه (Build یکسان)، لایسنس، Heartbeat اختصاصی و پورت‌های مشابه.

**22-2-ت2** — تا خرابی یک لینک Cluster را نشکند.

دو لینک Heartbeat تا خرابی یک لینک Cluster را نشکند و Split-brain نشود.

**22-2-ت3** — پس از بازگشت عضو قوی‌تر، Primary تغییر نمی‌کند و Flap نمی‌شود.

**22-2-ت4** — Config اعضا یکی نیست؛ checksum متفاوت.

Out-of-sync یعنی Config اعضا یکی نیست و checksum متفاوت است؛ با `diagnose sys ha checksum cluster` دیده می‌شود.

**22-2-ت5** — نسخه، Group، Password، لایسنس، HB.

عضو دوم Join نمی‌شود — روش بررسی: ۱) `get system status` روی هر دو: نسخه/Build و Serial. ۲) `get system ha status` روی Primary: آیا عضو دوم دیده می‌شود؟ ۳) Group name و Password یکسان؟ ۴) Heartbeat: کابل، `hbdev` و VLAN. ۵) لایسنس هر دو. رفع معمول: هم‌نسخه‌سازی یا Group/Password یکسان؛ پس از Join checksum را مقایسه کنید.

**22-2-ت6** — برگه‌ی HA

**برگه‌ی HA (قابل اجرا و با دلیل):**
| پارامتر | مقدار | دلیل |
|---|---|---|
| mode | a-p | سادگی و عدم Asymmetric |
| group-name/group-id | یکتا | VMAC و جداسازی Cluster |
| password | Vault | اعتبار Cluster |
| hbdev | دو لینک مستقیم | حذف SPOF Heartbeat |
| priority | A=200، B=100 | تعیین نقش ترجیحی |
| override | disable | جلوگیری از Failback ناخواسته |
| monitor | Interfaceهای حیاتی | Failover منطقی |
| session-pickup | enable | حفظ TCP |
| ha-mgmt | Interface Mgmt | دسترسی به Secondary |

**نکته‌ی علمی:** مقدار هر پارامتر با مستند FGCP همان نسخه تطبیق داده شود؛ برگه بدون ستون «دلیل» فقط کپی دستور است نه طراحی.

**22-2-Q1** — Because configuration is synchronized from the primary to the secondary.

### پاسخ‌های بازنویسی درس 22-3


### پاسخ‌های بازنویسی عمیق درس 22-3

**22-3-ت1** — تعداد بسته‌ی گمشده × Interval.

زمان قطع = تعداد بسته‌ی گمشده × فاصله‌ی ping؛ مثال ۱۲ بسته × ۰٫۲ ثانیه = ۲٫۴ ثانیه.

**22-3-ت2** — همگام‌سازی Session.

Session pickup Sessionهای TCP را بین اعضا همگام می‌کند تا پس از Failover ادامه یابند.

**22-3-ت3** — برخی UTM/Proxy.

Sessionهای مبتنی بر UTM/Proxy یا SSL Inspection ممکن است پس از Failover ریست شوند.

**22-3-ت4** — جلوگیری از Flap.

Failback کنترل‌شده از Flap و قطع‌های پیاپی جلوگیری می‌کند.

**22-3-ت5** — Failover ۱۲ ثانیه؛ تحلیل

**علامت:** Failover ۱۲ ثانیه، بیش از هدف (مثلاً ۱۰ ثانیه). این علامت است نه علت.

**فرضیه‌ها و آزمون تفکیک:**
1. **تشخیص دیر:** `diagnose sys ha history read` زمان رویداد و دلیل را نشان می‌دهد؛ اگر فاصله‌ی «خرابی» تا «تغییر وضعیت» زیاد است، فرضیه‌ی Heartbeat/Monitor Timer تقویت می‌شود.
2. **Monitor نداشتن:** خرابی لینک بدون Monitor فقط با Heartbeat دیده می‌شود (کندتر).
3. **پس از Failover:** ARP/Gratuitous، MAC مجازی و سوئیچ بالادست (جدول MAC) ممکن است ثانیه‌ها طول بکشد؛ Sniffer روی سوئیچ/اولین بسته‌ی خروجی Primary جدید.
4. **Session/Route:** همگرایی BGP/OSPF یا SD-WAN بعد از Failover که نه به HA بلکه به مسیریابی برمی‌گردد.

**استدلال:** برای هر فرضیه پیش‌بینی بنویسید و آزمون ارزان را اول بزنید. پیش‌فرض Timerها را از مستند نسخه بخوانید (در این دوره تأیید نشده). علت وقتی اثبات می‌شود که با تغییر Timer/Monitor یا رفع مسئله‌ی ARP، زمان واقعاً کم شود.

**22-3-ت6** — ماتریس تست HA

| # | آزمون | انتظار | شاهد |
|---|---|---|---|
| 1 | Reboot Primary | Failover + حفظ TCP | Ping/iperf + `history` |
| 2 | قطع Interface Monitor | Failover | `get system ha status` |
| 3 | قطع یک Heartbeat | بدون Failover | وضعیت HA بدون تغییر |
| 4 | قطع هر دو Heartbeat (Lab، پنجره) | Split-brain کنترل‌شده | وضعیت دو عضو |
| 5 | Failback کنترل‌شده | بدون قطع غیرمنتظره | Ping/Session |

**چرا همین پنج؟** هر آزمون یک مکانیزم متفاوت را می‌سنجد (خرابی دستگاه، Monitor، افزونگی Heartbeat، شکست Heartbeat، بازگشت). آزمون ۳ ثابت می‌کند افزونگی HB کار می‌کند؛ آزمون ۴ بدترین حالت را می‌شناساند.

**22-3-Q1** — Lost packets multiplied by the ping interval.

### پاسخ‌های بازنویسی عمیق درس 22-4


### پاسخ‌های بازنویسی عمیق درس 22-4

**22-4-ت1** — دو عضو هر دو Primary شده‌اند.

Split-brain یعنی هر دو عضو خود را Primary می‌دانند (HB قطع)؛ ARP/IP تکراری و قطعی ایجاد می‌کند.

**22-4-ت2** — تاریخچه‌ی علل تغییر Primary.

`diagnose sys ha history read` تاریخچه و علت تغییر Primary را نشان می‌دهد.

**22-4-ت3** — تغییر روی Secondary یا HB.

Out-of-sync معمولاً از تغییر مستقیم روی Secondary یا ضعف Heartbeat می‌آید.

**22-4-ت4** — Secondary، Failover، Primary.

ترتیب Upgrade: Secondary، Failover، سپس Primary قبلی؛ با checksum پس از هر مرحله.

**22-4-ت5** — رفع Split-brain

**فرض:** هر دو عضو Primary و Heartbeat قطع است.

**استدلال گام‌ها:**
1. تأیید با `get system ha status` از Console/ha-mgmt هر دو؛ هر اقدام از راه دور ممکن است خودش دچار تکرار IP/MAC باشد.
2. قبل از بازگرداندن Heartbeat، تصمیم بگیرید **کدام Config درست است** (اگر در فاصله‌ی Split تغییری روی هر دو انجام شده). Backup هر دو را بگیرید.
3. Heartbeat را بازگردانید (دو لینک مستقل).
4. Cluster طبق Election یک Primary انتخاب می‌کند؛ عضوی که نباید Primary بماند را در صورت نیاز Reboot/Rejoin کنید.
5. `diagnose sys ha checksum cluster` و Sync؛ سپس آزمون ترافیک.
6. RCA: چرا Heartbeat‌ها هر دو قطع شدند؟ (SPOF مشترک؟) و اصلاح طراحی.

**چرا همه‌ی گزینه‌ها یکسان نیستند؟** Reboot کورکورانه ممکن است Config جدیدتر را از بین ببرد؛ رفع بدون کشف علت دوباره تکرار می‌شود.

**22-4-ت6** — برنامه‌ی Rollback Cluster

**هدف:** بازگشت سریع و قابل‌پیش‌بینی پس از ارتقای ناموفق.
1. **پیش از ارتقا:** Backup Config هر دو عضو، Hash، ثبت نسخه‌ی قبلی و Partition قبلی؛ آزمون Rollback در Lab.
2. **اگر فقط Secondary مشکل دارد:** Boot از Partition قبلی همان عضو (`execute set-next-reboot` طبق مستند)، اتصال به Cluster و Sync.
3. **اگر بعد از Failover مشکل نمایان شد:** Failover به عضو قدیمی (در صورتی که هنوز ارتقا نشده)، سپس Rollback عضو جدید.
4. **اگر Config به قالب جدید تبدیل شده:** Restore Config پیش از ارتقا روی Firmware قدیمی.
5. **تأیید:** `get system ha status`، `checksum cluster`، VPN، BGP، UTM، Log.

**نکته‌ی استدلالی:** ارتقای Firmware و تبدیل Config دو تغییرند؛ Rollback ناقص (فقط یکی) باعث ناسازگاری می‌شود.

**22-4-Q1** — diagnose sys ha history read.

### پاسخ‌های بازنویسی عمیق درس 22-5


### پاسخ‌های بازنویسی عمیق درس 22-5

**22-5-ت1** — ارتباط بین اعضا برای تشخیص سلامت و همگام‌سازی؛ قطع کامل آن Split-brain می‌سازد.

**22-5-ت2** — پس از بازگشت عضو قوی‌تر، Primary فعلی را تغییر نمی‌دهد و از Flap جلوگیری می‌کند.

**22-5-ت3** — تا خرابی یک لینک Cluster را Split نکند.

دو لینک HB مستقل تا خرابی یک لینک Cluster را Split نکند.

**22-5-ت4** — Sessionهای TCP را بین اعضا همگام می‌کند تا پس از Failover ادامه یابند.

**22-5-ت5** — Split-brain در Gate HA

**شرح:** با قطع تمام لینک‌های Heartbeat، هر عضو نمی‌تواند وضعیت دیگری را ببیند و فرض می‌کند دیگری خراب است؛ طبق منطق Election خودش Primary می‌شود. نتیجه: دو Primary با VMAC/IP یکسان ⇒ آشفتگی ARP، قطع/نوسان.

**رفع (مرحله‌ای):** Console به هر دو ⇒ جلوگیری از آسیب ادامه‌دار (پورت‌های داده‌ی یکی را موقت Down) ⇒ بازگرداندن HB ⇒ Rejoin کنترل‌شده ⇒ بررسی Config/Sessionها ⇒ RCA.

**پیشگیری:** حداقل دو HB مستقل و مستقیم، Monitor مناسب، ha-mgmt برای دسترسی جدا، آزمون دوره‌ای.

**سوءبرداشت:** «Split-brain یعنی Config دو عضو متفاوت است» ← نه؛ مشکل در دید حالت (State) است؛ Config ممکن است حتی یکسان باشد.

**22-5-ت6** — برنامه‌ی Upgrade Cluster

1. Backup Config و ثبت Partition/نسخه‌ی فعلی؛ بررسی Upgrade Path و Release Notes.
2. Staging با Config واقعی.
3. Image روی Primary؛ Cluster ابتدا Secondary را ارتقا می‌دهد (روش Uninterruptible).
4. پس از Rejoin و `checksum` برابر، Failover کنترل‌شده.
5. ارتقای عضو قبلی؛ آزمون کامل (HA، VPN، BGP، SD-WAN، UTM، Log).
6. Rollback آماده: Partition قبلی/Restore Config؛ معیار Trigger از قبل.

**چرا ترتیب مهم است؟** اگر هر دو را هم‌زمان ارتقا دهید، افزونگی هنگام تغییر وجود ندارد؛ ترتیب «Secondary اول» همیشه یک عضو سالم را برای بازگشت نگه می‌دارد.

**22-5-Q1** — Loss of all heartbeat links so both units think they are primary.

### پاسخ‌های درس افزوده‌ی 22-0 (فصل 22)

**22-0-ت1** — Active-Passive: یک دستگاه ترافیک می‌برد؛ Active-Active: بار Inspection بین اعضا پخش می‌شود؛ a-p ساده‌تر.

**22-0-ت2** — قطع Heartbeat با دو دستگاه زنده که هر دو Primary می‌شوند.

Split-brain: HB قطع ولی هر دو دستگاه زنده‌اند و هر دو Primary می‌شوند.

**22-0-ت3** — Failback خودکار نمی‌شود؛ عضو فعلی Primary می‌ماند.

با override disable، Failback خودکار انجام نمی‌شود؛ عضو فعلی Primary می‌ماند.

**22-0-ت4** — تا خرابی یک لینک باعث Split-brain نشود.

دو لینک HB تا خرابی یک لینک Split-brain نسازد.

**22-0-ت5** — علت Session Pickup و راه‌حل

**فرض‌ها:** Cluster FGCP، ترافیک TCP عادی (بدون Proxy-based UTM)، لینک Heartbeat سالم.

**استدلال:**
1. FGCP پیکربندی را همیشه همگام می‌کند، اما جدول Session را فقط وقتی `session-pickup` فعال باشد به Secondary می‌فرستد. بدون آن، Secondary پس از Failover Sessionهای قبلی را نمی‌شناسد.
2. بسته‌ی بعدی TCP روی Primary جدید «بسته‌ی بدون Session» است؛ SYN نیست و به‌عنوان اتصال معتبر تلقی نمی‌شود، پس رد یا Reset می‌شود و برنامه اتصال را دوباره می‌سازد.
3. راه‌حل: `set session-pickup enable` (و برای UDP/ICMP `session-pickup-connectionless`)؛ اثبات: Failover آزمایشی با `ssh` یا `iperf` طولانی.
4. محدودیت‌ها: Sessionهای مبتنی بر Proxy/بعضی UTM، SSL Inspection یا Sessionهای وابسته به Helper ممکن است همگام نشوند؛ Session Pickup هم‌گام‌سازی نیمه‌همزمان است و بسته‌های لحظه‌ی Failover ممکن است گم شوند.

**چرا گزینه‌های دیگر کافی نیستند؟** کاهش Timeout یا Failover سریع‌تر Session را برنمی‌گرداند؛ فقط همگام‌سازی Session مشکل را هدف می‌گیرد.

**سؤال انتقالی:** در Cluster دارای Session Pickup، چرا ممکن است یک تماس SIP/UDP هنوز قطع شود؟ (راهنما: connectionless، NAT/Helper.)

**22-0-ت6** — HA و SD-WAN کنار هم

**فرض‌ها:** سایت مرکزی، دو FGT در Cluster A-P، دو ISP.

**استدلال نقش‌ها:**
| لایه | خطایی که حل می‌کند | خطایی که حل نمی‌کند |
|---|---|---|
| HA (FGCP) | خرابی دستگاه، Reboot، خرابی Interface Monitor | خرابی ISP، Config خراب (همگام می‌شود)، CVE مشترک |
| SD-WAN/Dual-ISP | خرابی یا افت کیفیت لینک ISP | خرابی خود فایروال |

**طراحی:** هر ISP به هر دو عضو Cluster (با سوئیچ‌های جدا یا Redundant Interface) تا خرابی یک فایروال ISP را قطع نکند؛ Heartbeat دو لینک مستقل؛ SD-WAN روی Cluster یک‌پارچه با Health-checkهایی که به مقصد خارجی (نه Gateway) می‌روند؛ Monitor Interface روی لینک‌های مهم.

**اشتباه رایج:** تصور اینکه HA «افزونگی ISP» هم می‌دهد؛ برعکس، اگر هر دو فایروال به یک ISP/سوئیچ وصل باشند همان SPOF می‌ماند.

**22-0-م1** — بررسی هم‌خوانی Config بین اعضا.

Checksum Cluster هم‌خوانی Config بین اعضا را بررسی می‌کند.

**22-0-Q1** — Loss of heartbeat between members that are both still running, so each assumes the primary role.

### پاسخ‌های درس افزوده‌ی 22-6 (فصل 22)

**22-6-ت1** — در a-p فقط Primary ترافیک را پردازش می‌کند؛ در a-a Primary بخشی از ترافیک (پیش‌فرض ترافیک نیازمند UTM/Proxy) را به Subordinate توزیع می‌کند.

**22-6-ت2** — Multi-VDOM؛ VDOMها بین دو Virtual Cluster تقسیم می‌شوند.

**22-6-ت3** — چون پس از افتادن یک عضو فقط یک دستگاه می‌ماند و باید کل بار را بردارد؛ ظرفیت طراحی باید بر پایه‌ی یک دستگاه باشد.

**22-6-ت4** — اتصال مستقیم به عضو Subordinate

**مسئله:** در Cluster، مدیریت معمولاً به Primary می‌رسد؛ برای عیب‌یابی عضو دیگر دسترسی مستقیم لازم است.

**راه‌ها:**
1. **ha-mgmt interface:** Interface مدیریتی اختصاصی با IP یکتا برای هر عضو (`config system ha → ha-mgmt-status`).
2. **`execute ha manage <ID> <admin>`** از CLI Primary.
3. Console/OOB.

**استدلال:** اتصال به Interface داده‌ی مشترک به Primary می‌رود؛ بنابراین بدون ha-mgmt یا Console مشاهده‌ی مستقل عضو دوم ممکن نیست. ha-mgmt را در شبکه‌ی Mgmt بگذارید نه روی لینک کاربران.

**22-6-Q1** — With it enabled, the primary distributes all sessions (not only those requiring content inspection) to the cluster members.

---

# فصل 23 — Multi-Firewall و Asymmetric Routing (معماری ۵)

> **یادداشت علمی v4.0 — فصل 23:** عمومی: Asymmetric Routing و Stateful. مختص محصول: RPF/`asymroute`/FGSP در FortiOS.
> فرض: رفتار RPF/Session وابسته به نسخه؛ غیرفعال‌سازی کنترل‌ها فقط موقت.
> مرجع: Fortinet Docs.
> **وضعیت منبع v4.1:** وجود، نام و رفتار `asymroute`، `tcp-session-without-syn`، `strict-src-check` و سینتکس FGSP در صفحات رسمی خوانده‌شده تأیید نشد؛ آن‌ها از حافظه‌اند و نباید قطعی تلقی شوند.


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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا مسیر نامتقارن مسئله‌ی فایروال است؟** تصور کنید نگهبان ساختمان دفتری دارد: هر کس وارد شود، نامش را ثبت می‌کند و هنگام خروج، نام را تطبیق می‌دهد. اگر کسی از در دیگر (که نگهبان دیگری با دفتر خالی دارد) خارج شود، آن نگهبان می‌گوید «من این آدم را ندیده‌ام» و جلویش را می‌گیرد. فایروال Stateful همین‌طور است: وقتی SYN می‌رسد Session می‌سازد؛ بسته‌ی بعدی را فقط اگر با Session بخواند می‌پذیرد.

**مسیر نامتقارن (Asymmetric Routing)** یعنی بسته‌ی رفت از مسیر A و بسته‌ی برگشت از مسیر B برود. برای روتر ساده بی‌اشکال است، برای فایروال Stateful مشکل‌ساز.

``` text
Client -> FW1 -> Server       (SYN, Session created on FW1)
Server -> FW2 -> Client       (SYN-ACK arrives at FW2: no session -> drop)
```

**چرا پیش می‌آید؟** دو ISP، ECMP، Policy Route یک‌طرفه، دو فایروال موازی، سرور با چند کارت شبکه. **علامت کلاسیک:** «گاهی کار می‌کند، گاهی نه» و در Debug Flow پیام `no session matched` یا Drop بسته‌ی SYN-ACK.

**RPF** (Reverse Path Forwarding) نیز مسیر نامتقارن را نمی‌پسندد: فایروال بررسی می‌کند بسته از همان Interface‌ای آمده که برای رسیدن به مبدأ استفاده می‌کند.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — شاهد با Sniffer

``` text
FW1: SYN seen, ACK seen, SYN-ACK NOT seen
FW2: SYN-ACK seen,       SYN NOT seen
```

هر فایروال فقط یک جهت را دیده است ⇒ رفت از FW1 و برگشت از FW2.

#### مثال متوسط — Debug Flow

``` text
diagnose debug flow filter addr 198.51.100.8
diagnose debug flow trace start 10
diagnose debug enable
```

روی FW2 پیام «no session matched» یا «Denied by forward policy check (policy 0)» برای SYN-ACK. این دلیل «Drop بسته‌ی برگشت» است.

#### مثال متوسط — RPF

``` text
get router info routing-table details 198.51.100.8
```

اگر Route به مبدأ از Interface دیگری برود، `reverse path check fail` دیده می‌شود.

#### مثال سخت — ECMP

دو لینک با ECMP؛ رفت و برگشت Hash متفاوت دارند و دو فایروال جدا پشت لینک‌ها هستند. اتصال‌ها بی‌نظم قطع می‌شوند. راه‌ها: Hash متقارن، SNAT، Session Sync (HA A-A)، یا حذف ECMP. تأیید: ۱۰۰ بار curl بدون خطا.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: ردیابی بسته‌به‌بسته‌ی مسیر نامتقارن

``` text
Client -> FW1 -> Server      (forward via ISP-A)
Server -> FW2 -> Client      (reply via ISP-B)
FW2 sees SYN-ACK without SYN -> drop (no session)
```

نشانه در Debug Flow: `no session matched` / `Denied ... (policy 0)` برای SYN-ACK. شواهد: Sniffer روی هر دو FW.

**پرسش‌های مصاحبه**
1. *چرا Stateful مسئله دارد؟* Session باید دو جهت را ببیند.
2. *Stateless؟* ACL مشکل ندارد.
3. *RPF؟* می‌تواند رد کند.

### تکمیل عمیق: چرا مسیر نامتقارن فایروال Stateful را زمین می‌زند؟

#### چرا باید یاد بگیریم؟

فایروال Stateful مثل نگهبانی است که دفتر ثبت دارد: وقتی کسی وارد می‌شود ثبت می‌کند و موقع خروج، اسمش را تطبیق می‌دهد. اگر فرد از در دیگری خارج شود که نگهبان دیگری دارد و دفترش خالی است، می‌گوید «من این آدم را ندیدم» و جلویش را می‌گیرد. مسیر نامتقارن (Asymmetric Routing) یعنی رفت از یک مسیر و برگشت از مسیر دیگر؛ در شبکه‌های دو ISP یا دو فایروال بسیار رایج است و علت بسیاری از «گاهی کار می‌کند، گاهی نه» است.

#### توضیح ساده

فایروال Stateful برای هر اتصال یک Session می‌سازد (با بسته‌ی SYN). بسته‌ی بعدی را فقط اگر با Session مطابقت داشته باشد می‌پذیرد.

``` text
Client -> FW1 -> Server       (SYN, session created on FW1)
Server -> FW2 -> Client       (SYN-ACK arrives at FW2, no session)
FW2: drop (no session / reverse path)
```

#### مثال ساده — نشانه در Debug Flow

``` text
msg="no session matched"
msg="Denied by forward policy check (policy 0)"
```

برای بسته‌ی SYN-ACK بدون SYN؛ و در Sniffer هر دو فایروال می‌بینید که هر کدام فقط یک جهت را دیده است.

#### مثال متوسط — دو ISP

کاربر از طریق ISP-A خارج می‌شود (SNAT به IP-A)؛ ولی اگر SNAT نباشد و سرور مقصد پاسخ را به IP داخلی از طریق ISP-B بفرستد ⇒ مسیر برگشت متفاوت. SNAT پاسخ را به IP همان ISP برمی‌گرداند و مسئله را حل می‌کند.

#### مثال سخت — ECMP

دو لینک با ECMP (Equal-Cost Multi-Path، یعنی «چندمسیره با هزینه‌ی برابر»): بسته‌های رفت و برگشت با Hash متفاوت ممکن است از لینک‌های مختلف بروند. اگر دو فایروال جدا پشت دو لینک باشند، Session یک‌جانبه می‌شود. راه: Hash بر اساس 5-tuple متقارن، یا Session Sync.

#### RPF

Reverse Path Forwarding: فایروال بررسی می‌کند بسته‌ی ورودی از همان Interface‌ای که برای رسیدن به آن منبع استفاده می‌کند آمده باشد؛ اگر نه، رد می‌کند (Anti-spoofing). با مسیر نامتقارن RPF شکست می‌خورد.

#### Lab

دو مسیر بین دو دستگاه بسازید و Sniffer هر دو را مقایسه کنید.

#### عیب‌یابی

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| SYN-ACK Drop | مسیر نامتقارن | متقارن‌سازی |
| RPF fail | Route | تصحیح |
| گاهی کار می‌کند | ECMP | Hash متقارن |

#### پرسش‌ها با پاسخ

**۱. چرا Stateful مشکل دارد؟** Session یک‌جانبه.
**۲. RPF چیست؟** بررسی مسیر معکوس.
**۳. ECMP چرا؟** توزیع بار.

#### English Corner

- *A stateful firewall must see both directions of a flow.*
- Q: How does SNAT help with asymmetric return paths?

## درس 23-1 — Asymmetric Routing برای Stateful: تعریف دقیق، علت‌ها، تحلیل بسته‌به‌بسته و تفکیک RPF از No-session

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰، ۱۰-۶، ۱۱-۷، ۱۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Asymmetric Routing (مسیر نامتقارن) را دقیق تعریف کنید.
2. علت‌های رایج (دو ISP، دو فایروال، ECMP، Policy Route) را بشناسید.
3. اثر آن را بر فایروال Stateful تحلیل بسته‌به‌بسته کنید.
4. تفاوت `reverse path check fail` (RPF) و `no session matched` را بگویید.
5. نشانه‌ها را در Sniffer و Debug Flow ببینید.
6. تشخیص را با Evidence ثبت کنید.

### چرا باید یاد بگیریم؟

فرض کنید نامه‌ای را با پست پیشتاز می‌فرستید، ولی پاسخ از شرکت پخش دیگری برمی‌گردد. شما به گیرنده‌ی اول (فایروال اول) رسید ثبت کرده‌اید، ولی پاسخ به گیرنده‌ی دوم می‌رسد که از ارسال شما خبر ندارد؛ آن را رد می‌کند. فایروال Stateful هم همین است: به بسته‌ی «پاسخ» فقط وقتی اجازه می‌دهد که بسته‌ی «درخواست» را دیده و Session ساخته باشد. در معماری‌های چند لینکی/چند فایروالی، مسیر رفت و برگشت ممکن است متفاوت باشد؛ نتیجه: اتصال‌هایی که «گاهی کار می‌کنند و گاهی نه». تشخیص درست این مشکل از ماهرترین عیب‌یابی‌هاست.

### تعریف

``` text
Forward : Client -> FW-A -> Server      (SYN passes FW-A, session created on A)
Return  : Server -> FW-B -> Client      (SYN-ACK passes FW-B, no session there)
```

مسیر **متقارن** یعنی رفت و برگشت از همان دستگاه (و همان Interface‌ها).

### علت‌ها

| علت | مثال |
|---|---|
| دو ISP | خروج از ISP1، پاسخ از ISP2 |
| دو فایروال موازی | بار روی هر دو بدون Session Sync |
| ECMP | هر Flow به یک لینک |
| Policy Route | مسیر رفت با Policy و برگشت با Route معمولی |
| Routing پویا | OSPF/BGP هزینه‌ی متفاوت |
| NAT ناقص | پاسخ با IP دیگری |

### اثر روی Stateful

فایروال برای هر Session یک ورودی دارد؛ بسته‌ی پاسخ را با آن تطبیق می‌دهد. اگر پاسخ به دستگاهی برسد که Session ندارد:

1. TCP: بسته‌ی SYN-ACK (بدون SYN قبلی) ⇒ Drop (`no session matched`) یا RST.
2. اگر Interface ورودی پاسخ با Route برگشت به مبدأ نخواند ⇒ RPF Drop.

### دو پیام متفاوت

| پیام Debug | معنی | علت اصلی |
|---|---|---|
| `reverse path check fail, drop` | Interface ورودی بسته با Route به مبدأ نمی‌خواند | Routing |
| `no session matched` / `Denied: no session` | Session برای این بسته نیست | State |

``` text
diagnose debug flow filter addr 10.10.0.5
diagnose debug flow trace start 20
diagnose debug enable
```

### تحلیل بسته‌به‌بسته

``` text
t0 Client 10.10.0.5 -> Srv 198.51.100.8 SYN            arrives FW-A port2
t1 FW-A: route -> port1 (ISP1), policy OK, session created, SNAT 203.0.113.2
t2 SYN leaves FW-A port1
t3 SYN-ACK returns via ISP2 -> FW-B port1 (dst 203.0.113.2? or 198.51.100.2)
t4 FW-B: no session -> drop (SYN-ACK without SYN)
```

نتیجه: کلاینت Timeout. FW-A Session را `SYN_SENT` نشان می‌دهد؛ FW-B در Debug: `no session matched`.

### نشانه‌ها

| ابزار | نشانه |
|---|---|
| Sniffer FW-A | SYN خروجی، SYN-ACK نه |
| Sniffer FW-B | SYN-ACK ورودی (غریب) |
| Session FW-A | `SYN_SENT` |
| Debug Flow FW-B | `no session matched` / RPF |

### مثال‌های حل‌شده

#### مثال ساده — دو ISP

NAT با IP ISP1 ولی پاسخ از ISP2 می‌آید (مقصد، IP ISP1 را از مسیر دیگری می‌فرستد). چون IP ISP1 متعلق به ISP1 است معمولاً پاسخ به همان ISP برمی‌گردد؛ اگر Policy/SNAT IP اشتباه شود (IP ISP2 روی لینک ISP1) پاسخ جای دیگر می‌رود. رفع: SNAT با IP همان Interface.

#### مثال متوسط — RPF

Debug: `reverse path check fail`. `get router info routing-table details 10.10.0.5` ⇒ از port3. بسته از port4 آمده. رفع: Route صحیح یا Policy Route.

#### مثال متوسط — دو فایروال موازی

Edge1 و Edge2 با ECMP. SYN به Edge1 و SYN-ACK به Edge2. Edge2 Session ندارد ⇒ Drop. این نمونه‌ی کلاسیک.

#### مثال سخت — تفکیک دو پیام

دو خرابی با علامت یکسان (Timeout): ۱) RPF (Routing اشتباه) ۲) نبود Session (State). تفکیک با Debug Flow: پیام متفاوت؛ رفع: Route در اولی، طراحی متقارن/Session Sync در دومی.

#### مثال سخت — UDP

UDP Session برای پاسخ می‌خواهد؛ DNS با Asymmetric گاهی کار می‌کند (Session دیرتر ساخته می‌شود). نتیجه‌ی «گاهی کار می‌کند» سخت‌ترین عیب‌یابی است. Evidence: Sniffer دو فایروال هم‌زمان.

### Lab هدایت‌شده (اجرا نشده)

1. توپولوژی دو ISP بسازید.
2. علامت‌ها را در Sniffer/Debug ببینید.
3. RPF و no session را تفکیک کنید.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| SYN_SENT دائم | پاسخ از مسیر دیگر | تقارن |
| RPF fail | Route | تصحیح |
| no session | دستگاه دیگر | Session Sync/تقارن |
| گاهی کار می‌کند | ECMP | طراحی |

### نکات امنیتی

غیرفعال کردن RPF/Asymmetric Check (`asymroute`) فایروال را در برابر Spoofing/Session Hijack حساس می‌کند؛ فقط به‌عنوان راه‌حل موقت و آگاهانه.

### جمع‌بندی

Asymmetric: رفت و برگشت از دو مسیر؛ Stateful پاسخ بدون Session را رد می‌کند؛ RPF و no-session دو پیام متفاوت‌اند؛ تشخیص با Sniffer دو سمت و Debug Flow.

### تمرین و ارزیابی

**ت1.** (ساده) چرا روتر معمولی Asymmetric را تحمل می‌کند ولی فایروال Stateful نه؟ *(پاسخ: 23-1-ت1)*

**ت2.** (ساده) دو نشانه‌ی Drop در Debug Flow را نام ببرید. *(پاسخ: 23-1-ت2)*

**ت3.** (متوسط) ECMP دو فایروال: ۵۰٪ Flowها شکست می‌خورند؛ توضیح و رفع. *(پاسخ: 23-1-ت3)*

**ت4.** (متوسط) چرا SNAT بدون Session برگشتی را خراب می‌کند؟ *(پاسخ: 23-1-ت4)*

**ت5.** (سخت) VPN+Internet نامتقارن: دو علت و روش تفکیک. *(پاسخ: 23-1-ت5)*

**ت6.** (سخت، طراحی) چه موقع Asymmetric را می‌پذیریم؟ *(پاسخ: 23-1-ت6)*

**Q1.** Quick quiz (English): What two firewall behaviors commonly cause drops under asymmetric routing? *(پاسخ: 23-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| RPF | Reverse Path Forwarding check | بررسی مسیر معکوس |
| Session sync | Session synchronization | همگام‌سازی Session |
| Anycast | Anycast routing | مسیریابی چندمقصدی |

- *Capture at both firewalls to prove asymmetry.* ← برای اثبات Asymmetric در هر دو فایروال Capture بگیرید.

### کارت Lab

**کارت Lab:** تشخیص Asymmetric. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/asym.md`.

### منابع

- [Debugging the packet flow](https://docs.fortinet.com/document/fortigate/7.0.3/administration-guide/54688/debugging-the-packet-flow)
- RFC 3704 (Ingress filtering/RPF)

<a id="l-23-2"></a>

## درس 23-2 — رفع Asymmetric: طراحی متقارن، Policy Route، SNAT، Session Sync و ریسک هر راه‌حل

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰، ۲۳-۱، ۱۰-۴، ۲۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. چهار راه‌حل رفع Asymmetric را بشناسید: طراحی متقارن، Policy Route، SNAT، Session Sync.
2. ریسک هر راه‌حل را بسنجید.
3. `asymroute` و `tcp-session-without-syn` را درست (و با آگاهی از ریسک) بشناسید.
4. SNAT برای اجبار برگشت را پیاده کنید.
5. HA/Session Sync را برای موازی‌سازی مقایسه کنید.
6. توصیه‌ی طراحی بنویسید.

### چرا باید یاد بگیریم؟

وقتی مسیر نامتقارن را تشخیص دادید، سه راه دارید: ۱) مسیر را متقارن کنید (بهترین)، ۲) فایروال را مجبور به پذیرش کنید (خطرناک)، ۳) Session را بین دو فایروال همگام کنید (پیچیده). مهندس خوب «راحت‌ترین» را انتخاب نمی‌کند؛ «ایمن‌ترین» را برمی‌گزیند. غیرفعال کردن کنترل‌ها چون «کار می‌کند» رایج‌ترین دام است.

### راه‌حل ۱ — طراحی متقارن

``` text
Rule: forward and return must traverse the same firewall interface pair.
```

ابزارها: Policy Route/SD-WAN Rule برای ثابت‌کردن خروج، تنظیم Metric/Local-Pref در BGP/OSPF، یا ECMP با Hash سازگار (`source-dest-ip-based` برای دو جهت).

``` text
config system settings
    set v4-ecmp-mode source-dest-ip-based
end
```

### راه‌حل ۲ — Policy Route

``` text
config router policy
    edit 1
        set input-device "port2"
        set src "10.10.0.0/255.255.255.0"
        set dst "198.51.100.0/255.255.255.0"
        set output-device "port1"
        set gateway 203.0.113.1
    next
end
```

برگشت باید همان Interface؛ Policy Route فقط جهت رفت را کنترل می‌کند؛ برای برگشت: SNAT با IP همان لینک تا مقصد پاسخ را به همان لینک بفرستد.

### راه‌حل ۳ — SNAT

اگر مبدأ را به IP لینک مشخص NAT کنید، پاسخ طبق Routing اینترنت به همان لینک می‌رسد:

``` text
config firewall ippool
    edit "POOL-ISP1"
        set startip 203.0.113.2
        set endip 203.0.113.2
    next
end
config firewall policy
    edit 140
        set name "LAN-ISP1"
        set srcintf "ZN-LAN"
        set dstintf "port1"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
        set ippool enable
        set poolname "POOL-ISP1"
    next
end
```

### راه‌حل ۴ — Session Sync / HA

دو فایروال موازی با FGCP Active-Active یا FGSP (FortiGate Session Life Support Protocol):

``` text
config system standalone-cluster
    set standalone-group-id 1
    set group-member-id 1
    config cluster-peer
        edit 1
            set peerip 10.99.99.2
            set syncvd "root"
        next
    end
end
```

(FGSP: Sessionها بین دو فایروال مستقل همگام می‌شوند؛ جزئیات سینتکس در مستند 7.0 بررسی شود؛ Unverified.)

### گزینه‌ی «پذیرش»

``` text
config system settings
    set asymroute enable
end
config system global
    set tcp-session-without-syn enable
end
```

`asymroute enable`: کنترل Asymmetric (RPF-like) سخت‌گیری کمتر؛ `tcp-session-without-syn enable`: بسته‌ی غیر-SYN بدون Session پذیرفته می‌شود. **ریسک:** فایروال دیگر State را به‌طور کامل اعمال نمی‌کند؛ UTM/NAT ممکن است درست کار نکند؛ حملات Spoofing/Session Injection. فقط راه‌حل موقت.

### مقایسه

| راه‌حل | امنیت | پیچیدگی | توصیه |
|---|---|---|---|
| طراحی متقارن | بالا | متوسط | اولین انتخاب |
| Policy Route | بالا | کم | وقتی ساده است |
| SNAT | بالا | کم | Dual-ISP |
| Session Sync (FGSP/HA) | بالا | بالا | موازی Active-Active |
| asymroute/tcp-session-without-syn | پایین | کم | فقط موقت |

### مثال‌های حل‌شده

#### مثال ساده — SNAT برای Dual-ISP

Policy ISP1 با Pool مخصوص IP ISP1؛ پاسخ به همان لینک. آزمون: `diagnose sys session list` ⇒ `act=snat ... (203.0.113.2)`.

#### مثال متوسط — ECMP

دو ISP Active-Active با ECMP: ترافیک Flow به Flow؛ SNAT با IP لینک خروجی تضمین می‌کند پاسخ برمی‌گردد. تنظیم `v4-ecmp-mode source-ip-based` برای ثبات.

#### مثال متوسط — Policy Route

شعبه‌ها: ترافیک ERP همیشه از Tunnel؛ بقیه از ISP محلی. Policy Route (یا SD-WAN Rule) خروج را ثابت می‌کند.

#### مثال سخت — FGSP

دو Edge موازی با Load Balancer بالادست. Asymmetric رایج. FGSP Sessionها را همگام می‌کند؛ پاسخ به هر Edge برسد، Session دارد. محدودیت: Sync UTM ناقص؛ لایسنس/مدل. آزمون: شکست یکی، Session ادامه.

#### مثال سخت — دام asymroute

مدیر `asymroute enable` کرد و مشکل «حل شد». سه ماه بعد حادثه: Spoofing از شبکه‌ی مهمان کنترل نشد (RPF خاموش). RCA: راه‌حل موقت دائمی شد. درس: ثبت تاریخ بازبینی و طرح جایگزین.

### مسیر GUI (مستندی، Unverified)

1. Network → Policy Routes → Create New.
2. Policy & Objects → IP Pools / NAT در Policy.
3. System → HA (Session pickup).
4. Log & Report → Forward Traffic.

### Lab هدایت‌شده (اجرا نشده)

1. SNAT با Pool.
2. Policy Route.
3. asymroute و مقایسه امنیتی.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| پاسخ از ISP دیگر | NAT/Policy | Pool |
| ECMP گاهی کار | Hash | تنظیم |
| asymroute | امنیت | طراحی |
| Sync ناقص | FGSP | بررسی |

### نکات امنیتی

از `asymroute`/`tcp-session-without-syn` فقط موقت و مستند؛ RPF را حفظ کنید؛ Session Sync لینک ایزوله.

### جمع‌بندی

ترتیب راه‌حل: متقارن‌سازی، Policy Route، SNAT، Session Sync؛ غیرفعال‌سازی کنترل‌ها آخرین و موقت؛ ریسک هر راه‌حل را مستند کنید.

### تمرین و ارزیابی

**ت1.** (ساده) Policy Route چه کاری می‌کند؟ *(پاسخ: 23-2-ت1)*

**ت2.** (ساده) چرا SNAT برگشت را به همان فایروال می‌کشد؟ *(پاسخ: 23-2-ت2)*

**ت3.** (متوسط) ترتیب انتخاب راه‌حل‌ها را با دلیل بنویسید. *(پاسخ: 23-2-ت3)*

**ت4.** (متوسط) SNAT چه اثر منفی روی Log دارد؟ *(پاسخ: 23-2-ت4)*

**ت5.** (سخت) دو فایروال Active-Active با ECMP؛ طرح را انتخاب کنید و دلیل بیاورید. *(پاسخ: 23-2-ت5)*

**ت6.** (سخت، طراحی) آزمون پذیرش پس از رفع Asymmetric. *(پاسخ: 23-2-ت6)*

**Q1.** Quick quiz (English): Why should symmetric routing be preferred over disabling stateful checks? *(پاسخ: 23-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PBR | Policy-based routing | مسیر مبتنی بر Policy |
| IP Pool | NAT IP pool | مخزن آدرس NAT |
| Symmetric hash | Symmetric hashing | Hash متقارن |

- *Prefer symmetric design over workarounds.* ← طراحی متقارن را به راه‌حل‌های موقت ترجیح دهید.

### کارت Lab

**کارت Lab:** رفع. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/asym-fix.md`.

### منابع

- Fortinet Docs: Policy routes، IP pools (7.0)
- RFC 2992 (ECMP analysis)

<a id="l-23-3"></a>

## درس 23-3 — چند فایروال سری و موازی: الگوها، NAT، Session، Failure Domain و مانیتورینگ

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۰، ۱۵-۰، ۲۲-۰ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. الگوهای چند فایروال (سری، موازی) را مقایسه کنید.
2. NAT و Session را در هر الگو تحلیل کنید.
3. Failure Domain (دامنه‌ی خرابی) را تعریف و حداقل کنید.
4. فایروال سری را با دو سازنده (تنوع) توجیه کنید.
5. فایروال موازی (Load-balanced) را با Session Sync طراحی کنید.
6. مانیتورینگ و Rule Drift را مدیریت کنید.

### چرا باید یاد بگیریم؟

دو فایروال می‌توانند مثل دو نگهبان پشت‌سر هم (سری) یا دو نگهبان کنار هم (موازی) باشند. سری امنیت لایه‌ای می‌دهد ولی دو نقطه‌ی خرابی و پیچیدگی NAT؛ موازی ظرفیت و دسترس‌پذیری می‌دهد ولی Asymmetric و Session Sync. انتخاب اشتباه یا بی‌دلیل، پیچیدگی را زیاد و امنیت را کم می‌کند.

### الگوی ۱ — سری (Edge + Internal)

``` text
Internet -- [FW1 Edge] -- [FW2 Internal] -- LAN
```

| ویژگی | توضیح |
|---|---|
| هدف | Defense in Depth، تفکیک DMZ/داخلی |
| NAT | فقط Edge (جلوگیری از Double NAT) |
| Session | هر دستگاه Session جدا؛ مسیر یکتا ⇒ Asymmetric ندارد |
| خطر | دو Policy مستقل ⇒ Drift؛ هر دستگاه SPOF |
| تنوع سازنده | امنیت بیشتر (آسیب‌پذیری مشترک کمتر) ولی مدیریت گران‌تر |

### الگوی ۲ — موازی (Load-sharing)

``` text
Internet -- [LB/Router] -- [FW-A]
                         -- [FW-B] -- [LB/Switch] -- LAN
```

| ویژگی | توضیح |
|---|---|
| هدف | ظرفیت و دسترس‌پذیری |
| Session | باید Hash سازگار (دو جهت) یا Session Sync |
| خطر | Asymmetric (۲۳-۱) |
| راه‌حل | ECMP با Hash متقارن، FGSP، یا HA Cluster |

### الگوی ۳ — Cluster (HA)

دو دستگاه به‌عنوان یک فایروال منطقی (FGCP): ساده‌ترین برای دسترس‌پذیری؛ Active-Active محدود.

### Failure Domain

``` text
Failure domain = set of services lost when one component fails
```

مثال: یک Edge FW تنها ⇒ دامنه = کل اینترنت؛ دو Edge موازی ⇒ نصف ظرفیت. طراحی هدف: دامنه‌ی خرابی کوچک و شناخته‌شده.

### NAT و Session در سری

فقط Edge NAT. Internal بدون NAT ⇒ Log Internal IP واقعی کاربر را دارد؛ Edge IP ترجمه‌شده. اگر NAT دو جا باشد: ردیابی کاربر دشوار و Hairpin/DNS پیچیده.

### مانیتورینگ

| سنجه | دلیل |
|---|---|
| CPU/Memory/Session | ظرفیت |
| وضعیت HA/Heartbeat | افزونگی |
| Policy Hit/Drift | سازگاری |
| Latency بین‌دو FW | سری |
| Sync Status | FGSP |

### Rule Drift

در سری، Policy دو دستگاه باید منطقی هماهنگ باشد (مثلاً DMZ→Internal در Edge Deny و در Internal Allow؟ تناقض). ابزار: ماتریس Policy مشترک، Change هم‌زمان، بازبینی فصلی.

### مثال‌های حل‌شده

#### مثال ساده — انتخاب الگو

ساختمان اداری ۲۰۰ نفر، دو اتصال اینترنت: HA Cluster Active-Passive (ساده‌ترین، بدون Asymmetric).

#### مثال متوسط — سری برای DMZ

Edge: اینترنت↔DMZ؛ Internal: DMZ↔LAN. NAT فقط Edge. Policy ماتریس. اگر Edge خراب: DMZ و اینترنت قطع؛ LAN داخلی ادامه (Failure Domain محدود).

#### مثال متوسط — موازی با ECMP

دو FW پشت دو Router با ECMP. ریسک Asymmetric. راه‌حل: Hash متقارن (`source-dest-ip`) یا FGSP. آزمون: Flow Hash در دو جهت.

#### مثال سخت — دو سازنده سری

Edge FortiGate و Internal دستگاه دیگر. مزیت: آسیب‌پذیری مشترک کمتر. هزینه: دو مهارت، دو لایسنس، Policy متفاوت. توجیه: داده‌ی بسیار حساس.

#### مثال سخت — Drift

Edge اجازه‌ی 443 به DMZ را دارد و Internal 8443؛ برنامه‌ی Web پورت را به 8443 تغییر داد؛ فقط Internal عوض شد ⇒ قطع. درس: Change هر دو و تست End-to-End.

### Lab هدایت‌شده (اجرا نشده)

1. سه الگو را رسم و مقایسه کنید.
2. Failure Domain هر الگو.
3. Drift با ماتریس.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Double NAT | NAT دو جا | فقط Edge |
| Asymmetric | موازی | Hash/Sync |
| Drift | دو Policy | ماتریس |
| ظرفیت | موازی بدون LB | طراحی |

### نکات امنیتی

Policy هر دو دستگاه حداقل؛ Sync لینک ایزوله؛ Log مرکزی با همبستگی دو دستگاه.

### جمع‌بندی

سری برای عمق دفاعی، موازی برای ظرفیت (با Hash/Sync)، Cluster ساده‌ترین دسترس‌پذیری؛ NAT فقط یک‌جا؛ Failure Domain و Drift را مدیریت کنید.

### تمرین و ارزیابی

**ت1.** (ساده) چرا NAT فقط روی یک فایروال؟ *(پاسخ: 23-3-ت1)*

**ت2.** (ساده) Blast radius چیست؟ *(پاسخ: 23-3-ت2)*

**ت3.** (متوسط) تفاوت Canary و تغییر هم‌زمان؟ *(پاسخ: 23-3-ت3)*

**ت4.** (متوسط) Drift Policy را چگونه کشف می‌کنید؟ *(پاسخ: 23-3-ت4)*

**ت5.** (سخت) Active-Active: ۴ الزام برای عملکرد صحیح. *(پاسخ: 23-3-ت5)*

**ت6.** (سخت، طراحی) الگوی مناسب برای ظرفیت ۳۰ Gbps با Defense in Depth. *(پاسخ: 23-3-ت6)*

**Q1.** Quick quiz (English): What is the main benefit of a canary change on multi-firewall designs? *(پاسخ: 23-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Canary | Canary change | تغییر آزمایشی روی بخش کوچک |
| Blast radius | Blast radius | دامنه‌ی اثر |
| Drift | Configuration drift | انحراف پیکربندی |

- *Test changes on one firewall before rolling out.* ← تغییرات را ابتدا روی یک فایروال آزمایش کنید.

### کارت Lab

**کارت Lab:** سری/موازی. **Evidence:** `02-design/multi-fw.md`.

### منابع

- NIST SP 800-41
- Google SRE Book (Canarying)

<a id="l-23-4"></a>

## درس 23-4 — آزمون معماری ۵: چندفایروالی و مسیر نامتقارن — صورت مسئله، کلید پاسخ و Rubric

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۱ تا ۲۳-۳، ۱۰-۶ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری چندفایروالی و مسیر نامتقارن را طراحی و تشخیص دهید.
2. سه عیب تزریق‌شده را با Evidence رفع کنید.
3. گزینه‌ی صحیح (متقارن‌سازی/SNAT/Session Sync) را توجیه کنید.
4. RCA و ریسک گزینه‌ها را بنویسید.
5. Rubric را اجرا کنید.
6. صداقت را ثبت کنید.

### چرا باید یاد بگیریم؟

مشتریان معمولاً نمی‌گویند «Asymmetric»؛ می‌گویند «بعضی اتصال‌ها گاهی قطع می‌شود». شما باید نشانه‌ها را به معماری تبدیل کنید. این Gate سنجش همین مهارت است: دیدن علت در چند فایروال و چند مسیر و پیشنهاد راه‌حل ایمن.

### صورت مسئله

سازمان: دو Edge Firewall (E1، E2) موازی با دو ISP؛ پشت آن‌ها Core Switch. ترافیک با ECMP توزیع می‌شود. شکایت: «حدود ۳۰٪ اتصال‌های HTTPS به سایت‌های خارجی Timeout می‌شوند؛ DNS و ping مشکلی ندارند».

عیب‌های تزریق‌شده:

1. ECMP با Hash مبتنی بر مبدأ فقط؛ Return از Edge دیگر.
2. `asymroute` فعال شده توسط تیم قبلی بدون مستند.
3. SNAT با IP ISP1 روی لینک ISP2.

### کلید پاسخ — تشخیص

1. Sniffer E1 و E2 هم‌زمان: SYN در E1، SYN-ACK در E2.
2. Debug Flow E2: `no session matched`.
3. Session E1: `SYN_SENT`.
4. `show system settings | grep asymroute` ⇒ enable.
5. Session NAT: `act=snat ... (203.0.113.2)` روی `port2` (ISP2).

### کلید پاسخ — رفع

**عیب ۱ (Hash):**

1. علت: Hash فقط مبدأ؛ برگشت Hash دیگر.
2. رفع: `set v4-ecmp-mode source-dest-ip-based` و Policy Route برای ثبات؛ یا Session Sync (FGSP).
3. تأیید: Sniffer: SYN و SYN-ACK روی همان Edge.

**عیب ۲ (`asymroute`):**

1. علت: راه‌حل موقت قدیمی که مشکل را پنهان کرده و RPF را ضعیف.
2. رفع: غیرفعال‌سازی پس از اصلاح تقارن؛ ثبت.
3. تأیید: آزمون Spoofing/RPF در Lab.

**عیب ۳ (SNAT):**

1. علت: IP ISP1 روی لینک ISP2.
2. رفع: Pool هر لینک با IP همان ISP.
3. تأیید: Session `snat` با IP درست؛ پاسخ از لینک درست.

### مقایسه‌ی راه‌حل‌ها

| گزینه | امنیت | عملی بودن | تصمیم |
|---|---|---|---|
| Hash متقارن + SNAT | بالا | ساده | انتخاب نهایی |
| FGSP | بالا | پیچیده | آینده |
| asymroute | پایین | ساده | حذف |

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| تشخیص با Evidence | 25 |
| رفع سه عیب | 30 |
| توجیه راه‌حل و ریسک | 20 |
| آزمون و تأیید | 15 |
| RCA/صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Sniffer

``` text
E1: port1 out SYN to 198.51.100.8
E2: port1 in  SYN-ACK from 198.51.100.8
```

نشانه‌ی کلاسیک.

#### مثال متوسط — RCA

``` text
Impact  : ~30% HTTPS timeouts for 3 weeks
Cause   : ECMP source-only hash + SNAT IP mismatch + asymroute masking
Fix     : symmetric hash, per-link SNAT pool, asymroute disable
Prevent : change checklist for dual-ISP; Sniffer on both Edges in acceptance test
```

#### مثال متوسط — آزمون پذیرش

۵۰ اتصال متوالی با `curl`؛ همه باید موفق (۱۰۰٪). قبل از رفع ۷۰٪؛ پس از رفع ۱۰۰٪.

#### مثال سخت — سه عیب هم‌زمان

ترتیب: ابتدا SNAT (سطح پایین)، سپس Hash، سپس `asymroute` را در پایان خاموش کنید (تا پوشش مشکل برداشته نشود پیش از رفع). ثبت هر مرحله.

#### مثال سخت — صداقت

Lab اجرا نشده؛ درصدها نمونه‌ی آموزشی؛ گزارش «Unverified».

### Lab هدایت‌شده (اجرا نشده)

1. سناریو را بسازید.
2. سه عیب را رفع کنید.
3. آزمون پذیرش.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| ۳۰٪ Timeout | Hash/SNAT | متقارن |
| asymroute روشن | راه‌حل موقت | خاموش |
| IP نادرست | Pool | اصلاح |

### جمع‌بندی

Gate معماری ۵: تشخیص Asymmetric با Sniffer دو Edge و Debug، رفع سه‌گانه (Hash، asymroute، SNAT)، مقایسه‌ی راه‌حل‌ها، RCA و صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Source-based؟ *(پاسخ: 23-4-ت1)*

**ت2.** (ساده) BFD چه می‌کند؟ *(پاسخ: 23-4-ت2)*

**ت3.** (متوسط) علت قطع Session پس از Failover؟ *(پاسخ: 23-4-ت3)*

**ت4.** (متوسط) SNAT دوم چه ریسکی دارد؟ *(پاسخ: 23-4-ت4)*

**ت5.** (سخت) Capture دو سمتی. *(پاسخ: 23-4-ت5)*

**ت6.** (سخت، طراحی) سه‌فایروالی. *(پاسخ: 23-4-ت6)*

**Q1.** Quick quiz (English): How can you prove asymmetric routing with captures? *(پاسخ: 23-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| BFD | Bidirectional Forwarding Detection | تشخیص دوطرفه |

- *Keep each session on one firewall.* ← هر Session را روی یک فایروال نگه دارید.

### کارت Lab

**کارت Lab:** معماری ۵ (اجرا نشده). **Evidence:** `03-ops/arch5.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Routing; Session

## پاسخ‌های فصل 23

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 23-1

**23-1-ت1** — روتر فقط بر پایه‌ی مقصد هر بسته تصمیم می‌گیرد؛ فایروال Stateful تصمیم را به Session وابسته می‌کند که فقط روی دستگاه اول ساخته شده.

**23-1-ت2** — `reverse path check fail, drop` و `Denied by forward policy check (policy 0)`.

**23-1-ت3** — Hash رفت و برگشت متفاوت؛ نیمی از Flowها هر دو جهت را از یک فایروال می‌بینند و نیمی نه. رفع: Hash متقارن (هر دو جهت یکسان)، یا Active-Passive، یا Session Sync.

**23-1-ت4** — ترجمه‌ی مبدأ فقط در Session فایروال اول ثبت شده؛ فایروال دوم نمی‌تواند پاسخ را به آدرس واقعی ترجمه کند.

**23-1-ت5** — VPN+Internet نامتقارن؛ دو علت و تفکیک

**علامت:** گاهی ترافیک VPN و اینترنت هم‌زمان مشکل دارد.

**فرضیه ۱:** Policy Route/ECMP متفاوت برای دو جهت ⇒ آزمون: Sniffer دو فایروال هم‌زمان؛ SYN و SYN-ACK کجا؟
**فرضیه ۲:** SNAT با IP اشتباه روی لینک دیگر ⇒ آزمون: `session list` برای `act=snat` و IP.
**فرضیه ۳:** Route برگشت Tunnel ناقص ⇒ `get router info routing-table details` به مقصد/مبدأ.

**روش تفکیک:** آزمونی را اول بزنید که چند فرضیه را رد کند؛ فقط یک متغیر را هر بار تغییر دهید؛ علت وقتی اثبات می‌شود که تغییر آن علامت را برطرف و بازگرداندنش علامت را برگرداند.

**23-1-ت6** — چه موقع Asymmetric پذیرفته می‌شود؟

**استدلال:** Asymmetric ذاتاً «خطا» نیست؛ مشکل برای Stateful Inspection است. می‌توان آن را پذیرفت وقتی:
1. Session Sync یا ساختار Stateless/نیمه‌حالت (Anycast، Scrubbing) آن را مدیریت می‌کند؛
2. کنترل جایگزین (Inspection جای دیگر، ACL Stateless) ریسک را جبران می‌کند؛
3. ریسک امنیتی (Spoofing/بی‌حالتی) صراحتاً ارزیابی، مستند و امضا شده؛
4. آزمون و پایش وجود دارد.

**چه موقع نمی‌پذیریم؟** برای ترافیک نیازمند UTM/NAT حالت‌دار یا ممیزی سخت.

**23-1-Q1** — Reverse path check failure and the absence of a matching session or policy for the return packet.


### پاسخ‌های بازنویسی عمیق درس 23-2

**23-2-ت1** — مسیر را بر اساس مبدأ/Interface ورودی/سرویس تعیین می‌کند، قبل از Routing Table.

**23-2-ت2** — چون آدرس مبدأ ترجمه‌شده متعلق به همان لینک است و Upstream پاسخ را به همان مسیر می‌دهد.

**23-2-ت3** — متقارن‌سازی (ریشه‌ای)، Session Sync/Active-Passive، Policy Route/SNAT، `asymroute` (آخرین).

**23-2-ت4** — آدرس واقعی مبدأ در سرور پنهان می‌شود و تحلیل حادثه سخت‌تر می‌شود.

**23-2-ت5** — دو فایروال Active-Active با ECMP؛ انتخاب طرح

**گزینه‌ها:** (الف) Hash متقارن + SNAT هر لینک، (ب) FGSP، (ج) HA Active-Passive.

**استدلال:** اگر ظرفیت یک دستگاه کافی است (ج) ساده‌ترین و ایمن‌ترین است. اگر ظرفیت دو دستگاه لازم است، (الف) هزینه‌ی کمتر ولی وابسته به رفتار تجهیز بالادست؛ (ب) State را همگام می‌کند و تحمل بیشتر دارد ولی پیچیده‌تر است.

**توصیه با فرض ظرفیت بیش از یک دستگاه و ISP دوگانه:** (الف) با SNAT/Pool هر لینک + آزمون پذیرش؛ (ب) برای آینده. دلیل: بدون وابستگی به Sync UTM و با ردیابی قابل‌قبول.

**23-2-ت6** — آزمون پذیرش پس از رفع Asymmetric

1. ۲۰ (یا ۵۰) اتصال متوالی از چند Source، همه باید موفق باشند.
2. Sniffer روی هر دو فایروال: SYN/SYN-ACK روی همان دستگاه.
3. `session list`: Session فقط در یک فایروال برای هر Flow.
4. Log کامل بدون `reverse path check fail`.
5. آزمون منفی: RPF فعال و Spoofing شبیه‌سازی‌شده ⇒ Drop.
6. آزمون خرابی: قطع یک مسیر ⇒ Flowهای جدید سالم.

**چرا همه‌ی این‌ها؟** فقط موفقیت اتصال ممکن است اتفاقی باشد؛ Sniffer و Session علت و تقارن را اثبات می‌کنند.

**23-2-Q1** — Because disabling checks weakens security, while symmetric routing solves the root cause.


### پاسخ‌های بازنویسی عمیق درس 23-3

**23-3-ت1** — Log و عیب‌یابی ساده می‌ماند و آدرس واقعی حفظ می‌شود.

NAT فقط روی Edge: Log و عیب‌یابی ساده می‌ماند و IP واقعی کاربر در Internal حفظ می‌شود.

**23-3-ت2** — دامنه‌ی اثر یک خطا/خرابی.

Blast radius دامنه‌ی اثر یک خطا یا خرابی است؛ جداسازی آن را کم می‌کند.

**23-3-ت3** — Canary ابتدا روی یک دستگاه؛ اگر سالم بود ادامه؛ تغییر هم‌زمان خطا را همه‌جا ایجاد می‌کند.

**23-3-ت4** — Diff پیکربندی دو فایروال پس از هر تغییر و به‌صورت دوره‌ای؛ Alert.

**23-3-ت5** — چهار الزام Active-Active

1. **Session Sync یا Hash متقارن** تا رفت و برگشت یک دستگاه.
2. **همسانی Config و نسخه** (Sync یا مدیریت مرکزی).
3. **ظرفیت N+1:** هر دستگاه باید بار کل را در خرابی تحمل کند؛ وگرنه Active-Active افزونگی واقعی نیست.
4. **پایش و آزمون:** Health-check، Failover، Drift.

**استدلال:** بدون ۱ Asymmetric؛ بدون ۲ رفتار متفاوت؛ بدون ۳ خرابی یک دستگاه اوج بار را قطع می‌کند؛ بدون ۴ مشکلات پنهان می‌مانند.

**23-3-ت6** — الگو برای ۳۰ Gbps با Defense in Depth

**فرض:** هیچ دستگاه تنها ۳۰ Gbps با UTM/Inspection نمی‌دهد (از Datasheet بررسی شود).

**الگو:** Edge موازی N+1 با ECMP/Hash متقارن برای ظرفیت (مثلاً ۳ دستگاه که هرکدام ≥ ۱۵ Gbps در شرایط واقعی) + لایه‌ی Internal سری با HA برای عمق دفاعی؛ NAT فقط Edge.

**معیارها:** ظرفیت واقعی با Inspection (نه ظرفیت Firewall خام)، ریسک Asymmetric، هزینه، پیچیدگی عملیاتی. عدد ۳۰ Gbps را با اندازه‌گیری/ Datasheet مدل تأیید کنید.

**23-3-Q1** — It limits the blast radius by testing the change on one device before applying it everywhere.


### پاسخ‌های بازنویسی عمیق درس 23-4


### پاسخ‌های بازنویسی عمیق درس 23-4

**23-4-ت1** — تا هر Session روی یک فایروال بماند.

Source-based تا هر Session روی یک فایروال بماند و Asymmetric نشود.

**23-4-ت2** — تشخیص سریع خرابی مسیر.

BFD خرابی مسیر را در حد ثانیه (یا کمتر) تشخیص می‌دهد؛ OSPF به‌تنهایی کندتر است.

**23-4-ت3** — Sync نیست.

پس از Failover Sessionها ریست می‌شوند چون فایروال‌ها Cluster نیستند و Session sync ندارند.

**23-4-ت4** — لیست مجاز مقصد.

SNAT دوم با IP متفاوت ریسک دارد: لیست مجاز مقصد باید هر دو IP را بپذیرد.

**23-4-ت5** — Capture دو سمتی

1. Capture هم‌زمان روی هر دو فایروال با فیلتر Host/Port یکسان و ساعت NTP همگام.
2. مقایسه‌ی جهت‌ها: SYN روی دستگاه A و SYN-ACK روی B یعنی Asymmetric.
3. Session list هر دو.
4. نتیجه‌گیری فقط وقتی که زمان‌ها همخوان باشند (اختلاف ساعت تفسیر را خراب می‌کند).

**23-4-ت6** — طرح سه‌فایروالی

طرح نمونه (قابل نقد): دو Edge موازی (ECMP متقارن + SNAT هر لینک) و یک Internal HA. جدول: نقش، مسیر رفت/برگشت، Failover (قطع یک Edge ⇒ نصف ظرفیت)، آزمون Asymmetric (Sniffer دو Edge).
**استدلال:** افزودن دستگاه بدون طراحی تقارن ریسک را بالا می‌برد؛ سه دستگاه فقط وقتی ارزش دارد که ظرفیت یا دسترس‌پذیری واقعاً لازم باشد.

**23-4-Q1** — By capturing on both firewalls and showing each sees only one direction.

### پاسخ‌های درس افزوده‌ی 23-0 (فصل 23)

**23-0-ت1** — رفت و برگشت یک ارتباط از دو مسیر/دستگاه متفاوت.

Asymmetric: رفت و برگشت یک ارتباط از دو مسیر/دستگاه متفاوت.

**23-0-ت2** — چون برگشتی بدون Session مطابق Handshake نیست (و/یا RPF fail) و رد می‌شود.

**23-0-ت3** — پیام reverse path check fail, drop.

پیام Debug flow: `reverse path check fail, drop` در ترافیک نامتقارن.

**23-0-ت4** — مقایسه‌ی سه راه‌حل Asymmetric

| راه‌حل | چه چیزی را درست می‌کند | ریسک/هزینه |
|---|---|---|
| طراحی متقارن | علت ریشه | نیاز به تغییر طراحی؛ کم‌ریسک امنیتی |
| Policy Route/SNAT | اجبار برگشت از همان مسیر | Log/ردیابی کاربر مبهم (SNAT)، وابسته به مقصد |
| Session Sync (FGSP/HA) | Session روی هر دو دستگاه | پیچیدگی، همگام‌سازی ناقص UTM |
| غیرفعال‌کردن کنترل‌ها | علامت را پنهان می‌کند | بالاترین ریسک امنیتی |

**انتخاب:** ابتدا علت ریشه؛ سپس راه‌حل‌هایی که State را حفظ می‌کنند؛ پذیرش بدون کنترل فقط موقت و مستند.

**23-0-ت5** — متقارن‌سازی دو فایروال موازی با ECMP

**فرض:** دو فایروال Active-Active پشت ECMP.

1. **Hash دوطرفه:** تنظیم ECMP/LB طوری که Flow در دو جهت یک دستگاه را انتخاب کند (مثلاً Hash بر اساس src+dst قرینه). فرض: تجهیز بالادست و پایین‌دست هر دو همین الگو را اجرا کنند.
2. **یا Active-Passive:** بدون Asymmetric ولی ظرفیت کمتر.
3. **یا Session Sync** (FGSP) تا هر دستگاه Session دارد.

**آزمون:** ۵۰ اتصال و Sniffer روی هر دو؛ SYN و SYN-ACK باید روی همان فایروال باشند.

**محدودیت:** Hash متقارن با NAT (تغییر IP) یا Failover ممکن است بر هم بخورد؛ آن را آزمون کنید.

**23-0-Q1** — Sniffer shows SYN on one firewall and SYN/ACK on another, and the session exists only on the first.

# فصل 24 — معماری Data Center و Segmentation (G9)

> **یادداشت علمی v4.0 — فصل 24:** عمومی: Segmentation، East-West. مختص محصول: VDOM/Zone.
> فرض: Lab/طراحی؛ لایسنس VDOM وابسته به مدل.
> مرجع: Fortinet Docs.


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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا VDOM؟** ساختمان چندواحدی را تصور کنید: برق و آسانسور مشترک، هر واحد قفل و دیوار خودش. VDOM (Virtual Domain) یک FortiGate را چند فایروال مجازی می‌کند؛ هر کدام Route، Policy، Interface و ادمین جدا دارند. مشتریان MSSP، دیتاسنترهای چندمستأجره و جداسازی بخش‌های حساس همین نیاز را دارند.

**دو سطح:** Global (سخت‌افزار، نسخه، HA، ادمین‌های سراسری، محدودیت منابع) و VDOM (Policy، Routing، VPN، UTM). ترافیک بین VDOMها فقط از **Inter-VDOM Link** با Policy دو سر می‌گذرد؛ چیزی خودبه‌خود جاری نمی‌شود. **لایسنس:** تعداد VDOM اضافه بر پیش‌فرض Needs-License.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — ساخت

``` text
config system settings
 set vdom-mode multi-vdom
end
config vdom
 edit TENANT-A
 next
 edit TENANT-B
 next
end
```

هشدار: تغییر حالت Config را متأثر می‌کند؛ Backup قبل از آن.

#### مثال متوسط — سهم منابع

``` text
Per-tenant cap = capacity / tenants = 200000 / 4 = 50000 sessions
```

#### مثال سخت — Inter-VDOM Link

``` text
config global
 config system vdom-link
  edit "A-B"
  next
 end
end
```

در هر VDOM یک Interface (`A-B0`، `A-B1`)، IP /30، Route و Policy؛ بدون Policy ping جواب نمی‌دهد (ایزولاسیون پیش‌فرض).

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: VDOM — سناریوی چند‌مستاجر

``` text
config vdom
 edit TENANT-A
next
end
config global
 config system vdom-link
  edit "A-LINK"
  next
 end
end
```

منابع: `config global; config system resource-limit` برای Session/Policy هر VDOM. Inter-VDOM Link ترافیک را بین مستاجران عبور می‌دهد با Policy.

**VDOM = Needs-License** برای تعداد بیش از پیش‌فرض (طبق مدل).

**پرسش‌های مصاحبه**
1. *Management VDOM؟* root.
2. *ایزوله کامل؟* جداول Route/Policy جدا.
3. *محدودیت منابع؟* resource-limit.

### تکمیل عمیق: VDOM — یک فایروال، چند فایروال مجازی

#### چرا باید یاد بگیریم؟

یک ساختمان اداری را تصور کنید که چند شرکت مستأجر دارد. همه از یک ورودی و آسانسور مشترک استفاده می‌کنند، ولی هر شرکت قفل، کلید و فضای خودش را دارد. VDOM (Virtual Domain، یعنی «دامنه‌ی مجازی») همین کار را با یک FortiGate می‌کند: هر VDOM جدول مسیر، Policy، Interface و ادمین جدا دارد. مشتریان MSSP، دیتاسنترهای چندمستأجره و جداسازی بخش‌های حساس همین نیاز را دارند.

#### توضیح ساده

دو سطح وجود دارد:

- **Global**: منابع مشترک (سخت‌افزار، نسخه، HA، Log سراسری).
- **VDOM**: هر مستأجر (Interface، Route، Policy، VPN).

یک VDOM ویژه به نام `root` معمولاً برای مدیریت استفاده می‌شود. ترافیک بین دو VDOM باید از **Inter-VDOM Link** عبور کند و Policy بخواهد؛ چیزی به‌صورت خودکار بین آنها جاری نمی‌شود.

#### مثال ساده — ساخت دو VDOM

``` text
config system settings
 set vdom-mode multi-vdom
end
config vdom
 edit TENANT-A
 next
 edit TENANT-B
 next
end
```

هشدار: تغییر به Multi-VDOM ساختار Config را تغییر می‌دهد؛ در Lab و پس از Backup انجام دهید. لایسنس: مدل‌ها تعداد VDOM پیش‌فرض دارند (معمولاً ۱۰)؛ بیش از آن Needs-License.

#### مثال متوسط — Inter-VDOM Link

``` text
config global
 config system vdom-link
  edit "A-B"
  next
 end
end
```

در هر VDOM یک Interface به نام `A-B0` و `A-B1` ساخته می‌شود؛ هرکدام را IP بدهید و Policy بنویسید.

#### مثال سخت — مدیریت منابع

``` text
config global
 config system vdom-property
  edit TENANT-A
   set session 50000
   set policy 500
  next
 end
end
```

محدودکردن Session باعث می‌شود یک مستأجر پرترافیک، منابع بقیه را نخورد. محاسبه: اگر ظرفیت ۲۰۰,۰۰۰ Session و ۴ مستأجر، سقف ۵۰,۰۰۰ برای هرکدام.

``` text
Per-tenant cap = capacity / tenants = 200000 / 4 = 50000
```

#### Lab

دو VDOM با Interface جدا بسازید، یک Inter-VDOM Link و یک Policy، و آزمون کنید که بدون Policy ارتباط برقرار نمی‌شود.

#### عیب‌یابی

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| ارتباط بین VDOM نیست | Policy/Route | Policy دو سر |
| ادمین Tenant همه را می‌بیند | Profile | `vdom` محدود |
| Session پر می‌شود | سقف نیست | vdom-property |

#### پرسش‌ها با پاسخ

**۱. VDOM چه چیزی را جدا می‌کند؟** Route، Policy، Interface، ادمین.
**۲. چرا Inter-VDOM Policy؟** ایزوله‌سازی پیش‌فرض.
**۳. محدودیت منابع چرا؟** جلوگیری از اثر همسایه‌ی پرمصرف.

#### English Corner

- *Each VDOM has its own routing table and policy set.*
- Q: What prevents one tenant from exhausting the device's sessions?

## درس 24-1 — East-West و Segmentation: Zone، Trust Level، Flow Discovery و Policy Matrix

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۱۱-۲، ۱۵-۴ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. East-West و North-South را تعریف و تفاوت ریسکشان را بگویید.
2. Segmentation را با Zone و Trust Level طراحی کنید.
3. Flow Discovery (کشف جریان‌های واقعی) را با Log انجام دهید.
4. ماتریس Policy مبتنی بر Trust Level بسازید.
5. Micro-segmentation را از Macro تمایز دهید.
6. اثر Lateral Movement را با و بدون Segmentation مقایسه کنید.

### چرا باید یاد بگیریم؟

مهاجمان معمولاً از در اصلی (North-South) وارد می‌شوند ولی خسارت اصلی در «حرکت جانبی» داخل شبکه (East-West) است. شبکه‌ی تخت (Flat) مثل ساختمانی است که یک بار از در رد شوید، به همه‌ی اتاق‌ها دسترسی دارید. Segmentation اتاق‌ها را قفل می‌کند. تجربه‌ی حوادث باج‌افزار نشان می‌دهد شبکه‌های Flat در ساعات به‌جای روزها آلوده می‌شوند.

### تعریف‌ها

| اصطلاح | معنی |
|---|---|
| North-South | ترافیک ورود/خروج Data Center یا شبکه |
| East-West | ترافیک بین سرورها/Zoneهای داخلی |
| Lateral Movement | حرکت مهاجم بین سیستم‌ها |
| Segmentation | تقسیم شبکه به بخش‌های قابل‌کنترل |
| Micro-segmentation | Policy تا سطح هر Workload |

### Trust Level

``` text
Level 0 Internet / Untrusted
Level 1 DMZ
Level 2 Users
Level 3 Servers (App)
Level 4 Data (DB, Secrets)
Level 5 Management
```

قاعده: ترافیک از سطح پایین‌تر به بالاتر باید با Policy صریح و حداقلی باشد؛ از اعتماد بالا به پایین هم بی‌حساب نیست (Outbound Control).

### Zone و ماتریس

``` text
config system zone
    edit "ZN-WEB"
        set interface "port5"
        set intrazone deny
    next
    edit "ZN-APP"
        set interface "port6"
        set intrazone deny
    next
    edit "ZN-DB"
        set interface "port7"
        set intrazone deny
    next
end
```

| از ↓ به → | WEB | APP | DB | MGMT |
|---|---|---|---|---|
| Internet | 443 | - | - | - |
| WEB | - | 8443 | - | - |
| APP | - | - | 1433 | - |
| DB | - | - | - | - |
| MGMT | SSH | SSH | SSH | - |

### Flow Discovery

قبل از نوشتن Policy حداقلی باید جریان‌های واقعی را بشناسید:

1. Policy موقت «Allow + Log» برای مشاهده (فقط در پنجره‌ی مشخص).
2. Log را تحلیل: Src، Dst، Port، حجم.
3. فهرست جریان‌های ضروری.
4. Policy حداقلی ⇒ حذف Policy موقت.

``` text
execute log filter category 0
execute log filter field srcintf port5
execute log display
```

ابزار: FortiAnalyzer/Fabric، یا Export و تحلیل با اسکریپت.

### مثال‌های حل‌شده

#### مثال ساده — ماتریس

Web فقط به App:8443؛ App فقط به DB:1433؛ DB به هیچ‌جا Outbound ندارد. هر Deny Log می‌شود.

#### مثال متوسط — Flow Discovery

یک هفته Log: Web→App 8443 (OK)، Web→DB 1433 (!). فهرست نشان داد یک اسکریپت قدیمی مستقیم به DB وصل می‌شد. تصمیم: اسکریپت اصلاح؛ سپس Policy Web→DB حذف.

``` text
Flow count by (src,dst,port):
 web01 -> app01:8443   120000
 web01 -> db01:1433         14   <- review
```

#### مثال متوسط — Trust Level

Users (Level 2) به DB (Level 4) مستقیم؟ ممنوع. کاربر از طریق App. Admin از MGMT با Bastion.

#### مثال سخت — Lateral Movement

وب‌سرور آلوده؛ مهاجم اسکن 10.30.0.0/24. در شبکه‌ی Flat: ۵۰ سرور پاسخ می‌دهند و SMB/RDP باز است ⇒ باج‌افزار. با Segmentation: فقط 8443 به App مجاز؛ اسکن Drop و Log. زمان تشخیص از روزها به دقیقه (آلارم Deny).

``` text
Without segmentation: reachable targets = 50 hosts x many ports
With segmentation   : reachable targets = 1 host x 1 port
Reduction           = 1 / (50 x many) -> orders of magnitude
```

#### مثال سخت — Micro-segmentation

حتی در یک Zone (مثلاً ZN-APP) سرورها نباید به هم Allow باشند (`intrazone deny`)؛ ارتباط‌ها با Policy. ابزار: Address Group جدا، یا Security Group در ابر. هزینه: مدیریت بیشتر. توصیه: از Macro شروع، سپس Micro برای داده‌ی حساس.

### Lab هدایت‌شده (اجرا نشده)

1. Zoneها و ماتریس.
2. Flow Discovery با Log.
3. آزمون اسکن و Deny.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Policy باز | Allow قدیمی | Discovery/حذف |
| برنامه نمی‌رسد | جریان جا افتاد | Log Deny |
| intrazone | Policy نیست | صریح |
| Log حجیم | همه‌چیز Log | فیلتر |

### نکات امنیتی

Default Deny؛ Log Deny؛ Alert روی Deny غیرعادی؛ Policy موقت با انقضا.

### جمع‌بندی

East-West خطر اصلی؛ Trust Level + Zone + intrazone deny؛ Flow Discovery قبل از Policy حداقلی؛ Micro-segmentation برای داده‌ی حساس.

### تمرین و ارزیابی

**ت1.** (ساده) East-West چیست؟ *(پاسخ: 24-1-ت1)*

**ت2.** (ساده) چرا Flow Discovery؟ *(پاسخ: 24-1-ت2)*

**ت3.** (متوسط) چرا Rollout مرحله‌ای؟ *(پاسخ: 24-1-ت3)*

**ت4.** (متوسط) WEB→DB مشکوک؟ *(پاسخ: 24-1-ت4)*

**ت5.** (سخت) Backup شبانه قطع شد. *(پاسخ: 24-1-ت5)*

**ت6.** (سخت، طراحی) Matrix DC. *(پاسخ: 24-1-ت6)*

**Q1.** Quick quiz (English): Why is east-west traffic a major risk in data centers? *(پاسخ: 24-1-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Lateral movement | Lateral movement | حرکت جانبی |

- *Discover flows before enforcing policies.* ← قبل از اعمال Policy جریان‌ها را کشف کنید.

### کارت Lab

**کارت Lab:** Segmentation (اجرا نشده). **Evidence:** `02-design/dc-matrix.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- NIST SP 800-125B

<a id="l-24-2"></a>

## درس 24-2 — Policy حداقلی Web/App/DB: ماتریس، پیاده‌سازی و آزمون Isolation

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۱، ۱۵-۴ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. ماتریس Policy سه‌لایه‌ی Web/App/DB را بنویسید.
2. Policyهای حداقلی را (سرویس‌های مشخص، Address Object، Log) پیاده کنید.
3. آزمون Isolation (مثبت و منفی) را اجرا کنید.
4. با `iprope lookup` و Log اثبات کنید.
5. Outbound سرورها را کنترل کنید.
6. مستندسازی Policy (Comment/Owner) را رعایت کنید.

### چرا باید یاد بگیریم؟

«Policy حداقلی» یعنی هر قانون فقط همان چیزی را اجازه دهد که لازم است؛ نه یک پورت بیشتر. ولی ساختن Policy حداقلی بدون آزمون منفی مثل نصب قفل بدون امتحان است: نمی‌دانید واقعاً بسته است. این درس نوشتن و اثبات را با هم آموزش می‌دهد.

### ماتریس

| # | از | به | سرویس | اجازه |
|---|---|---|---|---|
| 1 | Internet | WEB (VIP) | HTTPS 443 | بله |
| 2 | WEB | APP | TCP 8443 | بله |
| 3 | APP | DB | TCP 1433 | بله |
| 4 | MGMT | WEB/APP/DB | SSH 22 | بله |
| 5 | WEB | DB | هر | خیر |
| 6 | DB | Internet | هر | خیر |
| 7 | APP | Internet | HTTPS (Update) | محدود (FQDN) |

### پیاده‌سازی

``` text
config firewall address
    edit "HOST-WEB01"
        set subnet 10.30.0.10 255.255.255.255
    next
    edit "HOST-APP01"
        set subnet 10.20.0.30 255.255.255.255
    next
    edit "HOST-DB01"
        set subnet 10.20.0.40 255.255.255.255
    next
end
config firewall service custom
    edit "TCP-8443"
        set tcp-portrange 8443
    next
    edit "TCP-1433"
        set tcp-portrange 1433
    next
end
config firewall policy
    edit 301
        set name "WEB-to-APP-8443"
        set srcintf "ZN-WEB"
        set dstintf "ZN-APP"
        set srcaddr "HOST-WEB01"
        set dstaddr "HOST-APP01"
        set service "TCP-8443"
        set action accept
        set schedule "always"
        set logtraffic all
        set comments "owner=AppTeam; ticket=CHG-501; review=2026-Q4"
    next
    edit 302
        set name "APP-to-DB-1433"
        set srcintf "ZN-APP"
        set dstintf "ZN-DB"
        set srcaddr "HOST-APP01"
        set dstaddr "HOST-DB01"
        set service "TCP-1433"
        set action accept
        set schedule "always"
        set logtraffic all
        set comments "owner=DBTeam; ticket=CHG-502; review=2026-Q4"
    next
end
```

نکته‌ها: Address دقیق (نه subnet)، Service دقیق (نه ALL)، `comments` مالک و تیکت، `logtraffic all` برای اثبات.

### آزمون Isolation

``` text
# positive
diagnose firewall iprope lookup 10.30.0.10 40000 10.20.0.30 8443 tcp port5
# negative
diagnose firewall iprope lookup 10.30.0.10 40000 10.20.0.40 1433 tcp port5
diagnose firewall iprope lookup 10.20.0.40 40000 8.8.8.8 443 tcp port7
```

انتظار: مثبت ⇒ policy 301؛ دو منفی ⇒ policy 0 (Deny). سپس آزمون واقعی از میزبان‌ها: `nc -vz 10.20.0.40 1433` از Web ⇒ Timeout؛ و Log Deny.

### Outbound سرورها

DB: بدون Outbound. APP: فقط FQDN مجاز Update (Address FQDN) با HTTPS. WEB: فقط به APP و پاسخ.

### مثال‌های حل‌شده

#### مثال ساده — مثبت

Lookup Web→App:8443 ⇒ policy 301. `nc -vz 10.20.0.30 8443` از Web ⇒ Connected.

#### مثال متوسط — منفی

Web→DB:1433: Lookup ⇒ policy 0؛ `nc` ⇒ Timeout؛ Log: `action=deny policyid=0` (Implicit Deny) با `logtraffic` پیش‌فرض Deny (حتماً فعال).

``` text
config log setting
    set fwpolicy-implicit-log enable
end
```

#### مثال متوسط — ترتیب

Policy قدیمی «ZN-WEB → ZN-APP ALL» بالاتر از 301 ⇒ Isolation نقض. Hit Count قدیمی را دیدید؛ حذف/Disable و آزمون دوباره.

#### مثال سخت — Outbound DB

DB به اینترنت برای Update باز بود. ممیزی: آزمون منفی DB→Internet شکست (مجاز بود). رفع: Policy حذف؛ Update از Repository داخلی. حادثه‌ی نمونه: DB آلوده Exfiltration.

#### مثال سخت — Isolation در ابر هیبرید

DB روی VLAN دوم با ESXi. Isolation فقط در FortiGate کافی نیست؛ vSwitch/Port Group هم باید جدا باشد. آزمون از VM همسایه در همان Hypervisor. درس: Isolation یک زنجیره است.

### Lab هدایت‌شده (اجرا نشده)

1. سه Policy و Address/Service.
2. آزمون مثبت و دو منفی.
3. Implicit Deny Log.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| منفی مجاز | Policy قدیمی | ترتیب |
| مثبت رد | Service/Interface | Lookup |
| Log نیست | implicit log | فعال |
| DB Outbound | Policy | حذف |

### نکات امنیتی

Policy هر Workload با Owner؛ بازبینی فصلی؛ Alert Deny؛ بدون ALL.

### جمع‌بندی

Policy حداقلی (Address/Service دقیق، Owner، Log)، آزمون مثبت+منفی با Lookup و آزمون واقعی، Outbound کنترل‌شده، Isolation زنجیره‌ای (شبکه + Hypervisor).

### تمرین و ارزیابی

**ت1.** (ساده) چرا Object Host-level؟ *(پاسخ: 24-2-ت1)*

**ت2.** (ساده) Deny صریح؟ *(پاسخ: 24-2-ت2)*

**ت3.** (متوسط) آزمون منفی؟ *(پاسخ: 24-2-ت3)*

**ت4.** (متوسط) Lookup؟ *(پاسخ: 24-2-ت4)*

**ت5.** (سخت) Hit Count ۱۲؟ *(پاسخ: 24-2-ت5)*

**ت6.** (سخت، طراحی) Policy سه‌لایه. *(پاسخ: 24-2-ت6)*

**Q1.** Quick quiz (English): Why use host-level address objects between tiers? *(پاسخ: 24-2-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Least privilege | Least privilege | حداقل دسترسی |

- *Test the denied flows too.* ← جریان‌های ردشده را هم آزمون کنید.

### کارت Lab

**کارت Lab:** Policy سه‌لایه (اجرا نشده). **Evidence:** `02-design/dc-policy.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies

<a id="l-24-3"></a>

### ضمیمه: پرونده‌ی کامل حل‌شده — «Policy Deny بین Web و DB اثر ندارد»

**ورودی:** Policy 61 (DENY-WEB-to-DB) ساخته شده ولی telnet از WEB به DB:1433 موفق است.

**گام ۱ — Lookup:**

``` text
diagnose firewall iprope lookup 10.30.1.10 40000 10.30.3.10 1433 tcp ZN-WEB
 -> policy 12 (ALL, accept)
```

**گام ۲ — علت:** Policy 12 قدیمی (ZN-WEB→ZN-DB ALL) بالاتر از 61 قرار دارد (Shadow).

**گام ۳ — رفع:** Policy 61 را بالاتر از 12 ببرید؛ 12 را Disable کنید؛ پس از دو هفته مشاهده حذف.

**گام ۴ — آزمون منفی:** telnet 1433 ⇒ Timeout؛ Log: action=deny policyid=61.

**گام ۵ — Evidence:** خروجی Lookup قبل/بعد، Log، زمان، نام مجری.

## درس 24-3 — Lab عملی VDOM: ساخت، Inter-VDOM Link، Policy و محدودیت منابع

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۱، ۲۴-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. VDOM (Virtual Domain) را بسازید و وضعیت Multi-VDOM را روشن کنید.
2. Interface را به VDOM تخصیص دهید.
3. Inter-VDOM Link بسازید و Policy بین VDOMها بنویسید.
4. محدودیت منابع هر VDOM (Resource Limits) را تنظیم کنید.
5. Admin Profile و Administrator هر VDOM را جدا کنید.
6. ایزولاسیون را با آزمون منفی ثابت کنید.

### چرا باید یاد بگیریم؟

VDOM یعنی «یک فایروال فیزیکی، چند فایروال مجازی». مثل یک ساختمان که هر طبقه‌اش یک شرکت مستقل با کلید مجزاست. کاربردها: Multi-tenant (ISP/MSP)، جداسازی Production/Test، یا جداسازی دپارتمان‌ها با Admin متفاوت. ولی VDOM لایسنس و ظرفیت دارد (مدل: تعداد پیش‌فرض ۱۰؛ بیشتر Needs-License) و پیچیدگی را بالا می‌برد؛ فقط وقتی لازم است استفاده شود.

### مفاهیم

| مفهوم | معنی |
|---|---|
| Global | تنظیمات مشترک (Admin، HA، FortiGuard، Interfaces فیزیکی) |
| VDOM | Routing، Policy، VPN، Address مستقل |
| root | VDOM پیش‌فرض (مدیریت در حالت Management VDOM) |
| Inter-VDOM Link | لینک مجازی بین VDOMها |
| Resource Limits | سقف Session، Policy و … |

### فعال‌سازی Multi-VDOM

``` text
config system global
    set vdom-mode multi-vdom
end
```

(در 7.0 `vdom-mode multi-vdom` در Global؛ با ورود دوباره Admin؛ Backup قبل از فعال‌سازی؛ بازگشت به Single-VDOM ساده نیست.)

### ساخت VDOM و تخصیص

``` text
config vdom
    edit TENANT-A
    next
    edit TENANT-B
    next
end
config global
    config system interface
        edit "port5"
            set vdom "TENANT-A"
        next
        edit "port6"
            set vdom "TENANT-B"
        next
    end
end
```

### Inter-VDOM Link

``` text
config global
    config system vdom-link
        edit "vlnk-AB"
        next
    end
    config system interface
        edit "vlnk-AB0"
            set vdom "TENANT-A"
            set ip 10.254.0.1 255.255.255.252
        next
        edit "vlnk-AB1"
            set vdom "TENANT-B"
            set ip 10.254.0.2 255.255.255.252
        next
    end
end
```

سپس در هر VDOM Static Route و Policy. اگر نباید ارتباطی باشد، Inter-VDOM ایجاد نکنید.

### Policy در VDOM

``` text
config vdom
    edit TENANT-A
        config firewall policy
            edit 1
                set name "A-LAN-to-INTERNET"
                set srcintf "port5"
                set dstintf "port1"
                set srcaddr "all"
                set dstaddr "all"
                set action accept
                set schedule "always"
                set service "ALL"
                set nat enable
                set logtraffic all
            next
        end
    next
end
```

هر VDOM جدول مسیر، Policy، Address و VPN خودش را دارد. اینترنت مشترک (port1) باید به یک VDOM (مثلاً root یا TRANSIT) تعلق گیرد و بقیه از طریق Inter-VDOM دسترسی بگیرند.

### Resource Limits

``` text
config global
    config system vdom-property
        edit "TENANT-A"
            set session 100000
            set policy 500
            set firewall-address 1000
        next
    end
end
```

سقف‌ها از «طغیان» یک VDOM روی دیگران جلوگیری می‌کند. مقدار را از ظرفیت مدل و Baseline تعیین کنید.

### Admin و Profile

Administrator با Admin Profile محدود به VDOM خاص (`set vdom "TENANT-A"`). Super Admin فقط در Global. اصل: هر Tenant فقط VDOM خودش را ببیند.

### مثال‌های حل‌شده

#### مثال ساده — دو Tenant

TENANT-A و B با Interfaceهای جدا. Policy هر کدام اینترنت. آزمون: از A به B ping ⇒ Timeout (هیچ Inter-VDOM نیست). Isolation اثبات.

#### مثال متوسط — Inter-VDOM

A و B باید به یک سرویس مشترک (SHARED VDOM) برسند: Inter-VDOM Link A↔SHARED و B↔SHARED؛ Policyها حداقلی؛ بین A و B ارتباط نه. آزمون: A→B Timeout؛ A→SHARED سرویس OK.

#### مثال متوسط — Resource

`session 100000` برای A. یک Tenant حمله‌ی SYN Flood دارد؛ فقط A به سقف می‌رسد؛ B سالم. بدون سقف، Session Table کل دستگاه پر می‌شد.

#### مثال سخت — Admin نشت

Admin Tenant A دسترسی Global داشت ⇒ می‌تواند Config B را ببیند. رفع: Profile محدود + VDOM مشخص؛ آزمون: Login به‌عنوان Admin-A و تلاش به `config vdom edit TENANT-B` ⇒ Permission denied.

#### مثال سخت — لایسنس و HA

تعداد VDOM بیش از Default (۱۰) نیاز دارد؛ Needs-License؛ در HA هر دو عضو باید VDOM یکسان؛ Failover برای VDOMهای جداگانه (VCluster) پیچیده‌تر. تصمیم: طراحی با حداقل VDOM و ثبت.

### مسیر GUI (مستندی، Unverified)

1. System → Settings: Virtual Domains Enable.
2. Global → Virtual Domains → Create New.
3. Network → Interfaces → Inter-VDOM Link.

### Lab هدایت‌شده (اجرا نشده)

1. دو VDOM و Interface.
2. Inter-VDOM و Policy.
3. Resource Limit و Admin محدود.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Interface تخصیص نمی‌شود | Policy/Route دارد | حذف قبلی |
| ارتباط A↔B | Inter-VDOM ناخواسته | حذف |
| VDOM گیر | منابع | Limits |
| Admin می‌بیند همه | Profile | محدود |

### نکات امنیتی

Admin هر VDOM جدا؛ Global فقط Super Admin با MFA؛ Log هر VDOM جدا (یا Tag)؛ Inter-VDOM حداقلی.

### جمع‌بندی

VDOM = فایروال مجازی مستقل؛ Global/VDOM؛ Interface، Inter-VDOM و Policy؛ Resource Limits؛ Admin محدود؛ آزمون منفی Isolation؛ لایسنس و HA ملاحظه‌ی طراحی.

### تمرین و ارزیابی

**ت1.** (ساده) VDOM چیست؟ *(پاسخ: 24-3-ت1)*

**ت2.** (ساده) Inter-VDOM Link؟ *(پاسخ: 24-3-ت2)*

**ت3.** (متوسط) چرا Resource Limit؟ *(پاسخ: 24-3-ت3)*

**ت4.** (متوسط) Management VDOM؟ *(پاسخ: 24-3-ت4)*

**ت5.** (سخت) ping بین VDOM ندارد. *(پاسخ: 24-3-ت5)*

**ت6.** (سخت، طراحی) دو VDOM. *(پاسخ: 24-3-ت6)*

**Q1.** Quick quiz (English): What is the purpose of an inter-VDOM link? *(پاسخ: 24-3-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VDOM | Virtual Domain | دامنه‌ی مجازی |

- *Limit the resources of each VDOM.* ← منابع هر VDOM را محدود کنید.

### کارت Lab

**کارت Lab:** VDOM (اجرا نشده؛ Needs-License). **Evidence:** `02-design/vdom-lab.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Virtual Domains

<a id="l-24-4"></a>

## درس 24-4 — Logging Data Center و Gate G9: اثبات Isolation، آزمون منفی، Alert و مستندسازی

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۱ تا ۲۴-۳ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

<!--deep-->

### هدف آموزشی

در پایان این درس باید بتوانید:

1. Logging Data Center (مرکز، Tag، Retention) را طراحی کنید.
2. اثبات Isolation با آزمون منفی و Log را انجام دهید.
3. Alert برای Deny غیرعادی/Lateral Movement تعریف کنید.
4. Gate G9 را (طراحی، آزمون، Evidence، Rubric) اجرا کنید.
5. مستندسازی Policy/Isolation را بنویسید.
6. صداقت (اجرا نشده/Unverified) را رعایت کنید.

### چرا باید یاد بگیریم؟

امنیت Data Center بدون Log اثبات‌پذیر نیست. ادعای «وب به DB دسترسی ندارد» تا وقتی Log آزمون منفی را نشان ندهد فقط ادعاست. ممیز و مدیر حادثه به شواهد نیاز دارند: چه کسی، چه زمان، چه چیزی رد شد. G9 از شما می‌خواهد با آزمون منفی و Log ثابت کنید دو مستأجر/لایه جدا هستند و ناهنجاری در دقیقه دیده می‌شود.

### طراحی Logging

| مورد | تصمیم |
|---|---|
| مقصد | FortiAnalyzer/Syslog/SIEM |
| فیلد | Traffic، Event، UTM (در صورت لایسنس) |
| Retention | حداقل ۹۰ روز آنلاین، ۱ سال آرشیو (طبق الزام) |
| Tag | VDOM/Zone/Tenant در Log |
| زمان | NTP یکسان |
| امنیت | انتقال رمزگذاری‌شده (`reliable` + TLS) |

``` text
config log syslogd setting
    set status enable
    set server "10.50.0.20"
    set mode reliable
    set port 6514
    set enc-algorithm high
    set facility local7
end
config log setting
    set fwpolicy-implicit-log enable
    set local-in-allow enable
    set local-in-deny-unicast enable
end
```

(`mode reliable` و TLS در مستند 7.0 بررسی شود؛ Unverified.)

### آزمون منفی و Log

برای هر ادعای Isolation:

1. اجرای آزمون (مثلاً `nc -vz db 1433` از Web).
2. مشاهده‌ی Timeout.
3. پیدا کردن Log Deny متناظر (زمان، Src، Dst، Port، policyid=0).
4. ثبت Evidence.

``` text
execute log filter category 0
execute log filter field dstip 10.20.0.40
execute log filter field action deny
execute log display
```

### Alert

| Alert | شرط | واکنش |
|---|---|---|
| Lateral scan | >20 Deny از یک Src به Dst‌های مختلف در ۱ دقیقه | Isolation Host |
| Web→DB | هر Deny | بررسی فوری |
| DB Outbound | هر Allow/Deny به اینترنت | حادثه |
| Policy تغییر | Event config | Review |
| Admin ورود | خارج از ساعت | تأیید |

### Gate G9 — صورت مسئله

Data Center با دو Tenant (VDOM A و B) و سه‌لایه Web/App/DB. باید ثابت شود:

1. A و B هیچ ارتباطی ندارند.
2. Web به DB ندارد.
3. DB Outbound ندارد.
4. Log و Alert کار می‌کند.

عیب‌های تزریق‌شده:

1. Inter-VDOM Link ناخواسته بین A و B با Policy ALL.
2. Policy Web→DB قدیمی با Hit Count > 0.
3. Log Deny فعال نیست (implicit log خاموش).

### کلید پاسخ

**عیب ۱:**

1. Evidence: `ping` از A به B موفق؛ Log Policy ALL.
2. رفع: حذف Inter-VDOM و Policy.
3. تأیید: آزمون منفی Timeout + Log Deny.

**عیب ۲:**

1. Evidence: `Hit Count` Web→DB؛ Lookup ⇒ مجاز.
2. رفع: حذف Policy؛ بررسی چه کسی از آن استفاده کرده.
3. تأیید: Lookup ⇒ policy 0.

**عیب ۳:**

1. Evidence: آزمون منفی انجام شد ولی Log Deny نیست.
2. رفع: `fwpolicy-implicit-log enable`.
3. تأیید: Log Deny در FortiAnalyzer.

### Rubric (۱۰۰)

| معیار | امتیاز |
|---|---|
| طراحی Log/Tag/Retention | 15 |
| آزمون منفی و Evidence | 25 |
| رفع سه عیب | 25 |
| Alert | 15 |
| مستندسازی | 10 |
| صداقت | 10 |

### مثال‌های حل‌شده

#### مثال ساده — Evidence

آزمون: Web→DB:1433 Timeout. Log: `2026-11-27 10:15:01 srcip=10.30.0.10 dstip=10.20.0.40 dstport=1433 action=deny policyid=0`. Evidence: فایل `ev_negative_web_db.txt`.

#### مثال متوسط — Alert

Lateral scan: ۳۰ Deny در یک دقیقه از web01. Alert ⇒ Isolation (Quarantine Host) ⇒ تحقیق.

#### مثال متوسط — مستندسازی

جدول Isolation: ادعا، آزمون، Evidence، تاریخ، مالک؛ هر سه ماه تکرار.

| ادعا | آزمون | Evidence | تاریخ |
|---|---|---|---|
| A≠B | ping/nc | ev1.txt | 2026-11-27 |
| Web≠DB | nc 1433 | ev2.txt | 2026-11-27 |

#### مثال سخت — Retention

حادثه ۴ ماه بعد کشف شد؛ Log فقط ۹۰ روز. فاجعه. قاعده: Retention بر اساس «زمان تشخیص تیپیک» (Dwell Time) نه حداقل؛ آرشیو ارزان‌تر (Cold).

#### مثال سخت — صداقت

Lab اجرا نشده؛ Logهای بالا نمونه‌ی آموزشی؛ در گزارش «Unverified».

### Lab هدایت‌شده (اجرا نشده)

1. Log مرکزی.
2. آزمون منفی و Evidence.
3. Alert و گزارش.

### عیب‌یابی سریع

| علامت (مشاهده) | علت محتمل (باید اثبات شود) | اقدام پس از اثبات |
|---|---|---|
| Log Deny نیست | implicit log | enable |
| Log نمی‌رسد | syslog/TLS | بررسی |
| زمان متفاوت | NTP | همگام |
| Alert کاذب | آستانه | تنظیم |

### جمع‌بندی

Log مرکزی با Tag و Retention؛ آزمون منفی + Log = اثبات Isolation؛ Alert برای Lateral Movement؛ G9 با سه عیب؛ مستندسازی و صداقت.

### تمرین و ارزیابی

**ت1.** (ساده) چرا Deny صریح با Log؟ *(پاسخ: 24-4-ت1)*

**ت2.** (ساده) Isolation را چگونه اثبات می‌کنید؟ *(پاسخ: 24-4-ت2)*

**ت3.** (متوسط) Alert چه شرطی دارد؟ *(پاسخ: 24-4-ت3)*

**ت4.** (متوسط) Log کجا؟ *(پاسخ: 24-4-ت4)*

**ت5.** (سخت) Log ناقص. *(پاسخ: 24-4-ت5)*

**ت6.** (سخت، طراحی) ماتریس آزمون DC. *(پاسخ: 24-4-ت6)*

**Q1.** Quick quiz (English): Why is a negative test needed to prove isolation? *(پاسخ: 24-4-Q1)*

### اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SOC | Security Operations Center | مرکز عملیات امنیت |

- *Isolation must be proven with logs.* ← ایزولاسیون باید با Log اثبات شود.

### کارت Lab

**کارت Lab:** G9 (اجرا نشده). **Evidence:** `03-ops/g9-dc.md`.

### منابع

- Fortinet FortiOS 7.0 Administration Guide: Logging

## درس 24-5 — انواع VDOM، منابع Global و VDOM، مدیریت VDOM و طراحی چندمستاجره

**فصل 24 · درس افزوده برای سرفصل رسمی NSE 4 (FortiOS 7.0): «Describe and configure VDOMs to split a FortiGate into multiple virtual devices» · پیش‌نیاز: ۲۴-۰ تا ۲۴-۳**

> **وضعیت:** نظری/مستندی؛ FortiOS 7.0.3 نامی؛ دستورها `Unverified`؛ VDOM اضافه بر تعداد پیش‌فرض Needs-License؛ Lab اجرا نشده.

### ۱) این درس درباره چیست و چرا باید یاد بگیریم؟

**چه چیزی یاد می‌گیریم:** چه چیزی در سطح Global و چه چیزی در سطح VDOM تنظیم می‌شود، Management VDOM چیست، حالت NAT/Transparent هر VDOM، و چگونه ادمین‌ها و منابع را مدیریت کنیم.

**چرا لازم است؟** VDOM یک ساختمان چندواحدی است؛ برق و آسانسور مشترک (Global) و هر واحد کلید و دیوار خودش (VDOM). اگر ندانید فلان تنظیم Global است یا VDOM، یا آن را جای اشتباه می‌جویید یا یک تغییر Global همه‌ی مستأجران را قطع می‌کند.

### ۲) توضیح از پایه

#### ۲-۱) Global در برابر VDOM

| در Global | در VDOM |
|---|---|
| نسخه‌ی Firmware، Reboot | Firewall Policy، NAT |
| HA | Routing (Static/OSPF/BGP) |
| Interface فیزیکی (تخصیص به VDOM) | Interface مجازی/VLAN، Zone |
| Admin Profile و ادمین‌های Super | VPN، UTM Profile |
| Log سراسری، FortiGuard | کاربران/گروه‌ها (محدوده‌ی VDOM) |
| محدودیت منابع | Address/Service Objectها |

#### ۲-۲) انواع VDOM

- **Traffic VDOM (پیش‌فرض):** ترافیک عبوری مستأجر.
- **Admin VDOM:** مخصوص مدیریت/ارتباطات خود فایروال (FortiGuard، Log، DNS)؛ ترافیک کاربری از آن عبور نمی‌کند. (در FortiOS 7.0 مفهوم Management VDOM قابل‌تعیین است.)

``` text
config global
 config system global
  set management-vdom "root"
 end
end
```

#### ۲-۳) حالت هر VDOM

NAT/Route یا Transparent (درس ۱۲-۱۰) به‌ازای هر VDOM جدا. مثلاً VDOM مشتری A در NAT و VDOM بازرسی در Transparent.

#### ۲-۴) ادمین‌ها

- **Super Admin:** همه‌ی VDOMها و Global.
- **ادمین VDOM:** فقط VDOM یا VDOMهای تخصیص‌یافته.

``` text
config global
 config system admin
  edit "tenantA-admin"
   set accprofile "prof-tenant"
   set vdom "TENANT-A"
  next
 end
end
```

#### ۲-۵) منابع

``` text
config global
 config system vdom-property
  edit "TENANT-A"
   set session 50000
   set policy 500
   set firewall-address 1000
  next
 end
end
```

هر مستأجر سقف دارد؛ یک مستأجر پرمصرف نباید دیگران را خفه کند.

#### ۲-۶) ارتباط بین VDOMها

Inter-VDOM Link (Interface مجازی دو سر) با Policy هر دو سر؛ مستقیم هیچ ترافیکی بین VDOMها نمی‌رود.

### ۳) مثال‌های حل‌شده از ساده به سخت

**ساده — کجا؟** «ارتقای Firmware» Global؛ «افزودن Policy برای مستأجر A» داخل VDOM A.

**متوسط — محاسبه‌ی سهم منابع.** ظرفیت Session دستگاه = 200000 و ۴ مستأجر:

``` text
Equal share = 200000 / 4 = 50000
With 20 % reserve for management = 160000 / 4 = 40000 per tenant
```

**متوسط — طراحی.** سه VDOM: `MGMT` (Admin/Management)، `TENANT-A`، `TENANT-B` و یک VDOM `DMZ-SHARED` با Inter-VDOM Link. هر مستأجر فقط به DMZ مشترک (با Policy حداقلی).

**سخت — «ادمین مستأجر همه چیز را می‌بیند».** بررسی: `accprofile` (دسترسی سراسری؟) و `vdom` اختصاصی؛ حذف Super Admin از حساب مستأجر؛ پروفایل با `scope vdom`.

**سخت — تغییر Mode.** تبدیل VDOM از NAT به Transparent پاک‌سازی Interface/Route/Policy را می‌طلبد؛ Backup (Global و VDOM) و پنجره‌ی تغییر.

**سخت — Log.** هر VDOM Log جدا ارسال می‌کند؛ در Syslog فیلد `vd` را نگه دارید؛ در FortiAnalyzer ADOM به‌ازای VDOM/مستأجر.

### ۴) Lab (اجرا نشده)

دو VDOM با ادمین جدا؛ آزمون اینکه ادمین A VDOM B را نمی‌بیند.

### ۵) اصطلاحات این درس

| اصطلاح | شکل کامل | معنی |
|---|---|---|
| VDOM | Virtual Domain | دامنه‌ی مجازی |
| MGMT VDOM | Management VDOM | VDOM مدیریت |
| MSSP | Managed Security Service Provider | ارائه‌دهنده‌ی خدمات امنیت مدیریت‌شده |
| ADOM | Administrative Domain | دامنه‌ی مدیریتی FortiManager/Analyzer |

### ۶) تمرین‌ها

**ت1.** (ساده) سه تنظیم Global و سه تنظیم VDOM. *(پاسخ: 24-5-ت1 در بخش «پاسخ‌ها» انتهای فصل)*

**ت2.** (ساده) Management VDOM چیست؟ *(پاسخ: 24-5-ت2 در بخش «پاسخ‌ها» انتهای فصل)*

**ت3.** (متوسط) ظرفیت 120000 Session و ۳ مستأجر با ذخیره 10٪؛ سهم هر مستأجر؟ *(پاسخ: 24-5-ت3 در بخش «پاسخ‌ها» انتهای فصل)*

**ت4.** (سخت) ادمین مستأجر به VDOM دیگر دسترسی دارد؛ علت و رفع. *(پاسخ: 24-5-ت4 در بخش «پاسخ‌ها» انتهای فصل)*

### ۷) English Corner

- *Firmware upgrades and HA are configured globally, while policies and routing are per-VDOM.*
- *Each VDOM administrator should be restricted to their own VDOM.*
- **Q1.** What connects two VDOMs? *(پاسخ: 24-5-Q1 در بخش «پاسخ‌ها» انتهای فصل)*

---

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تکمیل عمیق: جدول عیب‌یابی سریع — VDOM

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| ادمین مستأجر همه‌چیز را می‌بیند | `accprofile` و `vdom` | Profile سراسری؛ ادمین VDOM-محدود |
| ارتباط بین VDOMها نیست | Inter-VDOM Link/Policy | Policy دو سر و Route |
| یک مستأجر منابع را می‌خورد | `vdom-property` | تعیین سقف Session/Policy |
| Log مخلوط | فیلد `vd` | جدا کردن Log هر VDOM |

## پاسخ‌های فصل 24

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی عمیق درس 24-1


### پاسخ‌های بازنویسی عمیق درس 24-1

**24-1-ت1** — ترافیک بین سرورهای داخلی.

East-West ترافیک بین سرورهای داخلی است و فایروال لبه آن را نمی‌بیند.

**24-1-ت2** — تا Policy روی جریان واقعی باشد.

Flow Discovery تا Policy روی جریان واقعی نوشته شود نه حدس.

**24-1-ت3** — جلوگیری از قطع سرویس ناشناخته.

Rollout مرحله‌ای از قطع سرویس ناشناخته (مثل Backup شبانه) جلوگیری می‌کند.

**24-1-ت4** — مسیر ممنوع طراحی.

WEB→DB در Log مسیر ممنوع طراحی بود و باید بررسی/مسدود شود.

**24-1-ت5** — Log طولانی‌تر و مالک.

Backup شبانه قطع شد — تحلیل: Log deny: BACKUP→DB 445 ساعت 02:00. در Discovery ۱۴ روزه دیده نشده چون Backup هفتگی بود. رفع: Policy مجزا برای BACKUP→DB با Service 445 و Schedule شبانه؛ آموزه: Log ≥ ۳۰ روز و مشورت مالک برای کارهای کم‌تکرار؛ پیش از Deny نهایی دوره‌ی Monitor.

**24-1-ت6** — ماتریس DC

| از ↓ به → | WEB | APP | DB | MGMT |
|---|---|---|---|---|
| Internet | 443 | - | - | - |
| WEB | - | 8443 | - | - |
| APP | - | - | 1433 | - |
| DB | - | - | - | - |
| MGMT | SSH | SSH | SSH | - |

**استدلال:** هر خانه‌ی خالی Deny صریح؛ مسیر فقط به لایه‌ی مجاور؛ DB بدون Outbound. بدون Flow Discovery، خانه‌ها را حدس نزنید.

**24-1-Q1** — Because attackers move laterally between servers once inside.

### پاسخ‌های بازنویسی درس 24-2


### پاسخ‌های بازنویسی عمیق درس 24-2

**24-2-ت1** — Least privilege.

Address Object در سطح Host تا Least privilege رعایت شود.

**24-2-ت2** — Log و Alert.

Deny صریح برای Log و Alert لازم است؛ Implicit Deny Log ندارد.

**24-2-ت3** — WEB→DB.

آزمون منفی WEB→DB: telnet 1433 رد و در Log Deny دیده شود.

**24-2-ت4** — Policy مطابق.

`iprope lookup` Policy مطابق جریان را نشان می‌دهد.

**24-2-ت5** — Hit Count ۱۲ برای Deny

**علامت:** Hit=12 روی Policy Deny. **علت اثبات‌نشده** است.

**فرضیه‌ها:** تلاش واقعی نفوذ/اسکن؛ برنامه‌ی قانونی با وابستگی جا افتاده؛ خطای پیکربندی.
**تفکیک:** Log Deny (Src، Dst، Port، زمان، الگو)؛ آیا Src شناخته‌شده؟ آیا زمان با Job مشخص مطابقت دارد؟ ۱۲ بار در یک ثانیه یا ۱۲ بار در ماه؟
**اقدام:** اگر قانونی، Policy حداقلی؛ اگر مشکوک، Alert/تحقیق.

**24-2-ت6** — Policy سه‌لایه

Policyهای ۵۰ (WEB→APP:8443)، ۶۰ (APP→DB:1433) و ۶۱ (Deny WEB→DB با Log) نمونه‌اند. **استدلال:** Policy Deny صریح WEB→DB اگرچه Implicit Deny هم هست، مشاهده‌پذیری و Hit Count می‌دهد؛ ترتیب باید درست باشد (Deny بالاتر از Allowهای عام). آزمون مثبت/منفی با `iprope lookup`.

**24-2-Q1** — To grant only the minimum necessary access.

### پاسخ‌های بازنویسی درس 24-3


### پاسخ‌های بازنویسی عمیق درس 24-3

**24-3-ت1** — فایروال مجازی مستقل.

VDOM فایروال مجازی مستقل است (Routing، Policy، Admin، منابع جدا).

**24-3-ت2** — لینک منطقی بین دو VDOM.

Inter-VDOM Link لینک منطقی بین دو VDOM بدون پورت فیزیکی است. طبق مستند Fortinet به‌صورت پیش‌فرض Point-to-Point (ppp) است؛ برای OSPFv3/IPv6 که به آدرس Link-local نیاز دارد، نوع لینک باید `ethernet` باشد؛ IP روی لینک فقط وقتی لازم است که مسیریابی پویا بخواهید.

**24-3-ت3** — جلوگیری از مصرف همه‌ی منابع.

Resource Limit تا یک VDOM همه‌ی Sessionها و منابع را نخورد.

**24-3-ت4** — VDOM سرویس‌های سیستمی.

Management VDOM VDOM سرویس‌های سیستمی (DNS، FortiGuard) است؛ معمولاً root.

**24-3-ت5** — IP، Route، Policy دو جهت.

ping بین VDOM ندارد — بررسی به ترتیب: ۱) IP روی دو سر vlk (vlk0 در DMZ و vlk1 در INT) و Subnet یکسان. ۲) Route در هر VDOM به Subnet VDOM دیگر از طریق vlk. ۳) Policy دو جهت. ۴) `diagnose debug flow` داخل هر VDOM (`config vdom / edit X`). ۵) آزمون ping. علت رایج: Policy فقط یک‌طرفه.

**24-3-ت6** — دو VDOM با Inter-VDOM Link

1. دو VDOM (DMZ و INT) و Interface هر کدام.
2. `vdom-link` و IP /30 دو سر.
3. Route در هر VDOM به Subnet دیگر از طریق vlnk.
4. Policy دو جهت حداقلی.
5. Resource Limit هر VDOM.
6. آزمون: مثبت ping/سرویس مجاز؛ منفی سرویس غیرمجاز.
**نکته:** ایجاد Inter-VDOM یعنی ایجاد مسیر؛ فقط اگر ارتباط لازم است.

**24-3-Q1** — To route traffic between two virtual domains.

### پاسخ‌های بازنویسی عمیق درس 24-4


### پاسخ‌های بازنویسی عمیق درس 24-4

**24-4-ت1** — Implicit Deny Log ندارد.

Implicit Deny Log ندارد؛ پس Deny صریح با Log لازم است.

**24-4-ت2** — آزمون منفی و Log Deny.

Isolation با آزمون منفی و Log Deny اثبات می‌شود.

**24-4-ت3** — تعداد Deny بین WEB و DB در بازه.

شرط Alert: تعداد Deny بین WEB و DB در یک بازه (مثلاً ≥۵ در ۵ دقیقه).

**24-4-ت4** — Syslog/FortiAnalyzer.

Log متمرکز در Syslog یا FortiAnalyzer ذخیره می‌شود.

**24-4-ت5** — Log ناقص

**علامت:** آزمون منفی انجام شد ولی Log Deny نیست. **علت محتمل:** `fwpolicy-implicit-log` خاموش، یا Policy Deny صریح بدون `logtraffic`، یا Log به مرکز نرسیده، یا فیلتر Log. **تفکیک:** ابتدا Log محلی `execute log display`؛ سپس Syslog/مرکز. **رفع:** فعال‌سازی Log Deny ضمنی/صریح و آزمون دوباره.

**24-4-ت6** — ماتریس آزمون DC

| # | ادعا | آزمون | انتظار |
|---|---|---|---|
| 1 | Web→App مجاز | `nc 8443` | Connected |
| 2 | App→DB مجاز | `nc 1433` | Connected |
| 3 | Web→DB ممنوع | `nc 1433` | Timeout + Log |
| 4 | DB→Internet ممنوع | curl | Timeout + Log |
| 5 | A≠B (مستأجر) | ping | Timeout |
| 6 | Mgmt محدود | SSH از Users | رد |
| 7 | Alert | اسکن | Alert |

**24-4-Q1** — Because isolation is proven by showing that forbidden traffic is denied and logged.

### پاسخ‌های درس افزوده‌ی 24-0 (فصل 24)

**24-0-ت1** — فایروال مجازی مستقل با Routing/Policy/Admin/منابع جدا.

VDOM فایروال مجازی مستقل با Routing/Policy/Admin/منابع جدا.

**24-0-ت2** — اتصال دو VDOM بدون پورت فیزیکی.

Inter-VDOM Link اتصال دو VDOM بدون پورت فیزیکی.

**24-0-ت3** — تا یک VDOM همه‌ی منابع (Session و ...) را نخورد.

Resource Limit تا یک VDOM همه‌ی منابع را مصرف نکند.

**24-0-ت4** — Zone در یک Routing/Policy مشترک؛ VDOM جدا و با Link ارتباط.

Zone در یک Routing/Policy مشترک است؛ VDOM جدا و با Link ارتباط می‌گیرد.

**24-0-ت5** — دو مشتری با Subnet هم‌پوشان و اینترنت مشترک

**فرض:** هر دو مشتری 10.0.0.0/24 دارند؛ اینترنت مشترک.

**طراحی:** هر مشتری یک VDOM؛ چون Routing جدول جدا دارد، Overlap مشکلی ایجاد نمی‌کند؛ اتصال به اینترنت از VDOM مشترک (Transit) با Inter-VDOM Link و **NAT در VDOM مشتری** (آدرس مبدأ به IP یکتا/Pool هر مشتری)؛ بین مشتری‌ها هیچ Inter-VDOM ایجاد نشود.

**استدلال:** Overlap در VDOM جدا قابل‌تحمل است؛ ولی ورود به VDOM مشترک باید NAT شود وگرنه آدرس‌های یکسان در Transit برخورد می‌کنند. آزمون: ping بین مشتری‌ها شکست؛ هر کدام اینترنت دارد.

**24-0-ت6** — جداسازی مدیریتی سه نقش

| نقش | دسترسی | دلیل |
|---|---|---|
| Super Admin | Global و همه VDOMها | کم‌تعداد، MFA، Break-glass |
| Admin مشتری | فقط VDOM خودش | حداقل دسترسی |
| Auditor | Log/Config فقط‌خواندنی | جداسازی وظایف |

**آزمون منفی:** Admin مشتری A تلاش به VDOM B ⇒ Permission denied. **استدلال:** بدون محدودیت VDOM، مستأجر Config مستأجر دیگر را می‌بیند.

**24-0-Q1** — Because one tenant could consume all sessions and resources and disrupt every other VDOM.

### پاسخ‌های درس افزوده‌ی 24-5 (فصل 24)

**24-5-ت1** — Global: Firmware، HA، Interface فیزیکی/تخصیص، ادمین‌ها و Profile؛ VDOM: Policy، Routing، VPN، UTM Profile.

**24-5-ت2** — VDOM مخصوص ارتباطات مدیریتی خود فایروال (FortiGuard، Log، DNS) که ترافیک کاربران از آن عبور نمی‌کند.

**24-5-ت3** — 120000 × 0.9 = 108000؛ 108000 / 3 = 36000 Session برای هر مستأجر.

**24-5-ت4** — ادمین مستأجر به VDOM دیگر دسترسی دارد

**علامت:** Admin مستأجر A به VDOM B دسترسی دارد.
**علت محتمل (باید اثبات شود):** Admin Profile/`vdom` اشتباه (دسترسی Global یا چند VDOM)، حساب مشترک، یا Inter-VDOM Link با Policy باز.
**تفکیک:** `show system admin <name>` برای `vdom` و `accprofile`؛ ورود به‌عنوان آن Admin و تلاش به VDOM B؛ بررسی vdom-link.
**رفع:** Profile حداقلی، VDOM مشخص، حذف Link/Policy غیرلازم، آزمون منفی تکراری.

**24-5-Q1** — An inter-VDOM link (with policies on both sides).

---

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
