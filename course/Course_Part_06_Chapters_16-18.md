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
