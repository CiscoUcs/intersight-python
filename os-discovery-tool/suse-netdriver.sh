#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
hwinfocmd=`which hwinfo`
${hwinfocmd} --network | grep Driver: | awk '{print $2}' 
