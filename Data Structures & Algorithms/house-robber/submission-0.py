class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabular dp
        # create table of all possible values

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # dp[2] = max(dp[1], dp[0] + nums[2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], (dp[i-2]+nums[i]))
        
        return dp[len(nums) - 1]