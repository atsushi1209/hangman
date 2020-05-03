import math

class Circle():
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2


a_circle = Circle(4)

print(a_circle.area())
