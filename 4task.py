string = input("Введите нескольких слов, разделённых пробелами ")
lst = string.split()
for i, el in enumerate(lst, 1):
    print(i, el[:10])
