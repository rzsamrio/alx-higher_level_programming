#!/usr/bin/bash
# Send HTTP GET request to server ip to obtain the byte size of the response body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}' 
