    class DividingByZero:
    def __init__(self, divided, divisor):
        self.divided = divided
        self.divisor = divisor

    @staticmethod
    def dividing_by_zero(divided, divisor):
        try:
            return divided / divisor
        except:
            return "Деление на ноль недопустимо"


print(DividingByZero.dividing_by_zero(50, 0))
print(DividingByZero.dividing_by_zero(50, 0.5))
print(DividingByZero.dividing_by_zero(50, 5))
