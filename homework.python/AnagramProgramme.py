str1 = "Party"
str2 = "Sports"

str1 = list(str1.upper())
str2 = list(str2.upper())

str1.sort(),str2.sort()

if(str1==str2):
    print("True")
else:
    print("False")
