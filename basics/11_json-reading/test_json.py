import json 

# now i need to call all the keys. for that reading is required.

file = open("file.json", "r")
data = json.load(file)
file.close()

# once i have this, i need to get all the keys of the mapping.

for keys, expected in data.items():
    actual = data[keys]
    assert expected == actual, (
        f"FAIL: {keys} - expected {expected}, "
        f"got {actual}"
    )
    print(f"PASS: {keys}")
