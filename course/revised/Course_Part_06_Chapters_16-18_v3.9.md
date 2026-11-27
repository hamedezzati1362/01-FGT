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

> **نسخه‌ی اصلاح‌شده (v3.9):** نسخه‌ی توسعه‌یافته‌ی فایل اصلی؛ درس‌های افزوده: ۱۶-۰، ۱۶-۷، ۱۸-۰ (دسته C). فایل اصلی در `course/` حفظ شده است. پاسخ‌های درس‌های افزوده در «پاسخ‌های فصل» همان فصل است.

# فصل 16 — UTM: آنتی‌ویروس، IPS، Application Control، Web Filter و SSL Inspection

**مدت:** ۳۶ ساعت | **پیش‌نیاز:** فصل ۱۳، ۱۴.
**اهداف:** Security Profile و Profile Group؛ AV؛ Web Filter (Static URL به‌جای Category)؛ IPS و DoS؛ Application Control؛ SSL/SSH Inspection؛ اثر Performance و عیب‌یابی.
**هشدار لایسنس (مهم):** طبق مستند Fortinet: AV و IPS به لایسنس **FortiGuard AV/IPS** برای به‌روزرسانی Signature؛ Web Filter و DNS Filter (Category) به **Web/DNS Security**؛ و Signature **Application Control** جزو سرویس‌های پایه‌ی قرارداد FortiCare است (لایسنس امنیتی جدا نمی‌خواهد ولی FortiCare معتبر لازم است). اگر لایسنس منقضی شود FortiGate همچنان فایروال می‌ماند: AV/IPS با Signature قدیمی اسکن می‌کنند و فقط به‌روزرسانی قطع می‌شود، ولی Category در Web/DNS Filter کار نمی‌کند. در Lab ایزوله و Evaluation این وابستگی `Needs-License` و وضعیتش `Unverified` است. هر درس بخش «بدون لایسنس چه می‌توان کرد» دارد (Static URL، Custom IPS، DoS، Port-based). **همه‌ی دستورها آزمایش‌نشده روی Image.**
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

### تعمیق: انتخاب Flow یا Proxy با معیار واقعی

**سناریو.** شعبه با ۱ Gbps و نیاز به Web Filter با Category + Antivirus.

| نیاز | Flow | Proxy |
|---|---|---|
| حداکثر سرعت | بهتر | کندتر |
| قابلیت‌های عمیق (مثلاً بعضی اسکن‌ها) | محدودتر | کامل‌تر |
| NPU Offload | امکان | معمولاً خیر |

قانون عملی: پیش‌فرض Flow؛ Proxy فقط اگر قابلیت لازم آن را بخواهد (طبق جدول قابلیت‌های مستند Fortinet برای نسخه).

**زنجیره‌ی اعتماد TLS:** مرورگر باید CA فایروال را بپذیرد؛ بدون نصب CA هشدار «Not Secure». استثنا برای بانکداری/پزشکی (Exemption) از نظر حریم خصوصی.

**پرسش‌های مصاحبه**
1. *چرا SSL Inspection بدون CA خطا می‌دهد؟* گواهی ساختگی اعتماد ندارد.
2. *Certificate Pinning؟* برنامه گواهی را قفل می‌کند؛ Exemption لازم.
3. *هزینه CPU؟* رمزگشایی/رمزگذاری دوباره.

### تکمیل عمیق: Flow در برابر Proxy و TLS Inspection — انتخاب درست

#### چرا باید یاد بگیریم؟

فایروال نسل جدید فقط «پورت» را نمی‌بیند؛ محتوا را هم بازرسی می‌کند. ولی بازرسی هزینه دارد و دو روش دارد که هر کدام جای خود را دارند. انتخاب غلط یا سرعت را می‌کشد یا قابلیت لازم را از دست می‌دهد.

#### توضیح ساده

- **Flow-based**: بسته‌ها در حین عبور بازرسی می‌شوند، بدون ذخیره‌ی کامل فایل. سریع‌تر؛ قابلیت NPU Offload بیشتر.
- **Proxy-based**: فایروال فایل/ارتباط را کامل دریافت و سپس تصمیم می‌گیرد. کندتر ولی بازرسی عمیق‌تر برای بعضی قابلیت‌ها.

جدول قابلیت‌های هر حالت در مستند Fortinet نسخه آمده؛ قاعده‌ی عملی: پیش‌فرض Flow، و Proxy فقط وقتی قابلیت مورد نیاز آن را بخواهد.

#### مثال ساده — انتخاب

شعبه 1 Gbps با Web Filter Category + Antivirus: Flow-based معمولاً کافی و سریع است.

#### مثال متوسط — SSL/TLS Inspection

بیش از ۹۰٪ ترافیک رمز است؛ بدون Inspection، AV/IPS/Web Filter عمیق نمی‌بینند. فایروال نقش «مرد میانی مجاز» دارد: اتصال کلاینت را با گواهی ساختگی (امضاشده با CA سازمان) خاتمه می‌دهد و اتصال دوم را به سرور می‌سازد.

``` text
Client <-TLS(cert signed by Corp CA)-> FortiGate <-TLS(real server cert)-> Server
```

کلاینت باید CA سازمان را بپذیرد.

#### مثال سخت — Certificate Pinning

برنامه‌هایی که گواهی را «قفل» می‌کنند (بانک، برخی Appها) با Inspection شکست می‌خورند. راه: Exemption برای آن دسته/Domain؛ و مستندسازی دلیل. همچنین دسته‌های حساس حریم (سلامت، مالی) را از Inspection مستثنی کنید.

#### هزینه

رمزگشایی/رمزنگاری دوباره CPU می‌خورد؛ ظرفیت را با Baseline اندازه بگیرید (درس 16-6).

#### Lab

یک Policy با Inspection را تنها در Lab بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| هشدار گواهی | CA نصب نیست | توزیع |
| برنامه شکست | Pinning | Exemption |
| CPU بالا | Inspection | مقیاس/Exemption |

#### پرسش‌ها با پاسخ

**۱. Flow یا Proxy؟** پیش‌فرض Flow.
**۲. چرا CA؟** اعتماد.
**۳. Pinning؟** گواهی قفل‌شده.

#### English Corner

- *Deep inspection requires clients to trust the inspection CA.*
- Q: Why are some categories exempted from SSL inspection?

## درس 16-1 — نقشه‌ی UTM: Security Profileها، لایسنس FortiGuard و ماتریس قابلیت

**فصل 16 · بازنویسی عمیق · پیش‌نیاز: ۱۶-۰، ۱۲-۰، ۱۳-۱ · ≈ 6 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. فهرست Security Profileها و محل اتصال آن‌ها به Policy را بگوید.
2. برای هر قابلیت وابستگی لایسنس را مشخص کند (Needs-License/بدون لایسنس).
3. یک «ماتریس لایسنس و قابلیت» برای Lab خود تکمیل کند.
4. نتیجه‌ی بررسی را با شواهد (وضعیت FortiGuard، Log) ثبت و از ادعای بدون شاهد پرهیز کند.
5. مسیر پردازش UTM را در Packet Flow (پس از Policy) جایابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

Security Profile مجموعه‌ی تنظیمات بازرسی لایه‌ی ۷ است که **داخل Firewall Policy** فعال می‌شود: Antivirus، Web Filter، DNS Filter، Application Control، IPS، File Filter، SSL/SSH Inspection (و DLP/Email Filter بسته به نسخه). Policy می‌گوید «اجازه‌ی عبور هست»؛ Profile می‌گوید «محتوای مجاز را هم بررسی کن».

مشکل رایج: تیم‌ها فرض می‌کنند چون Profile ساخته‌اند، حفاظت فعال است. حفاظت فقط وقتی واقعی است که (۱) Profile به Policy درست وصل باشد، (۲) سرویس مربوط لایسنس/DB داشته باشد، (۳) ترافیک قابل‌دیدن باشد (TLS)، (۴) Log اثباتش کند.

### ۳) توضیح عمیق فنی

#### ۱) جای UTM در Packet Flow

``` text
Ingress -> RPF -> Session -> DNAT -> Route -> Policy match -> [Security profiles] -> SNAT -> Egress
```

UTM فقط برای ترافیکی اجرا می‌شود که **Policy مطابق، `accept` کرده** باشد؛ ترافیک Denied اصلاً به Profile نمی‌رسد.

#### ۲) ماتریس قابلیت و لایسنس

| قابلیت | کار اصلی | نیاز لایسنس FortiGuard | بدون لایسنس چه می‌شود؟ |
|---|---|---|---|
| Antivirus | Signature بدافزار | بله (DB) | File Filter، بلاک نوع فایل |
| Web Filter | Category/URL | Category: بله | Static URL Filter |
| DNS Filter | بلاک دامنه‌ی مخرب | Category: بله | Static domain |
| Application Control | شناخت برنامه | DB برنامه: بله | Port/Service-based |
| IPS | Signature حمله | Signature: بله | Custom Signature، DoS Policy |
| File Filter | نوع فایل | خیر | کار می‌کند |
| SSL/SSH Inspection | رمزگشایی TLS | خیر (CA لازم) | کار می‌کند |

(ستون لایسنس بر اساس مدل FortiGuard است؛ جزئیات هر مدل/نسخه را در مستند 7.0 و Contract بررسی کنید.)

#### ۳) راستی‌آزمایی لایسنس

وضعیت سرویس‌ها از GUI (System → FortiGuard) و CLI دیده می‌شود. در Lab ایزوله به‌روزرسانی ممکن نیست؛ پس «Profile ساخته‌شده» ≠ «محافظت فعال».

#### ۴) سه سطح شاهد

1. **پیکربندی:** Profile در Policy (`show firewall policy`).
2. **وضعیت سرویس:** FortiGuard Valid/Expired.
3. **رفتار:** تست با فایل/سایت/پورت و Log.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| کدام Profile روی کدام Policy؟ | Users→Internet: همه؛ Servers: IPS؛ Guest: Web/DNS |
| Inspection Mode | Flow برای عموم؛ Proxy برای نیاز خاص (۱۶-۰) |
| حالت لایسنس‌نداشتن | لایه‌ی جایگزین بدون لایسنس + ثبت صریح محدودیت |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Policy 10 (Users→Internet) فقط Web Filter دارد. با `show firewall policy 10` اثبات می‌کنید `webfilter-profile` وصل است؛ بدون این شاهد، «Web Filter فعال است» ادعای تأییدنشده است.

**متوسط:** AV Profile ساخته و به Policy وصل است ولی EICAR رد می‌شود. بررسی: FortiGuard AV DB تاریخ دارد؟ (نه در Lab ایزوله) ← علت: نبود DB. ثبت: «Needs-License؛ آزمایش ناموفق».

**سخت:** سازمان می‌خواهد «هیچ بدافزاری وارد نشود». تحلیل: AV Signature به‌تنهایی کافی نیست (Zero-day، رمزدار، TLS بدون Deep). طرح لایه‌ای: File Filter + SSL Inspection + IPS + Sandbox (لایسنس) + EDR/Patch؛ و معیار «کشف/پیشگیری» را با FP/FN مستند کنید.

### ۶) پیاده‌سازی از مسیر GUI

1. Security Profiles → هر Profile: وضعیت و گزینه‌ها.
2. Policy & Objects → Firewall Policy → Security Profiles: فعال‌سازی و انتخاب.
3. System → FortiGuard: وضعیت لایسنس/DB.
4. Log & Report → Security Events.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get system fortiguard-service status
show firewall policy 10
show antivirus profile
show webfilter profile
```

### ۸) Verification (اثبات صحت)

- ماتریس لایسنس را با خروجی واقعی پر کنید.
- برای هر قابلیت یک آزمون و Log ثبت کنید.
- قابلیت بدون شاهد = «اجرا نشده».

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Profile اثر ندارد | Log بدون رویداد UTM | Profile به Policy وصل نیست یا Policy دیگری Match شده |
| Category کار نمی‌کند | Log: rating error | لایسنس/ارتباط FortiGuard |
| HTTPS دیده نمی‌شود | فقط SNI در Log | SSL Inspection فعال نیست |

### ۱۰) نکات امنیتی

- Profile پیش‌فرض را بدون بازبینی روی همه‌چیز فعال نکنید.
- UTM جایگزین Patch و Segmentation نیست.

### ۱۱) جمع‌بندی مفهومی

- Profile فقط برای ترافیک Accept‌شده اجرا می‌شود.
- سه سطح شاهد: پیکربندی، وضعیت سرویس، رفتار.
- Needs-License را صریح ثبت کنید.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) UTM در کجای Packet Flow است؟ *(پاسخ: 16-1-ت1)*

**ت2.** (ساده) کدام قابلیت‌ها بدون لایسنس کار می‌کنند؟ *(پاسخ: 16-1-ت2)*

**ت3.** (متوسط) چرا «Profile ساخته شد» شاهد کافی نیست؟ *(پاسخ: 16-1-ت3)*

**ت4.** (سخت) ماتریس لایسنس Lab خود را با ۳ شاهد بسازید. *(پاسخ: 16-1-ت4)*

**ت5.** (سخت، طراحی) طرح لایه‌ای ضدبدافزار برای سازمانی بدون Sandbox. *(پاسخ: 16-1-ت5)*

**Q1.** Quick quiz (English): Why is a created profile not proof of protection? *(پاسخ: 16-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| UTM | Unified Threat Management | مدیریت یکپارچه‌ی تهدید |
| FortiGuard | FortiGuard Services | سرویس به‌روزرسانی Fortinet |
| Profile | Security profile | مجموعه‌ی تنظیم بازرسی |

- *A security profile only works when it is attached to an accepting policy.* ← Profile فقط وقتی کار می‌کند که به Policy مجاز وصل شده باشد.

### ۱۴) کارت Lab

**Lab:** ماتریس UTM. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/utm-license-log.md`. **Rollback:** ندارد (فقط خواندنی).

### ۱۵) منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Security Profiles، FortiGuard.
- [Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison).

<a id="l-16-2"></a>

### تعمیق: ماتریس لایسنس قبل از وعده‌دادن به مدیر

**قاعده:** هیچ قابلیت UTM قبل از تأیید لایسنس FortiGuard «فعال» اعلام نمی‌شود.

| قابلیت | به لایسنس نیاز دارد؟ |
|---|---|
| Web Filter Category | بله (FortiGuard Web Filtering) |
| Static URL Filter | خیر |
| Antivirus | بله (AV) |
| IPS Signature به‌روز | بله |
| Application Control | بله |

**بررسی:** `diagnose debug rating` وضعیت سرور رتبه‌بندی؛ در GUI صفحه FortiGuard.

**نسخه‌ی Lab:** FortiGate VM بدون لایسنس ⇒ فقط Static URL و بخش‌های محلی؛ بقیه Needs-License.

**پرسش‌های مصاحبه**
1. *تفاوت Static و Category؟* دستی در برابر پایگاه داده‌ی ابری.
2. *لایسنس منقضی چه می‌شود؟* به‌روزرسانی متوقف؛ تنظیم فعلی ممکن است کار کند ولی Category جدید نه.
3. *چرا Evidence لایسنس؟* ادعای ظرفیت بدون آن خطاست.

### تکمیل عمیق: نقشه‌ی UTM و ماتریس لایسنس

#### چرا؟

قبل از وعده‌دادن به مدیر که «فایروال ویروس‌ها را می‌گیرد»، باید بدانید چه Profileی چه لایسنسی می‌خواهد.

#### ماتریس

| قابلیت | لایسنس | بدون لایسنس |
|---|---|---|
| Web Filter Category | FortiGuard Web Filtering | فقط Static URL |
| Antivirus | FortiGuard AV | امضای قدیمی/غیرفعال |
| IPS | FortiGuard IPS | امضای محدود |
| Application Control | FortiGuard AppCtrl | امضای محدود |
| DNS Filter | FortiGuard | محدود |

(وضعیت دقیق را از مستند همان نسخه تأیید کنید.)

#### مثال ساده — بررسی

``` text
get system status
diagnose debug rating
execute update-now
```

در GUI صفحه‌ی FortiGuard وضعیت لایسنس و آخرین به‌روزرسانی را می‌دهد.

#### مثال متوسط — VM بدون لایسنس

در Lab ما FortiGate VM لایسنس ندارد ⇒ Category/AV/IPS «Needs-License» و اجرا نشده؛ فقط Static URL و تنظیم Profile (Syntax) مستند می‌شود.

#### مثال سخت — لایسنس منقضی

لایسنس تمام شد؛ Profile هنوز روی Policy است ولی Category نمی‌تواند Rating بگیرد. رفتار پیش‌فرض (Allow/Block) را از مستند بخوانید (`rating-error` در Web Filter) و تنظیم کنید.

#### Lab

فهرست Profileهای شعبه‌ی خودتان با ستون لایسنس بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Category کار نمی‌کند | لایسنس/Rating | بررسی |
| IPS قدیمی | به‌روزرسانی | update-now |
| Log بی‌Category | rating error | تنظیم |

#### پرسش‌ها با پاسخ

**۱. Static URL لایسنس می‌خواهد؟** خیر.
**۲. rating-error؟** رفتار هنگام خطای Rating.
**۳. چرا ماتریس؟** وعده‌ی غلط.

#### English Corner

- *UTM features that rely on FortiGuard require an active subscription.*
- Q: What happens to category filtering when the license expires?

## درس 16-2 — Web Filter و DNS Filter: Static URL، Category، FQDN و عیب‌یابی HTTPS

**فصل ۱۶ · بازنویسی عمیق (جایگزین نسخه‌ی فشرده) · پیش‌نیاز: ۱۶-۰، ۱۶-۱، ۱۲-۰ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** Static URL Filter بدون لایسنس FortiGuard کار می‌کند؛ Category/Rating **Needs-License**. سینتکس `Unverified` روی Image. Lab «اجرا نشده».

### ۱) هدف آموزشی

دانشجو بتواند:

1. توضیح دهد Web Filter چگونه تصمیم می‌گیرد (Static URL، Category، Safe Search، Quota) و ترتیب ارزیابی چیست.
2. تفاوت **FQDN Filter** (در Policy/Address) با **Web Filter Profile** را بگوید.
3. بداند در HTTPS بدون Deep Inspection چه چیزی دیده می‌شود (SNI) و چه نه (مسیر URL).
4. **DNS Filter** را با Web Filter مقایسه و محدودیت‌اش (DoH) را بشناسد.
5. یک Profile بسازد، به Policy وصل کند و **با آزمون مثبت/منفی و Log** ثابت کند کار می‌کند.

### ۲) پیش‌نیازها

Flow/Proxy و TLS (۱۶-۰)، Packet Flow (۱۲-۰)، Policy (فصل ۱۳).

### ۳) مفهوم پایه

دسترسی وب مهم‌ترین مسیر ورود بدافزار و نشت داده است. Web Filter می‌پرسد: «این مقصد برای این کاربر مجاز است؟». سه منبع تصمیم: (۱) فهرست دستی شما (Static)، (۲) دسته‌بندی FortiGuard (Category؛ لایسنس)، (۳) رفتار (Quota، Safe Search).

### ۴) توضیح عمیق فنی

#### ۴-۱) ترتیب ارزیابی (مفهومی)

``` text
1. Static URL filter entries (first match: allow / block / monitor / exempt)
2. FortiGuard category filter (needs rating service)
3. Other options (safe search, quota, content checks)
```

اگر Static URL «Exempt» بزنید، بقیه‌ی بررسی‌ها برای آن مقصد رد می‌شوند؛ پس Exempt را با احتیاط استفاده کنید.

#### ۴-۲) انواع ورودی Static URL

- `simple`: مطابقت ساده‌ی دامنه/URL.
- `wildcard`: الگوی `*.example.com`.
- `regex`: عبارت منظم (قدرت زیاد، خطای زیاد، CPU بیشتر).
- Action: `allow`, `block`, `monitor`, `exempt`.

#### ۴-۳) HTTPS: چه چیزی دیده می‌شود؟

| حالت | دید | نتیجه |
|---|---|---|
| HTTP | URL کامل | فیلتر کامل |
| HTTPS + Certificate Inspection | دامنه (SNI/گواهی) | فیلتر بر اساس دامنه/Category؛ نه مسیر |
| HTTPS + Deep Inspection | URL کامل پس از رمزگشایی | فیلتر کامل؛ نیاز CA (۱۶-۰) |

مثال: بلاک `example.com/private` فقط با Deep Inspection ممکن است؛ بلاک `example.com` با SNI ممکن است.

#### ۴-۴) DNS Filter

فایروال Query را قبل از اتصال کنترل می‌کند: دامنه‌ی مخرب → NXDOMAIN/Redirect به Block Page. نقاط ضعف: **DoH/DoT** (DNS رمز) و IP مستقیم؛ راه‌حل: Application Control برای DoH + Deep Inspection + فقط DNS داخلی (Policy: DNS فقط به سرور شما).

#### ۴-۵) Block Page و Log

Block Page (Replacement Message) کاربر را مطلع می‌کند. Log: `action=blocked`، `catdesc`/`url`. برای عیب‌یابی، **Log Web Filter** اولین شاهد است.

### ۵) پیاده‌سازی: GUI و CLI

**GUI:**

1. Security Profiles → Web Filter → Create New (Name: WF-STD).
2. FortiGuard Category Based Filter (اگر لایسنس) یا خاموش.
3. Static URL Filter: Enable → Create New: URL `badsite.example`، Type Simple، Action Block.
4. Policy & Objects → Firewall Policy → Users-to-Internet → Security Profiles: Web Filter = WF-STD؛ SSL Inspection = certificate-inspection.
5. Log & Report → Web Filter.

**CLI:**

``` text
config webfilter urlfilter
    edit 1
        set name "URLF-LAB"
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
config firewall policy
    edit 10
        set utm-status enable
        set webfilter-profile "WF-STD"
        set ssl-ssh-profile "certificate-inspection"
    next
end
```

(سینتکس `Unverified` روی 7.0.3؛ فیلدهای `utm-status` و ساختار `config web` را با CLI Reference تطبیق دهید.)

### ۶) مثال‌ها

**ساده:** بلاک `badsite.example`. کلاینت: `curl -I http://badsite.example` → Block Page؛ `curl -I http://good.example` → OK.

**متوسط:** بلاک فقط `social.example/games` با HTTPS: با Certificate Inspection ممکن نیست؛ دو راه: Deep Inspection با Exemption مناسب، یا بلاک کل دامنه برای ساعات کاری با Schedule.

**سخت (تحلیل خطا):** URL بلاک شده ولی کاربر باز می‌کند. فرضیه‌ها به ترتیب: (۱) Profile به Policy وصل نیست؛ (۲) Policy دیگری بالاتر Match شده؛ (۳) HTTPS و ورودی نیازمند مسیر کامل؛ (۴) QUIC دور می‌زند؛ (۵) DoH/IP مستقیم؛ (۶) Exempt قبلی. شواهد: Debug Flow (Policy ID)، Log Web Filter، Capture (UDP 443).

### ۷) Troubleshooting

| علامت | شاهد | علت |
|---|---|---|
| Block نمی‌شود | Log خالی | Profile وصل نیست/Policy دیگر |
| HTTPS مسیر بلاک نمی‌شود | Log فقط دامنه | Certificate Inspection |
| Block Page خطای گواهی می‌دهد | مرورگر | CA نصب نیست |
| QUIC دور می‌زند | Capture UDP 443 | بلاک QUIC |
| Category کار نمی‌کند | Log: rating error | لایسنس/ارتباط FortiGuard |

### ۸) نکات امنیتی

- Exempt/Allow را محدود و مستند کنید.
- Safe Search و بلاک Proxy/Anonymizer Category (در صورت لایسنس).
- Web Filter جایگزین Patch/EDR نیست.

### ۹) جمع‌بندی

- ترتیب: Static → Category → سایر؛ Exempt همه چیز بعدی را رد می‌کند.
- HTTPS بدون Deep فقط دامنه؛ با Deep مسیر کامل.
- DNS Filter قبل از اتصال؛ ضعف DoH. طبق مستند Fortinet بازرسی DoT/DoH فقط با Deep Inspection ممکن است (قبل از 7.6.0 فقط Proxy mode)؛ جایگزین: مسدودسازی TCP 853/443 به ارائه‌دهندگان شناخته‌شده یا (7.6.0+) Blocklist خارجی.
- آزمون مثبت/منفی و Log.

### ۱۰) تمرین و ارزیابی

**ت1.** (ساده) Static URL با Category چه فرقی دارد؟ *(پاسخ: 16-2-ت1)*

**ت2.** (ساده) Exempt چه می‌کند؟ *(پاسخ: 16-2-ت2)*

**ت3.** (متوسط) چرا بلاک مسیر در HTTPS نیاز به Deep دارد؟ *(پاسخ: 16-2-ت3)*

**ت4.** (متوسط) DNS Filter چه نقطه‌ضعفی دارد؟ *(پاسخ: 16-2-ت4)*

**ت5.** (سخت) فرضیه‌های «URL بلاک‌شده باز می‌شود» را به ترتیب و با شاهد بنویسید. *(پاسخ: 16-2-ت5)*

**ت6.** (سخت، طراحی) سیاست وب برای ۳ گروه (کارمند، مهمان، سرور) طراحی کنید. *(پاسخ: 16-2-ت6)*

**Q1.** Quick quiz (English): What does an exempt action in a static URL filter do? *(پاسخ: 16-2-Q1)*

### ۱۱) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Static URL | Static URL filter | فیلتر دستی URL |
| FQDN | Fully Qualified Domain Name | نام کامل دامنه |
| DoH | DNS over HTTPS | DNS رمزشده |
| Safe Search | Safe search enforcement | اجبار جست‌وجوی امن |

- *HTTPS without deep inspection reveals only the domain name.* ← HTTPS بدون Deep فقط نام دامنه را نشان می‌دهد.

### ۱۲) Lab

**کارت Lab:** Static URL Filter. **هدف:** بلاک یک دامنه و اثبات با Log. **توپولوژی:** Client → FGT → Web Lab. **وضعیت:** اجرا نشده. **مراحل:** مطابق بخش ۵. **Verification:** مثبت/منفی؛ Log. **Rollback:** حذف Profile از Policy. **Evidence:** `03-ops/webfilter-static.md`.

### ۱۳) منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — Web filter، DNS filter؛ [Inspection modes](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/721410/inspection-modes).

<a id="l-16-3"></a>

### تعمیق: Web Filter برای HTTPS بدون Inspection

**مسئله:** URL کامل در HTTPS رمز است؛ بدون SSL Inspection فقط **SNI/Domain** دیده می‌شود.

``` text
config webfilter urlfilter
 edit 1
  config entries
   edit 1
    set url "*.example-bad.com"
    set type wildcard
    set action block
   next
  end
 next
end
```

**آزمون:** مرورگر به https://www.example-bad.com ⇒ صفحه‌ی Block (Replacement Message)؛ Log `utmaction=blocked`.

**DNS Filter** مستقل از TLS: پاسخ DNS را بر اساس Category تغییر/مسدود می‌کند؛ برای HTTPS بدون Inspection روش مناسب.

**پرسش‌های مصاحبه**
1. *چرا مسیر کامل دیده نمی‌شود؟* رمزگذاری TLS.
2. *DoH مشکل؟* DNS Filter دور می‌خورد؛ بلاک DoH Resolverها.
3. *Block Page روی HTTPS؟* نیازمند Inspection یا ارسال Reset.

### تکمیل عمیق: Web Filter و DNS Filter — HTTPS بدون Inspection

#### چرا؟

بسیاری از سازمان‌ها نمی‌خواهند ترافیک را رمزگشایی کنند؛ آیا باز هم می‌توان وب را فیلتر کرد؟ بله، با SNI و DNS.

#### آنچه بدون Inspection دیده می‌شود

در HTTPS مسیر کامل URL رمز است؛ ولی **SNI** (نام سرور در ClientHello) دیده می‌شود. پس Domain را می‌توان مسدود کرد، ولی نه مسیر خاص (`/video/123`).

#### مثال ساده — Static URL

``` text
config webfilter urlfilter
 edit 1
  set name "BLOCK-LIST"
  config entries
   edit 1
    set url "*.example-bad.com"
    set type wildcard
    set action block
   next
  end
 next
end
```

#### مثال متوسط — DNS Filter

پاسخ DNS را بر اساس Category تغییر/مسدود می‌کند؛ مستقل از TLS. دور زدن: DoH (DNS over HTTPS) به Resolverهای بیرونی؛ راه: مسدودکردن DoH Resolverهای شناخته‌شده یا App Control.

#### مثال سخت — Block Page

برای HTTPS بدون Inspection، فایروال نمی‌تواند Block Page سالم نشان دهد (گواهی نامعتبر)؛ معمولاً اتصال Reset می‌شود. با Inspection صفحه‌ی بلوک نمایش داده می‌شود.

#### آزمون

به https://www.example-bad.com برو ⇒ بلوک؛ Log: `utmaction=blocked`.

