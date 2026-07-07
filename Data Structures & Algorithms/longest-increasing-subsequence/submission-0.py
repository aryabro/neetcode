class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Pattern: 1D Dynamic Programming.

        Problem:
        Given an integer array nums, return the length of the longest strictly
        increasing subsequence.

        Key idea:
        LIS[i] = length of the longest increasing subsequence starting at index i.

        Since LIS[i] depends on elements to the right of i, we traverse from
        right to left. For each index i, we try to extend nums[i] with every
        later index j where nums[j] is greater than nums[i].

        Recurrence:
            If nums[i] < nums[j], then:
                LIS[i] = max(LIS[i], 1 + LIS[j])

        Time: O(n^2), because for each index i, we scan all indices j after it.
        Space: O(n), because we store one LIS value per index.
        """
        # Each number alone is an increasing subsequence of length 1.
        LIS = [1] * len(nums)

        # traverse right to left because LIS[i] depends on values after i.
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)