class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Each row is sorted in ascending order.
        The first value of each row is greater than the last value
        of the previous row.

        matrix = [[1, 3, 5], [6, 8, 9], [13, 17, 20], [23, 24, 78]]
        |  1  |  3  |  5  |
        |  6  |  8  |  9  |
        |  13 |  17 |  20 |
        |  23 |  24 |  78 |
        4 x 3 matrix (r x c)

        Because of this structure, we can search in two steps:

        1. Binary search over the rows to find the only row where
           target could possibly exist.
        2. Once that row is found, binary search inside that row.
        
        Time Complexity: O(log r + log c)
        Space Complexity: O(1)
        """
        n_rows, n_cols = len(matrix), len(matrix[0])

        # 1. Binary search to find the candidate row.
        top_row, bot_row = 0, n_rows - 1

        while top_row <= bot_row:
            mid_row = (bot_row + top_row) // 2

            # Target is larger than the biggest value in this row,
            # so it must be in a lower row.
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            
            # Target is smaller than the smallest value in this row,
            # so it must be in an upper row.            
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            else:
                break

        # If the row search crossed over, no row can contain target.
        if top_row > bot_row:
            return False
        
        # mid_row has been calculated during the final iteration to be the 
        # row that contains target, but we still recalculate it
        mid_row = (bot_row + top_row) // 2

        # Step 2: Binary search inside the selected row.
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
