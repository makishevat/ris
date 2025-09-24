#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Create and print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Print the "brand" value of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicate values will overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Print the number of items in the dictionary
print(len(thisdict))

#The values in dictionary items can be of any data type
#type: <class 'dict'>

#Using the dict() method to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Get the value of the "model" key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Get the value of the "model" key
x = thisdict.get("model")

#Get a list of the keys
x = thisdict.keys()

#Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change dict_keys(['brand', 'model', 'year', 'color'])

#Get a list of the values
x = thisdict.values()

#change values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["year"] = 2020

print(x) 

#add a new item yo te dict
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["color"] = "red"

print(x) 

#Get a list of the key:value pairs
x = thisdict.items()

#Check if "model" is present in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change the "year" to 2018
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#update the "year" of the car by using the update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#adding an item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#The pop() method removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely: 
del thisdict

#The clear() method empties the dictionary
thisdict.clear()

#Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

#you can also use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

#Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)

#Make a copy of a dictionary with the copy() method
mydict = thisdict.copy()

#you cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2

#Make a copy of a dictionary with the dict() function
mydict = dict(thisdict)

#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Print the name of child 2
print(myfamily["child2"]["name"])

#Loop through the keys and values of all nested dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#dict methods
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""