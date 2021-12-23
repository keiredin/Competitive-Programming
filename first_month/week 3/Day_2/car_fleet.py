from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stack = []
        
        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
                
        return len(stack)
        
s = Solution()
print(s.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))


















# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         p = len(position)
#         count = Counter(position)
#         stack = []
        
        
#         for i in range(p):
#             if not stack:
#                 stack.append((position[i],speed[i]))
#             else:
#                 while stack:
#                     pop,index = stack[-1]
                    
#                     if pop >= position[i] and (target - pop) // index >= (target - position[i]) // speed[i]:
#                         count[position[i]] -= 1 
#                         stack.pop()
#                     else:
#                         break
                    
#                 stack.append((position[i],speed[i]))
                
#         fleets = 0
#         for key in count:
#             fleets += count[key]
            
#         return fleets