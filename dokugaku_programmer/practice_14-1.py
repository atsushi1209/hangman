
class Square():
    square_list = []

    def __init__(self, hen):
        self.hen = hen
#        self.square_list.append((hen))
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.hen * 4


object1 = Square(20)
object2 = Square(30)
object3 = Square(40)

#print(object3.square_list)
print(Square.square_list)
