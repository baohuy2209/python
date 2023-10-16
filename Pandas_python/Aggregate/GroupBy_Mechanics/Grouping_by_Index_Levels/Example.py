import pandas as pd 
import numpy as np 

columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JD', 'JD'],
									[1,3,5,1,3]],
									names = ['cty', 'tenor'])

hier_df = pd.DataFrame(np.random.randn(4,5), columns = columns)

print(hier_df)

print(hier_df.groupby(level = 'cty', axis = 1).count())