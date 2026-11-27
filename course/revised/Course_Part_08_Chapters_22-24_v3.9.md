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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

### Lab هدایت‌شده (اجرا نشده)

1. برگه‌ی طراحی را کامل کنید.
2. Cluster بسازید و Verify کنید.
3. Out-of-sync عمدی و رفع.

### عیب‌یابی سریع

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

| علامت | علت | رفع |
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

### Lab هدایت‌شده (اجرا نشده)

1. Cluster، سه عیب را رفع کنید.
2. Split-brain کنترل‌شده.
3. Upgrade با Rollback.

### عیب‌یابی سریع

| علامت | علت | رفع |
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

**22-1-ت5** — ISP، Config خراب، CVE مشترک، Split-brain.

HA همه‌ی خرابی‌ها را حل نمی‌کند: خرابی ISP، Config خراب (همگام می‌شود!)، CVE مشترک بین دو دستگاه و Split-brain.

**22-1-ت6** — جدول با ستون راه مکمل و RTO.

جدول SPOF: هر جزء، ریسک، راه مکمل (HA، Dual-ISP، UPS) و RTO هدف.

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

**22-2-ت6** — جدول بالا.

برگه‌ی HA: Mode، Group، Password (Vault)، hbdev، Priority، monitor، override و session-pickup با دلیل.

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

**22-3-ت5** — Monitor/HB timers.

Failover کند (مثلاً ۱۲ ثانیه): ۱) `diagnose sys ha history read` علت و زمان را نشان می‌دهد. ۲) Monitor Interface: آیا خرابی لینک سریع دیده شد؟ ۳) Heartbeat interval و lost-threshold (پیش‌فرض‌ها را از مستند بخوانید؛ `Unverified`). ۴) کاهش محتاطانه و آزمون ۱۰ بار قطع/وصل. ریسک: Timer خیلی کم Flap می‌دهد؛ معیار: Failover < ۵ ثانیه بدون Flap.

**22-3-ت6** — ۵ آزمون.

ماتریس ۵ آزمون: Reboot، قطع Monitor، قطع یک HB، قطع هر دو HB، Failback.

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

**22-4-ت5** — HB، Reboot، Re-sync.

Split-brain رفع: ۱) تأیید: روی هر دو `get system ha status` Primary. ۲) Heartbeat را وصل کنید (دو لینک). ۳) عضوی را که نباید Primary باشد Reboot کنید. ۴) پس از Join `diagnose sys ha checksum cluster` را بررسی و در صورت نیاز Sync. ۵) Alert روی تغییر Primary. ۶) در RCA: چرا هر دو HB قطع شدند (سوییچ مشترک؟).

**22-4-ت6** — Partition قبلی.

Rollback Cluster: Boot از Partition قبلی هر دو یا Restore Config+Firmware.

**22-4-Q1** — diagnose sys ha history read.

### پاسخ‌های بازنویسی عمیق درس 22-5


### پاسخ‌های بازنویسی عمیق درس 22-5

**22-5-ت1** — ارتباط بین اعضا برای تشخیص سلامت و همگام‌سازی؛ قطع کامل آن Split-brain می‌سازد.

**22-5-ت2** — پس از بازگشت عضو قوی‌تر، Primary فعلی را تغییر نمی‌دهد و از Flap جلوگیری می‌کند.

**22-5-ت3** — تا خرابی یک لینک Cluster را Split نکند.

دو لینک HB مستقل تا خرابی یک لینک Cluster را Split نکند.

**22-5-ت4** — Sessionهای TCP را بین اعضا همگام می‌کند تا پس از Failover ادامه یابند.

**22-5-ت5** — دو Primary؛ بازگرداندن HB؛ انتخاب Primary و Re-sync؛ پیشگیری با HB مضاعف و Monitor.

**22-5-ت6** — Path، Backup، Secondary اول، Failover، Primary قبلی، checksum، Rollback.

**22-5-Q1** — Loss of all heartbeat links so both units think they are primary.

### پاسخ‌های درس افزوده‌ی 22-0 (فصل 22)

**22-0-ت1** — Active-Passive: یک دستگاه ترافیک می‌برد؛ Active-Active: بار Inspection بین اعضا پخش می‌شود؛ a-p ساده‌تر.

**22-0-ت2** — قطع Heartbeat با دو دستگاه زنده که هر دو Primary می‌شوند.

Split-brain: HB قطع ولی هر دو دستگاه زنده‌اند و هر دو Primary می‌شوند.

**22-0-ت3** — Failback خودکار نمی‌شود؛ عضو فعلی Primary می‌ماند.

با override disable، Failback خودکار انجام نمی‌شود؛ عضو فعلی Primary می‌ماند.

**22-0-ت4** — تا خرابی یک لینک باعث Split-brain نشود.

دو لینک HB تا خرابی یک لینک Split-brain نسازد.

**22-0-ت5** — Session Pickup خاموش است؛ فعال‌کردن آن (TCP) و بررسی محدودیت UDP/ICMP.

**22-0-ت6** — HA از خرابی دستگاه، SD-WAN از خرابی/افت کیفیت ISP؛ هر دو لازم‌اند؛ Heartbeat جدا و Health-check مستقل.

**22-0-م1** — بررسی هم‌خوانی Config بین اعضا.

Checksum Cluster هم‌خوانی Config بین اعضا را بررسی می‌کند.

**22-0-Q1** — Loss of heartbeat between members that are both still running, so each assumes the primary role.

### پاسخ‌های درس افزوده‌ی 22-6 (فصل 22)

**22-6-ت1** — در a-p فقط Primary ترافیک را پردازش می‌کند؛ در a-a Primary بخشی از ترافیک (پیش‌فرض ترافیک نیازمند UTM/Proxy) را به Subordinate توزیع می‌کند.

**22-6-ت2** — Multi-VDOM؛ VDOMها بین دو Virtual Cluster تقسیم می‌شوند.

**22-6-ت3** — چون پس از افتادن یک عضو فقط یک دستگاه می‌ماند و باید کل بار را بردارد؛ ظرفیت طراحی باید بر پایه‌ی یک دستگاه باشد.

**22-6-ت4** — با `ha-mgmt-status enable` و تعریف Interface مدیریتی اختصاصی روی هر عضو.

**22-6-Q1** — With it enabled, the primary distributes all sessions (not only those requiring content inspection) to the cluster members.

---

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

| علامت | علت | رفع |
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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Asymmetric Routing را در توپولوژی‌های واقعی (Dual-ISP، ECMP، دو فایروال، VPN+Internet) تشخیص دهد.
2. رفتار فایروال Stateful را بسته‌به‌بسته توضیح دهد (SYN، SYN/ACK، ACK، داده).
3. دو مکانیزم Drop (RPF fail و No-session/Denied) را تفکیک کند.
4. با Sniffer دو‌نقطه‌ای و Debug Flow و Session ثابت کند.
5. اثر Asymmetric روی NAT، UTM و Log را بگوید.
6. درباره‌ی «نامتقارن مجاز» (Stateless/IPS bypass) قضاوت کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا باید علت را قبل از رفع بدانیم؟** رفع مسیر نامتقارن بدون دانستن علت مثل مسکّن‌دادن بدون تشخیص است. پنج علت رایج هرکدام آزمون مشخص دارند:

1. **دو ISP بدون SNAT:** خروج از ISP-A ولی پاسخ سرور به IP داخلی از مسیر دیگر.
2. **Policy Route یک‌طرفه:** برگشت از مسیر پیش‌فرض.
3. **ECMP:** Hash متفاوت.
4. **دو فایروال موازی:** هر کدام یک جهت.
5. **سرور چندکارته (Multi-homed):** پاسخ را از کارتی می‌فرستد که Default Gateway دارد.

**اصل عیب‌یابی:** Sniffer هم‌زمان روی همه‌ی نقاط، مقایسه‌ی Route رفت و برگشت (`get router info routing-table details <src>` و `<dst>`)، و `diagnose firewall proute list`.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — سرور Multi-homed

سرور دو کارت شبکه (LAN و DMZ) دارد و Default Gateway فقط روی یکی است. درخواست از DMZ می‌آید ولی پاسخ از LAN می‌رود ⇒ نامتقارن. رفع: Policy-based routing روی سرور:

``` text
ip rule add from 10.30.0.10 table 100
ip route add default via 10.30.0.1 dev eth1 table 100
```

#### مثال متوسط — Policy Route

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.0.0/24"
  set output-device "port3"
  set gateway 198.51.100.1
 next
