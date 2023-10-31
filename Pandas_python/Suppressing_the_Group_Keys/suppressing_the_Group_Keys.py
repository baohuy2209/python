import pandas as pd 
import numpy as np

filename = "C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Data_Aggregation_and_Group_Operations/Column_Wise_and_Multiple_Function_Application/tips.csv"

tips = pd.read_csv(filename)

def top (df, n = 5, columns = "total_bill"):
    return df.sort_values(columns, ascending = True)[:n]

result = tips.groupby("smoker", group_keys = False).apply(top)

#      total_bill   tip     sex smoker   day    time  size
# 111        7.25  1.00  Female     No   Sat  Dinner     1
# 149        7.51  2.00    Male     No  Thur   Lunch     2
# 195        7.56  1.44    Male     No  Thur   Lunch     2
# 145        8.35  1.50  Female     No  Thur   Lunch     2
# 135        8.51  1.25  Female     No  Thur   Lunch     2
# 67         3.07  1.00  Female    Yes   Sat  Dinner     1
# 92         5.75  1.00  Female    Yes   Fri  Dinner     2
# 172        7.25  5.15    Male    Yes   Sun  Dinner     2
# 218        7.74  1.44    Male    Yes   Sat  Dinner     2
# 222        8.58  1.92    Male    Yes   Fri   Lunch     1