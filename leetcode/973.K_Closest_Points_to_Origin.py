import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = self.distance(points)
        heap = []
        for point in distances:
            dist,x,y = point
            heapq.heappush(heap,[-dist,-x,-y])
            if len(heap) > k:
                heapq.heappop(heap)
        return [[-point[1],-point[2]] for point in heap]
        
        

    def distance(self,points,origin = [0,0]):
        output = []
        for point in points:
            sum_ = (point[0]-origin[0])**2 + (point[1]-origin[1]) ** 2
            res = math.sqrt(sum_)
            output.append([res,point[0],point[1]])
        return output
