class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"У вас {self.title}. Запуск отрисовки Pen"


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"У вас {self.title}. Запуск отрисовки Pencil"


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"У вас {self.title}. Запуск отрисовки Handle"


pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
