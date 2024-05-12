#!/usr/bin/python3
""" Send a POST request with encoded data to a url """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(body.decode())
