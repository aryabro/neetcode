class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # can add open parentheses only if open_p left
        # can add closed parentheses only if closed_p < open_p
        # a string is valid only once all closed and open parentheses == n

        res = []
        stack = []
        def backtrack(open_p: int, closed_p: int):
            if open_p == closed_p == n:
                res.append("".join(stack))
                return
            
            if open_p < n:
                stack.append("(")
                backtrack(open_p + 1, closed_p)
                stack.pop()
            
            if closed_p < open_p:
                stack.append(")")
                backtrack(open_p, closed_p + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res