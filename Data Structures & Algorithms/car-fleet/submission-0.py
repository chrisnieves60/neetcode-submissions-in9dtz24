class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #we wanna loop basically, until. any car reaches the target. 
        pairs = []

        for position, speed in zip(position, speed): 
            pairs.append([position, speed])
        
        pairs = sorted(pairs, key=lambda x: x[0]) 

        print(pairs)

        stack = [] 
        res = 0 
        for i in range(len(pairs)-1, -1, -1): 
            time = (target - pairs[i][0]) / pairs[i][1]

            #so if a stack exists, and time for current car to reach dest, <= time at top of stack, (3=3) then, those are their own fleet. 
            if stack and time <= stack[-1]:  
                continue 
            stack.append(time) 

        
        return len(stack)


        
        
    
