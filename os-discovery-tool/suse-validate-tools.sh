#!/bin/bash

export PATH=$PATH:/sbin:/usr/sbin

hwinfocmd=`which hwinfo 2>&1`
modinfocmd=`which modinfo 2>&1`

invalid=" |'"
if [[ $hwinfocmd =~ $invalid ]] || [[ $modinfocmd =~ $invalid ]];
then
	echo "VALIDATION_FAILED";
else
	echo "VALIDATION_SUCCESS";
fi

