import sys 
import matplotlib 
matplotlib.use('TkAgg')

import pandas as pd 
import matplotlib.pyplot as plt 

filename = 'C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Plot_chart/data_chart.csv'

df = pd.read_csv(filename)

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

plt.savefig(sys.stdout.buffer) 
sys.stdout.flush()

# Specify that you want a scatter plot with the kind argument: 
# kind = 'scatter'
# A scatter plot needs an x- and a y-axis 
# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
# Include the x and y arguments like this: 
# 
# x = 'Duration', y = 'Calories'
# #