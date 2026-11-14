#!/bin/bash
# Show state / re-request DHCP quickly (use after a desk move or fault fix)
pkill dhclient 2>/dev/null || true
ip link set eth0 up
dhclient -v -1 eth0 || echo "no lease -> 169.254?  check VLAN/relay"
ip -br addr show eth0
ip route
