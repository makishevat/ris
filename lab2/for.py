#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Loop through the letters in the word "banana"
for x in "banana":
  print(x)

#Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #output:apple banana
  
#break before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) # ouput:apple

#Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#to loop through a set of code a specified number of times, we can use the range() function
for x in range(2, 6):
  print(x) # from 2 to 6 without 6

#Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x) #output 2 5 8 11 14...

#Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#the else block will NOT be executed if the loop is stopped by a break statement

#Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#if you for some reason have a for loop with no content, use pass
for x in [0, 1, 2]:
  pass

