import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data.csv') 

new_df = df.dropna() 

print(new_df)

# Notice in the result that same rows have been removed (row 18, 22 and 28)
# These rows had cells will empty values. 

#One way to deal with empty cells is to remove rows that contain empty cells. 
#This ís usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result. 

