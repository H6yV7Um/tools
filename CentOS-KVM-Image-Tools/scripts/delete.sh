
virsh destroy centos_vm_new
virsh undefine centos_vm_new
rm /var/lib/libvirt/images/centos_vm_new.qcow2  -rf
#cp /var/lib/libvirt/images/base_centos_vm.qcow2 /var/lib/libvirt/images/centos_vm_new.qcow2

