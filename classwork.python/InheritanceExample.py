# Single Inheritance

"""class Animal:
    def sound(self):
        print("This is the sound of an animal")
class dog(Animal):
    def sound(self):
        print("wof!wof")

Dog = dog()
Dog.sound()
"""

class Bird:
    def fly(self):
        print("The bird is flying")
class Mammal:
    def run(self):
        print("The mammal is running")
class bat(Bird,Mammal):
    pass

b = bat()
b.fly()
b.run()

