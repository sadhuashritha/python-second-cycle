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
