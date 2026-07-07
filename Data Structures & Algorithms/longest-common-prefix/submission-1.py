class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Pattern: Vertical Scanning of list elements

        Problem:
        Given a list of strings, return the longest common prefix shared by all strings.

        Key idea:
        Use the first string as the reference.
        Compare each character of the first string with the character at the same
        index in every other word.
        If:
            - some word ends before this index, or
            - some word has a different character at this index
        then the common prefix ends right before this index.

        Time: O(n * m), where n = no. of strings, m = len(first string)
              In the worst case, we compare every character of the first string
              against every other string.

        Space: O(1), ignoring the returned prefix.
        """
        if not strs:
            return ""

        # Use the first string as the reference prefix candidate.
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Compare the current character with the same index in every other word.
            for word in strs[1:]:
                # Stop if:
                # 1. The current word is shorter than the reference string, or
                # 2. The character at index i does not match.
                if i == len(word) or word[i] != char:
                    return strs[0][:i] # the char at i is not included here

        # if we finished checking entire string, then first string is longest common prefix
        return strs[0]
    