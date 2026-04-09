class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: 
            return 0 
        mySet = set() 

        #array of integer nums, return length of longest. consecutive sequence of elmeents formed. 

        #array is unsorted. elmenents wont be consecutive as you traverse... 


        res = 1
        for n in nums: 
            #if n - 1 isnt in the set, its the start of a sequence. 
            mySet.add(n) 

        

        for n in mySet: 
            if n-1 not in mySet: 
                #start of a sequence.
                accumulator = 1 
                while n+accumulator in mySet:  
                    accumulator += 1 
                
                res = max(res, accumulator)
        
        return res