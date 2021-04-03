result = {}
my_f = open("6task.txt", "r")
text = my_f.read().split("\n")

for line in text:
    lst = []
    a = line.split(' ')
    a[0] = a[0][:-1]
    a[1] = a[1][:-3]
    a[2] = a[2][:-4]
    a[3] = a[3][:-5]
    for i in a:
        if i == "":
            lst.append("0")
        else:
            lst.append(i)
    result[lst[0]] = int(lst[1]) + int(lst[2]) + int(lst[3])
print(f"Суммарное количество часов: {result}")
