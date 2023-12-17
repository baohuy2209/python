import pandas as pd 
df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv')

df.loc[7, 'Duration'] = 45 

print(df.to_string()) 
