class Employee :
    def __init__(self):
        print("Emp;oyee create ")

    def __del__(self):
        print(" Destructor called ")

def create_obj() :
    print("Making Object ...")
    obj = Employee()
    print("Function end ...")
    return obj

print ("Calling create_obj() function ... ")
obj = create_obj()
print("Program End ") 