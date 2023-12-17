import pandas as pd 
import numpy as np 

columns = pd.MultiIndex.from_arrays([['VietNam', 'VietNam', 'ThaiLand', 'ThaiLand', 'Indonesia'],
									[1,1,2,2,3]], 
									names = ['Country', 'N.o'])

my_data = pd.DataFrame(np.random.randn(3,5), columns = columns)

print(my_data) 