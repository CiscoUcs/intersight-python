#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
lshwcmd=`which lshw`
sudo ${lshwcmd} -C bus | awk '$1=="configuration:"{$1=""; print}' | grep fnic | awk '{print $1}' | awk -F"=" '{print $2}'| head -n 1
