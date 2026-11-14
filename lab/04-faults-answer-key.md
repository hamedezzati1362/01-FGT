# کلید جواب خرابی‌ها — **بعد از تلاش خودتان باز کنید**
شماره‌ها تصادفی‌اند (seed ثابت). برای هر خرابی: علامت، دستور تشخیص، علت، راه‌حل. فایل رفع: `configs/solutions/Snn.cfg`.

## F01 — DHCP reservation in the wrong scope  (اعمال روی: SRV1)
- **علامت:** HOST2 PC gets a random address from the pool instead of its reserved 192.168.103.62 (a firewall rule / printer mapping by IP fails).
- **دستورهای تشخیص:**
```
HOST2: ip -br addr show eth0   (not .62)
SRV1: grep -n "pc2" /etc/dhcp/dhcpd.conf   (reservation sits under the 104 subnet)
SRV1: tail /var/lib/dhcp/dhcpd.leases
```
- **علت:** The reservation block for that MAC was written inside the VLAN 104 scope (typo) instead of VLAN 103.
- **راه‌حل:** move the host block to the 103 scope; restart dhcpd; renew on the client.

## F02 — VTP higher revision (second-hand switch)  (اعمال روی: MINI-SW + ACC3)
- **علامت:** Within seconds many VLANs vanish from CORE/DIST/ACC (show vlan brief nearly empty); users lose DHCP/ports go inactive.
- **دستورهای تشخیص:**
```
CORE# show vtp status   (Revision jumped; "Number of existing VLANs" dropped)
CORE# show vlan brief
CORE# show cdp neighbors   (unknown MINI-SW behind ACC3)
```
- **علت:** A switch with the same VTP domain/password and a higher revision number was connected; the VTP server accepted its (smaller) VLAN database.
- **راه‌حل:** 1) disconnect/shut the link 2) MINI-SW -> vtp mode transparent 3) re-create VLANs on CORE (from backup) 4) check clients re-sync.
- **محدودیت شبیه‌ساز:** Depends on VTP being really implemented in viosl2 (Module M00 tests this). If not, read the sample output in M03 and the answer key.
- **کابل:** CABLE: MINI-SW Gi0/0 <-> ACC3 Gi1/0

## F03 — Port-Security err-disabled after a desk move  (اعمال روی: ACC3)
- **علامت:** HOST3 (PC+Phone) offline; the port LED/state is err-disabled.
- **دستورهای تشخیص:**
```
ACC3# show interfaces status err-disabled
ACC3# show port-security interface gi0/1
ACC3# show logging | include PSECURE|ERR_DISABLE
```
- **علت:** maximum 1 but two MACs (PC + phone) appeared (or an old sticky MAC from the previous desk remained).
- **راه‌حل:** fix the cause (maximum 3, clear old sticky) then shutdown / no shutdown.
- **محدودیت شبیه‌ساز:** Simulation limit: the Violation action may not trigger in this image (earlier probe: config OK, behaviour untested). If the port stays up, use the sample output in M05 and run the recovery commands anyway.

## F04 — Phone does not come up (voice VLAN not allowed on uplink)  (اعمال روی: ACC1)
- **علامت:** HOST1 PC works but the phone identity (eth0.97) gets no address.
- **دستورهای تشخیص:**
```
ACC1# show interfaces trunk   (97 missing)
ACC1# show mac address-table interface gi0/1   (phone MAC in VLAN 97 seen but no reply)
HOST1: ip -br addr show eth0.97
```
- **علت:** VLAN 97 removed from the allowed list of the ACC1 uplink.
- **راه‌حل:** switchport trunk allowed vlan add 97

## F05 — Uplink shutdown  (اعمال روی: DIST)
- **علامت:** Everything behind ACC2 is dead: HOST2, its management IP .12, CDP neighbor gone.
- **دستورهای تشخیص:**
```
DIST# show interfaces status | include Gi0/2   (disabled)
DIST# show cdp neighbors   (ACC2 missing)
DIST# show logging | include UPDOWN
```
- **علت:** Administratively shut uplink.
- **راه‌حل:** no shutdown (after asking why it was shut).

## F06 — VLAN missing from trunk allowed list  (اعمال روی: DIST)
- **علامت:** HOST1 PC (VLAN 101) gets no IP; its phone (VLAN 97) works. Other VLANs fine.
- **دستورهای تشخیص:**
```
DIST# show interfaces trunk   (VLAN 101 missing in "allowed" of Gi0/1)
DIST# show spanning-tree vlan 101
```
- **علت:** A trunk allowed-list edit removed VLAN 101 on the DIST->ACC1 link.
- **راه‌حل:** DIST(config-if)# switchport trunk allowed vlan add 101   (always "add")

