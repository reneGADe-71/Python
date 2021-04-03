with open("5task.txt", "w+") as file_obj:
    number = input("Введите цифры через пробел: ")
    file_obj.writelines(number)
    file_obj.seek(0)
    lst = file_obj.read().split()
    s = 0
    for i in lst:
        s = s + int(i)
    print(f"Сумма введенных чисел: {s}")
