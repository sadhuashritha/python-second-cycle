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
