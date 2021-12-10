def countingSort(arr):
    # Write your code here
    maxValue = arr[0]
    for i in arr:
        if (i > maxValue):
            maxValue = i
    countingArr = [0] * (maxValue + 1)
    for i in arr:
        countingArr[i] = countingArr[i] + 1
    for i in countingArr:
        print(i, end=' ')


countingSort([1,1,1,2,2,2,5,6,7,3])