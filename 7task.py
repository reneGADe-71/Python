from math import factorial


def fact(n):
    for i in range(1, n + 1):
        number = factorial(i)
        yield number


n = int(input("Укажите число конечного факториала: "))
for el in fact(n):
    print(el)
