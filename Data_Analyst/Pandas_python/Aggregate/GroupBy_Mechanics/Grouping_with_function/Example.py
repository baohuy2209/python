import pandas as pd 
import numpy as np 

def peak_to_peak (arr):
	return arr.max() - arr.min() 

df = pd.DataFrame({ 'data1' : np.random.randn(5), 
					'data2' : np.random.randn(5),
					'key1' : ['a', 'a', 'b', 'b', 'a'],
					'key2' : ['one', 'two', 'one', 'two', 'one'] 
					})

grouped = df.groupby('key1')
grouped['data1'].quantile(0.9) 

print(grouped.agg(peak_to_peak))