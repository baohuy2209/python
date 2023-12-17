import pandas as pd 
import numpy as np 

df = pd.DataFrame({ 'key1' : ['a', 'a', 'b', 'b', 'a'],
					'key2' : ['one', 'two', 'one', 'two', 'one'], 
					'data1' : np.random.randn(5), 
					'data2' : np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])

print(grouped) 
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x000001E820E74610>
print(grouped.mean()) # average 

# Result : 

# key1
# a    0.746929
# b    0.307919