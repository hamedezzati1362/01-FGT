# Runbook — Golden Ubuntu 22.04 (از دیسک NAS-BKP1 یا نصب تمیز)

> قانون: روی خود NAS (`NAS-BKP1`) هیچ پاک‌سازی/Generalize انجام نشود؛ فقط روی **کپی** دیسک.

## ۱. پیش‌شرط
نصب Ubuntu تمام، یک‌بار بوت، `sudo apt update && sudo apt -y upgrade && sudo apt -y install open-vm-tools`، سپس `sudo poweroff`.

## ۲. کپی دیسک (SSH ESXi)
```bash
mkdir -p /vmfs/volumes/ds01-ssd/GOLD-UBU2204
vmkfstools -i /vmfs/volumes/ds02-ssd/NAS-BKP1/NAS-BKP1.vmdk -d thin /vmfs/volumes/ds01-ssd/GOLD-UBU2204/GOLD-UBU2204.vmdk
```

## ۳. ساخت VM Golden (Wizard)
- نام `GOLD-UBU2204`، Ubuntu Linux (64-bit)، **همان Firmware (BIOS/EFI) که `NAS-BKP1` دارد**، 2 vCPU، 2 GB، **یک** کارت `VM Network` با **Connect خاموش**، بدون USB، دیسک پیش‌فرض را حذف و **Existing hard disk** = کپی بالا.

## ۳.۱ تنظیم داخل کپی (با کارت قطع)
```bash
sudo hostnamectl set-hostname ubuntu-gold
sudoedit /etc/netplan/50-cloud-init.yaml   # کارت اول: dhcp4: true ، IP ثابت و gateway حذف
sudo cloud-init clean
sudo truncate -s 0 /etc/machine-id
sudo rm -f /var/lib/dbus/machine-id
history -c
sudo poweroff
```
(Connect کارت را **فعال نکنید** تا Golden خاموش بماند؛ IP ثابت `192.168.88.198` نباید با NAS تداخل کند.)

## ۴. هر Clone جدید
```bash
mkdir -p /vmfs/volumes/ds02-ssd/<NAME>
vmkfstools -i /vmfs/volumes/ds01-ssd/GOLD-UBU2204/GOLD-UBU2204.vmdk -d thin /vmfs/volumes/ds02-ssd/<NAME>/<NAME>.vmdk
```
VM جدید با Wizard (همان Firmware) + Existing disk؛ بعد از بوت:
```bash
sudo hostnamectl set-hostname <NAME>
sudo rm -f /etc/ssh/ssh_host_* && sudo dpkg-reconfigure openssh-server
```
