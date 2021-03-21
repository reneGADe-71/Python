lst_1 = [2, 5, 8, 2, 12, 12, 4]
lst_2 = [2, 7, 12, 3]
for number in lst_1[:]:
    if number in lst_2:
        lst_1.remove(number)
print(lst_1)
