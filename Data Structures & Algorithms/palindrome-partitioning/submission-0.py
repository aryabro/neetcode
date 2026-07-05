class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Pattern: Backtracking / DFS.

        Problem:
        Return all possible palindrome partitions of string s.

        Key idea:
        At each index i of s, try every possible substring starting at i.
        If the substring s[i:j+1] is a palindrome, choose it and recursively
        partition the remaining string starting at j + 1.

        Example:
        s = "aab"

        Choices:
        - Choose "a" (as its a palindrome), then solve remaining "ab", choose "a" again
            (as its a palindrome), then solve remaining "b" as well.
        - Choose "aa", then solve remaining "b"

        Time: O(n * 2^n)
              There are roughly 2^n ways to split the string, and each palindrome
              check can take O(n).

        Space: O(n)
               Recursion depth and current path can both grow up to n.
               Output space is not included.
        """
        res = [] # stores final answer
        sol = [] # stores current partition being built

        def dfs_backtrack(i):
            # if i reaches the end, we found one valid partition collection
            if i >= len(s):
                res.append(sol.copy())
                return

            # Try every possible substring starting at index i
            for j in range(i,len(s)):

                # Check if s[i:j+1] is a palindrome
                if self.isPali(s, i, j):

                    # perform dfs on subsequent chars to check if they are palindrome
                    sol.append(s[i : j+1])
                    dfs_backtrack(j + 1)
                    sol.pop()
            
        dfs_backtrack(0)
        return res
            
    def isPali(self, string, l, r):
        # two pointers trick to check if palindrome
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True