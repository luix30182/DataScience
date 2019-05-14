import os
import sys
import re
import json
import pandas as pd
import matplotlib.pyplot as plt

rootDir = sys.argv[1]
content = ['Class Code','Open Date','ANNUAL SALARY ','DUTIES','REQUIREMENTS','WHERE TO APPLY','APPLICATION DEADLINE']

def isInList(compareList,word):
  for x in compareList:
    if len(re.findall(x,word))>0:
      return True, x
  return False, 'Nada'

def isNothing(line):
  if line == '' or line == ' ' or len(line) == 0:
    return True
  return False

def cutedList(l,n):
  return l[n:-1]

def formatList(l):
  l = [x+',' for x in l]
  return ''.join(l)[:-1]

with open('LosAngeles.json','w') as data:
  data.write('[\n')

csvFile = open('LosAngeles.json','a')

for root, subFolders, files in os.walk(rootDir):
  numberOfFiles = 0
  listOfFiles = []
  for file in files:
    if file[0] != '.':
      listOfFiles.append(file)
  dictHolder = {}
  for ii,file in enumerate(listOfFiles):
    tFile = os.path.join(root,file)
    with open(tFile, 'r',encoding="latin-1",errors='ignore') as f:
      lines = f.readlines()
      lines = list(map(lambda x: x.strip(),lines))
      lines = list(filter(lambda x: not isNothing(x), lines))
      # guarda el puesto, que se encuetra en la pimer linea
      title = lines[0]
      dictHolder['title'] = title
      # se remueve el puesto de la lista
      lines = lines[1:]
      code = False
      for i,line in enumerate(lines):
        # busca lineas que coinsidan con el campo
        search,word = isInList(content,line)
        if search:
          if word == 'Class Code' and not code:
            code = True
            try:
              # print(line.split(':')[1].strip())
              dictHolder[word] = line.split(':')[1].strip() 
              if ii == 0:
                print(dictHolder)
              # print(dictHolder[word])
            except:
              dictHolder[word] = line.split('.')[0].split(' ')[-1] 
          elif word == 'Open Date':
            dictHolder[word] = line.split(':')[1].strip() 
          # si se encuentra coincidencia, se genera una lista apartir del indice actual
          else:
            field = ''
            for x in cutedList(lines,i+1):
              if x.isupper():
                break
              else:
                field += x
            dictHolder[word] = field
            if ii == 0:
              print('***********')
              print(dictHolder)
      temp = json.dumps(dictHolder).replace(']',' ')
      if(ii == 0):
        print(dictHolder)
    # print(ii)
    if ii == len(listOfFiles)-1:
      csvFile.write(temp)
    else:
      csvFile.write(temp)
      csvFile.write(',')
csvFile.write(']\n')
csvFile.write('\n')
csvFile.close()

