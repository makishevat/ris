#1
"""def ounces(x):
    return x*28.3495231
print(ounces(5))"""

#2
"""def temp(x):
    return (5/9)*(x-32)
print(temp(270))"""

#3
"""def  solve(numheads, numlegs):
    rabbits=(numlegs-2*numheads)//2
    chikens=numheads-rabbits
    return chikens, rabbits

print(solve(35,94))"""

#4
"""def filter_prime(nums):
    result=[]
    for num in nums:
        if num<2:
            continue
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            result.append(num)
    return result
print(filter_prime([1,2,3,5,4,6,8,9,17,10,11]))"""

#5
"""def permute(s,answer=""):
    if len(s)==0:
        print(answer)
        return
    for i in range(len(s)):
        ch=s[i]
        left=s[:i]+s[i+1:]
        permute(left,answer+ch)


s = input("Enter a string: ")
permute(s)"""

#6
"""def reverse(str,answer=""):
    words=str.split()
    rwords=words[::-1]
    answer=" ".join(rwords)
    return answer

s=input("Input a string: ")
print(reverse(s))"""

#7
"""def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

print(has_33([1, 3, 3]))      
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))
"""

#8
"""def spy_game(nums):
    code=[0,0,7]
    for i in nums:
        if i==code[0]:
            code.pop(0)
        if len(code)==0:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))   
print(spy_game([1,7,2,0,4,5,0])) """ 

#9
"""pi=3.14159265359
def volume(r):
    return(4/3)*pi*(r**3)

radius=float(input("Enter radius: "))
print(volume(radius))"""

#10
"""def unique():
    elements=input("Input a list: ")
    elements=elements.split()
    result=[]
    for i in elements:
        if i not in result:
            result.append(i)
    return result

print(unique())"""

#11
"""def palindrome(str):
    return str==str[::-1]

print(palindrome("madam"))"""

#12
"""def histogram(list1):
    for num in list1:
        print("*" *num)

histogram([4,9,7])"""

#13
