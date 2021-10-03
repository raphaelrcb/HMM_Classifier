# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy

from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise

print ("Iniciando leitura do arquivo")

file = open ("teste_quat.csv")

csvreader = csv.reader(file)

cabecalho = []
cabecalho = next(csvreader)

while (cabecalho[0][0] != 'X'):   #Procura pela definicao dos dados no arquivo.
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


f = KalmanFilter (dim_x=2, dim_z=1)

#definindo valor inicial para os estados 
f.x = np.array([[0],                    #Posicao
                [0]])                   #Velocidade

#definindo Matriz de Transicao de Estados
f.F = np.array([[1.,1.],
                [0.,1.]])

#definindo a matriz de covariância (P jah eh a matriz identidade)
f.P *= 1000.

#definindo ruido de medicao
f.R = 5

f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13)

print(f)


