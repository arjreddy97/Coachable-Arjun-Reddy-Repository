class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        start_row = 0
        start_col = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[0]) -1

        while (start_row <= end_row and start_col <= end_col):

            for col in range(start_col,end_col+1):
                res.append(matrix[start_row][col])
            
            for row in range(start_row+1,end_row+1):
                res.append(matrix[row][end_col])
            
            if start_row == end_row:
                break
            
            for col in reversed(range(start_col,end_col)):
                res.append(matrix[end_row][col])
            
            if start_col == end_col:
                break
            
            for row in reversed(range(start_row+1,end_row)):
                res.append(matrix[row][start_col])

            start_row += 1
            start_col += 1
            end_row -=1
            end_col -=1

        return res

        


    """

    keep track of the start row
    start col
    end row and end col



    """
