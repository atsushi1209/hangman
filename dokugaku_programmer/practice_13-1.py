class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2


class Square():
    def __init__(self, hen):
        self.hen = hen

    def calculate_perimeter(self):
        return self.hen * 4


a_rectangle = Rectangle(20, 30)

a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

