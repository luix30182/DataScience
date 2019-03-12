import sys
import pandas as pd

movies = pd.read_csv(sys.argv[1])
categorie = sys.argv[2]
ratings = pd.read_csv(sys.argv[3])
n = int(sys.argv[4])

moviesList = {}
for x in range(len(movies['genres'])):
  try:
    moviesList[movies['movieId'][x]] = [movies['title'][x],movies['genres'][x].split('|')]
  except:
    print('error')

listInCat = []
for x in moviesList:
  if categorie in moviesList[x][1]:
    t = [x,moviesList[x]]
    listInCat.append(t)

ratingsList = []

for x in listInCat:
  name = x[1][0]
  id = x[0]
  c = 0
  for y in ratings['movieId']:
    if y == id:
      rate = ratings['info'][c].split(',')[0]
      numer = ratings['info'][c].split(',')[-1]
      ratingsList.append([int(x[0]),float(rate[1::]),int(numer[0:-1]),name])
    c += 1

ratingsList = sorted(ratingsList,key=lambda x: x[1])
ratingsList = ratingsList[::-1]
f = []

# for x in ratingsList:
#   print(x)

for x in range(0,n):
    print(ratingsList[x])