end
```

رفت از Policy Route؛ برگشت از جدول عادی ⇒ اگر مسیر برگشت متفاوت است، نامتقارن می‌شود.

#### مثال سخت — شواهد

FW1 و FW2 هم‌زمان Sniffer:

``` text
diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l
```

مقایسه‌ی زمان‌ها و Sequence: رفت در FW1 و برگشت در FW2 اثبات می‌شود. بدون این شاهد، «نامتقارن است» فقط حدس است.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: علل رایج

دو ISP، Policy Route ناهمخوان، ECMP، دو فایروال موازی، Multi-homed سرور. برای هر علت یک آزمون: `get router info routing-table details <src>` در مقایسه با مسیر رفت.

**پرسش‌های مصاحبه**
1. *ECMP و Session؟* Hash 5-tuple.
2. *Asymmetric در VPN؟* Selector/Route.
3. *تشخیص؟* Sniffer دوطرفه.

### تکمیل عمیق: علت‌های مسیر نامتقارن — شناسایی با شاهد

#### چرا؟

قبل از رفع باید علت را بدانید. پنج علت رایج دارد و هر کدام آزمون مشخص دارد.

#### فهرست علت‌ها و آزمون

| علت | آزمون |
|---|---|
| دو ISP بدون SNAT | `get router info routing-table details <src>` |
| Policy Route یک‌طرفه | `diagnose firewall proute list` |
| ECMP | `get router info routing-table all` (چندمسیره) |
| دو فایروال موازی | Sniffer دوطرفه |
| سرور چند‌کارت (Multi-homed) | `route -n` روی سرور |

#### مثال ساده — سرور Multi-homed

سرور دو کارت شبکه دارد (LAN و DMZ). پاسخ را از کارتی می‌فرستد که Default Gateway دارد، نه کارتی که درخواست از آن آمد. رفع: Policy-based routing روی سرور (ip rule) یا یک Default Gateway.

``` text
ip rule add from 10.30.0.10 table 100
ip route add default via 10.30.0.1 dev eth1 table 100
```

#### مثال متوسط — Policy Route

``` text
config router policy
 edit 1
  set input-device "port2"
  set src "10.10.0.0/24"
  set output-device "port3"
  set gateway 198.51.100.1
 next
end
```

اگر برگشت از Policy Route نداشته باشد، از مسیر پیش‌فرض می‌آید ⇒ نامتقارن.

#### مثال سخت — Sniffer هم‌زمان

روی FW1 و FW2 هم‌زمان:

``` text
FW1: SYN seen, ACK seen (after), SYN-ACK NOT seen
FW2: SYN-ACK seen, SYN NOT seen
```

تفسیر: رفت از FW1 و برگشت از FW2. راه: Route/Policy Route یا Session Sync.

#### Lab

سرور دو کارته بسازید و Asymmetric را تولید و رفع کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| فقط بعضی کاربران | Policy Route | همه‌ی منابع |
| فقط یک سرور | Multi-homed | ip rule |
| متناوب | ECMP | Hash |

#### پرسش‌ها با پاسخ

**۱. Multi-homed چه مشکلی؟** برگشت از کارت دیگر.
**۲. proute list؟** مشاهده‌ی Policy Route.
**۳. Sniffer دوطرفه چرا؟** مرز را نشان می‌دهد.

#### English Corner

- *Capture on both paths at once to see the asymmetry.*
- Q: Why can a multi-homed server cause asymmetric routing?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا ترتیب راه‌حل مهم است؟** پنج راه‌حل داریم و هرکدام هزینه و ریسک دارد. اولویت پیشنهادی: ۱) **طراحی متقارن** (رفت و برگشت از یک فایروال) ۲) **Policy Route/SD-WAN Rule** هماهنگ ۳) **SNAT** (برگشت را به IP همان فایروال می‌برد) ۴) **Session Sync** (HA/ Cluster) ۵) **`asymroute`** (آخرین؛ بازرسی Stateful را سست می‌کند و Evidence امنیتی کم می‌شود).

**SNAT چگونه کمک می‌کند؟** وقتی Source IP را به IP همان ISP/فایروال ترجمه می‌کنید، سرور مقصد پاسخ را به همان آدرس می‌فرستد و برگشت از همان مسیر می‌آید. هزینه: ردیابی IP واقعی کاربر در سرور مقصد سخت می‌شود (باید از Log فایروال استفاده کرد).

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — SNAT

``` text
config firewall policy
 edit 20
  set nat enable
  set ippool enable
  set poolname "POOL-ISP-A"
 next
end
```

برگشت به IP Pool ISP-A همان مسیر رفت.

#### مثال متوسط — SD-WAN

Rule با `mode manual` برای شبکه‌ی کاربران روی Member A؛ با SNAT برگشت هم از A.

#### مثال سخت — Session Sync

دو فایروال Active-Active با Session Sync: هر دو Session را می‌دانند و مسیر نامتقارن مجاز می‌شود. هزینه: ظرفیت و تأخیر لینک Sync؛ در ترافیک سنگین ممکن است گران باشد.

#### مثال سخت — asymroute

``` text
config system settings
 set asymroute enable
end
```

فقط موقت و با ثبت ریسک؛ پس از اصلاح طراحی حذف شود. آزمون: Sniffer نشان دهد دیگر بسته‌ی بی‌Session نمی‌رسد.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: راه‌حل‌ها

۱) طراحی متقارن (بهترین) ۲) Policy Route منبع-مبنا ۳) SNAT به IP هر ISP ۴) در موارد ناگزیر `asymroute` (ریسک امنیتی). برای HA/موازی: Session Sync.

``` text
config system settings
 set asymroute enable
end
```

هشدار: Asymroute بازرسی Stateful را سست می‌کند؛ آخرین راه.

**پرسش‌های مصاحبه**
1. *SNAT چگونه؟* برگشت به همان خروجی.
2. *Policy Route؟* بر اساس منبع.
3. *ریسک؟* Bypass بررسی.

### تکمیل عمیق: رفع Asymmetric — طراحی متقارن، SNAT و گزینه‌ی آخر

#### چرا؟

رفع مسیر نامتقارن یک ترتیب اولویت دارد: ابتدا طراحی متقارن، سپس NAT، و در آخر سست‌کردن بازرسی.

#### ترتیب راه‌حل‌ها

1. **طراحی متقارن**: برگشت از همان فایروال رفت.
2. **Policy Route / SD-WAN Rule**: خروج بر اساس منبع و برگشت هماهنگ.
3. **SNAT**: برگشت به IP همان فایروال.
4. **Session Sync / HA**: دو فایروال Session مشترک.
5. **`asymroute`**: آخرین راه.

#### مثال ساده — SNAT

اگر کاربر از ISP-A خارج می‌شود، SNAT به IP-A باعث می‌شود سرور مقصد پاسخ را به IP-A بفرستد؛ پس از همان لینک برمی‌گردد.

``` text
config firewall policy
 edit 20
  set nat enable
  set ippool enable
  set poolname "POOL-ISP-A"
 next
end
```

#### مثال متوسط — SD-WAN

قاعده‌ی SD-WAN با `mode manual` و عضو A برای 10.10.0.0/24؛ برگشت از همان Interface چون SNAT به IP عضو A.

#### مثال سخت — دو فایروال موازی

با Session Sync (HA Active-Active) هر دو فایروال Sessionها را می‌دانند و مسیر نامتقارن مجاز می‌شود. هشدار: Sync ظرفیت و تأخیر می‌خواهد؛ برای ترافیک سنگین ممکن است گران باشد.

#### `asymroute` — هشدار

``` text
config system settings
 set asymroute enable
