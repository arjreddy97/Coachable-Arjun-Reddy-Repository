import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        counter = k
        
        heap = [(matrix[i][0], i, 0) for i in range(min(k, len(matrix)))]
        
        kSmallest = None
        while counter != 0 and len(heap):
            
            
            element = heapq.heappop(heap)
            value,nextValInRow,array,idx = element
            
            kSmallest = value
            
            counter -=1
            if idx == len(matrix[array])-1:
                continue
            
            kSmallest = value
            
            newIdx = idx + 1
            nextValInRow = float("inf") if newIdx + 1 >= len(matrix[array]) else matrix[array][newIdx+1]
            newElement = (matrix[array][newIdx],nextValInRow,array,newIdx)
            
            heapq.heappush(heap,newElement)
            
        #if kSmallest == None:
                
            #return matrix[0][0]
        
        
        return kSmallest
            
