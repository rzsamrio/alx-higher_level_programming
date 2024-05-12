#!/usr/bin/python3
""" Getting web content with the requests model """
import requests

if __name__ == '__main__':
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
