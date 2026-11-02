#!/bin/sh
# CHG-0002 fix: add missing PCI bridge entries to NAS-BKP1.vmx (error: "No PCIe slot available for SCSI0").
# Run as a FILE on ESXi:  sh /tmp/fix_nas_vmx.sh
VM=NAS-BKP1
VMX=/vmfs/volumes/ds02-ssd/$VM/$VM.vmx
[ -f "$VMX" ] || { echo "ABORT: $VMX not found"; exit 1; }
ID=$(vim-cmd vmsvc/getallvms | awk -v n="$VM" '$2==n {print $1}')
[ -n "$ID" ] && { echo "unregister VM id $ID"; vim-cmd vmsvc/unregister "$ID"; }
cp "$VMX" "$VMX.bak"
if grep -q '^pciBridge0.present' "$VMX"; then
  echo "pciBridge entries already present - nothing to add"
else
  cat >> "$VMX" <<VMXADD
pciBridge0.present = "TRUE"
pciBridge4.present = "TRUE"
pciBridge4.virtualDev = "pcieRootPort"
pciBridge4.functions = "8"
pciBridge5.present = "TRUE"
pciBridge5.virtualDev = "pcieRootPort"
pciBridge5.functions = "8"
pciBridge6.present = "TRUE"
pciBridge6.virtualDev = "pcieRootPort"
pciBridge6.functions = "8"
pciBridge7.present = "TRUE"
pciBridge7.virtualDev = "pcieRootPort"
pciBridge7.functions = "8"
vmci0.present = "TRUE"
VMXADD
fi
vim-cmd solo/registervm "$VMX"
vim-cmd vmsvc/getallvms
echo "Now: vim-cmd vmsvc/power.on <VMID of $VM>"
