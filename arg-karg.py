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

