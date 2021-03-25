def my_func(a,b,c):
    number = [a, b, c]
    number.remove(min(a, b, c))
    return sum(number)


print(my_func(-5, 2, 5))
