# Nhap cac so nguyen vao file roi in ra cac so chan rieng va so le rieng

with open('fileinteger2.txt','r') as obj:
    even = [int(i) for i in obj if int(i)%2 == 0]
    odd  = [int(i) for i in obj if int(i)%2 != 0]


print("Even elements :")
print(even)
print("Odd elements :")
print(odd)