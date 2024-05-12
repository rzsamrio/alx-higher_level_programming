#!/usr/bin/python3
""" Handle error code with GET requests """
from sys import argv
from urllib.error import HTTPError, URLError
import urllib.request

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            body = resp.read()
        print(body.decode())
    except HTTPError as err:
        print(f"Error code: {err.code}")
    except URLError as err:
        print(err.reason)
