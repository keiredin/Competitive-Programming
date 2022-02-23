# leetcode - 347. Top K Frequent Elements - Medium

from ast import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[-1*v,k] for k,v in count.items()] # convert the dictionary to array
        heapq.heapify(arr)
        print(arr,"arr")
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(arr)[1])
        return ans


