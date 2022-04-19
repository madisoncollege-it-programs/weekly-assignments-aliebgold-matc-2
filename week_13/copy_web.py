#!/usr/bin/env python3
import requests

response = requests.get("http://www.notpurple.com")

with open("my_web_file.htlm",'w') as hFile:
    hFile.write(response.text)

print("File saved successfully!")
