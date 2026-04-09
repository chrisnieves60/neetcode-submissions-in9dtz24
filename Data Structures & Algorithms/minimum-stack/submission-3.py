class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and val <= self.minStack[-1] or not self.minStack: 
            self.minStack.append(val)
        

    def pop(self) -> None:
        poppedVal = self.stack.pop()
        if self.minStack[-1] == poppedVal: 
            self.minStack.pop() 

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.minStack[-1] 


  




