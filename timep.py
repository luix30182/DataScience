import sys,re
import time
import datetime
import calendar
import matplotlib.pyplot as plt

def plotBarChart(d):
    labels = ['menor a 10','menor a 30','menor a 50','mas de 50','menor a 100','mayor a 200']
    index = list(range(0,len(d)))
    plt.bar(index,d)
    plt.xlabel('minutos de viaje', fontsize=10)
    plt.ylabel('cantidad de viajes', fontsize=10)
    plt.xticks(index,labels, fontsize=8, rotation=30)
    plt.title('BarChart')
    plt.show()

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

def getDate(d,r):
    n = []
    for line in d:
        if(verifyLine(r,line)):
            l = line.split(',')
            t = []
            t.append(l[1])
            t.append(l[2])
            n.append(t)
    return n

def toTime(s):
    t = s.split(' ')
    t1 = t[0].split('-')
    t2 = t[1].split(':')
    t = t1 + t2
    t = [int(x) for x in t]
    return t

def numberToTime(t):
    t = time.gmtime(t)
    return(time.strftime('%a,%d %b %Y %H :%M:%S',t))
    # return(time.strftime('%d/%m/%y',t))

def timeToNumber(d):
    d = datetime.datetime(d[0],d[1],d[2],d[3],d[4],d[5])
    return(calendar.timegm(d.timetuple()))

f = open(sys.argv[1])
reg = getRegex(sys.argv[2]).split(',')
listTimes = getDate(f,reg)

times = []
for x in listTimes:
    t = []
    for y in x:
        t.append(timeToNumber(toTime(y)))
    times.append(t)

timesDiff = []
for x in times:
    # print('Fecha de subida: {0} y fecha de llegada: {1}'.format(numberToTime(x[0]),numberToTime(x[1])))
    tt = ((x[1]-x[0])/60)
    timesDiff.append(tt)

print(timesDiff[0])
maxTwHun = 0
maxHund = 0
maxTen = 0
maxthir = 0
maxfifth = 0
others = 0
for x in timesDiff:
    if x>60:
        others += 1
    elif x>30:
        maxTwHun += 1 
    elif x>20:
        maxHund +=1
    elif x>10:
        maxfifth += 1
    elif x>5:
        maxthir += 1
    else:
        maxTen += 1
arr = [maxTen,maxthir,maxfifth,maxHund,maxTwHun,others]

plotBarChart(arr)