x = "My Name Is Ruchit Soni"
y = "mY nAme is RUchit sOni"

print(x.upper())
print(y.lower())

print(y.capitalize())

print(x.swapcase())
print(y.casefold())

print(x.isalpha())

print(y.isspace())

print(x.isnumeric())

z = x.replace("i","@")
print(z)

start = x.startswith("R")
print(start)

end = y.endswith("@")
print(end)

p = x.split(" ")
print(p)

s = y[0:10]
print(s)

print(x.count("My"))
print(y.count("is"))

print(type(y))
print(type(x))

print(len(x))
print(len(y))
