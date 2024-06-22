s1 = "This Is First String"
s2 = "tHis iS sEcond sTring"

# upper and lower case
print(s1.lower())
print(s2.upper())

# To make the first letter capital
print(s2.capitalize())

#To convert upper into lower and lower into upper

print(s1.swapcase())

# To convert all letters in lower

print(s2.casefold())

# To check all letter should be alphabets

print(s1.isalpha())

# To check all the letter should be numeric

print(s2.isnumeric())

#to check all the letter should have space

print(s1.isspace())

#replace function
s3 = s1.replace("i","@")
print(s3)

#start and end with
start = s1.startswith("T")# it starts with T so print true
print(start)

end = s2.endswith("@")
print(end)

#split string

s5 = s1.split(" ")
print(s5)

#print substring
s6 = s1[0:10]
print(s6)

print(s1.count("This"))
print(s2.count("is"))

print(type(s1))
print(len(s1))