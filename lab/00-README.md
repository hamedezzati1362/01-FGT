# کارگاه عملی «شبکه‌ی سازمانی با سوییچ Cisco» روی PNETLab
مدت: ۴ ساعت (قابل فشرده‌سازی به ۳ ساعت و نیم). برای ادمین مایکروسافت که تازه با Cisco کار می‌کند.
**قانون:** همه‌چیز فقط داخل Lab ایزوله‌ی PNETLab؛ هیچ‌چیز روی ESXi، MikroTik یا شبکه‌ی واقعی تغییر نمی‌کند. رمزها همه نمونه‌اند (`Lab-Only-123`).

## ۱) چه چیزی می‌سازیم
هسته (VTP Server، فقط L2) ← توزیع ← ۳ سوییچ طبقه؛ یک روتر (نقش فایروال/Gateway، Router-on-a-Stick، `.254`) با DHCP Relay؛ یک سرور Linux (DHCP + TFTP)؛ سه میزبان Linux که هرکدام «کامپیوتر + IP Phone» روی یک کابل‌اند؛ و یک سوییچ کوچک اضافه (MINI-SW) برای خرابی‌های VTP و حلقه.

## ۲) پیش‌نیازها و منابع (طبق Inventory شما: PNETLab 4.2.8، 16 vCPU، 48 GB RAM)
| گره | تعداد | Image/Template | RAM | دلیل انتخاب |
|---|---|---|---|---|
| CORE, DIST, ACC1-3, MINI-SW | 6 | `viosl2` (vIOS-L2 15.2) | 1 GB هرکدام | سوییچ L2 Cisco واقعی-نما؛ در Inventory شما نصب است؛ VLAN/Trunk/PVST/Port-Security-config در Probe قبلی Tested-OK |
| FW-RTR | 1 | `vios` (IOSv 15.9) | 1 GB | Router-on-a-Stick و `ip helper-address` تست‌شده (RoAS Tested-OK) |
| SRV1, HOST1-3 | 4 | Linux سبک (بخش «Linux image») | 512-1024 MB | DHCP/TFTP و شبیه‌سازی تلفن+PC |
جمع: حدود ۱۰ تا ۱۱ GB RAM؛ بسیار کمتر از ظرفیت 48 GB. **IOL استفاده نشد** (طبق قانون پروژه) و **PoE واقعی نداریم** (فقط مفهومی).

### Linux image (یک‌بار آماده کنید)
Image لینوکس در Inventory ثبت‌نشده است (`Unverified`). ساده‌ترین راه: از Ubuntu 22.04 Golden خودتان در ESXi یک VM موقت بسازید، بسته‌ها را نصب کنید (ایزوله‌بودن Lab یعنی داخل Lab اینترنت نیست):
```
sudo apt-get update && sudo apt-get install -y isc-dhcp-server isc-dhcp-client tftpd-hpa vlan iproute2 tcpdump
sudo mkdir -p /opt/lab && sudo cp -r hosts/* /opt/lab/     # پوشه‌ی hosts همین ریپو
sudo systemctl disable isc-dhcp-server tftpd-hpa            # فقط SRV1 دستی راه می‌اندازد
```
سپس VMDK را به qcow2 تبدیل و در PNETLab بگذارید (دستور را شما روی PNETLab اجرا می‌کنید):
```
qemu-img convert -f vmdk -O qcow2 ubuntu-lab.vmdk virtioa.qcow2
mkdir -p /opt/unetlab/addons/qemu/linux-ubuntu2204-lab
mv virtioa.qcow2 /opt/unetlab/addons/qemu/linux-ubuntu2204-lab/
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
```
Template: `linux`. اگر Image لینوکس ندارید/نمی‌خواهید بسازید: «Fallback» پایین.

