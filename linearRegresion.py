import sys,re, math
import matplotlib.pyplot as plt

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

def fx(x,a,b):
    return b*x+a

data = open(sys.argv[1])
reg = getRegex(sys.argv[2]).split(',')
distancia = int(sys.argv[3])-1
total = int(sys.argv[4])-1

rightLines = []
for line in data:
    t = line.split(',')
    if len(t) == len(reg):
        if verifyLine(reg,line):
            rightLines.append(line)
XY = 0
X = 0
X2 = 0
Y = 0
Y2 = 0
SY2 = 0

distancias = []
totales = []
for i in rightLines:
    i = i.split(',')
    distancias.append(float(i[distancia]))
    totales.append(float(i[total]))
    XY += (float(i[distancia]) * float(i[total]))
    X += float(i[distancia])
    X2 += float(i[distancia]) ** 2
    Y += float(i[total])
    Y2 += float(i[total])**2

SY2 = Y**2
SX2 = X**2

N = len(rightLines)

print('Suma xy: {0}'.format(XY))
print('Suma x: {0}'.format(X))
print('Suma x^2: {0}'.format(X2))
print('Suma x al 2: {0}'.format(SX2))
print('Suma y: {0}'.format(Y))
print('Suma y^2: {0}'.format(Y2))
print('Suma y al 2: {0}'.format(SY2))
print('cantidad de n: {0}'.format(N))


b = (N*XY-X*Y)/((N*X2)-SX2)
print('b : {0}'.format(b))

a = ((X2*Y)-(XY*X))/((N*X2) - SX2)
print('a : {0}'.format(a))

sxx = X2 - (SX2/N)
print('sxx : {0}'.format(sxx))

syy = Y2 -(SY2/N)
print('syy : {0}'.format(syy))

sxy = XY - ((X*Y)/N)
print('sxy : {0}'.format(sxy))

r = sxy/math.sqrt(sxx*syy)
print('r : {0}'.format(r))

ys = [fx(x,a,b) for x in distancias]

plt.title('Scatter Plot', fontsize=20)
plt.xlabel('Distancia', fontsize=15)
plt.ylabel('Totales', fontsize=15)
plt.scatter(distancias,totales, marker = 'o')
plt.plot(distancias,ys)
plt.show()