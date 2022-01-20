# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head.next
        pnode = None        #previous node
        while head.next != None:
            head.next = pnode
            pnode = head
            head = temp
            temp = head.next
            
        head.next = pnode
        
        return head   