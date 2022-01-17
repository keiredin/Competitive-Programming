# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevNode = ""
        node = head
        count = 1
        while node and node.next:
            count += 1
            node = node.next
        if (count==n):
            head = head.next
            return head
        value = count - n + 1
        node = head
        while value > 1:
            prevNode = node
            node = node.next
            value -= 1
        prevNode.next = node.next
        node = None
        return head