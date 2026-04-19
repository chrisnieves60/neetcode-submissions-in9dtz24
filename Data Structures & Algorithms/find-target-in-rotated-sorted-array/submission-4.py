class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l+r) //2 

            if nums[m] == target: 
                return m

            #left sorted position 
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: 
                    r -= 1  
                else: 
                    l += 1 

            
            #right sorted portion 
            else: 
                if nums[m] < target <= nums[r]: 
                    l+=1 
                else: 
                    r-=1 
            
        return -1
                 
