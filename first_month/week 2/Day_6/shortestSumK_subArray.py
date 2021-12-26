from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        currentSum = 0
        n = len(nums)
        minlen = n*n
        
        while end < n and start < n-1:
            currentSum += nums[end]
            
            if(currentSum >= k):
                
                # subarrays += (end - start + 1)
                currentSum -= nums[start]
                minlen = min(minlen,len(nums[start:end+1]))
                print(nums[start:end+1])
                start += 1
                if end > start:
                    continue 
        
            if(end >= n-1):
                currentSum -= nums[start]
                start += 1
                continue
                
            end += 1
        return minlen if minlen <= n else -1
    


s = Solution()
print(s.shortestSubarray([2,1,4,-6,4,8],12))
print(s.shortestSubarray([1],1))
print(s.shortestSubarray([1,2],4))