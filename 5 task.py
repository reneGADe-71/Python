lst = [9, 8, 5, 5, 3, 1]
print(lst)
number = int(input("Введите целое число: "))
lst.append(number)
lst.sort(reverse=True)
print(lst)

lst_1 = [9, 8, 5, 5, 3, 1]
n = lst_1.count(number)
for i in lst_1:
    if n > 0:
        y = lst_1.index(number)
        lst_1.insert(y + n, number)
        break
    elif number > i:
        y = lst_1.index(i)
        lst_1.insert(y, number)
        break
    elif number < lst_1[len(lst_1) - 1]:
        lst_1.append(number)
print(lst_1)
