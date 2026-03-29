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
