class Solution:
    def trap(self, height: List[int]) -> int: 

        res = 0 

        for i in range(len(height)): 

            #find max height on left for a given i. 
            l, r = i-1, i+1 
            maxLeft = 0 
            maxRight = 0 

            while l >= 0: 
                maxLeft = max(maxLeft, height[l]) 
                l-=1
            while r < len(height): 
                maxRight = max(maxRight, height[r]) 
                r+=1
            print("MaxLeft on the "+ str(i) + "Iteration: " + str(maxLeft))
            
            
            trapped = min(maxLeft, maxRight) - height[i] 

            if trapped > 0: 
                res+= trapped 

        

        return res 