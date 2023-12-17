import pandas as pd 

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                "data1" : [2,12,23,11,19,20,8],
                "data2" : [3,2,34,12,20,31,4]})

print(df.groupby("key1").mean())
print("========================")

#       key2      data1  data2
# key1                        
# a      1.5  11.333333   12.0
# b      1.5  15.000000   16.0
# ========================

for name, group in df.groupby("key1"):
    print(name)
    print("=======================")
    print(group)
    
# a
# =======================
#   key1  key2  data1  data2
# 0    a     1      2      3
# 1    a     2     12      2
# 5    a  <NA>     20     31
# b
# =======================
#   key1  key2  data1  data2
# 3    b     2     11     12
# 4    b     1     19     20

for name, group in df.groupby("key1"):
    print(name)
    print("=======================")
    print(group)
    
# a
# =======================
#   key1  key2  data1  data2
# 0    a     1      2      3
# 1    a     2     12      2
# 5    a  <NA>     20     31
# b
# =======================
#   key1  key2  data1  data2
# 3    b     2     11     12
# 4    b     1     19     20