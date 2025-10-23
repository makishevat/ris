items=input("Enter list: ").split()

with open("10.txt", "w") as file:
    for item in items:
        file.write(item + " ")

print("Done")