#!/usr/bin/python3
"""Make a request to https://alx-intranet.hbtn.io/status."""
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen("https://alx-intranet.hbtn.io/status") as resp:
        body = resp.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
