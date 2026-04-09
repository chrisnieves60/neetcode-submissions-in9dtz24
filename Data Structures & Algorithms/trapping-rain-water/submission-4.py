class Solution:
    def trap(self, height: List[int]) -> int: 
        #OPTIMAL 

        res = 0 

        maxLeftArr = []
        maxRightArr = [] 
        maxLeft = 0
        maxRight = 0 
        for i in range(len(height)): 
            #how do we say, oh, whats the max left we seen so far? 

            maxLeftArr.append(maxLeft) 
            maxLeft = max(maxLeft, height[i] )  
        
        print(maxLeftArr)

        for i in range(len(height) -1, -1, -1): 
            maxRightArr.append(maxRight) 
            maxRight = max(maxRight, height[i]) 
        
        
        maxRightArr.reverse()

        print(maxRightArr)

        for i in range(len(height)): 

            trapped = min(maxLeftArr[i], maxRightArr[i]) - height[i] 

            if trapped > 0: 
                res+= trapped
        
        return res