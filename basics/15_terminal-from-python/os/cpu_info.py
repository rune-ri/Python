import os 

os_type = os.name
os_cpu_count = os.cpu_count()

print(f"The os interface interaction for this device is of type: {os_type}")
print(f"The number of CPU chips in this device are: {os_cpu_count}")
