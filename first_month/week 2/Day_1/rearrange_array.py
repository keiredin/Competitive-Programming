import math
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda i:[i])
        l = []
        n = len(nums)
        mid = n/2
        i = 0
        j = math.ceil(mid)
        
        
        while( (i < mid) and (j < n) ):
            l.append(nums[i])
            l.append(nums[j])
            i += 1
            j += 1
        
        if (n % 2 != 0):
            l.append(nums[i])

        return l


s = Solution()
print(s.rearrangeArray([10,7,5,4,3]))
print(s.rearrangeArray([1,2,3]))
print(s.rearrangeArray([3,1,12,10,7,6,17,14,4,13]))

