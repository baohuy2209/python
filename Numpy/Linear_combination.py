import numpy as np 

vt1 = np.array([1,2,4]) 
vt2 = np.array([2,1,8]) 
vt3 = np.array([4,5,1]) 

transpose1 = np.transpose(vt1)
transpose2 = np.transpose(vt2)
transpose3 = np.transpose(vt3)

matrix = []
for element1, element2, element3 in zip(transpose1, transpose2, transpose3):
	list = [element1, element2, element3]
	matrix.append(list)

linear_combination = np.array(matrix)
b = np.array([3,2,5])

result = np.transpose(b)*np.linalg.inv(linear_combination)

print(result)