end
```

بازرسی Stateful را برای بسته‌های بدون Session سست می‌کند و Evidence امنیتی کم می‌شود؛ فقط موقت و با ثبت ریسک.

#### Lab

یک Asymmetric ساخته‌شده را با SNAT رفع و Sniffer قبل/بعد را مقایسه کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| پس از SNAT هنوز Drop | Pool اشتباه | بررسی |
| Sync کند | لینک ضعیف | لینک اختصاصی |
| asymroute خطر | سست شدن | حذف پس از اصلاح |

#### پرسش‌ها با پاسخ

**۱. اولویت راه‌حل؟** متقارن‌سازی.
**۲. چرا asymroute آخر؟** کاهش امنیت.
**۳. SNAT چه می‌کند؟** برگشت را هدایت.

#### English Corner

- *Prefer symmetric design; use asymroute only as a last resort.*
- Q: How does SNAT force a symmetric return path?

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

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا چند فایروال؟** برای تفکیک نقش (Edge/Internal) یا ظرفیت. دو الگو:

- **سری:** ترافیک از هر دو می‌گذرد (Users → Internal FW → Edge FW → Internet). مسیر طبیعی متقارن، ساده؛ NAT فقط یک‌جا.
- **موازی:** بار تقسیم می‌شود؛ ظرفیت بیشتر ولی خطر نامتقارن؛ نیاز به Hash متقارن یا Session Sync.

**قاعده‌ی N+1:** ظرفیت را طوری بگیرید که با افتادن یک دستگاه، بقیه بار کامل را بردارند.

**جمع‌بندی اصلی درس:**

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

#### مثال ساده — محاسبه‌ی ظرفیت

``` text
Peak 6 Gbps, each FW (with UTM) = 4 Gbps
Needed = 6 / 4 = 1.5 -> 2 firewalls
N+1 -> 3 firewalls
```

#### مثال متوسط — NAT

اگر NAT هم در Internal و هم در Edge باشد، Log دو IP دارد و ردیابی سخت می‌شود. قاعده: یک نقطه‌ی NAT.

#### مثال سخت — خرابی یک فایروال موازی

با Hash منبع و بدون Session Sync، خرابی یک فایروال Hash را دوباره توزیع می‌کند و Sessionهای موجود قطع می‌شوند. با Sync فقط Failover سریع.

#### مثال‌های اصلی درس (مرور)

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: الگوهای سری و موازی

سری: هر بسته از هر دو؛ NAT یک‌جا. موازی (Active-Active/ECMP): Session Sync یا Hash ثابت. **NAT:** فقط در یک نقطه.

**پرسش‌های مصاحبه**
1. *الگوی ساده‌تر؟* سری.
2. *Load-balance؟* Hash منبع.
3. *Sync؟* HA یا دستی.

### تکمیل عمیق: چند فایروال سری و موازی — الگوها و NAT

#### چرا؟

در سازمان‌ها گاهی لازم است بیش از یک فایروال از مسیر ترافیک عبور کند؛ برای تفکیک نقش (Edge/Internal) یا ظرفیت. هر الگو مزایا و دام دارد.

#### الگوی سری (Serial)

``` text
Users -> Internal FW -> Edge FW -> Internet
```

هر بسته از هر دو می‌گذرد؛ مسیر متقارن طبیعی است. NAT فقط در Edge. مزیت: ساده؛ عیب: دو نقطه‌ی شکست.

#### الگوی موازی (Parallel)

``` text
Users -> {FW-A | FW-B} -> Internet
```

بار تقسیم می‌شود؛ خطر نامتقارن. راه: Hash منبع، یا HA Active-Active با Session Sync.

#### مثال ساده — محاسبه‌ی ظرفیت

``` text
Peak traffic = 6 Gbps ; FW capacity (with UTM) = 4 Gbps each
Need >= 6 / 4 = 1.5 -> 2 firewalls (parallel) + headroom for failure (N+1) -> 3
```

N+1: اگر یکی بیفتد دو دستگاه باقیمانده 8 Gbps دارند.

#### مثال متوسط — NAT در سری

اگر NAT هم در Internal و هم Edge باشد، Log دو IP دارد و ردیابی سخت است. قاعده: یک نقطه‌ی NAT.

#### مثال سخت — خرابی یک‌جانبه

در الگوی موازی با Hash منبع، یک FW می‌افتد؛ Hash دوباره توزیع می‌شود و Sessionهای موجود قطع می‌شوند (چون Session Sync نیست). با Sync فقط Failover سریع.

#### Lab

یک الگوی سری دو FW را بسازید و Session هر دو را مقایسه کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| دو IP در Log | دو NAT | یکی |
| قطع در خرابی | Sync ندارد | Session Sync |
| ظرفیت کم | UTM | N+1 |

#### پرسش‌ها با پاسخ

**۱. N+1 چیست؟** یک دستگاه اضافه.
**۲. چرا یک NAT؟** ردیابی.
**۳. موازی چه خطری؟** نامتقارن.

#### English Corner

- *Size for N+1 so a single failure does not cause overload.*
- Q: Why should NAT happen at only one point?

## درس 23-4 — آزمون معماری ۵: چندفایروالی و مسیر نامتقارن — صورت مسئله، کلید پاسخ و Rubric

**فصل 23 · بازنویسی عمیق · پیش‌نیاز: ۲۳-۱ تا ۲۳-۳، ۱۰-۶ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. معماری سه‌فایروالی (Edge، Internal، DR) را با جدول مسیر طراحی کند.
2. Asymmetric را تشخیص و با Capture دو سمتی اثبات کند.
3. راه‌حل‌ها (Symmetric design، Session sync، PBR) را مقایسه و انتخاب کند.
4. Failover بین فایروال‌ها را آزمون کند.
5. گزارش و Rubric تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا آزمون معماری ۵؟** یک سناریوی نامتقارن واقعی را از تشخیص تا رفع و اثبات دنبال می‌کند. روش پاسخ: ۱) شواهد (Sniffer دو سمت) ۲) علت ۳) راه‌حل متقارن ۴) آزمون مثبت و منفی ۵) ریسک راه‌حل.

**جمع‌بندی اصلی درس:**

با رشد سازمان یک مسیر دوم و فایروال دوم اضافه می‌شود. اگر مسیرها طراحی نشوند، بسته‌ی رفت از فایروال ۱ می‌رود و پاسخ از ۲ برمی‌گردد و Stateful آن را Drop می‌کند. معماری ۵ همین مسئله را در مقیاس چندفایروالی می‌سنجد.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

سایت اصلی دو فایروال (FW1، FW2) پشت دو ISP؛ سایت DR یک فایروال. شبکه‌ی داخلی 10.0.0.0/8 با OSPF. نیاز: خروج اینترنت از FW1 (ISP-A) و FW2 (ISP-B)؛ هر Session باید Symmetric باشد؛ خرابی یک فایروال بدون قطع طولانی.

#### ۲) طراحی مرجع

| مسئله | تصمیم |
|---|---|
| تقسیم ترافیک | بر اساس Source: Users→FW1، Servers→FW2 (PBR/Policy Route) |
| Return Path | NAT مبدأ در هر فایروال با IP خودش؛ برگشت خودکار از همان |
| Failover | OSPF Default از هر دو با Cost متفاوت؛ BFD |
| Asymmetric | آزمون Capture؛ Session sync فقط برای HA جفت |

``` text
FW1 default originate cost 10 ; FW2 default originate cost 20
Users 10.10.0.0/16 -> FW1 (PBR) ; Servers 10.20.0.0/16 -> FW2 (PBR)
```

#### ۳) خرابی‌ها و کلید

**A:** برخی Sessionها قطع. شاهد: Capture FW1 فقط SYN؛ FW2 فقط SYN-ACK. علت: Hash ECMP بین دو Default. رفع: PBR و Cost.

**B:** پس از Failover FW1 همه‌ی Sessionها ریست. علت: Session sync نیست (فایروال‌ها Cluster نیستند). پذیرش: ریست قابل‌قبول؛ برای حساس‌ها FGCP A-P.

**C:** ترافیک DR از مسیر اصلی می‌رود. علت: Cost OSPF. رفع: Policy Route و Cost.

#### ۴) آزمون

``` text
diagnose sniffer packet any 'host 10.10.0.5 and tcp port 443' 4 20 l   (on FW1 and FW2)
diagnose sys session list
get router info routing-table all
```

#### ۵) Rubric

طراحی ۲۰، جدول مسیر ۲۰، تشخیص ۳۰، Failover ۱۵، گزارش و صداقت ۱۵. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| تقسیم | Source-based |
| Failover | BFD+OSPF |
| Session sync | فقط جفت HA |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — تشخیص

شعبه با دو ISP و دو فایروال؛ کاربران گاهی به برنامه‌ی مرکزی نمی‌رسند. Sniffer: FW1 SYN/ACK؛ FW2 SYN-ACK.

#### مثال متوسط — رفع

SNAT به IP-A روی FW1؛ در صورت نیاز Policy Route؛ در A-A: Session Sync.

#### مثال سخت — اثبات و ریسک

``` text
for i in $(seq 1 100); do curl -s -o /dev/null -w "%{http_code}\n" https://app.example.com; done | sort | uniq -c
```

انتظار: ۱۰۰ × 200. ریسک SNAT: IP کاربر در سرور مقصد دیده نمی‌شود؛ جبران با Log فایروال. Rubric: تشخیص ۳۰، راه‌حل ۳۰، Evidence ۲۰، آزمون ۱۰، ریسک ۱۰.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Users از FW1: Session در FW1 با SNAT IP-A؛ برگشت همان؛ FW2 Session ندارد.

**متوسط (Asymmetric):** Capture: FW1 SYN، FW2 SYN-ACK. رفع: PBR Users→FW1 و OSPF Cost؛ Capture بعدی روی FW1 هر دو جهت.

**سخت (Failover):** FW1 خاموش: Users باید به FW2 بروند. مراحل: BFD تشخیص ۳ ثانیه؛ OSPF Default از FW2؛ Sessionهای فعال ریست؛ Sessionهای جدید از FW2؛ معیار: بازگشت سرویس < 10 ثانیه. ریسک: SNAT IP-B؛ لیست‌های مجاز مقصد باید IP-B را هم بپذیرند.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get router info routing-table all
diagnose sys session list
diagnose firewall proute list
```

### ۸) Verification (اثبات صحت)

- Capture Symmetric.
- Failover < 10 s.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Session قطع | Capture | PBR |
| DR از مسیر اصلی | Cost | Policy Route |

### ۱۰) نکات امنیتی

- SNAT دو IP را در لیست مجاز ثبت کنید.

### ۱۱) جمع‌بندی مفهومی

- Symmetric با طراحی.
- Failover BFD.
- Capture اثبات.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Source-based؟ *(پاسخ: 23-4-ت1)*

**ت2.** (ساده) BFD چه می‌کند؟ *(پاسخ: 23-4-ت2)*

**ت3.** (متوسط) علت قطع Session پس از Failover؟ *(پاسخ: 23-4-ت3)*

**ت4.** (متوسط) SNAT دوم چه ریسکی دارد؟ *(پاسخ: 23-4-ت4)*

