from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n-1):
            for j in range( i+1, n):
                if(self.compare(nums[i],nums[j])):
                    nums[i],nums[j] = nums[j],nums[i]

        return ''.join(map(str,nums))   # string_nums = [str(int) for int in nums] return "".join(string_nums)


    def compare(self,num1,num2):
        str1 = str(num1)
        str2 = str(num2)
        return str1+str2 < str2+str1

s = Solution()
print(s.largestNumber([3,30,34,5,9]))