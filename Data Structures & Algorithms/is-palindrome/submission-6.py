class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l<r:
            while l<r and self.alpha_check(s[l]) == False: # or s[l].isalnum()
                l += 1
            while l<r and self.alpha_check(s[r]) == False: # or s[r].isalnum()
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alpha_check(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')):
            return True
        else:
            return False