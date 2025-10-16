import re

text=input("Enter text: ")

x=re.findall(r"[a-z]+_[a-z]+", text)

if x:
    print(x)
else:
    print("NO")
    