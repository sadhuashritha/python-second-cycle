#find the number is even or odd from the given list of numbers

def check(n):
    for i in range(len(n)):
        if n[i] % 2 == 0:
            print(n[i], "is even")
        else:
            print(n[i], "is odd")
            
n = list(map(int,input("Enter Elements: ").split( )))
check(n)


#return True if the str contains Vowels
def vowel(l):
    count = 0
    for i in n:
        if i in "aeiouAEIOU":
            print(i)
            count += 1
    print(count)
n = str(input("Enter a Word: "))
vowel(n)

#Sum of first n numbers
def numbers(n):
    sum = 0
    for i in n:
        sum += i
    return sum
n = list(map(int,input("Enter Numbers: ").split( )))
print(numbers(n))

#Check whether the given string is palindrome
def palindrome(n):
    n1 = n[::-1]
    if n == n1:
        return True
    else:
        return False
n = str(input("Enter a String: "))
print(palindrome(n))


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

# FILTER
#Keep even numbers
nums = [1,2,3,4,5,6]
n = list(filter(lambda x : x % 2 == 0, nums))
print(n)
#Keep numbers greater than 10
nums = [5,12,7,18,3]
n = list(filter(lambda x:x>10,nums))
print(n)
#Keep words with length > 4
words = ["cat","elephant","dog","tiger"]
n = list(filter(lambda x: len(x)>4,words))
print(n)
#Keep positive numbers
nums = [-3,5,-1,7,0]
n = list(filter(lambda x : x>0,nums))
print(n)
#Keep numbers divisible by 3
nums = [3,5,6,8,9,10]
n = list(filter(lambda x : x % 3 == 0,nums))
print(n)


# SORT
#Sort numbers in descending order
nums = [4,1,7,2]
n = sorted(nums, key = lambda x : x)
print(n)
#Sort words by length
words = ["apple","kiwi","banana"]
n = sorted(words, key = lambda x : len(x))
print(n)
#Sort tuples by second value
arr = [(1,5),(2,3),(4,1)]
n = sorted(arr, key = lambda x : x[1])
print(n)
#Sort numbers by absolute value
nums = [-10,5,-2,8]
n = sorted(nums, key=lambda x: abs(x))
print(n)
#Sort dictionary items by value
d = {"a":3,"b":1,"c":2}
n = sorted(d.items(),key = lambda x : x[1])
print(n)
