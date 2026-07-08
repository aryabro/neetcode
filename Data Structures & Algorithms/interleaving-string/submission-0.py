class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Pattern: 2D Dynamic Programming with memoized DFS.

        Problem:
        Given strings s1, s2, and s3, return True if s3 can be formed by
        interleaving s1 and s2 while preserving the character order of both strings.

        Key idea:
        Use two pointers:
        - i points to the current character in s1
        - j points to the current character in s2

        helper(i, j) returns whether:
            s3[i + j:] can be formed using s1[i:] and s2[j:].

        At each state, we have up to two choices:
        1. If s1[i] matches s3[k], use s1[i].
        2. If s2[j] matches s3[k], use s2[j].

        If either choice eventually works, this state is True.

        Time: O(n1 * n2)
              There are n1 * n2 unique states.
        Space: O(n1 * n2)
               Used by memo and recursion stack.
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False

        memo = {} # (i, j)

        def dp(i, j):
            # Since every character used from s1 or s2 becomes one 
            # character in s3, the current index in s3 is always:
            k = i + j

            # base case
            if k == n3:
                return True
            if (i, j) in memo:
                return memo[i,j]

            # Choice 1:
            # Take the next character from s1 if it matches s3[k].
            take_s1 = (
                i < n1
                and s1[i] == s3[k]
                and dp(i + 1, j)
            )

            # Choice 2:
            # Take the next character from s2 if it matches s3[k].
            take_s2 = (
                j < n2
                and s2[j] == s3[k]
                and dp(i, j + 1)
            )

            # This state is valid if either choice can build the rest of s3.
            memo[(i, j)] = take_s1 or take_s2
            return memo[(i, j)]

        return dp(0, 0)
