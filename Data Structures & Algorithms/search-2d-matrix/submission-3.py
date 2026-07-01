class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        matrix = [[1, 3, 5], [6, 8, 9], [13, 17, 20], [23, 24, 78]]
        |  1  |  3  |  5  |
        |  6  |  8  |  9  |
        |  13 |  17 |  20 |
        |  23 |  24 |  78 |
        4 x 3 matrix (r x c)

        We start by first deciding which row to choose with binary search,
        then find the target with binary search on columns.
        """
        n_rows, n_cols = len(matrix), len(matrix[0])
        top_row, bot_row = 0, n_rows - 1

        while top_row <= bot_row:
            mid_row = (bot_row + top_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break
        
        if top_row > bot_row:
            return False
        
        # mid has been calculated during the final iteration to be the 
        # row that contains target, but we still recalculate it
        mid_row = (bot_row + top_row) // 2
        l, r = 0, n_cols - 1
        while l <= r:
            mid_col = (l + r) // 2
            if target > matrix[mid_row][mid_col]:
                l = mid_col + 1
            elif target < matrix[mid_row][mid_col]:
                r = mid_col - 1
            else:
                return True
        
        return False
