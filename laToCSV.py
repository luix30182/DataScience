import sys
import json
import csv

def toCSV(jsonFile,nameFile):
  with open(jsonFile,'r') as f:
    a = ''.join(f.readlines())

  json_parsed = json.loads(a) 

  empsData = open(nameFile,'w')
  csvWritter = csv.writer(empsData)

  for i,x in enumerate(json_parsed):
    if i==0:
      header = x.keys()
      csvWritter.writerow(header)
    csvWritter.writerow(x.values())

  empsData.close()