import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        counter = k
        minElements = []
        for row in range(len(matrix)):
            nextValInRow = float("inf") if len(matrix[row]) <= 1 else matrix[row][1]
            element = (matrix[row][0],nextValInRow,row,0)
            minElements.append(element)
        
        heapq.heapify(minElements)
        
        kSmallest = None
        while counter != 0 and len(minElements):
            
            
            element = heapq.heappop(minElements)
            value,nextValInRow,array,idx = element
            
            kSmallest = value
            
            counter -=1
            if idx == len(matrix[array])-1:
                continue
            
            kSmallest = value
            
            newIdx = idx + 1
            nextValInRow = float("inf") if newIdx + 1 >= len(matrix[array]) else matrix[array][newIdx+1]
            newElement = (matrix[array][newIdx],nextValInRow,array,newIdx)
            
            heapq.heappush(minElements,newElement)
            
        #if kSmallest == None:
                
            #return matrix[0][0]
        
        
        return kSmallest
            
