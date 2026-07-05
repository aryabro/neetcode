class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Pattern: DFS Backtracking.

        Problem:
        Given a 2D board of characters and a word, return True if the word
        exists in the board. The word must be formed by moving horizontally or vertically to adjacent
        cells. The same cell cannot be used more than once in one path.

        Key idea:
        Try starting DFS from every cell.
        At each cell:
        - Check if the current board letter matches word[i]
        - Mark the cell as visited
        - Explore all 4 directions for the next character
        - Unmark the cell when backtracking

        Example:
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "ABCCED"

        Time: O(m * n * 4^L), where:
              m = number of rows,
              n = number of columns,
              L = length of word.
              From each cell, DFS can branch in up to 4 directions.

        Space: O(L), because the path set and recursion stack can grow up to
               the length of the word.
        """
        ROWS = len(board)
        COLS = len(board[0])
        res = []
        path = set() # stores currently used cells

        def dfs_backtrack(r, c, i):
            # if i reaches the end, every char has been matched
            if i == len(word):
                return True
            
            if (r < 0 or
                r >= ROWS or
                c < 0 or
                c >= COLS or
                (r, c) in path or
                board[r][c] != word[i]
            ): return False

            # letter on board exists in word
            path.add((r, c))

            # recursion starts. try every neighbouring cell
            if (dfs_backtrack(r + 1, c, i + 1) or
                dfs_backtrack(r - 1, c, i + 1) or
                dfs_backtrack(r, c + 1, i + 1) or
                dfs_backtrack(r, c - 1, i + 1)
            ): return True

            # clean set(path) as we are backtracking
            path.remove((r, c))

            return False

        # for each letter on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs_backtrack(r, c, 0): return True
        
        return False