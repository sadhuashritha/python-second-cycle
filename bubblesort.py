
arr = [5,3,1,4]
n = len(arr)
for i in range(n): # 0
    for j in range(n-i-1): # 0 1 2
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        print(arr)

# -----------------------------------------
# | Pass (i) | j | j+1 | Compared Indices |
# | -------- | - | --- | ---------------- |
# | 0        | 0 | 1   | (0,1)            |
# | 0        | 1 | 2   | (1,2)            |
# | 0        | 2 | 3   | (2,3)            |
# | 1        | 0 | 1   | (0,1)            |
# | 1        | 1 | 2   | (1,2)            |
# | 2        | 0 | 1   | (0,1)            |
# -----------------------------------------
print()

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
nums = [2,0,2,1,1,0]
n = len(nums)
for i in range(n):
    for j in range(n-i-1):
        if nums[j] > nums[j+1]:
            temp = nums[j] 
            nums[j] = nums[j+1]
            nums[j+1] = temp
print(nums)
print()
print()
print()

s = [1,2,3,4,5,6.3,7,8]
target = 6.3
found = False
for i in range(len(s)): #1
    if s[i] == target:
        found = True
print(found)  