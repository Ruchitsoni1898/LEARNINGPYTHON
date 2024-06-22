Cars = ["Mercedez","Audi","BMW","ferrari","Kia"]
print(Cars)
print(type(Cars))
print(len(Cars))
Cars.append("Tata")
print(Cars)


Cars.insert(1,"Ford")
print(Cars)

Cars.remove("Audi")
print(Cars)
print(Cars[0])
print(Cars[-1])
print(Cars[0:3])
print(Cars[:2])
print(Cars[4:])

Cars.sort()
print(Cars)
Cars.sort(reverse=True)
print(Cars)
Cars.sort(key=str.lower)
print(Cars)
Cars.reverse()
print(Cars)





