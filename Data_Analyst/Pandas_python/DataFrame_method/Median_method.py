import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv') 

x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string()) 
#Median = the value in the middle, after you have sorted all values ascending


