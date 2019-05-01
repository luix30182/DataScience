import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# python suicide.py "..\..\..\Downloads\suicides1985-2016.csv"
# tendencias por país, rango de edad

def getCountryName(name, names):
  name = name.lower()
  for x in dataGroupByCountry.iteritems():
    if(x[0].lower() == name):
      return x[0]
  return ''

data = pd.read_csv(sys.argv[1])
try:
  option = int(sys.argv[2])
except: 
  option = 1

data = data.drop(columns=['HDI for year','gdp_per_capita ($)',' gdp_for_year ($) '])
dataGroupByAge = data.groupby(['country','age'])['suicides_no'].mean() #Agrupa por rango de edades
dataGroupBySex = data.groupby(['country','sex'])['suicides_no'].mean()  #agrupa por genero
dataGroupByYear = data.groupby(['country','year'])['suicides_no'].mean()  #agrupa por año
dataGroupByCountry = data.groupby(['country'])['suicides_no'].mean()  #agrupa por pais
# data = data.groupby(['country','year','sex','age'])['suicides_no'].mean()

if option == 1:
  # Plot by Country
  try:
    country = getCountryName(sys.argv[3], dataGroupByCountry)
  except:
    country = ''

  if len(country) > 0:
    print('Promedio de suicidios: ',dataGroupByCountry[country])
  else:
    names = dataGroupByCountry.index
    values = dataGroupByCountry.values

    plt.plot(names,values)
    plt.grid(True)
    plt.title('Promedio de suicidios por País',fontsize=20)
    plt.ylabel('Promedio de suicidios', fontsize=15)
    plt.xlabel('País')
    plt.xticks(rotation=90)
    plt.show()

elif option == 2:
  #plot by sex
  try:
    country = getCountryName(sys.argv[3], dataGroupByCountry)
  except:
    country = ''
  if len(country) > 0:
    print('Promedio de suicidios: ',dataGroupBySex[country])
  else:
    dataSexNames = dataGroupBySex.index
    dataSexValues = dataGroupBySex.values
    databySex = dict()
    for i,x in enumerate(dataSexNames):
      try:
        databySex[x[0]].update({x[1] : dataSexValues[i]})
      except:
        databySex[x[0]] = {x[1] : dataSexValues[i]}

    Countrynames = list()
    males = list()
    females = list()

    for x,y in databySex.items():
      try:
        if y['male'] > 10 or y['female'] > 10:
          Countrynames.append(x)
          males.append(y['male'])
          females.append(y['female'])
      except:
        print('Error')
    print(len(males))
    print(len(females))
    # plot
    fig, ax = plt.subplots()
    bar_width = 0.45
    opacity = 0.8
    index = np.arange(len(Countrynames))
    print(index)
    indexticks = [x + (bar_width/2) for x in index]
    rects1 = plt.bar(index, males, bar_width,
    alpha=opacity,
    color='b',
    label='Males')

    rects2 = plt.bar(index + bar_width, females, bar_width,
    alpha=opacity,
    color='g',
    label='Females')

    plt.xlabel('Genero por País')
    plt.ylabel('Suicidios')
    plt.title('Suicidios por genero')
    plt.xticks(indexticks,Countrynames)
    plt.xticks(rotation=90)
    plt.legend()

    plt.tight_layout()
    plt.show()
      