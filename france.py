import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_palette(sns.color_palette("Set1", n_colors=15))
# Accidentes por mes
data = pd.read_csv(sys.argv[1], encoding="ISO-8859-1")

data = data.drop(columns=['Num_Acc','hrmn','dep','gps','agg','lum','int','adr','com','lat','long'])
data.columns = ['year','month','hour','atmospheric','type collision']

accidentsByMonth = data.groupby(['year','month'])['month'].count()
dates = accidentsByMonth.index.values
dates = [(x[0]+2000,x[1]) for x in dates]
accidents = accidentsByMonth.values

years = {}
months = {}

for i,x in enumerate(dates):
  try:
    years[dates[i][0]] += 1
  except:
    years[dates[i][0]] = 1
  try:
    months[dates[i][1]] += 1
  except:
    months[dates[i][1]] = 1

yearsKey = list(years.keys())
monthsKey = list(months.keys())

dataPlot = []

i = 0
for x in yearsKey:
  n = years[x]
  t = []
  for x in range(n):
    t.append(accidents[i])
    i += 1
  dataPlot.append(t)

monthName = ['Jan','Feb','March','April','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']

for i,x in enumerate(dataPlot):
  plt.plot(monthName,dataPlot[i], label=yearsKey[i])

plt.xticks(range(len(dataPlot[0])),labels=monthName,fontsize=8)
plt.legend(loc='upper left')
plt.grid(True)
plt.xlabel('Mes')
plt.ylabel('Promedio de accidentes por mes', fontsize=15)
plt.title('Promedio de accidentes por mes en Francia',fontsize=20)
plt.show()