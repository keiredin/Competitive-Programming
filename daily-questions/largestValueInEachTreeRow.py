

# Definition for a binary tree node.
from ast import List
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root]) if root else deque()
        answ = []
        
        while q:
            l = len(q)
            largest = float('-inf')
            
            for i in range(l):
                curr = q.popleft()
                largest = max(largest,curr.val)
                if curr:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                        
            answ.append(largest)
        return answ