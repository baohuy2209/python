import pandas as pd 

myBook = {
    'Name of Book' : ["Python", "Java", "Javascript"],
    'Number of page' : [123,453,231]
}

mytable = pd.DataFrame(myBook)

print(mytable) 