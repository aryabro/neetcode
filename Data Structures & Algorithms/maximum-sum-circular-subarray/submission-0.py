class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Pattern: Kadane's Algorithm + Circular Array.

        Problem:
        Given a circular integer array nums, return the maximum possible
        subarray sum.

        Key idea:
        The best subarray can be one of two types:

        1. Non-circular max subarray:
           This is the normal maximum subarray problem.
           Use Kadane's algorithm to find the max subarray sum.
        2. Circular max subarray:
           If the best subarray wraps around, that means we are taking
           some prefix + some suffix.
           
           Another way to think about this:
           Instead of directly finding prefix + suffix, remove the minimum
           subarray from the middle.
           max_circular_sum = total_sum - min_subarray_sum

        Edge case:
        If all numbers are negative, total_sum - min_subarray_sum becomes 0,
        because the minimum subarray is the entire array.
        But we are not allowed to choose an empty subarray.
        So in that case, return the normal max subarray sum.

        Time: O(n), because we scan nums once.
        Space: O(1), because we only store running sums.
        """
        total = nums[0]

        curr_max = nums[0]
        max_sum = nums[0]

        # This helps us calculate max_circular_subarray_sum
        curr_min = nums[0]
        min_sum = nums[0]

        for n in nums[1:]:
            # Maximum subarray sum using normal Kadane's algorithm
            curr_max = max(n, curr_max + n)
            max_sum = max(max_sum, curr_max)

            # Minimum subarray sum using Kadane's algorithm
            curr_min = min(n, curr_min + n)
            min_sum = min(min_sum, curr_min)

            total += n

        # If all numbers are negative, circular case would incorrectly give 0
        if max_sum < 0:
            return max_sum

        # Case 1: best subarray does not wrap around
        non_circular_sum = max_sum

        # Case 2: best subarray wraps around
        # Remove the minimum subarray from the middle
        circular_sum = total - min_sum

        # Return the better of normal and circular cases
        return max(non_circular_sum, circular_sum)