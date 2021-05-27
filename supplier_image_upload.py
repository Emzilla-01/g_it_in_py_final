#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
dest_path = "supplier-data/images/"
imgs = os.listdir(dest_path)
results = list()

for fp in imgs:
  with open(os.path.join(dest_path, fp), 'rb') as opened:
    r = requests.post(url, files={'file': opened})
    results.append(r)

