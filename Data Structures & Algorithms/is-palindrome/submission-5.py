# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l<r:
#             while l<r and self.alpha_check(s[l]) == False:
#                 l += 1
#             while l<r and self.alpha_check(s[r]) == False:
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     def alpha_check(self, c):
#         if (ord('A') <= ord(c) <= ord('Z') or
#             ord('a') <= ord(c) <= ord('z') or
#             ord('0') <= ord(c) <= ord('9')):
#             return True
#         else:
#             return False
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        left = 0
        right = len(s) - 1
        while left < right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True