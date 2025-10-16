import re

text=input("Enter text: ")

x=re.findall("[A-Z][a-z]+", text)

if x:
    print(x)
else:
    print("NO")