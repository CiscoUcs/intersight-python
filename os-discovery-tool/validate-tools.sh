#!/bin/bash

export PATH=$PATH:/sbin:/usr/sbin

lshwcmd=`which lshw 2>&1`
lspcicmd=`which lspci 2>&1`
modinfocmd=`which modinfo 2>&1`

invalid=" |'"
if [[ $lshwcmd =~ $invalid ]] || [[ $lspcicmd =~ $invalid ]] || [[ $modinfocmd =~ $invalid ]];
then
	echo "VALIDATION_FAILED";
else
	echo "VALIDATION_SUCCESS";
fi

