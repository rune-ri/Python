# take input
# get the json configs,
# based on json configs, process the list of inputs, 
# discard inputs that after operation lead to outOfBoundError 
# check the ouput list to see if it is correct through testing.
import json

def square(x):
    return x*x
def cube(x):
    return x*x*x
def double(x):
    return 2*x

ops = {
    "square": square,
    "cube": cube,
    "double": double
}

li = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]

with open("configs.json", "r") as file:
    data = json.load(file)

print(data)

operation = data["operation"]
operation = ops[operation]
limit = data["limit"]
allow_neg = data["allow_negatives"]
i = 0
for x in li:
    # if operation == "square":
    # # false only matters for output so we do operatoi nfirst.
    # # similarly limit only matters after oepration so operation first.
    #     x = x * x
    x = operation(x)
    if allow_neg == False: 
        if x < 0:
            x = "nope"
    if x != "nope" and abs(x) >= limit:
        x = "nope"
    li[i] = x
    i += 1

print(li)

# now 2 approaches, i iterate backwards to remove "nope". but time complexity is high space is low.
# or i make list from old list where "nope" isnt there.
# try both.

lis = [x for x in li if x != "nope"]
# we do not use `is not` for string comparison
# or 

for j in range(len(li)-1, -1, -1):
    if li[j] == "nope":
        li.pop(j)

print(lis)
print(li)
