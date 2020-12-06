import json


def get_data_from_json():
    with open("json_file.json", "r") as file:
        data = json.load(file)
        file.close()
        return data


def add_new_task(title, description):
    data = get_data_from_json()
    data["tasks"].append({"title": title, "description": description})
    with open("json_file.json", "w") as file:
        file.seek(0)
        json.dump(data, file)
        file.close()


def remove_task(title):
    data = get_data_from_json()
    for task in data["tasks"]:
        if task["title"] == title:
            data["tasks"].remove(task)
    with open("json_file.json", "w") as file:
        file.seek(0)
        json.dump(data, file)
        file.close()


print("---TASKS---")
for task in get_data_from_json()["tasks"]:
    print("   {}\n      {}\n".format(task["title"], task["description"]))
print("-----------")
print("Add new task --> [a]")
print("Remove task --> [r]")
print("exit --> [exit]")
action = input("Action: ")
if action == "a":
    add_new_task(input("Task title: "), input("Task description: "))
elif action == "r":
    remove_task(input("Task title: "))
elif action == "exit":
    exit()
else:
    print("Improper actions cmd")
