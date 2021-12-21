from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n
        dict = {}
        
        for i in range(n):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    pop, idx = stack.pop()
                    answer[idx] = i - idx
                stack.append((temperatures[i],i))
        
        return answer

s = Solution()

print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))




