# Definition for singly-linked list.
from pip import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        front = head
        middleNode = self.middle(front)
        reversed_half = self.reverseLinkedList(middleNode)
       
        maxSum = 0
        
        while reversed_half:
            currSum = head.val + reversed_half.val
            maxSum = max(maxSum,currSum)
            
            head = head.next
            reversed_half = reversed_half.next
            
        return maxSum
            
        
        
    def middle(self,front):
        tail = front
        while tail and tail.next:
            front = front.next
            tail = tail.next.next
        return front
            
            
    def reverseLinkedList(self,head):    
        if head == None:
            return head
        prev = None
        node = head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
        