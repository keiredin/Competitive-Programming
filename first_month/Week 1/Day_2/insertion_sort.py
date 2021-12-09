def insertionSort1(n, arr):
    lastElement = arr[n-1]
    for i in range(n-1, 0, -1):
        if(arr[i-1] > lastElement):
            arr[i] = arr[i-1]
            for element in arr:
                print(element, end=" ")
            print()
            if( (i -1 == 0) and (arr[0] > lastElement)):
                arr[0] = lastElement
                for element in arr:
                    print(element, end=" ")
                print()
        else:
            arr[i] = lastElement
            for element in arr:
                print(element, end=" ")
            break

insertionSort1(10, [2,4,6,8,9,9,12,23,24,1])