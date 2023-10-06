import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/DSLopK23411.csv')

print(df.head(10)); 
#If you do not pass a parameter to the head function,
# the first 5 lines will be read by default

print("==========================")

print(df.head())

print(df.tail(12)) 

print("==========================")

print(df.tail())
#If you do not pass a parameter to the tail function,
# the last 5 lines will be read by default

print(df.info())