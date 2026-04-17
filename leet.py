# 2413. Smallest Even Multiple
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n*2


           
# 1880. Check if Word Equals Summation of Two Words
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        val = ""
        for i in firstWord:
            val += str(ord(i) - ord('a'))

        val1 = ""
        for j in secondWord:
            val1 += str(ord(j) - ord('a'))
        
        value = ""
        for k in targetWord:
            value += str(ord(k) - ord('a'))
        
        return int(val) + int(val1) == int(value)


#initialise a parent class as Employee-constructor with parameter name, child class as Developer - constructor with parameter prog_lang, user super()

class Employee:
    def __init__(self,name):
        self.name = name

class Developer(Employee):
    def __init__(self,name,fullname):
        super().__init__(name)
        self.fullname = fullname

d = Developer("Ashritha","Sadhu")
print(d.name)
print(d.fullname)

# Count Integers With Even Digit Sum
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1,num+1):
            sumi = 0
            for j in str(i):
                sumi += int(j)
            if sumi % 2 == 0:
                count+=1
        return count

# Valid Perfect Square .

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = int(num ** 0.5)
        return r * r == num

# 1413. Minimum Value to Get Positive Step by Step Sum
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # prefix = [0] * len(nums)
        # prefix[0] = nums[0]
        # for i in range(1,len(nums)):
        #     prefix[i] = prefix[i-1] + nums[i]
        # mini = min(prefix)
        prefix = 0
        mini = 0
        for i in nums:
            prefix += i
            mini = min(mini,prefix)
        return max(1,1-(mini))
 

#  1805. Number of Different Integers in a String
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        for i in word:
            if i.isdigit():
                s += i
            else:
                s += " "
        arr = s.split()
        unique = set()
        for i in arr:
            unique.add(int(i))
        return len(unique)
    
# 2108. Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        else:
            return ""

# 2778. Sum of Squares of Special Elements 
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in range(n):
            if n % (i + 1) == 0:
                sum += (nums[i] * nums[i])
        return sum

# 1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices

