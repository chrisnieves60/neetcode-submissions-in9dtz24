class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} 

        for number in nums: 
            freq[number] = freq.get(number, 0) + 1 
        

        freqTuple = tuple(sorted(freq.items(), key=lambda x: x[1]))   #freq sorted by key in tuple form 
                                                #key is second parameter. set it equal to 
                                                #lambda function, which takes in x, 
                                                #x is an array containing current
                                                #freq hashmap entry. 
                                                #x[1] is the value. x[0] is the key. 
        #freqTuple = [(1: 1), (2: 2), (3: 3)] 
        print(freqTuple)


        res = []
        for i in range(len(freqTuple)-1, len(freqTuple)- k - 1, -1):  
            res.append(freqTuple[i][0]) 
        
        return res 
        
        # return res 