class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a string is an anagram of another string if their frequency counters are equal. 


        #group anagrams together into sublists. return the output in any order. 
        #two anagrams are equal  when hashmaps are equal. 

        
        groups = {}
        for i in range(len(strs)): 
            freqCounter = {}
            #freq counter for current string. 
            for char in strs[i]: 
                freqCounter[char] = freqCounter.get(char, 0) + 1 
            
            #new array
            newArr = [] 
            #convert hashmap to an array of tuples, with first index being character, second being character count 
            for k, v in freqCounter.items(): 
                newArr.append((k, v)) 
            
            #sort by characters to keep order of characters, which helps for grouping later 
            newArr = tuple(sorted(newArr, key = lambda x: x[0]) )

            #reason this works is, key = tuple of sorted frequency counter, value = the actual strings grouped together

            if newArr in groups: 
                groups[newArr].append(strs[i]) 
            else: 
                groups[newArr] = []
                groups[newArr].append(strs[i]) 
        
        print(groups)

        res = []
        for k, v in groups.items(): 
            res.append(v)
        
        
            
        
        return res 
