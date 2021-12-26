import heapq
from collections import List,Counter,deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-c for c in counter.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        
        temp = deque()   # pairs of [-count, idletime]
        
        while maxHeap or temp:
            time += 1
            
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    temp.append([c,time+n])
                    
            if temp and temp[0][1] == time:
                heapq.heappush(maxHeap, temp.popleft()[0] )
                
            
        return time