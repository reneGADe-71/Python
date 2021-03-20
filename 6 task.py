a = int(input("Сколько товаров у вас будет: "))
my_list = []
n = 1
for i in range(0, a):
    lst = []
    a = input("Введите название: ")
    b = int(input("Введите цену: "))
    c = int(input("Введите количество: "))
    d = input("Введите единицу измерения: ")
    ele = dict(название=a, цена=b, количество=c, ед=d)
    lst.append(n)
    lst.append(ele)
    prod = tuple(lst)
    my_list.append(prod)
    n = n + 1
print(*my_list, sep="\n")

lst_name = []
lst_cost = []
lst_number = []
lst_unit = []
m = 0
for i in my_list:
    name = my_list[m][1]["название"]
    cost = my_list[m][1]["цена"]
    number = my_list[m][1]["количество"]
    unit = my_list[m][1]["ед"]
    lst_name.append(name)
    lst_cost.append(cost)
    lst_number.append(number)
    lst_unit.append(unit)
    m = m + 1
new_lst_name = []
new_lst_cost = []
new_lst_number = []
new_lst_unit = []
for i in lst_name:
    if i not in new_lst_name:
        new_lst_name.append(i)
for i in lst_cost:
    if i not in new_lst_cost:
        new_lst_cost.append(i)
for i in lst_number:
    if i not in new_lst_number:
        new_lst_number.append(i)
for i in lst_unit:
    if i not in new_lst_unit:
        new_lst_unit.append(i)
dct = dict(название=new_lst_name, цена=new_lst_cost, количество=new_lst_number, ед=new_lst_unit)
for key, value in dct.items():
    print(key, ":", value)
