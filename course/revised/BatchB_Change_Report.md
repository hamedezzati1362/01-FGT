# گزارش تغییرات دسته B (فصل ۵، ۹، ۱۰) — نسخه v3.1

## ۱) نسخه‌ی هدف
FortiOS 7.0.3 (طبق Inventory و مستندات پروژه)؛ بوت‌نشده؛ هیچ دستگاهی تغییر داده نشد. دسته B فقط Cisco Routing است و به نسخه‌ی FortiOS وابسته نیست؛ ارجاع به FortiGate فقط مفهومی (Local-in، Zone، VDOM) و `Unverified` است.

## ۲) اصلاح آمار گزارش قبلی
| وضعیت | تعداد | فصل‌ها |
|---|---|---|
| کامل | ۰ | — |
| تکمیل محدود | ۷ | ۱–۴، ۶–۸ |
| بازنویسی/توسعه‌ی جدی | ۲۰ | ۵، ۹–۱۵، ۱۷، ۱۹، ۲۰، ۲۳، ۲۵–۳۲ |
| کمبود علمی اساسی | ۵ | ۱۶، ۱۸، ۲۱، ۲۲، ۲۴ |
| جمع | ۳۲ | |
گزارش قبلی ۸ و ۱۸ نوشته بود که اشتباه بود.

## ۲-ب) یک ادعای قبلی که تصحیح می‌شود
گزارش قبل نوشته بود فصل ۵ «الگوریتم انتخاب مسیر (LPM → AD → Metric)» ندارد؛ این درست نبود: درس ۵-۱ LPM و AD را دارد. کمبود واقعی ۵ فقط Control/Data Plane، RIB/FIB/CEF، Forwarding بسته‌به‌بسته و Convergence بود که اکنون افزوده شد.

## ۳) درس‌های افزوده (۶ درس، ≈ ۷۹ KB متن جدید + ۱ شکل)
| درس | موضوع | خلأ برطرف‌شده |
|---|---|---|
| 5-0 | Control/Data Plane، RIB/FIB/CEF، Adjacency، Recursive Lookup، Punt، عبور بسته‌به‌بسته | Control/Data Plane، FIB، مسیر بسته |
| 5-7 | Convergence: Detect/Propagate/Compute/Install، Dead Timer، BFD، SPF Throttle، Black Hole، IP SLA | Convergence، BFD، Timers |
| 9-0 | چرا BGP: AS، Path Vector، پیام‌ها و Timerها، eBGP/iBGP، Split Horizon | مبنای BGP |
| 9-7 | ترتیب کامل انتخاب مسیر Cisco، Local-Pref/Prepend/MED، Timer/BFD/MRAI، Prefix-List/Bogon، Max-Prefix، TTL Security، Route Leak | Best-path، امنیت BGP |
| 10-8 | Route Leaking بین VRF، روش‌ها، خطرها، آزمون مثبت/منفی، پیوند با Zone/VDOM | Route Leaking |
| 10-9 | ECMP: شرط، Hash، Elephant/Polarization، Stateful Firewall، Rehash | ECMP عمیق |
هر درس: هدف، پیش‌نیاز، مفهوم، سازوکار، مثال حل‌شده و سخت، طراحی، CLI، Verification، Troubleshooting، امنیت، جمع‌بندی، ۷–۹ تمرین (با سطح‌بندی)، واژگان/English Corner، منابع. پاسخ‌ها در انتهای فصل.

## ۴) فایل‌ها
- `course/revised/Course_Part_02_Chapters_04-06_v3.1.md` (فصل ۵: ۵-۰، ۵-۷)
- `course/revised/Course_Part_03_Chapters_07-09_v3.1.md` (فصل ۹: ۹-۰، ۹-۷)
- `course/revised/Course_Part_04_Chapters_10-12_v3.1.md` (فصل ۱۰: ۱۰-۸، ۱۰-۹)
- `course/figures/ch05-l0-fig1.svg` (شکل جدید)؛ فایل‌های اصلی دست‌نخورده.
- هر سه فایل با `tools/check_part.py` در وضعیت OK.

## ۵) منابع استفاده‌شده
Cisco «Select BGP Best-path Algorithm» (cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html)، RFC 4271، RFC 7454 (BCP 194)، RFC 5880، RFC 2328، RFC 1812، RFC 4364، RFC 2991/2992.

## ۶) محدودیت‌ها و کمبودهای باقی‌مانده (صادقانه)
1. ترتیب مراحل Best-path برای ۶ مرحله‌ی اول از مستند Cisco تأیید شد؛ **Tie-breakerهای انتهایی و مقدار پیش‌فرض MRAI/Max-paths وابسته به نسخه/پلتفرم‌اند و `Unverified`**.
2. جدول ASN خصوصی/۴بایتی از حافظه است؛ باید با IANA تطبیق داده شود.
3. هیچ دستور روی vIOS/CSR اجرا نشده؛ Labها «اجرا نشده».
4. فقط یک شکل جدید؛ شکل‌های مناسب‌تر برای BGP Best-path، Convergence و Leak هنوز ساخته نشده‌اند.
5. درس‌های موجود ۹-۱ تا ۹-۶ و ۱۰-۱ تا ۱۰-۷ بازنویسی نشدند؛ فقط تکمیل شدند. اگر بخواهید عمق آن‌ها هم بررسی/بازنویسی شود، در دسته‌ی بعد انجام می‌شود.
6. تعداد ساعات فصل‌های ۵، ۹، ۱۰ حدود +۴ تا +۷ ساعت هر درس افزوده بیشتر می‌شود؛ مجموع پیشنهادی: ف۵ +۱۰ ساعت، ف۹ +۱۱ ساعت، ف۱۰ +۱۱ ساعت (تصمیم شما).
