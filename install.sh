#!/bin/bash

cp findip.py /usr/share
sleep 0.5
cp ipaddr /usr/local/bin
chmod +x /usr/local/bin/ipaddr

sleep 0.5
printf "type 'ipaddr <Domain name or web url>', for use\n"

