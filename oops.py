class Employee:
    def empmethod(self):
        print("Employee parent class and method")

class Developer(Employee):
    def devmethod(self):
        print("Developer child class and method")
        
ed = Developer()
ed.empmethod()
ed.devmethod()


# 1. Single Inheritance (Basic)

# Create a class Animal with a method eat().
# Create a class Dog that inherits from Animal and calls eat().

class Animal:
    def eat(self):
        print("Animal (parent)class")
class Dog(Animal):
    print("Animal")
d = Dog()
d.eat()
