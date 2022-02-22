# leetcode - 692. Top K Frequent Words - medium
from collections import Counter
from typing import List
import heapq as hq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        arr = [[-1*v,k] for k,v in count.items()] # convert the dictionary to array
        hq.heapify(arr)
        print(arr,"arr")
        
        ans = []
        for i in range(k):
            ans.append(hq.heappop(arr)[1])
        return ans