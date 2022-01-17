# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
      
        stack = []
        for i in range(len(ans)):
            if not stack:
                stack.append(i)
            else:
                while stack and ans[stack[-1]] < ans[i]:
                    ans[stack.pop()] = ans[i]
                stack.append(i)
        
        while stack:
            ans[stack.pop()] = 0
            
        return ans
            