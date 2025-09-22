#compare 2 values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#print true or falce based on condition
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#evaluate value
print(bool("Hello"))
print(bool(15))

#OPERATORS
#Python Arithmetic Operators
"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
#Python Assignment Operators
"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
                    print(x)
"""
#Python Comparison Operators
"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""

#Python Logical Operators
"""
and 	Returns True if both statements are true	                 x < 5 and  x < 10	
or	    Returns True if one of the statements is true	             x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	     not(x < 5 and x < 10)
"""

#Python Identity Operators
"""
is 	    Returns True if both variables are the same object	    x is y	
is not	Returns True if both variables are not the same object	x is not y
"""
#Python Membership Operators

"""
in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
"""

#Python Bitwise Operators
"""
& 	AND	Sets each bit to 1 if both bits are 1	                                                                                x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	                                                                            x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	                                                                        x ^ y	
~	NOT	Inverts all the bits	                                                                                                ~x	
<<	Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off	                    x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""

#PRECEDENCE

"""
1.()	Parentheses	
2.**	Exponentiation	
3.+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
4.*  /  //  %	Multiplication, division, floor division, and modulus	
5.+  -	Addition and subtraction	
6.<<  >>	Bitwise left and right shifts	
7.&	Bitwise AND	
8.^	Bitwise XOR	
9.|	Bitwise OR	
10.==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
11.not	Logical NOT	
12.and	AND	
13.or	OR
"""

