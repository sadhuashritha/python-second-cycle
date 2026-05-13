# Write a function using *args to find the sum of numbers.
def add(*n):
    sum = 0
    for i in n:
        sum += i
    print(sum)
add(1,2,3)
add(1,2,3,4,5,6,7,8,9,0)
add(3,2,5,7)
print()
# Create a function using *args to find the largest number.
def add(*n):
    print(max(n))
add(1,2,3)
add(1,2,3,4,5,6,7,8,9,0)
add(3,2,5,7)
print() 

# Write a function using **kwargs to print student details.
def student(**n):
    print(type(n["name"]))
    print(n["age"])
    print(n)
student(name = "ashritha",age = 20,section = "Beta")
print()

# Create a function using **kwargs to display employee information.
def student(**n):
    print(type(n["name"]))
    print(n["age"])
    print(n)
student(name = "ashritha",age = 20,department = "HR")
print()

# Write a function using *args to calculate average.
def avg(*n):
    ans = sum(n) / len(n)
    print(ans)
avg(2,3,1,4,5)
avg(1,2,3)
avg(0,6,7,8)
print()

# Create a function using *args to multiply all numbers.
def mul(*n):
    ans = 1
    for i in n:
        ans *= i
    print(ans)
mul(1,2,3,4)
mul(1,2)
mul(0,3,2,21)
print()

# Write a function using **kwargs to print key-value pairs.
def student(**n):
    print(n)
student(name = "ashritha",age = 20,section = "Beta")
print()

# Create a function using both *args and **kwargs.
def details(n,*args,**kwargs):
    print("Details of the student:",n)
    print("arguments:",args)
    print("keyword arguments:",kwargs)
details("details", "ashritha","Beta",age = 21,score = 80)
print()

# Write a function that counts total arguments passed using *args.
def num(*args):
    count = 0
    for i in args:
        count +=1
    print(count)
num(2,1,3,5,6,7)
num(1,2,3,4,6)
num(1,2,3)
print()

# Create a function to display product details using **kwargs.
def display(**kwargs):
    print(kwargs)
display(name = "ashritha",age = 21, section = "Beta")
print()