#!/bin/bash
# Simulates ONE cable with TWO identities: PC (untagged) + IP Phone (tagged VLAN 97, different MAC).
# Usage: bash phone-pc-sim.sh <N>      N = 1,2,3 (matches HOST1..HOST3)
set -e
N=${1:?usage: phone-pc-sim.sh N}
PCMAC=02:aa:00:00:0${N}:01
PHMAC=02:bb:00:00:0${N}:97
pkill dhclient 2>/dev/null || true
ip link set eth0 down; ip link set eth0 address $PCMAC; ip link set eth0 up
ip link del eth0.97 2>/dev/null || true
ip link add link eth0 name eth0.97 type vlan id 97
ip link set eth0.97 down; ip link set eth0.97 address $PHMAC; ip link set eth0.97 up
echo "[PC]    eth0    MAC $PCMAC  (untagged -> access VLAN)"
echo "[PHONE] eth0.97 MAC $PHMAC  (tag 97    -> voice VLAN)"
dhclient -v -1 eth0 || echo "PC: no DHCP lease (check relay/VLAN/trunk)"
dhclient -v -1 -pf /run/dhclient-97.pid -lf /var/lib/dhcp/dhclient-97.leases eth0.97 || echo "PHONE: no DHCP lease (voice VLAN/relay/trunk)"
ip -br addr show eth0 eth0.97
