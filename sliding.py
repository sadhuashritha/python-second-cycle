# def sliding(arr,k):
#     win_arr = arr[:k]
#     count = 0
#     for i in win_arr:
#         if i in 'aeiou':
#             count += 1
#     max_vow = count
#     for i in range(k,len(arr)):
#         if arr[i-k] in 'aeiou':
#             count -= 1
#         if arr[i] in 'aeiou':
#             count += 1
#         max_vow = max(max_vow,count)
#     return max_vow

# arr = ['a','i','o','r','t','u','o']
# k = 4
# print(sliding(arr,k))

# # arr1 = ['b','e','a','t','i','o','n']
# # k1 = 3
# # print(sliding(arr1,k1))

# # 643. Maximum Average Subarray I
# def findMaxAverage(nums,k):
#         total_sum = sum(nums[:k]) 
#         # total_avg = total_sum / k
#         max_avg =  total_sum
#         for i in range(k,len(nums)):
#             total_sum += nums[i] - nums[i - k] 
#             # total_avg = total_sum / k
#             max_avg = max(max_avg,total_sum)
#         return max_avg / k
# arr = [[1,12,-5,-6,50,3]]
# k = 4
# print(findMaxAverage(arr,k))
              

n = int(input("Enter a number: "))
for i in range(2,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
        


          