## ۳) زمان‌بندی (دقیق)
| # | بخش | دقیقه | فایل |
|---|---|---|---|
| 1 | آماده‌سازی PNETLab، توپولوژی و تست قابلیت‌ها (Probe) | 30 | `03-modules/M01-setup-probe.md` |
| 2 | پایه: شناخت، پیدا کردن دستگاه، VLAN، VTP، Trunk | 40 | `M02-basics-vlan-vtp-trunk.md` |
| 3 | DHCP و IP Phone | 30 | `M03-dhcp-phone.md` |
| 4 | Port-Security، پورت‌های بلااستفاده، سرعت/دوپلکس | 25 | `M04-security-ports.md` |
| 5 | بکاپ و بازیابی | 25 | `M05-backup-restore.md` |
| 6 | سناریوهای جابه‌جایی میز و تغییر | 40 | `M06-change-scenarios.md` |
| 7 | رفع خرابی‌های پنهان (۱۲ خرابی تصادفی) | 35 | `M07-hidden-faults.md` |
| 8 | جمع‌بندی و آزمون | 15 | `M08-wrapup-quiz.md` |
جمع: 240 دقیقه. اگر ۳ ساعت می‌خواهید: از M07 فقط ۶ خرابی و از M06 فقط دو سناریو.

## ۴) محدودیت‌های صریح (قبل از شروع)
| موضوع | وضعیت | جایگزین |
|---|---|---|
| IP Phone/PoE واقعی | وجود ندارد | میزبان Linux با دو هویت (MAC متفاوت، VLAN 97 تگ‌دار)؛ PoE فقط مفهومی (`show power inline` نمونه‌ی واقعی در M03) |
| VTP، voice VLAN، Port-Security (اجرای Violation)، `archive`، `configure replace`، `show archive config differences`، `dir flash:` روی viosl2 | **آزمایش‌نشده** (فقط بخشی از config در Probe دیده شده) | Module M01 قبل از شروع ۱۰ دقیقه همه را می‌سنجد؛ هرجا نشد، نمونه‌ی خروجی واقعی و جایگزین در همان Module هست |
| Duplex/Speed/CRC | فقط Config پذیرفته می‌شود؛ شمارنده‌ی خطا تولید نمی‌شود | نمونه خروجی واقعی در M04 |
| 169.254.x.x | Linux بدون Avahi 169.254 نمی‌سازد؛ «آدرس ندارد» معادل آن است | همان را بخوانید |
| نام پورت | سوییچ واقعی `Gi1/0/N`؛ Lab: `Gi0/N` و `Gi1/N` | جدول نگاشت در `01-topology.md` |
| فایل Import (.unl) | **نساخته‌ام**: قالب آن را بدون آزمایش روی نسخه‌ی شما نمی‌توانم تضمین کنم | ساخت دستی ۱۱ گره طبق `02-build-guide.md` (۱۵ دقیقه) + Configها قابل Paste |

## ۵) تزریق Startup-config
۱) با Console هر گره (Telnet از PNETLab) وارد شوید؛ `enable`؛ `configure terminal`.
۲) فایل `configs/base/<گره>.cfg` را **در دسته‌های حداکثر ۲۵ خطی** Paste کنید و بین دسته‌ها چند ثانیه صبر کنید (Paste طولانی روی Console گاهی کاراکتر گم می‌کند؛ هرجا `% Invalid input` دیدید همان خط را دوباره بزنید).
۳) دستور `crypto key generate rsa modulus 2048` آخرین خط است و ~۱۰ ثانیه طول می‌کشد.
۴) `end` سپس `write memory`.
(راه پیشرفته: بعد از بالا آمدن SRV1، فایل‌ها را در `/srv/tftp` بگذارید و با `copy tftp://192.168.90.11/<file> running-config` Merge کنید؛ همین، تمرین TFTP هم هست.)

## ۶) Fallback اگر Linux ندارید
- DHCP: روی FW-RTR برای هر VLAN `ip dhcp pool` + `host`/`client-identifier 01<MAC>` بسازید و `ip helper-address` را حذف کنید (Relay را فقط مفهومی بخوانید).
- TFTP: IOS فقط می‌تواند «سرور خواندنی» باشد؛ برای بکاپ از `copy running-config flash:` استفاده کنید.
- تلفن+PC: بدون Linux قابل‌شبیه‌سازی نیست؛ M03 را مفهومی بخوانید.

## ۷) محتوای پوشه
`01-topology.md` نقشه‌ی شبکه ‖ `02-build-guide.md` ساخت ‖ `03-modules/` ‖ `configs/base|faults|solutions` ‖ `hosts/` ‖ `04-faults-answer-key.md` (**بعد از تمرین باز کنید**) ‖ `05-quiz*.md` ‖ `06-cheatsheet.md` ‖ `07-checklist.md` ‖ `backups/`
