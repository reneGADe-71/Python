def my_func(number_1, number_2):
    try:
        division = number_1 / number_2
        return division
    except ZeroDivisionError:
        return "Нельзя делить на ноль"


print(my_func(float(input("Введите первое число: ")), float(input("Введите второе число: "))))
