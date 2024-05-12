#!/usr/bin/python3
""" POST Data with req package """
import sys
import requests

if __name__ == '__main__':
    var = {'email': sys.argv[2]}
    req = requests.get(sys.argv[1], params=var)
    print(req.text)
