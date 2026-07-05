class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        res = []
        path = set()

        def dfs_backtrack(r, c, i):
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

            # recursion starts
            if (dfs_backtrack(r + 1, c, i + 1) or
                dfs_backtrack(r - 1, c, i + 1) or
                dfs_backtrack(r, c + 1, i + 1) or
                dfs_backtrack(r, c - 1, i + 1)
            ): return True

            # clean set(path) as we are backtracking
            path.remove((r, c))

        # for each letter on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs_backtrack(r, c, 0): return True
        
        return False