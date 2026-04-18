class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        boolean = True 
        res = float('inf')


        def helper(piles, k):
            hours = 0 
            for i in range(len(piles)): 
                count = piles[i] 
                hours += (math.ceil(count / k))

            return hours  
        
        



        

        #k = bananas per hour eating speed. we want the minimum number thats below h.
        l, r = 1, max(piles) 
        while l <= r:  
            m = (l + r) // 2

            k = m #determined eating speed 

            hoursToEatBananas = helper(piles, k) #This is calculating the amount of time it takes to eat the current pile at speed k

            if hoursToEatBananas <= h: 
                res = min(res, k)
            #if it takes too many hours at current speed to eat all the bananas, we need to go faster. thus. l = m + 1
            if hoursToEatBananas > h: 
                l = m + 1
            #if we eating them too quick, we tryna find th emin k, thus, we need to go slower. r = m - 1, find lesser values. 
            else: 
                r = m - 1

            

        
        return res