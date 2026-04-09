class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] + nums[j] == target: 
        #             return [i, j] 

        
        #goal. two numbers that == target. 

        myMap = {} 

        for i in range(len(nums)): 

            if target - nums[i] in myMap: 
                return [myMap[target - nums[i]], i]

            myMap[nums[i]] = i 
                
        
        return 0