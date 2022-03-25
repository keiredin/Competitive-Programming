from ast import List

# solution 1 
  # -> time - O(n**2)  and space - O(1)

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        answ = 0
        n = len(nums)
        for i in range(n):
            l,r = nums[i], nums[i]
            for j in range(i, n):
                l = min(l, nums[j])
                r = max(r, nums[j])
                answ += r - l
        return answ


# solution 2
# time - O(n) and space - O(n)

