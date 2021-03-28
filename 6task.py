def int_func(a):
   return a.title()


print(int_func("my test text"))


def my_func(text):
   lst = []
   for i in range(len(text)):
      lst.append(text[i][0:1].upper() + text[i][1:])
   return ' '.join(lst)


print(my_func(input("Введите текст через пробел: ").split()))
