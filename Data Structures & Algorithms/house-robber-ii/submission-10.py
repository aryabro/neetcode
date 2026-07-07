class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Pattern: Tabular Dynamic Programming.

        Problem:
        This is House Robber II.
        Given a list nums where nums[i] represents the money in the ith house,
        return the maximum amount of money you can rob.
        The houses are arranged in a circle.
        This means the first and last house are adjacent, so we cannot rob both.

        Key idea:
        Convert the circular problem into two normal House Robber I problems.

        Since we cannot rob both the first and last house, we have two choices:
        1. Exclude the first house:
           Rob from nums[1:] to nums[n - 1].
        2. Exclude the last house:
           Rob from nums[0] to nums[n - 2].
        Then take the maximum of both cases.

        Time: O(n), because we run House Robber I twice.
        Space: O(n), because each helper call builds a DP table.
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),
                   self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        """
        same as house robber I
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i -2] + nums[i])

        return dp[-1]