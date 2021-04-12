class Coat:
    def __init__(self, v):
        self.v = v
        self.square_c = self.v / 6.5 + 0.5

    def __str__(self):
        return f"Ткань на пальто {self.square_c}"


class Suit:
    def __init__(self, h):
        self.h = h
        self.square_s = self.h * 2 + 0.3

    def __str__(self):
        return f"Ткань на костюм {self.square_s}"


class Clothes:
    def __init__(self):
        self.v1 = []
        self.v2 = []

    def add_coat(self, v):
        self.v1.append(Coat(v))

    def add_suit(self, h):
        self.v2.append(Suit(h))

    @property
    def square(self):
        main_square = (self.v1 / 6.5 + 0.5) + (self.v2 * 2 + 0.3)
        return f"Сумма ткани {main_square}"


coat = Coat(13)
suit = Suit(1)
print(coat)
print(suit)
print(Clothes.square)
