class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Pattern: Backtracking / DFS using Stack.
        Problem:
        Generate all combinations of well-formed parentheses using n pairs.

        Possible approaches:
        1. Brute force:
           Generate every possible string of length 2n using '(' and ')',
           then check which strings are valid.
           2^(2n) possible strings, and most are invalid.
        2. Backtracking:
           Build the string one character at a time and only make valid choices.
           - Add '(' if we still have open parentheses left to use.
           - Add ')' only if it will not make the string invalid.

        Valid prefix:   "(()"   open_p = 2, closed_p = 1
        Invalid prefix: "())"   open_p = 1, closed_p = 2

        Time: O(C_n * n), where C_n is the nth Catalan number.
              We generate C_n valid strings, each of length 2n.
        Space: O(n), for the recursion depth and current stack.
               Output space is O(C_n * n).
        """
        # can add open parentheses only if open_p left
        # can add closed parentheses only if closed_p < open_p
        # a string is valid only once all closed and open parentheses == n

        res = []
        # stack is used as the current string we are building.
        stack = []
        def backtrack(open_p: int, closed_p: int):
            # base case
            if open_p == closed_p == n:
                # join all chars in stack and append the string to res
                res.append("".join(stack))
                return
            # choice 1: add open parentheses if some left
            if open_p < n:
                stack.append("(")
                backtrack(open_p + 1, closed_p)
                stack.pop()
            # choice 2: add closed parentheses if unmatched open parentheses available
            if closed_p < open_p:
                stack.append(")")
                backtrack(open_p, closed_p + 1)
                stack.pop()

        # start func with 0, 0. It goes on till n, n. 
        backtrack(0, 0)
        return res