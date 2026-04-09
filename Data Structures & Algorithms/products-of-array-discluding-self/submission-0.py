class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #given integer array nums, return array output, where output[i] is prod of 

        #all elements of nums except nums[i] 

        res = [1] * len(nums) 

        for i in range(len(nums)): 
            for j in range(len(nums)): 

                if i==j: 
                    continue
                
                res[i] *= nums[j] 
        
        print(res)
        return res
