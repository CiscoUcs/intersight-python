#!/bin/bash
cat /etc/*-release 2>/dev/null | grep -i ^ID= | head -n1 | awk -F"=" '{print $2}'| xargs
