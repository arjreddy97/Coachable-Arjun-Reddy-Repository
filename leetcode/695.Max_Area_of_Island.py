from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                key = str(row)+":"+str(col)
                if key in visited or grid[row][col] == 0:
                    continue
                size = self.bfs(row,col,grid,visited)
                max_area = max(max_area,size)
        return max_area

    def bfs(self,i,j,grid,visited):

        queue = deque([(i,j)])
        size = 0
        while len(queue):
            i,j = queue.popleft()
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    continue
            key = str(row)+":"+str(col)
            if key in visited or grid[i][j] == 0:
                continue
            visited.add(key)
            size += 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dir_ in directions:
                new_i = dir_[0] + i
                new_j = dir_[1] + j
                
                queue.append((new_i,new_j))
        return size
