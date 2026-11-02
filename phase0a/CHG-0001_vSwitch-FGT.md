# CHG-0001 — ساخت vSwitch ایزوله برای دوره و اتصال کارت‌های PNetLab

| فیلد | مقدار |
|---|---|
| تاریخ | 2026-11-02 |
| مجری | کاربر (دستی روی ESXi) |
| دلیل | VM «PNETLAB» بدون Port Group معتبر بود (Port Group قبلی `PG-PNET-MGMT` حذف شده بود) → عدم دسترسی وب/SSH |
| تغییرات | 1) `vSwitch-FGT` (بدون Uplink، ۱۲۸ پورت) 2) Port Group `PG-FGT-TRUNK` با VLAN 4095 و Security: Promiscuous/MAC change/Forged transmits = Accept 3) حذف و ساخت مجدد ۲ کارت شبکه VM: Adapter 1 → `VM Network`، Adapter 2 → `PG-FGT-TRUNK` (VMXNET3) |
| دست‌نخورده | `vSwitch0`، `vmk0`، `Management Network`، MikroTik/WireGuard |
| Verification | `esxcli network vswitch standard list`، `portgroup list`، `portgroup policy security get`، وب PNetLab و SSH روی `192.168.88.199` در دسترس |
| Rollback | جدا کردن Adapter 2 از `PG-FGT-TRUNK` سپس `esxcli network vswitch standard remove --vswitch-name=vSwitch-FGT` |
| وضعیت | **موفق** |
| نکته | رمز پیش‌فرض PNetLab (روی بنر کنسول) باید در Phase 0B/ابتدای Lab تغییر کند |
