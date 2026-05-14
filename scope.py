# Write a program showing use of local variables.
def local():
    n = 10
    print(n)
local()

# Create a program showing use of global variables.
n = 10
def glo():
    print(n)
glo()
print(n)


# Write a function to modify a global variable using global keyword.
x = 300
print("Before using global keyword:",x)
def glo():
    global x
    x = 200
    print("After using global keyword:",x)
glo()
print()

# Create nested functions to demonstrate local scope.
def nested():
    n = 10
    print(n)
    def nested1():
        print(n)
    nested1()  
nested()
print()

# Write a program to show variable shadowing.
x = 90
def var():
    x = 80
    print("Variable Shadowing: ",x)
var()
print("Global Variable: ",x)
print()

# Create a program to access global variable inside a function.
x = 10
def glo():
    print("Printing global variable inside a fun:",x)
glo()
print()

# Write a function where local and global variables have same name.
x = 90
def fun():
    x = 10
    print("Local variable:",x)
fun()
print("Global variable: ",x)

# Create a nested function using nonlocal keyword.
n = 10
def var1():
    n = 20
    def var2():
        nonlocal n
        n = 90
    var2()
    return n
print(var1())