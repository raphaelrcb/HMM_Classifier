# -*- coding: utf-8 -*-

###     Programa para abrir e separar um .csv em diferentes arrays. Depende da organização do csv e caso tenha um número diferente de colunas, deverá ser levemente alterado
###     Lógica a ser usada em cósgis futuros
###

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

print ("Iniciando leitura do arquivo")

file = open ("teste_euler.csv")

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
emg_value_list = []
emg_time_list = []

PitchX_value_list = []
RollY_value_list = []
YawZ_value_list = []

PitchX_time_list = []
RollY_time_list = []
YawZ_time_list = []


list_mover = []


for i in rows:
    list_mover = float(i[0])
    emg_time_list.append(list_mover)
    list_mover = float(i[1])
    emg_value_list.append(list_mover)
    if (i[2] != ''):
        list_mover = float(i[2])
        PitchX_time_list.append(list_mover)
    if (i[3] != ''):
        list_mover = float(i[3])
        PitchX_value_list.append(list_mover)
    if (i[4] != ''):
        list_mover = float(i[4])
        RollY_time_list.append(list_mover)
    if (i[5] != ''):
        list_mover = float(i[5])
        RollY_value_list.append(list_mover)
    if (i[6] != ''):
        list_mover = float(i[6])
        YawZ_time_list.append(list_mover)
    if (i[7] != ''):
        list_mover = float(i[7])
        YawZ_value_list.append(list_mover)

#convert list to numpy array
emg_time = np.array(emg_time_list)
emg_value = np.array(emg_value_list)

Orientation_time = np.array(PitchX_time_list)

PitchX_value = np.array(PitchX_value_list)
RollY_value = np.array(RollY_value_list)
YawZ_value = np.array(YawZ_value_list)

plt.figure()
plt.plot(emg_time, emg_value,label='EMG')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(Orientation_time, PitchX_value, label='Pitch X')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(Orientation_time, RollY_value, label='Roll Y')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(Orientation_time, YawZ_value, label='Yaw Z')
plt.legend()
plt.grid()
plt.show()

#Transformando rows em arrays para melhor manipulação.


