class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #lets see.  so we want a stack. 

        stack = [] 


        #our stack, essentially, represents. increasing, vals. why? bc. we want to sorta, track, at certain, indeces, like, how muchlike, how big of a 
        #rectangle we can make. at an indecy. 

        #for i in range(len(heights)) 

        #for every thing, append to stack at end. 


        #while loop right before the append. 

        res = 0 

        for i in range(len(heights)): 
            start = i 

            while stack and heights[i] <= stack[-1][1]: 
                #monotonic, increasing, bc... 
                #we wanna pop from the stack when. we come across a val that isnt increasing. 
                #why? bc. thats a "hole". we cant make large rectangles from 7 -> 1 -> 7    
                
                val = stack.pop()
                width = i - val[0]
                length = val[1]

                res = max(res, width * length) 

                start = val[0]

            stack.append((start, heights[i]))    
        while stack: 
            val = stack.pop()
            width = len(heights) - val[0] 
            length = val[1]

            res = max(res, width * length)

        return res