a = int(input("Введите время в секундах "))
b = a // 3600 % 24
c = a // 60 % 60
d = a % 60
if b < 10:
    b = "0" + str(b)
else:
    b = str(b)
if c < 10:
    c = "0" + str(c)
else:
    c = str(c)
if d < 10:
    d = "0" + str(d)
else:
    d = str(d)
print("Время ", b, ":", c, ":", d)
