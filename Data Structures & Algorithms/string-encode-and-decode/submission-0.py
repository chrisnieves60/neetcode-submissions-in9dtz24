class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:  
            string+=str(len(word)) + "#" + word
        #["Hello", "World", "#4k55n2"] -> "5#Hello5#World7##4k55n2" 
        print(string )
        return string 

    def decode(self, s: str) -> List[str]:
        #encoded setup is essentially, first character, or sometimes even first few, 
        #will always be the length. so this means, 


        #we wanna traverse from the beginning, until the first # we see. 

        # thats our delimiter. tells us, okay, the characters before this, is the length of the string in front. 

        l, r = 0, 0 

        res = []
        while l < len(s): 

            r = l 
            while r < len(s) and s[r] != "#": 
                r += 1 
            
            length = int(s[l:r])

            res.append(s[r+1: r + length + 1]) 

            l = r + length + 1
        
        return res 

        #["Hello", "World", "#4k55n2"] -> 
        # "5#Hello5#World7##4k55n2"  








