class NotNumber:
    def __init__(self):
        self.lst = []

    def my_list(self):
        while True:
            try:
                number = input("Введите целое число или stop чтоб выйти: ")
                if number == "stop":
                    break
                self.lst.append(int(number))
            except:
                print(f"Вы ввели некорректно")
        print(f"Введенный список {self.lst}")


n = NotNumber()
n.my_list()
