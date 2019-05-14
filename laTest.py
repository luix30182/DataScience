import os
import sys

dataDir = sys.argv[1]

for root, subFolders, files in os.walk(dataDir):
  print(root)
  print(files[0][0])
