import pandas as pd 

data = {
    "Fullname" : ["Nguyen Bao Huy", "Nguyen Cao Phat"], 
    "Age" : [12,13]  
}

df = pd.DataFrame(data) 

print(df) 
print("Print first rows :")
print(df.loc[0])
print("Print second rows:")
print(df.loc[1])

print("Print full data : ")
print(df.loc[[0,1]])
