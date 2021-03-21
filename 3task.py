name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
weight = int(input("Введите вес: "))
if age < 30 and 50 < weight < 120:
    a = "хорошее состояние"
elif age > 30 and 120 < weight < 50:
    a = "следует заняться собой"
else:
    a = "следует обратиться к врачу"
print(name, ",", surname, ",", age, "год", ", вес",  weight, ", -", a)
