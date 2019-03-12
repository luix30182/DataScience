import sys,os
import folium
import pandas as pd
from folium.plugins import HeatMap

data = pd.read_csv(sys.argv[1])

#Eliminar registro nulos
data = data.dropna()
data = data.drop(columns=[ 'ID', 'Case Number', 'IUCR','Domestic', 'Beat', 'Ward','X Coordinate', 'Y Coordinate','Updated On', 'FBI Code'], axis = 1)

# chicago = folium.Map(location=[41.864073,-87.706819], zoom_start= 11)

crimesLocations = data.groupby('Community Area').first()
crimesLocationsc = data.groupby(['Community Area']).size()
print(crimesLocationsc)

print(crimesLocationsc.values)
# #pone las marcar de las coordenadas 
# for index, row in crimesLocations.iterrows():
#   popupd = 'Number of crimes: {0} <br> Location: {1}'.format(crimesLocationsc[row['Community Area'][index]],row['Location Description'])
#   folium.CircleMarker([row['Latitude'], row['Longitude']],radius=5,popup=popupd).add_to(chicago)

# chicago.save('plot_t.html')
