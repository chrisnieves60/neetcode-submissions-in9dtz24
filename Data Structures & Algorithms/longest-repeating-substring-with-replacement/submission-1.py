class Solution:
    def characterReplacement(self, s: str, k: int) -> int:



        l, r = 0, 0

        res = 0

        hashMap = {}



        while r < len(s): 
            
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1 
            

            print(r-l+1)



            replacements = max(hashMap.values())  - (r - l + 1 )

            while (r - l + 1)  - max(hashMap.values()) > k: 
                hashMap[s[l]] = hashMap.get(s[l], 0) - 1 
                l += 1
            res = max(res, r - l + 1 )
            r += 1
        
        return res
