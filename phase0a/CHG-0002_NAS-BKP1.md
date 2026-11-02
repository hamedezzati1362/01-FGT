# CHG-0002 — ساخت VM `NAS-BKP1` (NAS بکاپ و فایل‌سرور)

| فیلد | مقدار |
|---|---|
| تاریخ | 2026-11-02 |
| مجری | کاربر (ESXi Host Client) |
| تلاش ۱ | `.vmx` دستی با اسکریپت → ناموفق: «No PCIe slot available for SCSI0» (فایل دستی بدون Slotهای PCI کامل) |
| روش نهایی | ساخت با Wizard Host Client (Ubuntu Linux 64-bit، 2 vCPU، 4 GB، 40 GB Thin، `VM Network` + `PG-FGT-TRUNK`، ISO Ubuntu 22.04.5) |
| Rollback | `power.off`، `unregister`، حذف پوشه VM (فقط پس از اطمینان از مسیر) |
| درس | برای VM تازه از Wizard یا Template استفاده کنید؛ `.vmx` دستی نیازمند آگاهی از PCI/Slot است |
| وضعیت | در حال انجام |
