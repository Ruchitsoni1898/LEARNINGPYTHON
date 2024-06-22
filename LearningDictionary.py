student = {
  "name": "Ruchit",
   "age": "25",
   "Email": "ruchitsoni1898@gmail.com",
}
print(student)
for x in student.keys():
    print(x)


for y in student.values():
    print(y)

z = student.get("name")
print(z)

student["mobile_number"]= "+491793963161"
print(student)

student.update({"name":"Mahesh"})
print(student)