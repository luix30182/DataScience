import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])
data = data.dropna()
data = data.drop(columns=['Type','Source','DST','Tz database time zone','IATA','ICAO','Altitude','Timezone','Latitude','Longitude','Airport ID'])

airports = data.groupby(['Country'])['City'].count()

countries = airports.index.values
airpot = airports.values

plt.plot(countries,airpot, label="Number of airports")
plt.grid(True)
plt.xlabel('Countrie')
plt.ylabel('# of Airports', fontsize=15)
plt.xticks(rotation=90)
plt.title('# of Airports per Countrie',fontsize=20)
plt.legend(loc='upper left')
plt.show()