import os 

# i will put all os realted info in here.

a = os.name
b = os.cpu_count()

# only works in mac/linux
c = os.uname()

# Returns the system memory page size in bytes (usually 4096)
page_size = os.sysconf("SC_PAGESIZE")

# Returns the maximum number of files a single process can open simultaneously
max_files = os.sysconf("SC_OPEN_MAX")

print(a)
print(b)
print(c)
print(page_size)
print(max_files)

# i found out new things using this. apparently the page size for cpu memory management and transfer
#   for me is 16384 ie 16 kb. this from what i gather online indicates that it is m1 or above for mac.
# and max file ie sc open max is 2560 which means that i can opne that many number of files on a single process
#   at once. if 2561 then it would throw an error. mac limits this for safety. safety of process or 
#   safety of memory lead or something is unknown. but the quantity is humongous so most likely 
#   we can conclude that if someone wants to open more, they do process synchronization between 2 processes 
#   and then does transfer of infmraotn between them to properly make things work.
#   this was just a hypothesis, i dont even know if that is possible.
