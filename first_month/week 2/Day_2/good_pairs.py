from typing import Counter, List

class Solution:
    def numIdenticalPairs(self,nums: List[int]) -> int:
            count = Counter(nums)
            pairs = 0
            for num in nums:
                if (count[num] > 0):
                    pairs += count[num] * (count[num] -1) // 2   # number of a good pairs a number can make
                    count[num] = 0
            return pairs


s = Solution()
print(s.numIdenticalPairs([1,1,1,2,3,3]))
print(s.numIdenticalPairs([1,1,1,1]))
print(s.numIdenticalPairs([1,2,3]))

