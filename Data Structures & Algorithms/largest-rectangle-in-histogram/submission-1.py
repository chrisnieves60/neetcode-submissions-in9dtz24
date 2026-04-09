class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: 
            return heights[0]

        res = 0
        for i in range(len(heights)): 
            minHeight = float("inf")
            for j in range(i+1, len(heights)): 
                minHeight = min(heights[i], heights[j], minHeight) 
                area = (j-i + 1) * minHeight

                res = max(res, area, heights[i], heights[j]) 
        

        return res