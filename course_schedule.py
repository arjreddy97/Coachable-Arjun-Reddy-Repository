class Solution:
   def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       directedadj = self.buildAdj(numCourses,prerequisites )
       inDegrees = [0]* numCourses
       for i,v in directedadj.items():
           for x in v:
               inDegrees[x] += 1


       q = deque()
       count = 0
       for j in range(numCourses):
           if inDegrees[j] < 1:
               q.append(j)
       while q:
           v = q.popleft()
           count += 1
           for i in directedadj[v]:
               inDegrees[i] -= 1
               if inDegrees[i] == 0:
                   q.append(i)
       if count != numCourses:
           return False
       return True
          


   def buildAdj(self,n, p):
       directedadj = defaultdict(list)
      
       for v1,v2 in p:
           directedadj[v2].append(v1)


       return directedadj
