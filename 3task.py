class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f"Размер клетки после сложения: {self.quantity + other.quantity}"

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f"Размер клетки после вычитания: {sub}" if sub > 0 else "Клетка пропала"

    def __truediv__(self, other):
        fun = self.quantity // other.quantity
        return f"Размер клетки после деления: {fun}" if other.quantity > 0 else "Деление невозможно"

    def __mul__(self, other):
        return f"Размер клетки после умножения: {self.quantity * other.quantity}"

    def make_order(self, row):
        result = ""
        for i in range(int(self.quantity / row)):
            result += "*" * row + "\n"
        result += "*" * (self.quantity % row) + "\n"
        return result


cell_1 = Cell(15)
cell_2 = Cell(5)
print(f"Первая клетка: {cell_1.quantity}")
print(f"Вторая клетка: {cell_2.quantity}")
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(4))
