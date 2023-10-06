import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv') 
# Pandas uses the mean() methods to calculate the respective values for a specified column: 
x = df["Calories"].mean()
# Mean = The average value (the sum off all values divided by number of values)
df["Calories"].fillna(x, inplace = True) 
print(df.to_string())

y = df["Pulse"].mean()
df["Pulse"].fillna(y, inplace = True)

