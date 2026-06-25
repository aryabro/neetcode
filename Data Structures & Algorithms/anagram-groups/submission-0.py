class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Sort all the strings in the array. Now anagrams will have same string. Then iterate through array, take the string as key, and add same strings to
        the answer_dictionary where the values with same keys are added to same list. O(m*n.logn) where m is number of total strings, n is 
        longest string and n.logn comes from sort time.
        Space complexity is m*n.

        2. Hash Table. Same approach as 242 valid_anagram. Store frequencies in dict (the key would be freq which would be stored as tuple)
        """
        from collections import defaultdict
        # This creates a dictionary where every new key automatically starts with an empty list.
        # res = defaultdict(list)
        res = {}

        for s in strs:
            count = [0] * 26
            
            # this adjusts count list with freq of c in s
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())
                