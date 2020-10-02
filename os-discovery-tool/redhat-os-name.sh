#!/bin/bash
redhat_version=$(cat /etc/*-release | grep ^VERSION | head -n1 | awk -F"=" '{print $2}' | xargs | awk -F'[ ]' '{print $1}' | xargs)
min_version=8.0
version=$(echo "$redhat_version>=$min_version" | bc) 2>/dev/null

if [[ $version -eq 1 ]];
  then
  echo $(cat /etc/redhat-release 2>/dev/null | awk '{print $1" "$2" "$3" "$4" "$6}')

else
  echo $(cat /etc/redhat-release 2>/dev/null | awk '{print $1" "$2" "$3" "$4" "$7}')
fi