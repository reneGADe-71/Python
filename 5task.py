summ = 0
while True:
    numbers = input("Введите числа через пробел или символ # для выхода: ")
    numbers.split()
    for i in numbers:
        try:
            summ = summ + float(i)
        except:
            if i == "#":
                print(f"Ваша сумма {summ}, выход")
                exit(0)
    print(f"Ваша сумма {summ}")
