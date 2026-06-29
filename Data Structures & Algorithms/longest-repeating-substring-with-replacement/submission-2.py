class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Pattern: Sliding Window.
        Possible approaches:
        1. Brute force:
           Check every substring and count how many replacements are needed.
           O(n^2)

        2. Sliding Window:
           Keep a window s[l:r+1] and track character frequencies inside it.
           For a window to be valid:
               window_length - most_frequent_char_count <= k

           Why?
           We keep the most frequent character unchanged and replace all other
           characters. If replacements needed is more than k, shrink from left.

        Time: O(26n) = O(n), because max(count.values()) checks at most 26 letters.
        Space: O(26) = O(1), because there are only uppercase English letters.
        """
        res = 0
        count = {}

        l = 0

        for r in range(len(s)):
            # Add the new right-side character count into the current window
            count[s[r]] = 1 + count.get(s[r], 0)

            # Current window size is r - l + 1.
            # max(count.values()) is the count of the most frequent char.
            # Everything else would need to be replaced.
            while (r - l + 1) - max(count.values()) > k:
                # Window is invalid, so remove the left-side character
                count[s[l]] -= 1

                # Shrink the window from the left
                l += 1

            # After fixing the window, update the best valid window length
            res = max(res, r - l + 1)

        return res