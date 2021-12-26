class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left,right = 0,0
        current_abs = 0
        size = 0
        ans = []
        
        
        
        while (left < n-1 and right < n):
            
            largest = max(nums[left:right+1])
            smallest = min(nums[left:right+1])
            print(left,right,"left right")
            print(smallest,largest)
            
            
            current_abs = abs(nums[left] - nums[right])
            
            
            if current_abs <= limit and abs(largest - smallest) <= limit:
                right += 1
                size += 1
                        
                if size > 1:
                    ans.append(size)
                
            else:
                left += 1
                size -= 1
        
        return max(ans) if ans else 1