## F07 — VLAN does not exist (port inactive)  (اعمال روی: ACC1)
- **علامت:** The Wi-Fi access point on ACC1 Gi0/3 is offline; port shows inactive.
- **دستورهای تشخیص:**
```
ACC1# show interfaces status | include Gi0/3   (inactive)
ACC1# show vlan brief   (VLAN 106 absent)
ACC1# show running-config interface gi0/3
```
- **علت:** Access VLAN number typed that does not exist in the VTP database.
- **راه‌حل:** use the right VLAN (105), or create the VLAN on CORE if it was really needed.

## F08 — Duplex mismatch (a-half) on a user port  (اعمال روی: ACC2)
- **علامت:** User complains "network is slow / file copy stalls"; link is up. (Real hardware: CRC/late-collision counters grow. Simulator: may only show the forced speed/duplex.)
- **دستورهای تشخیص:**
```
ACC2# show interfaces status | include Gi0/1
ACC2# show interfaces gi0/1 | include duplex|CRC|collision|drops
```
- **علت:** One side forced to half/100 while the other side auto -> mismatch.
- **راه‌حل:** speed auto / duplex auto on both ends (or identical forced values).
- **محدودیت شبیه‌ساز:** Simulation limit: virtual NICs do not generate collisions/CRC. Use the sample output in 03-modules/M04 for the real-hardware picture.

## F09 — Native VLAN mismatch  (اعمال روی: DIST)
- **علامت:** Log noise (CDP/STP), occasional odd connectivity for untagged/VLAN 1 traffic behind ACC3; VLAN 2 and VLAN 1 mix.
- **دستورهای تشخیص:**
```
DIST# show interfaces trunk   (native 2 vs 1)
DIST# show logging | include NATIVE|PVID
DIST# show cdp neighbors detail | include Native
```
- **علت:** Native VLAN differs on the two ends of the trunk.
- **راه‌حل:** make both ends native 1 (or both the same value).

## F10 — Loop via a small switch (BPDU Guard missing)  (اعمال روی: MINI-SW + ACC3)
- **علامت:** Within seconds the network crawls; CPU high on switches; MAC-flap messages; VLAN 107 hosts unreachable.
- **دستورهای تشخیص:**
```
ACC3# show processes cpu sorted | head
ACC3# show logging | include MACFLAP
ACC3# show interfaces counters | include Gi1/
ACC3# show spanning-tree vlan 107
```
- **علت:** Two cables from an unmanaged/STP-less small switch to two edge (PortFast) ports; no BPDU Guard.
- **راه‌حل:** shut one cable at once; enable BPDU Guard on edge ports; the small switch must run STP or not be loopable.
- **محدودیت شبیه‌ساز:** Loop storms are heavy: apply, observe 20 seconds, fix immediately. Never run this on a real network.
- **کابل:** CABLE: MINI-SW Gi0/0 <-> ACC3 Gi1/0 ; MINI-SW Gi0/1 <-> ACC3 Gi1/1

## F11 — 10/100 Mbps link instead of 1000 (CRC suspicion)  (اعمال روی: ACC3)
- **علامت:** Everything behind ACC3 is slow; uplink shows 100 instead of 1000.
- **دستورهای تشخیص:**
```
ACC3# show interfaces status | include Gi0/0   (a-100 / 100 instead of a-1000)
ACC3# show interfaces gi0/0 | include BW|rate|CRC
```
- **علت:** Forced/negotiated 100 Mbps on an uplink (bad cable or manual speed).
- **راه‌حل:** speed auto; replace cable if it renegotiates down on real hardware.
- **محدودیت شبیه‌ساز:** Simulation limit: no physical layer; the "speed" keyword is accepted but throughput may not change.

## F12 — VLAN without DHCP relay (helper-address missing)  (اعمال روی: FW-RTR)
- **علامت:** HOST2 PC (VLAN 103) gets NO address (Windows would show 169.254.x.x). Gateway .254 still answers ping from a static IP.
- **دستورهای تشخیص:**
```
FW-RTR# show running-config interface Gi0/0.103   (no ip helper-address)
HOST2: pc-only.sh -> no lease; on SRV1: tcpdump -ni eth0 port 67  (no DISCOVER arrives)
```
- **علت:** Relay line missing on the gateway sub-interface of that VLAN.
- **راه‌حل:** FW-RTR(config-subif)# ip helper-address 192.168.90.11
