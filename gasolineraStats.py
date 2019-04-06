import sys
import folium
import math
import pandas as pd
import xml.etree.ElementTree as ET
#desviacion estandar,maximo,minimo,promedio
root = ET.parse(sys.argv[1]).getroot()

gassPricessPremium = []
gassPricessRegular = []
gassPricessDiesel = []
error = 0
for element in root:
  for subElement  in element:
    gassType = subElement.attrib['type']
    gassValue = subElement.text
    if float(gassValue) > 10:
      if gassType == 'premium':
        gassPricessPremium.append(float(gassValue))
      elif gassType == 'regular':
        gassPricessRegular.append(float(gassValue))
      elif gassType == 'diesel':
        gassPricessDiesel.append(float(gassValue))
      else:
        error += 1

totalPremium = 'Total de registros Premium = {}'.format(len(gassPricessPremium))
totalRegular = 'Total de registros Regular = {}'.format(len(gassPricessRegular))
totalDiesel = 'Total de registros Diesel = {}'.format(len(gassPricessDiesel))

print(totalPremium)
print(totalRegular)
print(totalDiesel)

averagePremium = sum(gassPricessPremium) / len(gassPricessPremium)
averageRegular = sum(gassPricessRegular) / len(gassPricessRegular)
averageDiesel = sum(gassPricessDiesel) / len(gassPricessDiesel)

print('*******************************************+')
print('Promedio de Premium = {}'.format(averagePremium))
print('Promedio de Regular = {}'.format(averageRegular))
print('Promedio de Diesel = {}'.format(averageDiesel))

minPremium = min(gassPricessPremium)
minRegular = min(gassPricessRegular)
minDiesel = min(gassPricessDiesel)

print('*******************************************+')
print('Valor minimo Premium = {}'.format(minPremium))
print('Valor minimo Regular = {}'.format(minRegular))
print('Valor minimo Diesel = {}'.format(minDiesel))

maxPremium = max(gassPricessPremium)
maxRegular = max(gassPricessRegular)
maxDiesel = max(gassPricessDiesel)

print('*******************************************+')
print('Valor maximo Premium = {}'.format(maxPremium))
print('Valor maximo Regular = {}'.format(maxRegular))
print('Valor maximo Diesel = {}'.format(maxDiesel))

# Desviacion estandar
desviacionPremiumCuadrado = [(x-averagePremium)**2 for x in gassPricessPremium]
desviacionPremium = math.sqrt(sum(desviacionPremiumCuadrado)/len(gassPricessPremium))

desviacionRegularCuadrado = [(x-averageRegular)**2 for x in gassPricessRegular]
desviacionRegular = math.sqrt(sum(desviacionRegularCuadrado)/len(gassPricessRegular))

desviacionDieselCuadrado = [(x-averageDiesel)**2 for x in gassPricessDiesel]
desviacionDiesel = math.sqrt(sum(desviacionDieselCuadrado)/len(gassPricessDiesel))

print('*******************************************+')
print('La desviacion estandar Premium = {}'.format(desviacionPremium))
print('La desviacion estandar Regular = {}'.format(desviacionRegular))
print('La desviacion estandar Diesel = {}'.format(desviacionDiesel))