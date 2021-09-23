
import csv
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy
from filterpy.kalman import KalmanFilter
# f = KalmanFilter (dim_x=2, dim_z=1)

print ("Iniciando leitura do arquivo")

file = open ("teste_quat.csv")

csvreader = csv.reader(file)

cabecalho = []
cabecalho = next(csvreader)

while (cabecalho[0][0] != 'X'):   #Procura pela definição dos dados no arquivo.
    cabecalho = next(csvreader)

print(cabecalho)
n_variables = (len(cabecalho))
# print(n_variables)

rows = []
for row in csvreader:
        rows.append(row)
file.close()
# print(rows[0][0])
# print(len(rows))

# emg_list = float(rows[0][1])
emg_value = []
emg_time = []

list_mover = []

for i in rows:
    list_mover = float(i[0])
    emg_time.append(list_mover)
    list_mover = float(i[1])
    emg_value.append(list_mover)

