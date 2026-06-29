class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Pattern: Sliding Window with Set.
        Possible approaches:
        1. Brute force:
           Check every substring and verify if it has duplicate characters.
           O(n^3): O(n^2) substrings and O(n) duplicate check.
        2. Sliding Window:
        For each r, create the best valid substring that ends at r,
        then compare its length with the global max.
            - r expands the window one character at a time.
            - l shrinks the window only when the window becomes invalid.
            - seen stores the characters currently inside the window.

        Time: O(n), because each character is added and removed at most once.
        Space: O(k), where k is the number of unique characters in the current window.
        """
        l = 0
        max_substring = 0
        seen = set()
        # r always moves forward, so for loop
        for r in range(len(s)):
            # Creating best substring for current r
            # If s[r] already exists in the window, shrink from the left
            # until the old duplicate is removed.
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # now window valid, add s[r]
            seen.add(s[r])
            # s[l:r+1] is the best valid substring ending at r.
            max_substring = max(max_substring, r - l + 1)

        return max_substring