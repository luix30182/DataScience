import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def lzero(n):
  return [0] * n

def fillData(start,end,list):
  t = []
  if start != 1:
    t = lzero(start-1)
  t += list
  if end != 12:
    t += lzero(12-end)
  return t

data = pd.read_csv(sys.argv[1])
data = data.dropna()
data = data.drop(columns=['Station Name','Wet Bulb Temperature','Humidity','Rain Intensity','Interval Rain','Total Rain','Precipitation Type','Wind Direction','Wind Speed','Maximum Wind Speed','Barometric Pressure','Solar Radiation','Heading','Battery Life','Measurement ID','Measurement Timestamp Label'], axis=1)

data['Measurement Timestamp'] = pd.to_datetime(data['Measurement Timestamp']) 

data = data.sort_values(by=['Measurement Timestamp'])


data['date_minus_time'] = data['Measurement Timestamp'].apply( lambda data : pd.datetime(year=data.year, month=data.month, day=data.day))	

data.set_index(data["date_minus_time"],inplace=True)


# data.resample('D').mean() agrupar por dia
# data.resample('W').mean() agrupar por semana
# data.resample('M').mean() agrupar por mes
# data.resample('Y').mean() agrupar por year

yearConut = data.resample('Y').size().index.year

data = data.resample('M').mean() 
year = data.index
tavg = data.values
tavg = [x[0] for x in tavg]

dataPlotT = []
dataPlot = []
for x in yearConut:
  y = []
  w = []
  for z in range(len(year)):
    date = str(year[z]).split(' ')[0]
    yy = date.split('-')[0]
    if yy == str(x):
      y.append(date)
      w.append(tavg[z])
  dataPlot.append(y)
  dataPlotT.append(w)

monthName = ['Jan','Feb','March','April','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
idYm = list(range(len(dataPlotT[0])))

for x in range(len(dataPlotT)):
  if len(dataPlotT[x]) != 12:
    # print(dataPlotT[x])
    # print(dataPlot[x])
    start = int(dataPlot[x][0].split('-')[1])
    end = int(dataPlot[x][-1].split('-')[1])
    dataPlotT[x] = fillData(start,end,dataPlotT[x])

plt.plot(dataPlot[1],dataPlotT[0], label="2015")
plt.plot(dataPlot[1],dataPlotT[1], label="2016")
plt.plot(dataPlot[1],dataPlotT[2], label="2017")
plt.plot(dataPlot[1],dataPlotT[3], label="2018")
plt.plot(dataPlot[1],dataPlotT[4], label="2019")
plt.legend(loc='upper left')
plt.xticks(range(len(dataPlotT[1])),labels=monthName,fontsize=8)
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Temperatura Promedio en °C', fontsize=15)
plt.title('Temperatura promedio por mes de Chicago',fontsize=20)
plt.show()