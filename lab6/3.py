text=input("Enter a staing: ")

text=text.replace(" ","").lower()

if text=="".join(reversed(text)):
    print ("yes")
else:
    print("no")
