#!/bin/bash
# Send GET request with data that would otherwise be sent as a post request
curl -sGH "X-School-User-Id=98" "$1"