#### Lab

Static URL را بدون لایسنس تست کنید (اجرا نشده).

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| مسدود نمی‌شود | wildcard | الگو |
| DoH دور می‌زند | Resolver بیرونی | مسدود |
| Block Page نه | بدون Inspection | Reset طبیعی |

#### پرسش‌ها با پاسخ

**۱. SNI چیست؟** نام سرور.
**۲. DNS Filter مزیت؟** مستقل از TLS.
**۳. DoH؟** دور زدن DNS.

#### English Corner

- *Without inspection, the firewall can filter by SNI and DNS but not by URL path.*
- Q: How can users bypass DNS filtering?

## درس 16-3 — Antivirus و File Filter: سازوکار، حالت‌ها و تست امن

**فصل ۱۶ · بازنویسی عمیق · پیش‌نیاز: ۱۶-۰، ۱۶-۲ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** AV Signature **Needs-License**؛ File Filter بدون لایسنس. گزینه‌های Flow/Proxy از جدول مقایسه‌ی رسمی ([Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison)). Lab «اجرا نشده».

### ۱) هدف آموزشی

1. بداند AV چه چیزی را کشف می‌کند (Signature، Heuristic) و چه چیزی را نه (Zero-day، فایل رمزدار، ترافیک رمز بدون Deep).
2. تفاوت AV در Flow و Proxy را بداند و انتخاب کند.
3. **File Filter** را به‌عنوان لایه‌ی مکمل بدون لایسنس طراحی کند.
4. با **فایل EICAR** تست امن انجام دهد و نتیجه‌ی واقعی ثبت کند.
5. FP/FN و اثر Performance را ارزیابی کند.

### ۲) پیش‌نیازها

۱۶-۰ (Flow/Proxy، TLS)، ۱۶-۷ (FP/FN).

### ۳) مفهوم پایه

بدافزار معمولاً به‌صورت فایل از وب/ایمیل/اشتراک می‌رسد. AV فایل را (یا جریان را) با پایگاه Signature می‌سنجد. اما هر امضا از گذشته می‌آید؛ بدافزار جدید یا رمزدار را نمی‌گیرد. پس AV **یک لایه** است، نه راه‌حل کامل.

### ۴) توضیح عمیق فنی

#### ۴-۱) AV چگونه کار می‌کند

- **Flow-based:** بسته‌ها در جریان اسکن می‌شوند؛ سریع؛ بدون بازسازی کامل فایل؛ گزینه‌ها کمتر.
- **Proxy-based:** فایل کامل Buffer می‌شود و پس از اسکن به کاربر می‌رسد؛ دقیق‌تر و گزینه‌های بیشتر (مثلاً محدودیت اندازه‌ی Buffer، Content Disarm بسته به نسخه)؛ تأخیر و مصرف حافظه بیشتر.
- سقف اندازه‌ی فایل: فایل بزرگ‌تر از Threshold اسکن نمی‌شود (Pass یا Block طبق تنظیم) — **این یک نقطه‌ی کور است**.

#### ۴-۲) چه چیزی دیده نمی‌شود

| مورد | علت |
|---|---|
| Zero-day | Signature ندارد (نیاز Sandbox) |
| فایل رمزدار (zip با رمز) | محتوا قابل اسکن نیست |
| HTTPS بدون Deep | محتوا رمز است |
| فایل بزرگ‌تر از سقف | اسکن نمی‌شود |
| پروتکل غیراسکن‌شده | AV روی پروتکل‌های انتخاب‌شده کار می‌کند |

#### ۴-۳) File Filter

کنترل بر اساس **نوع/پسوند** (و Magic bytes در صورت پشتیبانی) و جهت (Upload/Download). مثال: بلاک `exe, scr, js, vbs` از اینترنت؛ بلاک فایل رمزدار. مزیت: بدون لایسنس، سبک؛ ضعف: پسوند جعل‌شدنی، محتوای مخرب در نوع مجاز.

#### ۴-۴) EICAR

فایل متنی استاندارد بی‌خطر که همه‌ی AVها به‌عنوان «ویروس تست» می‌شناسند؛ برای آزمون زنجیره (Policy→Profile→Inspection→Log). **نتیجه‌ی آزمون باید ثبت شود؛ اگر Signature در Lab نیست، «اجرا نشده/ناموفق» بنویسید، نه «کار می‌کند».**

### ۵) پیاده‌سازی: GUI و CLI

**GUI:**

1. Security Profiles → AntiVirus → Create New (AV-STD): Inspected Protocols: HTTP/FTP/SMTP/... ؛ Action Block.
2. Security Profiles → File Filter → Create New (FF-STD): Rule: File types exe/script؛ Direction Incoming؛ Action Block.
3. Policy: AntiVirus = AV-STD؛ File Filter = FF-STD؛ SSL Inspection (مناسب).
4. Log & Report → AntiVirus / Security Events.

**CLI (ساختار؛ `Unverified`):**

``` text
config antivirus profile
    edit "AV-STD"
        set comment "lab"
    next
end
config file-filter profile
    edit "FF-STD"
        config rules
            edit "block-exe"
                set protocol http ftp
                set action block
                set file-type "exe"
            next
        end
    next
end
config firewall policy
    edit 10
        set av-profile "AV-STD"
        set file-filter-profile "FF-STD"
    next
end
```

### ۶) مثال‌ها

**ساده:** دانلود EICAR از وب: Block + Log AV.

**متوسط:** `setup.exe` بلاک می‌شود با File Filter در حالی‌که AV لایسنس ندارد؛ درس: لایه‌ی بدون لایسنس مفید است.

**سخت:** مهاجم zip رمزدار می‌فرستد؛ AV نمی‌بیند؛ File Filter رمزدار را بلاک می‌کند اگر پشتیبانی شود؛ سیاست: بلاک آرشیو رمزدار از منبع ناشناس + آموزش + Sandbox (در صورت لایسنس). **FN را بپذیرید و مستند کنید.**

### ۷) Troubleshooting

| علامت | علت |
|---|---|
| EICAR رد می‌شود | Profile وصل نیست/لایسنس/DB نیست/HTTPS بدون Deep |
| فایل بزرگ اسکن نمی‌شود | سقف اندازه |
| کندی دانلود | Proxy Buffer |
| FP | Signature/استثنا |

### ۸) نکات امنیتی

- EICAR فقط برای تست؛ بدافزار واقعی ممنوع.
- Exception محدود.
- ترکیب با Patch/EDR.

### ۹) جمع‌بندی

- AV Signature؛ Zero-day و رمزدار نه.
- Flow سریع/Proxy دقیق.
- File Filter لایه‌ی بدون لایسنس.
- نتیجه‌ی واقعی ثبت شود.

### ۱۰) تمرین و ارزیابی

**ت1.** (ساده) EICAR چیست؟ *(پاسخ: 16-3-ت1)*

**ت2.** (ساده) AV چه چیزی را نمی‌بیند؟ *(پاسخ: 16-3-ت2)*

**ت3.** (متوسط) تفاوت AV در Flow و Proxy؟ *(پاسخ: 16-3-ت3)*

**ت4.** (متوسط) چرا سقف اندازه‌ی فایل نقطه‌ی کور است؟ *(پاسخ: 16-3-ت4)*

**ت5.** (سخت) سیاست دفاع از zip رمزدار را طراحی کنید. *(پاسخ: 16-3-ت5)*

**Q1.** Quick quiz (English): Why can't antivirus inspect a password-protected archive? *(پاسخ: 16-3-Q1)*

### ۱۱) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| AV | Antivirus | ضدویروس |
| Heuristic | Heuristic detection | تشخیص رفتاری/الگویی |
| Sandbox | Sandbox | محیط اجرای ایزوله |
| Magic bytes | File magic bytes | امضای ابتدای فایل |

- *Antivirus is one layer, not a complete defense.* ← ضدویروس یک لایه است، نه دفاع کامل.

### ۱۲) Lab

**کارت Lab:** AV/File Filter. **هدف:** EICAR و بلاک exe. **وضعیت:** اجرا نشده. **Verification:** Log AV/File Filter. **Rollback:** حذف Profile. **Evidence:** `03-ops/av-notes.md` (نتیجه‌ی واقعی).

### ۱۳) منابع

- Fortinet Docs: [Inspection mode feature comparison](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/922096/inspection-mode-feature-comparison)؛ EICAR (eicar.org).

<a id="l-16-4"></a>

### تعمیق: تست امن AV با EICAR و تفسیر

``` text
curl -O https://secure.eicar.org/eicar.com.txt
```

فایل EICAR بی‌خطر است و همه‌ی AVها آن را می‌شناسند. نتیجه‌ی مورد انتظار: Block + Log `virus=EICAR_TEST_FILE`.

**حالت‌ها:** Flow-based (سریع‌تر، امضای پایه) در برابر Proxy-based (بافر کامل فایل). **File Filter** بر اساس نوع/پسوند مستقل از امضا است؛ مثلاً مسدودسازی exe از اینترنت.

**محدودیت:** فایل رمزگذاری‌شده/بزرگ‌تر از Oversize Limit اسکن نمی‌شود؛ Policy برای Oversize را مشخص کنید.

**پرسش‌های مصاحبه**
1. *چرا EICAR؟* تست بی‌خطر.
2. *فایل zip رمزدار؟* قابل اسکن نیست؛ Policy جدا.
3. *AV در HTTPS؟* فقط با SSL Inspection.

### تکمیل عمیق: Antivirus و File Filter

#### چرا؟

فایل آلوده معمولاً از وب یا ایمیل می‌آید؛ AV امضا را بررسی و File Filter نوع فایل را کنترل می‌کند.

#### آزمون امن با EICAR

EICAR یک فایل متنی بی‌خطر است که همه‌ی AVها آن را «ویروس تست» می‌شناسند.

``` text
curl -O https://secure.eicar.org/eicar.com.txt
```

انتظار: Block و Log `virus=EICAR_TEST_FILE`.

#### مثال ساده — File Filter

مسدودکردن `exe` و `scr` از اینترنت:

``` text
config file-filter profile
 edit "FF1"
  config rules
   edit 1
    set name "block-exe"
    set protocol http https
    set action block
    set file-type "exe"
   next
  end
 next
end
```

(Syntax را از مستند نسخه تأیید کنید.)

#### مثال متوسط — محدودیت‌ها

فایل رمزدار (zip با رمز) و فایل بزرگ‌تر از Oversize Limit اسکن نمی‌شود؛ Policy برای رفتار Oversize (block/pass) را صریح بگذارید.

#### مثال سخت — HTTPS

بدون SSL Inspection، فایل داخل HTTPS دیده نمی‌شود؛ AV در وب رمز بی‌اثر است. با Inspection فعال می‌شود.

#### Lab

EICAR را در Lab با AV (در صورت لایسنس) تست کنید؛ در غیر این صورت «اجرا نشده».

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| EICAR عبور می‌کند | بدون Inspection/لایسنس | بررسی |
| فایل بزرگ | Oversize | سیاست |
| zip رمزدار | قابل اسکن نیست | سیاست |

#### پرسش‌ها با پاسخ

**۱. EICAR چیست؟** ویروس تست بی‌خطر.
**۲. Oversize؟** فایل بزرگ‌تر از حد.
**۳. AV در HTTPS؟** نیاز به Inspection.

#### English Corner

- *The EICAR test file safely validates antivirus inspection.*
- Q: Why is an encrypted archive hard for antivirus to scan?

## درس 16-4 — IPS، DoS Policy و Application Control: سازوکار، تنظیم و FP

**فصل ۱۶ · بازنویسی عمیق · پیش‌نیاز: ۱۶-۰، ۱۶-۷، ۱۱-۷ · ≈ ۷ ساعت**

> **وضعیت (FortiOS 7.0.3):** Signature IPS **Needs-License** (FortiGuard AV/IPS)؛ Signature برنامه (Application Control) طبق مستند جزو FortiCare پایه است؛ DoS Policy و Custom Signature بدون لایسنس. سینتکس `Unverified`. تست حمله فقط در Lab ایزوله و مجاز. Lab «اجرا نشده».

### ۱) هدف آموزشی

1. IPS (Signature، Severity، Target، Action) و تفاوت **Monitor/Block** را توضیح دهد.
2. **DoS Policy** (Anomaly: SYN Flood، UDP Flood، Port Scan، Session Limit) را به Threshold درست تبدیل کند.
3. **Application Control** را (Category، Application، Action، QUIC/DoH) به کار ببرد.
4. اثر Performance و FP را بسنجد و **Exception دقیق** بنویسد.
5. در Lab با ابزار مجاز تست و نتیجه را ثبت کند.

### ۲) مفهوم پایه

- **IPS:** الگوی اکسپلویت را در ترافیک می‌شناسد (مثل «آنتی‌ویروس برای حمله»).
- **DoS Policy:** حجم/نرخ غیرعادی را می‌گیرد، بدون نیاز به شناخت محتوا.
- **Application Control:** می‌پرسد «این چه برنامه‌ای است؟» حتی روی پورت غیرمعمول.

### ۳) توضیح عمیق فنی

#### ۳-۱) IPS Sensor

Sensor مجموعه‌ای از Filter/Signature است: انتخاب بر اساس **Severity** (Critical تا Info)، **Target** (Server/Client)، **OS**، **Protocol**. Action: `pass`, `monitor`, `block`, `reset`, `quarantine`. اصول: ابتدا Monitor؛ برای سرور مشخص (Target=Server) Signatureهای مرتبط؛ Severity High/Critical Block؛ کم‌اهمیت‌ها Monitor. **Virtual Patching:** Signature آسیب‌پذیری را تا Patch سرور بلاک می‌کند.

#### ۳-۲) DoS Policy

``` text
Threshold examples (tune from baseline, not copied):
tcp_syn_flood   : 2000 pkts/s per source
udp_flood       : 2000 pkts/s
ip_src_session  : 5000 sessions per source
tcp_port_scan   : 1000 pkts/s
```

اعداد را از **Baseline** (۲۷-۰) بسازید؛ Threshold کم = FP برای کاربران واقعی؛ زیاد = ناکارآمد. DoS Policy **قبل از Firewall Policy** (در مسیر سریع Ingress) اعمال می‌شود و ارزان است؛ روی Interface WAN.

#### ۳-۳) Application Control

Signature برنامه‌ها (Teams، Dropbox، BitTorrent، DoH ...). Action: Allow/Monitor/Block/Quarantine. نکات: (۱) **QUIC:** بلاک تا ترافیک به TCP/TLS برگردد و Inspection ممکن شود. (۲) **DoH:** بلاک برنامه‌ی DoH یا Policy DNS فقط به سرور داخلی. (۳) Deep Inspection برای شناسایی دقیق‌تر در HTTPS. (۴) بدون لایسنس: Port-based/Service-based.

#### ۳-۴) Performance

IPS/App بازرسی محتوایی است: CPU↑ و Offload↓ (۱۲-۹). راه: Sensor انتخابی روی Policyهای مهم؛ DoS ارزان‌تر؛ Baseline قبل/بعد.

### ۴) پیاده‌سازی: GUI و CLI

**GUI:** Policy & Objects → DoS Policy → Create New (Incoming: port1؛ Source/Dest: all؛ Service ALL؛ Anomaly: Threshold). Security Profiles → Intrusion Prevention → Create New (Filters: Severity High, Critical؛ Action Block). Security Profiles → Application Control → Create New (Category Proxy/P2P: Block؛ QUIC: Block). Policy: فعال‌سازی هر دو.

**CLI (`Unverified`):**

``` text
config firewall DoS-policy
    edit 1
        set interface "port1"
        set srcaddr "all"
        set dstaddr "all"
        set service "ALL"
        config anomaly
            edit "tcp_syn_flood"
                set status enable
                set threshold 2000
                set action block
            next
        end
    next
end
config ips sensor
    edit "IPS-LAB"
        config entries
            edit 1
                set severity high critical
                set action block
            next
        end
    next
end
config application list
    edit "APP-LAB"
        config entries
            edit 1
                set category 2
                set action block
            next
        end
    next
end
```

### ۵) مثال‌ها

**ساده:** SYN Flood آزمایشی (hping3 در Lab) با 5000 pkt/s؛ DoS Policy Block؛ Log anomaly.

**متوسط:** FP: سامانه‌ی مالی با Signature اشتباه قطع شد؛ Log IPS → Signature ID؛ Exception فقط برای آن Signature و آن سرور؛ تاریخ بازبینی.

**سخت:** CPU ۹۰٪ پس از فعال‌کردن IPS روی همه‌ی ترافیک؛ تحلیل: `diagnose sys top` (ipsengine)، Offload کم. راه: Sensor انتخابی (Target=Server، Severity High+) و Monitor برای بقیه؛ اندازه‌گیری مجدد.

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| DoS اثر ندارد | Interface اشتباه، Threshold بالا |
| FP کاربران | Threshold کم |
| IPS بلاک نمی‌کند | Action=monitor/لایسنس/Profile وصل نیست |
| QUIC دور می‌زند | بلاک نشده |
| CPU زیاد | Sensor گسترده |

### ۷) نکات امنیتی

- آزمون حمله فقط در Lab ایزوله و مجاز.
- IPS جایگزین Patch نیست.
- Exception با تاریخ بازبینی.

### ۸) جمع‌بندی

- IPS بر اساس Signature؛ ابتدا Monitor؛ Virtual Patching.
- DoS Policy با Baseline؛ ارزان و Ingress.
- App Control با QUIC/DoH.
- Performance را اندازه بگیرید.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) IPS و DoS Policy چه فرقی دارند؟ *(پاسخ: 16-4-ت1)*

**ت2.** (ساده) Virtual Patching یعنی چه؟ *(پاسخ: 16-4-ت2)*

**ت3.** (متوسط) Threshold DoS را چگونه تعیین می‌کنید؟ *(پاسخ: 16-4-ت3)*

**ت4.** (متوسط) چرا QUIC بلاک می‌شود؟ *(پاسخ: 16-4-ت4)*

**ت5.** (سخت) پس از IPS، CPU ۹۰٪ شد؛ تحلیل و رفع. *(پاسخ: 16-4-ت5)*

**Q1.** Quick quiz (English): Why start an IPS sensor in monitor mode? *(پاسخ: 16-4-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| IPS | Intrusion Prevention System | جلوگیری از نفوذ |
| DoS | Denial of Service | انکار سرویس |
| Anomaly | Anomaly threshold | آستانه‌ی ناهنجاری |
| Virtual patching | Virtual patching | وصله‌ی مجازی |

- *Tune thresholds from your own baseline.* ← آستانه‌ها را از Baseline خودتان تنظیم کنید.

### ۱۱) Lab

**کارت Lab:** DoS و IPS. **وضعیت:** اجرا نشده. **Verification:** Log anomaly/IPS، `sys top`. **Rollback:** حذف Policy/Profile. **Evidence:** `03-ops/ips-dos.md`.

### ۱۲) منابع

- Fortinet Docs: FortiOS 7.0 Administration Guide — DoS policy، Intrusion prevention، Application control.

<a id="l-16-5"></a>

### تعمیق: تنظیم IPS با کاهش False Positive

**روش:** ابتدا Monitor (Pass + Log)، دو هفته مشاهده، سپس Block برای امضاهای ایمن.

``` text
config ips sensor
 edit "IPS-SRV"
  config entries
   edit 1
    set severity high critical
    set action block
   next
  end
 next
end
```

**DoS Policy:** `tcp_syn_flood threshold 2000 action block` برای محافظت VIP؛ آستانه را از Baseline ترافیک واقعی بگیرید (مثلاً Peak × 3).

**Application Control:** مسدودسازی Category (مثل P2P) و محدودیت Shaper.

**FP:** هر Block ناخواسته ⇒ Exemption مستند با مالک و تاریخ.

**پرسش‌های مصاحبه**
1. *چرا ابتدا Monitor؟* جلوگیری از قطع سرویس.
2. *DoS بر چه چیزی؟* نرخ بسته/اتصال.
3. *IPS روی ترافیک رمزی؟* فقط با Inspection.

### تکمیل عمیق: IPS، DoS و Application Control — تنظیم و FP

#### چرا؟

IPS بد تنظیم‌شده یا همه‌چیز را قطع می‌کند (False Positive) یا چیزی را نمی‌گیرد. تنظیم مرحله‌ای کلید است.

#### روش مرحله‌ای

1. Monitor (Pass + Log) برای ۲ هفته.
2. بررسی Logها: کدام امضاها FP هستند؟
3. Block برای شدت بالا/بحرانی و امضاهای مطمئن.
4. Exemption مستند برای FP با مالک و تاریخ.

#### مثال ساده

``` text
config ips sensor
 edit "IPS-SRV"
  config entries
   edit 1
    set severity high critical
    set action block
   next
  end
 next
end
```

#### مثال متوسط — DoS Policy

``` text
config firewall DoS-policy
 edit 1
  set interface "port1"
  set srcaddr "all"
  set dstaddr "VIP-WEB"
  set service "ALL"
  config anomaly
   edit "tcp_syn_flood"
    set status enable
    set threshold 2000
    set action block
   next
  end
 next
end
```

آستانه را از Baseline بگیرید: اگر Peak عادی SYN 500/s است، آستانه ≈ Peak × 3 = 1500–2000.

#### مثال سخت — Application Control

مسدودکردن P2P/Proxy-anonymizers؛ ولی بدون Inspection برنامه‌های رمز را نمی‌بیند. و `Shaper` برای محدود کردن پهنای باند برنامه‌های غیرضروری.

#### Lab

IPS را در Monitor بگذارید و Log را بخوانید (در صورت لایسنس).

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| FP زیاد | Block زود | Monitor |
| DoS قطع قانونی | آستانه کم | افزایش |
| App رمز دیده نمی‌شود | Inspection | فعال |

#### پرسش‌ها با پاسخ

**۱. چرا Monitor اول؟** جلوگیری از قطع.
**۲. آستانه DoS؟** Baseline × ضریب.
**۳. Exemption؟** مستند.

#### English Corner

- *Start in monitor mode and tune before enforcing blocks.*
- Q: How do you choose a DoS threshold?

## درس 16-5 — SSL Inspection عملی: ساخت CA، نصب، Exemption و آزمون

**فصل ۱۶ · بازنویسی عمیق · پیش‌نیاز: ۱۶-۰ (مفاهیم TLS/CA)، ۱۶-۲ · ≈ ۶ ساعت**

> **وضعیت (FortiOS 7.0.3):** پروفایل‌های `certificate-inspection`/`deep-inspection` طبق مستند. سینتکس `Unverified`. Lab «اجرا نشده».

### ۱) هدف آموزشی

1. پروفایل SSL سفارشی (Deep) بسازد، CA را Export و روی کلاینت نصب کند.
2. **Exemption** درست (Category، FQDN، Address) تعریف کند.
3. رفتار گواهی نامعتبر (Block/Allow/Warn) را تنظیم کند.
4. نتیجه را با مرورگر/`openssl s_client`/Capture اثبات کند.
5. مشکلات Pinning، Firefox Trust Store و QUIC را عیب‌یابی کند.

### ۲) پیش‌نیازها

۱۶-۰ (TLS، Chain، Deep vs Certificate).

### ۳) توضیح عمیق فنی

#### ۳-۱) تفاوت CA صادرکننده

فایروال برای هر سایت گواهی جدید با همان Subject/SAN می‌سازد و با **CA فایروال** امضا می‌کند. اگر CA فایروال Self-signed پیش‌فرض باشد، باید روی همه‌ی کلاینت‌ها دستی/GPO نصب شود. بهتر: **Intermediate CA سازمانی** (ADCS) به فایروال بدهید تا زنجیره به Root سازمان برسد و Trust از قبل موجود باشد.

#### ۳-۲) گواهی نامعتبر (Untrusted)

فایروال گواهی سرور مقصد را اعتبارسنجی می‌کند. اگر نامعتبر/منقضی/Self-signed بود، باید به کلاینت **گواهی ناموثق** بدهد (CA جداگانه‌ی Untrusted) تا مرورگر هشدار بدهد؛ نه گواهی معتبر صادر کند. تنظیم Action برای گواهی نامعتبر: Block (امن‌تر برای کاربران عادی) یا Allow/Ignore (خطرناک).

#### ۳-۳) Exemption

- **Category:** Finance/Health (حریم خصوصی).
- **FQDN/Address:** Update سرویس‌های Pinned.
- **Policy جدا:** سرورها با Certificate Inspection.
اصل: Exemption کمترین گستره + مستند + بازبینی.

#### ۳-۴) Trust Storeها

Windows/Chrome/Edge: Store سیستم. **Firefox:** Store مستقل (یا `security.enterprise_roots.enabled`). **Java/Python/curl:** Store/Bundle خودشان (`curl --cacert`، `REQUESTS_CA_BUNDLE`). **موبایل:** MDM. خطای «فقط یک برنامه» معمولاً Trust Store جدا است.

### ۴) پیاده‌سازی: GUI و CLI

**GUI:**

1. Security Profiles → SSL/SSH Inspection → Create New (Deep-Lab): Inspection Method Full SSL Inspection؛ CA Certificate انتخاب؛ Untrusted SSL Certificates: Block؛ Exempt: Web Categories و Addresses.
2. System → Certificates → CA مربوطه → Download (برای نصب).
3. Policy: SSL Inspection = Deep-Lab.
4. Log & Report → Forward Traffic.

**CLI (`Unverified`):**

``` text
config firewall ssl-ssh-profile
    edit "Deep-Lab"
        config https
            set ports 443
            set status deep-inspection
        end
        set untrusted-caname "Fortinet_CA_Untrusted"
        config ssl-exempt
            edit 1
                set type fortiguard-category
                set category 31
            next
        end
    next
end
```

### ۵) مثال‌ها

**ساده:** مرورگر روی `https://example.com`؛ گواهی Issuer = CA فایروال؛ بدون خطا (CA نصب‌شده).

**متوسط:** `openssl s_client -connect example.com:443 -servername example.com | openssl x509 -noout -issuer` در کلاینت: Issuer فایروال؛ مقایسه با خارج از فایروال: Issuer واقعی.

**سخت:** بعد از Deep Inspection، `git` و `pip` در Linux خطای گواهی می‌دهند: Trust Store سیستم و Bundle را به‌روز کنید؛ برای Updaterهای Pinned Exemption بگذارید؛ مستند کنید.

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| خطای گواهی همه‌ی سایت‌ها | CA نصب نیست |
| فقط Firefox | Trust Store جدا |
| بعضی برنامه‌ها | Pinning/Bundle |
| کندی | Deep روی ترافیک سنگین |
| سایت باز نمی‌شود | گواهی مقصد نامعتبر + Block |

### ۷) نکات امنیتی

- کلید خصوصی CA را حفاظت کنید.
- Exemption برای حریم خصوصی/قانون.
- ثبت رضایت/سیاست رمزگشایی.

### ۸) جمع‌بندی

- Deep = CA فایروال + نصب + Exemption.
- گواهی نامعتبر باید به کاربر منتقل شود.
- Trust Storeهای متعدد.
- اثبات با openssl/مرورگر.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) چرا Intermediate CA سازمانی بهتر است؟ *(پاسخ: 16-5-ت1)*

**ت2.** (ساده) کاربر Firefox خطا می‌بیند؛ چرا؟ *(پاسخ: 16-5-ت2)*

**ت3.** (متوسط) گواهی Untrusted چه نقشی دارد؟ *(پاسخ: 16-5-ت3)*

**ت4.** (سخت) با `openssl s_client` اثبات کنید Deep Inspection فعال است. *(پاسخ: 16-5-ت4)*

**ت5.** (سخت، طراحی) برنامه‌ی Exemption برای یک سازمان بنویسید. *(پاسخ: 16-5-ت5)*

