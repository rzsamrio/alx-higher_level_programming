#!/usr/bin/python3
""" Prints the Header id value of a request """
import requests
import sys

if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
