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

# Create a method returning square of a number.
# Create a method to update employee salary.
# Create a class method using @classmethod.
# Create a static method using @staticmethod.
# Create multiple methods in one class.
# Create a method calling another method.
# Create a method to check even or odd.
# Create a menu-driven calculator using methods.