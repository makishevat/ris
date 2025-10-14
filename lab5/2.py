import re

txt=input("Enter a string: ")

x=re.findall(r"ab{2,3}",txt)

if x:
    print("YES")
    for m in x:
        print(m)
else:
    print("No match")