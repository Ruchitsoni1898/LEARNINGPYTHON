fruits = ("Mango","Pomegranate","Apple","Banana","Orange")
print(len(fruits))
print(type(fruits))
print(fruits[1:4])
print(fruits[1:])
print(fruits[-1])
print(fruits[:3])
x = fruits.count("Banana")
print(x)


# Tuple converted into list
z = list(fruits)
print(z)

# In list we use append method
z.append("onion")
print(z)

# list is converted into tuple
y = tuple(z)
print(y)
