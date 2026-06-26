class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Pattern: Hash Set duplicate detection. r//3,c//3 for square detection.

        Possible approaches:
        1. Brute force: Check every row, every column, and every 3x3 box separately.
        2. Single pass with hash sets:
           While scanning the board once, store each seen number in:
           - its row set
           - its column set
           - its 3x3 square set
           If the number already exists in any of those sets, Sudoku is invalid.
        Square idea:
            squares[(r // 3, c // 3)] stores all numbers already seen
            in the 3x3 box containing cell (r, c).

        Use defaultdict(set): So rows[r], cols[c], or squares[key] can directly use .add().

        Time: O(9 * 9), which is O(1) because board size is fixed.
        Space: O(9 * 9), which is O(1) because at most 81 cells are stored.
        """

        # set of numbers already seen in that row/column/square
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Empty cells are ignored
                if val == ".":
                    continue

                # Convert the current cell position into one of the 9 square keys.
                square_key = (r // 3, c // 3)

                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in squares[square_key]
                ):
                    return False

                # Unique value. Add it as value to all the dicts as item of set
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)

        return True