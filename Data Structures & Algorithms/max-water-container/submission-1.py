class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Pattern: Two Pointers.
        Possible approaches:
        1. Brute force:
           Try every pair of lines and calculate the container area.
           O(n^2).
        2. Two pointers:
           Start with the widest possible container using the leftmost and rightmost lines.
           The area depends on:
           Since width always decreases as pointers move inward, we only move the
           pointer with the smaller height.
        Time: O(n)
        Space: O(1)
        """

        l, r = 0, len(heights) - 1
        max_amt = 0

        while l < r:
            # Current container area: width = r - l * height = shorter wall
            cur_amt = min(heights[l], heights[r]) * (r - l)
            max_amt = max(max_amt, cur_amt)

            # Move the shorter wall inward.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_amt