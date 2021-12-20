from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        stack = []
        dict = {}
        
        for i in range(n2):
            if not stack:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    pop = stack.pop()
                    dict[pop] = nums2[i]
                    
                stack.append(nums2[i])
                
        answer = []
        for i in range(n1):
            if nums1[i] not in dict:
                dict[nums1[i]] = -1
            answer.append(dict[nums1[i]])
            
        return answer