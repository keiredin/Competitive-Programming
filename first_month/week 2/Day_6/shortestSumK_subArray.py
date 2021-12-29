import collections
from typing import  List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = collections.deque()
        queue.append([0,0])
        summ = 0
        minlen = float('inf')
        
        for i, num in enumerate(nums):
            summ += num
            
            while queue and summ - queue[0][1] >= k:
                minlen = min(minlen, i - queue[0][0] + 1)
                queue.popleft()
                
            while queue and summ <= queue[-1][1]:
                queue.pop()
                
            queue.append([i+1, summ])
            
        return minlen if minlen < float('inf') else -1
                
    


s = Solution()
print(s.shortestSubarray([2,1,4,-6,4,8],12))
print(s.shortestSubarray([1],1))
print(s.shortestSubarray([1,2],4))