class Coat:
    def __init__(self, v):
        self.square_c = v / 6.5 + 0.5


class Suit:
    def __init__(self, h):
        self.square_s = h * 2 + 0.3


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
        main_square1 = 0
        main_square2 = 0
        for v1 in self.v1:
            main_square1 = main_square1 + v1.square_c
        for v2 in self.v2:
            main_square2 = main_square2 + v2.square_s
        main_square = main_square1 + main_square2
        return f"Итоговый расход ткани: {main_square}"


clothes = Clothes()
clothes.add_coat(6.5)
clothes.add_coat(13)
clothes.add_suit(0.35)
clothes.add_suit(0.85)

print(clothes.square)