**ت5.** (سخت) Capture دو سمتی. *(پاسخ: 23-4-ت5)*

**ت6.** (سخت، طراحی) سه‌فایروالی. *(پاسخ: 23-4-ت6)*

**Q1.** Quick quiz (English): How can you prove asymmetric routing with captures? *(پاسخ: 23-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| BFD | Bidirectional Forwarding Detection | تشخیص دوطرفه |

- *Keep each session on one firewall.* ← هر Session را روی یک فایروال نگه دارید.

### ۱۴) کارت Lab

**کارت Lab:** معماری ۵ (اجرا نشده). **Evidence:** `03-ops/arch5.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Routing; Session

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Rubric معماری ۵

تشخیص ۳۰، راه‌حل متقارن ۳۰، Evidence ۲۰، آزمون ۱۰، ریسک ۱۰.

**پرسش‌های مصاحبه**
1. *Evidence؟* Sniffer + Debug.
2. *ریسک راه‌حل؟* پیچیدگی.
3. *آزمون منفی؟* قطع یک مسیر.

### تکمیل عمیق: ارزیابی معماری ۵ — حل یک سناریوی نامتقارن کامل

#### چرا؟

این آزمون یک سناریوی واقعی را از تشخیص تا رفع و اثبات دنبال می‌کند.

#### صورت مسئله

شعبه با دو ISP و دو فایروال موازی؛ کاربران گاهی به برنامه‌ی مرکزی نمی‌رسند.

#### گام ۱ — شواهد

``` text
FW1 sniffer: SYN, ACK seen ; no SYN-ACK
FW2 sniffer: SYN-ACK seen ; no SYN
```

#### گام ۲ — علت

رفت از ISP-A/FW1 و برگشت از ISP-B/FW2.

#### گام ۳ — راه‌حل‌ها

1. SNAT به IP-A روی FW1 (برگشت از ISP-A).
2. در صورت نیاز Policy Route برای منابع.
3. اگر Active-Active لازم است ⇒ Session Sync.

#### گام ۴ — اثبات

Sniffer نشان دهد هر دو جهت از یک FW؛ `curl` ۱۰۰ بار بدون خطا.

``` text
for i in $(seq 1 100); do curl -s -o /dev/null -w "%{http_code}\n" https://app.example.com; done | sort | uniq -c
```

انتظار: 100 × 200.

#### Rubric

``` text
Diagnosis 30 | Symmetric solution 30 | Evidence 20 | Negative/regression test 10 | Risks 10
```

#### مثال سخت — ریسک راه‌حل

SNAT پنهان می‌کند IP واقعی کاربر در Log سرور مقصد (همه‌ی کاربران یک IP). ریسک ردیابی؛ جبران: Log فایروال با Session و ثبت NAT.

#### Lab

سناریو را شبیه‌سازی کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| درصدی خطا | مسیر دوم | بررسی Route |
| IP کاربر دیده نمی‌شود | SNAT | Log فایروال |
| Sync کند | لینک | ارتقا |

#### پرسش‌ها با پاسخ

**۱. چرا ۱۰۰ بار؟** خطای متناوب.
**۲. ریسک SNAT؟** ردیابی.
**۳. شاهد اصلی؟** Sniffer دوطرفه.

#### English Corner

- *Run repeated tests when the failure is intermittent.*
- Q: What is the trade-off of using SNAT to fix asymmetry?

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

NAT فقط روی Edge: Log و عیب‌یابی ساده می‌ماند و IP واقعی کاربر در Internal حفظ می‌شود.

**23-3-ت2** — دامنه‌ی اثر یک خطا/خرابی.

Blast radius دامنه‌ی اثر یک خطا یا خرابی است؛ جداسازی آن را کم می‌کند.

**23-3-ت3** — Canary ابتدا روی یک دستگاه؛ اگر سالم بود ادامه؛ تغییر هم‌زمان خطا را همه‌جا ایجاد می‌کند.

**23-3-ت4** — Diff پیکربندی دو فایروال پس از هر تغییر و به‌صورت دوره‌ای؛ Alert.

**23-3-ت5** — Hash/Routing متقارن یا Sync، Policy یکسان، Log مرکزی/زمان، Failover آزمایش‌شده.

**23-3-ت6** — سری (Edge+Internal)، هر لایه A-P؛ Edge برای ظرفیت N+1 با ECMP متقارن اگر لازم؛ معیارها: ریسک، هزینه، عملیات.

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

**23-4-ت5** — فیلتر Host روی هر دو.

Capture دو سمتی: Host فیلتر روی هر دو فایروال و مقایسه‌ی جهت‌ها.

**23-4-ت6** — جدول.

طرح سه‌فایروالی: جدول نقش، مسیر، Failover و آزمون Asymmetric.

**23-4-Q1** — By capturing on both firewalls and showing each sees only one direction.

### پاسخ‌های درس افزوده‌ی 23-0 (فصل 23)

**23-0-ت1** — رفت و برگشت یک ارتباط از دو مسیر/دستگاه متفاوت.

Asymmetric: رفت و برگشت یک ارتباط از دو مسیر/دستگاه متفاوت.

**23-0-ت2** — چون برگشتی بدون Session مطابق Handshake نیست (و/یا RPF fail) و رد می‌شود.

**23-0-ت3** — پیام reverse path check fail, drop.

پیام Debug flow: `reverse path check fail, drop` در ترافیک نامتقارن.

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

| علامت | علت | رفع |
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

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. تفاوت North-South و East-West را بگوید و ریسک East-West را توضیح دهد.
2. Zoneها و Trust Level را برای DC طراحی کند.
3. Flow Discovery را با Log و Sniffer اجرا و Matrix واقعی بسازد.
4. Policy Matrix حداقلی بنویسد و Rollout تدریجی را برنامه‌ریزی کند.
5. Evidence و ریسک‌ها را مستند کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا East-West؟** اغلب حملات واقعی پس از نفوذ اولیه با **حرکت جانبی** ادامه می‌یابند: مهاجم از یک سرور وب به بقیه‌ی سرورها می‌رود. فایروال لبه فقط ترافیک شمال–جنوب (ورود/خروج از سازمان) را می‌بیند؛ ترافیک بین سرورها (شرق–غرب) را باید با Segmentation کنترل کرد.

**Segmentation:** شبکه را به بخش‌های با سطح اعتماد متفاوت تقسیم کنید (Web < App < DB < Mgmt) و بین آنها Policy حداقلی بگذارید. **Flow Discovery:** پیش از Deny، جریان‌های واقعی را در یک دوره‌ی کامل (ترجیحاً یک ماه) با Log کشف کنید تا برنامه‌ای (مثل Job فصلی) را نبندید.

**جمع‌بندی اصلی درس:**

بیشتر ترافیک DC شرق-غربی است (سرور به سرور)، نه از اینترنت. حمله‌های واقعی بعد از ورود از وب‌سرور به سمت سرورهای دیگر حرکت می‌کنند. Segmentation همان دیوارهای داخلی است. ولی نوشتن Policy قبل از دانستن جریان‌ها یعنی قطع سرویس؛ پس اول کشف (Flow Discovery) و بعد سیاست.

### ۳) توضیح عمیق فنی

#### ۱) North-South در برابر East-West

North-South: ورود/خروج DC. East-West: بین سرورهای داخلی. فایروال لبه East-West را نمی‌بیند؛ Segmentation داخلی لازم است.

#### ۲) Zone و Trust

| Zone | Trust | نمونه |
|---|---|---|
| WEB | کم | وب‌سرور |
| APP | متوسط | App |
| DB | بالا | پایگاه داده |
| MGMT | بالا | مدیریت |
| BACKUP | بالا | Backup |

#### ۳) Flow Discovery

``` text
# 1) turn on logging all on a permissive 'discovery' policy for 14 days
# 2) export unique src/dst/port from logs
# 3) classify: needed / unknown / suspicious
```

نمونه خروجی:

``` text
WEB -> APP : tcp/8443 (2.1M sessions)
APP -> DB  : tcp/1433 (900k)
WEB -> DB  : tcp/1433 (12)   <- suspicious, investigate
```

#### ۴) Matrix حداقلی

| از ↓ به → | WEB | APP | DB | MGMT |
|---|---|---|---|---|
| Internet | 443 | - | - | - |
| WEB | - | 8443 | - | - |
| APP | - | - | 1433 | - |
| MGMT | SSH | SSH | SSH | - |

#### ۵) Rollout

مرحله‌ای: ابتدا Policy Allow با Log (Monitor)، بعد Deny با Log فقط برای «suspicious»، سپس Default Deny. هر مرحله یک هفته و Rollback آماده.

#### ۶) ریسک

قطع سرویس ناشناخته (Batch شبانه، Backup)؛ پوشش با Log ۳۰ روزه و مشورت مالکان.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Rollout | Monitor → Deny → Default Deny |
| Log | ۳۰ روز |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — ماتریس

| از | به | سرویس |
|---|---|---|
| Web | App | tcp/8443 |
| App | DB | tcp/5432 |
| Mgmt | همه | SSH/HTTPS |

هرچه در ماتریس نیست ⇒ Deny.

#### مثال متوسط — Flow Discovery

۲ هفته Log در حالت Monitor؛ فهرست مبدأ/مقصد/پورت؛ سپس Policy دقیق و در پایان Deny.

#### مثال سخت — Job فصلی

گزارش پایان ماه پس از Segmentation قطع شد؛ در ۲ هفته‌ی مشاهده دیده نشده بود. درس: دوره‌ی کامل، تماس با مالکان سرویس‌ها و حالت Monitor قبل از Deny.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** Log: WEB→DB 12 Session؛ مشکوک؛ بررسی: اسکریپت قدیمی؛ حذف دسترسی و مستندسازی.

**متوسط (Matrix):** از Log ۱۴ روزه: ۴ مسیر مجاز؛ Matrix 4 خانه؛ بقیه Deny با Log؛ هفته‌ی اول فقط Monitor.

**سخت (Backup شبانه):** پس از Deny، Backup شبانه قطع شد. مراحل: ۱) Log deny: BACKUP→DB 445 ساعت 02:00. ۲) در Discovery ۱۴ روز ثبت نشده بود (Backup هفتگی). ۳) افزودن Policy. درس: Log حداقل ۳۰ روز و مشورت مالک.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute log filter field srcintf WEB
execute log display
```

### ۸) Verification (اثبات صحت)

- Matrix با Log.
- آزمون منفی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| سرویس قطع | Log deny | افزودن Policy |

### ۱۰) نکات امنیتی

- Default Deny با Log.

### ۱۱) جمع‌بندی مفهومی

- East-West ریسک اصلی.
- Flow Discovery.
- Rollout مرحله‌ای.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) East-West چیست؟ *(پاسخ: 24-1-ت1)*

