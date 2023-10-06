import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv')
print(df.to_string())
print("==================================")
df.drop_duplicates(inplace = True)
print(df.to_string())