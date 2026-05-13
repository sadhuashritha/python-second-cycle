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
