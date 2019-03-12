import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1])

data = data.dropna()
data = data.drop(columns=['113 Cause Name','Year'])

# deaths = data.groupby(['State']).sum()
# states = deaths.index.values
# totalDeaths = deaths['Deaths'].values

# Plot total Deaths in each state

# plt.plot(states,totalDeaths, label="Deaths US")
# plt.grid(True)
# plt.xlabel('State')
# plt.ylabel('Total number of deaths', fontsize=15)
# plt.xticks(rotation=90)
# plt.title('Total number of deaths per state',fontsize=20)
# plt.show()

deathsAge = data.groupby(['State']).first()
deathsAge = deathsAge.drop(columns=['Cause Name'])
deathsAge = deathsAge.drop('United States')
states = deathsAge.index.values
ages = deathsAge['Age-adjusted Death Rate'].values
deathsByAge = deathsAge['Deaths'].values
deathsByAge = [(x/100) for x in deathsByAge]
# Plot by age

plt.plot(states,ages, label="Age US")
plt.plot(states,deathsByAge, label="Deaths US")
plt.grid(True)
plt.xlabel('State')
plt.ylabel('Average Age per state', fontsize=15)
plt.xticks(rotation=90)
plt.title('Deaths by Average Age per state',fontsize=20)
plt.legend(loc='upper left')
plt.show()