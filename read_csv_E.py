# -*- coding: utf-8 -*-

###     Programa para abrir e separar um .csv em diferentes arrays. Depende da organização do csv e caso tenha um número diferente de colunas, deverá ser levemente alterado
###     Lógica a ser usada em cósgis futuros
###

import csv
import matplotlib.pyplot as plt
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
emg_value = []
emg_time = []

PitchX_value = []
RollY_value = []
YawZ_value = []

PitchX_time = []
RollY_time = []
YawZ_time = []


list_mover = []


# for n in range(n_variables):
#     for i in rows:
#         # print(i[n])
#         if (i[n] != ''):
#             list_mover = float(i[n])
#         emg_value.append(list_mover)

for i in rows:
    list_mover = float(i[0])
    emg_time.append(list_mover)
    list_mover = float(i[1])
    emg_value.append(list_mover)
    if (i[2] != ''):
        list_mover = float(i[2])
        PitchX_time.append(list_mover)
    if (i[3] != ''):
        list_mover = float(i[3])
        PitchX_value.append(list_mover)
    if (i[4] != ''):
        list_mover = float(i[4])
        RollY_time.append(list_mover)
    if (i[5] != ''):
        list_mover = float(i[5])
        RollY_value.append(list_mover)
    if (i[6] != ''):
        list_mover = float(i[6])
        YawZ_time.append(list_mover)
    if (i[7] != ''):
        list_mover = float(i[7])
        YawZ_value.append(list_mover)

# print(len(emg_value))
# print("time: ", emg_time[0] ,"s Emg = ", emg_value[0], "V")

plt.figure()
plt.plot(emg_time, emg_value,label='EMG')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(PitchX_time, PitchX_value, label='Pitch X')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(RollY_time, RollY_value, label='Roll Y')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(YawZ_time, YawZ_value, label='Yaw Z')
plt.legend()
plt.grid()
plt.show()

#Transformando rows em arrays para melhor manipulação.


