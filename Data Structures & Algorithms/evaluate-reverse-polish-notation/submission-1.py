class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #i just realized, it is assumed that  two given operands are grouped together. when a operation is hit. 
        stack = [] 
        for token in tokens: 
            if token == "+": 
                stack.append(stack.pop() + stack.pop()) 

            elif token == "-": 
                a, b = stack.pop(), stack.pop() 
                stack.append(b - a) 
            elif token == "/": 
                a, b = stack.pop(), stack.pop() 
                stack.append(int(b / a)) 
            elif token == "*": 
                stack.append(stack.pop() * stack.pop()) 
            
            else: 
                stack.append(int(token)) 
            
        
        return stack[-1] 