**ت2.** (ساده) چرا Flow Discovery؟ *(پاسخ: 24-1-ت2)*

**ت3.** (متوسط) چرا Rollout مرحله‌ای؟ *(پاسخ: 24-1-ت3)*

**ت4.** (متوسط) WEB→DB مشکوک؟ *(پاسخ: 24-1-ت4)*

**ت5.** (سخت) Backup شبانه قطع شد. *(پاسخ: 24-1-ت5)*

**ت6.** (سخت، طراحی) Matrix DC. *(پاسخ: 24-1-ت6)*

**Q1.** Quick quiz (English): Why is east-west traffic a major risk in data centers? *(پاسخ: 24-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Lateral movement | Lateral movement | حرکت جانبی |

- *Discover flows before enforcing policies.* ← قبل از اعمال Policy جریان‌ها را کشف کنید.

### ۱۴) کارت Lab

**کارت Lab:** Segmentation (اجرا نشده). **Evidence:** `02-design/dc-matrix.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Firewall policies
- NIST SP 800-125B

<a id="l-24-2"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: East-West

Flow Discovery: Log ۲ هفته برای شناخت جریان‌ها؛ سپس Policy حداقلی. Trust Level: Web < App < DB.

**پرسش‌های مصاحبه**
1. *چرا East-West؟* حرکت جانبی.
2. *Zone؟* گروه Interface.
3. *Intra-zone؟* پیش‌فرض رد/مجاز طبق تنظیم.

### تکمیل عمیق: East-West، Segmentation و کشف جریان‌ها

#### چرا؟

بیشتر حملات واقعی پس از نفوذ اولیه با **حرکت جانبی** (Lateral Movement) ادامه می‌یابند: مهاجم از یک سرور وب به بقیه‌ی سرورها می‌رود. فایروال لبه فقط ترافیک شمال–جنوب را می‌بیند. East-West یعنی ترافیک بین سرورها/ Zoneهای داخلی؛ باید آن را هم کنترل کرد.

#### توضیح ساده

Segmentation یعنی شبکه را به بخش‌هایی با «سطح اعتماد» متفاوت تقسیم کنیم و ترافیک بین آنها فقط با Policy حداقلی عبور کند.

| Zone | سطح اعتماد |
|---|---|
| Mgmt | بالاترین |
| DB | بالا |
| App | متوسط |
| Web | پایین |
| Guest | کمترین |

قاعده: ارتباط از اعتماد پایین به بالا فقط در صورت نیاز و از مسیر مشخص.

#### مثال ساده — ماتریس نیاز

| از | به | سرویس |
|---|---|---|
| Web | App | tcp/8443 |
| App | DB | tcp/5432 |
| Mgmt | همه | SSH/HTTPS |

هرچه در ماتریس نیست ⇒ Deny.

#### مثال متوسط — کشف جریان (Flow Discovery)

پیش از نوشتن Policy، ۲ هفته Log را در حالت «Allow همه + Log» (در Lab/مرحله‌ی یادگیری) جمع کنید و جریان‌های واقعی را فهرست کنید.

``` text
execute log filter category 0
execute log filter field srcintf "port-app"
execute log display | summarize by dstip,dstport
```

بعد از مشاهده، Policyهای دقیق را بنویسید و در پایان Deny.

#### مثال سخت — جریان‌های فراموش‌شده

پس از Segmentation، گزارش ماهانه‌ی پایان ماه قطع می‌شود؛ علت: Job فصلی که در ۲ هفته‌ی مشاهده دیده نشد. راه: مشاهده‌ی چرخه‌ی کامل (۱ ماه)، تماس با مالکان سرویس‌ها، و دوره‌ی «Monitor» با Log قبل از Deny.

#### Lab

سه Zone بسازید، Policy حداقلی بنویسید و آزمون منفی Web→DB را انجام دهید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| قطع برنامه | جریان فراموش‌شده | Log + افزودن |
| Policy زیاد | رشد کنترل‌نشده | مالک و بازبینی |
| Intra-zone باز | تنظیم Zone | `intrazone deny` |

#### پرسش‌ها با پاسخ

**۱. Lateral Movement چیست؟** حرکت جانبی مهاجم.
**۲. چرا کشف جریان؟** Policy بر اساس واقعیت.
**۳. Intrazone؟** ترافیک داخل یک Zone.

#### English Corner

- *East-west traffic needs the same scrutiny as north-south.*
- Q: How do you discover legitimate flows before enforcing deny?

## درس 24-2 — Policy حداقلی Web/App/DB: ماتریس، پیاده‌سازی و آزمون Isolation

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۱، ۱۵-۴ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Policyهای حداقلی بین سه لایه را با Object و Service مشخص بنویسد.
2. Deny صریح با Log را بین لایه‌ها بسازد.
3. آزمون مثبت/منفی را اجرا و Evidence کند.
4. Hit Count و Log را برای ممیزی بخواند.
5. خطاهای رایج را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Policy حداقلی؟** «حداقل دسترسی» با عمل ثابت می‌شود: Policyهایی که فقط جریان‌های لازم را باز می‌کنند و آزمونی که نشان می‌دهد بقیه بسته است. برای هر Policy یک آزمون مثبت و برای خانه‌های خالی ماتریس آزمون منفی.

**محدودیت:** Policy شبکه فقط یک لایه است؛ مهاجمی که Web را هک کرده از مسیر مجاز App به DB هم می‌رسد؛ پس حساب DB با کمترین مجوز، WAF/IPS و Log لازم است.

**جمع‌بندی اصلی درس:**

ماتریس روی کاغذ تا وقتی Policy نشده تأثیری ندارد. این درس ماتریس ۲۴-۱ را به Policy تبدیل می‌کند و ثابت می‌کند Isolation واقعی است.

### ۳) توضیح عمیق فنی

#### ۱) Objectها

``` text
config firewall address
 edit "SRV-WEB"
  set subnet 10.30.1.10 255.255.255.255
 next
 edit "SRV-APP"
  set subnet 10.30.2.10 255.255.255.255
 next
 edit "SRV-DB"
  set subnet 10.30.3.10 255.255.255.255
 next
end
config firewall service custom
 edit "TCP-8443"
  set tcp-portrange 8443
 next
end
```

#### ۲) Policyها

``` text
config firewall policy
 edit 50
  set name "WEB-to-APP"
  set srcintf "ZN-WEB"
  set dstintf "ZN-APP"
  set srcaddr "SRV-WEB"
  set dstaddr "SRV-APP"
  set action accept
  set schedule "always"
  set service "TCP-8443"
  set logtraffic all
 next
 edit 60
  set name "APP-to-DB"
  set srcintf "ZN-APP"
  set dstintf "ZN-DB"
  set srcaddr "SRV-APP"
  set dstaddr "SRV-DB"
  set action accept
  set schedule "always"
  set service "MS-SQL"
  set logtraffic all
 next
 edit 61
  set name "DENY-WEB-to-DB"
  set srcintf "ZN-WEB"
  set dstintf "ZN-DB"
  set srcaddr "all"
  set dstaddr "all"
  set action deny
  set logtraffic all
 next
end
```

#### ۳) آزمون

| # | آزمون | انتظار |
|---|---|---|
| 1 | WEB→APP 8443 | Accept (50) |
| 2 | APP→DB 1433 | Accept (60) |
| 3 | WEB→DB 1433 | Deny (61) |
| 4 | WEB→APP 22 | Deny (Default) |
| 5 | DB→Internet | Deny |

``` text
diagnose firewall iprope lookup 10.30.1.10 40000 10.30.3.10 1433 tcp ZN-WEB
```

#### ۴) Evidence

برای هر آزمون: دستور، نتیجه، Log (policyid، action)، زمان.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Deny صریح | برای Alert |
| Object | Host-level |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

``` text
Policy WEB-to-APP  ZN-WEB -> ZN-APP  tcp/8443  accept log
Policy APP-to-DB   ZN-APP -> ZN-DB   tcp/5432  accept log
Policy DENY-ALL    any -> any        deny log
```

#### مثال متوسط — آزمون

``` text
from WEB: nc -zv APP 8443    # open
from WEB: nc -zv DB 5432     # timeout (negative)
diagnose firewall iprope lookup <WEB> 40000 <DB> 5432 tcp ZN-WEB   # policy DENY-ALL
```

#### مثال سخت — دور زدن از مسیر مجاز

حمله از Web → App (مجاز) → DB. کاهش: حساب DB با کمترین مجوز، IPS/WAF، پایش Query غیرعادی، Rate.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** WEB→DB: Lookup policy 61؛ telnet Timeout؛ Log deny.

**متوسط (Shadow):** Policy 61 زیر ALL قدیمی؛ Lookup ID قدیمی؛ جابه‌جایی؛ آزمون منفی.

**سخت (ممیزی):** Hit Count: Policy 50 با ۲M، 60 با ۹۰۰k، 61 با ۱۲ (تلاش‌ها). ۱۲ تلاش با Source مشخص بررسی؛ نتیجه: اسکریپت قدیمی؛ مستند.

### ۷) پیاده‌سازی از مسیر CLI

``` text
show firewall policy 61
diagnose firewall iprope lookup 10.30.1.10 40000 10.30.3.10 1433 tcp ZN-WEB
```

### ۸) Verification (اثبات صحت)

- آزمون ۵‌گانه.
- Log.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Web به DB می‌رسد | Lookup | Policy ALL |

### ۱۰) نکات امنیتی

- Least privilege.

### ۱۱) جمع‌بندی مفهومی

- Policy از ماتریس.
- Deny صریح.
- Evidence.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Object Host-level؟ *(پاسخ: 24-2-ت1)*

**ت2.** (ساده) Deny صریح؟ *(پاسخ: 24-2-ت2)*

**ت3.** (متوسط) آزمون منفی؟ *(پاسخ: 24-2-ت3)*

**ت4.** (متوسط) Lookup؟ *(پاسخ: 24-2-ت4)*

**ت5.** (سخت) Hit Count ۱۲؟ *(پاسخ: 24-2-ت5)*

**ت6.** (سخت، طراحی) Policy سه‌لایه. *(پاسخ: 24-2-ت6)*

**Q1.** Quick quiz (English): Why use host-level address objects between tiers? *(پاسخ: 24-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Least privilege | Least privilege | حداقل دسترسی |

- *Test the denied flows too.* ← جریان‌های ردشده را هم آزمون کنید.

### ۱۴) کارت Lab

**کارت Lab:** Policy سه‌لایه (اجرا نشده). **Evidence:** `02-design/dc-policy.md`.

### ۱۵) منابع

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

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: ماتریس Web/App/DB

| از | به | سرویس |
|---|---|---|
| Web | App | tcp/8443 |
| App | DB | tcp/5432 |

هر سطر یک Policy؛ آزمون منفی Web→DB.

**پرسش‌های مصاحبه**
1. *Policy تعداد؟* به‌اندازه‌ی نیاز.
2. *Log؟* All.
3. *Hit Count؟* بازبینی.

### تکمیل عمیق: Policy حداقلی Web/App/DB — پیاده‌سازی و آزمون منفی

#### چرا؟

«حداقل دسترسی» (Least Privilege) تنها در عمل ثابت می‌شود: Policyهایی که فقط همان جریان‌های لازم را باز می‌کنند و آزمونی که نشان می‌دهد بقیه بسته است.

#### پیاده‌سازی

``` text
config firewall policy
 edit 100
  set name "WEB-to-APP"
  set srcintf "ZN-WEB"
  set dstintf "ZN-APP"
  set srcaddr "GRP-WEB"
  set dstaddr "GRP-APP"
  set service "APP-8443"
  set action accept
  set logtraffic all
 next
 edit 110
  set name "APP-to-DB"
  set srcintf "ZN-APP"
  set dstintf "ZN-DB"
  set srcaddr "GRP-APP"
  set dstaddr "GRP-DB"
  set service "PGSQL"
  set action accept
  set logtraffic all
 next
 edit 190
  set name "DENY-ALL"
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

#### آزمون مثبت و منفی

``` text
from WEB: nc -zv 10.30.2.10 8443      # expect open
from WEB: nc -zv 10.30.3.10 5432      # expect timeout (negative test)
from APP: nc -zv 10.30.3.10 5432      # expect open
diagnose firewall iprope lookup 10.30.1.5 40000 10.30.3.10 5432 tcp ZN-WEB   # expect deny policy 190
```

#### مثال متوسط — Address Group

به‌جای IP تکی از Group استفاده کنید تا افزودن سرور جدید فقط عضوشدن در Group باشد (Standard Change).

#### مثال سخت — دور زدن از مسیر دوم

مهاجم از Web به DB مستقیم نمی‌رسد ولی از طریق App (که Policy دارد) می‌تواند Query بزند. جلوگیری کامل غیرممکن است؛ کاهش: Application-level (WAF/IPS)، حساب DB با کمترین مجوز، Log برای Query غیرعادی. توجه: Policy شبکه فقط یکی از لایه‌هاست.

#### Lab

سه Zone و ۳ Policy بالا را بسازید و چهار آزمون بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Web به DB وصل می‌شود | Policy گسترده | تنگ‌سازی |
| App به DB نمی‌رسد | Service/Route | Lookup |
| Log زیاد | all روی همه | تنظیم |

#### پرسش‌ها با پاسخ

**۱. چرا آزمون منفی؟** اثبات بسته‌بودن.
**۲. Group چرا؟** مدیریت ساده.
**۳. محدودیت Policy شبکه؟** لایه‌ی کاربرد را نمی‌بیند.

#### English Corner

- *Prove that what should be blocked is actually blocked.*
- Q: Why use address groups in segmentation policies?

## درس 24-3 — Lab عملی VDOM: ساخت، Inter-VDOM Link، Policy و محدودیت منابع

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۱، ۲۴-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ دستورها طبق مستندات 7.0 ولی `Unverified` تا اجرای Lab؛ Lab «اجرا نشده»؛ HA/VDOM وابسته به مدل/لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. VDOM را فعال و VDOM جدید بسازد (Multi-VDOM).
2. Inter-VDOM Link را بسازد و Routing/Policy بین VDOMها بنویسد.
3. Resource Limit (Session، Policy) برای هر VDOM تنظیم کند.
4. Management VDOM و Global را تفکیک کند.
5. محدودیت‌های لایسنس و خطاهای رایج را بداند.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا Lab VDOM؟** تا خودتان نسازید ایزولاسیون را نمی‌فهمید. مراحل: ساخت VDOM، تخصیص Interface، Inter-VDOM Link، Route، Policy و آزمون. به نکات: هر VDOM Admin جدا، Backup هم Global هم VDOM، ارتقای نسخه همه‌ی VDOMها را هم‌زمان درگیر می‌کند.

**جمع‌بندی اصلی درس:**

VDOM (Virtual Domain) یک فایروال فیزیکی را به چند فایروال مجازی مستقل تقسیم می‌کند؛ هر VDOM Interface، Route و Policy خودش را دارد. استفاده: جداسازی مشتری یا بخش (DMZ، Internal). هزینه: پیچیدگی و محدودیت لایسنس (Needs-License؛ پیش‌فرض ۱۰ VDOM در بسیاری مدل‌ها).

### ۳) توضیح عمیق فنی

#### ۱) فعال‌سازی

``` text
config system global
 set vdom-mode multi-vdom
end
```

فعال‌سازی سرویس را برای لحظه‌ای قطع و GUI را ریست می‌کند؛ در Window.

#### ۲) ساخت VDOM

``` text
config vdom
 edit "DMZ"
 next
 edit "INT"
 next
end
config global
 config system interface
  edit "port3"
   set vdom "DMZ"
  next
  edit "port2"
   set vdom "INT"
  next
 end
end
```

#### ۳) Inter-VDOM Link

``` text
config global
 config system vdom-link
  edit "vlk"
   set type ethernet
  next
 end
 config system interface
  edit "vlk0"
   set vdom "DMZ"
   set ip 10.255.1.1 255.255.255.252
  next
  edit "vlk1"
   set vdom "INT"
   set ip 10.255.1.2 255.255.255.252
  next
 end
end
```

(در 7.0 ساختار `vdom-link` با Type Ethernet/PPP؛ `Unverified`.)

#### ۴) Routing و Policy

در هر VDOM Route به شبکه‌ی VDOM دیگر از طریق vlk و Policy مربوطه. بین VDOMها Policy برای هر دو جهت.

#### ۵) Resource Limit

``` text
config global
 config system vdom-property
  edit "DMZ"
   set session 200000
   set policy 500
  next
 end
end
```

#### ۶) Management

Management VDOM (معمولاً root) برای Admin/FortiGuard؛ ترافیک سرویس‌ها از آن VDOM. Admin per-VDOM با Profile محدود.

#### ۷) خطاها

- Interface در VDOM اشتباه ⇒ Policy پیدا نمی‌شود.
- DNS/FortiGuard از VDOM غیر Management کار نمی‌کند.
- لایسنس VDOM محدود.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| VDOM | فقط در صورت نیاز جداسازی |
| Resource | Limit هر VDOM |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده — تخصیص

``` text
config global
 config system interface
  edit port2
   set vdom TENANT-A
  next
  edit port3
   set vdom TENANT-B
  next
 end
end
```

#### مثال متوسط — Link

Link `A-B` با 10.99.60.1/30 و 10.99.60.2/30، Route دو سر و Policy فقط 443.

#### مثال سخت — آزمون

``` text
from A: curl -m 3 https://10.60.2.10    # OK
from A: ping 10.60.2.10                 # fail (not allowed)
```

اگر ping جواب داد، Policy بیش‌ازحد باز است.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** DMZ و INT ساخته؛ port3 به DMZ، port2 به INT؛ `get system status` Virtual domain: enable.

**متوسط (Inter-VDOM):** DMZ→INT ping ندارد. مراحل: ۱) vlk0 در DMZ و vlk1 در INT IP دارند. ۲) Route در هر VDOM. ۳) Policy هر دو جهت. ۴) ping ok.

