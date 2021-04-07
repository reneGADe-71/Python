class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn_right(self):
        return f"{self.name} повернула направо"

    def turn_left(self):
        return f"{self.name} повернула налево"

    def show_speed(self):
        return f"Скорость {self.name} {self.speed}"


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость {self.name} {self.speed}")

        if self.speed > 40:
            return f"{self.name} превышает для городской"
        else:
            return f"У {self.name} допустимая скорость"


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость {self.name} {self.speed}")

        if self.speed > 60:
            return f"{self.name} превышает для рабочей"
        else:
            return f"У {self.name} допустимая скорость"


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        return f"{self.name} полицейская"


a = TownCar(60, "White", "Opel", False)
b = SportCar(150, "Yellow", "Bugatti", False)
c = WorkCar(50, "Black", "Ford", False)
d = PoliceCar(100, "Blue", "Nissan", True)

print(f"{a.go()} на перекрестке, а {c.stop()} пропускать")
print(f"{b.turn_left()}, а потом {b.turn_right()}")
print(a.show_speed())
print(c.show_speed())
print(f"{b.name} {b.color} цвета")
print(f"{c.name} полицеская? {c.is_police}")
print(f"{d.name} полицеская? {d.is_police}")
print(d.police())
