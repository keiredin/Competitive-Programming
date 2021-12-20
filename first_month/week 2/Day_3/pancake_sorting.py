from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr) -1
        output = []

        def flip(start,end):
            while start < end:
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -= 1
        for i in range(n,-1,-1):
            maxVIndex = i
            for j in range(0,i):
                if arr[j] > arr[maxVIndex]:
                    maxVIndex = j
            
            if maxVIndex != i:
                flip(0,maxVIndex) # bring the maximum element to index 0
                output.append(maxVIndex+1)
                flip(0,i)               #flip it to the last index of the array
                output.append(i+1)
                           
        return output

s = Solution()
print(s.pancakeSort([3,2,4,1]))