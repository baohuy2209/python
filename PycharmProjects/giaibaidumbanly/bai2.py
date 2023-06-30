a = int(input("enter a : "))
tong = 0
for i in range(1,a+1) :
    tong += i
f = open('KQ.txt','w')
f.write(str(tong))
f.close()
f = open('KQ.txt','r')
nd = f.read()
print(nd)