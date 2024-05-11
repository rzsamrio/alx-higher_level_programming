#!/usr/bin/python3
""" Get the content of a url
    curl equiv: `curl <url>` but with formatting """
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as url:
    body = url.read()
print("Body response:")
print("\t- type: " + str(type(body)))
print("\t- content: " + str(body))
print("\t- utf8 content: " + str(body.decode()))
