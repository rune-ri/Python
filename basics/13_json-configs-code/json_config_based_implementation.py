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

def config_imp(li, data):
    operation = data["operation"]
    operation = ops[operation]
    limit = data["limit"]
    allow_neg = data["allow_negatives"]
    i = 0
    for x in li:
        x = operation(x)
        if allow_neg == False: 
            if x < 0:
                x = "nope"
        if x != "nope" and abs(x) >= limit:
            x = "nope"
        li[i] = x
        i += 1
    
    lis = [x for x in li if x != "nope"]
   
    for j in range(len(li)-1, -1, -1):
        if li[j] == "nope":
            li.pop(j)
    return lis,li

if __name__ == "__main__":
    li = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
    
    with open("configs.json", "r") as file:
        data = json.load(file)
    
    
    print(config_imp(li,data))

