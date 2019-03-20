#Use with Flights Dataset/flights
import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])

data = data.drop(columns=['YEAR','MONTH','DAY','DAY_OF_WEEK','FLIGHT_NUMBER','TAIL_NUMBER','TAXI_OUT','WHEELS_OFF','DESTINATION_AIRPORT','SCHEDULED_DEPARTURE','DEPARTURE_DELAY','SCHEDULED_TIME','DISTANCE','ELAPSED_TIME','WHEELS_ON','TAXI_IN','SCHEDULED_ARRIVAL','ARRIVAL_TIME','AIR_TIME','DIVERTED','CANCELLED','CANCELLATION_REASON','WEATHER_DELAY','LATE_AIRCRAFT_DELAY','AIR_SYSTEM_DELAY','SECURITY_DELAY','DEPARTURE_TIME'])

# data = data.dropna()

data = data.groupby(['AIRLINE']).first()
data2 = data.index.values
 
airline = data.index.values
delays = data['ARRIVAL_DELAY'].values

plt.plot(airline,delays, label="Average Delay per Airline")
plt.grid(True)
plt.xlabel('Airport')
plt.ylabel('Delay', fontsize=15)
plt.xticks(rotation=90)
plt.title('Delay per Airline',fontsize=20)
plt.legend(loc='upper left')
plt.show()