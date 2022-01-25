# Definition for singly-linked list.
from pip import Optional


class SingleyLinkedListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def has_cycle(head):
        stack = []
        while head:
            if head.next in stack:
                return 1
            stack.append(head)
            head = head.next

        return 0
    



