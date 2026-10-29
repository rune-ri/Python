import json

with open("data.json", "r") as file:
    data = json.load(file)

newentry = {
    "id": 4,
    "name": "ri",
    "age": 21
}
data["users"].append(newentry)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

