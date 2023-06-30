a = int(input("Enter a : "))
b = int(input("Enter b : "))
dem = 0
for i in range(a,b+1) :
    dem += i
f = open('DL.txt','w')
f.write(str(a))
f.write('\n')
f.write(str(b))
f.write('\n')
f.write(str(dem))
f.close()
f.open('DL.txt','r')
nd = f.read()
print(nd)
