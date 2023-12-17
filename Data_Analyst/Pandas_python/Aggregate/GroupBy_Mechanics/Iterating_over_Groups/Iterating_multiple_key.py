import pandas as pd 
import numpy as np 

df = pd.DataFrame({ 'key1' : ['a', 'a', 'b', 'b', 'a'],
					'key2' : ['one', 'two', 'one', 'two', 'one'], 
					'data1' : np.random.randn(5), 
					'data2' : np.random.randn(5)})

grouped = df.groupby([df['key1'], df['key2']]) 
print(grouped.mean())

for (k1,k2), group in grouped: 
	print((k1, k2))
	print(group)

for (k1,k2), group in grouped: 
	print(k1)
	print(group)
for name, _ in grouped: 
	print(name)

for _,group in grouped:
	print(group)