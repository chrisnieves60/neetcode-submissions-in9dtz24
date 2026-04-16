class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#goal is, to return an array, where each value is the number of days for a warmer day to appear for that index. 
        array = [0] * len(temperatures) 
        stack = [] 

        #so my paproach is, im going to parse this backwards with for loop. 

        #if not stack, append to stack, so lets say, we had [50] on the stack. 


        #when we reach 26, 27, and 28, ALL of their next warmest days is that 50.  

        #, this means, we want this stack to be , monotonic DECREASING. 

        #always append to stack. 

        #but write a forloop saying, if current value > stack[-1] 

        #then stack.pop, 

        for i in range(len(temperatures) - 1, -1, -1): 

            while stack and temperatures[i] >= stack[-1][1]: 
                index, val = stack.pop() 

                if stack: 
                    array[index] = stack[-1][0] - index
            stack.append([i, temperatures[i]])


        while stack: 
            index, val = stack.pop() 

            if stack: 
                array[index] = stack[-1][0] - index 


        
        return array