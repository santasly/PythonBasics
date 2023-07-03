class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color


    def speak(self):
        raise NotImplementedError("Child classes must implent this method")
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"


dog=Dog("Bosco","Black")
print(dog.name)
print(dog.speak())
print(dog.color)
cat=Cat("Minnie","White")
print(cat.name)
print(cat.color)
print(cat.speak())
cow=Cow("Momo","Brown")
print(cow.name)
print(cow.speak())
print(cow.color)