#!/bin/bash
# Request and display body if HTTP Response is 200 OK
LOG=$(curl -s -o /dev/null -w "%{http_code}" "$1"); if [ "$LOG" == 200 ]; then curl -s "$1"; fi
