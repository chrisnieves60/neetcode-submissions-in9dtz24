import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        [1, 1, 2, 8] 
        [48, 24, 6, 1]

        #key: build up prefix upon first run. 

        prefix = [] 
        prefixMult = 1 

        for i in range(len(nums)): 
            if i==0: 
                prefix.append(prefixMult) 
            else: 
                prefixMult*=nums[i-1]
                prefix.append(prefixMult) 
        
        print(prefix) 

        suffix = []
        suffixMult = 1 

        for i in range(len(nums) - 1, -1, -1): 
            if i==len(nums) - 1: 
                suffix.append(suffixMult) 
            else: 
                suffixMult*=nums[i+1]
                suffix.append(suffixMult) 
        
        suffix.reverse()        
        print(suffix)

        for i in range(len(prefix)): 
            prefix[i] *= suffix[i] 
        
        print(prefix)

        return prefix

