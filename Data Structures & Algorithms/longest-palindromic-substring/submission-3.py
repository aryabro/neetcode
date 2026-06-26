class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Pattern: Two Pointer. Expand Around Center.

        Possible approaches:
        1. Brute force:
           Check every substring and test if it is a palindrome.
           Declined because it is O(n^3) if each substring check takes O(n).
        2. DP: Store whether s[l:r] is a palindrome. 
        Works in O(n^2), but uses O(n^2) space.
        3. Expand Around Center:
           Every palindrome expands from a center.
           - Odd palindrome has one center: "racecar"
           - Even palindrome has two centers: "abba"

            For each index, expand outward while left and right chars match.
            Keep track of the best starting index and best length.

        Time: O(n^2), because each center can expand up to O(n).
        Space: O(1), because we only store indices and lengths.
        """

        pali_ind = 0
        pali_len = 0

        for i in range(len(s)):
            # Even-length palindrome: abba
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > pali_len:
                    pali_ind = l
                    pali_len = r - l + 1

                l -= 1
                r += 1

            # Odd-length palindrome: racecar
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > pali_len:
                    pali_ind = l
                    pali_len = r - l + 1

                l -= 1
                r += 1

        return s[pali_ind:pali_ind + pali_len]