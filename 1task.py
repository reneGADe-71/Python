from sys import argv

script_name, time, pay, bonus = argv

salary = int(time) * int(pay) + int(bonus)
print(f"Заработная плата: {salary}")

# в командной строке
# python 1task.py 15 5 20
# ответ 95
