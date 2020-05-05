class Rider():
    def __init__(self, name):
        self.name = name


class Horse():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner



a_rider = Rider("Atsushi")
a_horse = Horse("Sekitoba", a_rider)


print(a_horse.owner.name)
