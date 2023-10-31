import pandas as pd 
import numpy as np 

def peak_to_peak(arr):
    return arr.max() - arr.min() 

tips = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Data_Aggregation_and_Group_Operations/Column_Wise_and_Multiple_Function_Application/tips.csv")

tips["tip_pct"] = tips["tip"]/tips["total_bill"]
grouped = tips.groupby(["day", "smoker"]).mean() 

grouped_pct = grouped["tip_pct"]
print(grouped_pct.agg(["mean","min","max", peak_to_peak]))

print(grouped_pct.agg([("average", "mean"), ("stdev", "std")]))

unction = ["count", "mean", "max", "min", "size"]
result = grouped[["tip_pct", "total_bill"]].agg(function)

print(result)

ftuples = [("Average", "mean"), ("Variance", "var")]
result1 = grouped[["tip_pct", "total_bill"]].agg(ftuples)

print(result1)

print(grouped.agg({"tip" : np.max, "size": "sum"}))

print(grouped.agg({"tip_pct" : ["min", "max", "mean", "std"], "size" : "sum"}))