import os

path=input("Enter a path: ")

if os.path.exists(path):
    print("The path exists")

    dirname=os.path.dirname(path)

    filename=os.path.basename(path)

    print("Direcotry:",dirname)
    print("File name:",filename)
else:
    print("The path does not exist")

