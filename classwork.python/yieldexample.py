def car():
    yield "Audi"
    yield "Audisq8"
    yield "1987"

x = car()
for data in x:
    print(data)