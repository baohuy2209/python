# The example above replaces all empty cells in the whole Data Frame. 


import pandas as pd 

df = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv") 

print("Before replace null value : ")
print(df.to_string())

print("Delete rows have null value : ")
new_df = df.dropna() 
print(new_df.to_string())

print("Àfter replace null value at columns Calories : ")
df["Calories"].fillna(130, inplace = True)
print(df.to_string())

print("Àter replace null value at columns Pulse : ")
df["Pulse"].fillna(120, inplace = True)
print(df.to_string())  