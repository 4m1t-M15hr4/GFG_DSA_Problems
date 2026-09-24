class myStack:
    def __init__(self, n):
        self. arr =[0] * n
        self.cap = n
        self.top = -1
        # Define Data Structures

    
    def isEmpty(self):
        # Check if stack is empty
        return self.top == -1

    
    def isFull(self):
        return self.top == self.cap -1
        
        # Check if stack is full

    
    def push(self, x):
        if self.top == self.cap -1:
            return -1
        self.top +=1
        self.arr[self.top] = x
        
        # Insert x at the top of the stack
        

    
    def pop(self):
        if self.top == -1:
            return -1
        x = self.arr[self.top]
        self.top -=1
        return x
        # Removes an element from the top of the stack

    
    def peek(self):
        # Returns the top element of the stack
        if self.top == -1:
            return -1
        return self.arr[self.top]
            