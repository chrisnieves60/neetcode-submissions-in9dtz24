class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = float('inf')

        while l<=r:  
            m = (l+r) //2 
            print(m)
            res = min(res, nums[l], nums[m], nums[r]) 

            if nums[l] <= nums[m]: 
                #we in left sorted portion 
                l = m + 1 
            else: 
                #we in right sorted portion  
                r = m-1
        
        return res 


