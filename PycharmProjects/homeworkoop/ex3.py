# Example about super()
# -----------------------------------------------------------
# Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
# @author cafedevn
# Contact: cafedevn@gmail.com
# Fanpage: https://www.facebook.com/cafedevn
# Instagram: https://instagram.com/cafedevn
# Twitter: https://twitter.com/CafedeVn
# Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
# -----------------------------------------------------------


# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base(object):

    # Constructor
    def __init__(self, x):
        self.x = x


class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        # In Python 3.x, "super().__init__(name)"
            #also works'''
        super(Derived, self).__init__(x)
        self.y = y

    def printXY(self):
        # Note that Base.x won't work here
        # because super() is used in constructor
        print(self.x, self.y)

    # Driver Code


d = Derived(10, 20)
d.printXY()