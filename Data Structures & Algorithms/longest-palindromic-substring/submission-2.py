class Solution:
    def longestPalindrome(self, s: str) -> str:
        pali_ind = 0
        pali_len = 0
        for i in range(len(s)):
            #for even palindrome
            l, r = i, i + 1
            while (l >= 0) and (r<len(s)) and s[l] == s[r]:
                if (r - l + 1) > pali_len:
                    pali_ind = l
                    pali_len = r - l + 1
                l -= 1
                r += 1
            
            # for odd palindrome
            l, r = i, i
            while (l >= 0) and (r<len(s)) and s[l] == s[r]:
                if (r - l + 1) > pali_len:
                    pali_ind = l
                    pali_len = r - l + 1
                l -= 1
                r += 1
        return s[pali_ind: pali_ind + pali_len]





