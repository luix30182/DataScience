import sys
import re
import functools
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1],encoding='latin-1')
data = data.drop(columns=['Class Code','DUTIES','WHERE TO APPLY','APPLICATION DEADLINE'])
salary = data['ANNUAL SALARY'].values

names = list(data['title'].values)

def cleanValue(x):
  return int(''.join(re.findall(r"\d",x)))
     
def getClean(x):
  temp2 = []
  try:
    temp = x.strip().split(' ')
    for x in temp:
      if '$' in x:
        temp2.append(cleanValue(x))
  except:
    pass
  return temp2

salary = list(map(lambda x:getClean(x), salary))

min_salary = []
max_salary = []
average_salary = []

for x in salary:
    try:
      min_salary.append(x[0])
      max_salary.append(x[-1])
      suma = functools.reduce(lambda a,b:a+b,x) / len(x)
      average_salary.append(suma)
    except:
      min_salary.append(0)
      max_salary.append(0)
      average_salary.append(0)

# print(type(names),names)
# for i in range(len(min_salary)):
#   print(min_salary[i], max_salary[i],average_salary[i],names[i])

# Plot by age
ngroups = len(min_salary)
fig,ax = plt.subplots()
# index = np.arange(len(min_salary))
bar_width = 0.5
opacity = 0.8

n = int(math.floor(len(min_salary)/2))
n = 10
min_salary1 = min_salary[0:n]
max_salary1 = max_salary[0:n]
average_salary1 = average_salary[0:n]
index = np.arange(n)

rect1 = plt.bar(index,min_salary1, label="Min salary", color = 'b', alpha = opacity)
rect2 = plt.bar(index + bar_width,max_salary1, label="Max Salary", color = 'g', alpha = opacity)

plt.xlabel('Job')
plt.ylabel('Salar in dollars')
plt.title('Min, Max & Average')
plt.xticks(index, names[0:n])
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
