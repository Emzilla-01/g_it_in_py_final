#!/usr/bin/env python3
from PIL import Image

import os

source_path = 'supplier-data/images_o'
dest_path = 'supplier-data/images'

if not os.path.exists(dest_path):
  os.mkdir(dest_path)
print(os.listdir(source_path))

for p in os.listdir(source_path):
  if p[-4:]!= "tiff":
    continue
  img_ = Image.open(os.path.join(source_path,p))
  img_ = img_.resize((600,400))
  img_ = img_.convert("RGB")
  img_ = img_.save(os.path.join(dest_path,p.replace("tiff","jpeg")), format="jpeg")
