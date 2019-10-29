#!/bin/bash
kernel=$(uname -a | awk '{print $3}' | awk -F"." '{print $(NF-1)}')
version=$(uname -a | awk '{print $3}' | awk -F"[.-]" '{print $1 "." $2 "." $3 "-" $4 ".x" }')
oracle_version=$(cat /etc/*-release | grep ^VERSION | head -n1 | awk -F"=" '{print $2}' | xargs)

if [[ $kernel == *"uek"* ]];
  then
  echo $oracle_version "(UEK "$version")"
else
  echo $oracle_version
fi
