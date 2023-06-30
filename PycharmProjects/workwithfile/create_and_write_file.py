x = int(input("Enter the integer :"))

f = open('fileinteger.txt','w')
f.write(str(x))
f.close()
f = open('fileinteger.txt','r')
nd = f.readline()
print(nd)
