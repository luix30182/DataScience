import sys, os
import pandas as pd
import folium 
from folium.plugins import HeatMap
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])

try:
  option = int(sys.argv[2])
except:
  option = 1

if option == 1:
  totalTransportByType = data.groupby(['Transport'])['Code'].count()
  dataByDisctrict = data.groupby(['District.Name','Neighborhood.Name'])['Code'].count()
  data = data.drop(columns=['Bus.Stop'])
  titlesData = list(totalTransportByType.index.values)
  values = list(totalTransportByType.values)

  print('Total del trasnportes por tipo de transporte')
  plt.bar(titlesData, values, align='center', alpha=0.5)
  plt.xticks(titlesData, titlesData)
  plt.ylabel('Tipo de transporte')
  plt.title('Total de transportes por tipos de transportes')
  plt.show()
elif option == 2:
  # MAPA
  dataCoordinates = data.dropna()
  barcelona = folium.Map(location=[41.3887901,2.1589899],tiles='Stamen Toner', zoom_start= 11)

  for x in data.iterrows():
    popup = 'Code: {0} </br> Tipo de transporte: {1} </br> Distrito: {2} </br> Colonia: {3}'.format(x[1]['Code'],x[1]['Transport'],x[1]['District.Name'],x[1]['Neighborhood.Name'])
    folium.CircleMarker([x[1]['Latitude'],x[1]['Longitude']], radius=15, popup=popup, color='#3186cc',fill=True,fill_color='#3186cc').add_to(barcelona)

  #crear lista de listas
  buss = dataCoordinates[['Latitude','Longitude']].values.tolist()
  barcelona.add_child(HeatMap(buss, radius=35))

  barcelona.save('plot_barcelona.html')