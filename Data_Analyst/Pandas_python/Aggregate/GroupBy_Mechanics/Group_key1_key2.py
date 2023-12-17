import pandas as pd 
import numpy as np 

df = pd.DataFrame({ 'key1' : ['a', 'a', 'b', 'b', 'a'],
					'key2' : ['one', 'two', 'one', 'two', 'one'], 
					'data1' : np.random.randn(5), 
					'data2' : np.random.randn(5)})

print(df) 
grouped1 = df.groupby([df['key1'] ,df['key2']])

print("Mean method : ")
print(grouped1.mean())

print("Median method : ")
print(grouped1.median())

grouped2 = df.groupby([df['key2'], df['key1']])

print("Mean method : ")
print(grouped2.mean())

print("Median method : ")
print(grouped2.median())

