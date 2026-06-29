class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_substring = 0
        while r < len(s):
            if s[r] not in s[l:r]:
                longest_substring = max(longest_substring, r + 1 - l)
            else:
                while l<r and s[r] in s[l:r]:
                    l += 1
            r += 1
        return longest_substring