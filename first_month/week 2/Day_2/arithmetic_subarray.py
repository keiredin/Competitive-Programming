from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(nums)
        left = len(l)
        right = len(r)
        answer = []
        
        for i in range(left):
            answer.append(self.isArithmetic(nums[l[i]: r[i]+1]))

        return answer    
    
    def isArithmetic(self,subArray):
        n = len(subArray)
        if n < 2:
            return False
        elif n == 2:
            return True
        subArray.sort()
        difference = subArray[1] - subArray[0] 
        for i in range(n-1) :
            if subArray[i+1] - subArray[i] != difference:
                return False
        
        return True

s = Solution()
nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

print(s.checkArithmeticSubarrays(nums,l,r))