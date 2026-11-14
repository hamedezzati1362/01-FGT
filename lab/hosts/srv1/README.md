# SRV1 (DHCP + TFTP)
- Run `bash /opt/lab/srv1/setup-srv1.sh` after every boot of the node.
- Watch leases:  `tail -f /var/lib/dhcp/dhcpd.leases`   and   `journalctl -u isc-dhcp-server -f`
- TFTP root `/srv/tftp` (created with `--create` so switches may upload files).
- Fault F10: `cp /opt/lab/srv1/dhcpd-FAULT.conf /etc/dhcp/dhcpd.conf && systemctl restart isc-dhcp-server`
  Restore: `cp /opt/lab/srv1/dhcpd.conf /etc/dhcp/dhcpd.conf && systemctl restart isc-dhcp-server`
- Fallback if you have no Linux DHCP: use Cisco pools on FW-RTR (see 00-README, section "Fallback").
