import abc
class Solution:

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
            #find the delimiter #
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end

        return result


