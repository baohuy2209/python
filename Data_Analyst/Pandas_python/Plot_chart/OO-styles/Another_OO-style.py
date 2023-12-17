import sys 
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np 
matplotlib.use('TkAgg')

x = np.linspace(0,10,10) 


fig, ax = plt.subplots(figsize = (7.9, 4.2) , layout = 'constrained')
ax.plot(x, 2*x-1, label = 'line')
ax.plot(x, x**2-1, label = 'parabol')
ax.plot(x, x**3 - 2*x**2+1, label = 'curve')
ax.set_xlabel('horizontal')
ax.set_ylabel('vertical')
ax.set_title('Another OO-style')
ax.legend()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush() 