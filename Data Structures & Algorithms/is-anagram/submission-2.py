class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approaches from worst to best:
        1. Sort both strings and compare: O(n log n + m log m) time
        2. Dictionary / hash map. Count occurrences of characters.

        Pitfalls:
        1. Check length in the beginning as uneven is straight up false.
        2. Clarify whether comparison is case-sensitive.
        """
        if len(s) != len(t):
            return False
        
        occ_s = {}
        occ_t = {}
        
        # EASIER way using .get for dict in python. Skips below two for loops.
        # dictionary.get(keyname, value) 
        # Here value is used if keyname does not exist in dict
        for i in range(len(s)):
            occ_s[s[i]] = 1 + occ_s.get(s[i], 0)
            occ_t[t[i]] = 1 + occ_t.get(t[i], 0)

        # prepare occurrences of s str
        # for char in s:
        #     if char not in occ_s:
        #         occ_s[char] = 1
        #     else:
        #         occ_s[char] += 1
        
        # # prepare occurrences of t str
        # for char in t:
        #     if char not in occ_t:
        #         occ_t[char] = 1
        #     else:
        #         occ_t[char] += 1
        
        # compare the occurrences dictionaries
        return occ_s == occ_t
        