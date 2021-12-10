# class Solution:
#     def __init__(self) -> None:
#         pass
def swap(a,b):
    c = a
    a = b
    b = c

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minV_index = i
        for j in range(i+1,n):
            if(arr[j] < arr[minV_index]):
                minV_index = j
        arr[minV_index],arr[i] = arr[i], arr[minV_index]
    return arr

print(selectionSort([1,4,3,2,1]))