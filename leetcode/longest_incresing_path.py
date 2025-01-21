class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return longestIncreasingMatrixPath(matrix)
        
        
        
        
def longestIncreasingMatrixPath(matrix):
    cache = [[None for col in row] for row in matrix]
    longestPath = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if cache[row][col] != None:
                continue
            currentPath = getLongestIncreasing(row,col,matrix,cache,float("-inf"))
            if currentPath > longestPath:
                longestPath = currentPath
				
    return longestPath
				

def getLongestIncreasing(row,col,matrix,cache,previousNum):
    if row <0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0
    if matrix[row][col] <= previousNum:
        return 0
    if cache[row][col] != None:
        return cache[row][col]
	
	
    currentNum = matrix[row][col]
	
    cache[row][col] = 1 + max(getLongestIncreasing(row+1,col,matrix,cache,currentNum),
							  getLongestIncreasing(row-1,col,matrix,cache,currentNum),
							  getLongestIncreasing(row,col+1,matrix,cache,currentNum),
							  getLongestIncreasing(row,col-1,matrix,cache,currentNum))
	
	
    return cache[row][col]
	
        
