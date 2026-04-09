class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")

        l, r = 0, len(s) - 1

        while l<=r: 
            if s[l].isalnum() == False: 
                l+=1
                continue
            elif s[r].isalnum() == False: 
                r-=1 
                continue 

            if s[l].lower() == s[r].lower(): 
                l += 1 
                r -= 1
                continue 
            else: 
                return False 
        
        return True 

        