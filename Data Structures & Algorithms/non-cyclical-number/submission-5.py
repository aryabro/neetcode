class Solution:
    def isHappy(self, digit: int) -> bool:
        # track seen nos
        seen = set()
        ans = 0
        nums = [int(i) for i in str(digit)]
        while ans not in seen:
            seen.add(ans)
            ans = 0
            for digit in nums:
                ans += digit*digit
            if ans == 1:
                return True
            nums = [int(i) for i in str(ans)]

        return False

        """
        19
        82
        66
        72
        53
        34
        25
        29
        85
        89
        145
        42
        20
        4
        16
        37
        58
        89

        """