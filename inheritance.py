# Create single inheritance using Animal and Dog.
class Parent:
    def p(self):
        print("Parent class")
class Child(Parent):
    def c(self):
        print("Child class")
a = Child()
a.p()
a.c()
print()

# Create multilevel inheritance example.
class Grandparent:
    def gp(self):
        print("Grandparent")
class Parent(Grandparent):
    def p(self):
        print("Parent")
class Child(Parent):
    def c(self):
        print("Child")
a = Child()
a.gp()
a.p()
a.c()
print()

# Create hierarchical inheritance example.
class Parent:
    def p(self):
        print("Parent class")
class Child1(Parent):
    def c1(self):
        print("Child 1")
class Child2(Parent):
    def c2(self):
        print("Child 2")
a = Child1()
a.p()
a.c1()
print()
b =Child2()
b.p()
b.c2()
print()

# Create multiple inheritance example.
class Parent1:
    def p1(self):
        print("Parent1")
class Parent2:
    def p2(self):
        print("Parent2")
class Child(Parent1,Parent2):
    def c1(self):
        print("Child")
c = Child()
c.p1()
c.p2()
c.c1()
print()
# Demonstrate method overriding.
class Parent():
    def details(self):
        print("Parent class")
class Child(Parent):
    def details(self):
        print("Child class")
c = Child()
c.details()
print()

# Use super() in inheritance.
class Parent():
    def details(self):
        print("Parent class")
class Child(Parent):
    def details(self):
        super().details()
        print("Child class")
c = Child()
c.details()
print()
# Create employee-manager inheritance program.
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
class Manager(Employee):
    def details(self):
        print("Manager can view Employee details")

m = Manager("Ashritha",21,2000000)
m.display()
m.details()
print()

# Create inheritance with constructor calling.
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
class Manager(Employee):
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
        print("Manager can view Employee details")

m = Manager("Ashritha",21,2000000)
m.display()
print()
