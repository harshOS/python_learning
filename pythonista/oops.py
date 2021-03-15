class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walks(self):
        print("{} is walking".format(self.name))
    
    def noise(self):
        print("{} is making noise".format(self.name))

sher = Animal('Sher', 15)
print(sher.walks())

#inheritance 

class Dog(Animal):
    
    def barks(self):
        print('{} is barking'.format(self.name))

john = Dog('john', 6)

print(john.barks())

#encapsulation

class CellPhone():
    def __init__(self,name):
        self.name = name
        self.__price = 5000
    
    def sell(self):
        print("{} is selling at {}".format(self.name,self.__price))
    
    def setPrice(self,price):
        self.__price = price
    
Nokia = CellPhone('Nokia2020')
print(Nokia.sell())
Nokia.__price = 4500
print(Nokia.sell())

Nokia.setPrice(4500)
print(Nokia.sell())

# Polymorphism

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
