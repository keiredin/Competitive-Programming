from ast import List
from collections import Counter,deque


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        queue = deque(s[0])  # to contain letter in current partition with count greater than 0
        curr = queue.popleft()
        answ = []
        size = 0
        visited = set()
        
        for letter in s:
            curr = curr if curr != 0 else letter
            
            if letter not in visited:
                visited.add(letter)
                queue.append(letter)
                count[letter] -= 1
                size += 1
      
            elif letter in visited:
                count[letter] -= 1
                size += 1
                
            if count[letter] == 0:
                visited.remove(letter)
          
        
            if count[curr] == 0:
                if len(visited) == 0:   # if visited is empty
                    queue = deque()
                    answ.append(size)
                    size = 0
                    curr = 0
                    continue
                else:
                    curr = queue.popleft()
                    while curr not in visited:
                        curr = queue.popleft()
                        
                    visited.remove(curr)
          
        return answ