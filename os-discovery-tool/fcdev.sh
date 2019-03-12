#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
lshwcmd=`which lshw`
lspcicmd=`which lspci`
modinfocmd=`which modinfo`
found_fnic=`sudo ${lshwcmd} -C bus | grep fnic | wc -l`;
if [[ ${found_fnic} -ne 0 ]];
    then ${modinfocmd} fnic | grep "^description: "| awk '{print $2" "$3" "$4" " $5}';
fi
