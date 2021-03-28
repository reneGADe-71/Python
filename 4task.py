def my_func(x, y):
    n = 1
    try:
        for i in range(abs(y)):
            n *= x
        return 1 / n
    except ZeroDivisionError:
        return "ноль в отрицательной степени не имеет смысла"


print(my_func(3, -5))
