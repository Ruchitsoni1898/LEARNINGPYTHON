car = {
  "name": "TATA",
   "model": "punch",
}

print(car)
for x in car.keys():
    print(x)

for y in car.values():
    print(y)

z = car.get("name")
print(z)

car["Established_Year"]="1868"
print(car)

car.update({"name":"Audi"})
print(car)

car.update({"model":"E-tron"})
print(car)


