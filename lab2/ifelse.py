
#If statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

#indentation is important

#if the previous conditions were not true, then try this condition
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#if no one condition is true, else will work
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#short hand if, when we have only one statement to execute
if a > b: print("a is greater than b")

#One line if-else statement
a = 2
b = 330
print("A") if a > b else print("B")

#This technique is known as Ternary Operators, or Conditional Expressions

#combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#if you for some reason have an if statement with no content
a = 33
b = 200

if b > a:
  pass