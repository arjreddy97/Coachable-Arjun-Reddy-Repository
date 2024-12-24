class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = [[False for col in range(len(grid[row]))] for row in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if visited[row][col] or grid[row][col] == 0:
                    continue
                size = self.bfs(row,col,grid,visited)
                max_area = max(max_area,size)
        return max_area

    def bfs(self,i,j,grid,visited):

        queue = [(i,j)]
        size = 0
        while len(queue):
            i,j = queue.pop(0)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    continue
            if visited[i][j] or grid[i][j] == 0:
                continue
            visited[i][j] = True
            size += 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dir_ in directions:
                new_i = dir_[0] + i
                new_j = dir_[1] + j
                
                queue.append((new_i,new_j))
        return size
