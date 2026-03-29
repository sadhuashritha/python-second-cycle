
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