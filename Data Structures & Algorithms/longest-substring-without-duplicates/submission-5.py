class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        elif len(s) == 1:  
            return 1  

        #have some ideas. 

        #l pointing to 0, r pointing to 1. 

        mySet = set() 

        mySet.add(s[0]) #fuck it add first char to set why not. 

        l, r = 0, 1


        res = len(mySet) 
        while r < len(s): 
            res = max(res, len(mySet)) 
            print(len(mySet))
            if s[r] not in mySet: 
                mySet.add(s[r])
                r+=1 
                res = max(res, len(mySet)) 

                continue 
            
            while s[r] in mySet: 
                
                mySet.remove(s[l]) 
                l += 1
            
            mySet.add(s[r])
            r += 1
        
        return res 
        