**Q1.** Quick quiz (English): How can openssl s_client show that traffic is being inspected? *(پاسخ: 16-5-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| ADCS | Active Directory Certificate Services | سرویس گواهی AD |
| Trust store | Certificate trust store | مخزن CAهای معتبر |
| Exemption | SSL exemption | استثنای Inspection |

- *Verify inspection by comparing the certificate issuer.* ← با مقایسه‌ی Issuer گواهی، Inspection را اثبات کنید.

### ۱۱) Lab

**کارت Lab:** SSL Inspection. **وضعیت:** اجرا نشده. **Verification:** Issuer گواهی، Log. **Rollback:** بازگشت به certificate-inspection. **Evidence:** `03-ops/ssl-inspection.md`.

### ۱۲) منابع

- Fortinet Docs: [SSL & SSH Inspection](https://docs.fortinet.com/document/fortigate/7.0.1/administration-guide/929997/ssl-ssh-inspection)؛ OpenSSL s_client manual.

<a id="l-16-6"></a>

### تعمیق: ساخت CA و توزیع به کلاینت‌ها

**گام‌ها**

1. ساخت/ورود CA سازمانی (ترجیحاً Sub-CA از CA داخلی، نه Self-Signed پیش‌فرض).
2. تنظیم Profile `deep-inspection` با همان CA.
3. توزیع CA با GPO در Active Directory (Trusted Root Certification Authorities).
4. Exemption برای دسته‌های حساس (Health, Finance).

``` text
certutil -dspublish -f corp-ca.cer RootCA
gpupdate /force
certutil -store Root | findstr Corp
```

**آزمون:** مرورگر به https://example.org ⇒ زنجیره باید به CA سازمان برسد؛ در Wireshark SNI قابل‌رؤیت.

**اشتباه رایج:** نصب نکردن CA روی Android/Linux و Java Keystore؛ نتیجه خطای SSL در برنامه‌ها.

**پرسش‌های مصاحبه**
1. *چرا Sub-CA؟* ابطال و کنترل.
2. *Pinning؟* Exemption.
3. *مسائل حقوقی؟* اطلاع‌رسانی و سیاست حریم خصوصی.

### تکمیل عمیق: SSL Inspection عملی — CA، توزیع و Exemption

#### چرا؟

بدون نصب CA روی کلاینت‌ها، Inspection صفحه‌های خطا تولید می‌کند. توزیع درست مرحله‌ی کلیدی است.

#### گام‌ها

1. CA مناسب: ترجیحاً Sub-CA از CA سازمان (قابل ابطال).
2. Import به FortiGate و انتخاب در Profile.
3. توزیع با GPO (Trusted Root).
4. Exemption.
5. آزمون.

#### مثال ساده — GPO

``` text
certutil -dspublish -f corp-ca.cer RootCA
gpupdate /force
certutil -store Root | findstr Corp
```

#### مثال متوسط — Profile

``` text
config firewall ssl-ssh-profile
 edit "deep-inspect"
  config https
   set ports 443
   set status deep-inspection
  end
  set caname "Corp-SubCA"
  config ssl-exempt
   edit 1
    set type fortiguard-category
    set fortiguard-category <ID>
   next
  end
 next
end
```

(کد Category را از مستند بخوانید.)

#### مثال سخت — Android/Linux/Java

CA باید در Keystore هر پلتفرم نصب شود (Java `keytool`، Firefox Store جدا). برنامه‌های Pinning مستثنا.

#### آزمون

مرورگر به https://example.org ⇒ Issuer باید CA سازمان باشد.

``` text
openssl s_client -connect example.org:443 -servername example.org </dev/null | openssl x509 -noout -issuer
```

#### Lab

CA آزمایشی بسازید و در یک VM نصب کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| خطای گواهی | CA نصب نشده | GPO |
| Java شکست | Keystore | keytool |
| بانک شکست | Pinning | Exemption |

#### پرسش‌ها با پاسخ

**۱. چرا Sub-CA؟** ابطال.
**۲. Issuer چه می‌گوید؟** Inspection فعال.
**۳. Keystore؟** فروشگاه گواهی.

#### English Corner

- *Use a revocable sub-CA for inspection rather than a self-signed root.*
- Q: How can you verify that inspection is active from the client?

## درس 16-6 — Performance UTM، اندازه‌گیری، عیب‌یابی و آزمون عملی فصل ۱۶

**فصل 16 · بازنویسی عمیق · پیش‌نیاز: ۱۶-۰ تا ۱۶-۵، ۱۲-۹، ۲۷-۰ · ≈ 6 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. اثر هر Profile بر CPU/Throughput را با آزمایش کنترل‌شده بسنجد.
2. مشکلات UTM (کندی، FP، عدم اثر) را با شواهد عیب‌یابی کند.
3. Exception را امن و مستند بنویسد.
4. آزمون عملی فصل را با Rubric اجرا کند.

### ۲) مفهوم پایه: چیست و چرا؟

UTM منابع می‌خورد؛ «فعال کن و ببین» روش مهندسی نیست. باید **Baseline** داشت، **یک Profile در هر زمان** اضافه کرد، و اثر را اندازه گرفت.

### ۳) توضیح عمیق فنی

#### ۱) روش اندازه‌گیری

``` text
1 Baseline: no profiles; run iperf (N parallel streams, 5 min); record CPU, Throughput, Latency, Sessions
2 Enable profile A only; repeat; record
3 Enable A+B; repeat
4 Compare: delta CPU, delta Throughput
```

شرایط یکسان: همان سرور، همان تعداد Flow، همان نوع ترافیک. نتیجه = جدول اثر هر Profile.

#### ۲) علل رایج کندی

- Proxy-based + Deep Inspection روی ترافیک سنگین.
- IPS روی همه‌ی ترافیک (Offload کم، ۱۲-۹).
- File/Archive بزرگ در AV Proxy (Buffer).
- Logging همه‌ی Allow (I/O).

#### ۳) ابزارها

``` text
get system performance status
diagnose sys top 2 20
diagnose sys session stat
diagnose debug flow filter addr <host>
```

#### ۴) FP: Exception امن

Exception را (۱) فقط برای همان Signature/دامنه، (۲) فقط برای همان Source/Destination، (۳) با تاریخ بازبینی، (۴) با صاحب ثبت کنید.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| ترتیب فعال‌سازی | Web/DNS → AV → App → IPS → Deep |
| چه چیزی را Log کنیم | Deny + رویداد UTM؛ نه همه‌ی Allow |
| مدل فایروال | Throughput با UTM فعال، نه عدد Datasheet خام |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Baseline 900 Mbps و CPU 12٪؛ با Web Filter 880 Mbps و CPU 20٪؛ اثر کم.

**متوسط:** با IPS: 420 Mbps، CPU 85٪. تحلیل: IPS روی همه‌ی ترافیک. اقدام: Sensor انتخابی (Target=Server) و Monitor برای بقیه؛ اندازه‌گیری مجدد: 760 Mbps.

**سخت:** کاربران گزارش می‌دهند «بعضی سایت‌ها لود نمی‌شود» پس از Deep Inspection. شواهد: Capture: TLS Alert unknown_ca فقط برای چند برنامه؛ Log: Certificate error. علت: Pinning. رفع: Exemption آن FQDN؛ آزمون منفی: برنامه‌های دیگر هنوز Inspect می‌شوند.

### ۶) پیاده‌سازی از مسیر GUI

1. Dashboard → Performance (CPU/Memory/Sessions).
2. FortiView → Sources/Destinations.
3. Log & Report → Security Events.
4. Policy → ستون Security Profiles برای مقایسه.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get system performance status
diagnose sys top 2 20
diagnose sys session stat
```

### ۸) Verification (اثبات صحت)

- جدول Baseline/اثر هر Profile با اعداد واقعی.
- آزمون مثبت/منفی Exception.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| CPU بالا | `diagnose sys top` | Profile گسترده؛ Flow/Proxy؛ Deep |
| FP | Log (Signature ID) | Exception دقیق |
| برنامه خطا می‌دهد | Capture: TLS Alert | Pinning؛ Exemption |

### ۱۰) نکات امنیتی

- Exception بدون تاریخ بازبینی ممنوع.
- Profile را بر اساس ریسک، نه همه‌جا.

### ۱۱) جمع‌بندی مفهومی

- Baseline → یک Profile در هر زمان → مقایسه.
- Exception دقیق و مستند.
- عدد Datasheet برای انتخاب مدل کافی نیست.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا هر بار فقط یک Profile اضافه می‌کنیم؟ *(پاسخ: 16-6-ت1)*

**ت2.** (متوسط) Offload IPS را چگونه محدود می‌کند؟ *(پاسخ: 16-6-ت2)*

**ت3.** (سخت) جدول اثر برای ۴ Profile طراحی کنید. *(پاسخ: 16-6-ت3)*

**ت4.** (سخت) آزمون عملی: Web Filter + File Filter + Deep با Exemption را پیاده و ۵ آزمون مثبت/منفی بنویسید. *(پاسخ: 16-6-ت4)*

**ت5.** (سخت، طراحی) Rubric ۱۰۰ نمره‌ای برای آزمون این فصل بنویسید. *(پاسخ: 16-6-ت5)*

**Q1.** Quick quiz (English): Why measure performance with one profile at a time? *(پاسخ: 16-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Baseline | Performance baseline | مرجع عملکرد عادی |
| iperf | iperf | ابزار اندازه‌گیری Throughput |
| Exception | Exception rule | استثنای کنترل‌شده |

- *Measure before and after enabling each profile.* ← قبل و بعد از فعال‌سازی هر Profile اندازه بگیرید.

### ۱۴) کارت Lab

**Lab:** آزمون UTM. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/utm-perf.md`. **Rollback:** حذف Profile از Policy.

### ۱۵) منابع

- Fortinet Docs: FortiOS 7.0 — Performance، Inspection modes؛ iperf3 documentation.

### تعمیق: اندازه‌گیری هزینه‌ی UTM

**روش:** Baseline بدون UTM ⇒ فعال‌سازی هر Profile به‌تنهایی ⇒ ثبت CPU و Throughput.

``` text
diagnose sys top 2 20
get system performance status
iperf3 -c 10.20.0.10 -P 8 -t 30
```

| حالت | Throughput | CPU |
|---|---|---|
| Baseline | مرجع | مرجع |
| +AV | کمتر | بیشتر |
| +IPS | کمتر | بیشتر |
| +SSL Inspection | کمترین | بیشترین |

(اعداد را از Lab خودتان ثبت کنید؛ هیچ عددی ثابت نیست.)

**قاعده‌ی ظرفیت:** مقدار SSL Inspection را بر درصد ترافیک رمزشده (امروز ~۹۰٪) حساب کنید.

**پرسش‌های مصاحبه**
1. *چرا یکی‌یکی؟* تأثیر هر Profile جدا.
2. *Offload NPU با UTM؟* کاهش می‌یابد.
3. *بهینه‌سازی؟* Profile فقط روی Policyهای لازم.

### تکمیل عمیق: اندازه‌گیری هزینه‌ی UTM

#### چرا؟

«UTM کند می‌کند» جمله‌ای است که بدون عدد معنایی ندارد. باید بدانید هر Profile چقدر هزینه دارد.

#### روش

1. Baseline بدون UTM.
2. فعال‌کردن یک Profile و اندازه‌گیری.
3. افزودن بعدی.
4. ثبت CPU و Throughput.

``` text
diagnose sys top 2 20
get system performance status
iperf3 -c 10.20.0.10 -P 8 -t 30
```

#### جدول ثبت

| حالت | Throughput | CPU |
|---|---|---|
| Baseline | ثبت | ثبت |
| +AV | ثبت | ثبت |
| +IPS | ثبت | ثبت |
| +SSL Inspection | ثبت | ثبت |

اعداد را از Lab خودتان بنویسید.

#### محاسبه‌ی افت

``` text
Drop % = (baseline - measured) / baseline x 100
(900 - 600) / 900 x 100 = 33.3 %
```

#### مثال سخت — ظرفیت

اگر ۹۰٪ ترافیک رمز است و Inspection ظرفیت را به ۴۰٪ می‌رساند، برای ۱ Gbps ترافیک به مدلی با Inspection ≥ 1 Gbps نیاز دارید، نه فقط Firewall Throughput.

#### Lab

جدول را در Lab پر کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| افت شدید | Inspection | Exemption/مدل |
| CPU 100٪ | بی‌Offload | Policy |
| عدد ناپایدار | آزمون ضعیف | تکرار |

#### پرسش‌ها با پاسخ

**۱. چرا یکی‌یکی؟** تأثیر جدا.
**۲. افت چگونه؟** درصد.
**۳. دیتاشیت؟** Inspection Throughput.

#### English Corner

- *Measure each security profile's cost separately against a baseline.*
- Q: Why does SSL inspection throughput matter more than firewall throughput?

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

### تعمیق: کارت ۱۰ پرسشی برای Web Filter (نمونه‌ی پر)

| # | پرسش | پاسخ |
|---|---|---|
| 1 | چه می‌بیند؟ | URL/Category HTTP، SNI در HTTPS |
| 2 | چه نمی‌بیند؟ | مسیر کامل HTTPS بدون Inspection |
| 3 | لایسنس؟ | Category: بله؛ Static: خیر |
| 4 | Inspection لازم؟ | برای URL کامل بله |
| 5 | هزینه؟ | کم تا متوسط |
| 6 | Bypass؟ | DoH، VPN، IP مستقیم |
| 7 | Log؟ | utmaction، catdesc |
| 8 | آزمون مثبت؟ | سایت Category مسدود |
| 9 | آزمون منفی؟ | سایت مجاز باز می‌شود |
| 10 | وضعیت | تأیید مستندی؛ اجرا نشده |

همین قالب برای هر Profile تکمیل شود.

**پرسش‌های مصاحبه**
1. *چرا ستون «چه نمی‌بیند»؟* جلوگیری از اعتماد کاذب.
2. *Bypass چرا؟* طراحی دفاع چندلایه.
3. *وضعیت اجرا؟* صادقانه ثبت.

### تکمیل عمیق: کارت ده‌پرسشی — نمونه‌ی پر برای IPS و DNS Filter

#### چرا؟

هر قابلیت امنیتی باید یک «کارت» داشته باشد تا بدانید دقیقاً چه کاری می‌کند و چه کاری نمی‌کند.

#### کارت IPS

| # | پرسش | پاسخ |
|---|---|---|
| 1 | چه می‌بیند؟ | الگوهای حمله در بسته/جریان |
| 2 | چه نمی‌بیند؟ | ترافیک رمز بدون Inspection |
| 3 | لایسنس؟ | امضای به‌روز: بله |
| 4 | Inspection لازم؟ | برای ترافیک رمز بله |
| 5 | هزینه؟ | متوسط تا زیاد |
| 6 | Bypass؟ | Tunnel رمز/Fragmentation |
| 7 | Log؟ | attack, severity |
| 8 | آزمون مثبت؟ | الگوی تست |
| 9 | آزمون منفی؟ | ترافیک عادی عبور |
| 10 | وضعیت | تأیید مستندی؛ اجرا نشده |

#### کارت DNS Filter

| # | پرسش | پاسخ |
|---|---|---|
| 1 | چه می‌بیند؟ | پرس‌وجوی DNS |
| 2 | چه نمی‌بیند؟ | DoH/IP مستقیم |
| 3 | لایسنس؟ | Category: بله |
| 4 | Inspection؟ | خیر |
| 5 | هزینه؟ | کم |
| 6 | Bypass؟ | DoH |
| 7 | Log؟ | domain, action |
| 8-10 | مثبت/منفی/وضعیت | مانند بالا |

#### مثال سخت — استفاده در تصمیم

مدیر می‌پرسد «چرا بدون DoH Block فقط DNS Filter کافی نیست؟». کارت ستون Bypass پاسخ می‌دهد.

#### Lab

کارت‌های Web Filter، AV، App Control را بنویسید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| کارت ناقص | خلأ دانش | مستند |
| Bypass نادیده | ساده‌انگاری | ستون 6 |
| وضعیت نادرست | ادعا | صداقت |

#### پرسش‌ها با پاسخ

**۱. چرا ستون Bypass؟** اعتماد کاذب.
**۲. وضعیت؟** اجرا شده/مستندی.
**۳. کارت برای هر قابلیت؟** بله.

#### English Corner

- *Document what each security feature cannot see as well as what it can.*
- Q: Which bypass techniques affect DNS filtering?

## پاسخ‌های فصل 16

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی درس 16-1

**16-1-ت1** — بعد از Policy lookup و قبل از SNAT؛ فقط برای ترافیک Accept‌شده.

Security Profile پس از Policy lookup و پیش از SNAT روی ترافیک Accept‌شده اعمال می‌شود؛ ترافیک Deny‌شده هرگز بازرسی نمی‌شود. پس بدون Policy مجاز، Profile اثری ندارد.

**16-1-ت2** — File Filter، SSL Inspection، Static URL، DoS Policy، Custom IPS.

زیرمجموعه‌ی Security Profile: File Filter، SSL Inspection، Static URL، DoS Policy و Custom IPS؛ هر کدام لایسنس یا شرط جدا دارد (Needs-License برای FortiGuard).

**16-1-ت3** — باید به Policy وصل، لایسنس معتبر و رفتار با Log اثبات شود.

برای ادعای «فعال است»: Profile به Policy وصل، لایسنس معتبر (`diagnose autoupdate versions`) و رفتار با Log (بلاک/اجازه) اثبات شود.

**16-1-ت4** — برای هر ردیف: خروجی `fortiguard-service status`، `show firewall policy`، و Log آزمون؛ ردیف بدون شاهد «اجرا نشده».

**16-1-ت5** — File Filter، Deep Inspection با Exemption، AV، IPS، Web/DNS Filter، EDR و Patch؛ FN باقی‌مانده را مستند کنید.

**16-1-Q1** — Because it must be attached to a policy, backed by a valid license/database, and verified by logs.

### پاسخ‌های بازنویسی درس 16-2

**16-2-ت1** — Static دستی و بدون لایسنس؛ Category بر پایه‌ی رتبه‌بندی FortiGuard (Needs-License).

**16-2-ت2** — Exempt مقصد را از بقیه‌ی بررسی‌های Web Filter معاف می‌کند.

Exempt مقصد را از بقیه‌ی بررسی‌های Web Filter معاف می‌کند (مثلاً وب‌سایت بانک)؛ باید با دقت استفاده شود تا سوراخ امنیتی نسازد.

**16-2-ت3** — مسیر URL داخل HTTPS رمزشده است؛ فقط با رمزگشایی (Deep) دیده می‌شود.

در HTTPS مسیر URL رمزشده است و فقط با رمزگشایی (Deep Inspection) دیده می‌شود؛ بدون آن فقط SNI/دامنه قابل‌رؤیت است.

**16-2-ت4** — DoH/DoT و IP مستقیم دور می‌زنند.

DoH/DoT و دسترسی مستقیم با IP، Web Filter مبتنی بر DNS/نام را دور می‌زنند؛ باید DoH را کنترل و Application Control اعمال کرد.

**16-2-ت5** — Profile وصل نیست؛ Policy دیگر بالاتر؛ HTTPS و نیاز مسیر؛ QUIC؛ DoH؛ Exempt. شاهد: Debug Flow، Log، Capture.

**16-2-ت6** — کارمند: Category+Static+Deep با Exemption؛ مهمان: سخت‌گیرانه با Safe Search؛ سرور: فقط FQDN مجاز Update.

**16-2-Q1** — It exempts the matching destination from the remaining web filter checks.


### پاسخ‌های بازنویسی درس 16-3

**16-3-ت1** — فایل تست استاندارد بی‌خطر که ضدویروس‌ها آن را ویروس تست می‌شناسند.

فایل EICAR تست استاندارد بی‌خطر است که همه‌ی ضدویروس‌ها آن را ویروس شناسایی می‌کنند؛ برای آزمون AV بدون خطر.

**16-3-ت2** — Zero-day، آرشیو رمزدار، HTTPS بدون Deep و فایل بزرگ‌تر از سقف.

AV نمی‌بیند: Zero-day، آرشیو رمزدار، HTTPS بدون Deep Inspection و فایل بزرگ‌تر از سقف اسکن.

**16-3-ت3** — Flow در جریان و سبک؛ Proxy فایل را کامل بازسازی می‌کند و دقیق‌تر ولی سنگین‌تر است.

**16-3-ت4** — فایل بزرگ‌تر از سقف اسکن نمی‌شود و ممکن است عبور کند.

فایل بزرگ‌تر از سقف اسکن (oversize) اسکن نمی‌شود و بسته به تنظیم ممکن است عبور کند؛ سقف را با ریسک تنظیم و Log کنید.

**16-3-ت5** — File Filter برای آرشیو رمزدار، Sandbox (لایسنس)، محدودسازی منبع، آموزش کاربر و Monitor.

**16-3-Q1** — Because its contents are encrypted and cannot be read by the scanner.


### پاسخ‌های بازنویسی درس 16-4

**16-4-ت1** — IPS بر اساس Signature حمله‌ی شناخته‌شده؛ DoS Policy بر اساس حجم/نرخ غیرعادی.

**16-4-ت2** — بلاک اکسپلویت آسیب‌پذیری تا Patch سرور با Signature IPS.

Virtual Patching: Signature IPS اکسپلویت آسیب‌پذیری را تا زمان Patch واقعی سرور مسدود می‌کند.

**16-4-ت3** — از Baseline حجم عادی؛ آستانه کمی بالاتر از پیک عادی و آزمون با ترافیک واقعی.

**16-4-ت4** — QUIC با TLS1.3 روی UDP قابل Inspection عمیق نیست؛ بلاک آن ترافیک را به TCP/TLS برمی‌گرداند.

**16-4-ت5** — `sys top` فرایند ipsengine، Sensor گسترده؛ رفع: Sensor انتخابی (Target=Server، Severity High+)، Monitor برای بقیه و اندازه‌گیری مجدد.

**16-4-Q1** — To measure false positives before blocking and avoid business disruption.


### پاسخ‌های بازنویسی درس 16-5

**16-5-ت1** — Trust از قبل برقرار است و نصب دستی روی کلاینت‌ها کم می‌شود.

CA سازمانی در دامنه توزیع می‌شود و Trust از قبل برقرار است؛ نصب دستی روی کلاینت‌ها کم می‌شود.

**16-5-ت2** — Firefox Trust Store جدا دارد.

Firefox Trust Store جدا از ویندوز دارد؛ CA باید جدا نصب یا از طریق Policy توزیع شود.

**16-5-ت3** — به کلاینت گواهی ناموثق می‌دهد تا گواهی نامعتبر مقصد دیده شود.

گواهی ناموثق به کلاینت داده می‌شود تا گواهی نامعتبر مقصد دیده شود و کاربر هشدار بگیرد؛ بدون آن مقصد مشکوک مخفی می‌ماند.

**16-5-ت4** — `openssl s_client -connect host:443 -servername host` و مقایسه‌ی Issuer با CA فایروال.

**16-5-ت5** — Exemption برای Finance/Health، Pinned Updaterها، سرورهای داخلی؛ حداقل گستره، مستند و بازبینی دوره‌ای.

**16-5-Q1** — The certificate issuer is the firewall CA instead of the real public CA.


### پاسخ‌های بازنویسی درس 16-6

**16-6-ت1** — تا اثر هر Profile جداگانه دیده شود.

Profile را یکی‌یکی فعال کنید تا اثر هر کدام (CPU، Latency، Block) جدا دیده شود و علت مشکل معلوم باشد.

**16-6-ت2** — بازرسی محتوایی در CPU/CP انجام می‌شود و Session کامل Offload نمی‌شود.

بازرسی محتوایی در CPU/CP انجام می‌شود و Session کامل Offload نمی‌شود؛ بنابراین Throughput کم می‌شود.

**16-6-ت3** — ستون‌ها: Profile، CPU، Throughput، Latency، FP؛ ردیف Baseline و هر Profile و ترکیب؛ شرایط یکسان.

**16-6-ت4** — مثبت: سایت مجاز باز؛ دانلود مجاز؛ منفی: سایت ممنوع Block؛ exe Block؛ سایت Exempt بدون Inspect؛ همه با Log.

**16-6-ت5** — پیکربندی ۳۰، آزمون مثبت/منفی ۳۰، Log و Evidence ۲۰، عیب‌یابی ۱۰، صداقت (Unverified/اجرا نشده) ۱۰.

**16-6-Q1** — To isolate the impact of each profile instead of guessing which one caused the load.

### پاسخ‌های درس افزوده‌ی 16-0 (فصل 16)

**16-0-ت1** — Flow: بازرسی در جریان بدون بازسازی کامل؛ سریع‌تر. Proxy: ختم و بازسازی؛ قابلیت بیشتر و هزینه‌ی بیشتر.

**16-0-ت2** — نام سرور در ClientHello (SNI) که معمولاً رمزنشده است و گواهی.

در TLS رمزنشده‌ی ClientHello نام سرور (SNI) و بعد گواهی دیده می‌شود؛ پایه‌ی Web Filter بدون رمزگشایی.

**16-0-ت3** — فایروال برای کلاینت گواهی جایگزین صادر می‌کند؛ مرورگر فقط اگر CA آن را بپذیرد خطا نمی‌دهد.

**16-0-ت4** — برنامه گواهی مشخصی را انتظار دارد؛ با Deep Inspection خطا می‌دهد؛ راه‌حل Exemption.

**16-0-ت5** — کاربران عادی: Deep + Exemption؛ سرورها: Certificate Inspection؛ بانک/سلامت: Exempt.

**16-0-ت6** — QUIC روی UDP 443 با TLS 1.3 قابل Inspection عمیق نیست؛ مدیریت: بلاک QUIC با Application Control تا به TCP/TLS برگردد.

**16-0-م1** — Detection فقط Log می‌کند؛ Prevention ترافیک را مسدود می‌کند.

Detection فقط Log می‌کند؛ Prevention ترافیک را مسدود می‌کند. شروع با Detection برای سنجش False Positive، بعد Prevention.

**16-0-Q1** — Certificate inspection sees the certificate and SNI; deep inspection additionally sees the decrypted payload.


### پاسخ‌های درس افزوده‌ی 16-7 (فصل 16)

**16-7-ت1** — FP: بی‌خطر به‌اشتباه تهدید؛ FN: تهدید واقعی که دیده نشد.

False Positive: ترافیک بی‌خطر به‌اشتباه تهدید؛ False Negative: تهدید واقعی که دیده نشد. هر دو هزینه دارند؛ تنظیم باید تعادل ایجاد کند.

**16-7-ت2** — دامنه/SNI و اطلاعات گواهی.

فقط دامنه/SNI و اطلاعات گواهی در دسترس است مگر Deep Inspection فعال باشد.

**16-7-ت3** — DoH درخواست DNS را داخل HTTPS رمز می‌کند و فایروال Query را نمی‌بیند.

DoH درخواست DNS را داخل HTTPS رمز می‌کند و فایروال Query را نمی‌بیند؛ لازم است DoH کنترل شود.

**16-7-ت4** — IPS به بازرسی محتوا در CPU/CP نیاز دارد.

IPS به بازرسی محتوا در CPU/CP نیاز دارد و Offload کامل Session ممکن نیست.

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

![شکل: حالت‌های FSSO.](../figures/ch17-l0-fig1.svg)

*شکل: حالت‌های FSSO.*

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

### تعمیق: ردیابی یک ورود کاربر از پایه تا Policy

**جریان LDAP + Group:** کاربر → FortiGate (Captive/VPN) → Bind با حساب سرویس → Search کاربر در Base DN → خواندن memberOf → تطبیق با User Group → Policy.

``` text
Base DN : DC=corp,DC=local
Filter  : (sAMAccountName=ali)
Group   : CN=VPN-Users,OU=Groups,DC=corp,DC=local
```

**Kerberos در FSSO:** DC رویداد 4768/4769 را ثبت می‌کند؛ Collector آن را می‌خواند و IP↔User را به FortiGate می‌دهد.

**پرسش‌های مصاحبه**
1. *چرا حساب سرویس؟* Bind بدون کاربر انسانی.
2. *RADIUS یا LDAP؟* RADIUS برای VPN/Wi-Fi/MFA؛ LDAP برای جستجوی دایرکتوری.
3. *نقطه‌ی شکست؟* DNS، ساعت (Kerberos ±5 دقیقه)، پورت 389/636.

### تکمیل عمیق: AAA و هویت از درون — LDAP، Kerberos، RADIUS، FSSO

#### چرا باید یاد بگیریم؟

Policy بر اساس IP یعنی «این دستگاه» را کنترل می‌کنیم، نه «این انسان» را. کاربر لپ‌تاپش را عوض می‌کند، IP عوض می‌شود و Policy بی‌اثر می‌شود. هویت (Identity) Policy را به «کاربر/گروه» وصل می‌کند: «گروه مالی به ERP دسترسی دارد»، فارغ از IP.

#### AAA

AAA = Authentication (چه کسی هستی؟)، Authorization (چه اجازه‌ای داری؟)، Accounting (چه کردی؟).

#### مثال ساده — چهار مسیر هویت

| روش | کاربرد | منبع حقیقت |
|---|---|---|
| LDAP | جستجوی کاربر/گروه | Active Directory |
| RADIUS | VPN، Wi-Fi، MFA | NPS/FortiAuthenticator |
| Kerberos | SSO در Windows | KDC روی DC |
| FSSO | شناسایی بدون Login جدا | رویدادهای DC |

#### مثال متوسط — جریان LDAP

``` text
1 user submits username/password to FortiGate (portal/VPN)
2 FortiGate binds with service account
3 search (sAMAccountName=ali) under Base DN
4 verify password (bind as user) or compare
5 read memberOf -> match user group -> policy
```

#### مثال سخت — FSSO و Kerberos

کاربر وارد ویندوز می‌شود؛ DC رویداد 4768 (TGT) یا 4624 را ثبت می‌کند؛ Collector آن را می‌خواند و جدول IP↔User را برای FortiGate می‌فرستد. ساعت‌ها باید حداکثر ۵ دقیقه اختلاف داشته باشند (Kerberos).

#### نکته‌ی امنیتی

حساب سرویس LDAP حداقل دسترسی (فقط خواندن)؛ هرگز Domain Admin. ارتباط LDAPS (636) با گواهی معتبر.

#### Lab

نقشه‌ی جریان یک ورود را روی کاغذ بکشید و محل شکست‌های ممکن را علامت بزنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Bind شکست | DN/رمز | بررسی |
| Group match نه | Base DN | تصحیح |
| FSSO خالی | رویداد نمی‌رسد | Collector |

#### پرسش‌ها با پاسخ

**۱. AAA یعنی؟** هویت، مجوز، حسابداری.
**۲. چرا حساب سرویس کم‌دسترسی؟** حمله به Bind.
**۳. FSSO چه فایده؟** Policy کاربری بدون Login اضافه.

#### English Corner

- *Identity-based policies follow the user, not the IP address.*
- Q: Why must the LDAP service account have minimal privileges?

## درس 17-1 — آماده‌سازی Lab هویت: Active Directory، DNS، OU، گروه و حساب سرویس روی Windows Server

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۰، Golden_W2025_Runbook · ≈ 6 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است. دستورهای Windows را شما اجرا می‌کنید؛ رمزها نمونه‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. زیرساخت AD را برای Lab بسازد (Forest/Domain، DNS، OU، گروه، کاربر تست، حساب سرویس).
2. وابستگی‌های FortiGate (DNS، زمان، پورت‌ها) را بشناسد.
3. ساختار OU/گروه را برای Policy هویتی طراحی کند.
4. Snapshot و Rollback را اجرا کند.

### ۲) مفهوم پایه: چیست و چرا؟

FortiGate برای Policy مبتنی بر هویت به یک Directory نیاز دارد. بدون AD تمیز و DNS/ساعت درست، همه‌ی مراحل بعد (LDAP، FSSO، RADIUS) شکست می‌خورند و مشکل در جای اشتباه جست‌وجو می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) طراحی دامنه‌ی Lab

``` text
Domain  : lab.local       DC: DC1 192.168.90.40   DNS: DC1
OU      : Corp -> Users, Groups, ServiceAccounts
Groups  : GRP-FINANCE, GRP-IT, GRP-GUEST
Users   : u.fin1 (Finance), u.it1 (IT), svc-fgt (read-only bind)
Time    : DC is time source (NTP upstream); FortiGate uses same NTP
```

#### ۲) چرا این طراحی؟

- **OU جدا برای ServiceAccounts:** حساب Bind حداقل دسترسی و قابل‌ممیزی.
- **گروه‌ها برای نقش:** Policy روی گروه نوشته می‌شود، نه کاربر.
- **DNS روی DC:** AD بدون DNS درست کار نمی‌کند (SRV records).
- **زمان:** Kerberos به اختلاف زمان حساس است (۱۷-۰).

#### ۳) پورت‌های مورد نیاز (مرور)

LDAP 389/TCP، LDAPS 636/TCP، Kerberos 88/TCP+UDP، DNS 53، RADIUS 1812/UDP (NPS)، FSSO Collector 8000/TCP (۱۷-۰).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| OU/گروه | ساختار نقش‌محور؛ نام‌گذاری استاندارد |
| حساب سرویس | Read-only، رمز قوی، بدون Interactive logon |
| زمان | یک منبع NTP برای DC و FGT |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** PowerShell: ساخت Forest و گروه‌ها؛ تست `Get-ADDomain` و `nslookup lab.local`.

**متوسط:** FortiGate نمی‌تواند DC را resolve کند: DNS فایروال را روی DC1 بگذارید یا Conditional Forward؛ آزمون `execute nslookup`.

**سخت:** LDAP Bind از FGT شکست می‌خورد با پیام invalid credentials: حساب svc-fgt با UPN اشتباه (DN صحیح لازم). اثبات: `ldp.exe` یا `Get-ADUser svc-fgt` برای DN دقیق؛ سپس تست از FGT. درس: DN را از خود AD بخوانید، حدس نزنید.

### ۶) پیاده‌سازی از مسیر GUI

1. Server Manager → Add Roles → Active Directory Domain Services و DNS.
2. Active Directory Users and Computers → ساخت OU/Group/User.
3. DNS Manager → بررسی Zone lab.local.
4. FortiGate: Network → DNS = 192.168.90.40.

### ۷) پیاده‌سازی از مسیر CLI

``` text
# Windows PowerShell on DC1 (lab only; run by the user)
Install-WindowsFeature AD-DS -IncludeManagementTools
Install-ADDSForest -DomainName lab.local -InstallDns
New-ADOrganizationalUnit -Name Corp -Path "DC=lab,DC=local"
New-ADGroup -Name GRP-FINANCE -GroupScope Global -Path "OU=Corp,DC=lab,DC=local"
New-ADUser -Name svc-fgt -SamAccountName svc-fgt -AccountPassword (Read-Host -AsSecureString) -Enabled $true
Get-ADDomain
Get-ADUser svc-fgt | Select DistinguishedName
```

### ۸) Verification (اثبات صحت)

- `nslookup lab.local` از FortiGate و کلاینت.
- `Get-ADUser` DN حساب سرویس.
- Snapshot VM گرفته شده.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| FGT نام DC را نمی‌یابد | `execute nslookup` | DNS فایروال |
| Kerberos خطا | اختلاف زمان | NTP/زمان DC |
| Bind شکست | DN/رمز | DN دقیق از AD |

### ۱۰) نکات امنیتی

- رمزها نمونه و غیر ذخیره‌ای در ریپو.
- حساب سرویس read-only.
- DC را از اینترنت ایزوله نگه دارید.

### ۱۱) جمع‌بندی مفهومی

- AD تمیز + DNS + زمان = پیش‌نیاز هویت.
- DN را از AD بخوانید.
- Snapshot قبل از تغییر.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا DNS روی DC لازم است؟ *(پاسخ: 17-1-ت1)*

**ت2.** (ساده) چرا حساب سرویس جدا؟ *(پاسخ: 17-1-ت2)*

**ت3.** (متوسط) FGT نام DC را resolve نمی‌کند؛ مراحل. *(پاسخ: 17-1-ت3)*

**ت4.** (سخت) طراحی OU/گروه برای ۳ نقش. *(پاسخ: 17-1-ت4)*

**ت5.** (سخت، طراحی) برنامه‌ی Snapshot/Rollback برای Lab AD. *(پاسخ: 17-1-ت5)*

**Q1.** Quick quiz (English): Why must DNS be correct before AD authentication works? *(پاسخ: 17-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| AD DS | Active Directory Domain Services | سرویس Directory |
| OU | Organizational Unit | واحد سازمانی |
| SRV | DNS service record | رکورد سرویس |

- *Use a least-privilege service account for LDAP binds.* ← برای Bind از حساب سرویس با حداقل دسترسی استفاده کنید.

### ۱۴) کارت Lab

**Lab:** DC و کاربران. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ad-lab.md`. **Rollback:** Snapshot.

### ۱۵) منابع

- Microsoft Learn: Active Directory Domain Services Overview.
- `phase0a/Golden_W2025_Runbook.md`.

<a id="l-17-2"></a>

### تعمیق: چک‌لیست Lab و آزمون سلامت AD

``` text
dcdiag /v
repadmin /replsummary
nslookup -type=SRV _ldap._tcp.corp.local
w32tm /query /status
```

نتیجه‌ی مورد انتظار: همه‌ی تست‌های dcdiag `passed`، SRV ریکورد برگردد، ساعت با تفاوت کمتر از ۵ دقیقه.

**ساخت OU/گروه:** `OU=Groups`، گروه `VPN-Users`، حساب `svc-fgt-ldap` با کمترین مجوز (فقط خواندن).

**اشتباهات رایج:** حساب سرویس Domain Admin، DNS داخلی ناقص، ساعت خارج از تلورانس.

**پرسش‌های مصاحبه**
1. *چرا کمترین مجوز؟* حمله به حساب Bind.
2. *LDAPS؟* 636 با گواهی.
3. *مشکل ساعت؟* Kerberos شکست.

### تکمیل عمیق: آماده‌سازی Lab هویت با AD — چک‌لیست سلامت

#### چرا؟

اگر AD ناسالم باشد (DNS خراب، ساعت اشتباه)، هر آزمون هویت شکست می‌خورد و علت را در FortiGate می‌گردید. اول سلامت پایه را بسنجید.

#### آزمون‌های سلامت

``` text
dcdiag /v
repadmin /replsummary
nslookup -type=SRV _ldap._tcp.corp.local
w32tm /query /status
```

انتظار: dcdiag همه Passed، رکورد SRV برگردد، ساعت درست.

#### ساخت ساختار

``` text
OU=Groups ; OU=Service ; OU=Users
Group VPN-Users ; Group FIN-ERP
User svc-fgt-ldap (read-only, password never expires, no interactive logon)
```

#### مثال متوسط — اعطای حداقل دسترسی

حساب `svc-fgt-ldap` را فقط عضو Domain Users نگه دارید؛ خواندن Directory به‌صورت پیش‌فرض برای کاربران معتبر مجاز است.

#### مثال سخت — LDAPS

``` text
openssl s_client -connect dc1.corp.local:636 -showcerts </dev/null
```

گواهی باید با CA مورد اعتماد FortiGate امضا شده باشد؛ وگرنه Bind شکست می‌خورد.

#### Lab

یک AD Lab با دو کاربر و دو گروه بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| SRV نیست | DNS | رفع |
| Kerberos خطا | ساعت | NTP |
| LDAPS شکست | گواهی | CA |

#### پرسش‌ها با پاسخ

**۱. چرا SRV؟** کشف DC.
**۲. چرا NTP؟** Kerberos.
**۳. چرا LDAPS؟** رمزنگاری.

#### English Corner

- *Verify DNS and time before troubleshooting authentication.*
- Q: Why create a dedicated read-only service account?

## درس 17-2 — LDAP در FortiGate و Policy بر اساس گروه: Bind، Search، User Group و آزمون

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۰، ۱۷-۱، ۱۲-۰ · ≈ 7 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سرور LDAP را در FortiGate بسازد (cnid، dn، Bind، LDAPS).
2. User Group با Remote Group (DN کامل) بسازد.
3. Policy گروهی بنویسد و رفتار نگاشت IP→User را بداند.
4. با ابزار تست و Debug مشکل را عیب‌یابی کند.

### ۲) مفهوم پایه: چیست و چرا؟

LDAP به FortiGate می‌گوید «کاربر کیست و عضو کدام گروه است». اما Policy مبتنی بر هویت فقط وقتی کار می‌کند که کاربر **احراز هویت** شده باشد (Captive/FSSO/VPN)؛ خود LDAP فقط منبع تأیید و عضویت است.

### ۳) توضیح عمیق فنی

#### ۱) اجزای تنظیم LDAP

- **Server/Port/Secure:** `ldaps`/636 یا StartTLS.
- **cnid:** ویژگی نام ورود (`sAMAccountName`).
- **dn:** ریشه‌ی جست‌وجو (`dc=lab,dc=local`).
- **Bind:** `regular` با DN و رمز حساب سرویس.
- **Group:** Remote Group با DN کامل گروه.

#### ۲) جریان احراز هویت

``` text
user -> FGT (login)
FGT -> LDAP: bind with svc-fgt, search cnid=user under dn
FGT -> LDAP: bind with found user DN + user password
FGT -> LDAP: read memberOf / match remote group
FGT: allow policy for group
```

#### ۳) نکات

- DN گروه باید دقیق باشد؛ فرق Users container و OU.
- Nested group ممکن است نیاز به تنظیم جداگانه داشته باشد (`Unverified` برای 7.0.3).
- گواهی LDAPS باید معتبر باشد (CA را به FortiGate معرفی کنید).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| LDAP یا LDAPS | LDAPS/StartTLS |
| گروه‌ها | نقش‌محور؛ Nested را آگاهانه |
| Fallback | Captive Portal برای IP بدون هویت |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Test Connectivity موفق و Test User Credentials برای u.fin1 موفق.

**متوسط:** کاربر یافت نمی‌شود: dn روی OU محدود بود؛ تغییر dn به ریشه‌ی دامنه.

**سخت:** کاربر Login می‌کند ولی Policy گروه Finance مطابق نمی‌شود. فرضیه‌ها: DN گروه اشتباه (CN=Finance در OU دیگر)، کاربر عضو مستقیم نیست (Nested)، نگاشت IP→User نیامده، ترتیب Policy. آزمون: `diagnose test authserver`، Group membership در AD، Debug Flow Policy ID.

### ۶) پیاده‌سازی از مسیر GUI

1. User & Authentication → LDAP Servers → Create New (Server، cnid، dn، Bind).
2. Test Connectivity و Test User Credentials.
3. User Groups → Create New → Remote Groups → Add (انتخاب گروه از LDAP).
4. Policy → Source = گروه.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config user ldap
    edit "LDAP-AD"
        set server "192.168.90.40"
        set cnid "sAMAccountName"
        set dn "dc=lab,dc=local"
        set type regular
        set username "CN=svc-fgt,OU=ServiceAccounts,OU=Corp,DC=lab,DC=local"
        set password <SERVICE-ACCOUNT-PASSWORD>
        set secure ldaps
        set port 636
    next
end
config user group
    edit "GRP-FINANCE"
        config match
            edit 1
                set server-name "LDAP-AD"
                set group-name "CN=GRP-FINANCE,OU=Groups,OU=Corp,DC=lab,DC=local"
            next
        end
    next
end
diagnose test authserver ldap LDAP-AD u.fin1 <PASSWORD>
```

### ۸) Verification (اثبات صحت)

- Test Connectivity/Credentials در GUI.
- `diagnose test authserver ldap ...` موفق.
- آزمون مثبت/منفی Policy.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Bind شکست | `diagnose debug application fnbamd -1` | DN/رمز/TLS/پورت |
| User یافت نمی‌شود | Debug | cnid/dn |
| Policy مطابق نمی‌شود | Debug Flow | گروه/نگاشت |

### ۱۰) نکات امنیتی

- LDAPS؛ رمز در ریپو نیست؛ حساب Read-only.

### ۱۱) جمع‌بندی مفهومی

- LDAP منبع احراز و عضویت است؛ Policy هویتی به نگاشت نیاز دارد.
- DN دقیق و TLS.
- آزمون مثبت/منفی.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) cnid چیست؟ *(پاسخ: 17-2-ت1)*

**ت2.** (ساده) چرا LDAPS؟ *(پاسخ: 17-2-ت2)*

**ت3.** (متوسط) کاربر یافت نمی‌شود؛ علت محتمل؟ *(پاسخ: 17-2-ت3)*

**ت4.** (سخت) Policy گروهی مطابق نمی‌شود؛ فرضیه‌ها. *(پاسخ: 17-2-ت4)*

**ت5.** (سخت، طراحی) طرح گروه‌بندی برای ۳ دسترسی. *(پاسخ: 17-2-ت5)*

**Q1.** Quick quiz (English): Which information must an LDAP server entry in FortiGate contain to find a user? *(پاسخ: 17-2-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| cnid | Common name identifier | ویژگی ورود |
| DN | Distinguished Name | نام مسیر |
| LDAPS | LDAP over TLS | LDAP رمزشده |

- *Test the LDAP connection before building policies.* ← قبل از Policy اتصال LDAP را تست کنید.

### ۱۴) کارت Lab

**Lab:** LDAP. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/ldap.md`. **Rollback:** حذف User Group/LDAP.

### ۱۵) منابع

- RFC 4511 (LDAP)؛ Fortinet Docs: FortiOS 7.0 — LDAP servers، User groups.

<a id="l-17-3"></a>

### تعمیق: عیب‌یابی Bind و Group

``` text
config user ldap
 edit "AD"
  set server "10.20.0.5"
  set cnid "sAMAccountName"
  set dn "DC=corp,DC=local"
  set type regular
  set username "CN=svc-fgt-ldap,OU=Service,DC=corp,DC=local"
  set secure ldaps
 next
end
diagnose test authserver ldap AD ali Pass123
```

نتایج: `authenticate 'ali' against 'AD' succeeded` یا خطا. علل رایج خطا: DN اشتباه، گواهی LDAPS نامعتبر، گروه تو در تو (از `memberOf` مستقیم نمی‌آید؛ از Recursive/Group Match استفاده).

**Policy:** `set groups "G-VPN"`؛ آزمون منفی کاربر خارج از گروه ⇒ رد.

**پرسش‌های مصاحبه**
1. *cnid؟* ویژگی نام کاربری.
2. *گروه تو در تو؟* حالت Recursive.
3. *رمز در Log؟* هرگز.

### تکمیل عمیق: LDAP در FortiGate و Policy گروهی

#### چرا؟

یک تنظیم کوچک اشتباه (Base DN، cnid) باعث می‌شود Auth موفق شود ولی Policy مچ نکند.

#### مثال ساده — تعریف سرور

``` text
config user ldap
 edit "AD"
  set server "10.20.0.5"
  set cnid "sAMAccountName"
  set dn "DC=corp,DC=local"
  set type regular
  set username "CN=svc-fgt-ldap,OU=Service,DC=corp,DC=local"
  set password ***
  set secure ldaps
  set port 636
 next
end
```

#### مثال متوسط — گروه و Policy

``` text
config user group
 edit "G-VPN"
  set member "AD"
  config match
   edit 1
    set server-name "AD"
    set group-name "CN=VPN-Users,OU=Groups,DC=corp,DC=local"
   next
  end
 next
end
```

سپس در Policy: `set groups "G-VPN"`.

#### آزمون

``` text
diagnose test authserver ldap AD ali Pass123
```

نتیجه: `authenticate ... succeeded` و گروه‌های کاربر.

#### مثال سخت — گروه تو در تو

کاربر عضو گروه B است و B عضو A. Policy روی A مچ نمی‌کند چون `memberOf` مستقیم است. راه: Recursive Match (`set search-type recursive` یا استفاده از OID `1.2.840.113556.1.4.1941`) در Filter.

#### Lab

یک کاربر را در گروه تو در تو بگذارید و رفتار را مشاهده کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Bind ok، Group نه | DN گروه | تصحیح |
| Auth شکست | رمز | بررسی |
| تو در تو | Recursive | فعال |

#### پرسش‌ها با پاسخ

**۱. cnid؟** ویژگی نام کاربری.
**۲. چرا Recursive؟** گروه تو در تو.
**۳. test authserver؟** تست مستقل از Policy.

#### English Corner

- *Nested groups need a recursive match to be honored by the policy.*
- Q: What does the cnid attribute define?

## درس 17-3 — RADIUS و NPS، احراز هویت چندعاملی (MFA) و Attributeها

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۰، ۱۷-۲ · ≈ 6 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است. MFA به FortiToken/OTP وابسته است (Needs-License/سرویس جداگانه).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. جریان RADIUS (Access-Request/Accept/Reject/Challenge) را شرح دهد.
2. NPS را به‌عنوان RADIUS Server با Client و Policy پیکربندی کند.
3. FortiGate را RADIUS Client کند و تست را بخواند.
4. MFA را با Access-Challenge/OTP مفهومی توضیح دهد.
5. Attributeها (Group/VLAN) را برای Authorization به‌کار ببرد.

### ۲) مفهوم پایه: چیست و چرا؟

RADIUS برای احراز هویت دسترسی راه‌دور/شبکه (VPN، Wi-Fi، Admin) و مدیریت متمرکز است. FortiGate Client است؛ NPS (یا FreeRADIUS) Server. مزیت: سیاست یکجا، Accounting، MFA.

### ۳) توضیح عمیق فنی

#### ۱) جریان

``` text
FGT (client) -> NPS: Access-Request (User-Name, User-Password encrypted with shared secret, NAS-IP)
NPS: check AD + Network Policy
NPS -> FGT: Access-Accept (attributes) | Access-Reject | Access-Challenge (OTP)
FGT: Accounting-Request (1813) optional
```

#### ۲) NPS

- RADIUS Client: IP فایروال + Shared Secret.
- Network Policy: شرط (گروه AD) + روش احراز (PAP/MS-CHAPv2/EAP) + Constraints.
- پورت‌ها 1812/1813 UDP.

#### ۳) امنیت RADIUS

Shared Secret قوی؛ PAP رمز را (با Secret) رمز می‌کند ولی در برابر شنود/جعل ضعیف‌تر از EAP-TLS؛ برای VPN با MFA از Challenge استفاده کنید.

#### ۴) MFA

پس از رمز، سرور OTP می‌خواهد (Access-Challenge)؛ کاربر کد را وارد می‌کند. FortiToken یا OTP خارجی (Needs-License/سرویس).

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| PAP/CHAP/EAP | EAP/MS-CHAPv2 برای VPN؛ PAP فقط با Secret قوی و شبکه‌ی مدیریت |
| Accounting | برای حسابرسی ورود |
| MFA | OTP/Token برای Admin و VPN |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** `diagnose test authserver radius RADIUS-NPS pap u.fin1 <PASSWORD>` ← success.

**متوسط:** Access-Reject: NPS Event Viewer: «policy not matched» چون کاربر در گروه مجاز نیست.

**سخت:** VPN با MFA: کاربر بعد از رمز OTP می‌خواهد ولی GUI FortiClient خطا می‌دهد. بررسی: RADIUS timeout (کوتاه)، Challenge پشتیبانی کلاینت، Secret. اثبات با Sniffer 1812 و NPS Log.

### ۶) پیاده‌سازی از مسیر GUI

1. User & Authentication → RADIUS Servers → Create New (Name، Primary Server، Secret).
2. Test Connectivity/Credentials.
3. NPS: RADIUS Clients → New (IP فایروال، Secret).
4. NPS: Network Policies → شرط Group.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config user radius
    edit "RADIUS-NPS"
        set server "192.168.90.41"
        set secret <RADIUS-SECRET>
        set timeout 10
    next
end
diagnose test authserver radius RADIUS-NPS pap u.fin1 <PASSWORD>
```

### ۸) Verification (اثبات صحت)

- Test موفق؛ NPS Event "granted".
- Sniffer: Access-Request/Accept.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Access-Reject | NPS Event | Secret/Policy/گروه |
| بدون پاسخ | Sniffer 1812 | Client تعریف نشده/Firewall |
| Challenge خطا | Log | Timeout/کلاینت |

### ۱۰) نکات امنیتی

- Secret قوی و یکتا؛ RADIUS را از اینترنت ببندید.

### ۱۱) جمع‌بندی مفهومی

- RADIUS: Request/Accept/Reject/Challenge.
- NPS Client+Policy.
- MFA با Challenge.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) پورت‌های RADIUS؟ *(پاسخ: 17-3-ت1)*

**ت2.** (ساده) Shared Secret چیست؟ *(پاسخ: 17-3-ت2)*

**ت3.** (متوسط) Access-Reject با رمز درست؛ علت؟ *(پاسخ: 17-3-ت3)*

**ت4.** (سخت) VPN با MFA بعد از رمز قطع می‌شود؛ فرضیه‌ها. *(پاسخ: 17-3-ت4)*

**ت5.** (سخت، طراحی) طرح RADIUS برای مدیریت فایروال با MFA. *(پاسخ: 17-3-ت5)*

**Q1.** Quick quiz (English): What does Access-Challenge enable? *(پاسخ: 17-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| NPS | Network Policy Server | سرور RADIUS ویندوز |
| NAS | Network Access Server | دستگاه دسترسی (فایروال) |
| OTP | One-Time Password | رمز یک‌بارمصرف |

- *The shared secret must match on both sides.* ← Secret باید دو سر یکی باشد.

### ۱۴) کارت Lab

**Lab:** RADIUS. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/radius.md`. **Rollback:** حذف RADIUS.

### ۱۵) منابع

- RFC 2865 (RADIUS)؛ Microsoft Learn: NPS.

<a id="l-17-4"></a>

### تعمیق: RADIUS و NPS با MFA

**جریان:** FortiGate (NAS) → NPS (Shared Secret، پورت 1812) → AD → پاسخ Access-Accept + Attribute (Fortinet-Group-Name).

``` text
config user radius
 edit "NPS"
  set server "10.20.0.6"
  set secret ENC ***
  set timeout 10
 next
end
```

MFA: NPS Extension یا FortiAuthenticator/FortiToken (Needs-License). **خطاهای رایج:** Secret ناهمخوان (Log NPS: Event 6273 reason 16)، NAS IP ثبت‌نشده.

**آزمون:** `diagnose test authserver radius NPS pap ali pass`.

**پرسش‌های مصاحبه**
1. *Access-Challenge؟* درخواست OTP.
2. *چرا Timeout بیشتر با MFA؟* زمان واکنش کاربر.
3. *Accounting؟* پورت 1813.

### تکمیل عمیق: RADIUS، NPS و MFA

#### چرا؟

VPN و Wi-Fi معمولاً RADIUS می‌خواهند؛ با NPS (Network Policy Server در ویندوز) و MFA امن‌تر می‌شود.

#### جریان

``` text
FortiGate (NAS) -> Access-Request (UDP 1812) -> NPS -> AD check
NPS -> Access-Accept (+attributes) or Access-Reject
```

نقش‌ها: NAS = Network Access Server (فایروال)، Shared Secret بین NAS و NPS.

#### مثال ساده

``` text
config user radius
 edit "NPS"
  set server "10.20.0.6"
  set secret ***
  set timeout 10
  set nas-ip 10.50.0.1
 next
end
```

#### مثال متوسط — آزمون

``` text
diagnose test authserver radius NPS pap ali pass
```

در NPS لاگ ویندوز Event 6272 (موفق) / 6273 (رد) با Reason Code بخوانید.

#### مثال سخت — MFA

با NPS Extension یا FortiAuthenticator/FortiToken: پس از رمز، RADIUS **Access-Challenge** با درخواست OTP می‌فرستد. Timeout را بیشتر کنید (کاربر وقت می‌خواهد).

#### Attribute

با Attribute می‌توان گروه را برگرداند (مثلاً `Fortinet-Group-Name`) و در Policy استفاده کرد.

#### Lab

NPS را با یک Client و یک Policy بسازید؛ اجرا نشده تا اطلاع بعدی.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Reject (reason 16) | Secret/Credential | یکسان |
| Timeout | پورت/Firewall | 1812 |
| OTP شکست | زمان | NTP |

#### پرسش‌ها با پاسخ

**۱. NAS چیست؟** سرور دسترسی شبکه.
**۲. Access-Challenge؟** درخواست مرحله‌ی بعد.
**۳. Event 6273؟** رد شدن.

#### English Corner

- *RADIUS Access-Challenge carries the second authentication factor.*
- Q: Where do you find the reason a user was rejected on NPS?

## درس 17-4 — FSSO عملی: انتخاب حالت، پیکربندی، Group Filter و عیب‌یابی

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۰، ۱۷-۲ · ≈ 6 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. حالت مناسب FSSO را (DC Agent/Collector/Polling) انتخاب کند.
2. Polling را پیکربندی و کاربران را ببیند.
3. Group Filter و Policy را درست بنویسد.
4. مشکلات NTLM/زمان/Event Log را تشخیص دهد.

### ۲) مفهوم پایه: چیست و چرا؟

FSSO کاربر را بدون Login دوباره به فایروال می‌شناساند. در 7.0، Polling بدون Agent ساده است ولی محدودیت دارد (Kerberos، ورود هم‌زمان)؛ Collector Agent مقیاس‌پذیرتر است.

### ۳) توضیح عمیق فنی

#### ۱) انتخاب حالت

| شرایط | حالت |
|---|---|
| ≤ چند صد کاربر، Kerberos، ساده | FortiGate Polling |
| NTLM یا بار زیاد | Collector Agent/DC Agent |
| Terminal Server | Terminal Server Agent |

#### ۲) تنظیم Polling (طبق مستند 7.0)

پیش‌نیاز: LDAP Server موفق. سپس Security Fabric → External Connectors → FSSO (Poll Active Directory Server) با حساب مجاز خواندن Event Log. `polling-frequency` بین 1 تا 30 ثانیه (پیش‌فرض 10).

#### ۳) Group Filter

فقط کاربران عضو گروه‌های Filter به لیست FSSO می‌روند؛ اگر گروه را نگذارید، کاربر دیده نمی‌شود.

#### ۴) رویدادها

Polling فقط Kerberos 4768/4769 را می‌خواند؛ NTLM پشتیبانی نمی‌شود؛ ورود هم‌زمان زیاد ممکن است ورودی را از دست بدهد.

> **دقت مفهومی (طبق مستند Fortinet):** این محدودیت مربوط به **FortiGate Polling Connector** است. **Collector Agent در حالت Polling** مجموعه‌ی رویداد گسترده‌تری می‌خواند (مثلاً 4768 و 4776 و بسته به تنظیم 4769 و 4624) و NTLM را هم پوشش می‌دهد؛ ولی خودش با NTLM به DCها احراز هویت می‌کند و با Windows Server 2025 گزینه‌ی «Enforce Kerberos» لازم می‌شود. پس برای محیط NTLM-محور Collector/DC Agent مناسب‌تر از FortiGate Polling است. ([مرجع](https://community.fortinet.com/fortigate-3/technical-tip-enforcing-kerberos-instead-of-ntlm-on-fsso-collector-agent-226817))

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| حالت | طبق جدول |
| Fallback | Captive Portal |
| Redundancy | چند Collector (تا ۵ طبق مستند) |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** کاربر u.fin1 به PC Login می‌کند؛ `diagnose debug authd fsso list` او را با IP و گروه نشان می‌دهد.

**متوسط:** کاربر دیده نمی‌شود: گروه در Filter نبود؛ افزودن گروه؛ آزمون.

**سخت:** نیمی از کاربران دیده نمی‌شوند: آن‌ها با NTLM (IP به‌جای نام) به File Server وصل می‌شوند و Kerberos Ticket ندارند. راه‌حل: اصلاح DNS/SPN تا Kerberos استفاده شود یا گذار به Collector Agent.

### ۶) پیاده‌سازی از مسیر GUI

1. User & Authentication → LDAP (از ۱۷-۲).
2. Security Fabric → External Connectors → Create New → FSSO.
3. Poll Active Directory Server: IP، User، Password، LDAP Server.
4. User Groups → FSSO → Members.
5. Policy: Source = گروه FSSO.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config user fsso-polling
    edit 1
        set server "192.168.90.40"
        set ldap-server "LDAP-AD"
        set polling-frequency 10
    next
end
diagnose debug authd fsso list
```

### ۸) Verification (اثبات صحت)

- `fsso list` کاربر و IP.
- Policy Hit و Log با User.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| کاربر نیست | `fsso list` | Group Filter/Kerberos/ساعت |
| IP→User اشتباه | Terminal Server | Agent مخصوص |
| کند/ناقص | Load | Collector |

### ۱۰) نکات امنیتی

- حساب Polling حداقل دسترسی؛ شبکه‌ی مدیریت.

### ۱۱) جمع‌بندی مفهومی

- حالت را با NTLM/بار انتخاب کنید.
- Group Filter الزامی.
- Fallback داشته باشید.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Polling چه رویدادهایی را می‌خواند؟ *(پاسخ: 17-4-ت1)*

**ت2.** (متوسط) کاربر Login کرده ولی دیده نمی‌شود؛ ۳ علت. *(پاسخ: 17-4-ت2)*

**ت3.** (سخت) چرا Terminal Server مشکل‌ساز است؟ *(پاسخ: 17-4-ت3)*

**ت4.** (سخت) Collector یا Polling برای ۲۰۰۰ کاربر با NTLM؟ *(پاسخ: 17-4-ت4)*

**ت5.** (سخت، طراحی) آزمون ۵ مورد FSSO. *(پاسخ: 17-4-ت5)*

**Q1.** Quick quiz (English): Why can FSSO polling miss users who authenticate with NTLM? *(پاسخ: 17-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| FSSO | Fortinet Single Sign-On | ورود یکپارچه |
| DC Agent | Domain controller agent | Agent روی DC |
| Collector | Collector agent | جمع‌کننده |

- *Choose the FSSO mode by authentication protocol and scale.* ← حالت FSSO را بر اساس پروتکل احراز و مقیاس انتخاب کنید.

### ۱۴) کارت Lab

**Lab:** FSSO. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/fsso.md`. **Rollback:** حذف Connector.

### ۱۵) منابع

- [FSSO polling connector agent installation](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/503764/fsso-polling-connector-agent-installation)
- [FSSO](https://docs.fortinet.com/document/fortigate/7.0.8/administration-guide/450337)

<a id="l-17-5"></a>

### تعمیق: FSSO — انتخاب حالت با مثال

| حالت | شرح | کاربرد |
|---|---|---|
| Agent-based DC Agent | روی هر DC نصب | سازمان‌های بزرگ |
| Collector Agent polling | خواندن Event Log | ساده |
| Agentless (Polling) | FortiGate خودش DC را می‌خواند | Lab/کوچک |

**Group Filter:** فقط گروه‌های لازم؛ در غیر این صورت Collector سنگین می‌شود.

``` text
diagnose debug authd fsso list
diagnose debug authd fsso server-status
```

**عیب‌یابی:** IP در جدول نیست ⇒ Event 4768 نمی‌آید یا ساعت/DNS مشکل؛ کاربران NAT‌شده Terminal Server نیاز به TS Agent دارند.

**پرسش‌های مصاحبه**
1. *FSSO چه مشکلی را حل می‌کند؟* Policy بر اساس کاربر بدون Login جدا.
2. *محدودیت؟* IP-مبنا؛ Multi-user در یک IP.
3. *Workstation Check؟* اعتبارسنجی ورود.

### تکمیل عمیق: FSSO — انتخاب حالت و عیب‌یابی

#### چرا؟

کاربر وارد ویندوز می‌شود و انتظار دارد بدون Login دوم از فایروال رد شود. FSSO (Fortinet Single Sign-On) این را ممکن می‌کند.

#### حالت‌ها

| حالت | کار | مناسب |
|---|---|---|
| Collector Agent + DC Agent | نصب روی ویندوز | سازمان‌های بزرگ |
| Agentless (Polling) | FortiGate DC را می‌خواند | Lab/کوچک |

#### مثال ساده — Agentless

``` text
config user fsso-polling
 edit 1
  set server "10.20.0.5"
  set user "corp\\svc-fsso"
  set ldap-server "AD"
 next
end
```

#### مثال متوسط — Group Filter

فقط گروه‌هایی که در Policy لازم‌اند را بخوانید؛ بدون Filter، Collector سنگین و جدول بزرگ می‌شود.

#### بررسی

``` text
diagnose debug authd fsso list
diagnose debug authd fsso server-status
```

#### مثال سخت — Terminal Server

چند کاربر پشت یک IP (RDS/Citrix): FSSO فقط یک کاربر را می‌بیند. راه: TS Agent با تفکیک بر اساس پورت.

#### Lab

FSSO را با یک DC Lab تست کنید و جدول را بخوانید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| کاربر نمی‌آید | Event نمی‌رسد | دسترسی Log |
| گروه ناقص | Filter | تصحیح |
| TS | یک IP | TS Agent |

#### پرسش‌ها با پاسخ

**۱. FSSO چه حل می‌کند؟** Policy کاربری بی‌Login دوم.
**۲. Group Filter؟** سبک‌سازی.
**۳. TS Agent؟** چندکاربره.

#### English Corner

- *FSSO maps IP addresses to users from domain controller events.*
- Q: Why does a terminal server need a dedicated agent?

## درس 17-5 — Captive Portal، مهمان و Firewall Authentication: طراحی ایمن Guest

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۰، ۱۱-۰ · ≈ 6 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده»؛ وابستگی لایسنس هر قابلیت صریح ذکر شده است.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Captive Portal و Firewall Authentication (Policy-level) را مقایسه کند.
2. شبکه‌ی Guest ایزوله با حساب موقت طراحی کند.
3. HTTPS Redirect و گواهی Portal را درست بسازد.
4. Timeout/Re-auth و محدودیت دسترسی را تنظیم کند.

### ۲) مفهوم پایه: چیست و چرا؟

کاربر بدون هویت (مهمان/BYOD) نمی‌تواند با FSSO دیده شود. Captive Portal قبل از دسترسی صفحه‌ی ورود می‌دهد؛ هویت و Policy بر اساس ورود ساخته می‌شود.

### ۳) توضیح عمیق فنی

#### ۱) دو روش

- **Captive Portal روی Interface/Zone:** همه‌ی ترافیک آن شبکه قبل از Login مسدود و به Portal هدایت می‌شود.
- **Authentication در Policy:** فقط ترافیک آن Policy نیازمند Login است.

#### ۲) طراحی Guest

Zone/VLAN جدا (Guest) ← فقط اینترنت (HTTP/HTTPS/DNS) ← بدون دسترسی به داخل ← حساب موقت (زمان‌دار) یا Sponsor ← Log.

#### ۳) HTTPS و گواهی

Redirect HTTPS بدون گواهی معتبر هشدار می‌دهد؛ گواهی Portal معتبر یا CA داخلی. بدون آن کاربر عادت به «ادامه‌ی ناامن» می‌کند.

#### ۴) Timeout

Idle Timeout، Session Timeout و Re-auth؛ برای مهمان کوتاه.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Guest دسترسی | فقط اینترنت؛ Isolation داخلی |
| حساب | موقت/Sponsor |
| Timeout | کوتاه |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** Guest به Portal هدایت می‌شود، با guest1 وارد و اینترنت دارد.

**متوسط:** Portal باز نمی‌شود: allowaccess/Policy DNS؛ کاربر باید DNS را بتواند resolve کند.

**سخت:** Login Loop: گواهی Portal نامعتبر و مرورگر Redirect را رد می‌کند؛ رفع: گواهی معتبر/CA؛ شواهد Capture و Log.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Interfaces → VLAN Guest → Security Mode: Captive Portal.
2. User & Authentication → User Definition → Local User موقت.
3. Policy: Guest→WAN با Web Filter.
4. Log & Report.

### ۷) پیاده‌سازی از مسیر CLI

``` text
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

### ۸) Verification (اثبات صحت)

- Redirect، Login، دسترسی اینترنت، آزمون منفی: Guest→داخل Block.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Portal باز نمی‌شود | Capture | DNS/Policy/گواهی |
| Loop | مرورگر | گواهی |
| Guest به داخل | nmap | Policy گسترده |

### ۱۰) نکات امنیتی

- حساب مهمان زمان‌دار؛ بدون دسترسی داخلی؛ Log.

### ۱۱) جمع‌بندی مفهومی

- Portal برای IP بدون هویت.
- Isolation Guest.
- گواهی معتبر.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) Captive Portal چیست؟ *(پاسخ: 17-5-ت1)*

**ت2.** (متوسط) چرا گواهی Portal مهم است؟ *(پاسخ: 17-5-ت2)*

**ت3.** (سخت) طراحی Guest با ۴ کنترل. *(پاسخ: 17-5-ت3)*

**ت4.** (سخت) Login Loop را عیب‌یابی کنید. *(پاسخ: 17-5-ت4)*

**ت5.** (سخت، طراحی) آزمون منفی Guest. *(پاسخ: 17-5-ت5)*

**Q1.** Quick quiz (English): Why must a guest network be isolated from internal networks? *(پاسخ: 17-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Captive portal | Captive portal | صفحه‌ی ورود قبل از اینترنت |
| Sponsor | Guest sponsor | مسئول تأیید مهمان |
| BYOD | Bring Your Own Device | دستگاه شخصی |

- *Keep guest accounts time-limited and isolated.* ← حساب‌های مهمان زمان‌دار و ایزوله باشند.

### ۱۴) کارت Lab

**Lab:** Captive Portal. **وضعیت:** اجرا نشده. **Evidence:** `03-ops/captive.md`. **Rollback:** `set security-mode none`.

### ۱۵) منابع

- Fortinet Docs: FortiOS 7.0 — Captive portal، Firewall authentication.

<a id="l-17-6"></a>

### تعمیق: طراحی Guest امن

**اصول:** VLAN/Zone جدا، فقط اینترنت، بدون دسترسی داخلی، محدودیت پهنای باند، انقضای حساب.

``` text
Policy GUEST->INTERNET  svc HTTP,HTTPS,DNS  nat  utm  schedule always  captive-portal enable
Policy GUEST->INTERNAL  deny log
```

**آزمون:** Guest به 10.20.0.10 ⇒ Timeout؛ به اینترنت ⇒ پس از Portal باز. **حریم/قانون:** ثبت Log هویت طبق قوانین محلی.

**پرسش‌های مصاحبه**
1. *چرا Portal HTTPS؟* حفاظت رمز.
2. *Client Isolation؟* مهمان‌ها همدیگر را نبینند.
3. *انقضا؟* حساب موقت خودکار.

### تکمیل عمیق: Captive Portal و Guest امن

#### چرا؟

مهمان باید اینترنت داشته باشد ولی به شبکه‌ی داخلی دسترسی نه. Captive Portal هویت را (حتی ساده) ثبت می‌کند.

#### طراحی

``` text
GUEST VLAN -> Policy GUEST->INTERNET (HTTP/HTTPS/DNS, nat, utm, captive-portal)
GUEST -> INTERNAL : deny log
Client isolation, bandwidth limit, account expiry
```

#### مثال ساده — Policy

``` text
config firewall policy
 edit 300
  set name "GUEST-NET"
  set srcintf "port-guest"
  set dstintf "port1"
  set srcaddr "all"
  set dstaddr "all"
  set service "HTTP" "HTTPS" "DNS"
  set action accept
  set nat enable
  set groups "G-GUEST"
  set logtraffic all
 next
end
```

#### مثال متوسط — آزمون

مهمان به 10.20.0.10 ⇒ Timeout؛ به اینترنت ⇒ پس از Portal باز.

#### مثال سخت — حریم و قانون

ثبت هویت و Log مطابق قانون محلی؛ مدت نگهداری، دسترسی و رضایت کاربر را با بخش حقوقی مشخص کنید.

#### Lab

Portal را در Lab با یک حساب مهمان موقت بسازید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Portal نمی‌آید | HTTPS Redirect | Policy |
| دسترسی داخلی | Policy | Deny |
| حساب منقضی نمی‌شود | تنظیم | expiry |

#### پرسش‌ها با پاسخ

**۱. چرا Client isolation؟** مهمان‌ها همدیگر را نبینند.
**۲. چرا Log؟** ردیابی.
**۳. چرا انقضا؟** حساب‌های موقت.

#### English Corner

- *Guest networks must be isolated from internal resources.*
- Q: What controls would you apply to a guest portal?

## درس 17-6 — آزمون عملی هویت و عیب‌یابی Authentication: سه پرونده‌ی واقعی با شواهد، کلید و Rubric

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۰ تا ۱۷-۵، ۱۷-۷، ۱۴-۷ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده) و CSR1000v؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سه سناریوی خرابی Auth (LDAP، FSSO، RADIUS+MFA) را با روش فرضیه‌محور تشخیص و رفع کند.
2. برای هر لایه (شبکه، DNS/ساعت، TLS، Bind، Search، گروه، نگاشت، Policy) شاهد جمع کند.
3. RCA و Evidence Index بنویسد.
4. آزمون مثبت/منفی دسترسی هویتی را اجرا کند.
5. Rubric خودارزیابی را با صداقت (اجرا نشده/Unverified) تکمیل کند.

### ۲) مفهوم پایه: چیست و چرا؟

هویت زنجیره‌ای از حلقه‌هاست: کاربر → فایروال → سرور Auth → Directory → گروه → نگاشت IP→User → Policy. خرابی هر حلقه علامت یکسان («لاگین نمی‌شود» یا «دسترسی ندارم») می‌دهد. این آزمون مهارت جداسازی حلقه‌ی خراب را می‌سنجد.

### ۳) توضیح عمیق فنی

#### ۱) روش

``` text
symptom -> scope(one user / group / all) -> hypotheses by layer -> cheapest evidence -> test -> root cause -> fix -> verify positive+negative -> document
```

نقشه‌ی لایه‌ها: شبکه (ping/Sniffer 389/636/1812/8000) → DNS/ساعت → TLS (گواهی LDAPS) → Bind (حساب سرویس) → Search (cnid/dn) → گروه (DN/Nested) → FSSO/نگاشت → Policy (Source/ترتیب).

#### ۲) سناریوها

**S1 — LDAP:** کاربران Login نمی‌شوند. `diagnose test authserver ldap ...` ⇒ bind error 49 یا Can't contact. علت‌ها (تزریق): DN حساب سرویس غلط / رمز منقضی / پورت 636 بسته.

**S2 — FSSO:** فقط کاربران Mac دیده نمی‌شوند. `diagnose debug authd fsso list` بدون آن‌ها. علت: NTLM/نبود Kerberos یا Group Filter.

**S3 — RADIUS+MFA:** VPN پس از رمز OTP می‌خواهد ولی Reject. علت: Shared Secret/Policy NPS/Timeout کوتاه.

#### ۳) کلید پاسخ (خلاصه)

| S | شواهد | علت | رفع | آزمون |
|---|---|---|---|---|
| S1 | authserver: bind failed؛ NPS/AD event | DN/رمز | DN دقیق از AD، رمز | authserver موفق + Login |
| S2 | fsso list بدون Mac | NTLM/Group Filter | Collector/Captive یا Filter | کاربر در لیست + Policy |
| S3 | NPS Event: policy not matched | گروه/Secret | Policy/Secret | OTP موفق، Reject برای گروه دیگر |

#### ۴) Rubric (۱۰۰)

رفع سه سناریو ۳۰؛ شواهد خام و لایه‌ای ۲۵؛ RCA ۲۰؛ آزمون مثبت/منفی ۱۵؛ صداقت ۱۰.

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**S1 (ساده):** bind error: DN حساب سرویس با `CN=Users` ولی کاربر در OU=ServiceAccounts؛ DN را از `Get-ADUser` بخوانید و اصلاح کنید؛ `authserver` ⇒ success.

**S2 (متوسط):** Mac‌ها با NTLM به File Server وصل‌اند و Kerberos Ticket ندارند؛ Polling فقط Kerberos را می‌خواند. راه‌حل: Collector Agent/DC Agent یا Captive Portal برای Mac؛ آزمون: کاربر Mac در لیست.

**S3 (سخت):** VPN: پس از OTP قطع؛ `Access-Reject`؛ NPS Event: «Network Policy not matched»؛ دلیل: گروه کاربر در شرط Policy نیست؛ رفع؛ آزمون منفی: کاربر خارج از گروه Reject؛ Timeout RADIUS 10 s برای OTP.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose test authserver ldap LDAP-AD <user> <password>
diagnose debug authd fsso list
diagnose test authserver radius RADIUS-NPS pap <user> <password>
diagnose debug application fnbamd -1
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

### ۸) Verification (اثبات صحت)

- Evidence Index: برای هر سناریو شاهد قبل/بعد.
- آزمون مثبت/منفی.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Auth شکست | fnbamd debug | لایه‌ی خراب را با جدول لایه‌ها بیابید |
| Policy مطابق نمی‌شود | Debug Flow | گروه/نگاشت/ترتیب |

### ۱۰) نکات امنیتی

- Debug رمز را آشکار می‌کند؛ پاک‌سازی.
- Evidence بدون Secret.

### ۱۱) جمع‌بندی مفهومی

- روش فرضیه‌محور و لایه‌ای.
- شواهد خام.
- RCA و آزمون مثبت/منفی.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) bind error 49 یعنی چه؟ *(پاسخ: 17-6-ت1)*

**ت2.** (ساده) چرا Debug را Reset می‌کنیم؟ *(پاسخ: 17-6-ت2)*

**ت3.** (متوسط) S2: چرا Mac دیده نمی‌شود؟ *(پاسخ: 17-6-ت3)*

**ت4.** (متوسط) S3: Reject با رمز درست؛ سه علت. *(پاسخ: 17-6-ت4)*

**ت5.** (سخت) RCA کامل S1. *(پاسخ: 17-6-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست ۸ لایه‌ای Auth با آزمون هر لایه. *(پاسخ: 17-6-ت6)*

**Q1.** Quick quiz (English): Which approach finds the failing layer fastest in an authentication problem? *(پاسخ: 17-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Bind | LDAP bind | ورود به Directory |
| Group filter | FSSO group filter | فیلتر گروه‌ها |

- *Test authentication independently of policies first.* ← ابتدا Authentication را جدا از Policy تست کنید.

### ۱۴) کارت Lab

**کارت Lab:** آزمون Auth. **Evidence:** `03-ops/rca-auth.md`.

### ۱۵) منابع

- درس‌های ۱۷-۰ تا ۱۷-۷
- RFC 4511، RFC 2865

### تعمیق: پرونده‌ی «کاربر LDAP وارد می‌شود ولی Policy مچ نمی‌شود»

``` text
diagnose test authserver ldap AD ali pass -> succeeded
diagnose firewall auth list              -> user ali, group (empty)
```

علت: Group Matching غلط (Base DN گروه‌ها یا Group تو در تو). رفع: Group Object صحیح در `config user group` با `match` و Base DN درست؛ آزمون با کاربر دوم.

**Rubric:** تشخیص ۳۰، Evidence ۳۰، رفع ۲۰، آزمون منفی ۱۰، صداقت ۱۰.

**پرسش‌های مصاحبه**
1. *چرا Auth موفق ولی Policy نه؟* Group Mapping.
2. *firewall auth list؟* کاربران فعال.
3. *Timeout Auth؟* `auth-timeout`.

### تکمیل عمیق: آزمون عملی هویت — سه پرونده با Rubric

#### چرا؟

این آزمون سه مشکل واقعی هویت را می‌سنجد.

#### پرونده ۱ — Auth موفق، Policy نه

``` text
diagnose test authserver ldap AD ali pass -> succeeded
diagnose firewall auth list -> user ali, group (none)
```

علت: Group Match اشتباه ⇒ تصحیح `group-name` و آزمون.

#### پرونده ۲ — RADIUS Reject

NPS Event 6273 Reason 16 ⇒ Secret یا Credential؛ Secret یکسان.

#### پرونده ۳ — FSSO خالی

Collector Event نمی‌گیرد ⇒ مجوز خواندن Event Log DC؛ تصحیح.

#### Rubric

``` text
Diagnosis 30 | Evidence 30 | Fix 20 | Negative test 10 | Honesty 10
```

#### مثال سخت — دو علت

پس از رفع Secret، کاربر وصل شد ولی Policy نه: دو علت جدا، یکی‌یکی.

#### Lab

سه پرونده را ایجاد و رفع کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| چندعلتی | هم‌زمان | یکی‌یکی |
| Evidence ناقص | ثبت | الگو |
| Lockout | آزمون زیاد | حساب تست |

#### پرسش‌ها با پاسخ

**۱. firewall auth list؟** کاربران فعال.
**۲. Reason 16؟** Credential/Secret.
**۳. چرا حساب تست؟** جلوگیری از Lockout.

#### English Corner

- *Use a dedicated test account to avoid locking real users.*
- Q: How do you confirm a user is mapped to the right group?

## درس 17-7 — عیب‌یابی Authentication بر اساس شواهد: از Bind تا Policy (LDAP، RADIUS، FSSO)

**فصل 17 · بازنویسی عمیق · پیش‌نیاز: ۱۷-۱ تا ۱۷-۶ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مسیر Authentication (کاربر → FortiGate → Auth Server → گروه → Policy) را مرحله‌به‌مرحله بکشد.
2. با `diagnose test authserver` و Debug fnbamd علت شکست Bind/رمز/گروه را بیابد.
3. خطاهای رایج LDAP (Bind DN، Base DN، Filter، LDAPS)، RADIUS (Shared Secret، NAS-IP) و FSSO را تشخیص دهد.
4. نتیجه را با Event Log اثبات و رفع کند.
5. گزارش RCA با شواهد بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

«کاربر وارد نمی‌شود» از مبهم‌ترین گزارش‌هاست. می‌تواند رمز اشتباه باشد، سرور احراز هویت در دسترس نباشد، کاربر عضو گروه نباشد، یا Policy گروه را نشناسد. اگر زنجیره را نشناسید، ساعت‌ها حدس می‌زنید؛ اگر بشناسید، در پنج دقیقه می‌دانید حلقه‌ی شکسته کجاست.

### ۳) توضیح عمیق فنی

#### ۱) زنجیره‌ی Authentication

``` text
User -> FortiGate (portal / VPN / captive) -> Auth server (LDAP/RADIUS)
   1 reachability (UDP/TCP 389/636/1812)
   2 bind / shared secret
   3 user lookup (Base DN, filter)
   4 password check
   5 group membership returned
   6 firewall policy matches group
```

#### ۲) ابزار

``` text
diagnose test authserver ldap AD-LDAP user01 'Password'
diagnose test authserver radius RAD01 pap user01 'Password'
diagnose debug application fnbamd -1
diagnose debug enable
...
diagnose debug disable
diagnose debug reset
diagnose debug authd fsso list
```

(`Unverified`؛ رمز واقعی در Lab؛ هرگز در گزارش ثبت نشود.)

#### ۳) نگاشت علامت به علت

| علامت / پیام | علت | رفع |
|---|---|---|
| LDAP bind failed / invalid credentials | Bind DN یا رمز سرویس | حساب سرویس |
| user not found | Base DN/Identifier/Filter | `cnid`, `dn` |
| سرور unreachable | Route/Policy/Firewall سرور | UDP/TCP پورت |
| RADIUS Access-Reject | Shared Secret یا کاربر | Secret/NPS |
| لاگین ok ولی دسترسی نه | گروه به Policy وصل نیست | Group در Policy |
| FSSO: کاربر دیده نمی‌شود | Collector Agent/Polling | `fsso list` |

#### ۴) نمونه Debug

``` text
fnbamd: ldap_connect ... 10.20.0.2:636
fnbamd: ldap_bind  result=49 (Invalid credentials)
```

کد 49 یعنی اعتبار Bind نادرست.

#### ۵) روش

ابتدا Reachability، سپس Bind سرویس، سپس کاربر، سپس گروه، سپس Policy. هر گام یک Evidence.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| LDAPS | TLS 636 |
| حساب سرویس | Least privilege |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** `diagnose test authserver ldap AD-LDAP user01 ...` پاسخ موفق همراه گروه‌ها؛ یعنی سرور و Bind سالم است.

**متوسط (گروه):** لاگین موفق ولی دسترسی ندارد. مراحل: ۱) تست authserver: گروه CN=VPN-FIN نیامد. ۲) کاربر عضو نیست. ۳) افزودن عضویت. ۴) تست دوباره ⇒ گروه؛ ۵) Policy hit. پاسخ: عضویت گروه.

