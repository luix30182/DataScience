import sys,re,csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(sys.argv[1])

allCats = {}
for x in data['genres']:
    x = x.split('|')
    for y in x:
        try:
            allCats[y] += 1
        except:
            allCats[y] = 1
categories = []
moviesCat = []
for x in allCats:
    categories.append(x)
    moviesCat.append(allCats[x])

movie = []
year = []
for x in range(len(data['title'])):
    try:
        y = data['title'][x].split('(')[0]
        movie.append(y)
        z = int(data['title'][x].split('(')[-1][:-1])
    except:
        z = 0
    year.append(z)

print('Total de categorias: {0}'.format(len(categories)))

listYears = {}
for x in year:
    try:
        listYears[x] += 1
    except:
        listYears[x] = 1
listYears = dict(sorted(listYears.items()))

for x in listYears:
    print('Year: {0} #of movies {1}'.format(x,listYears[x]))

listYearsC = dict(sorted(listYears.items()))
del listYearsC[0]
print('Peligulas sin year: {0}'.format(min(listYears.items(), key=lambda x: x[0])[1]))
print('Peligulas last year: {0}'.format(min(listYearsC.items(), key=lambda x: x[0])[0]))
print('Peligulas most recent year: {0}'.format(max(listYearsC.items(), key=lambda x: x[0])[0]))
# Plot
labels = []
for x in range(len(categories)):
    labels.append(categories[x] + ' ' + str(moviesCat[x]))
colormap = plt.cm.nipy_spectral 
colors = [colormap(i) for i in np.linspace(0, 1,len(categories))]
patches, texts = plt.pie(moviesCat, colors=colors, shadow=False, startangle=90)
plt.legend(patches, labels, loc="best")
plt.suptitle('Categorias de peliculas :#{0}'.format(len(categories)))
plt.axis('equal')
plt.tight_layout()
plt.show()