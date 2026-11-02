# Phase 0A — اجرای Read-Only توسط خود شما

**هیچ‌کدام از این اسکریپت‌ها تغییری نمی‌دهند.** اسکریپت از طریق SSH پایپ می‌شود و روی میزبان فایلی نوشته نمی‌شود. رمز/کلیدی جمع‌آوری نمی‌شود (`config.php` و فایل‌های رمز خوانده نمی‌شوند).

```bash
ssh root@192.168.88.3   'sh -s' < esxi_phase0a_readonly.sh    > esxi_phase0a.txt
```
```bash
ssh root@192.168.88.199 'sh -s' < pnetlab_phase0a_readonly.sh > pnetlab_phase0a.txt
```

اگر از PowerShell استفاده می‌کنید (`<` پشتیبانی نمی‌شود):

```powershell
Get-Content -Raw .\esxi_phase0a_readonly.sh   | ssh root@192.168.88.3   "sh -s" | Out-File esxi_phase0a.txt
Get-Content -Raw .\pnetlab_phase0a_readonly.sh | ssh root@192.168.88.199 "sh -s" | Out-File pnetlab_phase0a.txt
```

**قبل از ارسال:** دو فایل خروجی را سرسری بخوانید؛ اگر چیز حساسی دیدید (مثلاً نام داخلی) حذف کنید. سپس محتوا را اینجا بچسبانید.

**کارهایی که قبل از ارسال نباید بکنید:** فعال/غیرفعال‌کردن سرویس، ساخت Port Group/vSwitch، Snapshot، Boot Node، تغییر MikroTik/WireGuard.

## موارد دستی (خارج از اسکریپت)
- در PNetLab وب (`192.168.88.199`): نسخه (About/Settings)، فهرست Labهای موجود.
- Imageهای قانونی که دارید (نام فایل + منبع لایسنس): Cisco IOSv/IOSvL2، FortiGate 7.0.3.
- Subnet/ماسک شبکه واقعی و Subnetهای محل کار (برای جلوگیری از هم‌پوشانی).
- تأیید: آیا Snapshot/Backup اخیر از VM PNetLab دارید؟
