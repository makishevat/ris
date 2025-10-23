file=input("Enter the file name:")

with open(file,'r') as f:
    lines=f.readlines()
    print("Number of lines: ", len(lines))