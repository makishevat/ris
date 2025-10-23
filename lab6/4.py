import math
from time import sleep

num=int(input("Eneter a number: "))
msec=int(input("Enter ms: "))

sleep(msec/1000)
result=math.sqrt(num)

print(f"Square root of {num} after {msec} miliseconds is {result}")