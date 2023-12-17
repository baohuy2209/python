import pandas as pd 

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                "data1" : [2,12,23,11,19,20,8],
                "data2" : [3,2,34,12,20,31,4]})

# Of course, you can choose to do whatever you want with the pieces of data. A recipe
# you may find useful is computing a dictionary of the data pieces as a one-liner:

grouped1 = {name : group for name, group in df.groupby("key1")}
for name, group in grouped1.items():
    print(name)
    print(group)

# a
#   key1  key2  data1  data2
# 0    a     1      2      3
# 1    a     2     12      2
# 5    a  <NA>     20     31
# b
#   key1  key2  data1  data2
# 3    b     2     11     12
# 4    b     1     19     20

grouped2 = {name : group for name, group in df.groupby("key2")}
for name, group in grouped2.items():
    print(name)
    print(group)
    
#   key1  key2  data1  data2
# 0     a     1      2      3
# 2  None     1     23     34
# 4     b     1     19     20
# 6  None     1      8      4
# 2
#   key1  key2  data1  data2
# 1    a     2     12      2
# 3    b     2     11     12
