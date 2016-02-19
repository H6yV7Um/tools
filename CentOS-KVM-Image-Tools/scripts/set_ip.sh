
### remove eth0 and rename eth1 to eth0

#mac=`tail -n1 /etc/udev/rules.d/70-persistent-net.rules | sed 's/.*ATTR{address}=="\([^"]*\).*/\1/'`
#foot=`tail -n3 /etc/udev/rules.d/70-persistent-net.rules| sed 's/eth1/eth0/'`
#head=`head -n5 /etc/udev/rules.d/70-persistent-net.rules`

tmp_file="/tmp/qq"
echo $tmp_file

#if [ -e $tmp_file ];then
#        rm -rf $tmp_file
#fi
#head -n5 /etc/udev/rules.d/70-persistent-net.rules >> $tmp_file
#tail -n3 /etc/udev/rules.d/70-persistent-net.rules| sed 's/eth1/eth0/' >> $tmp_file
#
#cp $tmp_file /etc/udev/rules.d/70-persistent-net.rules
#
#
#### set new mac to /etc/sysconfig/network-scripts/ifcfg-eth0
#
#
#sed -i "s|\(HWADDR=\"\)[^\"]*\(.*\)|\1$mac\2|" /etc/sysconfig/network-scripts/ifcfg-eth0
#
#reboot
#
