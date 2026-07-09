from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Pattern: Greedy.

        Problem:
        Given a string s, split it into as many parts as possible so that
        each character appears in at most one part.
        Return a list containing the size of each partition.

        Key idea:
        For every character, first record the last index where it appears.

        Then scan the string from left to right and build the current partition.
        The partition must extend at least until the farthest last occurrence
        of any character seen so far.

        When the current index reaches that farthest end, we know:
        - every character in this partition ends inside this partition
        - no character from this partition appears later
        - so we can safely cut here

        Example:
        s = "ababcbacadefegdehijhklij"

        First partition:
        - 'a' last appears at index 8
        - 'b' last appears at index 5
        - 'c' last appears at index 7
        So the first partition must end at index 8: "ababcbaca"

        Time: O(n), because we scan the string twice.
        Space: O(1), because there are only 26 lowercase English letters.
        """

        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        