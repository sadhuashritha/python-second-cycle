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


