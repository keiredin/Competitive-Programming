# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        
        while tail and tail.next != None:
            if tail.val == tail.next.val:
                nextNext = tail.next.next
                tail.next = tail.next.next
                
            else:
                tail = tail.next
            
        return head