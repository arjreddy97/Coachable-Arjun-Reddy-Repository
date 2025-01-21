class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    count += 4 + self.incrementCounts(grid,row,col)
        return count
    
    def incrementCounts(self,grid,row,col):
        counts = 0
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] == 1:
                counts -= 1
        return counts
        
