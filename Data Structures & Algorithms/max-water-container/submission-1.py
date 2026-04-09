class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = float("-inf")

        l, r = 0, len(heights) - 1

        while l < r: 

            width = r - l 
            length = min(heights[r], heights[l]) 
            containerSize = width * length 
            res = max(res, containerSize)

            if heights[l] <= heights[r]: 
                l += 1
            
            elif heights[l] > heights[r]: 
                r -= 1 
        
        return res