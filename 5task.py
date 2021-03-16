receipt = float(input("Введите вашу выручку "))
cost = float(input("Введите ваши издержки "))
if receipt > cost:
    print("У вас прибыль!")
    rent = (receipt - cost) / receipt
    print("Ваша рентабельность ", rent * 100, "%")
    members = float(input("Введите численность сотрудников "))
    print("Прибыль на 1 человека равна ", (receipt - cost) / members)
else:
    print("У вас убыток(")
