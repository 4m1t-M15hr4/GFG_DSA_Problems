
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def detectLoop(self, head):
        # code here
        st = set()
        while head is not None:
            if head in st:
                return True
            st.add(head)
            head = head.next
        return False
        
