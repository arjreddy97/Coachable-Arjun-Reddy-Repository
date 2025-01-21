class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if (board[i][j] == word[0]):
                    
                    if(self.found(board,i,j,0,word)):
                        return True
        return False
            
        
        
    def found(self,board,row,col,idx,word):
        
        
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0])):
            return False
        
        
        if (board[row][col] != word[idx]):
            return False
        if (idx == len(word)-1):
            return True
        
        origChar = word[idx]
        
        board[row][col] = "#"
        
    
        xDir = [1,-1,0,0]
        yDir = [0,0,-1,1]
        
        found = False
        for i in range(4):
            
            nextRow = xDir[i] + row
            nextCol = yDir[i] + col
            
        
            found = self.found(board,nextRow,nextCol,idx+1,word)
            if (found):
                return True
            
            
        board[row][col] = origChar
        
        return found
        
        
        
        
            
        
        
        
    
