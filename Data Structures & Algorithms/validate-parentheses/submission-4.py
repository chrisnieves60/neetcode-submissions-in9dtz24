class Solution:
    def isValid(self, s: str) -> bool:
        
        #bracket types: {} [] () 

        stack = [] 

        dictionary = {} 

        dictionary["]"] = "["
        dictionary["}"] = "{"
        dictionary[")"] = "(" 
        
        for char in s: 
            #its an opening bracket 
            if char == "{" or char == "[" or char == "(": 
                stack.append(char)
            
            #its a closing bracket 
            else: 
                #we know its matching if , stack.pop() == dictonary[char] 
                if stack and stack.pop() == dictionary[char]: 
                    #matching bracket, continue 
                    continue 
                else: 
                    return False
        

        return True if not stack else False 



"[]"