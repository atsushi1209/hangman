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


def same_object_check(object1, object2):
    print(object1 is object2)


object1 = Square(20)
object2 = object1

same_object_check(object1, object2)

object3 = Square(20)
object4 = Square(20)


same_object_check(object3, object4)


# 以下が正解

def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "a"))
print(compare("a", "b"))
