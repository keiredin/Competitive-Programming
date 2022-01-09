from collections import Counter
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        
        for h in range(n,-1,-1):
            for j in range(n):
                if h <= citations[j] and n-j >= h and j+1 >= n-h:
                    return h



s = Solution()
print(s.hIndex([[3,0,6,1,5]]))


# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         n = len(citations)
#         counter = Counter(citations)
#         counter[i if i >= 3]
#         citations.sort()
#         i = 0

#         while i <= n // 2:
#             if len(citations[:i+1]) == n - i and len(citations[i:]) >= i:
#                 return i