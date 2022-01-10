from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        stack = []
        nums.sort()
        
        for i in nums:
            if not stack:
                stack.append(i)
            elif(stack[-1] >= i):
                moves += stack[-1]+1 - i
                i += stack[-1]+1 - i  
                       
            stack.append(i)
            
        return moves