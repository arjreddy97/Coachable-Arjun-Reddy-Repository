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
        if row > 0 and grid[row-1][col] == 1:
            print("hello")
            counts -= 1

        if row < len(grid)-1 and grid[row+1][col] == 1:
            counts -=1
        if col > 0 and grid[row][col-1] == 1:
            counts -=1
        if col < len(grid[0])-1 and grid[row][col+1]:
            counts -=1
        return counts
        
