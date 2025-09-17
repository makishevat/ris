#creating variables
x = 5
y = "John"
print(x)
print(y)

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#get the type
x = 5
y = "John"
print(type(x))
print(type(y))

#illegal variable nemes
2myvar = "John"
my-var = "John"
my var = "John"

#camel case
myVariableName = "John"

#pascal case
MyVariableName = "John"

#snake case
my_variable_name = "John"

#assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#unpaking a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you use the global keyword, the variable belongs to the global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)