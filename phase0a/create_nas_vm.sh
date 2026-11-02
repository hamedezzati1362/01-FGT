#!/bin/sh
# CHG-0002: create VM "NAS-BKP1" (Ubuntu installer ISO attached). Run on ESXi:
#   ssh root@192.168.88.3 'sh -s' < create_nas_vm.sh
# It only creates a NEW VM folder/disk and registers it. It does NOT power it on.
DS=/vmfs/volumes/ds02-ssd
ISO=/vmfs/volumes/ds01-ssd/ubuntu-22.04.5-live-server-amd64.iso
VM=NAS-BKP1
DIR=$DS/$VM
set -e
[ -d "$DS" ]  || { echo "ABORT: datastore $DS not found"; exit 1; }
[ -f "$ISO" ] || { echo "ABORT: ISO not found: $ISO"; exit 1; }
[ ! -e "$DIR" ] || { echo "ABORT: $DIR already exists"; exit 1; }
esxcli network vswitch standard portgroup list | grep -q "VM Network"   || { echo "ABORT: port group 'VM Network' missing"; exit 1; }
esxcli network vswitch standard portgroup list | grep -q "PG-FGT-TRUNK" || { echo "ABORT: port group 'PG-FGT-TRUNK' missing"; exit 1; }
mkdir -p "$DIR"
vmkfstools -c 40G -d thin "$DIR/$VM.vmdk"
cat > "$DIR/$VM.vmx" <<VMX
.encoding = "UTF-8"
config.version = "8"
virtualHW.version = "19"
displayName = "$VM"
guestOS = "ubuntu-64"
numvcpus = "2"
memSize = "4096"
scsi0.present = "TRUE"
scsi0.virtualDev = "pvscsi"
scsi0:0.present = "TRUE"
scsi0:0.fileName = "$VM.vmdk"
disk.EnableUUID = "TRUE"
ide1:0.present = "TRUE"
ide1:0.deviceType = "cdrom-image"
ide1:0.fileName = "$ISO"
ide1:0.startConnected = "TRUE"
ethernet0.present = "TRUE"
ethernet0.virtualDev = "vmxnet3"
ethernet0.networkName = "VM Network"
ethernet0.addressType = "generated"
ethernet0.startConnected = "TRUE"
ethernet1.present = "TRUE"
ethernet1.virtualDev = "vmxnet3"
ethernet1.networkName = "PG-FGT-TRUNK"
ethernet1.addressType = "generated"
ethernet1.startConnected = "TRUE"
usb_xhci.present = "TRUE"
floppy0.present = "FALSE"
svga.present = "TRUE"
bios.bootOrder = "cdrom,hdd"
bios.bootDelay = "3000"
tools.syncTime = "FALSE"
VMX
vim-cmd solo/registervm "$DIR/$VM.vmx"
echo "---- done. VM list:"; vim-cmd vmsvc/getallvms
echo "Power on with: vim-cmd vmsvc/power.on <VMID of $VM>"
