#!/bin/bash
used_mem=$(free -m | awk ' /Mem:/{print $3} ')
total_mem=$(free -m | awk '/Mem:/{print $2} ')
usage_percent=$((used_mem *100 /total_mem))
echo "Memory usage:$used_mem MB /$total_mem MB ($usage_percent%)"
if [ "$usage_percent" -gt 80 ]; then  
       echo "ALERT :memory usage is above 80%!"
fi
