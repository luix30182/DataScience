import os
import sys
import re
import json
import datetime
import laToCSV

rootDir = sys.argv[2]
content = ['Class Code','ANNUAL SALARY','Open Date','ANNUAL SALARY ','DUTIES','REQUIREMENTS','WHERE TO APPLY','APPLICATION DEADLINE']

option = 1

try:
  option = int(sys.argv[1])
except:
  option = 1

now = datetime.datetime.now().strftime('%d-%m-%Y(%H-%M-%S)')
filename = 'LosAngeles-{}'.format(now)

if option == 1:
  filename = filename + '.json'
else:
  filename = filename + '.csv'

print(filename)
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

with open('LosAngelesTempFile.json','w') as data:
  data.write('[\n')

csvFile = open('LosAngelesTempFile.json','a')

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
            classCode1 = 0
            classCode2 = 0
            try:
                classCode1 = line.split(':')[1].strip()
            except:
                classCode2 = line.split('.')[0].split(' ')[-1]
            
            if classCode1 != 0:
              dictHolder[word] = classCode1
              
            else:
              dictHolder[word] = classCode2

          elif word == 'Open Date':
            dictHolder[word] = line.split(':')[1].strip() 
          # si se encuentra coincidencia, se genera una lista apartir del indice actual
          elif word != 'Class Code' and word != 'Open Date':
            field = ''
            for x in cutedList(lines,i+1):
              if x.isupper():
                break
              else:
                field += x
                
            dictHolder[word] = field
      temp = json.dumps(dictHolder).replace(']',' ')
    if ii == len(listOfFiles)-1:
      csvFile.write(temp)
    else:
      csvFile.write(temp)
      csvFile.write(',')
csvFile.write(']\n')
csvFile.write('\n')
csvFile.close()
print(option)
if option == 1:
  os.rename('LosAngelesTempFile.json',filename)
else:
  laToCSV.toCSV('LosAngelesTempFile.json',filename)