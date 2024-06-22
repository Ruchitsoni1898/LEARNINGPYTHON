sports = ["Bat","Ball","Football","Hockey","Baseball"]
for x in sports:
    if x == "Hockey":
        print("Hockey is found")
        break
    else:
        print(x)

# list is converted into tuple
x = tuple(sports)
print(x)
# append method to add new value
sports.append("Badminton")
print(sports)

#list is converted into set
z = set(sports)
print(z)
