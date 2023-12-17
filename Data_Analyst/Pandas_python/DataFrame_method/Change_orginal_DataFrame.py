import pandas as pd 
df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv')
#If you want to change the orginal DataFrame, use the inplace = True argument
df.dropna(inplace = True)

print(df.to_string()); 

#Notice in the result that some rows have been removed (row 18, 22 and 28).

#These rows had cells with empty values.
