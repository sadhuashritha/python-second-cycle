
def lamuto(arr,low,high):
    pivot = high
    i = low -1
    j = low
    for j in range(low,high):
        if arr[j] < arr[pivot]:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[pivot] = arr[pivot],arr[i+1]
    print(arr,i+1)
    return i+1

def quicksort(arr,low,high):
    if low < high:
        pi = lamuto(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
a = [2,6,13,9,8,4,1,3,0]
print(a)
print(quicksort(a,0,len(a)-1))
print()
print()


def hoare(arr,low,high):
    pivot = 


