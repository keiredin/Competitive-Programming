from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  #make sure that all previous heights were checked when we end the for loop
        largest = 0
        inc_stack = []
        
        for index, element in enumerate(heights):
            if not inc_stack:
                inc_stack.append(index)
            else:
                while inc_stack and heights[inc_stack[-1]] > element:

                    height = heights[inc_stack[-1]]
                    inc_stack.pop()
                    if inc_stack:
                        length = index - inc_stack[-1] -1
                    else:
                        length = index

                    largest = max(largest, height * length)
                    
                inc_stack.append(index)
                
        return largest