class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #a substring of s2, contains a permutation of s1, IF: 
            #len(s1) == len(s2substring) 
            #dictionary(s1) == dictionary(s2substring) 

        
        s1Dictionary = {}

        for char in s1: 
            s1Dictionary[char] = s1Dictionary.get(char, 0) + 1


        l, r = 0, 0

        s2Dictionary = {}


        #for loop, r runs till, the end of the array. 
        while r < len(s2): 
            #we wanna buidl up the dictionary with r as well. so. we're gonna do that same frequency counting. 
            # the real trick/key/challenge. knowing, when exactly, a substring ofs2, contains all characters from s1, what if it only contains some?? 

            #im thinkin r slides over, 
            #if s2[r] not in s1Dictionary, or, s2Dictionary[s2[r]] > s1Dictionary[s2[r]] , slide l over to r, and slide r = r+1. but this has to be done gracefully... 

            #remove s2[l] from s2Dictinoary, do l+=1 while l <=r 

            #once l passes r, do r = l . and continue.  

            # if it IS in the s1Dictionary, add it to s2Dictionary. 

            s2Dictionary[s2[r]] = s2Dictionary.get(s2[r], 0) + 1 

            if s1Dictionary == s2Dictionary: 
                return True 
            
            #if s2[r] not in s1Dictionary this straight up means, like, r isnt in s1 dictionary, we need to close the window up to that point. we can cehck along the way but, 
            #its looking like, this is a bad substring. and we need to close it. up to r. 
            if s2[r] not in s1Dictionary: 
                if s1Dictionary == s2Dictionary: 
                    return True     
                while l <= r:  
                    s2Dictionary[s2[l]] -= 1 
                    if s2Dictionary[s2[l]] == 0: 
                        del s2Dictionary[s2[l]] 
                    l += 1
                r = l 
                continue
            
            #if, count of s2[r] greater than in string 1. then, this is bad, bc. we need to decrement window. for as long as this is true. 
            elif s2Dictionary[s2[r]] and s2Dictionary[s2[r]] > s1Dictionary[s2[r]]: 
                if s1Dictionary == s2Dictionary: 
                    return True     
                while s2Dictionary[s2[r]] and s2Dictionary[s2[r]] > s1Dictionary[s2[r]]:  
                    s2Dictionary[s2[l]] -= 1 
                    if s2Dictionary[s2[l]] == 0: 
                        del s2Dictionary[s2[l]] 
                    l += 1
                
                r += 1
                continue
            
            r+=1 

            #a: 1 d: 1 c: 1 

            #d: 2 c: 1 


            
        

        return False 