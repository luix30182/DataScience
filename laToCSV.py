import sys

jsonFile = sys.argv[1]

with open(jsonFile,'r') as f:
  for x in f:
    print(x)