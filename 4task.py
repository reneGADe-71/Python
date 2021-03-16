n = input("Введите положительное целое число ")
n = float(n)
m = 0
if (n > 0) and (n % 1 == 0):
    while n:
        if n % 10 > m:
            m = n % 10
        n = n // 10
    print(int(m))
else:
    print("Вы ввели некорректное число")
