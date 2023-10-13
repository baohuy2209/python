import sys 
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np 
matplotlib.use('TkAgg')

x = np.linspace(0,10,10)

plt.figure(figsize = (10, 10), layout = 'constrained') # limit layout 
plt.plot(x, 2*x, label = 'line', color = 'red')
plt.plot(x, 2*x**2 - 1, label = 'parabol', color = 'blue')
plt.plot(x, x**3-2, label = 'curve1', color = 'green')
plt.plot(x, x**4 + x**3 - x**2 + 6, label = 'curve2', color = 'grey')
plt.xlabel('horizontal')
plt.ylabel('vertical')
plt.title('Simple plot with pyplot styles')
plt.legend()

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush() 
