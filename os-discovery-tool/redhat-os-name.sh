#!/bin/bash
cat /etc/redhat-release 2>/dev/null | awk '{print $1" "$2" "$3" "$4" "$7}' 
