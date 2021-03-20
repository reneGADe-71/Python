a = int(input("Сколько элементов будет в вашем списке: "))
lst = []
for i in range(0, a):
    ele = input("Введите элемент: ")
    lst.append(ele)
print(lst)
n = len(lst)
if n % 2 == 0:
    lst[::2], lst[1::2] = lst[1::2], lst[::2]
else:
    lst[:-1:2], lst[1:-1:2] = lst[1:-1:2], lst[:-1:2]
print(lst)
