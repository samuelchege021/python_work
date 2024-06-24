class Animal:
    def speak(self):
        print("Animal is speaking")

    def walk(self):
        print("animal is walking")


class Dog(Animal):
    def bark(self):
        print("dog is barking")

class Cat(Animal):
    def meow(self):
        print("cat is meowing")



class Cow(Animal):
    def Mooing(self):
        print("the cow is mooing")



d=Dog()
d.bark()
c=Cat()
c.meow()
d.speak()
cw=Cow()


cw.Mooing()
cw.speak()
cw.walk()





