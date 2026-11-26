# Enterprise Network & Security Engineering — دوره‌ی تخصصی Cisco و Enterprise Firewall
## بخش ۶ از ۱۱ — فصل‌های ۱۶ تا ۱۸

| مورد | مقدار |
|---|---|
| نام دوره | Enterprise Network & Security Engineering (Cisco + FortiGate) |
| شماره بخش | ۶ از ۱۱ |
| فصل‌های این فایل | ۱۶ ، ۱۷ ، ۱۸ |
| تاریخ تولید | ۲۰۲۶-۱۱-۲۶ |
| نسخه Blueprint | v3.0 (+ بازبینی ۱٫۱) |
| نسخه‌های نرم‌افزار | FortiOS 7.0.3 (اسمی؛ بوت‌نشده؛ تأیید با `get system status`) ؛ Cisco vIOS-L2 15.2(20200924، Experimental) ؛ Cisco vIOS 15.9(3)M9 ؛ VPCS ؛ PNetLab 4.2.8 ؛ ESXi 8.0U2 ؛ CSR1000v 17.03.02 (IOS-XE؛ آزمایش‌نشده) |
| وضعیت تکمیل | **فصل‌های ۱۶–۱۸ تولید شد؛ UTM، Authentication، IPsec S2S.** Labها «اجرا نشده»؛ UTM به لایسنس FortiGuard وابسته (Needs-License)؛ دستورها آزمایش‌نشده. |

> **قوانین خواندن:** تمرین‌ها و پرسش‌های مرور بدون پاسخ‌اند؛ پاسخ در «پاسخ‌های فصل». «اجرا نشده» یعنی خروجی‌ها **پیش‌نیاز/پیش‌بینی** هستند. «CLI-Accepted» ≠ «کار می‌کند». رمزها نمونه‌اند.

### وضعیت راستی‌آزمایی Labهای این بخش
خلاصه: اجرا نشده (فقط طراحی): 18.

| Lab | وضعیت |
|---|---|
| 16-1 | اجرا نشده (فقط طراحی) |
| 16-2 | اجرا نشده (فقط طراحی) |
| 16-3 | اجرا نشده (فقط طراحی) |
| 16-4 | اجرا نشده (فقط طراحی) |
| 16-5 | اجرا نشده (فقط طراحی) |
| 16-6 | اجرا نشده (فقط طراحی) |
| 17-1 | اجرا نشده (فقط طراحی) |
| 17-2 | اجرا نشده (فقط طراحی) |
| 17-3 | اجرا نشده (فقط طراحی) |
| 17-4 | اجرا نشده (فقط طراحی) |
| 17-5 | اجرا نشده (فقط طراحی) |
| 17-6 | اجرا نشده (فقط طراحی) |
| 18-1 | اجرا نشده (فقط طراحی) |
| 18-2 | اجرا نشده (فقط طراحی) |
| 18-3 | اجرا نشده (فقط طراحی) |
| 18-4 | اجرا نشده (فقط طراحی) |
| 18-5 | اجرا نشده (فقط طراحی) |
| 18-6 | اجرا نشده (فقط طراحی) |

---

<a id="ch16"></a>

> **نسخه‌ی اصلاح‌شده (v3.3):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۱۶-۰، ۱۶-۷، ۱۸-۰ (دسته C). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

# فصل 16 — UTM: آنتی‌ویروس، IPS، Application Control، Web Filter و SSL Inspection

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۱۴.
**اهداف:** Security Profile و Profile Group؛ AV؛ Web Filter (Static URL به‌جای Category)؛ IPS و DoS؛ Application Control؛ SSL/SSH Inspection؛ اثر Performance و عیب‌یابی.
**هشدار لایسنس (مهم):** AV/IPS/Web Filter/App Control به **FortiGuard Subscription** وابسته‌اند. در Lab ایزوله و Evaluation این وابستگی `Needs-License` و وضعیتش `Unverified` است. هر درس بخش «بدون لایسنس چه می‌توان کرد» دارد (Static URL، Custom IPS، DoS، Port-based). **همه‌ی دستورها آزمایش‌نشده روی Image.**
**معیار تسلط:** Profile ساخته و به Policy وصل؛ اثبات با Log/تست؛ توضیح اثر SSL Inspection بر Performance و Certificate.
**اشتباهات رایج:** فعال‌کردن Deep Inspection بدون نصب CA؛ Profile روی همه‌ی ترافیک؛ نادیده‌گرفتن لایسنس؛ بدون تست.

