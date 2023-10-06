import pandas as pd 

df = pd.read_csv("s&p500.csv", index_col='Date', parse_dates=True)
df.head()
df.tail()