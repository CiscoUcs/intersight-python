#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
modinfocmd=`which modinfo`
lshwcmd=`which lshw`
found_fnic=`sudo ${lshwcmd} -C bus | grep fnic | wc -l`;
if [[ ${found_fnic} -ne 0 ]];
    then ${modinfocmd} fnic 2>/dev/null | grep "^version: "| awk '{print $2}';
fi
