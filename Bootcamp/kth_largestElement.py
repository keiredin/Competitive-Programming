# leetcode - 703. Kth Largest Element in a Stream - easy

from ast import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # self.nums = [-i for i in nums]
        
        

    def add(self, val: int) -> int:
        heapq.heapify(self.nums)
        heapq.heappush(self.nums,val)
        
        n = len(self.nums)
        
        while n > self.k:
            heapq.heappop(self.nums)
            n -= 1
        return self.nums[0]

        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)