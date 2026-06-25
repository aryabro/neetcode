class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        occ_s = {}
        occ_t = {}
        
        # prepare occurances of s str
        for char in s:
            if char not in occ_s:
                occ_s[char] = 1
            else:
                occ_s[char] += 1
        
        # prepare occurances of t str
        for char in t:
            if char not in occ_t:
                occ_t[char] = 1
            else:
                occ_t[char] += 1
        
        # compare the occurances dictionaries
        for char_s in occ_s:
            if char_s not in occ_t:
                return False

            if occ_s[char_s] != occ_t[char_s]:
                return False
        
        return True