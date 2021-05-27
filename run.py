#! /usr/bin/env python3
import os
import requests
from string import ascii_letters


source_path = os.path.abspath("supplier-data/descriptions")

strip_letters = lambda s: "".join([c for c in s if c not in ascii_letters])
fp_to_img = lambda s: s.replace(".txt",".jpeg")

results = list()

for fp in os.listdir(source_path):
  print(fp)
  with open(os.path.join(source_path, fp), 'rt') as textfile:
    record_ = [l for l in textfile.readlines()]
    record= {"name":record_[0].replace("\n",""),
             "weight": int(strip_letters(record_[1])),
             "description":record_[2].replace("\n",""),
             "image_name":fp_to_img(fp)
             }
    #print(record)
    #json_lst.append(record)
    results.append(requests.post("http://34.70.151.237/fruits/", data=record))

print(results)

