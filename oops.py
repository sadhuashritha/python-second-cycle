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


'''
Create an Abstract Class
Create an abstract class Shape with:

abstract method area()
abstract method perimeter()

Then create:

Circle
Rectangle
'''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        print("Area method")
    def perimeter(self):
        print("Perimeter method")
        
class Circle(shape):
    def area(self):
        print("Circle area")
    def perimeter(self):
        print("Circle perimeter")
    def total(self):
        print("Total")
        
class Rectangle(shape):
    def area(self):
        print("Rectangle area")
    def perimeter(self):
        print("Rectangle perimeter")
    def total(self):
        print("Total")

c = Circle()
r = Rectangle()

c.area()
c.perimeter()

r.area()
r.perimeter()


# Payment System
# Design an abstract class Payment:
# * method: pay(amount)
# Implement:
# * CreditCardPayment
# * UPIPayment
# * NetBankingPayment
'''
'''
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        print("Credit card payment",amount)
class UPIPayment(Payment):
    def pay(self,amount):
        print("UPI payment",amount)
class NetBankingPayment(Payment):
    def pay(self,amount):
        print("NetBanking payment",amount)







