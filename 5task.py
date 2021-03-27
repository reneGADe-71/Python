from functools import reduce

lst = [el for el in range(100, 1001, 2)]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, lst))
