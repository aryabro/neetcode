class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:      
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0] * 26
        count_s2_window = [0] * 26

        # create first window and update both arrays above at once
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2_window[ord(s2[i]) - ord('a')] += 1
        
        # check if first window is equal
        if count_s1 == count_s2_window:
            return True

        # start sliding window now
        for i in range(len(s1), len(s2)):
            # increment count of value after increasing in right
            count_s2_window[ord(s2[i]) - ord('a')] += 1

            # decrement count of value removed from left
            count_s2_window[ord(s2[i-len(s1)]) - ord('a')] -= 1
            
            if count_s1 == count_s2_window:
                return True
        
        return False