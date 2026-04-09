class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # [index, temp]

        for i in range(len(temperatures) - 1, -1, -1): 

            
            #pop till temperatures[i] is not greater than top of stack 
            while stack and temperatures[i] >= stack[-1][1]: 
                stack.pop() 
            
            #after pops, top of stack is next warmest day, for temperatures[i], calulate it. 
            if stack and stack[-1][1] > temperatures[i]: 
                res[i] = stack[-1][0] - i

            stack.append((i, temperatures[i]))
        

        return res