import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)
pd.set_option('display.max_colwidth',1000)
pd.set_option('display.width',1000)
#calcular lospromedios por mes y por estacion
# hacer grafica de una estacion dada por año

data = pd.read_csv(sys.argv[1])
data = data.drop(columns=['Unnamed: 0'])
if len(sys.argv) >2:
  stationId = sys.argv[2]
  averageBy = data.groupby(['station_id','year','month'])['max_temp'].mean()[stationId]
else:
  averageBy = data.groupby(['year','month'])['max_temp'].mean()
  # with pd.option_context('display.max_rows', None, 'display.max_columns', 10000):
  #   print(averageByMonth)
years = {}

for i,val  in averageBy.iteritems():
  y = i[0]
  m = i[1]
  avg = val
  try:
    years[i[0]]['months'].append(i[1])
    years[i[0]]['average'].append(val)
  except:
    years[i[0]] = {'months':[i[1]],'average':[val]}

for x in years:
  m = years[x]['months']
  avg = years[x]['average']
  if len(m) > 10:
    plt.plot(m,avg, label=x)

plt.legend(loc='upper left',ncol=4)
plt.grid(True)
if len(sys.argv) >2:
  plt.title('Temperatura promedio de ' + sys.argv[2],fontsize=20)
else:
  plt.title('Temperatura promedio por mes',fontsize=20)

plt.ylabel('Temperatura Promedio en °F', fontsize=15)
plt.xlabel('Month')
plt.show()
