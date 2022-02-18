from ast import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
            
        r = len(nums) - k
        nums[:] = nums[r:len(nums)] + nums[0:r] 
        return nums