**سخت (چندعلتی):** پس از تغییر رمز حساب سرویس، همه‌ی کاربران رد می‌شوند. مراحل: ۱) Debug fnbamd: result=49. ۲) رمز Bind در FortiGate قدیمی. ۳) به‌روزرسانی. ۴) تست. RCA: رمز سرویس بدون CHG تغییر کرد؛ اقدام: Vault و Alert.

### ۶) پیاده‌سازی از مسیر GUI

1. User & Authentication → LDAP Servers → Test Connectivity / Test User Credentials.
2. User Groups → Remote Groups.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose test authserver ldap AD-LDAP user01 Password
diagnose debug application fnbamd -1
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

### ۸) Verification (اثبات صحت)

- Bind OK.
- گروه برگشت.
- Policy hit.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Invalid credentials | Bind | حساب |
| user not found | Base DN | dn/cnid |
| Reject | Secret | Shared secret |

### ۱۰) نکات امنیتی

- LDAPS.
- رمز در Vault.
- Debug را خاموش کنید.

### ۱۱) جمع‌بندی مفهومی

- زنجیره‌ی ۶ گام.
- Debug fnbamd.
- Policy و گروه.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) کد 49 LDAP؟ *(پاسخ: 17-7-ت1)*

**ت2.** (ساده) چرا Test authserver؟ *(پاسخ: 17-7-ت2)*

