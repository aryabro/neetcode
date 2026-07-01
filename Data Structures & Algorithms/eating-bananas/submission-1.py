class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Pattern: Binary Search on Answer instead of iteration.
        Problem:
        Koko can eat k bananas per hour from one pile at a time.
        Find the minimum integer speed k such that she can finish all piles within h hours.

        Key idea:
        Instead of trying every speed from 1 to max(piles), binary search the speed.

        For a chosen speed k:
        - Each pile p takes ceil(p / k) hours.
        - If total hours > h, k is too slow, so search higher speeds.
        - If total hours <= h, k works, but maybe there is a smaller valid k.

        Time: O(n log m)
        - n = number of piles
        - m = max(piles)
        Space: O(1)
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            # try with middle eating speed
            k = (l + r) // 2

            # Calculate how many hours Koko needs at speed k
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            # If it takes too long, speed k is too slow.
            # Move left pointer right to try faster speeds.
            if hours > h:
                l = k + 1

            # If Koko can finish within h hours, k is valid.
            # Save it and try to find an even smaller valid speed.
            else:
                res = k
                r = k - 1

        return res