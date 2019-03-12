import sys,re,math
# import matplotlib.pyplot as plt


# def plotPieChart(d):
#     # w = 20
#     # h = 10
#     # plt.figure(figsize=(w, h))
#     pie = plt.pie(d['info'], shadow=False, autopct='%1.1f%%')
#     plt.legend(pie[0],d['label'], loc="upper left",ncol=3)
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.show()


# def plotLineChart(d):
#     index = list(range(0,len(d['label'])))
#     plt.plot(index,d['info'],label='linear')
#     plt.xlabel('info label', fontsize=10)
#     plt.ylabel('number data', fontsize=10)
#     plt.legend()
#     plt.show()

# def plotBarChart(d):
#     index = list(range(0,len(d['label'])))
#     plt.bar(index,d['info'])
#     plt.xlabel('info label', fontsize=10)
#     plt.ylabel('number data', fontsize=10)
#     plt.xticks(index,d['label'], fontsize=8, rotation=90)
#     plt.title('BarChart')
#     plt.show()

# def getSum(list):
#     c = 0
#     for x in list:
#         c += x
#     return c

def getRegex(s):
    r = ''
    s = [x for x in s]
    for x in s:
        if x == 'c':
            r += '.+,'
        elif x == 'n':
            r += '(^[+-]?(\\d*\\.)?\\d+$),'
            # r += '\\d,'
    r = r[:-1]
    return r

def verifyLine(r,s):
    c = 0
    s = s.split(',')
    for i,x in enumerate(s):
        if re.match(r[i],x):
            c +=1
    if c == len(r):
        return True
    return False

# def getDesviacion(list):
#     m = getSum(list)/len(list)
#     d = [(x-m)**2 for x in list]
#     ds = math.sqrt(getSum(d)/len(list))
#     return ds

# main
data = open(sys.argv[1])
reg = getRegex(sys.argv[2]).split(',')
# column = int(input('Ingresa x >> ')) -1 
# row = int(input('Ingresa y >> ')) -1 
# labels = int(input('Ingresa la columna de las etiquetas >> ')) -1

# counter = 0
# total = 0
rightLines = []
# colors = ['gold','yellowgreen','lightcoral','lightskyblue']

for line in data:
    # total += 1
    t = line.split(',')
    if len(t) == len(reg):
        if verifyLine(reg,line):
            rightLines.append(line)
            # counter += 1

listN = []
for line in rightLines:
    r = line.split(',')
    listN.append(float(r[column]))

percentage = (counter/total)*100

print('total: ',total)
print('{0} registros correctos de {1} ({2:.2f}%)'.format(counter,total,percentage))

print('El promedio es : {0}'.format(getSum(listN)/len(listN)))
print('El valor maximo es: {0}'.format(max(listN)))
print('El valor menor es: {0}'.format(min(listN)))
print('La desviaciion estandar es: {0}'.format(getDesviacion(listN)))


# plot

d = {}
for x in rightLines:
    t = x.split(',')
    l = t[labels]
    try:
        d[l] += float(t[column])
    except:
        d[l] = float(t[column])

toPlot = {'label':[],'info':[]}
for l,i in d.items():
    toPlot['info'].append(i)
    toPlot['label'].append(l)

# plotPieChart(toPlot)
# plotLineChart(toPlot)
# plotBarChart(toPlot)