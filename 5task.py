def my_func():
    summ = 0
    a = []
    while True:
        numbers = input("Введите числа через пробел или символ # для выхода: ")
        a = numbers.split(" ")
        for i in a:
            try:
                summ = summ + float(i)
            except:
                if i == "#":
                    return summ
        print(f"Ваша сумма {summ}")


print(f"Ваша сумма {my_func()}, выход")
