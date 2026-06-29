class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            # Closing bracket must match the latest opening bracket.
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Store opening bracket
                stack.append(c)

        # Valid only if no unmatched opening brackets remain.
        return not stack