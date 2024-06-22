fruits = {"Mango","Orange","Watermelon","Apple"}
for x in fruits:
    if x == "Orange":
        print("Orange is Found")
        break
    else:
        print(x)

#fruits.discard("Mango")
#print(fruits)




vegetables = {"Onion","Potato","Cabbage","Mango"}
mix = fruits.difference(vegetables)
print(mix)

z = fruits.copy()
print(z)