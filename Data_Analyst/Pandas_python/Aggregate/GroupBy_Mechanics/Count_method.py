import pandas as pd 
import numpy as np 

df = pd.DataFrame({ 'key1' : ['a', 'a', 'b', 'b', 'a'],
					'key2' : ['one', 'two', 'one', 'two', 'one'], 
					'data1' : np.random.randn(5), 
					'data2' : np.random.randn(5)})

print(df.groupby(['key1', 'key2']).count())