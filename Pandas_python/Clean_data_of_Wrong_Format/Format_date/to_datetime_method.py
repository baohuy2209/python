import pandas as pd

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv')

df['Date'] = pd.to_datetime(df['Date'], format = ' %y/%m/%d, ' )

print(df.to_string())