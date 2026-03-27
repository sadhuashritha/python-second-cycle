#1. Sum of numbers using *args
def summation(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
#print(summation(1,2,3,4,5))
s = list(map(int,input().split()))
print(summation(*s))

# 2. Find maximum using *args
def func(*args):
    s = max(args)
    print(s)

s = list(map(int,input().split()))
func(*s)
 
#3. Count arguments
def count(*args):
    count = 0
    for i in args:
        count += 1
    return count
s = list(map(int,input().split()))
print(count(*s))

#4. Print all arguments
def count(*args):
    count = 0
    for i in args:
        print(i)
s = list(map(int,input().split()))
count(*s)

#5. Multiply numbers
def count(*args):
    mul = 1
    for i in args:
        mul *= i
    print(mul)
s = list(map(int,input().split()))
count(*s)


