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
def vowel(n):
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
