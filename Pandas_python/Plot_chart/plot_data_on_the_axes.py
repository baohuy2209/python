import sys 
import matplotlib 
import matplotlib.pyplot as plt 
matplotlib.use('TkAgg')

fig, ax = plt.subplots() 
ax.plot([1,2,3,4], [1,4,2,3]) # draws the plot
plt.show() # show graph 

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

