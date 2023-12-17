#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Plot_chart/data_chart.csv')

df.plot(kind = "line")
plt.style.use('ggplot')
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig("mygraph.png")
sys.stdout.flush()
