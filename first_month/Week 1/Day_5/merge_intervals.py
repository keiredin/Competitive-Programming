import math
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        nonOverlapping = [intervals[0]]
        for i in range(len(intervals) - 1):
            if((nonOverlapping[-1][1] >= intervals[i+1][0]) ):
                nonOverlapping[-1][1] = max(nonOverlapping[-1][1],intervals[i+1][1])
            else:
                nonOverlapping.append(intervals[i+1])
        return nonOverlapping



s = Solution()
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(s)