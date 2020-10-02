#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
lshwcmd=`which lshw`
lspcicmd=`which lspci`
gpuvendor='nvidia'

for pciaddress in $(${lshwcmd} -C Display 2>/dev/null | grep "pci@" | awk -F":" '{print $3":"$4}');
do
    displaydevice=$(${lspcicmd} -v -s ${pciaddress} | grep "Subsystem" | awk -F":" '{print $2}'| xargs);
    #If the display device contains NVIDIA
    if [[ ${displaydevice,,} =~ ${gpuvendor} ]]; then
      echo $displaydevice
    fi
done