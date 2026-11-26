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

> **نسخه‌ی اصلاح‌شده (v3.5):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۲۲-۰، ۲۴-۰ (دسته C). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

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

## درس 22-1 — مفاهیم HA و FGCP

**فصل 22 - روز 1 · پیش‌نیاز: فصل ۲۱ · ۶ ساعت**

### ۱) معرفی درس

قبل از پیکربندی: Active-Passive در برابر Active-Active و اجزای FGCP.

### ۲) پیش‌نیازها

فصل ۲۱

### ۳) توضیح مفهومی

- Active-Passive: یک دستگاه ترافیک می‌برد.
- Active-Active: بار تقسیم می‌شود (پیچیده‌تر).
- FGCP: پروتکل HA فورتی‌نت.
- Heartbeat: لینک اختصاصی همگام‌سازی.
- Cluster ID و Group Name.

### ۴) مثال ساده

دو دستگاه؛ یکی بمیرد دیگری ادامه دهد.

### ۵) مثال سازمانی

سازمان: HA برای فایروال لبه بدون قطع بلندمدت.

### ۶) تصویر و توپولوژی

```text
FGT-1 (Primary) <-HB-> FGT-2 (Secondary)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > HA.

#### روش خط فرمان (CLI)

```text
get system ha status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- نمودار HA را بکشید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | HA بالا نمی‌آید |
| شواهد/دستور | `get system ha status` |
| علت | Group/Password |
| رفع | تطبیق |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Active-Passive؟ *(پاسخ: 22-1-ت1)*

