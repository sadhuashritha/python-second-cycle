#Map
#Double all numbers
nums = [1,2,3,4,5]
n = list(map(lambda x : x*x, nums))
print(n)

#Convert strings to integers
nums = ["10","20","30","40"]
n = list(map(lambda x: int(x), nums))
print(n)

#Square each number
nums = [2,3,4,5]
n = list(map(lambda x : x**2, nums))
print(n)
#Get length of each word
words = ["apple","cat","banana"]
n = list(map(lambda x: len(x),words))
print(n)
#Add 5 to every number
nums = [1,5,10]
n = list(map(lambda x : x + 5,nums))
print(n)

#find the number is even or odd from the given list of numbers

def check(n):
    for i in range(len(n)):
        if n[i] % 2 == 0:
            print(n[i], "is even")
        else:
            print(n[i], "is odd")
            
n = list(map(int,input("Enter Elements: ").split( )))
check(n)

#Sum of first n numbers
def numbers(n):
    sum = 0
    for i in n:
        sum += i
    return sum
n = list(map(int,input("Enter Numbers: ").split( )))
print(numbers(n))

