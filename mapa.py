import sys,os
import folium
import pandas as pd
from folium.plugins import HeatMap

data = pd.read_csv(sys.argv[1])

#Eliminar registro nulos
data = data.dropna()
data = data.drop(columns=[ 'ID', 'Case Number', 'IUCR','Domestic', 'Beat', 'Ward','X Coordinate', 'Y Coordinate','Updated On', 'FBI Code'], axis = 1)

# chicago = folium.Map(location=[41.864073,-87.706819], zoom_start= 11, tiles='CartoDB dark_matter')
chicago = folium.Map(location=[41.864073,-87.706819], zoom_start= 11)

# crimesLocations = data.groupby('Community Area').first()
crimesLocationsc = data.groupby(['Community Area']).size()

# print(crimesLocations)
# print('Latitud maxima: {}'.format(crimesLocations['Latitude'].max()))
# print('Latitud minima: {}'.format(crimesLocations['Latitude'].min()))
# print('Longitud maxima: {}'.format(crimesLocations['Longitude'].max()))
# print('Longitud minima: {}'.format(crimesLocations['Longitude'].min()))

#pone las marcar de las coordenadas 
for index, row in data.iterrows():
  # popupd = 'Number of crimes: {0}'.format(crimesLocationsc.get(index))
  # print(popupd)
  folium.CircleMarker([row['Latitude'], row['Longitude']],radius=15).add_to(chicago)

#crear lista de listas
# crimes = crimesLocations[['Latitude','Longitude']].values.tolist()
# chicago.add_child(HeatMap(crimes, radius=35))

chicago.save('plot_total.html')
