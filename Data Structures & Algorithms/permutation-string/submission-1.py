class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:      
        """
        Pattern: Sliding Window + Frequency Count.

        Problem:
        Return True if any permutation of s1 exists as a substring in s2.

        Possible approaches:
        1. Brute force:
           Generate all permutations of s1 and check if any permutation exists in s2.
           O(n!)

        2. Fixed Sliding Window + Frequency Count:
        A permutation has the same character counts, just in a different order.
        So instead of generating all permutations, we keep a fixed-size window
        of length len(s1) in s2 and compare its character frequency with s1.

        Time: O(n), where n = len(s2).
              Each window comparison is O(26), which is constant.
        Space: O(1), because both count arrays are fixed size 26.
        """        
        if len(s1) > len(s2):
            return False
        
        # freq count, size = 26 as only lowercase letters in input
        count_s1 = [0] * 26 
        count_s2_window = [0] * 26

        # build count for first window
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2_window[ord(s2[i]) - ord('a')] += 1
        
        if count_s1 == count_s2_window:
            return True

        # slide fixed window across s2
        for i in range(len(s1), len(s2)):
            # add new char entering window from right
            count_s2_window[ord(s2[i]) - ord('a')] += 1

            # remove old char leaving window from left
            count_s2_window[ord(s2[i-len(s1)]) - ord('a')] -= 1
            
            if count_s1 == count_s2_window:
                return True
        
        return False