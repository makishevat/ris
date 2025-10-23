text=input("Enter a text: ")

upper=sum(1 for char in text if char.isupper() )
lower=sum(1 for char in text if char.islower())

print ("upper: ", upper)
print("lower: ",lower)