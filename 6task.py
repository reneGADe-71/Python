from itertools import count
from itertools import cycle

n = int(input("Введите стартовое число: "))
for el in count(n):
    if el > n + 5:
        break
    else:
        print(el)

lst = ["one", "two", "three"]
c = 0
for el in cycle(lst):
    if c > 5:
        break
    print(el)
    c = c + 1
