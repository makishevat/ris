import string

for letter in string.ascii_uppercase:
    file=open(letter+ ".txt", "w")
    file.close()
