my_f = open("3task.txt", "r")
text = my_f.read().split('\n')
print(text)
low = []
pay = 0
for i in text:
    lst = i.split(" ")
    if int(lst[1]) < 20000:
        low.append(lst[0])
    pay = pay + int(lst[1])

print(f"Зарплата ниже у {', '.join(low)}")
print(f"Средняя зарплата {pay / len(text)}")
my_f.close()
