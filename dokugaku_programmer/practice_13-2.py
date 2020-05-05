class Square():
    def __init__(self, hen):
        self.hen = hen

    def calculate_perimeter(self):
        return self.hen * 4

    def change_size(self, param):
        origin_hen = self.hen
        self.hen = self.hen + param
        if self.hen < 0:
            print("0より小さくはできません。")
            self.hen = origin_hen
            


a_square = Square(20)
print(a_square.calculate_perimeter())

a_square.change_size(5)
print(a_square.calculate_perimeter())

a_square.change_size(-5)
print(a_square.calculate_perimeter())

a_square.change_size(-25)
print(a_square.calculate_perimeter())

a_square.change_size(-19)
print(a_square.calculate_perimeter())
