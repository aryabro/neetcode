from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Brute force by window size.

        Idea:
        Start with the smallest possible window size: len(t).
        For each window size, check every substring of s with that length.
        The first valid substring we find is guaranteed to be the minimum window,
        because we are checking smaller window sizes first.

        Time: O(n^2 * k), roughly
              where n = len(s), k = number of unique chars in t.
        Space: O(k)
        """

        if len(t) > len(s):
            return ""

        t_count = Counter(t)

        # Start from smallest possible window size
        for window_size in range(len(t), len(s) + 1):

            # Try every window of this size
            for l in range(0, len(s) - window_size + 1):
                r = l + window_size
                window = s[l:r]

                window_count = Counter(window)

                # Check if this window contains all required chars from t
                valid = True
                for char in t_count:
                    if window_count[char] < t_count[char]:
                        valid = False
                        break

                if valid:
                    return window

        return ""