class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #just think about it logically. two strings are anagrams if btoh contain the same frequency of characters/amount of characters. 

        #what we really wanna do is create freq counters of, both s and t. and then. check if the hashmaps equal each other at the end. 

        sCounter = {}
        tCounter = {}

        for char in s: 
            sCounter[char] = sCounter.get(char, 0) + 1 
        for char in t: 
            tCounter[char] = tCounter.get(char, 0) + 1  
        
        if sCounter == tCounter: 
            return True 
        
        return False 