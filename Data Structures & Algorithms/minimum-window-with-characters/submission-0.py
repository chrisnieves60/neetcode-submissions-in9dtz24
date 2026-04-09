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

        for i in range(len(s)): 
            sFreq = {}
            sFreq[s[i]] = sFreq.get(s[i], 0) + 1 
            if helper(sFreq, tFreq) == True: 
                string = s[i:i+1]
                
                res.append(s[i:i+1])

            for j in range(i+1, len(s)): 
                sFreq[s[j]] = sFreq.get(s[j], 0) + 1 

                if helper(sFreq, tFreq) == True: 
                    string = s[i:j+1]
                    res.append(s[i:j+1])

        return "" if not res else min(res, key=len)




                        
        