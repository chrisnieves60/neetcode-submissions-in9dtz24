class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we need to find a substring in s where, substring t is present in s. 

        #Present as in, "in the substring of s" 

        #there may be other characters in the given substring. 


        tFreq = {}
        l, r = 0, 0
        for char in t: 
            tFreq[char] = tFreq.get(char, 0) + 1 

        
        res = [] 

        #if this returns true. then, the string t appears in the current substring. 
        def helper(map1, map2): 
            for k, v in map2.items(): 
                if k in map1 and map1[k] >= v: 
                    continue
                else:
                    return False
            
            print("True for the above iteration ")
            return True 

        sFreq = {}
        while r < len(s):
            sFreq[s[r]] = sFreq.get(s[r], 0) + 1 

            if s[r] in tFreq and tFreq[s[r]] <= sFreq[s[r]]: 

                while helper(sFreq, tFreq) == True: 
                    string = s[l:r+1]
                    res.append(string) 
                    sFreq[s[l]] = sFreq.get(s[l], 0) - 1 
                    if sFreq[s[l]] == 0: 
                        del sFreq[s[l]] 
                    l += 1
            
            r += 1


        return "" if not res else min(res, key=len)
