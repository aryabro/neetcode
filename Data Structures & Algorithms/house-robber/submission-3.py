class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Pattern: Dynamic Programming (Solved with Tabular bottom up approach)

        Problem:
        Given a list nums where nums[i] represents the money in the ith house,
        return the maximum amount of money you can rob
        You cannot rob two adjacent houses.

        Key idea:
        At every house, we have two choices:
        1. Skip the current house:
           Then the best amount stays the same as the previous house.
           This is dp[i - 1].

        2. Rob the current house:
           Then we cannot rob the previous house, so we add the current house
           to the best amount from two houses back.
           This is dp[i - 2] + nums[i].

        Recurrence:
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        Base cases:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

        Time: O(n), because we visit each house once.
        Space: O(n), because we store the best answer for every index.
        """
        if len(nums) == 1:
            return nums[0]

        # create dp table of max possible robbed amount from i house
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # fill table from left to right
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], (dp[i-2]+nums[i]))
        
        return dp[len(nums) - 1]