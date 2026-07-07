class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        memo = {(n1,n2): 0}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n1 or j == n2:
                memo[(i,j)] = 0
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
                return memo[(i,j)]

        return dfs(0,0)