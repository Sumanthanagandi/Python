class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
            print("Bow")


class Cat(Mammal):
    def meow(self):
            print("meow")


raju = Dog()
raju.walk()
Kaju = Dog()
Kaju.bark()
Haju = Cat()
Haju.walk()
Haju.meow()