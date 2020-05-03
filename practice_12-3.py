class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


a_triangle = Triangle(2,3)

print(a_triangle.area())
