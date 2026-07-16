#!/bin/bash
cat ~/slr/ssrn/pid.txt
ps aux | grep -F -f <(awk '{print $1}' ~/slr/ssrn/pid.txt) | grep -v grep
