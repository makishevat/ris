import os

path =input("Enter path: ")

items=os.listdir(path)

directories=[d for d in items if os.path.isdir(path+"/"+d)]
files=[f for f in items if os.path.isfile(path+"/"+f)]

print("Directories: ")
for d in directories:
    print("-",d)

print("Files: ")
for f in files:
    print("-",f)

print("Directories and files: ")
for i in items:
    print("-",i)