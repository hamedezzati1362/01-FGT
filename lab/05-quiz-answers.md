# پاسخ آزمون
1. `>` User EXEC (دستورهای مشاهده‌ی محدود)؛ `#` Privileged EXEC (همه‌ی show و کپی، با `enable`)؛ `(config)#` پیکربندی (با `configure terminal`).
2. `?` فهرست گزینه‌ها؛ Tab کامل‌کردن؛ مخفف یکتا هم کار می‌کند (`sh int sta`).
3. `show cdp neighbors` (و `detail` برای IP/Port).
4. `show mac address-table address <MAC>` روی هسته ← پورت به DIST؛ همان روی DIST ← پورت به ACC؛ `show cdp neighbors` برای تعیین سوییچ؛ روی ACC همان دستور ← پورت کاربر و VLAN.
5. Client اجازه‌ی تغییر دیتابیس ندارد؛ VLAN را روی VTP Server (هسته) می‌سازیم و پخش می‌شود.
6. اگر Domain/Password یکی و Revision بالاتر باشد، دیتابیس VLAN شبکه را با دیتابیس خودش جایگزین می‌کند. قبل از وصل: `vtp mode transparent` یا حذف `vlan.dat` و reload.
7. بدون `add` کل لیست جایگزین می‌شود و بقیه‌ی VLANها قطع؛ با `add` فقط اضافه می‌شود.
8. پورت در VLAN اشتباه؛ VLAN در Trunk مجاز نیست؛ Relay یا Scope نیست؛ سرور/Lease/Pool مشکل دارد.
9. Broadcast مشتری به Unicast تبدیل می‌شود؛ روی Interface/Sub-interface Gateway همان VLAN (در Lab: `Gi0/0.<VLAN>` روی FW-RTR).
10. PC + Phone + یک MAC برای تعویض دستگاه؛ با ۲ در اولین تعویض Violation می‌خورید.
11. notconnect: کابل/دستگاه نیست؛ disabled: shutdown (Admin down)؛ inactive: VLAN پورت وجود ندارد؛ err-disabled: سوییچ به‌خاطر خطا (Port-Security/BPDU Guard/Loop) بسته.
12. a-half/a-100: Duplex/Speed auto-negotiate شده نیمه‌دوطرفه؛ معمولاً یک سمت Force و سمت دیگر Auto (Mismatch).
13. تاریخچه‌ی شمارنده را از دست می‌دهید؛ به‌جایش «تفاضل شمارنده» بین دو زمان را حساب می‌کنیم.
14. Merge: `copy file running-config` (اضافه/روی‌هم، حذفی ندارد). Replace: `configure replace file force` (دقیقاً مثل فایل، هرچه نیست پاک).
15. وضعیت فعلی ثبت؛ بکاپ؛ راه برگشت؛ `reload in 10`؛ تغییر مرحله‌ای با راستی‌آزمایی؛ تست نهایی + `write memory` + `reload cancel`.
