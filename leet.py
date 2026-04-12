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

