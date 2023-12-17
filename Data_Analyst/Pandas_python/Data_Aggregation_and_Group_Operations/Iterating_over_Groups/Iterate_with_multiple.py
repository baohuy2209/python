import pandas as pd 

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                "data1" : [2,12,23,11,19,20,8],
                "data2" : [3,2,34,12,20,31,4]})


for (k1,k2), group in df.groupby(["key1","key2"]): 
    print((k1,k2)) # print two keys in current time 
    print(group)
    
# ('a', 1)
#   key1  key2  data1  data2
# 0    a     1      2      3
# ('a', 2)
#   key1  key2  data1  data2
# 1    a     2     12      2
# ('b', 1)
#   key1  key2  data1  data2
# 4    b     1     19     20
# ('b', 2)
#   key1  key2  data1  data2
# 3    b     2     11     12