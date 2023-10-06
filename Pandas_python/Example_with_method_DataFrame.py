import pandas as pd

mydataset = {
    'cars' : ["BNW", "Volvo", "Ford"],
    'passings' : [3,7,2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)