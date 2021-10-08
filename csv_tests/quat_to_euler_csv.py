# -*- coding: utf-8 -*-
### 
###     Programa para converter os dados em um arquivo CSV de Quaternion para Euler       
###     

import csv
import matplotlib.pyplot as plt
import math

def quartenion_to_euler (QX, QY, QZ, QW):
        # """
        # Convert a quaternion into euler angles (roll, pitch, yaw)
        # roll is rotation around x in radians (counterclockwise)
        # pitch is rotation around y in radians (counterclockwise)
        # yaw is rotation around z in radians (counterclockwise)
        # """
    roll_x = []
    pitch_y = []
    yaw_z = []
    
    t0 = +2.0 * (QW * QX + QY * QZ)
    t1 = +1.0 - 2.0 * (QX * QX + QY * QY)
    roll_x = math.atan2(t0, t1)
    
    t2 = +2.0 * (QW * QY - QZ * QX)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)
    
    t3 = +2.0 * (QW * QZ + QX * QY)
    t4 = +1.0 - 2.0 * (QY * QY + QZ * QZ)
    yaw_z = math.atan2(t3, t4)
     
    
    return roll_x, pitch_y, yaw_z # in radians

def main ():
    print("begin")

    file = open("teste_quat.csv") 

    csvreader = csv.reader(file)

    cabecalho = []
    cabecalho = next(csvreader)

    rows = []
    while (cabecalho[0][0] != 'X'):   #Procura pela definição dos dados no arquivo.
        cabecalho = next(csvreader)

    for row in csvreader:
        rows.append(row)
    file.close()


    

    QuatW_value = []
    QuatX_value = []
    QuatY_value = []
    QuatZ_value = []
    # QuatAcc_value = []

    QuatW_time = []
    QuatX_time = []
    QuatY_time = []
    QuatZ_time = []

    list_mover = []

    RollX = []
    PitchY = []
    YawZ = []
    count = 0

    for i in rows:
        # print(count)
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
        

    # print(len(QuatY_time))
    EulerX = []
    EulerY = []
    EulerZ = []
    Euler_time = []
    for count in range(len(QuatX_value)):
        RollX, PitchY, YawZ = quartenion_to_euler(QuatX_value[count], QuatY_value[count], QuatZ_value[count], QuatW_value[count])
        Euler_time.append(QuatW_time[count])
        EulerX.append(RollX*180/math.pi)
        EulerY.append(PitchY*180/math.pi)
        EulerZ.append(YawZ*180/math.pi)

    plt.figure()
    plt.plot(Euler_time, EulerX, label='Euler X')
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(Euler_time, EulerY, label='Euler Y')
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(Euler_time, EulerZ, label='Euler Z')
    plt.legend()
    plt.grid()
    plt.show()

    new_csv = open('teste_convertido.csv', 'w', newline = '')
    # create the csv writer
    writer = csv.writer(new_csv)
    cabecalho = ['X[s]', 'Avanti Sensor 1: Roll 1 [degrees]', 'X[s]', 'Avanti Sensor 1: Pitch 1 [degrees]', 'X[s]', 'Avanti Sensor 1: Yaw 1 [degrees]']
    writer.writerow(cabecalho)

    for i in range(len(EulerY)):
        new_row = [Euler_time[i], EulerX[i], Euler_time[i], EulerY[i], Euler_time[i], EulerZ[i]]
        writer.writerow(new_row)





    new_csv.close()



if __name__ == '__main__': # chamada da funcao principal
    main()