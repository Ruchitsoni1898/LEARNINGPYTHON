fruits = ["Apple","Kiwi","watermelon","Banana","Guava"]
print(fruits)
print(type(fruits))
print(len(fruits))
fruits.append("Mango")
print(fruits)

fruits.insert(1,"Grapes")
print(fruits)

fruits.remove("Guava")
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[0:5])
print(fruits[2:])
print(fruits[:3])


fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.sort(key=str.lower)
print(fruits)
fruits.reverse()
print(fruits)