import pandas as pd 
import numpy as np

filename = "C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Data_Aggregation_and_Group_Operations/Column_Wise_and_Multiple_Function_Application/tips.csv"

tips = pd.read_csv(filename)

tips["tip_pct"] = tips["tip"]/tips["total_bill"] 
result = tips.groupby("smoker")["tip_pct"].describe()
print(tips.groupby("smoker")["tip_pct"].describe())

#         count      mean       std  ...       50%       75%       max
# smoker                             ...                              
# No      151.0  0.159328  0.039910  ...  0.155625  0.185014  0.291990
# Yes      93.0  0.163196  0.085119  ...  0.153846  0.195059  0.710345

print(result.unstack())

#        smoker
# count  No        151.000000
#        Yes        93.000000
# mean   No          0.159328
#        Yes         0.163196
# std    No          0.039910
#        Yes         0.085119
# min    No          0.056797
#        Yes         0.035638
# 25%    No          0.136906
#        Yes         0.106771
# 50%    No          0.155625
#        Yes         0.153846
# 75%    No          0.185014
#        Yes         0.195059
# max    No          0.291990
#        Yes         0.710345