**سخت (Resource):** VDOM DMZ تمام Session را مصرف می‌کند. مراحل: ۱) `vdom-property` session 200000. ۲) آزمون بار. ۳) هشدار Resource. معیار: INT تحت‌تأثیر نیست.

### ۶) پیاده‌سازی از مسیر GUI

1. System → Settings: Virtual Domains Enable.
2. Global → Virtual Domains → Create New.
3. Network → Interfaces → Inter-VDOM Link.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config global
 config system vdom-link
  edit "vlk"
  next
 end
end
get system status
```

### ۸) Verification (اثبات صحت)

- VDOMها و Interfaceها.
- ping بین VDOMها.
- Limit.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Policy پیدا نمی‌شود | VDOM Interface | اصلاح |
| FortiGuard کار نمی‌کند | Management VDOM | root |

### ۱۰) نکات امنیتی

- Admin per-VDOM.

### ۱۱) جمع‌بندی مفهومی

- VDOM=فایروال مجازی.
- Inter-VDOM Link.
- Limit.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) VDOM چیست؟ *(پاسخ: 24-3-ت1)*

**ت2.** (ساده) Inter-VDOM Link؟ *(پاسخ: 24-3-ت2)*

**ت3.** (متوسط) چرا Resource Limit؟ *(پاسخ: 24-3-ت3)*

**ت4.** (متوسط) Management VDOM؟ *(پاسخ: 24-3-ت4)*

**ت5.** (سخت) ping بین VDOM ندارد. *(پاسخ: 24-3-ت5)*

**ت6.** (سخت، طراحی) دو VDOM. *(پاسخ: 24-3-ت6)*

**Q1.** Quick quiz (English): What is the purpose of an inter-VDOM link? *(پاسخ: 24-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| VDOM | Virtual Domain | دامنه‌ی مجازی |

- *Limit the resources of each VDOM.* ← منابع هر VDOM را محدود کنید.

### ۱۴) کارت Lab

**کارت Lab:** VDOM (اجرا نشده؛ Needs-License). **Evidence:** `02-design/vdom-lab.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Virtual Domains

