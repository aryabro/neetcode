class Solution:
    def isHappy(self, digit: int) -> bool:
        """
        Pattern: Hash Set / Cycle Detection.

        Repeatedly replace the number with the sum of the squares
        of its digits.

        If we reach 1, the number is happy.
        If we encounter a number we've already seen, we've entered
        a cycle that does not contain 1.

        Time: O(log n) per transformation.
        Space: O(k), where k is the number of unique states visited.
        """

        seen = set()

        while digit not in seen:
            seen.add(digit)

            ans = 0
            temp = digit

            # Extract each digit mathematically.
            while temp:
                d = temp % 10
                ans += d * d
                temp //= 10

            if ans == 1:
                return True

            digit = ans

        return False