from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words_list = copy(wordList)
        words = set(words_list)
        return self.breadthFirstSearch(beginWord,endWord,words,set())
        
        
        
        
        
    def breadthFirstSearch(self,beginWord,endWord,words,seen):
        queue = Deque([(beginWord,1)])
        while (len(queue) > 0):
            
            currWord,level = queue.popleft()
            
            if (currWord == endWord):
                return level
            
            seen.add(currWord)
        
            nextWords = self.getNextWords(currWord,words,seen)
            for word in nextWords:
                queue.append((word, level + 1))
                             
                             
        return 0
            
            
    def getNextWords(self,word,words,seen):
        nextWords = []
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for letter in alpha:
                newWord = word[:i] + letter + word[i+1:]
                if (newWord not in words or newWord in seen):
                    continue
                    
                nextWords.append(newWord)
                words.remove(newWord)
            
        return nextWords
            
