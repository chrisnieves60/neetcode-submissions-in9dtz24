class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r: 
            m = (l + r) // 2

            print(matrix[m][len(matrix[m]) -1])
            #if it hits this if statement, then its in this row. 
            if matrix[m][0] <= target and matrix[m][len(matrix[m]) -1] >= target: 


                innerL = 0
                innerR = len(matrix[m]) - 1

                while innerL <= innerR: 
                    innerM = (innerL + innerR) // 2  
    
                    if matrix[m][innerM] == target: 
                        return True 
                    elif matrix[m][innerM] < target: 
                        innerL = innerM + 1
                    elif matrix[m][innerM] > target: 
                        innerR = innerM - 1 
                
                return False 
                
                

            elif matrix[m][0] > target:  
                r = m - 1
                continue 
            elif matrix[m][len(matrix[m]) - 1] < target: 
                l = m + 1 
                continue 
            
        
        return False 