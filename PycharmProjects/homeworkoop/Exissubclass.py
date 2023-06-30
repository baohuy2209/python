class Base(object) :
    pass
class Derived(Base) :
    pass


print(issubclass(Derived,Base)) # ham kiem tra co phai la lop con hay khong
# Cu phap : issubclass(lop con , lop cha) # se tra ve gia tri true .
# Neu dao lai hoac khong phai lop con thi tra ve gia tri true
print(issubclass(Base,Derived))

d = Derived()
b = Base()

print(isinstance(b,Derived))
# Cu phap : isinstance
print(isinstance(d,Base))