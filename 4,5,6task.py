class Storage:
    def __init__(self):
        self.dict = {}

    def add_to(self, equipment):
        self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class BaseClass:
    def __init__(self, name, model, cost):
        self.name = name
        self.model = model
        self.cost = cost
        self.group = self.__class__.__name__

    def group_name(self):
        return f"{self.group}"

    def __repr__(self):
        return f"{self.name} {self.model} {self.cost}"


class Printer(BaseClass):
    def __init__(self, name, model, series, cost):
        super().__init__(name, model, cost)
        self.series = series

    def __repr__(self):
        return f"{self.name} {self.series} {self.model} {self.cost}"


class Scanner(BaseClass):
    def __init__(self, name, model, cost):
        super().__init__(name, model, cost)


class Xerox(BaseClass):
    def __init__(self, name, model, cost):
        super().__init__(name, model, cost)


storage = Storage()
xerox = Xerox("Samsung", "150-I", 15000)
storage.add_to(xerox)
scanner = Scanner("HP", "320-TL", 8000)
storage.add_to(scanner)
scanner = Scanner('LG', '240-Y', 9000)
storage.add_to(scanner)
printer = Printer("Sony", "1035-MF", "1-series", 10000)
storage.add_to(printer)
printer = Printer("Sony", "1025-MF", "2-series", 12000)
storage.add_to(printer)
print(f"Сейчас на складе: {storage.dict}")
storage.extract("Scanner")
storage.extract("Xerox")
storage.extract("Printer")
print(f"Осталось на складе: {storage.dict}")
