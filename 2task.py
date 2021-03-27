from random import randint

number = int(input("Введите количество чисел в списке: "))
lst = [randint(0, 100) for el in range(number)]
new_lst = [lst[el] for el in range(1, number) if lst[el] > lst[el-1]]
print(f"Исходный список {lst}")
print(f"Новый список {new_lst}")
