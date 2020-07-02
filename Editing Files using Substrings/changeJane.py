#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1],"r")
for line in f.readlines():
  old = line.strip()
  new = old.replace("jane","jdoe")
  subprocess.run(["mv", old , new])
f.close()
