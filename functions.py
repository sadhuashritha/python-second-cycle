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


# Write a function to find GCD of two numbers.

# Write a function to return list of prime numbers up to n.

# Write a function that takes a list and returns only unique elements.