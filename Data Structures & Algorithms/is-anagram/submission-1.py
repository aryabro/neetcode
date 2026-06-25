class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approaches from worst to best:
        1. Sort and then check if equal. n+m time complex
        2. Dictionary. Check occurences of values
        3. Fixed list. if char in s, add 1; if char in t, minus 1. In the end if all 0, you are good.

        Pitfalls:
        1. Check length in the beginning as uneven is straight up false.
        2. Check case sensitivity
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

        # prepare occurences of s str
        # for char in s:
        #     if char not in occ_s:
        #         occ_s[char] = 1
        #     else:
        #         occ_s[char] += 1
        
        # # prepare occurences of t str
        # for char in t:
        #     if char not in occ_t:
        #         occ_t[char] = 1
        #     else:
        #         occ_t[char] += 1
        
        # compare the occurences dictionaries
        for char_s in occ_s:
            if char_s not in occ_t:
                return False

            if occ_s[char_s] != occ_t[char_s]:
                return False
        
        return True