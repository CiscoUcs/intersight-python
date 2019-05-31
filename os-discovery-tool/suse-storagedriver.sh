#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
hwinfocmd=`which hwinfo`
${hwinfocmd} --storage | grep Driver: | awk '{print $2}' 
