import json

with open("file.json", "r") as file: 
    data = json.load(file)
# for this you could also just write `file = open("file.json", "r")` and then continue.
# but for that, you would also have to at the end take care of `file.close()` 
# using `with`, you can directly ignore it coz python automatically closes it.
print(data)
print(data["name"])
print(data["subjects"][0])
