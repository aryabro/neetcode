class Solution:
    def isHappy(self, digit: int) -> bool:
        
        seen = set()
        
        while digit not in seen:
            seen.add(digit)

            ans = 0
            # for d in str(digit):
            #     ans += int(d) * int(d)
            while digit:
                d = digit % 10
                d = d ** 2
                ans += d
                digit = digit // 10

            if ans == 1:
                return True

            digit = ans

        return False