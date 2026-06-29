class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Count of characters in window
        char_set = set(s)
        res = 0

        for c in char_set:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res