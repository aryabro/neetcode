class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Problem:
        Given an m x n grid, count how many unique paths exist from the
        top-left cell to the bottom-right cell.
        You can only move:
        - down
        - right

        Possible approaches:
        1. Brute force DFS:
           Explore every possible path by trying down and right.
           Declined because the same cells are recomputed many times.

        2. DFS + Memoization:
           Store the answer for each cell after computing it once.
           This avoids repeated work.

        3. Bottom-up 2D DP:
           Build a table from the destination backward or from the start forward.

        Pattern: Dynamic Programming on a Grid. DFS + Memoization.

        I look at the start. How do I calculate the answer? Oh I know, It is just the
        number of ways to get to start from the below cell and the right cell. Ok but how
        do I calculate those values? This goes on continuing until I reach the end destination
        base case which states, return 1 as I am destination, this is the only correct way. 

        Key idea:
        From each cell, the total number of paths is:
            paths going down + paths going right
        We use memo[r][c] to store the number of paths from cell (r, c)
        to the destination so we do not recompute the same state.

        Time: O(m * n), because each cell is solved once.
        Space: O(m * n), because memo stores one value per cell.
        """
        memo = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] =  dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)