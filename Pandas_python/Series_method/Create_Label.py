import pandas as pd 

a = [1,23,43]
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["x"]) 
print(myvar["y"])
print(myvar["z"]) 

