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
# used to check if a file name is already taken.

# another way is to check if only file eixsts
if os.path.isfile(to_check):
    print("It exists")
else: 
    print("It doesnt exist")
# used to check if a file exists so that it may be opened using open()

# final method is a complicated way i found
contents = os.listdir()
def exists(contents):
    for content in contents:
        if content == to_check:
            return "It exists"
    return "It doesnt exist"
print(exists(contents))
# apparently it could have been easier with:
# for to_check in contents:
#   print("It exists")
# the thing was that hte `in` command is useful
