class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}':'{', ']' : '['}

        for c in s:
            if c in pairs:
                if len(stack) != 0 and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
