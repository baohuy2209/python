import pandas as pd 

df = pd.DataFrame({"key1" : ["a", "a", None, "b", "b", "a", None],
                "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                "data1" : [2,12,23,11,19,20,8],
                "data2" : [3,2,34,12,20,31,4]})

print(df.groupby(["key1", "key2"])[["data2"]].mean())
print(df.groupby(["key1", "key2"])[["data2"]].mean())


