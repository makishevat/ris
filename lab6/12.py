file1=input("Enter the source file name: ")
file2=input("Enter the second file name: ")

with open(file1, "r") as first:
    with open(file2, "w") as second:
        for line in first:
            second.write(line)

print("Done") 