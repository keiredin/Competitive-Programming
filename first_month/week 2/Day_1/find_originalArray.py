from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        n = len(changed)
        
        if(n % 2 == 0 ):
            for i in range(n-1):
                for j in range(i+1,n):
                    if(changed[j] == 2 * changed[i]):
                        original.append(changed[i])
                        changed[j] = -1
                        
        else:
            original = []

        return original

s = Solution()
print(s.findOriginalArray([1,3,4,2,6,8]))
print(s.findOriginalArray([6,3,0,1]))
print(s.findOriginalArray([1]))
print(s.findOriginalArray([0]))