**ت2.** Heartbeat؟ *(پاسخ: 22-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Heartbeat اختصاصی؟ *(پاسخ: 22-1-م1)*

**م2.** سناریو: Split-brain؛ علت؟ *(پاسخ: 22-1-م2)*

**معیار تسلط:** ساخت HA و تست Failover.

**اشتباهات رایج:** Heartbeat و Override.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| HA | High Availability | دسترس‌پذیری بالا | FGT |
| FGCP | FortiGate Clustering Protocol | پروتکل HA | FGT |

| English sentence | ترجمه |
|---|---|
| Use a dedicated heartbeat link. | از لینک Heartbeat اختصاصی استفاده کنید. |

#### کارت Lab — درس 22-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | نقشه HA |
| 2 | پیش‌نیاز | فصل ۲۱ |
| 3 | توپولوژی | — |
| 4 | تجهیزات | — |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | نمودار |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | HA بالا نمی‌آید |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/ha-map.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

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

## درس 22-4 — عیب‌یابی HA و Upgrade

**فصل 22 - روز 4 · پیش‌نیاز: درس ۲۲-۲ · ۶ ساعت**

### ۱) معرفی درس

مشکلات رایج و ارتقای Cluster.

### ۲) پیش‌نیازها

درس ۲۲-۲

### ۳) توضیح مفهومی

- Split-brain.
- Config Sync.
- Upgrade یکی‌یکی.
- Backup قبل از Upgrade.
- Log.

### ۴) مثال ساده

دو دستگاه؛ یکی بمیرد دیگری ادامه دهد.

### ۵) مثال سازمانی

سازمان: HA برای فایروال لبه بدون قطع بلندمدت.

### ۶) تصویر و توپولوژی

```text
FGT-1 (Primary) <-HB-> FGT-2 (Secondary)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Firmware.

#### روش خط فرمان (CLI)

```text
diagnose sys ha checksum cluster
diagnose sys ha history read
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- رفع Sync.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Checksum ناهمسان |
| شواهد/دستور | `checksum cluster` |
| علت | Config |
| رفع | Sync |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Checksum؟ *(پاسخ: 22-4-ت1)*

**ت2.** Upgrade؟ *(پاسخ: 22-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Backup؟ *(پاسخ: 22-4-م1)*

**م2.** سناریو: Upgrade شکست؛ چه می‌کنید؟ *(پاسخ: 22-4-م2)*

**معیار تسلط:** ساخت HA و تست Failover.

**اشتباهات رایج:** Heartbeat و Override.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Checksum | HA checksum | تطبیق Config | HA |

| English sentence | ترجمه |
|---|---|
| Back up before upgrading. | قبل از ارتقا Backup بگیرید. |

#### کارت Lab — درس 22-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Upgrade HA |
| 2 | پیش‌نیاز | درس ۲۲-۲ |
| 3 | توپولوژی | FGT-1+FGT-2 |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | HA |
| 8 | صورت مسئله | Upgrade |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | status |
| 11 | سناریوی خرابی | Checksum ناهمسان |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | موفق |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/ha-upgrade.md` |
| 16 | Cleanup و بازگردانی | Rollback |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-22-5"></a>

## درس 22-5 — آزمون فصل ۲۲

**فصل 22 - روز 5 · پیش‌نیاز: درس ۲۲-۳ · ۶ ساعت**

### ۱) معرفی درس

ارزیابی.

### ۲) پیش‌نیازها

درس ۲۲-۳

### ۳) توضیح مفهومی

- HA A-P.
- Failover.
- Sync.
- Backup.
- آزمون.

### ۴) مثال ساده

دو دستگاه؛ یکی بمیرد دیگری ادامه دهد.

### ۵) مثال سازمانی

سازمان: HA برای فایروال لبه بدون قطع بلندمدت.

### ۶) تصویر و توپولوژی

```text
FGT-1 (Primary) <-HB-> FGT-2 (Secondary)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > HA.

#### روش خط فرمان (CLI)

```text
get system ha status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- اجرای سناریو.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Failover کند |
| شواهد/دستور | ha status |
| علت | Heartbeat |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** HA چیست؟ *(پاسخ: 22-5-ت1)*

**ت2.** Sync؟ *(پاسخ: 22-5-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا تست؟ *(پاسخ: 22-5-م1)*

**م2.** سناریو: Heartbeat قطع؛ پیامد؟ *(پاسخ: 22-5-م2)*

**معیار تسلط:** ساخت HA و تست Failover.

**اشتباهات رایج:** Heartbeat و Override.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Heartbeat | HA heartbeat | نبض HA | HA |

| English sentence | ترجمه |
|---|---|
| Always test failover. | همیشه Failover را تست کنید. |

#### کارت Lab — درس 22-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون HA |
| 2 | پیش‌نیاز | درس ۲۲-۳ |
| 3 | توپولوژی | FGT×2 |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | HA |
| 8 | صورت مسئله | Failover |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping |
| 11 | سناریوی خرابی | Failover کند |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | ثبت |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/ha-exam.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-22"></a>

## پاسخ‌های فصل 22

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**22-1-ت1** — Active-Passive؟

یک فعال.

**22-1-ت2** — Heartbeat؟

لینک همگام‌سازی.

**22-1-م1** — چرا Heartbeat اختصاصی؟

پایداری.

**22-1-م2** — سناریو: Split-brain؛ علت؟

قطع Heartbeat.


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

**22-4-ت1** — Checksum؟

تطبیق Config.

**22-4-ت2** — Upgrade؟

Backup اول.

**22-4-م1** — چرا Backup؟

بازگشت.

**22-4-م2** — سناریو: Upgrade شکست؛ چه می‌کنید؟

Rollback.

**22-5-ت1** — HA چیست؟

دو دستگاه.

**22-5-ت2** — Sync؟

Config.

**22-5-م1** — چرا تست؟

اثبات.

**22-5-م2** — سناریو: Heartbeat قطع؛ پیامد؟

Split-brain.


---

<a id="ch23"></a>


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

## درس 23-1 — چرا Asymmetric برای Stateful مشکل است

**فصل 23 - روز 1 · پیش‌نیاز: فصل ۱۰ · ۶ ساعت**

### ۱) معرفی درس

فایروال Stateful برگشت را بدون ورودی Session می‌ریزد.

### ۲) پیش‌نیازها

فصل ۱۰

### ۳) توضیح مفهومی

- Session روی FW1 ساخته می‌شود.
- برگشت به FW2 می‌رسد و Session ندارد.
- نتیجه: Drop (SYN/ACK).
- علامت: Handshake ناقص.
- Sniffer هر دو سو.

### ۴) مثال ساده

بسته رفت از یک مسیر و برگشت از مسیر دیگر.

### ۵) مثال سازمانی

سازمان: دو فایروال لبه با مسیر نامتقارن.

### ۶) تصویر و توپولوژی

```text
Client -> FW1 -> Server ; Server -> FW2 -> Client
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Packet Capture.

#### روش خط فرمان (CLI)

```text
diagnose sniffer packet any "host 192.168.20.10" 4 20 a
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Sniffer را کوتاه اجرا کنید.
- `Unverified`.

### ۸) تست عملکرد

- مسیر رفت/برگشت را رسم کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | SYN بدون ACK |
| شواهد/دستور | sniffer |
| علت | Asymmetric |
| رفع | اصلاح مسیر |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Stateful؟ *(پاسخ: 23-1-ت1)*

**ت2.** Asymmetric؟ *(پاسخ: 23-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Drop؟ *(پاسخ: 23-1-م1)*

**م2.** سناریو: وب باز نمی‌شود؛ علت؟ *(پاسخ: 23-1-م2)*

**معیار تسلط:** تشخیص و رفع Asymmetric.

**اشتباهات رایج:** Stateful drop.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Stateful | Stateful inspection | بازرسی حالت‌دار | FW |
| SYN | TCP SYN | شروع اتصال | TCP |

| English sentence | ترجمه |
|---|---|
| Stateful firewalls require symmetric paths. | فایروال Stateful به مسیر متقارن نیاز دارد. |

#### کارت Lab — درس 23-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | تشخیص Asym |
| 2 | پیش‌نیاز | فصل ۱۰ |
| 3 | توپولوژی | FW1+FW2 |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Sniffer |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | sniffer |
| 11 | سناریوی خرابی | SYN بدون ACK |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول |
| 14 | معیار پذیرش | شاهد |
| 15 | مستندات نهایی | `03-ops/asym.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-23-2"></a>

## درس 23-2 — رفع Asymmetric: Policy Routing و Source NAT

**فصل 23 - روز 2 · پیش‌نیاز: درس ۲۳-۰ · ۶ ساعت**

### ۱) معرفی درس

راه‌حل‌ها: همسان‌سازی مسیر یا SNAT.

### ۲) پیش‌نیازها

درس ۲۳-۰

### ۳) توضیح مفهومی

- Policy Route برای مسیر برگشت.
- Source NAT تا برگشت به همان فایروال.
- `asymroute` (با احتیاط).
- طراحی بهتر: Route متقارن.
- Session Sync بین فایروال‌ها (HA).

### ۴) مثال ساده

بسته رفت از یک مسیر و برگشت از مسیر دیگر.

### ۵) مثال سازمانی

سازمان: دو فایروال لبه با مسیر نامتقارن.

### ۶) تصویر و توپولوژی

```text
Client -> FW1 -> Server ; Server -> FW2 -> Client
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Policy Routes.

#### روش خط فرمان (CLI)

```text
config router policy
    edit 1
        set input-device "port2"
        set src "192.168.20.0/24"
        set output-device "port1"
        set gateway 10.0.0.1
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.
- asymroute امنیت را کم می‌کند.

### ۸) تست عملکرد

- ارتباط بعد از اصلاح.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | هنوز Drop |
| شواهد/دستور | sniffer |
| علت | Route ناقص |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Policy Route؟ *(پاسخ: 23-2-ت1)*

**ت2.** asymroute؟ *(پاسخ: 23-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا SNAT؟ *(پاسخ: 23-2-م1)*

**م2.** سناریو: فقط یک سرور؛ راه‌حل؟ *(پاسخ: 23-2-م2)*

**معیار تسلط:** تشخیص و رفع Asymmetric.

**اشتباهات رایج:** Stateful drop.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| SNAT | Source NAT | تغییر مبدأ | NAT |

| English sentence | ترجمه |
|---|---|
| Prefer symmetric design over workarounds. | طراحی متقارن را به راه‌حل‌های موقت ترجیح دهید. |

#### کارت Lab — درس 23-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | رفع Asym |
| 2 | پیش‌نیاز | درس ۲۳-۰ |
| 3 | توپولوژی | FW1+FW2 |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Asym |
| 8 | صورت مسئله | Policy Route |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping |
| 11 | سناریوی خرابی | هنوز Drop |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Reply |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/asym-fix.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-23-3"></a>

## درس 23-3 — چند فایروال سری و موازی

**فصل 23 - روز 3 · پیش‌نیاز: درس ۲۳-۱ · ۶ ساعت**

### ۱) معرفی درس

سری: Defense in Depth؛ موازی: Load/Redundancy.

### ۲) پیش‌نیازها

درس ۲۳-۱

### ۳) توضیح مفهومی

- سری: دو لایه Policy.
- موازی: ECMP/HA.
- Zone و Trust.
- NAT یک‌بار.
- مانیتورینگ.

### ۴) مثال ساده

بسته رفت از یک مسیر و برگشت از مسیر دیگر.

### ۵) مثال سازمانی

سازمان: دو فایروال لبه با مسیر نامتقارن.

### ۶) تصویر و توپولوژی

```text
Client -> FW1 -> Server ; Server -> FW2 -> Client
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Monitor > Routing.

#### روش خط فرمان (CLI)

```text
get router info routing-table all
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خواندنی.

### ۸) تست عملکرد

- طرح سری و موازی.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | NAT دوباره |
| شواهد/دستور | session list |
| علت | دو NAT |
| رفع | حذف یکی |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** سری؟ *(پاسخ: 23-3-ت1)*

**ت2.** موازی؟ *(پاسخ: 23-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا یک NAT؟ *(پاسخ: 23-3-م1)*

**م2.** سناریو: دو NAT؛ مشکل؟ *(پاسخ: 23-3-م2)*

**معیار تسلط:** تشخیص و رفع Asymmetric.

**اشتباهات رایج:** Stateful drop.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| ECMP | Equal-Cost Multi-Path | مسیر موازی | Routing |

| English sentence | ترجمه |
|---|---|
| Avoid double NAT. | از Double NAT پرهیز کنید. |

#### کارت Lab — درس 23-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | سری/موازی |
| 2 | پیش‌نیاز | درس ۲۳-۱ |
| 3 | توپولوژی | FW1+FW2 |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | طرح |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | NAT دوباره |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/multi-fw.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-23-4"></a>

## درس 23-4 — مانیتورینگ Session و آزمون معماری ۵

**فصل 23 - روز 4 · پیش‌نیاز: درس ۲۳-۲ · ۶ ساعت**

### ۱) معرفی درس

ردیابی Session روی چند فایروال.

### ۲) پیش‌نیازها

درس ۲۳-۲

### ۳) توضیح مفهومی

- `diagnose sys session list`.
- Filter.
- Log Forward.
- RCA.
- آزمون.

### ۴) مثال ساده

بسته رفت از یک مسیر و برگشت از مسیر دیگر.

### ۵) مثال سازمانی

سازمان: دو فایروال لبه با مسیر نامتقارن.

### ۶) تصویر و توپولوژی

```text
Client -> FW1 -> Server ; Server -> FW2 -> Client
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Dashboard > Sessions.

#### روش خط فرمان (CLI)

```text
diagnose sys session filter src 192.168.10.5
diagnose sys session list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- ردیابی Session.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Session نیست |
| شواهد/دستور | session list |
| علت | FW دیگر |
| رفع | بررسی |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Filter؟ *(پاسخ: 23-4-ت1)*

**ت2.** Log؟ *(پاسخ: 23-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا RCA؟ *(پاسخ: 23-4-م1)*

**م2.** سناریو: Session روی FW2؛ چرا؟ *(پاسخ: 23-4-م2)*

**معیار تسلط:** تشخیص و رفع Asymmetric.

**اشتباهات رایج:** Stateful drop.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RCA | Root Cause Analysis | علت ریشه‌ای | Ops |

| English sentence | ترجمه |
|---|---|
| Trace sessions on both firewalls. | Session را روی هر دو فایروال دنبال کنید. |

#### کارت Lab — درس 23-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون A5 |
| 2 | پیش‌نیاز | درس ۲۳-۲ |
| 3 | توپولوژی | FW1+FW2 |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Asym |
| 8 | صورت مسئله | RCA |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | session |
| 11 | سناریوی خرابی | Session نیست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/a5.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-23"></a>

## پاسخ‌های فصل 23

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**23-1-ت1** — Stateful؟

Session محور.

**23-1-ت2** — Asymmetric؟

رفت/برگشت متفاوت.

**23-1-م1** — چرا Drop؟

نبود Session.

**23-1-م2** — سناریو: وب باز نمی‌شود؛ علت؟

مسیر نامتقارن.

**23-2-ت1** — Policy Route؟

مسیر مبتنی بر مبدأ.

**23-2-ت2** — asymroute؟

ریسک.

**23-2-م1** — چرا SNAT؟

برگشت به همان FW.

**23-2-م2** — سناریو: فقط یک سرور؛ راه‌حل؟

Policy Route.

**23-3-ت1** — سری؟

دو لایه.

**23-3-ت2** — موازی؟

Redundancy.

**23-3-م1** — چرا یک NAT؟

سادگی.

**23-3-م2** — سناریو: دو NAT؛ مشکل؟

عیب‌یابی سخت.

**23-4-ت1** — Filter؟

محدود Session.

**23-4-ت2** — Log؟

Forward.

**23-4-م1** — چرا RCA؟

یادگیری.

**23-4-م2** — سناریو: Session روی FW2؛ چرا؟

Route.


---

<a id="ch24"></a>


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

## درس 24-1 — East-West و Segmentation

**فصل 24 - روز 1 · پیش‌نیاز: فصل ۲۳ · ۶ ساعت**

### ۱) معرفی درس

ترافیک داخلی Data Center را هم باید کنترل کرد.

### ۲) پیش‌نیازها

فصل ۲۳

### ۳) توضیح مفهومی

- North-South: ورود/خروج.
- East-West: بین سرورها.
- Zone: Web/App/DB.
- Policy حداقلی.
- Logging.

### ۴) مثال ساده

اتاق سرور با بخش‌های جدا.

### ۵) مثال سازمانی

سازمان: Web/App/DB جدا با Policy حداقلی.

### ۶) تصویر و توپولوژی

```text
Web -> App -> DB (only required ports)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces > Zone.

#### روش خط فرمان (CLI)

```text
config system zone
    edit "ZN-DB"
        set interface "vlan30"
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- طرح Zoneها.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | DB قابل دسترس از Web |
| شواهد/دستور | policy lookup |
| علت | Policy باز |
| رفع | محدود |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** East-West؟ *(پاسخ: 24-1-ت1)*

**ت2.** Zone؟ *(پاسخ: 24-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا East-West؟ *(پاسخ: 24-1-م1)*

**م2.** سناریو: Web به DB مستقیم؛ چه می‌کنید؟ *(پاسخ: 24-1-م2)*

**معیار تسلط:** Segmentation و تست.

**اشتباهات رایج:** any-any.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| East-West | East-West traffic | ترافیک داخلی | DC |

| English sentence | ترجمه |
|---|---|
| Control east-west traffic. | ترافیک East-West را کنترل کنید. |

#### کارت Lab — درس 24-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | طرح Zone |
| 2 | پیش‌نیاز | فصل ۲۳ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Zone |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | DB قابل دسترس از Web |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | سند |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `02-design/dc-zones.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

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

## درس 24-4 — Logging و Gate G9

**فصل 24 - روز 4 · پیش‌نیاز: درس ۲۴-۲ · ۶ ساعت**

### ۱) معرفی درس

ثبت، تست Isolation و ارزیابی.

### ۲) پیش‌نیازها

درس ۲۴-۲

### ۳) توضیح مفهومی

- Log همه‌ی Deny.
- تست Isolation.
- Backup.
- RCA.
- آزمون G9.

### ۴) مثال ساده

اتاق سرور با بخش‌های جدا.

### ۵) مثال سازمانی

سازمان: Web/App/DB جدا با Policy حداقلی.

### ۶) تصویر و توپولوژی

```text
Web -> App -> DB (only required ports)
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Forward Traffic.

#### روش خط فرمان (CLI)

```text
execute backup config tftp fgt-g9.conf 192.168.90.10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `Unverified`.

### ۸) تست عملکرد

- اجرای G9.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Isolation شکست |
| شواهد/دستور | تست |
| علت | Policy |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** G9؟ *(پاسخ: 24-4-ت1)*

**ت2.** Backup؟ *(پاسخ: 24-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا تست؟ *(پاسخ: 24-4-م1)*

**م2.** سناریو: Web به DB؛ شکست G9؟ *(پاسخ: 24-4-م2)*

**معیار تسلط:** Segmentation و تست.

**اشتباهات رایج:** any-any.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| G9 | Gate 9 | دروازه‌ی ۹ | دوره |

| English sentence | ترجمه |
|---|---|
| Test isolation explicitly. | Isolation را صریحاً تست کنید. |

#### کارت Lab — درس 24-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون G9 |
| 2 | پیش‌نیاز | درس ۲۴-۲ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Zone |
| 8 | صورت مسئله | G9 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | تست |
| 11 | سناریوی خرابی | Isolation شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | شاهد |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/g9.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-24"></a>

## پاسخ‌های فصل 24

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**24-1-ت1** — East-West؟

داخلی.

**24-1-ت2** — Zone؟

گروه Interface.

**24-1-م1** — چرا East-West؟

حرکت جانبی مهاجم.

**24-1-م2** — سناریو: Web به DB مستقیم؛ چه می‌کنید؟

Policy حداقلی.


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

**24-4-ت1** — G9؟

سه Zone+Isolation.

**24-4-ت2** — Backup؟

execute backup.

**24-4-م1** — چرا تست؟

اثبات.

**24-4-م2** — سناریو: Web به DB؛ شکست G9؟

بله.


---

<a id="end8"></a>


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
