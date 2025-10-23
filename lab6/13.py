import os

path=input("Enter the path: ")

if os.path.exists(path):
    if os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
        print("Done")
    else:
        print("No access")      
else:
    print("Path does not exist") 