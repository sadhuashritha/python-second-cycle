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
# Create a method to update employee salary.
# Create a class method using @classmethod.
# Create a static method using @staticmethod.
# Create multiple methods in one class.
# Create a method calling another method.
# Create a method to check even or odd.
# Create a menu-driven calculator using methods.