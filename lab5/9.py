import re

text=input("Enter a string: ")

x=re.sub(r"([A-Z])", r" \1", text)

print("Result: ",x)