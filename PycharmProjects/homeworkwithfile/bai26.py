import math


class Circle:
    def __init__(self, radius:float, color:str):
        self.radius = radius
        self.color = color

    def getradius(self):
        return self.radius

    def setradius(self, radius):
        self.radius = radius

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def getarea(self):
        return self.radius ** 2 * math.pi


class Cylinder(Circle):
    def __init__(self, radius:float, color:str, height:float):
        Circle .__init__(self, radius, color)
        self.height = height


    def getheight(self):


    def setheight(self,height):


    def getvolume(self):
        return self.getarea()*self.height
