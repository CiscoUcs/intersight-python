#!/bin/bash

cat /etc/*-release | grep VERSION | head -n1 | awk -F"=" '{print $2}' | xargs | \
awk '{print "Ubuntu Server "$1" "$2}'; 