<a id="l-24-4"></a>

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Lab VDOM

مراحل: ساخت VDOM، اختصاص Interface، Inter-VDOM Link، Route، Policy، آزمون. محدودیت: هر VDOM Admin جدا.

``` text
config vdom
 edit TENANT-A
  config system interface
   edit A-LINK0
   next
  end
end
```

**پرسش‌های مصاحبه**
1. *VDOM Link؟* Interface مجازی دو سر.
2. *Admin Profile؟* محدوده.
3. *Backup؟* Global.

### تکمیل عمیق: Lab عملی VDOM — مرحله‌به‌مرحله

#### چرا؟

VDOM را تا وقتی خودتان نسازید، درک نمی‌کنید که ایزولاسیون یعنی چه. این Lab با Checkpoint نوشته شده تا در هر گام بدانید درست است.

#### توپولوژی

``` text
TENANT-A: port2 10.60.1.1/24  <->  A-B0 10.99.60.1/30
TENANT-B: port3 10.60.2.1/24  <->  A-B1 10.99.60.2/30
```

#### گام ۱ — ساخت VDOM و اختصاص Interface

``` text
config vdom
 edit TENANT-A
 next
 edit TENANT-B
 next
end
config global
 config system interface
  edit port2
   set vdom TENANT-A
  next
  edit port3
   set vdom TENANT-B
  next
 end
end
```

Checkpoint: `get system interface` در هر VDOM فقط Interface خودش را نشان دهد.

#### گام ۲ — Inter-VDOM Link

``` text
config global
 config system vdom-link
  edit "A-B"
  next
 end
 config system interface
  edit "A-B0"
   set vdom TENANT-A
   set ip 10.99.60.1 255.255.255.252
  next
  edit "A-B1"
   set vdom TENANT-B
   set ip 10.99.60.2 255.255.255.252
  next
 end
end
```

#### گام ۳ — Route و Policy

در TENANT-A: Route به 10.60.2.0/24 از طریق 10.99.60.2؛ در TENANT-B: مسیر برگشت. Policy فقط برای یک سرویس (مثلاً tcp/443).

#### گام ۴ — آزمون

``` text
from A: curl -m 3 https://10.60.2.10   # expect OK
from A: ping 10.60.2.10                # expect fail (not allowed)
```

#### مثال سخت — محدودیت‌ها

VDOM‌ها یک سخت‌افزار و یک نسخه‌ی مشترک دارند؛ ارتقا همه را هم‌زمان درگیر می‌کند. Config هر VDOM جدا Backup می‌شود (Backup VDOM-مبنا). نقش ادمین: `Prof-admin` با `vdom` مشخص.

#### Lab

Lab را کامل کنید و سه شاهد (Interface، Route، Log) ثبت کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Link Down | VDOM اشتباه | بررسی |
| ping جواب می‌دهد | Policy بیش‌ازحد | تنگ‌سازی |
| Route نیست | VDOM اشتباه | اضافه‌کردن |

#### پرسش‌ها با پاسخ

**۱. هر VDOM Route جدا؟** بله.
**۲. ارتقا؟** هم‌زمان.
**۳. ادمین محدود؟** با Profile.

#### English Corner

- *Inter-VDOM traffic requires explicit policy on both sides.*
- Q: What is shared between VDOMs?

## درس 24-4 — Logging Data Center و Gate G9: اثبات Isolation، آزمون منفی، Alert و مستندسازی

**فصل 24 · بازنویسی عمیق · پیش‌نیاز: ۲۴-۱ تا ۲۴-۳ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Logging Policy برای DC (Forward Traffic، Event، UTM) را طراحی کند.
2. آزمون Isolation مثبت/منفی را اجرا و از Log اثبات کند.
3. Alert برای تلاش‌های ممنوع بسازد.
4. گزارش Evidence و Rubric G9 را تحویل دهد.

### ۲) مفهوم پایه: چیست و چرا؟ (از صفر، با زبان ساده)

**چرا G9؟** ایزولاسیون بدون اثبات ادعاست. G9 از شما می‌خواهد با آزمون منفی و Log ثابت کنید دو مستأجر جدا هستند و منابع محدودند.

**جمع‌بندی اصلی درس:**

امنیت Data Center بدون Log اثبات‌پذیر نیست. ادعای «وب به DB دسترسی ندارد» تا وقتی Log آزمون منفی را نشان ندهد، فقط ادعاست. G9 همین اثبات را می‌خواهد.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

DC با Zoneهای WEB، APP، DB و MGMT. نیاز: Policy حداقلی، آزمون Isolation، Log متمرکز (Syslog/FortiAnalyzer)، Alert روی Deny بین لایه‌ها، گزارش.

#### ۲) Logging

``` text
config log syslogd setting
 set status enable
 set server 10.99.0.20
 set port 514
 set facility local7
end
config firewall policy
 edit 61
  set logtraffic all
 next
end
```

(`Unverified`.) برای FortiAnalyzer: `config log fortianalyzer setting` (Needs-License اگر Appliance/VM).

#### ۳) ماتریس آزمون (مثبت/منفی)

