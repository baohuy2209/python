import sys 
import matplotlib 

matplotlib.use('TkAgg')

import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Plot_chart/Score_of_11A1/Diem_GK2_11A1_2021-2022.csv')

fig = plt.figure()
plt.style.use('ggplot')

ax1 = fig.add_subplot(3,3,1)
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)
ax4 = fig.add_subplot(3,3,4)
ax5 = fig.add_subplot(3,3,5)
ax6 = fig.add_subplot(3,3,6)
ax7 = fig.add_subplot(3,3,7)
ax8 = fig.add_subplot(3,3,8)
ax9 = fig.add_subplot(3,3,9)

df['Toán'].plot(ax = ax1, kind = 'bar', color = 'red')
df['Lí'].plot(ax = ax2, kind = 'barh', color = 'blue')
df['Hóa'].plot(ax = ax3, kind = 'hist', color = 'orange')
df['Sinh'].plot(ax = ax4, kind = 'bar', color = 'red')
df['Văn'].plot(ax = ax5, kind = 'barh', color = 'blue')
df['Sử'].plot(ax = ax6, kind = 'hist', color = 'orange')
df['Địa'].plot(ax = ax7, kind = 'bar', color = 'red')
df['Ng.ngữ'].plot(ax = ax8, kind = 'barh', color = 'blue')
df['GDCD'].plot(ax = ax9, kind = 'hist', color = 'orange')


plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush() 




