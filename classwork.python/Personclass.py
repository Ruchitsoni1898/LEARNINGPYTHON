class person:
     def __init__(self,name,gender,profession):
          self.name = name
          self.gender = gender
          self.profession = profession
     def show(self):
          print("Name:",self.name,"gender:",self.gender,"profession:",self.profession)

     def work(self):
          print(self.name,"working as a",self.profession)

Data = person("Ruchit","Male","Software Engineer")

Data.show()
Data.work()