**ت3.** (متوسط) لاگین موفق ولی دسترسی نه؟ *(پاسخ: 17-7-ت3)*

**ت4.** (متوسط) RADIUS Reject؟ *(پاسخ: 17-7-ت4)*

**ت5.** (سخت) پس از تغییر رمز همه رد می‌شوند. *(پاسخ: 17-7-ت5)*

**ت6.** (سخت، طراحی) چک‌لیست. *(پاسخ: 17-7-ت6)*

**Q1.** Quick quiz (English): What does LDAP result code 49 mean? *(پاسخ: 17-7-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| LDAP | Lightweight Directory Access Protocol | پروتکل دایرکتوری |
| FSSO | Fortinet Single Sign-On | ورود یکپارچه |

- *Test each hop of the authentication chain.* ← هر گام زنجیره‌ی Authentication را آزمون کنید.

### ۱۴) کارت Lab

**کارت Lab:** عیب‌یابی Auth (اجرا نشده). **Evidence:** `03-ops/auth-rca.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: Authentication; LDAP; RADIUS; FSSO

### تعمیق: درخت تصمیم Authentication

``` text
User cannot login
 -> Server reachable? (ping/port 389|1812)   no -> network/firewall
 -> Bind ok? (diagnose test authserver)       no -> DN/secret/cert
 -> User found?                               no -> Base DN/filter
 -> Group matched? (firewall auth list)       no -> group mapping
 -> Policy hit? (iprope lookup/log)           no -> policy order
```

هر شاخه یک Evidence مشخص دارد؛ ثبت زمان و خروجی.

**پرسش‌های مصاحبه**
1. *اول چه؟* دسترسی شبکه به سرور.
2. *چرا Log سرور مقابل؟* دلیل رد (NPS 6273، AD 4625).
3. *Lockout؟* آزمون با حساب تست.

### تکمیل عمیق: درخت تصمیم عیب‌یابی Authentication

#### چرا؟

عیب‌یابی هویت لایه‌لایه است؛ یک درخت تصمیم زمان را کم می‌کند.

#### درخت

``` text
User cannot login
 1 network to auth server? (ping, port 389/636/1812)    no -> network/firewall
 2 bind/secret ok? (diagnose test authserver)           no -> DN/secret/cert
 3 user found?                                          no -> Base DN / filter
 4 group matched? (diagnose firewall auth list)         no -> group mapping
 5 policy hit? (iprope lookup / log)                    no -> policy order
 6 MFA ok?                                              no -> time / token
```

#### مثال ساده

گام ۱: `nc -zv 10.20.0.5 636` ⇒ باز ⇒ گام ۲.

#### مثال متوسط — خواندن Log دو سمت

FortiGate: `diagnose debug application fnbamd -1`؛ سرور: AD Event 4625 (ورود ناموفق).

#### مثال سخت — Lockout

حساب سرویس به‌دلیل رمز اشتباه قفل شد؛ همه‌ی ورودی‌ها شکست. شاهد: Event 4740. رفع: Unlock، رمز صحیح، رمز در Vault.

#### Lab

درخت را روی ۳ خرابی تمرین کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| همه شکست | حساب سرویس | Unlock |
| بعضی شکست | گروه | تصحیح |
| MFA | ساعت | NTP |

#### پرسش‌ها با پاسخ

**۱. اولین گام؟** شبکه به سرور.
**۲. 4740؟** قفل شدن حساب.
**۳. fnbamd؟** Debug Authentication.

#### English Corner

- *Work through authentication problems from the network layer upward.*
- Q: What does Windows event 4740 indicate?

## پاسخ‌های فصل 17

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی درس 17-1

**17-1-ت1** — AD از SRV Record برای یافتن سرویس‌ها استفاده می‌کند.

AD برای یافتن سرویس‌های دامنه (KDC، LDAP) از رکورد SRV در DNS استفاده می‌کند؛ DNS خراب یعنی دامنه خراب.

**17-1-ت2** — حداقل دسترسی و ممیزی‌پذیری.

حساب سرویس باید Least Privilege و ممیزی‌پذیر باشد تا افشای آن آسیب را محدود کند.

**17-1-ت3** — DNS فایروال، `execute nslookup`، Route/Policy Local-out، Sniffer 53.

DNS کار نمی‌کند: DNS فایروال، `execute nslookup`، Route/Policy Local-out و Sniffer روی 53.

**17-1-ت4** — Corp/Users/Groups/ServiceAccounts؛ گروه‌های Finance/IT/Guest؛ Policy بر پایه‌ی گروه.

**17-1-ت5** — Snapshot قبل از Forest، بعد از پایه، قبل از هر تغییر؛ آزمون Restore.

Snapshot: قبل از ساخت Forest، پس از پایه و پیش از هر تغییر؛ و آزمون Restore برای اثبات.

**17-1-Q1** — Because AD clients locate domain services through DNS SRV records.


### پاسخ‌های بازنویسی درس 17-2

**17-2-ت1** — ویژگی نام ورود در Directory (مثل sAMAccountName).

Common Name Identifier (cnid) ویژگی نام ورود در Directory است (مثل sAMAccountName) که FortiGate با آن کاربر را می‌جوید.

**17-2-ت2** — تا رمزها قابل شنود نباشند.

LDAPS رمز و پرس‌وجو را رمز می‌کند؛ LDAP ساده می‌تواند رمزها را قابل شنود کند.

**17-2-ت3** — dn/OU اشتباه یا cnid ناسازگار.

user not found: dn/OU اشتباه یا cnid ناسازگار؛ با `diagnose test authserver ldap` بررسی کنید.

**17-2-ت4** — DN گروه، Nested، نگاشت IP→User، ترتیب Policy؛ آزمون‌ها: authserver، AD، Debug Flow.

**17-2-ت5** — گروه‌ها: Finance (ERP)، IT (مدیریت)، Guest (اینترنت)؛ Policy هر کدام Source=Group.

**17-2-Q1** — The base DN, the common name identifier (cnid) and bind credentials.


### پاسخ‌های بازنویسی درس 17-3

**17-3-ت1** — UDP 1812 و 1813.

RADIUS Authentication روی UDP 1812 و Accounting روی 1813 (برخی پیاده‌سازی قدیمی 1645/1646).

**17-3-ت2** — رمز مشترک Client/Server برای محافظت/اعتبارسنجی.

Shared Secret رمز مشترک FortiGate و RADIUS است که بسته‌ها را اعتبارسنجی/محافظت می‌کند؛ عدم‌تطابق باعث Reject می‌شود.

**17-3-ت3** — Policy NPS/گروه مجاز نیست.

Access-Reject با رمز درست: Policy NPS/گروه مجاز نیست؛ شاهد در Event Log سرور NPS.

**17-3-ت4** — Timeout کوتاه، Challenge پشتیبانی‌نشده، Secret، NPS Policy.

Timeout کوتاه، Challenge پشتیبانی‌نشده، Secret و NPS Policy از علل ناموفق‌بودن MFA هستند.

**17-3-ت5** — Admin remote auth=RADIUS، Challenge OTP، گروه Admin، Accounting، Fallback local admin.

**17-3-Q1** — Additional authentication steps such as one-time passwords.


### پاسخ‌های بازنویسی درس 17-4

**17-4-ت1** — Kerberos 4768/4769.

FSSO Polling فقط رویدادهای Kerberos 4768/4769 را می‌خواند؛ ورود NTLM دیده نمی‌شود.

**17-4-ت2** — Group Filter، NTLM، ساعت/Event Log.

FSSO کاربر را نمی‌بیند: Group Filter، NTLM، ساعت و دسترسی به Event Log را بررسی کنید.

**17-4-ت3** — چند کاربر با یک IP؛ نگاشت یک‌به‌یک ممکن نیست؛ TS Agent.

چند کاربر با یک IP (Terminal Server) نگاشت یک‌به‌یک را ممکن نمی‌کند؛ از TS Agent استفاده کنید.

**17-4-ت4** — Collector/DC Agent؛ Polling محدودیت‌های NTLM و بار دارد.

Collector/DC Agent مدل جایگزین Polling است؛ Polling محدودیت NTLM و بار دارد.

**17-4-ت5** — Login/Logout، تغییر IP، گروه جدید، NTLM، قطع Collector؛ هر کدام Evidence.

آزمون FSSO: Login/Logout، تغییر IP، گروه جدید، NTLM و قطع Collector؛ برای هرکدام Evidence.

**17-4-Q1** — Polling reads only Kerberos events, so NTLM logons are not captured.


### پاسخ‌های بازنویسی درس 17-5

**17-5-ت1** — صفحه‌ی ورود قبل از دسترسی.

Captive Portal قبل از دسترسی صفحه‌ی ورود را نشان می‌دهد؛ برای Guest و BYOD.

**17-5-ت2** — Redirect HTTPS و جلوگیری از عادت کاربر به هشدار.

Redirect باید HTTPS باشد تا کاربر به هشدار گواهی عادت نکند و رمز در متن ساده نرود.

**17-5-ت3** — Zone جدا، Policy حداقلی، حساب موقت، Log و Timeout.

Guest Wi-Fi: Zone جدا، Policy حداقلی (فقط اینترنت)، حساب موقت، Log و Timeout.

**17-5-ت4** — گواهی، Redirect، DNS، Policy.

Captive Portal کار نمی‌کند: گواهی، Redirect، DNS و Policy را بررسی کنید.

**17-5-ت5** — nmap از Guest به Users/Servers باید Filtered باشد.

nmap از Guest به Users/Servers باید Filtered باشد؛ آزمون منفی جداسازی.

**17-5-Q1** — Because guests are untrusted devices and could attack or scan internal systems.


### پاسخ‌های بازنویسی عمیق درس 17-6

**17-6-ت1** — اعتبارنامه‌ی نامعتبر: DN یا رمز حساب/کاربر اشتباه.

اعتبارنامه‌ی نامعتبر: DN یا رمز حساب/کاربر اشتباه؛ Bind را تست کنید.

**17-6-ت2** — بار CPU، حجم Log و افشای اطلاعات حساس.

Debug بار CPU، حجم Log و افشای اطلاعات حساس دارد؛ محدود و موقتی.

**17-6-ت3** — NTLM؛ Polling فقط Kerberos را می‌بیند؛ یا Group Filter.

FSSO کاربر را نمی‌بیند: NTLM (Polling فقط Kerberos)، یا Group Filter.

**17-6-ت4** — Policy NPS/گروه، Secret، Constraint روش احراز؛ شاهد: NPS Event.

RADIUS Reject: Policy NPS/گروه، Secret و Constraint روش احراز؛ شاهد: NPS Event.

**17-6-ت5** — علامت: Login شکست؛ شواهد: bind error؛ علت: DN حساب سرویس؛ رفع: DN دقیق؛ پیشگیری: ثبت DN و تست پس از تغییر OU.

**17-6-ت6** — شبکه، DNS/ساعت، TLS، Bind، Search، گروه، FSSO، Policy؛ برای هرکدام یک دستور/آزمون.

**17-6-Q1** — Testing each layer from the cheapest check upward and recording evidence at every step.

### پاسخ‌های درس افزوده‌ی 17-0 (فصل 17)

**17-0-ت1** — Authentication (کیستی)، Authorization (چه می‌توانی)، Accounting (چه کردی).

Authentication کیستی، Authorization چه می‌توانی و Accounting چه کردی؛ سه رکن AAA.

**17-0-ت2** — LDAP 389؛ LDAPS 636.

LDAP روی TCP 389 و LDAPS روی 636.

**17-0-ت3** — Kerberos به Ticket با Timestamp وابسته است؛ اختلاف زمان زیاد باعث رد Ticket می‌شود.

**17-0-ت4** — فقط Kerberos (4768/4769)؛ NTLM پشتیبانی نمی‌شود؛ در ورود هم‌زمان زیاد ممکن است ورودی از دست برود.

**17-0-ت5** — چند کاربر یک IP دارند و FSSO فقط یک نگاشت IP→User می‌بیند؛ راه‌حل Terminal Server Agent یا Policy IP-based.

**17-0-ت6** — ویندوز: FSSO + LDAP؛ Mac/Linux: Captive Portal/RADIUS یا Policy IP-based؛ MFA برای VPN؛ Fallback و Redundancy.

**17-0-Q1** — The first bind uses a service account to find the user DN; the second bind with the user DN and password verifies the password.


### پاسخ‌های درس افزوده‌ی 17-7 (فصل 17)


### پاسخ‌های بازنویسی عمیق درس 17-7

**17-7-ت1** — اعتبار Bind نامعتبر.

کد 49 LDAP یعنی اعتبار Bind نامعتبر؛ حساب سرویس/رمز را بررسی کنید.

**17-7-ت2** — برای جدا کردن مشکل سرور از Policy.

`diagnose test authserver` مشکل سرور را از مشکل Policy جدا می‌کند.

**17-7-ت3** — گروه در Policy/عضویت.

لاگین موفق ولی دسترسی نه: گروه در Policy یا عضویت گروه.

**17-7-ت4** — Shared Secret/کاربر.

RADIUS Reject: Shared Secret یا کاربر.

**17-7-ت5** — رمز Bind؛ به‌روزرسانی؛ CHG.

پس از تغییر رمز Bind همه رد می‌شوند: رمز را به‌روز کنید و CHG ثبت.

**17-7-ت6** — ۶ گام.

چک‌لیست شش‌گامی: Reachability، Bind، کاربر، رمز، گروه، Policy.

**17-7-Q1** — Invalid credentials.

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

![شکل: مذاکره‌ی IKEv2 و خطاهای رایج.](../figures/ch18-l0-fig1.svg)

*شکل: مذاکره‌ی IKEv2 و خطاهای رایج.*

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

### تعمیق: ردیابی لایه‌ای یک Tunnel که بالا نمی‌آید

**لایه‌ها:** ۱) UDP/500 می‌رسد؟ ۲) Phase1 (IKE_SA) ۳) Phase2 (Child SA/Selector) ۴) Route و Policy ۵) داده.

``` text
diagnose vpn ike gateway list
diagnose vpn tunnel list
get vpn ipsec tunnel summary
```

تفسیر: Gateway بالا ولی Tunnel پایین ⇒ مشکل Selector یا Proposal Phase2؛ هیچ Gateway ⇒ Reachability/PSK/IKE Version.

**قاعده‌ی عددی Rekey:** اگر `keylife` = 43200 ثانیه، Rekey کمی قبل از انقضا آغاز می‌شود؛ ناهمخوانی دو سر معمولاً با کمترین مقدار حل می‌شود.

**پرسش‌های مصاحبه**
1. *Selector ناهمخوان چه نشانه‌ای؟* `no matching selector` / TS_UNACCEPTABLE.
2. *NAT-T چه موقع؟* دستگاه پشت NAT؛ UDP/4500.
3. *PFS؟* کلید جدید برای Phase2.

### تکمیل عمیق: IPsec از درون — IKE، SA، Selector و Rekey با مثال

#### چرا باید یاد بگیریم؟

IPsec را بسیاری با «کپی کردن پیکربندی» برپا می‌کنند و وقتی بالا نیامد، نمی‌دانند از کجا شروع کنند. درک مراحل داخلی، عیب‌یابی را از «حدس» به «خواندن پیام» تبدیل می‌کند.

#### توضیح ساده

IPsec دو مرحله دارد:

1. **IKE SA (Phase 1)**: دو سر یکدیگر را احراز هویت می‌کنند و یک کانال امن برای مذاکره می‌سازند.
2. **Child SA / IPsec SA (Phase 2)**: روی همان کانال، پارامترهای رمزنگاری داده و Selector (چه ترافیکی محافظت شود) توافق می‌شود.

IKE = Internet Key Exchange، یعنی «تبادل کلید اینترنتی». SA = Security Association، یعنی «تفاهم امنیتی» بین دو سر.

#### مثال ساده — لایه‌های عیب‌یابی

``` text
L1 reachability : UDP/500 (and 4500 for NAT-T) reachable?
L2 IKE SA       : diagnose vpn ike gateway list
L3 Child SA     : diagnose vpn tunnel list
L4 route/policy : route to remote subnet + policy both ways
L5 data         : counters enc/dec increase
```

#### مثال متوسط — نشانه‌ها

- Gateway ندارید ⇒ Reachability/PSK/نسخه‌ی IKE.
- Gateway هست ولی Tunnel Down ⇒ Proposal/Selector Phase2.
- Tunnel Up ولی ping نه ⇒ Route/Policy.
- Tunnel Up ولی فقط `enc` افزایش می‌یابد، `dec` نه ⇒ طرف مقابل رمزگشایی نمی‌کند (Policy/Route آن سمت).

#### Rekey

کلیدها محدود زمانی دارند؛ قبل از انقضا کلید جدید ساخته می‌شود تا قطع نشود.

``` text
keylife 43200 s = 12 hours
Rekey margin ~ a few minutes before expiry
```

اگر دو سر Lifetime متفاوت دارند، هرکدام زودتر منقضی شود Rekey را آغاز می‌کند؛ بهتر است یکسان باشند.

#### PFS

Perfect Forward Secrecy یعنی برای هر Child SA، DH جدید انجام شود تا لو رفتن یک کلید، کلیدهای دیگر را لو ندهد.

#### NAT-T

اگر یکی از دو سر پشت NAT باشد، ESP روی UDP/4500 کپسوله می‌شود.

#### مثال سخت — شکست متناوب

Tunnel هر ۸ ساعت یک بار برای چند ثانیه قطع می‌شود: Lifetime Phase1 متفاوت و Rekey Collision. رفع: یکسان‌سازی و فعال‌بودن `auto-negotiate`.

#### Lab

دو FortiGate (یا FGT و CSR) را با Proposal یکسان بسازید و سپس عمداً یک پارامتر را عوض کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| no proposal chosen | رمز | یکسان |
| AUTH_FAILED | PSK/ID | یکسان |
| TS_UNACCEPTABLE | Selector | یکسان |

#### پرسش‌ها با پاسخ

**۱. تفاوت Phase1 و 2؟** هویت/کانال در برابر داده.
**۲. PFS چیست؟** DH جدید برای هر SA.
**۳. NAT-T؟** کپسوله روی UDP/4500.

#### English Corner

- *Phase 1 authenticates the peers; phase 2 negotiates the data protection.*
- Q: What does perfect forward secrecy protect against?

## درس 18-1 — IPsec در عمل: از نیاز تا طراحی — Proposal، شبکه‌ها و برگه‌ی پارامتر

**فصل 18 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۰، ۵-۰ · ≈ 5 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده)؛ دستورها `Unverified`؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. از نیاز کسب‌وکار به «برگه‌ی پارامتر IPsec» برسد.
2. Proposal امن و سازگار انتخاب کند و دلیل بگوید.
3. محدودیت‌های مسیر (NAT، فایروال میانی، MTU) را پیش از پیاده‌سازی بسنجد.
4. معیار پذیرش Tunnel را بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

در فصل ۱۸-۰ مفاهیم را آموختید. این درس همان مفاهیم را به **تصمیم طراحی** تبدیل می‌کند: چه Proposal، چه Selector، چه Route، چه Policy، و چه چیزی باید قبل از شروع بررسی شود.

### ۳) توضیح عمیق فنی

#### ۱) پرسش‌های پیش از طراحی

1. دو سر IP عمومی ثابت دارند یا یکی Dynamic/پشت NAT؟ (Static/Dynamic، NAT-T)
2. چه شبکه‌هایی باید ارتباط داشته باشند؟ Overlap دارند؟ (IP Plan، NAT)
3. مسیر بین دو سر چه فایروال‌هایی دارد؟ UDP 500/4500 و ESP باز است؟
4. چه سرویس‌هایی؟ حجم/Latency؟ (MTU، MSS، Offload)
5. یک مسیر یا Failover؟ (Dual-ISP، SD-WAN)
6. هویت با PSK یا گواهی؟

#### ۲) برگه‌ی پارامتر (قالب)

| پارامتر | مقدار پیشنهادی | دلیل |
|---|---|---|
| IKE | v2 | مدرن‌تر؛ پیش‌فرض 7.0 v1 است و باید صریح تغییر کند |
| Encryption | AES-256-GCM | AEAD |
| Integrity/PRF | SHA-256 | امن |
| DH | 20 (یا ≥ 14) | PFS قوی |
| PFS | Enable | رازداری رو به جلو |
| Lifetime | Phase1 86400، Phase2 43200 (پیش‌فرض‌های 7.0) | هماهنگ دو سر |
| DPD | on-idle/on-demand | کشف مرگ Peer |
| Auth | PSK قوی/گواهی | مقیاس |
| Selector | 0.0.0.0/0 (route-based) | Routing تعیین‌کننده |

#### ۳) معیار پذیرش

IKE SA Established؛ Child SA با شمارنده‌ی دوطرفه؛ ping/TCP بین شبکه‌ها؛ آزمون منفی؛ MTU بدون فرگمنت؛ Failover (در صورت وجود) در زمان هدف.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| PSK یا Cert | Cert برای مقیاس؛ PSK قوی در کوچک |
| Failover | دو Tunnel/دو ISP + SD-WAN (۲۱-۷) |
| Overlap | NAT/Re-IP |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده:** دو شعبه با IP ثابت و بدون NAT: IKEv2، AES-GCM، DH 20، PFS، Route-based، دو Policy.

**متوسط:** یک سر پشت NAT: NAT-T لازم؛ UDP 4500؛ Peer ID/Local ID مشخص.

**سخت:** دو شعبه با Subnet هم‌پوشان 192.168.1.0/24: Route-based مستقیم ممکن نیست. گزینه‌ها: NAT یکطرفه/دوطرفه (VIP/IP Pool)، یا تغییر Addressing. معیار: ریسک، پیچیدگی، Log. راه‌حل: NAT به Subnetهای یکتا در Tunnel و ثبت در IP Plan.

### ۶) پیاده‌سازی از مسیر GUI

1. VPN → IPsec Wizard یا Custom: گام‌ها مطابق ۱۸-۲.

### ۷) پیاده‌سازی از مسیر CLI

``` text
show vpn ipsec phase1-interface
show vpn ipsec phase2-interface
diagnose vpn ike gateway list
```

### ۸) Verification (اثبات صحت)

- برگه‌ی پارامتر امضا‌شده توسط دو سر.
- Pre-check: ping Peer، UDP 500/4500، MTU مسیر.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Pre-check شکست | Sniffer/ping | فایروال میانی/Route |
| Overlap | Route | NAT/Re-IP |

### ۱۰) نکات امنیتی

- الگوریتم ضعیف را حذف کنید.
- PSK در ریپو نیست.

### ۱۱) جمع‌بندی مفهومی

- طراحی پیش از پیکربندی.
- برگه‌ی پارامتر آینه‌ای.
- معیار پذیرش قابل‌آزمایش.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) چرا IKEv2؟ *(پاسخ: 18-1-ت1)*

**ت2.** (متوسط) چرا Pre-check شبکه؟ *(پاسخ: 18-1-ت2)*

**ت3.** (سخت) Overlap 192.168.1.0/24 را چگونه حل می‌کنید؟ *(پاسخ: 18-1-ت3)*

**ت4.** (سخت) برگه‌ی پارامتر برای دو شعبه بنویسید. *(پاسخ: 18-1-ت4)*

**ت5.** (سخت، طراحی) معیار پذیرش Tunnel را ۵ بند بنویسید. *(پاسخ: 18-1-ت5)*

**Q1.** Quick quiz (English): Why prepare a parameter sheet before configuring a tunnel? *(پاسخ: 18-1-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Peer ID | IKE peer identity | هویت همتا |

- *Mirror every parameter on both peers.* ← هر پارامتر را روی هر دو سر آینه کنید.

### ۱۴) کارت Lab

**Lab:** برگه‌ی پارامتر. **Evidence:** `02-design/ipsec-params.md`.

### ۱۵) منابع

- [phase1-interface](https://docs.fortinet.com/document/fortigate/7.0.5/cli-reference/371620/config-vpn-ipsec-phase1-interface)
- RFC 7296

<a id="l-18-2"></a>

### تعمیق: برگه‌ی پارامتر برای دو سر

| پارامتر | سایت A | سایت B |
|---|---|---|
| IKE | v2 | v2 |
| Encryption | AES256 | AES256 |
| Integrity | SHA256 | SHA256 |
| DH Group | 14 | 14 |
| Local Subnet | 10.1.0.0/24 | 10.2.0.0/24 |
| Keylife P1 | 28800 | 28800 |

هر ناهمخوانی در این جدول قبل از کانفیگ پیدا می‌شود. **PSK:** ≥۳۲ نویسه تصادفی، در Vault نه ریپو.

**پرسش‌های مصاحبه**
1. *چرا برگه؟* جلوگیری از Mismatch.
2. *DH 14 چرا؟* حداقل ایمن قابل قبول (۲۰۴۸ بیت).
3. *IKEv1 یا v2؟* v2 ترجیح.

### تکمیل عمیق: طراحی IPsec — برگه‌ی پارامتر دو سر

#### چرا؟

بیشتر «Tunnel بالا نمی‌آید»ها به ناهمخوانی یک پارامتر برمی‌گردد. برگه‌ی طراحی، قبل از دست‌بردن به CLI، ناهمخوانی را آشکار می‌کند.

#### برگه‌ی نمونه

| پارامتر | سایت A | سایت B | هم‌خوان؟ |
|---|---|---|---|
| IKE نسخه | 2 | 2 | بله |
| رمزنگاری | AES256 | AES256 | بله |
| Integrity | SHA256 | SHA256 | بله |
| DH | 14 | 14 | بله |
| Keylife P1 | 28800 | 28800 | بله |
| Local subnet | 10.1.0.0/24 | 10.2.0.0/24 | — |
| PSK | Vault | Vault | بله |

#### مثال ساده — انتخاب پارامتر

AES256 + SHA256 + DH14 (۲۰۴۸ بیت) حداقل مناسب؛ DH 19/20/21 (ECP) سریع‌تر و امن. پارامترهای ضعیف (DES، MD5، DH 1/2/5) را کنار بگذارید.

#### مثال متوسط — PSK

PSK باید تصادفی و بلند باشد (≥ 32 نویسه) و در Vault نگه‌داری شود؛ هرگز در ریپو یا ایمیل.

``` text
openssl rand -base64 32
```

#### مثال سخت — شبکه‌های هم‌پوشان

دو سایت هر دو 192.168.1.0/24 دارند؛ IPsec مسیر مبهم می‌شود. راه: NAT ایستا ۱:۱ روی Tunnel (مثلاً سایت B به 10.222.1.0/24 ترجمه شود) یا Renumber.

#### Lab

برگه را برای دو سایت خودتان پر کنید و با همکار مقابله کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| تونل بالا نمی‌آید | ناهمخوانی | برگه |
| Overlap | IP | NAT/Renumber |
| PSK لو رفت | نگهداری | Rotate |

#### پرسش‌ها با پاسخ

**۱. چرا برگه؟** قبل از CLI ناهمخوانی دیده شود.
**۲. PSK چگونه؟** تصادفی، بلند، Vault.
**۳. Overlap؟** NAT یا Renumber.

#### English Corner

- *Agree on all IKE and IPsec parameters on paper before configuring.*
- Q: How do you build a tunnel between two sites with overlapping subnets?

## درس 18-2 — ساخت Tunnel Site-to-Site بین دو FortiGate: طراحی، GUI، CLI و Verification

**فصل ۱۸ · بازنویسی عمیق · پیش‌نیاز: ۱۸-۰ (IKE، Selector، PFS)، ۱۲-۰، فصل ۵ · ≈ ۷ ساعت**

> **وضعیت (FortiOS 7.0.3):** پیش‌فرض‌ها از CLI Reference 7.0؛ سینتکس `Unverified`؛ PSK نمونه؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

1. برگه‌ی طراحی Tunnel (IP Plan، Proposal، Selector، Route، Policy) را قبل از پیکربندی بنویسد.
2. Tunnel Route-based را با **GUI و CLI** بسازد.
3. سه چیز لازم (Route، Policy، Selector) را جداگانه بسنجد.
4. با `diagnose vpn tunnel list`، Monitor و Ping Verification کند.
5. Rollback و Backup را اجرا کند.

### ۲) برگه‌ی طراحی

``` text
Site A: WAN 203.0.113.1  LAN 192.168.10.0/24   Tunnel if: TO-B
Site B: WAN 203.0.113.2  LAN 192.168.20.0/24   Tunnel if: TO-A
IKE: v2  Proposal: aes256gcm-prfsha256  DH 20  PFS on  DPD on-idle  NAT-T: auto
Phase2 selectors: 0.0.0.0/0 <-> 0.0.0.0/0 (route-based)
Routing: static 192.168.20.0/24 via TO-B (A) and 192.168.10.0/24 via TO-A (B)
Policies: LAN->TO-B accept ; TO-B->LAN accept (both sides)
```

اصل: **دو سر آینه‌ی هم** (Proposal، DH، PFS، Lifetime، PSK، Selector).

### ۳) پیاده‌سازی

**GUI (Site A):**

1. VPN → IPsec Tunnels → Create New → Custom: Name TO-B.
2. Network: Remote Gateway = Static IP 203.0.113.2؛ Interface = wan1؛ NAT Traversal = Enable.
3. Authentication: Method Pre-shared Key؛ IKE Version 2.
4. Phase 1 Proposal: Encryption AES256GCM؛ DH Group 20.
5. Phase 2 Selectors: Local/Remote Address = 0.0.0.0/0؛ Phase 2 Proposal AES256GCM؛ Enable PFS (DH 20).
6. Network → Static Routes → 192.168.20.0/24 → Interface TO-B.
7. Policy & Objects → Firewall Policy: LAN→TO-B و TO-B→LAN (Accept، NAT خاموش).

**CLI (Site A):**

``` text
config vpn ipsec phase1-interface
    edit "TO-B"
        set interface "wan1"
        set ike-version 2
        set remote-gw 203.0.113.2
        set proposal aes256gcm-prfsha256
        set dhgrp 20
        set dpd on-idle
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
config firewall policy
    edit 100
        set name "LAN-to-B"
        set srcintf "port2"
        set dstintf "TO-B"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
    edit 101
        set name "B-to-LAN"
        set srcintf "TO-B"
        set dstintf "port2"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end
```

(در تولید `service ALL` و `all` را محدود کنید؛ اینجا برای Lab اولیه است. سینتکس `Unverified`.) Site B آینه است.

### ۴) Verification (سه سطح)

``` text
get vpn ipsec tunnel summary
diagnose vpn ike gateway list
diagnose vpn tunnel list
execute ping-options source 192.168.10.1
execute ping 192.168.20.1
get router info routing-table details 192.168.20.5
diagnose debug flow filter addr 192.168.20.5
```

- **IKE SA:** Established.
- **Child SA:** Bytes encrypt/decrypt هر دو رشد.
- **داده:** ping کلاینت‌ها؛ Log Policy.

### ۵) مثال‌ها

**ساده:** ping 192.168.10.5 → 192.168.20.5 موفق؛ `tunnel list`: Encrypt/Decrypt افزایش.

**متوسط:** فقط یک‌سو: Bytes out می‌رود، in صفر؛ بررسی Policy B→LAN و Route برگشت در B.

**سخت:** Tunnel پس از ۸ ساعت یک لحظه قطع می‌شود: Rekey؛ بررسی Lifetime دو سر (۱۸-۰)، DPD، PFS Group ناهمسان؛ شاهد: Log VPN.

### ۶) Troubleshooting

| علامت | علت |
|---|---|
| IKE برقرار نمی‌شود | Reachability، Proposal، PSK، ID |
| Phase 2 شکست | Selector/PFS/DH |
| Up ولی ping نه | Route/Policy/NAT-T |
| ping کوچک OK و بزرگ نه | MTU/MSS |

### ۷) نکات امنیتی

- PSK قوی و منحصر؛ در ریپو نیست.
- Policy حداقلی؛ ترافیک Tunnel هم Inspect شود.
- `service ALL` فقط Lab.

### ۸) جمع‌بندی

- برگه‌ی طراحی آینه‌ای.
- Route + Policy + Selector.
- Verification سه‌سطحی.
- Backup قبل از تغییر.

### ۹) تمرین و ارزیابی

**ت1.** (ساده) سه چیز لازم برای ترافیک Tunnel Route-based؟ *(پاسخ: 18-2-ت1)*

**ت2.** (متوسط) چرا Policy دوطرفه لازم است؟ *(پاسخ: 18-2-ت2)*

**ت3.** (متوسط) Verification سه‌سطحی را بنویسید. *(پاسخ: 18-2-ت3)*

**ت4.** (سخت) فقط Bytes out رشد می‌کند؛ فرضیه‌ها و آزمون. *(پاسخ: 18-2-ت4)*

**ت5.** (سخت، طراحی) Policy حداقلی برای دسترسی Site A به یک سرور در Site B. *(پاسخ: 18-2-ت5)*

**Q1.** Quick quiz (English): Which three elements must be correct for route-based VPN traffic to flow? *(پاسخ: 18-2-Q1)*

### ۱۰) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Route-based | Route-based VPN | VPN مبتنی بر Interface و Route |
| Mirror | Mirrored config | پیکربندی آینه‌ای |
| Encrypt/Decrypt counters | SA counters | شمارنده‌ی SA |

- *Both peers must have mirrored proposals and selectors.* ← هر دو Peer باید Proposal و Selector آینه‌ای داشته باشند.

### ۱۱) Lab

**کارت Lab:** Tunnel S2S. **وضعیت:** اجرا نشده. **Verification:** مطابق بخش ۴. **Rollback:** حذف phase2/phase1/Route/Policy. **Evidence:** `03-ops/s2s-a-b.md`.

### ۱۲) منابع

- Fortinet Docs: [config vpn ipsec phase1-interface](https://docs.fortinet.com/document/fortigate/7.0.5/cli-reference/371620/config-vpn-ipsec-phase1-interface)، [phase2-interface](https://docs.fortinet.com/document/fortigate/7.0.0/cli-reference/371620/config-vpn-ipsec-phase2-interface).

<a id="l-18-3"></a>

### تعمیق: ساخت و اثبات Tunnel

``` text
config vpn ipsec phase1-interface
 edit "TO-B"
  set interface port1
  set ike-version 2
  set remote-gw 198.51.100.2
  set proposal aes256-sha256
  set dhgrp 14
  set psk ENC ***
 next
end
config vpn ipsec phase2-interface
 edit "TO-B-P2"
  set phase1name TO-B
  set proposal aes256-sha256
  set src-subnet 10.1.0.0 255.255.255.0
  set dst-subnet 10.2.0.0 255.255.255.0
 next
end
```

سپس Route `10.2.0.0/24 dev TO-B` و Policy دوطرفه (LAN↔TO-B).

**اثبات:** `ping 10.2.0.1 -S 10.1.0.1`؛ `diagnose vpn tunnel list` با شمارنده‌ی `enc/dec pkts` افزایشی.

**پرسش‌های مصاحبه**
1. *چرا Policy دوطرفه؟* Stateful فقط جهت آغاز را می‌شناسد.
2. *Route ناقص؟* ترافیک از Tunnel نمی‌رود.
3. *کانتر صفر؟* ترافیک اصلاً وارد نمی‌شود.

### تکمیل عمیق: ساخت Tunnel Site-to-Site — GUI، CLI و اثبات

#### چرا؟

یک Tunnel وقتی «ساخته شده» است که هم Phase1/2 بالا باشد، هم Route و Policy درست و هم ترافیک عبور کند و شمارنده‌ها افزایش یابند.

#### مراحل

1. Phase1 (Interface-based).
2. Phase2 و Selector.
3. Static Route یا Routing پویا به Interface Tunnel.
4. Policy دوطرفه.
5. آزمون.

#### مثال ساده — CLI

``` text
config vpn ipsec phase1-interface
 edit "TO-B"
  set interface "port1"
  set ike-version 2
  set remote-gw 198.51.100.2
  set proposal aes256-sha256
  set dhgrp 14
  set psk ENC ***
 next
end
config vpn ipsec phase2-interface
 edit "TO-B-P2"
  set phase1name "TO-B"
  set proposal aes256-sha256
  set src-subnet 10.1.0.0 255.255.255.0
  set dst-subnet 10.2.0.0 255.255.255.0
 next
end
config router static
 edit 100
  set dst 10.2.0.0 255.255.255.0
  set device "TO-B"
 next
end
```

#### مثال متوسط — Policy

دو Policy: `LAN -> TO-B` و `TO-B -> LAN`، سرویس و Log مشخص؛ NAT خاموش (ترافیک بین شبکه‌های خصوصی بدون NAT).

#### مثال سخت — اثبات

``` text
diagnose vpn ike gateway list
diagnose vpn tunnel list
execute ping-options source 10.1.0.1
execute ping 10.2.0.1
```

شمارنده‌ی `enc pkts` و `dec pkts` باید افزایش یابد؛ اگر فقط یکی، Policy/Route سمت مقابل را بررسی کنید.

#### Lab

دو FortiGate VM (یا یک FGT و یک CSR) را وصل و اثبات را ثبت کنید (اجرا نشده تا اطلاع بعدی).

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| تونل Up بدون ترافیک | Route | افزودن |
| فقط enc | Policy مقابل | افزودن |
| ping از LAN نه | NAT فعال | غیرفعال |

#### پرسش‌ها با پاسخ

**۱. چرا Policy دوطرفه؟** هر جهت مجوز می‌خواهد.
**۲. NAT چرا خاموش؟** شبکه‌های خصوصی.
**۳. enc بدون dec؟** مشکل سمت مقابل.

#### English Corner

- *If only the encrypted counter increases, check the remote side.*
- Q: Why disable NAT on the tunnel policy?

## درس 18-3 — عیب‌یابی IPsec با Debug IKE: خواندن پیام‌ها و تصمیم‌گیری لایه‌ای

**فصل 18 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۱، ۱۸-۲ · ≈ 11 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید آموزشی؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ FMG/FAZ وابسته به لایسنس (Needs-License).

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. مراحل IKEv2 (SA_INIT، AUTH، CREATE_CHILD_SA) را بشناسد.
2. Debug IKE را محدود و ایمن اجرا کند.
3. پیام‌های رایج (no proposal، AUTHENTICATION_FAILED، TS_UNACCEPTABLE) را تفسیر کند.
4. عیب را به Phase، Proposal، Auth، Selector یا NAT-T نگاشت کند.
5. رفع و Verify را انجام دهد.

### ۲) مفهوم پایه: چیست و چرا؟

تونل بالا نمی‌آید و Debug صدها خط می‌نویسد. بدون دانستن ساختار پیام‌ها، غرق می‌شوید؛ با دانستن، فقط به چند خط کلیدی نگاه می‌کنید: کدام مرحله شکست خورد و چرا.

### ۳) توضیح عمیق فنی

#### ۱) مراحل IKEv2

| تبادل | هدف | شکست رایج |
|---|---|---|
| IKE_SA_INIT | توافق الگوریتم و DH | no proposal chosen |
| IKE_AUTH | احراز هویت و Child SA | AUTHENTICATION_FAILED، TS_UNACCEPTABLE |
| CREATE_CHILD_SA | Rekey | عدم‌تطابق PFS/Lifetime |

#### ۲) Debug محدود

``` text
diagnose vpn ike log-filter clear
diagnose vpn ike log-filter dst-addr4 203.0.113.2
diagnose debug application ike -1
diagnose debug enable
... trigger traffic ...
diagnose debug disable
diagnose debug reset
```

#### ۳) تفسیر

| خط | معنی | اقدام |
|---|---|---|
| `no suitable proposal found` / `NO_PROPOSAL_CHOSEN` | Proposal یا DH متفاوت | یکسان‌سازی |
| `AUTHENTICATION_FAILED` | PSK/هویت متفاوت | PSK، peerid |
| `TS_UNACCEPTABLE` | Selector نامتطابق | Subnet |
| `negotiation timeout` | Reachability/UDP 500/4500 | ACL/NAT |
| `NAT-T` مشکل | UDP 4500 | بازکردن |

#### ۴) وضعیت

``` text
diagnose vpn ike gateway list
diagnose vpn tunnel list
get vpn ipsec tunnel summary
```

#### ۵) درخت تصمیم

Timeout ⇒ Reachability. NO_PROPOSAL ⇒ Proposal/DH. AUTH_FAILED ⇒ PSK/ID. TS_UNACCEPTABLE ⇒ Selector. Up ولی ترافیک نه ⇒ Route/Policy/MTU.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| Debug | فیلتر peer |
| درخت تصمیم | پایین‌به‌بالا |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Debug: NO_PROPOSAL_CHOSEN؛ مقایسه Proposal دو سر؛ یکسان‌سازی؛ Established.

**متوسط (AUTH):** AUTHENTICATION_FAILED. مراحل: PSK دو سر و `peertype`؛ تفاوت یک کاراکتر؛ اصلاح؛ up. درس: PSK را کپی/پیست از Vault.

**سخت (Timeout):** negotiation timeout. مراحل: Sniffer UDP 500/4500: خروج هست، ورود نه؛ ACL ISP/Firewall سایت مقابل؛ رفع؛ تونل up.

### ۷) پیاده‌سازی از مسیر CLI

``` text
diagnose vpn ike log-filter dst-addr4 203.0.113.2
diagnose debug application ike -1
diagnose debug enable
diagnose debug disable
diagnose vpn ike gateway list
```

### ۸) Verification (اثبات صحت)

- Phase 1 و 2 up.
- ping.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| NO_PROPOSAL | Proposal | یکسان |
| AUTH_FAILED | PSK | اصلاح |
| TS_UNACCEPTABLE | Selector | Subnet |
| Timeout | UDP 500/4500 | ACL |

### ۱۰) نکات امنیتی

- PSK در Vault.
- Debug را خاموش کنید.

### ۱۱) جمع‌بندی مفهومی

- IKE سه تبادل.
- خط کلیدی.
- درخت تصمیم.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) IKE_SA_INIT چه می‌کند؟ *(پاسخ: 18-3-ت1)*

**ت2.** (ساده) TS_UNACCEPTABLE؟ *(پاسخ: 18-3-ت2)*

**ت3.** (متوسط) AUTH_FAILED؟ *(پاسخ: 18-3-ت3)*

**ت4.** (متوسط) Timeout؟ *(پاسخ: 18-3-ت4)*

**ت5.** (سخت) Timeout رفع. *(پاسخ: 18-3-ت5)*

**ت6.** (سخت، طراحی) درخت تصمیم. *(پاسخ: 18-3-ت6)*

**Q1.** Quick quiz (English): Which IKEv2 exchange negotiates algorithms and DH? *(پاسخ: 18-3-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| TS | Traffic Selector | انتخابگر ترافیک |

- *Filter the IKE debug to a single peer.* ← Debug IKE را به یک peer محدود کنید.

### ۱۴) کارت Lab

**کارت Lab:** Debug IKE (اجرا نشده). **Evidence:** `03-ops/ike-debug.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: IPsec VPN troubleshooting
- RFC 7296

<a id="l-18-4"></a>

### تعمیق: خواندن Debug IKE

``` text
diagnose vpn ike log filter name TO-B
diagnose debug application ike -1
diagnose debug enable
```

پیام‌های کلیدی:
- `negotiation failure` + `no proposal chosen` ⇒ Proposal ناهمخوان.
- `received notify type AUTHENTICATION_FAILED` ⇒ PSK.
- `TS_UNACCEPTABLE` ⇒ Selector.

پایان: `diagnose debug disable`.

**پرسش‌های مصاحبه**
1. *Debug چه خطری؟* بار CPU و Log زیاد.
2. *فیلتر چرا؟* فقط Peer هدف.
3. *AUTH_FAILED؟* PSK/Identity.

### تکمیل عمیق: Debug IKE — خواندن پیام‌ها

#### چرا؟

پیام‌های Debug IKE دقیقاً می‌گویند چرا مذاکره شکست خورد؛ فقط باید زبانش را بدانید.

#### راه‌اندازی ایمن

``` text
diagnose vpn ike log filter clear
diagnose vpn ike log filter rem-addr4 198.51.100.2
diagnose debug application ike -1
diagnose debug enable
```

فیلتر روی Peer هدف؛ پایان: `diagnose debug disable` و `diagnose debug reset`.

#### جدول پیام‌ها

| پیام | معنی | رفع |
|---|---|---|
| no proposal chosen | Proposal ناهمخوان | یکسان |
| AUTHENTICATION_FAILED | PSK/ID | یکسان |
| TS_UNACCEPTABLE | Selector ناهمخوان | یکسان |
| peer ... not responding | Reachability/Firewall | UDP 500 |
| INVALID_KE_PAYLOAD | DH ناهمخوان | یکسان |

#### مثال ساده

خروجی: `negotiation failure ... no proposal chosen`. فوراً Proposal دو سر را مقایسه کنید.

#### مثال متوسط — نبود پاسخ

فقط پیام‌های ارسال بدون دریافت: ISP یا فایروال بین راه UDP/500 را مسدود کرده؛ با Sniffer ببینید.

``` text
diagnose sniffer packet port1 'host 198.51.100.2 and udp port 500' 4 10 l
```

#### مثال سخت — NAT-T

پس از IKE_SA موفق، ESP قطع است: UDP/4500 مسدود. با Sniffer روی 4500 بررسی کنید.

#### Lab

PSK را عمداً متفاوت و پیام AUTH_FAILED را مشاهده کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| Debug سنگین | بی‌فیلتر | فیلتر |
| پیام نمی‌آید | Reachability | Sniffer |
| ESP قطع | 4500 | باز کردن |

#### پرسش‌ها با پاسخ

**۱. چرا فیلتر؟** CPU.
**۲. TS_UNACCEPTABLE؟** Selector.
**۳. NAT-T پورت؟** 4500.

#### English Corner

- *Filter IKE debug to one peer to keep the output readable.*
- Q: What does a no-proposal-chosen error tell you?

## درس 18-4 — MTU/MSS و Fragmentation در Tunnel IPsec: محاسبه‌ی سربار، آزمون DF، PMTUD و تنظیم

**فصل 18 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۰، ۲۸-۲ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده) و CSR1000v؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده».

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. سربار ESP/UDP-encap را برای Cipherهای مختلف تخمین بزند و MTU/MSS را محاسبه کند.
2. با ping DF و Capture MTU مؤثر را اندازه بگیرد.
3. PMTUD و Black hole را توضیح و تشخیص دهد.
4. MSS Clamp و `mtu-override` را تنظیم و اثرشان را اثبات کند.
5. رفتار UDP/ICMP/Fragmentation و DF را در Tunnel تحلیل کند.

