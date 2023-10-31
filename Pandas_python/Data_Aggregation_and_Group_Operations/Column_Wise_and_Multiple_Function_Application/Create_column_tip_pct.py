import pandas as pd 
import numpy as np 

def peak_to_peak(arr):
    return arr.max() - arr.min() 

tips = pd.read_csv("C:/Users/ADMIN/Documents/GitHub/python/Pandas_python/Data_Aggregation_and_Group_Operations/Column_Wise_and_Multiple_Function_Application/tips.csv")

tips["tip_pct"] = tips["tip"]/tips["total_bill"]
grouped = tips.groupby(["day", "smoker"])

grouped_pct = grouped["tip_pct"]
print(grouped_pct.agg(["mean","min","max", peak_to_peak]))

#                  mean       min       max  peak_to_peak
# day  smoker                                            
# Fri  No      0.151650  0.120385  0.187735      0.067349
#      Yes     0.174783  0.103555  0.263480      0.159925
# Sat  No      0.158048  0.056797  0.291990      0.235193
#      Yes     0.147906  0.035638  0.325733      0.290095
# Sun  No      0.160113  0.059447  0.252672      0.193226
#      Yes     0.187250  0.065660  0.710345      0.644685
# Thur No      0.160298  0.072961  0.266312      0.193350
#      Yes     0.163863  0.090014  0.241255      0.151240

print("\n")

print(grouped_pct.agg([("average", "mean"), ("stdev", "std")]))

#               average     stdev
# day  smoker                    
# Fri  No      0.151650  0.028123
#      Yes     0.174783  0.051293
# Sat  No      0.158048  0.039767
#      Yes     0.147906  0.061375
# Sun  No      0.160113  0.042347
#      Yes     0.187250  0.154134
# Thur No      0.160298  0.038774
#      Yes     0.163863  0.039389

function = ["count", "mean", "max", "min", "size"]
result = grouped[["tip_pct", "total_bill"]].agg(function)

print(result)

#             tip_pct                                ... total_bill                   
#               count      mean       max       min  ...       mean    max    min size
# day  smoker                                        ...                              
# Fri  No           4  0.151650  0.187735  0.120385  ...  18.420000  22.75  12.46    4
#      Yes         15  0.174783  0.263480  0.103555  ...  16.813333  40.17   5.75   15
# Sat  No          45  0.158048  0.291990  0.056797  ...  19.661778  48.33   7.25   45
#      Yes         42  0.147906  0.325733  0.035638  ...  21.276667  50.81   3.07   42
# Sun  No          57  0.160113  0.252672  0.059447  ...  20.506667  48.17   8.77   57
#      Yes         19  0.187250  0.710345  0.065660  ...  24.120000  45.35   7.25   19
# Thur No          45  0.160298  0.266312  0.072961  ...  17.113111  41.19   7.51   45
#      Yes         17  0.163863  0.241255  0.090014  ...  19.190588  43.11  10.34   17

ftuples = [("Average", "mean"), ("Variance", "var")]
result1 = grouped[["tip_pct", "total_bill"]].agg(ftuples)

print(result1)
#               tip_pct           total_bill            
#               Average  Variance    Average    Variance
# day  smoker                                           
# Fri  No      0.151650  0.000791  18.420000   25.596333
#      Yes     0.174783  0.002631  16.813333   82.562438
# Sat  No      0.158048  0.001581  19.661778   79.908965
#      Yes     0.147906  0.003767  21.276667  101.387535
# Sun  No      0.160113  0.001793  20.506667   66.099980
#      Yes     0.187250  0.023757  24.120000  109.046044
# Thur No      0.160298  0.001503  17.113111   59.625081
#      Yes     0.163863  0.001551  19.190588   69.808518

print(grouped.agg({"tip" : np.max, "size": "sum"}))

#                tip  size
# day  smoker             
# Fri  No       3.50     9
#      Yes      4.73    31
# Sat  No       9.00   115
#      Yes     10.00   104
# Sun  No       6.00   167
#      Yes      6.50    49
# Thur No       6.70   112
#      Yes      5.00    40

print(grouped.agg({"tip_pct" : ["min", "max", "mean", "std"], "size" : "sum"}))

#               tip_pct                               size
#                   min       max      mean       std  sum
# day  smoker                                             
# Fri  No      0.120385  0.187735  0.151650  0.028123    9
#      Yes     0.103555  0.263480  0.174783  0.051293   31
# Sat  No      0.056797  0.291990  0.158048  0.039767  115
#      Yes     0.035638  0.325733  0.147906  0.061375  104
# Sun  No      0.059447  0.252672  0.160113  0.042347  167
#      Yes     0.065660  0.710345  0.187250  0.154134   49
# Thur No      0.072961  0.266312  0.160298  0.038774  112
#      Yes     0.090014  0.241255  0.163863  0.039389   40