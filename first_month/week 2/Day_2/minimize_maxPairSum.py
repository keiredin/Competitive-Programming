from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = n/2
        left = 0
        right = n - 1
        minMax = 0
        
        while left < mid and right >= mid:
            minMax = max(minMax,(nums[left] + nums[right]))
            left += 1
            right -= 1
        return minMax


s = Solution()
print(s.minPairSum([4,1,5,1,2,5,1,5,5,4]))