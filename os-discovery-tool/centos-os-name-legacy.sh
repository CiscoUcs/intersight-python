#!/bin/bash
cat /etc/centos-release 2>/dev/null | awk '{print $1" "$3}'
