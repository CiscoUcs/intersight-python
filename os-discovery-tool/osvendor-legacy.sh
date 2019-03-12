#!/bin/bash
cat /etc/*-release | grep "Linux" | head -n 1 | awk '{print $1" "$2}'
