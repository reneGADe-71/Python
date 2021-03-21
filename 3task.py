lst_1 = input('Введите любые целые числа в любом порядке через пробел: ').split()
lst_2 = []
numbers = 0
for number in lst_1:
    if lst_1.count(number) == 1:
        lst_2.append(number)
print('Исходный список: ', lst_1)
print('Список уникальных элементов:', lst_2)
