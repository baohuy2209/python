import sys
import matplotlib 
import matplotlib.pyplot as plt 
import numpy as np 
matplotlib.use('TkAgg') 


# Hàm np.linspace() cũng là một hàm được sử dụng để tạo ra một mảng từ các dãy số được chỉ định trước.
# Hàm này sẽ tạo ra một mảng Numpy thông qua một dãy số và các phần tử trong mảng sẽ được cách đều sao cho phù hợp với ví trị bắt đầu và vị trí kết thúc khoảng.
# Kết quả dãy số được trả vể sau khi sử dụng hàm np.linspace() sẽ có kiểu "numpy.ndarray"

x = np.linspace(0, 2, 100) #Sample data/ 

#Note that evene in the OO-style, we use '.pyplot.figure' to create the figure. 
fig, ax = plt.subplots(figsize =(5, 2.7), layout = 'constrained')
ax.plot(x, x, label = 'linear') #Plot some data on the axes. 
ax.plot(x, x**2, label = 'quadratic') #Plot more data on the axes ... 
ax.plot(x, x**3, label = 'cubic') #... and more. 
ax.set_xlabel('horizontal')
ax.set_ylabel('vertical')
ax.set_title('Simple plot according to OO-style')
ax.legend()
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush() 