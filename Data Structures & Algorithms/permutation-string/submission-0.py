class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #a substring of s2, contains a permutation of s1, IF: 
            #len(s1) == len(s2substring) 
            #dictionary(s1) == dictionary(s2substring) 

        
        s1Dictionary = {}

        for char in s1: 
            s1Dictionary[char] = s1Dictionary.get(char, 0) + 1
        

        for i in range(len(s2)): 
            s2Dictionary = {}
            s2Dictionary[s2[i]] = s2Dictionary.get(s2[i], 0) + 1
            if s1Dictionary == s2Dictionary: 
                return True 
            if i+1 < len(s2): 
                for j in range(i+1, len(s2)): 
                    s2Dictionary[s2[j]] = s2Dictionary.get(s2[j], 0) + 1 

                    if s1Dictionary == s2Dictionary: 
                        return True 
            else: 
                break 
        
        
        

     
        

        return False 