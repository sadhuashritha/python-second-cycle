arr = [3,2,8,4,5,2,5,2,0]
def quicksort(low,high):
    if low >= high:
        return
    pivot = low
    left = pivot + 1
    right = high
    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while left <= right and arr[right] > arr[pivot]:
            right -= 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    arr[right],arr[pivot] = arr[pivot],arr[right]
    quicksort(low,right-1)
    quicksort(right+1,high)
quicksort(0,len(arr)-1) 
print(arr)
