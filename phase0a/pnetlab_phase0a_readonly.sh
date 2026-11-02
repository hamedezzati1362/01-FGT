#!/bin/sh
# Phase 0A - PNetLab (Linux) READ-ONLY discovery. Changes NOTHING. Does NOT read config.php or password files.
# Run from your PC:
#   ssh root@192.168.88.199 'sh -s' < pnetlab_phase0a_readonly.sh > pnetlab_phase0a.txt
sec() { echo; echo "=== $1 ==="; }
sec "OS";             date; hostname; cat /etc/os-release | head -5; uname -a
sec "PNETLAB PKG";    dpkg -l 2>/dev/null | grep -iE "pnet|unetlab|eve" | awk '{print $2, $3}'
sec "CPU";            lscpu | grep -E "Model name|^CPU\(s\)|Thread|Core|Socket|Hypervisor|Virtualization|Flags" | cut -c1-200
sec "NESTED VIRT";    echo "vmx/svm flag count: $(grep -cE '(vmx|svm)' /proc/cpuinfo)"; ls -l /dev/kvm 2>&1; lsmod | grep -E "^kvm"
sec "MEMORY";         free -m; cat /proc/swaps
sec "DISK";           df -h; lsblk
sec "IMAGES qemu";    ls /opt/unetlab/addons/qemu 2>&1
sec "IMAGES iol";     ls /opt/unetlab/addons/iol/bin 2>&1
sec "IMAGES dynamips"; ls /opt/unetlab/addons/dynamips 2>&1
sec "IMAGE SIZES";    du -sh /opt/unetlab/addons/qemu/* 2>/dev/null
sec "LABS DIR SIZE";  du -sh /opt/unetlab/labs /opt/unetlab/tmp 2>/dev/null
sec "NETWORK";        ip -br addr; ip route; ip -br link | grep -E "pnet|vnet|nat" 
sec "BRIDGES";        (brctl show 2>/dev/null || bridge link 2>/dev/null) | head -40
sec "RUNNING NODES";  echo "qemu processes: $(pgrep -c qemu 2>/dev/null)"; pgrep -c iol 2>/dev/null
sec "SERVICES";       systemctl list-units --type=service --state=running 2>/dev/null | grep -iE "apache|mysql|maria|docker|ssh|ntp|chrony" 
sec "TIME SYNC";      timedatectl 2>/dev/null | head -8
sec "END"
