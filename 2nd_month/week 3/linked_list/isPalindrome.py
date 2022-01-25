# Definition for singly-linked list.
from pip import Optional


class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        cur = head
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next
        cur.next = None
        
        reversed_list = self.reverseLinedList(slow)
        cur = head
        while cur:
            if cur.val != reversed_list.val:
                return False
            cur = cur.next 
            reversed_list = reversed_list.next
            
        return True
        
    
        
    def reverseLinedList(self,head):    
        prev = None
        node = head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev




# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         s = []
#         while head:
#             s.append(head.val)
#             head = head.next
            
#         return s == s[::-1]