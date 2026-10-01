class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 52 AZ
        # 67 BO
        # letter_map = {i: chr((ord("A") + i)) for i in range(26)}
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            remaining = columnNumber % 26
            columnNumber //= 26

            res.append(chr(ord("A")+remaining))
        res.reverse()
        return "".join(res)
            
