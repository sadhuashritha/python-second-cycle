def sliding(arr,k):
    win_arr = arr[:k]
    count = 0
    for i in win_arr:
        if i in 'aeiou':
            count += 1
    max_vow = count
    for i in range(k,len(arr)):
        if arr[i-k] in 'aeiou':
            count -= 1
        if arr[i] in 'aeiou':
            count += 1
        max_vow = max(max_vow,count)
    return max_vow

arr = ['a','i','o','r','t','u','o']
k = 4
print(sliding(arr,k))

# arr1 = ['b','e','a','t','i','o','n']
# k1 = 3
# print(sliding(arr1,k1))

# 643. Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum = sum(nums[:k]) 
        # total_avg = total_sum / k
        max_avg =  total_sum
        for i in range(k,len(nums)):
            total_sum += nums[i] - nums[i - k] 
            # total_avg = total_sum / k
            max_avg = max(max_avg,total_sum)
        return max_avg / k
              


