arr = [5,3,1,4]
n = len(arr)
for i in range(n): # 0
    for j in range(n-i-1): # 0 1 2
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        print(arr)


