import pandas as pd 
import numpy as np 
import matplotlib 
import sys
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
df = pd.DataFrame([[10,9,5,3,2,6], 
					[10,8,9,5,6,6], 
					[9,10,3,5,9,5],
					[6,7,4,10,9,7]],
					index = ['Huy', 'Han', 'Hung', 'Duy'],
					columns = ['Math', 'Physic', 'Chemistry', 'Biology', 'History', 'Geography'])

df.iloc[0:4, [2,3]] = np.nan

print(df.to_string())

fig, ax = plt.subplots(2,2)
plt.title('Chart score')
axes = df['Math'].plot.bar(ax= ax[0][0], alpha = 0.7, title = 'Math score')
rects1 = axes.patches
labels1 = ["%d" %i for i in df["Math"]]
for rect, label in zip(rects1, labels1): 
		height = rect.get_height()
		ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha = 'center', va = 'bottom')
df['Physic'].plot.bar(ax = ax[0][1], alpha = 0.7, title = 'Physic score')
df['History'].plot.bar(ax = ax[1][0], alpha = 0.7, title = 'History score')
df['Geography'].plot.bar(ax = ax[1][1], alpha = 0.7, title = 'Geography score')

plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()