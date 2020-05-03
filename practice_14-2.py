class Square():
    square_list = []

    def __init__(self, hen):
        self.hen = hen
#        self.square_list.append((hen))
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.hen * 4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.hen, self.hen, self.hen, self.hen)


object1 = Square(20)
print(object1)
