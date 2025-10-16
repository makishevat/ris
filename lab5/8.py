import re

text=input("Enter a st: ")

result=re.split(r"[A-Z]",text)

print("Result: ",result)