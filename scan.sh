#!/bin/bash
masscan 0.0.0.0/0 -p8080 --exclude 255.255.255.255 --max-rate 100000000 --open -oG - | grep 'Ports' | awk '{print $2}' > $1

