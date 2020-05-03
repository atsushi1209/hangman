class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2


class Square(Shape):
    def __init__(self, hen):
        self.hen = hen

    def calculate_perimeter(self):
        return self.hen * 4


a_rectangle = Rectangle(20, 30)

a_square = Square(20)


a_rectangle.what_am_i()

a_square.what_am_i()

