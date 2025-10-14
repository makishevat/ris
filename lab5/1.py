import re

txt=input("Enter a string: ")

x=re.search("^ab*$",txt)

if x:
    print("YES")
else:
    print("No match")
    