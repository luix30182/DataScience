import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getMinim(d):
  min = 100
  for x in d:
    if d[x][0] < min:
      min = d[x][0]
  return x

def getMax(d):
  max = 0
  for x in d:
    if d[x][0] > max:
      max = d[x][0]
  return x

data = pd.read_csv(sys.argv[1])
ratings = []

for x in range(len(data['movieId'])):
  t = []
  t.append(int(data['movieId'][x]))
  t.append(float(data['rating'][x]))
  t.append(data['timestamp'][x]) 
  ratings.append(t)

ratings = sorted(ratings, key=lambda x: x[0])

drated = {}

for x in ratings:
  try:
    drated[x[0]][0] += x[1]
    if drated[x[0]][1] > x[2]:
      drated[x[0]][1] = x[2]
    if drated[x[0]][2] < x[2]:
      drated[x[0]][2] = x[2]
    drated[x[0]][3] += 1
  except:
    drated[x[0]] = [x[1],x[2],x[2],1]

for x in drated:
  drated[x][0] = drated[x][0]/drated[x][3]

for x in drated:
    print(x,drated[x])
