# Create method overriding example.
class Parent:
    def details(self):
        print("Parent class")
class Child(Parent):
    def details(self):
        super().details()
        print("Child class")
c = Child()
c.details()
print()
# Create operator overloading example.
class operator:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a + other.a
o = operator(5)
o1 = operator(10)
print(o+o1)
print()

# Create polymorphism using inheritance.
class Parent:
    def details(self):
        print("Parent class")
class Child(Parent):
    def details(self):
        print("Child class")
c = Child()
c.details()
print()
# Create a program where different classes use same method name.
class Parent:
    def details(self):
        print("Parent class")
class Child(Parent):
    def details(self):
        print("Child class")
c = Child()
c.details()
print()
# Create shape area calculation using polymorphism.
class Area:
    def rect(self,x=1,y=1):
        return 2 * (x + y)
a = Area()
print(a.rect(2,3))
print(a.rect())

# Create animal sound program using polymorphism.
# Create polymorphism using loops.
# Create duck typing example.
# Create runtime polymorphism example.
# Create polymorphism for payment methods.