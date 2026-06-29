class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Pattern: Sliding Window with Hash Maps.
        Problem:
        Find the shortest substring in s that contains all characters from t,
        including duplicate characters.

        Possible approaches:
        1. Brute force by window size:
           Start with window size len(t), check every window, then increase size.
           The first valid window is the answer, but this is still too slow: O(n^3).

        2. Optimized Sliding Window:
           Expand the right pointer to include characters.
           Once the window is valid, shrink from the left to make it as small as possible.

        Time: O(n), where n = len(s).
        Each character is added once by r and removed once by l.
        Space: O(k), where k is the number of unique characters in s and t.
        """

        if t == "":
            return ""

        count_t = {}
        window = {}

        # Build frequency map for t.
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # have = how many required chars are currently satisfied
        # need = how many unique chars must be satisfied
        have = 0
        need = len(count_t)

        # Store best answer as indices [left, right].
        # res_len tracks the length of the best valid window found so far.
        res = [-1, -1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]

            # Add current right character into the window count.
            window[c] = 1 + window.get(c, 0)

            # If this character is required and we now have exactly enough of it,
            # then one more unique character requirement is satisfied.
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # When have == need, the current window contains all chars from t.
            # Now try shrinking from the left to find the smallest valid window.
            while have == need:
                # Update result if this valid window is smaller.
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Remove the leftmost character from the window.
                window[s[l]] -= 1

                # If removing s[l] makes this required character insufficient,
                # then the window is no longer valid.
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                # Move left pointer forward to shrink the window.
                l += 1

        l, r = res

        # If res_len was never updated, no valid window exists.
        return s[l: r + 1] if res_len != float("inf") else ""