#!/bin/bash

cat /etc/*-release | grep PRETTY_NAME | awk -F"=" '{print $2}' | xargs
