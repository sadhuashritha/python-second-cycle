# 1. Create a method to display student information.
class Student:
    def __init__(self,name,age,section):
        self.name = name
        self.age = age 
        self.section = section
stu = Student("Ashritha",20,10)
print(stu.name)
print(stu.age)
print(stu.section)
print()

# 2. Create a method to calculate addition.
class addition:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def res(self):
        return self.a + self.b
add = addition(1,2)
print(add.res())
print()

class addition:
    def __init__(self,value):
        self.value = value
    def __add__(a,b):
        return a.value + b.value
x = addition(3)
y = addition(3)
print(x + y)
print()

# Create a method returning square of a number.
class Square:
    def __init__(self,a):
        self.a = a
    def res(self):
        print(self.a * self.a)
s = Square(8)
s.res()
print()

class Square:
    def __init__(self,value):
        self.value = value
    def __pow__(a,b):
        return a.value ** b.value
x = Square(4)
y = Square(2)
print(x ** y)
print()
# Create a method to update employee salary.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def upd_salary(self,new_salary):
        self.salary = new_salary
        print(self.salary)
e = Employee("ashritha",900000)
e.upd_salary(1000000)
print()

# Create a class method using @classmethod.
class Student:
    x = 10
    @classmethod
    def details(cls):
        print(cls.x)
s = Student()
s.details()
print()

# Create a static method using @staticmethod.
class Static:
    @staticmethod
    def Add(a,b):
        return a+b
print(Static.Add(10,20))
print()

# Create multiple methods in one class.
class Employee:
    def __init__(self,name,age,dept):
        self.name = name 
        self.age = age
        self.dept = dept
    def details (self):
        print(self.name,self.age,self.dept)
    def upd_details(self,x):
        self.dept = x
        print(self.name,self.age,self.dept)
e = Employee("ashritha",20,"HR")
e.details()
e.upd_details("Manager")
print()

# Create a method calling another method.
class Student:
    def greet(self):
        return "Hello"
    def details(self,name):
        print(self.greet() , name)
s = Student()
s.details("Ashritha")
print()
# Create a method to check even or odd.
class Check:
    def res(self,a):
        return a%2 == 0
c = Check()
print(c.res(3))
print()
# Create a menu-driven calculator using methods.