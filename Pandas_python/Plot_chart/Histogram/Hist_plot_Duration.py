import sys 
import matplotlib 
matplotlib.use('TkAgg')

import pandas as pd 
import matplotlib.pyplot as plt 

filename = 'C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Plot_chart/data_chart.csv'
df = pd.read_csv(filename)
df["Duration"].plot(kind = 'hist')
plt.show()

plt.savefib(sys.stdout.buffer)
sys.stdout.flush()