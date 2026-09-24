
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 

class myStack:

    def __init__(self):
        self.top = None
        self.count = 0
        # Initialize your data members
        

    def isEmpty(self):
        if self.top is None:
            return -1
            
        # Check if the stack is empty
        

    def push(self, x):
        tem = Node(x)
        tem.next = self.top
        self.top = tem
        self.count +=1
        # Adds element x to the top of the stack
        

    def pop(self):
        if self.top is None:
            return -1
        tem = self.top 
        self.top = self.top.next
        val = tem.data
    
         
        self.count -=1
        return val
        # Removes an element from the top of the stack


    def peek(self):
        if self.top is None:
            return -1
        return self.top.data
        # Returns the top element of the stack
        # If the stack is empty, return -1


    def size(self):
        return self.count
        # Returns the current size of the stack