import re

text=input("Enter text: ")

x=re.search("^a.*b$",text)

if x:
    print("YES")
else:
    print("NO")