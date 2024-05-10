#!/bin/bash
# View all method allowed by the URI (-i includes the http response header in the code)
curl -i -sX  OPTIONS "$1" | grep 'Allow' | cut -d : f2 | cut -b 2-
