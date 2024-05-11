#!/usr/bin/python3
""" View Header attribute content of url """
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as url:
        print(url.info()['X-Request-Id'])
