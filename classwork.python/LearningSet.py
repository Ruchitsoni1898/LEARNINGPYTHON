fruits = {"Orange","Apple","Banana","Watermelon"}
fruits.remove("Orange")
print(fruits)
print(type(fruits))
print(len(fruits))

fruits.add("Mango")
print(fruits)

# Set converted into list
y = list(fruits)
print(y)

# In list we use append method
y.append("Guava")
print(y)

#list is converted into Tuple.
z = tuple(y)
print(z)



