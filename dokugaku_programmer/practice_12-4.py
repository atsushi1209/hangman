class Hexagon():
    def __init__(self, hen):
        self.hen = hen


    def calculate_perimeter(self):
        return self.hen * 6

a_hexagon = Hexagon(6)
print(a_hexagon.calculate_perimeter())
