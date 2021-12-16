from collections import Counter
from typing import List
import math

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        nums.sort()
        numOfOpns = 0
        for num in nums:
            if count[num] and count[k - num]:
                if num == k - num and count[num]  >= 2:
                    numOfOpns += math.floor(count[num] / 2)
                    count[num] = 0
                elif num == k-num and count[num] < 2:
                    continue
                else:
                    numOfOpns += min(count[num],count[k-num])
                    count[num] = 0
                    count[k-num] = 0                
        return numOfOpns

s = Solution()
f = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]

print(s.maxOperations(f,4))   #59


