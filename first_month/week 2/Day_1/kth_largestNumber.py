from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = self.selectionSort(nums)
        return nums[k-1]
        
    def selectionSort(self,array):
        n = len(array)
        for i in range(n):
            # set maximum to this position
            maxValueIndex = i
            for j in range(i+1,n):
                # check the rest of the array to see if anything is greater
                if(int(array[j]) > int(array[maxValueIndex])):
                    maxValueIndex = j

            # if the maximum isn't in the position, swap it
            if(i != maxValueIndex):
                self.swap(array,i,maxValueIndex)
        return array

    def swap(self,array,i1,i2):
        temp = array[i1]
        array[i1] = array[i2]
        array[i2] = temp


s = Solution()
print(s.kthLargestNumber(["3","6","7","10"],4))
print(s.kthLargestNumber(["2","21","12","1"],3))