### ۲) مفهوم پایه: چیست و چرا؟

کلاسیک‌ترین مشکل VPN: «ping کوچک OK، دانلود بزرگ قفل». علت MTU است. باید بتوانید **محاسبه، آزمون، رفع و اثبات** کنید.

### ۳) توضیح عمیق فنی

#### ۱) سربار

``` text
Outer IP header                20 B
[UDP encap (NAT-T)]             8 B   (+ non-ESP marker 4 B in some cases)
ESP header (SPI+Seq)            8 B
IV (cipher dependent)       8-16 B    (AES-GCM: 8 B IV)
ESP trailer (pad+len+next)  2+pad B
ICV (auth tag)             16 B (GCM) / 12-32 B (HMAC-SHA)
```

مجموع تقریبی: AES-GCM بدون NAT-T حدود 50–56 B؛ با NAT-T حدود 58–66 B؛ CBC+SHA-256 تا 70+ B.

``` text
Effective MTU ~= link MTU - overhead      (1500 - 60 = 1440 typical)
MSS = effective MTU - 40  (IP 20 + TCP 20) -> ~1400
```

(اعداد تقریبی؛ با آزمون واقعی تأیید کنید.)

#### ۲) آزمون

``` text
Linux : ping -M do -s 1372 10.2.0.5       (1372+28 = 1400)
Windows: ping -f -l 1372 10.2.0.5
```

