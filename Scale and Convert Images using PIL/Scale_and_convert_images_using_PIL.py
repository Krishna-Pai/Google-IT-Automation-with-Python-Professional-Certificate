#!/usr/bin/env python3

import os, glob
from PIL import Image

newsize = 128, 128

for file in glob.glob("ic_*"):
       im = Image.open(file).convert('RGB')
       im.rotate(270).resize((newsize)).save("/opt/icons/" + file, "JPEG")