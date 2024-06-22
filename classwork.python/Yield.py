def student():
    yield "ruchit"
    yield 9601153777
    yield "ruchitsoni1898@gmail.com"

x = student()
for data in x:
    print(data)