اندازه را تا اولین موفقیت کم کنید؛ MTU مؤثر = اندازه + 28.

#### ۳) PMTUD

فرستنده بسته‌ی بزرگ با DF=1 می‌فرستد؛ روتر میانی که MTU کوچک‌تر دارد، ICMP «Fragmentation Needed (Type 3 Code 4)» برمی‌گرداند. اگر ICMP بلاک شود، فرستنده نمی‌فهمد ⇒ **Black hole** (قفل). رفع: اجازه‌ی ICMP 3/4، یا MSS Clamp که TCP را از ابتدا کوچک می‌کند.

#### ۴) FortiGate

``` text
config system interface
    edit "TO-B"
        set mtu-override enable
        set mtu 1400
    next
end
config firewall policy
    edit 100
        set tcp-mss-sender 1360
        set tcp-mss-receiver 1360
    next
end
```

(`Unverified`.) فرگمنت‌شدن: `ip-fragmentation` در Phase1 (`Unverified`)؛ Fragmentation افت کارایی دارد.

#### ۵) UDP و غیر TCP

MSS Clamp فقط TCP را حل می‌کند. UDP بزرگ (DNS، VoIP، QUIC) به MTU/Fragmentation حساس است؛ راه: MTU Tunnel پایین‌تر، برنامه با اندازه‌ی کوچک، یا اجازه‌ی Fragmentation.

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| MSS Clamp | 1360 (یا محاسبه) |
| MTU Tunnel | 1400 |
| ICMP | Type 3/4 باز |
| Fragmentation | اجتناب |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** ping DF 1472 شکست، 1372 موفق ⇒ MTU مؤثر 1400؛ MSS 1360.

**متوسط (تحلیل):** دانلود 1 MB می‌ایستد؛ Capture: Retransmission بسته‌های 1500 B؛ هیچ ICMP 3/4. تحلیل: Black hole؛ رفع: MSS Clamp + اجازه‌ی ICMP؛ تأیید: دانلود کامل.

**سخت (چند پروتکل):** پس از Clamp، وب OK ولی DNS روی TCP/UDP بزرگ و VoIP مشکل دارند. تحلیل: UDP MSS ندارد؛ باید MTU Tunnel کمتر (1360) یا Fragmentation؛ اندازه‌گیری Loss با ping DF؛ تصمیم: MTU 1400 و آزمون VoIP؛ ثبت.

### ۶) پیاده‌سازی از مسیر GUI

1. Network → Interfaces → Tunnel → MTU.
2. Policy → CLI برای MSS.

### ۷) پیاده‌سازی از مسیر CLI

``` text
config system interface
    edit "TO-B"
        set mtu-override enable
        set mtu 1400
    next
end
config firewall policy
    edit 100
        set tcp-mss-sender 1360
        set tcp-mss-receiver 1360
    next
end
```

### ۸) Verification (اثبات صحت)

- ping DF اندازه‌ها.
- Capture: عدم Retransmission.
- دانلود بزرگ و UDP بزرگ.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| بزرگ قفل | ping DF | MTU/ICMP |
| کند | Capture | Fragmentation |
| فقط UDP | Capture | MTU Tunnel |

### ۱۰) نکات امنیتی

- ICMP را کورکورانه نبندید.

### ۱۱) جمع‌بندی مفهومی

- سربار تقریبی؛ آزمون واقعی.
- MSS برای TCP؛ UDP نیاز MTU.
- PMTUD نیاز ICMP.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) MSS از MTU چگونه محاسبه می‌شود؟ *(پاسخ: 18-4-ت1)*

**ت2.** (ساده) PMTUD Black hole چیست؟ *(پاسخ: 18-4-ت2)*

**ت3.** (متوسط) سربار ESP+UDP با GCM چقدر است؟ *(پاسخ: 18-4-ت3)*

**ت4.** (متوسط) ping DF 1372 موفق/1400 شکست؛ MTU مؤثر؟ *(پاسخ: 18-4-ت4)*

**ت5.** (سخت) چرا MSS Clamp برای UDP کافی نیست؟ *(پاسخ: 18-4-ت5)*

**ت6.** (سخت، طراحی) استاندارد MTU/MSS سازمان. *(پاسخ: 18-4-ت6)*

**Q1.** Quick quiz (English): Why do small pings succeed while large transfers hang when the path MTU is too small? *(پاسخ: 18-4-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| PMTUD | Path MTU Discovery | کشف MTU مسیر |
| DF | Don’t Fragment bit | بیت عدم فرگمنت |
| Black hole | PMTUD black hole | حفره‌ی سیاه PMTUD |

- *Measure the effective MTU with DF-bit pings.* ← MTU مؤثر را با ping و DF-bit اندازه بگیرید.

### ۱۴) کارت Lab

**کارت Lab:** MTU. **Evidence:** `03-ops/mtu.md`.

### ۱۵) منابع

- RFC 1191
- RFC 4821
- RFC 4303 (ESP)

<a id="l-18-5"></a>

### تعمیق: محاسبه‌ی MTU Tunnel

``` text
Link MTU           = 1500
ESP overhead (AES+SHA, tunnel mode) ~ 58-73 bytes
Inner MTU          ~ 1427
TCP MSS            = 1427 - 40 = 1387  (use 1360 for margin)
```

تست: `ping -f -l 1400 10.2.0.1`. رفع: `set tcp-mss` روی Policy یا کاهش MTU Tunnel Interface.

**پرسش‌های مصاحبه**
1. *Fragmentation چرا بد؟* کارایی و Drop.
2. *DF bit؟* ممنوعیت Fragment.
3. *PMTUD Blackhole؟* ICMP مسدود.

### تکمیل عمیق: MTU/MSS در Tunnel — محاسبه و آزمون DF

#### چرا؟

IPsec سربار اضافه می‌کند؛ بسته‌ی ۱۵۰۰ بایتی بعد از کپسوله‌شدن بزرگ‌تر از MTU لینک می‌شود. نتیجه: «سایت باز می‌شود ولی تصاویر نه» یا «ping کار می‌کند ولی HTTPS نه».

#### محاسبه‌ی سربار

``` text
ESP tunnel mode overhead ~ 50-73 bytes (IP 20 + ESP 8 + IV 16 + pad + ICV 12-32)
Link MTU 1500 -> inner MTU ~ 1427 (conservative)
TCP MSS = inner MTU - 40 = ~1387 ; use 1360 for margin
```

عدد دقیق به الگوریتم بستگی دارد؛ همیشه با آزمون اندازه بگیرید.

#### آزمون DF

``` text
ping -f -l 1472 10.2.0.1   (Windows: -f = Don't Fragment)
ping -f -l 1400 10.2.0.1
ping -M do -s 1400 10.2.0.1   (Linux)
```

بزرگ‌ترین اندازه‌ای که جواب می‌دهد + 28 = MTU مسیر.

#### مثال متوسط — رفع با MSS Clamp

``` text
config firewall policy
 edit 100
  set tcp-mss-sender 1360
  set tcp-mss-receiver 1360
 next
end
```

یا کاهش MTU Interface Tunnel: `set mtu 1400` با `mtu-ignore` طبق نیاز.

#### مثال سخت — ICMP مسدود

PMTUD به ICMP «Fragmentation Needed» وابسته است؛ اگر ICMP در مسیر مسدود باشد، فرستنده نمی‌فهمد و Blackhole رخ می‌دهد. رفع: MSS Clamp (چون روی SYN) و باز کردن ICMP Type 3 Code 4.

#### Lab

Path MTU را با ping اندازه بگیرید و MSS را محاسبه کنید.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| HTTPS قطع‌قطع | MTU | Clamp |
| ping بزرگ رد | Fragmentation | MTU Tunnel |
| ICMP مسدود | PMTUD | باز کردن |

#### پرسش‌ها با پاسخ

**۱. MSS از کجا؟** MTU منهای هدرها.
**۲. چرا ping کار می‌کند ولی HTTPS نه؟** اندازه‌ی بسته.
**۳. Clamp روی؟** SYN.

#### English Corner

- *MSS clamping works on the TCP SYN and avoids dependence on PMTUD.*
- Q: How do you find the path MTU with ping?

## درس 18-5 — Interop FGT–CSR: IPsec IKEv2 route-based، نگاشت، Debug دوطرفه و آزمون Rekey

**فصل 18 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۰، ۲۵-۰، ۲۵-۳ · ≈ 8 ساعت**

> **وضعیت:** FortiOS 7.0.3 (بوت‌نشده) و CSR1000v؛ دستورها `Unverified` مگر با لینک؛ Lab «اجرا نشده». CSR دستورها `Unverified`.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. Tunnel IKEv2 FGT–CSR را با Proposal یکسان بسازد.
2. معادل‌های دستور و پیام‌های خطا را نگاشت کند.
3. ناهمسانی Lifetime/PFS/Selector را کشف و رفع کند.
4. Rekey/DPD را آزمایش و گزارش Interop بنویسد.

### ۲) مفهوم پایه: چیست و چرا؟

Interop واقعی نیاز به «برگه‌ی پارامتر مشترک» و «Debug هم‌زمان» دارد (۲۵-۳). این درس ساخت پایه‌ی Tunnel است.

### ۳) توضیح عمیق فنی

#### ۱) برگه

``` text
IKEv2, AES-256-GCM, PRF SHA-256, DH 20, PFS group 20, lifetime P1 86400 / P2 3600, DPD on-idle
Selectors any/any (route-based), PSK <PSK-LAB>, FGT 203.0.113.1  CSR 203.0.113.2, tunnel 10.255.0.0/30
```

#### ۲) CSR

``` text
crypto ikev2 proposal PROP
 encryption aes-gcm-256
 prf sha256
 group 20
crypto ikev2 policy POL
 proposal PROP
crypto ikev2 keyring KR
 peer FGT
  address 203.0.113.1
  pre-shared-key <PSK-LAB>
crypto ikev2 profile PROF
 match identity remote address 203.0.113.1 255.255.255.255
 authentication local pre-share
 authentication remote pre-share
 keyring local KR
crypto ipsec transform-set TS esp-gcm 256
crypto ipsec profile IPS
 set transform-set TS
 set ikev2-profile PROF
 set pfs group20
 set security-association lifetime seconds 3600
interface Tunnel0
 ip address 10.255.0.2 255.255.255.252
 ip mtu 1400
 tunnel source GigabitEthernet1
 tunnel destination 203.0.113.1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile IPS
```

#### ۳) FortiGate

``` text
config vpn ipsec phase1-interface
    edit "TO-CSR"
        set interface "wan1"
        set ike-version 2
        set remote-gw 203.0.113.2
        set proposal aes256gcm-prfsha256
        set dhgrp 20
        set psksecret <PSK-LAB>
    next
end
config vpn ipsec phase2-interface
    edit "TO-CSR-P2"
        set phase1name "TO-CSR"
        set proposal aes256gcm
        set pfs enable
        set dhgrp 20
        set keylifeseconds 3600
        set src-subnet 0.0.0.0 0.0.0.0
        set dst-subnet 0.0.0.0 0.0.0.0
    next
end
```

#### ۴) نگاشت

| | CSR | FGT |
|---|---|---|
| وضعیت | `show crypto ikev2 sa` | `diagnose vpn ike gateway list` |
| Child | `show crypto ipsec sa` | `diagnose vpn tunnel list` |
| Debug | `debug crypto ikev2` | `diagnose debug application ike -1` |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده):** Up؛ ping 10.255.0.1↔.2؛ counters.

**متوسط (تحلیل):** Phase 2 شکست: PFS 19 روی CSR و 20 روی FGT؛ هم‌گروه‌کردن.

**سخت (Rekey):** پس از ۶۰ دقیقه قطع؛ Lifetime CSR 3600 و FGT 43200 و PFS ناهمسان در Rekey؛ یکسان‌سازی؛ آزمون ۴ ساعت.

