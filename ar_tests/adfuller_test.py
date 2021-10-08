import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from numpy import log
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

# Import data
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/wwwusage.csv', names=['value'], header=0)

# print(df.columns)

df = pd.read_csv('run6.csv', header=32, index_col=0, usecols=[0, 1])
df.index = pd.to_datetime(df.index, unit='ms')
df.index = pd.DatetimeIndex(df.index, freq=df.index.inferred_freq) 

# print(df.values)

result = adfuller(df.values)
print('ADF Statistic: %.10f' % result[0])
print('p-value: %.10f' % result[1])