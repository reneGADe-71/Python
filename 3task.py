class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


a = Position("Aleksey", "Kiselev", "Worker", 35000, 5000)
b = Position("Ivan", "Ivanov", "Director", 47500, 13000)
print(f"В компании {a.position} {a.name} и {b.position} {b.name}")
print(f"Полное имя {a.get_full_name()}")
print(f"Доход с учетом премии {a.get_total_income()}")
print(f"Полное имя {b.get_full_name()}")
print(f"Доход с учетом премии {b.get_total_income()}")
