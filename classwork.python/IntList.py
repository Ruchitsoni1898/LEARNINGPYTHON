num = [11,22,33,44,55]
for i in num:
    if i == 11:
        print("11 is found")
        break
    else:
        print(num)

print(type(i))

# list is converted into set
x = set(num)
print(x)

x = tuple(num)
print(x)

z = num.copy()
print(z)