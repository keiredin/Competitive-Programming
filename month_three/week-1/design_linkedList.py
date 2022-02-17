class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or (index == 0 and self.head == None):
            return -1
        
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val
        
        
    def addAtHead(self, val: int) -> None:
        if (self.size == 0):
            self.head.val = val
        else:
            newNode = ListNode(next=self.head, val=val)
            self.head = newNode
        self.size += 1


    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            tail = self.head
            while tail.next :
                tail = tail.next
            tail.next = ListNode(val=val)
            
            self.size += 1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next

            nextNode = temp.next
            temp.next = ListNode(val,nextNode)
            self.size += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            iter = self.head
            for i in range(index-1):
                iter = iter.next
            if (index == self.size-1):
                node = iter.next
                iter.next = None
                del node
            else:
                node = iter.next
                iter.next = node.next
                del node
            self.size -= 1
            # temp = self.head
            # for i in range(index-1):
            #     temp = temp.next
            # temp.next = temp.next.next 
            # self.size -= 1 if self.size > 0 else 0
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)