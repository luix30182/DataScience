import sys,re
import matplotlib.pyplot as plt

def getTotals(f,ignore):
    total = []
    for i,x in enumerate(f):
        if i>ignore:
            if x != 0:
                total.append(float(x))
    return total

def getRange(min,max,step):
    l = list(range(round(min),round(max),step))
    if l[-1] != round(max):
        l[-1] = round(max)
    if l[0] != 0:
        l = [0] + l
    return l

def getSum(list):
    c = 0
    for x in list:
        c += x
    return c

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

data = open(sys.argv[1])
reg = getRegex(sys.argv[2]).split(',')
distancia = int(sys.argv[3])-1
total = int(sys.argv[4])-1
step = int(sys.argv[5])
# ignore = int(sys.argv[2]) -1
rightLines = []

for line in data:
    t = line.split(',')
    if len(t) == len(reg):
        if verifyLine(reg,line):
            rightLines.append(line)

linearData = []
for x in rightLines:
    x = x.split(',')
    t = []
    t.append(float(x[distancia]))
    t.append(float(x[total]))
    linearData.append(t)

linearData = sorted(linearData, key = lambda x: float(x[0]), reverse = False)
dicT = {}
for x in linearData:
    try:
        dicT[x[0]] += x[1]
    except:
        dicT[x[0]] = x[1]
dx = []
dy = []

for x,y in dicT.items():
    dx.append(x)
    dy.append(y)

XT = 0
X = 0
T = 0
T2 = 0
TT2 = 0
for x,y in dicT.items():
    XT += (x*y)
    X += x
    T += y
    T2 += y**2
TT2 = T**2
N = len(dicT)

b = ((N*XT)-(X*T))/((N*T2)-TT2)
xpromedio = X/N
tpromedio = T/N
a = xpromedio-(b*tpromedio)

xn = a + (b*800)
# print(XT)
# print(X)
# print(T)
# print(T2)
# print(TT2)
# print(N)
# print(b)
# print(xpromedio)
# print(tpromedio)
# print(a)
# print(xn)
r = getRange(min(dx),max(dx),step)
xx = []
yy = []

counter = 0
while counter < len(dx):
    xx.append(dx[counter])
    yy.append(dy[counter])
    counter += step
if counter != len(dx):
    xx = xx + [dx[-1]]
    yy = yy + [dy[-1]]
print(xx)
print(yy)
plt.title('Scatter Plot', fontsize=20)
plt.xlabel('Distancia', fontsize=15)
plt.ylabel('Totales', fontsize=15)
plt.scatter(xx, yy, marker = 'o')
plt.plot([0,800],[yy[0],xn])
plt.show()