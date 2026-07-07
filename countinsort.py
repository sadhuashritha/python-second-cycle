# Stable sorting:
def countingsort(arr):
    s = max(arr)
    count = [0] * (s + 1)
    for i in arr:
        count[i] += 1
    print("freq count arr: ",count)
    for i in range(1,len(count)):
        count[i] += count[i-1]
    print("prefix sum arr: ",count)
    ans = [0] * len(arr)
    for i in range(len(arr)-1,-1,-1):
        ans[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return ans
arr = [4,3,2,5,6,1,8,4,3,0]
print(countingsort(arr))
