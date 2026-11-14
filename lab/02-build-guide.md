# ساخت قدم‌به‌قدم داخل PNETLab (حدود ۱۵ دقیقه)
۱) Lab جدید بسازید: `Workshop-CiscoDaily` (Path دلخواه). **هیچ Cloud/pnet0 وصل نکنید** (ایزوله بماند).
۲) گره‌ها (Add an object → Node):
| نام | Template | Image | RAM | Ethernet |
|---|---|---|---|---|
| CORE, DIST, ACC1, ACC2, ACC3, MINI-SW | Cisco vIOS Switch (`viosl2`) | `viosl2-adventerprisek9-m.ssa.high_iron_20200929` | 1024 | 8 |
| FW-RTR | Cisco vIOS Router (`vios`) | `vios-adventerprisek9-m.spa.159-3.m9` | 1024 | 4 |
| SRV1, HOST1, HOST2, HOST3 | Linux | `linux-ubuntu2204-lab` | 512-1024 | 1 |
۳) اتصال‌ها را دقیقاً طبق جدول `01-topology.md` بکشید (یک کابل = کلیک روی آیکن اتصال گره و کشیدن روی گره مقابل، انتخاب پورت).
۴) فعلاً MINI-SW را روشن کنید ولی **کابل آن را نکشید**.
۵) همه را Start کنید؛ ۲ تا ۳ دقیقه صبر (Console هر گره: دوبار کلیک → Telnet).
۶) Configها را Paste کنید به این ترتیب: CORE ← DIST ← ACC1 ← ACC2 ← ACC3 ← FW-RTR (دسته‌های ≤ 25 خط؛ بخش «تزریق» در README).
۷) روی SRV1: `bash /opt/lab/srv1/setup-srv1.sh` ؛ روی HOST1 تا 3: `bash /opt/lab/pc-phone/phone-pc-sim.sh <N>` (N=1,2,3).
۸) بررسی سریع:
```
CORE# show vlan brief
ACC1# show vtp status
ACC1# show interfaces trunk
FW-RTR# show ip interface brief
HOST1:  ip -br addr
```
انتظار: روی ACC1 همان VLANهای CORE دیده شود (VTP)، Trunk بالا باشد، HOST1 در 192.168.101.61 و تلفن در 192.168.97.61.
۹) در پایان `write memory` روی همه و در PNETLab Lab را Save کنید.
**اگر چیزی بالا نیامد:** Module M01 را ببینید (Probe) و گره را نشانم بدهید؛ حدس نزنید.
