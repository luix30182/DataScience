import sys
import pandas as pd
import numpy as np

def getShannon(n):
  m = 1/n
  l = np.log(n)
  print('El valor de n es:',n) 
  print('El valor del log es:',l)
  return n*m*l

data = pd.read_csv(sys.argv[1])

data = data.drop(columns=['YEAR','MONTH','DAY','DAY_OF_WEEK','FLIGHT_NUMBER','TAIL_NUMBER','TAXI_OUT','WHEELS_OFF','DESTINATION_AIRPORT','SCHEDULED_DEPARTURE','DEPARTURE_DELAY','SCHEDULED_TIME','DISTANCE','ELAPSED_TIME','WHEELS_ON','TAXI_IN','SCHEDULED_ARRIVAL','ARRIVAL_TIME','AIR_TIME','DIVERTED','CANCELLED','CANCELLATION_REASON','WEATHER_DELAY','LATE_AIRCRAFT_DELAY','AIR_SYSTEM_DELAY','SECURITY_DELAY','DEPARTURE_TIME'])

endata = data['ARRIVAL_DELAY'].values
# print(endata)

print(getShannon(len(endata)))