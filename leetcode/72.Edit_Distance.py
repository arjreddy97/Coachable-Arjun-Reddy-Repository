class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        edits = [ [j for j in range(len(word1)+1)] for i in range(len(word2)+1)] 
        
        self.initBaseCase(edits)
        
        for i in range(1,len(word2)+1):
            
            for j in range(1,len(word1)+1):
                
                
                if (word2[i-1] == word1[j-1]):
                    
                    edits[i][j] = edits[i-1][j-1]
                    
                else:
                    edits[i][j] = 1 + min(edits[i][j-1], edits[i-1][j-1],edits[i-1][j])
                    
        return edits[-1][-1]
        
        
        
        
    def initBaseCase(self,edits):
        
        for i in range(1,len(edits)):
            edits[i][0] = i
        
        

        
