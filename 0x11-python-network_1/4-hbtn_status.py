#!/usr/bin/python3
import requests
""" Getting web content with the requests model """

if __name__ == '__main__':
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
