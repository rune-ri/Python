import os
# for environment variables, 
# it basically can be used to get device information and data that is applicable to current state of device.
# you cannot get network id or ip or such.
# but you can get os name, computer name, host name, processor architecture.

computerName = os.environ.get("HOSTNAME") or os.environ.get("COMPUTERNAME")
currentUser = os.environ.get("USER") or os.environ.get("USERNAME")
operatingSystem = os.environ.get("PROCESSOR_ARCHITECTURE")

print(computerName)
print(currentUser)
print(operatingSystem)

# doesnt work on mac, only on windows. some of these work some dont. it is because of diffrent operating system 
#   methodoloty of working and since `import os` works directly with os, many a times some parameters do not 
#   work.

