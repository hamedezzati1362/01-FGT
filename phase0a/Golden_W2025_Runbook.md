# Runbook — ساخت Golden Image (Windows Server 2025) روی ESXi

> نام VM: `GOLD-W2025`؛ دیسک روی `ds01-ssd`. هرگز بعد از Sysprep دوباره روشنش نکنید؛ فقط از آن Clone بگیرید.

## ۱. ساخت VM (Host Client → Create/Register VM)
| مورد | مقدار |
|---|---|
| Compatibility | ESXi 8.0 U2 (یا 7.0 U2 اگر ESXi قدیمی‌تر مقصد باشد) |
| Guest OS | Windows → Microsoft Windows Server 2022 (64-bit) (اگر 2025 در لیست بود، همان) |
| Storage | `ds01-ssd` |
| CPU / RAM | 2 vCPU / 4 GB |
| Disk | 60 GB، **Thin** |
| SCSI Controller | **LSI Logic SAS** (درایور داخل ویندوز) |
| NIC | `VM Network`، VMXNET3 |
| VM Options → Boot | **Firmware: EFI**، Secure Boot روشن |
| CD/DVD | Datastore ISO file → ISO ویندوز سرور 2025 + **Connect** |

## ۲. نصب
- Boot from CD («Press any key» را سریع بزنید).
- Edition: **Windows Server 2025 Standard (Desktop Experience)**.
- Custom install روی دیسک خالی؛ رمز Administrator (در چت ننویسید).

## ۳. داخل ویندوز
1. نصب **VMware Tools** (Host Client → Actions → Guest OS → Install VMware Tools؛ داخل VM `setup64.exe` از درایو CD) و Reboot.
2. Windows Update تا نماندن آپدیت؛ Reboot.
3. تنظیمات: Time zone، فعال‌کردن RDP، Power Plan = High performance، شبکه = **DHCP**.
4. **ننصب AD DS، عدم Join به دامنه، عدم Activation، عدم نصب نرم‌افزار اضافه.**
5. پاک‌سازی: Disk Cleanup.

## ۴. پیش از Sysprep (اختیاری ولی توصیه‌شده)
VM را خاموش و یک **کپی** از پوشه‌اش با نام `GOLD-W2025-PRE` نگه دارید (برای آپدیت‌های بعدی بدون ساخت از صفر).

## ۵. Sysprep
```text
C:\Windows\System32\Sysprep\sysprep.exe /generalize /oobe /shutdown
```
اگر خطا داد: `C:\Windows\System32\Sysprep\Panther\setupact.log`. بعد از خاموش‌شدن، CD را Disconnect کنید و **VM را دیگر روشن نکنید**.

## ۶. Clone برای VM جدید (از SSH ESXi)
```bash
mkdir -p /vmfs/volumes/ds02-ssd/DC1
vmkfstools -i /vmfs/volumes/ds01-ssd/GOLD-W2025/GOLD-W2025.vmdk -d thin /vmfs/volumes/ds02-ssd/DC1/DC1.vmdk
```
بعد در Host Client یک VM جدید با Wizard بسازید **با همان تنظیمات** (EFI + Secure Boot، LSI Logic SAS، Windows Server 2022 64-bit) و دیسک پیش‌فرض را حذف کنید → **Add hard disk → Existing hard disk** → `DC1.vmdk`. بوت اول وارد OOBE می‌شود (رمز Administrator و نام جدید).

## ۷. بکاپ
Export OVF از `GOLD-W2025` به هارد 1 TB (Host Client → Export).
