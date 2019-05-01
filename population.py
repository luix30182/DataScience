import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])
country = sys.argv[2]

data = data.set_index('Country Name')

countryData = data.loc[country,:]
countryData = countryData.dropna()

for x in countryData.iteritems():
  if not isinstance(x[1], np.float64):
    countryData = countryData.drop(labels=x[0])

years = countryData.index.values
population = countryData.values

plt.plot(years,population, label=x)

# plt.legend(loc='upper left',ncol=4)
plt.grid(True)
plt.title('Poblacion de ' + country,fontsize=20)
plt.ylabel('Poblacion', fontsize=15)
plt.xlabel('Año')
plt.show()

