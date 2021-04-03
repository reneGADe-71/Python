my_f = open("test.txt", "w")
lst = []
while True:
    text = input("Введите текст, чтоб выйти оставьте строку пустой: ") + "\n"
    if text == "\n":
        break
    lst.append(text)
print(lst)
my_f.writelines(lst)
my_f.close()
