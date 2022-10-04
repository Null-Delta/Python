# 1
from curses import newwin
from operator import le
from turtle import pen


class Cat:
    name: str
    color: str
    weight: float
    
    def meow(self):
        print("Мяв")
        
cat = Cat()
cat.name = "Мурзик"
cat.color = "white"
cat.weight = 3

cat.meow()

# 2
class Animal:    
    @property
    def name(self):
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        self.hidden_name = input_name
        
    def eat(self):
        print("Намнем")
        
    def makeNoize(self):
        print(self.name + " говорит гррр")
        
    def __init__(self, animalName) -> None:
        self.name = animalName
        print("родилось животное " + self.name)
        

penguin = Animal("Люся")

print(penguin.name)
penguin.name = "Ибрагим"

penguin.eat()
penguin.makeNoize()

# 3
class StringVal:    
    @property
    def value(self):
        return self.hidden_string
    @value.setter
    def value(self, input_string):
        self.hidden_string = input_string
        

strVal = StringVal()
strVal.value = "aaa"

print(strVal.value)

# 4

class Point:
    x: float
    y: float
    def __init__(self, _x, _y) -> None:
        self.x = _x
        self.y = _y
        
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def normal(self):
        lenght = pow(self.x * self.x + self.y * self.y, 0.5)
        return Point(self.x / lenght, self.y / lenght)
    
    def print(self):
        print("Point(" + str(self.x) + ", " + str(self.y) + ")")
    
p = Point(10,5)

p.normal().print()

# 5

class Cat2(Animal):
    def makeNoize(self):
        print(self.name + " говорит мяв")
        
    def __init__(self, animalName) -> None:
        super().__init__(animalName)
        print("родился котик " + self.name)
        
coolCat = Cat2("aaa")

coolCat.makeNoize()

# 6

class Dog(Animal):
    def makeNoize(self):
        print(self.name + " говорит гав")
        
    def __init__(self, animalName) -> None:
        super().__init__(animalName)
        print("родился песик " + self.name)
        
# 7

animals = [
    Cat2("биба"),
    Cat2("боба"),
    Dog("астерикс"),
    Dog("абеликс"),
    Animal("Артем")
]

for animal in animals:
    animal.eat()
    animal.makeNoize()