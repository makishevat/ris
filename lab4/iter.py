class Square:
    def __init__(self,num):
        self.num=num
        self.current=1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<= self.num:
            result=self.current**2
            self.current+=1
            return result
        else:
            raise StopIteration

"""num=int(input("Enter a num:"))     
square=Square(num)
myiter=iter(square)

for x in myiter:
    print(x)
"""

class Even:
    def __init__(self,n):
        self.n=n
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.n:
            if self.current%2==0:
                x=self.current
                self.current+=1
                return x
            self.current+=1
        raise StopIteration
"""n=int(input("NUM:"))
even=Even(n)
myiter=iter(even)

print(",".join(str(x) for x in myiter))
"""
class Myclass:
    def __init__(self,n):
        self.n=n
        self.current=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.n:
            if self.current%3==0 and self.current%4==0:
                x=self.current
                self.current+=1
                return x
            self.current += 1
        raise StopIteration
    
"""n=int(input("NUM:"))
myclass=Myclass(n)
myiter=iter(myclass)

for a in myiter:
    print(a)"""

class Squares:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.current=a
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <=self.b:
            result=self.current**2
            self.current+=1
            return result
        else:
            raise StopIteration

"""a=int(input("start:"))
b=int(input("end:"))
squares=Squares(a,b)

for num in squares:
    print(num)"""

class Nums:
    def __init__(self,n):
        self.n=n
        self.current=n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >=0:
            result=self.current
            self.current-=1
            return result
        else:
            raise StopIteration

"""n=int(input("enter:"))
nums=Nums(n)

for x in nums:
    print(x)"""


