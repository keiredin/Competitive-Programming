def countSwaps(a):
    # Write your code here
    swap = 0
    for i in range(1, len(a)):
        for j in range(0, len(a)-1):
            if (a[j] > a[j+1]):
                right = a[j]
                a[j] = a[j+1]
                a[j+1] = right
                swap += 1
                
    print("Array is sorted in "+str(swap)+ " swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[j+1]))

countSwaps([1,2,3])