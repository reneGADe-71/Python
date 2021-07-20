# import cProfile


def eratosthenes(n):
    lst_er = [i for i in range(2, n + 1)]
    for i in lst_er:
        for y in lst_er[i:]:
            if y % i == 0:
                lst_er.remove(y)
    return lst_er


def without_eratosthenes(n):
    lst = []
    for i in range(2, n + 1):
        number = True
        for y in range(2, i):
            if i % y == 0:
                number = False
                break
        if number:
            lst.append(i)
    return lst


# cProfile.run("eratosthenes(10)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:4(eratosthenes)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         5    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
# cProfile.run("eratosthenes(100)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:4(eratosthenes)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:5(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        74    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
# cProfile.run("eratosthenes(1000)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 Les4_Task2.py:4(eratosthenes)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:5(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       831    0.003    0.000    0.003    0.000 {method 'remove' of 'list' objects}
# cProfile.run("without_eratosthenes(10)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:13(without_eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run("without_eratosthenes(100)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Les4_Task2.py:13(without_eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run("without_eratosthenes(1000)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 Les4_Task2.py:13(without_eratosthenes)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Les4_Task2.eratosthenes(10)
# 1000 loops, best of 5: 1.99 usec per loop
# Les4_Task2.eratosthenes(100)
# 1000 loops, best of 5: 38.6 usec per loop
# Les4_Task2.eratosthenes(1000)
# 1000 loops, best of 5: 2.31 msec per loop
# Les4_Task2.without_eratosthenes(10)
# 1000 loops, best of 5: 2.56 usec per loop
# Les4_Task2.without_eratosthenes(100)
# 1000 loops, best of 5: 58.7 usec per loop
# Les4_Task2.without_eratosthenes(1000)
# 1000 loops, best of 5: 3.28 msec per loop
