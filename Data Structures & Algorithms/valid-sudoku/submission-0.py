class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #each row must contain digits 1-9 without duplicates. 

        for row in board: 
            rowSet = set() 
            for col in row: 
                if col == ".": 
                    continue 
                
                if col not in rowSet: 
                    rowSet.add(col)
                else: 
                    return False 

        #Each col must contain digits 1-9 without duplicates 
        for i in range(len(board)): 
            colSet = set() 
            for j in range(len(board[0])): 
                cell = board[j][i] 
                if cell == ".": 
                    continue 
                if cell not in colSet: 
                    colSet.add(cell)
                else: 
                    return False 
        

        #traverse each 3x3 box 
        #for each box, traverse each cell, and add them to set. 
        for boxRow in range(0, len(board), 3): 
            for boxCol in range(0, len(board[0]), 3): 
                #boxCol always starts at, topright of square, and traverses -> right. 
                subBoxSet = set()

                for k in range(boxRow, boxRow + 3): 
                    for j in range(boxCol, boxCol + 3): 
                        cell = board[k][j] 
                        if cell == ".": 
                            continue 
                        if cell not in subBoxSet: 
                            subBoxSet.add(cell)
                        else: 
                            return False 


        return True 