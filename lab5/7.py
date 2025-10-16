import re

text=input("Enter string: ")

result=re.sub("_","",text)
print(result)