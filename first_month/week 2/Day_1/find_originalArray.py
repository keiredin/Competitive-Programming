from typing import Counter, List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if(n%2 != 0):
            return []
        count = Counter(changed)
        changed.sort()
        original = []
        
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                original.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                original.append(num)
                
        return original if len(original) == n // 2 else []

s = Solution()
print(s.findOriginalArray([1,3,4,2,6,8]))
print(s.findOriginalArray([6,3,0,1]))
print(s.findOriginalArray([1]))
print(s.findOriginalArray([0,2,0,4]))
print(s.findOriginalArray([0,0,0,0]))
