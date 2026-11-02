# Send-ToLab.ps1

اسکریپت ساده PowerShell برای ارسال فایل از لپ‌تاپ به ESXi/PNetLab با `scp` و بررسی SHA256.

```powershell
# ISO به Datastore ESXi (پوشه iso روی ds01-ssd؛ ساخته می‌شود اگر نبود)
.\Send-ToLab.ps1 -Path .\Win2022.iso -Target EsxiIso

# Image برای PNetLab (نام پوشه Image الزامی است)
.\Send-ToLab.ps1 -Path .\virtioa.qcow2 -Target PnetImage -ImageFolder fortinet-7.0.3

# Lab Export به PNetLab
.\Send-ToLab.ps1 -Path .\MyLab.zip -Target PnetLabs
```

- رمز ذخیره نمی‌شود (scp/ssh می‌پرسند). برای راحتی می‌توانید بعداً کلید SSH تنظیم کنیم (تغییر روی ESXi؛ با Change Record).
- قبل از رونویسی تأیید می‌گیرد و بعد از کپی SHA256 را مقایسه می‌کند.
- **آزمایش‌نشده**: ابتدا با فایل کوچک امتحان کنید. مسیرهای مقصد `Unverified` تا اجرا.
