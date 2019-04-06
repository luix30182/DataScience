import sys
import folium
import math
import pandas as pd
import xml.etree.ElementTree as ET

root = ET.parse(sys.argv[1]).getroot()
columns = ['name','cre_id','location x','location y']

mexico = folium.Map(location=[ 19.4978,-99.1269 ], zoom_start= 5)
# errors = 0 
# errorCoords = 0
for element in root:
  for x in element:
    if x.tag == 'location':
      errors += 1
      longitude = float(element.find('location').find('x').text)
      latitude = float(element.find('location').find('y').text)
      if longitude == 0 or latitude == 0:
        errorCoords += 1
        print(latitude,longitude)
      if latitude < 1:
        t = latitude
        latitude = longitude
        longitude = t

      if longitude > 1:
        if(math.floor(longitude) > 40):
          longitude = longitude * -1

      popup = 'Latitude: {} Longitude; {}'.format(latitude,longitude)
      folium.CircleMarker([float(latitude),float(longitude)],radius=5, popup=popup).add_to(mexico)
    # else: 
    #   print(element.find(x.tag).text)
mexico.save('gasolineras.html')