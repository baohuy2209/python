import pandas as pd 
import numpy as np 

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                "data1" : [2,12,23,11,19,20,8],
                "data2" : [3,2,34,12,20,31,4]})

print(df) 

#     key1  key2  data1  data2
# 0     a     1      2      3
# 1     a     2     12      2
# 2  None     1     23     34
# 3     b     2     11     12
# 4     b     1     19     20
# 5     a  <NA>     20     31
# 6  None     1      8      4


grouped1 = df["data1"].groupby(df["key1"])
grouped2 = df["data2"].groupby(df["key2"])
print(grouped1.mean())

# key1
# a    11.333333
# b    15.000000
# Name: data1, dtype: float64

print(grouped2.mean())

# key2
# 1    15.25
# 2     7.00
# Name: data2, dtype: float64

print(grouped1.median())

# key1
# a    12.0
# b    15.0
# Name: data1, dtype: float64

print(grouped2.median()) 

# key1
# a    12.0
# b    15.0
# Name: data1, dtype: float64


# If instead we had passed multiple arrays as a list,
# we’d get something different:
my_mean1 = df["data1"].groupby([df["key1"], df["key2"]]).mean()

print(my_mean1)

# key1  key2
# a     1        2.0
#       2       12.0
# b     1       19.0
#       2       11.0
# Name: data1, dtype: float64

print("Use unstacked method : ")
print(my_mean1.unstack())

# Use unstacked method : 
# key2     1     2
# key1            
# a      2.0  12.0
# b     19.0  11.0

print("================================")

states = np.array(["OH", "CA", "CA", "OH", "OH", "CA", "OH"])
years = np.array([2005, 2005, 2006, 2005, 2006, 2005, 2006])
print(df["data1"].groupby([states, years]).mean())

# Frequently, the grouping information is found in the same DataFrame as the data you
# want to work on. In that case, you can pass column names (whether those are strings,
# numbers, or other Python objects) as the group keys:

print(df.groupby("key1").mean())

#       key2      data1  data2
# key1                        
# a      1.5  11.333333   12.0
# b      1.5  15.000000   16.0

print(df.groupby("key1").median())

#       key2  data1  data2
# key1                    
# a      1.5   12.0    3.0
# b      1.5   15.0   16.0

print(df.groupby(["key1","key2"]).mean())

#            data1  data2
# key1 key2              
# a    1       2.0    3.0
#      2      12.0    2.0
# b    1      19.0   20.0
#      2      11.0   12.0

print(df.groupby(["key1","key2"]).median())

#            data1  data2
# key1 key2              
# a    1       2.0    3.0
#      2      12.0    2.0
# b    1      19.0   20.0
#      2      11.0   12.0



# Regardless of the objective in using groupby, a generally useful GroupBy method is
# size, which returns a Series containing group sizes:

print(df.groupby(["key1", "key2"]).size())

# key1  key2
# a     1       1
#       2       1
# b     1       1
#       2       1
# dtype: int64



