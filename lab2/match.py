#Instead of writing many if..else statements, you can use the match statement

#Syntax
"""match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
"""

#example
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#when there are not other matches, use "_"
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

#