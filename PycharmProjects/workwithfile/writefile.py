n = int(input("Enter the length of array :"))

with open('fileinteger2.txt','w') as obj :
    for i in range(n):
        x = int(input("Element :"))
        obj.write(str(x)+"\n")
