###     Programa para abrir e separar um .csv em diferentes arrays. Depende da organização do csv e caso tenha um número diferente de colunas, deverá ser levemente alterado
###     Lógica a ser usada em cósgis futuros
###

import csv
import matplotlib.pyplot as plt
import math

print ("Iniciando leitura do arquivo")

file = open ("run8.csv")

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

QuatW_value = []
QuatX_value = []
QuatY_value = []
QuatZ_value = []
QuatAcc_value = []

QuatW_time = []
QuatX_time = []
QuatY_time = []
QuatZ_time = []
QuatAcc_time = []


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
        QuatW_time.append(list_mover)
    if (i[3] != ''):
        list_mover = float(i[3])
        QuatW_value.append(list_mover)
    if (i[4] != ''):
        list_mover = float(i[4])
        QuatX_time.append(list_mover)
    if (i[5] != ''):
        list_mover = float(i[5])
        QuatX_value.append(list_mover)
    if (i[6] != ''):
        list_mover = float(i[6])
        QuatY_time.append(list_mover)
    if (i[7] != ''):
        list_mover = float(i[7])
        QuatY_value.append(list_mover)
    if (i[8] != ''):
        list_mover = float(i[8])
        QuatZ_time.append(list_mover)
    if (i[9] != ''):
        list_mover = float(i[9])
        QuatZ_value.append(list_mover)
    if (i[10] != ''):
        list_mover = float(i[10])
        QuatAcc_time.append(list_mover)
    if (i[11] != ''):
        list_mover = float(i[11])
        QuatAcc_value.append(list_mover)

# print(len(emg_value))
# print("time: ", emg_time[0] ,"s Emg = ", emg_value[0], "V")

plt.figure()
plt.plot(emg_time, emg_value,label='EMG')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(QuatW_time, QuatW_value, label='Quaternion W')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(QuatX_time, QuatX_value, label='Quaternion X')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(QuatY_time, QuatY_value, label='Quaternion Y')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(QuatZ_time, QuatZ_value, label='Quaternion Z')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(QuatAcc_time, QuatAcc_value, label='Quaternion Accuracy')
plt.legend()
plt.grid()
plt.show()

#Transformando rows em arrays para melhor manipulação.


