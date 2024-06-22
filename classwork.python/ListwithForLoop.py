fruits = ["Mango","Apple","Banana","Guava","Watermelon"]
for x in fruits:
    if x == "Banana":
        print("Banana is found")
        break
    else:
        print(x)


y = fruits.count("Orange")
print(y)