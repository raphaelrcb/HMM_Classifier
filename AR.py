# -*- coding: utf-8 -*-

###     Programa para abrir e separar um .csv em diferentes arrays. Depende da organização do csv e caso tenha um número diferente de colunas, deverá ser levemente alterado
###     Lógica a ser usada em cósgis futuros
###

import csv
import numpy as np
import math
from read_file import read_csv_to_array
from pandas import datetime
from pandas import read_csv
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

# from statsmodels.tsa.stattools import adfuller
# from numpy import log



def main ():
    print ("Starting AR Code")
    # emg_time = []
    # emg_value = []
    # orientarion_time = []
    # pitch_x = []
    # roll_y = []
    # yaw_z = []
    # emg_time, emg_value, orientarion_time, pitch_x, roll_y, yaw_z = read_csv_to_array()    
    # emg_time = np.array(emg_time)
    # emg_value = np.array(emg_value)
    # orientarion_time = np.array(orientarion_time)
    # pitch_x = np.array(pitch_x)
    # roll_y = np.array(roll_y)
    # yaw_z = np.array(yaw_z)

    # series = read_csv('run6.csv', header=32, usecols=[0, 1], dtype={'X[s]': np.float64, 'Avanti Sensor 1: EMG 1 [V]': np.float64}, index_col=0)
    series = read_csv('run8.csv', header=46, index_col=0, usecols=[0, 1])
    # emg = np.column_stack((series.index.to_numpy(), series.to_numpy()))
    # print(emg)
    series.index = pd.to_datetime(series.index, unit='ms')
    series.index = pd.DatetimeIndex(series.index, freq=series.index.inferred_freq) 
    #To do: Fix Index to correct date
    # print(series.index)
    # print(series.head())

    series.plot()
    pyplot.legend(['EMG (V)'])
    pyplot.show()

    print("---------------------------------------------------------------------------------")

    autocorrelation_plot(series)
    pyplot.show()

    # model = ARIMA(series, order=(4,0,0))
    # model_fit = model.fit()
    # print(model_fit.summary())

    # residuals = DataFrame(model_fit.resid)
    # residuals.plot()
    # pyplot.show()
    # residuals.plot(kind='kde')
    # pyplot.show()
    # # summary stats of residuals
    # print(residuals.describe())


if __name__ == '__main__': # chamada da funcao principal
    main()