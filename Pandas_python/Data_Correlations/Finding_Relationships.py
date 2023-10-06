import pandas as pd 

df = pd.read_csv('C:/Users/ADMIN/Documents/GitHub/Pandas_python/DataFrame_method/data1.csv') 
print(df.corr())

#RESULT EXPLAINED
# The Result of the corr() method is a table with a lot of numbers that respresents how well the relationship is between two columns. 
# The number varies from -1 to 1 
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, 
# each time a value went up in the first column, the other on went up as well. 
# 
# 0.9 is also a good relationship, and if you increase one value,
# the other will probably increase as well. 
# 
# -0.9 is also a good relationship, 
# but if you increase one value, 
# the other will probably go down. 
#
# 0.2 means NOT a good relationship,
# meaning that if one value goes up does not mean that the other will 
#
# What is a good correlation? 
# It depends on the use,
# but I think it is safe to say you have to have at least 0.6 ( or -0.6) to call it a good correlation.
#  
# PERFECT CORRELATION: 
# We can see that "Duration" and "Duration" got the number 1.000000, 
# which makes sense, each column always has a perfect relationship with itself. 
# 
# GOOD CORRELATION:
# "Duration" and "Calories" got a 0.922721 correlation, 
# which is a very good correlation, and we can predict that the longer you work out,
# the more calories you burn, and the other way around: If you burned a lot of calories, 
# you probably had a long work out. 
# 
# 
# 
# 
# 
# 
# 
# ##