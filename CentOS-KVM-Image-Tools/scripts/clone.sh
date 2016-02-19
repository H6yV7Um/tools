virt-install \
--name "centos_vm_new" \
--cpu host \
--vcpus 1 \
--ram 1024 \
--os-type=linux \
--os-variant=rhel6 \
--disk path=/var/lib/libvirt/images/centos_vm_new.qcow2 \
--nographics \
--force \
--import \
--noreboot \
--noautoconsole 



#  145  virt-sysprep --script set_ip.sh --root-password password:changeme1122  -d centos_vm_new
#  146  virt-sysprep --script /home/xiong/set_ip.sh --root-password password:changeme1122  -d centos_vm_new
#  147  virt-sysprep --script /home/xiong/set_ip.sh --password root:changeme1122 -d centos_vm_new
#  148  virt-sysprep --script /home/xiong/set_ip.sh --password root:password:changeme1122 -d centos_vm_new
#  149  virt-sysprep --script /home/xiong/set_ip.sh --password root:password:changeme1122 --enable script -d centos_vm_new
#  150  virt-sysprep --script /home/xiong/set_ip.sh --password root:password:changeme1122 --enable script -q -n -a /var/lib/libvirt/images/centos_vm_new.qcow2
#  151  virt-sysprep --script /home/xiong/set_ip.sh  --enable script -q -n -a /var/lib/libvirt/images/centos_vm_new.qcow2
#  152  virt-sysprep --script /home/xiong/test.sh  --enable script -q -n -a /var/lib/libvirt/images/centos_vm_new.qcow2
#  153  virt-sysprep --enable script --script /home/xiong/test.sh  -q -n -a /var/lib/libvirt/images/centos_vm_new.qcow2
#
virt-sysprep -a /var/lib/libvirt/images/centos_vm_new.qcow2 --firstboot /home/xiong/set_ip.sh

