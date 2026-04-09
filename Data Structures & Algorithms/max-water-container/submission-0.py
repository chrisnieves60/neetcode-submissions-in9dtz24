class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = float("-inf")

        for i in range(len(heights)): 
            for j in range(i+1, len(heights)): 

                width = j - i 
                length = min(heights[i], heights[j]) 

                containerSize = width * length 

                res = max(res, containerSize)

        
        return res