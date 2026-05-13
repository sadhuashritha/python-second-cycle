'''
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
def unique(*n):
    arr = []
    dic = {}
    for i in n:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i,j in dic.items():
        if j == 1:
            arr.append(i)
    return arr
print(unique(2,3,4,5,2,3,4,5,6,7,8))

'''
# Write a function to add two numbers and return the result.
def addi():
    return 3+4+7
print(addi())

# Create a function to check whether a number is even or odd.
def check(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
check(9)

# Write a function to find the factorial of a number.
def fact(n):
    # 5! = 5 *4*3*2*1
    if n == 0 | n== 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(6))

# Create a function that returns the largest among three numbers.
def largest(a,b,c):
    if a > b and a > c:
        print("A is Greater")
    elif b > a and b > c:
        print("B is Greater")
    else:
        print("C is Greater")

largest(3,1234,9)

# Create a function that takes three arguments and prints their average.
def avg(a,b,c):
    print((a+b+c)/3)
avg(1,1,1)

# Write a function to count vowels in a string.
def vowel(n):
    count = 0
    for i in n:
        if i in "aeiouAEIOU":
            count += 1
    print(count)
vowel("ashritha")


# Create a function to reverse a string.
def rev(n):
    return n == n[::-1]
print(rev("wow"))

# Write a function to calculate the sum of elements in a list.
def ele(n):
    sum = 0
    for i in n:
        sum += i
    return sum
n = [1,2,3,4,5,6,7,8,9,0]
print(ele(n))

# Create a function to check whether a string is a palindrome.
def pali(n):
    return n == n[::-1]
print(pali("madam"))