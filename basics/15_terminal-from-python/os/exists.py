# basically tryint to code if a file or directory exists 
# 1. there is a function already implemented in os for this.
# 2. i can just ask for contents and then check if in that list some file or dir is there.

import os

# apparently from research, there are 3 ways to do this.

to_check = "cwd.py"

# for file or directory.
if os.path.exists(to_check):
    print("It exists")
else:
    print("It doesnt exist")

# another way is to check if only file eixsts
if os.path.isfile(to_check):
    print("It exists")
else: 
    print("It doesnt exist")

# final method is a complicated way i found
contents = os.listdir()
def exists(contents):
    for content in contents:
        if content == to_check:
            return "It exists"
    return "It doesnt exist"
print(exists(contents))
