import pandas as pd 

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                "data1" : [2,12,23,11,19,20,8],
                "data2" : [3,2,34,12,20,31,4]})

grouped = df.groupby({"key1" : "key", "key2": "key",
                    "data1" : "data", "data2": "data"}, axis = "columns")

for group_key, group_values in grouped: 
    print(group_key)
    print(group_values)
    
# data
#    data1  data2
# 0      2      3
# 1     12      2
# 2     23     34
# 3     11     12
# 4     19     20
# 5     20     31
# 6      8      4
# key
#    key1  key2
# 0     a     1
# 1     a     2
# 2  None     1
# 3     b     2
# 4     b     1
# 5     a  <NA>
# 6  None     1
    
