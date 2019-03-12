import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])

data = data.dropna()
data = data.drop(columns=['113 Cause Name','Year'])

# deaths = data.groupby('State').first()
deaths = data.groupby(['State']).sum()

states = deaths.index.values
totalDeaths = deaths['Deaths'].values

print(totalDeaths)
# plt.plot(states,totalDeaths, label="Deaths US")
# plt.grid(True)
# plt.xlabel('State')
# plt.ylabel('Total number of deaths', fontsize=15)
# plt.title('Total number of deaths per state',fontsize=20)
# plt.show()