### ۷) پیاده‌سازی از مسیر CLI

``` text
show crypto ikev2 sa
show crypto ipsec sa
diagnose vpn ike gateway list
diagnose vpn tunnel list
```

### ۸) Verification (اثبات صحت)

- دو سر Up؛ Rekey پایدار.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| Phase1 | Debug | Proposal/PSK |
| Phase2 | Debug | PFS/Selector |
| قطع دوره‌ای | Log | Lifetime |

### ۱۰) نکات امنیتی

- PSK قوی.

### ۱۱) جمع‌بندی مفهومی

- برگه‌ی مشترک؛ Lifetime/PFS؛ Debug دو سر.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) معادل diagnose vpn tunnel list در CSR؟ *(پاسخ: 18-5-ت1)*

**ت2.** (ساده) چرا Selector any/any؟ *(پاسخ: 18-5-ت2)*

**ت3.** (متوسط) PFS ناهمسان چه نشانه‌ای دارد؟ *(پاسخ: 18-5-ت3)*

**ت4.** (متوسط) چرا Lifetime ناهمسان خطرناک است؟ *(پاسخ: 18-5-ت4)*

**ت5.** (سخت) Tunnel هر ساعت قطع؛ تحلیل. *(پاسخ: 18-5-ت5)*

**ت6.** (سخت، طراحی) گزارش Interop. *(پاسخ: 18-5-ت6)*

**Q1.** Quick quiz (English): What is the CSR equivalent of FortiGate "diagnose vpn ike gateway list"? *(پاسخ: 18-5-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| Transform set | IPsec transform set | الگوریتم‌های ESP |

- *Align lifetimes across vendors.* ← Lifetime را بین سازندگان هم‌سان کنید.

### ۱۴) کارت Lab

**کارت Lab:** FGT–CSR. **Evidence:** `03-ops/fgt-csr.md`.

### ۱۵) منابع

- Cisco IKEv2 configuration guide
- RFC 7296

<a id="l-18-6"></a>

### تعمیق: Interop FortiGate–Cisco IKEv2

``` text
crypto ikev2 proposal P1
 encryption aes-cbc-256
 integrity sha256
 group 14
crypto ikev2 keyring KR
 peer FGT
  address 203.0.113.2
  pre-shared-key local ***
```

نقاط ناهمخوانی رایج: Lifetime، شناسه‌ی Local/Remote، Selector (Cisco با ACL، FortiGate با Selector). برای Route-based در Cisco از Tunnel/VTI با `tunnel mode ipsec ipv4`.

**اثبات:** `show crypto ikev2 sa` و `diagnose vpn ike gateway list`.

**پرسش‌های مصاحبه**
1. *چرا Route-based؟* Routing پویا.
2. *Selector 0.0.0.0/0؟* با VTI رایج.
3. *Debug دوطرفه؟* دو سر هم‌زمان.

### تکمیل عمیق: Interop FortiGate–Cisco CSR با IKEv2 Route-based

#### چرا؟

در دنیای واقعی IPsec اغلب بین دو سازنده است. اگر مفهوم را بدانید فقط Syntax عوض می‌شود.

#### پیکربندی Cisco (VTI)

``` text
crypto ikev2 proposal P1
 encryption aes-cbc-256
 integrity sha256
 group 14
crypto ikev2 policy POL1
 proposal P1
crypto ikev2 keyring KR
 peer FGT
  address 203.0.113.2
  pre-shared-key local ***
  pre-shared-key remote ***
crypto ikev2 profile PROF
 match identity remote address 203.0.113.2 255.255.255.255
 authentication remote pre-share
 authentication local pre-share
 keyring local KR
crypto ipsec transform-set TS esp-aes 256 esp-sha256-hmac
 mode tunnel
crypto ipsec profile IPS
 set transform-set TS
 set ikev2-profile PROF
interface Tunnel0
 ip address 10.99.0.2 255.255.255.252
 tunnel source GigabitEthernet1
 tunnel destination 203.0.113.2
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile IPS
```

سمت FortiGate: Phase1/Phase2 Route-based با Selector 0.0.0.0/0 (VTI معمولاً با Selector کامل کار می‌کند).

#### مثال متوسط — اثبات

``` text
Cisco: show crypto ikev2 sa ; show crypto ipsec sa | include pkts
FGT  : diagnose vpn ike gateway list ; diagnose vpn tunnel list
```

شمارنده‌ها در هر دو سر باید هم‌خوان و افزایشی باشند.

#### مثال سخت — اختلاف Selector

Cisco VTI با Selector any/any و FGT با Selector محدود ⇒ TS_UNACCEPTABLE. رفع: FGT را 0.0.0.0/0 یا Cisco را محدود.

#### Lab

یک CSR و یک FGT VM در PNETLab؛ تغییر ندادن تجهیز واقعی؛ اجرا نشده.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| SA بالا ولی ping نه | Route روی Tunnel0 | افزودن |
| TS_UNACCEPTABLE | Selector | همسان |
| Identity | match identity | تصحیح |

#### پرسش‌ها با پاسخ

**۱. چرا Route-based؟** Routing پویا.
**۲. VTI Selector؟** any/any.
**۳. چرا Debug دوسر؟** مقایسه.

#### English Corner

- *Route-based VPN uses a virtual tunnel interface and supports dynamic routing.*
- Q: What does match identity remote address do on the Cisco profile?

## درس 18-6 — Gate G7: آزمون عملی IPsec — صورت مسئله، کلید پاسخ کامل و Rubric

**فصل 18 · بازنویسی عمیق · پیش‌نیاز: ۱۸-۱ تا ۱۸-۵ · ≈ 12 ساعت**

> **وضعیت:** FortiOS 7.0.3 نامی (بوت‌نشده)؛ سناریو و کلید پاسخ آموزشی‌اند؛ Lab «اجرا نشده»؛ دستورها `Unverified` تا اجرای Lab؛ ویژگی‌های وابسته به لایسنس مشخص شده‌اند.

### ۱) هدف آموزشی

در پایان این درس باید بتوانید:

1. یک تونل Site-to-Site IPsec (IKEv2) را از طراحی تا Verification مستند و پیاده‌سازی کند.
2. سه خرابی تزریق‌شده (عدم‌تطابق Proposal، Selector، NAT-T/MTU) را با شواهد تشخیص دهد.
3. هر خرابی را با Debug محدود و دستور Verification اثبات و رفع کند.
4. گزارش RCA و Evidence Index را تحویل دهد.
5. خود را با Rubric نمره‌دهی و ضعف‌ها را صادقانه ثبت کند.

### ۲) مفهوم پایه: چیست و چرا؟

Gate G7 آخرین سنجش فصل IPsec است. در دنیای واقعی تونل «بالا نمی‌آید» و مشتری فقط همین را می‌گوید؛ شما باید مرحله‌به‌مرحله ثابت کنید مشکل در Phase 1 است یا Phase 2، در Proposal است یا Selector، در NAT-T است یا MTU. این درس صورت مسئله، کلید پاسخ کامل و Rubric را یک‌جا می‌دهد تا هم تمرین کنید و هم خودتان را ارزیابی.

### ۳) توضیح عمیق فنی

#### ۱) صورت مسئله

دو سایت: HQ (FGT-HQ، WAN 198.51.100.2، LAN 10.10.0.0/16) و Branch (FGT-BR، WAN 203.0.113.2، LAN 10.20.0.0/16). نیاز: تونل IPsec IKEv2 با AES-256/SHA-256، DH Group 14، PFS فعال، DPD، فقط ترافیک LAN↔LAN، Log و Policy دوطرفه.

#### ۲) طراحی (پاسخ مرجع)

| پارامتر | مقدار |
|---|---|
| IKE | v2 |
| Phase1 Proposal | aes256-sha256 |
| DH Group | 14 |
| Lifetime P1 | 86400 s |
| Phase2 Proposal | aes256-sha256 |
| PFS | enable (DH 14) |
| Lifetime P2 | 43200 s |
| Selector | 10.10.0.0/16 ↔ 10.20.0.0/16 |
| DPD | on-idle، interval 10، retry 3 |
| NAT-T | enable |
| MTU/MSS | MSS-clamp 1350 |

#### ۳) پیکربندی مرجع HQ

``` text
config vpn ipsec phase1-interface
 edit "TO-BR"
  set interface "port1"
  set ike-version 2
  set peertype any
  set net-device disable
  set proposal aes256-sha256
  set dhgrp 14
  set remote-gw 203.0.113.2
  set psksecret <PSK-FROM-VAULT>
  set dpd on-idle
  set dpd-retrycount 3
  set dpd-retryinterval 10
  set nattraversal enable
 next
end
config vpn ipsec phase2-interface
 edit "TO-BR-P2"
  set phase1name "TO-BR"
  set proposal aes256-sha256
  set pfs enable
  set dhgrp 14
  set src-subnet 10.10.0.0 255.255.0.0
  set dst-subnet 10.20.0.0 255.255.0.0
 next
end
config router static
 edit 50
  set dst 10.20.0.0 255.255.0.0
  set device "TO-BR"
 next
end
config firewall policy
 edit 70
  set name "HQ-to-BR"
  set srcintf "port2"
  set dstintf "TO-BR"
  set srcaddr "NET-HQ"
  set dstaddr "NET-BR"
  set action accept
  set schedule "always"
  set service "ALL"
  set logtraffic all
 next
 edit 71
  set name "BR-to-HQ"
  set srcintf "TO-BR"
  set dstintf "port2"
  set srcaddr "NET-BR"
  set dstaddr "NET-HQ"
  set action accept
  set schedule "always"
  set service "ALL"
  set logtraffic all
 next
end
```

(PSK را هرگز در ریپو ننویسید؛ دستورها `Unverified` تا Lab؛ نام پارامتر `dpd` و `net-device` را با CLI help تأیید کنید.)

دقت DPD (طبق مستند/KB Fortinet): حالت پیش‌فرض DPD بسته به نوع تونل فرق دارد (on-demand یا on-idle برای dynamic)؛ در **IKEv2** تنظیم‌های `dpd-retrycount` و `dpd-retryinterval` به‌طور مستقل رعایت نمی‌شوند و Retransmission IKEv2 زمان ثابت حدود ۹۳ ثانیه دارد؛ اگر retrycount × retryinterval از ۹۳ بیشتر شود SA در ۹۳ ثانیه پاک می‌شود. پس زمان تشخیص قطع را روی IKEv2 با آزمون اندازه بگیرید.

#### ۴) خرابی‌های تزریق‌شده و کلید پاسخ

**خرابی A: Proposal متفاوت.** Branch با aes128-sha1 پیکربندی شده. شاهد:

``` text
diagnose vpn ike gateway list
diagnose debug application ike -1
diagnose debug enable
 ... "no proposal chosen" / NO_PROPOSAL_CHOSEN
```

علت: عدم‌تطابق Phase 1 Proposal. رفع: یکسان‌سازی aes256-sha256. آزمون: `diagnose vpn ike gateway list` وضعیت established.

**خرابی B: Selector.** Phase 1 ok ولی Phase 2 نمی‌آید؛ Branch Selector 10.20.0.0/24 است. شاهد: `diagnose vpn tunnel list` بدون SA یا پیام `TS_UNACCEPTABLE`/`no matching selector`. رفع: یکسان‌سازی /16 (یا Selector دقیق در هر دو). آزمون: `get vpn ipsec tunnel summary` up و ping.

**خرابی C: MTU/NAT-T.** تونل up ولی انتقال فایل بزرگ می‌ایستد. شاهد: ping با DF: 1372 ok و 1422 fail؛ Capture: Retransmission بزرگ. رفع: MSS-clamp 1350 و اجازه‌ی ICMP؛ NAT-T فعال و UDP 4500 باز. آزمون: دانلود ۱۰۰ MB.

#### ۵) Verification مرجع

``` text
get vpn ipsec tunnel summary
diagnose vpn ike gateway list
diagnose vpn tunnel list name TO-BR
diagnose sys session filter dst 10.20.0.5
diagnose sys session list
```

#### ۶) Rubric (۱۰۰ امتیاز)

| معیار | امتیاز |
|---|---|
| طراحی و جدول پارامتر | 15 |
| پیکربندی صحیح هر دو سر | 20 |
| تشخیص سه خرابی با شواهد | 30 |
| رفع و آزمون مثبت/منفی | 20 |
| Evidence Index و RCA | 10 |
| صداقت (Unverified و محدودیت‌ها) | 5 |

نمره‌ی قبولی ۷۵ و حداقل ۲۰ در بخش «تشخیص».

### ۴) طراحی و تصمیم‌گیری

| سؤال طراحی | گزینه‌ها و معیار انتخاب |
|---|---|
| IKEv2 یا v1 | IKEv2 برای Site-to-Site جدید |
| PFS | enable |
| DPD | on-idle |
| Policy | دوطرفه با Log |

### ۵) مثال‌های حل‌شده (ساده، متوسط، سخت)

**ساده (حل‌شده: خرابی A):** ورودی: Debug IKE پیام NO_PROPOSAL_CHOSEN. مراحل: ۱) `diagnose vpn ike gateway list` تونل در حالت connecting. ۲) Debug محدود به peer: `diagnose vpn ike log-filter dst-addr4 203.0.113.2`. ۳) خط Proposal دو سر مقایسه می‌شود: HQ aes256-sha256، BR aes128-sha1. پاسخ: عدم‌تطابق Proposal؛ رفع در BR و آزمون established.

**متوسط (خرابی B):** Phase 1 established ولی ping به 10.20.0.5 ندارد. مراحل: ۱) `diagnose vpn tunnel list` تعداد SA صفر برای Phase 2. ۲) Selector HQ /16 و BR /24. ۳) رفع Selector. ۴) `get vpn ipsec tunnel summary` selectors up. پاسخ: Selector Mismatch؛ با /16 یکسان یا Subnet دقیق.

**سخت (خرابی C + RCA):** تونل up ولی فایل بزرگ می‌ایستد. مراحل: ۱) PMTU با ping DF: 1372 ok، 1422 fail ⇒ PMTU≈1400. ۲) MSS=1400−40=1360 با حاشیه 1350. ۳) `set tcp-mss-sender 1350` روی Policy تونل. ۴) ICMP frag-needed مجاز. ۵) دانلود ۱۰۰MB سه بار بدون Retransmission. RCA: سربار ESP/UDP-encap MTU مؤثر را کم کرد و MSS تنظیم نشده بود؛ پیشگیری: MSS-clamp استاندارد برای همه‌ی تونل‌ها.

### ۶) پیاده‌سازی از مسیر GUI

1. VPN → IPsec Wizard یا Custom: Phase 1 و Phase 2 را مطابق جدول بسازید.
2. Network → Static Routes: مسیر 10.20.0.0/16 به Interface تونل.
3. Policy & Objects → دو Policy (HQ→BR و BR→HQ).
4. Monitor → IPsec Monitor برای وضعیت.

### ۷) پیاده‌سازی از مسیر CLI

``` text
get vpn ipsec tunnel summary
diagnose vpn ike gateway list
diagnose vpn tunnel list name TO-BR
diagnose debug application ike -1
diagnose debug enable
diagnose debug disable
diagnose debug reset
```

### ۸) Verification (اثبات صحت)

- Phase 1 و Phase 2 در حالت up.
- ping و TCP بین LANها.
- Session با policy_id درست.
- دانلود بزرگ بدون Retransmission.
- آزمون منفی: ترافیک غیرمجاز رد.

### ۹) Troubleshooting

| علامت | شاهد برای بررسی | علت محتمل و رفع |
|---|---|---|
| NO_PROPOSAL_CHOSEN | Proposal دو سر | یکسان‌سازی |
| TS_UNACCEPTABLE | Selector | Subnet |
| فایل بزرگ می‌ایستد | PMTU | MSS-clamp |
| تونل flap | DPD/NAT-T | تایمر/UDP 4500 |

### ۱۰) نکات امنیتی

- PSK قوی و در Vault.
- Policy حداقلی.
- Debug را خاموش کنید.

### ۱۱) جمع‌بندی مفهومی

- Proposal، Selector، MTU سه خرابی رایج.
- Debug محدود به peer.
- Rubric و Evidence.

### ۱۲) تمرین و ارزیابی

**ت1.** (ساده) NO_PROPOSAL_CHOSEN یعنی چه؟ *(پاسخ: 18-6-ت1)*

**ت2.** (ساده) Selector چیست؟ *(پاسخ: 18-6-ت2)*

**ت3.** (متوسط) Phase 1 up ولی ping نه؛ بررسی‌ها؟ *(پاسخ: 18-6-ت3)*

**ت4.** (متوسط) چرا Debug محدود به peer؟ *(پاسخ: 18-6-ت4)*

**ت5.** (سخت) MSS را برای PMTU 1400 محاسبه کنید. *(پاسخ: 18-6-ت5)*

**ت6.** (سخت، طراحی) Evidence Index برای G7. *(پاسخ: 18-6-ت6)*

**Q1.** Quick quiz (English): Which command lists IKE gateways and their state? *(پاسخ: 18-6-Q1)*

### ۱۳) اصطلاحات و English Corner

| مخفف | شکل کامل | معنی |
|---|---|---|
| IKE | Internet Key Exchange | تبادل کلید اینترنت |
| PFS | Perfect Forward Secrecy | محرمانگی پیش‌رونده |
| DPD | Dead Peer Detection | تشخیص همتای مرده |
| NAT-T | NAT Traversal | عبور از NAT |

- *The tunnel is up but traffic does not flow.* ← تونل up است ولی ترافیک عبور نمی‌کند.

### ۱۴) کارت Lab

**کارت Lab:** G7 IPsec (اجرا نشده). **Evidence:** `03-ops/g7-ipsec.md`.

### ۱۵) منابع

- Fortinet FortiOS 7.0 Administration Guide: IPsec VPN
- FortiOS 7.0 IPsec troubleshooting

### تعمیق: کلید ارزیابی G7

**Rubric:** Tunnel برقرار ۲۰، Routing ۱۵، Policy ۱۵، MTU ۱۵، عیب‌یابی خرابی تزریقی ۲۵، گزارش ۱۰.

**خرابی‌های نمونه:** PSK متفاوت، Selector اشتباه، Route ناقص؛ برای هرکدام پیام Debug، علت و رفع.

**پرسش‌های مصاحبه**
1. *تفاوت Route-based و Policy-based؟* Interface مجازی در برابر Policy.
2. *Dead Peer Detection؟* تشخیص قطع.
3. *شاهد برقراری؟* شمارنده‌ها و ping.

### تکمیل عمیق: G7 — صورت مسئله، کلید پاسخ و Rubric

#### چرا؟

G7 ثابت می‌کند IPsec را از طراحی تا عیب‌یابی اجرا می‌کنید.

#### صورت مسئله

دو سایت 10.1.0.0/24 و 10.2.0.0/24؛ Tunnel IKEv2؛ سه خرابی تزریقی: PSK، Selector، Route.

#### کلید

1. برگه‌ی پارامتر.
2. ساخت Tunnel.
3. اثبات (counter + ping).
4. خرابی ۱: AUTH_FAILED ⇒ PSK.
5. خرابی ۲: TS_UNACCEPTABLE ⇒ Selector.
6. خرابی ۳: Tunnel Up بدون ping ⇒ Route.
7. MTU.

#### Rubric

``` text
Up 20 | Routing 15 | Policy 15 | MTU 15 | Fault diagnosis 25 | Report 10
```

#### مثال سخت — دو خرابی هم‌زمان

PSK درست شد ولی Selector هنوز؛ پس از هر رفع آزمون جدید. قاعده: یک تغییر در هر زمان.

#### Lab

سه خرابی را ایجاد و رفع کنید و شواهد را ثبت.

#### عیب‌یابی

| علامت | علت | رفع |
|---|---|---|
| چند خطا | هم‌زمان | یکی‌یکی |
| Evidence ناقص | ثبت | الگو |
| MTU فراموش | آزمون ناقص | DF |

#### پرسش‌ها با پاسخ

**۱. چرا یکی‌یکی؟** ردیابی.
**۲. Evidence؟** debug + counters.
**۳. MTU؟** آزمون DF.

#### English Corner

- *Fix one fault at a time and retest.*
- Q: How do you distinguish a selector problem from a routing problem?

## پاسخ‌های فصل 18

> ابتدا بدون نگاه حل کنید. شناسه: درس-نوع+شماره (ت = تمرین، م = مرور).


### پاسخ‌های بازنویسی درس 18-1

**18-1-ت1** — مدرن‌تر؛ پیام کمتر؛ پیش‌فرض 7.0 v1 است.

IKEv2 مدرن‌تر است، پیام کمتر و ویژگی بهتر دارد؛ پیش‌فرض FortiOS 7.0 هنوز v1 است و باید صریح انتخاب شود.

**18-1-ت2** — تا خطای شبکه با خطای IPsec اشتباه نشود.

Reachability را جدا تست کنید تا خطای شبکه با خطای IPsec اشتباه نشود.

**18-1-ت3** — NAT به Subnet یکتا یا Re-IP؛ ثبت در IP Plan.

Overlap آدرس: NAT به Subnet یکتا یا Re-IP و ثبت در IP Plan.

**18-1-ت4** — جدول ۱۸-۱ کامل شده با مقادیر و دلایل.

**18-1-ت5** — IKE/Child SA، ping، TCP، MTU، Failover.

آزمون: IKE/Child SA، ping، TCP، MTU و Failover.

**18-1-Q1** — To ensure both peers use mirrored settings and to avoid trial and error.

### پاسخ‌های بازنویسی درس 18-2

**18-2-ت1** — Route به Tunnel، Policy دوطرفه و Selector سازگار.

تونل Route-based نیاز به Route به Tunnel، Policy دوطرفه و Selector سازگار دارد.

**18-2-ت2** — چون ترافیک در هر دو جهت باید اجازه داشته باشد و Stateful فقط جهت شروع را به Session می‌گذارد.

**18-2-ت3** — IKE SA Established؛ Child SA با شمارنده‌ی Encrypt/Decrypt؛ ping/Log داده.

Verify: IKE SA Established، Child SA با شمارنده‌ی Encrypt/Decrypt و ping/Log داده.

**18-2-ت4** — Policy سمت مقابل، Route برگشت، NAT-T/UDP 4500، Selector. شاهد: tunnel list، Sniffer، Debug Flow.

**18-2-ت5** — Source=Subnet/Host مجاز Site A، Destination=سرور خاص، Service=پورت لازم، Log فعال.

**18-2-Q1** — A route to the tunnel interface, policies in both directions, and compatible selectors.


### پاسخ‌های بازنویسی درس 18-3


### پاسخ‌های بازنویسی عمیق درس 18-3

**18-3-ت1** — الگوریتم و DH را توافق می‌کند.

IKE_SA_INIT الگوریتم و DH را توافق می‌کند.

**18-3-ت2** — Selector نامطابق.

TS_UNACCEPTABLE یعنی Selector نامطابق.

**18-3-ت3** — PSK/هویت.

AUTHENTICATION_FAILED یعنی PSK یا هویت متفاوت.

**18-3-ت4** — UDP 500/4500.

Timeout: UDP 500/4500 را بررسی کنید.

**18-3-ت5** — Sniffer و ACL.

Timeout را با Sniffer و ACL دو سر رفع کنید.

**18-3-ت6** — طبق متن.

**18-3-Q1** — IKE_SA_INIT.

### پاسخ‌های بازنویسی عمیق درس 18-4

**18-4-ت1** — MSS ≈ MTU − 40 (هدر IP و TCP).

MSS ≈ MTU − 40 (هدر IP و TCP)؛ در تونل MTU مؤثر کمتر است.

**18-4-ت2** — بسته‌ی بزرگ DF Drop می‌شود و ICMP Frag-Needed بلاک است؛ فرستنده اندازه را کم نمی‌کند.

**18-4-ت3** — حدود 58–66 بایت (IP 20، UDP 8، ESP 8، IV 8، trailer/pad، ICV 16).

سربار ESP حدود ۵۸ تا ۶۶ بایت (IP 20، UDP 8، ESP 8، IV 8، trailer/pad، ICV 16).

**18-4-ت4** — 1372+28 = 1400.

MTU مسیر = اندازه‌ی ping موفق + 28؛ 1372 + 28 = 1400.

**18-4-ت5** — MSS مخصوص TCP است؛ UDP باید با MTU کم/اندازه‌ی برنامه/Fragmentation حل شود.

**18-4-ت6** — MTU Tunnel 1400، MSS 1360، ICMP 3/4 باز، آزمون پس از هر تغییر.

MTU تونل 1400، MSS 1360، ICMP 3/4 باز و آزمون پس از هر تغییر.

**18-4-Q1** — Small packets fit through the tunnel, but large DF packets are dropped without ICMP feedback.


### پاسخ‌های بازنویسی عمیق درس 18-5

**18-5-ت1** — show crypto ipsec sa.

`show crypto ipsec sa` در Cisco برای Child SA و شمارنده‌ها.

**18-5-ت2** — Route-based؛ Routing تعیین می‌کند ترافیک وارد Tunnel شود.

Route-based: Routing تعیین می‌کند ترافیک وارد Tunnel شود؛ برخلاف Policy-based.

**18-5-ت3** — Phase 2/Rekey شکست؛ INVALID_KE_PAYLOAD/NO_PROPOSAL.

Phase 2/Rekey شکست: INVALID_KE_PAYLOAD یا NO_PROPOSAL (PFS/DH).

**18-5-ت4** — Rekey رفتار متفاوت دارد و ممکن است قطع/Flap شود.

Rekey در سازنده‌ها رفتار متفاوت دارد و ممکن است Flap بدهد.

**18-5-ت5** — Lifetime/PFS؛ Log دو سر؛ یکسان‌سازی؛ آزمون.

Lifetime/PFS را در دو سر یکسان کنید و Log دو سر را مقایسه کنید.

**18-5-ت6** — جدول پارامتر/نتیجه/نسخه.

**18-5-Q1** — show crypto ikev2 sa.


### پاسخ‌های بازنویسی عمیق درس 18-6


### پاسخ‌های بازنویسی عمیق درس 18-6

**18-6-ت1** — دو سر روی الگوریتم‌های Phase 1 توافق نکردند؛ Proposal هر دو سر را مقایسه و یکسان کنید.

**18-6-ت2** — شبکه‌های مبدأ و مقصدی که در Phase 2 رمز می‌شوند؛ باید در دو سر یکسان (متقارن) باشد.

**18-6-ت3** — Phase 2/Selector، Route به Interface تونل، Policy دوطرفه، سپس Debug و Session.

**18-6-ت4** — تا CPU و حجم Log کنترل شود و فقط همان تونل دیده شود.

Debug محدود به peer تا CPU و حجم Log کنترل شود.

**18-6-ت5** — MSS = 1400 − 40 = 1360؛ با حاشیه 1350 تنظیم و با دانلود بزرگ آزمون می‌شود.

**18-6-ت6** — فهرست خروجی‌ها: ike gateway، tunnel list، session، ping/TCP، Debug محدود، تصویر، زمان و نتیجه.

**18-6-Q1** — diagnose vpn ike gateway list.

### پاسخ‌های درس افزوده‌ی 18-0 (فصل 18)

**18-0-ت1** — Phase 1 کانال کنترل امن (IKE SA)؛ Phase 2 SA داده (Child SA) و Selector.

Phase 1 کانال کنترل امن (IKE SA) و Phase 2 SA داده (Child SA) با Selector.

**18-0-ت2** — با هر Rekey کلید تازه با DH جدید می‌سازد تا افشای کلید قدیمی ترافیک گذشته را باز نکند.

**18-0-ت3** — Selector باز + Routing + Policy؛ Routing پویا و مقیاس‌پذیری راحت.

Route-based: Selector باز + Routing + Policy؛ مقیاس‌پذیر و مناسب Routing پویا.

**18-0-ت4** — عبور از NAT با کپسوله‌کردن ESP در UDP؛ پورت UDP 4500.

NAT-T ESP را در UDP 4500 کپسوله می‌کند تا از NAT عبور کند.

**18-0-ت5** — ۱) Policy سمت مقابل؛ ۲) Route برگشت؛ ۳) NAT-T/UDP 4500؛ ۴) Selector. شاهد: tunnel list، Sniffer، Debug Flow سمت مقابل.

**18-0-ت6** — AES-256-GCM، SHA-256، DH 20 یا ≥ 14، PFS روشن، Lifetime حدود 8 تا 24 ساعت، DPD on-idle با retry 3؛ دلیل: امنیت و سازگاری.

**18-0-ت7** — Selectorها آینه‌ی هم باشند؛ در Route-based از 0.0.0.0/0 استفاده یا Subnetهای دقیق هم‌سان؛ بررسی Debug IKE.

**18-0-م1** — پیام دوره‌ای برای تشخیص مرگ Peer و پاک‌کردن SA.

DPD پیام دوره‌ای برای تشخیص مرگ Peer و پاک‌کردن SA است.

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
