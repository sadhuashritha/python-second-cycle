'''
# Write a function using positional arguments to add two numbers.
def add(n,m):
    return n + m
print(add(5,5))
print()

# Write a function using default arguments to calculate simple interest.
def si(p = 1000, r = 1, t = 1):
    s = (p * r * t)/100
    print("Simple Interest:",s)
si(2000,5,2)
si()
print()

# Write a function using keyword arguments to display student details.
def student(name,section):
    print(name,"is in",section,"class")
student(name ="ashritha", section = 9)
student(name ="blah", section = "blahhhhh")
print()

# Write a function that accepts mixed arguments (positional + keyword).
def student(name,age,section):
    print(name,"is in",section,"class and",name,"is", age,"years old")
student("ashritha",age = 15,section = "10th")
student("radha",14,section = "9th")
print()

# Write a function with default argument and override it.
def add(n=1,m=1):
    return n + m
print(add(5,5))
print()

# Write a function to demonstrate incorrect argument order (and fix it).

# Write a function that prints arguments in different formats.
# Write a function where missing argument raises error.
# Write a function that swaps two numbers using arguments.
# Write a function that takes list as argument and modifies it.
'''
# Write a function using positional arguments to multiply two numbers.
def mul(a,b,/):
    return a * b
print(mul(2,4))

# Create a function using keyword arguments to display student details
def details(*,name,age,cls,section):
    print("name:",name, "age:",age,"cls:",cls,"section:",section)
details(name = "ashritha",age = 80,cls = "B-Tech",section = "Beta") 

# Write a function with a default argument for country name.
def country(name = "India"):
    print(name)
country("Sweden")
country("UK")
country()
country("Australia")
country("Japan")
country()

# Create a function that takes three arguments and prints their average.
def avg(a,b,c):
    return (a+b+c) / 3
print(avg(1,2,3))