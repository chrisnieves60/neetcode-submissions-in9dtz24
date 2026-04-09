class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val) 
        if self.minStack and val <= self.minStack[-1] or not self.minStack: 
            self.minStack.append(val)  
        
    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop() 

        self.stack.pop() 


    def top(self) -> int:
        if self.stack: 
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack: 
            return self.minStack[-1] 



