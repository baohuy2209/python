import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/DataFrame_method/data.csv') 

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df["Calories"]) 

# Mode = the value that appears most frequently 