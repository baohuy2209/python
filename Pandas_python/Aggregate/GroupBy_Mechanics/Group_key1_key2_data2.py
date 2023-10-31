import pandas as pd 
import numpy as np 

df = pd.DataFrame({ 'key1' : ['a', 'a', 'b', 'b', 'a'],
					'key2' : ['one', 'two', 'one', 'two', 'one'], 
					'data1' : np.random.randn(5), 
					'data2' : np.random.randn(5)})

print(df) 
grouped1 = df['data2'].groupby([df['key2'], df['key1']])
print(grouped1.mean())

grouped2 = df['data2'].groupby([df['key1'], df['key2']])
print(grouped2.mean())