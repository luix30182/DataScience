import sys
import pandas as pd
import numpy as np

def getShannon(d,n):
  s = 0
  for x in d.values():
    f = x/n
    l = np.log2(f)
    r = f * l
    s += r
  return s*-1

data = pd.read_csv(sys.argv[1])
col = sys.argv[2]

endata = data[col].values

datat = {}

for x in endata:
  try:
    datat[x] += 1
  except:
    datat[x] = 1

print(getShannon(datat,len(endata)))