| # | آزمون | انتظار | Log |
|---|---|---|---|
| 1 | Internet→WEB 443 | Accept | policyid VIP |
| 2 | WEB→APP 8443 | Accept | policy 50 |
| 3 | APP→DB 1433 | Accept | policy 60 |
| 4 | WEB→DB 1433 | Deny | policy Deny |
| 5 | DB→Internet | Deny | policy Deny |
| 6 | MGMT→WEB SSH | Accept | policy 70 |
| 7 | WEB→MGMT | Deny | policy Deny |

#### ۴) Alert

``` text
Alert: action=deny and (srcintf=WEB and dstintf=DB) count>=5 in 5 min -> notify SOC
```

#### ۵) نمونه Log

``` text
date=2026-11-26 time=11:02:10 type="traffic" subtype="forward" srcip=10.30.1.10 dstip=10.30.3.10 dstport=1433 policyid=61 action="deny"
```

#### ۶) Rubric

طراحی Log ۱۵، آزمون ۷ مورد ۳۰، Alert ۲۰، Evidence ۲۰، گزارش و صداقت ۱۵. قبولی ۷۵.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Log | Deny همیشه؛ Accept حساس |
| Alert | روی Deny بین لایه‌ها |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

#### مثال ساده

``` text
from TENANT-A host: nc -zv 10.60.2.10 22   # expect timeout
diagnose firewall iprope lookup ... -> deny
```

#### مثال متوسط — Log هر VDOM

Syslog با فیلد `vd=` برای جداسازی.

#### مثال سخت — نقض

Policy قدیمی `all` بین مستأجران پیدا شد؛ Disable، بازبینی همه‌ی Policyهای Inter-VDOM، Evidence و PIR. Rubric: Isolation ۳۰، Least-privilege ۲۵، Logging ۲۰، منابع ۱۵، گزارش ۱۰.

#### مثال‌های اصلی درس (مرور)

**ساده (حل‌شده):** آزمون ۴: telnet 10.30.3.10 1433 از WEB؛ Timeout؛ Log: action=deny policyid=61؛ ثبت Evidence.

**متوسط (Alert):** ۶ تلاش WEB→DB در ۲ دقیقه؛ Alert ارسال؛ SOC بررسی؛ تشخیص Scan؛ Quarantine وب‌سرور؛ زمان تشخیص ۳ دقیقه.

**سخت (Log ناقص):** Log Deny DB→Internet نیست. مراحل: ۱) Policy Deny صریح با Log ندارد. ۲) Implicit Deny بی‌Log. ۳) افزودن Policy Deny با Log. ۴) آزمون ۵ دوباره Log دارد. درس: Implicit Deny Log ندارد.

### ۷) پیاده‌سازی از مسیر CLI

``` text
execute log filter field policyid 61
execute log display
```

### ۸) Verification (اثبات صحت)

- هر ۷ آزمون Log دارد.
- Alert ارسال شد.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Log Deny نیست | Policy Deny صریح | Log |
| Alert نمی‌آید | فیلتر/Threshold | اصلاح |

### ۱۰) نکات امنیتی

- Log را متمرکز کنید.

### ۱۱) جمع‌بندی مفهومی

- Isolation با Log اثبات می‌شود.
- Alert روی Deny.
- Evidence.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا Deny صریح با Log؟ *(پاسخ: 24-4-ت1)*

**ت2.** (ساده) Isolation را چگونه اثبات می‌کنید؟ *(پاسخ: 24-4-ت2)*

**ت3.** (متوسط) Alert چه شرطی دارد؟ *(پاسخ: 24-4-ت3)*

**ت4.** (متوسط) Log کجا؟ *(پاسخ: 24-4-ت4)*

**ت5.** (سخت) Log ناقص. *(پاسخ: 24-4-ت5)*

**ت6.** (سخت، طراحی) ماتریس آزمون DC. *(پاسخ: 24-4-ت6)*

**Q1.** Quick quiz (English): Why is a negative test needed to prove isolation? *(پاسخ: 24-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SOC | Security Operations Center | مرکز عملیات امنیت |

- *Isolation must be proven with logs.* ← ایزولاسیون باید با Log اثبات شود.

### ۱۴) کارت Lab

**کارت Lab:** G9 (اجرا نشده). **Evidence:** `03-ops/g9-dc.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Logging

### بخش تکمیلی درس: سناریوی واقعی، مثال‌های بیشتر و عیب‌یابی

> بخش‌های زیر درس بالا را کامل می‌کنند: سناریوی گام‌به‌گام، مثال‌های بیشتر از ساده تا سخت، جدول عیب‌یابی و پرسش‌های مصاحبه. ابتدا بخش‌های اصلی بالا را مطالعه کنید.

### تعمیق: Logging و G9

Isolation اثبات: آزمون منفی TENANT-A→TENANT-B ⇒ Timeout؛ Log در VDOM مبدأ. معیار G9: ایزولاسیون، Policy حداقلی، Log، Rubric.

**پرسش‌های مصاحبه**
1. *Log هر VDOM؟* ارسال جدا.
2. *Evidence ایزولاسیون؟* Lookup + Log.
3. *منابع؟* محدودیت تنظیم‌شده.

### تکمیل عمیق: Logging دیتاسنتر و Gate G9 — اثبات Isolation

#### چرا؟

ایزولاسیون بدون اثبات فقط ادعاست. G9 از شما می‌خواهد با آزمون منفی و Log ثابت کنید دو مستأجر/Zone از هم جدا هستند.

#### مثال ساده — آزمون Isolation

``` text
from TENANT-A host: nc -zv 10.60.2.10 22   # to TENANT-B, expect timeout
diagnose firewall iprope lookup 10.60.1.5 40000 10.60.2.10 22 tcp port2   # expect deny
```

شاهد: Log Deny با `policyid=0` یا Deny صریح.

#### مثال متوسط — Log هر VDOM

در هر VDOM تنظیم Log جدا:

``` text
config log syslogd setting
 set status enable
 set server 10.50.0.20
end
```

در Syslog سرور فیلد `vd=` را برای جداسازی نگه دارید.

#### مثال سخت — نقض Isolation

Log نشان می‌دهد ترافیک TENANT-A→TENANT-B با Policy 5 (قدیمی `all`) عبور کرده. اقدام: گزارش، Disable Policy، بازبینی همه‌ی Policyهای Inter-VDOM، Evidence، PIR.

#### Rubric G9

``` text
Isolation proof 30 | Least-privilege policy 25 | Logging 20 | Resource limits 15 | Report 10
```

#### Lab

آزمون منفی و Log را برای دو VDOM ثبت کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Log مخلوط | بدون vd | فیلتر |
| نقض | Policy قدیمی | حذف |
| منابع | سقف نیست | تعیین |

#### پرسش‌ها با پاسخ

**۱. Evidence ایزولاسیون؟** آزمون منفی + Log.
**۲. چرا vd؟** تفکیک.
**۳. بازبینی چرا؟** Policy قدیمی.

#### English Corner

- *Isolation is proven by negative tests and logs.*
- Q: How do you separate logs per tenant?

<a id="l-24-5"></a>

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

**24-1-ت6** — جدول.

ماتریس DC: Internet→WEB 443، WEB→APP 8443، APP→DB 1433، MGMT→SSH و بقیه Deny.

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

**24-2-ت5** — تلاش‌های ممنوع؛ بررسی.

Hit Count ۱۲ برای Deny یعنی ۱۲ تلاش ممنوع؛ Source را بررسی و مستند کنید.

**24-2-ت6** — طبق متن.

Policyهای ۵۰ (WEB→APP)، ۶۰ (APP→DB) و ۶۱ (Deny WEB→DB) با Log All.

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

**24-3-ت6** — DMZ/INT.

دو VDOM (DMZ و INT) با vlk و Policy دو جهت و Resource Limit.

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

**24-4-ت5** — Deny صریح با Log.

Log ناقص: Deny صریح با Log اضافه کنید.

**24-4-ت6** — ۷ آزمون.

ماتریس آزمون DC: ۷ آزمون مثبت/منفی با Log.

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

**24-0-ت5** — دو VDOM با Routing جدا (Overlap مجاز)، NAT و اینترنت در root، بدون ارتباط مشتری‌ها، DNS مشترک با Policy.

**24-0-ت6** — Super Admin فقط Global؛ Admin مشتری محدود به VDOM خودش؛ Auditor فقط خواندنی.

**24-0-Q1** — Because one tenant could consume all sessions and resources and disrupt every other VDOM.

### پاسخ‌های درس افزوده‌ی 24-5 (فصل 24)

**24-5-ت1** — Global: Firmware، HA، Interface فیزیکی/تخصیص، ادمین‌ها و Profile؛ VDOM: Policy، Routing، VPN، UTM Profile.

**24-5-ت2** — VDOM مخصوص ارتباطات مدیریتی خود فایروال (FortiGuard، Log، DNS) که ترافیک کاربران از آن عبور نمی‌کند.

**24-5-ت3** — 120000 × 0.9 = 108000؛ 108000 / 3 = 36000 Session برای هر مستأجر.

**24-5-ت4** — `accprofile`/Scope سراسری یا ادمین بدون `vdom` اختصاصی؛ رفع: ادمین VDOM-محدود با Profile مناسب و حذف دسترسی Super.

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
