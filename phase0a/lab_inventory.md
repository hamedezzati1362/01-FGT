# Lab Inventory (ثبت‌شده توسط کاربر — بدون رمز)

> **هیچ رمزی در این فایل نیست و نباید باشد.**

| دستگاه | آدرس | یوزر | نقش/یادداشت |
|---|---|---|---|
| ESXi (`esxi01.lab.local`) | `192.168.88.3` | root | ESXi 8.0 U2؛ HPE DL360 Gen9؛ 256 GB RAM |
| PNetLab | `192.168.88.199` | root (وب: admin) | PNetLab 4.2.8؛ VM `PNETLAB` (12 vCPU، 24 GB) |
| MikroTik | `192.168.88.1` | — | Gateway/Firewall؛ WireGuard برای دسترسی از محل کار |
| **NAS-BKP1** | **`192.168.88.198`** (IP ثابت، دستی توسط کاربر) | **`admin1`** | Ubuntu Server 22.04 (VM روی ESXi)؛ NAS/بکاپ/فایل‌سرور؛ کارت دوم روی `PG-FGT-TRUNK` بدون IP |
