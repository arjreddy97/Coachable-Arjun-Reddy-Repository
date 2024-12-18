class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> 
List[str]:
        trie = self.initTree(words)
        visited = [[False for col in row] for row in board]
        allWords = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(i,j,board,trie,visited,allWords)
        return allWords
    
    def search(self,row,col,board,trie,visited,allWords):
        if ("*" in trie):
            if len(trie.keys()) == 0:
                return
            else:
                allWords.add(trie["*"])
                del trie["*"]
        

        if (row < 0 or row >= len(board) or col < 0 or col >= 
len(board[0])):
            return
        
        if (visited[row][col]):
            return 
        char = board[row][col]
        
        if (char not in trie):
            return
        
        
        if (len(trie[char]) == 0):
            del trie[char]
            return
        
        visited[row][col] = True
        
        xDir = [-1,1,0,0]
        yDir = [0,0,-1,1]
        
        for i in range(4):
            nextRow = row + xDir[i]
            nextCol = col + yDir[i]
            self.search(nextRow,nextCol,board,trie[char],visited,allWords)
            
        visited[row][col] = False
        
        
        
        
    def initTree(self,words):
        trie = {}
        for word in words:
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current["*"] = word
        return trie
    
