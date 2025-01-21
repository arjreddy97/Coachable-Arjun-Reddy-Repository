import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
        frequencyTable = getFreqTable(nums)
        frequencyScores = getTuples(frequencyTable)
        
        heapq.heapify(frequencyScores)
        counter = k
        
        kFreqElements = []
        while counter != 0 and len(frequencyScores):
            
            currentElement = heapq.heappop(frequencyScores)
            currentFreq,currentWord = currentElement
            kFreqElements.append(currentWord)
            counter -= 1
        
        return kFreqElements
        
    
def getTuples(freqTable):
    tuples = []
    for word in freqTable:
        tuples.append((-freqTable[word],word))
    return tuples
    
        
def getFreqTable(words):
    table = {}
    for word in words:
        if word not in table:
            table[word] = 0
        table[word] += 1
    return table
