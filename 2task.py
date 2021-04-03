my_f = open("2task.txt", "r")
text = my_f.readlines()
print(text)
print(f"Количество строк: {len(text)}")

number = 0
for i in text:
    count = 1
    number = number + 1
    while "  " in i:
        i = i.replace("  ", " ")
    for n in i:
        if n == " ":
            count = count + 1
    print(f"Количество слов в строке {number}: {count}")
my_f.close()
