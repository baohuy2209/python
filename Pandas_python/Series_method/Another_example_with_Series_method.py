import pandas as pd 

a = [8.0, 9.4, 10.4, 8.5]

myseries = pd.Series(a) 

print(myseries)

print(myseries[3])

print(myseries[1])

for i in range(0, len(myseries)):
    print(myseries[i])
    