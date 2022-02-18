# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find middle
        slow,fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the first half and the reversed second half
        first,second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2