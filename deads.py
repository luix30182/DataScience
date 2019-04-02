import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)
pd.set_option('display.max_colwidth',1000)
pd.set_option('display.width',1000)

data = pd.read_csv(sys.argv[1], encoding='latin-1')
word = sys.argv[2].lower()
entityName = pd.read_csv('DataScienceDataSets\\defunciones2017\\catalogos\\decateml.csv',encoding='latin-1')
entityCVE = pd.read_csv('DataScienceDataSets\\defunciones2017\\conjunto_de_datos\\conjunto_de_datos_defunciones_generales_2017.CSV', encoding='latin-1')

entityCVE = entityCVE.drop(columns=['tloc_resid','mun_regis','ent_resid','mun_resid','loc_resid','ent_ocurr','par_agre','ent_ocules','mun_ocules','loc_ocules','razon_m','dis_re_oax','mun_ocurr','tloc_ocurr','loc_ocurr','complicaro','dia_cert','mes_cert','anio_cert','maternas','lengua','sexo','edad','dia_ocurr','mes_ocurr','anio_ocur','grupo','lista1','gr_lismex','vio_fami','area_ur','edad_agru','cond_act','derechohab','embarazo','rel_emba','horas','minutos','capitulo','lugar_ocur','necropsia','asist_medi','sitio_ocur','cond_cert','dia_regis','mes_regis','anio_regis','dia_nacim','ocupacion','escolarida','edo_civil','presunto','ocurr_trab','lista_mex','mes_nacim','anio_nacim','nacionalid'])

entityName = entityName.drop(columns=['cve_mun','cve_loc'])
entityName = entityName.groupby('cve_ent').first()
entityName = entityName[:-5]

entityCVE.rename(columns={'ent_regis': 'id'}, inplace=True)
entityName.index.names = ['id']

fulldata = pd.merge(entityCVE,entityName, on='id')
fulldata.rename(columns={'causa_def':'CVE'}, inplace=True)
fulldata2 = pd.merge(fulldata,data, on='CVE')
fulldata2['DESCRIP'] = fulldata2['DESCRIP'].str.lower()

filterRows = fulldata2[fulldata2['DESCRIP'].str.contains(word)]
filtered = filterRows.groupby(['nom_loc','CVE']).first()
filteredCounter = filterRows.groupby(['nom_loc'])['DESCRIP'].count()

wCounter = data[data['DESCRIP'].str.contains(word)]
wCounter = wCounter.groupby('DESCRIP').count()

r = data['DESCRIP'].values
for x in r:
    print(x)
# print(filteredCounter)
# with pd.option_context('display.max_rows', None, 'display.max_columns', 10000):
    # print(filtered)