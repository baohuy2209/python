import pandas as pd 
import numpy as np 

s = pd.Series(np.random.standard_normal(5))

s[::2] = np.nan 
print(s.to_string())
print("======================")
result = s.fillna(s.mean())
print(result)