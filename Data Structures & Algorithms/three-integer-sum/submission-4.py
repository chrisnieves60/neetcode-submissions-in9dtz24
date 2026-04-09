class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 

        print(nums) 
        res = set()


        for i in range(len(nums)): 
            l = i+1 
            r = len(nums) - 1

            while l < r: 

                if nums[i] + nums[l] + nums[r] == 0: 
                    triplet = tuple(sorted([nums[i], nums[l], nums[r]]))
                    res.add(triplet)
                    l += 1
                    
                elif nums[i] + nums[l] + nums[r] < 0: 
                    #too small, move l += 1 
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0: 
                    #too big, move r -= 1 
                    r -= 1



        return list(res)