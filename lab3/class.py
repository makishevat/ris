class Myclass:
    def __init__(self):
        self.text=""
    def getString(self):
        self.text=input("Enter a string:")
    def printString(self):
        print(self.text.upper())

"""a=Myclass()
a.getString()
a.printString()"""

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):

    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
    
"""shape=Shape()
print(shape.area())

square=Square(5)
print(square.area())"""

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

"""rect=Rectangle(5,4)
print(rect.area())"""

class Point():

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"Coordinates:({self.x},{self.y})")
    
    def move(self,nx,ny):
        self.x=nx
        self.y=ny
    
    def dist(self,x1,y1):
        return ((self.x-x1)**2+(self.y-y1)**2)**(0.5)

"""point=Point(2,3)
point.show()
point.move(4,5)
point.show()
print(point.dist(5,7))
"""

class Bank():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print(f"Owner: {owner},Balance: {balance}")

    def deposit(self,amount):
        self.balance+=amount
        print (f"Deposited: {amount},New balance: {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrew: {amount}, New balance: {self.balance}")
        else:
            print("Withdrawals may not exceed the available balance!")

"""bank=Bank("Tomiris",250)

bank.deposit(5000)
bank.withdraw(1000)"""

nums = [1, 2, 3, 5, 4, 6, 8, 9, 17, 10, 11]

primes = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, n)), nums))

print(primes)
        

