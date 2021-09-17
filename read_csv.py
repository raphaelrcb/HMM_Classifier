
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

# print(len(emg_value))
print("time: ", emg_time[0] ,"s Emg = ", emg_value[0], "V")

plt.figure()
plt.plot(emg_time, emg_value,label='EMG')
plt.plot(QuatW_time, QuatW_value, label='Quaternion W')    
# plt.plot(tempo, QuaternionZ, label='Quaternion Z')
# plt.plot(tempo, QuaternionW, label='Quaternion W')
plt.legend()
plt.grid()
plt.show()


# print(emg_list[1])
# print(emg_list[2])
# print(emg_list[21599])
#Transformando rows em arrays para melhor manipulação.


