#!/bin/bash
cat /etc/*-release | grep NAME | head -n1 | awk -F"=" '{print $2}' | xargs
