month = int(input("Введите номер месяц от 1 до 12: "))
a = "Зима"
b = "Весна"
c = "Лето"
d = "Осень"
lst = [a, a, b, b, b, c, c, c, d, d, d, a]
print(lst[month - 1])

dict_m = {1: a, 2: a, 3: b, 4: b, 5: b, 6: c, 7: c, 8: c, 9: d, 10: d, 11: d, 12: a}
print(dict_m[month])
