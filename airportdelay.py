#Use with Flights Dataset/flights
import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])

data = data.drop(columns=['YEAR','MONTH','DAY','DAY_OF_WEEK','FLIGHT_NUMBER','TAIL_NUMBER','TAXI_OUT','WHEELS_OFF','DESTINATION_AIRPORT','SCHEDULED_DEPARTURE','DEPARTURE_DELAY','SCHEDULED_TIME','DISTANCE','ELAPSED_TIME','WHEELS_ON','TAXI_IN','SCHEDULED_ARRIVAL','ARRIVAL_TIME','AIR_TIME','DIVERTED','CANCELLED','CANCELLATION_REASON','WEATHER_DELAY','LATE_AIRCRAFT_DELAY','AIR_SYSTEM_DELAY','SECURITY_DELAY','DEPARTURE_TIME'])

# data = data.dropna()

airport = data['ORIGIN_AIRPORT'].values
arrival_delay = data['ARRIVAL_DELAY'].values
# arrival_delay = [0 for x in arrival_delay if type(x) is not int]
airportdict = {}
airCounter = {}
for i,x in enumerate(airport):
  try:
    if arrival_delay[i] <0 or arrival_delay[i] > 0:
      airportdict[x] += arrival_delay[i]
      airCounter[x] += 1
  except:
    if arrival_delay[i] <0 or arrival_delay[i] > 0:
      airportdict[x] = arrival_delay[i]
      airCounter[x] = 0
    else:
      airportdict[x] = 0
      airCounter[x] = 0

for x in list(airportdict):
  if type(x) is int:
    del airportdict[x]
  elif len(x) > 3:
    del airportdict[x]

delayAverage = []

for x in airportdict:
  delayAverage.append(airportdict[x]/airCounter[x])
  # print(x,airportdict[x],airCounter[x])

aiportslist = [*airportdict]

plt.plot(aiportslist,delayAverage, label="Average Delay per Airport")
plt.grid(True)
plt.xlabel('Airport')
plt.ylabel('Delay', fontsize=15)
plt.xticks(rotation=90)
plt.title('Delay per Airport',fontsize=20)
plt.legend(loc='upper left')
plt.show()