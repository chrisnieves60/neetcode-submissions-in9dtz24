class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 

        print(nums) 
        res = set()


        for i in range(len(nums)): 
            l = i+1 
            r = l+1 

            while r < len(nums): 
                while r < len(nums): 
                    if nums[i] + nums[l] + nums[r] == 0: 
                        triplet = tuple(sorted([nums[i], nums[l], nums[r]]))
                        res.add(triplet)
                    r+=1 

                l += 1  
                r = l + 1 



        return list(res)