import pandas as pd 
import numpy as np 

people = pd.DataFrame(np.random.randn(5,5),
						columns = ['a', 'b', 'c', 'd', 'e'],
						index = ['Joe', 'Steve', 'Wes', 
						'Jim', 'Travis'])

people.iloc[2:3, [1,2]] = np.nan 

mapping = {
	'a' : 'red', 
	'b' : 'red', 
	'c' : 'blue',
	'd' : 'blue',
	'e' : 'red',
	'f' : 'orange'
}

bycolumn = people.groupby(mapping)
print(bycolumn.sum())

map_series = pd.Series(mapping)

print(map_series.to_string())

print(people.groupby(map_series, axis = 1).count())