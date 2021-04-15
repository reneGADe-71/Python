class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extraction(cls, day_month_year):
        date = day_month_year.split("-")
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return "Правильная дата"
                else:
                    return "Неправильный год"
            else:
                return "Неправильный месяц"
        else:
            return "Неправильный день"

    def __str__(self):
        return f'Текущая дата {Data.extraction(self.day_month_year)}'


today = Data("11-1-2001")
print(today)
print(Data.validation(32, 10, 2021))
print(Data.validation(15, 15, 2021))
print(Data.validation(15, 10, 2025))
print(Data.validation(15, 10, 2021))
print(Data.extraction("20-04-1990"))
