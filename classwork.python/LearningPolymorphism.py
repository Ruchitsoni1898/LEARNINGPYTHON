# polymorphism - one type has a many forms.
# e.g - Type and Length

class Animal():
    def make_sound(self):
        print("The animal makes sound")
class Dog(Animal):
    def make_sound(self):
        print("The dog barks...")

class cat(Animal):
    def make_sound(self):
        print("The cat meows")

def animal_sounds(animal):
    animal.make_sound()

a = animal()
a= Dog()
