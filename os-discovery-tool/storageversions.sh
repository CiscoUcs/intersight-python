#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
lshwcmd=`which lshw`
lspcicmd=`which lspci`
modinfocmd=`which modinfo`
for pciaddress in $(${lshwcmd} -C Storage 2>/dev/null | grep "pci@" | awk -F":" '{print $3":"$4}');
do
    ${lspcicmd} -v -s ${pciaddress} | grep "Kernel driver" | awk -F":" '{print $2}' | \
    xargs ${modinfocmd} 2>/dev/null| grep -i "version" | head -n1 | awk '{print $2}' | xargs;
done
