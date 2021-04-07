class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self.__weight_1sm = 0.025
        self.__height = 5

    def calculation(self):
        return self._length * self._width * self.__weight_1sm * self.__height


road = Road(5000, 20)
print(road.calculation())