**درس‌های فصل:**
- [درس 16-1 — Security Profile و لایسنس: نقشه‌ی UTM](#l-16-1)
- [درس 16-2 — Web Filter و DNS Filter (Static و Category)](#l-16-2)
- [درس 16-3 — Antivirus و File Filter](#l-16-3)
- [درس 16-4 — IPS، DoS و Application Control](#l-16-4)
- [درس 16-5 — SSL/SSH Inspection: Certificate و CA](#l-16-5)
- [درس 16-6 — Performance، عیب‌یابی UTM و آزمون فصل](#l-16-6)

---

<a id="l-16-1"></a>

## درس 16-0 — Inspection Mode (Flow در برابر Proxy)، TLS Inspection و زنجیره‌ی اعتماد

**فصل ۱۶ · درس افزوده (پیش‌درس ۱۶-۱) · پیش‌نیاز: ۱۲-۰، ۱۱-۷، مفاهیم TLS و PKI · ≈ ۸ ساعت**

> **وضعیت (FortiOS 7.0.3):** تفاوت Flow/Proxy و پروفایل‌های SSL از مستند رسمی 7.0 تأیید شد ([Inspection modes](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/721410/inspection-modes)، [Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison)، [SSL & SSH Inspection](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/929997/ssl-ssh-inspection)). جزئیات روی Image `Unverified`. Needs-License: سرویس‌های FortiGuard.

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. تفاوت **Flow-based** و **Proxy-based Inspection** را از نظر سازوکار، قابلیت و Performance بگوید و برای هر سناریو انتخاب کند.
2. توضیح دهد TLS چگونه کار می‌کند و چرا بدون **SSL Inspection** محتوای HTTPS دیده نمی‌شود.
3. **Certificate Inspection** و **Deep Inspection** را از نظر دید، ریسک و پیش‌نیاز مقایسه کند.
4. **زنجیره‌ی اعتماد (Certificate Chain)، CA و Trust Store** را توضیح دهد و بگوید چرا مرورگر به CA فایروال باید اعتماد کند.
5. **SNI** و محدودیت‌های دید روی ترافیک رمزشده (TLS 1.3، ECH، Certificate Pinning) را بشناسد.
6. در سناریوی واقعی Exemption امن بنویسد.

### ۲) پیش‌نیازها

Handshake TLS در سطح مفهومی (Client Hello، Certificate، Key Exchange)، مفهوم کلید عمومی/خصوصی و گواهی (PKI)، Packet Flow (۱۲-۰).

### ۳) مفهوم پایه

بیشتر ترافیک امروز رمزشده است. فایروالی که فقط پورت و IP را ببیند، نمی‌تواند بدافزار داخل HTTPS را کشف کند. **UTM** یعنی بازرسی محتوا؛ و بازرسی محتوا برای ترافیک رمزشده نیاز به **رمزگشایی** دارد. این رمزگشایی یک **حمله‌ی Man-in-the-Middle مجاز** است: فایروال به‌جای سرور، گواهی صادر می‌کند. کاربر فقط وقتی خطا نمی‌بیند که به CA فایروال اعتماد کرده باشد.

### ۴) توضیح عمیق فنی

#### ۴-۱) Flow-based در برابر Proxy-based

طبق مستند Fortinet (7.0):

- **Flow-based:** بسته‌ها را «در جریان» می‌بیند؛ یک Snapshot از محتوا می‌گیرد و با Pattern Matching بررسی می‌کند؛ بسته‌ها بازسازی کامل نمی‌شوند. تأخیر کمتر، Throughput بیشتر (و قابلیت NPU Offload در بعضی حالت‌ها).
- **Proxy-based:** فایروال اتصال کلاینت را ختم و اتصال جدیدی به سرور می‌سازد؛ **محتوا را کامل بازسازی** می‌کند (فایل کامل، پاسخ کامل HTTP). قابلیت بیشتر (مثلاً بعضی گزینه‌های AV/Web Filter/DLP مثل Content Disarm، Quota و ...)، هزینه‌ی CPU/Memory و تأخیر بیشتر.
- در 7.0 حالت بازرسی **در هر Policy** انتخاب می‌شود (`set inspection-mode flow|proxy`)؛ پیش‌فرض Flow است.

| معیار | Flow | Proxy |
|---|---|---|
| سازوکار | بدون بازسازی کامل، Pattern | ختم و بازسازی |
| تأخیر | کمتر | بیشتر |
| CPU/Memory | کمتر | بیشتر |
| قابلیت‌ها | کمتر (جدول مقایسه‌ی Fortinet) | بیشتر |
| پوشش پورت | همه‌ی پورت‌ها در Deep (طبق مستند) | فقط پورت‌های نگاشت‌شده مگر «Inspect all ports» |
| کاربرد | Throughput، ترافیک عمومی | حساسیت بالا، قابلیت خاص |

(برای هر Profile باید جدول «Inspection mode feature comparison» همان نسخه بررسی شود.)

#### ۴-۲) TLS در یک نگاه

``` text
1. ClientHello  : supported versions/ciphers, SNI (server name, plaintext in TLS<=1.2/1.3 default)
2. ServerHello  : chosen cipher
3. Certificate  : server certificate chain
4. Key exchange : (EC)DHE -> session keys
5. Finished     : encrypted application data
```

- **SNI (Server Name Indication):** نام سرور در ClientHello (معمولاً رمزنشده)؛ فایروال بدون رمزگشایی می‌تواند بر اساس SNI فیلتر کند.
- TLS 1.3: گواهی سرور رمز می‌شود؛ بنابراین Certificate Inspection روی TLS 1.3 اطلاعات کمتری دارد (SNI می‌ماند). با **ECH (Encrypted Client Hello)** حتی SNI هم رمز می‌شود (محدودیت آینده/مرورگرهای جدید).

#### ۴-۳) Certificate Inspection

فایروال فقط **اطلاعات گواهی و SNI** را می‌بیند (تا لایه‌ی TLS) و محتوای رمزشده را باز نمی‌کند. توانایی: Web Filter بر اساس Category/FQDN، بلاک گواهی نامعتبر/منقضی. محدودیت: AV/IPS/DLP روی محتوای HTTPS ناممکن.

#### ۴-۴) Deep Inspection (Full SSL Inspection)

فایروال به‌عنوان **Proxy TLS** عمل می‌کند:

``` text
Client <==TLS(session A, cert signed by firewall CA)==> FortiGate <==TLS(session B)==> Server
                       decrypt -> inspect (AV/IPS/Web/DLP) -> re-encrypt
```

- باید **CA فایروال** (یا CA سازمانی) در Trust Store همه‌ی کلاینت‌ها نصب باشد (GPO/MDM)، وگرنه خطای گواهی.
- ریسک: بار CPU، مشکل با برنامه‌های Pin‌شده، مسائل حریم خصوصی/حقوقی، افزایش سطح حمله به خود فایروال (گواهی‌های صادرشده، کلید CA).
- **Exemption:** بانک، سلامت، به‌روزرسانی‌های Pin‌شده، برنامه‌های خاص (Teams/OS update) از Inspection مستثنا شوند (Address/FQDN/Category).
- 7.0 دو Profile آماده دارد: `certificate-inspection` و `deep-inspection` (و `no-inspection`) طبق مستند.

#### ۴-۵) Certificate Chain، CA و Trust

``` text
Root CA (in trust store) -> Intermediate CA -> Server certificate
Browser: verify signature chain up to a trusted root, check name (SAN), validity, revocation (OCSP/CRL)
```

در Deep Inspection فایروال زنجیره‌ی سرور واقعی را **اعتبارسنجی می‌کند** و برای کلاینت گواهی جدید (با همان Subject/SAN) با **CA فایروال** امضا می‌کند. اگر گواهی سرور معتبر نباشد، فایروال باید به کلاینت هشدار بدهد (گواهی «untrusted» جداگانه؛ تنظیم Action برای گواهی نامعتبر مهم است: Allow/Block/Warning). CA فایروال به‌صورت پیش‌فرض Self-signed است؛ بهتر است CA داخلی سازمان (Intermediate) استفاده شود.

#### ۴-۶) محدودیت‌های دید

- **Certificate Pinning:** برنامه‌ای که گواهی خاص را انتظار دارد با گواهی فایروال خطا می‌دهد.
- **TLS 1.3/ECH/QUIC (HTTP/3 روی UDP 443):** QUIC معمولاً قابل Inspection عمیق نیست؛ سیاست معمول: بلاک QUIC تا ترافیک به TCP/TLS برگردد (Application Control).
- **mTLS (Mutual TLS):** گواهی کلاینت؛ Inspection ممکن است آن را بشکند.
- **STARTTLS، SMTPS، IMAPS:** پروتکل‌های دیگر هم Profile جدا دارند.

#### ۴-۷) Detection در برابر Prevention

- **Detection (Monitor):** رویداد را Log می‌کند ولی ترافیک را عبور می‌دهد.
- **Prevention (Block):** ترافیک را مسدود می‌کند.
- روش ایمن استقرار: ابتدا **Monitor** و بررسی False Positive، سپس Block برای موارد با اطمینان بالا.

### ۵) مثال حل‌شده

**نیاز:** Policy Users→Internet با AV و Web Filter و SSL Inspection.

``` text
config firewall policy
    edit 10
        set name "Users-to-Internet"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "Users-Net"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "HTTP" "HTTPS" "DNS"
        set inspection-mode flow
        set ssl-ssh-profile "certificate-inspection"
        set nat enable
        set logtraffic all
    next
end
```

(نام فیلدها طبق مستند 7.0؛ `Unverified` روی Image.) سپس برای سناریوی بانک: Profile سفارشی Deep با Exemption.

**مثال متوسط:** پس از فعال‌کردن Deep Inspection، برنامه‌ی Updater خطای TLS می‌دهد. علت: Pinning. راه‌حل: Exemption آن FQDN، نه خاموش‌کردن Deep برای همه.

**مثال سخت:** کاربران مرورگر Firefox هنوز هشدار گواهی می‌بینند در حالی‌که Chrome ندارد. تحلیل: Firefox Trust Store جداگانه دارد؛ CA فقط در Windows Store نصب شده است. راه‌حل: Policy Firefox (`security.enterprise_roots.enabled`) یا نصب CA در Firefox (مدیریت متمرکز). ثبت در RCA.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| Flow یا Proxy؟ | Flow برای عموم؛ Proxy برای نیاز خاص (طبق جدول مقایسه) |
| Deep یا Certificate Inspection؟ | Deep برای Users→Internet؛ Certificate برای سرورها/سلامت |
| CA فایروال یا CA سازمانی؟ | CA سازمانی (Intermediate) با توزیع GPO |
| Exemptionها | بانک، سلامت، Pinned، Update |
| QUIC | بلاک یا Exempt طبق سیاست |
| گواهی نامعتبر | Block/Warning برای Users |

### ۷) پیاده‌سازی: GUI و CLI

**GUI:**

1. Security Profiles → SSL/SSH Inspection → Create New (یا Clone از deep-inspection).
2. Inspection Method: Full SSL Inspection / SSL Certificate Inspection.
3. CA Certificate: انتخاب، و Download/Export CA برای نصب روی کلاینت.
4. Exempt from SSL Inspection: Web Categories، Addresses.
5. Policy & Objects → Firewall Policy → ویرایش Policy → Inspection Mode و SSL Inspection.

**CLI:**

``` text
config firewall ssl-ssh-profile
    edit "SSL-DEEP-LAB"
        config https
            set ports 443
            set status deep-inspection
        end
        set untrusted-caname "Fortinet_CA_Untrusted"
    next
end
get firewall ssl-ssh-profile
```

(`untrusted-caname`، `status` و ... با CLI Reference 7.0 تطبیق شود؛ `Unverified`.)

### ۸) Troubleshooting

| علامت | شاهد | علت |
|---|---|---|
| خطای گواهی در مرورگر | Issuer = CA فایروال | CA روی کلاینت نصب نیست |
| برنامه TLS خطا می‌دهد | Capture: Alert | Pinning |
| سایت HTTPS کند | CPU، `sys top` | Deep روی ترافیک سنگین |
| Block کار نمی‌کند | Log بدون UTM | Profile/SSL Inspection وصل نیست یا Pinned |
| QUIC دور می‌زند | Capture UDP 443 | QUIC Inspect نمی‌شود |

### ۹) نکات امنیتی

- کلید خصوصی CA فایروال حساس‌ترین دارایی این سیستم است؛ دسترسی Admin محدود و Backup رمزشده.
- رمزگشایی داده‌ی کاربران ملاحظات حقوقی و حریم خصوصی دارد؛ سیاست و رضایت لازم.
- گواهی‌های نامعتبر را Block کنید؛ اجازه‌ی «Allow» پیش‌فرض خطرناک است.

### ۱۰) جمع‌بندی مفهومی

- Flow سریع‌تر و محدودتر؛ Proxy کامل‌تر و سنگین‌تر؛ انتخاب Per-Policy.
- Certificate Inspection فقط گواهی/SNI؛ Deep محتوا را می‌بیند ولی نیاز به CA و Exemption دارد.
- TLS 1.3/ECH/QUIC/Pinning دید را کم می‌کنند.
- Monitor قبل از Block.
- کلید CA یک دارایی بحرانی است.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) Flow و Proxy چه فرقی دارند؟ *(پاسخ: 16-0-ت1)*

**ت2.** (ساده) SNI چیست؟ *(پاسخ: 16-0-ت2)*

**ت3.** (متوسط) چرا Deep Inspection نیاز به نصب CA روی کلاینت دارد؟ *(پاسخ: 16-0-ت3)*

**ت4.** (متوسط) Certificate Pinning چه مشکلی ایجاد می‌کند؟ راه‌حل؟ *(پاسخ: 16-0-ت4)*

**ت5.** (سخت) برای ۳ گروه (کاربران عادی، سرورها، بانک/سلامت) استراتژی SSL Inspection را طراحی کنید. *(پاسخ: 16-0-ت5)*

**ت6.** (سخت، طراحی) QUIC چه مشکلی برای Inspection دارد و چگونه مدیریت می‌شود؟ *(پاسخ: 16-0-ت6)*

**م1.** Detection و Prevention چه فرقی دارند؟ *(پاسخ: 16-0-م1)*

**Q1.** Quick quiz (English): What can certificate inspection see that deep inspection also sees, and what only deep inspection sees? *(پاسخ: 16-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| SNI | Server Name Indication | نام سرور در Hello |
| CA | Certificate Authority | مرجع گواهی |
| PKI | Public Key Infrastructure | زیرساخت کلید عمومی |
| ECH | Encrypted Client Hello | رمزکردن Hello |
| QUIC | QUIC | پروتکل انتقال روی UDP |
| mTLS | Mutual TLS | TLS دوطرفه |
| OCSP | Online Certificate Status Protocol | بررسی ابطال گواهی |

- *Deep inspection decrypts and re-encrypts TLS sessions.* ← Deep Inspection نشست TLS را رمزگشایی و دوباره رمزگذاری می‌کند.
- *Exempt pinned and privacy-sensitive destinations from inspection.* ← مقصدهای Pinned و حساس حریم خصوصی را از Inspection مستثنا کنید.

### ۱۳) منابع

- Fortinet Docs: [Inspection modes](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/721410/inspection-modes)، [Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison)، [SSL & SSH Inspection](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/929997/ssl-ssh-inspection)، [Inspection mode per policy](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/366651/inspection-mode-per-policy).
- RFC 8446 — TLS 1.3؛ RFC 6066 (SNI)؛ RFC 5280 (X.509 PKI).

## درس 16-1 — Security Profile و لایسنس: نقشه‌ی UTM

**فصل 16 - روز 1 · پیش‌نیاز: فصل ۱۳ · ۶ ساعت**

### ۱) معرفی درس

Profileهای امنیتی بازرسی لایه‌ی ۷ را روی Policy اضافه می‌کنند. اول باید بدانیم کدام نیاز به Subscription دارد.

### ۲) پیش‌نیازها

فصل ۱۳

### ۳) توضیح مفهومی

- Profileها: AntiVirus، Web Filter، DNS Filter، IPS، Application Control، SSL/SSH Inspection، File Filter.
- Profile به Policy وصل می‌شود (`utm-status enable` در 7.0؛ `Unverified`).
- **Needs-License:** AV/IPS/Web Rating/App DB به FortiGuard وابسته؛ در Lab ایزوله به‌روزرسانی ممکن نیست.
- **بدون لایسنس:** Static URL Filter، Custom IPS، DoS Policy، Port-based App، File Filter ساده.
- ثبت «Feature/License Log» برای هر قابلیت (آزمایش‌شده/Needs-License/Unverified).

### ۴) مثال ساده

یک Profile ساده روی Policy کاربران.

### ۵) مثال سازمانی

سازمان: Profile استاندارد برای هر گروه (کاربران، سرورها، مهمان).

### ۶) تصویر و توپولوژی

```text
Policy -> [Profile: AV/IPS/Web/App/SSL] -> accept/block
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Security Profiles > Web Filter > Create New.
2. Policy > Security Profiles: Web Filter را روشن و Profile را انتخاب.
3. System > FortiGuard: وضعیت لایسنس را ببینید.
4. Log & Report > Web Filter.

#### روش خط فرمان (CLI)

```text
config firewall policy
    edit 10
        set utm-status enable
        set ssl-ssh-profile "certificate-inspection"
        set webfilter-profile "WF-STD"
    next
end
get system fortiguard-service status
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `ssl-ssh-profile`: لازم برای بازرسی HTTPS.
- `get system fortiguard-service status` (`Unverified`) وضعیت لایسنس.
- راستی‌آزمایی: Log با فیلد utm/ action.
- بازگشت: `unset webfilter-profile`.

### ۸) تست عملکرد

- وضعیت FortiGuard را ثبت و Matrix لایسنس را پر کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Profile اثر ندارد |
| شواهد/دستور | Log: بدون utm |
| علت | Profile به Policy وصل نشده |
| رفع | اتصال Profile |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** کدام Profileها Needs-License؟ *(پاسخ: 16-1-ت1)*

**ت2.** بدون لایسنس چه؟ *(پاسخ: 16-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Feature/License Log؟ *(پاسخ: 16-1-م1)*

**م2.** سناریو: AV کار نمی‌کند؛ علت؟ *(پاسخ: 16-1-م2)*

**معیار تسلط:** ساخت Profile، اتصال به Policy، اثبات با Log/تست.

**اشتباهات رایج:** فعال‌کردن بی‌برنامه؛ نادیده‌گرفتن لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Security profile | Security profile | بازرسی لایه ۷ | Policy |
| FortiGuard | FortiGuard Services | سرویس به‌روزرسانی | Subscription |
| Feature log | Feature/License log | ثبت وضعیت قابلیت | طراحی |

| English sentence | ترجمه |
|---|---|
| Many UTM features require a FortiGuard subscription. | بسیاری از قابلیت‌های UTM به اشتراک FortiGuard نیاز دارند. |
| Record what you actually tested. | آنچه واقعاً آزمایش کرده‌اید را ثبت کنید. |

#### کارت Lab — درس 16-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Matrix لایسنس UTM |
| 2 | پیش‌نیاز | فصل ۱۳ |
| 3 | توپولوژی | FGT |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Matrix لایسنس |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | `get system fortiguard-service status` |
| 11 | سناریوی خرابی | Profile اثر ندارد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول |
| 14 | معیار پذیرش | با شواهد |
| 15 | مستندات نهایی | `03-ops/utm-license-log.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-16-2"></a>

## درس 16-2 — Web Filter و DNS Filter (Static و Category)

**فصل 16 - روز 2 · پیش‌نیاز: درس ۱۶-۱ · ۶ ساعت**

### ۱) معرفی درس

کنترل دسترسی وب: Category (نیاز لایسنس) یا Static URL/FQDN (بدون لایسنس).

### ۲) پیش‌نیازها

درس ۱۶-۱

### ۳) توضیح مفهومی

- Static URL Filter: `simple`/`wildcard`/`regex` با action `block`/`allow`.
- Category Filter: نیاز به Rating (Needs-License).
- DNS Filter: بلاک بر اساس دامنه/Category.
- ترتیب: Static URL پیش از Category.
- Log Web Filter: category، action، URL.

### ۴) مثال ساده

یک Profile ساده روی Policy کاربران.

### ۵) مثال سازمانی

سازمان: Profile استاندارد برای هر گروه (کاربران، سرورها، مهمان).

### ۶) تصویر و توپولوژی

```text
Policy -> [Profile: AV/IPS/Web/App/SSL] -> accept/block
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Security Profiles > Web Filter > Static URL Filter فعال > Create New.
2. URL badsite.example، Type Simple، Action Block.
3. Policy > Web Filter = WF-STD.
4. Log & Report > Web Filter.

#### روش خط فرمان (CLI)

```text
config webfilter urlfilter
    edit 1
        set name "URLF-STATIC"
        config entries
            edit 1
                set url "badsite.example"
                set type simple
                set action block
            next
        end
    next
end
config webfilter profile
    edit "WF-STD"
        config web
            set urlfilter-table 1
        end
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `type simple`: مطابقت ساده‌ی دامنه.
- Profile به Policy وصل می‌شود (درس قبل).
- راستی‌آزمایی: مرورگر Block Page؛ Log.
- بازگشت: حذف ورودی/Profile.

### ۸) تست عملکرد

- دسترسی به badsite.example مسدود و دیگری مجاز.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Block کار نمی‌کند |
| شواهد/دستور | Log نیست؛ HTTPS بدون SSL Inspection |
| علت | HTTPS رمز است |
| رفع | فعال‌کردن SSL Inspection یا FQDN در Policy |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Static URL نیاز لایسنس دارد؟ *(پاسخ: 16-2-ت1)*

**ت2.** چرا HTTPS مشکل می‌سازد؟ *(پاسخ: 16-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Static URL را ابتدا امتحان می‌کنیم؟ *(پاسخ: 16-2-م1)*

**م2.** سناریو: دامنه‌ی HTTPS مسدود نشد؛ چرا؟ *(پاسخ: 16-2-م2)*

**معیار تسلط:** ساخت Profile، اتصال به Policy، اثبات با Log/تست.

**اشتباهات رایج:** فعال‌کردن بی‌برنامه؛ نادیده‌گرفتن لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| URL filter | Web URL filter | فیلتر URL | Web |
| Category | Web category | دسته‌ی وب | Needs-License |
| SNI | Server Name Indication | نام سرور در TLS | فیلتر HTTPS |

| English sentence | ترجمه |
|---|---|
| Static URL filters work without a subscription. | فیلترهای URL ایستا بدون اشتراک کار می‌کنند. |
| HTTPS needs SSL inspection for full filtering. | HTTPS برای فیلتر کامل به SSL Inspection نیاز دارد. |

#### کارت Lab — درس 16-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Static URL Filter |
| 2 | پیش‌نیاز | درس ۱۶-۱ |
| 3 | توپولوژی | FGT + Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | Block یک دامنه |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | مرورگر |
| 11 | سناریوی خرابی | Block کار نمی‌کند |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Block Page |
| 14 | معیار پذیرش | Log |
| 15 | مستندات نهایی | `03-ops/webfilter-static.md` |
| 16 | Cleanup و بازگردانی | حذف Profile |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-16-3"></a>

## درس 16-3 — Antivirus و File Filter

**فصل 16 - روز 3 · پیش‌نیاز: درس ۱۶-۲ · ۶ ساعت**

### ۱) معرفی درس

AV فایل‌های آلوده را در HTTP/FTP/SMTP... بررسی می‌کند؛ File Filter بر اساس نوع/پسوند.

### ۲) پیش‌نیازها

درس ۱۶-۲

### ۳) توضیح مفهومی

- AV: نیازمند Signature DB (FortiGuard).
- **File Filter:** بلاک بر اساس نوع/پسوند بدون لایسنس.
- تست استاندارد: فایل EICAR (فایل تست بی‌خطر) — نتیجه در Lab ایزوله `Unverified`.
- حالت Flow در برابر Proxy برای AV.
- Log: virus, action.

### ۴) مثال ساده

یک Profile ساده روی Policy کاربران.

### ۵) مثال سازمانی

سازمان: Profile استاندارد برای هر گروه (کاربران، سرورها، مهمان).

### ۶) تصویر و توپولوژی

```text
Policy -> [Profile: AV/IPS/Web/App/SSL] -> accept/block
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Security Profiles > AntiVirus > Create New؛ Inspect HTTP/…؛ Action Block.
2. Security Profiles > File Filter: پسوند exe را بلاک کنید.
3. Policy: AV و File Filter را فعال.
4. Log & Report > AntiVirus.

#### روش خط فرمان (CLI)

```text
config antivirus profile
    edit "AV-STD"
    next
end
! file filter (no subscription): see GUI path
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- جزئیات Option برای 7.0.3 را در GUI مقایسه کنید (`Unverified`).
- راستی‌آزمایی: دانلود EICAR مسدود/Log.
- بازگشت: حذف Profile.

### ۸) تست عملکرد

- دانلود EICAR و ثبت نتیجه واقعی.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | EICAR رد می‌شود |
| شواهد/دستور | Log AV نیست |
| علت | DB/لایسنس نیست |
| رفع | ثبت محدودیت؛ استفاده از File Filter |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** EICAR چیست؟ *(پاسخ: 16-3-ت1)*

**ت2.** File Filter لایسنس دارد؟ *(پاسخ: 16-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا نتیجه‌ی AV را ثبت می‌کنیم؟ *(پاسخ: 16-3-م1)*

**م2.** سناریو: exe بلاک نمی‌شود؛ چرا؟ *(پاسخ: 16-3-م2)*

**معیار تسلط:** ساخت Profile، اتصال به Policy، اثبات با Log/تست.

**اشتباهات رایج:** فعال‌کردن بی‌برنامه؛ نادیده‌گرفتن لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| AV | Antivirus | ضدویروس | UTM |
| EICAR | EICAR test file | فایل تست | تست |
| File filter | File filter | فیلتر نوع فایل | UTM |

| English sentence | ترجمه |
|---|---|
| Use the EICAR file to test antivirus safely. | برای تست ایمن ضدویروس از فایل EICAR استفاده کنید. |
| A file filter blocks by file type. | File Filter بر اساس نوع فایل مسدود می‌کند. |

#### کارت Lab — درس 16-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | AV/File Filter |
| 2 | پیش‌نیاز | درس ۱۶-۲ |
| 3 | توپولوژی | FGT + Client + Web |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | EICAR و exe |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | دانلود |
| 11 | سناریوی خرابی | EICAR رد می‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Block/نتیجه ثبت |
| 14 | معیار پذیرش | نتیجه‌ی واقعی ثبت |
| 15 | مستندات نهایی | `03-ops/av-notes.md` |
| 16 | Cleanup و بازگردانی | حذف Profile |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-16-4"></a>

## درس 16-4 — IPS، DoS و Application Control

**فصل 16 - روز 4 · پیش‌نیاز: درس ۱۶-۳ · ۶ ساعت**

### ۱) معرفی درس

IPS حملات شناخته‌شده را با Signature می‌گیرد؛ DoS Policy جلوی سیل را؛ Application Control برنامه‌ها را می‌شناسد.

### ۲) پیش‌نیازها

درس ۱۶-۳

### ۳) توضیح مفهومی

- IPS: Sensor با Signatureهای FortiGuard (Needs-License) و **Custom Signature** محلی.
- **DoS Policy:** آستانه‌ی Session/Packet روی Interface (بدون لایسنس).
- Application Control: DB App (Needs-License)؛ بدون آن فقط Port/Protocol.
- Action: monitor/block/reset.
- اثر Performance: IPS روی CPU.

### ۴) مثال ساده

یک Profile ساده روی Policy کاربران.

### ۵) مثال سازمانی

سازمان: Profile استاندارد برای هر گروه (کاربران، سرورها، مهمان).

### ۶) تصویر و توپولوژی

```text
Policy -> [Profile: AV/IPS/Web/App/SSL] -> accept/block
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Policy & Objects > DoS Policy > Create New: Interface port1، All.
2. Anomalies: آستانه‌ی SYN Flood را تنظیم.
3. Security Profiles > Intrusion Prevention: Sensor با Severity High/Critical (اگر لایسنس).
4. Security Profiles > Application Control.

#### روش خط فرمان (CLI)

```text
config firewall DoS-policy
    edit 1
        set name "DOS-WAN"
        set interface "port1"
        set srcaddr "all"
        set dstaddr "all"
        set service "ALL"
    next
end
! thresholds under config anomaly (see GUI)
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `DoS-policy` روی WAN؛ آستانه‌ها در GUI تنظیم شوند.
- Custom IPS: نیاز به آزمایش؛ `Unverified`.
- راستی‌آزمایی: Log anomaly.
- بازگشت: حذف Policy.

### ۸) تست عملکرد

- تولید ترافیک زیاد (hping/ab) و دیدن Log anomaly؛ نتیجه واقعی ثبت.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | DoS Policy اثر ندارد |
| شواهد/دستور | Log نیست |
| علت | Interface اشتباه |
| رفع | Interface ورودی درست |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** DoS Policy چه می‌کند؟ *(پاسخ: 16-4-ت1)*

**ت2.** IPS Needs-License؟ *(پاسخ: 16-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا DoS روی WAN؟ *(پاسخ: 16-4-م1)*

**م2.** سناریو: CPU بالا؛ علت محتمل IPS؟ *(پاسخ: 16-4-م2)*

**معیار تسلط:** ساخت Profile، اتصال به Policy، اثبات با Log/تست.

**اشتباهات رایج:** فعال‌کردن بی‌برنامه؛ نادیده‌گرفتن لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| IPS | Intrusion Prevention System | جلوگیری از نفوذ | UTM |
| DoS | Denial of Service | محدودسازی سیل | WAN |
| App control | Application control | کنترل برنامه | UTM |

| English sentence | ترجمه |
|---|---|
| Protect the WAN interface with a DoS policy. | Interface WAN را با DoS Policy محافظت کنید. |
| IPS consumes CPU; apply it selectively. | IPS CPU مصرف می‌کند؛ انتخابی اعمال کنید. |

#### کارت Lab — درس 16-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | DoS و IPS |
| 2 | پیش‌نیاز | درس ۱۶-۳ |
| 3 | توپولوژی | FGT + Client + Attacker-Lab |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | DoS ساده |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | hping/ab |
| 11 | سناریوی خرابی | DoS Policy اثر ندارد |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Log anomaly |
| 14 | معیار پذیرش | ثبت نتیجه |
| 15 | مستندات نهایی | `03-ops/ips-dos.md` |
| 16 | Cleanup و بازگردانی | حذف Policy |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-16-5"></a>

## درس 16-5 — SSL/SSH Inspection: Certificate و CA

**فصل 16 - روز 5 · پیش‌نیاز: درس ۱۶-۴ · ۶ ساعت**

### ۱) معرفی درس

Inspection ترافیک HTTPS بدون رمزگشایی ممکن نیست. گواهی CA، Exemption و اثر Performance را باید بدانید.

### ۲) پیش‌نیازها

درس ۱۶-۴

### ۳) توضیح مفهومی

- **Certificate Inspection:** فقط SNI/گواهی را می‌بیند (بدون رمزگشایی).
- **Deep Inspection:** رمزگشایی و رمزگذاری مجدد؛ نیاز به نصب CA فایروال روی کلاینت.
- Exemption: بانک/Update/حریم خصوصی از Inspection مستثنا.
- خطاهای Certificate در کلاینت = CA نصب نیست.
- Performance: Deep Inspection سنگین است.

### ۴) مثال ساده

یک Profile ساده روی Policy کاربران.

### ۵) مثال سازمانی

سازمان: Profile استاندارد برای هر گروه (کاربران، سرورها، مهمان).

### ۶) تصویر و توپولوژی

```text
Policy -> [Profile: AV/IPS/Web/App/SSL] -> accept/block
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Security Profiles > SSL/SSH Inspection > Create New: Deep Inspection.
2. System > Certificates: CA فایروال را Export و روی کلاینت نصب کنید.
3. Exempt: Addresses/Categories.
4. Policy: SSL Inspection را انتخاب.

#### روش خط فرمان (CLI)

```text
config firewall ssl-ssh-profile
    edit "SSL-DEEP-LAB"
        config https
            set ports 443
            set status deep-inspection
        end
    next
end
! use only in lab; install the FortiGate CA on the client first
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Deep Inspection فقط پس از نصب CA روی کلاینت.
- `status deep-inspection` روی HTTPS.
- راستی‌آزمایی: گواهی مرورگر توسط CA فایروال امضا شده.
- بازگشت: Profile را `certificate-inspection` کنید.
- هشدار: شکستن TLS مسائل حریم خصوصی/Pinning دارد.

### ۸) تست عملکرد

- در کلاینت گواهی سایت را بررسی کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | خطای گواهی در مرورگر |
| شواهد/دستور | Issuer = فایروال؛ مرورگر آن را نمی‌شناسد |
| علت | CA نصب نیست |
| رفع | نصب CA یا Exempt |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Deep و Certificate Inspection؟ *(پاسخ: 16-5-ت1)*

**ت2.** چرا CA لازم؟ *(پاسخ: 16-5-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا بانک‌ها Exempt؟ *(پاسخ: 16-5-م1)*

**م2.** سناریو: برنامه خطای TLS می‌دهد؛ چه می‌کنید؟ *(پاسخ: 16-5-م2)*

**معیار تسلط:** ساخت Profile، اتصال به Policy، اثبات با Log/تست.

**اشتباهات رایج:** فعال‌کردن بی‌برنامه؛ نادیده‌گرفتن لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| SSL inspection | SSL/SSH inspection | بازرسی TLS | UTM |
| CA | Certificate Authority | مرجع گواهی | TLS |
| Pinning | Certificate pinning | پین‌کردن گواهی | — |

| English sentence | ترجمه |
|---|---|
| Install the firewall CA on every client before deep inspection. | قبل از Deep Inspection CA فایروال را روی همه‌ی کلاینت‌ها نصب کنید. |
| Exempt sensitive categories from deep inspection. | دسته‌های حساس را از Deep Inspection مستثنا کنید. |

#### کارت Lab — درس 16-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | SSL Inspection |
| 2 | پیش‌نیاز | درس ۱۶-۴ |
| 3 | توپولوژی | FGT + Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | Deep + CA |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | مرورگر |
| 11 | سناریوی خرابی | خطای گواهی در مرورگر |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | گواهی فایروال |
| 14 | معیار پذیرش | بدون خطا |
| 15 | مستندات نهایی | `03-ops/ssl-inspection.md` |
| 16 | Cleanup و بازگردانی | بازگشت Profile |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-16-6"></a>

## درس 16-6 — Performance، عیب‌یابی UTM و آزمون فصل

**فصل 16 - روز 6 · پیش‌نیاز: درس ۱۶-۵ · ۶ ساعت**

### ۱) معرفی درس

UTM منابع می‌خورد. باید اثر را بسنجید و خطاهای رایج را پیدا کنید.

### ۲) پیش‌نیازها

درس ۱۶-۵

### ۳) توضیح مفهومی

- شاخص‌ها: CPU، Memory، Session، Throughput (`get system performance status`, `diagnose sys top`).
- Flow vs Proxy و اثر آن.
- کاهش بار: Profile انتخابی، Exempt، IPS سبک.
- عیب‌یابی: Log UTM، Debug Flow، `diagnose test application ...` (`Unverified`).
- آزمون: ۵ مورد.

### ۴) مثال ساده

یک Profile ساده روی Policy کاربران.

### ۵) مثال سازمانی

سازمان: Profile استاندارد برای هر گروه (کاربران، سرورها، مهمان).

### ۶) تصویر و توپولوژی

```text
Policy -> [Profile: AV/IPS/Web/App/SSL] -> accept/block
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Monitor > Performance/Dashboard: CPU/Memory.
2. FortiView.
3. Log & Report > Security Events.

#### روش خط فرمان (CLI)

```text
get system performance status
diagnose sys top 2 20
diagnose debug flow filter addr 192.168.20.11
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `diagnose sys top`: فرایندها (q برای خروج).
- راستی‌آزمایی: CPU قبل/بعد از فعال‌سازی Profile.
- بازگشت: کاهش Profile.

### ۸) تست عملکرد

- اندازه‌گیری CPU قبل/بعد.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | CPU بالا بعد از UTM |
| شواهد/دستور | `diagnose sys top`: ipsengine/wad |
| علت | Profile گسترده |
| رفع | Profile انتخابی |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا UTM CPU می‌خورد؟ *(پاسخ: 16-6-ت1)*

**ت2.** Flow/Proxy؟ *(پاسخ: 16-6-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا اندازه‌گیری قبل/بعد؟ *(پاسخ: 16-6-م1)*

**م2.** سناریو: کندی بعد از Deep Inspection؛ چه می‌کنید؟ *(پاسخ: 16-6-م2)*

**معیار تسلط:** ساخت Profile، اتصال به Policy، اثبات با Log/تست.

**اشتباهات رایج:** فعال‌کردن بی‌برنامه؛ نادیده‌گرفتن لایسنس.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| CPU | Central Processing Unit | پردازنده | Performance |
| wad | WAD proxy daemon | فرایند Proxy | CPU |

| English sentence | ترجمه |
|---|---|
| Measure CPU before and after enabling profiles. | CPU را قبل و بعد از فعال‌سازی Profile اندازه بگیرید. |
| Apply profiles selectively. | Profileها را انتخابی اعمال کنید. |

#### کارت Lab — درس 16-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون فصل ۱۶ |
| 2 | پیش‌نیاز | درس ۱۶-۵ |
| 3 | توپولوژی | FGT + Client |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Policy v1 |
| 8 | صورت مسئله | اندازه‌گیری |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | sys top |
| 11 | سناریوی خرابی | CPU بالا بعد از UTM |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول CPU |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/utm-perf.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-16"></a>

## درس 16-7 — کارت قابلیت هر Security Profile: چه می‌بیند، چه نمی‌بیند، هزینه و راستی‌آزمایی

**فصل ۱۶ · درس افزوده (پس از ۱۶-۶) · پیش‌نیاز: ۱۶-۰، ۱۶-۱ تا ۱۶-۶ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** برای هر قابلیت وابستگی لایسنس و حالت Inspection در جدول مقایسه‌ی رسمی ([Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison)) باید تأیید شود؛ ستون «Needs-License» برای Signatureهای FortiGuard است. دستورها `Unverified`. Lab «اجرا نشده».

### ۱) هدف آموزشی

برای هر قابلیت UTM دانشجو بتواند هفت سؤال را پاسخ دهد: چه می‌کند؟ چه چیزی را می‌بیند؟ چه چیزی را نمی‌بیند؟ محدودیت؟ اثر Performance؟ کی استفاده شود؟ چگونه نتیجه‌اش را بسنجیم؟ و **تفاوت Detection و Prevention** و **False Positive/Negative** را در مثال بفهمد.

### ۲) مفاهیم پایه: False Positive و False Negative

| اصطلاح | معنی | مثال | هزینه |
|---|---|---|---|
| True Positive | تهدید واقعی، شناسایی شد | بدافزار بلاک شد | — |
| **False Positive (FP)** | بی‌خطر، به‌اشتباه تهدید گفته شد | سایت قانونی بلاک شد | اختلال کسب‌وکار |
| **False Negative (FN)** | تهدید واقعی، دیده نشد | بدافزار رد شد | نفوذ |
| True Negative | بی‌خطر، درست عبور کرد | — | — |

``` text
Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
```

هیچ سامانه‌ای FP و FN را هم‌زمان صفر نمی‌کند؛ کاهش یکی معمولاً دیگری را زیاد می‌کند. تصمیم: برای دارایی حساس FN گران‌تر است (سخت‌گیرتر)؛ برای سرویس عمومی FP گران‌تر است (سهل‌گیرتر + Monitor).

### ۳) کارت قابلیت‌ها

#### کارت ۱: Antivirus (AV)

- **چه می‌کند:** فایل/محتوا را با Signature بدافزار می‌سنجد (و در بعضی حالت‌ها Heuristic/Sandbox).
- **می‌بیند:** بدافزار شناخته‌شده در HTTP/FTP/SMTP/...، و با Deep Inspection در HTTPS.
- **نمی‌بیند:** بدافزار ناشناخته (Zero-day) بدون Sandbox، فایل رمزشده با رمز، ترافیک HTTPS بدون Deep Inspection.
- **محدودیت:** وابسته به DB (Needs-License)؛ سقف اندازه‌ی فایل؛ گزینه‌ها در Proxy بیشتر از Flow.
- **Performance:** متوسط تا زیاد (Proxy سنگین‌تر).
- **کاربرد:** دانلود کاربران، ایمیل.
- **راستی‌آزمایی:** فایل تست EICAR (بی‌خطر) و Log AV؛ نتیجه واقعی ثبت شود.

#### کارت ۲: Web Filter

- **می‌کند:** مجاز/ممنوع‌کردن وب بر اساس URL/Category/Static List.
- **می‌بیند:** نام دامنه، Category، URL (HTTP یا HTTPS با Inspection)؛ SNI در HTTPS بدون Deep.
- **نمی‌بیند:** مسیر کامل URL و محتوای HTTPS بدون Deep؛ سایت‌های Rating‌نشده.
- **محدودیت:** Category نیاز FortiGuard Rating (Needs-License)؛ Static URL بدون لایسنس.
- **Performance:** کم تا متوسط.
- **کاربرد:** سیاست استفاده‌ی قابل‌قبول، جلوگیری از سایت‌های مخرب.
- **راستی‌آزمایی:** مرورگر به سایت ممنوع؛ Block Page؛ Log Category.

#### کارت ۳: DNS Filter

- **می‌کند:** پرس‌وجوهای DNS را بر اساس Category/دامنه‌ی مخرب بلاک یا Redirect می‌کند.
- **می‌بیند:** نام دامنه‌ی DNS Query قبل از اتصال (حتی اگر بعداً HTTPS باشد).
- **نمی‌بیند:** DoH/DoT رمزشده (دور می‌زند)، IP مستقیم بدون DNS.
- **محدودیت:** Needs-License برای Category؛ DoH باید با Application Control مدیریت شود.
- **Performance:** کم.
- **کاربرد:** پوشش اولیه‌ی دامنه‌های مخرب/C2.
- **راستی‌آزمایی:** `nslookup` دامنه‌ی تست؛ Log DNS.

#### کارت ۴: Application Control

- **می‌کند:** برنامه‌ها را (حتی روی پورت‌های غیراستاندارد) با Signature شناسایی و کنترل می‌کند.
- **می‌بیند:** برنامه‌ی لایه‌ی کاربرد (Teams، BitTorrent، ...).
- **نمی‌بیند:** برنامه‌های رمزشده بدون Deep Inspection ممکن است با دقت کمتر؛ برنامه‌های ناشناخته.
- **محدودیت:** DB برنامه (Needs-License)؛ QUIC؛ بروزرسانی.
- **Performance:** متوسط.
- **کاربرد:** بلاک P2P/Proxy/Remote Tools؛ مدیریت QUIC.
- **راستی‌آزمایی:** اجرای برنامه‌ی تست و Log Application.

#### کارت ۵: IPS

- **می‌کند:** الگوی حمله/اکسپلویت را در ترافیک با Signature می‌شناسد و Block/Monitor می‌کند.
- **می‌بیند:** حمله‌ی شناخته‌شده علیه سرویس‌ها (CVE).
- **نمی‌بیند:** حمله‌ی ناشناخته (Zero-day) بدون Signature؛ حمله‌ی داخل TLS بدون Deep.
- **محدودیت:** Signature (Needs-License)؛ FP؛ تنظیم Severity/Target.
- **Performance:** زیاد؛ Offload را محدود می‌کند.
- **کاربرد:** محافظت سرور (Virtual Patching)، لبه‌ی اینترنت.
- **راستی‌آزمایی:** تست در Lab ایزوله با ابزار تست مجاز؛ Log IPS.

#### کارت ۶: File Filter

- **می‌کند:** فایل را بر اساس نوع/پسوند/Magic بلاک می‌کند.
- **می‌بیند:** نوع فایل (exe، zip، doc).
- **نمی‌بیند:** محتوای مخرب داخل نوع مجاز.
- **محدودیت:** پسوند قابل‌جعل (بهتر Magic/نوع واقعی)؛ فایل رمزشده.
- **Performance:** کم تا متوسط.
- **کاربرد:** جلوگیری از exe/script از اینترنت.
- **راستی‌آزمایی:** دانلود فایل تست exe.

#### کارت ۷: SSL/SSH Inspection

(درس ۱۶-۰) پیش‌نیاز AV/IPS/Web (محتوا) روی HTTPS؛ Performance زیاد؛ Exemption و CA الزامی.

### ۴) Detection در برابر Prevention (روش استقرار)

``` text
Phase 1  Monitor/Detect  : log only for 2 weeks; collect FP/FN data
Phase 2  Tune            : exceptions, thresholds, exemptions
Phase 3  Prevent/Block   : block high-confidence signatures; keep monitor for others
Phase 4  Review          : monthly FP/FN and performance review
```

### ۵) مثال حل‌شده

**سناریو:** پس از فعال‌کردن IPS، سیستم مالی قطع می‌شود. تحلیل: Signature اشتباه (FP) روی ترافیک سامانه‌ی مالی. اقدام: Log IPS را بررسی (Signature ID)، Exception برای آن Signature **فقط** روی آن سرور/مقصد (نه حذف کل Signature)، ثبت علت و تاریخ بازبینی. اثر امنیتی: ریسک باقی‌مانده مستند.

**مثال سخت (Evasion):** مهاجم بدافزار را در zip رمزدار می‌فرستد. AV نمی‌بیند؛ File Filter «zip» را اگر مجاز کرده باشید رد می‌کند؛ پس سیاست «zip رمزدار» با File Filter + آموزش/Sandbox تکمیل می‌شود. درس: **هر کنترل حفره دارد؛ لایه‌ها را ترکیب کنید.**

### ۶) پیاده‌سازی (GUI/CLI)

**GUI:** Security Profiles → هر Profile → Create New؛ Policy → Security Profiles → فعال‌کردن؛ Log & Report → Security Events.

**CLI (ساختار):**

``` text
config antivirus profile
    edit "AV-LAB"
    next
end
config webfilter profile
    edit "WF-LAB"
    next
end
config ips sensor
    edit "IPS-LAB"
    next
end
config application list
    edit "APP-LAB"
    next
end
config firewall policy
    edit 10
        set av-profile "AV-LAB"
        set webfilter-profile "WF-LAB"
        set ips-sensor "IPS-LAB"
        set application-list "APP-LAB"
        set ssl-ssh-profile "certificate-inspection"
    next
end
```

(نام فیلدها با CLI Reference 7.0 تطبیق شود؛ `Unverified`.)

### ۷) Verification و Performance

``` text
get system performance status
diagnose sys top 2 20
diagnose debug flow filter addr 192.168.10.5
```

**اندازه‌گیری:** CPU/Throughput را قبل و بعد از فعال‌کردن هر Profile در همان بار ثبت و مقایسه کنید.

### ۸) Troubleshooting

| علامت | علت |
|---|---|
| Profile اثر ندارد | به Policy وصل نیست، Inspection Mode، SSL Inspection |
| FP زیاد | Signature/Category، نبود Exception |
| کندی | Profile روی همه‌ی ترافیک، Proxy، Deep |
| Log UTM نیست | `logtraffic`/Log Settings |

### ۹) نکات امنیتی

- Exception را محدود (دامنه، زمان) و مستند کنید.
- UTM جایگزین Patch و Segmentation نیست.
- Profile پیش‌فرض را بدون بازبینی روی همه‌چیز فعال نکنید.

### ۱۰) جمع‌بندی مفهومی

- هر قابلیت ورودی/محدودیت/هزینه‌ی مشخص دارد.
- FP و FN هر دو هزینه دارند؛ بر اساس دارایی تعادل بگذارید.
- Monitor قبل از Block.
- Needs-License را صریح بدانید.
- با Capture/Log/EICAR نتیجه را اثبات کنید.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) FP و FN را با مثال تعریف کنید. *(پاسخ: 16-7-ت1)*

**ت2.** (ساده) Web Filter چه چیزی را در HTTPS بدون Deep می‌بیند؟ *(پاسخ: 16-7-ت2)*

**ت3.** (متوسط) چرا DNS Filter در برابر DoH ضعیف است؟ *(پاسخ: 16-7-ت3)*

**ت4.** (متوسط) IPS چرا Offload را محدود می‌کند؟ *(پاسخ: 16-7-ت4)*

**ت5.** (سخت) استقرار فازی یک IPS را با معیار خروج از هر فاز بنویسید. *(پاسخ: 16-7-ت5)*

**ت6.** (سخت، طراحی) برای ۳ دارایی (سرور مالی، کاربران، مهمان) ترکیب Profileها و Detection/Prevention را پیشنهاد دهید. *(پاسخ: 16-7-ت6)*

**Q1.** Quick quiz (English): Why can't a file filter stop malware inside an allowed file type? *(پاسخ: 16-7-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FP | False Positive | هشدار کاذب |
| FN | False Negative | عدم تشخیص |
| IPS | Intrusion Prevention System | سامانه‌ی جلوگیری از نفوذ |
| EICAR | EICAR test file | فایل تست استاندارد |
| DoH | DNS over HTTPS | DNS رمزشده |
| Zero-day | Zero-day | حمله‌ی بدون Signature |

- *Start in monitor mode, tune, then enforce.* ← با Monitor شروع کنید، تنظیم کنید، سپس اعمال کنید.
- *Every control has blind spots; combine layers.* ← هر کنترل نقطه‌ی کور دارد؛ لایه‌ها را ترکیب کنید.

### ۱۳) منابع

- Fortinet Docs: [Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison)، FortiOS 7.0 Administration Guide — Security Profiles.
- EICAR: www.eicar.org (فایل تست).

## پاسخ‌های فصل 16

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**16-1-ت1** — کدام Profileها Needs-License؟

AV، IPS، Web Rating، App DB.

**16-1-ت2** — بدون لایسنس چه؟

Static URL، Custom IPS، DoS.

**16-1-م1** — چرا Feature/License Log؟

تا ادعای بدون آزمایش نکنیم.

**16-1-م2** — سناریو: AV کار نمی‌کند؛ علت؟

لایسنس/DB.

**16-2-ت1** — Static URL نیاز لایسنس دارد؟

خیر.

**16-2-ت2** — چرا HTTPS مشکل می‌سازد؟

محتوا رمز است؛ نیاز SSL Inspection.

**16-2-م1** — چرا Static URL را ابتدا امتحان می‌کنیم؟

بدون لایسنس کار می‌کند.

**16-2-م2** — سناریو: دامنه‌ی HTTPS مسدود نشد؛ چرا؟

SSL Inspection/SNI.

**16-3-ت1** — EICAR چیست؟

فایل تست استاندارد بی‌خطر.

**16-3-ت2** — File Filter لایسنس دارد؟

خیر.

**16-3-م1** — چرا نتیجه‌ی AV را ثبت می‌کنیم؟

Unverified در Lab.

**16-3-م2** — سناریو: exe بلاک نمی‌شود؛ چرا؟

Profile روی Policy نیست.

**16-4-ت1** — DoS Policy چه می‌کند؟

محدود/مسدودکردن سیل.

**16-4-ت2** — IPS Needs-License؟

Signature رسمی بله؛ Custom خیر.

**16-4-م1** — چرا DoS روی WAN؟

ورودی حمله از اینترنت.

**16-4-م2** — سناریو: CPU بالا؛ علت محتمل IPS؟

Inspection سنگین/Profile گسترده.

**16-5-ت1** — Deep و Certificate Inspection؟

Deep رمزگشایی؛ Certificate فقط گواهی.

**16-5-ت2** — چرا CA لازم؟

تا مرورگر گواهی فایروال را بپذیرد.

**16-5-م1** — چرا بانک‌ها Exempt؟

حریم خصوصی/Pinning.

**16-5-م2** — سناریو: برنامه خطای TLS می‌دهد؛ چه می‌کنید؟

Exempt یا نصب CA.

**16-6-ت1** — چرا UTM CPU می‌خورد؟

بازرسی لایه ۷.

**16-6-ت2** — Flow/Proxy؟

Flow سبک‌تر.

**16-6-م1** — چرا اندازه‌گیری قبل/بعد؟

اثر را ثابت می‌کند.

**16-6-م2** — سناریو: کندی بعد از Deep Inspection؛ چه می‌کنید؟

Exempt/Profile انتخابی.


---

<a id="ch17"></a>


### پاسخ‌های درس افزوده‌ی 16-0 (فصل 16)

**16-0-ت1** — Flow: بازرسی در جریان بدون بازسازی کامل؛ سریع‌تر. Proxy: ختم و بازسازی؛ قابلیت بیشتر و هزینه‌ی بیشتر.

**16-0-ت2** — نام سرور در ClientHello (SNI) که معمولاً رمزنشده است و گواهی.

**16-0-ت3** — فایروال برای کلاینت گواهی جایگزین صادر می‌کند؛ مرورگر فقط اگر CA آن را بپذیرد خطا نمی‌دهد.

**16-0-ت4** — برنامه گواهی مشخصی را انتظار دارد؛ با Deep Inspection خطا می‌دهد؛ راه‌حل Exemption.

**16-0-ت5** — کاربران عادی: Deep + Exemption؛ سرورها: Certificate Inspection؛ بانک/سلامت: Exempt.

**16-0-ت6** — QUIC روی UDP 443 با TLS 1.3 قابل Inspection عمیق نیست؛ مدیریت: بلاک QUIC با Application Control تا به TCP/TLS برگردد.

**16-0-م1** — Detection فقط Log می‌کند؛ Prevention ترافیک را مسدود می‌کند.

**16-0-Q1** — Certificate inspection sees the certificate and SNI; deep inspection additionally sees the decrypted payload.


### پاسخ‌های درس افزوده‌ی 16-7 (فصل 16)

**16-7-ت1** — FP: بی‌خطر به‌اشتباه تهدید؛ FN: تهدید واقعی که دیده نشد.

**16-7-ت2** — دامنه/SNI و اطلاعات گواهی.

**16-7-ت3** — DoH درخواست DNS را داخل HTTPS رمز می‌کند و فایروال Query را نمی‌بیند.

**16-7-ت4** — IPS به بازرسی محتوا در CPU/CP نیاز دارد.

**16-7-ت5** — فاز ۱ Monitor (معیار: جمع FP)، فاز ۲ تنظیم (معیار: FP زیر آستانه)، فاز ۳ Block سیگنچرهای با اطمینان بالا، فاز ۴ بازبینی ماهانه.

**16-7-ت6** — سرور مالی: IPS Prevention + SSL Certificate + AV؛ کاربران: Web+AV+App+Deep؛ مهمان: Web Filter+DNS Filter، Prevention سبک.

**16-7-Q1** — Because the file type is allowed and the malicious content is inside that type; the filter only looks at the type.

# فصل 17 — Authentication: AD، LDAP، RADIUS، FSSO و Captive Portal

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، فصل ۷ (DNS/DHCP).
**اهداف:** Active Directory روی Windows Server (VM Lab)؛ LDAP و گروه‌ها؛ RADIUS (NPS)؛ FSSO؛ Captive Portal؛ Policy مبتنی بر هویت؛ عیب‌یابی Auth.
**Windows:** Domain Controller روی Golden Windows Server (`phase0a/Golden_W2025_Runbook.md`)؛ همه‌ی دستورهای Windows را شما اجرا می‌کنید. **رمزها نمونه‌اند.**
**نسخه:** FortiOS 7.0.3 اسمی؛ دستورها آزمایش‌نشده.
**معیار تسلط:** Policy بر اساس گروه AD؛ تست LDAP/RADIUS؛ رفع «Auth شکست» با `diagnose test authserver` و Debug.
**اشتباهات رایج:** DN اشتباه؛ ساعت نامتوازن (Kerberos)؛ پورت 389/636 بسته؛ حساب سرویس با رمز منقضی.

**درس‌های فصل:**
- [درس 17-1 — AD، DNS و DHCP روی Windows Server (آماده‌سازی Lab)](#l-17-1)
- [درس 17-2 — LDAP و Policy بر اساس گروه](#l-17-2)
- [درس 17-3 — RADIUS (NPS) و MFA](#l-17-3)
- [درس 17-4 — FSSO: Single Sign-On](#l-17-4)
- [درس 17-5 — Captive Portal، مهمان و Firewall Authentication](#l-17-5)
- [درس 17-6 — عیب‌یابی Authentication و آزمون فصل](#l-17-6)

---

<a id="l-17-1"></a>

## درس 17-0 — AAA و هویت: LDAP، Kerberos، RADIUS و FSSO از درون

**فصل ۱۷ · درس افزوده (پیش‌درس ۱۷-۱) · پیش‌نیاز: ۱۲-۰، ۱۱-۰، آشنایی با AD · ≈ ۸ ساعت**

> **وضعیت (FortiOS 7.0):** حالت‌های FSSO و محدودیت Polling از مستند رسمی ([FSSO polling connector](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/503764/fsso-polling-connector-agent-installation)، [FSSO](https://docs.fortinet.com/document/fortigate/7.0.8/administration-guide/450337)) تأیید شد؛ سینتکس روی Image `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. **AAA** (Authentication، Authorization، Accounting) را تعریف و با مثال تفکیک کند.
2. سازوکار **LDAP Bind/Search** و تفاوت **Simple/Regular Bind** را بفهمد.
3. **Kerberos** و **NTLM** را در حد مفهومی (Ticket، KDC، ساعت) و اثر آن‌ها بر FSSO بگوید.
4. **RADIUS** (Access-Request/Accept/Reject، Shared Secret، Attributes) را توضیح دهد.
5. حالت‌های **FSSO** (DC Agent، Collector Agent Polling، FortiGate Polling) را مقایسه و انتخاب کند.
6. **Policy مبتنی بر هویت** را بنویسد و محدودیت‌ها (IP→User) را بشناسد.

### ۲) پیش‌نیازها

DNS و AD (مفهوم)، Packet Flow (۱۲-۰)، مدل تهدید (۱۱-۰).

### ۳) مفهوم پایه

فایروال سنتی «IP» می‌شناسد؛ ولی امنیت واقعی بر پایه‌ی **هویت** است: «گروه Finance به سرور مالی»، نه «192.168.10.5». AAA سه پرسش را جواب می‌دهد: **تو کیستی؟ (Authentication)** **چه کاری می‌توانی بکنی؟ (Authorization)** **چه کردی؟ (Accounting)**.

### ۴) توضیح عمیق فنی

#### ۴-۱) LDAP

LDAP پروتکل پرس‌وجو از Directory است (AD یک Directory است). مراحل Authentication با LDAP:

1. فایروال به سرور LDAP **Bind** می‌کند (با حساب سرویس) تا بتواند جست‌وجو کند.
2. کاربر را با **cnid** (مثلاً `sAMAccountName`) و **DN** پایه جست‌وجو می‌کند و DN کاربر را می‌یابد.
3. با DN کاربر و رمزی که وارد کرده، **Bind دوم** انجام می‌دهد؛ موفقیت = رمز صحیح.
4. گروه‌های کاربر را (برای Authorization) می‌خواند.

نکات: پورت 389 (بدون رمزنگاری)، 636 (LDAPS)، StartTLS؛ حساب سرویس حداقل دسترسی؛ **رمز LDAP بدون رمزنگاری قابل شنود است** پس LDAPS/StartTLS.

#### ۴-۲) Kerberos و NTLM

- **Kerberos:** احراز هویت مبتنی بر Ticket؛ KDC (در DC) Ticket Granting Ticket صادر می‌کند؛ نیاز به ساعت هماهنگ (≤ 5 دقیقه اختلاف) و DNS درست. رویدادهای ورود در Security Log DC (مثلاً 4768/4769) تولید می‌شوند.
- **NTLM:** قدیمی‌تر، چالش–پاسخ؛ ضعیف‌تر و در حال حذف.
- اثر بر FSSO: طبق مستند، **FSSO Polling فقط Kerberos را پشتیبانی می‌کند** (رویدادهای 4768 و 4769)، **NTLM ساپورت نمی‌شود**، و در ورود هم‌زمان کاربران زیاد ممکن است ورودی‌ها از دست برود.

#### ۴-۳) RADIUS

- Client (فایروال) **Access-Request** به سرور (NPS) می‌فرستد با User-Name/Password (رمز با Shared Secret محافظت می‌شود).
- پاسخ: **Access-Accept** (با Attributeها مثل Group/VLAN)، **Access-Reject**، یا **Access-Challenge** (برای MFA/OTP).
- پورت UDP 1812 (Auth) و 1813 (Accounting).
- Shared Secret باید دو سر یکی باشد؛ NPS فقط Clientهای تعریف‌شده را می‌پذیرد.

#### ۴-۴) FSSO (Fortinet Single Sign-On)

هدف: کاربر یک بار به دامنه Login می‌کند؛ FSSO این ورود را به فایروال خبر می‌دهد تا **IP→User/Group** نگاشت شود و Policy بر اساس گروه کار کند، بدون Login دوباره.

| حالت | سازوکار | نکته |
|---|---|---|
| DC Agent + Collector | Agent روی هر DC رویداد را به Collector می‌دهد؛ Collector به FortiGate (TCP 8000؛ UDP 8002 برای DC Agent) | تا ۵ Collector برای Redundancy (مستند) |
| Collector Agent Polling | Collector خودش DCها را Poll می‌کند (نیاز به DC Agent نیست) | نصب روی یک سرور |
| FortiGate Polling (Agentless) | FortiGate مستقیم DC را Poll می‌کند (Security Event Log) و گروه‌ها را از LDAP می‌گیرد | فقط Kerberos 4768/4769؛ NTLM نه؛ ممکن است ورود را از دست بدهد؛ پیش‌نیاز: LDAP server تنظیم‌شده |

نکات مستند: در Polling، چون Security Event Log اطلاعات گروه ندارد، FortiGate با LDAP گروه را می‌پرسد و فقط کاربرانی که در گروه‌های Filter هستند به لیست FSSO می‌روند؛ `polling-frequency` بین 1 تا 30 ثانیه (پیش‌فرض 10).

#### ۴-۵) محدودیت‌های هویت مبتنی بر IP

- **چند کاربر روی یک IP** (Terminal Server، NAT): FSSO فقط یک کاربر را می‌بیند (راه‌حل: Terminal Server Agent).
- **IP عوض می‌شود** (DHCP، VPN): نگاشت باید به‌روز شود؛ Timeout ورود.
- **سرور/Printer بدون Login:** استثنا/Policy IP-based.
- **Spoofing:** اگر مهاجم IP کاربر را جعل کند، هویت اشتباه می‌شود؛ به Anti-spoofing و Segmentation وابسته است.

#### ۴-۶) Policy مبتنی بر هویت

Policy Source = User/Group (FSSO) به‌علاوه‌ی Subnet برای دقت. ترتیب: Policy مبتنی بر هویت وقتی Match می‌شود که نگاشت IP→User موجود باشد؛ در غیر این صورت Policy بعدی (یا Captive Portal) مطابق می‌شود.

### ۵) مثال حل‌شده

**نیاز:** گروه Finance به سرور مالی، بقیه ممنوع.

``` text
config user ldap
    edit "LDAP-AD"
        set server "192.168.90.40"
        set cnid "sAMAccountName"
        set dn "dc=lab,dc=local"
        set type regular
        set username "CN=svc-fgt,CN=Users,DC=lab,DC=local"
        set password <SERVICE-ACCOUNT-PASSWORD>
        set secure ldaps
        set port 636
    next
end
config user fsso-polling
    edit 1
        set server "192.168.90.40"
        set ldap-server "LDAP-AD"
        set polling-frequency 10
    next
end
config user group
    edit "GRP-FINANCE"
        set group-type fsso-service
        set member "CN=Finance,CN=Users,DC=lab,DC=local"
    next
end
```

(سینتکس نمونه؛ `Unverified`؛ با CLI Reference 7.0 تطبیق شود.) Policy: Source = GRP-FINANCE، Destination = SRV-FIN، Service = HTTPS.

**GUI:** User & Authentication → LDAP Servers؛ Security Fabric → External Connectors → FSSO (Poll Active Directory Server)؛ User & Authentication → User Groups؛ Policy & Objects → Firewall Policy.

**آزمون‌ها:** مثبت: کاربر Finance دسترسی دارد؛ منفی: کاربر دیگر ندارد؛ IP عوض شود؛ Terminal Server.

**مثال متوسط:** کاربر Login کرد ولی Policy مطابق نشد. علت‌ها به ترتیب: نگاشت IP→User نیامده (Polling/Log)، گروه در Filter نیست، DN اشتباه، ساعت ناهماهنگ.

**مثال سخت:** بعضی کاربران پس از ورود با NTLM در Polling دیده نمی‌شوند. علت طبق مستند: Polling فقط Kerberos. راه‌حل: Collector Agent یا اصلاح DNS/SPN تا Kerberos استفاده شود.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| LDAP یا RADIUS؟ | LDAP برای Directory/گروه؛ RADIUS برای VPN/Wi-Fi/MFA/NPS |
| FSSO کدام حالت؟ | کوچک: Polling؛ بزرگ/NTLM: Collector/DC Agent |
| رمزنگاری | LDAPS/StartTLS |
| Redundancy | چند Collector، چند LDAP |
| Fallback | Captive Portal برای IP بدون Login |

### ۷) Verification

``` text
diagnose test authserver ldap LDAP-AD <user> <password>
diagnose debug authd fsso list
diagnose debug application fnbamd -1
diagnose debug enable
diagnose debug disable
```

### ۸) Troubleshooting

| علامت | علت |
|---|---|
| Bind شکست | DN/رمز/پورت/TLS |
| کاربر یافت نمی‌شود | DN/OU/cnid |
| FSSO کاربر نیست | Kerberos/NTLM، ساعت، Event Log، Group Filter |
| RADIUS Reject | Secret/Client/Policy NPS |
| Policy مطابق نمی‌شود | نگاشت IP→User |

### ۹) نکات امنیتی

- حساب سرویس LDAP read-only؛ رمز قوی؛ ذخیره‌ی رمز در ریپو ممنوع.
- LDAP بدون TLS ممنوع در تولید.
- MFA برای مدیریت و VPN.
- Log ورود ناموفق را مانیتور کنید.

### ۱۰) جمع‌بندی مفهومی

- AAA سه سؤال: کیستی، چه می‌توانی، چه کردی.
- LDAP: Bind سرویس + Search + Bind کاربر.
- Kerberos نیازمند ساعت و DNS؛ Polling فقط Kerberos.
- RADIUS: Request/Accept/Reject با Secret.
- هویت مبتنی بر IP محدودیت دارد؛ طراحی با Fallback.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) AAA را تعریف کنید. *(پاسخ: 17-0-ت1)*

**ت2.** (ساده) پورت LDAP و LDAPS؟ *(پاسخ: 17-0-ت2)*

**ت3.** (متوسط) چرا ساعت برای Kerberos مهم است؟ *(پاسخ: 17-0-ت3)*

**ت4.** (متوسط) FSSO Polling چه محدودیتی دارد؟ *(پاسخ: 17-0-ت4)*

**ت5.** (سخت) چند کاربر روی یک Terminal Server دارید؛ چه مشکلی در FSSO پیش می‌آید؟ *(پاسخ: 17-0-ت5)*

**ت6.** (سخت، طراحی) برای ۵۰۰ کاربر ویندوزی و ۵۰ کاربر Mac/Linux راه‌حل هویت را بنویسید. *(پاسخ: 17-0-ت6)*

**Q1.** Quick quiz (English): Why does LDAP authentication use two binds? *(پاسخ: 17-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| AAA | Authentication, Authorization, Accounting | هویت، مجوز، حسابرسی |
| LDAP | Lightweight Directory Access Protocol | پروتکل Directory |
| KDC | Key Distribution Center | مرکز توزیع کلید Kerberos |
| FSSO | Fortinet Single Sign-On | ورود یکپارچه |
| NPS | Network Policy Server | سرور RADIUS ویندوز |
| DN | Distinguished Name | نام مسیر در Directory |

- *Use LDAPS or StartTLS to protect directory credentials.* ← برای محافظت از اعتبارنامه‌ها LDAPS/StartTLS بزنید.
- *FSSO maps logons to IP addresses.* ← FSSO ورود را به IP نگاشت می‌کند.

### ۱۳) منابع

- Fortinet Docs: [FSSO polling connector agent installation](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/503764/fsso-polling-connector-agent-installation)، [FSSO](https://docs.fortinet.com/document/fortigate/7.0.8/administration-guide/450337)، [config user fsso-polling](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/516620/config-user-fsso-polling).
- RFC 4511 (LDAP)، RFC 4120 (Kerberos)، RFC 2865 (RADIUS).

## درس 17-1 — AD، DNS و DHCP روی Windows Server (آماده‌سازی Lab)

**فصل 17 - روز 1 · پیش‌نیاز: فصل ۷ · ۶ ساعت**

### ۱) معرفی درس

FortiGate برای هویت به Directory نیاز دارد. DC را با دامنه‌ی `lab.local` آماده می‌کنیم.

### ۲) پیش‌نیازها

فصل ۷

### ۳) توضیح مفهومی

- DC با DNS؛ کاربران/گروه‌ها (IT، Finance) و حساب سرویس read-only.
- ساعت هماهنگ (NTP) برای Kerberos.
- FortiGate باید DNS/IP DC را بتواند برساند.
- LDAP 389 / LDAPS 636.
- رمزها نمونه، حساب سرویس حداقل دسترسی.

### ۴) مثال ساده

کاربر IT با گروه AD به منابع خاص دسترسی دارد.

### ۵) مثال سازمانی

سازمان: Policy بر اساس گروه (Finance، IT) به‌جای IP.

### ۶) تصویر و توپولوژی

```text
User -> FGT (Auth) -> AD/NPS ; Policy by group
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. (Windows GUI) Server Manager > Add Roles > AD DS و DNS.
2. Active Directory Users and Computers: گروه IT و کاربر testuser.
3. FortiGate: System > DNS: DC.

#### روش خط فرمان (CLI)

```text
# Windows PowerShell on the lab DC (lab only)
Install-WindowsFeature AD-DS -IncludeManagementTools
Install-ADDSForest -DomainName lab.local -InstallDns
New-ADGroup -Name IT -GroupScope Global
New-ADUser -Name svc-fgt -AccountPassword (Read-Host -AsSecureString) -Enabled $true
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Forest فقط در Lab؛ پس از ساخت Reboot.
- راستی‌آزمایی: `Get-ADDomain`.
- بازگشت: Snapshot VM.

### ۸) تست عملکرد

- `nslookup lab.local` و `Get-ADUser`.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | DC دیده نمی‌شود |
| شواهد/دستور | ping/ nslookup شکست |
| علت | DNS/VLAN |
| رفع | تنظیم DNS/Route |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا DNS روی DC؟ *(پاسخ: 17-1-ت1)*

**ت2.** حساب سرویس؟ *(پاسخ: 17-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا ساعت مهم؟ *(پاسخ: 17-1-م1)*

**م2.** سناریو: LDAP وصل نمی‌شود؛ بررسی؟ *(پاسخ: 17-1-م2)*

**معیار تسلط:** تنظیم Auth Server و تست با ابزار تشخیص.

**اشتباهات رایج:** DN/Port/ساعت اشتباه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| AD | Active Directory | دایرکتوری ویندوز | Auth |
| DC | Domain Controller | سرور دامنه | AD |
| LDAP | Lightweight Directory Access Protocol | پروتکل دایرکتوری | FGT |

| English sentence | ترجمه |
|---|---|
| Use a least-privilege service account for LDAP binds. | برای LDAP Bind از حساب سرویس با حداقل دسترسی استفاده کنید. |
| Synchronize time with NTP. | زمان را با NTP هماهنگ کنید. |

#### کارت Lab — درس 17-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | DC و کاربران |
| 2 | پیش‌نیاز | فصل ۷ |
| 3 | توپولوژی | DC VM + FGT |
| 4 | تجهیزات | Windows DC + FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.90.40 |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | DC آماده |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | nslookup |
| 11 | سناریوی خرابی | DC دیده نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | کاربر/گروه |
| 14 | معیار پذیرش | LDAP قابل‌اتصال |
| 15 | مستندات نهایی | `03-ops/ad-lab.md` |
| 16 | Cleanup و بازگردانی | Snapshot |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-17-2"></a>

## درس 17-2 — LDAP و Policy بر اساس گروه

**فصل 17 - روز 2 · پیش‌نیاز: درس ۱۷-۱ · ۶ ساعت**

### ۱) معرفی درس

FortiGate را به AD وصل می‌کنیم و Policy را بر اساس گروه می‌نویسیم.

### ۲) پیش‌نیازها

درس ۱۷-۱

### ۳) توضیح مفهومی

- `config user ldap`: server، cnid=sAMAccountName، dn، bind account.
- User Group با `match` گروه AD (DN کامل).
- Policy مبتنی بر هویت نیاز به Authentication فعال (Firewall Auth/Captive/FSSO).
- تست: `diagnose test authserver ldap`.
- Debug: `diagnose debug application fnbamd -1`.

### ۴) مثال ساده

کاربر IT با گروه AD به منابع خاص دسترسی دارد.

### ۵) مثال سازمانی

سازمان: Policy بر اساس گروه (Finance، IT) به‌جای IP.

### ۶) تصویر و توپولوژی

```text
User -> FGT (Auth) -> AD/NPS ; Policy by group
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. User & Authentication > LDAP Servers > Create New: Name، Server IP، Common Name Identifier sAMAccountName، Distinguished Name.
2. Bind Type Regular؛ Username/Password.
3. Test Connectivity و Test User Credentials.
4. User Groups > Create New: Remote Groups > Add > گروه IT.

#### روش خط فرمان (CLI)

```text
config user ldap
    edit "LDAP-AD"
        set server "192.168.90.40"
        set cnid "sAMAccountName"
        set dn "dc=lab,dc=local"
        set type regular
        set username "CN=svc-fgt,CN=Users,DC=lab,DC=local"
        set password <SERVICE-ACCOUNT-PASSWORD>
    next
end
diagnose test authserver ldap LDAP-AD testuser <PASSWORD>
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `dn`: ریشه‌ی جستجو.
- `username/password`: حساب Bind.
- تست باید Authentication success بدهد.
- بازگشت: `delete "LDAP-AD"`.

### ۸) تست عملکرد

- Test Connectivity موفق.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Test credentials شکست |
| شواهد/دستور | `diagnose debug application fnbamd -1` |
| علت | DN/رمز/پورت |
| رفع | اصلاح DN/رمز/Firewall |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** cnid؟ *(پاسخ: 17-2-ت1)*

**ت2.** Bind؟ *(پاسخ: 17-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا DN دقیق؟ *(پاسخ: 17-2-م1)*

**م2.** سناریو: کاربر یافت نمی‌شود؛ علت؟ *(پاسخ: 17-2-م2)*

**معیار تسلط:** تنظیم Auth Server و تست با ابزار تشخیص.

**اشتباهات رایج:** DN/Port/ساعت اشتباه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| cnid | Common name identifier | ویژگی ورود | LDAP |
| DN | Distinguished Name | نام مسیر | LDAP |
| Bind | LDAP bind | احراز حساب سرویس | LDAP |

| English sentence | ترجمه |
|---|---|
| Test the LDAP connection before building policies. | قبل از ساخت Policy اتصال LDAP را تست کنید. |
| Use the full DN of the group. | از DN کامل گروه استفاده کنید. |

#### کارت Lab — درس 17-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | LDAP |
| 2 | پیش‌نیاز | درس ۱۷-۱ |
| 3 | توپولوژی | FGT + DC |
| 4 | تجهیزات | FGT + DC |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.90.40 |
| 7 | وضعیت اولیه | DC آماده |
| 8 | صورت مسئله | LDAP + Group |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | diagnose test |
| 11 | سناریوی خرابی | Test credentials شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | success |
| 14 | معیار پذیرش | کاربر تأیید |
| 15 | مستندات نهایی | `03-ops/ldap.md` |
| 16 | Cleanup و بازگردانی | حذف LDAP |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-17-3"></a>

## درس 17-3 — RADIUS (NPS) و MFA

**فصل 17 - روز 3 · پیش‌نیاز: درس ۱۷-۲ · ۶ ساعت**

### ۱) معرفی درس

RADIUS برای Authentication VPN/Wi-Fi/Firewall با NPS ویندوز یا سرور دیگر.

### ۲) پیش‌نیازها

درس ۱۷-۲

### ۳) توضیح مفهومی

- `config user radius`: server، secret.
- NPS: Network Policy/Client (FGT به‌عنوان RADIUS Client).
- پورت‌ها UDP 1812/1813.
- MFA (مفهومی): OTP/Token.
- تست: `diagnose test authserver radius`.

### ۴) مثال ساده

کاربر IT با گروه AD به منابع خاص دسترسی دارد.

### ۵) مثال سازمانی

سازمان: Policy بر اساس گروه (Finance، IT) به‌جای IP.

### ۶) تصویر و توپولوژی

```text
User -> FGT (Auth) -> AD/NPS ; Policy by group
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. User & Authentication > RADIUS Servers > Create New.
2. Name، Primary Server IP، Secret.
3. Test Connectivity.
4. NPS (Windows): RADIUS Clients > New > IP فایروال و Secret.

#### روش خط فرمان (CLI)

```text
config user radius
    edit "RADIUS-NPS"
        set server "192.168.90.41"
        set secret <RADIUS-SECRET>
    next
end
diagnose test authserver radius RADIUS-NPS pap testuser <PASSWORD>
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Secret باید در NPS هم یکی باشد.
- `pap`: روش تست.
- بازگشت: `delete`.

### ۸) تست عملکرد

- Test موفق.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Access-Reject |
| شواهد/دستور | NPS Event Log |
| علت | Secret/Policy NPS |
| رفع | تطبیق Secret/Policy |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** پورت RADIUS؟ *(پاسخ: 17-3-ت1)*

**ت2.** Secret؟ *(پاسخ: 17-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا RADIUS Client لازم؟ *(پاسخ: 17-3-م1)*

**م2.** سناریو: Reject؛ بررسی؟ *(پاسخ: 17-3-م2)*

**معیار تسلط:** تنظیم Auth Server و تست با ابزار تشخیص.

**اشتباهات رایج:** DN/Port/ساعت اشتباه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RADIUS | Remote Authentication Dial-In User Service | پروتکل AAA | VPN/Wi-Fi |
| NPS | Network Policy Server | سرور RADIUS ویندوز | Windows |
| MFA | Multi-Factor Authentication | احراز چندعاملی | VPN |

| English sentence | ترجمه |
|---|---|
| Define the firewall as a RADIUS client on NPS. | فایروال را در NPS به‌عنوان RADIUS Client تعریف کنید. |
| The shared secret must match. | Secret مشترک باید یکی باشد. |

#### کارت Lab — درس 17-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | RADIUS |
| 2 | پیش‌نیاز | درس ۱۷-۲ |
| 3 | توپولوژی | FGT + NPS |
| 4 | تجهیزات | FGT + Windows NPS |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 192.168.90.41 |
| 7 | وضعیت اولیه | DC |
| 8 | صورت مسئله | RADIUS |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | diagnose test |
| 11 | سناریوی خرابی | Access-Reject |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | success |
| 14 | معیار پذیرش | تأیید |
| 15 | مستندات نهایی | `03-ops/radius.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-17-4"></a>

## درس 17-4 — FSSO: Single Sign-On

**فصل 17 - روز 4 · پیش‌نیاز: درس ۱۷-۳ · ۶ ساعت**

### ۱) معرفی درس

FSSO ورود ویندوزی کاربر را به FortiGate اطلاع می‌دهد تا کاربر دوباره لاگین نکند.

### ۲) پیش‌نیازها

درس ۱۷-۳

### ۳) توضیح مفهومی

- Collector Agent روی DC یا پیمایش مستقیم (DC Agent / Polling).
- FSSO groups در Policy.
- پورت‌ها (TCP 8000 و ...) `Unverified`.
- نیاز به Event Log خواندن از DC.
- مناسب شبکه‌ی ویندوزی.

### ۴) مثال ساده

کاربر IT با گروه AD به منابع خاص دسترسی دارد.

### ۵) مثال سازمانی

سازمان: Policy بر اساس گروه (Finance، IT) به‌جای IP.

### ۶) تصویر و توپولوژی

```text
User -> FGT (Auth) -> AD/NPS ; Policy by group
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Security Fabric > External Connectors > Create New > FSSO Agent on Windows AD.
2. Name، Primary FSSO agent، Password.
3. User Groups: FSSO > Members.
4. Policy: Source = گروه FSSO.

#### روش خط فرمان (CLI)

```text
config user fsso
    edit "FSSO-AD"
        set server "192.168.90.40"
        set password <FSSO-PASSWORD>
    next
end
diagnose debug authd fsso list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `diagnose debug authd fsso list`: کاربران لاگین‌شده (`Unverified`).
- بازگشت: `delete`.

### ۸) تست عملکرد

- ورود کاربر دامنه‌ای و دیدن در FSSO list.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | کاربر شناسایی نمی‌شود |
| شواهد/دستور | `fsso list` خالی |
| علت | Agent/Log/Port |
| رفع | بررسی Agent و ارتباط |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** FSSO چیست؟ *(پاسخ: 17-4-ت1)*

**ت2.** چرا کاربر دوباره لاگین نمی‌کند؟ *(پاسخ: 17-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا ساعت مهم؟ *(پاسخ: 17-4-م1)*

**م2.** سناریو: گروه خالی؛ چرا؟ *(پاسخ: 17-4-م2)*

**معیار تسلط:** تنظیم Auth Server و تست با ابزار تشخیص.

**اشتباهات رایج:** DN/Port/ساعت اشتباه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| FSSO | Fortinet Single Sign-On | ورود یکپارچه | AD |
| Collector | FSSO collector agent | جمع‌آوری ورود | DC |

| English sentence | ترجمه |
|---|---|
| FSSO maps Windows logons to firewall identities. | FSSO ورودهای ویندوز را به هویت‌های فایروال نگاشت می‌کند. |
| Verify the collector can read the domain controller logs. | بررسی کنید Collector می‌تواند Log دامنه را بخواند. |

#### کارت Lab — درس 17-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | FSSO |
| 2 | پیش‌نیاز | درس ۱۷-۳ |
| 3 | توپولوژی | FGT + DC + Client |
| 4 | تجهیزات | FGT + DC |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | LDAP آماده |
| 8 | صورت مسئله | FSSO |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | fsso list |
| 11 | سناریوی خرابی | کاربر شناسایی نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | کاربر دیده شود |
| 14 | معیار پذیرش | Policy گروهی |
| 15 | مستندات نهایی | `03-ops/fsso.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-17-5"></a>

## درس 17-5 — Captive Portal، مهمان و Firewall Authentication

**فصل 17 - روز 5 · پیش‌نیاز: درس ۱۷-۴ · ۶ ساعت**

### ۱) معرفی درس

برای مهمان/کاربران غیر دامنه‌ای، صفحه‌ی Login قبل از دسترسی.

### ۲) پیش‌نیازها

درس ۱۷-۴

### ۳) توضیح مفهومی

- Interface `security-mode captive-portal` یا Policy با Authentication.
- Groups مجاز.
- HTTPS Redirect و Certificate.
- Timeout و Re-auth.
- Guest: حساب موقت (Local User).

### ۴) مثال ساده

کاربر IT با گروه AD به منابع خاص دسترسی دارد.

### ۵) مثال سازمانی

سازمان: Policy بر اساس گروه (Finance، IT) به‌جای IP.

### ۶) تصویر و توپولوژی

```text
User -> FGT (Auth) -> AD/NPS ; Policy by group
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces > VLAN50 > Security Mode: Captive Portal؛ Authentication Portal: Local؛ Groups.
2. User & Authentication > User Definition > Local User.
3. Policy برای VLAN50.
4. تست مرورگر.

#### روش خط فرمان (CLI)

```text
config system interface
    edit "VLAN50"
        set security-mode captive-portal
        set security-groups "GRP-GUEST"
    next
end
config user local
    edit "guest1"
        set type password
        set passwd <GUEST-PASSWORD>
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `security-mode captive-portal`: Portal روی VLAN.
- Local User موقت.
- راستی‌آزمایی: مرورگر به صفحه‌ی Login هدایت.
- بازگشت: `set security-mode none`.

### ۸) تست عملکرد

- ورود Guest و دسترسی اینترنت.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Portal باز نمی‌شود |
| شواهد/دستور | HTTP/HTTPS؛ Certificate |
| علت | allowaccess/Portal |
| رفع | تنظیم Portal |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Captive Portal چه کاری می‌کند؟ *(پاسخ: 17-5-ت1)*

**ت2.** Guest حساب چگونه؟ *(پاسخ: 17-5-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Certificate مهم؟ *(پاسخ: 17-5-م1)*

**م2.** سناریو: Login لوپ؛ علت؟ *(پاسخ: 17-5-م2)*

**معیار تسلط:** تنظیم Auth Server و تست با ابزار تشخیص.

**اشتباهات رایج:** DN/Port/ساعت اشتباه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Captive portal | Captive portal | صفحه‌ی Login | Guest |
| Local user | Local user | کاربر محلی | Guest |

| English sentence | ترجمه |
|---|---|
| Use a captive portal for guest access. | برای دسترسی مهمان از Captive Portal استفاده کنید. |
| Time-limit the guest accounts. | حساب‌های مهمان را زمان‌دار کنید. |

#### کارت Lab — درس 17-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Captive Portal |
| 2 | پیش‌نیاز | درس ۱۷-۴ |
| 3 | توپولوژی | FGT + Guest PC |
| 4 | تجهیزات | FGT + Client |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | VLAN50 |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | Portal |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | مرورگر |
| 11 | سناریوی خرابی | Portal باز نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Login |
| 14 | معیار پذیرش | دسترسی |
| 15 | مستندات نهایی | `03-ops/captive.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-17-6"></a>

## درس 17-6 — عیب‌یابی Authentication و آزمون فصل

**فصل 17 - روز 6 · پیش‌نیاز: درس ۱۷-۵ · ۶ ساعت**

### ۱) معرفی درس

عیب‌یابی منظم: ارتباط، DNS، ساعت، DN، رمز، پورت.

### ۲) پیش‌نیازها

درس ۱۷-۵

### ۳) توضیح مفهومی

- چک‌لیست: ping/پورت، DNS، ساعت، DN، حساب سرویس، Secret.
- ابزار: `diagnose test authserver`, `diagnose debug application fnbamd -1`.
- سناریوها: LDAP DN غلط، RADIUS Secret، FSSO Agent.
- آزمون: ۵ مورد.

### ۴) مثال ساده

کاربر IT با گروه AD به منابع خاص دسترسی دارد.

### ۵) مثال سازمانی

سازمان: Policy بر اساس گروه (Finance، IT) به‌جای IP.

### ۶) تصویر و توپولوژی

```text
User -> FGT (Auth) -> AD/NPS ; Policy by group
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Events (User).
2. User Monitor.
3. Test در GUI.

#### روش خط فرمان (CLI)

```text
diagnose debug application fnbamd -1
diagnose debug enable
diagnose test authserver ldap LDAP-AD testuser <PASSWORD>
diagnose debug disable
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- خروجی را با شناسه‌ی خطا بخوانید.
- بازگشت: debug disable.

### ۸) تست عملکرد

- سه خطای Auth را رفع کنید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Auth شکست |
| شواهد/دستور | Debug: bind failed |
| علت | رمز/DN |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** ابزار تست؟ *(پاسخ: 17-6-ت1)*

**ت2.** Debug؟ *(پاسخ: 17-6-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا چک‌لیست؟ *(پاسخ: 17-6-م1)*

**م2.** سناریو: فقط یک کاربر؛ چرا؟ *(پاسخ: 17-6-م2)*

**معیار تسلط:** تنظیم Auth Server و تست با ابزار تشخیص.

**اشتباهات رایج:** DN/Port/ساعت اشتباه.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| fnbamd | FortiGate authentication daemon | فرایند Auth | Debug |

| English sentence | ترجمه |
|---|---|
| Use the test tools before reading debug output. | قبل از Debug از ابزار تست استفاده کنید. |

#### کارت Lab — درس 17-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون Auth |
| 2 | پیش‌نیاز | درس ۱۷-۵ |
| 3 | توپولوژی | FGT + DC + NPS |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Auth آماده |
| 8 | صورت مسئله | سه خطا |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | diagnose |
| 11 | سناریوی خرابی | Auth شکست |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | RCA |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/rca-auth.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-17"></a>

## درس 17-7 — عیب‌یابی Authentication بر اساس شواهد: از Bind تا Policy

**فصل ۱۷ · درس افزوده (پس از ۱۷-۶) · پیش‌نیاز: ۱۷-۰، ۱۴-۷ · ≈ ۴ ساعت**

> **وضعیت:** `Unverified` روی Image؛ فرمت خروجی نمونه است.

### ۱) هدف آموزشی

مشکل Authentication را لایه‌به‌لایه (شبکه، TLS، Bind، Search، Group، نگاشت، Policy) پیدا و رفع کند و برای هر لایه شاهد جمع کند.

### ۲) مفهوم پایه

«Login نمی‌شود» علامت است؛ علت ممکن است در هر نقطه‌ی زنجیره‌ی **کاربر → فایروال → سرور Auth → Directory → گروه → Policy** باشد. با تقسیم مسیر (۱۴-۷) هر حلقه را جدا می‌آزماییم.

### ۳) توضیح عمیق فنی

| لایه | سؤال | آزمون |
|---|---|---|
| شبکه | فایروال به سرور می‌رسد؟ | `execute ping`، Sniffer روی 389/636/1812 |
| DNS/ساعت | نام و زمان درست؟ | `execute nslookup`، NTP |
| TLS | گواهی LDAPS معتبر؟ | Capture، پیام خطای TLS |
| Bind | حساب سرویس درست؟ | `diagnose test authserver ldap` |
| Search | DN/cnid درست؟ | Debug fnbamd |
| گروه | کاربر عضو گروه؟ | AD Users and Computers |
| FSSO | نگاشت IP→User هست؟ | `diagnose debug authd fsso list` |
| Policy | Source گروه درست؟ | Debug Flow (Policy ID) |

#### ۳-۱) خواندن خطاها

- **Invalid credentials (49):** رمز/DN کاربر اشتباه.
- **Can't contact LDAP server:** شبکه/پورت/TLS.
- **No such object (32):** DN پایه اشتباه.
- RADIUS **Access-Reject:** Secret/Policy NPS؛ **بدون پاسخ:** Firewall/Client تعریف نشده.

#### ۳-۲) FSSO

- کاربر Login کرده ولی در لیست نیست: Event Log DC (Kerberos)، Group Filter، ارتباط Collector (TCP 8000)، ساعت.
- کاربر در لیست هست ولی Policy مطابق نمی‌شود: گروه در Policy/Group Mapping، ترتیب Policy.

### ۴) مثال حل‌شده

**پرونده:** کاربر testuser Login نمی‌شود.

``` text
FGT # diagnose test authserver ldap LDAP-AD testuser <PASSWORD>
FGT # diagnose debug application fnbamd -1
FGT # diagnose debug enable
```

شواهد (نمونه): `ldap_bind... error 49` ← رمز یا DN. بررسی: حساب سرویس OK (تست جداگانه)، DN کاربر با `cnid` ناسازگار بود (`userPrincipalName` به‌جای `sAMAccountName`). **رفع:** `cnid` اصلاح. **تأیید:** تست دوباره + Login واقعی + Log. **پیشگیری:** مستندسازی cnid.

``` text
FGT # diagnose debug disable
FGT # diagnose debug reset
```

**مثال سخت:** فقط کاربران یک OU Login می‌شوند. علت: `dn` پایه روی OU محدود. **رفع:** dn پایه‌ی دامنه یا چند Search.

### ۵) GUI و CLI

**GUI:** User & Authentication → LDAP Servers → Test Connectivity / Test User Credentials؛ Monitor → Firewall User Monitor؛ Log & Report → Events → User.

**CLI:** `diagnose test authserver ...`، `diagnose debug authd fsso list`، `diagnose debug application fnbamd -1`.

### ۶) نکات امنیتی

- Debug رمز را آشکار می‌کند؛ فایل Capture را حذف کنید.
- تست با کاربر واقعی در Change.

### ۷) جمع‌بندی

Auth را در ۸ لایه تقسیم کنید؛ شاهد جمع کنید؛ یک تغییر در هر زمان؛ Debug را Disable کنید.

### ۸) تمرین و ارزیابی

**ت1.** (ساده) خطای 49 LDAP یعنی چه؟ *(پاسخ: 17-7-ت1)*

**ت2.** (متوسط) نقشه‌ی «لایه → آزمون» را بنویسید. *(پاسخ: 17-7-ت2)*

**ت3.** (سخت) FSSO کاربر را نشان می‌دهد ولی Policy مطابق نمی‌شود؛ ۴ فرضیه و آزمون. *(پاسخ: 17-7-ت3)*

**Q1.** Quick quiz (English): Which tool checks an LDAP login independently of firewall policies? *(پاسخ: 17-7-Q1)*

### ۹) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| fnbamd | FortiGate authentication daemon | فرایند Authentication |
| cnid | Common name identifier | ویژگی نام ورود |
| Bind | LDAP bind | ورود به Directory |

- *Test authentication with the CLI tool before debugging policies.* ← قبل از Policy، Authentication را با ابزار CLI تست کنید.

### ۱۰) منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Authentication؛ CLI Reference `diagnose test authserver`.

## پاسخ‌های فصل 17

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**17-1-ت1** — چرا DNS روی DC؟

AD بدون DNS کار نمی‌کند.

**17-1-ت2** — حساب سرویس؟

حداقل دسترسی read-only.

**17-1-م1** — چرا ساعت مهم؟

Kerberos.

**17-1-م2** — سناریو: LDAP وصل نمی‌شود؛ بررسی؟

پورت و DNS.

**17-2-ت1** — cnid؟

نام ویژگی ورود (sAMAccountName).

**17-2-ت2** — Bind؟

ورود حساب سرویس.

**17-2-م1** — چرا DN دقیق؟

جستجو در مسیر درست.

**17-2-م2** — سناریو: کاربر یافت نمی‌شود؛ علت؟

DN/OU اشتباه.

**17-3-ت1** — پورت RADIUS؟

UDP 1812/1813.

**17-3-ت2** — Secret؟

رمز مشترک Client/Server.

**17-3-م1** — چرا RADIUS Client لازم؟

NPS فقط Clientهای تعریف‌شده را می‌پذیرد.

**17-3-م2** — سناریو: Reject؛ بررسی؟

Event Viewer NPS.

**17-4-ت1** — FSSO چیست؟

انتقال هویت ورود ویندوز به FGT.

**17-4-ت2** — چرا کاربر دوباره لاگین نمی‌کند؟

SSO.

**17-4-م1** — چرا ساعت مهم؟

Kerberos.

**17-4-م2** — سناریو: گروه خالی؛ چرا؟

Collector نمی‌بیند.

**17-5-ت1** — Captive Portal چه کاری می‌کند؟

Login قبل از دسترسی.

**17-5-ت2** — Guest حساب چگونه؟

Local User موقت.

**17-5-م1** — چرا Certificate مهم؟

HTTPS Redirect.

**17-5-م2** — سناریو: Login لوپ؛ علت؟

Certificate/Redirect.

**17-6-ت1** — ابزار تست؟

diagnose test authserver.

**17-6-ت2** — Debug؟

fnbamd.

**17-6-م1** — چرا چک‌لیست؟

ترتیب سریع.

**17-6-م2** — سناریو: فقط یک کاربر؛ چرا؟

گروه/پسورد.


---

<a id="ch18"></a>


### پاسخ‌های درس افزوده‌ی 17-0 (فصل 17)

**17-0-ت1** — Authentication (کیستی)، Authorization (چه می‌توانی)، Accounting (چه کردی).

**17-0-ت2** — LDAP 389؛ LDAPS 636.

**17-0-ت3** — Kerberos به Ticket با Timestamp وابسته است؛ اختلاف زمان زیاد باعث رد Ticket می‌شود.

**17-0-ت4** — فقط Kerberos (4768/4769)؛ NTLM پشتیبانی نمی‌شود؛ در ورود هم‌زمان زیاد ممکن است ورودی از دست برود.

**17-0-ت5** — چند کاربر یک IP دارند و FSSO فقط یک نگاشت IP→User می‌بیند؛ راه‌حل Terminal Server Agent یا Policy IP-based.

**17-0-ت6** — ویندوز: FSSO + LDAP؛ Mac/Linux: Captive Portal/RADIUS یا Policy IP-based؛ MFA برای VPN؛ Fallback و Redundancy.

**17-0-Q1** — The first bind uses a service account to find the user DN; the second bind with the user DN and password verifies the password.


### پاسخ‌های درس افزوده‌ی 17-7 (فصل 17)

**17-7-ت1** — Invalid credentials: رمز یا DN کاربر اشتباه.

**17-7-ت2** — شبکه (ping/Sniffer)، DNS/ساعت، TLS، Bind، Search/DN، گروه، نگاشت FSSO، Policy.

**17-7-ت3** — ۱) نگاشت IP→User منقضی؛ ۲) گروه در Group Filter/Policy نیست؛ ۳) ترتیب Policy؛ ۴) IP عوض شده. آزمون: fsso list، Debug Flow، Log.

**17-7-Q1** — diagnose test authserver (the authentication test command).

# فصل 18 — IPsec Site-to-Site: IKEv2، Phase 1/2، MTU و عیب‌یابی (G7)

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۱۴؛ فصل ۵ (Routing).
**اهداف:** مفهوم IPsec (IKE Phase 1/2، SA، Proposal)؛ ساخت Tunnel بین دو FortiGate (و بعداً CSR)؛ Static Route و Policy برای ترافیک Tunnel؛ MTU/MSS؛ عیب‌یابی «Tunnel بالا ولی ترافیک نه».
**نسخه:** FortiOS 7.0.3 اسمی؛ دستورها آزمایش‌نشده. IPsec در Lab بدون لایسنس ممکن است (`Unverified`).
**Gate G7:** Tunnel بالا + ترافیک دوطرفه + سناریوی عیب Phase 2 mismatch.
**اشتباهات رایج:** Proposal ناهمسان؛ Selector نادرست؛ Route/Policy فراموش‌شده؛ NAT-T؛ MTU.

**درس‌های فصل:**
- [درس 18-1 — مفهوم IPsec: IKE، SA و Proposal](#l-18-1)
- [درس 18-2 — ساخت Tunnel بین دو FortiGate (CLI و GUI)](#l-18-2)
- [درس 18-3 — عیب‌یابی IPsec: Phase 1/2 و Debug](#l-18-3)
- [درس 18-4 — MTU/MSS و Fragmentation در Tunnel](#l-18-4)
- [درس 18-5 — Tunnel با Cisco CSR و Dead Peer Detection](#l-18-5)
- [درس 18-6 — Gate G7 و آزمون فصل](#l-18-6)

---

<a id="l-18-1"></a>

## درس 18-0 — IPsec از پایه تا عیب‌یابی لایه‌ای: IKE، SA، PFS، Selector، Rekey و NAT-T

**فصل ۱۸ · درس افزوده (پیش‌درس ۱۸-۱، تکمیل ۱۸-۱ و ۱۸-۲) · پیش‌نیاز: ۵-۰، ۱۲-۰، مفاهیم رمزنگاری · ≈ ۱۰ ساعت**

> **وضعیت (FortiOS 7.0.3):** پیش‌فرض‌ها از CLI Reference 7.0 ([phase1-interface](https://docs.fortinet.com/document/fortigate/7.0.5/cli-reference/371620/config-vpn-ipsec-phase1-interface)، [phase2-interface](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/371620/config-vpn-ipsec-phase2-interface)) بررسی شد: `ike-version` پیش‌فرض ۱، DPD پیش‌فرض on-demand و `dpd-retrycount` ۳، `npu-offload` پیش‌فرض enable، Phase 1 keylife پیش‌فرض 86400، Phase 2 PFS پیش‌فرض enable و keylifeseconds پیش‌فرض 43200؛ مستند خود تأکید می‌کند بین نقطه‌نسخه‌ها فرق دارد. Lab «اجرا نشده».

### ۱) هدف آموزشی

دانشجو در پایان می‌تواند:

1. توضیح دهد IPsec چه تضمین‌هایی می‌دهد (محرمانگی، یکپارچگی، احراز هویت، ضد Replay).
2. **IKEv1 و IKEv2**، Phase 1/Phase 2 و **Child SA** را مقایسه کند.
3. الگوریتم‌های رمز (AES/GCM)، یکپارچگی (SHA2)، **Diffie-Hellman** و **PFS** را توضیح دهد و انتخاب کند.
4. **Traffic Selector** را بفهمد و ناسازگاری آن را کشف کند.
5. **Route-based در برابر Policy-based VPN** را مقایسه و انتخاب کند.
6. **NAT-T، DPD، Rekey/Lifetime** و رفتار ناپایداری Tunnel را تحلیل کند.
7. مشکل VPN را **لایه‌به‌لایه** کشف کند: شبکه، IKE، هویت، Proposal، Selector، Routing، Policy، MTU.

### ۲) پیش‌نیازها

مفاهیم کلید متقارن/نامتقارن، هش، تبادل کلید (به‌طور شهودی)؛ Routing (فصل ۵)؛ Packet Flow (۱۲-۰)؛ MTU/MSS (۱۸-۴).

### ۳) مفهوم پایه

اینترنت امن نیست. IPsec یک «لوله‌ی رمزشده» بین دو Gateway می‌سازد تا شبکه‌های خصوصی از میان اینترنت با هم صحبت کنند. IPsec در لایه‌ی ۳ است (برخلاف TLS که لایه‌ی کاربرد/انتقال است) و به همین دلیل برای **هر** ترافیک IP قابل‌استفاده است.

> **تشبیه:** دو دفتر قرار است نامه‌ها را با پیک امن رد و بدل کنند. اول (Phase 1) هویت یکدیگر را در یک اتاق خصوصی تأیید و یک رمز مشترک برای مکالمات مدیریتی می‌سازند. سپس (Phase 2) برای هر دسته‌ی نامه یک پاکت مهر‌ومومشده و قفل مخصوص می‌سازند (کلید داده).

### ۴) توضیح عمیق فنی

#### ۴-۱) تضمین‌های IPsec

| تضمین | سازوکار |
|---|---|
| محرمانگی | رمزنگاری (AES-CBC/GCM) |
| یکپارچگی | HMAC/AEAD (SHA-2، GCM) |
| احراز هویت | PSK یا گواهی/Certificate |
| ضد Replay | شماره‌ی توالی (Sequence Number) |

پروتکل‌ها: **ESP** (رمز + یکپارچگی؛ پروتکل IP 50) و **AH** (فقط یکپارچگی؛ کم‌کاربرد). مدیریت کلید: **IKE** (UDP 500؛ و UDP 4500 با NAT-T).

#### ۴-۲) IKEv1 و IKEv2

| | IKEv1 | IKEv2 |
|---|---|---|
| مراحل | Phase 1 (Main/Aggressive) + Phase 2 (Quick Mode) | IKE_SA_INIT + IKE_AUTH + CREATE_CHILD_SA |
| تعداد پیام | بیشتر (Main: 6 + QM: 3) | کمتر (معمولاً ۴ پیام برای Tunnel) |
| EAP/MOBIKE | محدود | EAP، MOBIKE |
| Traffic Selector | Phase 2 Selector تک‌جفت | Selector چندگانه (Narrowing) |
| پایداری | قدیمی‌تر | مدرن‌تر؛ بهبود NAT-T و DPD |
| پیش‌فرض FortiOS 7.0 | ۱ (طبق CLI Reference) | باید صریحاً `set ike-version 2` |

**Aggressive Mode (IKEv1)** هویت را به‌صورت آشکار می‌فرستد و در برابر حمله‌ی Offline روی PSK ضعیف‌تر است؛ مورد استفاده با Dial-up قدیمی. در طراحی جدید IKEv2 ترجیح داده می‌شود.

#### ۴-۳) IKE SA و Child SA

``` text
Phase 1 / IKE SA : authenticate peers, negotiate IKE proposal, derive keys for IKE channel
Phase 2 / Child SA: negotiate IPsec proposal and traffic selectors, derive keys for ESP data
```

هر Child SA در هر جهت یک **SPI** دارد. Tunnel «بالا» یعنی هر دو SA برقرارند.

#### ۴-۴) الگوریتم‌ها، DH و PFS

- **Encryption:** AES-128/256 (CBC یا GCM)؛ GCM هم رمز و هم یکپارچگی (AEAD).
- **Integrity/PRF:** SHA-256/384/512؛ MD5/SHA-1 منسوخ.
- **DH Group:** تبادل کلید اولیه. گروه‌های کوچک (۱، ۲، ۵) ضعیف‌اند؛ ≥ 14 (2048-bit MODP) یا منحنی‌های بیضوی (19، 20، 21) توصیه می‌شود (راهنمای NIST/RFC؛ دقیق‌ترین گزینه‌ها را از سیاست سازمان بگیرید).
- **PFS (Perfect Forward Secrecy):** در هر Rekey Phase 2 یک تبادل DH تازه انجام می‌شود تا افشای کلید بلندمدت، ترافیک گذشته را باز نکند. طبق CLI Reference 7.0 پیش‌فرض Phase 2 PFS روشن است. هزینه: CPU بیشتر هنگام Rekey؛ **ناسازگاری PFS/DH group بین دو سر یکی از رایج‌ترین دلایل شکست Phase 2** است.

#### ۴-۵) احراز هویت

- **PSK:** ساده؛ باید طولانی/تصادفی؛ مدیریت سخت در مقیاس.
- **Certificate:** مقیاس‌پذیر و امن‌تر؛ نیازمند PKI و CRL/OCSP.
- Peer ID: `peertype`/`peerid` هنگام چند Peer یا Aggressive مهم است.

#### ۴-۶) Traffic Selector و Route-based/Policy-based

**Selector** می‌گوید کدام ترافیک وارد Tunnel شود (Local/Remote Subnet).

- **Policy-based:** Selector همان Policy رمزنگاری است؛ هر جفت Subnet = SA جداگانه؛ ساده برای دو شبکه ولی مقیاس‌پذیر نیست؛ Routing پویا مشکل.
- **Route-based (Interface-based) — توصیه‌ی اصلی FortiOS:** Tunnel یک Interface مجازی است؛ Selector معمولاً `0.0.0.0/0` ↔ `0.0.0.0/0` و **Routing + Firewall Policy** تعیین می‌کنند چه چیزی عبور کند. مناسب Hub-and-Spoke، OSPF/BGP روی Tunnel، SD-WAN.

> **قانون:** در Route-based سه چیز باید هم‌زمان درست باشند: **Route به Tunnel Interface، Policy دوطرفه، Selector سازگار.**

#### ۴-۷) NAT-T

اگر بین دو Peer NAT باشد، ESP (پروتکل 50) عبور نمی‌کند. **NAT-T** ESP را داخل UDP 4500 کپسوله می‌کند. در Phase 1 `nattraversal` (پیش‌فرض enable) و باز بودن UDP 500/4500. علامت: Tunnel بالا ولی ESP ترافیک ندارد.

#### ۴-۸) DPD، Rekey و Lifetime

- **DPD (Dead Peer Detection):** پیام دوره‌ای برای کشف مرگ Peer؛ پیش‌فرض on-demand (طبق CLI 7.0) با `dpd-retrycount` ۳؛ زمان‌های کوتاه Failover سریع می‌دهند ولی با Jitter لینک Flap می‌کنند.
- **Keylife:** Phase 1 پیش‌فرض 86400 s؛ Phase 2 پیش‌فرض 43200 s (طبق CLI Reference 7.0). **Rekey** قبل از انقضا انجام می‌شود تا SA بدون قطع تعویض شود.
- ناسازگاری Lifetime دو سر: معمولاً مشکل نیست (کوچک‌تر برنده می‌شود)، ولی با تجهیزات برخی سازندگان باعث Rekey ناموفق/قطع دوره‌ای می‌شود.

#### ۴-۹) MTU و MSS

سربار ESP/UDP (تقریباً ۵۰ تا ۸۰ بایت بسته به الگوریتم و NAT-T) اندازه‌ی مؤثر بسته را کم می‌کند. علامت: ping کوچک OK، دانلود بزرگ قفل (درس ۱۸-۴). راه‌حل: کاهش MTU Tunnel یا `tcp-mss-sender/receiver`.

### ۵) مثال حل‌شده (Route-based S2S)

``` text
config vpn ipsec phase1-interface
    edit "TO-B"
        set interface "wan1"
        set ike-version 2
        set remote-gw 203.0.113.2
        set peertype any
        set proposal aes256gcm-prfsha256
        set dhgrp 20
        set dpd on-idle
        set dpd-retrycount 3
        set nattraversal enable
        set psksecret <PSK-LAB>
    next
end
config vpn ipsec phase2-interface
    edit "TO-B-P2"
        set phase1name "TO-B"
        set proposal aes256gcm
        set pfs enable
        set dhgrp 20
        set src-subnet 0.0.0.0 0.0.0.0
        set dst-subnet 0.0.0.0 0.0.0.0
    next
end
config router static
    edit 100
        set dst 192.168.20.0 255.255.255.0
        set device "TO-B"
    next
end
```

(مقادیر الگوریتم نمونه‌اند؛ نام دقیق Proposal/`dpd on-idle` با CLI Reference 7.0 و سیاست سازمان تطبیق شود؛ `Unverified`.)

**GUI معادل:** VPN → IPsec Tunnels → Create New → Custom → Network (Remote Gateway، Interface) → Authentication (PSK، IKE Version 2) → Phase 1 Proposal (Encryption/Authentication/DH Group) → Phase 2 Selectors (Local/Remote Address) → Phase 2 Proposal، PFS → OK؛ سپس Network → Static Routes و Policy & Objects → Firewall Policy (دو جهت).

**مثال متوسط (تحلیل):** Phase 1 بالا ولی Phase 2 شکست می‌خورد. اولین فرضیه‌ها: Proposal Phase 2 ناهمسان، PFS/DH ناهمسان، Selector ناهمسان. شاهد: `diagnose debug application ike -1` پیام NO_PROPOSAL_CHOSEN یا TS_UNACCEPTABLE.

**مثال سخت:** Tunnel Up، Bytes out بالا، in صفر. فرضیه‌ها به ترتیب: (۱) Policy سمت مقابل ندارد، (۲) Route برگشت ندارد، (۳) NAT-T/فایروال میانی UDP 4500 را نمی‌دهد (ESP نمی‌رسد)، (۴) Selector نامطابق (ترافیک Drop قبل Encrypt). تفکیک با `diagnose vpn tunnel list` (شمارنده Encrypt/Decrypt)، Sniffer روی WAN (ESP/UDP 4500)، Debug Flow در سمت مقابل.

### ۶) طراحی و تصمیم‌گیری

| سؤال | تصمیم |
|---|---|
| IKEv1 یا IKEv2؟ | IKEv2 مگر سازگاری مانع شود |
| PSK یا Certificate؟ | Certificate برای مقیاس؛ PSK قوی برای Lab/کوچک |
| Route-based یا Policy-based؟ | Route-based (توصیه‌ی FortiOS) |
| Proposal | AES-GCM + SHA2 + DH ≥ 14 یا ECP؛ حذف الگوریتم ضعیف |
| PFS | روشن؛ هزینه‌ی CPU را بسنجید |
| DPD | on-idle/on-demand؛ زمان متوازن |
| MTU/MSS | از ابتدا تنظیم و با Capture تأیید |

### ۷) Verification

``` text
diagnose vpn ike gateway list
diagnose vpn tunnel list
get vpn ipsec tunnel summary
diagnose vpn ike log filter name TO-B
diagnose debug application ike -1
diagnose debug enable
diagnose debug disable
diagnose debug reset
diagnose sniffer packet wan1 "host 203.0.113.2 and (udp port 500 or udp port 4500 or proto 50)" 4 20 l
```

(`diagnose` فرمت دقیق `Unverified`.)

### ۸) Troubleshooting لایه‌ای (جدول تصمیم)

| لایه | آزمون | علامت | رفع |
|---|---|---|---|
| ۱) شبکه | ping/Sniffer روی UDP 500 | بسته‌ی IKE به Peer نمی‌رسد | Route/ACL/NAT |
| ۲) IKE_SA/Phase 1 | Debug IKE | NO_PROPOSAL_CHOSEN، AUTH_FAILED | Proposal، DH، PSK/گواهی، Peer ID |
| ۳) Child SA/Phase 2 | Debug IKE | TS_UNACCEPTABLE، NO_PROPOSAL | Selector، PFS/DH، Proposal |
| ۴) داده | `tunnel list` Encrypt/Decrypt | Out بالا In صفر | Policy مقابل، NAT-T، Route برگشت |
| ۵) Routing | `get router info routing-table details` | مسیر به Tunnel نیست | Static/OSPF/BGP |
| ۶) Policy | Debug Flow | Denied policy 0 | Policy دوطرفه |
| ۷) MTU | ping -f، Capture | بزرگ‌ها قفل | MTU/MSS |
| ۸) پایداری | Log، `ike gateway list` | قطع دوره‌ای | Lifetime/DPD/لینک |

### ۹) نکات امنیتی

- PSK قوی و منحصربه‌فرد برای هر Peer؛ در ریپو ذخیره نکنید.
- الگوریتم‌های منسوخ (DES، MD5، DH1/2) را غیرفعال کنید.
- IKEv1 Aggressive با PSK ضعیف خطرناک است.
- `peertype any` را فقط در Lab/نیاز؛ در تولید Peer ID مشخص.
- لاگ VPN را مانیتور کنید (تلاش‌های ناموفق).

### ۱۰) جمع‌بندی مفهومی

- IPsec = IKE (مدیریت کلید) + ESP (داده)؛ IKE_SA و Child SA.
- IKEv2 مدرن‌تر؛ PFS روشن؛ DH/Proposal دو سر یکی.
- Route-based = Selector باز + Route + Policy.
- NAT-T، DPD، Rekey و MTU علت اصلی ناپایداری‌اند.
- عیب‌یابی لایه‌ای: شبکه → IKE → Selector → Routing → Policy → MTU.

### ۱۱) تمرین و ارزیابی

**ت1.** (ساده) تفاوت Phase 1 و Phase 2 را بگویید. *(پاسخ: 18-0-ت1)*

**ت2.** (ساده) PFS چه کاری می‌کند؟ *(پاسخ: 18-0-ت2)*

**ت3.** (متوسط) چرا Route-based برای Hub-and-Spoke بهتر است؟ *(پاسخ: 18-0-ت3)*

**ت4.** (متوسط) NAT-T چه مشکلی را حل می‌کند و از چه پورتی استفاده می‌کند؟ *(پاسخ: 18-0-ت4)*

**ت5.** (سخت) Tunnel بالا ولی Bytes in صفر است. فرضیه‌ها را به ترتیب و شاهد هرکدام بنویسید. *(پاسخ: 18-0-ت5)*

**ت6.** (سخت، طراحی) Proposal پیشنهادی برای سازمان (Cipher، Hash، DH، PFS، Lifetime، DPD) را با دلیل بنویسید. *(پاسخ: 18-0-ت6)*

**ت7.** (سخت) Phase 2 با TS_UNACCEPTABLE شکست می‌خورد؛ Selectorهای دو طرف را چگونه تطبیق می‌دهید؟ *(پاسخ: 18-0-ت7)*

**م1.** DPD چیست؟ *(پاسخ: 18-0-م1)*

**Q1.** Quick quiz (English): Why is PFS recommended for IPsec? *(پاسخ: 18-0-Q1)*

### ۱۲) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| IKE | Internet Key Exchange | تبادل کلید |
| ESP | Encapsulating Security Payload | کپسوله‌سازی امن (IP 50) |
| SA | Security Association | قرارداد امنیتی |
| SPI | Security Parameter Index | شناسه‌ی SA |
| DH | Diffie-Hellman | تبادل کلید |
| PFS | Perfect Forward Secrecy | رازداری رو به جلو |
| DPD | Dead Peer Detection | تشخیص Peer مرده |
| TS | Traffic Selector | انتخاب‌گر ترافیک |
| NAT-T | NAT Traversal | عبور از NAT |
| AEAD | Authenticated Encryption with Associated Data | رمز و یکپارچگی توأم |

- *Phase 2 usually fails because of mismatched proposals or selectors.* ← Phase 2 معمولاً به‌خاطر ناهمسانی Proposal یا Selector شکست می‌خورد.
- *Enable PFS so that a key compromise does not expose past traffic.* ← PFS را فعال کنید تا افشای کلید ترافیک گذشته را باز نکند.

### ۱۳) منابع

- Fortinet Docs: [config vpn ipsec phase1-interface](https://docs.fortinet.com/document/fortigate/7.0.5/cli-reference/371620/config-vpn-ipsec-phase1-interface)، [phase2-interface](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/371620/config-vpn-ipsec-phase2-interface)، [Phase 1 configuration](https://docs.fortinet.com/document/fortigate/7.0.2/administration-guide/790613/phase-1-configuration).
- RFC 7296 — IKEv2؛ RFC 4303 — ESP؛ RFC 3947/3948 — NAT-T؛ RFC 3706 — DPD؛ RFC 8247 — Algorithm Requirements for IKEv2.

## درس 18-1 — مفهوم IPsec: IKE، SA و Proposal

**فصل 18 - روز 1 · پیش‌نیاز: فصل ۱۳ · ۶ ساعت**

### ۱) معرفی درس

IPsec ترافیک بین دو سایت را رمز می‌کند. اول مراحل و اصطلاحات را می‌فهمیم.

### ۲) پیش‌نیازها

فصل ۱۳

### ۳) توضیح مفهومی

- IKE Phase 1: ساخت کانال امن مدیریتی (IKE SA).
- Phase 2: ساخت SA ترافیک داده (IPsec SA).
- Proposal: الگوریتم رمز/Hash/DH باید دو طرف یکی باشد.
- IKEv2 جدیدتر و ساده‌تر.
- NAT-T: عبور از NAT (UDP 4500).

### ۴) مثال ساده

دو دفتر با Tunnel رمزشده.

### ۵) مثال سازمانی

سازمان: شعبه به مرکز با IPsec و مسیر پشتیبان.

### ۶) تصویر و توپولوژی

```text
Site-A LAN -> FGT-A ==IPsec== FGT-B -> Site-B LAN
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Monitor > IPsec Monitor.
2. VPN > IPsec Wizard (برای مقایسه).

#### روش خط فرمان (CLI)

```text
diagnose vpn ike gateway list
diagnose vpn tunnel list
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- فقط خواندن؛ ایمن.
- راستی‌آزمایی: وضعیت IKE/Tunnel.

### ۸) تست عملکرد

- مراحل IKE را روی کاغذ بکشید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Phase 1 بالا نمی‌شود |
| شواهد/دستور | Log IKE |
| علت | Proposal/PSK |
| رفع | تطبیق |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Phase 1 و 2؟ *(پاسخ: 18-1-ت1)*

**ت2.** NAT-T؟ *(پاسخ: 18-1-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Proposal یکی؟ *(پاسخ: 18-1-م1)*

**م2.** سناریو: فقط Phase 1 بالا؛ علت؟ *(پاسخ: 18-1-م2)*

**معیار تسلط:** ساخت Tunnel، Route/Policy، اثبات با Ping و Diagnose.

**اشتباهات رایج:** Proposal/Selector/Route.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| IPsec | Internet Protocol Security | رمزنگاری IP | VPN |
| IKE | Internet Key Exchange | تبادل کلید | IPsec |
| SA | Security Association | قرارداد امنیتی | IPsec |
| DH | Diffie-Hellman | تبادل کلید | IKE |

| English sentence | ترجمه |
|---|---|
| Phase 1 builds the control channel. | Phase 1 کانال کنترل را می‌سازد. |
| Both ends must agree on proposals. | دو سر باید روی Proposalها توافق کنند. |

#### کارت Lab — درس 18-1

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | نقشه‌ی IKE |
| 2 | پیش‌نیاز | فصل ۱۳ |
| 3 | توپولوژی | FGT-A + FGT-B |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | — |
| 8 | صورت مسئله | نمودار IKE |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | — |
| 11 | سناریوی خرابی | Phase 1 بالا نمی‌شود |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | نمودار |
| 14 | معیار پذیرش | با شواهد |
| 15 | مستندات نهایی | `03-ops/ike-map.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-18-2"></a>

## درس 18-2 — ساخت Tunnel بین دو FortiGate (CLI و GUI)

**فصل 18 - روز 2 · پیش‌نیاز: درس ۱۸-۰ · ۶ ساعت**

### ۱) معرفی درس

حالا Tunnel واقعی: Phase 1، Phase 2، Route، Policy.

### ۲) پیش‌نیازها

درس ۱۸-۰

### ۳) توضیح مفهومی

- Phase 1: interface، remote-gw، PSK، proposal، IKEv2.
- Phase 2: selector (src/dst)، proposal.
- Static Route به Tunnel Interface.
- Policy دوطرفه (LAN->Tunnel، Tunnel->LAN).
- PSK نمونه؛ رمز واقعی در ریپو نیست.

### ۴) مثال ساده

دو دفتر با Tunnel رمزشده.

### ۵) مثال سازمانی

سازمان: شعبه به مرکز با IPsec و مسیر پشتیبان.

### ۶) تصویر و توپولوژی

```text
Site-A LAN -> FGT-A ==IPsec== FGT-B -> Site-B LAN
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. VPN > IPsec Tunnels > Create New > Custom: Name، Remote Gateway Static IP، Interface، PSK.
2. Phase 1 Proposal: AES256-SHA256؛ IKE v2.
3. Phase 2: Local/Remote Address Subnet.
4. Network > Static Routes: مقصد LAN دیگر، Interface = Tunnel.
5. Policy & Objects: دو Policy.

#### روش خط فرمان (CLI)

```text
config vpn ipsec phase1-interface
    edit "TO-SITE-B"
        set interface "port1"
        set ike-version 2
        set remote-gw 203.0.113.2
        set psksecret <PSK-LAB>
        set proposal aes256-sha256
    next
end
config vpn ipsec phase2-interface
    edit "TO-SITE-B-P2"
        set phase1name "TO-SITE-B"
        set proposal aes256-sha256
        set src-subnet 192.168.10.0 255.255.255.0
        set dst-subnet 192.168.20.0 255.255.255.0
    next
end
config router static
    edit 50
        set dst 192.168.20.0 255.255.255.0
        set device "TO-SITE-B"
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Proposal دو طرف یکی.
- Selector باید آینه‌ی هم باشد.
- Policy جدا لازم است.
- بازگشت: حذف phase2 سپس phase1.

### ۸) تست عملکرد

- Tunnel در Monitor بالا.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Tunnel بالا ولی ping نه |
| شواهد/دستور | `diagnose sniffer`؛ Route/Policy |
| علت | Route/Policy |
| رفع | افزودن |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** چرا Static Route لازم؟ *(پاسخ: 18-2-ت1)*

**ت2.** Selector؟ *(پاسخ: 18-2-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا دو Policy؟ *(پاسخ: 18-2-م1)*

**م2.** سناریو: فقط یک سو کار می‌کند؛ علت؟ *(پاسخ: 18-2-م2)*

**معیار تسلط:** ساخت Tunnel، Route/Policy، اثبات با Ping و Diagnose.

**اشتباهات رایج:** Proposal/Selector/Route.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| Phase1 | IKE Phase 1 | کانال کنترل | VPN |
| Selector | Phase 2 selector | ترافیک مجاز | VPN |

| English sentence | ترجمه |
|---|---|
| Create a policy for each direction. | برای هر جهت یک Policy بسازید. |
| Selectors must mirror each other. | Selectorها باید آینه‌ی هم باشند. |

#### کارت Lab — درس 18-2

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | Tunnel S2S |
| 2 | پیش‌نیاز | درس ۱۸-۰ |
| 3 | توپولوژی | FGT-A + FGT-B |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | 203.0.113.1/2 |
| 7 | وضعیت اولیه | Baseline |
| 8 | صورت مسئله | Tunnel |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping 192.168.20.x |
| 11 | سناریوی خرابی | Tunnel بالا ولی ping نه |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Reply |
| 14 | معیار پذیرش | Monitor Up |
| 15 | مستندات نهایی | `03-ops/s2s-a-b.md` |
| 16 | Cleanup و بازگردانی | حذف phase2/1 |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-18-3"></a>

## درس 18-3 — عیب‌یابی IPsec: Phase 1/2 و Debug

**فصل 18 - روز 3 · پیش‌نیاز: درس ۱۸-۱ · ۶ ساعت**

### ۱) معرفی درس

با ابزار تشخیص علت را پیدا کنید.

### ۲) پیش‌نیازها

درس ۱۸-۱

### ۳) توضیح مفهومی

- `diagnose vpn ike log filter`.
- `diagnose debug application ike -1`.
- `diagnose vpn tunnel list`: Bytes in/out.
- علائم: Phase 1 down، Phase 2 down، Up بدون ترافیک.
- Log رویدادهای VPN.

### ۴) مثال ساده

دو دفتر با Tunnel رمزشده.

### ۵) مثال سازمانی

سازمان: شعبه به مرکز با IPsec و مسیر پشتیبان.

### ۶) تصویر و توپولوژی

```text
Site-A LAN -> FGT-A ==IPsec== FGT-B -> Site-B LAN
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Log & Report > Events > VPN.
2. Monitor > IPsec Monitor.

#### روش خط فرمان (CLI)

```text
diagnose vpn ike log filter name TO-SITE-B
diagnose debug application ike -1
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- Debug را حتماً Disable کنید.
- `Unverified` روی Image.

### ۸) تست عملکرد

- یک عیب Proposal بسازید و Debug بخوانید.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | NO_PROPOSAL_CHOSEN |
| شواهد/دستور | Debug IKE |
| علت | Proposal ناهمسان |
| رفع | تطبیق Proposal |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** Debug IKE؟ *(پاسخ: 18-3-ت1)*

**ت2.** پایان Debug؟ *(پاسخ: 18-3-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا Bytes in/out؟ *(پاسخ: 18-3-م1)*

**م2.** سناریو: Bytes out بالا و in صفر؛ علت؟ *(پاسخ: 18-3-م2)*

**معیار تسلط:** ساخت Tunnel، Route/Policy، اثبات با Ping و Diagnose.

**اشتباهات رایج:** Proposal/Selector/Route.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| NO_PROPOSAL_CHOSEN | No proposal chosen | Proposal ناهمسان | IKE |

| English sentence | ترجمه |
|---|---|
| Run debug only briefly. | Debug را فقط کوتاه اجرا کنید. |

#### کارت Lab — درس 18-3

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | عیب Proposal |
| 2 | پیش‌نیاز | درس ۱۸-۱ |
| 3 | توپولوژی | FGT-A + FGT-B |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Tunnel |
| 8 | صورت مسئله | عیب Proposal |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | debug |
| 11 | سناریوی خرابی | NO_PROPOSAL_CHOSEN |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | RCA |
| 14 | معیار پذیرش | رفع |
| 15 | مستندات نهایی | `03-ops/rca-ike.md` |
| 16 | Cleanup و بازگردانی | Disable debug |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-18-4"></a>

## درس 18-4 — MTU/MSS و Fragmentation در Tunnel

**فصل 18 - روز 4 · پیش‌نیاز: درس ۱۸-۲ · ۶ ساعت**

### ۱) معرفی درس

Tunnel سربار اضافه می‌کند؛ MTU نادرست باعث «کار می‌کند ولی بزرگ‌ها نه» می‌شود.

### ۲) پیش‌نیازها

درس ۱۸-۲

### ۳) توضیح مفهومی

- سربار IPsec ≈ ۵۰–۷۰ بایت (تقریبی).
- PMTUD و DF-bit.
- کاهش MSS: `tcp-mss-sender`/policy.
- ping با اندازه‌ی بزرگ و DF.
- علامت: وب باز می‌شود ولی دانلود بزرگ قفل.

### ۴) مثال ساده

دو دفتر با Tunnel رمزشده.

### ۵) مثال سازمانی

سازمان: شعبه به مرکز با IPsec و مسیر پشتیبان.

### ۶) تصویر و توپولوژی

```text
Site-A LAN -> FGT-A ==IPsec== FGT-B -> Site-B LAN
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. Network > Interfaces > TO-SITE-B > MTU.
2. Policy: CLI فقط برای MSS.

#### روش خط فرمان (CLI)

```text
config system interface
    edit "TO-SITE-B"
        set mtu-override enable
        set mtu 1400
    next
end
config firewall policy
    edit 20
        set tcp-mss-sender 1360
        set tcp-mss-receiver 1360
    next
end
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `mtu 1400` نمونه.
- `Unverified` روی Image.
- راستی‌آزمایی: ping -f -l 1372.
- بازگشت: غیرفعال‌کردن override.

### ۸) تست عملکرد

- ping با اندازه‌های مختلف و ثبت نتیجه.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | دانلود بزرگ قفل |
| شواهد/دستور | ping -f بزرگ شکست |
| علت | MTU |
| رفع | کاهش MTU/MSS |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** MSS؟ *(پاسخ: 18-4-ت1)*

**ت2.** DF؟ *(پاسخ: 18-4-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا MSS کمک می‌کند؟ *(پاسخ: 18-4-م1)*

**م2.** سناریو: ping کوچک OK بزرگ نه؛ علت؟ *(پاسخ: 18-4-م2)*

**معیار تسلط:** ساخت Tunnel، Route/Policy، اثبات با Ping و Diagnose.

**اشتباهات رایج:** Proposal/Selector/Route.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| MTU | Maximum Transmission Unit | حداکثر اندازه‌ی بسته | Tunnel |
| MSS | Maximum Segment Size | حداکثر قطعه‌ی TCP | Tunnel |
| PMTUD | Path MTU Discovery | کشف MTU مسیر | Tunnel |

| English sentence | ترجمه |
|---|---|
| Lower the MSS to avoid fragmentation. | MSS را برای جلوگیری از Fragmentation کاهش دهید. |

#### کارت Lab — درس 18-4

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | MTU Tunnel |
| 2 | پیش‌نیاز | درس ۱۸-۲ |
| 3 | توپولوژی | FGT-A + FGT-B |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Tunnel |
| 8 | صورت مسئله | MTU آزمایش |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping -f |
| 11 | سناریوی خرابی | دانلود بزرگ قفل |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | جدول اندازه |
| 14 | معیار پذیرش | نتیجه ثبت |
| 15 | مستندات نهایی | `03-ops/mtu.md` |
| 16 | Cleanup و بازگردانی | بازگشت MTU |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-18-5"></a>

## درس 18-5 — Tunnel با Cisco CSR و Dead Peer Detection

**فصل 18 - روز 5 · پیش‌نیاز: درس ۱۸-۳ · ۶ ساعت**

### ۱) معرفی درس

اتصال FGT به CSR1000v (IOS-XE). مفاهیم Interoperability.

### ۲) پیش‌نیازها

درس ۱۸-۳

### ۳) توضیح مفهومی

- CSR: crypto ikev2/ipsec profile.
- هماهنگی Proposal/DH/Lifetime.
- DPD برای تشخیص قطع.
- Lifetime تفاوت دو سر.
- تأیید با `show crypto ipsec sa` (CSR).

### ۴) مثال ساده

دو دفتر با Tunnel رمزشده.

### ۵) مثال سازمانی

سازمان: شعبه به مرکز با IPsec و مسیر پشتیبان.

### ۶) تصویر و توپولوژی

```text
Site-A LAN -> FGT-A ==IPsec== FGT-B -> Site-B LAN
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. FortiGate: VPN > IPsec Tunnels با Remote GW = CSR.

#### روش خط فرمان (CLI)

```text
! CSR (IOS-XE) example, lab only
crypto ikev2 keyring KR
 peer FGT
  address 203.0.113.1
  pre-shared-key <PSK-LAB>
crypto ikev2 profile PROF
 match identity remote address 203.0.113.1 255.255.255.255
 authentication local pre-share
 authentication remote pre-share
 keyring local KR
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- CSR آزمایش‌نشده؛ `Unverified`.
- راستی‌آزمایی: show crypto ikev2 sa.
- بازگشت: حذف profile.

### ۸) تست عملکرد

- Tunnel FGT-CSR بالا (اگر قابل‌انجام).

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Phase 2 mismatch با CSR |
| شواهد/دستور | show crypto ipsec sa |
| علت | Selector/Transform |
| رفع | تطبیق |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** DPD؟ *(پاسخ: 18-5-ت1)*

**ت2.** چرا Lifetime مهم؟ *(پاسخ: 18-5-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا CSR؟ *(پاسخ: 18-5-م1)*

**م2.** سناریو: Tunnel هر ساعت قطع؛ علت؟ *(پاسخ: 18-5-م2)*

**معیار تسلط:** ساخت Tunnel، Route/Policy، اثبات با Ping و Diagnose.

**اشتباهات رایج:** Proposal/Selector/Route.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| DPD | Dead Peer Detection | تشخیص همتای مرده | IPsec |
| CSR | CSR1000v | روتر مجازی Cisco | Lab |

| English sentence | ترجمه |
|---|---|
| Match lifetimes on both vendors. | Lifetime را روی هر دو سازنده یکسان کنید. |

#### کارت Lab — درس 18-5

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | FGT-CSR |
| 2 | پیش‌نیاز | درس ۱۸-۳ |
| 3 | توپولوژی | FGT + CSR |
| 4 | تجهیزات | FGT + CSR |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Tunnel |
| 8 | صورت مسئله | Interop |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | show |
| 11 | سناریوی خرابی | Phase 2 mismatch با CSR |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | Up |
| 14 | معیار پذیرش | ثبت |
| 15 | مستندات نهایی | `03-ops/fgt-csr.md` |
| 16 | Cleanup و بازگردانی | حذف |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="l-18-6"></a>

## درس 18-6 — Gate G7 و آزمون فصل

**فصل 18 - روز 6 · پیش‌نیاز: درس ۱۸-۴ · ۶ ساعت**

### ۱) معرفی درس

ارزیابی: Tunnel، Route/Policy، MTU، عیب Phase 2.

### ۲) پیش‌نیازها

درس ۱۸-۴

### ۳) توضیح مفهومی

- G7: Tunnel بالا و ترافیک دوطرفه.
- سناریوی عیب Phase 2 mismatch حل شود.
- Backup پیکربندی.
- RCA یک صفحه.
- آزمون ۵ مورد.

### ۴) مثال ساده

دو دفتر با Tunnel رمزشده.

### ۵) مثال سازمانی

سازمان: شعبه به مرکز با IPsec و مسیر پشتیبان.

### ۶) تصویر و توپولوژی

```text
Site-A LAN -> FGT-A ==IPsec== FGT-B -> Site-B LAN
```

### ۷) پیکربندی (GUI و CLI)

> نسخه‌ی هدف: FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`). دستورها/منوها از مستند عمومی FortiOS 7.0 و دانش مؤلف هستند و **روی Image شما هنوز آزمایش نشده‌اند**؛ در بوت اول مقایسه کنید.

#### روش گرافیکی (GUI)

1. System > Config > Backup.

#### روش خط فرمان (CLI)

```text
execute backup config tftp fgt-g7.conf 192.168.90.10
```

**توضیح دستورها (چه / چرا / خروجی / راستی‌آزمایی / بازگشت):**

- `execute backup` آزمایش‌نشده؛ مسیر TFTP نمونه.

### ۸) تست عملکرد

- اجرای G7 و ثبت شاهد.

### ۹) عیب‌یابی

| بخش | شرح |
|---|---|
| Symptom | Phase 2 mismatch |
| شواهد/دستور | Debug |
| علت | Selector |
| رفع | اصلاح |

### ۱۰) تمرین مستقل

> پاسخ‌ها در بخش «پاسخ‌های فصل» انتهای فصل است؛ اول خودتان حل کنید.

**ت1.** G7 چیست؟ *(پاسخ: 18-6-ت1)*

**ت2.** Backup؟ *(پاسخ: 18-6-ت2)*

### ۱۱) مرور و ارزیابی

**م1.** چرا RCA؟ *(پاسخ: 18-6-م1)*

**م2.** سناریو: Selector یکطرفه؛ پیامد؟ *(پاسخ: 18-6-م2)*

**معیار تسلط:** ساخت Tunnel، Route/Policy، اثبات با Ping و Diagnose.

**اشتباهات رایج:** Proposal/Selector/Route.

### ۱۲) واژگان و English Corner

| واژه | شکل کامل | معنی | کاربرد واقعی |
|---|---|---|---|
| RCA | Root Cause Analysis | تحلیل ریشه | Ops |

| English sentence | ترجمه |
|---|---|
| Document the root cause and the fix. | علت ریشه‌ای و راه‌حل را مستند کنید. |

#### کارت Lab — درس 18-6

| # | فیلد | محتوا |
|---|---|---|
| 1 | عنوان و هدف | آزمون G7 |
| 2 | پیش‌نیاز | درس ۱۸-۴ |
| 3 | توپولوژی | FGT-A + FGT-B |
| 4 | تجهیزات | FGT |
| 5 | نسخه نرم‌افزار | FortiOS 7.0.3 (اسمی؛ از نام Image؛ بوت‌نشده؛ تأیید با `get system status`) |
| 6 | IP Plan | — |
| 7 | وضعیت اولیه | Tunnel |
| 8 | صورت مسئله | G7 |
| 9 | مراحل هدایت‌شده | بخش‌های ۷ و ۸ همین درس (گام‌به‌گام) |
| 10 | تست عملکرد | ping |
| 11 | سناریوی خرابی | Phase 2 mismatch |
| 12 | روش عیب‌یابی | بخش ۹ همین درس (لایه‌ای/با شواهد) |
| 13 | نتیجه‌ی مورد انتظار | RCA |
| 14 | معیار پذیرش | ≥ ۴ از ۵ |
| 15 | مستندات نهایی | `03-ops/g7.md` |
| 16 | Cleanup و بازگردانی | — |

> **وضعیت راستی‌آزمایی (خارج از ۱۶ فیلد):** **اجرا نشده (فقط طراحی).** Image FortiGate هنوز بوت نشده؛ دستورها/منوها آزمایش‌نشده‌اند.

---

<a id="ans-18"></a>

## پاسخ‌های فصل 18

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).

**18-1-ت1** — Phase 1 و 2؟

IKE SA و IPsec SA.

**18-1-ت2** — NAT-T؟

UDP 4500.

**18-1-م1** — چرا Proposal یکی؟

وگرنه مذاکره شکست.

**18-1-م2** — سناریو: فقط Phase 1 بالا؛ علت؟

Selector/Proposal Phase 2.

**18-2-ت1** — چرا Static Route لازم؟

تا ترافیک وارد Tunnel شود.

**18-2-ت2** — Selector؟

مشخص‌کننده‌ی ترافیک مجاز.

**18-2-م1** — چرا دو Policy؟

دو جهت.

**18-2-م2** — سناریو: فقط یک سو کار می‌کند؛ علت؟

Policy جهت مقابل.

**18-3-ت1** — Debug IKE؟

application ike -1.

**18-3-ت2** — پایان Debug؟

disable/reset.

**18-3-م1** — چرا Bytes in/out؟

وجود/نبود ترافیک.

**18-3-م2** — سناریو: Bytes out بالا و in صفر؛ علت؟

سمت مقابل Policy/Route ندارد.

**18-4-ت1** — MSS؟

حداکثر قطعه‌ی TCP.

**18-4-ت2** — DF؟

Don't Fragment.

**18-4-م1** — چرا MSS کمک می‌کند؟

Fragmentation را نمی‌خواهد.

**18-4-م2** — سناریو: ping کوچک OK بزرگ نه؛ علت؟

MTU.

**18-5-ت1** — DPD؟

Dead Peer Detection.

**18-5-ت2** — چرا Lifetime مهم؟

عدم تطابق قطع دوره‌ای.

**18-5-م1** — چرا CSR؟

Interop واقعی.

**18-5-م2** — سناریو: Tunnel هر ساعت قطع؛ علت؟

Lifetime ناهمسان.

**18-6-ت1** — G7 چیست؟

Tunnel+ترافیک+عیب.

**18-6-ت2** — Backup؟

execute backup.

**18-6-م1** — چرا RCA؟

یادگیری.

**18-6-م2** — سناریو: Selector یکطرفه؛ پیامد؟

فقط یک جهت.


---

<a id="end6"></a>


### پاسخ‌های درس افزوده‌ی 18-0 (فصل 18)

**18-0-ت1** — Phase 1 کانال کنترل امن (IKE SA)؛ Phase 2 SA داده (Child SA) و Selector.

**18-0-ت2** — با هر Rekey کلید تازه با DH جدید می‌سازد تا افشای کلید قدیمی ترافیک گذشته را باز نکند.

**18-0-ت3** — Selector باز + Routing + Policy؛ Routing پویا و مقیاس‌پذیری راحت.

**18-0-ت4** — عبور از NAT با کپسوله‌کردن ESP در UDP؛ پورت UDP 4500.

**18-0-ت5** — ۱) Policy سمت مقابل؛ ۲) Route برگشت؛ ۳) NAT-T/UDP 4500؛ ۴) Selector. شاهد: tunnel list، Sniffer، Debug Flow سمت مقابل.

**18-0-ت6** — AES-256-GCM، SHA-256، DH 20 یا ≥ 14، PFS روشن، Lifetime حدود 8 تا 24 ساعت، DPD on-idle با retry 3؛ دلیل: امنیت و سازگاری.

**18-0-ت7** — Selectorها آینه‌ی هم باشند؛ در Route-based از 0.0.0.0/0 استفاده یا Subnetهای دقیق هم‌سان؛ بررسی Debug IKE.

**18-0-م1** — پیام دوره‌ای برای تشخیص مرگ Peer و پاک‌کردن SA.

**18-0-Q1** — Because it gives forward secrecy: compromise of a long-term key does not expose past sessions.

# پایان بخش ۶ (فصل‌های ۱۶ تا ۱۸)

## ۱) خلاصه‌ی مهارت‌های کسب‌شده
- Security Profile و SSL Inspection؛ LDAP/RADIUS/FSSO/Captive؛ IPsec S2S با FGT و CSR، MTU/MSS و عیب‌یابی.

## ۲) آزمون پایان سه فصل
**س1** — کدام قابلیت‌های UTM بدون لایسنس کار می‌کنند؟

**س2** — چرا Deep Inspection نیاز به CA دارد؟

**س3** — Static URL در برابر Category؟

**س4** — cnid در LDAP؟

**س5** — پورت RADIUS؟

**س6** — FSSO چه می‌کند؟

**س7** — Phase 1 و 2 چیست؟

**س8** — چرا Tunnel بالا ولی ترافیک نه؟

**س9** — دستور Debug IKE؟

**س10** — MSS چیست؟

**س11** — NAT-T پورت؟

**س12** — چرا Debug را Disable می‌کنیم؟


## ۳) پاسخ آزمون
- **س1:** Static URL، File Filter، DoS Policy، Custom IPS.
- **س2:** تا مرورگر گواهی فایروال را بپذیرد.
- **س3:** Static محلی؛ Category نیاز Rating.
- **س4:** ویژگی ورود (sAMAccountName).
- **س5:** UDP 1812/1813.
- **س6:** هویت ورود ویندوز را به FGT می‌دهد.
- **س7:** IKE SA و IPsec SA.
- **س8:** Route/Policy/Selector.
- **س9:** diagnose debug application ike -1.
- **س10:** حداکثر قطعه‌ی TCP.
- **س11:** UDP 4500.
- **س12:** بار CPU و Log.

## ۴) معیارهای تسلط
| مهارت | سطح | شاهد |
|---|---|---|
| UTM | L2 | آزمون فصل ۱۶ |
| Authentication | L3 | آزمون فصل ۱۷ |
| IPsec S2S | L3 | G7 |

## ۵) مشکلات و موارد باقی‌مانده (صریح)
1. همه‌ی Labها اجرا نشده. 2. UTM به لایسنس وابسته. 3. سینتکس IPsec/CSR/MSS در 7.0.3 `Unverified`. 4. Windows DC/NPS لازم است.

## ۶) پیش‌نیازهای بخش بعد
Tunnel S2S پایدار و Backup؛ آشنایی با OSPF/BGP؛ برنامه‌ی Dual-ISP.

## ۷) فهرست Lab و منابع مرتبط
کارت‌های Lab، `03-ops/*` (خروجی دانشجو)

## ۸) وضعیت دوره
| مورد | مقدار |
|---|---|
| آخرین فصل تکمیل‌شده | ۱۸ |
| آخرین درس تکمیل‌شده | ۱۸-۶ |
| مهارت‌های تأییدشده | **هیچ‌کدام هنوز آزمون عملی واقعی نشده‌اند** (ممیزی/اجرای شما لازم است) |
| موضوعات نیازمند مرور | طبق «معیارهای تسلط» |
| فصل بعدی | ۱۹ |
| فایل تولیدشده | `course/Course_Part_06_Chapters_16-18.md` |
