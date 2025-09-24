#Tuples are used to store multiple items in a single variable
#A tuple is a collection which is ordered and unchangeable,and  are written with round brackets

#Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""Tuple items are ordered and we can't change the order, unchangeable ,
we cannot change, add or remove items after the tuple has been created, and allow duplicate values."""

#Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

#any data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values
tuple1 = ("abc", 34, True, 40, "male")

#data type of tuple: <class 'tuple'>

#Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

#Print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#from the start
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#to the end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])\

#range of the negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#check if the target present in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#we can convert the tuple into a list, change the list, and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#add an item by converting to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

#add an item by adding tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#also we can delete an element by creating a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

#delite the tuple
thistuple = ("apple", "banana", "cherry")
del thistuple

#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruits = ("apple", "banana", "cherry")

print(fruits)

#unpaking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Assign the rest of the values as a list called "red",because number of values in tuplle more than number of variables
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#iterate through the items 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#loop by referring to their index number
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Print all items, using a while loop to go through all the index numbers
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join 2 tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiply tuple by 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#