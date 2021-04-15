class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма чисел s = {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"Произведение чисел p = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"

    def __str__(self):
        return f"Комплексное число n = {self.a} + {self.b} * i"


n1 = ComplexNumber(1, -1)
n2 = ComplexNumber(2, 2)
n3 = ComplexNumber(5, 6)
print(n1)
print(n1 + n2)
print(n1 * n3)
