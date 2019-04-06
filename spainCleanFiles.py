import sys
import numpy as np
import pandas as pd
#Limpia los datos de los archivos de españa
data = pd.read_csv(sys.argv[1])
namesys = sys.argv[1].split('\\')[-1].split('_')
nameFile = 'spainClean\\' + namesys[0]+'-'+namesys[1]+'.csv';

data = data.drop(columns=['lat_dir','lat','long','long_dir','altitude','province','day','max_temp_time','min_temp_time','avg_temp','max_wind','max_wind_direction','max_wind_time','avg_wind','rainfall','sun','max_atmospheric_pressure','max_atmospheric_pressure_hour','min_atmospheric_pressure','min_atmospheric_pressure_hour','location','date']) 

data = data.dropna(subset=['max_temp','min_temp'])
data.to_csv(nameFile, sep=',')


