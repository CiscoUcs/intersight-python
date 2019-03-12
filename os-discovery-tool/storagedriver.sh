#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
lshwcmd=`which lshw`
lspcicmd=`which lspci`
for pciaddress in $(${lshwcmd} -C Storage 2>/dev/null | grep "pci@" | awk -F":" '{print $3":"$4}');
do
    ${lspcicmd} -v -s ${pciaddress} | grep "Kernel driver" | awk -F":" '{print $2}' | xargs;
done
