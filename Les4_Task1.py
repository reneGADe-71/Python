# 3.1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

# import cProfile


n_1 = 2
n_2 = 9


def func_1(i):
    number = {}
    for n in range(n_1, n_2 + 1):
        number = []
        for f in range(2, i + 1):
            if f % n == 0:
                number.append(f)
    return len(number)


# Les4_Task1.func_1(99)
# 1000 loops, best of 5: 40.3 usec per loop
# Les4_Task1.func_1(999)
# 1000 loops, best of 5: 448 usec per loop
# Les4_Task1.func_1(9999)
# 1000 loops, best of 5: 4.69 msec per loop
# cProfile.run("func_1(99)")
# 1    0.000    0.000    0.000    0.000 Les4_Task1.py:10(func_1)
# cProfile.run("func_1(999)")
# 1    0.001    0.001    0.001    0.001 Les4_Task1.py:10(func_1)
# cProfile.run("func_1(9999)")
# 1    0.007    0.007    0.008    0.008 Les4_Task1.py:10(func_1)

def func_2(i):
    func_dict = dict()
    for div in range(n_1, n_2 + 1):
        func_dict[div] = i // div
    return func_dict


# Les4_Task1.func_2(99)
# 1000 loops, best of 5: 760 nsec per loop
# Les4_Task1.func_2(999)
# 1000 loops, best of 5: 780 nsec per loop
# Les4_Task1.func_2(9999)
# 1000 loops, best of 5: 851 nsec per loop
# cProfile.run("func_2(99)")
# 1    0.000    0.000    0.000    0.000 Les4_Task1.py:33(func_2)
# cProfile.run("func_2(999)")
# 1    0.000    0.000    0.000    0.000 Les4_Task1.py:33(func_2)
# cProfile.run("func_2(9999)")
# 1    1    0.000    0.000    0.000    0.000 Les4_Task1.py:33(func_2)


def func_3(i):
    func_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for n in range(n_1, i + 1):
        if n % 2 == 0:
            func_dict[2] += 1
        elif n % 3 == 0:
            func_dict[3] += 1
        elif n % 4 == 0:
            func_dict[4] += 1
        elif n % 5 == 0:
            func_dict[5] += 1
        elif n % 6 == 0:
            func_dict[6] += 1
        elif n % 7 == 0:
            func_dict[7] += 1
        elif n % 8 == 0:
            func_dict[8] += 1
        elif n % 9 == 0:
            func_dict[9] += 1
    return func_dict

# Les4_Task1.func_3(99)
# 1000 loops, best of 5: 15.3 usec per loop
# Les4_Task1.func_3(999)
# 1000 loops, best of 5: 165 usec per loop
# Les4_Task1.func_3(9999)
# 1000 loops, best of 5: 1.71 msec per loop
# cProfile.run("func_3(99)")
# 1    0.000    0.000    0.000    0.000 Les4_Task1.py:55(func_3)
# cProfile.run("func_3(999)")
# 1    0.000    0.000    0.000    0.000 Les4_Task1.py:55(func_3)
# cProfile.run("func_3(9999)")
# 1    0.002    0.002    0.002    0.002 Les4_Task1.py:55(func_3)

# Вариант 2 самый оптимальный. Алгоритм работает одинаково быстро на любых размерах входящих данных.
# Остальных два варианта работают медленне и при увеличении количества чисел в 10 раз время работы
# тоже увеличивается в 10 раз.
