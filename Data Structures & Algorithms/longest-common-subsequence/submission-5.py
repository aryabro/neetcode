class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Pattern: 2D Dynamic Programming with memoized DFS.

        Problem:
        Given two strings, return the length of their longest common subsequence.
        A subsequence does not need to be contiguous, but the order of characters
        must stay the same.

        Grid intuition:
        Think of this problem as a 2D grid.
            - Rows represent indices in text1
            - Columns represent indices in text2
            - Each cell (i, j) represents the LCS length between:
                  text1[i:] and text2[j:]

        Example:
            text1 = "abc"
            text2 = "ac"

            Grid states:

                    j
                    0     1    2
                    a     c   end
              i   ----------------
              0 a |(0,0)(0,1)
              1 b |(1,0)(1,1)
              2 c |(2,0)(2,1)
              3 end

        Goal:
        Start from the top-left state (0, 0), which compares text1[0] and text2[0].
        Eventually move toward the bottom-right boundary, where one string is exhausted.

        Movement rules:
        1. If text1[i] == text2[j]:
           The characters match, so include this character in the answer.
           Then move diagonally down-right:
                dfs(i + 1, j + 1)

        2. If text1[i] != text2[j]:
           The characters do not match, so try both options.
           Remember that this is a split in the path, so only 
           choose the best of the two options:
           - move down:  dfs(i + 1, j), skipping text1[i]
           - move right: dfs(i, j + 1), skipping text2[j]

        Base case:
        If i reaches the end of text1 or j reaches the end of text2,
        there are no more characters to match, so return 0.

        Memoization:
        Save each (i, j) result so we do not recompute the same grid cell.

        Time: O(n * m), where n = len(text1), m = len(text2)
              Each grid cell is solved once.

        Space: O(n * m)
               For the memo dictionary.
               Recursion stack can also go up to O(n + m).
        """
        n1, n2 = len(text1), len(text2)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # If either string is exhausted, no more common subsequence is possible.
            if i == n1 or j == n2:
                memo[(i,j)] = 0
                return memo[(i,j)]

            # if both chars match, movie diagonally in 2D grid
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                memo[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
            
            return memo[(i,j)]

        return dfs(0,0)