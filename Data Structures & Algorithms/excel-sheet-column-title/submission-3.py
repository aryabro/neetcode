class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # letter_map = {i: chr((ord("A") + i)) for i in range(26)}
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            columnNumber //= 26

            res.append(chr(ord("A")+remainder))
        res.reverse()
        return "".join(res)
            
