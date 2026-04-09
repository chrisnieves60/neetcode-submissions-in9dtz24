class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #return res, where res[i] is num of days after ith day before a warmer temp appears... 

        #if none appears. set it to 0. 

        res = []

        for i in range(len(temperatures)): 
            tempFound = False
            for j in range(i+1, len(temperatures)): 
                if temperatures[j] > temperatures[i]: 
                    tempFound = True 
                    res.append( j - i ) 
                    break 
            
            if tempFound == False: 
                res.append(0)


        return res  