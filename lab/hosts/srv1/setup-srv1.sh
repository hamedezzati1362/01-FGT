#!/bin/bash
# SRV1 setup (run as root). Packages must already exist in the image (lab is isolated, no internet):
#   isc-dhcp-server, tftpd-hpa, iproute2, tcpdump
set -e
ip addr flush dev eth0
ip addr add 192.168.90.11/24 dev eth0
ip link set eth0 up
ip route replace default via 192.168.90.254
cp /opt/lab/srv1/dhcpd.conf /etc/dhcp/dhcpd.conf
sed -i 's/^INTERFACESv4=.*/INTERFACESv4="eth0"/' /etc/default/isc-dhcp-server
mkdir -p /srv/tftp && chmod 777 /srv/tftp
sed -i 's/^TFTP_DIRECTORY=.*/TFTP_DIRECTORY="\/srv\/tftp"/; s/^TFTP_OPTIONS=.*/TFTP_OPTIONS="--secure --create"/' /etc/default/tftpd-hpa
systemctl restart isc-dhcp-server tftpd-hpa
systemctl --no-pager status isc-dhcp-server | head -5
ss -ulnp | egrep ':(67|69) '
