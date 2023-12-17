import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv')
print(df.to_string())

for x in df.index: 
    if df.loc[x, "Duration"] > 60: 
        df.loc[x, "Duration"] = df.loc[x, "Duration"]/10
        
print(df.to_string()) 