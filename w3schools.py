
#data types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

#numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#python castig
y = int(2.8) # y will be 2
x = float(1)     # x will be 1.0
z = str(3.0)  # z will be '3.0'

#strings
print("Hello")
print('Hello')

#quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#multiline string by using 3 quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)  # or 3 single qoutes

#getting characters from 2 to 5(not included)
b = "Hello, World!"
print(b[2:5])

#slice from the start
b = "Hello, World!"
print(b[:5])

#slice to the end
b = "Hello, World!"
print(b[2:])

#negative indexing
b = "Hello, World!"
print(b[2:])

#string in upper case
a = "Hello, World!"
print(a.upper())

#string in lower case
a = "Hello, World!"
print(a.lower())

#remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#merge variable a with variable b into variable c
a = "Hello"
b = "World"
c = a + b
print(c)

#f-string, formating string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#escape character
txt = "We are the so-called \"Vikings\" from the north."

#\'	Single Quote	
#\\	Backslash	
#\n	New Line	
#\r	Carriage Return	
#\t	Tab	
#\b	Backspace	
#\f	Form Feed	
#\ooo	Octal value	
#\xhh	Hex value

#STRING METHODS
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#count()	Returns the number of times a specified value occurs in a string
#find()	Searches the string for a specified value and returns the position of where it was found
#index()	Searches the string for a specified value and returns the position of where it was found
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdigit()	Returns True if all characters in the string are digits
#lower()	Converts a string into lower case
#split()	Splits the string at the specified separator, and returns a list
#upper()	Converts a string into upper case
