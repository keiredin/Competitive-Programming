from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n
        
        for i in range(n):
            if not stack:
                stack.append(temperatures[i])
            else:
                while stack and stack[-1] < temperatures[i]:
                    pop = stack.pop()
                    popIndex = temperatures.index(pop)
                    answer[popIndex] = i - popIndex
                    
                stack.append(temperatures[i])
        
        return answer

s = Solution()

print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
