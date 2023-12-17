import sys 
import matplotlib 
matplotlib.use('TkAgg') 

import pandas as pd 
import matplotlib.pyplot as plt 

filename = 'C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Plot_chart/Score_of_11A1/Diem_GK2_11A1_2021-2022.csv'

df = pd.read_csv(filename)
plt.figure()
ax = df["Toán"].plot(kind = 'bar')
ax.set_title('Score Math of mid-term of 11A1 2021 - 2022')
ax.set_xlabel('Fullname of students')
ax.set_ylabel('Score')
ax.set_xticklabels([str for str in df['Ho Ten']])
for tick in ax.get_xticklabels():
    tick.set_rotation(55)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()