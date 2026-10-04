
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val


class Solution:
    def removeLoop(self, head):
        temp = set()
        prev = None
        while head:
            if head in temp:
                prev.next = None
                return
            temp.add(head)
            prev = head
            head = head.next
        # if head is None and head.next is None:
        #     return 
        # # code here
        # slow = head
        # fast = head 
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         cycle = True
        #         return
            
                