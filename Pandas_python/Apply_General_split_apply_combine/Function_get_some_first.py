import pandas as pd 
import numpy as np 

filename = "C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Data_Aggregation_and_Group_Operations/Column_Wise_and_Multiple_Function_Application/tips.csv"

df = pd.read_csv(filename) 
df["tip_pct"] = df["tip"]/df["total_bill"]

def top(df, n = 5, column = "tip_pct"):
    return df.sort_values(column, ascending = False)[:n] 

result = top(df, n = 6)
print(result.to_string())

