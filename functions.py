#return True if the str contains Vowels
def vowel(n):
    count = 0
    for i in n:
        if i in "aeiouAEIOU":
            print(i)
            count += 1
    print(count)
# n = str(input("Enter a Word: "))
vowel("ashritha")
print()

#Sum of first n numbers
def numbers(*n):
    sum = 0
    for i in n:
        sum += i
    return sum
print(numbers(1,2,3,4,5))
print()

#Check whether the given string is palindrome
def palindrome(n):
    n1 = n[::-1]
    if n == n1:
        return True
    else:
        return False
# n = str(input("Enter a String: "))
print(palindrome("ashritha"))
print()

# Write a function to return the square of a number
def square(n):
    print(n**2)
# n = int(input("Enter a number: "))
square(8)
print()

# Write a function to check if a number is even or odd.
def eo(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("False")
eo(9)
print()

# Write a function to find the factorial of a number.
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)
print(facto(3))
print()

# Write a function that returns the maximum of three numbers.
def maxi(*n):
    great = 0
    for i in n:
        if i >= great:
            great = i
    return great
print(maxi(5,6,980))
print()

# Write a function to count vowels in a string.
def vowel(n):
    count = 0
    for i in n:
        if i in "aeiouAEIOU":
            count += 1
    return count
print(vowel("ashritha"))
print()
# Write a function that returns multiple values (sum and product of two numbers).
def sm(*n):
    sum= 0
    prod = 1
    for i in n:
        sum += i
        prod *= i
    return (sum,prod)
print(sm(1,2,1))
print()

# Write a function that checks if a string is palindrome.
def palin(n):
    if n == n[::-1]:
        return True
    else:
        return False
print(palin("wow"))
print()
# Write a function to find GCD of two numbers.

# Write a function to return list of prime numbers up to n.

# Write a function that takes a list and returns only unique elements.