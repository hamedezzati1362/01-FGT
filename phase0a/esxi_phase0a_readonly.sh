#!/bin/sh
# Phase 0A - ESXi READ-ONLY discovery. Changes NOTHING. Contains no passwords.
# Run from your PC (script is piped over SSH, nothing is written on the host):
#   ssh root@192.168.88.3 'sh -s' < esxi_phase0a_readonly.sh > esxi_phase0a.txt
sec() { echo; echo "=== $1 ==="; }
sec "TIME/HOST";      date; esxcli system hostname get; esxcli system time get
sec "VERSION";        vmware -vl; esxcli system version get
sec "HARDWARE";       esxcli hardware platform get; esxcli hardware cpu global get; esxcli hardware memory get
sec "CPU SUMMARY";    vim-cmd hostsvc/hostsummary | grep -E "cpuModel|numCpuPkgs|numCpuCores|numCpuThreads|cpuMhz|memorySize|overallCpuUsage|overallMemoryUsage|uptime"
sec "DATASTORES";     esxcli storage filesystem list; df -h 2>/dev/null | head -20
sec "VMFS EXTENTS";   esxcli storage vmfs extent list
sec "DISKS";          esxcli storage core device list | grep -E "Display Name:|   Size:|Is SSD:|Device Type:"
sec "PHYSICAL NICS";  esxcli network nic list
sec "VSWITCHES";      esxcli network vswitch standard list
sec "PORTGROUPS";     esxcli network vswitch standard portgroup list
sec "VMKERNEL";       esxcli network ip interface list; esxcli network ip interface ipv4 get
sec "VM LIST";        vim-cmd vmsvc/getallvms
sec "RUNNING VMS";    esxcli vm process list | grep -E "Display Name|World ID|Config File"
sec "SNAPSHOTS";      for id in $(vim-cmd vmsvc/getallvms | awk 'NR>1 && $1 ~ /^[0-9]+$/ {print $1}'); do echo "-- VM id $id"; vim-cmd vmsvc/snapshot.get $id; done
sec "PER-VM RESOURCES (cpu/ram/nested/nics)"
for id in $(vim-cmd vmsvc/getallvms | awk 'NR>1 && $1 ~ /^[0-9]+$/ {print $1}'); do
  echo "-- VM id $id"
  vim-cmd vmsvc/get.config $id | grep -E "^\s+name = |numCPU|memoryMB|nestedHVEnabled|guestFullName|networkName|vhv|virtualHW" | head -25
done
sec "END"
