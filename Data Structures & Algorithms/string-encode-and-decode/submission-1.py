import abc
class Solution:
    """
    Length + delimiter approach:
    For each string, store its length, then a delimiter, then the actual string.
    E.g. ["abc", "de"] = "3#abc2#de".
    During decode, first read the length before "#", then use that length to know exactly
    how many characters belong to the current string.
    This works even if the string itself contains "#".

    Time complexity:
    Encode: O(n), where n is the total number of characters across all strings.
    Decode: O(n), where n is the length of the encoded string.

    Space complexity:
    Encode: O(n), because we build one encoded string.
    Decode: O(n), because we build the decoded list of strings.
    """
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):

            # j starts at i and moves until it finds the delimiter "#". so j = "#"
            # everything before "#" is the length of the next string
            j = i
            while s[j] != "#":
                j += 1
            # Now write the length in int. Using slice as length could be >1 digit
            length = int(s[i:j])

            # slice value prep
            start = j + 1
            end = start + length
            # add string to result list
            result.append(s[start:end])

            i = end

        return result


