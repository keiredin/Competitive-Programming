# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev, curr = head , head.next
        
        while curr:
            if curr.val >= prev.val:
                prev,curr =  prev.next, curr.next
                continue
                
            front = dummy
            while front.next.val < curr.val:
                front = front.next
            prev.next = curr.next
            curr.next = front.next
            front.next = curr
            curr = prev.next
            
        return dummy.next