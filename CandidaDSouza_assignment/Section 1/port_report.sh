#!/bin/bash

# check if IP is given
if [ "$1" == "" ]; then
    echo "Usage: ./port_report.sh <IP>"
    exit
fi

ip=$1
date=$(date +%F)
file="scan_${ip}_${date}.txt"

echo "Scanning $ip..." > $file

open_count=0

# scan ports
for port in 21 22 80 443 3306
do
    timeout 1 bash -c "echo > /dev/tcp/$ip/$port" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "Port $port OPEN" >> $file
        open_count=$((open_count + 1))
    else
        echo "Port $port CLOSED" >> $file
    fi
done

echo "------------------" >> $file
echo "Total Open Ports: $open_count" >> $file

echo "Scan complete"
echo "Total Open Ports: $open_count"
