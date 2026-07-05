#  leap year
n = 2024
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print("True")
else:
    print("False")

# max,min in arr
arr = [10,25,5,4,10,4,7,90,100, 15]
maximum = arr[0]
minimum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Max:", maximum)
print("Mini:", minimum)

# Fibnocci
n = 10
arr = []
a, b = 0, 1
for i in range(n):
    arr.append(a)
    a, b = b, a + b
print("Fibonacci Series:", arr)

# prime number
n = 17
if n <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")