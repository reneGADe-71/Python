text = {"One": "Odin", "Two": "Dva", "Three": "Tri", "Four": "Chetyry"}
new_text = []
with open("4task.txt", "r") as file_obj:
    for i in file_obj:
        i = i.split(" ", 1)
        new_text.append(text[i[0]] + " " + i[1])

with open("4task_new.txt", "w") as file_obj:
    file_obj.writelines(new_text)
