#Sets are used to store multiple items in a single variable.

#A set is a collection which is unordered,unindexed , unchangeable, but you can remove items and add new items.

#create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: the set list is unordered, meaning: the items will appear in a random order.

#Set items are unordered, unchangeable, and do not allow duplicate values.
#duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#true and 1 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#also False and 0 is considered the same value

#get the number of items
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set items can be of any data type
#A set can contain different data types
#type -<class 'set'>
#the set constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)

#You cannot access items in a set by referring to an index or a key

#but we can loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Once a set is created, you cannot change its items, but you can add new items

#Add an item to a set, using the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add elements from tropical into thisset (from another to current set)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#we can add  any iterable object
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Remove "banana" by using the remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remove a random item by using the pop() method, it removes random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Loop through the set, and print the values
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join set1 and set2 into a new set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Use | to join two sets, instead of union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Join multiple sets with the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#join a set with a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#The  | operator only allows you to join sets with sets

"""
The update() method inserts all items from one set into another
The update() changes the original set, and does not return a new set"""

#The update() method inserts the items in set2 into set1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items

#join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Use & to join two sets instead of intersection

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#Keep all items from set1 that are not in set2, difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

#we can use the - operator instead of the difference() method, and you will get the same result.

#Use the difference_update() method to keep the items that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#Keep the items that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result

#The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

"""
frozenset is an immutable version of a set.
Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset."""

#Create a frozenset and check its type:
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#frozenset methods
"""
copy()	 	Returns a shallow copy	
difference()	-	Returns a new frozenset with the difference	
intersection()	&	Returns a new frozenset with the intersection	
isdisjoint()	 	Returns whether two frozensets have an intersection	
issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union
"""

"""SET METHODS
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
"""
