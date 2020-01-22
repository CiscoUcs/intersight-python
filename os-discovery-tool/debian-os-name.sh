#!/bin/bash
cat /etc/*-release | grep VERSION | head -n1 | awk -F"=" '{print $2}' | xargs | awk '{print "Ubuntu "$1" "$2}'
