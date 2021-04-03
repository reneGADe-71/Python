import json
dct = {}
profit = {}
profit_sum = 0
n = 0
with open("7task.txt", "r") as file_obj:
    for i in file_obj:
        firm, organization, gain, costs = i.split()
        dct[firm] = int(gain) - int(costs)
        if dct.setdefault(firm) >= 0:
            profit_sum = profit_sum + dct.setdefault(firm)
            n = n + 1
    average = profit_sum / n
    print(f"Average profit: {average}")

    profit = {"Average profit:": round(average)}
    dct.update(profit)
    print(f"Result work: {dct}")

with open("7task.json", "w") as json_obj:
    json.dump(dct, json_obj)
